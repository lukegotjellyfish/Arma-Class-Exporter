d = {
    "_generalmacro": "Heli_Light_02_base_F",
    "_mainbladecenter": "rotor_center",
    "access": 0,
    "accuracy": 0.5,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 200,
    "aggregatereflectors": [
        [
            "Left",
            "Right"
        ]
    ],
    "agm_fuelcapacity": 1870,
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
    "altfullforce": 4500,
    "altnoforce": 6000,
    "alwaystarget": 0,
    "animated": 1,
    "animationsources": {
        "addcargohook": {
            "animperiod": 1e-07,
            "initphase": 0,
            "iscomponent": 1,
            "source": "user"
        },
        "addcargohook_cover": {
            "animperiod": 1e-07,
            "initphase": 1,
            "iscomponent": 1,
            "source": "user"
        },
        "bench_hide": {
            "animperiod": 1e-06,
            "displayname": "hide benches",
            "initphase": 0,
            "mass": 1,
            "onphasechanged": "{(_this select 0) lockCargo [_x,(_this select 1) isEqualTo 1]}foreach [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,17,18];",
            "source": "user"
        },
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
        "doors": {
            "animperiod": 1,
            "initphase": 0,
            "source": "user"
        },
        "exhaust_hide": {
            "animperiod": 1e-15,
            "displayname": "hide exhaust",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "gatling": {
            "source": "revolving",
            "weapon": "LMG_Minigun_heli"
        },
        "gatling_flash": {
            "source": "ammorandom",
            "weapon": "LMG_Minigun_heli"
        },
        "helicopter_brakes": {
            "animperiod": 0.01,
            "initphase": 1,
            "source": "user"
        },
        "hide_door_hatch": {
            "animperiod": 1e-15,
            "initphase": 1,
            "source": "user"
        },
        "hide_front_armor": {
            "animperiod": 1e-15,
            "displayname": "hide front armor",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "hide_turrets": {
            "animperiod": 1e-15,
            "initphase": 0,
            "source": "user"
        },
        "hide_weapon_holders": {
            "animperiod": 1e-15,
            "displayname": "hide weapon holders",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "hide_winch": {
            "animperiod": 1e-15,
            "displayname": "hide winch",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "hideweapon": {
            "animperiod": 1e-05,
            "initphase": 0,
            "source": "user"
        },
        "hideweapons_dl": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "hit_pylon_1_source": {
            "hitpoint": "HitPylon1",
            "source": "Hit"
        },
        "hit_pylon_2_source": {
            "hitpoint": "HitPylon2",
            "source": "Hit"
        },
        "hit_pylon_3_source": {
            "hitpoint": "HitPylon3",
            "source": "Hit"
        },
        "hit_pylon_4_source": {
            "hitpoint": "HitPylon4",
            "source": "Hit"
        },
        "hit_pylon_5_source": {
            "hitpoint": "HitPylon5",
            "source": "Hit"
        },
        "hit_pylon_6_source": {
            "hitpoint": "HitPylon6",
            "source": "Hit"
        },
        "hitbatteries": {
            "hitpoint": "HitBatteries",
            "raw": 1,
            "source": "hit"
        },
        "hitengine": {
            "hitpoint": "HitEngine",
            "raw": 1,
            "source": "hit"
        },
        "hitengine1": {
            "hitpoint": "HitEngine1",
            "raw": 1,
            "source": "hit"
        },
        "hitengine2": {
            "hitpoint": "HitEngine2",
            "raw": 1,
            "source": "hit"
        },
        "hitfuel": {
            "hitpoint": "HitFuel",
            "raw": 1,
            "source": "hit"
        },
        "hitglass1": {
            "hitpoint": "HitGlass1",
            "raw": 1,
            "source": "hit"
        },
        "hitglass10": {
            "hitpoint": "HitGlass10",
            "raw": 1,
            "source": "hit"
        },
        "hitglass11": {
            "hitpoint": "HitGlass11",
            "raw": 1,
            "source": "hit"
        },
        "hitglass12": {
            "hitpoint": "HitGlass12",
            "raw": 1,
            "source": "hit"
        },
        "hitglass13": {
            "hitpoint": "HitGlass13",
            "raw": 1,
            "source": "hit"
        },
        "hitglass14": {
            "hitpoint": "HitGlass14",
            "raw": 1,
            "source": "hit"
        },
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "raw": 1,
            "source": "hit"
        },
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "raw": 1,
            "source": "hit"
        },
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "raw": 1,
            "source": "hit"
        },
        "hitglass5": {
            "hitpoint": "HitGlass5",
            "raw": 1,
            "source": "hit"
        },
        "hitglass6": {
            "hitpoint": "HitGlass6",
            "raw": 1,
            "source": "hit"
        },
        "hitglass7": {
            "hitpoint": "HitGlass7",
            "raw": 1,
            "source": "hit"
        },
        "hitglass8": {
            "hitpoint": "HitGlass8",
            "raw": 1,
            "source": "hit"
        },
        "hitglass9": {
            "hitpoint": "HitGlass9",
            "raw": 1,
            "source": "hit"
        },
        "hithrotor": {
            "hitpoint": "HitHRotor",
            "raw": 1,
            "source": "hit"
        },
        "hithydraulics": {
            "hitpoint": "HitHydraulics",
            "raw": 1,
            "source": "hit"
        },
        "hittransmission": {
            "hitpoint": "HitTransmission",
            "raw": 1,
            "source": "hit"
        },
        "hitvrotor": {
            "hitpoint": "HitVRotor",
            "raw": 1,
            "source": "hit"
        },
        "hitwinch_source": {
            "hitpoint": "HitWinch",
            "raw": 1,
            "source": "hit"
        },
        "holder_small_hide": {
            "animperiod": 1e-15,
            "initphase": 0,
            "source": "user"
        },
        "hudaction": {
            "animperiod": 1,
            "initphase": 0,
            "source": "user"
        },
        "hudaction_hide": {
            "animperiod": 1,
            "initphase": 0,
            "source": "user"
        },
        "intake_hide": {
            "animperiod": 1e-06,
            "displayname": "hide intake covers",
            "initphase": 0,
            "mass": 1,
            "source": "user"
        },
        "leftdoor": {
            "animperiod": 0.8,
            "initphase": 1,
            "source": "user"
        },
        "missiles_revolving": {
            "source": "revolving",
            "weapon": "missiles_DAGR"
        },
        "muzzle_rot_hmg1": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkt_v1"
        },
        "muzzle_rot_hmg2": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkt_v2"
        },
        "muzzle_rot_hmg3": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkt_v3"
        },
        "proxy": {
            "animperiod": 1,
            "initphase": 0,
            "source": "user"
        },
        "reardoors": {
            "animperiod": 1.6,
            "displayname": "",
            "initphase": 0,
            "mass": 1,
            "onphasechanged": "(_this select 0) animateDoor ['RearDoors',_this select 1]",
            "sound": "ServoDoorsSound",
            "soundposition": "pos cargo dir",
            "source": "door"
        },
        "reloadanim": {
            "source": "reload",
            "weapon": "rhs_weap_pkt_v1"
        },
        "reloadanim_2": {
            "source": "reload",
            "weapon": "rhs_weap_pkt_v2"
        },
        "reloadanim_3": {
            "source": "reload",
            "weapon": "rhs_weap_pkt_v3"
        },
        "reloadmagazine": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_pkt_v1"
        },
        "reloadmagazine_2": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_pkt_v2"
        },
        "reloadmagazine_3": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_pkt_v3"
        },
        "revolving": {
            "source": "revolving",
            "weapon": "rhs_weap_pkt_v1"
        },
        "revolving_2": {
            "source": "revolving",
            "weapon": "rhs_weap_pkt_v2"
        },
        "revolving_3": {
            "source": "revolving",
            "weapon": "rhs_weap_pkt_v3"
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
    "armor": 25,
    "armorlights": 0.4,
    "armorstructural": 2,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "HeliAttenuation",
    "attributes": {
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        "rhs_decalnumber": {
            "control": "Edit",
            "defaultvalue": "-1",
            "displayname": "Set side number",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3/data_f/clear_empty.paa']]}foreach cRHSAIRMI8NumberPlaces}else{[_this, [['Number', cRHSAIRMI8NumberPlaces, _this getVariable ['rhs_decalNumber_type','AviaYellow'], _value] ] ] call rhs_fnc_decalsInit}};",
            "property": "rhs_decalNumber",
            "tooltip": "Set side number. 2 numbers are required. Type 0 to hide numbers completly",
            "typename": "Number",
            "validate": "Number"
        },
        "rhs_decalnumber_type": {
            "control": "Combo",
            "defaultvalue": 0,
            "displayname": "Define font type of side number",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHSAIRMI8NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "property": "rhs_decalNumber_type",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "typename": "STRING",
            "values": {
                "aviablue": {
                    "defaultvalue": "AviaBlue",
                    "name": "Aviation Blue",
                    "value": "AviaBlue"
                },
                "aviacdf": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                "aviared": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                "aviawhiteout": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                "aviayellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                "default": {
                    "name": "Default (White)",
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
                "nochange": {
                    "name": "Default",
                    "value": "NoChange"
                }
            }
        },
        "rhs_decaltail": {
            "control": "Combo",
            "defaultvalue": -1,
            "displayname": "Define tail decal",
            "expression": "[_this,[['Label', cRHSAIRMI8TailPlaces, 'Aviation',_value]]] call rhs_fnc_decalsInit",
            "property": "rhs_decalTail",
            "tooltip": "Define tail decalthat will be drawn on vehicle",
            "typename": "Number",
            "values": {
                "default": {
                    "name": "Default",
                    "value": -1
                },
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                "vvs": {
                    "defaultvalue": 3,
                    "name": "VVS Russia",
                    "value": 3
                }
            }
        }
    },
    "audible": 6,
    "author": "Bohemia Interactive",
    "autocenter": 1,
    "availableforsupporttypes": [
        "Drop",
        "Transport"
    ],
    "backrotorforcecoef": 0.9,
    "backrotorspeed": 1,
    "bodyfrictioncoef": 1.25,
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
        "frequency": 3,
        "minspeed": 1,
        "power": 0.2
    },
    "canhidedriver": -1,
    "canusescanners": 1,
    "cargoaction": [
        "RHS_Mi17_Cargo02"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1"
    ],
    "cargodoors": [],
    "cargogetinaction": [
        "GetInHelicopterCargo"
    ],
    "cargogetoutaction": [
        "GetOutHelicopterCargo"
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
                    "attachment": "rhs_ASO2_CMFlare_Chaff_Magazine_x4",
                    "hardpoints": [
                        "RHS_cm_ASO2",
                        "RHS_cm_ASO2_x2",
                        "RHS_cm_ASO2_x4"
                    ],
                    "maxweight": 800,
                    "priority": 1,
                    "uiposition": [
                        0.33,
                        0
                    ]
                },
                "pylon1": {
                    "attachment": "rhs_mag_b8v20a_s8kom",
                    "hardpoints": [
                        "RHS_HP_FAB250",
                        "RHS_HP_FAB500",
                        "RHS_HP_KMGU2",
                        "RHS_HP_B13L1",
                        "RHS_HP_B8V20",
                        "RHS_HP_UB16",
                        "RHS_HP_UB32",
                        "RHS_HP_UPK23"
                    ],
                    "hitpoint": "HitPylon1",
                    "maxweight": 1200,
                    "priority": 1,
                    "uiposition": [
                        0.525,
                        0.48
                    ]
                },
                "pylon2": {
                    "attachment": "rhs_mag_b8v20a_s8kom",
                    "hardpoints": [
                        "RHS_HP_FAB250",
                        "RHS_HP_FAB500",
                        "RHS_HP_KMGU2",
                        "RHS_HP_B13L1",
                        "RHS_HP_B8V20",
                        "RHS_HP_UB16",
                        "RHS_HP_UB32",
                        "RHS_HP_UPK23"
                    ],
                    "hitpoint": "HitPylon2",
                    "maxweight": 1200,
                    "mirroredmissilepos": 1,
                    "priority": 1,
                    "uiposition": [
                        0.14,
                        0.48
                    ]
                },
                "pylon3": {
                    "attachment": "rhs_mag_b8v20a_s8df",
                    "hardpoints": [
                        "RHS_HP_FAB250",
                        "RHS_HP_FAB500",
                        "RHS_HP_B8V20",
                        "RHS_HP_UB16",
                        "RHS_HP_UB32",
                        "RHS_HP_UPK23"
                    ],
                    "hitpoint": "HitPylon3",
                    "maxweight": 1200,
                    "priority": 2,
                    "uiposition": [
                        0.575,
                        0.43
                    ]
                },
                "pylon4": {
                    "attachment": "rhs_mag_b8v20a_s8df",
                    "hardpoints": [
                        "RHS_HP_FAB250",
                        "RHS_HP_FAB500",
                        "RHS_HP_B8V20",
                        "RHS_HP_UB16",
                        "RHS_HP_UB32",
                        "RHS_HP_UPK23"
                    ],
                    "hitpoint": "HitPylon4",
                    "maxweight": 1200,
                    "mirroredmissilepos": 3,
                    "priority": 2,
                    "uiposition": [
                        0.09,
                        0.43
                    ]
                },
                "pylon5": {
                    "attachment": "rhs_mag_b8v20a_s8kom",
                    "hardpoints": [
                        "RHS_HP_FAB250",
                        "RHS_HP_B8V20",
                        "RHS_HP_UB16",
                        "RHS_HP_UB32",
                        "RHS_HP_UPK23"
                    ],
                    "hitpoint": "HitPylon5",
                    "maxweight": 400,
                    "priority": 4,
                    "uiposition": [
                        0.625,
                        0.38
                    ]
                },
                "pylon6": {
                    "attachment": "rhs_mag_b8v20a_s8kom",
                    "hardpoints": [
                        "RHS_HP_FAB250",
                        "RHS_HP_B8V20",
                        "RHS_HP_UB16",
                        "RHS_HP_UB32",
                        "RHS_HP_UPK23"
                    ],
                    "hitpoint": "HitPylon6",
                    "maxweight": 400,
                    "mirroredmissilepos": 5,
                    "priority": 4,
                    "uiposition": [
                        0.04,
                        0.38
                    ]
                }
            },
            "uipicture": "rhsafrf/addons/rhs_a2port_air/data/loadouts/RHS_Mi8_EDEN_CA.paa"
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
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
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
                },
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        }
    },
    "cost": 2000000.0,
    "countermeasureactivationradius": 10000,
    "countsforscoreboard": 1,
    "crew": "rhs_pilot_transport_heli",
    "crewcrashprotection": 0.25,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "cyclicasideforcecoef": 1,
    "cyclicforwardforcecoef": 1,
    "damage": {
        "mat": [
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_body_amt.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_body_amt_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_body_amt_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_det_g.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_det_g_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_det_g_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_glass.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_glass_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_glass_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_glass_in.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_glass_in_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_glass_in_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_inter.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_inter_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_inter_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_air/data/pkm.rvmat",
            "rhsafrf/addons/rhs_a2port_air/data/pkm.rvmat",
            "rhsafrf/addons/rhs_a2port_air/data/pkm_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_body_mtv.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_body_mtv_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_body_mtv_destruct.rvmat",
            "rhsafrf/addons/rhs_a2port_air/Mi17/data/mi8t/mi8t_tv2.rvmat",
            "rhsafrf/addons/rhs_a2port_air/Mi17/data/mi8t/mi8t_tv2_damage.rvmat",
            "rhsafrf/addons/rhs_a2port_air/Mi17/data/mi8t/mi8t_tv2_destruct.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default_destruct.rvmat"
        ],
        "tex": []
    },
    "damageeffect": "AirDestructionEffects",
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.00172,
    "damagetexdelay": 0,
    "dammagefull": [],
    "dammagehalf": [],
    "defaultusermfdvalues": [
        0.15,
        1,
        0.15,
        0.7
    ],
    "destrtype": "DestructWreck",
    "destructioneffects": {},
    "detectskill": 20,
    "displayname": "Mi-8AMTSh",
    "dlc": "RHS_AFRF",
    "driveoncomponent": [
        "wheels"
    ],
    "driveraction": "RHS_Mi8_PilotV2",
    "drivercaneject": 0,
    "drivercansee": "2+4+16",
    "drivercompartments": "Compartment1",
    "driverdoor": "",
    "driverforceoptics": 0,
    "driverinaction": "RHS_Mi8_PilotV2",
    "driverlefthandanimname": "stick_pilot",
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
    "editorpreview": "rhsafrf/addons/rhs_editorPreviews/data/rhs_mi8amtsh_base.paa",
    "editorsubcategory": "rhs_EdSubcat_helicopter",
    "ejectdeadcargo": 0,
    "ejectdeaddriver": 0,
    "emptysound": [
        "",
        0,
        1
    ],
    "enablegps": 1,
    "enablemanualfire": 0,
    "enableradio": 1,
    "enablesweep": 1,
    "enablewatch": 0,
    "engineer": 0,
    "enginemoi": 10,
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
        "bis_randomisation": {
            "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;}"
        },
        "fired": "",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        },
        "rhs_eventhandlers": {
            "init": "_this call rhs_fnc_air_init"
        }
    },
    "exhausts": {
        "exhaust01": {
            "direction": "exhaust1h_dir",
            "effect": "ExhaustEffectHeli",
            "position": "exhaust1h"
        },
        "exhaust02": {
            "direction": "exhaust2h_dir",
            "effect": "ExhaustEffectHeli",
            "position": "exhaust2h"
        }
    },
    "explosionshielding": 4,
    "extcameraparams": [
        -1
    ],
    "extcameraposition": [
        0,
        2,
        -20
    ],
    "faction": "CIV_F",
    "features": "Randomization: No\t\t\t\t\t\t<br />Camo selections: 1 - the whole exterior\t\t\t\t\t\t<br />Script door sources: No\t\t\t\t\t\t<br />Script animations: Doors, HideWeapon, proxy\t\t\t\t\t\t<br />Executed scripts: None \t\t\t\t\t\t<br />Firing from vehicles: No\t\t\t\t\t\t<br />Slingload: Slingloads up to 500 kg\t\t\t\t\t\t<br />Cargo proxy indexes: 1 to 8",
    "featuretype": 0,
    "fireresistance": 10,
    "flarevelocity": 100,
    "forcehidedriver": 0,
    "formationtime": 10,
    "formationx": 50,
    "formationz": 100,
    "fuelcapacity": 1870,
    "fuelconsumptionrate": 0.33,
    "fuelexplosionpower": 1,
    "fxexplo": {
        "access": 1
    },
    "geardowntime": 2,
    "gearminalt": 0.5,
    "gearretracting": 0,
    "gearsupfrictioncoef": 0.5,
    "gearuptime": 3.33,
    "getinaction": "GetInHeli_Transport_01Cargo",
    "getinoutonproxy": 0,
    "getinradius": 1.7,
    "getoutaction": "RHS_HIND_Cargo_Exit",
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
    "gunnercansee": "2+4+8+16",
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
        "Camo1",
        "Camo2",
        "Camo3",
        "Camo4",
        "n1",
        "n2",
        "tail_decals"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsafrf/addons/rhs_a2port_air/mi17/data/mi_171_co.paa",
        "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_det_g_co.paa",
        "a3/data_f/clear_empty.paa",
        "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_decals_ca.paa",
        "a3/data_f/clear_empty.paa",
        "a3/data_f/clear_empty.paa",
        "rhsafrf/addons/rhs_decals/data/labels/aviation/vvs_ca.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hitpoints": {
        "hitavionics": {
            "armor": "0.15*2",
            "explosionshielding": 1,
            "material": 51,
            "name": "avionics_hit",
            "passthrough": 1,
            "visual": "-"
        },
        "hitengine": {
            "armor": 999,
            "convexcomponent": "engine_hit",
            "depends": "0.5 * (HitEngine1 + HitEngine2)",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "engine_hit",
            "passthrough": 1,
            "radius": 0.4,
            "visual": "motor"
        },
        "hitengine1": {
            "armor": "0.7*2",
            "convexcomponent": "engine_1_hit",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "engine_1_hit",
            "passthrough": 1,
            "radius": 0.4,
            "visual": "motor"
        },
        "hitengine2": {
            "armor": "0.7*2",
            "convexcomponent": "engine_2_hit",
            "explosionshielding": 3,
            "material": -1,
            "minimalhit": 0.1,
            "name": "engine_2_hit",
            "passthrough": 1,
            "radius": 0.4,
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
            "armor": "5*2",
            "convexcomponent": "fuel_hit",
            "explosionshielding": 1,
            "material": 51,
            "minimalhit": 0.05,
            "name": "fuel_hit",
            "passthrough": 1,
            "radius": 0.25,
            "visual": "zbytek"
        },
        "hitgear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passthrough": 0
        },
        "hitglass1": {
            "armor": -10,
            "armorcomponent": "glass1",
            "explosionshielding": 1.5,
            "minimalhit": 0.1,
            "name": "glass1",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "glass1"
        },
        "hitglass10": {
            "armor": 0.8,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects10",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects10",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects10",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects10",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects10",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects10",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects10",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects10",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects10",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects10",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "name": "glass10",
            "passthrough": 0,
            "radius": 0.24,
            "visual": "glass10"
        },
        "hitglass11": {
            "armor": 0.8,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects11",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects11",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects11",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects11",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects11",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects11",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects11",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects11",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects11",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects11",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "name": "glass11",
            "passthrough": 0,
            "radius": 0.24,
            "visual": "glass11"
        },
        "hitglass12": {
            "armor": 0.8,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects12",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects12",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects12",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects12",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects12",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects12",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects12",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects12",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects12",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects12",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "name": "glass12",
            "passthrough": 0,
            "radius": 0.24,
            "visual": "glass12"
        },
        "hitglass13": {
            "armor": 0.8,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects13",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects13",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects13",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects13",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects13",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects13",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects13",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects13",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects13",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects13",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "name": "glass13",
            "passthrough": 0,
            "radius": 0.24,
            "visual": "glass13"
        },
        "hitglass14": {
            "armor": 0.8,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects14",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects14",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects14",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects14",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects14",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects14",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects14",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects14",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects14",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects14",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "name": "glass14",
            "passthrough": 0,
            "radius": 0.24,
            "visual": "glass14"
        },
        "hitglass2": {
            "armor": -10,
            "armorcomponent": "glass2",
            "explosionshielding": 1.5,
            "minimalhit": 0.1,
            "name": "glass2",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": -10,
            "armorcomponent": "glass3",
            "explosionshielding": 1.5,
            "minimalhit": 0.1,
            "name": "glass3",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": -10,
            "armorcomponent": "glass4",
            "explosionshielding": 1.5,
            "minimalhit": 0.1,
            "name": "glass4",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "glass4"
        },
        "hitglass5": {
            "armor": -10,
            "armorcomponent": "glass5",
            "explosionshielding": 1.5,
            "minimalhit": 0.1,
            "name": "glass5",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "glass5"
        },
        "hitglass6": {
            "armor": -10,
            "armorcomponent": "glass6",
            "explosionshielding": 1.5,
            "minimalhit": 0.1,
            "name": "glass6",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "glass6"
        },
        "hitglass7": {
            "armor": -10,
            "armorcomponent": "glass7",
            "explosionshielding": 1.5,
            "minimalhit": 0.1,
            "name": "glass7",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "glass7"
        },
        "hitglass8": {
            "armor": -10,
            "armorcomponent": "glass8",
            "explosionshielding": 1.5,
            "minimalhit": 0.1,
            "name": "glass8",
            "passthrough": 0.1,
            "radius": 0.1,
            "visual": "glass8"
        },
        "hitglass9": {
            "armor": 0.8,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects9",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects9",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects9",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects9",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects9",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects9",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects9",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects9",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects9",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects9",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "name": "glass9",
            "passthrough": 0,
            "radius": 0.24,
            "visual": "glass9"
        },
        "hithrotor": {
            "armor": "0.5*2",
            "explosionshielding": 1,
            "material": 51,
            "name": "main_rotor_hit",
            "passthrough": 0.1,
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
            "armor": 999,
            "convexcomponent": "hull_hit",
            "depends": "Total",
            "explosionshielding": 1,
            "material": 51,
            "minimalhit": 0.05,
            "name": "hull_hit",
            "passthrough": 1,
            "radius": 0.01,
            "visual": "zbytek"
        },
        "hithydraulics": {
            "armor": -50,
            "explosionshielding": 0.5,
            "minimalhit": 0.1,
            "name": "hit_hydraulics",
            "passthrough": 0.1,
            "radius": 0.13,
            "visual": "-"
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
            "armor": 1,
            "convexcomponent": "ammo_hit",
            "explosionshielding": 1,
            "material": 51,
            "minimalhit": 0.05,
            "name": "ammo_hit",
            "passthrough": 0.5,
            "radius": 0.15,
            "visual": "munice"
        },
        "hitpitottube": {
            "armor": 0.5,
            "material": -1,
            "name": "pitot tube",
            "passthrough": 0.2
        },
        "hitpylon1": {
            "armor": -30,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "rhs_pylon_flash": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006,
                    "position": "fx_pylon_1",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash"
                },
                "rhs_pylon_shard": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03,
                    "position": "fx_pylon_1",
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard"
                },
                "rhs_pylon_smoke": {
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04,
                    "position": "fx_pylon_1",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke"
                },
                "rhs_pylon_sound": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1,
                    "position": "fx_pylon_1",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound"
                }
            },
            "explosionshielding": 0.1,
            "material": -1,
            "minimalhit": 0.8,
            "name": "hit_pylon_1",
            "passthrough": 0,
            "radius": 0.75,
            "visual": "-"
        },
        "hitpylon2": {
            "armor": -30,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "rhs_pylon_flash": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006,
                    "position": "fx_pylon_2",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash"
                },
                "rhs_pylon_shard": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03,
                    "position": "fx_pylon_2",
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard"
                },
                "rhs_pylon_smoke": {
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04,
                    "position": "fx_pylon_2",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke"
                },
                "rhs_pylon_sound": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1,
                    "position": "fx_pylon_2",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound"
                }
            },
            "explosionshielding": 0.1,
            "material": -1,
            "minimalhit": 0.8,
            "name": "hit_pylon_2",
            "passthrough": 0,
            "radius": 0.75,
            "visual": "-"
        },
        "hitpylon3": {
            "armor": -30,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "rhs_pylon_flash": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006,
                    "position": "fx_pylon_3",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash"
                },
                "rhs_pylon_shard": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03,
                    "position": "fx_pylon_3",
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard"
                },
                "rhs_pylon_smoke": {
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04,
                    "position": "fx_pylon_3",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke"
                },
                "rhs_pylon_sound": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1,
                    "position": "fx_pylon_3",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound"
                }
            },
            "explosionshielding": 0.1,
            "material": -1,
            "minimalhit": 0.8,
            "name": "hit_pylon_3",
            "passthrough": 0,
            "radius": 0.75,
            "visual": "-"
        },
        "hitpylon4": {
            "armor": -30,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "rhs_pylon_flash": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006,
                    "position": "fx_pylon_4",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash"
                },
                "rhs_pylon_shard": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03,
                    "position": "fx_pylon_4",
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard"
                },
                "rhs_pylon_smoke": {
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04,
                    "position": "fx_pylon_4",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke"
                },
                "rhs_pylon_sound": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1,
                    "position": "fx_pylon_4",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound"
                }
            },
            "explosionshielding": 0.1,
            "material": -1,
            "minimalhit": 0.8,
            "name": "hit_pylon_4",
            "passthrough": 0,
            "radius": 0.75,
            "visual": "-"
        },
        "hitpylon5": {
            "armor": -30,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "rhs_pylon_flash": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006,
                    "position": "fx_pylon_5",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash"
                },
                "rhs_pylon_shard": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03,
                    "position": "fx_pylon_5",
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard"
                },
                "rhs_pylon_smoke": {
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04,
                    "position": "fx_pylon_5",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke"
                },
                "rhs_pylon_sound": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1,
                    "position": "fx_pylon_5",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound"
                }
            },
            "explosionshielding": 0.1,
            "material": -1,
            "minimalhit": 0.8,
            "name": "hit_pylon_5",
            "passthrough": 0,
            "radius": 0.75,
            "visual": "-"
        },
        "hitpylon6": {
            "armor": -30,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "rhs_pylon_flash": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006,
                    "position": "fx_pylon_6",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash"
                },
                "rhs_pylon_shard": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03,
                    "position": "fx_pylon_6",
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard"
                },
                "rhs_pylon_smoke": {
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04,
                    "position": "fx_pylon_6",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke"
                },
                "rhs_pylon_sound": {
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1,
                    "position": "fx_pylon_6",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound"
                }
            },
            "explosionshielding": 0.1,
            "material": -1,
            "minimalhit": 0.8,
            "name": "hit_pylon_6",
            "passthrough": 0,
            "radius": 0.75,
            "visual": "-"
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
            "armor": -150,
            "armorcomponent": "Hit_Tail",
            "explosionshielding": 0.2,
            "minimalhit": 0.1,
            "name": "Hit_Tail",
            "passthrough": 0.1,
            "radius": 0.13,
            "visual": "vis_tail"
        },
        "hittransmission": {
            "armor": -80,
            "explosionshielding": 0.5,
            "minimalhit": 0.1,
            "name": "hit_transmission",
            "passthrough": 0.1,
            "radius": 0.13,
            "visual": "-"
        },
        "hitvrotor": {
            "armor": "0.5*2",
            "explosionshielding": 1,
            "material": 51,
            "name": "tail_rotor_hit",
            "passthrough": 0.3,
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
    "icon": "rhsafrf/addons/rhs_a2port_air/data/map_ico/icomap_mi17_ca.paa",
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsAir",
    "incomingmissiledetectionsystem": "8",
    "indirecthitciviliancoefai": -20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "insidedetectcoef": 0.05,
    "insidesoundcoef": 0.0316228,
    "irscanground": 1,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "irtarget": 1,
    "irtargetsize": 0.9,
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
        "A3/Sounds_F/vehicles/air/noises/landing_wheels_large_int1",
        1,
        1,
        100
    ],
    "landingsoundint1": [
        "A3/Sounds_F/vehicles/air/noises/landing_wheels_large_int2",
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
        7.5,
        -2.4
    ],
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_wheeloffset": [
        0,
        0.6
    ],
    "library": {
        "libtextdesc": "The PO-30 Orca is a transport and utility helicopter primarily developed for the Russian Air Force. The helicopter was intended to replace the Mi-8 and can be used for reconnaissance, transporting a full squad with combat gear and special operations. Armed variants of the PO-30 carry a Minigun and DAGR guided rockets."
    },
    "liftforcecoef": 1,
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": "8",
    "magazines": [],
    "mainbladecenter": "main_blade_center",
    "mainbladeradius": 11,
    "mainrotorspeed": 1,
    "mapsize": 25,
    "markerlights": {
        "greenstill": {
            "activelight": 0,
            "ambient": [
                0,
                0.08,
                0
            ],
            "blinking": 0,
            "brightness": 0.01,
            "color": [
                0,
                0.8,
                0
            ],
            "drawlight": 1,
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.25,
            "flaresize": 0.5,
            "intensity": 55,
            "name": "zeleny pozicni",
            "useflare": 1
        },
        "redblinking": {
            "activelight": 0,
            "ambient": [
                0.09,
                0.015,
                0.01
            ],
            "blinking": 1,
            "brightness": 0.01,
            "color": [
                0.9,
                0.15,
                0.1
            ],
            "drawlight": 1,
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.25,
            "flaresize": 0.5,
            "intensity": 55,
            "name": "cerveny pozicni blik",
            "useflare": 1
        },
        "redstill": {
            "activelight": 0,
            "ambient": [
                0.08,
                0,
                0
            ],
            "blinking": 0,
            "brightness": 0.01,
            "color": [
                0.8,
                0,
                0
            ],
            "drawlight": 1,
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.25,
            "flaresize": 0.5,
            "intensity": 55,
            "name": "cerveny pozicni",
            "useflare": 1
        },
        "whiteblicking": {
            "activelight": 0,
            "ambient": [
                0.1,
                0.1,
                0.1
            ],
            "blinking": 1,
            "brightness": 0.01,
            "color": [
                1,
                1,
                1
            ],
            "drawlight": 1,
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.25,
            "flaresize": 0.5,
            "intensity": 55,
            "name": "bily pozicni blik",
            "useflare": 1
        },
        "whitestill": {
            "activelight": 0,
            "ambient": [
                0.1,
                0.1,
                0.1
            ],
            "blinking": 0,
            "brightness": 0.01,
            "color": [
                1,
                1,
                1
            ],
            "drawlight": 1,
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.25,
            "flaresize": 0.5,
            "intensity": 55,
            "name": "bily pozicni",
            "useflare": 1
        }
    },
    "maxbackrotordive": 0,
    "maxdetectrange": 20,
    "maxfordingdepth": 0.55,
    "maxgforce": 2,
    "maximumload": 3500,
    "maxmainrotordive": 0,
    "maxomega": 2000,
    "maxsmokedamage": 0.99,
    "maxspeed": 240,
    "memorypointcm": [
        "flare_launcher1",
        "flare_launcher2"
    ],
    "memorypointcmdir": [
        "flare_launcher1_dir",
        "flare_launcher2_dir"
    ],
    "memorypointdriveroptics": "slingCamera",
    "memorypointgun": [
        "chase01",
        "chase02",
        "chase03",
        "chase04"
    ],
    "memorypointlmissile": "l strela",
    "memorypointlrocket": "l raketa",
    "memorypointpilot": "pilot",
    "memorypointrmissile": "p strela",
    "memorypointrrocket": "p raketa",
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
    "mfact": 0.2,
    "mfd": {},
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
    "model": "rhsafrf/addons/rhs_a2port_air/mi17/Mi_171",
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
    "occludesoundswhenin": 0.316228,
    "outsidesoundfilter": 1,
    "picture": "rhsafrf/addons/rhs_a2port_air/data/ico/rhs_mi8amtsh_pic_ca.paa",
    "pilotcamera": {},
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
    "radartargetsize": 1,
    "radartype": 4,
    "reflectors": {
        "lsvetla": {
            "ambient": [
                1100,
                1000,
                900
            ],
            "attenuation": {
                "constant": 1,
                "linear": 0,
                "quadratic": 15,
                "start": 1
            },
            "color": [
                1100,
                1000,
                900
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "konec L svetla",
            "flaresize": 0.75,
            "hitpoint": "L svetlo",
            "innerangle": 30,
            "intensity": 100,
            "outerangle": 120,
            "position": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "useflare": 1
        },
        "rsvetla": {
            "ambient": [
                1100,
                1000,
                900
            ],
            "attenuation": {
                "constant": 1,
                "linear": 0,
                "quadratic": 15,
                "start": 1
            },
            "color": [
                1100,
                1000,
                900
            ],
            "conefadecoef": 5,
            "daylight": 0,
            "direction": "konec P svetla",
            "flaresize": 0.75,
            "hitpoint": "P svetlo",
            "innerangle": 30,
            "intensity": 100,
            "outerangle": 120,
            "position": "P svetlo",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {
        "leftmirror": {
            "bboxes": [
                "PIP_0_TL",
                "PIP_0_TR",
                "PIP_0_BL",
                "PIP_0_BR"
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
                "PIP_1_TL",
                "PIP_1_TR",
                "PIP_1_BL",
                "PIP_1_BR"
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
        "['Number',cRHSAIRMI8NumberPlaces,'AviaYellow']"
    ],
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
        "A3/Sounds_F/vehicles/air/noises/heli_damage_rotor_int_1",
        1,
        1
    ],
    "rotordamageout": [
        "A3/Sounds_F/vehicles/air/noises/heli_damage_rotor_ext_1",
        2.51189,
        1,
        300
    ],
    "rotorlibhelicopterproperties": {
        "autohovercorrection": [
            4.3,
            -1.7,
            0
        ],
        "defaultcollective": 0.665,
        "horizontalwingsanglecollmax": 0,
        "horizontalwingsanglecollmin": 0,
        "maxhorizontalstabilizerleftstress": 10000,
        "maxhorizontalstabilizerrightstress": 10000,
        "maxmainrotorstress": 320000,
        "maxtailrotorstress": 60000,
        "maxtorque": 201754,
        "maxverticalstabilizerstress": 10000,
        "retreatbladestallwarningspeed": 92.583,
        "rtdconfig": "rhsafrf/addons/rhs_c_a2port_air/Mi17/RTD_MI8.xml",
        "stressdamagepersec": 0.00333333
    },
    "scope": 0,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionclan": "clan",
    "selectiondamage": "trup",
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
    "side": 3,
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
        1.77828,
        1,
        200
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
        1.77828,
        1,
        200
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
        300
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
        200
    ],
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "slingloadmaxcargomass": 2700,
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
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_bush_int_1",
        1,
        1,
        100
    ],
    "soundbushcollision2": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_bush_int_2",
        1,
        1,
        100
    ],
    "soundbushcollision3": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_bush_int_3",
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
        "A3/Sounds_F/vehicles/crashes/helis/Heli_crash_default_int_1",
        10,
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
        "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_ext_stop_v2",
        0.794328,
        1,
        600
    ],
    "soundengineoffint": [
        "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_int_stop_v2",
        0.398107,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_ext_start_v2",
        0.794328,
        1,
        600
    ],
    "soundengineonint": [
        "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_int_start_v2",
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
    "soundgeneralcollision1": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_default_int_1",
        1,
        1,
        100
    ],
    "soundgeneralcollision2": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_default_int_2",
        1,
        1,
        100
    ],
    "soundgeneralcollision3": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_default_int_3",
        1,
        1,
        100
    ],
    "soundgetin": [
        "A3/Sounds_F/vehicles/air/Heli_Light_02/open",
        0.562341,
        1
    ],
    "soundgetout": [
        "A3/Sounds_F/vehicles/air/Heli_Light_02/close",
        1,
        1,
        50
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
        "emptySound",
        0
    ],
    "soundlandinggear": [
        "",
        1,
        1
    ],
    "soundlocked": [
        "/A3/Sounds_F/weapons/Rockets/opfor_lock_1",
        1,
        1
    ],
    "soundrecovered": {},
    "sounds": {
        "damagealarmext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_alarm_opfor",
                0.223872,
                1,
                20
            ],
            "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
        },
        "damagealarmint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_alarm_opfor",
                0.316228,
                1
            ],
            "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
        },
        "engineext": {
            "frequency": "rotorSpeed",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_ext_engine_v2",
                1.77828,
                1,
                700
            ],
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        "engineint": {
            "frequency": "rotorSpeed",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_int_engine_v2",
                1,
                1
            ],
            "volume": "2 * (1-camPos)*(rotorSpeed factor[0.4,1])"
        },
        "gstress": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/vehicle_stress2e",
                0.398107,
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
            "frequency": "rotorSpeed * (1-rotorThrust/5)",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_ext_rotor_normal",
                1.41254,
                1,
                1500
            ],
            "volume": "camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
        },
        "rotorint": {
            "frequency": "rotorSpeed * (1-rotorThrust/5)",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_int_rotor_normal",
                0.707946,
                1
            ],
            "volume": "(1-camPos) * (rotorSpeed factor[0.3, 1]) * (1 + rotorThrust)"
        },
        "rotorlowalarmext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_alarm_rotor_low",
                0.223872,
                1,
                20
            ],
            "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        "rotorlowalarmint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_alarm_rotor_low",
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
                "A3/Sounds_F/vehicles/air/Heli_Light_02/rotor_swist",
                1,
                1,
                400
            ],
            "volume": "(camPos*(rotorThrust factor [0.6, 1]))"
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
                1.25893,
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
                1.25893,
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
        "transmissiondamageext_phase1": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_ext_1",
                1,
                1,
                150
            ],
            "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "transmissiondamageext_phase2": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_ext_2",
                1,
                1,
                150
            ],
            "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "transmissiondamageint_phase1": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_int_1",
                1,
                1,
                150
            ],
            "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "transmissiondamageint_phase2": {
            "frequency": "0.66 + rotorSpeed / 3",
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_int_2",
                1,
                1,
                150
            ],
            "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        "windint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/wind_closed",
                0.446684,
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
                    "A3/Sounds_F/vehicles/air/noises/heli_alarm_opfor",
                    0.223872,
                    1,
                    20
                ],
                "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
            },
            "damagealarmint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_alarm_opfor",
                    0.316228,
                    1
                ],
                "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
            },
            "engineext": {
                "frequency": "rotorSpeed",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_ext_engine_v2",
                    1.77828,
                    1,
                    700
                ],
                "volume": "camPos*((rotorSpeed-0.72)*4)"
            },
            "engineint": {
                "frequency": "rotorSpeed",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_int_engine_v2",
                    1,
                    1
                ],
                "volume": "2 * (1-camPos)*(rotorSpeed factor[0.4,1])"
            },
            "gstress": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/noises/vehicle_stress2e",
                    0.398107,
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
                "frequency": "rotorSpeed * (1-rotorThrust/5)",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_ext_rotor_normal",
                    1.41254,
                    1,
                    1500
                ],
                "volume": "camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
            },
            "rotorint": {
                "frequency": "rotorSpeed * (1-rotorThrust/5)",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_02/Heli_Light_02_int_rotor_normal",
                    0.707946,
                    1
                ],
                "volume": "(1-camPos) * (rotorSpeed factor[0.3, 1]) * (1 + rotorThrust)"
            },
            "rotorlowalarmext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_alarm_rotor_low",
                    0.223872,
                    1,
                    20
                ],
                "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            "rotorlowalarmint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_alarm_rotor_low",
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
                    "A3/Sounds_F/vehicles/air/Heli_Light_02/rotor_swist",
                    1,
                    1,
                    400
                ],
                "volume": "(camPos*(rotorThrust factor [0.6, 1]))"
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
            "transmissiondamageext_phase1": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_ext_1",
                    1,
                    1,
                    150
                ],
                "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "transmissiondamageext_phase2": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_ext_2",
                    1,
                    1,
                    150
                ],
                "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "transmissiondamageint_phase1": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_int_1",
                    1,
                    1,
                    150
                ],
                "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "transmissiondamageint_phase2": {
                "frequency": "0.66 + rotorSpeed / 3",
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/heli_damage_transmission_int_2",
                    1,
                    1,
                    150
                ],
                "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            "windint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/wind_closed",
                    0.446684,
                    1,
                    50
                ],
                "volume": "(1-camPos)*(speed factor[5, 60])*(speed factor[5, 60])"
            }
        },
        "waternoise_ext": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/noises/air_driving_in_water",
                0.707946,
                1,
                300
            ],
            "volume": "(speed factor[0, 5]) * water * camPos + (speed factor[-0.1, -5]) * water * camPos"
        },
        "waternoise_int": {
            "frequency": "1",
            "sound": [
                "A3/Sounds_F/vehicles/noises/soft_driving_in_water_int",
                0.562341,
                1,
                100
            ],
            "volume": "(speed factor[0, 5]) * water * (1-camPos) + (speed factor[-0.1, -5]) * water * (1-camPos)"
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
        "A3/Sounds_F/vehicles/crashes/planes/plane_crash_water_1",
        1.41254,
        1,
        500
    ],
    "soundwatercollision2": [
        "A3/Sounds_F/vehicles/crashes/planes/plane_crash_water_2",
        1.41254,
        1,
        500
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
    "supplyradius": 2.5,
    "tailbladecenter": "tail_blade_center",
    "tailbladeradius": 0.5,
    "tailbladevertical": 1,
    "taildamage": [
        "tailDamageInt",
        "tailDamageOut"
    ],
    "taildamageint": [
        "A3/Sounds_F/vehicles/air/noises/heli_damage_tail",
        1,
        1
    ],
    "taildamageout": [
        "A3/Sounds_F/vehicles/air/noises/heli_damage_tail",
        1,
        1,
        300
    ],
    "tbody": 150,
    "textplural": "helicopters",
    "textsingular": "helicopter",
    "texturelist": [],
    "texturesources": {
        "camo": {
            "author": "Red Hammer Studios",
            "displayname": "CDF",
            "factions": [
                "rhs_faction_vvs_c",
                "rhs_faction_vvs"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_air/Mi17/data/camo/mi_171_cdf_co.paa",
                "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_det_g_cdf_co.paa"
            ]
        },
        "camo1": {
            "author": "Red Hammer Studios",
            "displayname": "Chedaki",
            "factions": [
                "rhs_faction_vvs_c",
                "rhs_faction_vvs"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_air/mi17/data/camo/mi_171_chdkz_co.paa",
                "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8_det_g_cdf_co.paa"
            ]
        },
        "camo2": {
            "author": "Red Hammer Studios",
            "displayname": "Camo #1",
            "factions": [
                "rhs_faction_vvs_c",
                "rhs_faction_vvs"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_air/mi17/data/camo/mi_171_camo1_co.paa",
                "rhsafrf/addons/rhs_a2port_air/mi17/data/camo/mi8_det_g_camo1_co.paa"
            ]
        },
        "camo3": {
            "author": "Red Hammer Studios",
            "displayname": "Camo #2",
            "factions": [
                "rhs_faction_vvs_c",
                "rhs_faction_vvs"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_air/mi17/data/camo/mi_171_camo2_co.paa",
                "rhsafrf/addons/rhs_a2port_air/mi17/data/camo/mi8_det_g_camo2_co.paa"
            ]
        },
        "camo4": {
            "author": "Red Hammer Studios",
            "displayname": "Camo #3",
            "factions": [
                "rhs_faction_vvs_c",
                "rhs_faction_vvs"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_air/mi17/data/camo/mi_171_camo_mvd_co.paa",
                "rhsafrf/addons/rhs_a2port_air/mi17/data/camo/mi8_det_g_camo_mvd_co.paa"
            ]
        },
        "camo5": {
            "author": "Red Hammer Studios",
            "displayname": "Camo #4",
            "factions": [
                "rhs_faction_vvs_c",
                "rhs_faction_vvs"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_air/mi17/data/camo/mi_171_camo3_co.paa",
                "rhsafrf/addons/rhs_a2port_air/mi17/data/camo/mi8_det_g_camo3_co.paa"
            ]
        },
        "civilian": {
            "author": "Red Hammer Studios",
            "displayname": "Civilian",
            "factions": [
                "rhs_faction_vvs_c",
                "rhs_faction_vvs"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_air/Mi17/data/camo/mi_171_civil_co.paa",
                "rhsafrf/addons/rhs_a2port_air/mi17/data/mi8civil_det_g_co.paa"
            ]
        },
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Grey",
            "factions": [
                "rhs_faction_vvs_c",
                "rhs_faction_vvs"
            ],
            "textures": [
                "rhsafrf/addons/rhs_a2port_air/mi17/data/mi_171_co.paa",
                "rhsafrf/addons/rhs_a2port_air/mi17/data/mi171_det_co.paa"
            ]
        }
    },
    "tf_isolatedamount_api": 0.4,
    "threat": [
        0.8,
        0.8,
        0.6
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportbackpacks": {
        "_xx_rhs_d6_parachute_backpack": {
            "backpack": "rhs_d6_Parachute_backpack",
            "count": 8
        }
    },
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 8,
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
        "_xx_rhs_30rnd_545x39_7n10_ak": {
            "count": 30,
            "magazine": "rhs_30Rnd_545x39_7N10_AK"
        },
        "_xx_rhs_mag_nspn_red": {
            "count": 10,
            "magazine": "rhs_mag_nspn_red"
        },
        "_xx_rhs_mag_rdg2_white": {
            "count": 4,
            "magazine": "rhs_mag_rdg2_white"
        },
        "_xx_rhs_mag_rgd5": {
            "count": 10,
            "magazine": "rhs_mag_rgd5"
        }
    },
    "transportmaxbackpacks": 10,
    "transportmaxmagazines": 48,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 13,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {},
    "turrets": {
        "backturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "Turret_2",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "Gun_2",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "Turret_2",
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 1,
            "commanding": -3,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
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
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "Gun_2",
            "gunbeg": "muzzle_2",
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
            "gunend": "chamber_2",
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
            "gunneraction": "RHS_Mi17v2_Gunner",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "RHS_Mi17v2_Gunner",
            "gunnerlefthandanimname": "OtocHlaven2",
            "gunnerleftleganimname": "gunner2_leg_left",
            "gunnername": "Rear gunner",
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
            "gunnerrighthandanimname": "OtocHlaven2",
            "gunnerrightleganimname": "gunner2_leg_right",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": -41,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 180,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "magazines": [
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100"
            ],
            "maxcamelev": 90,
            "maxelev": 15,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 235,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "muzzle_2",
            "memorypointgunneroptics": "gunnerview2",
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
            "minelev": -51,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 130,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 3,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "zasleh2",
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
            "stabilizedinaxes": 0,
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
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25
            },
            "weapons": [
                "rhs_weap_pkt_v2"
            ]
        },
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
                        },
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent",
                            "resource": "RscCustomInfoSlingLoad"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
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
            "gunneraction": "RHS_Mi8_Pilot",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_HIND_Cargo_Exit",
            "gunnerinaction": "RHS_Mi8_Pilot",
            "gunnerlefthandanimname": "stick_copilot",
            "gunnerleftleganimname": "pedalL",
            "gunnername": "Co-pilot",
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
            "gunnerrighthandanimname": "stick_copilot",
            "gunnerrightleganimname": "pedalR",
            "gunnertype": "",
            "gunnerusespilotview": 0,
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
            "lodopticsin": 1200,
            "lodopticsout": 1200,
            "lodturnedin": 1200,
            "lodturnedout": 1200,
            "magazines": [],
            "maxcamelev": 90,
            "maxelev": 30,
            "maxhorizontalrotspeed": 3,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 170,
            "maxverticalrotspeed": 3,
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetincargo": "pos copilot",
            "memorypointsgetincargodir": "pos copilot dir",
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
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 4,
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
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
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
                        "hardlimitend": 2.5,
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
                    "intensity": 10,
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
                        "hardlimitend": 2.5,
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
                    "intensity": 10,
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
                        "hardlimitend": 2.5,
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
                    "intensity": 10,
                    "outerangle": 165,
                    "position": "cargo_light_3",
                    "selection": "cargo_light_3",
                    "size": 1,
                    "useflare": 0
                }
            },
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
        "frontturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "Turret_3",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "Gun_3",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.4,
            "body": "Turret_3",
            "caneject": 0,
            "canhidegunner": -1,
            "canusescanners": 1,
            "castgunnershadow": 1,
            "commanding": -2,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
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
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "Gun_3",
            "gunbeg": "muzzle_3",
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
            "gunend": "chamber_3",
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
            "gunneraction": "RHS_Mi8_Gunner",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "RHS_Mi8_Gunner",
            "gunnerlefthandanimname": "OtocHlaven3",
            "gunnerleftleganimname": "gunner3_leg_left",
            "gunnername": "Crew chief",
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
            "gunnerrighthandanimname": "OtocHlaven3",
            "gunnerrightleganimname": "gunner3_leg_right",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": -10,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": -70,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "magazines": [
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100"
            ],
            "maxcamelev": 90,
            "maxelev": 25,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": -30,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "muzzle_3",
            "memorypointgunneroptics": "gunnerview3",
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
            "minelev": -45,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -121,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 1,
            "proxytype": "CPGunner",
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
            "stabilizedinaxes": 0,
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
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25
            },
            "weapons": [
                "rhs_weap_pkt_v3"
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
            "commanding": -2,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
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
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "mainGun",
            "gunbeg": "muzzle_1",
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
            "gunend": "chamber_1",
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
            "gunneraction": "RHS_Mi8_Gunner",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "RHS_Mi8_Gunner",
            "gunnerlefthandanimname": "OtocHlaven",
            "gunnerleftleganimname": "gunner1_leg_left",
            "gunnername": "Crew Chief",
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
            "gunnerrighthandanimname": "OtocHlaven",
            "gunnerrightleganimname": "gunner1_legs",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": -60,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 90,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "magazines": [
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100"
            ],
            "maxcamelev": 90,
            "maxelev": 25,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 130,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "muzzle_1",
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
            "minelev": -80,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 30,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
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
            "stabilizedinaxes": 0,
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
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25
            },
            "weapons": [
                "rhs_weap_pkt_v1"
            ]
        },
        "sideturret": {
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
            "commanding": -4,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
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
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "mainGun",
            "gunbeg": "muzzle_1",
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
            "gunend": "chamber_1",
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
            "gunneraction": "RHS_Mi8_Gunner",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "RHS_Mi8_Gunner",
            "gunnerlefthandanimname": "OtocHlaven",
            "gunnerleftleganimname": "gunner1_leg_left",
            "gunnername": "Door gunner",
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
            "gunnerrighthandanimname": "OtocHlaven",
            "gunnerrightleganimname": "gunner1_legs",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": -60,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 90,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodopticsin": 1000,
            "lodopticsout": 1000,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "magazines": [
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100",
                "rhs_mag_762x54mm_100"
            ],
            "maxcamelev": 90,
            "maxelev": 25,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 130,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "muzzle_1",
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
            "minelev": -80,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 30,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
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
            "stabilizedinaxes": 0,
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
                "initfov": 0.7,
                "maxanglex": 30,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.25
            },
            "weapons": [
                "rhs_weap_pkt_v1"
            ]
        }
    },
    "type": 2,
    "typicalcargo": [
        "rhs_pilot_transport_heli"
    ],
    "uavhacker": 0,
    "unitinfotype": "RHS_RscUnitInfoAir_Mi8",
    "unitinfotypelite": "RHS_RscUnitInfoAir_RTD_Basic_Mi8",
    "unitinfotypertd": "RHS_RscUnitInfoAir_RTD_Mi8",
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "hudoff": {
            "condition": "(player==driver this) and (this animationphase 'HUDAction' !=0)",
            "displayname": "HUD on",
            "displaynamedefault": "HUD on",
            "onlyforplayer": 1,
            "position": "zamerny",
            "radius": 1,
            "statement": "this animate ['HUDAction',0];this animate ['HUDaction_Hide',0]"
        },
        "hudon": {
            "condition": "(player==driver this) and (this animationphase 'HUDAction' !=1)",
            "displayname": "HUD off",
            "displaynamedefault": "HUD off",
            "onlyforplayer": 1,
            "position": "zamerny",
            "radius": 1,
            "statement": "this animate ['HUDAction',1];this animate ['HUDaction_Hide',1]"
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
        "wheelbrakes": {
            "condition": "!difficultyEnabledRTD && (call rhs_fnc_findPlayer) isEqualTo (driver this)",
            "displayname": "Toggle Wheel Brakes",
            "onlyforplayer": 1,
            "position": "pos driver",
            "radius": 15,
            "shortcut": "binocular",
            "showwindow": 0,
            "statement": "[this] call rhs_fnc_heli_wheelBrakes"
        }
    },
    "vehicleclass": "rhs_vehclass_helicopter",
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
        "initfov": 0.1,
        "maxanglex": 0,
        "maxangley": 0,
        "maxfov": 1.2,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": 0,
        "minangley": 0,
        "minfov": 0.1,
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
    "visualtargetsize": 1,
    "washdowndiameter": "40.0f",
    "washdownstrength": "1.0f",
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "watereffect": "HeliWater",
    "waterleakiness": 100,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.5,
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
            "bonename": "damper_front",
            "boundary": "wheel_1_bound",
            "center": "wheel_1_axis",
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
            "latstiffx": 2.5,
            "latstiffy": 18,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 15,
            "maxbraketorque": 2000,
            "maxcompression": 0,
            "maxdroop": 0.1,
            "maxhandbraketorque": 0,
            "moi": 0.62208,
            "side": "left",
            "springdamperrate": 99280,
            "springstrength": 600,
            "sprungmass": 200,
            "steering": 1,
            "suspforceapppointoffset": "wheel_1_axis",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_axis",
            "width": 0.488
        },
        "wheel_2": {
            "bonename": "damper_left",
            "boundary": "wheel_2_bound",
            "center": "wheel_2_axis",
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
            "latstiffx": 2.5,
            "latstiffy": 18,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 15,
            "maxbraketorque": 2000,
            "maxcompression": 0,
            "maxdroop": 0.2,
            "maxhandbraketorque": 0,
            "moi": 1.323,
            "side": "left",
            "springdamperrate": 99280,
            "springstrength": 600,
            "sprungmass": 667,
            "steering": 0,
            "suspforceapppointoffset": "wheel_2_axis",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_axis",
            "width": 0.27
        },
        "wheel_3": {
            "bonename": "damper_right",
            "boundary": "wheel_3_bound",
            "center": "wheel_3_axis",
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
            "latstiffx": 2.5,
            "latstiffy": 18,
            "longitudinalstiffnessperunitgravity": 5000,
            "mass": 15,
            "maxbraketorque": 2000,
            "maxcompression": 0,
            "maxdroop": 0.2,
            "maxhandbraketorque": 0,
            "moi": 1.323,
            "side": "right",
            "springdamperrate": 99280,
            "springstrength": 600,
            "sprungmass": 667,
            "steering": 0,
            "suspforceapppointoffset": "wheel_3_axis",
            "susptraveldirection": [
                0,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_3_axis",
            "width": 0.27
        }
    },
    "windsockexist": 0
}