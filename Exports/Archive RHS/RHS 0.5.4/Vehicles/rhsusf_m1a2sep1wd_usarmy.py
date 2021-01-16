rhsusf_m1a2sep1wd_usarmy = {
    "editorpreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_m1a2sep1wd_usarmy.paa",
    "scope": 2,
    "displayname": "M1A2SEPv1",
    "author": "Red Hammer Studios",
    "faction": "rhs_faction_usarmy_wd",
    "vehicleclass": "rhs_vehclass_tank",
    "crew": "rhsusf_army_ucp_combatcrewman",
    "rhs_decalparameters": ["['Label', cM1PlnSymPlaces, 'ArmyPlt_Abrams_WD']","['Label', cM1BarrelSymPlaces, 'BarrelArt_Abrams_WD']"],
    "accuracy": 0.3,
    "model": "rhsusf|addons|rhsusf_m1a2|m1a2v1",
    "icon": "rhsusf|addons|rhsusf_m1a2|icons|M1A2SEPV1.paa",
    "picture": "rhsusf|addons|rhsusf_m1a2|icons|M1A2SIDE_ca.paa",
    "typicalcargo": [],
    "side": 1,
    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets [Indent level: 3]
            "turrets": {
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics [Indent level: 4]
                "commanderoptics": {
                    "body": "CITVTurret",
                    "gun": "CITVGun",
                    "animationsourcebody": "CITVTurret",
                    "animationsourcegun": "CITVGun",
                    "maxhorizontalrotspeed": 1.3,
                    "maxverticalrotspeed": 0.48,
                    "stabilizedinaxes": 3,
                    "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",1,1,30],
                    "soundservovertical": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",1,1,30],
                    "minelev": -5,
                    "maxelev": 60,
                    "initelev": 0,
                    "minturn": -360,
                    "maxturn": 360,
                    "initturn": 0,
                    "memorypointgun": "usti hlavne3",
                    "gunbeg": "usti hlavne3",
                    "gunend": "konec hlavne3",
                    "lodturnedout": 1200,
                    "weapons": ["rhsusf_weap_M250"],
                    "magazines": ["rhsusf_mag_L8A3_12"],
                    "turretinfotype": "RscOptics_Offroad_01",
                    "memorypointgunneroutoptics": "",
                    "memorypointgunneroptics": "CITV_view",
                    "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Commander_02_F",
                    "gunneroutforceoptics": 0,
                    "gunneroutopticsmodel": "",
                    "gunneropticseffect": [],
                    "gunnerhasflares": 1,
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
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
                        "thermalmode": [2,3],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Wide [Indent level: 6]
                        "wide": {
                            "initfov": 0.233333,
                            "minfov": 0.233333,
                            "maxfov": 0.233333,
                            "hitpoint": "Hit_Optic_CITV",
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CITV_w",
                            "visionmode": ["Normal","NVG","TI"],
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Medium [Indent level: 6],
                        "medium": {
                            "initfov": 0.116667,
                            "minfov": 0.116667,
                            "maxfov": 0.116667,
                            "hitpoint": "Hit_Optic_CITV",
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CITV_m",
                            "visionmode": ["Normal","NVG","TI"],
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Medium_TI [Indent level: 6],
                        "medium_ti": {
                            "initfov": 0.0538462,
                            "minfov": 0.0538462,
                            "maxfov": 0.0538462,
                            "visionmode": ["Ti"],
                            "hitpoint": "Hit_Optic_CITV",
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CITV_m",
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Medium2_TI [Indent level: 6],
                        "medium2_ti": {
                            "initfov": 0.028,
                            "minfov": 0.028,
                            "maxfov": 0.028,
                            "visionmode": ["Ti"],
                            "hitpoint": "Hit_Optic_CITV",
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CITV_m",
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Narrow_TI [Indent level: 6],
                        "narrow_ti": {
                            "initfov": 0.014,
                            "minfov": 0.014,
                            "maxfov": 0.014,
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CITV_n",
                            "visionmode": ["Ti"],
                            "hitpoint": "Hit_Optic_CITV",
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: Optics_Commander_01|Narrow [Indent level: 0],
                        "narrow": {
                            "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Commander_01_n_F.p3d",
                            "initfov": "(60 * 0.05625 / 120)",
                            "minfov": "(60 * 0.05625 / 120)",
                            "maxfov": "(60 * 0.05625 / 120)",
                            "visionmode": ["Normal","NVG","TI"],
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        }
                    },
                    "gunneraction": "mbt2_slot2b_out",
                    "gunnerinaction": "RHS_M1A2_Commander",
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "startengine": 0,
                    "viewgunnerinexternal": 1,
                    "outgunnermayfire": 1,
                    "ingunnermayfire": 1,
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitTurretCom [Indent level: 6]
                        "hitturretcom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25,
                            "isturret": 1
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitGunCom [Indent level: 6],
                        "hitguncom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25,
                            "isgun": 1
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|Hit_Optic_CITV [Indent level: 6],
                        "hit_optic_citv": {
                            "armor": -40,
                            "explosionshielding": 0,
                            "name": "",
                            "visual": "vis_optic_CITV",
                            "armorcomponent": "Hit_Optic_CITV",
                            "passthrough": 0
                        }
                    },
                    "selectionfireanim": "",
                    "discretedistance": [400],
                    "discretedistanceinitindex": 0,
                    "canusescanners": 0,
                    "showcrewaim": 0,
                    "allowtablock": 0,
                    "gunnerforceoptics": 1,
                    "gunnerdoor": "hatchC",
                    "turretfollowfreelook": 2,
                    "usepip": 2,
                    "animationsourcestickx": "com_turret_control_x",
                    "animationsourcesticky": "com_turret_control_y",
                    "gunnerrighthandanimname": "com_turret_control",
                    "lodturnedin": 1100,
                    "lodopticsin": 0,
                    "viewgunnershadowamb": 0.5,
                    "viewgunnershadowdiff": 0.05,
                    "ispersonturret": 1,
                    "personturretaction": "vehicle_turnout_2",
                    "minoutelev": -10,
                    "maxoutelev": 25,
                    "initoutelev": 0,
                    "minoutturn": -95,
                    "maxoutturn": 95,
                    "initoutturn": 0,
                    # Class: CfgVehicles|MBT_01_base_F|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
                    "viewgunner": {
                        "initanglex": -10,
                        "initangley": 0,
                        "initfov": 0.9,
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
                    # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: VehicleSystemsTemplateLeftCommander|Components [Indent level: 0]
                            "components": {
                                # Class: VehicleSystemsTemplateLeftCommander|Components|VehicleDriverDisplay [Indent level: 1]
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateLeftCommander|Components|VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "left": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        },
                        # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: VehicleSystemsTemplateRightCommander|Components [Indent level: 0]
                            "components": {
                                # Class: VehicleSystemsTemplateRightCommander|Components|VehicleDriverDisplay [Indent level: 1]
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateRightCommander|Components|VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "right": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "proxytype": "CPCommander",
                    "proxyindex": 1,
                    "gunnername": "Commander",
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "animationsourcehatch": "hatchCommander",
                    "animationsourcecamelev": "camElev",
                    "commanding": 2,
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
                    "gunnertype": "",
                    "soundelevation": ["",0.00316228,1],
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
                    "gunneropticsshowcursor": 0,
                    "gunnerfirealsoininternalcamera": 1,
                    "gunneroutfirealsoininternalcamera": 1,
                    "gunnerusespilotview": 0,
                    "castgunnershadow": 0,
                    "viewgunnershadow": 1,
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
                    "gunnerleftleganimname": "",
                    "gunnerrightleganimname": "",
                    "precisegetinout": 0,
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
                    }
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|Loader [Indent level: 4],
                "loader": {
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|Loader|HitPoints [Indent level: 5]
                    "hitpoints": {
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|Loader|HitPoints|Hit_Optic_LoaderPeriscope [Indent level: 6]
                        "hit_optic_loaderperiscope": {
                            "armor": -40,
                            "explosionshielding": 0,
                            "name": "",
                            "visual": "vis_optic_LoaderPeriscope",
                            "armorcomponent": "Hit_Optic_LoaderPeriscope",
                            "passthrough": 0
                        }
                    },
                    "ispersonturret": 1,
                    "lockwhendriverout": 0,
                    "lodturnedout": 1200,
                    "minturn": -140,
                    "maxturn": 140,
                    "stabilizedinaxes": 0,
                    "gunneraction": "RHS_M1A1_Loader_out",
                    "gunnerinaction": "RHS_M1A1_Loader_in",
                    "weapons": [],
                    "magazines": [],
                    "gunneroutforceoptics": 0,
                    "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                    "ingunnermayfire": 1,
                    "outgunnermayfire": 1,
                    "memorypointgun": "usti hlavne5",
                    "gunbeg": "usti hlavne5",
                    "gunend": "konec hlavne5",
                    "selectionfireanim": "",
                    "soundattenuationturret": "HeliAttenuationGunner",
                    "disablesoundattenuation": 0,
                    "animationsourcehatch": "HatchGunner",
                    "animationsourcebody": "LoaderVisorTurret",
                    "animationsourcegun": "LoaderVisorGun",
                    "body": "LoaderVisorTurret",
                    "gun": "LoaderVisorGun",
                    "animationsourcestickx": "",
                    "animationsourcesticky": "",
                    "commanding": -3,
                    "primaryobserver": 0,
                    "memorypointsgetingunner": "pos gunner",
                    "memorypointsgetingunnerdir": "pos gunner dir",
                    "gunnername": "Loader",
                    "memorypointgunneroptics": "loadervisor_view",
                    "soundservo": ["A3|sounds_f|dummysound",1e-006,1],
                    "gunnerdoor": "hatchL",
                    "proxyindex": 2,
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|Loader|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|Loader|OpticsIn|Periscope [Indent level: 6]
                        "periscope": {
                            "initfov": 0.7,
                            "minfov": 0.7,
                            "maxfov": 0.7,
                            "visionmode": ["Normal"],
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhs_periscope_BISType",
                            "hitpoint": "Hit_Optic_LoaderPeriscope",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "thermalmode": [2,3],
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0,
                            "speedzoommaxspeed": 1e+010,
                            "speedzoommaxfov": 0
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|Loader|OpticsIn|Wide [Indent level: 6],
                        "wide": {
                            "campos": "CITV_view",
                            "camdir": "CITV_view_dir",
                            "initfov": 0.233333,
                            "minfov": 0.233333,
                            "maxfov": 0.233333,
                            "hitpoint": "Hit_Optic_CITV",
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CITV_w",
                            "visionmode": ["Normal","NVG","TI"],
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|Loader|OpticsIn|Medium [Indent level: 6],
                        "medium": {
                            "campos": "CITV_view",
                            "camdir": "CITV_view_dir",
                            "initfov": 0.116667,
                            "minfov": 0.116667,
                            "maxfov": 0.116667,
                            "hitpoint": "Hit_Optic_CITV",
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CITV_m",
                            "visionmode": ["Normal","NVG","TI"],
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|Loader|OpticsIn|Medium_TI [Indent level: 6],
                        "medium_ti": {
                            "campos": "CITV_view",
                            "camdir": "CITV_view_dir",
                            "initfov": 0.0538462,
                            "minfov": 0.0538462,
                            "maxfov": 0.0538462,
                            "visionmode": ["Ti"],
                            "hitpoint": "Hit_Optic_CITV",
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CITV_m",
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|Loader|OpticsIn|Medium2_TI [Indent level: 6],
                        "medium2_ti": {
                            "campos": "CITV_view",
                            "camdir": "CITV_view_dir",
                            "initfov": 0.028,
                            "minfov": 0.028,
                            "maxfov": 0.028,
                            "visionmode": ["Ti"],
                            "hitpoint": "Hit_Optic_CITV",
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CITV_m",
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|Loader|OpticsIn|Narrow_TI [Indent level: 6],
                        "narrow_ti": {
                            "campos": "CITV_view",
                            "camdir": "CITV_view_dir",
                            "initfov": 0.014,
                            "minfov": 0.014,
                            "maxfov": 0.014,
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_CITV_n",
                            "visionmode": ["Ti"],
                            "hitpoint": "Hit_Optic_CITV",
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: Optics_Commander_01|Narrow [Indent level: 0],
                        "narrow": {
                            "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Commander_01_n_F.p3d",
                            "initfov": "(60 * 0.05625 / 120)",
                            "minfov": "(60 * 0.05625 / 120)",
                            "maxfov": "(60 * 0.05625 / 120)",
                            "visionmode": ["Normal","NVG","TI"],
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        }
                    },
                    "maxhorizontalrotspeed": 1.3,
                    "maxverticalrotspeed": 0.48,
                    "soundservovertical": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",1,1,30],
                    "minelev": -5,
                    "maxelev": 60,
                    "initelev": 0,
                    "initturn": 0,
                    "turretinfotype": "RscOptics_Offroad_01",
                    "memorypointgunneroutoptics": "",
                    "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Commander_02_F",
                    "gunneropticseffect": [],
                    "gunnerhasflares": 1,
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
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
                        "thermalmode": [2,3],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "startengine": 0,
                    "viewgunnerinexternal": 1,
                    "discretedistance": [400],
                    "discretedistanceinitindex": 0,
                    "canusescanners": 0,
                    "showcrewaim": 0,
                    "allowtablock": 0,
                    "gunnerforceoptics": 1,
                    "turretfollowfreelook": 2,
                    "usepip": 2,
                    "gunnerrighthandanimname": "com_turret_control",
                    "lodturnedin": 1100,
                    "lodopticsin": 0,
                    "viewgunnershadowamb": 0.5,
                    "viewgunnershadowdiff": 0.05,
                    "personturretaction": "vehicle_turnout_2",
                    "minoutelev": -10,
                    "maxoutelev": 25,
                    "initoutelev": 0,
                    "minoutturn": -95,
                    "maxoutturn": 95,
                    "initoutturn": 0,
                    # Class: CfgVehicles|MBT_01_base_F|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
                    "viewgunner": {
                        "initanglex": -10,
                        "initangley": 0,
                        "initfov": 0.9,
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
                    # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: VehicleSystemsTemplateLeftCommander|Components [Indent level: 0]
                            "components": {
                                # Class: VehicleSystemsTemplateLeftCommander|Components|VehicleDriverDisplay [Indent level: 1]
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateLeftCommander|Components|VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "left": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        },
                        # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: VehicleSystemsTemplateRightCommander|Components [Indent level: 0]
                            "components": {
                                # Class: VehicleSystemsTemplateRightCommander|Components|VehicleDriverDisplay [Indent level: 1]
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateRightCommander|Components|VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "right": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "proxytype": "CPCommander",
                    "primarygunner": 0,
                    "animationsourcecamelev": "camElev",
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "gunnertype": "",
                    "soundelevation": ["",0.00316228,1],
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
                    "gunneropticsshowcursor": 0,
                    "gunnerfirealsoininternalcamera": 1,
                    "gunneroutfirealsoininternalcamera": 1,
                    "gunnerusespilotview": 0,
                    "castgunnershadow": 0,
                    "viewgunnershadow": 1,
                    "ejectdeadgunner": 0,
                    "hideweaponsgunner": 1,
                    "canhidegunner": -1,
                    "forcehidegunner": 0,
                    "showhmd": 0,
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
                    "gunnerleftleganimname": "",
                    "gunnerrightleganimname": "",
                    "precisegetinout": 0,
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
                    }
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderMG [Indent level: 4],
                "commandermg": {
                    "gunnername": "Commander MG",
                    "proxyindex": 3,
                    "dontcreateai": 1,
                    "cantcreateai": 1,
                    "ispersonturret": 0,
                    "body": "ObsTurret",
                    "gun": "ObsGun",
                    "animationsourcebody": "ObsTurret",
                    "animationsourcegun": "ObsGun",
                    "animationsourcestickx": "CommanderTurret_Inertia",
                    "animationsourcesticky": "CommanderGun_Inertia",
                    "gunnerdoor": "",
                    "stabilizedinaxes": 0,
                    "gunneraction": "RHS_M1A2_CommanderOUT",
                    "gunnerinaction": "RHS_M1A2_CommanderOUT",
                    "canhidegunner": 0,
                    "memorypointgunneroutoptics": "commander_out_view",
                    "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                    "soundattenuationturret": "HeliAttenuationGunner",
                    "disablesoundattenuation": 0,
                    "lodopticsin": 1200,
                    "lodopticsout": 1200,
                    "gunnerlefthandanimname": "handleL",
                    "gunnerrighthandanimname": "handleR",
                    "minelev": -8,
                    "maxelev": 30,
                    "minturn": -61,
                    "maxturn": 61,
                    "discretedistance": [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500],
                    "discretedistanceinitindex": 2,
                    "turretinfotype": "RHS_RscWeaponZeroing",
                    "weapons": ["RHS_M2_Abrams_Commander"],
                    "magazines": ["rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Red"],
                    "selectionfireanim": "zasleh3",
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderMG|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderMG|OpticsIn|Wide [Indent level: 6]
                        "wide": {
                            "visionmode": ["Normal"],
                            "initfov": 0.35,
                            "minfov": 0.35,
                            "maxfov": 0.35,
                            "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Commander_01_w_F.p3d",
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: Optics_Commander_01|Medium [Indent level: 0],
                        "medium": {
                            "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Commander_01_m_F.p3d",
                            "initfov": "(150 * 0.05625 / 120)",
                            "minfov": "(150 * 0.05625 / 120)",
                            "maxfov": "(150 * 0.05625 / 120)",
                            "visionmode": ["Normal","NVG","TI"],
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        },
                        # Class: Optics_Commander_01|Narrow [Indent level: 0],
                        "narrow": {
                            "gunneropticsmodel": "A3|Weapons_F|Reticle|Optics_Commander_01_n_F.p3d",
                            "initfov": "(60 * 0.05625 / 120)",
                            "minfov": "(60 * 0.05625 / 120)",
                            "maxfov": "(60 * 0.05625 / 120)",
                            "visionmode": ["Normal","NVG","TI"],
                            "thermalmode": [2,3],
                            "gunneropticseffect": [],
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
                            "maxmovez": 0
                        }
                    },
                    "gunnercompartments": "Compartment5",
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderMG|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderMG|HitPoints|HitTurretComM2 [Indent level: 6]
                        "hitturretcomm2": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "com_m2_turret",
                            "visual": "-",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25,
                            "isturret": 1
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderMG|HitPoints|HitGunComM2 [Indent level: 6],
                        "hitguncomm2": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "com_m2_gun",
                            "visual": "-",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25,
                            "isgun": 1
                        }
                    },
                    "maxhorizontalrotspeed": 1.3,
                    "maxverticalrotspeed": 0.48,
                    "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",1,1,30],
                    "soundservovertical": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",1,1,30],
                    "initelev": 0,
                    "initturn": 0,
                    "memorypointgun": "usti hlavne3",
                    "gunbeg": "usti hlavne3",
                    "gunend": "konec hlavne3",
                    "lodturnedout": 1200,
                    "memorypointgunneroptics": "CITV_view",
                    "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Commander_02_F",
                    "gunneroutforceoptics": 0,
                    "gunneropticseffect": [],
                    "gunnerhasflares": 1,
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
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
                        "thermalmode": [2,3],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "startengine": 0,
                    "viewgunnerinexternal": 1,
                    "outgunnermayfire": 1,
                    "ingunnermayfire": 1,
                    "canusescanners": 0,
                    "showcrewaim": 0,
                    "allowtablock": 0,
                    "gunnerforceoptics": 1,
                    "turretfollowfreelook": 2,
                    "usepip": 2,
                    "lodturnedin": 1100,
                    "viewgunnershadowamb": 0.5,
                    "viewgunnershadowdiff": 0.05,
                    "personturretaction": "vehicle_turnout_2",
                    "minoutelev": -10,
                    "maxoutelev": 25,
                    "initoutelev": 0,
                    "minoutturn": -95,
                    "maxoutturn": 95,
                    "initoutturn": 0,
                    # Class: CfgVehicles|MBT_01_base_F|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
                    "viewgunner": {
                        "initanglex": -10,
                        "initangley": 0,
                        "initfov": 0.9,
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
                    # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: VehicleSystemsTemplateLeftCommander|Components [Indent level: 0]
                            "components": {
                                # Class: VehicleSystemsTemplateLeftCommander|Components|VehicleDriverDisplay [Indent level: 1]
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateLeftCommander|Components|VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "left": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        },
                        # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: VehicleSystemsTemplateRightCommander|Components [Indent level: 0]
                            "components": {
                                # Class: VehicleSystemsTemplateRightCommander|Components|VehicleDriverDisplay [Indent level: 1]
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateRightCommander|Components|VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "right": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "proxytype": "CPCommander",
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "animationsourcehatch": "hatchCommander",
                    "animationsourcecamelev": "camElev",
                    "commanding": 2,
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
                    "gunnertype": "",
                    "soundelevation": ["",0.00316228,1],
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
                    "gunneropticsshowcursor": 0,
                    "gunnerfirealsoininternalcamera": 1,
                    "gunneroutfirealsoininternalcamera": 1,
                    "gunnerusespilotview": 0,
                    "castgunnershadow": 0,
                    "viewgunnershadow": 1,
                    "ejectdeadgunner": 0,
                    "hideweaponsgunner": 1,
                    "forcehidegunner": 0,
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
                    "forcenvg": 0,
                    "iscopilot": 0,
                    "caneject": 1,
                    "gunnerleftleganimname": "",
                    "gunnerrightleganimname": "",
                    "precisegetinout": 0,
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
                    }
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|LoaderMG [Indent level: 4],
                "loadermg": {
                    "proxyindex": 4,
                    "dontcreateai": 1,
                    "cantcreateai": 1,
                    "ispersonturret": 0,
                    "canhidegunner": 0,
                    "gunnername": "Loader MG",
                    "animationsourcebody": "LoaderTurret",
                    "animationsourcegun": "LoaderGun",
                    "memorypointgunneroutoptics": "loaderview",
                    "memorypointgunneroptics": "loaderview",
                    "gunnerlefthandanimname": "Loader_Gun",
                    "gunnerrighthandanimname": "Loader_Gun",
                    "animationsourcestickx": "LoaderTurret_Inertia",
                    "animationsourcesticky": "LoaderGun_Inertia",
                    "body": "LoaderTurret",
                    "gun": "LoaderGun",
                    "gunneraction": "RHS_M1A2_CommanderOUT",
                    "minturn": 48,
                    "maxturn": 140,
                    "lodopticsin": 1200,
                    "lodopticsout": 1200,
                    "selectionfireanim": "zasleh5",
                    "discretedistance": [100,200,300,400,500,600,700,800,900],
                    "discretedistanceinitindex": 2,
                    "turretinfotype": "RHS_RscWeaponZeroing",
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|LoaderMG|OpticsIn [Indent level: 5],
                    "opticsin": {
                    },
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|LoaderMG|ViewOptics [Indent level: 5],
                    "viewoptics": {
                        "initfov": 0.7,
                        "minfov": 0.25,
                        "maxfov": 1.1,
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "visionmode": ["Normal"],
                        "thermalmode": [2,3],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|LoaderMG|ViewGunner [Indent level: 5],
                    "viewgunner": {
                        "initfov": 0.7,
                        "minfov": 0.25,
                        "maxfov": 1.1,
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "visionmode": ["Normal"],
                        "thermalmode": [2,3],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    "weapons": ["rhs_weap_m240_abrams"],
                    "magazines": ["rhs_mag_762x51_M240_200","rhs_mag_762x51_M240_200","rhs_mag_762x51_M240_200"],
                    # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|LoaderMG|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|LoaderMG|HitPoints|HitTurretLoader [Indent level: 6]
                        "hitturretloader": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "LoaderTurret",
                            "visual": "-",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25,
                            "isturret": 1
                        },
                        # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|Turrets|LoaderMG|HitPoints|HitGunLoader [Indent level: 6],
                        "hitgunloader": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "LoaderGun",
                            "visual": "-",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.6,
                            "radius": 0.25,
                            "isgun": 1
                        }
                    },
                    "lockwhendriverout": 0,
                    "lodturnedout": 1200,
                    "stabilizedinaxes": 0,
                    "gunnerinaction": "RHS_M1A1_Loader_in",
                    "gunneroutforceoptics": 0,
                    "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
                    "ingunnermayfire": 1,
                    "outgunnermayfire": 1,
                    "memorypointgun": "usti hlavne5",
                    "gunbeg": "usti hlavne5",
                    "gunend": "konec hlavne5",
                    "soundattenuationturret": "HeliAttenuationGunner",
                    "disablesoundattenuation": 0,
                    "animationsourcehatch": "HatchGunner",
                    "commanding": -3,
                    "primaryobserver": 0,
                    "memorypointsgetingunner": "pos gunner",
                    "memorypointsgetingunnerdir": "pos gunner dir",
                    "soundservo": ["A3|sounds_f|dummysound",1e-006,1],
                    "gunnerdoor": "hatchL",
                    "maxhorizontalrotspeed": 1.3,
                    "maxverticalrotspeed": 0.48,
                    "soundservovertical": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_comm",1,1,30],
                    "minelev": -5,
                    "maxelev": 60,
                    "initelev": 0,
                    "initturn": 0,
                    "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Commander_02_F",
                    "gunneropticseffect": [],
                    "gunnerhasflares": 1,
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "startengine": 0,
                    "viewgunnerinexternal": 1,
                    "canusescanners": 0,
                    "showcrewaim": 0,
                    "allowtablock": 0,
                    "gunnerforceoptics": 1,
                    "turretfollowfreelook": 2,
                    "usepip": 2,
                    "lodturnedin": 1100,
                    "viewgunnershadowamb": 0.5,
                    "viewgunnershadowdiff": 0.05,
                    "personturretaction": "vehicle_turnout_2",
                    "minoutelev": -10,
                    "maxoutelev": 25,
                    "initoutelev": 0,
                    "minoutturn": -95,
                    "maxoutturn": 95,
                    "initoutturn": 0,
                    # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: VehicleSystemsTemplateLeftCommander|Components [Indent level: 0]
                            "components": {
                                # Class: VehicleSystemsTemplateLeftCommander|Components|VehicleDriverDisplay [Indent level: 1]
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateLeftCommander|Components|VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "left": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        },
                        # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: VehicleSystemsTemplateRightCommander|Components [Indent level: 0]
                            "components": {
                                # Class: VehicleSystemsTemplateRightCommander|Components|VehicleDriverDisplay [Indent level: 1]
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateRightCommander|Components|VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "right": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "proxytype": "CPCommander",
                    "primarygunner": 0,
                    "animationsourcecamelev": "camElev",
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "gunnertype": "",
                    "soundelevation": ["",0.00316228,1],
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
                    "gunneropticsshowcursor": 0,
                    "gunnerfirealsoininternalcamera": 1,
                    "gunneroutfirealsoininternalcamera": 1,
                    "gunnerusespilotview": 0,
                    "castgunnershadow": 0,
                    "viewgunnershadow": 1,
                    "ejectdeadgunner": 0,
                    "hideweaponsgunner": 1,
                    "forcehidegunner": 0,
                    "showhmd": 0,
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
                    "gunnerleftleganimname": "",
                    "gunnerrightleganimname": "",
                    "precisegetinout": 0,
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
                    }
                }
            },
            "memorypointgun": "usti hlavne2",
            "selectionfireanim": "zaslehCoax",
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "weapons": ["rhs_weap_m256","rhs_weap_m240_abrams_coax","rhs_weap_fcs"],
            "magazines": ["rhs_mag_M829A3","rhs_mag_M830A1","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_mag_762x51_M240_1200","rhs_laserfcsmag","rhs_laserfcsmag"],
            "minelev": -10,
            "maxelev": 22,
            "initelev": 5,
            "maxhorizontalrotspeed": 0.7,
            "maxverticalrotspeed": 0.44,
            "turretinfotype": "RHS_RscWeaponM1_FCS",
            "discretedistance": [],
            "memorypointgunneroptics": "gunnerview",
            "gunneroutopticsmodel": "",
            "gunneroutopticseffect": [],
            "gunneropticseffect": [],
            "gunnerforceoptics": 1,
            # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|OpticsIn|Wide [Indent level: 4]
                "wide": {
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "initfov": 0.233333,
                    "minfov": 0.233333,
                    "maxfov": 0.233333,
                    "visionmode": ["Normal"],
                    "thermalmode": [2,3],
                    "gunneropticsmodel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2",
                    "gunneropticseffect": [],
                    "hitpoint": "Hit_Optic_GPS",
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|OpticsIn|Medium [Indent level: 4],
                "medium": {
                    "gunneropticsmodel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A1_2",
                    "initfov": 0.07,
                    "minfov": 0.07,
                    "maxfov": 0.07,
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "visionmode": ["Normal"],
                    "thermalmode": [2,3],
                    "gunneropticseffect": [],
                    "hitpoint": "Hit_Optic_GPS",
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|OpticsIn|Wide_TI [Indent level: 4],
                "wide_ti": {
                    "gunneropticsmodel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2_ti",
                    "visionmode": ["Ti"],
                    "initfov": 0.233333,
                    "minfov": 0.233333,
                    "maxfov": 0.233333,
                    "hitpoint": "Hit_Optic_GPS_TI",
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "thermalmode": [2,3],
                    "gunneropticseffect": [],
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|OpticsIn|Wide2_TI [Indent level: 4],
                "wide2_ti": {
                    "initfov": 0.116667,
                    "minfov": 0.116667,
                    "maxfov": 0.116667,
                    "gunneropticsmodel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2_ti",
                    "visionmode": ["Ti"],
                    "hitpoint": "Hit_Optic_GPS_TI",
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "thermalmode": [2,3],
                    "gunneropticseffect": [],
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|OpticsIn|Medium_TI [Indent level: 4],
                "medium_ti": {
                    "gunneropticsmodel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2_2",
                    "initfov": 0.0538462,
                    "minfov": 0.0538462,
                    "maxfov": 0.0538462,
                    "visionmode": ["Ti"],
                    "hitpoint": "Hit_Optic_GPS_TI",
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "thermalmode": [2,3],
                    "gunneropticseffect": [],
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|OpticsIn|Medium2_TI [Indent level: 4],
                "medium2_ti": {
                    "gunneropticsmodel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2_3",
                    "initfov": 0.028,
                    "minfov": 0.028,
                    "maxfov": 0.028,
                    "visionmode": ["Ti"],
                    "hitpoint": "Hit_Optic_GPS_TI",
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "thermalmode": [2,3],
                    "gunneropticseffect": [],
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|OpticsIn|Narrow_TI [Indent level: 4],
                "narrow_ti": {
                    "gunneropticsmodel": "rhsusf|addons|rhsusf_m1a1|gunnerOptics_M1A2_4",
                    "initfov": 0.014,
                    "minfov": 0.014,
                    "maxfov": 0.014,
                    "visionmode": ["Ti"],
                    "hitpoint": "Hit_Optic_GPS_TI",
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "thermalmode": [2,3],
                    "gunneropticseffect": [],
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
            "gunnerinaction": "RHS_M1A1_Gunner",
            "forcehidegunner": 1,
            "ingunnermayfire": 1,
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 0.2,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passthrough": 0,
                    "minimalhit": 0.34,
                    "explosionshielding": 0.001,
                    "radius": 0.18
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 0.3,
                    "material": -1,
                    "name": "zbran",
                    "armorcomponent": "Hit_Gun",
                    "visual": "-",
                    "passthrough": 0,
                    "minimalhit": 0.15,
                    "explosionshielding": 0,
                    "radius": 0.12
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|HitPoints|Hit_GPS_HeadMirror [Indent level: 4],
                "hit_gps_headmirror": {
                    "armor": -40,
                    "explosionshielding": 0,
                    "name": "",
                    "visual": "-",
                    "armorcomponent": "Hit_HeadMirror",
                    "passthrough": 0
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|HitPoints|Hit_GPS_Optical [Indent level: 4],
                "hit_gps_optical": {
                    "visual": "vis_optic_GPS",
                    "armorcomponent": "Hit_Optic_GPS",
                    "armor": -40,
                    "explosionshielding": 0,
                    "name": "",
                    "passthrough": 0
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|HitPoints|Hit_GPS_TIS [Indent level: 4],
                "hit_gps_tis": {
                    "visual": "vis_optic_GPS_TI",
                    "armorcomponent": "Hit_Optic_GPS_TI",
                    "armor": -40,
                    "explosionshielding": 0,
                    "name": "",
                    "passthrough": 0
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|HitPoints|Hit_Optic_GPS [Indent level: 4],
                "hit_optic_gps": {
                    "visual": "-",
                    "armorcomponent": "-",
                    "depends": "Hit_GPS_HeadMirror max Hit_GPS_Optical",
                    "armor": -40,
                    "explosionshielding": 0,
                    "name": "",
                    "passthrough": 0
                },
                # Class: CfgVehicles|rhsusf_m1a2tank_base|Turrets|MainTurret|HitPoints|Hit_Optic_GPS_TI [Indent level: 4],
                "hit_optic_gps_ti": {
                    "visual": "-",
                    "armorcomponent": "-",
                    "depends": "Hit_GPS_HeadMirror max Hit_GPS_TIS",
                    "armor": -40,
                    "explosionshielding": 0,
                    "name": "",
                    "passthrough": 0
                }
            },
            "lockwhendriverout": 1,
            "animationsourcehatch": "",
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Turrets|MainTurret|TurnIn [Indent level: 3],
            "turnin": {
                "limitsarraytop": [[22,-180],[22,180]],
                "limitsarraybottom": [[1.4,-180],[0.7,-134.687],[-9.3683,-133.687],[-10,0],[-9.7173,133.637],[0.7,134.687],[1.4,180]]
            },
            "soundservo": ["rhsusf|addons|rhsusf_m1a1|sounds|traverse",15,1,20],
            "canusescanners": 0,
            "showcrewaim": 0,
            "allowtablock": 0,
            "memorypointsgetingunner": "pos commander",
            "memorypointsgetingunnerdir": "pos commander dir",
            "gunnerdoor": "hatchC",
            "startengine": 0,
            "lodturnedout": 0,
            # Class: CfgVehicles|MBT_01_base_F|Turrets|MainTurret|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initanglex": -17,
                "initangley": 0,
                "initfov": 0.9,
                "minfov": 0.25,
                "maxfov": 1.25,
                "minanglex": -65,
                "maxanglex": 85,
                "minangley": -150,
                "maxangley": 150,
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
            "usepip": 2,
            "lodturnedin": 1100,
            "lodopticsin": 0,
            "animationsourcestickx": "turret_control_x",
            "animationsourcesticky": "turret_control_y",
            "gunnerlefthandanimname": "turret_control_y",
            "gunnerrighthandanimname": "turret_control_y",
            "viewgunnershadowamb": 0.5,
            "viewgunnershadowdiff": 0.05,
            "gunnergetinaction": "GetInLow",
            "gunnergetoutaction": "GetOutLow",
            "soundservovertical": ["A3|Sounds_F|vehicles|armor|noises|servo_armor_gunner_vertical",0.158489,1,50],
            "discretedistanceinitindex": 5,
            "commanding": 1,
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "primarygunner": 1,
            # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: VehicleSystemsTemplateLeftGunner|Components [Indent level: 0]
                    "components": {
                        # Class: VehicleSystemsTemplateLeftGunner|Components|VehicleDriverDisplay [Indent level: 1]
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateLeftGunner|Components|VehicleCommanderDisplay [Indent level: 1],
                        "vehiclecommanderdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    # Class: VehicleSystemsTemplateRightGunner|Components [Indent level: 0]
                    "components": {
                        # Class: VehicleSystemsTemplateRightGunner|Components|VehicleDriverDisplay [Indent level: 1]
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateRightGunner|Components|VehicleCommanderDisplay [Indent level: 1],
                        "vehiclecommanderdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "body": "mainTurret",
            "gun": "mainGun",
            "animationsourcebody": "mainTurret",
            "animationsourcegun": "mainGun",
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
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
            "turretcansee": 0,
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
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "outgunnermayfire": 0,
            "showhmd": 0,
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
            }
        }
    },
    "hiddenselections": ["camo1","camo2","camo3","camo4","","","","n1","n2","n3","i1","i2","i3"],
    "hiddenselectionstextures": ["rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1a2_wd_01_co.paa","rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1a2_wd_02_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_03_co.paa","rhsusf|addons|rhsusf_m1a1|loaderspintle|data|loaderspintle_wd_co.paa"],
    # Class: CfgVehicles|rhsusf_m1a2tank_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhsusf_m1a2tank_base|textureSources|woodland [Indent level: 2]
        "woodland": {
            "displayname": "Woodland",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1a2_wd_01_co.paa","rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1a2_wd_02_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_03_co.paa","rhsusf|addons|rhsusf_m1a1|loaderspintle|data|loaderspintle_wd_co.paa"]
        },
        # Class: CfgVehicles|rhsusf_m1a2tank_base|textureSources|desert [Indent level: 2],
        "desert": {
            "displayname": "Desert",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1a2_d_01_co.paa","rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1a2_d_02_co.paa","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_d_03_co.paa","rhsusf|addons|rhsusf_m1a1|loaderspintle|data|loaderspintle_d_co.paa"]
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|rhsusf_m1a2tank_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aim_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_d_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aim_d_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_d_03.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_m1a1aim_t.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_dam_m1a1aim_t.rvmat","rhsusf|addons|rhsusf_m1a1|data|rhsusf_destr_m1a1aim_t.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1a2_d_01.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_dam_m1a2_d_01.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_destr_m1a2_d_01.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1a2_d_02.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_dam_m1a2_d_02.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_destr_m1a2_d_02.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1a2_wd_01.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_dam_m1a2_wd_01.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_destr_m1a2_wd_01.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1a2_wd_02.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_dam_m1a2_wd_02.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_destr_m1a2_wd_02.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_tuskia2_d.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_dam_tuskia2_d.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_destr_tuskia2_d.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_tuskia2_wd.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_dam_tuskia2_wd.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_destr_tuskia2_wd.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1slat_d.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_dam_m1slat_d.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_destr_m1slat_d.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_m1slat_wd.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_dam_m1slat_wd.rvmat","rhsusf|addons|rhsusf_m1a2|data|rhsusf_destr_m1slat_wd.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat","rhsusf|addons|rhsusf_m1a1|data|opticsglass.rvmat","rhsusf|addons|rhsusf_m1a1|data|opticsglass_damage.rvmat","rhsusf|addons|rhsusf_m1a1|data|opticsglass_damage.rvmat"]
    },
    # Class: CfgVehicles|rhsusf_m1a2tank_base|ViewOptics [Indent level: 1],
    "viewoptics": {
        "visionmode": ["Normal","NVG"],
        "thermalmode": [2,3],
        "initfov": 0.7,
        "minfov": 0.7,
        "maxfov": 0.7,
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
    # Class: CfgVehicles|rhsusf_m1a2tank_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhsusf_m1a2tank_base|AnimationSources|muzzle_rot_hmg2 [Indent level: 2]
        "muzzle_rot_hmg2": {
            "source": "ammorandom",
            "weapon": "rhs_M2_Abrams_Gunner"
        },
        # Class: CfgVehicles|rhsusf_m1a2tank_base|AnimationSources|reload2 [Indent level: 2],
        "reload2": {
            "source": "reload",
            "weapon": "RHS_M2_Abrams_Commander"
        },
        # Class: CfgVehicles|rhsusf_m1a2tank_base|AnimationSources|ReloadMagazine2 [Indent level: 2],
        "reloadmagazine2": {
            "source": "reloadmagazine",
            "weapon": "RHS_M2_Abrams_Commander"
        },
        # Class: CfgVehicles|rhsusf_m1a2tank_base|AnimationSources|Revolving2 [Indent level: 2],
        "revolving2": {
            "source": "revolving",
            "weapon": "RHS_M2_Abrams_Commander"
        },
        # Class: CfgVehicles|rhsusf_m1a2tank_base|AnimationSources|ObsTurret [Indent level: 2],
        "obsturret": {
            "source": "user",
            "animperiod": 1.5
        },
        # Class: CfgVehicles|rhsusf_m1a2tank_base|AnimationSources|ObsGun [Indent level: 2],
        "obsgun": {
            "source": "user",
            "animperiod": 7
        },
        # Class: CfgVehicles|rhsusf_m1a2tank_base|AnimationSources|Unhide_vis_optic_d_CITV [Indent level: 2],
        "unhide_vis_optic_d_citv": {
            "source": "hit",
            "hitpoint": "Hit_Optic_CITV"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|IFF_Panels_Hide [Indent level: 2],
        "iff_panels_hide": {
            "author": "Red Hammer Studios",
            "source": "user",
            "animperiod": 1e-005,
            "initphase": 0,
            "displayname": "hide IFF panels",
            "mass": -20
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|Miles_Hide [Indent level: 2],
        "miles_hide": {
            "author": "Red Hammer Studios",
            "displayname": "hide MILES panels",
            "source": "user",
            "animperiod": 1e-005,
            "initphase": 0,
            "mass": -20
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|muzzle_rot_CoaxMG [Indent level: 2],
        "muzzle_rot_coaxmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m240_abrams_coax"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "RHS_M2_Abrams_Commander"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|muzzle_rot_cannon [Indent level: 2],
        "muzzle_rot_cannon": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m256"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|recoil_source [Indent level: 2],
        "recoil_source": {
            "source": "reload",
            "weapon": "rhs_weap_m256"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|reload1 [Indent level: 2],
        "reload1": {
            "source": "reload",
            "weapon": "rhs_weap_m240_abrams"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|ReloadMagazine1 [Indent level: 2],
        "reloadmagazine1": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_m240_abrams"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|Revolving1 [Indent level: 2],
        "revolving1": {
            "source": "revolving",
            "weapon": "rhs_weap_m240_abrams"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|smoke_revolving_source [Indent level: 2],
        "smoke_revolving_source": {
            "source": "revolving",
            "weapon": "rhsusf_weap_M250"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|muzzle_hide_cannon [Indent level: 2],
        "muzzle_hide_cannon": {
            "source": "reload",
            "weapon": "rhs_weap_m256"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|elev [Indent level: 2],
        "elev": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|elev_bank [Indent level: 2],
        "elev_bank": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|lead [Indent level: 2],
        "lead": {
            "source": "user",
            "animperiod": 0.001
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|offset [Indent level: 2],
        "offset": {
            "source": "user",
            "animperiod": 0.0002
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|HatchC [Indent level: 2],
        "hatchc": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|HatchL [Indent level: 2],
        "hatchl": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|HatchD [Indent level: 2],
        "hatchd": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|Unhide_vis_optic_d_ComCWSS [Indent level: 2],
        "unhide_vis_optic_d_comcwss": {
            "source": "hit",
            "hitpoint": "Hit_Optic_ComCWSS"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|Unhide_vis_optic_d_ComM2 [Indent level: 2],
        "unhide_vis_optic_d_comm2": {
            "source": "hit",
            "hitpoint": "Hit_Optic_ComM2"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|Unhide_vis_optic_d_ComPeriscope [Indent level: 2],
        "unhide_vis_optic_d_comperiscope": {
            "source": "hit",
            "hitpoint": "Hit_Optic_ComPeriscope"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|Unhide_vis_optic_d_GPS [Indent level: 2],
        "unhide_vis_optic_d_gps": {
            "source": "hit",
            "hitpoint": "Hit_Optic_GPS"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|Unhide_vis_optic_d_GPS_TI [Indent level: 2],
        "unhide_vis_optic_d_gps_ti": {
            "source": "hit",
            "hitpoint": "Hit_Optic_GPS_TI"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|Unhide_vis_optic_d_Driver [Indent level: 2],
        "unhide_vis_optic_d_driver": {
            "source": "hit",
            "hitpoint": "Hit_Optic_Driver"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|AnimationSources|Unhide_vis_optic_d_LoaderPeriscope [Indent level: 2],
        "unhide_vis_optic_d_loaderperiscope": {
            "source": "hit",
            "hitpoint": "Hit_Optic_LoaderPeriscope"
        }
    },
    # Class: CfgVehicles|rhsusf_m1a2tank_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhsusf_m1a2tank_base|UserActions|trunk_open [Indent level: 2]
        "trunk_open": {
            "displayname": "Use M2",
            "position": "trunk_action",
            "radius": 4,
            "onlyforplayer": 0,
            "shortcut": "turnOut",
            "condition": "this animationPhase 'HatchCommander1'>0.5 and ((call rhsusf_fnc_findPlayer) == commander this)",
            "statement": "(call rhsusf_fnc_findPlayer) action ['moveToTurret', this, [0,2]];[this,[[0,0],true]] remoteExecCall ['lockTurret']"
        },
        # Class: CfgVehicles|rhsusf_m1a2tank_base|UserActions|trunk_close [Indent level: 2],
        "trunk_close": {
            "displayname": "Leave M2",
            "shortcut": "turnIn",
            "condition": "vehicle (call rhsusf_fnc_findPlayer) turretUnit [0,2] == (call rhsusf_fnc_findPlayer)",
            "statement": "(call rhsusf_fnc_findPlayer) action ['moveToTurret', this, [0,0]];[this,[[0,0],false]] remoteExecCall ['lockTurret']",
            "position": "trunk_action",
            "radius": 4,
            "onlyforplayer": 0
        },
        # Class: CfgVehicles|rhsusf_m1a2tank_base|UserActions|LoaderGun_Use [Indent level: 2],
        "loadergun_use": {
            "displayname": "Use M240",
            "position": "",
            "radius": 4,
            "onlyforplayer": 0,
            "shortcut": "turnOut",
            "condition": "this animationPhase 'HatchGunner'>0.5 and ((call rhsusf_fnc_findPlayer) == this turretUnit [0,1])",
            "statement": "(call rhsusf_fnc_findPlayer) action ['moveToTurret', this, [0,3]];[this,[[0,1],true]] remoteExecCall ['lockTurret']"
        },
        # Class: CfgVehicles|rhsusf_m1a2tank_base|UserActions|LoaderGun_Leave [Indent level: 2],
        "loadergun_leave": {
            "displayname": "Leave M240",
            "condition": "vehicle (call rhsusf_fnc_findPlayer) turretUnit [0,3] == (call rhsusf_fnc_findPlayer)",
            "shortcut": "turnIn",
            "statement": "(call rhsusf_fnc_findPlayer) action ['moveToTurret', this, [0,1]];[this,[[0,1],false]] remoteExecCall ['lockTurret']",
            "position": "",
            "radius": 4,
            "onlyforplayer": 0
        }
    },
    # Class: CfgVehicles|rhsusf_m1a2tank_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhsusf_m1a2tank_base|EventHandlers|RHSUSF_EventHandlers [Indent level: 2]
        "rhsusf_eventhandlers": {
            "getout": "_this call rhs_fnc_M1_hatch",
            "init": "_this call RHS_fnc_M1_init",
            "engine": "[_this select 0,_this select 1,20] call rhs_fnc_engineStartupDelay"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    # Class: CfgVehicles|rhsusf_m1a2tank_base|Sounds [Indent level: 1],
    "sounds": {
        "soundsetsext": ["RHSUSF_Abrams_ext_idle_SoundSet","RHSUSF_Abrams_ext_slow_SoundSet","RHSUSF_Abrams_ext_mid_SoundSet","RHSUSF_Abrams_ext_fast_SoundSet","RHSUSF_Abrams_exhaust_ext_idle_SoundSet","RHSUSF_Abrams_exhaust_ext_slow_SoundSet","RHSUSF_Abrams_exhaust_ext_mid_SoundSet","RHSUSF_Abrams_exhaust_ext_fast_SoundSet","RHSUSF_Abrams_ext_acce_soundSet","RHSUSF_Abrams_ext_acce_high_soundSet","RHSUSF_Abrams_dist_slow_SoundSet","RHSUSF_Abrams_dist_mid_SoundSet","RHSUSF_Abrams_dist_high_SoundSet","RHSUSF_Abrams_ext_tracks_slow_soundSet","RHSUSF_Abrams_ext_tracks_mid_soundSet","RHSUSF_Abrams_ext_tracks_fast_soundSet","RHSUSF_Abrams_ext_rumble_soundSet","RHSUSF_Abrams_ext_rain_soundSet","RHSUSF_trackSurfaceSound_ext_soft_soundSet","RHSUSF_trackSurfaceSound_ext_hard_soundSet","RHSUSF_trackSurfaceSound_ext_sand_soundSet"],
        "soundsetsint": ["RHSUSF_Abrams_int_idle_SoundSet","RHSUSF_Abrams_int_slow_SoundSet","RHSUSF_Abrams_int_mid_SoundSet","RHSUSF_Abrams_int_fast_SoundSet","RHSUSF_Abrams_int_acce_soundSet","RHSUSF_Abrams_exhaust_int_idle_SoundSet","RHSUSF_Abrams_exhaust_int_slow_SoundSet","RHSUSF_Abrams_exhaust_int_mid_SoundSet","RHSUSF_Abrams_exhaust_int_fast_SoundSet","RHSUSF_tankRattling_1_soundSet","RHSUSF_Abrams_int_rain_soundSet","RHSUSF_Abrams_ext_tracks_slow_soundSet","RHSUSF_Abrams_ext_tracks_mid_soundSet","RHSUSF_Abrams_ext_tracks_fast_soundSet","RHSUSF_Abrams_ext_rumble_soundSet","RHSUSF_int_breakingStrain_soundSet","RHSUSF_curveStress_1_soundSet"]
    },
    "category": "Armored",
    "destrtype": "DestructDefault",
    "unitinfotype": "RHSUSF_RscUnitInfoWestTank",
    "driveropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhs_m1_triplex",
    "getinaction": "GetInLow",
    "getoutaction": "GetOutLow",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "cargoaction": ["passenger_flatground_leanleft"],
    "transportsoldier": 0,
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "simulation": "tankX",
    "normalspeedforwardcoef": 0.6,
    "slowspeedforwardcoef": 0.45,
    "fuelcapacity": 20,
    "maxspeed": 66,
    "tankturnforce": 750000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.72,
    "accelaidforcecoef": 3.5,
    "accelaidforceyoffset": -3,
    "accelaidforcespd": 2.83,
    "maxfordingdepth": 0,
    "waterresistance": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "torquecurve": [[0.333333,1],[1,0.701027]],
    "enginemoi": 15,
    "enginepower": 1120,
    "peaktorque": 5355,
    "minomega": 100,
    "maxomega": 314.16,
    "idlerpm": 1000,
    "redrpm": 3000,
    "antirollbarforcecoef": 24,
    "antirollbarforcelimit": 42,
    "antirollbarspeedmin": 30,
    "antirollbarspeedmax": 75,
    "thrustdelay": 0,
    "clutchstrength": 35,
    "enginelosses": 25,
    "transmissionlosses": 15,
    "latency": 1.3,
    "switchtime": 0,
    "changegeartype": "rpmratio",
    "changegearomegaratios": [1,0.333333,0.333333,0,0.993333,0.333333,0.993333,0.633333,0.983333,0.733333,0.983333,0.766667,0.983333,0.733333],
    # Class: CfgVehicles|rhsusf_m1a1tank_base|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-1.67,"N",0,"D1",4.85,"D2",2.65,"D3",1.48,"D4",1,"D5",0.79],
        "transmissionratios": ["High",12],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.1
    },
    # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|L2 [Indent level: 2]
        "l2": {
            "susptraveldirection": [-0.125,-1,0],
            "bonename": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|L3 [Indent level: 2],
        "l3": {
            "bonename": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|L4 [Indent level: 2],
        "l4": {
            "bonename": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|L5 [Indent level: 2],
        "l5": {
            "bonename": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|L6 [Indent level: 2],
        "l6": {
            "bonename": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|L7 [Indent level: 2],
        "l7": {
            "bonename": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|L8 [Indent level: 2],
        "l8": {
            "bonename": "wheel_podkolol7",
            "center": "wheel_1_8_axis",
            "boundary": "wheel_1_8_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|L9 [Indent level: 2],
        "l9": {
            "bonename": "wheel_podkolol9",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|L1 [Indent level: 2],
        "l1": {
            "bonename": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|R2 [Indent level: 2],
        "r2": {
            "susptraveldirection": [0.125,-1,0],
            "bonename": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|R3 [Indent level: 2],
        "r3": {
            "bonename": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|R4 [Indent level: 2],
        "r4": {
            "bonename": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|R5 [Indent level: 2],
        "r5": {
            "bonename": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|R6 [Indent level: 2],
        "r6": {
            "bonename": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|R7 [Indent level: 2],
        "r7": {
            "bonename": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|R8 [Indent level: 2],
        "r8": {
            "bonename": "wheel_podkolop7",
            "center": "wheel_2_8_axis",
            "boundary": "wheel_2_8_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|R9 [Indent level: 2],
        "r9": {
            "bonename": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Wheels|R1 [Indent level: 2],
        "r1": {
            "bonename": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.477,
            "mass": 150,
            "moi": 10.83,
            "maxbraketorque": 9000,
            "sprungmass": 4642.86,
            "springstrength": 584000,
            "springdamperrate": 15000,
            "dampingrate": 205,
            "dampingrateinair": 205,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 60000,
            "frictionvsslipgraph": [[0,0.75],[0.18,1],[0.7,0.5]]
        }
    },
    "soundengineonint": ["rhsusf|addons|rhsusf_m1a1|sounds|m1start",1.41254,1,200],
    "soundengineoffint": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_int_stop",1.41254,1,200],
    "soundengineonext": ["rhsusf|addons|rhsusf_m1a1|sounds|m1start",3.16228,1,200],
    "soundengineoffext": ["rhsusf|addons|rhsusf_m1a1|sounds|ABRAMS_engine_ext_stop",3.16228,1,200],
    "driveoncomponent": ["Track_L","Track_R","slide"],
    "tracksspeed": -1.35,
    "wheelcircumference": 2.375,
    "attenuationeffecttype": "TankAttenuation",
    "extcameraposition": [0,2,-11],
    "reportownposition": 1,
    "dustfrontleftpos": "wheel_1_4_bound",
    "dustfrontrightpos": "wheel_2_4_bound",
    "dustbackleftpos": "wheel_1_7_bound",
    "dustbackrightpos": "wheel_2_7_bound",
    "cost": 1.5e+006,
    "damageresistance": 0.02,
    "crewvulnerable": 0,
    "incomingmissiledetectionsystem": 0,
    "driveraction": "driver_apcwheeled2_out",
    "driverinaction": "RHS_M1A1_Driver",
    "driverdoor": "hatchD",
    "forcehidedriver": 0,
    "driverforceoptics": 1,
    "loddriverturnedin": 0,
    "loddriverturnedout": 0,
    "loddriveropticsin": 0,
    "viewdriverinexternal": 1,
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
    "armor": 600,
    "armorstructural": 400,
    "explosionshielding": 150,
    "crewexplosionprotection": 1,
    "mintotaldamagethreshold": 0.5,
    # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|Armor_Composite_40 [Indent level: 2]
        "armor_composite_40": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_40_Hit",
            "armorcomponent": "Armor_CE_40",
            "simulation": "RHS_Composite_40",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|Armor_Composite_50 [Indent level: 2],
        "armor_composite_50": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_50_Hit",
            "armorcomponent": "Armor_CE_50",
            "simulation": "RHS_Composite_50",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|Armor_Composite_60 [Indent level: 2],
        "armor_composite_60": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_60_Hit",
            "armorcomponent": "Armor_CE_60",
            "simulation": "RHS_Composite_60",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|Armor_Composite_80 [Indent level: 2],
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
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|Armor_Composite_85 [Indent level: 2],
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
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitFuelTank_Left [Indent level: 2],
        "hitfueltank_left": {
            "armor": -80,
            "material": -1,
            "name": "Hit_FuelTank_Left",
            "armorcomponent": "Hit_FuelTank_Left",
            "visual": "-",
            "passthrough": 0,
            "minimalhit": -0.2,
            "explosionshielding": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitFuelTank_Right [Indent level: 2],
        "hitfueltank_right": {
            "name": "Hit_FuelTank_Right",
            "armorcomponent": "Hit_FuelTank_Right",
            "armor": -80,
            "material": -1,
            "visual": "-",
            "passthrough": 0,
            "minimalhit": -0.2,
            "explosionshielding": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 999,
            "material": -1,
            "name": "Hit_Fuel",
            "visual": "-",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.01,
            "depends": "(HitFuelTank_Left+HitFuelTank_Right)*0.5"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitAmmoHull [Indent level: 2],
        "hitammohull": {
            "name": "Hit_AmmoHull",
            "armorcomponent": "Hit_AmmoHull",
            "armor": -100,
            "material": -1,
            "passthrough": 0,
            "minimalhit": 0.14,
            "explosionshielding": 0,
            "radius": 0.15
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitAmmo [Indent level: 2],
        "hitammo": {
            "name": "Hit_Ammo",
            "armorcomponent": "Hit_AmmoTurret",
            "armor": -100,
            "material": -1,
            "passthrough": 0,
            "minimalhit": 0.14,
            "explosionshielding": 0,
            "radius": 0.15
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitHull [Indent level: 2],
        "hithull": {
            "armor": 0.8,
            "material": -1,
            "name": "Hit_Hull",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.14,
            "explosionshielding": 0,
            "radius": 0.21,
            "depends": "(HitAmmo factor [0.9,1])+(HitAmmoHull factor [0.9,1])",
            "armorcomponent": "hit_hull"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": -100,
            "material": -1,
            "name": "Hit_Engine",
            "armorcomponent": "Hit_Engine",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.14,
            "explosionshielding": 0.01,
            "radius": 0.18,
            # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "rhs_engine_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire [Indent level: 4],
                "rhs_engine_fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks [Indent level: 4],
                "rhs_engine_sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "rhs_engine_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "rhs_engine_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
                "rhs_engine_smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small3 [Indent level: 4],
                "rhs_engine_smoke_small3": {
                    "position": "engine_smoke4",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                }
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitLTrack [Indent level: 2],
        "hitltrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackL",
            "name": "Hit_TrackL",
            "passthrough": 0,
            "material": -1,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "visual": "-"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|HitRTrack [Indent level: 2],
        "hitrtrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackR",
            "name": "Hit_TrackR",
            "material": -1,
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "visual": "-"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|Hit_Optic_Driver [Indent level: 2],
        "hit_optic_driver": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optic_Driver",
            "armorcomponent": "Hit_Optic_Driver",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|Hit_Optic_DVEA [Indent level: 2],
        "hit_optic_dvea": {
            "visual": "vis_optic_DVEA",
            "armorcomponent": "Hit_Optic_DVEA",
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|HitPoints|Hit_Optic_Driver_Rear [Indent level: 2],
        "hit_optic_driver_rear": {
            "visual": "vis_optic_Driver_Rear",
            "armorcomponent": "Hit_Optic_Driver_Rear",
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "passthrough": 0
        }
    },
    # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportBackpacks|_xx_rhsusf_falconii [Indent level: 2]
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 4
        }
    },
    # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 30
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhsusf_mag_7x45acp_MHP [Indent level: 2],
        "_xx_rhsusf_mag_7x45acp_mhp": {
            "magazine": "rhsusf_mag_7x45acp_MHP",
            "count": 3
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhsusf_mag_15Rnd_9x19_FMJ [Indent level: 2],
        "_xx_rhsusf_mag_15rnd_9x19_fmj": {
            "magazine": "rhsusf_mag_15Rnd_9x19_FMJ",
            "count": 12
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 10
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhsusf_100Rnd_762x51 [Indent level: 2],
        "_xx_rhsusf_100rnd_762x51": {
            "magazine": "rhsusf_100Rnd_762x51",
            "count": 5
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhs_M136_mag [Indent level: 2],
        "_xx_rhs_m136_mag": {
            "magazine": "rhs_M136_mag",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhs_mag_m18_purple [Indent level: 2],
        "_xx_rhs_mag_m18_purple": {
            "magazine": "rhs_mag_m18_purple",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhs_mag_m18_yellow [Indent level: 2],
        "_xx_rhs_mag_m18_yellow": {
            "magazine": "rhs_mag_m18_yellow",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportMagazines|_xx_rhs_mine_M19_mag [Indent level: 2],
        "_xx_rhs_mine_m19_mag": {
            "magazine": "rhs_mine_M19_mag",
            "count": 2
        }
    },
    # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 8
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportWeapons [Indent level: 1],
    "transportweapons": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportWeapons|_xx_rhs_weap_m4_carryhandle [Indent level: 2]
        "_xx_rhs_weap_m4_carryhandle": {
            "weapon": "rhs_weap_m4_carryhandle",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|TransportWeapons|_xx_rhs_weap_M136 [Indent level: 2],
        "_xx_rhs_weap_m136": {
            "weapon": "rhs_weap_M136",
            "count": 2
        }
    },
    # Class: CfgVehicles|rhsusf_m1a1tank_base|DriverOpticsIn [Indent level: 1],
    "driveropticsin": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|DriverOpticsIn|Wide [Indent level: 2]
        "wide": {
            "campos": "view_driver",
            "opticsmodel": "rhsusf|addons|rhsusf_optics|data|rhs_m1_triplex",
            "visionmode": ["Normal"],
            "hitpoint": "Hit_Optic_Driver",
            "thermalmode": [2,3],
            "initfov": 0.7,
            "minfov": 0.7,
            "maxfov": 0.7,
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
        # Class: CfgVehicles|rhsusf_m1a1tank_base|DriverOpticsIn|DVE_Wide [Indent level: 2],
        "dve_wide": {
            "opticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_DVE_4x3",
            "visionmode": ["TI"],
            "initfov": 1.07692,
            "minfov": 1.07692,
            "maxfov": 1.07692,
            "hitpoint": "Hit_Optic_DVEA",
            "campos": "view_driver",
            "thermalmode": [2,3],
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
        # Class: CfgVehicles|rhsusf_m1a1tank_base|DriverOpticsIn|DVS_Rear [Indent level: 2],
        "dvs_rear": {
            "opticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_DVE2_4x3",
            "campos": "view_rear",
            "camdir": "view_rear_dir",
            "hitpoint": "Hit_Optic_Driver_Rear",
            "visionmode": ["TI"],
            "initfov": 1.07692,
            "minfov": 1.07692,
            "maxfov": 1.07692,
            "thermalmode": [2,3],
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
    # Class: CfgVehicles|rhsusf_m1a1tank_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaustL1",
            "direction": "exhaustL_Dir",
            "effect": "RHS_ExhaustEffectTankGasBack"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Exhausts|Exhaust1L [Indent level: 2],
        "exhaust1l": {
            "position": "exhaustL2",
            "direction": "exhaustL_Dir",
            "effect": "RHS_ExhaustEffectTankGasBack"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "exhaustR1",
            "direction": "exhaustR_Dir",
            "effect": "RHS_ExhaustEffectTankGasBack"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Exhausts|Exhaust2R [Indent level: 2],
        "exhaust2r": {
            "position": "exhaustR2",
            "direction": "exhaustR_Dir",
            "effect": "RHS_ExhaustEffectTankGasBack"
        }
    },
    # Class: CfgVehicles|rhsusf_m1a1tank_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Reflectors|Left [Indent level: 2]
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
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Reflectors|Right [Indent level: 2],
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
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Reflectors|Right2 [Indent level: 2],
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
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Reflectors|Left2 [Indent level: 2],
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
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Reflectors|Left|Attenuation [Indent level: 3],
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
    "aggregatereflectors": [["Left","Left2"],["Right","Right2"]],
    "armorlights": 0.01,
    # Class: CfgVehicles|rhsusf_m1a1tank_base|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|RenderTargets|driverView1 [Indent level: 2]
        "driverview1": {
            "rendertarget": "rendertarget1",
            # Class: CfgVehicles|rhsusf_m1a1tank_base|RenderTargets|driverView1|Camera [Indent level: 3],
            "camera": {
                "pointposition": "dVis1P",
                "pointdirection": "dVis1D",
                "rendervisionmode": 0,
                "renderquality": 4,
                "fov": 0.5
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|RenderTargets|driverView2 [Indent level: 2],
        "driverview2": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|rhsusf_m1a1tank_base|RenderTargets|driverView2|Camera [Indent level: 3],
            "camera": {
                "pointposition": "dVis2P",
                "pointdirection": "dVis2D",
                "rendervisionmode": 0,
                "renderquality": 4,
                "fov": 0.5
            }
        }
    },
    # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_hideIFFPanel [Indent level: 2],
        "rhs_hideiffpanel": {
            "displayname": "Hide IFF Panel",
            "property": "rhs_hideIFFPanel",
            "control": "CheckboxNumber",
            "expression": "_this animate ['IFF_Panels_Hide',_value,true]",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_hideMiles [Indent level: 2],
        "rhs_hidemiles": {
            "displayname": "Hide Miles Panel",
            "property": "rhs_hideMiles",
            "control": "CheckboxNumber",
            "expression": "_this animate ['Miles_Hide',_value,true]",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalBarrel_type [Indent level: 2],
        "rhs_decalbarrel_type": {
            "displayname": "Define type of barrel art",
            "tooltip": "Define type of barrel art. You can choose between desert & Woodland variants",
            "property": "rhs_decalBarrel_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalBarrel_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalBarrel_type|values|BarrelArt_Abrams_D [Indent level: 4]
                "barrelart_abrams_d": {
                    "name": "Desert",
                    "value": "BarrelArt_Abrams_D",
                    "defaultvalue": "BarrelArt_Abrams_D"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalBarrel_type|values|BarrelArt_Abrams_WD [Indent level: 4],
                "barrelart_abrams_wd": {
                    "name": "Woodland",
                    "value": "BarrelArt_Abrams_WD"
                }
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalBarrel [Indent level: 2],
        "rhs_decalbarrel": {
            "displayname": "Define barrel art",
            "tooltip": "Define barrel art. Available numbers from 0 to 55, type number above 55 to clear that place",
            "property": "rhs_decalBarrel",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cM1BarrelSymPlaces,  _this getVariable ['rhs_decalBarrel_type','BarrelArt_Abrams_WD'],_value] ] ] call rhsusf_fnc_decalsInit;};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon_type [Indent level: 2],
        "rhs_decalplatoon_type": {
            "displayname": "Define type of platoon symbol",
            "tooltip": "Define type of platoon symbol. You can choose between desert & Woodland variants",
            "property": "rhs_decalPlatoon_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon_type|values|ArmyPlt_Abrams_D [Indent level: 4]
                "armyplt_abrams_d": {
                    "name": "Desert",
                    "value": "ArmyPlt_Abrams_D",
                    "defaultvalue": "ArmyPlt_Abrams_D"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon_type|values|ArmyPlt_Abrams_WD [Indent level: 4],
                "armyplt_abrams_wd": {
                    "name": "Woodland",
                    "value": "ArmyPlt_Abrams_WD"
                }
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon [Indent level: 2],
        "rhs_decalplatoon": {
            "displayname": "Define platoon symbol",
            "tooltip": "Define platoon symbol",
            "property": "rhs_decalPlatoon",
            "control": "Combo",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cM1PlnSymPlaces,  _this getVariable ['rhs_decalPlatoon_type','ArmyPlt_Abrams_D'],_value] ] ] call rhsusf_fnc_decalsInit};",
            "defaultvalue": "-1",
            "typename": "Number",
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Random [Indent level: 4]
                "random": {
                    "name": "Random",
                    "value": -1,
                    "defaultvalue": -1
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0,
                    "defaultvalue": 0
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting1 [Indent level: 4],
                "setting1": {
                    "name": "1st Platoon, 1st Vehicle",
                    "value": 1,
                    "defaultvalue": 1
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting2 [Indent level: 4],
                "setting2": {
                    "name": "1st Platoon, 2nd Vehicle",
                    "value": 2,
                    "defaultvalue": 2
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting3 [Indent level: 4],
                "setting3": {
                    "name": "1st Platoon, 3rd Vehicle",
                    "value": 3,
                    "defaultvalue": 3
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting4 [Indent level: 4],
                "setting4": {
                    "name": "1st Platoon, 4th Vehicle",
                    "value": 4,
                    "defaultvalue": 4
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting5 [Indent level: 4],
                "setting5": {
                    "name": "2nd Platoon, 1st Vehicle",
                    "value": 5,
                    "defaultvalue": 5
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting6 [Indent level: 4],
                "setting6": {
                    "name": "2nd Platoon, 2nd Vehicle",
                    "value": 6,
                    "defaultvalue": 6
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting7 [Indent level: 4],
                "setting7": {
                    "name": "2nd Platoon, 3rd Vehicle",
                    "value": 7,
                    "defaultvalue": 7
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting8 [Indent level: 4],
                "setting8": {
                    "name": "2nd Platoon, 4th Vehicle",
                    "value": 8,
                    "defaultvalue": 8
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting9 [Indent level: 4],
                "setting9": {
                    "name": "3rd Platoon, 1st Vehicle",
                    "value": 9,
                    "defaultvalue": 9
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting10 [Indent level: 4],
                "setting10": {
                    "name": "3rd Platoon, 2nd Vehicle",
                    "value": 10,
                    "defaultvalue": 10
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting11 [Indent level: 4],
                "setting11": {
                    "name": "3rd Platoon, 3rd Vehicle",
                    "value": 11,
                    "defaultvalue": 11
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_decalPlatoon|values|Setting12 [Indent level: 4],
                "setting12": {
                    "name": "3rd Platoon, 4th Vehicle",
                    "value": 12,
                    "defaultvalue": 12
                }
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type [Indent level: 2],
        "rhs_ammoslot_1_type": {
            "displayname": "Ammo slot #1 type",
            "tooltip": "Define type of shell for #1 slot",
            "property": "rhs_ammoslot_1_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829A3 [Indent level: 4]
                "rhs_mag_m829a3": {
                    "name": "M829A3 APFSDS-T",
                    "value": "rhs_mag_M829A3",
                    "defaultvalue": "rhs_mag_M829A3"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829A2 [Indent level: 4],
                "rhs_mag_m829a2": {
                    "name": "M829A2 APFSDS-T",
                    "value": "rhs_mag_M829A2"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829A1 [Indent level: 4],
                "rhs_mag_m829a1": {
                    "name": "M829A1 APFSDS-T",
                    "value": "rhs_mag_M829A1"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829 [Indent level: 4],
                "rhs_mag_m829": {
                    "name": "M829 APFSDS-T",
                    "value": "rhs_mag_M829"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M830 [Indent level: 4],
                "rhs_mag_m830": {
                    "name": "M830 HEAT-FS",
                    "value": "rhs_mag_M830"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M830A1 [Indent level: 4],
                "rhs_mag_m830a1": {
                    "name": "M830A1 MPAT",
                    "value": "rhs_mag_M830A1"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M1028 [Indent level: 4],
                "rhs_mag_m1028": {
                    "name": "M1028 Canister",
                    "value": "rhs_mag_M1028"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M1147 [Indent level: 4],
                "rhs_mag_m1147": {
                    "name": "M1147 HE-FRAG",
                    "value": "rhs_mag_M1147"
                }
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1 [Indent level: 2],
        "rhs_ammoslot_1": {
            "displayname": "Ammo slot #1 count",
            "tooltip": "Define number of rounds stored inside of type #1. Max 36. Leave -1 for default loadout",
            "property": "rhs_ammoslot_1",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s'] spawn rhs_fnc_m1_defineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_2_type [Indent level: 2],
        "rhs_ammoslot_2_type": {
            "displayname": "Ammo slot #2 type",
            "tooltip": "Define type of shell for #2 slot",
            "property": "rhs_ammoslot_2_type",
            "defaultvalue": "0",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "typename": "STRING",
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829A3 [Indent level: 4]
                "rhs_mag_m829a3": {
                    "name": "M829A3 APFSDS-T",
                    "value": "rhs_mag_M829A3",
                    "defaultvalue": "rhs_mag_M829A3"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829A2 [Indent level: 4],
                "rhs_mag_m829a2": {
                    "name": "M829A2 APFSDS-T",
                    "value": "rhs_mag_M829A2"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829A1 [Indent level: 4],
                "rhs_mag_m829a1": {
                    "name": "M829A1 APFSDS-T",
                    "value": "rhs_mag_M829A1"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829 [Indent level: 4],
                "rhs_mag_m829": {
                    "name": "M829 APFSDS-T",
                    "value": "rhs_mag_M829"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M830 [Indent level: 4],
                "rhs_mag_m830": {
                    "name": "M830 HEAT-FS",
                    "value": "rhs_mag_M830"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M830A1 [Indent level: 4],
                "rhs_mag_m830a1": {
                    "name": "M830A1 MPAT",
                    "value": "rhs_mag_M830A1"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M1028 [Indent level: 4],
                "rhs_mag_m1028": {
                    "name": "M1028 Canister",
                    "value": "rhs_mag_M1028"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M1147 [Indent level: 4],
                "rhs_mag_m1147": {
                    "name": "M1147 HE-FRAG",
                    "value": "rhs_mag_M1147"
                }
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_2 [Indent level: 2],
        "rhs_ammoslot_2": {
            "displayname": "Ammo slot #2 count",
            "tooltip": "Define number of rounds stored inside of type #2. Max 36. Leave -1 for default loadout",
            "property": "rhs_ammoslot_2",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s'] spawn rhs_fnc_m1_defineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_3_type [Indent level: 2],
        "rhs_ammoslot_3_type": {
            "displayname": "Ammo slot #3 type",
            "tooltip": "Define type of shell for #3 slot",
            "property": "rhs_ammoslot_3_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829A3 [Indent level: 4]
                "rhs_mag_m829a3": {
                    "name": "M829A3 APFSDS-T",
                    "value": "rhs_mag_M829A3",
                    "defaultvalue": "rhs_mag_M829A3"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829A2 [Indent level: 4],
                "rhs_mag_m829a2": {
                    "name": "M829A2 APFSDS-T",
                    "value": "rhs_mag_M829A2"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829A1 [Indent level: 4],
                "rhs_mag_m829a1": {
                    "name": "M829A1 APFSDS-T",
                    "value": "rhs_mag_M829A1"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M829 [Indent level: 4],
                "rhs_mag_m829": {
                    "name": "M829 APFSDS-T",
                    "value": "rhs_mag_M829"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M830 [Indent level: 4],
                "rhs_mag_m830": {
                    "name": "M830 HEAT-FS",
                    "value": "rhs_mag_M830"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M830A1 [Indent level: 4],
                "rhs_mag_m830a1": {
                    "name": "M830A1 MPAT",
                    "value": "rhs_mag_M830A1"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M1028 [Indent level: 4],
                "rhs_mag_m1028": {
                    "name": "M1028 Canister",
                    "value": "rhs_mag_M1028"
                },
                # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_M1147 [Indent level: 4],
                "rhs_mag_m1147": {
                    "name": "M1147 HE-FRAG",
                    "value": "rhs_mag_M1147"
                }
            }
        },
        # Class: CfgVehicles|rhsusf_m1a1tank_base|Attributes|rhs_ammoslot_3 [Indent level: 2],
        "rhs_ammoslot_3": {
            "displayname": "Ammo slot #3 count",
            "tooltip": "Define number of rounds stored inside of type #3. Max 36. Leave -1 for default loadout",
            "property": "rhs_ammoslot_3",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s'] spawn rhs_fnc_m1_defineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        }
    },
    "dlc": "RHS_USAF",
    "soundgetin": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1],
    "soundgetout": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1,20],
    "soundturnin": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnout": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnininternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnoutinternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "sounddammage": ["",0.562341,1],
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
    "mapsize": 10.51,
    "_generalmacro": "MBT_01_base_F",
    "brakeidlespeed": 0.1,
    "waterresistancecoef": 0.25,
    "dampingratefullthrottle": 0.3,
    "dampingratezerothrottleclutchengaged": 3,
    "dampingratezerothrottleclutchdisengaged": 0.25,
    # Class: CfgVehicles|MBT_01_base_F|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading [Indent level: 2]
        "mfd_driver_heading": {
            "topleft": "MFD_1_TL",
            "topright": "MFD_1_TR",
            "bottomleft": "MFD_1_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading|Draw|Driver_Heading [Indent level: 4],
                "driver_heading": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1,0],1],
                    "down": [[0.5,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Speed [Indent level: 2],
        "mfd_driver_speed": {
            "topleft": "MFD_2_TL",
            "topright": "MFD_2_TR",
            "bottomleft": "MFD_2_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Speed|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Speed|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Speed|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Speed|Draw|Driver_Speed [Indent level: 4],
                "driver_speed": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 3.6,
                    "sourcelength": 2,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1,0],1],
                    "down": [[0.5,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading_text [Indent level: 2],
        "mfd_driver_heading_text": {
            "topleft": "MFD_Driver_1_TL",
            "topright": "MFD_Driver_1_TR",
            "bottomleft": "MFD_Driver_1_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading_text|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading_text|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading_text|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading_text|Draw|Driver_Heading [Indent level: 4],
                "driver_heading": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.45,0.02],1],
                    "right": [[0.7,0.02],1],
                    "down": [[0.45,0.87],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading_second [Indent level: 2],
        "mfd_driver_heading_second": {
            "topleft": "MFD_Driver_2_TL",
            "topright": "MFD_Driver_2_TR",
            "bottomleft": "MFD_Driver_2_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading_second|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading_second|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading_second|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Driver_Heading_second|Draw|Driver_Heading [Indent level: 4],
                "driver_heading": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.45,0],1],
                    "right": [[0.95,0],1],
                    "down": [[0.45,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Ready_To_Fire [Indent level: 2],
        "mfd_gunner_ready_to_fire": {
            "topleft": "mfd_gun_cli_TL",
            "topright": "mfd_gun_cli_TR",
            "bottomleft": "mfd_gun_cli_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Ready_To_Fire|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Ready_To_Fire|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw [Indent level: 3],
            "draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw|Top_text [Indent level: 4],
                "top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "READY TO",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.45,0.05],1],
                    "right": [[0.67,0.05],1],
                    "down": [[0.45,0.55],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw|Bottom_text [Indent level: 4],
                "bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "FIRE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.465,0.45],1],
                    "right": [[0.685,0.45],1],
                    "down": [[0.465,0.95],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display [Indent level: 2],
        "mfd_gunner_display": {
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "bottomleft": "mfd_gun_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|Draw|Main_armament [Indent level: 4],
                "main_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "MAIN ARMAMENT",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,-0.003],1],
                    "right": [[0.075,-0.003],1],
                    "down": [[0.015,0.075],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|Draw|Machinegun [Indent level: 4],
                "machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "COAX",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.31],1],
                    "right": [[0.075,0.31],1],
                    "down": [[0.015,0.388],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|Draw|Main_armament_ammo_type [Indent level: 4],
                "main_armament_ammo_type": {
                    "type": "text",
                    "source": "static",
                    "text": "AMMO TYPE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.545,-0.003],1],
                    "right": [[0.605,-0.003],1],
                    "down": [[0.545,0.075],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|Draw|Lased_distance_elevation [Indent level: 4],
                "lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "LASED DIST",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.84],1],
                    "right": [[0.065,0.84],1],
                    "down": [[0.015,0.918],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|Draw|Azimut [Indent level: 4],
                "azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.915],1],
                    "right": [[0.075,0.915],1],
                    "down": [[0.015,0.993],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|Draw|Damage [Indent level: 4],
                "damage": {
                    "type": "text",
                    "source": "static",
                    "text": "DAMAGE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.39],1],
                    "right": [[0.075,0.39],1],
                    "down": [[0.015,0.468],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|Draw|Heading [Indent level: 4],
                "heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 0.2,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.34,0.915],1],
                    "right": [[0.4,0.915],1],
                    "down": [[0.34,0.993],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Display|Draw|Lased_Range [Indent level: 4],
                "lased_range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.335,0.84],1],
                    "right": [[0.395,0.84],1],
                    "down": [[0.335,0.918],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type [Indent level: 2],
        "mfd_gunner_main_armament_ammo_type": {
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "bottomleft": "mfd_gun_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Draw|Gunner_AmmoType [Indent level: 4],
                "gunner_ammotype": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.56,0.09],1],
                    "right": [[0.62,0.09],1],
                    "down": [[0.56,0.168],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Coax_Ammo [Indent level: 2],
        "mfd_gunner_coax_ammo": {
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "bottomleft": "mfd_gun_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Coax_Ammo|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Coax_Ammo|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Coax_Ammo|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Coax_Ammo|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "sourceindex": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.37,0.31],1],
                    "right": [[0.43,0.31],1],
                    "down": [[0.37,0.388],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament [Indent level: 2],
        "mfd_gunner_ammoindicator_main_armament": {
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "bottomleft": "mfd_gun_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "EtelkaMonospacePro",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_1 [Indent level: 4],
                "main_armament_ammo_type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "APFSDS-T",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.065],1],
                    "right": [[0.075,0.065],1],
                    "down": [[0.015,0.143],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1000,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.385,0.065],1],
                    "right": [[0.445,0.065],1],
                    "down": [[0.385,0.143],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_2 [Indent level: 4],
                "main_armament_ammo_type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "HE-T",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.125],1],
                    "right": [[0.075,0.125],1],
                    "down": [[0.015,0.203],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_2 [Indent level: 4],
                "gunner_text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1001,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.385,0.125],1],
                    "right": [[0.445,0.125],1],
                    "down": [[0.385,0.203],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_3 [Indent level: 4],
                "main_armament_ammo_type_3": {
                    "type": "text",
                    "source": "static",
                    "text": "HEAT-MP-T",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.185],1],
                    "right": [[0.075,0.185],1],
                    "down": [[0.015,0.263],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_3 [Indent level: 4],
                "gunner_text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1002,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.385,0.185],1],
                    "right": [[0.445,0.185],1],
                    "down": [[0.385,0.263],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Generic1 [Indent level: 2],
        "mfd_gunner_generic1": {
            "topleft": "mfd_gun_generic1_TL",
            "topright": "mfd_gun_generic1_TR",
            "bottomleft": "mfd_gun_generic1_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "PuristaMedium",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Generic1|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Generic1|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Generic1|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Generic1|Draw|Generic_Text1 [Indent level: 4],
                "generic_text1": {
                    "type": "text",
                    "source": "static",
                    "text": "SIGHT: READY",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.05,0.1],1],
                    "right": [[0.17,0.1],1],
                    "down": [[0.05,0.5],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Gunner_Generic1|Draw|Generic_Text2 [Indent level: 4],
                "generic_text2": {
                    "type": "text",
                    "source": "static",
                    "text": "RETICLE: CALIBRATED",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.05,0.45],1],
                    "right": [[0.17,0.45],1],
                    "down": [[0.05,0.85],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display [Indent level: 2],
        "mfd_commander_display": {
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "bottomleft": "mfd_com_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0,0],
            "font": "PuristaMedium",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Main_armament [Indent level: 4],
                "main_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "MAIN ARMAMENT",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,-0.005],1],
                    "right": [[0.075,-0.005],1],
                    "down": [[0.015,0.145],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Machinegun [Indent level: 4],
                "machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "COAX MG",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.51,-0.005],1],
                    "right": [[0.57,-0.005],1],
                    "down": [[0.51,0.145],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Commander_machinegun [Indent level: 4],
                "commander_machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "----",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.84,0.19],1],
                    "right": [[0.9,0.19],1],
                    "down": [[0.84,0.34],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Commander_armament [Indent level: 4],
                "commander_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "COM ARMAMENT",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.785,-0.005],1],
                    "right": [[0.845,-0.005],1],
                    "down": [[0.785,0.145],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Commander_armament_magazines [Indent level: 4],
                "commander_armament_magazines": {
                    "type": "text",
                    "source": "static",
                    "text": "MAG",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.47,0.4],1],
                    "right": [[0.53,0.4],1],
                    "down": [[0.47,0.55],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Main_armament_ammo_type [Indent level: 4],
                "main_armament_ammo_type": {
                    "type": "text",
                    "source": "static",
                    "text": "AMMO TYPE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.61],1],
                    "right": [[0.075,0.61],1],
                    "down": [[0.015,0.76],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Lased_distance_elevation [Indent level: 4],
                "lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "LASED DST",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.73,0.61],1],
                    "right": [[0.785,0.61],1],
                    "down": [[0.73,0.76],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Azimut [Indent level: 4],
                "azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.72,0.8],1],
                    "right": [[0.78,0.8],1],
                    "down": [[0.72,0.95],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Damage [Indent level: 4],
                "damage": {
                    "type": "text",
                    "source": "static",
                    "text": "DAMAGE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.82],1],
                    "right": [[0.075,0.82],1],
                    "down": [[0.015,0.97],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Heading [Indent level: 4],
                "heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 0.2,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.925,0.8],1],
                    "right": [[0.985,0.8],1],
                    "down": [[0.925,0.95],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Display|Draw|Lased_Range [Indent level: 4],
                "lased_range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.925,0.61],1],
                    "right": [[0.985,0.61],1],
                    "down": [[0.925,0.76],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic1 [Indent level: 2],
        "mfd_commander_generic1": {
            "topleft": "mfd_com_generic1_TL",
            "topright": "mfd_com_generic1_TR",
            "bottomleft": "mfd_com_generic1_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "PuristaMedium",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic1|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic1|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic1|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic1|Draw|Generic_Text1 [Indent level: 4],
                "generic_text1": {
                    "type": "text",
                    "source": "static",
                    "text": "SIGHT: READY",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.05,0.1],1],
                    "right": [[0.17,0.1],1],
                    "down": [[0.05,0.5],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic1|Draw|Generic_Text2 [Indent level: 4],
                "generic_text2": {
                    "type": "text",
                    "source": "static",
                    "text": "RETICLE: CALIBRATED",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.05,0.45],1],
                    "right": [[0.17,0.45],1],
                    "down": [[0.05,0.85],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic2 [Indent level: 2],
        "mfd_commander_generic2": {
            "topleft": "mfd_com_generic2_TL",
            "topright": "mfd_com_generic2_TR",
            "bottomleft": "mfd_com_generic2_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "PuristaMedium",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic2|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic2|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic2|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic2|Draw|Generic_Text1 [Indent level: 4],
                "generic_text1": {
                    "type": "text",
                    "source": "static",
                    "text": "BRIGHTNESS: 7",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.05,0],1],
                    "right": [[0.2,0],1],
                    "down": [[0.05,0.5],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Generic2|Draw|Generic_Text2 [Indent level: 4],
                "generic_text2": {
                    "type": "text",
                    "source": "static",
                    "text": "AUTO: ON",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.05,0.45],1],
                    "right": [[0.2,0.45],1],
                    "down": [[0.05,0.95],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Ready_To_Fire [Indent level: 2],
        "mfd_commander_ready_to_fire": {
            "topleft": "mfd_com_cli_TL",
            "topright": "mfd_com_cli_TR",
            "bottomleft": "mfd_com_cli_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Ready_To_Fire|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Ready_To_Fire|Draw [Indent level: 3],
            "draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Ready_To_Fire|Draw|Top_text [Indent level: 4],
                "top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "READY TO",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.48,0.05],1],
                    "right": [[0.68,0.05],1],
                    "down": [[0.48,0.56],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Ready_To_Fire|Draw|Bottom_text [Indent level: 4],
                "bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "FIRE",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.5,0.41],1],
                    "right": [[0.7,0.41],1],
                    "down": [[0.5,0.92],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Smoke_Indicator [Indent level: 2],
        "mfd_commander_smoke_indicator": {
            "topleft": "mfd_com_smoke_TL",
            "topright": "mfd_com_smoke_TR",
            "bottomleft": "mfd_com_smoke_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Smoke_Indicator|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Smoke_Indicator|Draw [Indent level: 3],
            "draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Smoke_Indicator|Draw|Top_text [Indent level: 4],
                "top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "SMOKE",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.5,0],1],
                    "right": [[0.7,0],1],
                    "down": [[0.5,0.5],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Smoke_Indicator|Draw|Bottom_text [Indent level: 4],
                "bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "SCREEN",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.5,0.4],1],
                    "right": [[0.7,0.4],1],
                    "down": [[0.5,0.9],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type [Indent level: 2],
        "mfd_commander_main_armament_ammo_type": {
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "bottomleft": "mfd_com_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableparallax": 0,
            "font": "PuristaMedium",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Main_Armament_Ammo_Type|Draw|Gunner_AmmoType [Indent level: 4],
                "gunner_ammotype": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.33,0.615],1],
                    "right": [[0.39,0.615],1],
                    "down": [[0.33,0.745],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament [Indent level: 2],
        "mfd_commander_ammoindicator_main_armament": {
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "bottomleft": "mfd_com_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "PuristaMedium",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_1 [Indent level: 4],
                "main_armament_ammo_type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "APFSDS-T",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.13],1],
                    "right": [[0.075,0.13],1],
                    "down": [[0.015,0.28],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1000,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.39,0.13],1],
                    "right": [[0.45,0.13],1],
                    "down": [[0.39,0.28],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_2 [Indent level: 4],
                "main_armament_ammo_type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "HE-T",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.23],1],
                    "right": [[0.075,0.23],1],
                    "down": [[0.015,0.38],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Gunner_Text_2 [Indent level: 4],
                "gunner_text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1001,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.39,0.23],1],
                    "right": [[0.45,0.23],1],
                    "down": [[0.39,0.38],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_3 [Indent level: 4],
                "main_armament_ammo_type_3": {
                    "type": "text",
                    "source": "static",
                    "text": "HEAT-MP-T",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.33],1],
                    "right": [[0.075,0.33],1],
                    "down": [[0.015,0.48],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_AmmoIndicator_Main_Armament|Draw|Gunner_Text_3 [Indent level: 4],
                "gunner_text_3": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1002,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.39,0.33],1],
                    "right": [[0.45,0.33],1],
                    "down": [[0.39,0.48],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Coax_Ammo [Indent level: 2],
        "mfd_commander_coax_ammo": {
            "topleft": "mfd_com_ammo_count_TL",
            "topright": "mfd_com_ammo_count_TR",
            "bottomleft": "mfd_com_ammo_count_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "PuristaMedium",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Coax_Ammo|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Coax_Ammo|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Coax_Ammo|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Coax_Ammo|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "sourceindex": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[1.495,0.2],1],
                    "right": [[2.045,0.2],1],
                    "down": [[1.495,0.9],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Coax_Magazines [Indent level: 2],
        "mfd_commander_coax_magazines": {
            "topleft": "mfd_com_mag_count_TL",
            "topright": "mfd_com_mag_count_TR",
            "bottomleft": "mfd_com_mag_count_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "PuristaMedium",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Coax_Magazines|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Coax_Magazines|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Coax_Magazines|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_Coax_Magazines|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "sourceindex": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[-1.7,0.11],1],
                    "right": [[-0.95,0.11],1],
                    "down": [[-1.7,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_OnScreen [Indent level: 2],
        "mfd_commander_onscreen": {
            "topleft": "PIP_COM_TL",
            "topright": "PIP_COM_TR",
            "bottomleft": "PIP_COM_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0,0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_OnScreen|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_OnScreen|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_OnScreen|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.05],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_OnScreen|Draw|Azimuth_number [Indent level: 4],
                "azimuth_number": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0.235],1],
                    "right": [[0.525,0.235],1],
                    "down": [[0.5,0.272],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_OnScreen|Draw|Elevation_Text [Indent level: 4],
                "elevation_text": {
                    "type": "text",
                    "source": "static",
                    "text": "E: ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.23,0.3],1],
                    "right": [[0.255,0.3],1],
                    "down": [[0.23,0.337],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_OnScreen|Draw|Elevation_Number [Indent level: 4],
                "elevation_number": {
                    "type": "text",
                    "source": "[y]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "sourceprecision": 1,
                    "refreshrate": 0,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.26,0.3],1],
                    "right": [[0.285,0.3],1],
                    "down": [[0.26,0.337],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_OnScreen|Draw|Lased_Range [Indent level: 4],
                "lased_range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0.65],1],
                    "right": [[0.525,0.65],1],
                    "down": [[0.5,0.687],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_OnScreen|Draw|VisionMode_Text [Indent level: 4],
                "visionmode_text": {
                    "type": "text",
                    "source": "static",
                    "text": "WFOV",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.75,0.65],1],
                    "right": [[0.775,0.65],1],
                    "down": [[0.75,0.687],1]
                },
                # Class: CfgVehicles|MBT_01_base_F|MFD|MFD_Commander_OnScreen|Draw|VisionMode_String [Indent level: 4],
                "visionmode_string": {
                    "type": "text",
                    "source": "visionMode",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.825,0.65],1],
                    "right": [[0.85,0.65],1],
                    "down": [[0.825,0.687],1]
                }
            }
        }
    },
    "editorsubcategory": "EdSubcat_Tanks",
    "driverinfopanelcamerapos": "driverview_old",
    "driverlefthandanimname": "drivewheel",
    "driverrighthandanimname": "drivewheel",
    "driverleftleganimname": "pedal_brake",
    "driverrightleganimname": "pedal_thrust",
    "viewdrivershadowamb": 0.5,
    "viewdrivershadowdiff": 0.05,
    # Class: CfgVehicles|MBT_01_base_F|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -3,
        "initangley": 0,
        "initfov": 0.9,
        "minfov": 0.25,
        "maxfov": 1.25,
        "minanglex": -65,
        "maxanglex": 85,
        "minangley": -150,
        "maxangley": 150,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": -0.075,
        "maxmovey": 0.075,
        "minmovez": -0.075,
        "maxmovez": 0.1,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "epeimpulsedamagecoef": 18,
    "waterppinvehicle": 0,
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "hideweaponsdriver": 1,
    "hideweaponscargo": 1,
    "animationsourcehatch": "",
    "insidesoundcoef": 0.9,
    "threat": [0.8,1,0.3],
    # Class: CfgVehicles|MBT_01_base_F|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light1 [Indent level: 3]
            "light1": {
                "color": [13,20,20],
                "ambient": [0,0,0],
                "intensity": 2,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                },
                "point": "light_interior1"
            },
            # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light2 [Indent level: 3],
            "light2": {
                "point": "light_interior2",
                "color": [13,20,20],
                "ambient": [0,0,0],
                "intensity": 1.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light3 [Indent level: 3],
            "light3": {
                "point": "light_interior3",
                "color": [13,20,20],
                "ambient": [0,0,0],
                "intensity": 1.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light4 [Indent level: 3],
            "light4": {
                "point": "light_interior4",
                "color": [13,20,20],
                "ambient": [0,0,0],
                "intensity": 0.7,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light5 [Indent level: 3],
            "light5": {
                "point": "light_interior5",
                "color": [18,20,20],
                "ambient": [0,0,0],
                "intensity": 0.2,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light6 [Indent level: 3],
            "light6": {
                "point": "light_interior6",
                "color": [18,20,20],
                "ambient": [0,0,0],
                "intensity": 3,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light7 [Indent level: 3],
            "light7": {
                "point": "light_interior7",
                "color": [18,20,20],
                "ambient": [0,0,0],
                "intensity": 4,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light8 [Indent level: 3],
            "light8": {
                "point": "light_interior8",
                "color": [18,20,20],
                "ambient": [0,0,0],
                "intensity": 4,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|MBT_01_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            }
        }
    },
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_1",1,1],
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_1",0.316228,1],
    "smokelaunchergrenadecount": 8,
    "smokelaunchervelocity": 14,
    "smokelauncheronturret": 1,
    "smokelauncherangle": 120,
    "animationlist": ["showCamonetCannon",0,"showCamonetPlates1",0,"showCamonetPlates2",0,"showCamonetTurret",0,"showCamonetHull",0],
    # Class: CfgVehicles|MBT_01_base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": "A licensed copy of an Israeli tank built in Central Europe. This tank is built for versatile use on the battlefield and maximal crew protection, which gained significant appreciation from western Europe armies in the 21st century. The M2A1 is armed with 120 mm cannon and a coaxial machinegun and can also be used as mobile artillery. This tank has proven itself in battle and thanks to heavy manufacture, it became the second most wide spread main battle tank of many countries in the world."
    },
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
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
    # Class: CfgVehicles|Tank_F|CamShake [Indent level: 1],
    "camshake": {
        "power": 5,
        "frequency": 20,
        "distance": 20,
        "minspeed": 5
    },
    "camshakecoef": 0,
    # Class: CfgVehicles|Tank_F|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|Tank_F|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: VehicleSystemsTemplateLeftDriver|Components [Indent level: 0]
            "components": {
                # Class: VehicleSystemsTemplateLeftDriver|Components|VehiclePrimaryGunnerDisplay [Indent level: 1]
                "vehicleprimarygunnerdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateLeftDriver|Components|VehicleCommanderDisplay [Indent level: 1],
                "vehiclecommanderdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Tank_F|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            # Class: VehicleSystemsTemplateRightDriver|Components [Indent level: 0]
            "components": {
                # Class: VehicleSystemsTemplateRightDriver|Components|VehiclePrimaryGunnerDisplay [Indent level: 1]
                "vehicleprimarygunnerdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateRightDriver|Components|VehicleCommanderDisplay [Indent level: 1],
                "vehiclecommanderdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "right": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
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
    "predictturnsimul": 1.2,
    "predictturnplan": 1,
    "soundgear": ["",0.000316228,1],
    "outsidesoundfilter": 1,
    "nightvision": 0,
    "formationx": 20,
    "formationz": 30,
    "canfloat": 0,
    "type": 1,
    "camouflage": 8,
    "driveropticscolor": [1,1,1,1],
    # Class: CfgVehicles|Tank|CargoLight [Indent level: 1],
    "cargolight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
    "enablegps": 1,
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
    # Class: CfgVehicles|AllVehicles|SoundEvents [Indent level: 1],
    "soundevents": {
    },
    "cargoproxyindexes": [],
    "cargodoors": [],
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
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "obstructsoundlfratio": 0,
    "occludesoundlfratio": 0.25,
    "unloadincombat": 0,
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
    "enablewatch": 0,
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
    "cargoiscodriver": [0],
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
    "driveropticseffect": [],
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
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
    "features": "",
    "insidedetectcoef": 0.05,
}