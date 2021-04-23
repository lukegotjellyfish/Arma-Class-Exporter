rhsgref_cdf_t80bv_tv = {
    "editorpreview": "rhsgref|addons|rhsgref_editorPreviews|data|rhsgref_cdf_t80bv_tv.paa",
    "crew": "rhsgref_cdf_reg_crew",
    "author": "RHS (A2 port)",
    "side": 2,
    "dlc": "RHS_GREF",
    "faction": "rhsgref_faction_cdf_ground",
    "rhs_decalparameters": ["['Number',cRHST80NumberPlaces,'CDF']","['Label',cRHST80PlnSymPlaces, 'Platoon',8]"],
    "scope": 2,
    "hiddenselectionstextures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_t80_hull_cdf_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_t80_turret_cdf_co.paa","","rhsafrf|addons|rhs_t80|data|searchlightopen_co.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa"],
    # Class: CfgVehicles|rhsgref_cdf_t80bv_tv|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhsgref_cdf_t80bv_tv|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "magazines": ["rhs_mag_3bm22_10","rhs_mag_3bk18m_8","rhs_mag_3of26_6","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_9m112m_4","rhs_mag_3d17","rhs_laserfcsmag","rhs_laserfcsmag"],
            # Class: CfgVehicles|rhsgref_cdf_t80bv_tv|Turrets|MainTurret|Turrets [Indent level: 3],
            "turrets": {
                # Class: CfgVehicles|rhsgref_cdf_t80bv_tv|Turrets|MainTurret|Turrets|CommanderOptics [Indent level: 4]
                "commanderoptics": {
                    "gunnertype": "rhsgref_cdf_reg_crew_commander",
                    "weapons": [],
                    "magazines": [],
                    "outgunnermayfire": 1,
                    "ingunnermayfire": 1,
                    "gunbeg": "Mgun_end",
                    "gunend": "Mgun_start",
                    "body": "RHS_T80B_com_coppula",
                    "gun": "RHS_T80B_com_Gun",
                    "gunneraction": "rhs_t80_commander_out",
                    "gunnerinaction": "rhs_T80_Commander_in",
                    "viewgunnerinexternal": 1,
                    "gunnergetinaction": "GetInMedium",
                    "gunnergetoutaction": "GetOutMedium",
                    "gunnerdoor": "hatchC",
                    "ejectdeadgunner": 0,
                    "minelev": -15,
                    "maxelev": 80,
                    "initelev": 0,
                    "minturn": -360,
                    "maxturn": 360,
                    "initturn": 0,
                    "lockwhendriverout": 0,
                    "lodturnedout": 1200,
                    "gunneroutforceoptics": 0,
                    "animationsourcehatch": "HatchCommander",
                    "animationsourcebody": "obsTurret",
                    "animationsourcegun": "obsGun",
                    "memorypointgunneroptics": "commanderview",
                    "memorypointgunneroutoptics": "commander_out_view",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                    "gunneroutopticsmodel": "",
                    "nightvision": 1,
                    "stabilizedinaxes": 3,
                    "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
                    "gunnerhasflares": 1,
                    # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
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
                    # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
                    "viewoptics": {
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "initfov": 0.101,
                        "minfov": 0.102,
                        "maxfov": 0.102,
                        "visionmode": ["Normal"],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Wide [Indent level: 6]
                        "wide": {
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                            "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                            "initfov": 0.14,
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "minfov": 0.102,
                            "maxfov": 0.102,
                            "visionmode": ["Normal"],
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0,
                            "speedzoommaxspeed": 1e+010,
                            "speedzoommaxfov": 0
                        },
                        # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Night [Indent level: 6],
                        "night": {
                            "initfov": 0.166667,
                            "visionmode": ["NVG"],
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3_night.p3d",
                            "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "minfov": 0.102,
                            "maxfov": 0.102,
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0,
                            "speedzoommaxspeed": 1e+010,
                            "speedzoommaxfov": 0
                        },
                        # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Periscope [Indent level: 6],
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
                    "startengine": 0,
                    "selectionfireanim": "",
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
                    "lodopticsout": 1200,
                    "canusescanners": 0,
                    "allowtablock": 0,
                    "turretinfotype": "RHS_RscWeaponTKN3_FCS",
                    # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        },
                        # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        }
                    },
                    # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitTurretCom [Indent level: 6]
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
                        # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitGunCom [Indent level: 6],
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
                    "proxytype": "CPCommander",
                    "proxyindex": 1,
                    "gunnername": "Commander",
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "animationsourcecamelev": "camElev",
                    "soundservo": ["A3|sounds_f|dummysound",0.01,1,10],
                    "commanding": 2,
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointgun": "gun_muzzle",
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
                    "hideweaponsgunner": 1,
                    "canhidegunner": -1,
                    "forcehidegunner": 0,
                    "showhmd": 0,
                    "lockwhenvehiclespeed": -1,
                    "gunnercompartments": "Compartment1",
                    "lodturnedin": -1,
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
                # Class: CfgVehicles|rhsgref_cdf_t80bv_tv|Turrets|MainTurret|Turrets|CommanderMG [Indent level: 4],
                "commandermg": {
                    "gunnername": "Commander HMG",
                    "proxyindex": 2,
                    "dontcreateai": 1,
                    "cantcreateai": 1,
                    "body": "mg_turret",
                    "gun": "mg_gun",
                    "animationsourcebody": "mg_turret",
                    "animationsourcegun": "mg_gun",
                    "gunnerdoor": "",
                    "turretinfotype": "RHS_RscWeaponZeroing",
                    "discretedistance": [100,200,300,400,500,600,800,900,1000,1100,1200,1400,1500,1800,1900,2000],
                    "discretedistanceinitindex": 2,
                    "stabilizedinaxes": 0,
                    "canhidegunner": 0,
                    "viewgunnershadow": 0,
                    "lodturnedout": 1200,
                    "memorypointgunneroutoptics": "commander_out_view",
                    "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                    "disablesoundattenuation": 1,
                    "gunnerlefthandanimname": "",
                    "gunnerrighthandanimname": "mg_handle2",
                    "maxverticalrotspeed": 0.35,
                    "minelev": -5,
                    "maxelev": 45,
                    "initelev": 0,
                    "initturn": 0,
                    "weapons": ["rhs_weap_nsvt_t80"],
                    "magazines": ["rhs_mag_127x108mm_50","rhs_mag_127x108mm_50","rhs_mag_127x108mm_50"],
                    "selectionfireanim": "zasleh3",
                    # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderMG|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderMG|OpticsIn|Wide [Indent level: 6]
                        "wide": {
                            "visionmode": ["Normal"],
                            "initfov": 0.583333,
                            "minfov": 0.583333,
                            "maxfov": 0.583333,
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                            "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
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
                        # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Night [Indent level: 6],
                        "night": {
                            "initfov": 0.166667,
                            "visionmode": ["NVG"],
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3_night.p3d",
                            "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "minfov": 0.102,
                            "maxfov": 0.102,
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0,
                            "speedzoommaxspeed": 1e+010,
                            "speedzoommaxfov": 0
                        },
                        # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Periscope [Indent level: 6],
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
                    "gunnercompartments": "Compartment5",
                    "outgunnermayfire": 1,
                    "ingunnermayfire": 1,
                    "gunbeg": "Mgun_end",
                    "gunend": "Mgun_start",
                    "gunneraction": "rhs_t80_commander_out",
                    "gunnerinaction": "rhs_T80_Commander_in",
                    "gunnertype": "rhs_msv_crew_commander",
                    "viewgunnerinexternal": 1,
                    "gunnergetinaction": "GetInMedium",
                    "gunnergetoutaction": "GetOutMedium",
                    "ejectdeadgunner": 0,
                    "minturn": -360,
                    "maxturn": 360,
                    "lockwhendriverout": 0,
                    "gunneroutforceoptics": 0,
                    "animationsourcehatch": "HatchCommander",
                    "memorypointgunneroptics": "commanderview",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                    "nightvision": 1,
                    "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
                    "gunnerhasflares": 1,
                    # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
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
                    # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
                    "viewoptics": {
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "initfov": 0.101,
                        "minfov": 0.102,
                        "maxfov": 0.102,
                        "visionmode": ["Normal"],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    "startengine": 0,
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
                    "lodopticsout": 1200,
                    "canusescanners": 0,
                    "allowtablock": 0,
                    # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        },
                        # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        }
                    },
                    # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitTurretCom [Indent level: 6]
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
                        # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitGunCom [Indent level: 6],
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
                    "proxytype": "CPCommander",
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "animationsourcecamelev": "camElev",
                    "soundservo": ["A3|sounds_f|dummysound",0.01,1,10],
                    "commanding": 2,
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointgun": "gun_muzzle",
                    "soundelevation": ["",0.00316228,1],
                    "minoutelev": -4,
                    "maxoutelev": 20,
                    "initoutelev": 0,
                    "minoutturn": -60,
                    "maxoutturn": 60,
                    "initoutturn": 0,
                    "maxhorizontalrotspeed": 1.2,
                    "mincamelev": -90,
                    "maxcamelev": 90,
                    "initcamelev": 0,
                    "primary": 1,
                    "hasgunner": 1,
                    "turretcansee": 0,
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
                    "viewgunnershadowdiff": 1,
                    "viewgunnershadowamb": 1,
                    "hideweaponsgunner": 1,
                    "forcehidegunner": 0,
                    "showhmd": 0,
                    "lockwhenvehiclespeed": -1,
                    "lodturnedin": -1,
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
                    "gunnerleftleganimname": "",
                    "gunnerrightleganimname": "",
                    "precisegetinout": 0,
                    "turretfollowfreelook": 0,
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
                    "showcrewaim": 0
                }
            },
            # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Reflectors [Indent level: 3],
            "reflectors": {
                # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Reflectors|Searchlight_FG125 [Indent level: 4]
                "searchlight_fg125": {
                    "color": [1900,1300,950],
                    "ambient": [5,5,5],
                    "position": "Light_FG125",
                    "direction": "Light_FG125_end",
                    "hitpoint": "Light_FG125",
                    "selection": "Light_FG125",
                    "size": 1,
                    "innerangle": 8,
                    "outerangle": 15,
                    "conefadecoef": 1,
                    "intensity": 45,
                    "useflare": 1,
                    "daylight": 1,
                    "flaresize": 0.85,
                    # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Reflectors|Searchlight_FG125|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 1,
                        "constant": 0,
                        "linear": 0,
                        "quadratic": 0.02,
                        "hardlimitstart": 630,
                        "hardlimitend": 660
                    }
                },
                # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Reflectors|Searchlight_FG125_Flare [Indent level: 4],
                "searchlight_fg125_flare": {
                    "color": [7,6,6.5],
                    "ambient": [22,22,22],
                    "position": "Light_FG125",
                    "direction": "Light_FG125_end",
                    "hitpoint": "Light_FG125",
                    "selection": "Light_FG125",
                    "size": 1,
                    "innerangle": 30,
                    "outerangle": 175,
                    "conefadecoef": 10,
                    "intensity": 100,
                    "useflare": 1,
                    "daylight": 0,
                    "flaresize": 1.85,
                    # Class: CfgVehicles|rhs_t80bv|Turrets|MainTurret|Reflectors|Searchlight_FG125_Flare|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 0,
                        "quadratic": 10,
                        "hardlimitstart": 0,
                        "hardlimitend": 0.9
                    }
                }
            },
            "armorlights": 0.1,
            "initturn": -13,
            "gunneraction": "rhs_t80_gunner_out",
            "gunnerinaction": "rhs_t80_gunner_in",
            "viewgunnerinexternal": 1,
            "gunnergetinaction": "GetInMedium",
            "gunnergetoutaction": "GetOutMedium",
            "gunnerdoor": "hatchG",
            "ejectdeadgunner": 0,
            "startengine": 0,
            "soundservo": ["rhsafrf|addons|rhs_t80|Sound|servo.ogg",6,1,20],
            "armorstructural": 60,
            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": -100,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passthrough": 0,
                    "minimalhit": 0.01,
                    "explosionshielding": 0.009,
                    "radius": 0.15
                },
                # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": -150,
                    "material": -1,
                    "name": "zbran",
                    "visual": "-",
                    "passthrough": 0,
                    "minimalhit": -0.2,
                    "explosionshielding": 0.001,
                    "radius": 0.12
                }
            },
            "weapons": ["rhs_weap_2a46_2","rhs_weap_pkt","rhs_weap_902a","rhs_weap_fcs"],
            "memorypointgun": "Mgun",
            "selectionfireanim": "zasleh1",
            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_1g42.p3d",
            "gunneroutopticsmodel": "",
            "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
            "nightvision": 1,
            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|OpticsIn|day1 [Indent level: 4]
                "day1": {
                    "opticsdisplayname": "DAY",
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "initfov": 0.179487,
                    "minfov": 0.179487,
                    "maxfov": 0.179487,
                    "visionmode": ["Normal"],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_1g42.p3d",
                    "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|OpticsIn|day2 [Indent level: 4],
                "day2": {
                    "opticsdisplayname": "DAYZOOM",
                    "initfov": 0.0777778,
                    "minfov": 0.0777778,
                    "maxfov": 0.0777778,
                    "visionmode": ["Normal"],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_1g42.p3d",
                    "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
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
                # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|OpticsIn|Periscope [Indent level: 4],
                "periscope": {
                    "opticsdisplayname": "PERISCOPE",
                    "initfov": 0.466667,
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
                    "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "minfov": 0.179487,
                    "maxfov": 0.179487,
                    "visionmode": ["Normal"],
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|OpticsIn|night3 [Indent level: 4],
                "night3": {
                    "opticsdisplayname": "NIGHT",
                    "initfov": 0.1,
                    "minfov": 0.1,
                    "maxfov": 0.1,
                    "visionmode": ["NVG"],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_empty",
                    "gunneropticseffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
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
            "minelev": -4,
            "maxelev": 18,
            "minturn": -360,
            "maxturn": 360,
            "initelev": 5,
            "lockwhendriverout": 1,
            "maxhorizontalrotspeed": 0.4,
            "maxverticalrotspeed": 0.07,
            "radartype": 0,
            "turretinfotype": "rhs_gui_optic_t80_rangefinder",
            "discretedistance": [100],
            "discretedistanceinitindex": 0,
            "canusescanners": 0,
            "allowtablock": 0,
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "body": "RHS_T80B_MainTurret",
            "gun": "RHS_T80B_MainGun",
            "stabilizedinaxes": 3,
            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|ViewGunner [Indent level: 3],
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
            # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                },
                # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_tank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                }
            },
            "commanding": 1,
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "primarygunner": 1,
            "gunneroutopticseffect": [],
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
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "turretspec": {
                "showheadphones": 0
            },
            "gunneropticscolor": [0,0,0,1],
            "gunnerforceoptics": 1,
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
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "outgunnermayfire": 0,
            "ingunnermayfire": 1,
            "showhmd": 0,
            "lockwhenvehiclespeed": -1,
            "gunnercompartments": "Compartment1",
            "lodturnedin": -1,
            "lodturnedout": -1,
            "memorypointsgetingunnerprecise": "",
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
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
            "memorypointgunneroptics": "gunnerview",
            "showcrewaim": 0
        }
    },
    # Class: CfgVehicles|rhsgref_cdf_t80bv_tv|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|rhsgref_cdf_t80bv_tv|TransportMagazines|_xx_rhsusf_mag_17Rnd_9x19_FMJ [Indent level: 2]
        "_xx_rhsusf_mag_17rnd_9x19_fmj": {
            "magazine": "rhsusf_mag_17Rnd_9x19_FMJ",
            "count": 10
        },
        # Class: CfgVehicles|rhsgref_cdf_t80bv_tv|TransportMagazines|_xx_rhs_mag_rgd5 [Indent level: 2],
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 10
        },
        # Class: CfgVehicles|rhsgref_cdf_t80bv_tv|TransportMagazines|_xx_rhs_mag_nspn_red [Indent level: 2],
        "_xx_rhs_mag_nspn_red": {
            "magazine": "rhs_mag_nspn_red",
            "count": 10
        }
    },
    "model": "rhsafrf|addons|rhs_t80|T80BV.p3d",
    "displayname": "T-80BV",
    "armor": 550,
    "smokelaunchergrenadecount": 6,
    "smokelaunchervelocity": 14,
    "smokelauncheronturret": 1,
    "smokelauncherangle": 60,
    # Class: CfgVehicles|rhs_t80bv|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|smokecap_revolving_source [Indent level: 2]
        "smokecap_revolving_source": {
            "source": "revolving",
            "weapon": "rhs_weap_902a"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_1_source [Indent level: 2],
        "era_1_source": {
            "source": "Hit",
            "hitpoint": "era_1_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_2_source [Indent level: 2],
        "era_2_source": {
            "source": "Hit",
            "hitpoint": "era_2_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_3_source [Indent level: 2],
        "era_3_source": {
            "source": "Hit",
            "hitpoint": "era_3_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_4_source [Indent level: 2],
        "era_4_source": {
            "source": "Hit",
            "hitpoint": "era_4_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_5_source [Indent level: 2],
        "era_5_source": {
            "source": "Hit",
            "hitpoint": "era_5_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_6_source [Indent level: 2],
        "era_6_source": {
            "source": "Hit",
            "hitpoint": "era_6_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_7_source [Indent level: 2],
        "era_7_source": {
            "source": "Hit",
            "hitpoint": "era_7_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_8_source [Indent level: 2],
        "era_8_source": {
            "source": "Hit",
            "hitpoint": "era_8_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_9_source [Indent level: 2],
        "era_9_source": {
            "source": "Hit",
            "hitpoint": "era_9_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_10_source [Indent level: 2],
        "era_10_source": {
            "source": "Hit",
            "hitpoint": "era_10_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_11_source [Indent level: 2],
        "era_11_source": {
            "source": "Hit",
            "hitpoint": "era_11_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_12_source [Indent level: 2],
        "era_12_source": {
            "source": "Hit",
            "hitpoint": "era_12_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_13_source [Indent level: 2],
        "era_13_source": {
            "source": "Hit",
            "hitpoint": "era_13_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_14_source [Indent level: 2],
        "era_14_source": {
            "source": "Hit",
            "hitpoint": "era_14_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_15_source [Indent level: 2],
        "era_15_source": {
            "source": "Hit",
            "hitpoint": "era_15_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_16_source [Indent level: 2],
        "era_16_source": {
            "source": "Hit",
            "hitpoint": "era_16_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_17_source [Indent level: 2],
        "era_17_source": {
            "source": "Hit",
            "hitpoint": "era_17_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_18_source [Indent level: 2],
        "era_18_source": {
            "source": "Hit",
            "hitpoint": "era_18_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_19_source [Indent level: 2],
        "era_19_source": {
            "source": "Hit",
            "hitpoint": "era_19_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_20_source [Indent level: 2],
        "era_20_source": {
            "source": "Hit",
            "hitpoint": "era_20_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_21_source [Indent level: 2],
        "era_21_source": {
            "source": "Hit",
            "hitpoint": "era_21_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_22_source [Indent level: 2],
        "era_22_source": {
            "source": "Hit",
            "hitpoint": "era_22_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_23_source [Indent level: 2],
        "era_23_source": {
            "source": "Hit",
            "hitpoint": "era_23_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_24_source [Indent level: 2],
        "era_24_source": {
            "source": "Hit",
            "hitpoint": "era_24_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_25_source [Indent level: 2],
        "era_25_source": {
            "source": "Hit",
            "hitpoint": "era_25_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_26_source [Indent level: 2],
        "era_26_source": {
            "source": "Hit",
            "hitpoint": "era_26_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_27_source [Indent level: 2],
        "era_27_source": {
            "source": "Hit",
            "hitpoint": "era_27_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80bv|AnimationSources|era_28_source [Indent level: 2],
        "era_28_source": {
            "source": "Hit",
            "hitpoint": "era_28_hitpoint"
        },
        # Class: CfgVehicles|rhs_t80b|AnimationSources|kshield_unhide [Indent level: 2],
        "kshield_unhide": {
            "initphase": 1,
            "source": "user",
            "animperiod": 1e-010,
            "mass": -20,
            "displayname": "hide commander shield",
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles|rhs_t80b|AnimationSources|kdeck_unhide [Indent level: 2],
        "kdeck_unhide": {
            "initphase": 1,
            "displayname": "hide commander deck",
            "author": "Red Hammer Studios",
            "source": "user",
            "animperiod": 1e-010,
            "mass": -20
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|sideskirt_unhide [Indent level: 2],
        "sideskirt_unhide": {
            "displayname": "hide side skirt",
            "mass": -220,
            "source": "user",
            "animperiod": 1e-010,
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|fbskirt_unhide [Indent level: 2],
        "fbskirt_unhide": {
            "displayname": "hide front bottom rubber skirt",
            "mass": -100,
            "source": "user",
            "animperiod": 1e-010,
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|ftskirt_unhide [Indent level: 2],
        "ftskirt_unhide": {
            "displayname": "hide front top rubber skirt",
            "mass": -50,
            "source": "user",
            "animperiod": 1e-010,
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|log_unhide [Indent level: 2],
        "log_unhide": {
            "displayname": "hide back log",
            "mass": -100,
            "source": "user",
            "animperiod": 1e-010,
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|snorkel_unhide [Indent level: 2],
        "snorkel_unhide": {
            "displayname": "mount snorkel",
            "mass": 1,
            "onphasechanged": "if(_this select 1 == 0)then{_this select 0 animate ['snorkel_unhide2',0];_this select 0 animate ['snorkel_unhide2',0];_this select 0 animate ['snorkel_hide',1];}else{_this select 0 animate ['snorkel_unhide2',1];_this select 0 animate ['snorkel_unhide2',1];_this select 0 animate ['snorkel_hide',0];}",
            "source": "user",
            "animperiod": 1e-010,
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|snorkel_unhide2 [Indent level: 2],
        "snorkel_unhide2": {
            "source": "user",
            "initphase": 0,
            "animperiod": 1e-010
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|snorkel_hide [Indent level: 2],
        "snorkel_hide": {
            "initphase": 1,
            "source": "user",
            "animperiod": 1e-010
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|TCOverrideTurret [Indent level: 2],
        "tcoverrideturret": {
            "source": "user",
            "animperiod": 4,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|recoil_source [Indent level: 2],
        "recoil_source": {
            "source": "door",
            "animperiod": 6,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|reload_source [Indent level: 2],
        "reload_source": {
            "weapon": "rhs_weap_2a46_2",
            "source": "reload"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|reload_magazine_source [Indent level: 2],
        "reload_magazine_source": {
            "source": "reloadMagazine",
            "weapon": "rhs_weap_2a46_2"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|muzzle_rot_cannon [Indent level: 2],
        "muzzle_rot_cannon": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a46_2"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "weapon": "rhs_weap_nsvt_t80",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|muzzle_rot_coax [Indent level: 2],
        "muzzle_rot_coax": {
            "weapon": "rhs_weap_pkt",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|ReloadAnim [Indent level: 2],
        "reloadanim": {
            "source": "reload",
            "weapon": "rhs_weap_nsvt_t80"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|ReloadMagazine [Indent level: 2],
        "reloadmagazine": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_nsvt_t80"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|Revolving [Indent level: 2],
        "revolving": {
            "source": "revolving",
            "weapon": "rhs_weap_nsvt_t80"
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|autoloader [Indent level: 2],
        "autoloader": {
            "source": "user",
            "animperiod": 3.25,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|elev [Indent level: 2],
        "elev": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|elev_bank [Indent level: 2],
        "elev_bank": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|lead [Indent level: 2],
        "lead": {
            "source": "user",
            "animperiod": 0.001
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|offset [Indent level: 2],
        "offset": {
            "source": "user",
            "animperiod": 0.0002
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|HatchC [Indent level: 2],
        "hatchc": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|HatchG [Indent level: 2],
        "hatchg": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|HatchD [Indent level: 2],
        "hatchd": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_tank_base|AnimationSources|turretHide [Indent level: 2],
        "turrethide": {
            "animperiod": 1e-010,
            "source": "user",
            "initphase": 0
        }
    },
    # Class: CfgVehicles|rhs_t80bv|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_1_hitpoint [Indent level: 2]
        "era_1_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e1",
            "armorcomponent": "e1",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_1_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_2_hitpoint [Indent level: 2],
        "era_2_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e2",
            "armorcomponent": "e2",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_2_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_3_hitpoint [Indent level: 2],
        "era_3_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e3",
            "armorcomponent": "e3",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_3_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_4_hitpoint [Indent level: 2],
        "era_4_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e4",
            "armorcomponent": "e4",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_4_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_5_hitpoint [Indent level: 2],
        "era_5_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e5",
            "armorcomponent": "e5",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_5_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_6_hitpoint [Indent level: 2],
        "era_6_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e6",
            "armorcomponent": "e6",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_6_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_7_hitpoint [Indent level: 2],
        "era_7_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e7",
            "armorcomponent": "e7",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_7_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_8_hitpoint [Indent level: 2],
        "era_8_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e8",
            "armorcomponent": "e8",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_8_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e8",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e8",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e8",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e8",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_9_hitpoint [Indent level: 2],
        "era_9_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e9",
            "armorcomponent": "e9",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_9_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e9",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e9",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e9",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e9",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_10_hitpoint [Indent level: 2],
        "era_10_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e10",
            "armorcomponent": "e10",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_10_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e10",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e10",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e10",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e10",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_11_hitpoint [Indent level: 2],
        "era_11_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e11",
            "armorcomponent": "e11",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_11_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e11",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e11",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e11",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e11",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_12_hitpoint [Indent level: 2],
        "era_12_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e12",
            "armorcomponent": "e12",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_12_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e12",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e12",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e12",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e12",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_13_hitpoint [Indent level: 2],
        "era_13_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e13",
            "armorcomponent": "e13",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_13_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e13",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e13",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e13",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e13",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_14_hitpoint [Indent level: 2],
        "era_14_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e14",
            "armorcomponent": "e14",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_14_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e14",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e14",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e14",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e14",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_15_hitpoint [Indent level: 2],
        "era_15_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e15",
            "armorcomponent": "e15",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_15_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e15",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e15",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e15",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e15",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_16_hitpoint [Indent level: 2],
        "era_16_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e16",
            "armorcomponent": "e16",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_16_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e16",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e16",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e16",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e16",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_17_hitpoint [Indent level: 2],
        "era_17_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e17",
            "armorcomponent": "e17",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_17_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e17",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e17",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e17",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e17",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_18_hitpoint [Indent level: 2],
        "era_18_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e18",
            "armorcomponent": "e18",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_18_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e18",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e18",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e18",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e18",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_19_hitpoint [Indent level: 2],
        "era_19_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e19",
            "armorcomponent": "e19",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_19_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e19",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e19",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e19",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e19",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_20_hitpoint [Indent level: 2],
        "era_20_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e20",
            "armorcomponent": "e20",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_20_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e20",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e20",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e20",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e20",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_21_hitpoint [Indent level: 2],
        "era_21_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e21",
            "armorcomponent": "e21",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_21_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e21",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e21",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e21",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e21",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_22_hitpoint [Indent level: 2],
        "era_22_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e22",
            "armorcomponent": "e22",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_22_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e22",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e22",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e22",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e22",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_23_hitpoint [Indent level: 2],
        "era_23_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e23",
            "armorcomponent": "e23",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_23_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e23",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e23",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e23",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e23",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_24_hitpoint [Indent level: 2],
        "era_24_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e24",
            "armorcomponent": "e24",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_24_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e24",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e24",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e24",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e24",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_25_hitpoint [Indent level: 2],
        "era_25_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e25",
            "armorcomponent": "e25",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_25_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e25",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e25",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e25",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e25",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_26_hitpoint [Indent level: 2],
        "era_26_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e26",
            "armorcomponent": "e26",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_26_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e26",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e26",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e26",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e26",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_27_hitpoint [Indent level: 2],
        "era_27_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e27",
            "armorcomponent": "e27",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_27_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e27",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e27",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e27",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e27",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|HitPoints|era_28_hitpoint [Indent level: 2],
        "era_28_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e28",
            "armorcomponent": "e28",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|rhs_t80bv|HitPoints|era_28_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e28",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e28",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e28",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_t80bv|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e28",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|rhs_tank_base|HitPoints|Armor_Composite_65 [Indent level: 2],
        "armor_composite_65": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_65_Hit",
            "armorcomponent": "Armor_CE_65",
            "simulation": "RHS_Composite_65",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_tank_base|HitPoints|Armor_Composite_70 [Indent level: 2],
        "armor_composite_70": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_70_Hit",
            "armorcomponent": "Armor_CE_70",
            "simulation": "RHS_Composite_70",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_tank_base|HitPoints|Armor_Composite_75 [Indent level: 2],
        "armor_composite_75": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_75_Hit",
            "armorcomponent": "Armor_CE_75",
            "simulation": "RHS_Composite_75",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_tank_base|HitPoints|Armor_Composite_80 [Indent level: 2],
        "armor_composite_80": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_80_Hit",
            "armorcomponent": "Armor_CE_80",
            "simulation": "RHS_Composite_80",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_tank_base|HitPoints|Armor_Composite_85 [Indent level: 2],
        "armor_composite_85": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_85_Hit",
            "armorcomponent": "Armor_CE_85",
            "simulation": "RHS_Composite_85",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_tank_base|HitPoints|Armor_Composite_95 [Indent level: 2],
        "armor_composite_95": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_95_Hit",
            "armorcomponent": "Armor_CE_95",
            "simulation": "RHS_Composite_95",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_tank_base|HitPoints|HitHull [Indent level: 2],
        "hithull": {
            "armor": -100,
            "material": -1,
            "name": "telo",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.1,
            "explosionshielding": 0.01,
            "radius": 0.13
        },
        # Class: CfgVehicles|rhs_tank_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": -150,
            "material": -1,
            "name": "motor",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.14,
            "explosionshielding": 0.01,
            "radius": 0.23,
            # Class: CfgVehicles|rhs_tank_base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "rhs_engine_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire [Indent level: 4],
                "rhs_engine_fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks [Indent level: 4],
                "rhs_engine_sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "rhs_engine_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "rhs_engine_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
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
        # Class: CfgVehicles|rhs_tank_base|HitPoints|HitLTrack [Indent level: 2],
        "hitltrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_L",
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "visual": "pas_L"
        },
        # Class: CfgVehicles|rhs_tank_base|HitPoints|HitRTrack [Indent level: 2],
        "hitrtrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_P",
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "visual": "pas_P"
        },
        # Class: CfgVehicles|Tank_F|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 0.6,
            "material": -1,
            "name": "NEtelo",
            "visual": "motor",
            "passthrough": 0,
            "minimalhit": 0.1,
            "explosionshielding": 0.3
        }
    },
    # Class: CfgVehicles|rhs_t80bv|Library [Indent level: 1],
    "library": {
        "libtextdesc": "T-80BV, introduced in 1985. Derivation of the production T-80B with hanging dynamic armor Kontact. Weight 44.5 tonnes."
    },
    # Class: CfgVehicles|rhs_t80bv|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhs_t80bv|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cRHST80NumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "collapsed": 1,
            "displayname": "Set side number",
            "tooltip": "Set side number. 3 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHST80NumberPlaces}else{[_this, [['Number', cRHST80NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_decalArmy_type [Indent level: 2],
        "rhs_decalarmy_type": {
            "displayname": "Define army symbol type",
            "property": "rhs_decalArmy_type",
            # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalArmy_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalArmy_type|values|Army [Indent level: 4]
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalArmy_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalArmy_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalArmy_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalArmy_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalArmy_type|values|HonorGDR [Indent level: 4],
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
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_decalArmy [Indent level: 2],
        "rhs_decalarmy": {
            "displayname": "Set army symbol",
            "tooltip": "Define symbol located on gunner hatch. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalArmy",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHST80ArmSymPlaces,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_decalHonor_type [Indent level: 2],
        "rhs_decalhonor_type": {
            "displayname": "Define honor symbol type",
            "property": "rhs_decalHonor_type",
            # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalHonor_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalHonor_type|values|Honor [Indent level: 4]
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalHonor_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalHonor_type|values|Platoon [Indent level: 4],
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalHonor_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalHonor_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalHonor_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_decalHonor [Indent level: 2],
        "rhs_decalhonor": {
            "displayname": "Set honor symbol",
            "tooltip": "Define symbol located on IR Lamp. Usually used for honor symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalHonor",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHST80HnrSymPlaces,  _this getVariable ['rhs_decalHonor_type','Honor'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_ammoslot_1_type [Indent level: 2],
        "rhs_ammoslot_1_type": {
            "displayname": "Ammo slot #1 type",
            "tooltip": "Define type of shell for #1 slot [AP rounds]",
            "property": "rhs_ammoslot_1_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm42_10 [Indent level: 4]
                "rhs_mag_3bm42_10": {
                    "name": "APFSDS-T 3BM42",
                    "value": "rhs_mag_3bm42",
                    "defaultvalue": "rhs_mag_3bm42"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm9_10 [Indent level: 4],
                "rhs_mag_3bm9_10": {
                    "name": "APFSDS-T 3BM9",
                    "value": "rhs_mag_3bm9",
                    "defaultvalue": "rhs_mag_3bm9"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm12_10 [Indent level: 4],
                "rhs_mag_3bm12_10": {
                    "name": "APFSDS-T 3BM12",
                    "value": "rhs_mag_3bm12",
                    "defaultvalue": "rhs_mag_3bm12"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm15_10 [Indent level: 4],
                "rhs_mag_3bm15_10": {
                    "name": "APFSDS-T 3BM15",
                    "value": "rhs_mag_3bm15",
                    "defaultvalue": "rhs_mag_3bm15"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm17_10 [Indent level: 4],
                "rhs_mag_3bm17_10": {
                    "name": "APFSDS-T 3BM17",
                    "value": "rhs_mag_3bm17",
                    "defaultvalue": "rhs_mag_3bm17"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm22_10 [Indent level: 4],
                "rhs_mag_3bm22_10": {
                    "name": "APFSDS-T 3BM22",
                    "value": "rhs_mag_3bm22",
                    "defaultvalue": "rhs_mag_3bm22"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm29_10 [Indent level: 4],
                "rhs_mag_3bm29_10": {
                    "name": "APFSDS-T 3BM29",
                    "value": "rhs_mag_3bm29",
                    "defaultvalue": "rhs_mag_3bm29"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm26_10 [Indent level: 4],
                "rhs_mag_3bm26_10": {
                    "name": "APFSDS-T 3BM26",
                    "value": "rhs_mag_3bm26",
                    "defaultvalue": "rhs_mag_3bm26"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm32_10 [Indent level: 4],
                "rhs_mag_3bm32_10": {
                    "name": "APFSDS-T 3BM32",
                    "value": "rhs_mag_3bm32",
                    "defaultvalue": "rhs_mag_3bm32"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm42m_10 [Indent level: 4],
                "rhs_mag_3bm42m_10": {
                    "name": "APFSDS-T 3BM42M",
                    "value": "rhs_mag_3bm42m",
                    "defaultvalue": "rhs_mag_3bm42m"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm46_10 [Indent level: 4],
                "rhs_mag_3bm46_10": {
                    "name": "APFSDS-T 3BM46",
                    "value": "rhs_mag_3bm46",
                    "defaultvalue": "rhs_mag_3bm46"
                }
            }
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_ammoslot_1 [Indent level: 2],
        "rhs_ammoslot_1": {
            "displayname": "Ammo slot #1 count",
            "tooltip": "Define number of rounds stored inside of type #1. Max 28. Leave -1 for default loadout",
            "property": "rhs_ammoslot_1",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',28] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_ammoslot_2_type [Indent level: 2],
        "rhs_ammoslot_2_type": {
            "displayname": "Ammo slot #2 type",
            "tooltip": "Define type of shell for #2 slot [HEAT rounds]",
            "property": "rhs_ammoslot_2_type",
            # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_2_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk21_8 [Indent level: 4]
                "rhs_mag_3bk21_8": {
                    "name": "HEAT-FS 3BK21",
                    "value": "rhs_mag_3bk21",
                    "defaultvalue": "rhs_mag_3bk21"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk12_8 [Indent level: 4],
                "rhs_mag_3bk12_8": {
                    "name": "HEAT-FS 3BK12",
                    "value": "rhs_mag_3bk12",
                    "defaultvalue": "rhs_mag_3bk12"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk14_8 [Indent level: 4],
                "rhs_mag_3bk14_8": {
                    "name": "HEAT-FS 3BK14",
                    "value": "rhs_mag_3bk14",
                    "defaultvalue": "rhs_mag_3bk14"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk18_8 [Indent level: 4],
                "rhs_mag_3bk18_8": {
                    "name": "HEAT-FS 3BK18",
                    "value": "rhs_mag_3bk18",
                    "defaultvalue": "rhs_mag_3bk18"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk18m_8 [Indent level: 4],
                "rhs_mag_3bk18m_8": {
                    "name": "HEAT-FS 3BK18M",
                    "value": "rhs_mag_3bk18m",
                    "defaultvalue": "rhs_mag_3bk18m"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk29_8 [Indent level: 4],
                "rhs_mag_3bk29_8": {
                    "name": "HEAT-FS 3BK29",
                    "value": "rhs_mag_3bk29",
                    "defaultvalue": "rhs_mag_3bk29"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk31_8 [Indent level: 4],
                "rhs_mag_3bk31_8": {
                    "name": "HEAT-FS 3BK31",
                    "value": "rhs_mag_3bk31",
                    "defaultvalue": "rhs_mag_3bk31"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_ammoslot_2 [Indent level: 2],
        "rhs_ammoslot_2": {
            "displayname": "Ammo slot #2 count",
            "tooltip": "Define number of rounds stored inside of type #2. Max 28. Leave -1 for default loadout",
            "property": "rhs_ammoslot_2",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',28] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_ammoslot_3_type [Indent level: 2],
        "rhs_ammoslot_3_type": {
            "displayname": "Ammo slot #3 type",
            "tooltip": "Define type of shell for #3 slot [HE rounds]",
            "property": "rhs_ammoslot_3_type",
            # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_3_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_3_type|values|rhs_mag_3of26_6 [Indent level: 4]
                "rhs_mag_3of26_6": {
                    "name": "HE-FRAG-FS 3OF26",
                    "value": "rhs_mag_3of26",
                    "defaultvalue": "rhs_mag_3of26"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_3_type|values|rhs_mag_3of11_6 [Indent level: 4],
                "rhs_mag_3of11_6": {
                    "name": "HE-FRAG-FS 3OF11",
                    "value": "rhs_mag_3of11",
                    "defaultvalue": "rhs_mag_3of11"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_ammoslot_3 [Indent level: 2],
        "rhs_ammoslot_3": {
            "displayname": "Ammo slot #3 count",
            "tooltip": "Define number of rounds stored inside of type #3. Max 28. Leave -1 for default loadout",
            "property": "rhs_ammoslot_3",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',28] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_ammoslot_4_type [Indent level: 2],
        "rhs_ammoslot_4_type": {
            "displayname": "Ammo slot #4 type",
            "tooltip": "Define type of shell for #4 slot [ATGM rounds]",
            "property": "rhs_ammoslot4_type",
            # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_4_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m112m_6 [Indent level: 4]
                "rhs_mag_9m112m_6": {
                    "name": "ATGM 9M112M",
                    "value": "rhs_mag_9m112m",
                    "defaultvalue": "rhs_mag_9m112m"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m112_6 [Indent level: 4],
                "rhs_mag_9m112_6": {
                    "name": "ATGM 9M112",
                    "value": "rhs_mag_9m112",
                    "defaultvalue": "rhs_mag_9m112"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m112m2_6 [Indent level: 4],
                "rhs_mag_9m112m2_6": {
                    "name": "ATGM 9M112M2",
                    "value": "rhs_mag_9m112m2",
                    "defaultvalue": "rhs_mag_9m112m2"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m124_6 [Indent level: 4],
                "rhs_mag_9m124_6": {
                    "name": "ATGM 9M124",
                    "value": "rhs_mag_9m124",
                    "defaultvalue": "rhs_mag_9m124"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m128_6 [Indent level: 4],
                "rhs_mag_9m128_6": {
                    "name": "ATGM 9M128",
                    "value": "rhs_mag_9m128",
                    "defaultvalue": "rhs_mag_9m128"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_ammoslot_4 [Indent level: 2],
        "rhs_ammoslot_4": {
            "displayname": "Ammo slot #4 count",
            "tooltip": "Define number of rounds stored inside of type #4. Max 28. Leave -1 for default loadout",
            "property": "rhs_ammoslot_4",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',28] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|sideskirt_unhide [Indent level: 2],
        "sideskirt_unhide": {
            "displayname": "Hide side skirt",
            "property": "sideskirt_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|fbskirt_unhide [Indent level: 2],
        "fbskirt_unhide": {
            "displayname": "Hide front bottom rubber skirt",
            "property": "fbskirt_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|ftskirt_unhide [Indent level: 2],
        "ftskirt_unhide": {
            "displayname": "Hide front top rubber skirt",
            "property": "ftskirt_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|log_unhide [Indent level: 2],
        "log_unhide": {
            "displayname": "Hide back log",
            "property": "log_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|kshield_unhide [Indent level: 2],
        "kshield_unhide": {
            "displayname": "Unhide commander shield",
            "expression": "[_this,1-_value,'%s'] call rhs_fnc_setHabarEden",
            "property": "kshield_unhide",
            "control": "CheckboxNumber",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_disableHabar [Indent level: 2],
        "rhs_disablehabar": {
            "displayname": "Disable randomized habar",
            "property": "rhs_disableHabar",
            "expression": "[_this,_value,'%s',_value] call rhs_fnc_setHabarEden",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_snorkel [Indent level: 2],
        "rhs_snorkel": {
            "displayname": "Mount snorkel",
            "property": "rhs_snorkel",
            "expression": "_this  animate ['snorkel_unhide',_value];_this  animate ['snorkel_unhide2',_value];_this animate ['snorkel_hide',1-_value];",
            "defaultvalue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles|rhs_t80bv|Attributes|rhs_searchlight [Indent level: 2],
        "rhs_searchlight": {
            "displayname": "Close gunner searchlight",
            "property": "rhs_searchlight",
            "control": "Checkbox",
            "expression": "[_this,_value] call rhs_fnc_t80_searchlightTexture ",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhs_t80b|Attributes|rhs_decalPlatoon_type [Indent level: 2],
        "rhs_decalplatoon_type": {
            "displayname": "Define platoon symbol type",
            "tooltip": "Decal type",
            "property": "rhs_decalPlatoon_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING",
            # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalPlatoon_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalPlatoon_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalPlatoon_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalPlatoon_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalPlatoon_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "1"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalPlatoon_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultvalue": "0"
                },
                # Class: CfgVehicles|rhs_tank_base|Attributes|rhs_decalPlatoon_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            }
        },
        # Class: CfgVehicles|rhs_t80b|Attributes|rhs_decalPlatoon [Indent level: 2],
        "rhs_decalplatoon": {
            "displayname": "Set platoon symbol",
            "tooltip": "Set platoon symbol located on turret front. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHST80PlnSymPlaces,  _this getVariable ['rhs_decalPlatoon_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        }
    },
    # Class: CfgVehicles|rhs_t80bv|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhs_t80bv|textureSources|RHS_CDF [Indent level: 2]
        "rhs_cdf": {
            "displayname": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_t80_hull_cdf_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_t80_turret_cdf_co.paa"]
        }
    },
    "typicalcargo": ["rhs_msv_crew","rhs_msv_crew","rhs_msv_crew"],
    "rhs_hassnorkel": 1,
    "rhs_habartype": 2,
    "allowtablock": 0,
    "destrtype": "DestructDefault",
    "htmin": 60,
    "htmax": 1800,
    "afmax": 200,
    "mfmax": 100,
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "simulation": "tankX",
    "normalspeedforwardcoef": 0.75,
    "slowspeedforwardcoef": 0.25,
    "fuelcapacity": 19.5,
    "rhs_fuelcapacity": 1540,
    "brakeidlespeed": 1.78,
    "maxspeed": 65,
    "enginemoi": 20,
    "enginepower": 809,
    "peaktorque": 4393,
    "minomega": 114.72,
    "maxomega": 350.86,
    "idlerpm": 1200,
    "redrpm": 3255,
    "torquecurve": [[0.30722,0],[0.447619,0.948555],[0.526574,0.897109],[0.60553,0.845664],[0.684485,0.794218],[0.763441,0.742773],[0.842396,0.691327],[1.90292,0]],
    "thrustdelay": 0.3,
    "dampingratefullthrottle": 0.3,
    "dampingratezerothrottleclutchengaged": 3,
    "dampingratezerothrottleclutchdisengaged": 0.25,
    "antirollbarforcecoef": 24,
    "antirollbarforcelimit": 42,
    "antirollbarspeedmin": 30,
    "antirollbarspeedmax": 75,
    "enginebrakecoef": 0,
    "tracksspeed": 1.4,
    "tankturnforce": 850000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.72,
    "accelaidforcecoef": 3.3,
    "accelaidforceyoffset": -4,
    "accelaidforcespd": 2.53,
    "maxfordingdepth": 0,
    "waterresistance": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "enginelosses": 25,
    "transmissionlosses": 15,
    "clutchstrength": 30,
    "latency": 1.3,
    "switchtime": 0,
    "changegeartype": "rpmratio",
    "changegearomegaratios": [1,0.333333,0.333333,0,0.96,0.333333,0.983333,0.7,0.983333,0.733333,0.983333,0.733333],
    # Class: CfgVehicles|rhs_tank_base|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-9.36,"N",0,"D1",4.38,"D2",2.16,"D3",1.46,"D4",1],
        "transmissionratios": ["High",12.85],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.9
    },
    # Class: CfgVehicles|rhs_tank_base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhs_tank_base|Wheels|L2 [Indent level: 2]
        "l2": {
            "susptraveldirection": [-0.125,-1,0],
            "bonename": "RHS_T80B_SUSL_1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|L3 [Indent level: 2],
        "l3": {
            "bonename": "RHS_T80B_SUSL_3",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|L4 [Indent level: 2],
        "l4": {
            "bonename": "RHS_T80B_SUSL_5",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|L5 [Indent level: 2],
        "l5": {
            "bonename": "RHS_T80B_SUSL_7",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|L6 [Indent level: 2],
        "l6": {
            "bonename": "RHS_T80B_SUSL_9",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|L7 [Indent level: 2],
        "l7": {
            "bonename": "RHS_T80B_SUSL_11",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|L9 [Indent level: 2],
        "l9": {
            "bonename": "",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|L1 [Indent level: 2],
        "l1": {
            "bonename": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|R2 [Indent level: 2],
        "r2": {
            "susptraveldirection": [0.125,-1,0],
            "bonename": "RHS_T80B_SUSR_1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|R3 [Indent level: 2],
        "r3": {
            "bonename": "RHS_T80B_SUSR_3",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|R4 [Indent level: 2],
        "r4": {
            "bonename": "RHS_T80B_SUSR_5",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|R5 [Indent level: 2],
        "r5": {
            "bonename": "RHS_T80B_SUSR_7",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|R6 [Indent level: 2],
        "r6": {
            "bonename": "RHS_T80B_SUSR_9",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|R7 [Indent level: 2],
        "r7": {
            "bonename": "RHS_T80B_SUSR_11",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "maxdroop": 0.14,
            "maxcompression": 0.14,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|R9 [Indent level: 2],
        "r9": {
            "bonename": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles|rhs_tank_base|Wheels|R1 [Indent level: 2],
        "r1": {
            "bonename": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "moi": 14.0783,
            "maxbraketorque": 10000,
            "sprungmass": 3416.67,
            "springstrength": 354000,
            "springdamperrate": 11000,
            "dampingrate": 1382,
            "dampingrateinair": 1382,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 72000,
            "frictionvsslipgraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        }
    },
    "soundengineonext": ["rhsafrf|addons|rhs_vehiclesounds|sounds|armor|t80|t80_engine_ext_start",1.77828,1,100],
    "soundengineonint": ["rhsafrf|addons|rhs_vehiclesounds|sounds|armor|t80|t80_engine_ext_start",1.77828,1],
    # Class: CfgVehicles|rhs_tank_base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|rhs_tank_base|Sounds|Idle_ext [Indent level: 2]
        "idle_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",0.794328,1,200],
            "frequency": "0.95	+	((rpm/	2640) factor[(400*1.57/	2640),(900*1.57/	2640)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(100*1.57/	2640),(200*1.57/	2640)])	*	((rpm/	2640) factor[(900*1.57/	2640),(700*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine [Indent level: 2],
        "engine": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",0.891251,1,240],
            "frequency": "0.8	+	((rpm/	2640) factor[(700*1.57/	2640),(1100*1.57/	2640)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(705*1.57/	2640),(850*1.57/	2640)])	*	((rpm/	2640) factor[(1100 *1.57/	2640),(950*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine1_ext [Indent level: 2],
        "engine1_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",1.12202,1,280],
            "frequency": "0.8	+	((rpm/	2640) factor[(950*1.57/	2640),(1400*1.57/	2640)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(900*1.57/	2640),(1050*1.57/	2640)])	*	((rpm/	2640) factor[(1400*1.57/	2640),(1200*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine2_ext [Indent level: 2],
        "engine2_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",1.25893,1,320],
            "frequency": "0.8	+	((rpm/	2640) factor[(1200*1.57/	2640),(1700*1.57/	2640)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(1170*1.57/	2640),(1380*1.57/	2640)])	*	((rpm/	2640) factor[(1700*1.57/	2640),(1500*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine3_ext [Indent level: 2],
        "engine3_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",1.41254,1,360],
            "frequency": "0.8	+	((rpm/	2640) factor[(1500*1.57/	2640),(2100*1.57/	2640)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(1500*1.57/	2640),(1670*1.57/	2640)])	*	((rpm/	2640) factor[(2100*1.57/	2640),(1800*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine4_ext [Indent level: 2],
        "engine4_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",1.58489,1,400],
            "frequency": "0.8	+	((rpm/	2640) factor[(1800*1.57/	2640),(2300*1.57/	2640)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(1780*1.57/	2640),(2060*1.57/	2640)])	*	((rpm/	2640) factor[(2450*1.57/	2640),(2200*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine5_ext [Indent level: 2],
        "engine5_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",1.77828,1,440],
            "frequency": "0.8	+	((rpm/	2640) factor[(2100*1.57/	2640),(2640*1.57/	2640)])*0.1",
            "volume": "engineOn*camPos*((rpm/	2640) factor[(2150*1.57/	2640),(2500*1.57/	2640)])"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Idle_int [Indent level: 2],
        "idle_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm1",0.501187,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(400*1.57/	2640),(900*1.57/	2640)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(100*1.57/	2640),(200*1.57/	2640)])	*	((rpm/	2640) factor[(900*1.57/	2640),(700*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine_int [Indent level: 2],
        "engine_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm2",0.354813,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(700*1.57/	2640),(1100*1.57/	2640)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(705*1.57/	2640),(850*1.57/	2640)])	*	((rpm/	2640) factor[(1100 *1.57/	2640),(950*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine1_int [Indent level: 2],
        "engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm3",0.398107,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(950*1.57/	2640),(1400*1.57/	2640)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(900*1.57/	2640),(1050*1.57/	2640)])	*	((rpm/	2640) factor[(1400*1.57/	2640),(1200*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine2_int [Indent level: 2],
        "engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm4",0.446684,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(1200*1.57/	2640),(1700*1.57/	2640)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(1170*1.57/	2640),(1380*1.57/	2640)])	*	((rpm/	2640) factor[(1700*1.57/	2640),(1500*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine3_int [Indent level: 2],
        "engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm5",0.501187,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(1500*1.57/	2640),(2100*1.57/	2640)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(1500*1.57/	2640),(1670*1.57/	2640)])	*	((rpm/	2640) factor[(2100*1.57/	2640),(1800*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine4_int [Indent level: 2],
        "engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm6",0.562341,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(1800*1.57/	2640),(2300*1.57/	2640)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(1780*1.57/	2640),(2060*1.57/	2640)])	*	((rpm/	2640) factor[(2450*1.57/	2640),(2200*1.57/	2640)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|Engine5_int [Indent level: 2],
        "engine5_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm7",0.630957,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(2100*1.57/	2640),(2640*1.57/	2640)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	2640) factor[(2150*1.57/	2640),(2500*1.57/	2640)])"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|NoiseInt [Indent level: 2],
        "noiseint": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_int_1",0.501187,1],
            "frequency": "1",
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|NoiseExt [Indent level: 2],
        "noiseext": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_ext_1",0.891251,1,50],
            "frequency": "1",
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsOutH0 [Indent level: 2],
        "threadsouth0": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|T80-Treads",0.398107,1,140],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsOutH1 [Indent level: 2],
        "threadsouth1": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|T80-Treads",0.446684,1,160],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsOutH2 [Indent level: 2],
        "threadsouth2": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|T80-Treads",0.501187,1,180],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsOutH3 [Indent level: 2],
        "threadsouth3": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|T80-Treads",0.562341,1,200],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsOutH4 [Indent level: 2],
        "threadsouth4": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|T80-Treads",0.562341,1,220],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsOutS0 [Indent level: 2],
        "threadsouts0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_ext_treads_soft_01",0.316228,1,120],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsOutS1 [Indent level: 2],
        "threadsouts1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_ext_treads_soft_02",0.354813,1,140],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsOutS2 [Indent level: 2],
        "threadsouts2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_ext_treads_soft_03",0.398107,1,160],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsOutS3 [Indent level: 2],
        "threadsouts3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_ext_treads_soft_04",0.446684,1,180],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsOutS4 [Indent level: 2],
        "threadsouts4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_ext_treads_soft_05",0.501187,1,200],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsInH0 [Indent level: 2],
        "threadsinh0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_hard_01",0.251189,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsInH1 [Indent level: 2],
        "threadsinh1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_hard_02",0.281838,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsInH2 [Indent level: 2],
        "threadsinh2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_hard_03",0.316228,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsInH3 [Indent level: 2],
        "threadsinh3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_hard_04",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsInH4 [Indent level: 2],
        "threadsinh4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_hard_05",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsInS0 [Indent level: 2],
        "threadsins0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_soft_01",0.316228,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsInS1 [Indent level: 2],
        "threadsins1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_soft_02",0.316228,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsInS2 [Indent level: 2],
        "threadsins2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_soft_03",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsInS3 [Indent level: 2],
        "threadsins3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_soft_04",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles|rhs_tank_base|Sounds|ThreadsInS4 [Indent level: 2],
        "threadsins4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_soft_05",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        "soundsetsint": ["RHS_T80_Engine_RPM0_INT_SoundSet","RHS_T80_Engine_RPM1_INT_SoundSet","RHS_T80_Engine_RPM2_INT_SoundSet","RHS_T80_Engine_INT_Burst_SoundSet","RHS_T80_Tracks_01_INT_SoundSet","RHS_T80_Tracks_02_INT_SoundSet","RHS_T80_Tracks_03_INT_SoundSet","RHS_T80_Tracks_04_INT_SoundSet","RHS_T80_Tracks_05_INT_SoundSet","RHS_T80_Tracks_06_INT_SoundSet","RHS_T80_Interior_Tone_Engine_Off_SoundSet","RHS_T80_Interior_Tone_Engine_On_SoundSet","RHS_T80_Rattling_INT_SoundSet","RHS_T80_Rain_INT_SoundSet","RHS_T80_Tracks_Brake_Hard_INT_SoundSet","RHS_T80_Tracks_Brake_Soft_INT_SoundSet","RHS_T80_Tracks_Turn_Hard_INT_SoundSet","RHS_T80_Tracks_Turn_Soft_INT_SoundSet","RHS_T80_Drive_Water_INT_SoundSet","RHS_T80_Drive_Dirt_INT_SoundSet","","MBT_02_Turbine01_Int_Tonal_SoundSet","MBT_02_Turbine01_Int_Noisy_SoundSet","MBT_02_Servo01_Int_SoundSet","Tracks_Movement_Dirt_Int_01_SoundSet","Tracks_Surface_Soft_Int_SoundSet","Tracks_Surface_Sand_Int_SoundSet","Tracks_Surface_Squeaks_Soft_Int_SoundSet","Tracks_Surface_Squeaks_Hard_Int_SoundSet","Tanks_Material_Strain_Int_SoundSet","Tank_General_Collision_Int_SoundSet","rhs_tank_t72_int_autoloader_SoundSet"],
        "soundsetsext": ["RHS_T80_Engine_RPM0_EXT_SoundSet","RHS_T80_Engine_RPM1_EXT_SoundSet","RHS_T80_Engine_RPM2_EXT_SoundSet","RHS_T80_Engine_EXT_Burst_SoundSet","RHS_T80_Tracks_01_EXT_SoundSet","RHS_T80_Tracks_02_EXT_SoundSet","RHS_T80_Tracks_03_EXT_SoundSet","RHS_T80_Tracks_04_EXT_SoundSet","RHS_T80_Tracks_05_EXT_SoundSet","RHS_T80_Tracks_06_EXT_SoundSet","RHS_T80_Rain_EXT_SoundSet","RHS_T80_Tracks_Brake_Hard_EXT_SoundSet","RHS_T80_Tracks_Brake_Soft_EXT_SoundSet","RHS_T80_Tracks_Turn_Hard_EXT_SoundSet","RHS_T80_Tracks_Turn_Soft_EXT_SoundSet","RHS_T80_Drive_Water_EXT_SoundSet","RHS_T80_Drive_Dirt_EXT_SoundSet","","MBT_02_Turbine01_Ext_Front_Tonal_SoundSet","MBT_02_Turbine01_Ext_Rear_Tonal_SoundSet","MBT_02_Turbine01_Ext_Front_Noisy_SoundSet","MBT_02_Turbine01_Ext_Rear_Noisy_SoundSet","MBT_02_Servo01_Ext_SoundSet","MBT_02_Servo02_Ext_SoundSet","Tracks_Movement_Dirt_Ext_01_SoundSet","Tracks_Surface_Soft_Ext_SoundSet","Tracks_Surface_Sand_Ext_SoundSet","Tracks_Surface_Squeaks_Soft_Ext_SoundSet","Tracks_Surface_Squeaks_Hard_Ext_SoundSet","Tank_General_Collision_SoundShader","rhs_tank_t72_ext_autoloader_SoundSet"]
    },
    "picture": "rhsafrf|addons|rhs_t80|data|icon|rhs_t80_pic_ca.paa",
    "icon": "rhsafrf|addons|rhs_t72|data|icomap_t72_CA.paa",
    "mapsize": 9.5,
    "vehicleclass": "rhs_vehclass_tank",
    "editorsubcategory": "rhs_EdSubcat_tank",
    "accuracy": 0.2,
    "cost": 1.5e+006,
    "unitinfotype": "RHS_RscInfoT80",
    "tf_range_api": 45000,
    "enablegps": 0,
    "incomingmissiledetectionsystem": 0,
    "drivercansee": "2+4+8",
    "gunnercansee": "2+4+8",
    "commandercansee": "2+4+8",
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
    "viewdrivershadow": 1,
    "viewdriverinexternal": 1,
    "forcehidedriver": 0,
    "driverforceoptics": 1,
    "driveroutforceoptics": 1,
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "driveraction": "driver_apcwheeled2_out",
    "driverinaction": "rhs_t72_driver",
    "driverdoor": "hatchD",
    "memorypointdriveroutoptics": "Driver_out_view",
    "driveropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
    "loddriverturnedin": 0,
    "loddriverturnedout": 0,
    "loddriveropticsin": 0,
    "extcameraposition": [0,2.25,-10],
    # Class: CfgVehicles|rhs_tank_base|DriverOpticsIn [Indent level: 1],
    "driveropticsin": {
        # Class: CfgVehicles|rhs_tank_base|DriverOpticsIn|OpticView [Indent level: 2]
        "opticview": {
            "opticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5",
            "hitpoint": "Hit_Optic_Driver2",
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
    "hiddenselections": ["camo1","camo2","","Search_random","n1","n2","n3","i1","i2","i3"],
    "texturelist": [],
    "rhs_randomizedhabar": ["log_unhide","sideskirt_unhide","fbskirt_unhide","ftskirt_unhide"],
    "wheelcircumference": 2.312,
    "damageresistance": 0.02,
    "type": 1,
    "threat": [0.9,0.8,0.2],
    "driveoncomponent": ["Slide"],
    "armorstructural": 220,
    "explosionshielding": 100,
    "crewexplosionprotection": 1,
    "mintotaldamagethreshold": 0.5,
    "fireresistance": -1,
    "crewvulnerable": 0,
    # Class: CfgVehicles|rhs_tank_base|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initfov": 0.7,
        "minfov": 0.7,
        "maxfov": 0.7,
        "visionmode": ["Normal","NVG"],
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
    # Class: CfgVehicles|rhs_tank_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhs_tank_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles|rhs_tank_base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles|rhs_tank_base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    "insidesoundcoef": 0.9,
    # Class: CfgVehicles|rhs_tank_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhs_tank_base|Reflectors|Driver_FG125_Cover [Indent level: 2]
        "driver_fg125_cover": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerangle": 35,
            "outerangle": 75,
            "conefadecoef": 5,
            "intensity": 15,
            "useflare": 0,
            "daylight": 1,
            "flaresize": 0.85,
            # Class: CfgVehicles|rhs_tank_base|Reflectors|Driver_FG125_Cover|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.2,
                "hardlimitstart": 130,
                "hardlimitend": 160
            }
        },
        # Class: CfgVehicles|rhs_tank_base|Reflectors|Driver_FG125_Cover_Flare [Indent level: 2],
        "driver_fg125_cover_flare": {
            "intensity": 5,
            "innerangle": 55,
            "outerangle": 155,
            "flaresize": 0.3,
            "useflare": 1,
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "conefadecoef": 5,
            "daylight": 1,
            # Class: CfgVehicles|rhs_tank_base|Reflectors|Driver_FG125_Cover|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.2,
                "hardlimitstart": 130,
                "hardlimitend": 160
            }
        }
    },
    "aggregatereflectors": [["Driver_FG125_Cover","Driver_FG125_Cover_Flare"]],
    "armorlights": 0.1,
    # Class: CfgVehicles|rhs_tank_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhs_tank_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "vyfuk start",
            "direction": "vyfuk konec",
            "effect": "RHS_ExhaustEffectTankGasBack"
        },
        # Class: CfgVehicles|rhs_tank_base|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "vyfuk start 2",
            "direction": "vyfuk konec 2",
            "effect": "RHS_ExhaustEffectTankGasBack"
        }
    },
    "selectionleftoffset": "pasanimL",
    "selectionrightoffset": "pasanimP",
    # Class: CfgVehicles|rhs_tank_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhs_tank_base|EventHandlers|RHS_EventHandlers [Indent level: 2]
        "rhs_eventhandlers": {
            "init": "_this call RHS_fnc_t80_init;",
            "fired": "_this call RHS_fnc_t80_autoloader;",
            "killed": "[_this select 0,'rhs_Wreck_T80_turret_F'] call rhs_fnc_turretBlow",
            "engine": "[_this select 0,_this select 1,20] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_engineCheckDamage;",
            "getout": "_this call rhs_fnc_t72_hatch;_this call rhs_fnc_hatchAbandon"
        },
        # Class: CfgVehicles|rhs_tank_base|EventHandlers|RHS_HitSpall [Indent level: 2],
        "rhs_hitspall": {
            "hitpart": "_this call rhs_fnc_hitSpall"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    # Class: CfgVehicles|rhs_tank_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhs_tank_base|UserActions|trunk_open [Indent level: 2]
        "trunk_open": {
            "displayname": "Use NSVT",
            "position": "trunk_action",
            "radius": 2,
            "onlyforplayer": 0,
            "condition": "this animationPhase 'RHS_T80B_Hatch_commander'>0.5 and ((call rhs_fnc_findPlayer) == commander this)",
            "statement": "(call rhs_fnc_findPlayer) action ['moveToTurret', this, [0,1]];[this,[[0,0],true]] remoteExecCall ['lockTurret']"
        },
        # Class: CfgVehicles|rhs_tank_base|UserActions|trunk_close [Indent level: 2],
        "trunk_close": {
            "displayname": "Leave NSVT",
            "condition": "vehicle (call rhs_fnc_findPlayer) turretUnit [0,1] == (call rhs_fnc_findPlayer)",
            "statement": "(call rhs_fnc_findPlayer) action ['moveToTurret', this, [0,0]];[this,[[0,0],false]] remoteExecCall ['lockTurret']",
            "position": "trunk_action",
            "radius": 2,
            "onlyforplayer": 0
        }
    },
    # Class: CfgVehicles|rhs_tank_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_t80|data|materials|hull_g.rvmat","rhsafrf|addons|rhs_t80|data|materials|hull_g_dam.rvmat","rhsafrf|addons|rhs_t80|data|materials|hull_destroy.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_bk.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_G_dam.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_destroy.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_G.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_G_dam.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_destroy.rvmat","rhsafrf|addons|rhs_t80|data|materials|track.rvmat","rhsafrf|addons|rhs_t80|data|materials|track.rvmat","rhsafrf|addons|rhs_t80|data|materials|track_destroy.rvmat","rhsafrf|addons|rhs_t80|data|materials|searchlight.rvmat","rhsafrf|addons|rhs_t80|data|materials|searchlight.rvmat","rhsafrf|addons|rhs_t80|data|materials|searchlight_destroy.rvmat"]
    },
    # Class: CfgVehicles|rhs_tank_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhs_tank_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhs_tank_base|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_tank_base|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 3],
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles|rhs_tank_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            # Class: CfgVehicles|rhs_tank_base|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_tank_base|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 3],
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
    "attenuationeffecttype": "TankAttenuation",
    "soundgetin": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1],
    "soundgetout": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1,20],
    "soundturnin": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnout": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnininternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnoutinternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "sounddammage": ["",0.562341,1],
    "soundengineoffint": ["A3|Sounds_F|vehicles2|armor|MBT_02|MBT_02_Engine_Int_Stop",1,1],
    "soundengineoffext": ["A3|Sounds_F|vehicles2|armor|MBT_02|MBT_02_Engine_Ext_Stop",3.16228,1,100],
    "bushcrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_01",0.630957,1,100],
    "bushcrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_02",0.630957,1,100],
    "bushcrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_03",0.630957,1,100],
    "soundbushcrash": ["BushCrash1",0.33,"BushCrash2",0.33,"BushCrash3",0.33],
    "buildcrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "buildcrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "buildcrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "buildcrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "buildcrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "buildcrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundbuildingcrash": ["buildCrash0",0.166,"buildCrash1",0.166,"buildCrash2",0.166,"buildCrash3",0.166,"buildCrash4",0.166,"buildCrash5",0.166],
    "woodcrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "woodcrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "woodcrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "woodcrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "woodcrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "woodcrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundwoodcrash": ["woodCrash0",0.166,"woodCrash1",0.166,"woodCrash2",0.166,"woodCrash3",0.166,"woodCrash4",0.166,"woodCrash5",0.166],
    "armorcrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "armorcrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "armorcrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "armorcrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "armorcrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "armorcrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundarmorcrash": ["ArmorCrash0",0.166,"ArmorCrash1",0.166,"ArmorCrash2",0.166,"ArmorCrash3",0.166,"ArmorCrash4",0.166,"ArmorCrash5",0.166],
    "_generalmacro": "Tank_F",
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
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
    "secondaryexplosion": -1,
    "fuelexplosionpower": 1,
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
    "canfloat": 0,
    "camouflage": 8,
    "driveropticscolor": [1,1,1,1],
    # Class: CfgVehicles|Tank|CargoLight [Indent level: 1],
    "cargolight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
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
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "obstructsoundlfratio": 0,
    "occludesoundlfratio": 0.25,
    "unloadincombat": 0,
    "epeimpulsedamagecoef": 30,
    "gunnerhasflares": 1,
    "enablemanualfire": 1,
    "sensitivity": 2.5,
    "portrait": "",
    "ghostpreview": "",
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
    "artilleryscanner": 0,
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
    "showalltargets": 0,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
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
    "soundlocked": ["",1,1],
    "cargoaction": [],
    "cargoiscodriver": [0],
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
    "driveropticseffect": [],
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadowdiff": 1,
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
    "features": "",
    "insidedetectcoef": 0.05,
}