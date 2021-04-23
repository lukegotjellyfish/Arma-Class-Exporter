rhsusf_cgrcat1a2_usmc_d = {
    "editorpreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_CGRCAT1A2_usmc_d.paa",
    "displayname": "CGR CAT1A2",
    "picture": "rhsusf|addons|rhsusf_cougar|pictures|rhs_cgrcat1a2_unarmed_pic_ca.paa",
    "scope": 2,
    "accuracy": 0.5,
    "faction": "rhs_faction_usmc_d",
    "crew": "rhsusf_usmc_marpat_d_rifleman_m4",
    "author": "Red Hammer Studios",
    "hiddenselectionstextures": ["rhsusf|addons|rhsusf_cougar|data|CGR_Body_CO.paa","rhsusf|addons|rhsusf_cougar|data|CGR_Labels_CA.paa","rhsusf|addons|rhsusf_rg33l|data|MCTAGS_CO.paa","rhsusf|addons|rhsusf_hmmwv|textures|mk64mount_d_co.paa"],
    "dlc": "RHS_USAF",
    "category": "Car",
    "side": 1,
    "editorsubcategory": "rhs_EdSubcat_mrap",
    "vehicleclass": "rhs_vehclass_MRAP",
    "insidesoundcoef": 0.4,
    "unitinfotype": "RscUnitInfo",
    "weapons": ["TruckHorn2","rhsusf_weap_duke"],
    "magazines": ["rhsusf_mag_duke"],
    "model": "rhsusf|addons|rhsusf_cougar|CGRCAT1A2",
    "icon": "a3|soft_f_beta|Truck_01|Data|UI|map_truck_01_CA.paa",
    "mapsize": 12.02,
    "transportmaxbackpacks": 25,
    "transportsoldier": 4,
    "destrtype": "DestructDefault",
    "crewexplosionprotection": 1,
    "camshakecoef": 0.3,
    "dustfrontleftpos": "wheel_1_1_bound",
    "dustfrontrightpos": "wheel_2_1_bound",
    "dustbackleftpos": "wheel_1_2_bound",
    "dustbackrightpos": "wheel_2_2_bound",
    "tf_haslrradio_api": 1,
    "selectionbrakelights": "light_brake",
    "selectionbacklights": "light_drive",
    "driveraction": "RHS_cougar_Driver",
    "driverinaction": "RHS_cougar_Driver",
    "driverlefthandanimname": "drivewheel",
    "driverrighthandanimname": "drivewheel",
    "cargoaction": ["passenger_APC_narrow_generic01_ns","passenger_APC_generic04_ns","passenger_APC_generic04_ns","passenger_APC_generic03_ns"],
    "cargoproxyindexes": [1,2,3,5],
    "getinproxyorder": [1,2,3,4,5],
    "memorypointsgetincargo": ["pos codriver","pos cargo"],
    "memorypointsgetincargodir": ["pos codriver dir","pos cargo dir"],
    "getinaction": "GetInMRAP_01",
    "getoutaction": "GetOutMRAP_01",
    "driverdoor": "DoorL",
    "cargodoors": ["DoorR","DoorB"],
    "viewdriverinexternal": 1,
    "forcehidedriver": 1,
    "hiddenselections": ["camo","camo1","camo2","pintle"],
    # Class: CfgVehicles|rhsusf_Cougar_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhsusf_Cougar_base|textureSources|rhs_desert [Indent level: 2]
        "rhs_desert": {
            "displayname": "Desert",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_cougar|data|CGR_Body_CO.paa","rhsusf|addons|rhsusf_cougar|data|CGR_Labels_CA.paa","rhsusf|addons|rhsusf_rg33l|data|MCTAGS_CO.paa","rhsusf|addons|rhsusf_hmmwv|textures|mk64mount_d_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|textureSources|rhs_woodland [Indent level: 2],
        "rhs_woodland": {
            "displayname": "Woodland",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_cougar|data|CGR_Body_WD_CO.paa","rhsusf|addons|rhsusf_cougar|data|CGR_Labels_CA.paa","rhsusf|addons|rhsusf_rg33l|data|MCTAGS_WD_CO.paa","rhsusf|addons|rhsusf_hmmwv|textures|mk64mount_w_co.paa"],
            "factions": []
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|rhsusf_Cougar_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhsusf_Cougar_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Attributes|rhs_hideDUKE [Indent level: 2],
        "rhs_hideduke": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "hide DUKE antennas",
            "property": "rhs_hideDUKE",
            "expression": "_this animate ['DUKE_Hide',_value,true];if(_value isEqualTo 1)then{_this removeWeaponTurret ['rhsusf_weap_duke',[-1]]};"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Attributes|DoorB [Indent level: 2],
        "doorb": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open rear door",
            "property": "Door_B",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Attributes|DoorL [Indent level: 2],
        "doorl": {
            "displayname": "Open left door",
            "property": "Door_L",
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Attributes|DoorR [Indent level: 2],
        "doorr": {
            "displayname": "Open right door",
            "property": "Door_R",
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        }
    },
    "cargocompartments": [1,1],
    # Class: CfgVehicles|rhsusf_Cougar_base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhsusf_Cougar_base|Turrets|CargoTurret_01 [Indent level: 2]
        "cargoturret_01": {
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunneraction": "rhs_cougar_turnout_1",
            "gunnerinaction": "RHS_cougar_Cargo01_FFV",
            "animationsourcehatch": "hatch1",
            "enabledbyanimationsource": "hatch1_door",
            "ispersonturret": 2,
            "gunnergetinaction": "GetInMantis",
            "gunnergetoutaction": "GetOutMantis",
            "memorypointsgetingunner": "pos cargoFFV1",
            "memorypointsgetingunnerdir": "pos cargoFFV1 dir",
            "rhs_hatch_control": 1,
            "gunnername": "Passenger (Rear Hatch)",
            "gunnercompartments": "Compartment1",
            "gunnerdoor": "DoorB",
            "memorypointgunneroptics": "",
            "selectionfireanim": "",
            "canhidegunner": 1,
            "commanding": -2,
            "lodturnedin": 1200,
            "lodturnedout": 0,
            "proxyindex": 4,
            "maxelev": 45,
            "minelev": -35,
            "maxturn": 61,
            "minturn": -65,
            # Class: CfgVehicles|rhsusf_Cougar_base|Turrets|CargoTurret_01|TurnIn [Indent level: 3],
            "turnin": {
                "limitsarraytop": [[0,0],[0,0]],
                "limitsarraybottom": [[0,0],[0,0]]
            },
            # Class: CfgVehicles|rhsusf_Cougar_base|Turrets|CargoTurret_01|TurnOut [Indent level: 3],
            "turnout": {
                "limitsarraytop": [[45,-90.1745],[44.9894,80.629]],
                "limitsarraybottom": [[5.464,-89.894],[-9.4602,-71.7306],[-7.5523,-40.9866],[-16.3809,-30.7844],[-7.1172,-30.2764],[-13.0122,-5.9314],[-12.7133,26.3332],[-23.1407,58.6419],[-8.5688,77.4948],[-7.292,80.6933]]
            },
            # Class: CfgVehicles|rhsusf_Cougar_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
            "dontcreateai": 1,
            "gun": "",
            "hideweaponsgunner": 0,
            "iscopilot": 0,
            "primarygunner": 0,
            "proxytype": "CPCargo",
            "startengine": 0,
            "turretfollowfreelook": 0,
            "viewgunnerinexternal": 1,
            "disablesoundattenuation": 1,
            "outgunnermayfire": 1,
            "showascargo": 1,
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
            "ejectdeadgunner": 0,
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "showhmd": 0,
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
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "precisegetinout": 0,
            "allowtablock": 1,
            "showalltargets": 0,
            "slingloadoperator": 0,
            "playerposition": 0,
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|Car_F|Turrets|MainTurret [Indent level: 2],
        "mainturret": {
            "stabilizedinaxes": 4,
            "outgunnermayfire": 1,
            "memorypointgun": "machinegun",
            "body": "",
            "gun": "",
            "gunneraction": "ManActTestDriverOut",
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "soundservo": ["A3|sounds_f|dummysound",0.316228,1,15],
            "minelev": -5,
            "maxelev": 40,
            "minturn": -360,
            "maxturn": 360,
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "primarygunner": 1,
            "enablemanualfire": 0,
            "gunnerforceoptics": 0,
            "startengine": 0,
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 0.8,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passthrough": 0.5,
                    "explosionshielding": 0.4
                },
                # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 0.4,
                    "material": -1,
                    "name": "zbran",
                    "visual": "zbran",
                    "passthrough": 0,
                    "explosionshielding": 0.2
                }
            },
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|ViewOptics [Indent level: 3],
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
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|ViewGunner [Indent level: 3],
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
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
            },
            "disablesoundattenuation": 0,
            "animationsourcebody": "mainTurret",
            "animationsourcegun": "mainGun",
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "proxyindex": 1,
            "gunnername": "Gunner",
            "gunnertype": "",
            "primaryobserver": 0,
            "weapons": [],
            "magazines": [],
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
            "primary": 1,
            "hasgunner": 1,
            "commanding": 1,
            "turretcansee": 0,
            "canusescanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "turretspec": {
                "showheadphones": 0
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
            "castgunnershadow": 0,
            "viewgunnershadow": 1,
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
            "memorypointgunneroptics": "gunnerview",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        }
    },
    # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|longlights_hide [Indent level: 2]
        "longlights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|shortlights_hide [Indent level: 2],
        "shortlights_hide": {
            "initphase": 0,
            "source": "user",
            "animperiod": 1e-006
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|lights_hide [Indent level: 2],
        "lights_hide": {
            "initphase": 0,
            "source": "user",
            "animperiod": 1e-006
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|light_bo [Indent level: 2],
        "light_bo": {
            "source": "user",
            "animperiod": 1e-005,
            "initphase": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|light_stop [Indent level: 2],
        "light_stop": {
            "initphase": 0,
            "source": "user",
            "animperiod": 1e-005
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|DoorL [Indent level: 2],
        "doorl": {
            "source": "door",
            "animperiod": 0.8,
            "sound": "RHSUSF_Truck_Door",
            "soundposition": "osa_dvere_lp"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|DoorR [Indent level: 2],
        "doorr": {
            "soundposition": "osa_dvere_pp",
            "source": "door",
            "animperiod": 0.8,
            "sound": "RHSUSF_Truck_Door"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|DoorB [Indent level: 2],
        "doorb": {
            "animperiod": 1.8,
            "soundposition": "osa_dvere_pp",
            "source": "door",
            "sound": "RHSUSF_Truck_Door"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|hatch1_door [Indent level: 2],
        "hatch1_door": {
            "soundposition": "osa_dvere_pp",
            "initphase": 0,
            "source": "door",
            "animperiod": 0.8,
            "sound": "RHSUSF_Truck_Door"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|DUKE_Hide [Indent level: 2],
        "duke_hide": {
            "source": "user",
            "mass": -20,
            "displayname": "hide DUKE antennas",
            "author": "Red Hammer Studios",
            "animperiod": 1e-005,
            "initphase": 0,
            "onphasechanged": "_this call rhs_fnc_duke_vg;"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitDuke1 [Indent level: 2],
        "hitduke1": {
            "source": "Hit",
            "hitpoint": "HitDuke1"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitLFWheel [Indent level: 2],
        "hitlfwheel": {
            "source": "Hit",
            "hitpoint": "HitLFWheel",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitRFWheel [Indent level: 2],
        "hitrfwheel": {
            "hitpoint": "HitRFWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitLBWheel [Indent level: 2],
        "hitlbwheel": {
            "hitpoint": "HitLF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitRBWheel [Indent level: 2],
        "hitrbwheel": {
            "hitpoint": "HitRF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitLF2Wheel [Indent level: 2],
        "hitlf2wheel": {
            "hitpoint": "HitLBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitRF2Wheel [Indent level: 2],
        "hitrf2wheel": {
            "hitpoint": "HitRBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitLMWheel [Indent level: 2],
        "hitlmwheel": {
            "hitpoint": "HitLMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitRMWheel [Indent level: 2],
        "hitrmwheel": {
            "hitpoint": "HitRMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "source": "Hit",
            "hitpoint": "HitGlass2",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "source": "Hit",
            "hitpoint": "HitGlass3",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "source": "Hit",
            "hitpoint": "HitGlass4",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "source": "Hit",
            "hitpoint": "HitGlass5",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "source": "Hit",
            "hitpoint": "HitGlass6",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "source": "Hit",
            "hitpoint": "HitGlass7",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|AnimationSources|HitGlass8 [Indent level: 2],
        "hitglass8": {
            "source": "Hit",
            "hitpoint": "HitGlass8",
            "raw": 1
        }
    },
    # Class: CfgVehicles|rhsusf_Cougar_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhsusf_Cougar_base|UserActions|light_bo_off [Indent level: 2]
        "light_bo_off": {
            "displayname": "B.O. Light off",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyforplayer": 0,
            "condition": "(player == driver this) && this animationPhase 'light_bo'<0.5;",
            "statement": "this animate ['light_bo', 1];this animate ['light_brake_bo', 1]"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|UserActions|light_bo_on [Indent level: 2],
        "light_bo_on": {
            "displayname": "B.O. Light on",
            "condition": "(player == driver this) && this animationPhase 'light_bo'==1;",
            "statement": "this animate ['light_bo', 0];this animate ['light_brake_bo', 0]",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyforplayer": 0
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|UserActions|light_stop_off [Indent level: 2],
        "light_stop_off": {
            "displayname": "Stop Light off",
            "condition": "(player == driver this) && this animationPhase 'light_stop'<0.5",
            "statement": "this animate ['light_stop', 1]",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyforplayer": 0
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|UserActions|light_stop_on [Indent level: 2],
        "light_stop_on": {
            "displayname": "Stop Light on",
            "condition": "(player == driver this) && this animationPhase 'light_stop'==1",
            "statement": "this animate ['light_stop', 0]",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyforplayer": 0
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|UserActions|lights_toggle [Indent level: 2],
        "lights_toggle": {
            "displayname": "Toggle short/long lights",
            "position": "",
            "shortcut": "vehLockTargets",
            "radius": 12,
            "priority": 1.5,
            "showwindow": 0,
            "onlyforplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)",
            "statement": "[this,0] call rhsusf_fnc_carLightToggle"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|UserActions|cabinlights_toggle [Indent level: 2],
        "cabinlights_toggle": {
            "shortcut": "lockTarget",
            "displayname": "Toggle cabin lights",
            "statement": "[this,1] call rhsusf_fnc_carLightToggle",
            "position": "",
            "radius": 12,
            "priority": 1.5,
            "showwindow": 0,
            "onlyforplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|UserActions|OpenCargoDoor [Indent level: 2],
        "opencargodoor": {
            "displayname": "Open Rear Door",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "this doorPhase 'DoorB' == 0 and {(call rhsusf_fnc_findPlayer) in this};",
            "statement": "this animateDoor ['DoorB', 1];this setVariable ['ramp_handler',1,true]",
            "onlyforplayer": 1,
            "shortcut": "user12"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|UserActions|CloseCargoDoor [Indent level: 2],
        "closecargodoor": {
            "displayname": "Close Rear Door",
            "condition": "this doorPhase 'DoorB' > 0 and {(call rhsusf_fnc_findPlayer) in this};",
            "statement": "this animateDoor ['DoorB', 0];this setVariable ['ramp_handler',0,true]",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1,
            "shortcut": "user12"
        }
    },
    "hulldamagecauseexplosion": 1,
    "armorstructural": 8,
    # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": -200,
            "passthrough": 1,
            "name": "karoserie",
            "visual": "zbytek",
            "minimalhit": -45,
            "explosionshielding": 0.01,
            "radius": 0.22,
            "material": -1
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": -50,
            "material": -1,
            "name": "Hit_Fuel",
            "armorcomponent": "Hit_Fuel_L",
            "visual": "-",
            "explosionshielding": 0.5,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitFuel2 [Indent level: 2],
        "hitfuel2": {
            "armorcomponent": "Hit_Fuel_R",
            "armor": -50,
            "material": -1,
            "name": "Hit_Fuel",
            "visual": "-",
            "explosionshielding": 0.5,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": -50,
            "material": -1,
            "name": "Hit_Engine",
            "armorcomponent": "Hit_Engine",
            "visual": "zbytek",
            "passthrough": 0.2,
            # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "rhs_engine_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire [Indent level: 4],
                "rhs_engine_fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks [Indent level: 4],
                "rhs_engine_sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "rhs_engine_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "rhs_engine_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
                "rhs_engine_smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                }
            }
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitDuke1 [Indent level: 2],
        "hitduke1": {
            "armor": 0.75,
            "material": -1,
            "name": "duke1",
            "visual": "-",
            "passthrough": 0,
            "minimalhit": 0.05,
            "explosionshielding": 0.01,
            "radius": 0.15
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": -70,
            "explosionshielding": 0.4,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass1",
            "name": "glass1",
            "visual": "glass1"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": -70,
            "explosionshielding": 0.4,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass2",
            "name": "glass2",
            "visual": "glass2"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "armor": -70,
            "explosionshielding": 0.4,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass3",
            "name": "glass3",
            "visual": "glass3"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "armor": -70,
            "explosionshielding": 0.4,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass4",
            "name": "glass4",
            "visual": "glass4"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "armor": -70,
            "explosionshielding": 0.4,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass5",
            "name": "glass5",
            "visual": "glass5"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "armor": -70,
            "explosionshielding": 0.4,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass6",
            "name": "glass6",
            "visual": "glass6"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "armor": -70,
            "explosionshielding": 0.4,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass7",
            "name": "glass7",
            "visual": "glass7"
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|HitPoints|HitGlass8 [Indent level: 2],
        "hitglass8": {
            "armor": -70,
            "explosionshielding": 0.4,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.2,
            "armorcomponent": "glass8",
            "name": "glass8",
            "visual": "glass8"
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitLFWheel [Indent level: 2],
        "hitlfwheel": {
            "radius": 0.33,
            "visual": "wheel_1_1_damage",
            "armorcomponent": "wheel_1_1_hide",
            "armor": -250,
            "minimalhit": -0.016,
            "explosionshielding": 4,
            "passthrough": 0,
            "material": -1,
            "name": "wheel_1_1_steering"
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitLF2Wheel [Indent level: 2],
        "hitlf2wheel": {
            "radius": 0.33,
            "visual": "wheel_1_2_damage",
            "armorcomponent": "wheel_1_2_hide",
            "armor": -250,
            "minimalhit": -0.016,
            "explosionshielding": 4,
            "passthrough": 0,
            "material": -1,
            "name": "wheel_1_2_steering"
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitRFWheel [Indent level: 2],
        "hitrfwheel": {
            "radius": 0.33,
            "visual": "wheel_2_1_damage",
            "armorcomponent": "wheel_2_1_hide",
            "armor": -250,
            "minimalhit": -0.016,
            "explosionshielding": 4,
            "passthrough": 0,
            "material": -1,
            "name": "wheel_2_1_steering"
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitRF2Wheel [Indent level: 2],
        "hitrf2wheel": {
            "radius": 0.33,
            "visual": "wheel_2_2_damage",
            "armorcomponent": "wheel_2_2_hide",
            "armor": -250,
            "minimalhit": -0.016,
            "explosionshielding": 4,
            "passthrough": 0,
            "material": -1,
            "name": "wheel_2_2_steering"
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitBody [Indent level: 2],
        "hitbody": {
            "armor": 6,
            "material": -1,
            "name": "karoserie",
            "visual": "zbytek",
            "passthrough": 1,
            "minimalhit": 0.01,
            "explosionshielding": 1.5,
            "radius": 0.45
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitRGlass [Indent level: 2],
        "hitrglass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni P",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitLGlass [Indent level: 2],
        "hitlglass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni L",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitLBWheel [Indent level: 2],
        "hitlbwheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_4_steering",
            "visual": "-",
            "passthrough": 0.3,
            "explosionshielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitLMWheel [Indent level: 2],
        "hitlmwheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_3_steering",
            "visual": "-",
            "passthrough": 0.3,
            "explosionshielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitRBWheel [Indent level: 2],
        "hitrbwheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_4_steering",
            "visual": "-",
            "passthrough": 0.3,
            "explosionshielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitRMWheel [Indent level: 2],
        "hitrmwheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_3_steering",
            "visual": "-",
            "passthrough": 0.3,
            "explosionshielding": 4
        }
    },
    # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "Light_R",
            "direction": "Light_R_end",
            "hitpoint": "Light_R",
            "selection": "Light_R",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Right2 [Indent level: 2],
        "right2": {
            "position": "light_R_flare",
            "useflare": 1,
            "direction": "Light_R_end",
            "hitpoint": "Light_R",
            "selection": "Light_R",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Left2 [Indent level: 2],
        "left2": {
            "position": "light_L_flare",
            "useflare": 1,
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Long_Left [Indent level: 2],
        "long_left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L_Long",
            "direction": "Light_L_Long_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerangle": 22,
            "outerangle": 26,
            "conefadecoef": 1,
            "intensity": 100,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1.5,
            "flaremaxdistance": 750,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Long_Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardlimitstart": 500,
                "hardlimitend": 750
            }
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Long_Right [Indent level: 2],
        "long_right": {
            "position": "Light_R_Long",
            "direction": "Light_R_Long_end",
            "hitpoint": "Light_R",
            "selection": "Light_R",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 22,
            "outerangle": 26,
            "conefadecoef": 1,
            "intensity": 100,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1.5,
            "flaremaxdistance": 750,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Long_Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardlimitstart": 500,
                "hardlimitend": 750
            }
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Long_Right2 [Indent level: 2],
        "long_right2": {
            "useflare": 1,
            "position": "light_R_Long_flare",
            "innerangle": 50,
            "outerangle": 179,
            "conefadecoef": 51,
            "intensity": 1,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Long_Right2|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            },
            "direction": "Light_R_Long_end",
            "hitpoint": "Light_R",
            "selection": "Light_R",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "daylight": 0,
            "flaresize": 1.5,
            "flaremaxdistance": 750
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Long_Left2 [Indent level: 2],
        "long_left2": {
            "useflare": 1,
            "position": "light_L_Long_flare",
            "innerangle": 50,
            "outerangle": 179,
            "conefadecoef": 51,
            "intensity": 1,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|Long_Left2|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            },
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "direction": "Light_L_Long_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "daylight": 0,
            "flaresize": 1.5,
            "flaremaxdistance": 750
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|cabin1 [Indent level: 2],
        "cabin1": {
            "color": [800,900,650],
            "ambient": [5,5,5],
            "intensity": 4,
            "size": 1,
            "innerangle": 90,
            "outerangle": 165,
            "conefadecoef": 1,
            "position": "cabin_light1",
            "direction": "cabin_light1_dir",
            "hitpoint": "cabin_light1",
            "selection": "cabin_light1",
            "useflare": 1,
            "flaresize": 1,
            "flaremaxdistance": 5,
            "daylight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|cabin1|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 70,
                "hardlimitstart": 2,
                "hardlimitend": 2.5
            }
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|cabin2 [Indent level: 2],
        "cabin2": {
            "position": "cabin_light2",
            "direction": "cabin_light2_dir",
            "hitpoint": "cabin_light2",
            "selection": "cabin_light2",
            "color": [800,900,650],
            "ambient": [5,5,5],
            "intensity": 4,
            "size": 1,
            "innerangle": 90,
            "outerangle": 165,
            "conefadecoef": 1,
            "useflare": 1,
            "flaresize": 1,
            "flaremaxdistance": 5,
            "daylight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|cabin1|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 70,
                "hardlimitstart": 2,
                "hardlimitend": 2.5
            }
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|cabin3 [Indent level: 2],
        "cabin3": {
            "position": "cabin_light3",
            "direction": "cabin_light3_dir",
            "hitpoint": "cabin_light3",
            "selection": "cabin_light3",
            "color": [800,900,650],
            "ambient": [5,5,5],
            "intensity": 4,
            "size": 1,
            "innerangle": 90,
            "outerangle": 165,
            "conefadecoef": 1,
            "useflare": 1,
            "flaresize": 1,
            "flaremaxdistance": 5,
            "daylight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_Cougar_base|Reflectors|cabin1|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 70,
                "hardlimitstart": 2,
                "hardlimitend": 2.5
            }
        }
    },
    "aggregatereflectors": [["Left","Left2"],["Right","Right2"]],
    "armorlights": 0.01,
    # Class: CfgVehicles|rhsusf_Cougar_base|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|rhsusf_Cougar_base|RenderTargets|LeftMirror [Indent level: 2]
        "leftmirror": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|rhsusf_Cougar_base|RenderTargets|LeftMirror|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "m1p",
                "pointdirection": "m1d",
                "renderquality": 2,
                "rendervisionmode": 4,
                "fov": 0.7
            },
            "bboxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|RenderTargets|RightMirror [Indent level: 2],
        "rightmirror": {
            "rendertarget": "rendertarget1",
            # Class: CfgVehicles|rhsusf_Cougar_base|RenderTargets|RightMirror|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "m2p",
                "pointdirection": "m2d",
                "renderquality": 2,
                "rendervisionmode": 4,
                "fov": 0.7
            },
            "bboxes": ["PIP_2_TL","PIP_2_TR","PIP_2_BL","PIP_2_BR"]
        }
    },
    "normalspeedforwardcoef": 0.9,
    "turncoef": 3.5,
    "terraincoef": 0.5,
    "simulation": "carx",
    "precision": 9,
    "brakedistance": 3,
    "acceleration": 15,
    "fireresistance": 5,
    "maxspeed": 105,
    "fuelcapacity": 20,
    "wheelcircumference": 2.95,
    "brakeidlespeed": 2,
    "maxfordingdepth": 0.4,
    "waterspeedfactor": 0.3,
    "waterresistance": 10,
    "waterresistancecoef": 0.2,
    "waterleakiness": 250,
    # Class: CfgVehicles|rhsusf_Cougar_base|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-5.03,"N",0,"D1",3.49,"D2",1.86,"D3",1.41,"D4",1,"D5",0.75,"D6",0.55],
        "transmissionratios": ["High",8.2],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R"
    },
    "changegearmineffectivity": [0.95,0,0.99,0.99,0.99,0.99,0.99,0.99],
    "switchtime": 0.31,
    "latency": 1.3,
    "transmissionlosses": 18,
    "dampersbumpcoef": 6,
    "differentialtype": "all_limited",
    "frontrearsplit": 0.5,
    "frontbias": 1.3,
    "rearbias": 1.3,
    "centrebias": 1.3,
    "clutchstrength": 85,
    "dampingratefullthrottle": 0.078,
    "dampingratezerothrottleclutchengaged": 1.35,
    "dampingratezerothrottleclutchdisengaged": 0.35,
    "torquecurve": [[0.318182,0.457898],[0.454545,0.786724],[0.590909,1],[0.636364,1],[0.727273,0.990781],[0.909091,0.974186],[0.954545,0.940381],[1.05273,0]],
    "enginepower": 336,
    "peaktorque": 2277.8,
    "minomega": 65,
    "maxomega": 230.38,
    "idlerpm": 700,
    "redrpm": 2200,
    "enginelosses": 12,
    "thrustdelay": 1,
    "enginebrakecoef": 0.8,
    "antirollbarforcecoef": 26.5,
    "antirollbarforcelimit": 26.5,
    "antirollbarspeedmin": 10,
    "antirollbarspeedmax": 75,
    "accelaidforcespd": 2.23,
    "accelaidforcecoef": 4,
    "accelaidforceyoffset": -1.3,
    # Class: CfgVehicles|rhsusf_Cougar_base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhsusf_Cougar_base|Wheels|L1 [Indent level: 2]
        "l1": {
            "side": "left",
            "bonename": "wheel_1_1_damper",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "suspforceapppointoffset": "wheel_1_1_axis",
            "tireforceapppointoffset": "wheel_1_1_axis",
            "susptraveldirection": [-0.125,-1,0],
            "width": 0.37,
            "steering": 1,
            "mass": 80,
            "moi": 25,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 35000,
            "maxhandbraketorque": 0,
            "maxcompression": 0.12,
            "maxdroop": 0.12,
            "sprungmass": -1,
            "springstrength": 405000,
            "springdamperrate": 45725,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 40,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Wheels|L2 [Indent level: 2],
        "l2": {
            "bonename": "wheel_1_2_damper",
            "steering": 0,
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "suspforceapppointoffset": "wheel_1_2_axis",
            "tireforceapppointoffset": "wheel_1_2_axis",
            "side": "left",
            "susptraveldirection": [-0.125,-1,0],
            "width": 0.37,
            "mass": 80,
            "moi": 25,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 35000,
            "maxhandbraketorque": 0,
            "maxcompression": 0.12,
            "maxdroop": 0.12,
            "sprungmass": -1,
            "springstrength": 405000,
            "springdamperrate": 45725,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 40,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Wheels|R1 [Indent level: 2],
        "r1": {
            "bonename": "wheel_2_1_damper",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "suspforceapppointoffset": "wheel_2_1_axis",
            "tireforceapppointoffset": "wheel_2_1_axis",
            "steering": 1,
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "width": 0.37,
            "mass": 80,
            "moi": 25,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 35000,
            "maxhandbraketorque": 0,
            "maxcompression": 0.12,
            "maxdroop": 0.12,
            "sprungmass": -1,
            "springstrength": 405000,
            "springdamperrate": 45725,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 40,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|Wheels|R2 [Indent level: 2],
        "r2": {
            "bonename": "wheel_2_2_damper",
            "steering": 0,
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "suspforceapppointoffset": "wheel_2_2_axis",
            "tireforceapppointoffset": "wheel_2_2_axis",
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "width": 0.37,
            "mass": 80,
            "moi": 25,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 35000,
            "maxhandbraketorque": 0,
            "maxcompression": 0.12,
            "maxdroop": 0.12,
            "sprungmass": -1,
            "springstrength": 405000,
            "springdamperrate": 45725,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 40,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,2.5],[0.5,2.3],[1,2]]
        }
    },
    # Class: CfgVehicles|rhsusf_Cougar_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_cougar|data|CGR_Body.rvmat","rhsusf|addons|rhsusf_cougar|data|CGR_Body_dam.rvmat","rhsusf|addons|rhsusf_cougar|data|CGR_destruction.rvmat","rhsusf|addons|rhsusf_cougar|data|CGR_Int.rvmat","rhsusf|addons|rhsusf_cougar|data|CGR_Int_dam.rvmat","rhsusf|addons|rhsusf_cougar|data|CGR_destruction.rvmat","rhsusf|addons|rhsusf_rg33|data|glass.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_int.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles|rhsusf_Cougar_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhsusf_Cougar_base|EventHandlers|RHSUSF_EventHandlers [Indent level: 2]
        "rhsusf_eventhandlers": {
            "seatswitched": "if(not(_this select 1 in [driver (_this select 0),gunner (_this select 0)]))then{ (_this select 1) action ['turnIn',_this select 0]}",
            "turnin": "([0] + _this)  call rhsusf_fnc_turretAction;",
            "turnout": "([1] + _this) call rhsusf_fnc_turretAction;",
            "engine": "_this call rhs_fnc_engineCheckDamage"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    # Class: CfgVehicles|rhsusf_Cougar_base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|rhsusf_Cougar_base|TransportBackpacks|_xx_rhsusf_falconii [Indent level: 2]
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhsusf_Cougar_base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|rhsusf_Cougar_base|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 10
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|TransportMagazines|_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|TransportMagazines|_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|TransportMagazines|_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|TransportMagazines|_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 4
        }
    },
    # Class: CfgVehicles|rhsusf_Cougar_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhsusf_Cougar_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles|rhsusf_Cougar_base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhsusf_Cougar_base|TransportWeapons [Indent level: 1],
    "transportweapons": {
        # Class: CfgVehicles|rhsusf_Cougar_base|TransportWeapons|_xx_rhs_weap_m4_carryhandle [Indent level: 2]
        "_xx_rhs_weap_m4_carryhandle": {
            "weapon": "rhs_weap_m4_carryhandle",
            "count": 2
        }
    },
    "attenuationeffecttype": "MrapAttenuation",
    "soundgetin": ["A3|Sounds_F|vehicles2|soft|Mrap_01|Mrap_01_Enter",0.446684,1],
    "soundgetout": ["A3|Sounds_F|vehicles2|soft|Mrap_01|Mrap_01_Exit",0.446684,1,40],
    "sounddammage": ["",0.562341,1],
    "soundengineonint": ["A3|Sounds_F|vehicles2|soft|Mrap_01|Mrap_01_Engine_Int_Start",0.630957,1],
    "soundengineoffint": ["A3|Sounds_F|vehicles2|soft|Mrap_01|Mrap_01_Engine_Int_stop",0.501187,1],
    "soundengineonext": ["A3|Sounds_F|vehicles2|soft|Mrap_01|Mrap_01_Engine_Ext_Start",1.99526,1,50],
    "soundengineoffext": ["A3|Sounds_F|vehicles2|soft|Mrap_01|Mrap_01_Engine_Ext_stop",1.99526,1,50],
    "buildcrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "buildcrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "buildcrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "buildcrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "buildcrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "buildcrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "buildcrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "buildcrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundbuildingcrash": ["buildCrash0",0.125,"buildCrash1",0.125,"buildCrash2",0.125,"buildCrash3",0.125,"buildCrash4",0.125,"buildCrash5",0.125,"buildCrash6",0.125,"buildCrash7",0.125],
    "woodcrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_01",1.99526,1,75],
    "woodcrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_02",1.99526,1,75],
    "woodcrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_03",1.99526,1,75],
    "woodcrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_04",1.99526,1,75],
    "woodcrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_05",1.99526,1,75],
    "woodcrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_06",1.99526,1,75],
    "woodcrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_07",1.99526,1,75],
    "woodcrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_08",1.99526,1,75],
    "soundwoodcrash": ["woodCrash0",0.125,"woodCrash1",0.125,"woodCrash2",0.125,"woodCrash3",0.125,"woodCrash4",0.125,"woodCrash5",0.125,"woodCrash6",0.125,"woodCrash7",0.125],
    "armorcrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "armorcrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "armorcrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "armorcrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "armorcrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "armorcrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "armorcrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "armorcrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundarmorcrash": ["ArmorCrash0",0.125,"ArmorCrash1",0.125,"ArmorCrash2",0.125,"ArmorCrash3",0.125,"ArmorCrash4",0.125,"ArmorCrash5",0.125,"ArmorCrash6",0.125,"ArmorCrash7",0.125],
    "crash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "crash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "crash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "crash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "crash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "crash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "crash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "crash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundcrashes": ["Crash0",0.125,"Crash1",0.125,"Crash2",0.125,"Crash3",0.125,"Crash4",0.125,"Crash5",0.125,"Crash6",0.125,"Crash7",0.125],
    "bushcrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_01",0.630957,1,50],
    "bushcrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_02",0.630957,1,50],
    "bushcrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_03",0.630957,1,50],
    "bushcrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_03",0.630957,0.8,50],
    "soundbushcrash": ["BushCrash1",0.25,"BushCrash2",0.25,"BushCrash3",0.25,"BushCrash4",0.25],
    # Class: CfgVehicles|MRAP_01_base_F|Sounds [Indent level: 1],
    "sounds": {
        "soundsetsint": ["Mrap_01_Engine_RPM0_INT_SoundSet","Mrap_01_Engine_RPM1_INT_SoundSet","Mrap_01_Engine_RPM2_INT_SoundSet","Mrap_01_Engine_RPM3_INT_SoundSet","Mrap_01_Engine_RPM4_INT_SoundSet","Mrap_01_Engine_INT_Burst_SoundSet","Mrap_01_Rattling_INT_SoundSet","Mrap_01_Stress_INT_SoundSet","Mrap_01_Rain_INT_SoundSet","Mrap_01_Tires_Rock_Fast_INT_SoundSet","Mrap_01_Tires_Grass_Fast_INT_SoundSet","Mrap_01_Tires_Sand_Fast_INT_SoundSet","Mrap_01_Tires_Gravel_Fast_INT_SoundSet","Mrap_01_Tires_Mud_Fast_INT_SoundSet","Mrap_01_Tires_Asphalt_Fast_INT_SoundSet","Mrap_01_Tires_Water_Fast_INT_SoundSet","Mrap_01_Tires_Rock_Slow_INT_SoundSet","Mrap_01_Tires_Grass_Slow_INT_SoundSet","Mrap_01_Tires_Sand_Slow_INT_SoundSet","Mrap_01_Tires_Gravel_Slow_INT_SoundSet","Mrap_01_Tires_Mud_Slow_INT_SoundSet","Mrap_01_Tires_Asphalt_Slow_INT_SoundSet","Mrap_01_Tires_Water_Slow_INT_SoundSet","Mrap_01_Tires_Turn_Hard_INT_SoundSet","Mrap_01_Tires_Turn_Soft_INT_SoundSet","Mrap_01_Tires_Brake_Hard_INT_SoundSet","Mrap_01_Tires_Brake_Soft_INT_SoundSet","","Tires_Movement_Dirt_Int_01_SoundSet"],
        "soundsetsext": ["Mrap_01_Engine_RPM0_EXT_SoundSet","Mrap_01_Engine_RPM1_EXT_SoundSet","Mrap_01_Engine_RPM2_EXT_SoundSet","Mrap_01_Engine_RPM3_EXT_SoundSet","Mrap_01_Engine_RPM4_EXT_SoundSet","Mrap_01_Engine_EXT_Burst_SoundSet","Mrap_01_Rattling_EXT_SoundSet","Mrap_01_Stress_EXT_SoundSet","Mrap_01_Rain_EXT_SoundSet","Mrap_01_Tires_Rock_Fast_EXT_SoundSet","Mrap_01_Tires_Grass_Fast_EXT_SoundSet","Mrap_01_Tires_Sand_Fast_EXT_SoundSet","Mrap_01_Tires_Gravel_Fast_EXT_SoundSet","Mrap_01_Tires_Mud_Fast_EXT_SoundSet","Mrap_01_Tires_Asphalt_Fast_EXT_SoundSet","Mrap_01_Tires_Water_Fast_EXT_SoundSet","Mrap_01_Tires_Rock_Slow_EXT_SoundSet","Mrap_01_Tires_Grass_Slow_EXT_SoundSet","Mrap_01_Tires_Sand_Slow_EXT_SoundSet","Mrap_01_Tires_Gravel_Slow_EXT_SoundSet","Mrap_01_Tires_Mud_Slow_EXT_SoundSet","Mrap_01_Tires_Asphalt_Slow_EXT_SoundSet","Mrap_01_Tires_Water_Slow_EXT_SoundSet","Mrap_01_Tires_Turn_Hard_EXT_SoundSet","Mrap_01_Tires_Turn_Soft_EXT_SoundSet","Mrap_01_Tires_Brake_Hard_EXT_SoundSet","Mrap_01_Tires_Brake_Soft_EXT_SoundSet","","Tires_Movement_Dirt_Ext_01_SoundSet"]
    },
    "features": "Randomization: No						<br />Camo selections: 2 - the body, wheels and cover						<br />Script door sources: Door_LF, Door_RF, Door_LB, Door_RB						<br />Script animations: None						<br />Executed scripts: None						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: 1 to 3",
    # Class: CfgVehicles|MRAP_01_base_F|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|MRAP_01_base_F|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_vehicle_MRAP_s"],
            "speechplural": ["veh_vehicle_MRAP_p"]
        }
    },
    "textsingular": "MRAP",
    "textplural": "MRAPs",
    "namesound": "veh_vehicle_MRAP_s",
    "_generalmacro": "MRAP_01_base_F",
    # Class: CfgVehicles|MRAP_01_base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": "The Hunter is a Mine-Resistant Ambush Protected (MRAP) vehicle manufactured by US arms factories to provide troops with enhanced protection. The armored hull can withstand light weapons and protects the crew against landmines and improvised explosive devices. Even though the heavy armor and powerful engine cause increased fuel consumption, it has been favored by frontline troops over the lighter vehicles for its easy maintenance and good protection level.<br />Armed version of the sturdy Hunter MRAP vehicle is fitted with a Remotely Controlled Weapons System turret. The turret is fitted with the universal 12.7 mm heavy machinegun or the multi-role 40 mm Grenade Machine Gun. The armed Hunters are used for troop transport in combat zones, as light reconnaissance vehicles or even in fire support role in COIN operations."
    },
    "crewvulnerable": 0,
    "crewcrashprotection": 1.35,
    "enableradio": 1,
    "enablegps": 1,
    "armor": 200,
    "cost": 500000,
    "threat": [0.1,0.1,0.1],
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "slingloadcargomemorypoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    # Class: CfgVehicles|MRAP_01_base_F|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|MRAP_01_base_F|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaust_pos",
            "direction": "exhaust_dir",
            "effect": "ExhaustEffectHTruck"
        }
    },
    "wheeldamagethreshold": 0.18,
    "wheeldamageradiuscoef": 0.75,
    "wheeldestroyradiuscoef": 0.48,
    "cargogetinaction": ["GetInMRAP_01_cargo"],
    "cargogetoutaction": ["GetOutMRAP_01"],
    "sensorposition": "sensorPos",
    "hideweaponsdriver": 1,
    "hideweaponscargo": 1,
    "smokelaunchergrenadecount": 8,
    "smokelaunchervelocity": 14,
    "smokelauncheronturret": 0,
    "smokelauncherangle": 360,
    "extcameraposition": [0,2.2,-8],
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
    "secondaryexplosion": -10,
    "fuelexplosionpower": 3,
    "dammagehalf": [],
    "dammagefull": [],
    "explosionshielding": 1,
    "mintotaldamagethreshold": 0.01,
    "gunnerhasflares": 0,
    "steeraheadsimul": 0.5,
    "steeraheadplan": 0.35,
    "predictturnplan": 2,
    "predictturnsimul": 1.5,
    "epeimpulsedamagecoef": 15,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    # Class: CfgVehicles|Car_F|PlayerSteeringCoefficients [Indent level: 1],
    "playersteeringcoefficients": {
        "turnincreaseconst": 1,
        "turnincreaselinear": 1,
        "turnincreasetime": 0,
        "turndecreaseconst": 5,
        "turndecreaselinear": 0,
        "turndecreasetime": 0,
        "maxturnhundred": 1
    },
    # Class: CfgVehicles|Car_F|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initfov": 0.9,
        "minfov": 0.25,
        "maxfov": 1.25,
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
    "headgforceleaningfactor": [0.01,0.01,0.015],
    # Class: CfgVehicles|Car_F|NewTurret [Indent level: 1],
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
    "driverleftleganimname": "",
    "driverrightleganimname": "pedal_thrust",
    "holdoffroadformation": 1,
    # Class: CfgVehicles|Car_F|NVGMarkers [Indent level: 1],
    "nvgmarkers": {
        # Class: CfgVehicles|Car_F|NVGMarkers|NVGMarker01 [Indent level: 2]
        "nvgmarker01": {
            "name": "nvg_marker",
            "color": [0.03,0.003,0.003,1],
            "ambient": [0.003,0.0003,0.0003,1],
            "brightness": 0.001,
            "blinking": 1
        }
    },
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
    "audible": 5,
    "soundenviron": ["",0.000562341,1],
    "soundcrash": ["A3|sounds_f|dummysound",1,1],
    "soundgear": ["",1e-005,1],
    "collisioneffect": "collisionEffect",
    "hideunitinfo": 0,
    "htmin": 60,
    "htmax": 1800,
    "afmax": 100,
    "mfmax": 80,
    "mfact": 1,
    "tbody": 150,
    "transportmaxweapons": 12,
    "transportmaxmagazines": 64,
    "maximumload": 2000,
    "supplyradius": -1,
    "memorypointsupply": "doplnovani",
    "braketorque": 6000,
    "longstiff": 15000,
    "latstiffx": 2000,
    "latstiffy": 18000,
    "wheelmask": "wheel_X_X",
    "numberphysicalwheels": 4,
    "maxgforce": 3,
    # Class: CfgVehicles|Car_F|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 2,
        "frequency": 60,
        "distance": 0,
        "minspeed": 60
    },
    # Class: CfgVehicles|Car_F|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|Car|Components|AICarSteeringComponent [Indent level: 2]
        "aicarsteeringcomponent": {
            "steeringpidweights": [2.9,0.1,0.2],
            "speedpidweights": [0.7,0.2,0],
            "convoypidweights": [1,0.01,0.01],
            "doremapspeed": 1,
            "remapspeedrange": [30,70],
            "remapspeedscalar": [1,0.35],
            "dopredictforward": 1,
            "predictforwardrange": [1,20],
            "steeraheadsaturation": [0.01,0.4],
            "speedpredictionmethod": 2,
            "wheelanglecoef": 0.7,
            "forwardanglecoef": 0.7,
            "steeringanglecoef": 1,
            "differenceanglecoef": 0.4,
            "stuckmaxtime": 3,
            "allowovertaking": 1,
            "allowdrifting": 0,
            "allowcollisionavoidance": 1,
            "maxwheelanglediff": 0.2616,
            "minspeedtokeep": 0.1,
            "commandturnfactor": 1
        },
        # Class: CfgVehicles|LandVehicle|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    "unloadincombat": 1,
    "canfloat": 0,
    "limitedspeedcoef": 0.5,
    # Class: CfgVehicles|Car|PlateInfos [Indent level: 1],
    "plateinfos": {
        "name": "spz",
        "color": [0,0,0,0.75]
    },
    "selectionfireanim": "zasleh",
    "alphatracks": 0.2,
    "memorypointtrackfll": "Stopa PLL",
    "memorypointtrackflr": "Stopa PLP",
    "memorypointtrackbll": "Stopa ZLL",
    "memorypointtrackblr": "Stopa ZLP",
    "memorypointtrackfrl": "Stopa PPL",
    "memorypointtrackfrr": "Stopa PPP",
    "memorypointtrackbrl": "Stopa ZPL",
    "memorypointtrackbrr": "Stopa ZPP",
    "memorypointcirculumreference": "circulumReference",
    "gearbox": [-8,0,10,6.15,4.44,3.33],
    "scudeffect": "ScudEffect",
    "preferroads": 1,
    "formationx": 20,
    "formationz": 20,
    "type": 0,
    "typicalcargo": ["Soldier"],
    "scudmodel": "",
    "dampersize": 0.1,
    "damperforce": 1,
    "damperdamping": 1,
    "inputturncurve": [[0,[0,0,1,1]],[30,[0,0,0.2,0.008,0.4,0.032,0.6,0.216,0.8,0.512,1,1]]],
    "soundengine": ["",1.77828,0.9],
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffects"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffects"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffects"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffects"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","LDustEffects"]],
    # Class: CfgVehicles|Car|DustEffects [Indent level: 1],
    "dusteffects": {
        # Class: CfgDustEffectsCar|Both [Indent level: 0]
        "both": {
        },
        # Class: CfgDustEffectsCar|Left [Indent level: 0],
        "left": {
            "default": ["LDustEffects"],
            "gdtstratisconcrete": ["LDustEffects"],
            "gdtstratisbeach": ["LDustEffects"],
            "gdtstratisdirt": ["LDustEffects"],
            "gdtstratisseabedcluttered": ["LDustEffects"],
            "gdtstratisseabed": ["LDustEffects"],
            "gdtstratisdrygrass": ["LDustEffects"],
            "gdtstratisgreengrass": ["LDustEffects"],
            "gdtstratisrocky": ["LDustEffects"],
            "gdtstratisthistles": ["LDustEffects"],
            "gdtconcrete": ["LDustEffects"],
            "gdtasphalt": ["LDustEffects"],
            "gdtrubble": ["LDustEffects"],
            "gdtsoil": ["LDustEffects"],
            "gdtbeach": ["LDustEffects"],
            "gdtrock": ["LDustEffects"],
            "gdtdead": ["LDustEffects"],
            "gdtdesert": ["LDustEffects"],
            "gdtdesert1": ["LDustEffects"],
            "gdtdesert2": ["LDustEffects"],
            "gdtdirt": ["LDustEffects"],
            "gdtgrassgreen": ["LDustEffects"],
            "gdtgrassdry": ["LDustEffects"],
            "gdtgrasswild": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtwildfield": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtweed1": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtweed2": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtthorn": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtstony": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtstonygreen": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtstonythistle": ["LDustEffects","LGrassEffects","LDirtEffects"],
            "gdtseabeddeep": ["LDustEffects"],
            "gdtseabed": ["LDustEffects"],
            "surfroaddirt": ["LDustEffects"],
            "surfroadconcrete": ["LDustEffects"],
            "surfroadtarmac": ["LDustEffects"],
            "surfwood": ["LDustEffects"],
            "surfmetal": ["LDustEffects"],
            "surfrooftin": ["LDustEffects"],
            "surfrooftiles": ["LDustEffects"],
            "surfintwood": ["LDustEffects"],
            "surfintconcrete": ["LDustEffects"],
            "surfinttiles": ["LDustEffects"],
            "surfintmetal": ["LDustEffects"],
            "gdtgrassshort": ["LDustEffects","LGrassEffects"],
            "gdtgrasstall": ["LDustEffects","LGrassEffects"],
            "gdtreddirt": ["LDustEffectsRed"],
            "gdtfield": ["LDustEffects"],
            "gdtforest": ["LDustEffects"],
            "gdtvolcano": ["LDustEffects","LStonesEffects"],
            "gdtcliff": ["LDustEffects"],
            "gdtvolcanobeach": ["LDustEffects"],
            "surfroaddirt_exp": ["LDustEffectsRed"],
            "surfroadconcrete_exp": ["LDustEffects"],
            "surfroadtarmac_exp": ["LDustEffects"],
            "gdtkldirt": ["LDustEffects"],
            "gdtklgrass1": ["LDustEffects","LGrassEffects"],
            "gdtklgrass2": ["LDustEffects","LGrassEffects"],
            "gdtklforestcon": ["LDustEffects"],
            "gdtklforestdec": ["LDustEffects"],
            "gdtklmud": ["LDustEffects"],
            "gdtklsoil": ["LDustEffects"],
            "gdtkltarmac": ["LDustEffects"],
            "gdtklstubble": ["LDustEffects"],
            "gdtklstones": ["LStonesEffects"],
            "surfroaddirt_enoch": ["LDustEffects"],
            "surftraildirt_enoch": ["LDustEffects"],
            "surfroadtarmac1_enoch": ["LDustEffects"],
            "surfroadtarmac2_enoch": ["LDustEffects"],
            "surfroadtarmac3_enoch": ["LDustEffects"],
            "dirtrunway": ["LDustEffects"]
        },
        # Class: CfgDustEffectsCar|Right [Indent level: 0],
        "right": {
            "default": ["RDustEffects"],
            "gdtstratisconcrete": ["RDustEffects"],
            "gdtstratisbeach": ["RDustEffects"],
            "gdtstratisdirt": ["RDustEffects"],
            "gdtstratisseabedcluttered": ["RDustEffects"],
            "gdtstratisseabed": ["RDustEffects"],
            "gdtstratisdrygrass": ["RDustEffects"],
            "gdtstratisgreengrass": ["RDustEffects"],
            "gdtstratisrocky": ["RDustEffects"],
            "gdtstratisthistles": ["RDustEffects"],
            "gdtconcrete": ["RDustEffects"],
            "gdtasphalt": ["RDustEffects"],
            "gdtrubble": ["RDustEffects"],
            "gdtsoil": ["RDustEffects"],
            "gdtbeach": ["RDustEffects"],
            "gdtrock": ["RDustEffects"],
            "gdtdead": ["RDustEffects"],
            "gdtdesert": ["RDustEffects"],
            "gdtdesert1": ["RDustEffects"],
            "gdtdesert2": ["RDustEffects"],
            "gdtdirt": ["RDustEffects"],
            "gdtgrassgreen": ["RDustEffects"],
            "gdtgrassdry": ["RDustEffects"],
            "gdtgrasswild": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtwildfield": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtweed1": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtweed2": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtthorn": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtstony": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtstonygreen": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtstonythistle": ["RDustEffects","RGrassEffects","RDirtEffects"],
            "gdtseabeddeep": ["RDustEffects"],
            "gdtseabed": ["RDustEffects"],
            "surfroaddirt": ["RDustEffects"],
            "surfroadconcrete": ["RDustEffects"],
            "surfroadtarmac": ["RDustEffects"],
            "surfwood": ["RDustEffects"],
            "surfmetal": ["RDustEffects"],
            "surfrooftin": ["RDustEffects"],
            "surfrooftiles": ["RDustEffects"],
            "surfintwood": ["RDustEffects"],
            "surfintconcrete": ["RDustEffects"],
            "surfinttiles": ["RDustEffects"],
            "surfintmetal": ["RDustEffects"],
            "gdtgrassshort": ["RDustEffects","RGrassEffects"],
            "gdtgrasstall": ["RDustEffects","RGrassEffects"],
            "gdtreddirt": ["RDustEffectsRed"],
            "gdtfield": ["RDustEffects"],
            "gdtforest": ["RDustEffects"],
            "gdtvolcano": ["RDustEffects","RStonesEffects"],
            "gdtcliff": ["RDustEffects"],
            "gdtvolcanobeach": ["RDustEffects"],
            "surfroaddirt_exp": ["RDustEffectsRed"],
            "surfroadconcrete_exp": ["RDustEffects"],
            "surfroadtarmac_exp": ["RDustEffects"],
            "gdtkldirt": ["RDustEffects"],
            "gdtklgrass1": ["RDustEffects","RGrassEffects"],
            "gdtklgrass2": ["RDustEffects","RGrassEffects"],
            "gdtklforestcon": ["RDustEffects"],
            "gdtklforestdec": ["RDustEffects"],
            "gdtklmud": ["RDustEffects"],
            "gdtklsoil": ["RDustEffects"],
            "gdtkltarmac": ["RDustEffects"],
            "gdtklstubble": ["RDustEffects"],
            "gdtklstones": ["RStonesEffects"],
            "surfroaddirt_enoch": ["RDustEffects"],
            "surftraildirt_enoch": ["RDustEffects"],
            "surfroadtarmac1_enoch": ["RDustEffects"],
            "surfroadtarmac2_enoch": ["RDustEffects"],
            "surfroadtarmac3_enoch": ["RDustEffects"],
            "dirtrunway": ["RDustEffects"]
        }
    },
    # Class: CfgVehicles|Car|DestructionEffects [Indent level: 1],
    "destructioneffects": {
        # Class: CfgVehicles|Car|DestructionEffects|Light1 [Indent level: 2]
        "light1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 0.001,
            "interval": 1,
            "lifetime": 3,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles|Car|DestructionEffects|Sound [Indent level: 2],
        "sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifetime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles|Car|DestructionEffects|Fire1 [Indent level: 2],
        "fire1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1Small",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Car|DestructionEffects|Refract1 [Indent level: 2],
        "refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefractSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Car|DestructionEffects|Smoke1 [Indent level: 2],
        "smoke1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmokeSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5
        },
        # Class: CfgVehicles|Car|DestructionEffects|Sparks1 [Indent level: 2],
        "sparks1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifetime": 0
        },
        # Class: CfgVehicles|Car|DestructionEffects|FireSparks1 [Indent level: 2],
        "firesparks1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifetime": 2.8
        },
        # Class: CfgVehicles|Car|DestructionEffects|Fire2 [Indent level: 2],
        "fire2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Car|DestructionEffects|Smoke1_2 [Indent level: 2],
        "smoke1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5
        },
        # Class: CfgVehicles|Car|DestructionEffects|Smoke2 [Indent level: 2],
        "smoke2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifetime": 3.2
        }
    },
    "sensitivityear": 0.125,
    "sensitivity": 1.75,
    "memorypointmissile": ["spice rakety","usti hlavne"],
    "memorypointmissiledir": ["konec rakety","konec hlavne"],
    "enginestartspeed": 1.5,
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "leftwatereffect": "LWaterEffects",
    "rightwatereffect": "RWaterEffects",
    "leftfastwatereffect": "LWaterEffects",
    "rightfastwatereffect": "RWaterEffects",
    "tracksspeed": 0,
    "selectionleftoffset": "PasOffsetL",
    "selectionrightoffset": "PasOffsetP",
    "explosioneffect": "FuelExplosion",
    # Class: CfgVehicles|LandVehicle|CommanderOptics [Indent level: 1],
    "commanderoptics": {
        "proxytype": "CPCommander",
        "proxyindex": 1,
        "gunnername": "Commander",
        "primarygunner": 0,
        "primaryobserver": 1,
        "stabilizedinaxes": 0,
        "body": "obsTurret",
        "gun": "obsGun",
        "animationsourcebody": "obsTurret",
        "animationsourcegun": "obsGun",
        "animationsourcehatch": "hatchCommander",
        "animationsourcecamelev": "camElev",
        "soundservo": ["A3|sounds_f|dummysound",0.01,1,10],
        "gunbeg": "",
        "gunend": "",
        "minelev": -4,
        "maxelev": 20,
        "initelev": 0,
        "minturn": -360,
        "maxturn": 360,
        "initturn": 0,
        "commanding": 2,
        "outgunnermayfire": 1,
        "ingunnermayfire": 1,
        "viewgunnerinexternal": 0,
        "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Commander_02_F",
        "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
        "gunneroutopticscolor": [0,0,0,1],
        "gunneroutforceoptics": 0,
        "gunneroutopticsshowcursor": 0,
        "gunneropticseffect": [],
        "gunneroutopticseffect": [],
        "memorypointgunneroutoptics": "commander_weapon_view",
        "memorypointgunneroptics": "commanderview",
        "memorypointsgetingunner": "pos commander",
        "memorypointsgetingunnerdir": "pos commander dir",
        "gunnergetinaction": "GetInHigh",
        "gunnergetoutaction": "GetOutHigh",
        "memorypointgun": "gun_muzzle",
        "selectionfireanim": "zasleh_1",
        # Class: CfgVehicles|LandVehicle|CommanderOptics|ViewOptics [Indent level: 2],
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
        # Class: CfgVehicles|LandVehicle|CommanderOptics|ViewGunner [Indent level: 2],
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
        "gunnertype": "",
        "weapons": [],
        "magazines": [],
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
        "turretcansee": 0,
        "canusescanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "turretspec": {
            "showheadphones": 0
        },
        "gunneropticscolor": [0,0,0,1],
        "gunnerforceoptics": 1,
        "gunneropticsshowcursor": 0,
        "turretinfotype": "",
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
        "showhmd": 0,
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
        "showcrewaim": 0
    },
    "wheeldestroythreshold": 0.99,
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + 		4",
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "squadtitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memorypointdriveroptics": ["driverview","pilot"],
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsgetincargoprecise": ["pos cargo"],
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "selectionclan": "clan",
    "selectiondashboard": "podsvit pristroju",
    "selectionshowdamage": "poskozeni",
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
    # Class: CfgVehicles|AllVehicles|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initanglex": 0,
        "minanglex": -30,
        "maxanglex": 30,
        "initangley": 0,
        "minangley": -100,
        "maxangley": 100,
        "initfov": 0.7,
        "minfov": 0.42,
        "maxfov": 0.85,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|AllVehicles|PilotSpec [Indent level: 1],
    "pilotspec": {
        "showheadphones": 0
    },
    # Class: CfgVehicles|AllVehicles|CargoSpec [Indent level: 1],
    "cargospec": {
        # Class: CfgVehicles|AllVehicles|CargoSpec|Cargo1 [Indent level: 2]
        "cargo1": {
            "showheadphones": 0
        }
    },
    # Class: CfgVehicles|AllVehicles|MFD [Indent level: 1],
    "mfd": {
    },
    # Class: CfgVehicles|AllVehicles|SoundEvents [Indent level: 1],
    "soundevents": {
    },
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
    "availableforsupporttypes": [],
    "waterppinvehicle": 1,
    "impacteffectssea": "ImpactEffectsSea",
    "impacteffectspeedlimit": 8,
    "showcrewaim": 0,
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
    "camouflage": 2,
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "outsidesoundfilter": 0,
    "obstructsoundlfratio": 0,
    "occludesoundlfratio": 0.25,
    "slowspeedforwardcoef": 0.3,
    "enablemanualfire": 1,
    "portrait": "",
    "ghostpreview": "",
    "damageresistance": 0.004,
    "replacedamaged": "",
    "replacedamagedlimit": 0.9,
    "replacedamagedhitpoints": [],
    "keepinepesceneafterdeath": 0,
    "fuelconsumptionrate": 0.01,
    "groupcameraposition": [0,5,-30],
    "extcameraparams": [1],
    "camerasmoothspeed": 5,
    "minfiretime": 20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitciviliancoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "formationtime": 5,
    "alwaystarget": 0,
    "irtarget": 1,
    "irscanrangemin": 0,
    "irscanrangemax": 0,
    "irscantoeyefactor": 1,
    "irscanground": 1,
    "lasertarget": 0,
    "laserscanner": 0,
    "nvtarget": 0,
    "nvscanner": 0,
    "artillerytarget": 0,
    "artilleryscanner": 0,
    "canusescanners": 1,
    "unitinfotypelite": 0,
    "nightvision": 0,
    "radartype": 0,
    "hasdriver": 1,
    "driverforceoptics": 0,
    "getinradius": 2.5,
    "enablewatch": 0,
    "lockdetectionsystem": 0,
    "incomingmissiledetectionsystem": 0,
    "useprecisegetinaction": 0,
    "allowtablock": 1,
    "showalltargets": 0,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterangulardampingcoef": 0,
    "shownvgdriver": 0,
    "shownvgcommander": 0,
    "shownvggunner": 0,
    "shownvgcargo": [0],
    "soundattenuationcargo": [1],
    "countsforscoreboard": 1,
    # Class: CfgVehicles|All|MarkerLights [Indent level: 1],
    "markerlights": {
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
    # Class: CfgVehicles|All|SoundEnvironExt [Indent level: 1],
    "soundenvironext": {
    },
    # Class: CfgVehicles|All|SoundEquipment [Indent level: 1],
    "soundequipment": {
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
    "soundlandcrashes": ["soundLandCrash",1],
    "soundwatercrashes": ["soundWaterCrash",1],
    "emptysound": ["",0,1],
    "soundlocked": ["",1,1],
    "soundincommingmissile": ["",1,1],
    "cargoiscodriver": [0],
    "drivercompartments": "Compartment1",
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "hideproxyincombat": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
    "viewcargoshadow": 1,
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
    "drivercaneject": 1,
    "aircapacity": 10,
    "waterdamageengine": 0.2,
    "damagetexdelay": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "windsockexist": 0,
    "slingloadcargomemorypointsdir": [],
    "damagehalf": [],
    "damagefull": [],
    "mingforce": 0.2,
    "gforceshakeattenuation": 0.5,
    # Class: CfgVehicles|All|camShakeDamage [Indent level: 1],
    "camshakedamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minspeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "insidedetectcoef": 0.05,
}