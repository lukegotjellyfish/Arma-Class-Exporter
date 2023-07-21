d = {
    "_generalmacro": "Heli_light_03_base_F",
    "_mainbladecenter": "rotor_center",
    "access": 0,
    "accuracy": 1.5,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 200,
    "aggregatereflectors": [
        [
            "Light_1",
            "Light_2"
        ],
        [
            "Light_3",
            "Light_4"
        ]
    ],
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
        "collisionlightred_source": {
            "markerlight": "CollisionRed",
            "source": "MarkerLight"
        },
        "collisionlightwhite_source": {
            "markerlight": "CollisionWhite",
            "source": "MarkerLight"
        },
        "doorhandler_l": {
            "animperiod": 0.0001,
            "initphase": 0,
            "sound": "MetalDoorsSound",
            "soundposition": "doorL_axis",
            "source": "user"
        },
        "doorhandler_r": {
            "animperiod": 0.0001,
            "initphase": 0,
            "sound": "MetalDoorsSound",
            "soundposition": "doorL_axis",
            "source": "user"
        },
        "doorl": {
            "animperiod": 0.8,
            "initphase": 0,
            "sound": "MetalDoorsSound",
            "soundposition": "doorL_axis",
            "source": "door"
        },
        "doorlb": {
            "animperiod": 1.5,
            "initphase": 1,
            "sound": "MetalOldBigDoorsSound",
            "soundposition": "doorLB_axis",
            "source": "user"
        },
        "doorr": {
            "animperiod": 0.8,
            "initphase": 0,
            "sound": "MetalDoorsSound",
            "soundposition": "doorR_axis",
            "source": "door"
        },
        "doorrb": {
            "animperiod": 1.5,
            "initphase": 1,
            "sound": "MetalOldBigDoorsSound",
            "soundposition": "doorRB_axis",
            "source": "user"
        },
        "gatling_1": {
            "source": "revolving",
            "weapon": "rhs_weap_m134_minigun_1"
        },
        "gatling_2": {
            "source": "revolving",
            "weapon": "rhs_weap_m134_minigun_2"
        },
        "gunl_revolving": {
            "source": "revolving",
            "weapon": "M134_minigun"
        },
        "gunr_revolving": {
            "source": "revolving",
            "weapon": "M134_minigun"
        },
        "hide_cargodoors": {
            "animperiod": 0.0001,
            "displayname": "hide cargo doors",
            "initphase": 1,
            "mass": -200,
            "sound": "MetalDoorsSound",
            "soundposition": "doorL_axis",
            "source": "user"
        },
        "hide_frontdoors": {
            "animperiod": 0.0001,
            "displayname": "hide front doors",
            "initphase": 1,
            "mass": -100,
            "sound": "MetalDoorsSound",
            "soundposition": "doorL_axis",
            "source": "user"
        },
        "hide_mg": {
            "animperiod": 0.0001,
            "displayname": "hide MG",
            "initphase": 0,
            "mass": -120,
            "sound": "MetalDoorsSound",
            "soundposition": "doorL_axis",
            "source": "user"
        },
        "hide_rockets": {
            "animperiod": 0.0001,
            "initphase": 0,
            "mass": -50,
            "sound": "MetalDoorsSound",
            "soundposition": "doorL_axis",
            "source": "user"
        },
        "hideweapons": {
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
        "hitavionics": {
            "hitpoint": "HitAvionics",
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
        "hitwinch_source": {
            "hitpoint": "HitWinch",
            "raw": 1,
            "source": "hit"
        },
        "hudaction": {
            "animperiod": 2,
            "initphase": 0,
            "source": "user"
        },
        "hudaction_1": {
            "animperiod": 0.1,
            "initphase": 0,
            "source": "user"
        },
        "mainrotor_folded": {
            "animperiod": 0.001,
            "displayname": "fold main rotor",
            "initphase": 0,
            "mass": 1,
            "onphasechanged": "_this call rhs_fnc_foldHeli",
            "source": "user"
        },
        "missiles_revolving": {
            "source": "revolving",
            "weapon": "missiles_DAR"
        },
        "muzzle_flash": {
            "animperiod": 1e-06,
            "source": "ammorandom",
            "weapon": "M134_minigun"
        },
        "muzzle_hide": {
            "source": "reload",
            "weapon": "M134_minigun"
        },
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m134_minigun_1"
        },
        "muzzle_rot_hmg2": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m134_minigun_2"
        },
        "pip1_on": {
            "animperiod": 0.0001,
            "initphase": 0,
            "sound": "MetalDoorsSound",
            "soundposition": "doorL_axis",
            "source": "user"
        },
        "pip2_on": {
            "animperiod": 0.0001,
            "initphase": 0,
            "sound": "MetalDoorsSound",
            "soundposition": "doorL_axis",
            "source": "user"
        },
        "rocketpods_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        }
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmax": 60,
    "antirollbarspeedmin": 20,
    "armor": 40,
    "armorlights": 0.4,
    "armorstructural": 2,
    "armory": {
        "description": "The WY-55 Hellcat is a multi-purpose military helicopter, most suited for a role of anti-surface battlefield utility, which also has a limited transport capacity. It replaces its predecessor the Super Lynx, improving the maneuverability, durability and protection. The armed version is fitted with twin miniguns and unguided rockets."
    },
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "HeliAttenuation",
    "attributes": {
        "doorl": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open left door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "DoorL"
        },
        "doorr": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open right door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "DoorR"
        },
        "foldheli": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Fold helicopter rotors",
            "expression": "[_this,_value] call rhs_fnc_foldHeli",
            "property": "FoldHeli"
        },
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        }
    },
    "audible": 50,
    "author": "Red Hammer Studios",
    "autocenter": 1,
    "availableforsupporttypes": [
        "CAS_Heli",
        "Drop",
        "Transport"
    ],
    "backrotorforcecoef": 1,
    "backrotorspeed": 6.1,
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
        "RHS_UH1Y_Cargo02",
        "RHS_UH1Y_Cargo03",
        "RHS_UH1Y_Cargo03",
        "RHS_UH1Y_Cargo02",
        "RHS_UH1Y_Cargo01"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment2"
    ],
    "cargodoors": [
        "DoorLB"
    ],
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
    "cargoproxyindexes": [
        5
    ],
    "cargospec": {
        "cargo1": {
            "showheadphones": 1
        },
        "cargo2": {
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
                "irsensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 4000,
                        "minrange": 2000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 40,
                    "anglerangevertical": 30,
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
                        "maxrange": 4000,
                        "minrange": 4000,
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
                        "maxrange": 2000,
                        "minrange": 500,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 40,
                    "anglerangevertical": 30,
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
                        "maxrange": 2000,
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
            "presets": {
                "empty": {
                    "attachment": [
                        "",
                        ""
                    ],
                    "displayname": "<empty>"
                },
                "ffar": {
                    "attachment": [
                        "rhs_mag_M151_7_green",
                        "rhs_mag_M151_7_green",
                        "rhsusf_ANALE39_CMFlare_Chaff_Magazine_x4"
                    ],
                    "displayname": "FFAR"
                },
                "gs": {
                    "attachment": [
                        "rhs_mag_M151_19_green",
                        "rhs_mag_M151_19_green",
                        "rhsusf_ANALE39_CMFlare_Chaff_Magazine_x4"
                    ],
                    "displayname": "Ground Suppression"
                }
            },
            "pylons": {
                "cmdispenser": {
                    "attachment": "rhsusf_ANALE39_CMFlare_Chaff_Magazine_x4",
                    "hardpoints": [
                        "RHSUSF_cm_ANALE39",
                        "RHSUSF_cm_ANALE39_x2",
                        "RHSUSF_cm_ANALE39_x4"
                    ],
                    "maxweight": 800,
                    "priority": 1,
                    "uiposition": [
                        0.33,
                        0
                    ]
                },
                "pylon1": {
                    "attachment": "rhs_mag_M151_19_green",
                    "bay": -1,
                    "hardpoints": [
                        "RHS_HP_FFAR_USMC"
                    ],
                    "hitpoint": "HitPylon1",
                    "maxweight": 1200,
                    "priority": 1,
                    "uiposition": [
                        0.573,
                        0.44
                    ]
                },
                "pylon2": {
                    "attachment": "rhs_mag_M151_19_green",
                    "bay": -1,
                    "hardpoints": [
                        "RHS_HP_FFAR_USMC"
                    ],
                    "hitpoint": "HitPylon2",
                    "maxweight": 1200,
                    "mirroredmissilepos": 1,
                    "priority": 1,
                    "uiposition": [
                        0.1,
                        0.44
                    ]
                }
            },
            "uipicture": "rhsusf/addons/rhsusf_a2port_air2/data/loadouts/RHS_UH1_EDEN_CA.paa"
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
            "defaultdisplay": "SensorDisplay",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        }
    },
    "cost": 700000,
    "countermeasureactivationradius": 10000,
    "countsforscoreboard": 1,
    "crew": "rhsusf_usmc_marpat_d_helipilot",
    "crewcrashprotection": 0.25,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "cyclicasideforcecoef": 1,
    "cyclicforwardforcecoef": 0.9,
    "damage": {
        "mat": [
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_sklo.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_sklo_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_sklo_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_sklo_in.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_sklo_in_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_sklo_in_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_ext.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_ext_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_ext_destruct.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_int.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_int_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_int_destruct.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/launcher.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/launcher.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/launcher_destruct.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_cockpit.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_cockpit_damage.rvmat",
            "rhsusf/addons/rhsusf_a2port_air2/UH1Y/data/uh1y_cockpit_destruct.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default.rvmat",
            "a3/data_f/default_destruct.rvmat"
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
    "defaultusermfdvalues": [
        0,
        1,
        0.3,
        1
    ],
    "destrtype": "DestructWreck",
    "destructioneffects": {},
    "detectskill": 20,
    "displayname": "UH-1Y (Ground-Suppression)",
    "dlc": "RHS_USAF",
    "driveoncomponent": [
        "Skids"
    ],
    "driveraction": "RHS_UH1Y_Pilot",
    "drivercaneject": 0,
    "drivercansee": "2+4+8+16",
    "drivercompartments": 0,
    "driverdoor": "doorR",
    "driverforceoptics": 0,
    "driverinaction": "RHS_UH1Y_Pilot",
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
    "editorpreview": "rhsusf/addons/rhsusf_editorPreviews/data/RHS_UH1Y_d_GS.paa",
    "editorsubcategory": "EdSubcat_Helicopters",
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
        "rhsusf_eventhandlers": {}
    },
    "exhausts": {
        "exhaust1": {
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectHeliCom",
            "position": "exhaust1"
        },
        "exhaust2": {
            "direction": "exhaust2_dir",
            "effect": "ExhaustsEffectHeliCom",
            "position": "exhaust2"
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
    "faction": "rhs_faction_usmc_d",
    "features": "Randomization: No \t\t\t\t\t\t<br />Camo selections: 1 - the whole exterior \t\t\t\t\t\t<br />Script door sources: None \t\t\t\t\t\t<br />Script animations:  None \t\t\t\t\t\t<br />Executed scripts: None \t\t\t\t\t\t<br />Firing from vehicles: Positions 1, 2 (doors) \t\t\t\t\t\t<br />Slingload: Slingloads up to 2000 kg \t\t\t\t\t\t<br />Cargo proxy indexes: 1 to 6",
    "featuretype": 0,
    "fireresistance": 10,
    "flarevelocity": 100,
    "forcehidedriver": 0,
    "formationtime": 10,
    "formationx": 50,
    "formationz": 100,
    "fuelcapacity": 600,
    "fuelconsumptionrate": 0.103,
    "fuelexplosionpower": 1,
    "fxexplo": {
        "access": 1
    },
    "geardown": [
        "gearDownInt",
        "gearDownExt"
    ],
    "geardownext": [
        "A3/Sounds_F/vehicles/air/Heli_Transport_01/gear_down_OUT",
        1,
        1,
        1000
    ],
    "geardownint": [
        "A3/Sounds_F/vehicles/air/Heli_Transport_01/gear_down_IN",
        1,
        1,
        100
    ],
    "geardowntime": 2,
    "gearminalt": 0.5,
    "gearretracting": 0,
    "gearsupfrictioncoef": 0.5,
    "gearup": [
        "gearUpInt",
        "gearUpExt"
    ],
    "gearupext": [
        "A3/Sounds_F/vehicles/air/Heli_Transport_01/gear_up_OUT",
        1,
        1,
        1000
    ],
    "gearupint": [
        "A3/Sounds_F/vehicles/air/Heli_Transport_01/gear_up_IN",
        1,
        1,
        100
    ],
    "gearuptime": 3.33,
    "getinaction": "pilot_Heli_Light_02_Enter",
    "getinoutonproxy": 0,
    "getinproxyorder": [
        1,
        2,
        3,
        4,
        5,
        6,
        7
    ],
    "getinradius": 1.5,
    "getoutaction": "pilot_Heli_Light_02_Exit",
    "gforceshakeattenuation": 0.5,
    "ghostpreview": "",
    "groupcameraposition": [
        0,
        5,
        -30
    ],
    "gunbeg": [
        "z_gunL_muzzle",
        "z_gunR_muzzle"
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
    "gunend": [
        "z_gunL_chamber",
        "z_gunR_chamber"
    ],
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
    "helmetmounteddisplay": 0,
    "hiddenselections": [
        "camo1",
        "camo2",
        "rn1",
        "rn2",
        "rn3",
        "rn4",
        "tn1",
        "tn2",
        "tn3",
        "tn4",
        "tn5",
        "tn6",
        "dn1",
        "dn2",
        "dn3",
        "dn4",
        "dn5",
        "dn6",
        "dn7",
        "dn8",
        "dn9",
        "dn10",
        "dn11",
        "dn12",
        "zn1",
        "zn2",
        "zn3"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsusf/addons/rhsusf_a2port_air2/uh1y/data/uh1y_ext_co.paa",
        "rhsusf/addons/rhsusf_a2port_air2/uh1y/data/uh1y_int_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hideweaponsgunner": 1,
    "hitpoints": {
        "hitavionics": {
            "armor": 1.3,
            "convexcomponent": "avionics_hit",
            "explosionshielding": 1.5,
            "material": 51,
            "minimalhit": 0.05,
            "name": "avionics_hit",
            "passthrough": 1,
            "radius": 0.25,
            "visual": "-"
        },
        "hitengine": {
            "armor": 999,
            "convexcomponent": "engine_hit",
            "depends": "0.5 * (HitEngine1 + HitEngine2)",
            "explosionshielding": 1,
            "material": 51,
            "minimalhit": 1,
            "name": "engine_hit",
            "passthrough": 1,
            "radius": 0.05,
            "visual": "motor"
        },
        "hitengine1": {
            "armor": 2.5,
            "convexcomponent": "engine_1_hit",
            "explosionshielding": 3,
            "material": 51,
            "minimalhit": 0.05,
            "name": "engine_1_hit",
            "passthrough": 1,
            "radius": 0.12,
            "visual": "motor"
        },
        "hitengine2": {
            "armor": 2.5,
            "convexcomponent": "engine_2_hit",
            "explosionshielding": 3,
            "material": 51,
            "minimalhit": 0.05,
            "name": "engine_2_hit",
            "passthrough": 1,
            "radius": 0.12,
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
            "armor": 3,
            "convexcomponent": "hull_hit",
            "depends": "Total",
            "explosionshielding": 4,
            "material": 51,
            "minimalhit": 0.05,
            "name": "fuel_hit",
            "passthrough": 0.5,
            "radius": 0.2,
            "visual": "fuel_hit"
        },
        "hitgear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passthrough": 0
        },
        "hitglass1": {
            "armor": 1,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 2,
            "minimalhit": 0.025,
            "name": "glass1",
            "passthrough": 0,
            "radius": 0.37,
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
            "minimalhit": 0.025,
            "name": "glass10",
            "passthrough": 0,
            "radius": 0.24,
            "visual": "glass10"
        },
        "hitglass2": {
            "armor": 1,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects2",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects2",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects2",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects2",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects2",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects2",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects2",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects2",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects2",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects2",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1.5,
            "minimalhit": 0.025,
            "name": "glass2",
            "passthrough": 0,
            "radius": 0.37,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": 1,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects3",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects3",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects3",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects3",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects3",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects3",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects3",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects3",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects3",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects3",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1.5,
            "minimalhit": 0.025,
            "name": "glass3",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": 1,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects4",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects4",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects4",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects4",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects4",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects4",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects4",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects4",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects4",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects4",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1.5,
            "minimalhit": 0.025,
            "name": "glass4",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "glass4"
        },
        "hitglass5": {
            "armor": 1,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects5",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects5",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects5",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects5",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects5",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects5",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects5",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects5",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects5",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects5",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 2,
            "minimalhit": 0.025,
            "name": "glass5",
            "passthrough": 0,
            "radius": 0.34,
            "visual": "glass5"
        },
        "hitglass6": {
            "armor": 1,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects6",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects6",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects6",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects6",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects6",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects6",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects6",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects6",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects6",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects6",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1.5,
            "minimalhit": 0.025,
            "name": "glass6",
            "passthrough": 0,
            "radius": 0.34,
            "visual": "glass6"
        },
        "hitglass7": {
            "armor": 1,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects1",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 2,
            "minimalhit": 0.025,
            "name": "glass7",
            "passthrough": 0,
            "radius": 0.37,
            "visual": "glass7"
        },
        "hitglass8": {
            "armor": 1,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "brokenglass1": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects8",
                    "simulation": "particles",
                    "type": "BrokenGlass1NS"
                },
                "brokenglass1s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects8",
                    "simulation": "particles",
                    "type": "BrokenGlass1SS"
                },
                "brokenglass2": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects8",
                    "simulation": "particles",
                    "type": "BrokenGlass2NS"
                },
                "brokenglass2s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects8",
                    "simulation": "particles",
                    "type": "BrokenGlass2SS"
                },
                "brokenglass3": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects8",
                    "simulation": "particles",
                    "type": "BrokenGlass3NS"
                },
                "brokenglass3s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects8",
                    "simulation": "particles",
                    "type": "BrokenGlass3SS"
                },
                "brokenglass4": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects8",
                    "simulation": "particles",
                    "type": "BrokenGlass4NS"
                },
                "brokenglass4s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects8",
                    "simulation": "particles",
                    "type": "BrokenGlass4SS"
                },
                "brokenglass5": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects8",
                    "simulation": "particles",
                    "type": "BrokenGlass5NS"
                },
                "brokenglass5s": {
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05,
                    "position": "GlassEffects8",
                    "simulation": "particles",
                    "type": "BrokenGlass5SS"
                }
            },
            "explosionshielding": 1.5,
            "minimalhit": 0.025,
            "name": "glass8",
            "passthrough": 0,
            "radius": 0.34,
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
            "minimalhit": 0.025,
            "name": "glass9",
            "passthrough": 0,
            "radius": 0.24,
            "visual": "glass9"
        },
        "hithrotor": {
            "armor": 1,
            "material": 51,
            "name": "velka vrtule",
            "passthrough": 0.5,
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
        "hitpylon1": {
            "armor": -30,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
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
            "radius": 0.7,
            "visual": "-"
        },
        "hitpylon2": {
            "armor": -30,
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
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
            "radius": 0.7,
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
            "armor": 1,
            "material": 51,
            "name": "mala vrtule",
            "passthrough": 0.5,
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
    "icon": "rhsusf/addons/rhsusf_a2port_air2/data/mapico/Icon_UH1Y_CA.paa",
    "impacteffectspeedlimit": 8,
    "impacteffectssea": "ImpactEffectsAir",
    "incomingmissiledetectionsystem": 16,
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
    "library": {
        "libtextdesc": "The UH-1Y Venom is an American medium-size multipurpose utility army helicopter. It is equipped with two external Mk66 70 mm rocket stations and two M240D 7.62 mm machine guns.<br />The UH-1Y is able to carry up to 3 tons of cargo or up to 10 passengers. It can provide close air support missions as well as transportation or reconnaissance."
    },
    "liftforcecoef": 1,
    "limitedspeedcoef": 0.22,
    "lockdetectionsystem": "8 + 4",
    "magazines": [],
    "mainbladecenter": "rotor_center",
    "mainbladeradius": 6.2,
    "mainrotorspeed": 1.2,
    "mapsize": 15,
    "markerlights": {
        "greenstill": {
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
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.15,
            "intensity": 75,
            "name": "zeleny pozicni",
            "useflare": 0
        },
        "redblinking": {
            "ambient": [
                0.09,
                0.015,
                0.01
            ],
            "blinking": 1,
            "blinkingpattern": [
                0.1,
                0.9
            ],
            "blinkingpatternguarantee": 0,
            "color": [
                0.9,
                0.15,
                0.1
            ],
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.2,
            "intensity": 75,
            "name": "bily pozicni blik"
        },
        "redstill": {
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
            "daylight": 0,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.15,
            "intensity": 75,
            "name": "cerveny pozicni",
            "useflare": 0
        },
        "whiteblinking": {
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
            "drawlightcentersize": 0.08,
            "drawlightsize": 0.25,
            "intensity": 75,
            "name": "cerveny pozicni blik"
        },
        "whitestill": {
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
            "drawlightcentersize": 0.04,
            "drawlightsize": 0.2,
            "intensity": 75,
            "name": "bily pozicni"
        }
    },
    "maxbackrotordive": 0,
    "maxdetectrange": 20,
    "maxfordingdepth": 0.7,
    "maxgforce": 2,
    "maximumload": 2000,
    "maxmainrotordive": 0,
    "maxsmokedamage": 0.99,
    "maxspeed": 295,
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
        "z_gunL_muzzle",
        "z_gunR_muzzle"
    ],
    "memorypointlmissile": "l strela",
    "memorypointlrocket": "l raketa",
    "memorypointpilot": "pilot",
    "memorypointrmissile": "p strela",
    "memorypointrrocket": "p raketa",
    "memorypointsgetincargo": [
        "pos cargo L"
    ],
    "memorypointsgetincargodir": [
        "pos cargo L dir"
    ],
    "memorypointsgetincargoprecise": [
        "pos cargo"
    ],
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriver": "pos Driver",
    "memorypointsgetindriverdir": "pos gunner dir",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsgetingunner": "pos gunner",
    "memorypointsgetingunnerdir": "pos gunner dir",
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
    "model": "rhsusf/addons/rhsusf_a2port_air2/UH1Y/UH1Y.p3d",
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
    "numberphysicalwheels": 0,
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
    "picture": "rhsusf/addons/rhsusf_a2port_air/data/ico/rhs_uh1y_pic_ca.paa",
    "pilotcamera": {},
    "pilotspec": {
        "showheadphones": 0
    },
    "portrait": "",
    "precisegetinout": 1,
    "precision": 100,
    "predictturnplan": 1,
    "predictturnsimul": 1.2,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 1,
    "radartype": 0,
    "reflectors": {
        "middle": {
            "ambient": [
                100,
                100,
                100,
                0
            ],
            "attenuation": {
                "constant": 0,
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
            "direction": "svetlo konec",
            "flaresize": 6,
            "hitpoint": "svetlo",
            "innerangle": 20,
            "intensity": 50,
            "outerangle": 60,
            "position": "svetlo",
            "selection": "svetlo",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {},
    "replacedamaged": "",
    "replacedamagedhitpoints": [],
    "replacedamagedlimit": 0.9,
    "reversed": 1,
    "rhs_hasnoradar": 1,
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
        "A3/Sounds_F/vehicles/air/noises/heli_damage_rotor_int_open_1",
        1,
        1
    ],
    "rotordamageout": [
        "A3/Sounds_F/vehicles/air/noises/heli_damage_rotor_ext_1",
        2.51189,
        1,
        150
    ],
    "rotorlibhelicopterproperties": {
        "autohovercorrection": [
            5,
            2.4,
            0
        ],
        "defaultcollective": 0.75,
        "horizontalwingsanglecollmax": 0,
        "horizontalwingsanglecollmin": 0,
        "maxhorizontalstabilizerleftstress": 10000,
        "maxhorizontalstabilizerrightstress": 10000,
        "maxmainrotorstress": 130000,
        "maxtailrotorstress": 50000,
        "maxtorque": 1280,
        "maxverticalstabilizerstress": 10000,
        "retreatbladestallwarningspeed": 87.4556,
        "rtdconfig": "rhsusf/addons/rhsusf_c_a2port_air/UH1Y/RTD_UH1Y.xml",
        "stressdamagepersec": 0.00333333
    },
    "scope": 1,
    "scopecurator": 2,
    "secondaryexplosion": -1,
    "selectionbacklights": "zadni svetlo",
    "selectionclan": "clan",
    "selectiondamage": "trup",
    "selectiondashboard": "podsvit pristroju",
    "selectionfireanim": "",
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
    "slingloadmaxcargomass": 4084,
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
        "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_stop_ext",
        2.51189,
        1,
        600
    ],
    "soundengineoffint": [
        "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_stop_int",
        0.398107,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_start_ext",
        2.51189,
        1,
        600
    ],
    "soundengineonint": [
        "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_start_int",
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
        "A3/Sounds_F/vehicles/air/Heli_Light_03/open",
        1,
        1
    ],
    "soundgetout": [
        "A3/Sounds_F/vehicles/air/Heli_Light_03/close",
        1,
        1,
        50
    ],
    "soundhitscream": {},
    "soundincommingmissile": [
        "/A3/Sounds_F/vehicles/air/noises/alarm_locked_by_missile_2",
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
                "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_engine_ext",
                1.77828,
                1,
                700
            ],
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        "engineint": {
            "frequency": "rotorSpeed",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_engine_int",
                1,
                1
            ],
            "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
        },
        "gstress": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/noises/vehicle_stress2b",
                0.354813,
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
            "frequency": "rotorSpeed * (1-rotorThrust/5)",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_rotor_ext",
                1.41254,
                1,
                1100
            ],
            "volume": "camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
        },
        "rotorint": {
            "frequency": "rotorSpeed * (1-rotorThrust/5)",
            "sound": [
                "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_rotor_int",
                1.77828,
                1
            ],
            "volume": "(1-camPos)*(0 max (rotorSpeed*rotorSpeed-0.1))*(1 + rotorThrust)"
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
                "A3/Sounds_F/vehicles/air/Heli_Light_03/rotor_swist",
                1,
                1,
                300
            ],
            "volume": "camPos * (rotorThrust factor [0.7, 0.9])"
        },
        "scrubbuildingext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubBuildingExt",
                1,
                1,
                100
            ],
            "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
        },
        "scrubbuildingint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubBuildingInt",
                1,
                1,
                100
            ],
            "volume": "2 * (1 - camPos) * (scrubBuilding factor[0.02, 0.05])"
        },
        "scrublandext": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubLandExt",
                1,
                1,
                100
            ],
            "volume": "camPos * (scrubLand factor[0.02, 0.05])"
        },
        "scrublandint": {
            "frequency": 1,
            "sound": [
                "A3/Sounds_F/vehicles/air/noises/scrubLandInt_open",
                1,
                1,
                100
            ],
            "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05])"
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
                "A3/Sounds_F/vehicles/air/noises/scrubTreeExt",
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
                "A3/Sounds_F/vehicles/air/noises/wind_open_int",
                0.562341,
                1,
                50
            ],
            "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
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
                    "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_engine_ext",
                    1.77828,
                    1,
                    700
                ],
                "volume": "camPos*((rotorSpeed-0.72)*4)"
            },
            "engineint": {
                "frequency": "rotorSpeed",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_engine_int",
                    1,
                    1
                ],
                "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
            },
            "gstress": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/noises/vehicle_stress2b",
                    0.354813,
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
                "frequency": "rotorSpeed * (1-rotorThrust/5)",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_rotor_ext",
                    1.41254,
                    1,
                    1100
                ],
                "volume": "camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
            },
            "rotorint": {
                "frequency": "rotorSpeed * (1-rotorThrust/5)",
                "sound": [
                    "A3/Sounds_F/vehicles/air/Heli_Light_03/heli_rotor_int",
                    1.77828,
                    1
                ],
                "volume": "(1-camPos)*(0 max (rotorSpeed*rotorSpeed-0.1))*(1 + rotorThrust)"
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
                    "A3/Sounds_F/vehicles/air/Heli_Light_03/rotor_swist",
                    1,
                    1,
                    300
                ],
                "volume": "camPos * (rotorThrust factor [0.7, 0.9])"
            },
            "scrubbuildingext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubBuildingExt",
                    1,
                    1,
                    100
                ],
                "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
            },
            "scrubbuildingint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubBuildingInt",
                    1,
                    1,
                    100
                ],
                "volume": "2 * (1 - camPos) * (scrubBuilding factor[0.02, 0.05])"
            },
            "scrublandext": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubLandExt",
                    1,
                    1,
                    100
                ],
                "volume": "camPos * (scrubLand factor[0.02, 0.05])"
            },
            "scrublandint": {
                "frequency": 1,
                "sound": [
                    "A3/Sounds_F/vehicles/air/noises/scrubLandInt_open",
                    1,
                    1,
                    100
                ],
                "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05])"
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
                    "A3/Sounds_F/vehicles/air/noises/scrubTreeExt",
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
                    "A3/Sounds_F/vehicles/air/noises/wind_open_int",
                    0.562341,
                    1,
                    50
                ],
                "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
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
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_water_ext_1",
        1,
        1,
        100
    ],
    "soundwatercollision2": [
        "A3/Sounds_F/vehicles/crashes/helis/Heli_coll_water_ext_2",
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
    "supplyradius": 1.2,
    "tailbladecenter": "rotor_02_center",
    "tailbladeradius": 1.2,
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
    "texturelist": [
        "standard",
        1
    ],
    "texturesources": {
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Standard",
            "factions": [
                "rhs_faction_usmc_wd",
                "rhs_faction_usmc_d"
            ],
            "textures": [
                "rhsusf/addons/rhsusf_a2port_air2/uh1y/data/uh1y_ext_co.paa",
                "rhsusf/addons/rhsusf_a2port_air2/uh1y/data/uh1y_int_co.paa"
            ]
        }
    },
    "threat": [
        0.8,
        0.1,
        0.3
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportbackpacks": {
        "_xx_b_parachute": {
            "backpack": "B_Parachute",
            "count": 4
        }
    },
    "transportfuel": 0,
    "transportitems": {
        "_xx_firstaidkit": {
            "count": 10,
            "name": "FirstAidKit"
        },
        "_xx_medikit": {
            "count": 2,
            "name": "Medikit"
        }
    },
    "transportmagazines": {
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "count": 12,
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
        "_xx_rhs_mag_m67": {
            "count": 4,
            "magazine": "rhs_mag_m67"
        }
    },
    "transportmaxbackpacks": 1,
    "transportmaxmagazines": 20,
    "transportmaxweapons": 3,
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
            "canhidegunner": -1,
            "cantcreateai": 1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
            "gunneraction": "passenger_inside_2",
            "gunnercaneject": 1,
            "gunnercompartments": "Compartment2",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_HIND_Cargo_Exit",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Right Bench 1)",
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
            "maxelev": 15,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": -48,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
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
            "minelev": -45,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -104,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 1,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 1,
            "proxytype": "CPCargo",
            "reflectors": {},
            "selectionfireanim": "",
            "showalltargets": 0,
            "showascargo": 1,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundattenuationturret": "HeliAttenuationRamp",
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
                "rhsusf_weap_DummyLauncher"
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
            "canhidegunner": -1,
            "cantcreateai": 1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
            "gunneraction": "passenger_inside_2",
            "gunnercaneject": 1,
            "gunnercompartments": "Compartment2",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_HIND_Cargo_Exit",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Right Bench 2)",
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
            "maxelev": 15,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 47,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos cargo R4",
            "memorypointsgetingunnerdir": "pos cargo R4 dir",
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
            "minturn": 22,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 1,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 3,
            "proxytype": "CPCargo",
            "reflectors": {},
            "selectionfireanim": "",
            "showalltargets": 0,
            "showascargo": 1,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundattenuationturret": "HeliAttenuationRamp",
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
                "rhsusf_weap_DummyLauncher"
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
            "canhidegunner": -1,
            "cantcreateai": 1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
            "gunneraction": "passenger_inside_2",
            "gunnercaneject": 1,
            "gunnercompartments": "Compartment2",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_HIND_Cargo_Exit",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Right Bench 3)",
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
            "maxelev": 15,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 70,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos cargo R2",
            "memorypointsgetingunnerdir": "pos cargo R2 dir",
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
            "minturn": 22,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 1,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 6,
            "proxytype": "CPCargo",
            "reflectors": {},
            "selectionfireanim": "",
            "showalltargets": 0,
            "showascargo": 1,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundattenuationturret": "HeliAttenuationRamp",
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
                "rhsusf_weap_DummyLauncher"
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
            "canhidegunner": -1,
            "cantcreateai": 1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
            "gunneraction": "passenger_inside_2",
            "gunnercaneject": 1,
            "gunnercompartments": "Compartment2",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_HIND_Cargo_Exit",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Left Bench 1)",
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
            "maxelev": 15,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 104,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
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
            "minelev": -45,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 58,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 1,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 2,
            "proxytype": "CPCargo",
            "reflectors": {},
            "selectionfireanim": "",
            "showalltargets": 0,
            "showascargo": 1,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundattenuationturret": "HeliAttenuationRamp",
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
                "rhsusf_weap_DummyLauncher"
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
            "canhidegunner": -1,
            "cantcreateai": 1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
            "gunneraction": "passenger_inside_2",
            "gunnercaneject": 1,
            "gunnercompartments": "Compartment2",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_HIND_Cargo_Exit",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Left Bench 2)",
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
            "maxelev": 15,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": -16,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos cargo L4",
            "memorypointsgetingunnerdir": "pos cargo L4 dir",
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
            "minturn": -40,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 1,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 4,
            "proxytype": "CPCargo",
            "reflectors": {},
            "selectionfireanim": "",
            "showalltargets": 0,
            "showascargo": 1,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundattenuationturret": "HeliAttenuationRamp",
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
                "rhsusf_weap_DummyLauncher"
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
            "canhidegunner": -1,
            "cantcreateai": 1,
            "canusescanners": 1,
            "castgunnershadow": 0,
            "commanding": -1,
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
            "gunneraction": "passenger_inside_2",
            "gunnercaneject": 1,
            "gunnercompartments": "Compartment2",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_HIND_Cargo_Exit",
            "gunnerinaction": "ManActTestDriver",
            "gunnerlefthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnername": "Passenger (Left Bench 3)",
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
            "maxelev": 15,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 3,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
            "memorypointgunneroptics": "",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos cargo L2",
            "memorypointsgetingunnerdir": "pos cargo L2 dir",
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
            "minturn": -55,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "outgunnermayfire": 1,
            "playerposition": 1,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 7,
            "proxytype": "CPCargo",
            "reflectors": {},
            "selectionfireanim": "",
            "showalltargets": 0,
            "showascargo": 1,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundattenuationturret": "HeliAttenuationRamp",
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
                "rhsusf_weap_DummyLauncher"
            ]
        },
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
                                8000,
                                16000,
                                20000,
                                50000
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
                                8000,
                                16000,
                                20000,
                                50000
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
            "disablesoundattenuation": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "enablemanualfire": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "ObsGun",
            "gunbeg": "gun_end",
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
            "gunend": "gun_begin",
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
            "gunneraction": "RHS_UH1Y_Copilot",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "DoorL",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "copilot_Heli_Light_02_Enter",
            "gunnergetoutaction": "copilot_Heli_Light_02_Exit",
            "gunnerhasflares": 0,
            "gunnerinaction": "RHS_UH1Y_Copilot",
            "gunnerlefthandanimname": "lever_copilot",
            "gunnerleftleganimname": "pedalL",
            "gunnername": "Observer",
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
            "hitpoints": {
                "hitgun": {
                    "armor": 1,
                    "material": -1,
                    "name": "main_gun_hit",
                    "passthrough": 0.2,
                    "radius": 0.25,
                    "visual": "gun"
                },
                "hitturret": {
                    "armor": 1,
                    "material": -1,
                    "name": "main_turret_hit",
                    "passthrough": 0.2,
                    "radius": 0.25,
                    "visual": "gun"
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
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [
                "rhs_LaserMag_ai"
            ],
            "maxcamelev": 90,
            "maxelev": 30,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 180,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "gun_end",
            "memorypointgunneroptics": "commanderview",
            "memorypointgunneroutoptics": "",
            "memorypointsgetingunner": "pos codriver",
            "memorypointsgetingunnerdir": "pos codriver dir",
            "memorypointsgetingunnerprecise": "",
            "mfd": {},
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
            "minturn": -180,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "wide": {
                    "directionstabilized": 1,
                    "gunneropticsmodel": "rhsusf/addons/rhsusf_optics/data/rhs_uh1_flir",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.466,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 0.466,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.0218,
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
                    "minfov": 0.33,
                    "visionmode": [
                        "Normal",
                        "NVG"
                    ]
                }
            },
            "outgunnermayfire": 1,
            "playerposition": 0,
            "precisegetinout": 1,
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
                    "intensity": 4,
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
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
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
                    "intensity": 7,
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
                        "hardlimitend": 1.5,
                        "hardlimitstart": 1,
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
                    "intensity": 7,
                    "outerangle": 165,
                    "position": "cargo_light_2",
                    "selection": "cargo_light_2",
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
                "initanglex": -15,
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
            "animationsourcehatch": "",
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
                    "defaultdisplay": "SensorDisplay",
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
            "gunneraction": "RHS_UH1Y_Gunner_L",
            "gunnercompartments": "Compartment2",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_HIND_Cargo_Exit",
            "gunnerhasflares": 0,
            "gunnerinaction": "RHS_UH1Y_Gunner_L",
            "gunnerlefthandanimname": "OtocHlaven_1",
            "gunnerleftleganimname": "gunner_1_leg_left",
            "gunnername": "Left door gunner",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "A3/weapons_f/reticle/optics_empty",
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
            "gunneroutopticsshowcursor": 1,
            "gunnerrighthandanimname": "OtocHlaven_1",
            "gunnerrightleganimname": "gunner_1_legs",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 0,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": 90,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [
                "rhs_mag_762x51_m80a1_4000"
            ],
            "maxcamelev": 90,
            "maxelev": 20,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 125,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "gunnerview_1",
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
            "minelev": -55,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": 30,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "viewoptics": {
                    "gunneropticsmodel": "A3/weapons_f/reticle/optics_empty",
                    "gunneroutopticsmodel": "A3/weapons_f/reticle/optics_empty",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.7,
                    "maxanglex": 75,
                    "maxangley": 100,
                    "maxfov": 1.1,
                    "minanglex": -75,
                    "minangley": -100,
                    "minfov": 0.25,
                    "visionmode": []
                }
            },
            "opticsout": {
                "monocular": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.75,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 1.25,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.25,
                    "visionmode": [
                        "Normal",
                        "NVG"
                    ]
                }
            },
            "outgunnermayfire": 1,
            "playerposition": 1,
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
            "soundattenuationturret": "HeliAttenuationGunner",
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "",
                0.01,
                1
            ],
            "stabilizedinaxes": "StabilizedInAxesNone",
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            "turretfollowfreelook": 0,
            "turretinfotype": "RscWeaponZeroing",
            "turrets": {},
            "turretspec": {
                "showheadphones": 1
            },
            "usepip": 0,
            "viewgunner": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 75,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -75,
                "minangley": -100,
                "minfov": 0.25,
                "visionmode": []
            },
            "viewgunnerinexternal": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 75,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -75,
                "minangley": -100,
                "minfov": 0.25
            },
            "weapons": [
                "rhs_weap_m134_minigun_1"
            ]
        },
        "rightdoorgun": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 1,
            "animationsourcebody": "Turret_2",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "Gun_2",
            "animationsourcehatch": "",
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
                    "defaultdisplay": "SensorDisplay",
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
            "gunneraction": "RHS_UH1Y_Gunner_R",
            "gunnercompartments": "Compartment2",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInHeli_Transport_01Cargo",
            "gunnergetoutaction": "RHS_HIND_Cargo_Exit",
            "gunnerhasflares": 0,
            "gunnerinaction": "RHS_UH1Y_Gunner_R",
            "gunnerlefthandanimname": "OtocHlaven_2",
            "gunnerleftleganimname": "gunner_2_leg_left",
            "gunnername": "Right door gunner",
            "gunneropticscolor": [
                0,
                0,
                0,
                1
            ],
            "gunneropticseffect": [],
            "gunneropticsmodel": "A3/weapons_f/reticle/optics_empty",
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
            "gunneroutopticsshowcursor": 1,
            "gunnerrighthandanimname": "OtocHlaven_2",
            "gunnerrightleganimname": "gunner_2_legs",
            "gunnertype": "",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {},
            "ingunnermayfire": 1,
            "initcamelev": 0,
            "initelev": 0,
            "initoutelev": 0,
            "initoutturn": 0,
            "initturn": -90,
            "iscopilot": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "magazines": [
                "rhs_mag_762x51_m80a1_4000"
            ],
            "maxcamelev": 90,
            "maxelev": 20,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": -25,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "machinegun_1",
            "memorypointgunneroptics": "gunnerview_2",
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
            "minelev": -55,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -135,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "viewoptics": {
                    "gunneropticsmodel": "A3/weapons_f/reticle/optics_empty",
                    "gunneroutopticsmodel": "A3/weapons_f/reticle/optics_empty",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.7,
                    "maxanglex": 75,
                    "maxangley": 100,
                    "maxfov": 1.1,
                    "minanglex": -75,
                    "minangley": -100,
                    "minfov": 0.25,
                    "visionmode": []
                }
            },
            "opticsout": {
                "monocular": {
                    "gunneropticseffect": [],
                    "gunneropticsmodel": "",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.75,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "maxfov": 1.25,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.25,
                    "visionmode": [
                        "Normal",
                        "NVG"
                    ]
                }
            },
            "outgunnermayfire": 1,
            "playerposition": 1,
            "precisegetinout": 0,
            "primary": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "proxyindex": 3,
            "proxytype": "CPGunner",
            "reflectors": {},
            "selectionfireanim": "zasleh_1",
            "showalltargets": 0,
            "showascargo": 1,
            "showcrewaim": 0,
            "showhmd": 0,
            "slingloadoperator": 0,
            "soundattenuationturret": "HeliAttenuationGunner",
            "soundelevation": [
                "",
                0.00316228,
                1
            ],
            "soundservo": [
                "",
                0.01,
                1
            ],
            "stabilizedinaxes": "StabilizedInAxesNone",
            "startengine": 0,
            "turnin": {
                "turnoffset": 0
            },
            "turnout": {
                "turnoffset": 0
            },
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            "turretfollowfreelook": 0,
            "turretinfotype": "RscWeaponZeroing",
            "turrets": {},
            "turretspec": {
                "showheadphones": 1
            },
            "usepip": 0,
            "viewgunner": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 75,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -75,
                "minangley": -100,
                "minfov": 0.25,
                "visionmode": []
            },
            "viewgunnerinexternal": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowamb": 1,
            "viewgunnershadowdiff": 1,
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 75,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -75,
                "minangley": -100,
                "minfov": 0.25
            },
            "weapons": [
                "rhs_weap_m134_minigun_2"
            ]
        }
    },
    "type": 2,
    "typicalcargo": [
        "rhsusf_usmc_marpat_d_helicrew"
    ],
    "uavhacker": 0,
    "unitinfotype": "RHSUSF_RscUnitInfoAir_UH1Y",
    "unitinfotypelite": "RscUnitInfoAirRTDBasic",
    "unitinfotypertd": "RHSUSF_RscUnitInfoAirRTDFullDigital_UH1Y",
    "unloadincombat": 0,
    "useprecisegetinaction": 0,
    "useractions": {
        "hudoff": {
            "condition": "(player==driver this)and(this animationphase 'HUDAction' !=1)",
            "displayname": "HUD on",
            "displaynamedefault": "HUD on",
            "onlyforplayer": 1,
            "position": "zamerny",
            "radius": 1,
            "statement": "this animate ['HUDAction',1];this animate ['HUDAction_1',1]"
        },
        "hudon": {
            "condition": "(player==driver this)and(this animationphase 'HUDAction' !=0)",
            "displayname": "HUD off",
            "displaynamedefault": "HUD off",
            "onlyforplayer": 1,
            "position": "zamerny",
            "radius": 1,
            "statement": "this animate ['HUDAction',0];this animate ['HUDAction_1',0]"
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
        "togglepip": {
            "condition": "( (call rhsusf_fnc_findPlayer)==driver this) or ((call rhsusf_fnc_findPlayer)==this turretUnit [0]) ",
            "displayname": "Toggle monitor",
            "displaynamedefault": "Toggle monitor",
            "onlyforplayer": 1,
            "position": "zamerny",
            "radius": 1,
            "statement": "call rhs_fnc_uh1_toggleCam"
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
        "initanglex": -2.5,
        "initangley": 0,
        "initfov": 0.75,
        "maxanglex": 85,
        "maxangley": 150,
        "maxfov": 1.2,
        "maxmovex": 0.2,
        "maxmovey": 0.1,
        "maxmovez": 0.2,
        "minanglex": -65,
        "minangley": -150,
        "minfov": 0.3,
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
    "windsockexist": 0
}