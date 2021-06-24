rhsgref_ins_2s1 = {
    "editorpreview": "rhsgref|addons|rhsgref_editorPreviews|data|rhsgref_ins_2s1.paa",
    "crew": "rhsgref_ins_crew",
    "author": "Red Hammer Studios",
    "side": 0,
    "dlc": "RHS_GREF",
    "faction": "rhsgref_faction_chdkz",
    "scope": 2,
    "texturelist": ["ChDKZ",1,"light_dirty",0.1,"standard_dirty",0.1],
    "rhs_decalparameters": ["['Number', cRHS2S1NumberPlaces ,'Handpaint']"],
    # Class: CfgVehicles|rhsgref_ins_2s1|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhsgref_ins_2s1|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            # Class: CfgVehicles|rhsgref_ins_2s1|Turrets|MainTurret|Turrets [Indent level: 3]
            "turrets": {
                # Class: CfgVehicles|rhsgref_ins_2s1|Turrets|MainTurret|Turrets|CommanderOptics [Indent level: 4]
                "commanderoptics": {
                    "gunnertype": "rhsgref_ins_crew",
                    "body": "obsTurret",
                    "gun": "obsGun",
                    "animationsourcebody": "obsTurret",
                    "animationsourcegun": "obsGun",
                    "maxhorizontalrotspeed": 0.45,
                    "maxverticalrotspeed": 0.07,
                    "stabilizedinaxes": 3,
                    "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_best",0.01,1,50],
                    "minelev": -6,
                    "maxelev": 15,
                    "initelev": 0,
                    "minturn": -171,
                    "maxturn": 124,
                    "initturn": 0,
                    "memorypointgun": "usti hlavne3",
                    "gunbeg": "usti hlavne3",
                    "gunend": "konec hlavne3",
                    "weapons": [],
                    "magazines": [],
                    "turretinfotype": "RscWeaponZeroing",
                    "discretedistance": [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500],
                    "discretedistanceinitindex": 2,
                    "memorypointgunneroutoptics": "commanderview",
                    "memorypointgunneroptics": "commanderview",
                    "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Commander_02_F",
                    "gunneroutopticsmodel": "",
                    "gunneropticseffect": [],
                    "gunnerhasflares": 1,
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
                    "viewoptics": {
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "initfov": 0.155,
                        "minfov": 0.034,
                        "maxfov": 0.155,
                        "visionmode": ["Normal"],
                        "thermalmode": [0,1],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    "commanding": 3,
                    "gunneraction": "rhs_2s1_commander_out",
                    "gunnerinaction": "rhs_2s1_commander",
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "gunnerdoor": "hatchC",
                    "startengine": 0,
                    "viewgunnerinexternal": 1,
                    "outgunnermayfire": 0,
                    "ingunnermayfire": 1,
                    "lodturnedin": 0,
                    "lodturnedout": 0,
                    "lodopticsin": 0,
                    "lodopticsout": 0,
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitTurretCom [Indent level: 6]
                        "hitturretcom": {
                            "isturret": 1,
                            "armor": 0.3,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25
                        },
                        # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitGunCom [Indent level: 6],
                        "hitguncom": {
                            "isgun": 1,
                            "armor": 0.3,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25
                        }
                    },
                    "selectionfireanim": "zasleh3",
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Wide [Indent level: 6]
                        "wide": {
                            "opticsdisplayname": "TKN3",
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                            "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                            "initfov": 0.14,
                            "minfov": 0.14,
                            "maxfov": 0.14,
                            "hitpoint": "Hit_Optic_TKN3",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "visionmode": ["Normal"],
                            "thermalmode": [0,1],
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0,
                            "speedzoommaxspeed": 1e+010,
                            "speedzoommaxfov": 0
                        }
                    },
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        },
                        # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        }
                    },
                    # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
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
                    "proxytype": "CPCommander",
                    "proxyindex": 1,
                    "gunnername": "Commander",
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "animationsourcehatch": "hatchCommander",
                    "animationsourcecamelev": "camElev",
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutforceoptics": 0,
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
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
                    "showcrewaim": 0
                },
                # Class: CfgVehicles|rhsgref_ins_2s1|Turrets|MainTurret|Turrets|LoaderOptics [Indent level: 4],
                "loaderoptics": {
                    "gunnertype": "rhsgref_ins_crew",
                    "body": "LdrTurret",
                    "gun": "LdrGun",
                    "animationsourcebody": "LdrTurret",
                    "animationsourcegun": "LdrGun",
                    "memorypointgunneroutoptics": "loaderview",
                    "memorypointgunneroptics": "loaderview",
                    "gunneroutopticsmodel": "",
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|LoaderOptics|ViewOptics [Indent level: 5],
                    "viewoptics": {
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "initfov": 0.155,
                        "minfov": 0.034,
                        "maxfov": 0.155,
                        "visionmode": ["Normal"],
                        "thermalmode": [0,1],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    "gunnername": "Loader",
                    "proxyindex": 2,
                    "commanding": 2,
                    "gunneraction": "Commander_MBT_01_cannon_F_out",
                    "gunnerinaction": "rhs_2s1_commander",
                    "personturretaction": "vehicle_passenger_stand_2",
                    "ispersonturret": 1,
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "animationsourcehatch": "hatchLoader",
                    "gunnerdoor": "HatchL",
                    "viewgunnerinexternal": 1,
                    "outgunnermayfire": 0,
                    "ingunnermayfire": 0,
                    "lodturnedin": 0,
                    "lodturnedout": 0,
                    "lodopticsin": 0,
                    "lodopticsout": 0,
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|LoaderOptics|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|LoaderOptics|OpticsIn|Periscope [Indent level: 6]
                        "periscope": {
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "initfov": 0.26,
                            "minfov": 0.26,
                            "maxfov": 0.26,
                            "visionmode": ["Normal"],
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
                            "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                            "hitpoint": "Hit_Optic_Periscope",
                            "thermalmode": [0,1],
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0,
                            "speedzoommaxspeed": 1e+010,
                            "speedzoommaxfov": 0
                        }
                    },
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|LoaderOptics|HitPoints [Indent level: 5],
                    "hitpoints": {
                    },
                    "maxhorizontalrotspeed": 0.45,
                    "maxverticalrotspeed": 0.07,
                    "stabilizedinaxes": 3,
                    "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_best",0.01,1,50],
                    "minelev": -6,
                    "maxelev": 15,
                    "initelev": 0,
                    "minturn": -171,
                    "maxturn": 124,
                    "initturn": 0,
                    "memorypointgun": "usti hlavne3",
                    "gunbeg": "usti hlavne3",
                    "gunend": "konec hlavne3",
                    "weapons": [],
                    "magazines": [],
                    "turretinfotype": "RscWeaponZeroing",
                    "discretedistance": [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500],
                    "discretedistanceinitindex": 2,
                    "gunneropticseffect": [],
                    "gunnerhasflares": 1,
                    "startengine": 0,
                    "selectionfireanim": "zasleh3",
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        },
                        # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        }
                    },
                    # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
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
                    "proxytype": "CPCommander",
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "animationsourcecamelev": "camElev",
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutforceoptics": 0,
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
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
                    "showcrewaim": 0
                }
            },
            "memorypointgun": "usti hlavne2",
            "selectionfireanim": "zasleh2",
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "weapons": ["rhs_weap_2a31"],
            "magazines": ["rhs_mag_3of56_35","rhs_mag_bk13_5"],
            "minelev": -5,
            "maxelev": 72,
            "initelev": 10,
            "maxcamelev": 3.55,
            "mincamelev": -3.55,
            "elevationmode": 3,
            "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_best",0.01,1,50],
            "maxhorizontalrotspeed": 0.45,
            "maxverticalrotspeed": 0.15,
            "turretinfotype": "rhs_gui_optic_2s1_op5_computer",
            "discretedistance": [100],
            "discretedistanceinitindex": 0,
            "lockwhenvehiclespeed": 1,
            "memorypointgunneroptics": "gunnerview",
            "gunneroutopticsmodel": "",
            "gunneroutopticseffect": [],
            "gunneropticseffect": [],
            "gunnerforceoptics": 1,
            "lodturnedin": 0,
            "lodturnedout": 0,
            "lodopticsin": 0,
            "lodopticsout": 0,
            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|OpticsIn|PG2 [Indent level: 4]
                "pg2": {
                    "hitpoint": "Hit_Optic_PG2",
                    "opticsdisplayname": "PG2",
                    "initfov": 0.189189,
                    "minfov": 0.189189,
                    "maxfov": 0.189189,
                    "visionmode": ["Normal"],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_pg2.p3d",
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|OpticsIn|Op5_37 [Indent level: 4],
                "op5_37": {
                    "hitpoint": "Hit_Optic_OP5_37",
                    "opticsdisplayname": "OP5",
                    "campos": "op5_pos",
                    "camdir": "op5_dir",
                    "initfov": 0.127273,
                    "minfov": 0.127273,
                    "maxfov": 0.127273,
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_empty.p3d",
                    "visionmode": ["Normal"],
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                }
            },
            "gunneraction": "mbt2_slot2a_out",
            "gunnerinaction": "mbt2_slot2a_in",
            "gunnerdoor": "hatchC",
            "forcehidegunner": 1,
            "ingunnermayfire": 1,
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": -150,
                    "material": -1,
                    "name": "vez",
                    "armorcomponent": "Hit_Turret",
                    "visual": "vez",
                    "passthrough": 0,
                    "minimalhit": -0.2,
                    "explosionshielding": 0.0009,
                    "radius": 0.1
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": -150,
                    "material": -1,
                    "name": "zbran",
                    "armorcomponent": "Hit_Gun",
                    "visual": "-",
                    "passthrough": 0,
                    "minimalhit": -0.2,
                    "explosionshielding": 0.0001,
                    "radius": 0.1
                }
            },
            # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_2s1tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                }
            },
            "commanding": 1,
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "primarygunner": 1,
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
            "primaryobserver": 0,
            "soundelevation": ["",0.00316228,1],
            "minturn": -360,
            "maxturn": 360,
            "initturn": 0,
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
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
            "gunneropticscolor": [0,0,0,1],
            "gunneropticsshowcursor": 0,
            "gunneroutopticscolor": [0,0,0,1],
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
            "outgunnermayfire": 0,
            "showhmd": 0,
            "lockwhendriverout": 0,
            "gunnercompartments": "Compartment1",
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
            "showcrewaim": 0
        }
    },
    # Class: CfgVehicles|rhsgref_ins_2s1|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|rhsgref_ins_2s1|TransportMagazines|_xx_rhs_30Rnd_545x39_7N6M_plum_AK [Indent level: 2]
        "_xx_rhs_30rnd_545x39_7n6m_plum_ak": {
            "magazine": "rhs_30Rnd_545x39_7N6M_plum_AK",
            "count": 10
        },
        # Class: CfgVehicles|rhsgref_ins_2s1|TransportMagazines|_xx_rhs_mag_rgd5 [Indent level: 2],
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 10
        },
        # Class: CfgVehicles|rhsgref_ins_2s1|TransportMagazines|_xx_rhs_mag_nspn_red [Indent level: 2],
        "_xx_rhs_mag_nspn_red": {
            "magazine": "rhs_mag_nspn_red",
            "count": 10
        }
    },
    "category": "Armored",
    "destrtype": "DestructDefault",
    "availableforsupporttypes": ["Artillery"],
    "artilleryscanner": 1,
    "driveoncomponent": ["Track_L","Track_R","Slide"],
    "unitinfotype": "RscUnitInfoArtillery",
    "vehicleclass": "rhs_vehclass_artillery",
    "editorsubcategory": "rhs_EdSubcat_artillery",
    "displayname": "2S1",
    "accuracy": 0.3,
    "model": "rhsafrf|addons|rhs_2s1|rhs_2s1",
    "picture": "rhsafrf|addons|rhs_2s1|ico|rhs_2s1_pic_ca.paa",
    "icon": "rhsafrf|addons|rhs_2s3|ico|ico_2s3_ca.paa",
    "typicalcargo": [],
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "driveraction": "driver_apcwheeled2_out",
    "driverinaction": "rhs_2s1_driver",
    "driverdoor": "hatchD",
    "loddriverturnedout": 0,
    "loddriverturnedin": 0,
    "simulation": "tankX",
    "normalspeedforwardcoef": 0.85,
    "slowspeedforwardcoef": 0.5,
    "fuelcapacity": 25,
    "rhs_fuelcapacity": 1885,
    "maxspeed": 60,
    "canfloat": 1,
    "waterleakiness": 250,
    "maxfordingdepth": 0.05,
    "waterresistance": 2,
    "waterdamageengine": 0.9,
    "engineshifty": 0.7,
    "waterlineardampingcoefy": 2,
    "waterlineardampingcoefx": 2,
    "waterangulardampingcoef": 7.2,
    "waterresistancecoef": 1.75,
    "watereffectspeed": 5,
    "engineeffectspeed": 5,
    "waterfasteffectspeed": 28,
    "rudderforcecoef": 4.5,
    "tankturnforce": 310000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.72,
    "accelaidforcecoef": 4,
    "accelaidforceyoffset": -3.6,
    "accelaidforcespd": 2.23,
    "torquecurve": [[0.35,0.546867],[0.475,0.80136],[0.6,1],[0.7,1],[0.75,0.97863],[0.8,0.947062],[0.9,0.917921],[1.114,0]],
    "enginemoi": 10,
    "enginepower": 220,
    "peaktorque": 1079,
    "minomega": 72,
    "maxomega": 209.44,
    "idlerpm": 700,
    "redrpm": 2000,
    "thrustdelay": 0.3,
    "dampingratefullthrottle": 0.3,
    "dampingratezerothrottleclutchengaged": 3,
    "dampingratezerothrottleclutchdisengaged": 0.25,
    "enginelosses": 25,
    "transmissionlosses": 15,
    "clutchstrength": 20,
    "latency": 1.3,
    "switchtime": 0,
    "changegeartype": "rpmratio",
    "changegearomegaratios": [1,0.5,0.5,0,0.9,0.5,0.9,0.7,0.9,0.7,0.95,0.75,0.95,0.75,1,0.8],
    # Class: CfgVehicles|rhs_2s1tank_base|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-2.235,"N",0,"D1",2.6,"D2",1.5,"D3",1.125,"D4",0.85,"D5",0.64,"D6",0.5],
        "transmissionratios": ["High",12],
        "amphibiousratios": ["R1",-40,"N",0,"D1",40],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.1
    },
    # Class: CfgVehicles|rhs_2s1tank_base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|L2 [Indent level: 2]
        "l2": {
            "susptraveldirection": [-0.125,-1,0],
            "bonename": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|L3 [Indent level: 2],
        "l3": {
            "bonename": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|L4 [Indent level: 2],
        "l4": {
            "bonename": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|L5 [Indent level: 2],
        "l5": {
            "bonename": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|L6 [Indent level: 2],
        "l6": {
            "bonename": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|L7 [Indent level: 2],
        "l7": {
            "bonename": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|L8 [Indent level: 2],
        "l8": {
            "bonename": "wheel_podkolol7",
            "center": "wheel_1_8_axis",
            "boundary": "wheel_1_8_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|L9 [Indent level: 2],
        "l9": {
            "bonename": "",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|L1 [Indent level: 2],
        "l1": {
            "bonename": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|R2 [Indent level: 2],
        "r2": {
            "susptraveldirection": [0.125,-1,0],
            "bonename": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|R3 [Indent level: 2],
        "r3": {
            "bonename": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|R4 [Indent level: 2],
        "r4": {
            "bonename": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|R5 [Indent level: 2],
        "r5": {
            "bonename": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|R6 [Indent level: 2],
        "r6": {
            "bonename": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|R7 [Indent level: 2],
        "r7": {
            "bonename": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|R8 [Indent level: 2],
        "r8": {
            "bonename": "wheel_podkolop7",
            "center": "wheel_2_8_axis",
            "boundary": "wheel_2_8_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "maxdroop": 0.15,
            "maxcompression": 0.15,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|R9 [Indent level: 2],
        "r9": {
            "bonename": "",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Wheels|R1 [Indent level: 2],
        "r1": {
            "bonename": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "width": 0.33,
            "steering": 0,
            "mass": 150,
            "moi": 8.16966,
            "maxbraketorque": 12000,
            "sprungmass": 1142.86,
            "springstrength": 140000,
            "springdamperrate": 7500,
            "dampingrate": 1120,
            "dampingrateinair": 1120,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 4,
            "latstiffy": 50,
            "longitudinalstiffnessperunitgravity": 3000,
            "frictionvsslipgraph": [[0,0.8],[0.38,1],[0.7,0.65]]
        }
    },
    "soundgetin": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1],
    "soundgetout": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1,20],
    "sounddammage": ["",0.562341,1],
    "soundengineonint": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_start",0.707946,1],
    "soundengineonext": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_start",0.630957,1,200],
    "soundengineoffint": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_stop",0.707946,1],
    "soundengineoffext": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_stop",0.630957,1,200],
    "buildcrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "buildcrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "buildcrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "buildcrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "soundbuildingcrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "woodcrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "woodcrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "woodcrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "woodcrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "woodcrash4": ["A3|sounds_f|Vehicles|crashes|crash_01",1,1,200],
    "woodcrash5": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "soundwoodcrash": ["woodCrash0",0.166,"woodCrash1",0.166,"woodCrash2",0.166,"woodCrash3",0.166,"woodCrash4",0.166,"woodCrash5",0.166],
    "armorcrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "armorcrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "armorcrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "armorcrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "soundarmorcrash": ["ArmorCrash0",0.25,"ArmorCrash1",0.25,"ArmorCrash2",0.25,"ArmorCrash3",0.25],
    # Class: CfgVehicles|rhs_2s1tank_base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Idle_ext [Indent level: 2]
        "idle_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_idle",0.707946,1,200],
            "frequency": "0.95	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine [Indent level: 2],
        "engine": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_rpm1",0.794328,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine1_ext [Indent level: 2],
        "engine1_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_rpm2",0.794328,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine2_ext [Indent level: 2],
        "engine2_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_rpm3",0.891251,1,250],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine3_ext [Indent level: 2],
        "engine3_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_rpm4",1,1,300],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine4_ext [Indent level: 2],
        "engine4_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_rpm5",1.12202,1,340],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine5_ext [Indent level: 2],
        "engine5_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_rpm6",1.41254,1,400],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*camPos*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|IdleThrust [Indent level: 2],
        "idlethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_idle",0.891251,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|EngineThrust [Indent level: 2],
        "enginethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm1",1.12202,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine1_Thrust_ext [Indent level: 2],
        "engine1_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm2",1.25893,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine2_Thrust_ext [Indent level: 2],
        "engine2_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm3",1.41254,1,250],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine3_Thrust_ext [Indent level: 2],
        "engine3_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm4",1.58489,1,350],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine4_Thrust_ext [Indent level: 2],
        "engine4_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm5",1.77828,1,400],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine5_Thrust_ext [Indent level: 2],
        "engine5_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm6",1.99526,1,450],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Idle_int [Indent level: 2],
        "idle_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_idle",0.316228,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine_int [Indent level: 2],
        "engine_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm1",0.354813,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine1_int [Indent level: 2],
        "engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm2",0.398107,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine2_int [Indent level: 2],
        "engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm3",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine3_int [Indent level: 2],
        "engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm4",0.501187,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine4_int [Indent level: 2],
        "engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm5",0.562341,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine5_int [Indent level: 2],
        "engine5_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm6",0.630957,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|IdleThrust_int [Indent level: 2],
        "idlethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_idle",0.354813,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|EngineThrust_int [Indent level: 2],
        "enginethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm1",0.398107,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine1_Thrust_int [Indent level: 2],
        "engine1_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm2",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine2_Thrust_int [Indent level: 2],
        "engine2_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm3",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine3_Thrust_int [Indent level: 2],
        "engine3_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm4",0.501187,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine4_Thrust_int [Indent level: 2],
        "engine4_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm5",0.562341,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|Engine5_Thrust_int [Indent level: 2],
        "engine5_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm6",0.630957,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|NoiseInt [Indent level: 2],
        "noiseint": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_int_1",0.562341,1],
            "frequency": "1",
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 25])"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|NoiseExt [Indent level: 2],
        "noiseext": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_ext_1",0.794328,1,150],
            "frequency": "1",
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 25])"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsOutH0 [Indent level: 2],
        "threadsouth0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_01",0.398107,1,140],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsOutH1 [Indent level: 2],
        "threadsouth1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_02",0.446684,1,160],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsOutH2 [Indent level: 2],
        "threadsouth2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_03",0.501187,1,180],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsOutH3 [Indent level: 2],
        "threadsouth3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_04",0.562341,1,200],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsOutH4 [Indent level: 2],
        "threadsouth4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_05",0.562341,1,220],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsOutS0 [Indent level: 2],
        "threadsouts0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_01",0.316228,1,120],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsOutS1 [Indent level: 2],
        "threadsouts1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_02",0.354813,1,140],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsOutS2 [Indent level: 2],
        "threadsouts2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_03",0.398107,1,160],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsOutS3 [Indent level: 2],
        "threadsouts3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_04",0.446684,1,180],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsOutS4 [Indent level: 2],
        "threadsouts4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_05",0.501187,1,200],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsInH0 [Indent level: 2],
        "threadsinh0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_01",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsInH1 [Indent level: 2],
        "threadsinh1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_02",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsInH2 [Indent level: 2],
        "threadsinh2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_03",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsInH3 [Indent level: 2],
        "threadsinh3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_04",0.501187,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsInH4 [Indent level: 2],
        "threadsinh4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_05",0.562341,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsInS0 [Indent level: 2],
        "threadsins0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_01",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsInS1 [Indent level: 2],
        "threadsins1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_02",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsInS2 [Indent level: 2],
        "threadsins2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_03",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsInS3 [Indent level: 2],
        "threadsins3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_04",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Sounds|ThreadsInS4 [Indent level: 2],
        "threadsins4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_05",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        }
    },
    "tracksspeed": 1.35,
    "wheelcircumference": 2.01,
    "attenuationeffecttype": "TankAttenuation",
    "extcameraposition": [0,2,-15],
    "viewdriverinexternal": 1,
    "cost": 1.5e+006,
    "damageresistance": 0.02,
    "crewvulnerable": 0,
    "incomingmissiledetectionsystem": 0,
    "armor": 300,
    "armorstructural": 6,
    "explosionshielding": 10,
    "mintotaldamagethreshold": 0.5,
    # Class: CfgVehicles|rhs_2s1tank_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": -100,
            "name": "telo",
            "armorcomponent": "Hit_Ammo",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.04,
            "explosionshielding": 0.01,
            "radius": 0.1,
            "material": -1
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|HitFuelTank_1 [Indent level: 2],
        "hitfueltank_1": {
            "armor": -80,
            "material": -1,
            "name": "Hit_FuelTank_1",
            "armorcomponent": "Hit_FuelTank_1",
            "visual": "-",
            "passthrough": 0,
            "minimalhit": 0.3,
            "explosionshielding": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|HitFuelTank_2 [Indent level: 2],
        "hitfueltank_2": {
            "name": "Hit_FuelTank_2",
            "armorcomponent": "Hit_FuelTank_2",
            "armor": -80,
            "material": -1,
            "visual": "-",
            "passthrough": 0,
            "minimalhit": 0.3,
            "explosionshielding": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|HitFuelTank_3 [Indent level: 2],
        "hitfueltank_3": {
            "name": "Hit_FuelTank_3",
            "armorcomponent": "Hit_FuelTank_3",
            "armor": -80,
            "material": -1,
            "visual": "-",
            "passthrough": 0,
            "minimalhit": 0.3,
            "explosionshielding": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|HitFuelTank_4 [Indent level: 2],
        "hitfueltank_4": {
            "name": "Hit_FuelTank_4",
            "armorcomponent": "Hit_FuelTank_4",
            "armor": -80,
            "material": -1,
            "visual": "-",
            "passthrough": 0,
            "minimalhit": 0.3,
            "explosionshielding": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 999,
            "name": "Hit_FuelTank_1",
            "armorcomponent": "Hit_FuelTank_1",
            "visual": "-",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.01,
            "depends": "HitFuelTank_1*0.3+HitFuelTank_2*0.3+HitFuelTank_3*0.2+HitFuelTank_4*0.2"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": -150,
            "material": -1,
            "name": "motor",
            "armorcomponent": "Hit_Engine",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.14,
            "explosionshielding": 0.009,
            "radius": 0.18,
            # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: RHS_Effects_Tank_Engine_Destruction|RHS_Engine_Smoke [Indent level: 0],
                "rhs_engine_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                },
                # Class: RHS_Effects_Tank_Engine_Destruction|RHS_Engine_Fire [Indent level: 0],
                "rhs_engine_fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                },
                # Class: RHS_Effects_Tank_Engine_Destruction|RHS_Engine_Sparks [Indent level: 0],
                "rhs_engine_sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                },
                # Class: RHS_Effects_Tank_Engine_Destruction|RHS_Engine_Sounds [Indent level: 0],
                "rhs_engine_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                },
                # Class: RHS_Effects_Tank_Engine_Destruction|RHS_Engine_Smoke_small1 [Indent level: 0],
                "rhs_engine_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                },
                # Class: RHS_Effects_Tank_Engine_Destruction|RHS_Engine_Smoke_small2 [Indent level: 0],
                "rhs_engine_smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60,
                    "enabled": "engineDamage"
                }
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|HitLTrack [Indent level: 2],
        "hitltrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackL",
            "name": "Hit_TrackL",
            "passthrough": 0,
            "material": -1,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "visual": "pas_L"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|HitRTrack [Indent level: 2],
        "hitrtrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackR",
            "name": "Hit_TrackR",
            "material": -1,
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "visual": "pas_P"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|Hit_Optic_Driver [Indent level: 2],
        "hit_optic_driver": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "Hit_Optic_Driver",
            "visual": "-",
            "armorcomponent": "Hit_Optic_Driver",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|Hit_Optic_Periscope [Indent level: 2],
        "hit_optic_periscope": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "Hit_Optic_Periscope",
            "visual": "-",
            "armorcomponent": "Hit_Optic_Periscope",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|Hit_Optic_PG2 [Indent level: 2],
        "hit_optic_pg2": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "Hit_Optic_PG2",
            "visual": "-",
            "armorcomponent": "Hit_Optic_PG2",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|Hit_Optic_OP5_37 [Indent level: 2],
        "hit_optic_op5_37": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "Hit_Optic_OP5_37",
            "visual": "-",
            "armorcomponent": "Hit_Optic_OP5_37",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_2s1tank_base|HitPoints|Hit_Optic_TKN3 [Indent level: 2],
        "hit_optic_tkn3": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "Hit_Optic_TKN3",
            "visual": "-",
            "armorcomponent": "Hit_Optic_TKN3",
            "passthrough": 0
        }
    },
    # Class: CfgVehicles|rhs_2s1tank_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhs_2s1tank_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 4
        }
    },
    "hiddenselections": ["camo1","camo2","camo_sprocket","camo_idler","camo_wheel1","camo_wheel2","camo_wheel3","camo_wheel4","camo_wheel5","camo_wheel6","camo_wheel7","n1","n2","n3","n4","n5","n6","n7","n8","n9","n10","n11","n12","n13","n14","n15","n16","n17","n18","n19","n20","i1","i2","i3","i4","i5","i6","i7"],
    "hiddenselectionstextures": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_hull_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_turret_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa"],
    "hiddenselectionsmaterials": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_hull.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_turret.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat"],
    # Class: CfgVehicles|rhs_2s1tank_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhs_2s1tank_base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_hull_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_turret_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_co.paa"],
            "materials": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_hull.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_turret.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat"],
            "factions": ["rhs_faction_tv","rhs_faction_vmf"]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|textureSources|light [Indent level: 2],
        "light": {
            "displayname": "Light Green",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_hull_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_turret_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_suspension_co.paa"],
            "materials": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_hull.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_turret.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat"],
            "factions": ["rhs_faction_tv","rhs_faction_vmf"]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|textureSources|sand [Indent level: 2],
        "sand": {
            "displayname": "Sand",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_hull_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_turret_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_sand_suspension_co.paa"],
            "materials": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_hull.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_turret.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat"],
            "factions": ["rhs_faction_tv","rhs_faction_vmf"]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|textureSources|standard_dirty [Indent level: 2],
        "standard_dirty": {
            "displayname": "Green Weathered 1",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_hull_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_turret_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_co.paa"],
            "materials": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_hull.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_turret.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension.rvmat"],
            "factions": ["rhs_faction_tv","rhs_faction_vmf"]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|textureSources|light_dirty [Indent level: 2],
        "light_dirty": {
            "displayname": "Green Weathered 2",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_hull_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_turret_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_co.paa","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_co.paa"],
            "materials": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_hull.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_turret.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension.rvmat"],
            "factions": ["rhs_faction_tv","rhs_faction_vmf"]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|textureSources|RHS_SAF_Camo [Indent level: 2],
        "rhs_saf_camo": {
            "displayname": "SAF (Camo)",
            "author": "Red Hammer Studios",
            "textures": ["rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_hull_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_turret_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_suspension_red_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_suspension_green_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_suspension_green_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_suspension_black_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_suspension_green_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_suspension_black_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_suspension_black_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_suspension_green_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|2s1|data|rhs_2s1_saf_suspension_red_co.paa"],
            "factions": ["rhssaf_faction_army"]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|textureSources|CDF [Indent level: 2],
        "cdf": {
            "displayname": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_hull_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_turret_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_suspension_green_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_suspension_green_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_suspension_green_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_suspension_red_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_suspension_green_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_suspension_red_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_suspension_red_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_suspension_green_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_2s1_cdf_suspension_red_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_2s1tank_base|textureSources|ChDKZ [Indent level: 2],
        "chdkz": {
            "displayname": "ChDKZ",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_hull_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_turret_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension_co.paa"],
            "materials": ["rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_hull.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_turret.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|chdkz|rhs_2s1_chdkz_suspension.rvmat"],
            "factions": []
        }
    },
    # Class: CfgVehicles|rhs_2s1tank_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhs_2s1tank_base|UserActions|light_cateyes_off [Indent level: 2]
        "light_cateyes_off": {
            "displayname": "Cat Eyes Off",
            "position": "pos_driverpos",
            "priority": 0.5,
            "showwindow": 0,
            "radius": 2,
            "onlyforplayer": 0,
            "condition": "(call rhs_fnc_findPlayer isEqualTo driver this) && {this animationPhase 'light_cateyes'<0.5};",
            "statement": "this animate ['light_cateyes', 1];"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|UserActions|light_cateyes_on [Indent level: 2],
        "light_cateyes_on": {
            "displayname": "Cat Eyes On",
            "condition": "(call rhs_fnc_findPlayer isEqualTo driver this) && this animationPhase 'light_cateyes'==1;",
            "statement": "this animate ['light_cateyes', 0];",
            "position": "pos_driverpos",
            "priority": 0.5,
            "showwindow": 0,
            "radius": 2,
            "onlyforplayer": 0
        }
    },
    # Class: CfgVehicles|rhs_2s1tank_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of side hull number (3 digits)",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "collapsed": 1,
            "displayname": "Set side hull number (3 digits)",
            "tooltip": "Set side number. 3 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "0",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHS2S1NumberPlaces}else{[_this, [['Number', cRHS2S1NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type2 [Indent level: 2],
        "rhs_decalnumber_type2": {
            "displayname": "Define font type of back small numbers (3 digits)",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
            "property": "rhs_decalNumber_type2",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1BackSmallNumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "control": "Combo",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber2 [Indent level: 2],
        "rhs_decalnumber2": {
            "displayname": "Set back small number (3 digits)",
            "tooltip": "Set back small number. 3 numbers are required. Hides on 0",
            "property": "rhs_decalNumber2",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHS2S1BackSmallNumberPlaces}else{[_this, [['Number', cRHS2S1BackSmallNumberPlaces, _this getVariable ['rhs_decalNumber_type2','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "collapsed": 1,
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type3 [Indent level: 2],
        "rhs_decalnumber_type3": {
            "displayname": "Define font type of back large numbers (3 digits)",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
            "property": "rhs_decalNumber_type3",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1BackLargeNumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "control": "Combo",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber3 [Indent level: 2],
        "rhs_decalnumber3": {
            "displayname": "Set back large number (3 digits)",
            "tooltip": "Set back large number. 3 numbers are required. Hides on 0",
            "property": "rhs_decalNumber3",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHS2S1BackLargeNumberPlaces}else{[_this, [['Number', cRHS2S1BackLargeNumberPlaces, _this getVariable ['rhs_decalNumber_type3','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "collapsed": 1,
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type4 [Indent level: 2],
        "rhs_decalnumber_type4": {
            "displayname": "Define font type of back turret number (3 digits)",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
            "property": "rhs_decalNumber_type4",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1BackTurretNumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "control": "Combo",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber4 [Indent level: 2],
        "rhs_decalnumber4": {
            "displayname": "Set back turret number (3 digits)",
            "tooltip": "Set back turret number. 3 numbers are required. Hides on 0",
            "property": "rhs_decalNumber4",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHS2S1BackTurretNumberPlaces}else{[_this, [['Number', cRHS2S1BackTurretNumberPlaces, _this getVariable ['rhs_decalNumber_type4','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "collapsed": 1,
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type5 [Indent level: 2],
        "rhs_decalnumber_type5": {
            "displayname": "Define font type of front turret number (3 digits)",
            "tooltip": "Define kind of font that will be drawn on vehicle. 3 digits",
            "property": "rhs_decalNumber_type5",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1FrontTurretNumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "control": "Combo",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber5 [Indent level: 2],
        "rhs_decalnumber5": {
            "displayname": "Set front turret number (3 digits)",
            "tooltip": "Set front turret number. 3 numbers are required. Hides on 0",
            "property": "rhs_decalNumber5",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHS2S1FrontTurretNumberPlaces}else{[_this, [['Number', cRHS2S1FrontTurretNumberPlaces, _this getVariable ['rhs_decalNumber_type5','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "collapsed": 1,
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type6 [Indent level: 2],
        "rhs_decalnumber_type6": {
            "displayname": "Define font type of front turret number (5 digits)",
            "tooltip": "Define kind of font that will be drawn on vehicle. 5 digits",
            "property": "rhs_decalNumber_type6",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHS2S1SerbianNumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "control": "Combo",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalNumber6 [Indent level: 2],
        "rhs_decalnumber6": {
            "displayname": "Set front turret number (5 digits, Serbian)",
            "tooltip": "Set front turret number. 5 numbers are required. Hides on 0",
            "property": "rhs_decalNumber6",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHS2S1SerbianNumberPlaces}else{[_this, [['Number', cRHS2S1SerbianNumberPlaces, _this getVariable ['rhs_decalNumber_type6','CDF'], _value] ] ] call rhs_fnc_decalsInit}};",
            "collapsed": 1,
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonBack_type [Indent level: 2],
        "rhs_decalplatoonback_type": {
            "displayname": "Define back door platoon symbol type",
            "tooltip": "Decal type",
            "property": "rhs_decalPlatoonBack_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonBack_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonBack_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonBack_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonBack_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonBack_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonBack_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonBack_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonBack [Indent level: 2],
        "rhs_decalplatoonback": {
            "displayname": "Set platoon symbol",
            "tooltip": "Set platoon symbol located on the back of the vehicle. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1BackSymbol],  _this getVariable ['rhs_decalPlatoonBack_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackRight_type [Indent level: 2],
        "rhs_decalplatoonturretbackright_type": {
            "displayname": "Define back turret right symbol type",
            "property": "rhs_decalPlatoonTurretBackRight_type",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackRight_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackRight_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackRight_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackRight_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackRight_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackRight_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackRight_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackRight [Indent level: 2],
        "rhs_decalplatoonturretbackright": {
            "displayname": "Set back turret right symbol",
            "tooltip": "Define symbol located on right back side of vehicle turret. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoonTurretBackRight",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1TurretBackRightSymbol],  _this getVariable ['rhs_decalPlatoonTurretBackRight_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackLeft_type [Indent level: 2],
        "rhs_decalplatoonturretbackleft_type": {
            "displayname": "Define back turret left symbol type",
            "property": "rhs_decalPlatoonTurretBackLeft_type",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackLeft_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackLeft_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackLeft_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackLeft_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackLeft_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackLeft_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackLeft_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretBackLeft [Indent level: 2],
        "rhs_decalplatoonturretbackleft": {
            "displayname": "Set back turret left symbol",
            "tooltip": "Define symbol located on left back side of vehicle turret. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoonTurretBackLeft",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1TurretBackLeftSymbol],  _this getVariable ['rhs_decalPlatoonTurretBackLeft_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontRight_type [Indent level: 2],
        "rhs_decalplatoonturretfrontright_type": {
            "displayname": "Define front turret right symbol type",
            "property": "rhs_decalPlatoonTurretFrontRight_type",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontRight_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontRight_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontRight_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontRight_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontRight_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontRight_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontRight_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontRight [Indent level: 2],
        "rhs_decalplatoonturretfrontright": {
            "displayname": "Set front turret right symbol",
            "tooltip": "Define symbol located on right front side of vehicle turret. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoonTurretFrontRight",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1TurretFrontRightSymbol],  _this getVariable ['rhs_decalPlatoonTurretFrontRight_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontLeft_type [Indent level: 2],
        "rhs_decalplatoonturretfrontleft_type": {
            "displayname": "Define front turret left symbol type",
            "property": "rhs_decalPlatoonTurretFrontLeft_type",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontLeft_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontLeft_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontLeft_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontLeft_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontLeft_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontLeft_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontLeft_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonTurretFrontLeft [Indent level: 2],
        "rhs_decalplatoonturretfrontleft": {
            "displayname": "Set front turret left symbol",
            "tooltip": "Define symbol located on left front side of vehicle turret. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoonTurretFrontLeft",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1TurretFrontLeftSymbol],  _this getVariable ['rhs_decalPlatoonTurretFrontLeft_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullLeft_type [Indent level: 2],
        "rhs_decalplatoonhullleft_type": {
            "displayname": "Define hull left symbol type",
            "property": "rhs_decalPlatoonHullLeft_type",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullLeft_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullLeft_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullLeft_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullLeft_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullLeft_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullLeft_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullLeft_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullLeft [Indent level: 2],
        "rhs_decalplatoonhullleft": {
            "displayname": "Set hull left symbol",
            "tooltip": "Define symbol located on left side of vehicle hull. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoonHullLeft",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1HullLeftSymbol],  _this getVariable ['rhs_decalPlatoonHullLeft_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullRight_type [Indent level: 2],
        "rhs_decalplatoonhullright_type": {
            "displayname": "Define hull right symbol type",
            "property": "rhs_decalPlatoonHullRight_type",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullRight_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullRight_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullRight_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullRight_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullRight_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullRight_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullRight_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_decalPlatoonHullRight [Indent level: 2],
        "rhs_decalplatoonhullright": {
            "displayname": "Set hull right symbol",
            "tooltip": "Define symbol located on right side of vehicle hull. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoonHullRight",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', [cRHS2S1HullRightSymbol],  _this getVariable ['rhs_decalPlatoonHullRight_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_1_type [Indent level: 2],
        "rhs_ammoslot_1_type": {
            "displayname": "Ammo slot #1 type",
            "tooltip": "Define type of shell for #1 slot [HE rounds]",
            "property": "rhs_ammoslot_1_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_1_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_of462 [Indent level: 4]
                "rhs_mag_of462": {
                    "name": "53-OF-462 HE",
                    "value": "rhs_mag_of462",
                    "defaultvalue": "rhs_mag_of462"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3of56 [Indent level: 4],
                "rhs_mag_3of56": {
                    "name": "3OF56 HE",
                    "value": "rhs_mag_3of56",
                    "defaultvalue": "rhs_mag_3of56"
                }
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_1 [Indent level: 2],
        "rhs_ammoslot_1": {
            "displayname": "Ammo slot #1 count",
            "tooltip": "Define number of rounds stored inside of type #1. Max 40. Leave -1 for default loadout",
            "property": "rhs_ammoslot_1",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',40,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_2_type [Indent level: 2],
        "rhs_ammoslot_2_type": {
            "displayname": "Ammo slot #2 type",
            "tooltip": "Define type of shell for #2 slot [Smoke rounds]",
            "property": "rhs_ammoslot_2_type",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_2_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_d462 [Indent level: 4]
                "rhs_mag_d462": {
                    "name": "53-D-462 Smoke",
                    "value": "rhs_mag_d462",
                    "defaultvalue": "rhs_mag_d462"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_2 [Indent level: 2],
        "rhs_ammoslot_2": {
            "displayname": "Ammo slot #2 count",
            "tooltip": "Define number of rounds stored inside of type #2. Max 40. Leave -1 for default loadout",
            "property": "rhs_ammoslot_2",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',40,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_3_type [Indent level: 2],
        "rhs_ammoslot_3_type": {
            "displayname": "Ammo slot #3 type",
            "tooltip": "Define type of shell for #3 slot [Illumination rounds]",
            "property": "rhs_ammoslot_3_type",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_3_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_3_type|values|rhs_mag_s463 [Indent level: 4]
                "rhs_mag_s463": {
                    "name": "53-S-463 Flare",
                    "value": "rhs_mag_s463",
                    "defaultvalue": "rhs_mag_s463"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_3 [Indent level: 2],
        "rhs_ammoslot_3": {
            "displayname": "Ammo slot #3 count",
            "tooltip": "Define number of rounds stored inside of type #3. Max 40. Leave -1 for default loadout",
            "property": "rhs_ammoslot_3",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',40,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_4_type [Indent level: 2],
        "rhs_ammoslot_4_type": {
            "displayname": "Ammo slot #4 type",
            "tooltip": "Define type of shell for #4 slot [HEAT rounds]",
            "property": "rhs_ammoslot_4_type",
            # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_4_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_bk6m [Indent level: 4]
                "rhs_mag_bk6m": {
                    "name": "3BK6M HEAT",
                    "value": "rhs_mag_bk6m",
                    "defaultvalue": "rhs_mag_bk6m"
                },
                # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_bk13 [Indent level: 4],
                "rhs_mag_bk13": {
                    "name": "3BK13 HEAT",
                    "value": "rhs_mag_bk13",
                    "defaultvalue": "rhs_mag_bk13"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Attributes|rhs_ammoslot_4 [Indent level: 2],
        "rhs_ammoslot_4": {
            "displayname": "Ammo slot #4 count",
            "tooltip": "Define number of rounds stored inside of type #4. Max 40. Leave -1 for default loadout",
            "property": "rhs_ammoslot_4",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',40,['rhs_ammoslot_1','rhs_ammoslot_2','rhs_ammoslot_3','rhs_ammoslot_4','rhs_ammoslot_5']] spawn rhs_fnc_Eden_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        }
    },
    "driverforceoptics": 1,
    "driveropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpo170a",
    "driveropticscolor": [1,1,1,1],
    "driveropticseffect": ["OpticsCHAbera1"],
    "driveroutopticseffect": [],
    # Class: CfgVehicles|rhs_2s1tank_base|DriverOpticsIn [Indent level: 1],
    "driveropticsin": {
        # Class: CfgVehicles|rhs_2s1tank_base|DriverOpticsIn|OpticView [Indent level: 2]
        "opticview": {
            "opticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpo170a",
            "hitpoint": "Hit_Optic_Driver",
            "initfov": 0.7,
            "minfov": 0.7,
            "maxfov": 0.7,
            "initanglex": 7,
            "initangley": 0,
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
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        }
    },
    # Class: CfgVehicles|rhs_2s1tank_base|ViewOptics [Indent level: 1],
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
    # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources|reload_source [Indent level: 2]
        "reload_source": {
            "weapon": "rhs_weap_2a31",
            "source": "reload"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources|reload_magazine_source [Indent level: 2],
        "reload_magazine_source": {
            "source": "reloadMagazine",
            "weapon": "rhs_weap_2a31"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources|muzzle_hide_arty [Indent level: 2],
        "muzzle_hide_arty": {
            "source": "reload",
            "weapon": "rhs_weap_2a31"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources|HatchC [Indent level: 2],
        "hatchc": {
            "source": "door",
            "animperiod": 0.8
        },
        # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources|HatchD [Indent level: 2],
        "hatchd": {
            "source": "door",
            "animperiod": 0.8
        },
        # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources|turretHide [Indent level: 2],
        "turrethide": {
            "source": "user",
            "initphase": 0,
            "animperiod": 1e-010
        },
        # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources|hide_shields_hull [Indent level: 2],
        "hide_shields_hull": {
            "source": "user",
            "mass": 1,
            "animperiod": 1e-006,
            "initphase": 1,
            "displayname": "Hide Hull Watershields",
            "forceanimatephase": 0,
            "forceanimate": ["hide_shields_turret",1]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources|hide_shields_turret [Indent level: 2],
        "hide_shields_turret": {
            "displayname": "Hide Turret Watershields",
            "initphase": 0,
            "forceanimatephase": 0,
            "forceanimate": ["hide_shields_hull",1],
            "source": "user",
            "mass": 1,
            "animperiod": 1e-006
        },
        # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources|hide_backframe [Indent level: 2],
        "hide_backframe": {
            "displayname": "Hide Watershield Frame",
            "initphase": 0,
            "source": "user",
            "mass": 1,
            "animperiod": 1e-006,
            "forceanimatephase": 0,
            "forceanimate": ["hide_shields_turret",1]
        },
        # Class: CfgVehicles|rhs_2s1tank_base|AnimationSources|light_cateyes [Indent level: 2],
        "light_cateyes": {
            "source": "user",
            "animperiod": 1e-005,
            "initphase": 1
        }
    },
    "animationlist": ["hide_shields_hull",0.5,"hide_backframe",0.4,"hide_shields_turret",0.2],
    # Class: CfgVehicles|rhs_2s1tank_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_hull.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_hull_dam.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_hull_des.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_turret.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_turret_dam.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_turret_des.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_dam.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_light_dirty_suspension_des.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_hull.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_hull_dam.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_hull_des.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_turret.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_turret_dam.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_turret_des.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_dam.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_dirty_suspension_des.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_hull.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_hull_dam.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_hull_des.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_turret.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_turret_dam.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_turret_des.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_dam.rvmat","rhsafrf|addons|rhs_2s1|data|rhs_2s1_suspension_des.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles|rhs_2s1tank_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhs_2s1tank_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaustl",
            "direction": "exhaustl_dir",
            "effect": "ExhaustEffectTankSide"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "exhaustr",
            "direction": "exhaustr_dir",
            "effect": "ExhaustEffectTankSide"
        }
    },
    # Class: CfgVehicles|rhs_2s1tank_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhs_2s1tank_base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "l svetlo",
            "direction": "konec l svetla",
            "hitpoint": "l svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhs_2s1tank_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Reflectors|Left2 [Indent level: 2],
        "left2": {
            "direction": "konec l svetla",
            "useflare": 1,
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "l svetlo",
            "hitpoint": "l svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerangle": 100,
            "outerangle": 179,
            "conefadecoef": 10,
            "intensity": 1,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|rhs_2s1tank_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        }
    },
    "aggregatereflectors": [["Left"]],
    # Class: CfgVehicles|rhs_2s1tank_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhs_2s1tank_base|EventHandlers|RHS_EventHandlers [Indent level: 2]
        "rhs_eventhandlers": {
            "init": "_this call rhs_fnc_2s1_init",
            "postinit": "_this call rhs_fnc_reapplyTextures",
            "fired": "_this call RHS_fnc_2s1_ejection;",
            "engine": "[_this # 0,_this # 1,2] call rhs_fnc_engineStartupDelay",
            "killed": "[_this # 0,'rhs_Wreck_2s1_turret_F',50] call rhs_fnc_turretBlow"
        },
        # Class: CfgVehicles|rhs_2s1tank_base|EventHandlers|BIS_Randomisation [Indent level: 2],
        "bis_randomisation": {
            "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;}"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    # Class: CfgVehicles|rhs_2s1tank_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhs_2s1tank_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhs_2s1tank_base|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_2s1tank_base|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 3],
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles|rhs_2s1tank_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            # Class: CfgVehicles|rhs_2s1tank_base|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_2s1tank_base|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 3],
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles|Tank_F|Components|AITankSteeringComponent [Indent level: 2],
        "aitanksteeringcomponent": {
            "steeringpidweights": [2.9,0.1,0.2],
            "speedpidweights": [0.7,0.2,0],
            "doremapspeed": 0,
            "remapspeedrange": [30,70],
            "remapspeedscalar": [1,0.35],
            "dopredictforward": 1,
            "predictforwardrange": [1,20],
            "steeraheadsaturation": [0.01,0.4],
            "speedpredictionmethod": 3,
            "wheelanglecoef": 0.7,
            "forwardanglecoef": 0.7,
            "steeringanglecoef": 1,
            "differenceanglecoef": 1,
            "stuckmaxtime": 3,
            "allowovertaking": 1,
            "allowcollisionavoidance": 1,
            "allowdrifting": 0,
            "maxwheelanglediff": 0.2616,
            "minspeedtokeep": 0.01,
            "commandturnfactor": 2,
            "allowturnaroundinpoint": 1,
            "convoypidweights": [1,0,0],
            "predictforwardmaxspeed": 15
        },
        # Class: CfgVehicles|LandVehicle|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    "_generalmacro": "Tank_F",
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "sensorposition": "gunnerView",
    "audible": 18,
    "sensitivityear": "0.0075 /3",
    "turncoef": 5,
    "steeraheadsimul": 0.3,
    "steeraheadplan": 0.4,
    "brakedistance": 5,
    "precision": 10,
    "hideproxyincombat": 1,
    "radartarget": 1,
    "radartargetsize": 1.2,
    "visualtarget": 1,
    "visualtargetsize": 1,
    "irtargetsize": 1.2,
    "irscanground": 2,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "enableradio": 1,
    "lockdetectionsystem": 0,
    "countermeasureactivationradius": 2000,
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_3",0.316228,1],
    "memorypointcargolight": "cargo light",
    "dampersbumpcoef": 4.5,
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.9995,
    "secondaryexplosion": -1,
    "fuelexplosionpower": 1,
    "weapons": [],
    "magazines": [],
    "transportmaxweapons": 12,
    "transportmaxmagazines": 128,
    "transportmaxbackpacks": 12,
    "maximumload": 3000,
    "supplyradius": -1,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Tank_F|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
    # Class: CfgVehicles|Tank_F|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|Tank_F|CamShake [Indent level: 1],
    "camshake": {
        "power": 5,
        "frequency": 20,
        "distance": 20,
        "minspeed": 5
    },
    "camshakecoef": 0,
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 0.05,
    "viewcargoshadowamb": 0.5,
    # Class: CfgVehicles|Tank_F|NVGMarkers [Indent level: 1],
    "nvgmarkers": {
        # Class: CfgVehicles|Tank_F|NVGMarkers|NVGMarker01 [Indent level: 2]
        "nvgmarker01": {
            "name": "nvg_marker",
            "color": [0.03,0.003,0.003,1],
            "ambient": [0.003,0.0003,0.0003,1],
            "brightness": 0.001,
            "blinking": 1
        }
    },
    "memorypointdriveroptics": "driverview",
    "enginestartspeed": 5,
    "explosioneffect": "FuelExplosionBig",
    "htmin": 60,
    "htmax": 1800,
    "afmax": 100,
    "mfmax": 80,
    "mfact": 1,
    "tbody": 250,
    "numberphysicalwheels": 16,
    "getinradius": 3.5,
    "hulldamagecauseexplosion": 1,
    "selectionfireanim": "zasleh",
    "bounding": "usti hlavne",
    "firedusteffect": "FDustEffects",
    "gearbox": [-7,0,11,8,5.7,4.2],
    "alphatracks": 0.7,
    "texturetrackwheel": 0,
    "memorypointtrack1l": "Stopa LL",
    "memorypointtrack1r": "Stopa LR",
    "memorypointtrack2l": "Stopa RL",
    "memorypointtrack2r": "Stopa RR",
    # Class: CfgVehicles|Tank|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": 7,
        "initangley": 0,
        "initfov": 0.75,
        "minfov": 0.25,
        "maxfov": 1.25,
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
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "predictturnsimul": 1.2,
    "predictturnplan": 1,
    "soundgear": ["",0.000316228,1],
    "outsidesoundfilter": 1,
    "nightvision": 0,
    "formationx": 20,
    "formationz": 30,
    "type": 1,
    "threat": [0.7,1,0.3],
    "camouflage": 8,
    # Class: CfgVehicles|Tank|CargoLight [Indent level: 1],
    "cargolight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
    "enablegps": 1,
    "mapsize": 1.21,
    # Class: CfgVehicles|Tank|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Tank|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_vehicle_tank_s"],
            "speechplural": ["veh_vehicle_tank_p"]
        }
    },
    "textsingular": "tank",
    "textplural": "tanks",
    "namesound": "veh_vehicle_tank_s",
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffectsBig"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffectsBig"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffectsBig"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffectsBig"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffectsBig"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffectsBig"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassEffectsDryBig"],["GdtStratisDryGrass","RDirtEffectsBig"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffectsBig"],["GdtStratisGreenGrass","RDirtEffectsBig"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffectsBig"],["GdtStratisRocky","RDirtEffectsBig"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffectsBig"],["GdtStratisThistles","RDirtEffectsBig"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffectsBig"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffectsBig"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffectsBig"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffectsBig"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffectsBig"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffectsBig"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffectsBig"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RDirtEffectsBig"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RDirtEffectsBig"],["GdtDesert1","RStonesEffectsBig"],["GdtDesert2","RDustEffects"],["GdtDesert2","RGrassEffectsBig"],["GdtDesert2","RDirtEffectsBig"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffectsBig"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffectsBig"],["GdtGrassGreen","RDirtEffectsBig"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassEffectsDryBig"],["GdtGrassDry","RDirtEffectsBig"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffectsBig"],["GdtGrassWild","RDirtEffectsBig"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffectsBig"],["GdtWildField","RDirtEffectsBig"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffectsBig"],["GdtWeed1","RDirtEffectsBig"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffectsBig"],["GdtWeed2","RDirtEffectsBig"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffectsBig"],["GdtThorn","RDirtEffectsBig"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffectsBig"],["GdtStony","RDirtEffectsBig"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffectsBig"],["GdtStonyGreen","RDirtEffectsBig"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffectsBig"],["GdtStonyThistle","RDirtEffectsBig"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffectsBig"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffectsBig"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffectsBig"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffectsBig"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffectsBig"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffectsBig"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassEffectsDryBig"],["GdtStratisDryGrass","LDirtEffectsBig"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffectsBig"],["GdtStratisGreenGrass","LDirtEffectsBig"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffectsBig"],["GdtStratisRocky","LDirtEffectsBig"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffectsBig"],["GdtStratisThistles","LDirtEffectsBig"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffectsBig"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffectsBig"],["GdtRubble","LDustEffects"],["GdtRubble","LDirtEffectsBig"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffectsBig"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffectsBig"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffectsBig"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffectsBig"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LDirtEffectsBig"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LDirtEffectsBig"],["GdtDesert1","LStonesEffectsBig"],["GdtDesert2","LDustEffects"],["GdtDesert2","LGrassEffectsBig"],["GdtDesert2","LDirtEffectsBig"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffectsBig"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffectsBig"],["GdtGrassGreen","LDirtEffectsBig"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassEffectsDryBig"],["GdtGrassDry","LDirtEffectsBig"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffectsBig"],["GdtGrassWild","LDirtEffectsBig"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffectsBig"],["GdtWildField","LDirtEffectsBig"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffectsBig"],["GdtWeed1","LDirtEffectsBig"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffectsBig"],["GdtWeed2","LDirtEffectsBig"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffectsBig"],["GdtThorn","LDirtEffectsBig"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffectsBig"],["GdtStony","LDirtEffectsBig"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffectsBig"],["GdtStonyGreen","LDirtEffectsBig"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffectsBig"],["GdtStonyThistle","LDirtEffectsBig"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","RDustEffects"]],
    # Class: CfgVehicles|Tank|DustEffects [Indent level: 1],
    "dusteffects": {
        # Class: CfgDustEffectsTank|Both [Indent level: 0]
        "both": {
        },
        # Class: CfgDustEffectsTank|Left [Indent level: 0],
        "left": {
            "default": ["LDustEffects"],
            "gdtstratisconcrete": ["LDustEffects","LDirtEffectsBig"],
            "gdtstratisbeach": ["LDustEffects","LStonesEffectsBig"],
            "gdtstratisdirt": ["LDustEffects","LDirtEffectsBig"],
            "gdtstratisseabedcluttered": ["LDustEffects"],
            "gdtstratisseabed": ["LDustEffects"],
            "gdtstratisdrygrass": ["LDustEffects","LGrassEffectsDryBig","LDirtEffectsBig"],
            "gdtstratisgreengrass": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtstratisrocky": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtstratisthistles": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtconcrete": ["LDustEffects","LDirtEffectsBig"],
            "gdtasphalt": ["LDustEffects","LDirtEffectsBig"],
            "gdtrubble": ["LDustEffects","LDirtEffectsBig"],
            "gdtsoil": ["LDustEffects","LDirtEffectsBig"],
            "gdtbeach": ["LDustEffects","LStonesEffectsBig"],
            "gdtrock": ["LDustEffects","LDirtEffectsBig"],
            "gdtdead": ["LDustEffects","LDirtEffectsBig"],
            "gdtdesert": ["LDustEffects","LDirtEffectsBig","LStonesEffects"],
            "gdtdesert1": ["LDustEffects","LDirtEffectsBig","LStonesEffectsBig"],
            "gdtdesert2": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtdirt": ["LDustEffects","LDirtEffectsBig"],
            "gdtgrassgreen": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtgrassdry": ["LDustEffects","LGrassEffectsDryBig","LDirtEffectsBig"],
            "gdtgrasswild": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtwildfield": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtweed1": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtweed2": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtthorn": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtstony": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtstonygreen": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtstonythistle": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
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
            "gdtgrassshort": ["LDustEffects","LGrassEffectsBig"],
            "gdtgrasstall": ["LDustEffects","LGrassEffectsBig"],
            "gdtreddirt": ["LDustEffectsRed"],
            "gdtfield": ["LDustEffects"],
            "gdtforest": ["LDustEffects"],
            "gdtvolcano": ["LDustEffects","LStonesEffectsBig"],
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
        # Class: CfgDustEffectsTank|Right [Indent level: 0],
        "right": {
            "default": ["RDustEffects"],
            "gdtstratisconcrete": ["RDustEffects","RDirtEffectsBig"],
            "gdtstratisbeach": ["RDustEffects","RStonesEffectsBig"],
            "gdtstratisdirt": ["RDustEffects","RDirtEffectsBig"],
            "gdtstratisseabedcluttered": ["RDustEffects"],
            "gdtstratisseabed": ["RDustEffects"],
            "gdtstratisdrygrass": ["RDustEffects","RGrassEffectsDryBig","RDirtEffectsBig"],
            "gdtstratisgreengrass": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtstratisrocky": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtstratisthistles": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtconcrete": ["RDustEffects","RDirtEffectsBig"],
            "gdtasphalt": ["RDustEffects","RDirtEffectsBig"],
            "gdtrubble": ["RDustEffects","RDirtEffectsBig"],
            "gdtsoil": ["RDustEffects","RDirtEffectsBig"],
            "gdtbeach": ["RDustEffects","RStonesEffectsBig"],
            "gdtrock": ["RDustEffects","RDirtEffectsBig"],
            "gdtdead": ["RDustEffects","RDirtEffectsBig"],
            "gdtdesert": ["RDustEffects","RDirtEffectsBig","RStonesEffects"],
            "gdtdesert1": ["RDustEffects","RDirtEffectsBig","RStonesEffectsBig"],
            "gdtdesert2": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtdirt": ["RDustEffects","RDirtEffectsBig"],
            "gdtgrassgreen": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtgrassdry": ["RDustEffects","RGrassEffectsDryBig","RDirtEffectsBig"],
            "gdtgrasswild": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtwildfield": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtweed1": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtweed2": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtthorn": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtstony": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtstonygreen": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtstonythistle": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
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
            "gdtgrassshort": ["RDustEffects","RGrassEffectsBig"],
            "gdtgrasstall": ["RDustEffects","RGrassEffectsBig"],
            "gdtreddirt": ["RDustEffectsRed"],
            "gdtfield": ["RDustEffects"],
            "gdtforest": ["RDustEffects"],
            "gdtvolcano": ["RDustEffects","RStonesEffectsBig"],
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
    # Class: CfgVehicles|Tank|DestructionEffects [Indent level: 1],
    "destructioneffects": {
        # Class: CfgVehicles|Tank|DestructionEffects|LightBig1 [Indent level: 2]
        "lightbig1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 0.001,
            "interval": 1,
            "lifetime": 3,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles|Tank|DestructionEffects|Sound [Indent level: 2],
        "sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifetime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles|Tank|DestructionEffects|FireBig1 [Indent level: 2],
        "firebig1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Tank|DestructionEffects|Refract1 [Indent level: 2],
        "refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefract",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SmokeBig1 [Indent level: 2],
        "smokebig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SparksBig1 [Indent level: 2],
        "sparksbig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifetime": 0
        },
        # Class: CfgVehicles|Tank|DestructionEffects|FireSparksBig1 [Indent level: 2],
        "firesparksbig1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifetime": 2.8
        },
        # Class: CfgVehicles|Tank|DestructionEffects|FireBig2 [Indent level: 2],
        "firebig2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SmokeBig1_2 [Indent level: 2],
        "smokebig1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SmokeBig2 [Indent level: 2],
        "smokebig2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifetime": 3.2
        }
    },
    "headgforceleaningfactor": [0.0075,0.005,0.0075],
    "selectionbrakelights": "brzdove svetlo",
    "memorypointmissile": ["spice rakety","usti hlavne"],
    "memorypointmissiledir": ["konec rakety","konec hlavne"],
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "leftwatereffect": "LWaterEffects",
    "rightwatereffect": "RWaterEffects",
    "leftfastwatereffect": "LWaterEffects",
    "rightfastwatereffect": "RWaterEffects",
    "selectionleftoffset": "PasOffsetL",
    "selectionrightoffset": "PasOffsetP",
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
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + 		4",
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "squadtitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
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
    # Class: CfgVehicles|AllVehicles|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    "cargoproxyindexes": [],
    "driverlefthandanimname": "",
    "driverrighthandanimname": "",
    "driverleftleganimname": "",
    "driverrightleganimname": "",
    "cargodoors": [],
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
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
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "insidesoundcoef": 0.5,
    "obstructsoundlfratio": 0,
    "occludesoundlfratio": 0.25,
    "unloadincombat": 0,
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmin": 20,
    "antirollbarspeedmax": 60,
    "epeimpulsedamagecoef": 30,
    "gunnerhasflares": 1,
    "enablemanualfire": 1,
    "sensitivity": 2.5,
    "portrait": "",
    "ghostpreview": "",
    "armorlights": 0.4,
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
    "lasertarget": 0,
    "laserscanner": 0,
    "nvtarget": 0,
    "nvscanner": 0,
    "artillerytarget": 0,
    "canusescanners": 1,
    "preferroads": 0,
    "unitinfotypelite": 0,
    "hideunitinfo": 0,
    "radartype": 0,
    "limitedspeedcoef": 0.22,
    "hasdriver": 1,
    "hideweaponsdriver": 1,
    "hideweaponscargo": 0,
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
    "transportsoldier": 0,
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
    "soundcrashes": ["soundCrash",1],
    "soundlandcrashes": ["soundLandCrash",1],
    "soundwatercrashes": ["soundWaterCrash",1],
    "emptysound": ["",0,1],
    "soundbushcrash": ["emptySound",0],
    "soundlocked": ["",1,1],
    "cargoaction": [],
    "cargoiscodriver": [0],
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
    "ejectdeaddriver": 0,
    "ejectdeadcargo": 0,
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
    "fireresistance": 10,
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
    # Class: CfgVehicles|All|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minspeed": 1,
        "duration": 3
    },
    "mingforce": 0.2,
    "maxgforce": 2,
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