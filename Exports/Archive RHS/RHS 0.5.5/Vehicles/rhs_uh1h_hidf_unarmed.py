rhs_uh1h_hidf_unarmed = {
    "editorpreview": "rhsgref|addons|rhsgref_editorPreviews|data|rhs_uh1h_hidf_unarmed.paa",
    "author": "Red Hammer Studios",
    "forceingarage": 1,
    "displayname": "UH-1H Unarmed",
    "cargoaction": ["passenger_apc_narrow_generic02","passenger_apc_narrow_generic02","passenger_generic02_foldhands","passenger_generic01_leanleft","passenger_flatground_generic02","passenger_flatground_leanleft","Heli_Light_02_cargo","Heli_Light_02_cargo"],
    "transportsoldier": 8,
    "cargoproxyindexes": [1,2,3,4,5,6,9,10],
    "getinproxyorder": [2,3,1,4,5,6,7,8,9,10],
    # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|AnimationSources|Hide_mid_doors [Indent level: 2]
        "hide_mid_doors": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|AnimationSources|Hide_guns [Indent level: 2],
        "hide_guns": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 1
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|door_pilot [Indent level: 2],
        "door_pilot": {
            "source": "door",
            "animperiod": 0.8,
            "initphase": 0,
            "sound": "MetalDoorsSound",
            "soundposition": "axis_door_pilot"
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|door_copilot [Indent level: 2],
        "door_copilot": {
            "soundposition": "axis_door_copilot",
            "source": "door",
            "animperiod": 0.8,
            "initphase": 0,
            "sound": "MetalDoorsSound"
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|rightturretbase [Indent level: 2],
        "rightturretbase": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|rightturretgun [Indent level: 2],
        "rightturretgun": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|leftturretgun [Indent level: 2],
        "leftturretgun": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|leftturretbase [Indent level: 2],
        "leftturretbase": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|close_cargo_doors [Indent level: 2],
        "close_cargo_doors": {
            "source": "door",
            "sound": "RollDoorsSound",
            "soundposition": "door_sounds",
            "animperiod": 1.5,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|hide_crosshair [Indent level: 2],
        "hide_crosshair": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 1
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|hide_gunmount [Indent level: 2],
        "hide_gunmount": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 1
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|reloadAnim_1 [Indent level: 2],
        "reloadanim_1": {
            "source": "reload",
            "weapon": "rhs_weap_m240H_1"
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|reloadMagazine_1 [Indent level: 2],
        "reloadmagazine_1": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_m240H_1"
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|revolving_1 [Indent level: 2],
        "revolving_1": {
            "source": "revolving",
            "weapon": "rhs_weap_m240H_1"
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|reloadAnim_2 [Indent level: 2],
        "reloadanim_2": {
            "source": "reload",
            "weapon": "rhs_weap_m240H_2"
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|reloadMagazine_2 [Indent level: 2],
        "reloadmagazine_2": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_m240H_2"
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|revolving_2 [Indent level: 2],
        "revolving_2": {
            "source": "revolving",
            "weapon": "rhs_weap_m240H_2"
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|hit_pylon_1_source [Indent level: 2],
        "hit_pylon_1_source": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|hit_pylon_2_source [Indent level: 2],
        "hit_pylon_2_source": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "source": "Hit",
            "hitpoint": "HitGlass2",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "source": "Hit",
            "hitpoint": "HitGlass3",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "source": "Hit",
            "hitpoint": "HitGlass4",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "source": "Hit",
            "hitpoint": "HitGlass5",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "source": "Hit",
            "hitpoint": "HitGlass6",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_uh1h_base|AnimationSources|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "source": "Hit",
            "hitpoint": "HitGlass7",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|AddCargoHook [Indent level: 2],
        "addcargohook": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "iscomponent": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|AddCargoHook_COver [Indent level: 2],
        "addcargohook_cover": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 1,
            "iscomponent": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitHRotor [Indent level: 2],
        "hithrotor": {
            "source": "hit",
            "hitpoint": "HitHRotor",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitVRotor [Indent level: 2],
        "hitvrotor": {
            "source": "hit",
            "hitpoint": "HitVRotor",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitEngine [Indent level: 2],
        "hitengine": {
            "source": "hit",
            "hitpoint": "HitEngine",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "source": "hit",
            "hitpoint": "HitEngine2",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitBatteries [Indent level: 2],
        "hitbatteries": {
            "source": "hit",
            "hitpoint": "HitBatteries",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitTransmission [Indent level: 2],
        "hittransmission": {
            "source": "hit",
            "hitpoint": "HitTransmission",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitHydraulics [Indent level: 2],
        "hithydraulics": {
            "source": "hit",
            "hitpoint": "HitHydraulics",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter_Base_H|AnimationSources|HitFuel [Indent level: 2],
        "hitfuel": {
            "source": "hit",
            "hitpoint": "HitFuel",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitEngine1 [Indent level: 2],
        "hitengine1": {
            "source": "hit",
            "hitpoint": "HitEngine1",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitWinch_Source [Indent level: 2],
        "hitwinch_source": {
            "source": "hit",
            "hitpoint": "HitWinch",
            "raw": 1
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightRed_source [Indent level: 2],
        "collisionlightred_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionRed"
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightWhite_source [Indent level: 2],
        "collisionlightwhite_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionWhite"
        }
    },
    # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|UserActions|Open_Side_Doors [Indent level: 2]
        "open_side_doors": {
            "displayname": "Open Side Doors",
            "onlyforplayer": 1,
            "position": "aimpoint",
            "radius": 2,
            "priority": 1,
            "condition": "this doorPhase 'close_cargo_doors' > 0 and (alive this) and player in this;",
            "statement": "this animateDoor ['close_cargo_doors',0]",
            "showwindow": 0
        },
        # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|UserActions|Close_Side_Doors [Indent level: 2],
        "close_side_doors": {
            "displayname": "Close Side Doors",
            "condition": "this doorPhase 'close_cargo_doors' == 0 and (alive this) and player in this;",
            "statement": "this animateDoor ['close_cargo_doors',1]",
            "onlyforplayer": 1,
            "position": "aimpoint",
            "radius": 2,
            "priority": 1,
            "showwindow": 0
        }
    },
    # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|Attributes|uh1h_textures [Indent level: 2]
        "uh1h_textures": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Paint",
            "tooltip": "Select paint color."
        },
        # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|Attributes|close_cargo_doors [Indent level: 2],
        "close_cargo_doors": {
            "displayname": "Close Side Doors",
            "property": "close_cargo_doors",
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        }
    },
    # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhs_uh1h_hidf_unarmed|Turrets|CopilotTurret [Indent level: 2]
        "copilotturret": {
            "caneject": 0,
            "iscopilot": 1,
            "hideweaponsgunner": 0,
            "gunneraction": "RHS_UH1H_CoPilot",
            "gunnerinaction": "RHS_UH1H_CoPilot",
            "memorypointsgetingunner": "pos Codriver",
            "memorypointsgetingunnerdir": "pos Codriver dir",
            "gunnergetinaction": "copilot_Heli_Light_02_Enter",
            "gunnergetoutaction": "copilot_Heli_Light_02_Exit",
            "precisegetinout": 1,
            "gunnerdoor": "door_copilot",
            "gunnerlefthandanimname": "collective",
            "gunnerrighthandanimname": "stick_copilot",
            "gunnerleftleganimname": "PedalL",
            "gunnerrightleganimname": "PedalR",
            "gunbeg": "muzzle_copilot",
            "gunend": "chamber_copilot",
            "primarygunner": 1,
            "proxyindex": 1,
            "lodturnedin": 1100,
            "lodturnedout": 1100,
            "gunnercompartments": "Compartment2",
            "weapons": ["rhs_weap_DummyLauncher","rhs_weap_fcs_nolrf_ammo"],
            "magazines": ["rhs_laserfcsmag","rhs_laserfcsmag"],
            # Class: CfgVehicles|rhs_uh1h_base|Turrets|CopilotTurret|ViewGunner [Indent level: 3],
            "viewgunner": {
                "minanglex": -65,
                "maxanglex": 85,
                "initanglex": 0,
                "minangley": -150,
                "maxangley": 150,
                "initangley": 0,
                "minfov": 0.25,
                "maxfov": 0.95,
                "initfov": 0.85
            },
            # Class: CfgVehicles|rhs_uh1h_base|Turrets|CopilotTurret|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            "body": "",
            "gun": "",
            "animationsourcebody": "",
            "animationsourcegun": "",
            "gunnername": "Copilot",
            "gunnernotspawned": 1,
            "minelev": -50,
            "maxelev": 30,
            "initelev": 11,
            "minturn": -170,
            "maxturn": 170,
            "initturn": 0,
            "maxhorizontalrotspeed": 3,
            "maxverticalrotspeed": 3,
            "commanding": -1,
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            "gunneropticsmodel": "",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "startengine": 0,
            "outgunnermayfire": 1,
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "gunnerview",
            "selectionfireanim": "zasleh",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "gunnerforceoptics": 0,
            "enablemanualfire": 0,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "gunnertype": "",
            "primaryobserver": 0,
            "soundservo": ["",0.00316228,1],
            "soundelevation": ["",0.00316228,1],
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
            "canusescanners": 1,
            "gunneropticscolor": [0,0,0,1],
            "gunneropticsshowcursor": 0,
            "turretinfotype": "",
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneropticseffect": [],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunneroutopticsshowcursor": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "gunnerusespilotview": 0,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "memorypointsgetingunnerprecise": "",
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "armorlights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "reflectors": {
            },
            "aggregatereflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
            "gunfire": {
                "access": 0,
                "cloudletduration": 0.2,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 0.2,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 0.5,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletFire",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.01,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 4500,
                "deltat": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "t1": {
                        "maxt": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "t2": {
                        "maxt": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "t3": {
                        "maxt": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "t4": {
                        "maxt": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "t5": {
                        "maxt": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "t6": {
                        "maxt": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "t7": {
                        "maxt": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "t8": {
                        "maxt": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "t9": {
                        "maxt": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "t10": {
                        "maxt": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "t11": {
                        "maxt": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "t12": {
                        "maxt": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "t13": {
                        "maxt": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "t14": {
                        "maxt": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "t15": {
                        "maxt": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "t16": {
                        "maxt": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "t17": {
                        "maxt": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "t18": {
                        "maxt": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "t19": {
                        "maxt": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "t20": {
                        "maxt": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "t21": {
                        "maxt": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "t22": {
                        "maxt": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "gunclouds": {
                "access": 0,
                "cloudletduration": 0.3,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 1,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletaccy": 0.4,
                "cloudletminyspeed": 0.2,
                "cloudletmaxyspeed": 0.8,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "mgunclouds": {
                "access": 0,
                "cloudletgrowup": 0.05,
                "cloudletfadein": 0,
                "cloudletfadeout": 0.1,
                "cloudletduration": 0.05,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 0.3,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "timetolive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourcesize": 0.02,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "turrets": {
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.3,
                "minfov": 0.07,
                "maxfov": 0.35,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "forcenvg": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "dontcreateai": 0,
            "disablesoundattenuation": 0,
            "slingloadoperator": 0,
            "playerposition": 0,
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
            "turnin": {
                "turnoffset": 0
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
            "turnout": {
                "turnoffset": 0
            },
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|Turrets|RightGunner [Indent level: 2],
        "rightgunner": {
            "body": "RightTurretBase",
            "gun": "RightTurretGun",
            "animationsourcebody": "RightTurretBase",
            "animationsourcegun": "RightTurretGun",
            "turretinfotype": "RHS_RscWeaponZeroing",
            "caneject": 1,
            "iscopilot": 0,
            "initelev": 0,
            "initturn": -90,
            "maxelev": 20,
            "maxturn": -25,
            "minelev": -55,
            "minturn": -135,
            "soundservo": ["",0.01,1],
            "stabilizedinaxes": 0,
            "weapons": ["rhs_weap_m240H_2"],
            "magazines": ["rhs_mag_762x51_M240_200_M80","rhs_mag_762x51_M240_200_M80","rhs_mag_762x51_M240_200_M80","rhs_mag_762x51_M240_200_M80","rhs_mag_762x51_M240_200_M80"],
            "discretedistance": [200,300,400,500,600,700,800],
            "discretedistanceinitindex": 0,
            "gunbeg": "muzzle_2",
            "gunend": "chamber_2",
            "gunnername": "Right door gunner",
            "memorypointsgetingunner": "pos Gunner R",
            "memorypointsgetingunnerdir": "pos Gunner R dir",
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "memorypointgunneroptics": "gunnerview_2",
            "gunneroutopticsshowcursor": 1,
            "gunnerlefthandanimname": "OtocHlaven_2",
            "gunnerrighthandanimname": "OtocHlaven_2",
            "gunnerleftleganimname": "gunner_2_leg_left",
            "gunnerrightleganimname": "gunner_2_legs",
            "gunneraction": "RHS_UH1H_Gunner_R",
            "gunnerinaction": "RHS_UH1H_Gunner_R",
            "selectionfireanim": "zasleh_2",
            "primarygunner": 0,
            "proxyindex": 3,
            # Class: CfgVehicles|rhs_uh1h_base|Turrets|RightGunner|ViewOptics [Indent level: 3],
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
            "gunnercompartments": "Compartment3",
            "soundattenuationturret": "HeliAttenuationGunner",
            "disablesoundattenuation": 0,
            # Class: CfgVehicles|rhs_uh1h_base|Turrets|RightGunner|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "startengine": 0,
            "outgunnermayfire": 1,
            "commanding": -1,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "memorypointgun": "machinegun",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "gunnerforceoptics": 0,
            "enablemanualfire": 0,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "gunnertype": "",
            "primaryobserver": 0,
            "soundelevation": ["",0.00316228,1],
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "maxhorizontalrotspeed": 1.2,
            "maxverticalrotspeed": 1.2,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "primary": 1,
            "hasgunner": 1,
            "canusescanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewGunner [Indent level: 2],
            "viewgunner": {
                "initanglex": 5,
                "minanglex": -75,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "minfov": 0.25,
                "maxfov": 1.25,
                "initfov": 0.75,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "continuous": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "gunneropticscolor": [0,0,0,1],
            "gunneropticsshowcursor": 0,
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneropticseffect": [],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "gunnerusespilotview": 0,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "memorypointsgetingunnerprecise": "",
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "armorlights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "reflectors": {
            },
            "aggregatereflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
            "gunfire": {
                "access": 0,
                "cloudletduration": 0.2,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 0.2,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 0.5,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletFire",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.01,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 4500,
                "deltat": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "t1": {
                        "maxt": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "t2": {
                        "maxt": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "t3": {
                        "maxt": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "t4": {
                        "maxt": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "t5": {
                        "maxt": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "t6": {
                        "maxt": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "t7": {
                        "maxt": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "t8": {
                        "maxt": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "t9": {
                        "maxt": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "t10": {
                        "maxt": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "t11": {
                        "maxt": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "t12": {
                        "maxt": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "t13": {
                        "maxt": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "t14": {
                        "maxt": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "t15": {
                        "maxt": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "t16": {
                        "maxt": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "t17": {
                        "maxt": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "t18": {
                        "maxt": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "t19": {
                        "maxt": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "t20": {
                        "maxt": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "t21": {
                        "maxt": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "t22": {
                        "maxt": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "gunclouds": {
                "access": 0,
                "cloudletduration": 0.3,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 1,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletaccy": 0.4,
                "cloudletminyspeed": 0.2,
                "cloudletmaxyspeed": 0.8,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "mgunclouds": {
                "access": 0,
                "cloudletgrowup": 0.05,
                "cloudletfadein": 0,
                "cloudletfadeout": 0.1,
                "cloudletduration": 0.05,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 0.3,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "timetolive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourcesize": 0.02,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "turrets": {
            },
            "forcenvg": 0,
            "gunnerdoor": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "dontcreateai": 0,
            "slingloadoperator": 0,
            "playerposition": 0,
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
            "turnin": {
                "turnoffset": 0
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
            "turnout": {
                "turnoffset": 0
            },
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|Turrets|LeftGunner [Indent level: 2],
        "leftgunner": {
            "body": "LeftTurretBase",
            "gun": "LeftTurretGun",
            "animationsourcebody": "LeftTurretBase",
            "animationsourcegun": "LeftTurretGun",
            "weapons": ["rhs_weap_m240H_1"],
            "magazines": ["rhs_mag_762x51_M240_200_M80","rhs_mag_762x51_M240_200_M80","rhs_mag_762x51_M240_200_M80","rhs_mag_762x51_M240_200_M80","rhs_mag_762x51_M240_200_M80"],
            "gunbeg": "muzzle_1",
            "gunend": "chamber_1",
            "gunnerlefthandanimname": "OtocHlaven_1",
            "gunnerrighthandanimname": "OtocHlaven_1",
            "gunnerleftleganimname": "gunner_1_leg_left",
            "gunnerrightleganimname": "gunner_1_legs",
            "gunneraction": "RHS_UH1H_Gunner_L",
            "gunnerinaction": "RHS_UH1H_Gunner_L",
            "memorypointsgetingunner": "pos Gunner L",
            "memorypointsgetingunnerdir": "pos Gunner L dir",
            "primarygunner": 0,
            "proxyindex": 2,
            "memorypointgunneroptics": "gunnerview_1",
            "selectionfireanim": "zasleh_1",
            "gunnername": "Left door gunner",
            "initelev": 0,
            "initturn": 90,
            "maxelev": 20,
            "maxturn": 125,
            "minelev": -55,
            "minturn": 30,
            "turretinfotype": "RHS_RscWeaponZeroing",
            "caneject": 1,
            "iscopilot": 0,
            "soundservo": ["",0.01,1],
            "stabilizedinaxes": 0,
            "discretedistance": [200,300,400,500,600,700,800],
            "discretedistanceinitindex": 0,
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "gunneroutopticsshowcursor": 1,
            # Class: CfgVehicles|rhs_uh1h_base|Turrets|RightGunner|ViewOptics [Indent level: 3],
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
            "gunnercompartments": "Compartment3",
            "soundattenuationturret": "HeliAttenuationGunner",
            "disablesoundattenuation": 0,
            # Class: CfgVehicles|rhs_uh1h_base|Turrets|RightGunner|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "startengine": 0,
            "outgunnermayfire": 1,
            "commanding": -1,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "memorypointgun": "machinegun",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "gunnerforceoptics": 0,
            "enablemanualfire": 0,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "gunnertype": "",
            "primaryobserver": 0,
            "soundelevation": ["",0.00316228,1],
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "maxhorizontalrotspeed": 1.2,
            "maxverticalrotspeed": 1.2,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "primary": 1,
            "hasgunner": 1,
            "canusescanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewGunner [Indent level: 2],
            "viewgunner": {
                "initanglex": 5,
                "minanglex": -75,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "minfov": 0.25,
                "maxfov": 1.25,
                "initfov": 0.75,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "continuous": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "gunneropticscolor": [0,0,0,1],
            "gunneropticsshowcursor": 0,
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneropticseffect": [],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "gunnerusespilotview": 0,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "memorypointsgetingunnerprecise": "",
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "armorlights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "reflectors": {
            },
            "aggregatereflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
            "gunfire": {
                "access": 0,
                "cloudletduration": 0.2,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 0.2,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 0.5,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletFire",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.01,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 4500,
                "deltat": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "t1": {
                        "maxt": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "t2": {
                        "maxt": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "t3": {
                        "maxt": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "t4": {
                        "maxt": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "t5": {
                        "maxt": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "t6": {
                        "maxt": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "t7": {
                        "maxt": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "t8": {
                        "maxt": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "t9": {
                        "maxt": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "t10": {
                        "maxt": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "t11": {
                        "maxt": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "t12": {
                        "maxt": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "t13": {
                        "maxt": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "t14": {
                        "maxt": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "t15": {
                        "maxt": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "t16": {
                        "maxt": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "t17": {
                        "maxt": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "t18": {
                        "maxt": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "t19": {
                        "maxt": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "t20": {
                        "maxt": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "t21": {
                        "maxt": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "t22": {
                        "maxt": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "gunclouds": {
                "access": 0,
                "cloudletduration": 0.3,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 1,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletaccy": 0.4,
                "cloudletminyspeed": 0.2,
                "cloudletmaxyspeed": 0.8,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "mgunclouds": {
                "access": 0,
                "cloudletgrowup": 0.05,
                "cloudletfadein": 0,
                "cloudletfadeout": 0.1,
                "cloudletduration": 0.05,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 0.3,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "timetolive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourcesize": 0.02,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "turrets": {
            },
            "forcenvg": 0,
            "gunnerdoor": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "dontcreateai": 0,
            "slingloadoperator": 0,
            "playerposition": 0,
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
            "turnin": {
                "turnoffset": 0
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
            "turnout": {
                "turnoffset": 0
            },
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|Turrets|CargoTurret_01 [Indent level: 2],
        "cargoturret_01": {
            "gunneraction": "passenger_bench_1",
            "gunnergetinaction": "GetInHeli_Light_01bench",
            "gunnercompartments": "compartment3",
            "memorypointsgetingunner": "pos Gunner L",
            "memorypointsgetingunnerdir": "pos Gunner L dir",
            "gunnername": "Passenger (Left Door)",
            "gunbeg": "muzzle_copilot",
            "gunend": "chamber_copilot",
            "proxyindex": 7,
            "maxelev": 45,
            "minelev": -55,
            "maxturn": 70,
            "minturn": -10,
            "ispersonturret": 1,
            "ejectdeadgunner": 0,
            "playerposition": 4,
            "soundattenuationturret": "",
            "disablesoundattenuation": 1,
            "weapons": ["rhs_weap_DummyLauncher"],
            # Class: CfgVehicles|rhs_uh1h_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2],
            "viewgunner": {
                "initanglex": 5,
                "minanglex": -75,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "minfov": 0.25,
                "maxfov": 1.25,
                "initfov": 0.75,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "animationsourcebody": "",
            "animationsourcegun": "",
            "body": "",
            "caneject": 1,
            "commanding": 0,
            "dontcreateai": 1,
            "gun": "",
            "gunnergetoutaction": "GetOutLow",
            "hideweaponsgunner": 0,
            "iscopilot": 0,
            "primarygunner": 0,
            "proxytype": "CPCargo",
            "startengine": 0,
            "turretfollowfreelook": 0,
            "viewgunnerinexternal": 1,
            "outgunnermayfire": 1,
            "showascargo": 1,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "gunnertype": "",
            "primaryobserver": 0,
            "magazines": [],
            "soundservo": ["",0.00316228,1],
            "soundelevation": ["",0.00316228,1],
            "initelev": 0,
            "initturn": 0,
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "maxhorizontalrotspeed": 1.2,
            "maxverticalrotspeed": 1.2,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
            "turretcansee": 0,
            "canusescanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "turretspec": {
                "showheadphones": 0
            },
            "gunneropticsmodel": "",
            "gunneropticscolor": [0,0,0,1],
            "gunnerforceoptics": 1,
            "gunneropticsshowcursor": 0,
            "turretinfotype": "",
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneropticseffect": [],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunneroutopticsshowcursor": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "gunnerusespilotview": 0,
            "castgunnershadow": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "showhmd": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "memorypointsgetingunnerprecise": "",
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "armorlights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "reflectors": {
            },
            "aggregatereflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
            "gunfire": {
                "access": 0,
                "cloudletduration": 0.2,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 0.2,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 0.5,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletFire",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.01,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 4500,
                "deltat": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "t1": {
                        "maxt": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "t2": {
                        "maxt": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "t3": {
                        "maxt": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "t4": {
                        "maxt": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "t5": {
                        "maxt": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "t6": {
                        "maxt": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "t7": {
                        "maxt": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "t8": {
                        "maxt": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "t9": {
                        "maxt": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "t10": {
                        "maxt": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "t11": {
                        "maxt": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "t12": {
                        "maxt": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "t13": {
                        "maxt": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "t14": {
                        "maxt": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "t15": {
                        "maxt": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "t16": {
                        "maxt": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "t17": {
                        "maxt": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "t18": {
                        "maxt": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "t19": {
                        "maxt": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "t20": {
                        "maxt": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "t21": {
                        "maxt": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "t22": {
                        "maxt": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "gunclouds": {
                "access": 0,
                "cloudletduration": 0.3,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 1,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletaccy": 0.4,
                "cloudletminyspeed": 0.2,
                "cloudletmaxyspeed": 0.8,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "mgunclouds": {
                "access": 0,
                "cloudletgrowup": 0.05,
                "cloudletfadein": 0,
                "cloudletfadeout": 0.1,
                "cloudletduration": 0.05,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 0.3,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "timetolive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourcesize": 0.02,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "turrets": {
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.3,
                "minfov": 0.07,
                "maxfov": 0.35,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "forcenvg": 0,
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "gunnerdoor": "",
            "precisegetinout": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "slingloadoperator": 0,
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
            "turnin": {
                "turnoffset": 0
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
            "turnout": {
                "turnoffset": 0
            },
            "gunnerinaction": "ManActTestDriver",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_uh1h_base|Turrets|CargoTurret_02 [Indent level: 2],
        "cargoturret_02": {
            "gunnercompartments": "compartment3",
            "memorypointsgetingunner": "pos Gunner R",
            "memorypointsgetingunnerdir": "pos Gunner R dir",
            "gunnername": "Passenger (Right Door)",
            "proxyindex": 8,
            "maxturn": 35,
            "minturn": -60,
            "gunneraction": "passenger_bench_1",
            "gunnergetinaction": "GetInHeli_Light_01bench",
            "gunbeg": "muzzle_copilot",
            "gunend": "chamber_copilot",
            "maxelev": 45,
            "minelev": -55,
            "ispersonturret": 1,
            "ejectdeadgunner": 0,
            "playerposition": 4,
            "soundattenuationturret": "",
            "disablesoundattenuation": 1,
            "weapons": ["rhs_weap_DummyLauncher"],
            # Class: CfgVehicles|rhs_uh1h_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2],
            "viewgunner": {
                "initanglex": 5,
                "minanglex": -75,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "minfov": 0.25,
                "maxfov": 1.25,
                "initfov": 0.75,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "animationsourcebody": "",
            "animationsourcegun": "",
            "body": "",
            "caneject": 1,
            "commanding": 0,
            "dontcreateai": 1,
            "gun": "",
            "gunnergetoutaction": "GetOutLow",
            "hideweaponsgunner": 0,
            "iscopilot": 0,
            "primarygunner": 0,
            "proxytype": "CPCargo",
            "startengine": 0,
            "turretfollowfreelook": 0,
            "viewgunnerinexternal": 1,
            "outgunnermayfire": 1,
            "showascargo": 1,
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "gunnertype": "",
            "primaryobserver": 0,
            "magazines": [],
            "soundservo": ["",0.00316228,1],
            "soundelevation": ["",0.00316228,1],
            "initelev": 0,
            "initturn": 0,
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "maxhorizontalrotspeed": 1.2,
            "maxverticalrotspeed": 1.2,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
            "turretcansee": 0,
            "canusescanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "turretspec": {
                "showheadphones": 0
            },
            "gunneropticsmodel": "",
            "gunneropticscolor": [0,0,0,1],
            "gunnerforceoptics": 1,
            "gunneropticsshowcursor": 0,
            "turretinfotype": "",
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneropticseffect": [],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunneroutopticsshowcursor": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "gunnerusespilotview": 0,
            "castgunnershadow": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "showhmd": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "lodturnedin": -1,
            "lodturnedout": -1,
            "memorypointsgetingunnerprecise": "",
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "armorlights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "reflectors": {
            },
            "aggregatereflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
            "gunfire": {
                "access": 0,
                "cloudletduration": 0.2,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 0.2,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 0.5,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletFire",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.01,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 4500,
                "deltat": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "t1": {
                        "maxt": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "t2": {
                        "maxt": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "t3": {
                        "maxt": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "t4": {
                        "maxt": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "t5": {
                        "maxt": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "t6": {
                        "maxt": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "t7": {
                        "maxt": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "t8": {
                        "maxt": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "t9": {
                        "maxt": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "t10": {
                        "maxt": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "t11": {
                        "maxt": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "t12": {
                        "maxt": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "t13": {
                        "maxt": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "t14": {
                        "maxt": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "t15": {
                        "maxt": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "t16": {
                        "maxt": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "t17": {
                        "maxt": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "t18": {
                        "maxt": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "t19": {
                        "maxt": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "t20": {
                        "maxt": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "t21": {
                        "maxt": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "t22": {
                        "maxt": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "gunclouds": {
                "access": 0,
                "cloudletduration": 0.3,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 1,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletaccy": 0.4,
                "cloudletminyspeed": 0.2,
                "cloudletmaxyspeed": 0.8,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "mgunclouds": {
                "access": 0,
                "cloudletgrowup": 0.05,
                "cloudletfadein": 0,
                "cloudletfadeout": 0.1,
                "cloudletduration": 0.05,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 0.3,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "timetolive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourcesize": 0.02,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "turrets": {
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.3,
                "minfov": 0.07,
                "maxfov": 0.35,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "forcenvg": 0,
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "gunnerdoor": "",
            "precisegetinout": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "slingloadoperator": 0,
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
            "turnin": {
                "turnoffset": 0
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
            "turnout": {
                "turnoffset": 0
            },
            "gunnerinaction": "ManActTestDriver",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|Helicopter_Base_H|Turrets|MainTurret [Indent level: 2],
        "mainturret": {
            "gunneropticsmodel": "",
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "startengine": 0,
            "outgunnermayfire": 1,
            "commanding": -1,
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "gunnerview",
            "selectionfireanim": "zasleh",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "gunnerforceoptics": 0,
            "enablemanualfire": 0,
            "caneject": 0,
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|Helicopter|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "vez",
                    "visual": "vez",
                    "passthrough": 0.3
                },
                # Class: CfgVehicles|Helicopter|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "zbran",
                    "visual": "zbran",
                    "passthrough": 0.1
                }
            },
            "body": "mainTurret",
            "gun": "mainGun",
            "animationsourcebody": "mainTurret",
            "animationsourcegun": "mainGun",
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "proxyindex": 1,
            "gunnername": "Gunner",
            "gunnertype": "",
            "primarygunner": 1,
            "primaryobserver": 0,
            "weapons": [],
            "magazines": [],
            "soundservo": ["",0.00316228,1],
            "soundelevation": ["",0.00316228,1],
            "minelev": -4,
            "maxelev": 20,
            "initelev": 0,
            "minturn": -360,
            "maxturn": 360,
            "initturn": 0,
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "maxhorizontalrotspeed": 1.2,
            "maxverticalrotspeed": 1.2,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
            "canusescanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewGunner [Indent level: 2],
            "viewgunner": {
                "initanglex": 5,
                "minanglex": -75,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "minfov": 0.25,
                "maxfov": 1.25,
                "initfov": 0.75,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "continuous": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "gunneropticscolor": [0,0,0,1],
            "gunneropticsshowcursor": 0,
            "turretinfotype": "",
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneropticseffect": [],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunneroutopticsshowcursor": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "gunnerusespilotview": 0,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "showhmd": 0,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "gunnercompartments": "Compartment1",
            "lodturnedin": -1,
            "lodturnedout": -1,
            "memorypointsgetingunnerprecise": "",
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "armorlights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "reflectors": {
            },
            "aggregatereflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
            "gunfire": {
                "access": 0,
                "cloudletduration": 0.2,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 0.2,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 0.5,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletFire",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.01,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 4500,
                "deltat": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "t1": {
                        "maxt": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "t2": {
                        "maxt": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "t3": {
                        "maxt": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "t4": {
                        "maxt": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "t5": {
                        "maxt": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "t6": {
                        "maxt": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "t7": {
                        "maxt": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "t8": {
                        "maxt": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "t9": {
                        "maxt": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "t10": {
                        "maxt": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "t11": {
                        "maxt": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "t12": {
                        "maxt": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "t13": {
                        "maxt": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "t14": {
                        "maxt": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "t15": {
                        "maxt": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "t16": {
                        "maxt": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "t17": {
                        "maxt": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "t18": {
                        "maxt": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "t19": {
                        "maxt": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "t20": {
                        "maxt": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "t21": {
                        "maxt": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "t22": {
                        "maxt": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "gunclouds": {
                "access": 0,
                "cloudletduration": 0.3,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 1,
                "cloudletgrowup": 1,
                "cloudletfadein": 0.01,
                "cloudletfadeout": 1,
                "cloudletaccy": 0.4,
                "cloudletminyspeed": 0.2,
                "cloudletmaxyspeed": 0.8,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourcesize": 0.5,
                "timetolive": 0,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "mgunclouds": {
                "access": 0,
                "cloudletgrowup": 0.05,
                "cloudletfadein": 0,
                "cloudletfadeout": 0.1,
                "cloudletduration": 0.05,
                "cloudletanimperiod": 1,
                "cloudletsize": 1,
                "cloudletalpha": 0.3,
                "cloudletaccy": 0,
                "cloudletminyspeed": -100,
                "cloudletmaxyspeed": 100,
                "cloudletshape": "cloudletClouds",
                "cloudletcolor": [1,1,1,0],
                "timetolive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourcesize": 0.02,
                "initt": 0,
                "deltat": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                    "t0": {
                        "maxt": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "turrets": {
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.3,
                "minfov": 0.07,
                "maxfov": 0.35,
                "minmovex": 0,
                "maxmovex": 0,
                "minmovey": 0,
                "maxmovey": 0,
                "minmovez": 0,
                "maxmovez": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "forcenvg": 0,
            "iscopilot": 0,
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "gunnerdoor": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "dontcreateai": 0,
            "disablesoundattenuation": 0,
            "slingloadoperator": 0,
            "playerposition": 0,
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
            "turnin": {
                "turnoffset": 0
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
            "turnout": {
                "turnoffset": 0
            },
            "gunnerinaction": "ManActTestDriver",
            "gunneraction": "ManActTestDriver",
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "showcrewaim": 0
        }
    },
    "scope": 2,
    "scopecurator": 2,
    "side": 1,
    "faction": "rhsgref_faction_hidf",
    "crew": "rhsgref_hidf_helipilot",
    "typicalcargo": ["rhsgref_hidf_helipilot"],
    # Class: CfgVehicles|rhs_uh1h_hidf|TransportMagazines [Indent level: 1],
    "transportmagazines": {
    },
    # Class: CfgVehicles|rhs_uh1h_hidf|TransportItems [Indent level: 1],
    "transportitems": {
    },
    # Class: CfgVehicles|rhs_uh1h_hidf|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    "enablesweep": 0,
    "hiddenselections": ["Camo1","Camo2","Camo_mlod","decals"],
    "hiddenselectionstextures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_hidf_grey_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_hidf_grey_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_hidf_grey_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|uh1h_hidf_decals_ca.paa"],
    # Class: CfgVehicles|rhs_uh1h_hidf|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|hidf_grey [Indent level: 2]
        "hidf_grey": {
            "displayname": "HIDF Grey",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_hidf_grey_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_hidf_grey_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_hidf_grey_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|uh1h_hidf_decals_ca.paa"],
            "factions": ["rhsgref_faction_hidf"]
        },
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|hidf_summer [Indent level: 2],
        "hidf_summer": {
            "displayname": "HIDF MERDC (Summer verdant)",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_hidf_summer_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_hidf_summer_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_hidf_tropical_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|blank_ca.paa"],
            "factions": ["rhsgref_faction_hidf"]
        },
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|hidf_tropical [Indent level: 2],
        "hidf_tropical": {
            "displayname": "HIDF MERDC (Tropical verdant)",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_hidf_tropical_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_hidf_tropical_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_hidf_tropical_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|blank_ca.paa"],
            "factions": ["rhsgref_faction_hidf"]
        },
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|hidf_olv [Indent level: 2],
        "hidf_olv": {
            "displayname": "HIDF Olive",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_hidf_olv_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_hidf_olv_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_us_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|uh1h_hidf_decals_ca.paa"],
            "factions": ["rhsgref_faction_hidf"]
        },
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|hidf_tan [Indent level: 2],
        "hidf_tan": {
            "displayname": "HIDF Tan",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_tan_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_tan_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_tan_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|uh1h_hidf_decals_ca.paa"],
            "factions": ["rhsgref_faction_hidf"]
        },
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|us_army [Indent level: 2],
        "us_army": {
            "displayname": "US Army",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_us_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_us_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_us_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|uh1h_us_decals_ca.paa"],
            "factions": ["rhs_faction_usarmy_wd","rhs_faction_usarmy_d"]
        },
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|us_army_med [Indent level: 2],
        "us_army_med": {
            "displayname": "US Army (Medevac)",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_us_med_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_us_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_us_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|uh1h_us_decals_ca.paa"],
            "factions": ["rhs_faction_usarmy_wd","rhs_faction_usarmy_d"]
        },
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|black [Indent level: 2],
        "black": {
            "displayname": "Black",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_black_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_black_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_black_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|blank_ca.paa"],
            "factions": ["CIV_F"]
        },
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|iraq [Indent level: 2],
        "iraq": {
            "displayname": "Iraqi Air Force",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_iaf_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_iaf_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_iaf_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|blank_ca.paa"],
            "factions": ["IND_F"]
        },
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|takistan [Indent level: 2],
        "takistan": {
            "displayname": "Takistan",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_tka_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_in_tka_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_tka_co","rhsgref|addons|rhsgref_air|uh1h|data|decals|blank_ca.paa"],
            "factions": ["OPF_F"]
        },
        # Class: CfgVehicles|rhs_uh1h_hidf|textureSources|guerilla [Indent level: 2],
        "guerilla": {
            "displayname": "Guerilla",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_gue_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_gue_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_gue_co","rhsgref|addons|rhsgref_air|uh1h|data|decals|blank_ca.paa"],
            "factions": ["IND_G_F","BLU_G_F","OPF_G_F"]
        },
        # Class: CfgVehicles|rhs_uh1h_base|textureSources|un [Indent level: 2],
        "un": {
            "displayname": "UN",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_un_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_un_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_un_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|uh1h_un_decals_ca.paa"],
            "factions": ["rhsgref_faction_un"]
        },
        # Class: CfgVehicles|rhs_uh1h_base|textureSources|idap [Indent level: 2],
        "idap": {
            "displayname": "IDAP",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_idap_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_idap_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_un_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|uh1h_idap_decals_ca.paa"],
            "factions": ["CIV_IDAP_F"]
        },
        # Class: CfgVehicles|rhs_uh1h_base|textureSources|tan [Indent level: 2],
        "tan": {
            "displayname": "Tan",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_tan_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_tan_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_tan_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|blank_ca.paa"],
            "factions": ["IND_G_F","BLU_G_F","OPF_G_F","IND_F"]
        },
        # Class: CfgVehicles|rhs_uh1h_base|textureSources|olive [Indent level: 2],
        "olive": {
            "displayname": "Olive",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_olv_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_olv_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_us_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|blank_ca.paa"],
            "factions": ["IND_G_F","BLU_G_F","OPF_G_F","IND_F"]
        },
        # Class: CfgVehicles|rhs_uh1h_base|textureSources|white [Indent level: 2],
        "white": {
            "displayname": "White",
            "textures": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h_un_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_un_in_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|mlod_un_co.paa","rhsgref|addons|rhsgref_air|uh1h|data|decals|blank_ca.paa"],
            "factions": ["IND_G_F","BLU_G_F","OPF_G_F","IND_F"]
        }
    },
    "texturelist": [],
    "picture": "rhsgref|addons|rhsgref_air|uh1h|ui|rhs_uh1h_pic_ca.paa",
    "icon": "rhsgref|addons|rhsgref_air|uh1h|ui|icon_uh1h_ca.paa",
    "mapsize": 14,
    "model": "rhsgref|addons|rhsgref_air|uh1h|uh1h.p3d",
    "unitinfotype": "RHSGREF_RscUnitInfoAir_UH1H",
    "unitinfotypertd": "RHSGREF_RscUnitInfoAirRTDFullDigital_UH1H",
    "destrtype": "DestructWreck",
    "getinaction": "pilot_Heli_Light_02_Enter",
    "getoutaction": "pilot_Heli_Light_02_Exit",
    "driveraction": "RHS_UH1H_Pilot",
    "driverinaction": "RHS_UH1H_Pilot",
    "driverlefthandanimname": "collective",
    "driverdoor": "door_pilot",
    "precisegetinout": 1,
    "driveropticsmodel": "",
    "cargocompartments": ["compartment3"],
    "getinradius": 1,
    "hideweaponsdriver": 0,
    "gforceshakeattenuation": 0.3,
    "mingforce": 0.05,
    "maxgforce": 0.1,
    # Class: CfgVehicles|rhs_uh1h_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhs_uh1h_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "Exhaust",
            "direction": "Exhaust_dir",
            "effect": "ExhaustsEffectHeliBig"
        }
    },
    "availableforsupporttypes": ["Drop","Transport"],
    "supplyradius": 2,
    "epeimpulsedamagecoef": 20,
    "damageresistance": 0.01039,
    "crewcrashprotection": 0.2,
    "extcameraposition": [0,2,-17],
    "threat": [0.4,0,0],
    "showcrewaim": 0,
    "mainrotorspeed": 1.2,
    "backrotorspeed": 6.1,
    "fuelcapacity": 781,
    "fuelconsumptionrate": 0.09,
    "maxfordingdepth": 1,
    "driveoncomponent": ["Skids"],
    "mainbladeradius": 8.2,
    "tailbladeradius": 1.5,
    "washdownstrength": "0.9f",
    "maxspeed": 217,
    "slingloadmemorypoint": "slingLoad0",
    "slingloadmaxcargomass": 1900,
    "radartype": 0,
    "liftforcecoef": 1.3,
    "cyclicasideforcecoef": 0.55,
    "cyclicforwardforcecoef": 0.5,
    "backrotorforcecoef": 0.6,
    "bodyfrictioncoef": 0.6,
    "sensitivity": 0.5,
    "maximumload": 4309.13,
    "irtarget": 1,
    "irtargetsize": 0.9,
    "visualtarget": 1,
    "visualtargetsize": 1,
    "radartarget": 1,
    "radartargetsize": 1,
    "lockdetectionsystem": "0",
    "incomingmissiledetectionsystem": "0",
    # Class: CfgVehicles|rhs_uh1h_base|RotorLibHelicopterProperties [Indent level: 1],
    "rotorlibhelicopterproperties": {
        "rtdconfig": "rhsgref|addons|rhsgref_c_air|uh1h|rtd_uh1h.xml",
        "autohovercorrection": [5,2.4,0],
        "defaultcollective": 0.75,
        "startertime": 10,
        "throttleofftoidle": 10,
        "throttleidletooff": 10,
        "throttleidletofull": 8,
        "throttlefulltoidle": 15,
        "maxtorque": 2168,
        "maxmainrotorstress": 130000,
        "maxtailrotorstress": 10000,
        "retreatbladestallwarningspeed": 63,
        "rtd_center": "rtd_center",
        "maxhorizontalstabilizerleftstress": 8000,
        "maxhorizontalstabilizerrightstress": 8000,
        "maxverticalstabilizerstress": 8000,
        "stressdamagepersec": 0.01,
        "hasapu": 0,
        "horizontalwingsanglecollmin": 0,
        "horizontalwingsanglecollmax": 0,
        "vrsshakepowercoef": 1
    },
    "enablemanualfire": 0,
    # Class: CfgVehicles|rhs_uh1h_base|MFD [Indent level: 1],
    "mfd": {
    },
    # Class: CfgVehicles|rhs_uh1h_base|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initfov": 0.85,
        "maxfov": 0.95,
        "minfov": 0.25,
        "initanglex": 0,
        "initangley": 0,
        "minanglex": -65,
        "maxanglex": 85,
        "minangley": -150,
        "maxangley": 150,
        "minmovex": -0.2,
        "maxmovex": 0.2,
        "minmovey": -0.1,
        "maxmovey": 0.1,
        "minmovez": -0.1,
        "maxmovez": 0.2,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "soundgetin": ["rhsgref|addons|rhsgref_air|uh1h|Sounds|open_close",0.562341,1],
    "soundgetout": ["rhsgref|addons|rhsgref_air|uh1h|Sounds|open_close",0.794328,1,20],
    "soundengineonint": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_start_int",0.4,1],
    "soundengineonext": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_start_ext",0.794328,1,600],
    "soundengineoffint": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_stop_int",0.4,1],
    "soundengineoffext": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_stop_ext",0.794328,1,600],
    "soundgeneralcollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_1",1,1,100],
    "soundgeneralcollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_2",1,1,100],
    "soundgeneralcollision3": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_3",1,1,100],
    "soundcrashes": ["soundGeneralCollision1",0.33,"soundGeneralCollision2",0.33,"soundGeneralCollision3",0.33],
    "soundlandcrashes": ["emptySound",0],
    "soundbuildingcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundarmorcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundwoodcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundbushcollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_1",1,1,100],
    "soundbushcollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_2",1,1,100],
    "soundbushcollision3": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_3",1,1,100],
    "soundbushcrash": ["soundBushCollision1",0.33,"soundBushCollision2",0.33,"soundBushCollision3",0.33],
    "soundwatercollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_water_ext_1",1,1,100],
    "soundwatercollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_water_ext_2",1,1,100],
    "soundwatercrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "sounddammage": ["A3|Sounds_F|vehicles|crashes|helis|Heli_crash_default_ext_1",3.16228,1],
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_1",1,1],
    "soundincommingmissile": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_2",0.7,1],
    "rotordamageint": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_int_open_1",1,1],
    "rotordamageout": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_ext_1",2.51189,1,150],
    "rotordamage": ["rotorDamageInt","rotorDamageOut"],
    "taildamageint": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1],
    "taildamageout": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1,300],
    "taildamage": ["tailDamageInt","tailDamageOut"],
    "landingsoundint0": ["A3|Sounds_F|vehicles|air|noises|landing_skids_int1_open",1,1,100],
    "landingsoundint1": ["A3|Sounds_F|vehicles|air|noises|landing_skids_int1_open",1,1,100],
    "landingsoundint": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingsoundout0": ["A3|Sounds_F|vehicles|air|noises|landing_skids_ext1",1.77828,1,100],
    "landingsoundout1": ["A3|Sounds_F|vehicles|air|noises|landing_skids_ext1",1.77828,1,100],
    "landingsoundout": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    "slingcargoattach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEndINT",1,1],
    "slingcargoattach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookLock",1,1,80],
    "slingcargoattach": ["slingCargoAttach0","slingCargoAttach1"],
    "slingcargodetach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEndINT",1,1],
    "slingcargodetach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookUnlock",1,1,80],
    "slingcargodetach": ["slingCargoDetach0","slingCargoDetach1"],
    "slingcargodetachair0": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_int",1,1],
    "slingcargodetachair1": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_ext",1,1,80],
    "slingcargodetachair": ["slingCargoDetach0","slingCargoDetach1"],
    "slingcargoropebreak0": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_int",1,1],
    "slingcargoropebreak1": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_ext",1,1,80],
    "slingcargoropebreak": ["slingCargoDetach0","slingCargoDetach1"],
    # Class: CfgVehicles|rhs_uh1h_base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|Engine [Indent level: 2]
        "engine": {
            "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_engine_ext_2",1.28893,1,1200],
            "frequency": "rotorSpeed",
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|RotorLowOut [Indent level: 2],
        "rotorlowout": {
            "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_rotor_ext_1",1.25893,1,1500],
            "frequency": "rotorSpeed",
            "volume": "camPos*(0 max (rotorSpeed-0.1))",
            "cone": [1.6,3.14,2,0.5]
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|RotorHighOut [Indent level: 2],
        "rotorhighout": {
            "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_rotor_high_ext_1",1.25893,1,1500],
            "frequency": "rotorSpeed",
            "volume": "camPos*10*(0 max (rotorThrust-0.9))",
            "cone": [1.6,3.14,2,0.5]
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|EngineIn [Indent level: 2],
        "enginein": {
            "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_engine_int_1",1,1],
            "frequency": "rotorSpeed",
            "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|RotorLowIn [Indent level: 2],
        "rotorlowin": {
            "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_rotor_int_1",1,1],
            "frequency": "rotorSpeed",
            "volume": "2*(1-camPos)*((rotorSpeed factor[0.3, 1.1]) min (rotorSpeed factor[1.1, 0.3]))"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|RotorHighIn [Indent level: 2],
        "rotorhighin": {
            "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_rotor_high_int_1",1,1],
            "frequency": "rotorSpeed",
            "volume": "(1-camPos)*3*(rotorThrust-0.9)"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|TransmissionDamageExt_phase1 [Indent level: 2],
        "transmissiondamageext_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|TransmissionDamageExt_phase2 [Indent level: 2],
        "transmissiondamageext_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|TransmissionDamageInt_phase1 [Indent level: 2],
        "transmissiondamageint_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|TransmissionDamageInt_phase2 [Indent level: 2],
        "transmissiondamageint_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|damageAlarmInt [Indent level: 2],
        "damagealarmint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_bluefor",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|damageAlarmExt [Indent level: 2],
        "damagealarmext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_bluefor",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|rotorLowAlarmInt [Indent level: 2],
        "rotorlowalarmint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|rotorLowAlarmExt [Indent level: 2],
        "rotorlowalarmext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|scrubLandInt [Indent level: 2],
        "scrublandint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandInt_open",1,1,100],
            "frequency": 1,
            "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|scrubLandExt [Indent level: 2],
        "scrublandext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubLand factor[0.02, 0.05])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|scrubBuildingInt [Indent level: 2],
        "scrubbuildingint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingInt",1,1,100],
            "frequency": 1,
            "volume": "2 * (1 - camPos) * (scrubBuilding factor[0.02, 0.05])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|scrubBuildingExt [Indent level: 2],
        "scrubbuildingext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|scrubTreeInt [Indent level: 2],
        "scrubtreeint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
            "frequency": 1,
            "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|scrubTreeExt [Indent level: 2],
        "scrubtreeext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|RainExt [Indent level: 2],
        "rainext": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
            "frequency": 1,
            "volume": "camPos * (rain - rotorSpeed/2) * 2"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|RainInt [Indent level: 2],
        "rainint": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int_open",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|SlingLoadDownExt [Indent level: 2],
        "slingloaddownext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|SlingLoadUpExt [Indent level: 2],
        "slingloadupext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|SlingLoadDownInt [Indent level: 2],
        "slingloaddownint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|SlingLoadUpInt [Indent level: 2],
        "slingloadupint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|WindInt [Indent level: 2],
        "windint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wind_open_int",1,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|WindLateralMovementInt [Indent level: 2],
        "windlateralmovementint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wind_lateral_open_int",1,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*lateralMovement*((speed factor [5,40]) + (speed factor [-5,-40]))"
        },
        # Class: CfgVehicles|rhs_uh1h_base|Sounds|GStress [Indent level: 2],
        "gstress": {
            "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2b",0.116228,1,50],
            "frequency": 1,
            "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
        }
    },
    # Class: CfgVehicles|rhs_uh1h_base|SoundsExt [Indent level: 1],
    "soundsext": {
        # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|SoundEvents [Indent level: 2]
        "soundevents": {
        },
        # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds [Indent level: 2],
        "sounds": {
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|Engine [Indent level: 3]
            "engine": {
                "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_engine_ext_2",1.28893,1,1200],
                "frequency": "rotorSpeed",
                "volume": "camPos*((rotorSpeed-0.72)*4)"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|RotorLowOut [Indent level: 3],
            "rotorlowout": {
                "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_rotor_ext_1",1.25893,1,1500],
                "frequency": "rotorSpeed",
                "volume": "camPos*(0 max (rotorSpeed-0.1))",
                "cone": [1.6,3.14,2,0.5]
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|RotorHighOut [Indent level: 3],
            "rotorhighout": {
                "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_rotor_high_ext_1",1.25893,1,1500],
                "frequency": "rotorSpeed",
                "volume": "camPos*10*(0 max (rotorThrust-0.9))",
                "cone": [1.6,3.14,2,0.5]
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|EngineIn [Indent level: 3],
            "enginein": {
                "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_engine_int_1",1,1],
                "frequency": "rotorSpeed",
                "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|RotorLowIn [Indent level: 3],
            "rotorlowin": {
                "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_rotor_int_1",1,1],
                "frequency": "rotorSpeed",
                "volume": "2*(1-camPos)*((rotorSpeed factor[0.3, 1.1]) min (rotorSpeed factor[1.1, 0.3]))"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|RotorHighIn [Indent level: 3],
            "rotorhighin": {
                "sound": ["rhsgref|addons|rhsgref_air|uh1h|sounds|uh1h_rotor_high_int_1",1,1],
                "frequency": "rotorSpeed",
                "volume": "(1-camPos)*3*(rotorThrust-0.9)"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|TransmissionDamageExt_phase1 [Indent level: 3],
            "transmissiondamageext_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|TransmissionDamageExt_phase2 [Indent level: 3],
            "transmissiondamageext_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|TransmissionDamageInt_phase1 [Indent level: 3],
            "transmissiondamageint_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|TransmissionDamageInt_phase2 [Indent level: 3],
            "transmissiondamageint_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|damageAlarmInt [Indent level: 3],
            "damagealarmint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_bluefor",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|damageAlarmExt [Indent level: 3],
            "damagealarmext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_bluefor",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|rotorLowAlarmInt [Indent level: 3],
            "rotorlowalarmint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|rotorLowAlarmExt [Indent level: 3],
            "rotorlowalarmext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|scrubLandInt [Indent level: 3],
            "scrublandint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandInt_open",1,1,100],
                "frequency": 1,
                "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|scrubLandExt [Indent level: 3],
            "scrublandext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubLand factor[0.02, 0.05])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|scrubBuildingInt [Indent level: 3],
            "scrubbuildingint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingInt",1,1,100],
                "frequency": 1,
                "volume": "2 * (1 - camPos) * (scrubBuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|scrubBuildingExt [Indent level: 3],
            "scrubbuildingext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|scrubTreeInt [Indent level: 3],
            "scrubtreeint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
                "frequency": 1,
                "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|scrubTreeExt [Indent level: 3],
            "scrubtreeext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|RainExt [Indent level: 3],
            "rainext": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
                "frequency": 1,
                "volume": "camPos * (rain - rotorSpeed/2) * 2"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|RainInt [Indent level: 3],
            "rainint": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_int_open",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|SlingLoadDownExt [Indent level: 3],
            "slingloaddownext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|SlingLoadUpExt [Indent level: 3],
            "slingloadupext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|SlingLoadDownInt [Indent level: 3],
            "slingloaddownint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|SlingLoadUpInt [Indent level: 3],
            "slingloadupint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|WindInt [Indent level: 3],
            "windint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wind_open_int",1.12202,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|WindLateralMovementInt [Indent level: 3],
            "windlateralmovementint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wind_lateral_open_int",1.99526,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*lateralMovement*((speed factor [5,40]) + (speed factor [-5,-40]))"
            },
            # Class: CfgVehicles|rhs_uh1h_base|SoundsExt|Sounds|GStress [Indent level: 3],
            "gstress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2b",0.116228,1,50],
                "frequency": 1,
                "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
            }
        }
    },
    # Class: CfgVehicles|rhs_uh1h_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhs_uh1h_base|Reflectors|Front [Indent level: 2]
        "front": {
            "color": [11000,7000,5000],
            "ambient": [11,7,5],
            "intensity": 120,
            "size": 1,
            "innerangle": 15,
            "outerangle": 65,
            "conefadecoef": 10,
            "position": "Light_pos",
            "direction": "Light_dir",
            "hitpoint": "Light_hitpoint",
            "selection": "Light",
            "useflare": 1,
            "flaresize": 10,
            "flaremaxdistance": 250,
            "daylight": 1,
            # Class: CfgVehicles|rhs_uh1h_base|Reflectors|Front|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 1,
                "hardlimitstart": 100,
                "hardlimitend": 300
            }
        }
    },
    # Class: CfgVehicles|rhs_uh1h_base|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|rhs_uh1h_base|MarkerLights|CollisionLight_Red [Indent level: 2]
        "collisionlight_red": {
            "name": "CollisionLight_Red",
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 20,
            "blinking": 1,
            "blinkingpattern": [0.1,0.9],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.2,
            "drawlightcentersize": 0.04,
            # Class: CfgVehicles|rhs_uh1h_base|MarkerLights|CollisionLight_Red|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 25
            }
        },
        # Class: CfgVehicles|rhs_uh1h_base|MarkerLights|Red_Interior [Indent level: 2],
        "red_interior": {
            "name": "Interior_Red",
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 800,
            "blinking": 0,
            "drawlightsize": 0,
            "drawlightcentersize": 0,
            "blinkingpattern": [0.1,0.9],
            "blinkingpatternguarantee": 0,
            # Class: CfgVehicles|rhs_uh1h_base|MarkerLights|CollisionLight_Red|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 25
            }
        },
        # Class: CfgVehicles|rhs_uh1h_base|MarkerLights|Red_Top_Position [Indent level: 2],
        "red_top_position": {
            "name": "CollisionLight_Top_Red",
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 20,
            "blinking": 1,
            "blinkingpattern": [0.5,0.5],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.2,
            "drawlightcentersize": 0.04,
            # Class: CfgVehicles|rhs_uh1h_base|MarkerLights|CollisionLight_Red|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 25
            }
        },
        # Class: CfgVehicles|rhs_uh1h_base|MarkerLights|Green_Position [Indent level: 2],
        "green_position": {
            "name": "CollisionLight_Green",
            "color": [0.4,1,0.5],
            "ambient": [0.04,0.1,0.05],
            "intensity": 20,
            "blinking": 1,
            "blinkingpattern": [0.1,0.9],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.2,
            "drawlightcentersize": 0.04,
            # Class: CfgVehicles|rhs_uh1h_base|MarkerLights|CollisionLight_Red|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 25
            }
        }
    },
    "armor": 35,
    "armorstructural": 20,
    "hulldamagecauseexplosion": 1,
    "hullexplosiondelay": [10,20],
    # Class: CfgVehicles|rhs_uh1h_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "simulation": "RHS_Hull_Helicopter",
            "armor": -100,
            "minimalhit": -0.2,
            "explosionshielding": 2,
            "radius": 0.4,
            "armorcomponent": "Hit_Hull",
            "name": "hit_hull",
            "visual": "zbytek",
            "passthrough": 1,
            # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitHull|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Smoke [Indent level: 0]
                "rhs_hull_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Fire [Indent level: 0],
                "rhs_hull_fire": {
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Sparks [Indent level: 0],
                "rhs_hull_sparks": {
                    "type": "AirFireSparks",
                    "simulation": "particles",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Sounds [Indent level: 0],
                "rhs_hull_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Smoke_small1 [Indent level: 0],
                "rhs_hull_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "hull_fire_2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Smoke_small2 [Indent level: 0],
                "rhs_hull_smoke_small2": {
                    "position": "hull_fire_3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Fire_2 [Indent level: 0],
                "rhs_hull_fire_2": {
                    "type": "MediumDestructionFire",
                    "position": "hull_fire_2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Fire_3 [Indent level: 0],
                "rhs_hull_fire_3": {
                    "type": "MediumDestructionFire",
                    "position": "hull_fire_3",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1
            }
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": -70,
            "name": "hit_fuel",
            "visual": "-",
            "radius": 0.15,
            "explosionshielding": 1.5,
            "passthrough": 0.2
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": -12,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass1",
            "name": "glass1",
            "visual": "glass1"
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": -12,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass2",
            "name": "glass2",
            "visual": "glass2"
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "armor": -12,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass3",
            "name": "glass3",
            "visual": "glass3"
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "armor": -12,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass4",
            "name": "glass4",
            "visual": "glass4"
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "armor": -12,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass5",
            "name": "glass5",
            "visual": "glass5"
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "armor": -12,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass6",
            "name": "glass6",
            "visual": "glass6"
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "armor": -12,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass7",
            "name": "glass7",
            "visual": "glass7"
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitVRotor [Indent level: 2],
        "hitvrotor": {
            "simulation": "RHS_Hull_Helicopter",
            "armorcomponent": "Hit_Tail",
            "name": "Hit_Rotor_Tail",
            "visual": "tail rotor static",
            "armor": -80,
            "minimalhit": -0.2,
            "radius": 0.3,
            "explosionshielding": 3,
            "passthrough": 0.5,
            "convexcomponent": "tail_rotor_hit",
            "material": 51
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitHRotor [Indent level: 2],
        "hithrotor": {
            "armorcomponent": "Hit_Rotor_Main",
            "name": "Hit_Rotor_Main",
            "visual": "main rotor static",
            "armor": -90,
            "radius": 0.2,
            "explosionshielding": 0.5,
            "convexcomponent": "main_rotor_hit",
            "material": 51,
            "passthrough": 0.1
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": -40,
            "visual": "",
            "name": "elektronika",
            "radius": 0.05,
            "explosionshielding": 1.5,
            "convexcomponent": "avionics_hit",
            "material": 51,
            "passthrough": 1
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armorcomponent": "Hit_Engine",
            "armor": -80,
            "name": "motor",
            "passthrough": 0.5,
            "minimalhit": -0.12,
            "explosionshielding": 2,
            "radius": 0.27,
            "convexcomponent": "engine_hit",
            "material": 51,
            "visual": "motor"
        },
        # Class: CfgVehicles|rhs_uh1h_base|HitPoints|HitWinch [Indent level: 2],
        "hitwinch": {
            "armor": 999,
            "name": "",
            "visual": "-",
            "radius": 0.001,
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter_Base_F|HitPoints|HitEngine1 [Indent level: 2],
        "hitengine1": {
            "name": "engine_1_hit",
            "convexcomponent": "engine_1_hit",
            "explosionshielding": 1,
            "armor": 0.25,
            "material": 51,
            "visual": "motor",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter_Base_F|HitPoints|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "name": "engine_2_hit",
            "convexcomponent": "engine_2_hit",
            "explosionshielding": 1,
            "armor": 0.25,
            "material": 51,
            "visual": "motor",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter_Base_F|HitPoints|HitMissiles [Indent level: 2],
        "hitmissiles": {
            "name": "ammo_hit",
            "convexcomponent": "ammo_hit",
            "explosionshielding": 1,
            "armor": 0.1,
            "material": 51,
            "visual": "munice",
            "passthrough": 0.5
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitRGlass [Indent level: 2],
        "hitrglass": {
            "convexcomponent": "sklo predni P",
            "explosionshielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni P",
            "visual": "sklo predni P",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitLGlass [Indent level: 2],
        "hitlglass": {
            "convexcomponent": "sklo predni L",
            "explosionshielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni L",
            "visual": "sklo predni L",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitEngine3 [Indent level: 2],
        "hitengine3": {
            "name": "engine_3_hit",
            "convexcomponent": "engine_3_hit",
            "explosionshielding": 1,
            "armor": 0.25,
            "material": 51,
            "visual": "motor",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitTransmission [Indent level: 2],
        "hittransmission": {
            "armor": 0.8,
            "material": -1,
            "name": "transmission",
            "passthrough": 0.8
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitLight [Indent level: 2],
        "hitlight": {
            "armor": 0.1,
            "material": -1,
            "name": "light",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitHydraulics [Indent level: 2],
        "hithydraulics": {
            "armor": 0.8,
            "material": -1,
            "name": "hydraulics",
            "passthrough": 0.8
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitGear [Indent level: 2],
        "hitgear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitHStabilizerL1 [Indent level: 2],
        "hithstabilizerl1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerL1",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitHStabilizerR1 [Indent level: 2],
        "hithstabilizerr1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerR1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitVStabilizer1 [Indent level: 2],
        "hitvstabilizer1": {
            "armor": 0.8,
            "material": -1,
            "name": "VStabilizer1",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitTail [Indent level: 2],
        "hittail": {
            "armor": 0.8,
            "material": -1,
            "name": "tail boom",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitPitotTube [Indent level: 2],
        "hitpitottube": {
            "armor": 0.5,
            "material": -1,
            "name": "pitot tube",
            "passthrough": 0.2
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStaticPort [Indent level: 2],
        "hitstaticport": {
            "armor": 0.1,
            "material": -1,
            "name": "static port",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStarter1 [Indent level: 2],
        "hitstarter1": {
            "armor": 0.1,
            "material": -1,
            "name": "starter1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStarter2 [Indent level: 2],
        "hitstarter2": {
            "armor": 0.1,
            "material": -1,
            "name": "starter2",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStarter3 [Indent level: 2],
        "hitstarter3": {
            "armor": 0.1,
            "material": -1,
            "name": "starter3",
            "passthrough": 0
        }
    },
    # Class: CfgVehicles|rhs_uh1h_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsgref|addons|rhsgref_air|uh1h|data|uh1h.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_destruct.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_cockpit1.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_cockpit1.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_cockpit1_destruct.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_cockpit2.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_cockpit2.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_cockpit2_destruct.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_cockpit3.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_cockpit3.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_cockpit3_destruct.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_glass.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_glass_damage.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_glass_damage.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_in.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_in.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_in_destruct.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_instruments.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_instruments.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_instruments_destruct.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_rotor.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_rotor.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|uh1h_rotor_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","rhsgref|addons|rhsgref_air|uh1h|data|mlod_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    "irscanrangemin": 100,
    "irscanrangemax": 1000,
    "irscantoeyefactor": 2,
    "_generalmacro": "Helicopter_Base_H",
    # Class: CfgVehicles|Helicopter_Base_H|PilotSpec [Indent level: 1],
    "pilotspec": {
        "showheadphones": 1
    },
    # Class: CfgVehicles|Helicopter_Base_H|CargoSpec [Indent level: 1],
    "cargospec": {
        # Class: CfgVehicles|Helicopter_Base_H|CargoSpec|Cargo1 [Indent level: 2]
        "cargo1": {
            "showheadphones": 1
        }
    },
    "transportmaxweapons": 12,
    "transportmaxmagazines": 48,
    "transportmaxbackpacks": 24,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Helicopter_Base_H|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "washdowndiameter": "40.0f",
    "minsmokedamage": 0.3,
    "maxsmokedamage": 0.99,
    "selectionhrotorstill": "main rotor static",
    "selectionhrotormove": "main rotor blur",
    "selectionvrotorstill": "tail rotor static",
    "selectionvrotormove": "tail rotor blur",
    "driverrighthandanimname": "stick_pilot",
    "driverleftleganimname": "pedalL",
    "driverrightleganimname": "pedalR",
    # Class: CfgVehicles|Helicopter_Base_F|CamShake [Indent level: 1],
    "camshake": {
        "power": 30,
        "frequency": 20,
        "distance": 50,
        "minspeed": 50
    },
    "camshakecoef": 0,
    # Class: CfgVehicles|Helicopter_Base_F|EventHandlers [Indent level: 1],
    "eventhandlers": {
        "fired": "",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "simulation": "helicopterrtd",
    "unitinfotypelite": "RscUnitInfoAirRTDBasic",
    "vehicleclass": "Air",
    "gearretracting": 0,
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
    "gearuptime": 3.33,
    "geardowntime": 2,
    "gearminalt": 0.5,
    "startduration": 20,
    "maxmainrotordive": 0,
    "maxbackrotordive": 0,
    "minmainrotordive": 0,
    "minbackrotordive": 0,
    "neutralbackrotordive": 0,
    "neutralmainrotordive": 0,
    "memorypointlmissile": "L strela",
    "memorypointrmissile": "P strela",
    "memorypointlrocket": "L raketa",
    "memorypointrrocket": "P raketa",
    "memorypointgun": "",
    "memorypointpilot": "pilot",
    "_mainbladecenter": "rotor_center",
    "selectionfireanim": "zasleh",
    "envelope": [0,0.2,0.9,2.1,2.5,3.3,3.5,3.6,3.7,3.8,3.8,3,0.9,0.7,0.5],
    "minfiretime": 20,
    "steeraheadsimul": 0.5,
    "steeraheadplan": 0.7,
    # Class: CfgVehicles|Helicopter|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initanglex": 0,
        "minanglex": -40,
        "maxanglex": 17,
        "initangley": 0,
        "minangley": -100,
        "maxangley": 100,
        "initfov": 0.5,
        "minfov": 0.3,
        "maxfov": 1.2,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "weapons": [],
    "magazines": [],
    "soundlandinggear": ["",1,1],
    # Class: CfgVehicles|Helicopter|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Helicopter|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_air_helicopter_s"],
            "speechplural": ["veh_air_helicopter_p"]
        }
    },
    "editorsubcategory": "EdSubcat_Helicopters",
    "extcameraparams": [-1],
    "textsingular": "helicopter",
    "textplural": "helicopters",
    "namesound": "veh_air_helicopter_s",
    "accuracy": 0.02,
    "camouflage": 100,
    "audible": 50,
    "headgforceleaningfactor": [0.01,0.0025,0.01],
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "drivercaneject": 0,
    "damageeffect": "AirDestructionEffects",
    "type": 2,
    "dammagehalf": [],
    "dammagefull": [],
    "crewvulnerable": 1,
    "explosionshielding": 4,
    "mintotaldamagethreshold": 0.005,
    # Class: CfgVehicles|Helicopter|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "mainbladecenter": "rotor_center",
    "tailbladecenter": "rotor_02_center",
    "tailbladevertical": 1,
    "slingloadmincargomass": 0,
    "formationx": 50,
    "formationz": 100,
    "precision": 100,
    "brakedistance": 200,
    "formationtime": 10,
    "gearsupfrictioncoef": 0.5,
    "airbrakefrictioncoef": 3,
    "airfrictioncoefs2": [0.001,0.0005,6e-005],
    "airfrictioncoefs1": [0.1,0.05,0.006],
    "airfrictioncoefs0": [0,0,0],
    # Class: CfgVehicles|Air|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|Air|Components|TransportCountermeasuresComponent [Indent level: 2]
        "transportcountermeasurescomponent": {
        }
    },
    "altfullforce": 2000,
    "altnoforce": 6000,
    "cost": 1e+007,
    "attenuationeffecttype": "",
    "insidesoundcoef": 0.0316228,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "nightvision": 0,
    "drivercompartments": 0,
    "enablegps": 1,
    "weaponsgroup1": "1 + 		2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    # Class: CfgVehicles|Air|DustEffects [Indent level: 1],
    "dusteffects": {
        # Class: CfgDustEffectsAir|Both [Indent level: 0]
        "both": {
        },
        # Class: CfgDustEffectsAir|Left [Indent level: 0],
        "left": {
            "default": ["LDustEffectsAir"],
            "gdtstratisconcrete": ["LDustEffectsAir","LDirtEffects"],
            "gdtstratisbeach": ["LDustEffectsAir","LStonesEffects"],
            "gdtstratisdirt": ["LDustEffectsAir","LDirtEffects"],
            "gdtstratisseabedcluttered": ["LDustEffectsAir"],
            "gdtstratisseabed": ["LDustEffectsAir"],
            "gdtstratisdrygrass": ["LDustEffectsAir","LGrassDryEffects","LDirtEffects"],
            "gdtstratisgreengrass": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstratisrocky": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstratisthistles": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtconcrete": ["LDustEffectsAir","LDirtEffects"],
            "gdtasphalt": ["LDustEffectsAir","LDirtEffects"],
            "gdtrubble": ["LDustEffectsAir","LDirtEffects"],
            "gdtsoil": ["LDustEffectsAir","LDirtEffects"],
            "gdtbeach": ["LDustEffectsAir","LStonesEffects"],
            "gdtrock": ["LDustEffectsAir","LDirtEffects"],
            "gdtdead": ["LDustEffectsAir","LDirtEffects"],
            "gdtdesert1": ["LDustEffectsAir","LSandEffects","LDirtEffects","LStonesEffects"],
            "gdtdesert2": ["LDustEffectsAir","LSandEffects","LGrassEffects","LDirtEffects"],
            "gdtdirt": ["LDustEffectsAir","LDirtEffects"],
            "gdtgrassgreen": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtgrassdry": ["LDustEffectsAir","LGrassDryEffects","LDirtEffects"],
            "gdtgrasswild": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtwildfield": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtweed1": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtweed2": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtthorn": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstony": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstonygreen": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstonythistle": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtseabeddeep": ["LDustEffectsAir"],
            "gdtseabed": ["LDustEffectsAir"],
            "surfroaddirt": ["LDustEffectsAir"],
            "surfroadconcrete": ["LDustEffectsAir"],
            "surfroadtarmac": ["LDustEffectsAir"],
            "surfwood": ["LDustEffectsAir"],
            "surfmetal": ["LDustEffectsAir"],
            "surfrooftin": ["LDustEffectsAir"],
            "surfrooftiles": ["LDustEffectsAir"],
            "surfintwood": ["LDustEffectsAir"],
            "surfintconcrete": ["LDustEffectsAir"],
            "surfinttiles": ["LDustEffectsAir"],
            "surfintmetal": ["LDustEffectsAir"],
            "gdtgrassshort": ["LDustEffectsAir","LGrassEffects"],
            "gdtgrasstall": ["LDustEffectsAir","LGrassEffects"],
            "gdtreddirt": ["LDustEffectsAirRed"],
            "gdtfield": ["LDustEffectsAir"],
            "gdtforest": ["LDustEffectsAir"],
            "gdtvolcano": ["LDustEffectsAir","LStonesEffects"],
            "gdtcliff": ["LDustEffectsAir"],
            "gdtvolcanobeach": ["LDustEffectsAir"],
            "surfroaddirt_exp": ["LDustEffectsAirRed"],
            "surfroadconcrete_exp": ["LDustEffectsAir"],
            "surfroadtarmac_exp": ["LDustEffectsAir"],
            "gdtkldirt": ["LDustEffectsAir"],
            "gdtklgrass1": ["LDustEffectsAir","LGrassEffects"],
            "gdtklgrass2": ["LDustEffectsAir","LGrassEffects"],
            "gdtklforestcon": ["LDustEffectsAir"],
            "gdtklforestdec": ["LDustEffectsAir"],
            "gdtklmud": ["LDustEffectsAir"],
            "gdtklsoil": ["LDustEffectsAir"],
            "gdtkltarmac": ["LDustEffectsAir"],
            "gdtklstubble": ["LDustEffectsAir"],
            "gdtklstones": ["LDustEffectsAir"],
            "surfroaddirt_enoch": ["LDustEffectsAir"],
            "surftraildirt_enoch": ["LDustEffectsAir"],
            "surfroadtarmac1_enoch": ["LDustEffectsAir"],
            "surfroadtarmac2_enoch": ["LDustEffectsAir"],
            "surfroadtarmac3_enoch": ["LDustEffectsAir"]
        },
        # Class: CfgDustEffectsAir|Right [Indent level: 0],
        "right": {
            "default": ["RDustEffectsAir"],
            "gdtstratisconcrete": ["RDustEffectsAir","RDirtEffects"],
            "gdtstratisbeach": ["RDustEffectsAir","RStonesEffects"],
            "gdtstratisdirt": ["RDustEffectsAir","RDirtEffects"],
            "gdtstratisseabedcluttered": ["RDustEffectsAir"],
            "gdtstratisseabed": ["RDustEffectsAir"],
            "gdtstratisdrygrass": ["RDustEffectsAir","RGrassDryEffects","RDirtEffects"],
            "gdtstratisgreengrass": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstratisrocky": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstratisthistles": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtconcrete": ["RDustEffectsAir","RDirtEffects"],
            "gdtasphalt": ["RDustEffectsAir","RDirtEffects"],
            "gdtrubble": ["RDustEffectsAir","RDirtEffects"],
            "gdtsoil": ["RDustEffectsAir","RDirtEffects"],
            "gdtbeach": ["RDustEffectsAir","RStonesEffects"],
            "gdtrock": ["RDustEffectsAir","RDirtEffects"],
            "gdtdead": ["RDustEffectsAir","RDirtEffects"],
            "gdtdesert1": ["RDustEffectsAir","RSandEffects","RDirtEffects","RStonesEffects"],
            "gdtdesert2": ["RDustEffectsAir","RSandEffects","RGrassEffects","RDirtEffects"],
            "gdtdirt": ["RDustEffectsAir","RDirtEffects"],
            "gdtgrassgreen": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtgrassdry": ["RDustEffectsAir","RGrassDryEffects","RDirtEffects"],
            "gdtgrasswild": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtwildfield": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtweed1": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtweed2": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtthorn": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstony": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstonygreen": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstonythistle": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtseabeddeep": ["RDustEffectsAir"],
            "gdtseabed": ["RDustEffectsAir"],
            "surfroaddirt": ["RDustEffectsAir"],
            "surfroadconcrete": ["RDustEffectsAir"],
            "surfroadtarmac": ["RDustEffectsAir"],
            "surfwood": ["RDustEffectsAir"],
            "surfmetal": ["RDustEffectsAir"],
            "surfrooftin": ["RDustEffectsAir"],
            "surfrooftiles": ["RDustEffectsAir"],
            "surfintwood": ["RDustEffectsAir"],
            "surfintconcrete": ["RDustEffectsAir"],
            "surfinttiles": ["RDustEffectsAir"],
            "surfintmetal": ["RDustEffectsAir"],
            "gdtgrassshort": ["RDustEffectsAir","RGrassEffects"],
            "gdtgrasstall": ["RDustEffectsAir","RGrassEffects"],
            "gdtreddirt": ["RDustEffectsAirRed"],
            "gdtfield": ["RDustEffectsAir"],
            "gdtforest": ["RDustEffectsAir"],
            "gdtvolcano": ["RDustEffectsAir","RStonesEffects"],
            "gdtcliff": ["RDustEffectsAir"],
            "gdtvolcanobeach": ["RDustEffectsAir"],
            "surfroaddirt_exp": ["RDustEffectsAirRed"],
            "surfroadconcrete_exp": ["RDustEffectsAir"],
            "surfroadtarmac_exp": ["RDustEffectsAir"],
            "gdtkldirt": ["RDustEffectsAir"],
            "gdtklgrass1": ["RDustEffectsAir","RGrassEffects"],
            "gdtklgrass2": ["RDustEffectsAir","RGrassEffects"],
            "gdtklforestcon": ["RDustEffectsAir"],
            "gdtklforestdec": ["RDustEffectsAir"],
            "gdtklmud": ["RDustEffectsAir"],
            "gdtklsoil": ["RDustEffectsAir"],
            "gdtkltarmac": ["RDustEffectsAir"],
            "gdtklstubble": ["RDustEffectsAir"],
            "gdtklstones": ["RDustEffectsAir"],
            "surfroaddirt_enoch": ["RDustEffectsAir"],
            "surftraildirt_enoch": ["RDustEffectsAir"],
            "surfroadtarmac1_enoch": ["RDustEffectsAir"],
            "surfroadtarmac2_enoch": ["RDustEffectsAir"],
            "surfroadtarmac3_enoch": ["RDustEffectsAir"]
        }
    },
    "waterleakiness": 100,
    "waterresistance": 1,
    "impacteffectssea": "ImpactEffectsAir",
    "flarevelocity": 100,
    "enableradio": 1,
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "countermeasureactivationradius": 10000,
    # Class: CfgVehicles|Air|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 0.2,
        "frequency": 3,
        "distance": 0,
        "minspeed": 1
    },
    # Class: CfgVehicles|Air|camShakeDamage [Indent level: 1],
    "camshakedamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minspeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "secondaryexplosion": -1,
    "fuelexplosionpower": 1,
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "squadtitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memorypointdriveroptics": ["driverview","pilot"],
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsgetincargoprecise": ["pos cargo"],
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "memorypointtaskmarker": "",
    "selectionclan": "clan",
    "selectiondashboard": "podsvit pristroju",
    "selectionshowdamage": "poskozeni",
    "selectionbacklights": "zadni svetlo",
    # Class: CfgVehicles|AllVehicles|NewTurret [Indent level: 1],
    "newturret": {
        "body": "mainTurret",
        "gun": "mainGun",
        "animationsourcebody": "mainTurret",
        "animationsourcegun": "mainGun",
        "animationsourcehatch": "hatchGunner",
        "animationsourcecamelev": "camElev",
        "proxytype": "CPGunner",
        "proxyindex": 1,
        "gunnername": "Gunner",
        "gunnertype": "",
        "primarygunner": 1,
        "primaryobserver": 0,
        "weapons": [],
        "magazines": [],
        "soundservo": ["",0.00316228,1],
        "soundelevation": ["",0.00316228,1],
        "minelev": -4,
        "maxelev": 20,
        "initelev": 0,
        "minturn": -360,
        "maxturn": 360,
        "initturn": 0,
        "minoutelev": -4,
        "maxoutelev": 20,
        "initoutelev": 0,
        "minoutturn": -60,
        "maxoutturn": 60,
        "initoutturn": 0,
        "maxhorizontalrotspeed": 1.2,
        "maxverticalrotspeed": 1.2,
        "mincamelev": -90,
        "maxcamelev": 90,
        "initcamelev": 0,
        "stabilizedinaxes": 3,
        "primary": 1,
        "hasgunner": 1,
        "commanding": 1,
        "gunnergetinaction": "",
        "gunnergetoutaction": "",
        "turretcansee": 0,
        "canusescanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewGunner [Indent level: 2],
        "viewgunner": {
            "initanglex": 5,
            "minanglex": -75,
            "maxanglex": 85,
            "initangley": 0,
            "minangley": -150,
            "maxangley": 150,
            "minfov": 0.25,
            "maxfov": 1.25,
            "initfov": 0.75,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "continuous": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "turretspec": {
            "showheadphones": 0
        },
        "gunneropticsmodel": "",
        "gunneropticscolor": [0,0,0,1],
        "gunnerforceoptics": 1,
        "gunneropticsshowcursor": 0,
        "turretinfotype": "",
        "gunneroutopticsmodel": "",
        "gunneroutopticscolor": [0,0,0,1],
        "gunneropticseffect": [],
        "gunneroutopticseffect": [],
        "memorypointgunneroutoptics": "",
        "gunneroutforceoptics": 0,
        "gunneroutopticsshowcursor": 0,
        "gunnerfirealsoininternalcamera": 1,
        "gunneroutfirealsoininternalcamera": 1,
        "gunnerusespilotview": 0,
        "castgunnershadow": 0,
        "viewgunnershadow": 1,
        "viewgunnershadowdiff": 1,
        "viewgunnershadowamb": 1,
        "ejectdeadgunner": 0,
        "hideweaponsgunner": 1,
        "canhidegunner": -1,
        "forcehidegunner": 0,
        "outgunnermayfire": 0,
        "ingunnermayfire": 1,
        "showhmd": 0,
        "viewgunnerinexternal": 0,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "gunnercompartments": "Compartment1",
        "lodturnedin": -1,
        "lodturnedout": -1,
        "startengine": 1,
        "memorypointsgetingunnerprecise": "",
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "armorlights": 0.4,
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "reflectors": {
        },
        "aggregatereflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
        "gunfire": {
            "access": 0,
            "cloudletduration": 0.2,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletFire",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: WeaponFireGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
        "gunclouds": {
            "access": 0,
            "cloudletduration": 0.3,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 1,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletaccy": 0.4,
            "cloudletminyspeed": 0.2,
            "cloudletmaxyspeed": 0.8,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
        "mgunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints [Indent level: 2],
        "hitpoints": {
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitTurret [Indent level: 3]
            "hitturret": {
                "armor": 0.8,
                "material": 51,
                "name": "turret",
                "visual": "turret",
                "passthrough": 1,
                "explosionshielding": 1
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitGun [Indent level: 3],
            "hitgun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passthrough": 1,
                "explosionshielding": 1
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "turrets": {
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
        "viewoptics": {
            "initanglex": 0,
            "minanglex": -30,
            "maxanglex": 30,
            "initangley": 0,
            "minangley": -100,
            "maxangley": 100,
            "initfov": 0.3,
            "minfov": 0.07,
            "maxfov": 0.35,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        "forcenvg": 0,
        "iscopilot": 0,
        "caneject": 1,
        "gunnerlefthandanimname": "",
        "gunnerrighthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnerrightleganimname": "",
        "gunnerdoor": "",
        "precisegetinout": 0,
        "turretfollowfreelook": 0,
        "allowtablock": 1,
        "showalltargets": 0,
        "dontcreateai": 0,
        "disablesoundattenuation": 0,
        "slingloadoperator": 0,
        "playerposition": 0,
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "turnin": {
            "turnoffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
        "turnout": {
            "turnoffset": 0
        },
        "gunnerinaction": "ManActTestDriver",
        "gunneraction": "ManActTestDriver",
        "gunbeg": "usti hlavne",
        "gunend": "konec hlavne",
        "memorypointgunneroptics": "gunnerview",
        "memorypointsgetingunner": "pos gunner",
        "memorypointsgetingunnerdir": "pos gunner dir",
        "memorypointgun": "kulas",
        "selectionfireanim": "zasleh",
        "showcrewaim": 0
    },
    # Class: CfgVehicles|AllVehicles|ViewCargo [Indent level: 1],
    "viewcargo": {
        "initanglex": 5,
        "minanglex": -75,
        "maxanglex": 85,
        "initangley": 0,
        "minangley": -150,
        "maxangley": 150,
        "minfov": 0.25,
        "maxfov": 1.25,
        "initfov": 0.75,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|AllVehicles|SoundEvents [Indent level: 1],
    "soundevents": {
    },
    "tracksspeed": 0,
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    # Class: CfgVehicles|AllVehicles|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    "cargodoors": [],
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "cargoprecisegetinout": [0],
    "waterppinvehicle": 1,
    "htmin": 60,
    "htmax": 1800,
    "afmax": 200,
    "mfmax": 100,
    "mfact": 0.2,
    "tbody": 150,
    "impacteffectspeedlimit": 8,
    # Class: CfgVehicles|AllVehicles|CargoTurret [Indent level: 1],
    "cargoturret": {
        # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2]
        "viewgunner": {
            "initanglex": 5,
            "minanglex": -75,
            "maxanglex": 85,
            "initangley": 0,
            "minangley": -150,
            "maxangley": 150,
            "minfov": 0.25,
            "maxfov": 1.25,
            "initfov": 0.75,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        # Class: CfgVehicles|AllVehicles|CargoTurret|Hitpoints [Indent level: 2],
        "hitpoints": {
        },
        "animationsourcebody": "",
        "animationsourcegun": "",
        "body": "",
        "caneject": 1,
        "commanding": 0,
        "dontcreateai": 1,
        "gun": "",
        "gunnergetinaction": "GetInLow",
        "gunnergetoutaction": "GetOutLow",
        "gunnername": "cargo",
        "hideweaponsgunner": 0,
        "iscopilot": 0,
        "memorypointsgetingunner": "pos cargo",
        "memorypointsgetingunnerdir": "pos cargo dir",
        "primarygunner": 0,
        "proxytype": "CPCargo",
        "startengine": 0,
        "turretfollowfreelook": 0,
        "viewgunnerinexternal": 1,
        "disablesoundattenuation": 1,
        "outgunnermayfire": 1,
        "ispersonturret": 1,
        "showascargo": 1,
        "maxelev": 45,
        "minelev": -45,
        "maxturn": 95,
        "minturn": -95,
        "animationsourcehatch": "hatchGunner",
        "animationsourcecamelev": "camElev",
        "proxyindex": 1,
        "gunnertype": "",
        "primaryobserver": 0,
        "weapons": [],
        "magazines": [],
        "soundservo": ["",0.00316228,1],
        "soundelevation": ["",0.00316228,1],
        "initelev": 0,
        "initturn": 0,
        "minoutelev": -4,
        "maxoutelev": 20,
        "initoutelev": 0,
        "minoutturn": -60,
        "maxoutturn": 60,
        "initoutturn": 0,
        "maxhorizontalrotspeed": 1.2,
        "maxverticalrotspeed": 1.2,
        "mincamelev": -90,
        "maxcamelev": 90,
        "initcamelev": 0,
        "stabilizedinaxes": 3,
        "primary": 1,
        "hasgunner": 1,
        "turretcansee": 0,
        "canusescanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "turretspec": {
            "showheadphones": 0
        },
        "gunneropticsmodel": "",
        "gunneropticscolor": [0,0,0,1],
        "gunnerforceoptics": 1,
        "gunneropticsshowcursor": 0,
        "turretinfotype": "",
        "gunneroutopticsmodel": "",
        "gunneroutopticscolor": [0,0,0,1],
        "gunneropticseffect": [],
        "gunneroutopticseffect": [],
        "memorypointgunneroutoptics": "",
        "gunneroutforceoptics": 0,
        "gunneroutopticsshowcursor": 0,
        "gunnerfirealsoininternalcamera": 1,
        "gunneroutfirealsoininternalcamera": 1,
        "gunnerusespilotview": 0,
        "castgunnershadow": 0,
        "viewgunnershadow": 1,
        "viewgunnershadowdiff": 1,
        "viewgunnershadowamb": 1,
        "ejectdeadgunner": 0,
        "canhidegunner": -1,
        "forcehidegunner": 0,
        "ingunnermayfire": 1,
        "showhmd": 0,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "gunnercompartments": "Compartment1",
        "lodturnedin": -1,
        "lodturnedout": -1,
        "memorypointsgetingunnerprecise": "",
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "armorlights": 0.4,
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "reflectors": {
        },
        "aggregatereflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
        "gunfire": {
            "access": 0,
            "cloudletduration": 0.2,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletFire",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: WeaponFireGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
        "gunclouds": {
            "access": 0,
            "cloudletduration": 0.3,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 1,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletaccy": 0.4,
            "cloudletminyspeed": 0.2,
            "cloudletmaxyspeed": 0.8,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
        "mgunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "turrets": {
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
        "viewoptics": {
            "initanglex": 0,
            "minanglex": -30,
            "maxanglex": 30,
            "initangley": 0,
            "minangley": -100,
            "maxangley": 100,
            "initfov": 0.3,
            "minfov": 0.07,
            "maxfov": 0.35,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        "forcenvg": 0,
        "gunnerlefthandanimname": "",
        "gunnerrighthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnerrightleganimname": "",
        "gunnerdoor": "",
        "precisegetinout": 0,
        "allowtablock": 1,
        "showalltargets": 0,
        "slingloadoperator": 0,
        "playerposition": 0,
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "turnin": {
            "turnoffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
        "turnout": {
            "turnoffset": 0
        },
        "gunnerinaction": "ManActTestDriver",
        "gunneraction": "ManActTestDriver",
        "gunbeg": "usti hlavne",
        "gunend": "konec hlavne",
        "memorypointgunneroptics": "gunnerview",
        "memorypointgun": "kulas",
        "selectionfireanim": "zasleh",
        "showcrewaim": 0
    },
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "access": 0,
    "reversed": 1,
    "autocenter": 1,
    "animated": 1,
    "shadow": 1,
    "featuretype": 0,
    "speechsingular": [],
    "speechplural": [],
    "maxdetectrange": 20,
    "detectskill": 20,
    "minealerticonrange": 200,
    "killfriendlyexpcoef": 1,
    "weaponslots": 0,
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "obstructsoundlfratio": 0,
    "occludesoundlfratio": 0.25,
    "unloadincombat": 0,
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmin": 20,
    "antirollbarspeedmax": 60,
    "slowspeedforwardcoef": 0.3,
    "normalspeedforwardcoef": 0.85,
    "gunnerhasflares": 1,
    "sensitivityear": 0.0075,
    "portrait": "",
    "ghostpreview": "",
    "armorlights": 0.4,
    "replacedamaged": "",
    "replacedamagedlimit": 0.9,
    "replacedamagedhitpoints": [],
    "keepinepesceneafterdeath": 0,
    "groupcameraposition": [0,5,-30],
    "camerasmoothspeed": 5,
    "predictturnsimul": 1.2,
    "predictturnplan": 1,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitciviliancoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "alwaystarget": 0,
    "irscanground": 1,
    "lasertarget": 0,
    "laserscanner": 0,
    "nvtarget": 0,
    "nvscanner": 0,
    "artillerytarget": 0,
    "artilleryscanner": 0,
    "canusescanners": 1,
    "preferroads": 0,
    "hideunitinfo": 0,
    "limitedspeedcoef": 0.22,
    "hasdriver": 1,
    "driverforceoptics": 0,
    "hideweaponscargo": 0,
    "enablewatch": 0,
    "useprecisegetinaction": 0,
    "allowtablock": 1,
    "showalltargets": 0,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "wheelcircumference": 1,
    "waterresistancecoef": 0.5,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterangulardampingcoef": 0,
    "shownvgdriver": 0,
    "shownvgcommander": 0,
    "shownvggunner": 0,
    "shownvgcargo": [0],
    "soundattenuationcargo": [1],
    "countsforscoreboard": 1,
    # Class: CfgVehicles|All|NVGMarkers [Indent level: 1],
    "nvgmarkers": {
    },
    # Class: CfgVehicles|All|NVGMarker [Indent level: 1],
    "nvgmarker": {
        "diffuse": [1,1,1,1],
        "ambient": [1,1,1,1],
        "brightness": 1,
        "blinking": 0,
        "onlyinnvg": 0
    },
    # Class: CfgVehicles|All|HeadLimits [Indent level: 1],
    "headlimits": {
        "initanglex": 5,
        "minanglex": -30,
        "maxanglex": 40,
        "initangley": 0,
        "minangley": -90,
        "maxangley": 90,
        "minanglez": -45,
        "maxanglez": 45,
        "rotzradius": 0.2
    },
    "transportammo": 0,
    "isbackpack": 0,
    "transportfuel": 0,
    "transportrepair": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "attendant": 0,
    "engineer": 0,
    "uavhacker": 0,
    "soundengine": ["",1,1],
    "soundenviron": ["",1,1],
    # Class: CfgVehicles|All|SoundEnvironExt [Indent level: 1],
    "soundenvironext": {
    },
    # Class: CfgVehicles|All|SoundEquipment [Indent level: 1],
    "soundequipment": {
    },
    # Class: CfgVehicles|All|SoundGear [Indent level: 1],
    "soundgear": {
    },
    # Class: CfgVehicles|All|SoundBreath [Indent level: 1],
    "soundbreath": {
    },
    # Class: CfgVehicles|All|SoundBreathSwimming [Indent level: 1],
    "soundbreathswimming": {
    },
    # Class: CfgVehicles|All|SoundBreathInjured [Indent level: 1],
    "soundbreathinjured": {
    },
    # Class: CfgVehicles|All|SoundHitScream [Indent level: 1],
    "soundhitscream": {
    },
    # Class: CfgVehicles|All|SoundInjured [Indent level: 1],
    "soundinjured": {
    },
    # Class: CfgVehicles|All|SoundBreathAutomatic [Indent level: 1],
    "soundbreathautomatic": {
    },
    # Class: CfgVehicles|All|SoundDrown [Indent level: 1],
    "sounddrown": {
    },
    # Class: CfgVehicles|All|SoundChoke [Indent level: 1],
    "soundchoke": {
    },
    # Class: CfgVehicles|All|SoundRecovered [Indent level: 1],
    "soundrecovered": {
    },
    # Class: CfgVehicles|All|SoundBurning [Indent level: 1],
    "soundburning": {
    },
    # Class: CfgVehicles|All|PulsationSound [Indent level: 1],
    "pulsationsound": {
    },
    # Class: CfgVehicles|All|SoundDrowning [Indent level: 1],
    "sounddrowning": {
    },
    "soundcrash": ["",0.316228,1],
    "soundlandcrash": ["",1,1],
    "soundwatercrash": ["",0.177828,1],
    "soundservo": ["",0.00316228,0.5],
    "soundelevation": ["",0.00316228,0.5],
    "sounddamage": ["",1,1],
    "soundgearup": ["",1,1],
    "soundgeardown": ["",1,1],
    "soundflapsup": ["",1,1],
    "soundflapsdown": ["",1,1],
    "cabinopensound": ["",1,1],
    "cabinclosesound": ["",1,1],
    "cabinopensoundinternal": ["",1,1],
    "cabinclosesoundinternal": ["",1,1],
    "emptysound": ["",0,1],
    "aggregatereflectors": [],
    "cargoiscodriver": [0],
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "hideproxyincombat": 0,
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
    "ejectdeaddriver": 0,
    "ejectdeadcargo": 0,
    "hiddenselectionsmaterials": [],
    "hiddenunderwaterselections": [],
    "shownunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    # Class: CfgVehicles|All|FxExplo [Indent level: 1],
    "fxexplo": {
        "access": 1
    },
    # Class: CfgVehicles|All|GunFire [Indent level: 1],
    "gunfire": {
        "access": 0,
        "cloudletduration": 0.2,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletgrowup": 0.2,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 0.5,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletFire",
        "cloudletcolor": [1,1,1,0],
        "interval": 0.01,
        "size": 3,
        "sourcesize": 0.5,
        "timetolive": 0,
        "initt": 4500,
        "deltat": -3000,
        # Class: WeaponFireGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponFireGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun|Table|T1 [Indent level: 1],
            "t1": {
                "maxt": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun|Table|T2 [Indent level: 1],
            "t2": {
                "maxt": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun|Table|T3 [Indent level: 1],
            "t3": {
                "maxt": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun|Table|T4 [Indent level: 1],
            "t4": {
                "maxt": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun|Table|T5 [Indent level: 1],
            "t5": {
                "maxt": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun|Table|T6 [Indent level: 1],
            "t6": {
                "maxt": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun|Table|T7 [Indent level: 1],
            "t7": {
                "maxt": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun|Table|T8 [Indent level: 1],
            "t8": {
                "maxt": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun|Table|T9 [Indent level: 1],
            "t9": {
                "maxt": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun|Table|T10 [Indent level: 1],
            "t10": {
                "maxt": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun|Table|T11 [Indent level: 1],
            "t11": {
                "maxt": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun|Table|T12 [Indent level: 1],
            "t12": {
                "maxt": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun|Table|T13 [Indent level: 1],
            "t13": {
                "maxt": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun|Table|T14 [Indent level: 1],
            "t14": {
                "maxt": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun|Table|T15 [Indent level: 1],
            "t15": {
                "maxt": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun|Table|T16 [Indent level: 1],
            "t16": {
                "maxt": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun|Table|T17 [Indent level: 1],
            "t17": {
                "maxt": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun|Table|T18 [Indent level: 1],
            "t18": {
                "maxt": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun|Table|T19 [Indent level: 1],
            "t19": {
                "maxt": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun|Table|T20 [Indent level: 1],
            "t20": {
                "maxt": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun|Table|T21 [Indent level: 1],
            "t21": {
                "maxt": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun|Table|T22 [Indent level: 1],
            "t22": {
                "maxt": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|All|GunClouds [Indent level: 1],
    "gunclouds": {
        "access": 0,
        "cloudletduration": 0.3,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletgrowup": 1,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 1,
        "cloudletaccy": 0.4,
        "cloudletminyspeed": 0.2,
        "cloudletmaxyspeed": 0.8,
        "cloudletshape": "cloudletClouds",
        "cloudletcolor": [1,1,1,0],
        "interval": 0.05,
        "size": 3,
        "sourcesize": 0.5,
        "timetolive": 0,
        "initt": 0,
        "deltat": 0,
        # Class: WeaponCloudsGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|All|MGunClouds [Indent level: 1],
    "mgunclouds": {
        "access": 0,
        "cloudletgrowup": 0.05,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.1,
        "cloudletduration": 0.05,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 0.3,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletClouds",
        "cloudletcolor": [1,1,1,0],
        "timetolive": 0,
        "interval": 0.02,
        "size": 0.3,
        "sourcesize": 0.02,
        "initt": 0,
        "deltat": 0,
        # Class: WeaponCloudsMGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "selectiondamage": "zbytek",
    "headaimdown": 0,
    "cargocaneject": 1,
    "fireresistance": 10,
    "aircapacity": 10,
    "waterdamageengine": 0.2,
    "damagetexdelay": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "windsockexist": 0,
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "numberphysicalwheels": 0,
    "damagehalf": [],
    "damagefull": [],
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "features": "",
    "insidedetectcoef": 0.05,
}