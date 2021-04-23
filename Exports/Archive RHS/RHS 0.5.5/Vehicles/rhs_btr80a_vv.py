rhs_btr80a_vv = {
    "editorpreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_btr80a_vv.paa",
    "author": "Red Hammer Studios",
    "faction": "rhs_faction_vv",
    "crew": "rhs_msv_armoredcrew",
    "rhs_decalparameters": ["['Number', cBTR3NumberPlaces, 'Default']","_gvard1","_gvard2","_gvard3","['Label', cBTRVVLetterSymPlaces, 'Platoon',13]","['Label', cBTROMONSymbolPlaces,'Army',10]"],
    "displayname": "BTR-80A",
    "model": "rhsafrf|addons|rhs_btr80|rhs_btr80a.p3d",
    "icon": "rhsafrf|addons|rhs_c_btr|icons|rhs_btr80a_icon_ca.paa",
    "picture": "rhsafrf|addons|rhs_c_btr|icons|rhs_btr80a_pic_ca.paa",
    "transportsoldier": 7,
    "weaponsgroup1": 128,
    "weaponsgroup4": 64,
    # Class: CfgVehicles|rhs_btr80a_msv|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhs_btr80a_msv|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_01_std_co.paa","rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_02_std_co.paa","rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_03_std_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_btr80a_msv|textureSources|tricolourhard [Indent level: 2],
        "tricolourhard": {
            "displayname": "Tri-Colour (hard-edge)",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_01_tri01_co.paa","rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_02_tri01_co.paa","rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_03_tri01_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_btr80a_msv|textureSources|rhs_sand [Indent level: 2],
        "rhs_sand": {
            "displayname": "Sand",
            "author": "beaar",
            "textures": ["rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_01_des_co.paa","rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_02_des_co.paa","rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_03_des_co.paa"],
            "factions": []
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|rhs_btr80a_msv|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "turretinfotype": "RHS_RscWeaponBPK42_BTR80A_FCS",
            "discretedistance": [100],
            "discretedistanceinitindex": 0,
            "gunneraction": "rhs_btr80a_gunner",
            "gunnerlefthandanimname": "handleHoriz",
            "gunnerrighthandanimname": "handleElev",
            "minelev": -7,
            "maxelev": 70,
            "minturn": -360,
            "maxturn": 360,
            # Class: CfgVehicles|rhs_btr80a_msv|Turrets|MainTurret|TurnIn [Indent level: 3],
            "turnin": {
                "limitsarraytop": [[70,-180],[70,180]],
                "limitsarraybottom": [[-1.5,-180],[-1,-169],[1,-163],[-1,-157],[-7,-155],[-7,0],[-7,154],[-2,157],[-1.5,180]]
            },
            # Class: CfgVehicles|rhs_btr80a_msv|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhs_btr80a_msv|Turrets|MainTurret|OpticsIn|bpk142 [Indent level: 4]
                "bpk142": {
                    "opticsdisplayname": "DAY",
                    "initanglex": 0,
                    "minanglex": -110,
                    "maxanglex": 110,
                    "initangley": 0,
                    "minangley": -110,
                    "maxangley": 110,
                    "opticszoommin": 0.14,
                    "opticszoommax": 0.14,
                    "distancezoommin": 200,
                    "distancezoommax": 2000,
                    "initfov": 0.125,
                    "minfov": 0.125,
                    "maxfov": 0.125,
                    "visionmode": ["Normal"],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_empty",
                    "hitpoint": "Hit_Optic_MainSight"
                },
                # Class: CfgVehicles|rhs_btr80a_msv|Turrets|MainTurret|OpticsIn|bpk142n [Indent level: 4],
                "bpk142n": {
                    "opticsdisplayname": "NIGHT",
                    "initfov": 0.14,
                    "minfov": 0.14,
                    "maxfov": 0.14,
                    "visionmode": ["NVG"],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_bpk142n",
                    "initanglex": 0,
                    "minanglex": -110,
                    "maxanglex": 110,
                    "initangley": 0,
                    "minangley": -110,
                    "maxangley": 110,
                    "opticszoommin": 0.14,
                    "opticszoommax": 0.14,
                    "distancezoommin": 200,
                    "distancezoommax": 2000,
                    "hitpoint": "Hit_Optic_MainSight"
                }
            },
            "weapons": ["rhs_weap_2a72_btr","rhs_weap_pkt_btr80a","rhs_weap_902a"],
            "magazines": ["rhs_mag_3uof8_150","rhs_mag_3ubr11_150","rhs_mag_762x54mm_2000","rhs_mag_3d17_6"],
            "gunnerforceoptics": 0,
            "gunnerhasflares": 0,
            "radartype": 0,
            "soundservo": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|btr80|btr_turret",7,1,30],
            "soundservovertical": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|btr80|btr_turret_elev",7,1,30],
            "viewgunnerinexternal": 1,
            "maxhorizontalrotspeed": 0.65,
            "maxverticalrotspeed": 0.35,
            "gunnerinaction": "rhs_btr70_gunner",
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "gunnerdoor": "l_door",
            "usepip": 2,
            "forcehidegunner": 0,
            "canhidegunner": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 1000,
            "lodturnedout": 1000,
            "gunneroutopticsmodel": "",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh1",
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "body": "mainturret",
            "gun": "maingun",
            "visionmode": ["Normal"],
            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_pp61am",
            "gunneropticseffect": ["TankGunnerOptics1","WeaponsOptics","OpticsCHAbera3"],
            "gunneropticscolor": [1,1,1,1],
            "animationsourcebody": "mainTurret",
            "animationsourcegun": "mainGun",
            "outgunnermayfire": 1,
            "startengine": 0,
            "primarygunner": 1,
            "primaryobserver": 0,
            "stabilizedinaxes": 0,
            "canusescanners": 0,
            "allowtablock": 0,
            "gunnerusespilotview": 1,
            # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 0.8,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passthrough": 1,
                    "minimalhit": 0.44,
                    "radius": 0.2
                },
                # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 0.4,
                    "material": -1,
                    "name": "zbran",
                    "visual": "zbran",
                    "passthrough": 0.1,
                    "minimalhit": 0.44,
                    "radius": 0.2
                }
            },
            # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.241379,
                "minfov": 0.241379,
                "maxfov": 0.241379
            },
            # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initanglex": 5,
                "minanglex": -65,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1
            },
            # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|Turrets [Indent level: 3],
            "turrets": {
            },
            # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                },
                # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_btr_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                }
            },
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "proxyindex": 1,
            "gunnername": "Gunner",
            "gunnertype": "",
            "soundelevation": ["",0.00316228,1],
            "initelev": 0,
            "initturn": 0,
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "primary": 1,
            "hasgunner": 1,
            "commanding": 1,
            "turretcansee": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "turretspec": {
                "showheadphones": 0
            },
            "gunneropticsshowcursor": 0,
            "gunneroutopticscolor": [0,0,0,1],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunneroutopticsshowcursor": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "castgunnershadow": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "ingunnermayfire": 1,
            "showhmd": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "gunnercompartments": "Compartment1",
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
            "forcenvg": 0,
            "iscopilot": 0,
            "caneject": 1,
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "showalltargets": 0,
            "dontcreateai": 0,
            "disablesoundattenuation": 0,
            "slingloadoperator": 0,
            "playerposition": 0,
            "allowlauncherin": 0,
            "allowlauncherout": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
            "turnout": {
                "turnoffset": 0
            },
            "memorypointgunneroptics": "gunnerview",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|CommanderOptics [Indent level: 2],
        "commanderoptics": {
            "gunnerforceoptics": 0,
            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
            # Class: CfgVehicles|rhs_btr80_msv|Turrets|CommanderOptics|Reflectors [Indent level: 3],
            "reflectors": {
                # Class: CfgVehicles|rhs_btr80_msv|Turrets|CommanderOptics|Reflectors|cabin [Indent level: 4]
                "cabin": {
                    "color": [40,350,960],
                    "ambient": [5,0,0],
                    "intensity": 4,
                    "size": 1,
                    "innerangle": 90,
                    "outerangle": 165,
                    "conefadecoef": 1,
                    "position": "cabin_light",
                    "direction": "cabin_light_dir",
                    "hitpoint": "cabin_light",
                    "selection": "cabin_light",
                    "useflare": 1,
                    "flaresize": 1,
                    "flaremaxdistance": 5,
                    "daylight": 1,
                    "blinking": 0,
                    # Class: CfgVehicles|rhs_btr80_msv|Turrets|CommanderOptics|Reflectors|cabin|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 50,
                        "hardlimitstart": 1,
                        "hardlimitend": 1.5
                    }
                },
                # Class: CfgVehicles|rhs_btr80_msv|Turrets|CommanderOptics|Reflectors|cargo_light_1 [Indent level: 4],
                "cargo_light_1": {
                    "color": [40,350,960],
                    "position": "cargo_light_1",
                    "direction": "cargo_light_1_dir",
                    "hitpoint": "cargo_light_1",
                    "selection": "cargo_light_1",
                    "intensity": 3,
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|rhs_btr80_msv|Turrets|CommanderOptics|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 0.5,
                        "hardlimitend": 1.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerangle": 90,
                    "outerangle": 165,
                    "flaresize": 1,
                    "flaremaxdistance": 5,
                    "daylight": 1,
                    "blinking": 0
                }
            },
            "dontcreateai": 1,
            "gunnerdoor": "cHatch",
            "proxytype": "CPCommander",
            "proxyindex": 1,
            "gunnername": "Commander",
            "primarygunner": 0,
            "primaryobserver": 0,
            "gunneropticshidecursor": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "lodturnedin": 1100,
            "lodturnedout": 1100,
            "canhidegunner": 0,
            "body": "obsTurret",
            "gun": "obsGun",
            "animationsourcebody": "obsTurret",
            "animationsourcegun": "obsGun",
            "animationsourcehatch": "commanderHatch",
            "outgunnermayfire": 1,
            "soundservo": ["",0.00316228,1],
            "startengine": 0,
            "minelev": -5,
            "maxelev": 10,
            "initelev": 0,
            "minturn": -36,
            "maxturn": 36,
            "initturn": 0,
            "commanding": 2,
            "viewgunnerinexternal": 1,
            "radartype": 0,
            "gunneroutopticsmodel": "",
            "gunneropticscolor": [1,1,1,1],
            "gunneroutopticscolor": [1,1,1,1],
            "gunneroutforceoptics": 0,
            "gunneroutopticshidecursor": 0,
            "memorypointgunneroutoptics": "obsView_out",
            "memorypointgunneroptics": "obsView",
            "memorypointsgetingunner": "pos commander",
            "memorypointsgetingunnerdir": "pos commander dir",
            "gunnerusespilotview": 1,
            "canusescanners": 0,
            "allowtablock": 0,
            # Class: CfgVehicles|rhs_btr_base|Turrets|CommanderOptics|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initanglex": 5,
                "minanglex": -65,
                "maxanglex": 85,
                "initangley": 0,
                "minangley": -150,
                "maxangley": 150,
                "initfov": 0.7,
                "minfov": 0.25,
                "maxfov": 1.1
            },
            "gunneropticseffect": ["TankGunnerOptics2","OpticsBlur1","OpticsCHAbera3"],
            # Class: CfgVehicles|rhs_btr_base|Turrets|CommanderOptics|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "opticszoommin": 0.14,
                "opticszoommax": 0.14,
                "initfov": 0.14,
                "minfov": 0.14,
                "maxfov": 0.14,
                "visionmode": ["Normal","NVG"]
            },
            "hasgunner": 1,
            "gunneraction": "rhs_btr70_commander",
            "gunnerinaction": "rhs_btr70_commander",
            "weapons": [],
            "magazines": [],
            # Class: CfgVehicles|rhs_btr_base|Turrets|CommanderOptics|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhs_btr_base|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|rhs_btr_base|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_btr_base|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                },
                # Class: CfgVehicles|rhs_btr_base|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    # Class: CfgVehicles|rhs_btr_base|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_btr_base|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                }
            },
            # Class: CfgVehicles|rhs_btr_base|Turrets|CommanderOptics|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            "stabilizedinaxes": 0,
            "animationsourcecamelev": "camElev",
            "gunbeg": "",
            "gunend": "",
            "ingunnermayfire": 1,
            "gunneroutopticsshowcursor": 0,
            "gunneroutopticseffect": [],
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "memorypointgun": "gun_muzzle",
            "selectionfireanim": "zasleh_1",
            "gunnertype": "",
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
            "turretcansee": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "turretspec": {
                "showheadphones": 0
            },
            "gunneropticsshowcursor": 0,
            "turretinfotype": "",
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "castgunnershadow": 0,
            "viewgunnershadow": 1,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "forcehidegunner": 0,
            "showhmd": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "gunnercompartments": "Compartment1",
            "memorypointsgetingunnerprecise": "",
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
            "armorlights": 0.4,
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
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "showalltargets": 0,
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
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|CargoTurret_01 [Indent level: 2],
        "cargoturret_01": {
            "gunnername": "Passenger (Top Right)",
            "gunneraction": "passenger_flatground_2",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "commanding": -2,
            "weapons": ["rhs_weap_DummyLauncher"],
            "memorypointsgetingunner": "cargo9",
            "memorypointsgetingunnerdir": "cargo9 dir",
            "gunnercompartments": "Compartment2",
            "memorypointgunneroptics": "",
            "lodturnedin": 0,
            "lodturnedout": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "proxyindex": 9,
            "maxelev": 45,
            "minelev": -35,
            "maxturn": 61,
            "minturn": -65,
            # Class: CfgVehicles|rhs_btr80_msv|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
            "ispersonturret": 1,
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
            "ejectdeadgunner": 0,
            "canhidegunner": -1,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|CargoTurret_02 [Indent level: 2],
        "cargoturret_02": {
            "gunneraction": "passenger_inside_2",
            "gunnername": "Passenger (Top Front Left)",
            "memorypointsgetingunner": "cargo10",
            "memorypointsgetingunnerdir": "cargo10 dir",
            "proxyindex": 10,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "commanding": -2,
            "weapons": ["rhs_weap_DummyLauncher"],
            "gunnercompartments": "Compartment2",
            "memorypointgunneroptics": "",
            "lodturnedin": 0,
            "lodturnedout": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "maxelev": 45,
            "minelev": -35,
            "maxturn": 61,
            "minturn": -65,
            # Class: CfgVehicles|rhs_btr80_msv|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
            "ispersonturret": 1,
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
            "ejectdeadgunner": 0,
            "canhidegunner": -1,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|CargoTurret_03 [Indent level: 2],
        "cargoturret_03": {
            "gunneraction": "passenger_flatground_3",
            "gunnername": "Passenger (Top Front Right)",
            "memorypointsgetingunner": "cargo11",
            "memorypointsgetingunnerdir": "cargo11 dir",
            "proxyindex": 11,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "commanding": -2,
            "weapons": ["rhs_weap_DummyLauncher"],
            "gunnercompartments": "Compartment2",
            "memorypointgunneroptics": "",
            "lodturnedin": 0,
            "lodturnedout": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "maxelev": 45,
            "minelev": -35,
            "maxturn": 61,
            "minturn": -65,
            # Class: CfgVehicles|rhs_btr80_msv|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
            "ispersonturret": 1,
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
            "ejectdeadgunner": 0,
            "canhidegunner": -1,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|CargoTurret_04 [Indent level: 2],
        "cargoturret_04": {
            "gunneraction": "rhs_cargosys_btr70_12",
            "memorypointsgetingunner": "cargo12",
            "memorypointsgetingunnerdir": "cargo12 dir",
            "gunnername": "Passenger (Top Left)",
            "proxyindex": 12,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "commanding": -2,
            "weapons": ["rhs_weap_DummyLauncher"],
            "gunnercompartments": "Compartment2",
            "memorypointgunneroptics": "",
            "lodturnedin": 0,
            "lodturnedout": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "maxelev": 45,
            "minelev": -35,
            "maxturn": 61,
            "minturn": -65,
            # Class: CfgVehicles|rhs_btr80_msv|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
            "ispersonturret": 1,
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
            "ejectdeadgunner": 0,
            "canhidegunner": -1,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|CargoTurret_05 [Indent level: 2],
        "cargoturret_05": {
            "gunneraction": "passenger_inside_3",
            "gunnername": "Passenger (Top Rear Left)",
            "memorypointsgetingunner": "cargo13",
            "memorypointsgetingunnerdir": "cargo13 dir",
            "proxyindex": 13,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "commanding": -2,
            "weapons": ["rhs_weap_DummyLauncher"],
            "gunnercompartments": "Compartment2",
            "memorypointgunneroptics": "",
            "lodturnedin": 0,
            "lodturnedout": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "maxelev": 45,
            "minelev": -35,
            "maxturn": 61,
            "minturn": -65,
            # Class: CfgVehicles|rhs_btr80_msv|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
            "ispersonturret": 1,
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
            "ejectdeadgunner": 0,
            "canhidegunner": -1,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|CargoTurret_06 [Indent level: 2],
        "cargoturret_06": {
            "gunneraction": "rhs_cargosys_btr70_14",
            "gunnername": "Passenger (Top Back Left)",
            "memorypointsgetingunner": "cargo14",
            "memorypointsgetingunnerdir": "cargo14 dir",
            "proxyindex": 14,
            "maxturn": 71,
            "minturn": -75,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "commanding": -2,
            "weapons": ["rhs_weap_DummyLauncher"],
            "gunnercompartments": "Compartment2",
            "memorypointgunneroptics": "",
            "lodturnedin": 0,
            "lodturnedout": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "maxelev": 45,
            "minelev": -35,
            # Class: CfgVehicles|rhs_btr80_msv|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
            "ispersonturret": 1,
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
            "ejectdeadgunner": 0,
            "canhidegunner": -1,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|CargoTurret_07 [Indent level: 2],
        "cargoturret_07": {
            "gunneraction": "passenger_flatground_4",
            "gunnername": "Passenger (Top Right Middle)",
            "memorypointsgetingunner": "cargo15",
            "memorypointsgetingunnerdir": "cargo15 dir",
            "proxyindex": 15,
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "commanding": -2,
            "weapons": ["rhs_weap_DummyLauncher"],
            "gunnercompartments": "Compartment2",
            "memorypointgunneroptics": "",
            "lodturnedin": 0,
            "lodturnedout": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            "maxelev": 45,
            "minelev": -35,
            "maxturn": 61,
            "minturn": -65,
            # Class: CfgVehicles|rhs_btr80_msv|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
            "ispersonturret": 1,
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
            "ejectdeadgunner": 0,
            "canhidegunner": -1,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|CargoTurret_08 [Indent level: 2],
        "cargoturret_08": {
            "gunneraction": "rhs_cargosys_btr80_01",
            "gunnername": "Passenger (Top Front)",
            "memorypointsgetingunner": "cargo16",
            "memorypointsgetingunnerdir": "cargo16 dir",
            "proxyindex": 16,
            "ejectdeadgunner": 1,
            "maxelev": 0.001,
            "minelev": 0,
            "maxturn": 0.001,
            "minturn": 0,
            "enabledbyanimationsource": "cargoHandler1",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "commanding": -2,
            "weapons": ["rhs_weap_DummyLauncher"],
            "gunnercompartments": "Compartment2",
            "memorypointgunneroptics": "",
            "lodturnedin": 0,
            "lodturnedout": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            # Class: CfgVehicles|rhs_btr80_msv|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
            "ispersonturret": 1,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|CargoTurret_09 [Indent level: 2],
        "cargoturret_09": {
            "proxyindex": 17,
            "gunnername": "Passenger (Top Back Right)",
            "gunneraction": "rhs_cargosys_btr70_04",
            "memorypointsgetingunner": "cargo17",
            "memorypointsgetingunnerdir": "cargo17 dir",
            "ejectdeadgunner": 1,
            "maxelev": 0.001,
            "minelev": 0,
            "maxturn": 0.001,
            "minturn": 0,
            "enabledbyanimationsource": "cargoHandler1",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "commanding": -2,
            "weapons": ["rhs_weap_DummyLauncher"],
            "gunnercompartments": "Compartment2",
            "memorypointgunneroptics": "",
            "lodturnedin": 0,
            "lodturnedout": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            # Class: CfgVehicles|rhs_btr80_msv|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
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
            "ispersonturret": 1,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_btr80a_msv|Turrets|Commander_Out [Indent level: 2],
        "commander_out": {
            "gunnercompartments": "Compartment3",
            "gunnername": "Commander Out",
            "proxytype": "CPCommander",
            "lodturnedin": 0,
            "lodturnedout": 0,
            "proxyindex": 2,
            "gunneraction": "RHS_VehicleTurnout_1",
            "gunnerinaction": "RHS_VehicleTurnout_1",
            "personturretaction": "RHS_VehicleTurnout_1",
            "weapons": ["rhs_weap_DummyLauncher"],
            # Class: CfgVehicles|rhs_btr_base|Turrets|Commander_Out|Hitpoints [Indent level: 3],
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
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "hideweaponsgunner": 0,
            "iscopilot": 0,
            "memorypointsgetingunner": "pos cargo",
            "memorypointsgetingunnerdir": "pos cargo dir",
            "primarygunner": 0,
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
            "canhidegunner": -1,
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        }
    },
    "cargoproxyindexes": [4,1,2,6,3,7,5],
    "getinproxyorder": [4,1,2,6,3,7,5,9,10,11,12,13,14,15,16,17],
    "rhs_toppositions": [9,10,11,12,13,14,15,16,17],
    # Class: CfgVehicles|rhs_btr80a_msv|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhs_btr80a_msv|AnimationSources|recoil_source [Indent level: 2]
        "recoil_source": {
            "source": "reload",
            "weapon": "rhs_weap_2a72_btr"
        },
        # Class: CfgVehicles|rhs_btr80a_msv|AnimationSources|muzzle_hide_hmg [Indent level: 2],
        "muzzle_hide_hmg": {
            "source": "reload",
            "weapon": "rhs_weap_2a72_btr"
        },
        # Class: CfgVehicles|rhs_btr80a_msv|AnimationSources|muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a72_btr"
        },
        # Class: CfgVehicles|rhs_btr80a_msv|AnimationSources|muzzle_rot_mg [Indent level: 2],
        "muzzle_rot_mg": {
            "weapon": "rhs_weap_pkt_btr80a",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|rhs_btr80_msv|AnimationSources|HitPeriscope11 [Indent level: 2],
        "hitperiscope11": {
            "hitpoint": "HitPeriscope11",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr80_msv|AnimationSources|HitPeriscope12 [Indent level: 2],
        "hitperiscope12": {
            "hitpoint": "HitPeriscope12",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr80_msv|AnimationSources|HitPeriscope13 [Indent level: 2],
        "hitperiscope13": {
            "hitpoint": "HitPeriscope13",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr80_msv|AnimationSources|HitPeriscope14 [Indent level: 2],
        "hitperiscope14": {
            "hitpoint": "HitPeriscope14",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr80_msv|AnimationSources|HitPeriscope15 [Indent level: 2],
        "hitperiscope15": {
            "hitpoint": "HitPeriscope15",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr80_msv|AnimationSources|Hit_Optic_Turret_Rear [Indent level: 2],
        "hit_optic_turret_rear": {
            "hitpoint": "Hit_Optic_Turret_Rear",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|smokecap_revolving_source [Indent level: 2],
        "smokecap_revolving_source": {
            "source": "revolving",
            "weapon": "rhs_weap_902a"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|driverViewHatch [Indent level: 2],
        "driverviewhatch": {
            "source": "door",
            "animperiod": 2,
            "initphase": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|commanderViewHatch [Indent level: 2],
        "commanderviewhatch": {
            "source": "door",
            "animperiod": 2,
            "initphase": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|dHatch [Indent level: 2],
        "dhatch": {
            "initphase": 0,
            "animperiod": 1.7,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|cHatch [Indent level: 2],
        "chatch": {
            "initphase": 0,
            "animperiod": 1.7,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|l_door [Indent level: 2],
        "l_door": {
            "initphase": 0,
            "animperiod": 1.7,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|r_door [Indent level: 2],
        "r_door": {
            "initphase": 0,
            "animperiod": 1.7,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|windows [Indent level: 2],
        "windows": {
            "initphase": 0,
            "animperiod": 1.7,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|t_door_1 [Indent level: 2],
        "t_door_1": {
            "initphase": 0,
            "animperiod": 1.7,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|t_door_2 [Indent level: 2],
        "t_door_2": {
            "initphase": 0,
            "animperiod": 1.7,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|engineHatches [Indent level: 2],
        "enginehatches": {
            "initphase": 0,
            "animperiod": 1.7,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|propDoor [Indent level: 2],
        "propdoor": {
            "initphase": 0,
            "animperiod": 1.7,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|cargoHandler1 [Indent level: 2],
        "cargohandler1": {
            "initphase": 1,
            "animperiod": 1.7,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitLFWheel [Indent level: 2],
        "hitlfwheel": {
            "source": "Hit",
            "hitpoint": "HitLFWheel",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitRFWheel [Indent level: 2],
        "hitrfwheel": {
            "hitpoint": "HitRFWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitLBWheel [Indent level: 2],
        "hitlbwheel": {
            "hitpoint": "HitLBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitRBWheel [Indent level: 2],
        "hitrbwheel": {
            "hitpoint": "HitRBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitLF2Wheel [Indent level: 2],
        "hitlf2wheel": {
            "hitpoint": "HitLF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitRF2Wheel [Indent level: 2],
        "hitrf2wheel": {
            "hitpoint": "HitRF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitLMWheel [Indent level: 2],
        "hitlmwheel": {
            "hitpoint": "HitLMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitRMWheel [Indent level: 2],
        "hitrmwheel": {
            "hitpoint": "HitRMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|crate_l1_unhide [Indent level: 2],
        "crate_l1_unhide": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "displayname": "hide crate L1",
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|crate_l2_unhide [Indent level: 2],
        "crate_l2_unhide": {
            "displayname": "hide crate L2",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|crate_l3_unhide [Indent level: 2],
        "crate_l3_unhide": {
            "displayname": "hide crate L3",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|crate_l4_unhide [Indent level: 2],
        "crate_l4_unhide": {
            "displayname": "hide crate L4",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|crate_r1_unhide [Indent level: 2],
        "crate_r1_unhide": {
            "displayname": "hide crate R1",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|crate_r2_unhide [Indent level: 2],
        "crate_r2_unhide": {
            "displayname": "hide crate R2",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|crate_r3_unhide [Indent level: 2],
        "crate_r3_unhide": {
            "displayname": "hide crate R3",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|crate_r4_unhide [Indent level: 2],
        "crate_r4_unhide": {
            "displayname": "hide crate R4",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|water_1_unhide [Indent level: 2],
        "water_1_unhide": {
            "displayname": "hide water crate 1",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|water_2_unhide [Indent level: 2],
        "water_2_unhide": {
            "displayname": "hide water crate 2",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|wheel_1_unhide [Indent level: 2],
        "wheel_1_unhide": {
            "displayname": "hide spare wheel 1",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|wheel_2_unhide [Indent level: 2],
        "wheel_2_unhide": {
            "displayname": "hide spare wheel 2",
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0,
            "sourceaddress": "clamp",
            "mass": -20,
            "author": "Bohemia Interactive"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitPeriscope1 [Indent level: 2],
        "hitperiscope1": {
            "source": "Hit",
            "hitpoint": "HitPeriscope1"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitPeriscope2 [Indent level: 2],
        "hitperiscope2": {
            "hitpoint": "HitPeriscope2",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitPeriscope3 [Indent level: 2],
        "hitperiscope3": {
            "hitpoint": "HitPeriscope3",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitPeriscope4 [Indent level: 2],
        "hitperiscope4": {
            "hitpoint": "HitPeriscope4",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitPeriscope5 [Indent level: 2],
        "hitperiscope5": {
            "hitpoint": "HitPeriscope5",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitPeriscope6 [Indent level: 2],
        "hitperiscope6": {
            "hitpoint": "HitPeriscope6",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitPeriscope7 [Indent level: 2],
        "hitperiscope7": {
            "hitpoint": "HitPeriscope7",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitPeriscope8 [Indent level: 2],
        "hitperiscope8": {
            "hitpoint": "HitPeriscope8",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitPeriscope9 [Indent level: 2],
        "hitperiscope9": {
            "hitpoint": "HitPeriscope9",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitPeriscope10 [Indent level: 2],
        "hitperiscope10": {
            "hitpoint": "HitPeriscope10",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitMainSight [Indent level: 2],
        "hitmainsight": {
            "hitpoint": "Hit_Optic_MainSight",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhs_btr_base|AnimationSources|HitComSight [Indent level: 2],
        "hitcomsight": {
            "hitpoint": "Hit_optic_ComSight",
            "source": "Hit"
        }
    },
    "driverforceoptics": 0,
    "driveraction": "rhs_btr80_driver",
    # Class: CfgVehicles|rhs_btr80_msv|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhs_btr80_msv|UserActions|openDriverViewHatch [Indent level: 2]
        "opendriverviewhatch": {
            "displayname": "Open shield",
            "position": "",
            "radius": 5,
            "hidewindow": 0,
            "condition": "((call rhs_fnc_findPlayer)  == driver this) && (this animationPhase 'driverViewHatch' < 0.5)",
            "statement": "this animateDoor ['driverViewHatch',1];",
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|rhs_btr80_msv|UserActions|closeDriverViewHatch [Indent level: 2],
        "closedriverviewhatch": {
            "displayname": "Close shield",
            "condition": "((call rhs_fnc_findPlayer) == driver this) && (this animationPhase 'driverViewHatch' > 0.5)",
            "statement": "this animateDoor ['driverViewHatch',0];",
            "position": "",
            "radius": 5,
            "hidewindow": 0,
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|rhs_btr80_msv|UserActions|openCommanderViewHatch [Indent level: 2],
        "opencommanderviewhatch": {
            "condition": "((this turretUnit [1]) == (call rhs_fnc_findPlayer) ) && (this animationPhase 'commanderViewHatch' < 0.5)",
            "statement": "this animateDoor ['commanderViewHatch',1];",
            "displayname": "Open shield",
            "position": "",
            "radius": 5,
            "hidewindow": 0,
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|rhs_btr80_msv|UserActions|closeCommanderViewHatch [Indent level: 2],
        "closecommanderviewhatch": {
            "condition": "((this turretUnit [1]) == (call rhs_fnc_findPlayer) ) && (this animationPhase 'commanderViewHatch' > 0.5)",
            "statement": "this animateDoor ['commanderViewHatch',0];",
            "displayname": "Close shield",
            "position": "",
            "radius": 5,
            "hidewindow": 0,
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|rhs_btr80_msv|UserActions|hatch_commander [Indent level: 2],
        "hatch_commander": {
            "displayname": "Turn Out",
            "shortcut": "turnOut",
            "condition": "(this turretUnit [1] isEqualTo (call rhs_fnc_findPlayer)) AND (this turretUnit [9] isEqualTo objNull)",
            "statement": "[this,'cHatch',[[1],[11]],0] spawn rhs_fnc_btr_turnOut",
            "position": "",
            "radius": 5,
            "hidewindow": 0,
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|rhs_btr80_msv|UserActions|hatch_commander_in [Indent level: 2],
        "hatch_commander_in": {
            "displayname": "Turn In",
            "shortcut": "turnIn",
            "condition": "(this turretUnit [11] isEqualTo (call rhs_fnc_findPlayer))",
            "statement": "[this,'cHatch',[[1],[11]],1] spawn rhs_fnc_btr_turnOut",
            "position": "",
            "radius": 5,
            "hidewindow": 0,
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|rhs_btr80_msv|UserActions|ToggleLight [Indent level: 2],
        "togglelight": {
            "displayname": "Toggle interior light",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "(call rhs_fnc_findPlayer) in this;",
            "statement": "[this,'cabinlights_hide',[1]] call rhs_fnc_toggleIntLight",
            "onlyforplayer": 1
        }
    },
    # Class: CfgVehicles|rhs_btr80_msv|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhs_btr80_msv|HitPoints|HitPeriscope11 [Indent level: 2]
        "hitperiscope11": {
            "armor": -10,
            "name": "periscope11",
            "visual": "periscope11",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr80_msv|HitPoints|HitPeriscope12 [Indent level: 2],
        "hitperiscope12": {
            "armor": -10,
            "name": "periscope12",
            "visual": "periscope12",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr80_msv|HitPoints|HitPeriscope13 [Indent level: 2],
        "hitperiscope13": {
            "armor": -10,
            "name": "periscope13",
            "visual": "periscope13",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr80_msv|HitPoints|HitPeriscope14 [Indent level: 2],
        "hitperiscope14": {
            "armor": -10,
            "name": "periscope14",
            "visual": "periscope14",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr80_msv|HitPoints|HitPeriscope15 [Indent level: 2],
        "hitperiscope15": {
            "armor": -10,
            "name": "periscope15",
            "visual": "periscope15",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr80_msv|HitPoints|Hit_Optic_Turret_Rear [Indent level: 2],
        "hit_optic_turret_rear": {
            "name": "Hit_Optic_Turret_Rear",
            "visual": "Hit_Optic_Turret_Rear",
            "armor": -40,
            "explosionshielding": 0.3,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 1,
            "material": -1,
            "name": "engine",
            "visual": "zbytek",
            "passthrough": 0.2,
            "radius": 0.2,
            # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "rhs_engine_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire [Indent level: 4],
                "rhs_engine_fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks [Indent level: 4],
                "rhs_engine_sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "rhs_engine_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "rhs_engine_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
                "rhs_engine_smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small3 [Indent level: 4],
                "rhs_engine_smoke_small3": {
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire2 [Indent level: 4],
                "rhs_engine_fire2": {
                    "type": "SmallFireFPlace",
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_btr_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks2 [Indent level: 4],
                "rhs_engine_sparks2": {
                    "type": "RHS_FireSparks",
                    "position": "engine_smoke4",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                }
            }
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 4,
            "material": -1,
            "name": "palivo",
            "passthrough": 0,
            "radius": 0.15
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitHull [Indent level: 2],
        "hithull": {
            "armor": 0.8,
            "material": -1,
            "name": "telo",
            "visual": "zbytek",
            "passthrough": 1,
            "minimalhit": 0.44,
            "explosionshielding": 1,
            "radius": 0.25
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitLBWheel [Indent level: 2],
        "hitlbwheel": {
            "name": "wheel_1_4_steering",
            "armor": 4,
            "passthrough": 0.1,
            "explosionshielding": 0.9,
            "radius": 0.26,
            "material": -1,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitLMWheel [Indent level: 2],
        "hitlmwheel": {
            "name": "wheel_1_3_steering",
            "armor": 4,
            "passthrough": 0.1,
            "explosionshielding": 0.9,
            "radius": 0.26,
            "material": -1,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitLF2Wheel [Indent level: 2],
        "hitlf2wheel": {
            "name": "wheel_1_2_steering",
            "armor": 4,
            "passthrough": 0.1,
            "explosionshielding": 0.9,
            "radius": 0.26,
            "material": -1,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitLFWheel [Indent level: 2],
        "hitlfwheel": {
            "name": "wheel_1_1_steering",
            "armor": 4,
            "passthrough": 0.1,
            "explosionshielding": 0.9,
            "radius": 0.26,
            "material": -1,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitRBWheel [Indent level: 2],
        "hitrbwheel": {
            "name": "wheel_2_4_steering",
            "armor": 4,
            "passthrough": 0.1,
            "explosionshielding": 0.9,
            "radius": 0.26,
            "material": -1,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitRMWheel [Indent level: 2],
        "hitrmwheel": {
            "name": "wheel_2_3_steering",
            "armor": 4,
            "passthrough": 0.1,
            "explosionshielding": 0.9,
            "radius": 0.26,
            "material": -1,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitRF2Wheel [Indent level: 2],
        "hitrf2wheel": {
            "name": "wheel_2_2_steering",
            "armor": 4,
            "passthrough": 0.1,
            "explosionshielding": 0.9,
            "radius": 0.26,
            "material": -1,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitRFWheel [Indent level: 2],
        "hitrfwheel": {
            "name": "wheel_2_1_steering",
            "armor": 4,
            "passthrough": 0.1,
            "explosionshielding": 0.9,
            "radius": 0.26,
            "material": -1,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 2.5,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "passthrough": 0,
            "radius": 0.18
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "name": "glass2",
            "visual": "glass2",
            "armor": 2.5,
            "material": -1,
            "passthrough": 0,
            "radius": 0.18
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitPeriscope1 [Indent level: 2],
        "hitperiscope1": {
            "armor": -10,
            "name": "periscope1",
            "visual": "periscope1",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitPeriscope2 [Indent level: 2],
        "hitperiscope2": {
            "armor": -10,
            "name": "periscope2",
            "visual": "periscope2",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitPeriscope3 [Indent level: 2],
        "hitperiscope3": {
            "armor": -10,
            "name": "periscope3",
            "visual": "periscope3",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitPeriscope4 [Indent level: 2],
        "hitperiscope4": {
            "armor": -10,
            "name": "periscope4",
            "visual": "periscope4",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitPeriscope5 [Indent level: 2],
        "hitperiscope5": {
            "armor": -10,
            "name": "periscope5",
            "visual": "periscope5",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitPeriscope6 [Indent level: 2],
        "hitperiscope6": {
            "armor": -10,
            "name": "periscope6",
            "visual": "periscope6",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitPeriscope7 [Indent level: 2],
        "hitperiscope7": {
            "armor": -10,
            "name": "periscope7",
            "visual": "periscope7",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitPeriscope8 [Indent level: 2],
        "hitperiscope8": {
            "armor": -10,
            "name": "periscope8",
            "visual": "periscope8",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitPeriscope9 [Indent level: 2],
        "hitperiscope9": {
            "armor": -10,
            "name": "periscope9",
            "visual": "periscope9",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|HitPeriscope10 [Indent level: 2],
        "hitperiscope10": {
            "armor": -10,
            "name": "periscope10",
            "visual": "periscope10",
            "explosionshielding": 0.5,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|Hit_Optic_MainSight [Indent level: 2],
        "hit_optic_mainsight": {
            "armor": -40,
            "explosionshielding": 0.3,
            "name": "mainSight",
            "visual": "mainSight",
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_btr_base|HitPoints|Hit_Optic_ComSight [Indent level: 2],
        "hit_optic_comsight": {
            "name": "comSight",
            "visual": "comSight",
            "armor": -40,
            "explosionshielding": 0.3,
            "radius": 0.05,
            "material": -1,
            "passthrough": 0
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
        # Class: CfgVehicles|Car_F|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "armor": 0.1,
            "material": -1,
            "name": "glass3",
            "visual": "glass3",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "armor": 0.1,
            "material": -1,
            "name": "glass4",
            "visual": "glass4",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "armor": 0.1,
            "material": -1,
            "name": "glass5",
            "visual": "glass5",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "armor": 0.1,
            "material": -1,
            "name": "glass6",
            "visual": "glass6",
            "passthrough": 0,
            "explosionshielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitBody [Indent level: 2],
        "hitbody": {
            "armor": 1,
            "material": -1,
            "name": "karoserie",
            "visual": "zbytek",
            "passthrough": 1,
            "explosionshielding": 1.5
        }
    },
    "normalspeedforwardcoef": 0.6,
    "slowspeedforwardcoef": 0.45,
    "terraincoef": 1.2,
    "turncoef": 2.5,
    "simulation": "carx",
    "dampersbumpcoef": 3,
    "precision": 10,
    "brakedistance": 3,
    "acceleration": 15,
    "fireresistance": 5,
    "maxspeed": 85,
    "fuelcapacity": 30,
    "rhs_fuelcapacity": 300,
    "wheelcircumference": 3.55,
    "brakeidlespeed": 1,
    "canfloat": 1,
    "waterleakiness": 2.5,
    "waterspeedfactor": 0.8,
    "maxfordingdepth": 1.2,
    "waterresistance": 0.5,
    "waterdamageengine": 0.9,
    "waterangulardampingcoef": 5,
    "waterlineardampingcoefy": 2,
    "waterlineardampingcoefx": 2,
    "waterppinvehicle": 0,
    "waterresistancecoef": 0.195,
    "engineshifty": 0.3,
    "engineshiftz": -3,
    "rudderforcecoef": 3.7,
    "rudderforcecoefatmaxspeed": 0.3,
    # Class: CfgVehicles|rhs_btr80_msv|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-7.38,"N",0,"D1",7.82,"D2",4.03,"D3",2.5,"D4",1.53,"D5",1],
        "amphibiousratios": ["R1",-20,"N",0,"D1",25],
        "transmissionratios": ["High",6.13],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R"
    },
    "changegearmineffectivity": [0.95,0,0.85,0.85,0.85,0.85,0.85],
    "switchtime": 0.6,
    "latency": 1.5,
    "differentialtype": "all_limited",
    "frontrearsplit": 0.5,
    "frontbias": 1.3,
    "rearbias": 1.3,
    "centrebias": 1.3,
    "clutchstrength": 75,
    "dampingratefullthrottle": 0.08,
    "dampingratezerothrottleclutchengaged": 1.35,
    "dampingratezerothrottleclutchdisengaged": 0.35,
    "torquecurve": [[0.204778,0.550318],[0.341297,0.898089],[0.546075,1],[0.614334,1],[0.682594,0.955414],[0.750853,0.904459],[0.819113,0.847134],[1.18601,0]],
    "maxomega": 306.83,
    "enginepower": 194,
    "peaktorque": 785,
    "idlerpm": 600,
    "redrpm": 2930,
    "enginelosses": 14,
    "thrustdelay": 0.5,
    "enginebrakecoef": 0.7,
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 0.5,
    "antirollbarspeedmin": 10,
    "antirollbarspeedmax": 40,
    # Class: CfgVehicles|rhs_btr80_msv|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhs_btr80_msv|Wheels|LF [Indent level: 2]
        "lf": {
            "width": 0.33,
            "steering": 1,
            "side": "left",
            "bonename": "wheel_1_1_damper",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "mass": 160,
            "moi": 23,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [-0.125,-1,0],
            "suspforceapppointoffset": "wheel_1_1_axis",
            "tireforceapppointoffset": "wheel_1_1_axis",
            "maxcompression": 0.14,
            "mmaxdroop": 0.14,
            "maxdroop": 0.14,
            "sprungmass": 1595,
            "springstrength": 135000,
            "springdamperrate": 12471,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|rhs_btr80_msv|Wheels|LR [Indent level: 2],
        "lr": {
            "bonename": "wheel_1_2_damper",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "suspforceapppointoffset": "wheel_1_2_axis",
            "tireforceapppointoffset": "wheel_1_2_axis",
            "width": 0.33,
            "steering": 1,
            "side": "left",
            "mass": 160,
            "moi": 23,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [-0.125,-1,0],
            "maxcompression": 0.14,
            "mmaxdroop": 0.14,
            "maxdroop": 0.14,
            "sprungmass": 1595,
            "springstrength": 135000,
            "springdamperrate": 12471,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|rhs_btr80_msv|Wheels|LR2 [Indent level: 2],
        "lr2": {
            "steering": 0,
            "bonename": "wheel_1_3_damper",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "suspforceapppointoffset": "wheel_1_3_axis",
            "tireforceapppointoffset": "wheel_1_3_axis",
            "maxhandbraketorque": 10000,
            "width": 0.33,
            "side": "left",
            "mass": 160,
            "moi": 23,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "susptraveldirection": [-0.125,-1,0],
            "maxcompression": 0.14,
            "mmaxdroop": 0.14,
            "maxdroop": 0.14,
            "sprungmass": 1595,
            "springstrength": 135000,
            "springdamperrate": 12471,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|rhs_btr80_msv|Wheels|LR3 [Indent level: 2],
        "lr3": {
            "bonename": "wheel_1_4_damper",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "suspforceapppointoffset": "wheel_1_4_axis",
            "tireforceapppointoffset": "wheel_1_4_axis",
            "steering": 0,
            "maxhandbraketorque": 10000,
            "width": 0.33,
            "side": "left",
            "mass": 160,
            "moi": 23,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "susptraveldirection": [-0.125,-1,0],
            "maxcompression": 0.14,
            "mmaxdroop": 0.14,
            "maxdroop": 0.14,
            "sprungmass": 1595,
            "springstrength": 135000,
            "springdamperrate": 12471,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|rhs_btr80_msv|Wheels|RF [Indent level: 2],
        "rf": {
            "bonename": "wheel_2_1_damper",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "suspforceapppointoffset": "wheel_2_1_axis",
            "tireforceapppointoffset": "wheel_2_1_axis",
            "steering": 1,
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "width": 0.33,
            "mass": 160,
            "moi": 23,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxhandbraketorque": 0,
            "maxcompression": 0.14,
            "mmaxdroop": 0.14,
            "maxdroop": 0.14,
            "sprungmass": 1595,
            "springstrength": 135000,
            "springdamperrate": 12471,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|rhs_btr80_msv|Wheels|RR [Indent level: 2],
        "rr": {
            "bonename": "wheel_2_2_damper",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "suspforceapppointoffset": "wheel_2_2_axis",
            "tireforceapppointoffset": "wheel_2_2_axis",
            "steering": 1,
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "width": 0.33,
            "mass": 160,
            "moi": 23,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxhandbraketorque": 0,
            "maxcompression": 0.14,
            "mmaxdroop": 0.14,
            "maxdroop": 0.14,
            "sprungmass": 1595,
            "springstrength": 135000,
            "springdamperrate": 12471,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|rhs_btr80_msv|Wheels|RR2 [Indent level: 2],
        "rr2": {
            "steering": 0,
            "bonename": "wheel_2_3_damper",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "suspforceapppointoffset": "wheel_2_3_axis",
            "tireforceapppointoffset": "wheel_2_3_axis",
            "maxhandbraketorque": 10000,
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "width": 0.33,
            "mass": 160,
            "moi": 23,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxcompression": 0.14,
            "mmaxdroop": 0.14,
            "maxdroop": 0.14,
            "sprungmass": 1595,
            "springstrength": 135000,
            "springdamperrate": 12471,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles|rhs_btr80_msv|Wheels|RR3 [Indent level: 2],
        "rr3": {
            "bonename": "wheel_2_4_damper",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "suspforceapppointoffset": "wheel_2_4_axis",
            "tireforceapppointoffset": "wheel_2_4_axis",
            "steering": 0,
            "maxhandbraketorque": 10000,
            "side": "right",
            "susptraveldirection": [0.125,-1,0],
            "width": 0.33,
            "mass": 160,
            "moi": 23,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 12500,
            "maxcompression": 0.14,
            "mmaxdroop": 0.14,
            "maxdroop": 0.14,
            "sprungmass": 1595,
            "springstrength": 135000,
            "springdamperrate": 12471,
            "longitudinalstiffnessperunitgravity": 10000,
            "latstiffx": 3.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1.13],[1,1]]
        }
    },
    # Class: CfgVehicles|rhs_btr80_msv|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_btr70|data|btr_main.rvmat","rhsafrf|addons|rhs_btr70|data|btr_main_damage.rvmat","rhsafrf|addons|rhs_btr70|data|btr_main_destruct.rvmat","rhsafrf|addons|rhs_btr70|data|btr_main2.rvmat","rhsafrf|addons|rhs_btr70|data|btr_main2_damage.rvmat","rhsafrf|addons|rhs_btr70|data|btr_main2_destruct.rvmat","rhsafrf|addons|rhs_btr70|data|btr_in.rvmat","rhsafrf|addons|rhs_btr70|data|btr_in.rvmat","rhsafrf|addons|rhs_btr70|data|btr_in_destruct.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_btr80_01.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_dam_btr80_01.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_destr_btr80_01.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_btr80_02.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_dam_btr80_02.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_destr_btr80_02.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_btr80_03.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_dam_btr80_03.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_destr_btr80_03.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_btr80_04.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_dam_btr80_04.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_destr_btr80_04.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_btr80_01_int.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_btr80_01_int.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_destr_btr80_01.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_btr80_02_int.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_btr80_02_int.rvmat","rhsafrf|addons|rhs_btr80|data|rhs_destr_btr80_01.rvmat","rhsafrf|addons|rhs_btr70|data|scope_glass.rvmat","rhsafrf|addons|rhs_btr70|data|periscope_int_damage.rvmat","rhsafrf|addons|rhs_btr70|data|periscope_int_destroyed.rvmat","rhsafrf|addons|rhs_btr70|data|periscope_int_damage.rvmat","rhsafrf|addons|rhs_btr70|data|periscope_int_destroyed.rvmat","rhsafrf|addons|rhs_btr70|data|periscope_int_destroyed.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    "hiddenselectionstextures": ["rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_01_std_co.paa","rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_02_std_co.paa","rhsafrf|addons|rhs_btr80_camo|data|rhs_btr80_03_std_co.paa","rhsafrf|addons|rhs_btr70|habar|data|sa_gear_02_co.paa","rhsafrf|addons|rhs_btr70|habar|data|sa_gear_02_co.paa"],
    # Class: CfgVehicles|rhs_btr80_msv|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of side number (3 digits)",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cBTR3NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "collapsed": 1,
            "displayname": "Set side number (3 digits)",
            "tooltip": "Set side number. 4 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cBTR3NumberPlaces}else{[_this, [['Number', cBTR3NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalPlatoon_type [Indent level: 2],
        "rhs_decalplatoon_type": {
            "displayname": "Define platoon symbol type",
            "tooltip": "Decal type",
            "property": "rhs_decalPlatoon_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            }
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalPlatoon [Indent level: 2],
        "rhs_decalplatoon": {
            "displayname": "Set platoon symbol",
            "tooltip": "Set platoon symbol located on all 4 sides of vehicle. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBTRPlnSymPlaces,  _this getVariable ['rhs_decalPlatoon_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalArmy_type [Indent level: 2],
        "rhs_decalarmy_type": {
            "displayname": "Define back army symbol type",
            "property": "rhs_decalArmy_type",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Army [Indent level: 4]
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalArmy [Indent level: 2],
        "rhs_decalarmy": {
            "displayname": "Set back army symbol",
            "tooltip": "Define symbol located on right back side of vehicle hull. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalArmy",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBTRBackArmSymPlaces,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalRightTurret_type [Indent level: 2],
        "rhs_decalrightturret_type": {
            "displayname": "Define right turret side symbol type",
            "property": "rhs_decalRightTurret_type",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|Honor [Indent level: 4]
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalRightTurret [Indent level: 2],
        "rhs_decalrightturret": {
            "displayname": "Set right turret side symbol",
            "tooltip": "Define right turret side symbol. Usually used for honor symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalRightTurret",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBTRRightGvardSymPlaces,  _this getVariable ['rhs_decalRightTurret_type','Honor'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalFront_type [Indent level: 2],
        "rhs_decalfront_type": {
            "displayname": "Define front side roundels type",
            "property": "rhs_decalFront_type",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Army [Indent level: 4]
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalFront [Indent level: 2],
        "rhs_decalfront": {
            "displayname": "Set front side roundels",
            "tooltip": "Define symbol located on front of vehicle hull. Usually used for OMON symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalFront",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBTROMONSymbolPlaces,  _this getVariable ['rhs_decalFront_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalVV_type [Indent level: 2],
        "rhs_decalvv_type": {
            "displayname": "Define VV letter type",
            "property": "rhs_decalVV_type",
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalPlatoon_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            }
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_decalVV [Indent level: 2],
        "rhs_decalvv": {
            "displayname": "Set VV letter",
            "tooltip": "Define symbol next to VV 2 digits numbering system decal. Usually used for VV T letter for numbering system (code 13). -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalVV",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBTRVVLetterSymPlaces,  _this getVariable ['rhs_decalVV_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|crate_l1_unhide [Indent level: 2],
        "crate_l1_unhide": {
            "displayname": "hide l1 crate",
            "property": "crate_l1_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|crate_l2_unhide [Indent level: 2],
        "crate_l2_unhide": {
            "displayname": "Hide l2 crate",
            "property": "crate_l2_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|crate_l3_unhide [Indent level: 2],
        "crate_l3_unhide": {
            "displayname": "Hide l3 crate",
            "property": "crate_l3_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|crate_r1_unhide [Indent level: 2],
        "crate_r1_unhide": {
            "displayname": "Hide r1 crate",
            "property": "crate_r1_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|crate_r2_unhide [Indent level: 2],
        "crate_r2_unhide": {
            "displayname": "Hide r2 crate",
            "property": "crate_r2_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|wheel_1_unhide [Indent level: 2],
        "wheel_1_unhide": {
            "displayname": "Hide spare wheel 1",
            "property": "wheel_1_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_disableHabar [Indent level: 2],
        "rhs_disablehabar": {
            "displayname": "Disable habar",
            "property": "rhs_disableHabar",
            "expression": "[_this,_value,'%s',_value] call rhs_fnc_setHabarEden",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|driverViewHatch [Indent level: 2],
        "driverviewhatch": {
            "displayname": "Open driver view hatch",
            "property": "driverViewHatch",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|commanderViewHatch [Indent level: 2],
        "commanderviewhatch": {
            "displayname": "Open commander view hatch",
            "property": "commanderViewHatch",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr80_msv|Attributes|rhs_externalMount [Indent level: 2],
        "rhs_externalmount": {
            "displayname": "Disable external mount",
            "property": "rhs_externalMount",
            "control": "Checkbox",
            "expression": "[_this,_value] call rhs_fnc_lockTop",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type2 [Indent level: 2],
        "rhs_decalnumber_type2": {
            "displayname": "Define font type of side number (2 digits)",
            "tooltip": "Define kind of font that will be drawn on vehicle. 2 digits",
            "property": "rhs_decalNumber_type2",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cBTR2NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "control": "Combo",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber2 [Indent level: 2],
        "rhs_decalnumber2": {
            "displayname": "Set side number (2 digits)",
            "tooltip": "Set side number. 2 numbers are required. Hides on 0",
            "property": "rhs_decalNumber2",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cBTR2NumberPlaces}else{[_this, [['Number', cBTR2NumberPlaces, _this getVariable ['rhs_decalNumber_type2','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "collapsed": 1,
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type3 [Indent level: 2],
        "rhs_decalnumber_type3": {
            "displayname": "Define font type of side number (4 digits)",
            "tooltip": "Define kind of font that will be drawn on vehicle. 4 digits",
            "property": "rhs_decalNumber_type3",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cBTR4NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "control": "Combo",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber3 [Indent level: 2],
        "rhs_decalnumber3": {
            "displayname": "Set side number (4 digits)",
            "tooltip": "Set side number. 4 numbers are required. Hides on 0",
            "property": "rhs_decalNumber3",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cBTR4NumberPlaces}else{[_this, [['Number', cBTR4NumberPlaces, _this getVariable ['rhs_decalNumber_type3','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "collapsed": 1,
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type4 [Indent level: 2],
        "rhs_decalnumber_type4": {
            "displayname": "Define font type of side number (4 digits CDF)",
            "tooltip": "Define kind of font that will be drawn on vehicle. 4 digits, CDF style numbering",
            "property": "rhs_decalNumber_type4",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cBTRCDF4NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "control": "Combo",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalNumber4 [Indent level: 2],
        "rhs_decalnumber4": {
            "displayname": "Set side number (4 digits CDF)",
            "tooltip": "Set side number. 4 numbers are required. Hides on 0",
            "property": "rhs_decalNumber4",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cBTRCDF4NumberPlaces}else{[_this, [['Number', cBTRCDF4NumberPlaces, _this getVariable ['rhs_decalNumber_type4','CDF'], _value] ] ] call rhs_fnc_decalsInit}};",
            "collapsed": 1,
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalLeftTurret_type [Indent level: 2],
        "rhs_decalleftturret_type": {
            "displayname": "Define left turret symbol type",
            "property": "rhs_decalLeftTurret_type",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|Honor [Indent level: 4]
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalRightTurret_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalLeftTurret [Indent level: 2],
        "rhs_decalleftturret": {
            "displayname": "Set left turret symbol",
            "tooltip": "Define symbol located on left side of vehicle turret. Usually used for honor symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalLeftTurret",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBTRLeftGvardSymPlaces,  _this getVariable ['rhs_decalLeftTurret_type','Honor'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalLowerFront_type [Indent level: 2],
        "rhs_decallowerfront_type": {
            "displayname": "Define front hull symbol type",
            "property": "rhs_decalLowerFront_type",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Army [Indent level: 4]
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalLowerFront [Indent level: 2],
        "rhs_decallowerfront": {
            "displayname": "Set front hull symbol",
            "tooltip": "Define symbol located on front of vehicle hull. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalLowerFront",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBTRFrontPlatePlaces,  _this getVariable ['rhs_decalLowerFront_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalFlag_type [Indent level: 2],
        "rhs_decalflag_type": {
            "displayname": "Define flag/side marking type",
            "property": "rhs_decalFlag_type",
            # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Army [Indent level: 4]
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalArmy_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|rhs_decalFlag [Indent level: 2],
        "rhs_decalflag": {
            "displayname": "Set flag/side marking",
            "tooltip": "Define symbol located on front of vehicle hull. Usually used for navy flag symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalFlag",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cBTRFlagSymPlaces,  _this getVariable ['rhs_decalFlag_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|crate_l4_unhide [Indent level: 2],
        "crate_l4_unhide": {
            "displayname": "Hide l4 crate",
            "property": "crate_l4_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|crate_r3_unhide [Indent level: 2],
        "crate_r3_unhide": {
            "displayname": "Hide r3 crate",
            "property": "crate_r3_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|crate_r4_unhide [Indent level: 2],
        "crate_r4_unhide": {
            "displayname": "Hide r4 crate",
            "property": "crate_r4_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|water_1_unhide [Indent level: 2],
        "water_1_unhide": {
            "displayname": "Hide water tank 1",
            "property": "water_1_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|water_2_unhide [Indent level: 2],
        "water_2_unhide": {
            "displayname": "Hide water tank 2",
            "property": "water_2_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|wheel_2_unhide [Indent level: 2],
        "wheel_2_unhide": {
            "displayname": "Hide spare wheel 2",
            "property": "wheel_2_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|dHatch [Indent level: 2],
        "dhatch": {
            "displayname": "Open driver top hatch",
            "property": "dHatch",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|cHatch [Indent level: 2],
        "chatch": {
            "displayname": "Open commander top hatch",
            "property": "cHatch",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|l_door [Indent level: 2],
        "l_door": {
            "displayname": "Open left door",
            "property": "l_door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|r_door [Indent level: 2],
        "r_door": {
            "displayname": "Open right door",
            "property": "r_door",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|windows [Indent level: 2],
        "windows": {
            "displayname": "Open firing ports",
            "property": "windows",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|t_door_1 [Indent level: 2],
        "t_door_1": {
            "displayname": "Open top hatch 1",
            "property": "t_door_1",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|t_door_2 [Indent level: 2],
        "t_door_2": {
            "displayname": "Open top hatch 2",
            "property": "t_door_2",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|engineHatches [Indent level: 2],
        "enginehatches": {
            "displayname": "Open engine hatches",
            "property": "engineHatches",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_btr_base|Attributes|propDoor [Indent level: 2],
        "propdoor": {
            "displayname": "Open propulsion cover",
            "property": "propDoor",
            "expression": "_this animateDoor ['%s',_value,true]",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        }
    },
    "rhs_randomizedhabar": ["crate_l1_unhide","crate_l2_unhide","crate_l3_unhide","crate_r1_unhide","crate_r2_unhide","wheel_1_unhide"],
    # Class: CfgVehicles|rhs_btr80_msv|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhs_btr80_msv|EventHandlers|RHS_BTR_Init [Indent level: 2]
        "rhs_btr_init": {
            "init": "(_this select 0) lockTurret [[11],true];",
            "getout": "(_this + [[11],[9]]) call rhs_fnc_btr_hatch",
            "getin": "(_this + [[11],[9]]) call rhs_fnc_btr_hatch"
        },
        # Class: CfgVehicles|rhs_btr_base|EventHandlers|RHS_EventHandlers [Indent level: 2],
        "rhs_eventhandlers": {
            "init": "_this call rhs_fnc_btr_init;(_this select 0) addeventhandler ['HandleDamage',{[_this,0.1,0.002,0.9,0.2] spawn rhs_fnc_activeTirePressure; _this select 2;} ];",
            "engine": "_this call rhs_fnc_btr_handleHatch;_this call rhs_fnc_engineCheckDamage;"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "scope": 2,
    "driverrightleganimname": "pedalR",
    "driverleftleganimname": "pedalL",
    "vehicleclass": "rhs_vehclass_apc",
    "editorsubcategory": "rhs_EdSubcat_apc",
    "dlc": "RHS_AFRF",
    "rhs_habartype": 2,
    "insidesoundcoef": 0.8,
    "category": "Armored",
    "htmin": 60,
    "htmax": 1800,
    "afmax": 200,
    "mfmax": 100,
    "tf_isolatedamount_api": 0.8,
    "tf_range_api": 17000,
    "side": 0,
    "canhidedriver": 0,
    "mapsize": 8,
    "minomega": 60,
    "accelaidforceyoffset": -0.5,
    "radartype": 0,
    "incomingmissiledetectionsystem": 0,
    "driverlefthandanimname": "drivewheel",
    "driverrighthandanimname": "drivewheel",
    "unitinfotype": "RHS_RscUnitInfoBTR",
    "hideproxyincombat": 0,
    "driverdoor": "dHatch",
    "cargodoors": ["r_door","l_door","r_door","l_door","r_door","l_door","r_door","l_door"],
    "memorypointsgetincargo": ["pos cargo","pos gunner","pos cargo","pos gunner","pos cargo","pos gunner","pos cargo","pos gunner","pos gunner"],
    "memorypointsgetincargodir": ["pos cargo dir","pos gunner dir","pos cargo dir","pos gunner dir","pos cargo dir","pos gunner dir","pos cargo dir","pos gunner dir"],
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
    # Class: CfgVehicles|rhs_btr_base|Library [Indent level: 1],
    "library": {
        "libtextdesc": "This armored personnel carrier was created as a substitute for the older BTR-60 family of APCs and was among the best machines in its class at that time. It was adopted in 1972 and eventually become something more than just a troop carrier. Such numerous and important improvements like centralized tyre-pressure adjustment 2 new powerful eight-cylinder engines and outstanding amphibious capabilities allowed it to become a universal maneuverable and reliable combat vehicle."
    },
    # Class: CfgVehicles|rhs_btr_base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|rhs_btr_base|TransportMagazines|_xx_rhs_30Rnd_545x39_7N10_AK [Indent level: 2]
        "_xx_rhs_30rnd_545x39_7n10_ak": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": 30
        },
        # Class: CfgVehicles|rhs_btr_base|TransportMagazines|_xx_rhs_10Rnd_762x54mmR_7N1 [Indent level: 2],
        "_xx_rhs_10rnd_762x54mmr_7n1": {
            "magazine": "rhs_10Rnd_762x54mmR_7N1",
            "count": 10
        },
        # Class: CfgVehicles|rhs_btr_base|TransportMagazines|_xx_rhs_100Rnd_762x54mmR [Indent level: 2],
        "_xx_rhs_100rnd_762x54mmr": {
            "magazine": "rhs_100Rnd_762x54mmR",
            "count": 3
        },
        # Class: CfgVehicles|rhs_btr_base|TransportMagazines|_xx_rhs_mag_rdg2_white [Indent level: 2],
        "_xx_rhs_mag_rdg2_white": {
            "magazine": "rhs_mag_rdg2_white",
            "count": 2
        },
        # Class: CfgVehicles|rhs_btr_base|TransportMagazines|_xx_rhs_mag_rgd5 [Indent level: 2],
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 9
        },
        # Class: CfgVehicles|rhs_btr_base|TransportMagazines|_xx_rhs_VOG25 [Indent level: 2],
        "_xx_rhs_vog25": {
            "magazine": "rhs_VOG25",
            "count": 20
        },
        # Class: CfgVehicles|rhs_btr_base|TransportMagazines|_xx_rhs_vg40op_white [Indent level: 2],
        "_xx_rhs_vg40op_white": {
            "magazine": "rhs_vg40op_white",
            "count": 5
        },
        # Class: CfgVehicles|rhs_btr_base|TransportMagazines|_xx_rhs_GRD40_white [Indent level: 2],
        "_xx_rhs_grd40_white": {
            "magazine": "rhs_GRD40_white",
            "count": 5
        },
        # Class: CfgVehicles|rhs_btr_base|TransportMagazines|_xx_rhs_rpg26_mag [Indent level: 2],
        "_xx_rhs_rpg26_mag": {
            "magazine": "rhs_rpg26_mag",
            "count": 2
        },
        # Class: CfgVehicles|rhs_btr_base|TransportMagazines|_xx_rhs_rpg7_OG7V_mag [Indent level: 2],
        "_xx_rhs_rpg7_og7v_mag": {
            "magazine": "rhs_rpg7_OG7V_mag",
            "count": 2
        }
    },
    # Class: CfgVehicles|rhs_btr_base|TransportWeapons [Indent level: 1],
    "transportweapons": {
        # Class: CfgVehicles|rhs_btr_base|TransportWeapons|_xx_rhs_weap_ak74m [Indent level: 2]
        "_xx_rhs_weap_ak74m": {
            "weapon": "rhs_weap_ak74m",
            "count": 2
        },
        # Class: CfgVehicles|rhs_btr_base|TransportWeapons|_xx_rhs_weap_rpg26 [Indent level: 2],
        "_xx_rhs_weap_rpg26": {
            "weapon": "rhs_weap_rpg26",
            "count": 2
        },
        # Class: CfgVehicles|rhs_btr_base|TransportWeapons|_xx_rhs_weap_rpg7 [Indent level: 2],
        "_xx_rhs_weap_rpg7": {
            "weapon": "rhs_weap_rpg7",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhs_btr_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhs_btr_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 4
        },
        # Class: CfgVehicles|rhs_btr_base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhs_btr_base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|rhs_btr_base|TransportBackpacks|_xx_rhs_sidor [Indent level: 2]
        "_xx_rhs_sidor": {
            "backpack": "rhs_sidor",
            "count": 7
        },
        # Class: CfgVehicles|rhs_btr_base|TransportBackpacks|_xx_rhs_rpg [Indent level: 2],
        "_xx_rhs_rpg": {
            "backpack": "rhs_rpg",
            "count": 1
        }
    },
    "threat": [1,0.6,0.6],
    "armor": 100,
    "damageresistance": 0.018849,
    "mintotaldamagethreshold": 0.4,
    "crewvulnerable": 0,
    "armorstructural": 6,
    "fuelexplosionpower": 0.1,
    "secondaryexplosion": -1,
    "cargogetinaction": ["GetInAMV_cargo"],
    "cargogetoutaction": ["GetOutLow"],
    "getinaction": "GetInHigh",
    "getoutaction": "GetOutHigh",
    "attenuationeffecttype": "TankAttenuation",
    "soundgetin": ["A3|sounds_f|vehicles|armor|noises|get_in_out",1.56234,1],
    "soundgetout": ["A3|sounds_f|vehicles|armor|noises|get_in_out",1.56234,1,20],
    "sounddammage": ["",1.56234,1],
    "soundengineonint": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_engine_start",1.39811,1],
    "soundengineonext": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_engine_start",1.56234,1,200],
    "soundengineoffint": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_engine_stop",1.39811,1],
    "soundengineoffext": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_engine_stop",1.56234,1,200],
    "buildcrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "buildcrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "buildcrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "buildcrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "soundbuildingcrash": ["buildCrash0",1.25,"buildCrash1",1.25,"buildCrash2",1.25,"buildCrash3",1.25],
    "woodcrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "woodcrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "woodcrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "woodcrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "woodcrash4": ["A3|sounds_f|Vehicles|crashes|crash_01",1,1,200],
    "woodcrash5": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "soundwoodcrash": ["woodCrash0",1.166,"woodCrash1",1.166,"woodCrash2",1.166,"woodCrash3",1.166,"woodCrash4",1.166,"woodCrash5",1.166],
    "armorcrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "armorcrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "armorcrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "armorcrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "soundarmorcrash": ["ArmorCrash0",1.25,"ArmorCrash1",1.25,"ArmorCrash2",1.25,"ArmorCrash3",1.25],
    # Class: CfgVehicles|rhs_btr_base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|rhs_btr_base|Sounds|Idle_ext [Indent level: 2]
        "idle_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_engine_01",1.35481,1,200],
            "frequency": "0.95	+	((rpm/	2300) factor[(10/	2300),(200/	2300)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	2300) factor[(10/	2300),(200/	2300)])	*	((rpm/	2300) factor[(500/	2300),(425/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine [Indent level: 2],
        "engine": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_engine_02",1.39811,1,200],
            "frequency": "0.8	+	((rpm/	2300) factor[(430/	2300),(730/	2300)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2300) factor[(430/	2300),(510/	2300)])	*	((rpm/	2300) factor[(730/	2300),(620/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine1_ext [Indent level: 2],
        "engine1_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_engine_03",1.44668,1,200],
            "frequency": "0.8	+	((rpm/	2300) factor[(630/	2300),(1000/	2300)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2300) factor[(600/	2300),(720/	2300)])	*	((rpm/	2300) factor[(1100/	2300),(840/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine2_ext [Indent level: 2],
        "engine2_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_engine_06",1.50119,1,250],
            "frequency": "0.8	+	((rpm/	2300) factor[(850/	2300),(1300/	2300)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2300) factor[(800/	2300),(1000/	2300)])	*	((rpm/	2300) factor[(1300/	2300),(1100/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine3_ext [Indent level: 2],
        "engine3_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_engine_07",1.56234,1,300],
            "frequency": "0.8	+	((rpm/	2300) factor[(1100/	2300),(1600/	2300)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2300) factor[(1100/	2300),(1270/	2300)])	*	((rpm/	2300) factor[(1550/	2300),(1380/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine4_ext [Indent level: 2],
        "engine4_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_engine_08",1.63096,1,300],
            "frequency": "0.8	+	((rpm/	2300) factor[(1400/	2300),(2000/	2300)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2300) factor[(1380/	2300),(1500/	2300)])	*	((rpm/	2300) factor[(2000/	2300),(1700/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine5_ext [Indent level: 2],
        "engine5_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_engine_10",1.70795,1,300],
            "frequency": "0.8	+	((rpm/	2300) factor[(1700/	2300),(2300/	2300)])*0.1",
            "volume": "engineOn*camPos*((rpm/	2300) factor[(1600/	2300),(2100/	2300)])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|IdleThrust [Indent level: 2],
        "idlethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_exhaust_01",1.56234,1,200],
            "frequency": "0.8	+	((rpm/	2300) factor[(10/	2300),(200/	2300)])*0.15",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(10/	2300),(200/	2300)])	*	((rpm/	2300) factor[(500/	2300),(425/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|EngineThrust [Indent level: 2],
        "enginethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_exhaust_02",1.63096,1,200],
            "frequency": "0.8	+	((rpm/	2300) factor[(430/	2300),(730/	2300)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(430/	2300),(510/	2300)])	*	((rpm/	2300) factor[(730/	2300),(620/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine1_Thrust_ext [Indent level: 2],
        "engine1_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_exhaust_03",1.63096,1,230],
            "frequency": "0.8	+	((rpm/	2300) factor[(630/	2300),(1000/	2300)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(600/	2300),(720/	2300)])	*	((rpm/	2300) factor[(1100/	2300),(840/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine2_Thrust_ext [Indent level: 2],
        "engine2_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_exhaust_06",1.70795,1,250],
            "frequency": "0.8	+	((rpm/	2300) factor[(850/	2300),(1300/	2300)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(800/	2300),(1000/	2300)])	*	((rpm/	2300) factor[(1300/	2300),(1100/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine3_Thrust_ext [Indent level: 2],
        "engine3_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_exhaust_07",1.70795,1,350],
            "frequency": "0.8	+	((rpm/	2300) factor[(1100/	2300),(1600/	2300)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(1100/	2300),(1270/	2300)])	*	((rpm/	2300) factor[(1550/	2300),(1380/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine4_Thrust_ext [Indent level: 2],
        "engine4_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_exhaust_08",1,1,350],
            "frequency": "0.8	+	((rpm/	2300) factor[(1400/	2300),(2000/	2300)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(1380/	2300),(1500/	2300)])	*	((rpm/	2300) factor[(2000/	2300),(1700/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine5_Thrust_ext [Indent level: 2],
        "engine5_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|ext_exhaust_10",1.12202,1,400],
            "frequency": "0.8	+	((rpm/	2300) factor[(1700/	2300),(2300/	2300)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	2300) factor[(1600/	2300),(2100/	2300)])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Idle_int [Indent level: 2],
        "idle_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_engine_01",1.31623,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(10/	2300),(200/	2300)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	2300) factor[(10/	2300),(200/	2300)])	*	((rpm/	2300) factor[(500/	2300),(425/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine_int [Indent level: 2],
        "engine_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_engine_02",1.35481,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(430/	2300),(730/	2300)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2300) factor[(430/	2300),(510/	2300)])	*	((rpm/	2300) factor[(730/	2300),(620/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine1_int [Indent level: 2],
        "engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_engine_03",1.39811,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(630/	2300),(1000/	2300)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2300) factor[(600/	2300),(720/	2300)])	*	((rpm/	2300) factor[(1100/	2300),(840/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine2_int [Indent level: 2],
        "engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_engine_06",1.44668,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(850/	2300),(1300/	2300)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2300) factor[(800/	2300),(1000/	2300)])	*	((rpm/	2300) factor[(1300/	2300),(1100/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine3_int [Indent level: 2],
        "engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_engine_07",1.50119,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(1100/	2300),(1600/	2300)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	2300) factor[(1100/	2300),(1270/	2300)])	*	((rpm/	2300) factor[(1550/	2300),(1380/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine4_int [Indent level: 2],
        "engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_engine_08",1.56234,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(1400/	2300),(2000/	2300)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	2300) factor[(1380/	2300),(1500/	2300)])	*	((rpm/	2300) factor[(2000/	2300),(1700/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine5_int [Indent level: 2],
        "engine5_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_engine_10",1.63096,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(1700/	2300),(2300/	2300)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	2300) factor[(1600/	2300),(2100/	2300)])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|IdleThrust_int [Indent level: 2],
        "idlethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_exhaust_01",1.35481,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(10/	2300),(200/	2300)])*0.15",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(10/	2300),(200/	2300)])	*	((rpm/	2300) factor[(500/	2300),(425/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|EngineThrust_int [Indent level: 2],
        "enginethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_exhaust_02",1.39811,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(430/	2300),(730/	2300)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(430/	2300),(510/	2300)])	*	((rpm/	2300) factor[(730/	2300),(620/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine1_Thrust_int [Indent level: 2],
        "engine1_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_exhaust_03",1.44668,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(630/	2300),(1000/	2300)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(600/	2300),(720/	2300)])	*	((rpm/	2300) factor[(1100/	2300),(840/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine2_Thrust_int [Indent level: 2],
        "engine2_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_exhaust_06",1.44668,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(850/	2300),(1300/	2300)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(800/	2300),(1000/	2300)])	*	((rpm/	2300) factor[(1300/	2300),(1100/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine3_Thrust_int [Indent level: 2],
        "engine3_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_exhaust_07",1.50119,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(1100/	2300),(1600/	2300)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(1100/	2300),(1270/	2300)])	*	((rpm/	2300) factor[(1550/	2300),(1380/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine4_Thrust_int [Indent level: 2],
        "engine4_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_exhaust_08",1.56234,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(1400/	2300),(2000/	2300)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2300) factor[(1380/	2300),(1500/	2300)])	*	((rpm/	2300) factor[(2000/	2300),(1700/	2300)]))"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|Engine5_Thrust_int [Indent level: 2],
        "engine5_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC1|int_exhaust_10",1.63096,1],
            "frequency": "0.8	+	((rpm/	2300) factor[(1700/	2300),(2300/	2300)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	2300) factor[(1600/	2300),(2100/	2300)])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|NoiseInt [Indent level: 2],
        "noiseint": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_int_1",1.50119,1],
            "frequency": "1",
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|NoiseExt [Indent level: 2],
        "noiseext": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_ext_1",1.63096,1,150],
            "frequency": "1",
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresRockOut [Indent level: 2],
        "tiresrockout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_1",1,1,60],
            "frequency": "1",
            "volume": "camPos*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresSandOut [Indent level: 2],
        "tiressandout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-sand1",1,1,60],
            "frequency": "1",
            "volume": "camPos*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresGrassOut [Indent level: 2],
        "tiresgrassout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_2",1,1,60],
            "frequency": "1",
            "volume": "camPos*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresMudOut [Indent level: 2],
        "tiresmudout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-mud2",1,1,60],
            "frequency": "1",
            "volume": "camPos*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresGravelOut [Indent level: 2],
        "tiresgravelout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_gravel_1",1,1,60],
            "frequency": "1",
            "volume": "camPos*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresAsphaltOut [Indent level: 2],
        "tiresasphaltout": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_asfalt_2",1,1,60],
            "frequency": "1",
            "volume": "camPos*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|NoiseOut [Indent level: 2],
        "noiseout": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_int_car_3",1.58489,1,90],
            "frequency": "1",
            "volume": "camPos*(damper0 max 0.02)*(speed factor[0, 8])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresRockIn [Indent level: 2],
        "tiresrockin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_1",1.70795,1],
            "frequency": "1",
            "volume": "(1-camPos)*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresSandIn [Indent level: 2],
        "tiressandin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-sand2",1.70795,1],
            "frequency": "1",
            "volume": "(1-camPos)*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresGrassIn [Indent level: 2],
        "tiresgrassin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_2",1.70795,1],
            "frequency": "1",
            "volume": "(1-camPos)*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresMudIn [Indent level: 2],
        "tiresmudin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-mud2",1.70795,1],
            "frequency": "1",
            "volume": "(1-camPos)*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresGravelIn [Indent level: 2],
        "tiresgravelin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_gravel_1",1.70795,1],
            "frequency": "1",
            "volume": "(1-camPos)*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|TiresAsphaltIn [Indent level: 2],
        "tiresasphaltin": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_asfalt_2",1.70795,1],
            "frequency": "1",
            "volume": "(1-camPos)*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|NoiseIn [Indent level: 2],
        "noisein": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_int_car_3",1.50119,1],
            "frequency": "1",
            "volume": "(damper0 max 0.1)*(speed factor[0, 8])*(1-camPos)"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|breaking_ext_road [Indent level: 2],
        "breaking_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04",1,1,100],
            "frequency": 1,
            "volume": "engineOn*camPos*(LongSlipDrive Factor[-0.2, -0.3])*(Speed Factor[2, 10])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|acceleration_ext_road [Indent level: 2],
        "acceleration_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1,1,100],
            "frequency": 1,
            "volume": "engineOn*camPos*(LongSlipDrive Factor[0.2, 0.3])*(Speed Factor[10, 1])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|turn_left_ext_road [Indent level: 2],
        "turn_left_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1,1,100],
            "frequency": 1,
            "volume": "engineOn*camPos*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|turn_right_ext_road [Indent level: 2],
        "turn_right_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1,1,100],
            "frequency": 1,
            "volume": "engineOn*camPos*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|breaking_ext_dirt [Indent level: 2],
        "breaking_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04",1,1,100],
            "frequency": 1,
            "volume": "engineOn*camPos*(LongSlipDrive Factor[-0.2, -0.3])*(Speed Factor[2, 10])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|acceleration_ext_dirt [Indent level: 2],
        "acceleration_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1,1,100],
            "frequency": 1,
            "volume": "engineOn*camPos*(LongSlipDrive Factor[0.2, 0.3])*(Speed Factor[10, 1])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|turn_left_ext_dirt [Indent level: 2],
        "turn_left_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1,1,100],
            "frequency": 1,
            "volume": "engineOn*camPos*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|turn_right_ext_dirt [Indent level: 2],
        "turn_right_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1,1,100],
            "frequency": 1,
            "volume": "engineOn*camPos*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|breaking_int_road [Indent level: 2],
        "breaking_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04_int",1,1],
            "frequency": 1,
            "volume": "engineOn*(1-camPos)*(LongSlipDrive Factor[-0.2, -0.3])*(Speed Factor[2, 6])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|acceleration_int_road [Indent level: 2],
        "acceleration_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",1,1],
            "frequency": 1,
            "volume": "engineOn*(1-camPos)*(LongSlipDrive Factor[0.2, 0.3])*(Speed Factor[10, 1])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|turn_left_int_road [Indent level: 2],
        "turn_left_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",1,1],
            "frequency": 1,
            "volume": "engineOn*(1-camPos)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|turn_right_int_road [Indent level: 2],
        "turn_right_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",1,1],
            "frequency": 1,
            "volume": "engineOn*(1-camPos)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|breaking_int_dirt [Indent level: 2],
        "breaking_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04_int",1,1],
            "frequency": 1,
            "volume": "engineOn*(1-camPos)*(LongSlipDrive Factor[-0.2, -0.3])*(Speed Factor[2, 6])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|acceleration_int_dirt [Indent level: 2],
        "acceleration_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",1,1],
            "frequency": 1,
            "volume": "engineOn*(1-camPos)*(LongSlipDrive Factor[0.2, 0.3])*(Speed Factor[10, 1])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|turn_left_int_dirt [Indent level: 2],
        "turn_left_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",1,1],
            "frequency": 1,
            "volume": "engineOn*(1-camPos)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles|rhs_btr_base|Sounds|turn_right_int_dirt [Indent level: 2],
        "turn_right_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",1,1],
            "frequency": 1,
            "volume": "engineOn*(1-camPos)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        }
    },
    # Class: CfgVehicles|rhs_btr_base|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|rhs_btr_base|RenderTargets|driverView1 [Indent level: 2]
        "driverview1": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|rhs_btr_base|RenderTargets|driverView1|Camera [Indent level: 3],
            "camera": {
                "pointposition": "pp0",
                "pointdirection": "pd0",
                "rendervisionmode": 0,
                "renderquality": 2,
                "fov": 0.7
            },
            "bboxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles|rhs_btr_base|RenderTargets|driverView2 [Indent level: 2],
        "driverview2": {
            "rendertarget": "rendertarget1",
            # Class: CfgVehicles|rhs_btr_base|RenderTargets|driverView2|Camera [Indent level: 3],
            "camera": {
                "pointposition": "pp1",
                "pointdirection": "pd1",
                "rendervisionmode": 0,
                "renderquality": 2,
                "fov": 0.7
            },
            "bboxes": ["PIP_2_TL","PIP_2_TR","PIP_2_BL","PIP_2_BR"]
        },
        # Class: CfgVehicles|rhs_btr_base|RenderTargets|driverView3 [Indent level: 2],
        "driverview3": {
            "rendertarget": "rendertarget2",
            # Class: CfgVehicles|rhs_btr_base|RenderTargets|driverView3|Camera [Indent level: 3],
            "camera": {
                "pointposition": "pp2",
                "pointdirection": "pd2",
                "rendervisionmode": 0,
                "renderquality": 2,
                "fov": 0.7
            },
            "bboxes": ["PIP_3_TL","PIP_3_TR","PIP_3_BL","PIP_3_BR"]
        },
        # Class: CfgVehicles|rhs_btr_base|RenderTargets|driverView4 [Indent level: 2],
        "driverview4": {
            "rendertarget": "rendertarget3",
            # Class: CfgVehicles|rhs_btr_base|RenderTargets|driverView4|Camera [Indent level: 3],
            "camera": {
                "pointposition": "pp3",
                "pointdirection": "pd3",
                "rendervisionmode": 0,
                "renderquality": 2,
                "fov": 0.7
            },
            "bboxes": ["PIP_4_TL","PIP_4_TR","PIP_4_BL","PIP_4_BR"]
        },
        # Class: CfgVehicles|rhs_btr_base|RenderTargets|commanderView1 [Indent level: 2],
        "commanderview1": {
            "rendertarget": "rendertarget4",
            # Class: CfgVehicles|rhs_btr_base|RenderTargets|commanderView1|Camera [Indent level: 3],
            "camera": {
                "pointposition": "pp4",
                "pointdirection": "pd4",
                "rendervisionmode": 0,
                "renderquality": 2,
                "fov": 0.7
            },
            "bboxes": ["PIP_5_TL","PIP_5_TR","PIP_5_BL","PIP_5_BR"]
        },
        # Class: CfgVehicles|rhs_btr_base|RenderTargets|commanderView2 [Indent level: 2],
        "commanderview2": {
            "rendertarget": "rendertarget5",
            # Class: CfgVehicles|rhs_btr_base|RenderTargets|commanderView2|Camera [Indent level: 3],
            "camera": {
                "pointposition": "pp5",
                "pointdirection": "pd5",
                "rendervisionmode": 0,
                "renderquality": 2,
                "fov": 0.7
            },
            "bboxes": ["PIP_6_TL","PIP_6_TR","PIP_6_BL","PIP_6_BR"]
        },
        # Class: CfgVehicles|rhs_btr_base|RenderTargets|commanderView3 [Indent level: 2],
        "commanderview3": {
            "rendertarget": "rendertarget6",
            # Class: CfgVehicles|rhs_btr_base|RenderTargets|commanderView3|Camera [Indent level: 3],
            "camera": {
                "pointposition": "pp6",
                "pointdirection": "pd6",
                "rendervisionmode": 0,
                "renderquality": 2,
                "fov": 0.7
            },
            "bboxes": ["PIP_7_TL","PIP_7_TR","PIP_7_BL","PIP_7_BR"]
        }
    },
    "engineeffectspeed": 5,
    "memorypointsleftengineeffect": "EngineEffectL",
    "memorypointsrightengineeffect": "EngineEffectR",
    "enablegps": 0,
    "gunnercansee": 14,
    "commandercansee": 14,
    "forcehidedriver": 0,
    "gunnerhasflares": 1,
    "weapons": [],
    "magazines": [],
    "driveropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpo170a",
    "memorypointdriveroptics": "driverview",
    # Class: CfgVehicles|rhs_btr_base|DriverOpticsIn [Indent level: 1],
    "driveropticsin": {
        # Class: CfgVehicles|rhs_btr_base|DriverOpticsIn|OpticView [Indent level: 2]
        "opticview": {
            "opticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpo170a",
            "hitpoint": "Hit_Optic_Driver",
            "initfov": 0.7,
            "minfov": 0.7,
            "maxfov": 0.7,
            "minanglex": -65,
            "maxanglex": 85,
            "minangley": -150,
            "maxangley": 150,
            "minmovex": -0.075,
            "maxmovex": 0.075,
            "minmovey": -0.075,
            "maxmovey": 0.075,
            "minmovez": -0.075,
            "maxmovez": 0.1,
            "initanglex": 15,
            "initangley": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        }
    },
    # Class: CfgVehicles|rhs_btr_base|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initfov": 0.7,
        "minfov": 0.7,
        "maxfov": 0.7,
        "initanglex": 0,
        "minanglex": -110,
        "maxanglex": 110,
        "initangley": 0,
        "minangley": -110,
        "maxangley": 110,
        "opticszoommin": 0.7,
        "opticszoommax": 0.7,
        "distancezoommin": 20,
        "distancezoommax": 2000
    },
    # Class: CfgVehicles|rhs_btr_base|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": 0,
        "minanglex": -85,
        "maxanglex": 85,
        "initangley": 0,
        "minangley": -150,
        "maxangley": 150,
        "initfov": 0.7,
        "minfov": 0.3,
        "maxfov": 1,
        "minmovex": -0.075,
        "maxmovex": 0.075,
        "minmovey": -0.075,
        "maxmovey": 0.075,
        "minmovez": -0.075,
        "maxmovez": 0.1,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "typicalcargo": ["rhs_msv_armoredcrew","rhs_msv_armoredcrew","rhs_msv_armoredcrew"],
    "driverinaction": "rhs_btr70_driver",
    "cargoaction": ["RHS_BTR60_Cargo01","RHS_BMP3_Cargo","RHS_BMP3_Cargo","RHS_BMP3_Cargo","RHS_BTR60_Cargo01","RHS_BMP3_Cargo","RHS_BMP3_Cargo","RHS_BMP3_Cargo"],
    "viewcargoshadow": 1,
    "viewdrivershadow": 1,
    "viewgunnershadow": 1,
    "viewcargoshadowdiff": 0.05,
    "viewdrivershadowdiff": 0.05,
    "viewgunnershadowdiff": 0.05,
    "transportammo": 0,
    "supplyradius": 4.7,
    "memorypointsupply": "doplnovani",
    "transportmaxmagazines": 160,
    "transportmaxweapons": 10,
    # Class: CfgVehicles|rhs_btr_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhs_btr_base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "l svetlo",
            "selection": "Light_L",
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhs_btr_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.15,
                "hardlimitstart": 30,
                "hardlimitend": 120
            }
        },
        # Class: CfgVehicles|rhs_btr_base|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "Light_R",
            "direction": "Light_R_end",
            "hitpoint": "p svetlo",
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
            # Class: CfgVehicles|rhs_btr_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.15,
                "hardlimitstart": 30,
                "hardlimitend": 120
            }
        },
        # Class: CfgVehicles|rhs_btr_base|Reflectors|Right2 [Indent level: 2],
        "right2": {
            "position": "light_R_flare",
            "useflare": 1,
            "direction": "Light_R_end",
            "hitpoint": "p svetlo",
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
            # Class: CfgVehicles|rhs_btr_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.15,
                "hardlimitstart": 30,
                "hardlimitend": 120
            }
        },
        # Class: CfgVehicles|rhs_btr_base|Reflectors|Left2 [Indent level: 2],
        "left2": {
            "position": "light_L_flare",
            "useflare": 1,
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "direction": "Light_L_end",
            "hitpoint": "l svetlo",
            "selection": "Light_L",
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhs_btr_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.15,
                "hardlimitstart": 30,
                "hardlimitend": 120
            }
        }
    },
    "aggregatereflectors": [["Left","Right","Left2","Right2"]],
    "armorlights": 0.1,
    # Class: CfgVehicles|rhs_btr_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhs_btr_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "vyfuk start",
            "direction": "vyfuk konec",
            "effect": "ExhaustsEffect"
        },
        # Class: CfgVehicles|rhs_btr_base|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "vyfuk start 2",
            "direction": "vyfuk konec 2",
            "effect": "ExhaustsEffect"
        }
    },
    "hiddenselections": ["camo1","camo2","camo3","cover1","cover2","i1","i2","i3","i4","i5","i6","i7","n1","n2","n3","n4","n5","n6","n7","n8","n9","n10","n11","i8","i9","i10"],
    # Class: CfgVehicles|rhs_btr_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhs_btr_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhs_btr_base|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_btr_base|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 3],
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles|rhs_btr_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            # Class: CfgVehicles|rhs_btr_base|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_btr_base|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 3],
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles|Car|Components|AICarSteeringComponent [Indent level: 2],
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
    # Class: CfgVehicles|Wheeled_APC_F|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Wheeled_APC_F|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_vehicle_APC_s"],
            "speechplural": ["veh_vehicle_APC_p"]
        }
    },
    "textsingular": "APC",
    "textplural": "APCs",
    "namesound": "veh_vehicle_APC_s",
    "_generalmacro": "Wheeled_APC_F",
    "dampersize": 0.2,
    "damperforce": 1,
    "damperdamping": 1,
    "preferroads": 0,
    "steeraheadsimul": 0.3,
    "steeraheadplan": 0.4,
    "driveoncomponent": ["Slide"],
    "sensorposition": "gunnerView",
    "audible": 14,
    "type": 1,
    "radartarget": 1,
    "radartargetsize": 1.2,
    "visualtarget": 1,
    "visualtargetsize": 1,
    "irtargetsize": 1.2,
    "enableradio": 1,
    "lockdetectionsystem": 0,
    "countermeasureactivationradius": 2000,
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_3",0.316228,1],
    "epeimpulsedamagecoef": 20,
    "crewcrashprotection": 1.25,
    "crewexplosionprotection": 0.999,
    # Class: CfgVehicles|Wheeled_APC_F|PlayerSteeringCoefficients [Indent level: 1],
    "playersteeringcoefficients": {
        "turnincreaseconst": 0.5,
        "turnincreaselinear": 1,
        "turnincreasetime": 0,
        "turndecreaseconst": 5,
        "turndecreaselinear": 0,
        "turndecreasetime": 0,
        "maxturnhundred": 1
    },
    "headgforceleaningfactor": [0.0075,0.005,0.0075],
    "extcameraposition": [0,2,-10],
    "camshakecoef": 0.05,
    "maximumload": 3000,
    "transportmaxbackpacks": 12,
    "smokelaunchergrenadecount": 8,
    "smokelaunchervelocity": 14,
    "smokelauncheronturret": 0,
    "smokelauncherangle": 360,
    # Class: CfgVehicles|Wheeled_APC_F|NewTurret [Indent level: 1],
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
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
    "dammagehalf": [],
    "dammagefull": [],
    "explosionshielding": 1,
    "predictturnplan": 2,
    "predictturnsimul": 1.5,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
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
    "viewcargoshadowamb": 1,
    "accuracy": 0.25,
    "soundenviron": ["",0.000562341,1],
    "soundcrash": ["A3|sounds_f|dummysound",1,1],
    "soundgear": ["",1e-005,1],
    "collisioneffect": "collisionEffect",
    "hideunitinfo": 0,
    "mfact": 1,
    "tbody": 150,
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
    "cost": 40000,
    "unloadincombat": 1,
    "limitedspeedcoef": 0.5,
    "hulldamagecauseexplosion": 1,
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
    "formationx": 20,
    "formationz": 20,
    "scudmodel": "",
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
    "selectionbrakelights": "brzdove svetlo",
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
    "wheeldamagethreshold": 0.2,
    "wheeldestroythreshold": 0.99,
    "wheeldamageradiuscoef": 0.9,
    "wheeldestroyradiuscoef": 0.4,
    "weaponsgroup2": "2 + 		4",
    "weaponsgroup3": "8 + 	16 + 	32",
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "squadtitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
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
    "enablemanualfire": 1,
    "portrait": "",
    "ghostpreview": "",
    "destrtype": "DestructDefault",
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
    "hasdriver": 1,
    "hideweaponsdriver": 1,
    "hideweaponscargo": 0,
    "getinradius": 2.5,
    "enablewatch": 0,
    "useprecisegetinaction": 0,
    "allowtablock": 1,
    "showalltargets": 0,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
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
    "soundcrashes": ["soundCrash",1],
    "soundlandcrashes": ["soundLandCrash",1],
    "soundwatercrashes": ["soundWaterCrash",1],
    "emptysound": ["",0,1],
    "soundbushcrash": ["emptySound",0],
    "soundlocked": ["",1,1],
    "cargoiscodriver": [0],
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadowamb": 1,
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
    "damagetexdelay": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "windsockexist": 0,
    "slingloadcargomemorypoints": [],
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
    "features": "",
    "insidedetectcoef": 0.05,
}