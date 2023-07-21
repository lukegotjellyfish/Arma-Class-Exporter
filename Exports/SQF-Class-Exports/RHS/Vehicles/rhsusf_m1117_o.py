d = {
    "_generalmacro": "Wheeled_APC_F",
    "accelaidforcecoef": 3,
    "accelaidforcespd": 2.23,
    "accelaidforceyoffset": -1.3,
    "access": 0,
    "accuracy": 0.25,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "afmax": 200,
    "aggregatereflectors": [
        [
            "Left",
            "Left2"
        ],
        [
            "Right",
            "Right2"
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
        "door_b": {
            "animperiod": 1,
            "initphase": 0,
            "source": "door"
        },
        "door_l": {
            "animperiod": 1,
            "initphase": 0,
            "source": "door"
        },
        "door_r": {
            "animperiod": 1,
            "initphase": 0,
            "source": "door"
        },
        "duke_hide": {
            "animperiod": 1e-05,
            "displayname": "hide DUKE antennas",
            "initphase": 0,
            "mass": -20,
            "onphasechanged": "_this + ([[0,0]]) call rhs_fnc_duke_vg;",
            "source": "user"
        },
        "hatch_commander": {
            "animperiod": 1,
            "initphase": 0,
            "source": "door"
        },
        "hatch_driver": {
            "animperiod": 1,
            "initphase": 0,
            "source": "door"
        },
        "hatch_gunner": {
            "animperiod": 1,
            "initphase": 0,
            "source": "door"
        },
        "hitduke1": {
            "hitpoint": "HitDuke1",
            "source": "Hit"
        },
        "hitduke2": {
            "hitpoint": "HitDuke2",
            "source": "Hit"
        },
        "hitglass1": {
            "hitpoint": "HitGlass1",
            "source": "Hit"
        },
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit"
        },
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit"
        },
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit"
        },
        "hitglass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit"
        },
        "hitglass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit"
        },
        "hithull": {
            "hitpoint": "HitHull",
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
        "hitmainsight": {
            "hitpoint": "HitMainSight",
            "source": "Hit"
        },
        "hitperiscope1": {
            "hitpoint": "HitPeriscope1",
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
        "muzzle_flash_gl": {
            "source": "reload",
            "weapon": "RHS_MK19"
        },
        "muzzle_rot_gl": {
            "source": "ammorandom",
            "weapon": "RHS_MK19"
        },
        "muzzle_rot_mg": {
            "source": "ammorandom",
            "weapon": "RHS_M2_M1117"
        },
        "reloadanim": {
            "source": "reload",
            "weapon": "RHS_M2_M1117"
        },
        "revolving": {
            "source": "revolving",
            "weapon": "RHS_M2_M1117"
        },
        "shortlights_hide": {
            "animperiod": 1e-06,
            "initphase": 0,
            "source": "user"
        },
        "smoke_revolving_source": {
            "source": "revolving",
            "weapon": "rhsusf_weap_M257_8"
        },
        "zoom_handler": {
            "animperiod": 1,
            "initphase": 0,
            "source": "door"
        }
    },
    "antirollbarforcecoef": 0.5,
    "antirollbarforcelimit": 0.5,
    "antirollbarspeedmax": 50,
    "antirollbarspeedmin": 10,
    "armor": 150,
    "armorcrash0": [
        "A3/sounds_f/Vehicles/soft/noises/crash_vehicle_01",
        1,
        1,
        200
    ],
    "armorcrash1": [
        "A3/sounds_f/Vehicles/soft/noises/crash_vehicle_02",
        1,
        1,
        200
    ],
    "armorcrash2": [
        "A3/sounds_f/Vehicles/soft/noises/crash_vehicle_03",
        1,
        1,
        200
    ],
    "armorcrash3": [
        "A3/sounds_f/Vehicles/soft/noises/crash_vehicle_04",
        1,
        1,
        200
    ],
    "armorlights": 0.4,
    "armorstructural": 8,
    "artilleryscanner": 0,
    "artillerytarget": 0,
    "attendant": 0,
    "attenuationeffecttype": "CarAttenuation",
    "attributes": {
        "door_b": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open back doors",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "door_b"
        },
        "door_l": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open left door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "door_l"
        },
        "door_r": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open right door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "door_r"
        },
        "hatch_commander": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open commander hatch",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "hatch_commander"
        },
        "hatch_driver": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open driver hatch",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "hatch_driver"
        },
        "hatch_gunner": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open gunner hatch",
            "expression": "_this animateDoor ['%s',_value,true]",
            "property": "hatch_gunner"
        },
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        "rhs_hideduke": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "hide DUKE antennas",
            "expression": "_this animate ['DUKE_Hide',_value,true]",
            "property": "rhs_hideDUKE"
        }
    },
    "audible": 14,
    "author": "Cleggy",
    "autocenter": 1,
    "availableforsupporttypes": [],
    "brakedistance": 5,
    "brakeidlespeed": 2,
    "braketorque": 6000,
    "buildcrash0": [
        "A3/sounds_f/Vehicles/soft/noises/crash_building_01",
        1,
        1,
        200
    ],
    "buildcrash1": [
        "A3/sounds_f/Vehicles/soft/noises/crash_building_02",
        1,
        1,
        200
    ],
    "buildcrash2": [
        "A3/sounds_f/Vehicles/soft/noises/crash_building_03",
        1,
        1,
        200
    ],
    "buildcrash3": [
        "A3/sounds_f/Vehicles/soft/noises/crash_building_04",
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
    "camouflage": 2,
    "camshakecoef": 0.05,
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
        "rhs_M1117_passenger",
        "passenger_flatground_generic01",
        "passenger_low01",
        "passenger_flatground_crosslegs"
    ],
    "cargocaneject": 1,
    "cargocompartments": [
        "Compartment1"
    ],
    "cargodoors": [
        "door_r",
        "door_b",
        "door_l",
        "door_r"
    ],
    "cargogetinaction": [
        "GetInAMV_cargo"
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
        1
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
    "centrebias": 1.3,
    "changegearmineffectivity": [
        0.95,
        0,
        0.95,
        0.95,
        0.95,
        0.9,
        0.9,
        0.45
    ],
    "clutchstrength": 55,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "collisioneffect": "collisionEffect",
    "commandercansee": "2+4+16",
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
            -5.03,
            "N",
            0,
            "D1",
            3.49,
            "D2",
            1.86,
            "D3",
            1.41,
            "D4",
            1,
            "D5",
            0.75,
            "D6",
            0.6
        ],
        "moveoffgear": 1,
        "neutralstring": "N",
        "reversestring": "R",
        "transmissionratios": [
            "High",
            6.9
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
        "transportcountermeasurescomponent": {},
        "vehiclesystemsdisplaymanagercomponentleft": {
            "components": {
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent"
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
                },
                "vehiclecommanderdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                "vehicleprimarygunnerdisplay": {
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
                    "componenttype": "CrewDisplayComponent"
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
                },
                "vehiclecommanderdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                "vehicleprimarygunnerdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "EmptyDisplay",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        }
    },
    "cost": 600000,
    "countermeasureactivationradius": 2000,
    "countsforscoreboard": 1,
    "crew": "rhsusf_army_ocp_rifleman_m4",
    "crewcrashprotection": 0.15,
    "crewexplosionprotection": 0.999,
    "crewvulnerable": 1,
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "damage": {
        "mat": [
            "rhsusf/addons/rhsusf_m1117/data/m1117_tex1.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_tex1_damage.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_tex1_damage.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_armour.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_armour_damage.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_armour_damage.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_turret.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_turret_damage.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_turret_damage.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_wheel.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_wheel_damage.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/m1117_wheel_damage.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/periscope_int_damage.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/periscope_int_destroyed.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/periscope_int_destroyed.rvmat",
            "rhsusf/addons/rhsusf_m1117/data/glassz.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "a3/data_f/glass_veh_int.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat",
            "a3/data_f/glass_veh_armored_damage.rvmat"
        ],
        "tex": []
    },
    "damagefull": [],
    "damagehalf": [],
    "damageresistance": 0.03099,
    "damagetexdelay": 0,
    "dammagefull": [],
    "dammagehalf": [],
    "damperdamping": 0.1,
    "damperforce": 0.1,
    "dampersbumpcoef": 0,
    "dampersize": 0.1,
    "dampingratefullthrottle": 0.15,
    "dampingratezerothrottleclutchdisengaged": 0.35,
    "dampingratezerothrottleclutchengaged": 0.8,
    "destrtype": "DestructWreck",
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
    "displayname": "M1117 ASV (OD)",
    "dlc": "RHS_USAF",
    "driveoncomponent": [
        "Slide"
    ],
    "driveraction": "rhs_M1117_Driver",
    "drivercaneject": 1,
    "drivercansee": "2+4+16",
    "drivercompartments": "Compartment1",
    "driverdoor": "door_l",
    "driverforceoptics": 0,
    "driverinaction": "rhs_M1117_Driver",
    "driverlefthandanimname": "drivewheel",
    "driverleftleganimname": "",
    "driveropticscolor": [
        1,
        1,
        1,
        1
    ],
    "driveropticseffect": [],
    "driveropticsmodel": "rhsusf/addons/rhsusf_m1117/optics/driver_optic",
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
    "editorpreview": "rhsusf/addons/rhsusf_editorPreviews/data/rhsusf_M1117_O.paa",
    "editorsubcategory": "rhs_EdSubcat_mrap",
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
    "enablewatch": 0,
    "enginebrakecoef": 0.8,
    "engineer": 0,
    "enginelosses": 15,
    "enginemoi": 5,
    "enginepower": 194,
    "enginestartspeed": 1.5,
    "epeimpulsedamagecoef": 20,
    "eventhandlers": {
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        "rhs_m1117_eh": {
            "engine": "_this call rhs_fnc_engineCheckDamage",
            "getout": "_this call rhs_fnc_m1117_hatch",
            "handledamage": "_this call rhs_fnc_duke_destruction",
            "init": "(_this select 0) lockTurret [[1],true];(_this select 0) lockTurret [[2],true]",
            "postinit": "_this call rhs_fnc_reapplyTextures"
        }
    },
    "exhausts": {
        "exhaust": {
            "direction": "exhaust_dir",
            "effect": "ExhaustEffectMRAP_03",
            "position": "exhaust_pos"
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
        -9
    ],
    "faction": "rhs_faction_usarmy_d",
    "features": "",
    "featuretype": 0,
    "fireresistance": 10,
    "forcehidedriver": 0,
    "formationtime": 5,
    "formationx": 20,
    "formationz": 20,
    "frontbias": 1.3,
    "frontrearsplit": 0.5,
    "fuelcapacity": 35,
    "fuelconsumptionrate": 0.01,
    "fuelexplosionpower": 1,
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
    "getinaction": "GetInAMV_cargo",
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
    "gunnercansee": "2+4+16",
    "gunnerhasflares": 0,
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
        "camo6"
    ],
    "hiddenselectionsmaterials": [],
    "hiddenselectionstextures": [
        "rhsusf/addons/rhsusf_m1117/data/M1117_tex1_OD_co.paa",
        "rhsusf/addons/rhsusf_m1117/data/M1117_armour_od_co.paa",
        "rhsusf/addons/rhsusf_m1117/data/M1117_turret_od_co.paa",
        "rhsusf/addons/rhsusf_m1117/data/m1117_wheel_green_co.paa",
        "rhsusf/addons/rhsusf_hmmwv/textures/A2_parts_g_co.paa",
        "rhsusf/addons/rhsusf_m1a1/duke/data/duke_antennae_wd_co.paa"
    ],
    "hiddenunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "hideproxyincombat": 0,
    "hideunitinfo": 0,
    "hideweaponscargo": 1,
    "hideweaponsdriver": 1,
    "hideweaponsgunner": 1,
    "hitpoints": {
        "hitbody": {
            "armor": 0.8,
            "explosionshielding": 0.8,
            "material": -1,
            "minimalhit": 0.15,
            "name": "karoserie",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "zbytek"
        },
        "hitduke1": {
            "armor": 1,
            "explosionshielding": 0.01,
            "material": -1,
            "minimalhit": 0.15,
            "name": "duke1",
            "passthrough": 0,
            "radius": 0.15,
            "visual": ""
        },
        "hitduke2": {
            "armor": 1,
            "explosionshielding": 0.01,
            "material": -1,
            "minimalhit": 0.15,
            "name": "duke2",
            "passthrough": 0,
            "radius": 0.15,
            "visual": ""
        },
        "hitengine": {
            "armor": 1.8,
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
                "rhs_engine_smoke_small3": {
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "position": "engine_smoke4",
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
            "explosionshielding": 0.01,
            "material": -1,
            "minimalhit": 0.01,
            "name": "engine",
            "passthrough": 0,
            "radius": 0.15,
            "visual": "zbytek"
        },
        "hitfuel": {
            "armor": 4,
            "explosionshielding": 0.01,
            "material": -1,
            "minimalhit": 0.05,
            "name": "palivo",
            "passthrough": 0,
            "radius": 0.09,
            "visual": ""
        },
        "hitglass1": {
            "armor": 2.4,
            "explosionshielding": 1,
            "material": -1,
            "name": "glass1",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "glass1"
        },
        "hitglass2": {
            "armor": 2.4,
            "explosionshielding": 1,
            "material": -1,
            "name": "glass2",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "glass2"
        },
        "hitglass3": {
            "armor": 2.4,
            "explosionshielding": 1,
            "material": -1,
            "name": "glass3",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "glass3"
        },
        "hitglass4": {
            "armor": 2.4,
            "explosionshielding": 1,
            "material": -1,
            "name": "glass4",
            "passthrough": 0,
            "radius": 0.25,
            "visual": "glass4"
        },
        "hitglass5": {
            "armor": 2.4,
            "explosionshielding": 1,
            "material": -1,
            "name": "glass5",
            "passthrough": 0,
            "radius": 0.15,
            "visual": "glass5"
        },
        "hitglass6": {
            "armor": 2.4,
            "explosionshielding": 1,
            "material": -1,
            "name": "glass6",
            "passthrough": 0,
            "radius": 0.15,
            "visual": "glass6"
        },
        "hithull": {
            "armor": -350,
            "explosionshielding": 0.01,
            "minimalhit": -0.25,
            "name": "karoserie",
            "passthrough": 8,
            "radius": 0.22,
            "visual": "zbytek"
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
            "armor": -250,
            "armorcomponent": "wheel_1_2_damper",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": -0.025,
            "name": "wheel_1_2_steering",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "wheel_1_2_damage"
        },
        "hitlfwheel": {
            "armor": -250,
            "armorcomponent": "wheel_1_1_damper",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": -0.025,
            "name": "wheel_1_1_steering",
            "passthrough": 0,
            "radius": 0.3,
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
        "hitmainsight": {
            "armor": 1.2,
            "explosionshielding": 0.3,
            "material": -1,
            "name": "mainSight",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "mainSight"
        },
        "hitperiscope1": {
            "armor": 0.8,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope1",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope1"
        },
        "hitperiscope2": {
            "armor": 0.8,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope2",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope2"
        },
        "hitperiscope3": {
            "armor": 0.8,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope3",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope3"
        },
        "hitperiscope4": {
            "armor": 0.8,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope4",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope4"
        },
        "hitperiscope5": {
            "armor": 0.8,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope5",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope5"
        },
        "hitperiscope6": {
            "armor": 0.8,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope6",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope6"
        },
        "hitperiscope7": {
            "armor": 0.8,
            "explosionshielding": 0.5,
            "material": -1,
            "name": "periscope7",
            "passthrough": 0,
            "radius": 0.05,
            "visual": "periscope7"
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
            "armor": -250,
            "armorcomponent": "wheel_2_2_damper",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": -0.025,
            "name": "wheel_2_2_steering",
            "passthrough": 0,
            "radius": 0.3,
            "visual": "wheel_2_2_damage"
        },
        "hitrfwheel": {
            "armor": -250,
            "armorcomponent": "wheel_2_1_damper",
            "explosionshielding": 1,
            "material": -1,
            "minimalhit": -0.025,
            "name": "wheel_2_1_steering",
            "passthrough": 0,
            "radius": 0.3,
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
        }
    },
    "holdoffroadformation": 1,
    "htmax": 600,
    "htmin": 60,
    "hulldamagecauseexplosion": 1,
    "icon": "rhsusf/addons/rhsusf_m1117/data/UI/icon_m1117_ca.paa",
    "idlerpm": 1000,
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
    "insidesoundcoef": 0.9,
    "irscanground": 1,
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
        "libtextdesc": "M1117_Guardian ASV"
    },
    "limitedspeedcoef": 0.5,
    "lockdetectionsystem": 0,
    "longstiff": 15000,
    "magazines": [],
    "mapsize": 6,
    "markerlights": {},
    "maxdetectrange": 20,
    "maxfordingdepth": 0,
    "maxgforce": 3,
    "maximumload": 3000,
    "maxomega": 230.38,
    "maxspeed": 100,
    "memorypointcirculumreference": "circulumReference",
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
        "pos gunner",
        "pos cargo b",
        "pos cargo",
        "pos gunner"
    ],
    "memorypointsgetincargodir": [
        "pos gunner dir",
        "pos cargo b dir",
        "pos cargo dir",
        "pos gunner dir"
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
    "minealerticonrange": 200,
    "minfiretime": 20,
    "mingforce": 0.2,
    "minomega": 66,
    "mintotaldamagethreshold": 0.01,
    "model": "rhsusf/addons/rhsusf_m1117/blx_M1117",
    "namesound": "veh_vehicle_MRAP_s",
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
    "normalspeedforwardcoef": 0.7,
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
    "peaktorque": 1135,
    "picture": "rhsusf/addons/rhsusf_m1117/data/UI/picture_m1117_ca.paa",
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
        "maxturnhundred": 0.7,
        "turndecreaseconst": 5,
        "turndecreaselinear": 3,
        "turndecreasetime": 0,
        "turnincreaseconst": 0.1,
        "turnincreaselinear": 1,
        "turnincreasetime": 1
    },
    "portrait": "",
    "precisegetinout": 0,
    "precision": 15,
    "predictturnplan": 0.5,
    "predictturnsimul": 4.4,
    "preferroads": 0,
    "pulsationsound": {},
    "radartarget": 1,
    "radartargetsize": 1.2,
    "radartype": 8,
    "rearbias": 1.3,
    "redrpm": 2200,
    "reflectors": {
        "interior_light_1": {
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
                800,
                900,
                650
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "interior_light_1_dir",
            "flaremaxdistance": 5,
            "flaresize": 1,
            "hitpoint": "cabin_light",
            "innerangle": 90,
            "intensity": 4,
            "outerangle": 165,
            "position": "interior_light_1",
            "selection": "cabin_light",
            "size": 1,
            "useflare": 1
        },
        "interior_light_2": {
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
                800,
                900,
                650
            ],
            "conefadecoef": 1,
            "daylight": 0,
            "direction": "interior_light_2_dir",
            "flaremaxdistance": 5,
            "flaresize": 1,
            "hitpoint": "cabin_light",
            "innerangle": 90,
            "intensity": 4,
            "outerangle": 165,
            "position": "interior_light_2",
            "selection": "cabin_light",
            "size": 1,
            "useflare": 1
        },
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
            "direction": "konec L svetla",
            "flaresize": 1,
            "hitpoint": "L svetlo",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "L svetlo",
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
            "direction": "konec L svetla",
            "flaresize": 1,
            "hitpoint": "L svetlo",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "L svetlo",
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
                1900,
                1300,
                950
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
                1900,
                1300,
                950
            ],
            "conefadecoef": 51,
            "daylight": 0,
            "direction": "Light_L_Long_end",
            "flaremaxdistance": 750,
            "flaresize": 1.5,
            "hitpoint": "L svetlo",
            "innerangle": 50,
            "intensity": 1,
            "outerangle": 179,
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
                1900,
                1300,
                950
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
                1900,
                1300,
                950
            ],
            "conefadecoef": 51,
            "daylight": 0,
            "direction": "Light_R_Long_end",
            "flaremaxdistance": 750,
            "flaresize": 1.5,
            "hitpoint": "P svetlo",
            "innerangle": 50,
            "intensity": 1,
            "outerangle": 179,
            "position": "light_R_Long_flare",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 1
        },
        "right": {
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
            "direction": "konec P svetla",
            "flaresize": 1,
            "hitpoint": "P svetlo",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "P svetlo",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 0
        },
        "right2": {
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
            "direction": "konec P svetla",
            "flaresize": 1,
            "hitpoint": "P svetlo",
            "innerangle": 100,
            "intensity": 1,
            "outerangle": 179,
            "position": "P svetlo",
            "selection": "P svetlo",
            "size": 1,
            "useflare": 1
        }
    },
    "rendertargets": {
        "mirrorl": {
            "bboxes": [
                "PIP_1_TL",
                "PIP_1_TR",
                "PIP_1_BL",
                "PIP_1_BR"
            ],
            "cameraview1": {
                "fov": 0.35,
                "pointdirection": "PIP0_dir",
                "pointposition": "PIP0_pos",
                "renderquality": 2,
                "rendervisionmode": 4
            },
            "rendertarget": "rendertarget0"
        },
        "mirrorr": {
            "bboxes": [
                "PIP_2_TL",
                "PIP_2_TR",
                "PIP_2_BL",
                "PIP_2_BR"
            ],
            "cameraview1": {
                "fov": 0.35,
                "pointdirection": "PIP1_dir",
                "pointposition": "PIP1_pos",
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
    "rhs_duke_type": "rhsusf_duke",
    "rhs_hassmokecap": 1,
    "rhs_towingsystem": {
        "carrier": {
            "rhs_attachpoint": "",
            "rhs_attachpointpos": [
                0.02,
                -2.69,
                -1.12
            ],
            "rhs_maxcargomass": 1932
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
    "scopecurator": 2,
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
    "simulation": "carx",
    "slingloadcargomemorypoints": [
        "SlingLoadCargo1",
        "SlingLoadCargo2",
        "SlingLoadCargo3",
        "SlingLoadCargo4"
    ],
    "slingloadcargomemorypointsdir": [],
    "slownspeedforwardcoef": 0.55,
    "slowspeedforwardcoef": 0.3,
    "smokelauncherangle": 160,
    "smokelaunchergrenadecount": 4,
    "smokelauncheronturret": 1,
    "smokelaunchervelocity": 14,
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
        "A3/sounds_f/dummysound",
        1,
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
        1,
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
        "A3/Sounds_F/vehicles/soft/Truck_02/ext_stop",
        0.707946,
        1,
        200
    ],
    "soundengineoffint": [
        "A3/Sounds_F/vehicles/soft/Truck_02/int_stop",
        0.707946,
        1
    ],
    "soundengineonext": [
        "A3/Sounds_F/vehicles/soft/Truck_02/ext_start",
        0.707946,
        1,
        200
    ],
    "soundengineonint": [
        "A3/Sounds_F/vehicles/soft/Truck_02/int_start",
        0.707946,
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
        "A3/Sounds_F/vehicles/soft/MRAP_03/getin",
        0.562341,
        1
    ],
    "soundgetout": [
        "A3/Sounds_F/vehicles/soft/MRAP_03/getout",
        0.562341,
        1,
        40
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
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(610/\t3000),(1200/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_engine_01",
                0.630957,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t3000) factor[(620/\t3000),(820/\t3000)])\t*\t((rpm/\t3000) factor[(1200/\t3000),(1000/\t3000)]))"
        },
        "engine1_ext": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1000/\t3000),(1500/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_engine_02",
                0.707946,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t3000) factor[(950/\t3000),(1150/\t3000)])\t*\t((rpm/\t3000) factor[(1500/\t3000),(1300/\t3000)]))"
        },
        "engine1_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1000/\t3000),(1500/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_engine_02",
                0.501187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t3000) factor[(950/\t3000),(1150/\t3000)])\t*\t((rpm/\t3000) factor[(1500/\t3000),(1300/\t3000)]))"
        },
        "engine1_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1000/\t3000),(1500/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_exhaust_02",
                1.41254,
                1,
                350
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(950/\t3000),(1150/\t3000)])\t*\t((rpm/\t3000) factor[(1500/\t3000),(1300/\t3000)]))"
        },
        "engine1_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1000/\t3000),(1500/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_exhaust_02",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(950/\t3000),(1150/\t3000)])\t*\t((rpm/\t3000) factor[(1500/\t3000),(1300/\t3000)]))"
        },
        "engine2_ext": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1300/\t3000),(1850/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_engine_03",
                0.794328,
                1,
                250
            ],
            "volume": "engineOn*camPos*(((rpm/\t3000) factor[(1260/\t3000),(1500/\t3000)])\t*\t((rpm/\t3000) factor[(1850/\t3000),(1600/\t3000)]))"
        },
        "engine2_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1300/\t3000),(1850/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_engine_03",
                0.501187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t3000) factor[(1260/\t3000),(1500/\t3000)])\t*\t((rpm/\t3000) factor[(1850/\t3000),(1600/\t3000)]))"
        },
        "engine2_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1300/\t3000),(1850/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_exhaust_03",
                1.58489,
                1,
                400
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(1260/\t3000),(1500/\t3000)])\t*\t((rpm/\t3000) factor[(1850/\t3000),(1600/\t3000)]))"
        },
        "engine2_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1300/\t3000),(1850/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_exhaust_03",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(1260/\t3000),(1500/\t3000)])\t*\t((rpm/\t3000) factor[(1850/\t3000),(1600/\t3000)]))"
        },
        "engine3_ext": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1600/\t3000),(2200/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_engine_04",
                1.12202,
                1,
                300
            ],
            "volume": "engineOn*camPos*(((rpm/\t3000) factor[(1550/\t3000),(1800/\t3000)])\t*\t((rpm/\t3000) factor[(2200/\t3000),(1950/\t3000)]))"
        },
        "engine3_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1600/\t3000),(2200/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_engine_04",
                0.562341,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t3000) factor[(1550/\t3000),(1800/\t3000)])\t*\t((rpm/\t3000) factor[(2200/\t3000),(1950/\t3000)]))"
        },
        "engine3_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1600/\t3000),(2200/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_exhaust_04",
                1.99526,
                1,
                450
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(1550/\t3000),(1800/\t3000)])\t*\t((rpm/\t3000) factor[(2200/\t3000),(1950/\t3000)]))"
        },
        "engine3_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(1600/\t3000),(2200/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_exhaust_04",
                0.707946,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(1550/\t3000),(1800/\t3000)])\t*\t((rpm/\t3000) factor[(2200/\t3000),(1950/\t3000)]))"
        },
        "engine4_ext": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(2000/\t3000),(2600/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_engine_05",
                1.41254,
                1,
                350
            ],
            "volume": "engineOn*camPos*(((rpm/\t3000) factor[(1900/\t3000),(2150/\t3000)])\t*\t((rpm/\t3000) factor[(2600/\t3000),(2300/\t3000)]))"
        },
        "engine4_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(2000/\t3000),(2600/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_engine_05",
                0.562341,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t3000) factor[(1900/\t3000),(2150/\t3000)])\t*\t((rpm/\t3000) factor[(2600/\t3000),(2300/\t3000)]))"
        },
        "engine4_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(2000/\t3000),(2600/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_exhaust_05",
                1.99526,
                1,
                450
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(1900/\t3000),(2150/\t3000)])\t*\t((rpm/\t3000) factor[(2600/\t3000),(2300/\t3000)]))"
        },
        "engine4_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(2000/\t3000),(2600/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_exhaust_05",
                0.794328,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(1900/\t3000),(2150/\t3000)])\t*\t((rpm/\t3000) factor[(2600/\t3000),(2300/\t3000)]))"
        },
        "engine5_ext": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(2300/\t3000),(3000/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_engine_06",
                1.77828,
                1,
                400
            ],
            "volume": "engineOn*camPos*((rpm/\t3000) factor[(2300/\t3000),(2700/\t3000)])"
        },
        "engine5_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(2300/\t3000),(3000/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_engine_06",
                0.630957,
                1
            ],
            "volume": "engineOn*(1-camPos)*((rpm/\t3000) factor[(2300/\t3000),(2700/\t3000)])"
        },
        "engine5_thrust_ext": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(2300/\t3000),(3000/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_exhaust_06",
                2.23872,
                1,
                500
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/\t3000) factor[(2300/\t3000),(2700/\t3000)])"
        },
        "engine5_thrust_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(2300/\t3000),(3000/\t3000)])*0.1",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_exhaust_06",
                1,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/\t3000) factor[(2300/\t3000),(2700/\t3000)])"
        },
        "engine_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(610/\t3000),(1200/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_engine_01",
                0.446684,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t3000) factor[(620/\t3000),(820/\t3000)])\t*\t((rpm/\t3000) factor[(1200/\t3000),(1000/\t3000)]))"
        },
        "enginethrust": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(610/\t3000),(1200/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_exhaust_01",
                1.25893,
                1,
                300
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(620/\t3000),(820/\t3000)])\t*\t((rpm/\t3000) factor[(1200/\t3000),(1000/\t3000)]))"
        },
        "enginethrust_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(610/\t3000),(1200/\t3000)])*0.2",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_exhaust_01",
                0.562341,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(620/\t3000),(820/\t3000)])\t*\t((rpm/\t3000) factor[(1200/\t3000),(1000/\t3000)]))"
        },
        "idle_ext": {
            "frequency": "0.95\t+\t((rpm/\t3000) factor[(100/\t3000),(800/\t3000)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_engine_00",
                0.562341,
                1,
                200
            ],
            "volume": "engineOn*camPos*(((rpm/\t3000) factor[(10/\t3000),(50/\t3000)])\t*\t((rpm/\t3000) factor[(800/\t3000),(600/\t3000)]))"
        },
        "idle_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(100/\t3000),(800/\t3000)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_engine_00",
                0.398107,
                1
            ],
            "volume": "engineOn*(1-camPos)*(((rpm/\t3000) factor[(10/\t3000),(50/\t3000)])\t*\t((rpm/\t3000) factor[(800/\t3000),(600/\t3000)]))"
        },
        "idlethrust": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(100/\t3000),(800/\t3000)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/ext_exhaust_00",
                1,
                1,
                250
            ],
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(10/\t3000),(50/\t3000)])\t*\t((rpm/\t3000) factor[(800/\t3000),(600/\t3000)]))"
        },
        "idlethrust_int": {
            "frequency": "0.8\t+\t((rpm/\t3000) factor[(100/\t3000),(800/\t3000)])*0.15",
            "sound": [
                "A3/Sounds_F/vehicles/soft/Truck_02/int_exhaust_00",
                0.501187,
                1
            ],
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/\t3000) factor[(10/\t3000),(50/\t3000)])\t*\t((rpm/\t3000) factor[(800/\t3000),(600/\t3000)]))"
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
                "veh_vehicle_MRAP_p"
            ],
            "speechsingular": [
                "veh_vehicle_MRAP_s"
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
    "steeraheadplan": 0.2,
    "steeraheadsimul": 0.55,
    "supplyradius": -1,
    "switchtime": 0.5,
    "tbody": 150,
    "terraincoef": 2,
    "textplural": "MRAPs",
    "textsingular": "MRAP",
    "texturelist": [],
    "texturesources": {
        "desert": {
            "displayname": "Desert",
            "factions": [
                "rhs_faction_usarmy_wd",
                "rhs_faction_usarmy_d"
            ],
            "textures": [
                "rhsusf/addons/rhsusf_m1117/data/m1117_tex1_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/m1117_armour_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/m1117_turret_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/m1117_wheel_co.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/A2_parts_D_co.paa",
                "rhsusf/addons/rhsusf_m1a1/duke/data/duke_antennae_d_co.paa"
            ]
        },
        "olive": {
            "displayname": "OD",
            "factions": [
                "rhs_faction_usarmy_wd",
                "rhs_faction_usarmy_d"
            ],
            "textures": [
                "rhsusf/addons/rhsusf_m1117/data/M1117_tex1_OD_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/M1117_armour_od_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/M1117_turret_od_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/m1117_wheel_green_co.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/A2_parts_g_co.paa",
                "rhsusf/addons/rhsusf_m1a1/duke/data/duke_antennae_wd_co.paa"
            ]
        },
        "standard": {
            "displayname": "Woodland",
            "factions": [
                "rhs_faction_usarmy_wd",
                "rhs_faction_usarmy_d"
            ],
            "textures": [
                "rhsusf/addons/rhsusf_m1117/data/m1117_tex1_green_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/m1117_armour_green_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/m1117_turret_green_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/m1117_wheel_green_co.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/A2_parts_g_co.paa",
                "rhsusf/addons/rhsusf_m1a1/duke/data/duke_antennae_wd_co.paa"
            ]
        },
        "un": {
            "displayname": "UN",
            "factions": [
                "rhs_faction_usarmy_wd",
                "rhs_faction_usarmy_d"
            ],
            "textures": [
                "rhsusf/addons/rhsusf_m1117/data/m1117_tex1_un_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/m1117_armour_un_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/m1117_turret_un_co.paa",
                "rhsusf/addons/rhsusf_m1117/data/m1117_wheel_un_co.paa",
                "rhsusf/addons/rhsusf_hmmwv/textures/A2_parts_D_co.paa",
                "rhsusf/addons/rhsusf_m1a1/duke/data/duke_antennae_d_co.paa"
            ]
        }
    },
    "tf_haslrradio_api": 1,
    "tf_isolatedamount_api": 0.2,
    "tf_radiotype_api": "tf_rt1523g",
    "threat": [
        1,
        0.8,
        0.3
    ],
    "thrustdelay": 0.8,
    "torquecurve": [
        [
            0.454545,
            0.63348
        ],
        [
            0.5,
            0.856388
        ],
        [
            0.590909,
            0.987665
        ],
        [
            0.681818,
            1
        ],
        [
            0.772727,
            0.959471
        ],
        [
            0.863636,
            0.864317
        ],
        [
            0.954545,
            0.781498
        ],
        [
            1.05409,
            0
        ]
    ],
    "tracksspeed": 0,
    "transportammo": 0,
    "transportbackpacks": {
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 2
        }
    },
    "transportfuel": 0,
    "transportitems": {
        "_xx_binoculars": {
            "count": 1,
            "name": "Binocular"
        },
        "_xx_firstaidkit": {
            "count": 6,
            "name": "FirstAidKit"
        },
        "_xx_medikit": {
            "count": 1,
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
            "count": 4,
            "magazine": "rhs_mag_m18_green"
        },
        "_xx_rhs_mag_m18_red": {
            "count": 4,
            "magazine": "rhs_mag_m18_red"
        },
        "_xx_rhs_mag_m433_hedp": {
            "count": 12,
            "magazine": "rhs_mag_M433_HEDP"
        },
        "_xx_rhs_mag_m662_red": {
            "count": 4,
            "magazine": "rhs_mag_M662_red"
        },
        "_xx_rhs_mag_m67": {
            "count": 8,
            "magazine": "rhs_mag_m67"
        },
        "_xx_rhsusf_100rnd_556x45_soft_pouch": {
            "count": 8,
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch"
        },
        "_xx_rhsusf_8rnd_00buck": {
            "count": 8,
            "magazine": "rhsusf_8Rnd_00Buck"
        }
    },
    "transportmaxbackpacks": 2,
    "transportmaxmagazines": 90,
    "transportmaxweapons": 12,
    "transportrepair": 0,
    "transportsoldier": 4,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "transportweapons": {
        "_xx_rhs_weap_m136_hedp": {
            "count": 2,
            "weapon": "rhs_weap_M136_hedp"
        },
        "_xx_rhs_weap_m590_8rd": {
            "count": 1,
            "weapon": "rhs_weap_M590_8RD"
        },
        "_xx_weap": {
            "count": 1,
            "weapon": "rhs_weap_m4_carryhandle"
        }
    },
    "turncoef": 3,
    "turrets": {
        "mainturret": {
            "aggregatereflectors": [],
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "allowtablock": 0,
            "animationsourcebody": "MainTurret",
            "animationsourcecamelev": "camElev",
            "animationsourcegun": "MainGun",
            "animationsourcehatch": "hatchGunner",
            "armorlights": 0.1,
            "body": "MainTurret",
            "caneject": 1,
            "canhidegunner": 0,
            "canusescanners": 0,
            "castgunnershadow": 0,
            "commanding": -1,
            "components": {
                "vehiclesystemsdisplaymanagercomponentleft": {
                    "components": {
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent"
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
                        },
                        "vehiclecommanderdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
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
                            "componenttype": "CrewDisplayComponent"
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
                        },
                        "vehiclecommanderdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "defaultdisplay": "EmptyDisplay",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,\t((safezoneX + safezoneW) - (\t\t(10 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * \t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,\t(safezoneY + safezoneH - 21 * \t\t\t(\t\t\t(\t\t\t((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "disablesoundattenuation": 0,
            "discretedistance": [],
            "discretedistanceinitindex": 0,
            "dontcreateai": 0,
            "ejectdeadgunner": 0,
            "forcehidegunner": 0,
            "forcenvg": 0,
            "gun": "MainGun",
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
            "gunneraction": "rhs_M1117_Gunner",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "door_r",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 0,
            "gunnergetinaction": "GetInAMV_cargo",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "rhs_M1117_Gunner",
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
            "gunneropticsmodel": "A3/weapons_f/reticle/Optics_Gunner_02_F",
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
            "gunnertype": "rhsusf_army_ucp_grenadier",
            "gunnerusespilotview": 0,
            "hasgunner": 1,
            "hideweaponsgunner": 1,
            "hitpoints": {
                "hitgun": {
                    "armor": 1.3,
                    "explosionshielding": 0.5,
                    "material": -1,
                    "name": "zbran",
                    "passthrough": 0,
                    "radius": 0.15,
                    "visual": "-"
                },
                "hitturret": {
                    "armor": 1.5,
                    "explosionshielding": 0.5,
                    "material": -1,
                    "name": "vez",
                    "passthrough": 0,
                    "radius": 0.15,
                    "visual": "otocvez"
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
            "magazines": [
                "rhs_mag_200rnd_127x99_mag_Tracer_Red",
                "rhs_mag_200rnd_127x99_mag_Tracer_Red",
                "rhs_mag_200rnd_127x99_mag_Tracer_Red",
                "rhs_mag_200rnd_127x99_mag_Tracer_Red",
                "rhs_mag_200rnd_127x99_mag_Tracer_Red",
                "RHS_96Rnd_40mm_MK19_M430A1",
                "RHS_96Rnd_40mm_MK19_M430A1",
                "RHS_96Rnd_40mm_MK19_M430A1",
                "RHS_96Rnd_40mm_MK19_M430A1",
                "RHS_96Rnd_40mm_MK19_M430A1",
                "RHS_96Rnd_40mm_MK19_M430A1",
                "RHS_96Rnd_40mm_MK19_M1001",
                "rhsusf_mag_L8A3_8"
            ],
            "maxcamelev": 90,
            "maxelev": 60,
            "maxhorizontalrotspeed": 1.2,
            "maxoutelev": 20,
            "maxoutturn": 60,
            "maxturn": 360,
            "maxverticalrotspeed": 1.2,
            "memorypointgun": "kulas",
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
            "minelev": -5,
            "minoutelev": -4,
            "minoutturn": -60,
            "minturn": -360,
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "opticsin": {
                "narrow": {
                    "gunneropticsmodel": "rhsusf/addons/rhsusf_m1117/optics/rhs_m36_narrow",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.1,
                    "maxanglex": "+30",
                    "maxangley": "+100",
                    "maxfov": 0.1,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.1,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "thermalmode": [
                        2,
                        3
                    ],
                    "visionmode": [
                        "Normal",
                        "TI"
                    ]
                },
                "periscope": {
                    "gunneropticsmodel": "rhsusf/addons/rhsusf_optics/data/rhs_periscope_BISType",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.466667,
                    "maxanglex": "+30",
                    "maxangley": "+100",
                    "maxfov": 0.466667,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.466667,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "thermalmode": [
                        2,
                        3
                    ],
                    "visionmode": [
                        "Normal"
                    ]
                },
                "wide": {
                    "gunneropticsmodel": "rhsusf/addons/rhsusf_m1117/optics/rhs_m36_wide",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.233333,
                    "maxanglex": "+30",
                    "maxangley": "+100",
                    "maxfov": 0.233333,
                    "maxmovex": 0,
                    "maxmovey": 0,
                    "maxmovez": 0,
                    "minanglex": -30,
                    "minangley": -100,
                    "minfov": 0.233333,
                    "minmovex": 0,
                    "minmovey": 0,
                    "minmovez": 0,
                    "thermalmode": [
                        2,
                        3
                    ],
                    "visionmode": [
                        "Normal",
                        "TI"
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
                "gunlight": {
                    "ambient": [
                        5,
                        5,
                        5
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 150,
                        "hardlimitstart": 50,
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
                    "daylight": 1,
                    "direction": "konec t svetla",
                    "flaresize": 0.25,
                    "hitpoint": "t svetlo",
                    "innerangle": 10,
                    "intensity": 1,
                    "outerangle": 12,
                    "position": "t svetlo",
                    "selection": "t svetlo",
                    "size": 0.1,
                    "useflare": 1
                },
                "gunlight_flare": {
                    "ambient": [
                        5,
                        5,
                        5
                    ],
                    "attenuation": {
                        "constant": 0,
                        "hardlimitend": 0.15,
                        "hardlimitstart": 0.5,
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
                    "daylight": 1,
                    "direction": "konec t svetla",
                    "flaresize": 1.25,
                    "hitpoint": "t svetlo",
                    "innerangle": 10,
                    "intensity": 1,
                    "outerangle": 160,
                    "position": "t svetlo",
                    "selection": "t svetlo",
                    "size": 0.1,
                    "useflare": 1
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
                "A3/sounds_f/dummysound",
                "db-35",
                1,
                15
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
            "turrets": {
                "commanderoptics": {
                    "aggregatereflectors": [],
                    "allowlauncherin": 0,
                    "allowlauncherout": 0,
                    "allowtablock": 0,
                    "animationsourcebody": "obsTurret",
                    "animationsourcecamelev": "",
                    "animationsourcegun": "",
                    "animationsourcehatch": "",
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
                    "gun": "",
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
                    "gunneraction": "rhs_M1117_Commander",
                    "gunnercompartments": "Compartment1",
                    "gunnerdoor": "door_r",
                    "gunnerfirealsoininternalcamera": 1,
                    "gunnerforceoptics": 0,
                    "gunnergetinaction": "GetInAMV_cargo",
                    "gunnergetoutaction": "GetOutLow",
                    "gunnerinaction": "rhs_M1117_Commander",
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
                    "hitpoints": {},
                    "ingunnermayfire": 1,
                    "initcamelev": 0,
                    "initelev": 0,
                    "initoutelev": 0,
                    "initoutturn": 0,
                    "initturn": 0,
                    "iscopilot": 0,
                    "lockwhendriverout": 0,
                    "lockwhenvehiclespeed": -1,
                    "lodturnedin": 1100,
                    "lodturnedout": 1100,
                    "magazines": [
                        "rhsusf_mag_duke"
                    ],
                    "maxcamelev": 90,
                    "maxelev": 20,
                    "maxhorizontalrotspeed": 0.5,
                    "maxoutelev": 20,
                    "maxoutturn": 60,
                    "maxturn": 10,
                    "maxverticalrotspeed": 0.5,
                    "memorypointgun": "",
                    "memorypointgunneroptics": "gunnerview",
                    "memorypointgunneroutoptics": "gunnerview",
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
                    "minturn": -10,
                    "missilebeg": "spice rakety",
                    "missileend": "konec rakety",
                    "opticsin": {
                        "narrow": {
                            "gunneropticsmodel": "rhsusf/addons/rhsusf_m1117/optics/rhs_m36_narrow_com",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": 0.1,
                            "maxanglex": "+30",
                            "maxangley": "+100",
                            "maxfov": 0.1,
                            "maxmovex": 0,
                            "maxmovey": 0,
                            "maxmovez": 0,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": 0.1,
                            "minmovex": 0,
                            "minmovey": 0,
                            "minmovez": 0,
                            "thermalmode": [
                                2,
                                3
                            ],
                            "visionmode": [
                                "Normal",
                                "TI"
                            ]
                        },
                        "wide": {
                            "gunneropticsmodel": "rhsusf/addons/rhsusf_m1117/optics/rhs_m36_wide_com",
                            "initanglex": 0,
                            "initangley": 0,
                            "initfov": 0.233333,
                            "maxanglex": "+30",
                            "maxangley": "+100",
                            "maxfov": 0.233333,
                            "maxmovex": 0,
                            "maxmovey": 0,
                            "maxmovez": 0,
                            "minanglex": -30,
                            "minangley": -100,
                            "minfov": 0.233333,
                            "minmovex": 0,
                            "minmovey": 0,
                            "minmovez": 0,
                            "thermalmode": [
                                2,
                                3
                            ],
                            "visionmode": [
                                "Normal",
                                "TI"
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
                        "A3/sounds_f/dummysound",
                        0.01,
                        1,
                        10
                    ],
                    "stabilizedinaxes": 0,
                    "startengine": 0,
                    "turnin": {
                        "turnoffset": 0
                    },
                    "turnout": {
                        "turnoffset": 0
                    },
                    "turretcansee": 0,
                    "turretfollowfreelook": 0,
                    "turretinfotype": "RHS_RscM1117_Commander",
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
                        "initfov": 0.4,
                        "maxanglex": "+30",
                        "maxangley": "+100",
                        "maxfov": 0.4,
                        "maxmovex": 0,
                        "maxmovey": 0,
                        "maxmovez": 0,
                        "minanglex": -30,
                        "minangley": -100,
                        "minfov": 0.2,
                        "minmovex": 0,
                        "minmovey": 0,
                        "minmovez": 0,
                        "thermalmode": [
                            2,
                            3
                        ],
                        "visionmode": [
                            "Normal",
                            "TI"
                        ]
                    },
                    "weapons": [
                        "rhsusf_weap_duke"
                    ]
                }
            },
            "turretspec": {
                "showheadphones": 0
            },
            "viewgunner": {
                "initanglex": 5,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": "+85",
                "maxangley": "+150",
                "maxfov": 0.7,
                "minanglex": -60,
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
                "initfov": 0.4,
                "maxanglex": "+30",
                "maxangley": "+100",
                "maxfov": 0.4,
                "maxmovex": 0,
                "maxmovey": 0,
                "maxmovez": 0,
                "minanglex": -30,
                "minangley": -100,
                "minfov": 0.2,
                "minmovex": 0,
                "minmovey": 0,
                "minmovez": 0,
                "thermalmode": [
                    2,
                    3
                ],
                "visionmode": [
                    "Normal",
                    "TI"
                ]
            },
            "weapons": [
                "RHS_M2_M1117",
                "RHS_MK19",
                "rhsusf_weap_M257_8"
            ]
        },
        "mainturret2_out": {
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
            "gunneraction": "vehicle_turnout_1",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "vehicle_turnout_1",
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
            "lodturnedin": 0,
            "lodturnedout": 0,
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
            "personturretaction": "vehicle_turnout_1",
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
        "mainturret_out": {
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
            "gunneraction": "vehicle_turnout_2",
            "gunnercompartments": "Compartment3",
            "gunnerdoor": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunnerforceoptics": 1,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerinaction": "vehicle_turnout_2",
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
            "lodturnedin": 0,
            "lodturnedout": 0,
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
            "personturretaction": "vehicle_turnout_2",
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
        }
    },
    "type": 1,
    "typicalcargo": [
        "Soldier"
    ],
    "uavhacker": 0,
    "unitinfotype": "RHS_RscUnitInfoM1117",
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
            "statement": "[this,1] call rhsusf_fnc_carLightToggle"
        },
        "hatch_commander": {
            "condition": "(player == commander this)",
            "default": 1,
            "displayname": "Turn Out",
            "onlyforplayer": 1,
            "position": "",
            "radius": 20,
            "shortcut": "turnOut",
            "showwindow": 0,
            "statement": "[this,'hatch_commander',[[0,0],[2]],0] spawn rhs_fnc_m1117_turnOut"
        },
        "hatch_commander_in": {
            "condition": "this turretUnit [2] isEqualTo (call rhsusf_fnc_findPlayer)",
            "default": 1,
            "displayname": "Turn In",
            "onlyforplayer": 1,
            "position": "",
            "radius": 20,
            "shortcut": "turnIn",
            "showwindow": 0,
            "statement": "[this,'hatch_commander',[[0,0],[2]],1] spawn rhs_fnc_m1117_turnOut"
        },
        "hatch_driver": {
            "condition": "(player == driver this)",
            "default": 1,
            "displayname": "Open/Close roof hatch",
            "onlyforplayer": 1,
            "position": "",
            "radius": 20,
            "shortcut": "turnOut",
            "showwindow": 0,
            "statement": "this animateDoor ['hatch_driver',abs((this doorPhase 'hatch_driver')-1)]"
        },
        "hatch_gunner": {
            "condition": "(player == gunner this)",
            "default": 1,
            "displayname": "Turn Out",
            "onlyforplayer": 1,
            "position": "",
            "radius": 20,
            "shortcut": "turnOut",
            "showwindow": 0,
            "statement": "[this,'hatch_gunner',[[0],[1]],0] spawn rhs_fnc_m1117_turnOut"
        },
        "hatch_gunner_in": {
            "condition": "this turretUnit [1] isEqualTo (call rhsusf_fnc_findPlayer)",
            "default": 1,
            "displayname": "Turn In",
            "onlyforplayer": 1,
            "position": "",
            "radius": 20,
            "shortcut": "turnIn",
            "showwindow": 0,
            "statement": "[this,'hatch_gunner',[[0],[1]],1] spawn rhs_fnc_m1117_turnOut"
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
            "statement": "[this,0] call rhsusf_fnc_carLightToggle"
        }
    },
    "vehicleclass": "rhs_vehclass_MRAP",
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
    "viewgunnershadow": 1,
    "viewoptics": {
        "initanglex": 0,
        "initangley": 0,
        "initfov": 0.8,
        "maxanglex": 30,
        "maxangley": 90,
        "maxfov": 0.8,
        "maxmovex": 0,
        "maxmovey": 0,
        "maxmovez": 0,
        "minanglex": -45,
        "minangley": -90,
        "minfov": 0.8,
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
    "viewpilot": {
        "initanglex": -4.5,
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
    "visualtarget": 1,
    "visualtargetsize": 1,
    "waterangulardampingcoef": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 20,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterppinvehicle": 1,
    "waterresistance": 1,
    "waterresistancecoef": 0.3,
    "waterspeedfactor": 0.1,
    "weapons": [
        "TruckHorn"
    ],
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + \t\t4",
    "weaponsgroup3": "8 + \t16 + \t32",
    "weaponsgroup4": "64 + \t\t128",
    "weaponslots": 0,
    "wheelcircumference": 3.65671,
    "wheeldamageradiuscoef": 0.95,
    "wheeldamagethreshold": 0.7,
    "wheeldestroyradiuscoef": 0.45,
    "wheeldestroythreshold": 0.99,
    "wheelmask": "wheel_X_X",
    "wheels": {
        "lf": {
            "bonename": "wheel_1_1",
            "boundary": "wheel_1_1_bound",
            "center": "wheel_1_1_axis",
            "dampingrate": 1,
            "dampingratedamaged": 1.5,
            "dampingratedestroyed": 1000,
            "dampingrateinair": 1,
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
            "latstiffx": 35,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 13000,
            "mass": 80,
            "maxbraketorque": 26000,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "maxhandbraketorque": 0,
            "moi": 14.4,
            "side": "left",
            "springdamperrate": 17000,
            "springstrength": 178578,
            "sprungmass": -1,
            "steering": 1,
            "suspforceapppointoffset": "wheel_1_1_axis",
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_1_axis",
            "width": 0.35
        },
        "lr": {
            "bonename": "wheel_1_2",
            "boundary": "wheel_1_2_bound",
            "center": "wheel_1_2_axis",
            "dampingrate": 1,
            "dampingratedamaged": 1.5,
            "dampingratedestroyed": 1000,
            "dampingrateinair": 1,
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
            "latstiffx": 35,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 13000,
            "mass": 80,
            "maxbraketorque": 26000,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "maxhandbraketorque": 40000,
            "moi": 14.4,
            "side": "left",
            "springdamperrate": 17000,
            "springstrength": 178578,
            "sprungmass": -1,
            "steering": 0,
            "suspforceapppointoffset": "wheel_1_2_axis",
            "susptraveldirection": [
                -0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_1_2_axis",
            "width": 0.35
        },
        "rf": {
            "bonename": "wheel_2_1",
            "boundary": "wheel_2_1_bound",
            "center": "wheel_2_1_axis",
            "dampingrate": 1,
            "dampingratedamaged": 1.5,
            "dampingratedestroyed": 1000,
            "dampingrateinair": 1,
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
            "latstiffx": 35,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 13000,
            "mass": 80,
            "maxbraketorque": 26000,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "maxhandbraketorque": 0,
            "moi": 14.4,
            "side": "right",
            "springdamperrate": 17000,
            "springstrength": 178578,
            "sprungmass": -1,
            "steering": 1,
            "suspforceapppointoffset": "wheel_2_1_axis",
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_1_axis",
            "width": 0.35
        },
        "rr": {
            "bonename": "wheel_2_2",
            "boundary": "wheel_2_2_bound",
            "center": "wheel_2_2_axis",
            "dampingrate": 1,
            "dampingratedamaged": 1.5,
            "dampingratedestroyed": 1000,
            "dampingrateinair": 1,
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
            "latstiffx": 35,
            "latstiffy": 180,
            "longitudinalstiffnessperunitgravity": 13000,
            "mass": 80,
            "maxbraketorque": 26000,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "maxhandbraketorque": 40000,
            "moi": 14.4,
            "side": "right",
            "springdamperrate": 17000,
            "springstrength": 178578,
            "sprungmass": -1,
            "steering": 0,
            "suspforceapppointoffset": "wheel_2_2_axis",
            "susptraveldirection": [
                0.125,
                -1,
                0
            ],
            "tireforceapppointoffset": "wheel_2_2_axis",
            "width": 0.35
        }
    },
    "windsockexist": 0,
    "woodcrash0": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_01",
        1,
        1,
        200
    ],
    "woodcrash1": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_02",
        1,
        1,
        200
    ],
    "woodcrash2": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_03",
        1,
        1,
        200
    ],
    "woodcrash3": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_04",
        1,
        1,
        200
    ],
    "woodcrash4": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_05",
        1,
        1,
        200
    ],
    "woodcrash5": [
        "A3/sounds_f/Vehicles/soft/noises/crash_mix_wood_06",
        1,
        1,
        200
    ]
}