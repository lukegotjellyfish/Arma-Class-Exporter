rhsusf_f22 = {
    "rhs_gearanim": "fold_gear_F",
    "scope": 2,
    "dlc": "RHS_USAF",
    "author": "Red Hammer Studios",
    "category": "Air",
    "side": 1,
    "crew": "rhsusf_airforce_jetpilot",
    "typicalcargo": ["rhsusf_airforce_jetpilot"],
    "unitinfotype": "RHSUSF_RscUnitInfoJet_F22",
    "vehicleclass": "rhs_vehclass_aircraft",
    "faction": "rhs_faction_usaf",
    # Class: CfgVehicles|rhsusf_f22|pilotCamera [Indent level: 1],
    "pilotcamera": {
    },
    # Class: CfgVehicles|rhsusf_f22|EjectionSystem [Indent level: 1],
    "ejectionsystem": {
    },
    "model": "rhsusf|addons|rhsusf_f22|rhsusf_f22",
    "editorpreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_f22.paa",
    "displayname": "F-22A",
    "driveraction": "RHS_F22_Pilot",
    "driverlefthandanimname": "stick_thrust",
    "driverleftleganimname": "pedal_L",
    "driverrightleganimname": "pedal_R",
    "drivercaneject": 1,
    "drivercompartments": 1,
    "htmin": 6,
    "htmax": 18,
    "afmax": 10,
    "mfmax": 30,
    "mfact": 10.02,
    "tbody": 150,
    "irtarget": 1,
    "irtargetsize": 0.5,
    "visualtarget": 1,
    "visualtargetsize": 1,
    "radartarget": 1,
    "radartargetsize": 0.3,
    "radartype": 4,
    "lockdetectionsystem": 8,
    "incomingmissiledetectionsystem": 16,
    "receiveremotetargets": 1,
    "reportremotetargets": 1,
    "reportownposition": 1,
    "laserscanner": 1,
    # Class: CfgVehicles|rhsusf_f22|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            "uipicture": "rhsusf|addons|rhsusf_f22|data|loadouts|RHS_F22_EDEN_CA.paa",
            # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|pylons|pylonBayLeft1 [Indent level: 4]
                "pylonbayleft1": {
                    "hardpoints": ["RHS_HP_AIM9_int"],
                    "priority": 2,
                    "attachment": "rhs_mag_Sidewinder_int",
                    "maxweight": 1200,
                    "uiposition": [0.36,0.4],
                    "bay": 1
                },
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|pylons|pylonBayCenter1 [Indent level: 4],
                "pylonbaycenter1": {
                    "hardpoints": ["RHS_HP_aim120_int"],
                    "priority": 1,
                    "attachment": "rhs_mag_aim120d_int",
                    "maxweight": 1200,
                    "uiposition": [0.36,0.35],
                    "bay": 2
                },
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|pylons|pylonBayCenter2 [Indent level: 4],
                "pylonbaycenter2": {
                    "hardpoints": ["RHS_HP_aim120_int","RHS_HP_F22_lBay","RHS_HP_JDAM_500","RHS_HP_JDAM_1000"],
                    "attachment": "rhs_mag_aim120d_2_F22_l",
                    "uiposition": [0.36,0.3],
                    "priority": 1,
                    "maxweight": 1200,
                    "bay": 2
                },
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|pylons|pylonBayCenter3 [Indent level: 4],
                "pylonbaycenter3": {
                    "hardpoints": ["RHS_HP_aim120_int","RHS_HP_F22_rBay","RHS_HP_JDAM_500","RHS_HP_JDAM_1000"],
                    "attachment": "rhs_mag_aim120d_2_F22_r",
                    "uiposition": [0.36,0.25],
                    "bay": 3,
                    "priority": 1,
                    "maxweight": 1200
                },
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|pylons|pylonBayCenter4 [Indent level: 4],
                "pylonbaycenter4": {
                    "hardpoints": ["RHS_HP_aim120_int"],
                    "attachment": "rhs_mag_aim120d_int",
                    "uiposition": [0.36,0.2],
                    "mirroredmissilepos": 2,
                    "bay": 3,
                    "priority": 1,
                    "maxweight": 1200
                },
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|pylons|pylonBayRight1 [Indent level: 4],
                "pylonbayright1": {
                    "uiposition": [0.36,0.15],
                    "mirroredmissilepos": 1,
                    "bay": 4,
                    "hardpoints": ["RHS_HP_AIM9_int"],
                    "priority": 2,
                    "attachment": "rhs_mag_Sidewinder_int",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4],
                "cmdispenser": {
                    "hardpoints": ["RHSUSF_cm_ANALE52","RHSUSF_cm_ANALE52_x2","RHSUSF_cm_ANALE52_x4","RHSUSF_cm_ANALE52_x6"],
                    "priority": 1,
                    "attachment": "rhsusf_ANALE52_CMFlare_Chaff_Magazine_x4",
                    "maxweight": 800,
                    "uiposition": [0.625,0.275]
                }
            },
            # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|Bays [Indent level: 3],
            "bays": {
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|Bays|BayLeft1 [Indent level: 4]
                "bayleft1": {
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 1,
                    "autoclosewhenemptydelay": 1
                },
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|Bays|BayCenter1 [Indent level: 4],
                "baycenter1": {
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 0,
                    "autoclosewhenemptydelay": 4.5
                },
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|Bays|BayCenter2 [Indent level: 4],
                "baycenter2": {
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 0,
                    "autoclosewhenemptydelay": 4.5
                },
                # Class: CfgVehicles|rhsusf_f22|Components|TransportPylonsComponent|Bays|BayRight1 [Indent level: 4],
                "bayright1": {
                    "bayopentime": 0.5,
                    "openbaywhenweaponselected": 1,
                    "autoclosewhenemptydelay": 1
                }
            }
        },
        # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4]
                "passiveradarsensorcomponent": {
                    # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 18000,
                        "maxrange": 18000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 18000,
                        "maxrange": 18000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "componenttype": "PassiveRadarSensorComponent",
                    "typerecognitiondistance": 12000,
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 360,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "color": [0.5,1,0.5,0.5],
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010,
                    "allowsmarking": 0
                },
                # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent [Indent level: 4],
                "activeradarsensorcomponent": {
                    # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 35000,
                        "maxrange": 35000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 10000,
                        "maxrange": 10000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "groundnoisedistancecoef": 0.0005,
                    "maxgroundnoisedistance": 50,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "anglerangehorizontal": 60,
                    "anglerangevertical": 60,
                    "typerecognitiondistance": 20000,
                    "maxfogseethrough": 1,
                    "maxtrackablespeed": 830,
                    "componenttype": "ActiveRadarSensorComponent",
                    "color": [0,1,1,1],
                    "allowsmarking": 1,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent_Wide [Indent level: 4],
                "activeradarsensorcomponent_wide": {
                    # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent_Wide|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 10000,
                        "maxrange": 10000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent_Wide|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 10000,
                        "maxrange": 10000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "groundnoisedistancecoef": 0.0005,
                    "maxgroundnoisedistance": 50,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "anglerangehorizontal": 110,
                    "anglerangevertical": 110,
                    "typerecognitiondistance": 10000,
                    "maxfogseethrough": 1,
                    "maxtrackablespeed": 830,
                    "componenttype": "ActiveRadarSensorComponent",
                    "color": [0,1,1,1],
                    "allowsmarking": 1,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|rhsusf_f22|Components|SensorsManagerComponent|Components|DataLinkSensorComponent [Indent level: 4],
                "datalinksensorcomponent": {
                    "componenttype": "DataLinkSensorComponent",
                    "allowsmarking": 1,
                    "typerecognitiondistance": 0,
                    "color": [1,1,1,0],
                    # Class: SensorTemplatePassiveRadar|AirTarget [Indent level: 0],
                    "airtarget": {
                        "minrange": 16000,
                        "maxrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: SensorTemplatePassiveRadar|GroundTarget [Indent level: 0],
                    "groundtarget": {
                        "minrange": 16000,
                        "maxrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 360,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                }
            }
        },
        # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentLeft|Components|UAVDisplay [Indent level: 4],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [16000,35000,3000,8000]
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentRight|Components|UAVDisplay [Indent level: 4],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles|rhsusf_f22|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [16000,35000,3000,8000]
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Air|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    "icon": "rhsusf|addons|rhsusf_f22|data|f22_icon.paa",
    "picture": "rhsusf|addons|rhsusf_f22|data|f22_pic.paa",
    "weapons": ["rhs_weap_MASTERSAFE_Holdster15","rhsusf_M61A2"],
    "magazines": ["rhsusf_20mm_M61A2"],
    "insidesoundcoef": 0.2,
    "hiddenselections": ["tex1","tex2","tex3","tex4","tex5","tex6","tex7","tex8","tex9"],
    "hiddenselectionstextures": ["|rhsusf|addons|rhsusf_f22|data|f22_b1.paa","|rhsusf|addons|rhsusf_f22|data|f22_wing_spads.paa","|rhsusf|addons|rhsusf_f22|data|1stfw.paa","|rhsusf|addons|rhsusf_f22|data|94fs.paa","|rhsusf|addons|rhsusf_f22|data|acc.paa","|rhsusf|addons|rhsusf_f22|data|af04-066.paa","|rhsusf|addons|rhsusf_f22|data|ff.paa","|rhsusf|addons|rhsusf_f22|data|marking1.paa","|rhsusf|addons|rhsusf_f22|data|star1.paa"],
    "camouflage": 18,
    "audible": 6,
    "accuracy": 0.2,
    "gunaimdown": 0.045,
    "memorypointlrocket": "Rocket_1",
    "memorypointrrocket": "Rocket_2",
    "gunbeg": ["muzzle_1"],
    "gunend": ["chamber_1"],
    "camshakecoef": 0.6,
    "headgforceleaningfactor": [0.005,0.001,0.015],
    "extcameraposition": [0,3.8,-23],
    "minfiretime": 30,
    "cost": 8e+007,
    "type": 2,
    "threat": [1,1,0.7],
    "driveoncomponent": [],
    "armor": 80,
    "armorstructural": 3,
    "ejectdamagelimit": 1,
    "epeimpulsedamagecoef": 1,
    "damageresistance": 0.00336,
    # Class: CfgVehicles|rhsusf_f22|Hitpoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0.01,
            "minimalhit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull",
            "visual": "",
            "depends": "Total"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 0.5,
            "explosionshielding": 0.6,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.7,
            "explosionshielding": 0.25,
            "passthrough": 0.01,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_l",
            "depends": "0"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "armor": 0.7,
            "explosionshielding": 0.25,
            "passthrough": 0.01,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_r",
            "depends": "0"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 0.75,
            "explosionshielding": 0.2,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel",
            "visual": "vis_fuel",
            "depends": "0"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitLAileron [Indent level: 2],
        "hitlaileron": {
            "armor": 0.5,
            "explosionshielding": 0.6,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "visual": "vis_wing_l",
            "depends": "0"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitRAileron [Indent level: 2],
        "hitraileron": {
            "armor": 0.5,
            "explosionshielding": 0.6,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "visual": "vis_wing_r",
            "depends": "0"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitControlRear [Indent level: 2],
        "hitcontrolrear": {
            "armor": 0.5,
            "explosionshielding": 0.1,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.17,
            "material": -1,
            "name": "hit_control_rear",
            "visual": "",
            "depends": "0"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitLCElevator [Indent level: 2],
        "hitlcelevator": {
            "armor": 0.5,
            "explosionshielding": 0.5,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitRElevator [Indent level: 2],
        "hitrelevator": {
            "armor": 0.5,
            "explosionshielding": 0.5,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitLCRudder [Indent level: 2],
        "hitlcrudder": {
            "armor": 0.5,
            "explosionshielding": 0.5,
            "passthrough": 0.01,
            "minimalhit": 0.02,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder_l",
            "visual": "vis_rudder_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitRRudder [Indent level: 2],
        "hitrrudder": {
            "armor": 0.5,
            "explosionshielding": 0.5,
            "passthrough": 0.01,
            "minimalhit": 0.02,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder_r",
            "visual": "vis_rudder_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|rhsusf_f22|Hitpoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 0.4,
            "explosionshielding": 0.5,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "glass_1",
            "visual": "glass_1",
            "depends": "0"
        }
    },
    "soundengineonint": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_01|B_PLANE_FIGHTER_01_engine_start_int",1,1],
    "soundengineonext": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_01|B_PLANE_FIGHTER_01_engine_start_ext",1.75,1,300],
    "soundengineoffint": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_01|B_PLANE_FIGHTER_01_engine_shut_int",1,1],
    "soundengineoffext": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_01|B_PLANE_FIGHTER_01_engine_shut_ext",1.75,1,300],
    "soundlocked": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_lockedOn1",1,1],
    "soundincommingmissile": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_lockedon2",1,1.5],
    "soundgearup": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_gear_up",2.25,1,250],
    "soundgeardown": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_gear_down",2.25,1,250],
    "soundflapsup": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_Flaps_Up",1.5,1,150],
    "soundflapsdown": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_Flaps_Down",1.5,1,150],
    "soundsetsonicboom": ["Plane_Fighter_SonicBoom_SoundSet"],
    # Class: CfgVehicles|rhsusf_f22|Sounds [Indent level: 1],
    "sounds": {
        "soundsets": ["Plane_Fighter_01_EngineLowExt_SoundSet","Plane_Fighter_01_EngineHighExt_SoundSet","Plane_Fighter_01_ForsageExt_SoundSet","Plane_Fighter_01_WindNoiseExt_SoundSet","Plane_Fighter_01_EngineExt_Dist_Front_SoundSet","Plane_Fighter_01_EngineExt_Middle_SoundSet","Plane_Fighter_01_EngineExt_Dist_Rear_SoundSet","Plane_Fighter_01_EngineLowInt_SoundSet","Plane_Fighter_01_EngineHighInt_SoundSet","Plane_Fighter_01_ForsageInt_SoundSet","Plane_Fighter_01_WindNoiseInt_SoundSet","Plane_Fighter_01_VelocityInt_SoundSet"]
    },
    # Class: CfgVehicles|rhsusf_f22|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhsusf_f22|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "rightengine",
            "direction": "rightengine_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 1
        },
        # Class: CfgVehicles|rhsusf_f22|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "leftengine",
            "direction": "leftengine_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 0
        }
    },
    # Class: CfgVehicles|rhsusf_f22|WingVortices [Indent level: 1],
    "wingvortices": {
        # Class: CfgVehicles|rhsusf_f22|WingVortices|WingTipLeft [Indent level: 2]
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "wing_vortex_l"
        },
        # Class: CfgVehicles|rhsusf_f22|WingVortices|WingTipRight [Indent level: 2],
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "wing_vortex_r"
        },
        # Class: CfgVehicles|rhsusf_f22|WingVortices|BodyLeft [Indent level: 2],
        "bodyleft": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles|rhsusf_f22|WingVortices|BodyRight [Indent level: 2],
        "bodyright": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_S"
        },
        # Class: CfgVehicles|rhsusf_f22|WingVortices|BodyLeft2 [Indent level: 2],
        "bodyleft2": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_E"
        },
        # Class: CfgVehicles|rhsusf_f22|WingVortices|BodyRight2 [Indent level: 2],
        "bodyright2": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_E"
        }
    },
    # Class: CfgVehicles|rhsusf_f22|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhsusf_f22|AnimationSources|afterburner_source [Indent level: 2]
        "afterburner_source": {
            "source": "user",
            "initphase": 0,
            "animperiod": 1.5
        },
        # Class: CfgVehicles|rhsusf_f22|AnimationSources|eject [Indent level: 2],
        "eject": {
            "source": "door",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_f22|AnimationSources|eject_hide [Indent level: 2],
        "eject_hide": {
            "source": "user",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|rhsusf_f22|AnimationSources|CollisionLights_source [Indent level: 2],
        "collisionlights_source": {
            "source": "MarkerLight",
            "markerlight": "PositionLeft"
        },
        # Class: CfgVehicles|rhsusf_f22|AnimationSources|CollisionBlinking_source [Indent level: 2],
        "collisionblinking_source": {
            "markerlight": "CollisionLeft",
            "source": "MarkerLight"
        },
        # Class: CfgVehicles|rhsusf_f22|AnimationSources|Wheel_1_source [Indent level: 2],
        "wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|rhsusf_f22|AnimationSources|Wheel_2_source [Indent level: 2],
        "wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|rhsusf_f22|AnimationSources|Wheel_3_source [Indent level: 2],
        "wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        }
    },
    # Class: CfgVehicles|rhsusf_f22|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|rhsusf_f22|MarkerLights|PositionLeft [Indent level: 2]
        "positionleft": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "intensity": 750,
            "name": "PositionLight_Left_1_pos",
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|rhsusf_f22|MarkerLights|PositionLeft|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|rhsusf_f22|MarkerLights|PositionRight [Indent level: 2],
        "positionright": {
            "name": "PositionLight_Right_1_pos",
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "intensity": 750,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|rhsusf_f22|MarkerLights|PositionLeft|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|rhsusf_f22|MarkerLights|CollisionLeft [Indent level: 2],
        "collisionleft": {
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 2750,
            "blinking": 1,
            "blinkingpattern": [0.2,1.3],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.35,
            "drawlightcentersize": 0.18,
            "name": "PositionLight_Left_1_pos",
            "drawlight": 1,
            "activelight": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|rhsusf_f22|MarkerLights|PositionLeft|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|rhsusf_f22|MarkerLights|CollisionRight [Indent level: 2],
        "collisionright": {
            "name": "PositionLight_Right_1_pos",
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 2750,
            "blinking": 1,
            "blinkingpattern": [0.2,1.3],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.35,
            "drawlightcentersize": 0.18,
            "drawlight": 1,
            "activelight": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|rhsusf_f22|MarkerLights|PositionLeft|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        }
    },
    # Class: CfgVehicles|rhsusf_f22|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhsusf_f22|UserActions|SAFEMODE [Indent level: 2]
        "safemode": {
            "displayname": "<t color='#00FF7F'>MASTERSAFE</t>",
            "condition": "(call rhsusf_fnc_findPlayer) in this",
            "statement": "(call rhsusf_fnc_findPlayer) action ['SwitchWeapon', this, (call rhsusf_fnc_findPlayer), (weapons this) find 'rhs_weap_MASTERSAFE'];",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showwindow": 0,
            "shortcut": "user13",
            "hideonuse": 1
        }
    },
    # Class: CfgVehicles|rhsusf_f22|Eventhandlers [Indent level: 1],
    "eventhandlers": {
        "hit": "",
        # Class: CfgVehicles|rhsusf_f22|Eventhandlers|RHSUSF_EventHandlers [Indent level: 2],
        "rhsusf_eventhandlers": {
            "init": "_this execVM '|rhsusf|addons|rhsusf_c_f22|scripts|rhs_f22_mfdHandler.sqf'",
            "hit": "_this call RHS_fnc_AI_eject",
            "getout": "[_this select 0, _this select 2,'rhs_f22_canopy'] call rhs_fnc_ACESII_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes;"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "defaultusermfdvalues": [0.082,0.408,0.039,0.8],
    "defaultusermfdtext": ["test"],
    # Class: CfgVehicles|rhsusf_f22|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD [Indent level: 2]
        "airplanehud": {
            "topleft": "HUD LH",
            "topright": "HUD PH",
            "bottomleft": "HUD LD",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 1,
            "font": "rhsusf_digital_font_usa",
            # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|PlaneOrientation [Indent level: 4],
                "planeorientation": {
                    "type": "vector",
                    "source": "forward",
                    "pos": [0.495,0.546],
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|WeaponAim [Indent level: 4],
                "weaponaim": {
                    "type": "vector",
                    "source": "weapon",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|ImpactPoint [Indent level: 4],
                "impactpoint": {
                    "type": "vector",
                    "source": "ImpactPointWeaponRelative",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|NormalizeBombCircle [Indent level: 4],
                "normalizebombcircle": {
                    "type": "normalizedorsmaller",
                    "limit": 0.08,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|ImpactPointRelative [Indent level: 4],
                "impactpointrelative": {
                    "type": "vector",
                    "source": "impactpointweaponRelative",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|Target [Indent level: 4],
                "target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|TargetingPodDir [Indent level: 4],
                "targetingpoddir": {
                    "source": "pilotcamera",
                    "type": "vector",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|TargetingPodTarget [Indent level: 4],
                "targetingpodtarget": {
                    "source": "pilotcameratarget",
                    "type": "vector",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|Limit0109 [Indent level: 4],
                "limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LimitWaypoint [Indent level: 4],
                "limitwaypoint": {
                    "type": "limit",
                    "limits": [0.33,0.1,0.67,0.1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|WPPoint [Indent level: 4],
                "wppoint": {
                    "type": "vector",
                    "source": "WPPoint",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|ASL_Instrument [Indent level: 4],
                "asl_instrument": {
                    "type": "rotational",
                    "source": "altitudeASL",
                    "center": [0.9,0.446429],
                    "min": 0,
                    "max": 20000,
                    "minangle": 0,
                    "maxangle": 72000,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|Speed_Instrument [Indent level: 4],
                "speed_instrument": {
                    "source": "speed",
                    "center": [0.1,0.446429],
                    "max": 555.556,
                    "maxangle": 7200,
                    "type": "rotational",
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|Airport1 [Indent level: 4],
                "airport1": {
                    "type": "vector",
                    "source": "airportCorner1",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|Airport2 [Indent level: 4],
                "airport2": {
                    "source": "airportCorner2",
                    "type": "vector",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|Airport3 [Indent level: 4],
                "airport3": {
                    "source": "airportCorner3",
                    "type": "vector",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|Airport4 [Indent level: 4],
                "airport4": {
                    "source": "airportCorner4",
                    "type": "vector",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|ILS_H [Indent level: 4],
                "ils_h": {
                    "type": "ils",
                    "pos0": [0.5,0.536],
                    "pos3": [0.68228,0.536]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|ILS_W [Indent level: 4],
                "ils_w": {
                    "pos3": [0.5,0.69875],
                    "type": "ils",
                    "pos0": [0.5,0.536]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|HorizonBankRot [Indent level: 4],
                "horizonbankrot": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "center": [0.5,0.5],
                    "min": "-rad(45)",
                    "max": "rad(45)",
                    "minangle": "180.25-35.5",
                    "maxangle": "180.75+35.5",
                    "aspectratio": 0.8
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|HorizonBankRotFull [Indent level: 4],
                "horizonbankrotfull": {
                    "center": [0,0],
                    "min": -3.1416,
                    "max": 3.1416,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 1,
                    "type": "rotational",
                    "source": "horizonBank"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],
                "level0": {
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP5 [Indent level: 4],
                "levelp5": {
                    "angle": "1.0*5",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM5 [Indent level: 4],
                "levelm5": {
                    "angle": "1.0*-5",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": "1.0*10",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": "1.0*-10",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": "1.0*15",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": "1.0*-15",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": "1.0*20",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": "1.0*-20",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": "1.0*25",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": "1.0*-25",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": "1.0*30",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": "1.0*-30",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": "1.0*35",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": "1.0*-35",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": "1.0*40",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": "1.0*-40",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": "1.0*45",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": "1.0*-45",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP50 [Indent level: 4],
                "levelp50": {
                    "angle": "1.0*50",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM50 [Indent level: 4],
                "levelm50": {
                    "angle": "1.0*-50",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP60 [Indent level: 4],
                "levelp60": {
                    "angle": "1.0*60",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM60 [Indent level: 4],
                "levelm60": {
                    "angle": "1.0*-60",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP70 [Indent level: 4],
                "levelp70": {
                    "angle": "1.0*70",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM70 [Indent level: 4],
                "levelm70": {
                    "angle": "1.0*-70",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP80 [Indent level: 4],
                "levelp80": {
                    "angle": "1.0*80",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM80 [Indent level: 4],
                "levelm80": {
                    "angle": "1.0*-80",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelP90 [Indent level: 4],
                "levelp90": {
                    "angle": "1.0*90",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LevelM90 [Indent level: 4],
                "levelm90": {
                    "angle": "1.0*-90",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot1 [Indent level: 4],
                "missileflighttimerot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minangle": 0,
                    "maxangle": 18,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot2 [Indent level: 4],
                "missileflighttimerot2": {
                    "maxangle": 36,
                    "max": 1,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot3 [Indent level: 4],
                "missileflighttimerot3": {
                    "maxangle": 54,
                    "max": 1.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot4 [Indent level: 4],
                "missileflighttimerot4": {
                    "maxangle": 72,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot5 [Indent level: 4],
                "missileflighttimerot5": {
                    "maxangle": 90,
                    "max": 2.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot6 [Indent level: 4],
                "missileflighttimerot6": {
                    "maxangle": 108,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot7 [Indent level: 4],
                "missileflighttimerot7": {
                    "maxangle": 126,
                    "max": 3.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot8 [Indent level: 4],
                "missileflighttimerot8": {
                    "maxangle": 144,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot9 [Indent level: 4],
                "missileflighttimerot9": {
                    "maxangle": 162,
                    "max": 4.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot10 [Indent level: 4],
                "missileflighttimerot10": {
                    "maxangle": 180,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot11 [Indent level: 4],
                "missileflighttimerot11": {
                    "maxangle": 198,
                    "max": 5.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot12 [Indent level: 4],
                "missileflighttimerot12": {
                    "maxangle": 216,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot13 [Indent level: 4],
                "missileflighttimerot13": {
                    "maxangle": 234,
                    "max": 6.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot14 [Indent level: 4],
                "missileflighttimerot14": {
                    "maxangle": 252,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot15 [Indent level: 4],
                "missileflighttimerot15": {
                    "maxangle": 270,
                    "max": 7.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot16 [Indent level: 4],
                "missileflighttimerot16": {
                    "maxangle": 288,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot17 [Indent level: 4],
                "missileflighttimerot17": {
                    "maxangle": 306,
                    "max": 8.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot18 [Indent level: 4],
                "missileflighttimerot18": {
                    "maxangle": 324,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot19 [Indent level: 4],
                "missileflighttimerot19": {
                    "maxangle": 342,
                    "max": 9.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|MissileFlightTimeRot20 [Indent level: 4],
                "missileflighttimerot20": {
                    "maxangle": 360,
                    "max": 10,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LarAmmoMax [Indent level: 4],
                "larammomax": {
                    "type": "linear",
                    "source": "LarAmmoMax",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LarAmmoMin [Indent level: 4],
                "larammomin": {
                    "source": "LarAmmoMin",
                    "type": "linear",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LarTargetDist [Indent level: 4],
                "lartargetdist": {
                    "source": "LarTargetDist",
                    "type": "linear",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LarAmmoMGunMax [Indent level: 4],
                "larammomgunmax": {
                    "type": "rotational",
                    "source": "LarAmmoMax",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 1,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 0.892857
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Bones|LarAmmoMGunMin [Indent level: 4],
                "larammomgunmin": {
                    "source": "LarAmmoMin",
                    "type": "rotational",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 1,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 0.892857
                }
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|PlaneW [Indent level: 4],
                "planew": {
                    "type": "line",
                    "width": 3,
                    "points": [["PlaneW",[-0.02,0],1],["PlaneW",[0.02,0],1],[],["PlaneW",[0,-0.0178571],1],["PlaneW",[0,0.0178571],1],[],[[0.11,0.777],1],[[0.09,0.76],1],[[0.085,0.758],1],[[0.08,0.758],1],[[0.075,0.76],1],[[0.073,0.767],1],[[0.075,0.774],1],[[0.08,0.776],1],[[0.085,0.776],1],[[0.09,0.774],1],[[0.11,0.757],1],[],["PlaneW",["-0.4-0.01",-0.25],1],["PlaneW",["-0.4-0",-0.241071],1],["PlaneW",["-0.4-0.01",-0.232143],1],[],[],[[0.805,0.779407],1],[[0.815,0.794872],1],[],[[0.732264,0.811433],1],[[0.739917,0.827931],1],[],[[0.655468,0.834709],1],[[0.660644,0.851958],1],[],[[0.575926,0.848836],1],[[0.578537,0.86654],1],[],[[0.495,0.853571],1],[[0.495,0.871429],1],[],[[0.414074,0.848836],1],[[0.411463,0.86654],1],[],[[0.334532,0.834709],1],[[0.329356,0.851958],1],[],[[0.257736,0.811433],1],[[0.250082,0.827931],1],[],[[0.185,0.779407],1],[[0.175,0.794872],1],[],["HorizonBankRot",[0,0.4375],1],["HorizonBankRot",[0.01,0.419643],1],["HorizonBankRot",[-0.01,0.419643],1],["HorizonBankRot",[0,0.4375],1],[],["Velocity",[0,-0.02],1],["Velocity",[0.01,-0.01732],1],["Velocity",[0.01732,-0.01],1],["Velocity",[0.02,0],1],["Velocity",[0.01732,0.01],1],["Velocity",[0.01,0.01732],1],["Velocity",[0,0.02],1],["Velocity",[-0.01,0.01732],1],["Velocity",[-0.01732,0.01],1],["Velocity",[-0.02,0],1],["Velocity",[-0.01732,-0.01],1],["Velocity",[-0.01,-0.01732],1],["Velocity",[0,-0.02],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.04],1],["Velocity",[0,-0.02],1]]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Static_Bold [Indent level: 4],
                "static_bold": {
                    "type": "line",
                    "width": 5,
                    "points": [[[0.0965,0.511161],1],[[0.1035,0.511161],1],[],[[0.1,0.508036],1],[[0.1,0.514286],1],[],[[0.139114,0.498798],1],[[0.146114,0.498798],1],[],[[0.142614,0.495673],1],[[0.142614,0.501923],1],[],[[0.165452,0.466432],1],[[0.172452,0.466432],1],[],[[0.168952,0.463307],1],[[0.168952,0.469557],1],[],[[0.165452,0.426425],1],[[0.172452,0.426425],1],[],[[0.168952,0.4233],1],[[0.168952,0.42955],1],[],[[0.139114,0.394059],1],[[0.146114,0.394059],1],[],[[0.142614,0.390934],1],[[0.142614,0.397184],1],[],[[0.0965,0.381696],1],[[0.1035,0.381696],1],[],[[0.1,0.378571],1],[[0.1,0.384821],1],[],[[0.0538856,0.394059],1],[[0.0608856,0.394059],1],[],[[0.0573856,0.390934],1],[[0.0573856,0.397184],1],[],[[0.0275484,0.426425],1],[[0.0345484,0.426425],1],[],[[0.0310484,0.4233],1],[[0.0310484,0.42955],1],[],[[0.0275484,0.466432],1],[[0.0345484,0.466432],1],[],[[0.0310484,0.463307],1],[[0.0310484,0.469557],1],[],[[0.0538856,0.498798],1],[[0.0608856,0.498798],1],[],[[0.0573856,0.495673],1],[[0.0573856,0.501923],1],[],["Speed_Instrument",[0,0.055],1],["Speed_Instrument",[0,0.075],1],[],[[0.8965,0.511161],1],[[0.9035,0.511161],1],[],[[0.9,0.508036],1],[[0.9,0.514286],1],[],[[0.939114,0.498798],1],[[0.946114,0.498798],1],[],[[0.942614,0.495673],1],[[0.942614,0.501923],1],[],[[0.965452,0.466432],1],[[0.972452,0.466432],1],[],[[0.968952,0.463307],1],[[0.968952,0.469557],1],[],[[0.965452,0.426425],1],[[0.972452,0.426425],1],[],[[0.968952,0.4233],1],[[0.968952,0.42955],1],[],[[0.939114,0.394059],1],[[0.946114,0.394059],1],[],[[0.942614,0.390934],1],[[0.942614,0.397184],1],[],[[0.8965,0.381696],1],[[0.9035,0.381696],1],[],[[0.9,0.378571],1],[[0.9,0.384821],1],[],[[0.853886,0.394059],1],[[0.860886,0.394059],1],[],[[0.857386,0.390934],1],[[0.857386,0.397184],1],[],[[0.827548,0.426425],1],[[0.834548,0.426425],1],[],[[0.831048,0.4233],1],[[0.831048,0.42955],1],[],[[0.827548,0.466432],1],[[0.834548,0.466432],1],[],[[0.831048,0.463307],1],[[0.831048,0.469557],1],[],[[0.853886,0.498798],1],[[0.860886,0.498798],1],[],[[0.857386,0.495673],1],[[0.857386,0.501923],1],[],["ASL_Instrument",[0,0.055],1],["ASL_Instrument",[0,0.075],1],[]]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AfterBurner [Indent level: 4],
                "afterburner": {
                    "condition": "throttle >=1",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AfterBurner|PlaneW [Indent level: 5],
                    "planew": {
                        "type": "line",
                        "width": 3,
                        "points": [["PlaneW",["-0.38-0.01",-0.25],1],["PlaneW",["-0.38-0",-0.241071],1],["PlaneW",["-0.38-0.01",-0.232143],1],[]]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0.1,0.15],
                    "clipbr": [0.85,0.99],
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "level0": {
                            "type": "line",
                            "width": 3,
                            "points": [["Level0",[0.25,0],1],["Level0",[0.065,0],1],[],["Level0",[-0.065,0],1],["Level0",[-0.25,0],1]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|Level0 [Indent level: 5],
                    "level0": {
                        "type": "line",
                        "width": 2,
                        "points": []
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM5 [Indent level: 5],
                    "levelm5": {
                        "type": "line",
                        "points": [["LevelM5",[-0.175,-0.02],1],["LevelM5",[-0.175,0],1],[],["LevelM5",[-0.16,"-0.001*1"],1],["LevelM5",[-0.145,"-0.001*2"],1],[],["LevelM5",[-0.13,"-0.001*3"],1],["LevelM5",[-0.115,"-0.001*4"],1],[],["LevelM5",[-0.1,"-0.001*5"],1],["LevelM5",[-0.085,"-0.001*6"],1],[],["LevelM5",[-0.07,"-0.001*7"],1],["LevelM5",[-0.055,"-0.001*8"],1],[],["LevelM5",[-0.04,"-0.001*9"],1],[],["LevelM5",[0.175,-0.02],1],["LevelM5",[0.175,0],1],[],["LevelM5",[0.16,"-0.001*1"],1],["LevelM5",[0.145,"-0.001*2"],1],[],["LevelM5",[0.13,"-0.001*3"],1],["LevelM5",[0.115,"-0.001*4"],1],[],["LevelM5",[0.1,"-0.001*5"],1],["LevelM5",[0.085,"-0.001*6"],1],[],["LevelM5",[0.07,"-0.001*7"],1],["LevelM5",[0.055,"-0.001*8"],1],[],["LevelM5",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_5 [Indent level: 5],
                    "valm_1_5": {
                        "type": "text",
                        "source": "static",
                        "text": -5,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM5",[-0.19,-0.032],1],
                        "right": ["LevelM5",[-0.13,-0.032],1],
                        "down": ["LevelM5",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_5_R [Indent level: 5],
                    "valm_1_5_r": {
                        "type": "text",
                        "source": "static",
                        "text": -5,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM5",[0.19,-0.032],1],
                        "right": ["LevelM5",[0.25,-0.032],1],
                        "down": ["LevelM5",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP5 [Indent level: 5],
                    "levelp5": {
                        "type": "line",
                        "points": [["LevelP5",["-0.16-0.015",0.02],1],["LevelP5",["-0.16-0.015",0],1],["LevelP5",[-0.06,"0.001*9"],1],[],["LevelP5",[0.06,"0.001*9"],1],["LevelP5",["+0.16+0.015",0],1],["LevelP5",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_5 [Indent level: 5],
                    "valp_1_5": {
                        "type": "text",
                        "source": "static",
                        "text": "5",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP5",[-0.19,-0.017],1],
                        "right": ["LevelP5",[-0.13,-0.017],1],
                        "down": ["LevelP5",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_5_R [Indent level: 5],
                    "valp_1_5_r": {
                        "type": "text",
                        "source": "static",
                        "text": "5",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP5",[0.19,-0.017],1],
                        "right": ["LevelP5",[0.25,-0.017],1],
                        "down": ["LevelP5",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM10 [Indent level: 5],
                    "levelm10": {
                        "type": "line",
                        "points": [["LevelM10",[-0.175,-0.02],1],["LevelM10",[-0.175,0],1],[],["LevelM10",[-0.16,"-0.001*1"],1],["LevelM10",[-0.145,"-0.001*2"],1],[],["LevelM10",[-0.13,"-0.001*3"],1],["LevelM10",[-0.115,"-0.001*4"],1],[],["LevelM10",[-0.1,"-0.001*5"],1],["LevelM10",[-0.085,"-0.001*6"],1],[],["LevelM10",[-0.07,"-0.001*7"],1],["LevelM10",[-0.055,"-0.001*8"],1],[],["LevelM10",[-0.04,"-0.001*9"],1],[],["LevelM10",[0.175,-0.02],1],["LevelM10",[0.175,0],1],[],["LevelM10",[0.16,"-0.001*1"],1],["LevelM10",[0.145,"-0.001*2"],1],[],["LevelM10",[0.13,"-0.001*3"],1],["LevelM10",[0.115,"-0.001*4"],1],[],["LevelM10",[0.1,"-0.001*5"],1],["LevelM10",[0.085,"-0.001*6"],1],[],["LevelM10",[0.07,"-0.001*7"],1],["LevelM10",[0.055,"-0.001*8"],1],[],["LevelM10",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_10 [Indent level: 5],
                    "valm_1_10": {
                        "type": "text",
                        "source": "static",
                        "text": -10,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM10",[-0.19,-0.032],1],
                        "right": ["LevelM10",[-0.13,-0.032],1],
                        "down": ["LevelM10",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_10_R [Indent level: 5],
                    "valm_1_10_r": {
                        "type": "text",
                        "source": "static",
                        "text": -10,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM10",[0.19,-0.032],1],
                        "right": ["LevelM10",[0.25,-0.032],1],
                        "down": ["LevelM10",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP10 [Indent level: 5],
                    "levelp10": {
                        "type": "line",
                        "points": [["LevelP10",["-0.16-0.015",0.02],1],["LevelP10",["-0.16-0.015",0],1],["LevelP10",[-0.06,"0.001*9"],1],[],["LevelP10",[0.06,"0.001*9"],1],["LevelP10",["+0.16+0.015",0],1],["LevelP10",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_10 [Indent level: 5],
                    "valp_1_10": {
                        "type": "text",
                        "source": "static",
                        "text": "10",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP10",[-0.19,-0.017],1],
                        "right": ["LevelP10",[-0.13,-0.017],1],
                        "down": ["LevelP10",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_10_R [Indent level: 5],
                    "valp_1_10_r": {
                        "type": "text",
                        "source": "static",
                        "text": "10",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP10",[0.19,-0.017],1],
                        "right": ["LevelP10",[0.25,-0.017],1],
                        "down": ["LevelP10",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM15 [Indent level: 5],
                    "levelm15": {
                        "type": "line",
                        "points": [["LevelM15",[-0.175,-0.02],1],["LevelM15",[-0.175,0],1],[],["LevelM15",[-0.16,"-0.001*1"],1],["LevelM15",[-0.145,"-0.001*2"],1],[],["LevelM15",[-0.13,"-0.001*3"],1],["LevelM15",[-0.115,"-0.001*4"],1],[],["LevelM15",[-0.1,"-0.001*5"],1],["LevelM15",[-0.085,"-0.001*6"],1],[],["LevelM15",[-0.07,"-0.001*7"],1],["LevelM15",[-0.055,"-0.001*8"],1],[],["LevelM15",[-0.04,"-0.001*9"],1],[],["LevelM15",[0.175,-0.02],1],["LevelM15",[0.175,0],1],[],["LevelM15",[0.16,"-0.001*1"],1],["LevelM15",[0.145,"-0.001*2"],1],[],["LevelM15",[0.13,"-0.001*3"],1],["LevelM15",[0.115,"-0.001*4"],1],[],["LevelM15",[0.1,"-0.001*5"],1],["LevelM15",[0.085,"-0.001*6"],1],[],["LevelM15",[0.07,"-0.001*7"],1],["LevelM15",[0.055,"-0.001*8"],1],[],["LevelM15",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_15 [Indent level: 5],
                    "valm_1_15": {
                        "type": "text",
                        "source": "static",
                        "text": -15,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM15",[-0.19,-0.032],1],
                        "right": ["LevelM15",[-0.13,-0.032],1],
                        "down": ["LevelM15",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_15_R [Indent level: 5],
                    "valm_1_15_r": {
                        "type": "text",
                        "source": "static",
                        "text": -15,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM15",[0.19,-0.032],1],
                        "right": ["LevelM15",[0.25,-0.032],1],
                        "down": ["LevelM15",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP15 [Indent level: 5],
                    "levelp15": {
                        "type": "line",
                        "points": [["LevelP15",["-0.16-0.015",0.02],1],["LevelP15",["-0.16-0.015",0],1],["LevelP15",[-0.06,"0.001*9"],1],[],["LevelP15",[0.06,"0.001*9"],1],["LevelP15",["+0.16+0.015",0],1],["LevelP15",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_15 [Indent level: 5],
                    "valp_1_15": {
                        "type": "text",
                        "source": "static",
                        "text": "15",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP15",[-0.19,-0.017],1],
                        "right": ["LevelP15",[-0.13,-0.017],1],
                        "down": ["LevelP15",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_15_R [Indent level: 5],
                    "valp_1_15_r": {
                        "type": "text",
                        "source": "static",
                        "text": "15",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP15",[0.19,-0.017],1],
                        "right": ["LevelP15",[0.25,-0.017],1],
                        "down": ["LevelP15",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM20 [Indent level: 5],
                    "levelm20": {
                        "type": "line",
                        "points": [["LevelM20",[-0.175,-0.02],1],["LevelM20",[-0.175,0],1],[],["LevelM20",[-0.16,"-0.001*1"],1],["LevelM20",[-0.145,"-0.001*2"],1],[],["LevelM20",[-0.13,"-0.001*3"],1],["LevelM20",[-0.115,"-0.001*4"],1],[],["LevelM20",[-0.1,"-0.001*5"],1],["LevelM20",[-0.085,"-0.001*6"],1],[],["LevelM20",[-0.07,"-0.001*7"],1],["LevelM20",[-0.055,"-0.001*8"],1],[],["LevelM20",[-0.04,"-0.001*9"],1],[],["LevelM20",[0.175,-0.02],1],["LevelM20",[0.175,0],1],[],["LevelM20",[0.16,"-0.001*1"],1],["LevelM20",[0.145,"-0.001*2"],1],[],["LevelM20",[0.13,"-0.001*3"],1],["LevelM20",[0.115,"-0.001*4"],1],[],["LevelM20",[0.1,"-0.001*5"],1],["LevelM20",[0.085,"-0.001*6"],1],[],["LevelM20",[0.07,"-0.001*7"],1],["LevelM20",[0.055,"-0.001*8"],1],[],["LevelM20",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_20 [Indent level: 5],
                    "valm_1_20": {
                        "type": "text",
                        "source": "static",
                        "text": -20,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM20",[-0.19,-0.032],1],
                        "right": ["LevelM20",[-0.13,-0.032],1],
                        "down": ["LevelM20",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_20_R [Indent level: 5],
                    "valm_1_20_r": {
                        "type": "text",
                        "source": "static",
                        "text": -20,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM20",[0.19,-0.032],1],
                        "right": ["LevelM20",[0.25,-0.032],1],
                        "down": ["LevelM20",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP20 [Indent level: 5],
                    "levelp20": {
                        "type": "line",
                        "points": [["LevelP20",["-0.16-0.015",0.02],1],["LevelP20",["-0.16-0.015",0],1],["LevelP20",[-0.06,"0.001*9"],1],[],["LevelP20",[0.06,"0.001*9"],1],["LevelP20",["+0.16+0.015",0],1],["LevelP20",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_20 [Indent level: 5],
                    "valp_1_20": {
                        "type": "text",
                        "source": "static",
                        "text": "20",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP20",[-0.19,-0.017],1],
                        "right": ["LevelP20",[-0.13,-0.017],1],
                        "down": ["LevelP20",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_20_R [Indent level: 5],
                    "valp_1_20_r": {
                        "type": "text",
                        "source": "static",
                        "text": "20",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP20",[0.19,-0.017],1],
                        "right": ["LevelP20",[0.25,-0.017],1],
                        "down": ["LevelP20",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM25 [Indent level: 5],
                    "levelm25": {
                        "type": "line",
                        "points": [["LevelM25",[-0.175,-0.02],1],["LevelM25",[-0.175,0],1],[],["LevelM25",[-0.16,"-0.001*1"],1],["LevelM25",[-0.145,"-0.001*2"],1],[],["LevelM25",[-0.13,"-0.001*3"],1],["LevelM25",[-0.115,"-0.001*4"],1],[],["LevelM25",[-0.1,"-0.001*5"],1],["LevelM25",[-0.085,"-0.001*6"],1],[],["LevelM25",[-0.07,"-0.001*7"],1],["LevelM25",[-0.055,"-0.001*8"],1],[],["LevelM25",[-0.04,"-0.001*9"],1],[],["LevelM25",[0.175,-0.02],1],["LevelM25",[0.175,0],1],[],["LevelM25",[0.16,"-0.001*1"],1],["LevelM25",[0.145,"-0.001*2"],1],[],["LevelM25",[0.13,"-0.001*3"],1],["LevelM25",[0.115,"-0.001*4"],1],[],["LevelM25",[0.1,"-0.001*5"],1],["LevelM25",[0.085,"-0.001*6"],1],[],["LevelM25",[0.07,"-0.001*7"],1],["LevelM25",[0.055,"-0.001*8"],1],[],["LevelM25",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_25 [Indent level: 5],
                    "valm_1_25": {
                        "type": "text",
                        "source": "static",
                        "text": -25,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM25",[-0.19,-0.032],1],
                        "right": ["LevelM25",[-0.13,-0.032],1],
                        "down": ["LevelM25",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_25_R [Indent level: 5],
                    "valm_1_25_r": {
                        "type": "text",
                        "source": "static",
                        "text": -25,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM25",[0.19,-0.032],1],
                        "right": ["LevelM25",[0.25,-0.032],1],
                        "down": ["LevelM25",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP25 [Indent level: 5],
                    "levelp25": {
                        "type": "line",
                        "points": [["LevelP25",["-0.16-0.015",0.02],1],["LevelP25",["-0.16-0.015",0],1],["LevelP25",[-0.06,"0.001*9"],1],[],["LevelP25",[0.06,"0.001*9"],1],["LevelP25",["+0.16+0.015",0],1],["LevelP25",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_25 [Indent level: 5],
                    "valp_1_25": {
                        "type": "text",
                        "source": "static",
                        "text": "25",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP25",[-0.19,-0.017],1],
                        "right": ["LevelP25",[-0.13,-0.017],1],
                        "down": ["LevelP25",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_25_R [Indent level: 5],
                    "valp_1_25_r": {
                        "type": "text",
                        "source": "static",
                        "text": "25",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP25",[0.19,-0.017],1],
                        "right": ["LevelP25",[0.25,-0.017],1],
                        "down": ["LevelP25",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM30 [Indent level: 5],
                    "levelm30": {
                        "type": "line",
                        "points": [["LevelM30",[-0.175,-0.02],1],["LevelM30",[-0.175,0],1],[],["LevelM30",[-0.16,"-0.001*1"],1],["LevelM30",[-0.145,"-0.001*2"],1],[],["LevelM30",[-0.13,"-0.001*3"],1],["LevelM30",[-0.115,"-0.001*4"],1],[],["LevelM30",[-0.1,"-0.001*5"],1],["LevelM30",[-0.085,"-0.001*6"],1],[],["LevelM30",[-0.07,"-0.001*7"],1],["LevelM30",[-0.055,"-0.001*8"],1],[],["LevelM30",[-0.04,"-0.001*9"],1],[],["LevelM30",[0.175,-0.02],1],["LevelM30",[0.175,0],1],[],["LevelM30",[0.16,"-0.001*1"],1],["LevelM30",[0.145,"-0.001*2"],1],[],["LevelM30",[0.13,"-0.001*3"],1],["LevelM30",[0.115,"-0.001*4"],1],[],["LevelM30",[0.1,"-0.001*5"],1],["LevelM30",[0.085,"-0.001*6"],1],[],["LevelM30",[0.07,"-0.001*7"],1],["LevelM30",[0.055,"-0.001*8"],1],[],["LevelM30",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_30 [Indent level: 5],
                    "valm_1_30": {
                        "type": "text",
                        "source": "static",
                        "text": -30,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM30",[-0.19,-0.032],1],
                        "right": ["LevelM30",[-0.13,-0.032],1],
                        "down": ["LevelM30",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_30_R [Indent level: 5],
                    "valm_1_30_r": {
                        "type": "text",
                        "source": "static",
                        "text": -30,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM30",[0.19,-0.032],1],
                        "right": ["LevelM30",[0.25,-0.032],1],
                        "down": ["LevelM30",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP30 [Indent level: 5],
                    "levelp30": {
                        "type": "line",
                        "points": [["LevelP30",["-0.16-0.015",0.02],1],["LevelP30",["-0.16-0.015",0],1],["LevelP30",[-0.06,"0.001*9"],1],[],["LevelP30",[0.06,"0.001*9"],1],["LevelP30",["+0.16+0.015",0],1],["LevelP30",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_30 [Indent level: 5],
                    "valp_1_30": {
                        "type": "text",
                        "source": "static",
                        "text": "30",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP30",[-0.19,-0.017],1],
                        "right": ["LevelP30",[-0.13,-0.017],1],
                        "down": ["LevelP30",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_30_R [Indent level: 5],
                    "valp_1_30_r": {
                        "type": "text",
                        "source": "static",
                        "text": "30",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP30",[0.19,-0.017],1],
                        "right": ["LevelP30",[0.25,-0.017],1],
                        "down": ["LevelP30",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM35 [Indent level: 5],
                    "levelm35": {
                        "type": "line",
                        "points": [["LevelM35",[-0.175,-0.02],1],["LevelM35",[-0.175,0],1],[],["LevelM35",[-0.16,"-0.001*1"],1],["LevelM35",[-0.145,"-0.001*2"],1],[],["LevelM35",[-0.13,"-0.001*3"],1],["LevelM35",[-0.115,"-0.001*4"],1],[],["LevelM35",[-0.1,"-0.001*5"],1],["LevelM35",[-0.085,"-0.001*6"],1],[],["LevelM35",[-0.07,"-0.001*7"],1],["LevelM35",[-0.055,"-0.001*8"],1],[],["LevelM35",[-0.04,"-0.001*9"],1],[],["LevelM35",[0.175,-0.02],1],["LevelM35",[0.175,0],1],[],["LevelM35",[0.16,"-0.001*1"],1],["LevelM35",[0.145,"-0.001*2"],1],[],["LevelM35",[0.13,"-0.001*3"],1],["LevelM35",[0.115,"-0.001*4"],1],[],["LevelM35",[0.1,"-0.001*5"],1],["LevelM35",[0.085,"-0.001*6"],1],[],["LevelM35",[0.07,"-0.001*7"],1],["LevelM35",[0.055,"-0.001*8"],1],[],["LevelM35",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_35 [Indent level: 5],
                    "valm_1_35": {
                        "type": "text",
                        "source": "static",
                        "text": -35,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM35",[-0.19,-0.032],1],
                        "right": ["LevelM35",[-0.13,-0.032],1],
                        "down": ["LevelM35",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_35_R [Indent level: 5],
                    "valm_1_35_r": {
                        "type": "text",
                        "source": "static",
                        "text": -35,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM35",[0.19,-0.032],1],
                        "right": ["LevelM35",[0.25,-0.032],1],
                        "down": ["LevelM35",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP35 [Indent level: 5],
                    "levelp35": {
                        "type": "line",
                        "points": [["LevelP35",["-0.16-0.015",0.02],1],["LevelP35",["-0.16-0.015",0],1],["LevelP35",[-0.06,"0.001*9"],1],[],["LevelP35",[0.06,"0.001*9"],1],["LevelP35",["+0.16+0.015",0],1],["LevelP35",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_35 [Indent level: 5],
                    "valp_1_35": {
                        "type": "text",
                        "source": "static",
                        "text": "35",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP35",[-0.19,-0.017],1],
                        "right": ["LevelP35",[-0.13,-0.017],1],
                        "down": ["LevelP35",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_35_R [Indent level: 5],
                    "valp_1_35_r": {
                        "type": "text",
                        "source": "static",
                        "text": "35",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP35",[0.19,-0.017],1],
                        "right": ["LevelP35",[0.25,-0.017],1],
                        "down": ["LevelP35",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM40 [Indent level: 5],
                    "levelm40": {
                        "type": "line",
                        "points": [["LevelM40",[-0.175,-0.02],1],["LevelM40",[-0.175,0],1],[],["LevelM40",[-0.16,"-0.001*1"],1],["LevelM40",[-0.145,"-0.001*2"],1],[],["LevelM40",[-0.13,"-0.001*3"],1],["LevelM40",[-0.115,"-0.001*4"],1],[],["LevelM40",[-0.1,"-0.001*5"],1],["LevelM40",[-0.085,"-0.001*6"],1],[],["LevelM40",[-0.07,"-0.001*7"],1],["LevelM40",[-0.055,"-0.001*8"],1],[],["LevelM40",[-0.04,"-0.001*9"],1],[],["LevelM40",[0.175,-0.02],1],["LevelM40",[0.175,0],1],[],["LevelM40",[0.16,"-0.001*1"],1],["LevelM40",[0.145,"-0.001*2"],1],[],["LevelM40",[0.13,"-0.001*3"],1],["LevelM40",[0.115,"-0.001*4"],1],[],["LevelM40",[0.1,"-0.001*5"],1],["LevelM40",[0.085,"-0.001*6"],1],[],["LevelM40",[0.07,"-0.001*7"],1],["LevelM40",[0.055,"-0.001*8"],1],[],["LevelM40",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_40 [Indent level: 5],
                    "valm_1_40": {
                        "type": "text",
                        "source": "static",
                        "text": -40,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM40",[-0.19,-0.032],1],
                        "right": ["LevelM40",[-0.13,-0.032],1],
                        "down": ["LevelM40",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_40_R [Indent level: 5],
                    "valm_1_40_r": {
                        "type": "text",
                        "source": "static",
                        "text": -40,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM40",[0.19,-0.032],1],
                        "right": ["LevelM40",[0.25,-0.032],1],
                        "down": ["LevelM40",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP40 [Indent level: 5],
                    "levelp40": {
                        "type": "line",
                        "points": [["LevelP40",["-0.16-0.015",0.02],1],["LevelP40",["-0.16-0.015",0],1],["LevelP40",[-0.06,"0.001*9"],1],[],["LevelP40",[0.06,"0.001*9"],1],["LevelP40",["+0.16+0.015",0],1],["LevelP40",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_40 [Indent level: 5],
                    "valp_1_40": {
                        "type": "text",
                        "source": "static",
                        "text": "40",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP40",[-0.19,-0.017],1],
                        "right": ["LevelP40",[-0.13,-0.017],1],
                        "down": ["LevelP40",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_40_R [Indent level: 5],
                    "valp_1_40_r": {
                        "type": "text",
                        "source": "static",
                        "text": "40",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP40",[0.19,-0.017],1],
                        "right": ["LevelP40",[0.25,-0.017],1],
                        "down": ["LevelP40",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM45 [Indent level: 5],
                    "levelm45": {
                        "type": "line",
                        "points": [["LevelM45",[-0.175,-0.02],1],["LevelM45",[-0.175,0],1],[],["LevelM45",[-0.16,"-0.001*1"],1],["LevelM45",[-0.145,"-0.001*2"],1],[],["LevelM45",[-0.13,"-0.001*3"],1],["LevelM45",[-0.115,"-0.001*4"],1],[],["LevelM45",[-0.1,"-0.001*5"],1],["LevelM45",[-0.085,"-0.001*6"],1],[],["LevelM45",[-0.07,"-0.001*7"],1],["LevelM45",[-0.055,"-0.001*8"],1],[],["LevelM45",[-0.04,"-0.001*9"],1],[],["LevelM45",[0.175,-0.02],1],["LevelM45",[0.175,0],1],[],["LevelM45",[0.16,"-0.001*1"],1],["LevelM45",[0.145,"-0.001*2"],1],[],["LevelM45",[0.13,"-0.001*3"],1],["LevelM45",[0.115,"-0.001*4"],1],[],["LevelM45",[0.1,"-0.001*5"],1],["LevelM45",[0.085,"-0.001*6"],1],[],["LevelM45",[0.07,"-0.001*7"],1],["LevelM45",[0.055,"-0.001*8"],1],[],["LevelM45",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_45 [Indent level: 5],
                    "valm_1_45": {
                        "type": "text",
                        "source": "static",
                        "text": -45,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM45",[-0.19,-0.032],1],
                        "right": ["LevelM45",[-0.13,-0.032],1],
                        "down": ["LevelM45",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_45_R [Indent level: 5],
                    "valm_1_45_r": {
                        "type": "text",
                        "source": "static",
                        "text": -45,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM45",[0.19,-0.032],1],
                        "right": ["LevelM45",[0.25,-0.032],1],
                        "down": ["LevelM45",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP45 [Indent level: 5],
                    "levelp45": {
                        "type": "line",
                        "points": [["LevelP45",["-0.16-0.015",0.02],1],["LevelP45",["-0.16-0.015",0],1],["LevelP45",[-0.06,"0.001*9"],1],[],["LevelP45",[0.06,"0.001*9"],1],["LevelP45",["+0.16+0.015",0],1],["LevelP45",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_45 [Indent level: 5],
                    "valp_1_45": {
                        "type": "text",
                        "source": "static",
                        "text": "45",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP45",[-0.19,-0.017],1],
                        "right": ["LevelP45",[-0.13,-0.017],1],
                        "down": ["LevelP45",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_45_R [Indent level: 5],
                    "valp_1_45_r": {
                        "type": "text",
                        "source": "static",
                        "text": "45",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP45",[0.19,-0.017],1],
                        "right": ["LevelP45",[0.25,-0.017],1],
                        "down": ["LevelP45",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM50 [Indent level: 5],
                    "levelm50": {
                        "type": "line",
                        "points": [["LevelM50",[-0.175,-0.02],1],["LevelM50",[-0.175,0],1],[],["LevelM50",[-0.16,"-0.001*1"],1],["LevelM50",[-0.145,"-0.001*2"],1],[],["LevelM50",[-0.13,"-0.001*3"],1],["LevelM50",[-0.115,"-0.001*4"],1],[],["LevelM50",[-0.1,"-0.001*5"],1],["LevelM50",[-0.085,"-0.001*6"],1],[],["LevelM50",[-0.07,"-0.001*7"],1],["LevelM50",[-0.055,"-0.001*8"],1],[],["LevelM50",[-0.04,"-0.001*9"],1],[],["LevelM50",[0.175,-0.02],1],["LevelM50",[0.175,0],1],[],["LevelM50",[0.16,"-0.001*1"],1],["LevelM50",[0.145,"-0.001*2"],1],[],["LevelM50",[0.13,"-0.001*3"],1],["LevelM50",[0.115,"-0.001*4"],1],[],["LevelM50",[0.1,"-0.001*5"],1],["LevelM50",[0.085,"-0.001*6"],1],[],["LevelM50",[0.07,"-0.001*7"],1],["LevelM50",[0.055,"-0.001*8"],1],[],["LevelM50",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_50 [Indent level: 5],
                    "valm_1_50": {
                        "type": "text",
                        "source": "static",
                        "text": -50,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM50",[-0.19,-0.032],1],
                        "right": ["LevelM50",[-0.13,-0.032],1],
                        "down": ["LevelM50",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_50_R [Indent level: 5],
                    "valm_1_50_r": {
                        "type": "text",
                        "source": "static",
                        "text": -50,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM50",[0.19,-0.032],1],
                        "right": ["LevelM50",[0.25,-0.032],1],
                        "down": ["LevelM50",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP50 [Indent level: 5],
                    "levelp50": {
                        "type": "line",
                        "points": [["LevelP50",["-0.16-0.015",0.02],1],["LevelP50",["-0.16-0.015",0],1],["LevelP50",[-0.06,"0.001*9"],1],[],["LevelP50",[0.06,"0.001*9"],1],["LevelP50",["+0.16+0.015",0],1],["LevelP50",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_50 [Indent level: 5],
                    "valp_1_50": {
                        "type": "text",
                        "source": "static",
                        "text": "50",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP50",[-0.19,-0.017],1],
                        "right": ["LevelP50",[-0.13,-0.017],1],
                        "down": ["LevelP50",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_50_R [Indent level: 5],
                    "valp_1_50_r": {
                        "type": "text",
                        "source": "static",
                        "text": "50",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP50",[0.19,-0.017],1],
                        "right": ["LevelP50",[0.25,-0.017],1],
                        "down": ["LevelP50",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM60 [Indent level: 5],
                    "levelm60": {
                        "type": "line",
                        "points": [["LevelM60",[-0.175,-0.02],1],["LevelM60",[-0.175,0],1],[],["LevelM60",[-0.16,"-0.001*1"],1],["LevelM60",[-0.145,"-0.001*2"],1],[],["LevelM60",[-0.13,"-0.001*3"],1],["LevelM60",[-0.115,"-0.001*4"],1],[],["LevelM60",[-0.1,"-0.001*5"],1],["LevelM60",[-0.085,"-0.001*6"],1],[],["LevelM60",[-0.07,"-0.001*7"],1],["LevelM60",[-0.055,"-0.001*8"],1],[],["LevelM60",[-0.04,"-0.001*9"],1],[],["LevelM60",[0.175,-0.02],1],["LevelM60",[0.175,0],1],[],["LevelM60",[0.16,"-0.001*1"],1],["LevelM60",[0.145,"-0.001*2"],1],[],["LevelM60",[0.13,"-0.001*3"],1],["LevelM60",[0.115,"-0.001*4"],1],[],["LevelM60",[0.1,"-0.001*5"],1],["LevelM60",[0.085,"-0.001*6"],1],[],["LevelM60",[0.07,"-0.001*7"],1],["LevelM60",[0.055,"-0.001*8"],1],[],["LevelM60",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_60 [Indent level: 5],
                    "valm_1_60": {
                        "type": "text",
                        "source": "static",
                        "text": -60,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM60",[-0.19,-0.032],1],
                        "right": ["LevelM60",[-0.13,-0.032],1],
                        "down": ["LevelM60",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_60_R [Indent level: 5],
                    "valm_1_60_r": {
                        "type": "text",
                        "source": "static",
                        "text": -60,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM60",[0.19,-0.032],1],
                        "right": ["LevelM60",[0.25,-0.032],1],
                        "down": ["LevelM60",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP60 [Indent level: 5],
                    "levelp60": {
                        "type": "line",
                        "points": [["LevelP60",["-0.16-0.015",0.02],1],["LevelP60",["-0.16-0.015",0],1],["LevelP60",[-0.06,"0.001*9"],1],[],["LevelP60",[0.06,"0.001*9"],1],["LevelP60",["+0.16+0.015",0],1],["LevelP60",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_60 [Indent level: 5],
                    "valp_1_60": {
                        "type": "text",
                        "source": "static",
                        "text": "60",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP60",[-0.19,-0.017],1],
                        "right": ["LevelP60",[-0.13,-0.017],1],
                        "down": ["LevelP60",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_60_R [Indent level: 5],
                    "valp_1_60_r": {
                        "type": "text",
                        "source": "static",
                        "text": "60",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP60",[0.19,-0.017],1],
                        "right": ["LevelP60",[0.25,-0.017],1],
                        "down": ["LevelP60",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM70 [Indent level: 5],
                    "levelm70": {
                        "type": "line",
                        "points": [["LevelM70",[-0.175,-0.02],1],["LevelM70",[-0.175,0],1],[],["LevelM70",[-0.16,"-0.001*1"],1],["LevelM70",[-0.145,"-0.001*2"],1],[],["LevelM70",[-0.13,"-0.001*3"],1],["LevelM70",[-0.115,"-0.001*4"],1],[],["LevelM70",[-0.1,"-0.001*5"],1],["LevelM70",[-0.085,"-0.001*6"],1],[],["LevelM70",[-0.07,"-0.001*7"],1],["LevelM70",[-0.055,"-0.001*8"],1],[],["LevelM70",[-0.04,"-0.001*9"],1],[],["LevelM70",[0.175,-0.02],1],["LevelM70",[0.175,0],1],[],["LevelM70",[0.16,"-0.001*1"],1],["LevelM70",[0.145,"-0.001*2"],1],[],["LevelM70",[0.13,"-0.001*3"],1],["LevelM70",[0.115,"-0.001*4"],1],[],["LevelM70",[0.1,"-0.001*5"],1],["LevelM70",[0.085,"-0.001*6"],1],[],["LevelM70",[0.07,"-0.001*7"],1],["LevelM70",[0.055,"-0.001*8"],1],[],["LevelM70",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_70 [Indent level: 5],
                    "valm_1_70": {
                        "type": "text",
                        "source": "static",
                        "text": -70,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM70",[-0.19,-0.032],1],
                        "right": ["LevelM70",[-0.13,-0.032],1],
                        "down": ["LevelM70",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_70_R [Indent level: 5],
                    "valm_1_70_r": {
                        "type": "text",
                        "source": "static",
                        "text": -70,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM70",[0.19,-0.032],1],
                        "right": ["LevelM70",[0.25,-0.032],1],
                        "down": ["LevelM70",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP70 [Indent level: 5],
                    "levelp70": {
                        "type": "line",
                        "points": [["LevelP70",["-0.16-0.015",0.02],1],["LevelP70",["-0.16-0.015",0],1],["LevelP70",[-0.06,"0.001*9"],1],[],["LevelP70",[0.06,"0.001*9"],1],["LevelP70",["+0.16+0.015",0],1],["LevelP70",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_70 [Indent level: 5],
                    "valp_1_70": {
                        "type": "text",
                        "source": "static",
                        "text": "70",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP70",[-0.19,-0.017],1],
                        "right": ["LevelP70",[-0.13,-0.017],1],
                        "down": ["LevelP70",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_70_R [Indent level: 5],
                    "valp_1_70_r": {
                        "type": "text",
                        "source": "static",
                        "text": "70",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP70",[0.19,-0.017],1],
                        "right": ["LevelP70",[0.25,-0.017],1],
                        "down": ["LevelP70",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM80 [Indent level: 5],
                    "levelm80": {
                        "type": "line",
                        "points": [["LevelM80",[-0.175,-0.02],1],["LevelM80",[-0.175,0],1],[],["LevelM80",[-0.16,"-0.001*1"],1],["LevelM80",[-0.145,"-0.001*2"],1],[],["LevelM80",[-0.13,"-0.001*3"],1],["LevelM80",[-0.115,"-0.001*4"],1],[],["LevelM80",[-0.1,"-0.001*5"],1],["LevelM80",[-0.085,"-0.001*6"],1],[],["LevelM80",[-0.07,"-0.001*7"],1],["LevelM80",[-0.055,"-0.001*8"],1],[],["LevelM80",[-0.04,"-0.001*9"],1],[],["LevelM80",[0.175,-0.02],1],["LevelM80",[0.175,0],1],[],["LevelM80",[0.16,"-0.001*1"],1],["LevelM80",[0.145,"-0.001*2"],1],[],["LevelM80",[0.13,"-0.001*3"],1],["LevelM80",[0.115,"-0.001*4"],1],[],["LevelM80",[0.1,"-0.001*5"],1],["LevelM80",[0.085,"-0.001*6"],1],[],["LevelM80",[0.07,"-0.001*7"],1],["LevelM80",[0.055,"-0.001*8"],1],[],["LevelM80",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_80 [Indent level: 5],
                    "valm_1_80": {
                        "type": "text",
                        "source": "static",
                        "text": -80,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM80",[-0.19,-0.032],1],
                        "right": ["LevelM80",[-0.13,-0.032],1],
                        "down": ["LevelM80",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_80_R [Indent level: 5],
                    "valm_1_80_r": {
                        "type": "text",
                        "source": "static",
                        "text": -80,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM80",[0.19,-0.032],1],
                        "right": ["LevelM80",[0.25,-0.032],1],
                        "down": ["LevelM80",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP80 [Indent level: 5],
                    "levelp80": {
                        "type": "line",
                        "points": [["LevelP80",["-0.16-0.015",0.02],1],["LevelP80",["-0.16-0.015",0],1],["LevelP80",[-0.06,"0.001*9"],1],[],["LevelP80",[0.06,"0.001*9"],1],["LevelP80",["+0.16+0.015",0],1],["LevelP80",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_80 [Indent level: 5],
                    "valp_1_80": {
                        "type": "text",
                        "source": "static",
                        "text": "80",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP80",[-0.19,-0.017],1],
                        "right": ["LevelP80",[-0.13,-0.017],1],
                        "down": ["LevelP80",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_80_R [Indent level: 5],
                    "valp_1_80_r": {
                        "type": "text",
                        "source": "static",
                        "text": "80",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP80",[0.19,-0.017],1],
                        "right": ["LevelP80",[0.25,-0.017],1],
                        "down": ["LevelP80",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelM90 [Indent level: 5],
                    "levelm90": {
                        "type": "line",
                        "points": [["LevelM90",[-0.175,-0.02],1],["LevelM90",[-0.175,0],1],[],["LevelM90",[-0.16,"-0.001*1"],1],["LevelM90",[-0.145,"-0.001*2"],1],[],["LevelM90",[-0.13,"-0.001*3"],1],["LevelM90",[-0.115,"-0.001*4"],1],[],["LevelM90",[-0.1,"-0.001*5"],1],["LevelM90",[-0.085,"-0.001*6"],1],[],["LevelM90",[-0.07,"-0.001*7"],1],["LevelM90",[-0.055,"-0.001*8"],1],[],["LevelM90",[-0.04,"-0.001*9"],1],[],["LevelM90",[0.175,-0.02],1],["LevelM90",[0.175,0],1],[],["LevelM90",[0.16,"-0.001*1"],1],["LevelM90",[0.145,"-0.001*2"],1],[],["LevelM90",[0.13,"-0.001*3"],1],["LevelM90",[0.115,"-0.001*4"],1],[],["LevelM90",[0.1,"-0.001*5"],1],["LevelM90",[0.085,"-0.001*6"],1],[],["LevelM90",[0.07,"-0.001*7"],1],["LevelM90",[0.055,"-0.001*8"],1],[],["LevelM90",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_90 [Indent level: 5],
                    "valm_1_90": {
                        "type": "text",
                        "source": "static",
                        "text": -90,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM90",[-0.19,-0.032],1],
                        "right": ["LevelM90",[-0.13,-0.032],1],
                        "down": ["LevelM90",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALM_1_90_R [Indent level: 5],
                    "valm_1_90_r": {
                        "type": "text",
                        "source": "static",
                        "text": -90,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelM90",[0.19,-0.032],1],
                        "right": ["LevelM90",[0.25,-0.032],1],
                        "down": ["LevelM90",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|LevelP90 [Indent level: 5],
                    "levelp90": {
                        "type": "line",
                        "points": [["LevelP90",["-0.16-0.015",0.02],1],["LevelP90",["-0.16-0.015",0],1],["LevelP90",[-0.06,"0.001*9"],1],[],["LevelP90",[0.06,"0.001*9"],1],["LevelP90",["+0.16+0.015",0],1],["LevelP90",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_90 [Indent level: 5],
                    "valp_1_90": {
                        "type": "text",
                        "source": "static",
                        "text": "90",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP90",[-0.19,-0.017],1],
                        "right": ["LevelP90",[-0.13,-0.017],1],
                        "down": ["LevelP90",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|Horizont|VALP_1_90_R [Indent level: 5],
                    "valp_1_90_r": {
                        "type": "text",
                        "source": "static",
                        "text": "90",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP90",[0.19,-0.017],1],
                        "right": ["LevelP90",[0.25,-0.017],1],
                        "down": ["LevelP90",[0.19,0.033],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|SpeedNumber [Indent level: 4],
                "speednumber": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 3.6,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.1,0.424107],1],
                    "right": [[0.16,0.424107],1],
                    "down": [[0.1,0.46875],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AltNumber [Indent level: 4],
                "altnumber": {
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "pos": [[0.9,0.424107],1],
                    "right": [[0.96,0.424107],1],
                    "down": [[0.9,0.46875],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|MachText [Indent level: 4],
                "machtext": {
                    "type": "text",
                    "source": "static",
                    "align": "left",
                    "text": "M",
                    "scale": 1,
                    "pos": [[0.1,0.63],1],
                    "right": [[0.15,0.63],1],
                    "down": [[0.1,0.68],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|MachNumber [Indent level: 4],
                "machnumber": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 0.002939,
                    "sourceprecision": 2,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.12,0.63],1],
                    "right": [[0.17,0.63],1],
                    "down": [[0.12,0.68],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|GmeterText [Indent level: 4],
                "gmetertext": {
                    "type": "text",
                    "source": "static",
                    "align": "left",
                    "text": "G",
                    "scale": 1,
                    "pos": [[0.1,0.7],1],
                    "right": [[0.15,0.7],1],
                    "down": [[0.1,0.75],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|GmeterNumber [Indent level: 4],
                "gmeternumber": {
                    "type": "text",
                    "source": "gmeter",
                    "sourcescale": 0.3,
                    "sourceprecision": 1,
                    "refreshrate": 0.4,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.12,0.7],1],
                    "right": [[0.17,0.7],1],
                    "down": [[0.12,0.75],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|PitchNumber [Indent level: 4],
                "pitchnumber": {
                    "type": "text",
                    "source": "aoa",
                    "sourcescale": 57.2958,
                    "sourceprecision": 1,
                    "refreshrate": 0.4,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.12,0.74],1],
                    "right": [[0.17,0.74],1],
                    "down": [[0.12,0.79],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarATLText [Indent level: 4],
                "radaratltext": {
                    "type": "text",
                    "source": "static",
                    "align": "left",
                    "text": "R",
                    "scale": 1,
                    "pos": [[0.85,0.55],1],
                    "right": [[0.9,0.55],1],
                    "down": [[0.85,0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarATLNumber [Indent level: 4],
                "radaratlnumber": {
                    "type": "text",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "sourceoffset": -2,
                    "sourceprecision": 0,
                    "refreshrate": 0.01,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.87,0.55],1],
                    "right": [[0.92,0.55],1],
                    "down": [[0.87,0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|HeadingNumber [Indent level: 4],
                "headingnumber": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.5,0.14],1],
                    "right": [[0.57,0.14],1],
                    "down": [[0.5,0.21],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|HeadingArrows [Indent level: 4],
                "headingarrows": {
                    "type": "line",
                    "width": 3,
                    "points": [[[0.45,0.2],1],[[0.55,0.2],1],[[0.55,0.157143],1],[[0.45,0.157143],1],[[0.45,0.2],1],[],["WPPoint",1,"LimitWaypoint",1,[-0.011,0.13],1],["WPPoint",1,"LimitWaypoint",1,[-0.011,0.152],1],[],["WPPoint",1,"LimitWaypoint",1,[0.011,0.13],1],["WPPoint",1,"LimitWaypoint",1,[0.011,0.152],1]]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],
                "headingscale": {
                    "type": "scale",
                    "horizontal": 1,
                    "source": "heading",
                    "sourcescale": 0.1,
                    "sourcelength": 2,
                    "width": 4,
                    "top": 0.3,
                    "center": 0.5,
                    "bottom": 0.7,
                    "linexleft": 0.22,
                    "lineyright": 0.2,
                    "linexleftmajor": 0.23,
                    "lineyrightmajor": 0.2,
                    "majorlineeach": 2,
                    "numbereach": 0,
                    "step": 0.5,
                    "stepsize": 0.0555556,
                    "align": "center",
                    "scale": 1,
                    "pos": [0.295,0.165],
                    "right": [0.335,0.165],
                    "down": [0.295,0.205]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|HeadingScale_Left [Indent level: 4],
                "headingscale_left": {
                    "cliptl": [0,0],
                    "clipbr": [0.45,1],
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|HeadingScale_Left|HeadingScale [Indent level: 5],
                    "headingscale": {
                        "linexleft": 0,
                        "lineyright": 0,
                        "linexleftmajor": 0,
                        "lineyrightmajor": 0,
                        "numbereach": 2,
                        "type": "scale",
                        "horizontal": 1,
                        "source": "heading",
                        "sourcescale": 0.1,
                        "sourcelength": 2,
                        "width": 4,
                        "top": 0.3,
                        "center": 0.5,
                        "bottom": 0.7,
                        "majorlineeach": 2,
                        "step": 0.5,
                        "stepsize": 0.0555556,
                        "align": "center",
                        "scale": 1,
                        "pos": [0.295,0.165],
                        "right": [0.335,0.165],
                        "down": [0.295,0.205]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|HeadingScale_Right [Indent level: 4],
                "headingscale_right": {
                    "cliptl": [0.55,0],
                    "clipbr": [1,1],
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|HeadingScale_Right|HeadingScale [Indent level: 5],
                    "headingscale": {
                        "linexleft": 0,
                        "lineyright": 0,
                        "linexleftmajor": 0,
                        "lineyrightmajor": 0,
                        "numbereach": 2,
                        "type": "scale",
                        "horizontal": 1,
                        "source": "heading",
                        "sourcescale": 0.1,
                        "sourcelength": 2,
                        "width": 4,
                        "top": 0.3,
                        "center": 0.5,
                        "bottom": 0.7,
                        "majorlineeach": 2,
                        "step": 0.5,
                        "stepsize": 0.0555556,
                        "align": "center",
                        "scale": 1,
                        "pos": [0.295,0.165],
                        "right": [0.335,0.165],
                        "down": [0.295,0.205]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|ThrustNumber [Indent level: 4],
                "thrustnumber": {
                    "type": "text",
                    "source": "throttle",
                    "sourcescale": 100,
                    "sourcelength": 3,
                    "sourceoffset": 0,
                    "sourceprecision": 0,
                    "refreshrate": 0.01,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.15,0.89],1],
                    "right": [[0.2,0.89],1],
                    "down": [[0.15,0.94],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|NavigationMode [Indent level: 4],
                "navigationmode": {
                    "condition": "1-(AAmissile+mgun+bomb)",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|NavigationMode|ModeText [Indent level: 5],
                    "modetext": {
                        "type": "text",
                        "source": "static",
                        "align": "left",
                        "text": "NAV",
                        "scale": 1,
                        "pos": [[0.15,0.85],1],
                        "right": [[0.2,0.85],1],
                        "down": [[0.15,0.9],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|NavigationMode|WP [Indent level: 5],
                    "wp": {
                        "condition": "wpvalid",
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|NavigationMode|WP|WPdist [Indent level: 6],
                        "wpdist": {
                            "type": "text",
                            "source": "wpdist",
                            "sourcescale": 0.001,
                            "sourceprecision": 1,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.795,0.82],1],
                            "right": [[0.855,0.82],1],
                            "down": [[0.795,0.88],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|NavigationMode|WP|WPIndex [Indent level: 6],
                        "wpindex": {
                            "type": "text",
                            "source": "wpIndex",
                            "sourcescale": 1,
                            "sourcelength": 2,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.725,0.82],1],
                            "right": [[0.785,0.82],1],
                            "down": [[0.725,0.88],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|NavigationMode|WP|WPstatic [Indent level: 6],
                        "wpstatic": {
                            "type": "text",
                            "source": "static",
                            "text": "/",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "right",
                            "pos": [[0.765,0.82],1],
                            "right": [[0.825,0.82],1],
                            "down": [[0.765,0.88],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|NavigationMode|WP|WPTime [Indent level: 6],
                        "wptime": {
                            "type": "text",
                            "source": "static",
                            "text": ":14:36/-00:0",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "right",
                            "pos": [[0.725,0.865],1],
                            "right": [[0.785,0.865],1],
                            "down": [[0.725,0.925],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|NavigationMode|WP|WPCurrentTime [Indent level: 6],
                        "wpcurrenttime": {
                            "source": "time",
                            "text": "%X",
                            "align": "right",
                            "pos": [[0.725,0.91],1],
                            "right": [[0.785,0.91],1],
                            "down": [[0.725,0.97],1],
                            "type": "text",
                            "sourcescale": 0.001,
                            "sourceprecision": 1,
                            "scale": 1
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|NavigationMode|WP|WP [Indent level: 6],
                        "wp": {
                            "width": 1,
                            "type": "line",
                            "points": [["wppoint",[0,-0.00892857],1],["wppoint",[0.005,-0.00773214],1],["wppoint",[0.00866,-0.00446429],1],["wppoint",[0.01,0],1],["wppoint",[0.00866,0.00446429],1],["wppoint",[0.005,0.00773214],1],["wppoint",[0,0.00892857],1],["wppoint",[-0.005,0.00773214],1],["wppoint",[-0.00866,0.00446429],1],["wppoint",[-0.01,0],1],["wppoint",[-0.00866,-0.00446429],1],["wppoint",[-0.005,-0.00773214],1],["wppoint",[0,-0.00892857],1],[],["wppoint",1,["HorizonBankRotFull",0,-0.01],1],["wppoint",1,["HorizonBankRotFull",0,-0.023],1]]
                        }
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup [Indent level: 4],
                "aamissilecrosshairgroup": {
                    "type": "group",
                    "condition": "AAmissile",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|ModeText [Indent level: 5],
                    "modetext": {
                        "type": "text",
                        "source": "static",
                        "align": "left",
                        "text": "MSL",
                        "scale": 1,
                        "pos": [[0.15,0.85],1],
                        "right": [[0.2,0.85],1],
                        "down": [[0.15,0.9],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|AAMissileCrosshair [Indent level: 5],
                    "aamissilecrosshair": {
                        "type": "line",
                        "width": 4,
                        "points": [["PlaneW",[0,-0.25],1],["PlaneW",[0.048608,-0.2462],1],["PlaneW",[0.09576,-0.234925],1],["PlaneW",[0.14,-0.2165],1],[],["PlaneW",[0.179984,-0.1915],1],["PlaneW",[0.21448,-0.1607],1],["PlaneW",[0.24248,-0.125],1],["PlaneW",[0.263116,-0.0855],1],[],["PlaneW",[0.275744,-0.0434],1],["PlaneW",[0.28,0],1],["PlaneW",[0.275744,0.0434],1],["PlaneW",[0.263116,0.0855],1],[],["PlaneW",[0.24248,0.125],1],["PlaneW",[0.21448,0.1607],1],["PlaneW",[0.179984,0.1915],1],["PlaneW",[0.14,0.2165],1],[],["PlaneW",[0.09576,0.234925],1],["PlaneW",[0.048608,0.2462],1],["PlaneW",[0,0.25],1],["PlaneW",[-0.048608,0.2462],1],[],["PlaneW",[-0.09576,0.234925],1],["PlaneW",[-0.14,0.2165],1],["PlaneW",[-0.179984,0.1915],1],["PlaneW",[-0.21448,0.1607],1],[],["PlaneW",[-0.24248,0.125],1],["PlaneW",[-0.263116,0.0855],1],["PlaneW",[-0.275744,0.0434],1],["PlaneW",[-0.28,0],1],[],["PlaneW",[-0.275744,-0.0434],1],["PlaneW",[-0.263116,-0.0855],1],["PlaneW",[-0.24248,-0.125],1],["PlaneW",[-0.21448,-0.1607],1],[],["PlaneW",[-0.179984,-0.1915],1],["PlaneW",[-0.14,-0.2165],1],["PlaneW",[-0.09576,-0.234925],1],["PlaneW",[-0.048608,-0.2462],1],[],["PlaneW",[0,-0.25],1]]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|AmmoCount [Indent level: 5],
                    "ammocount": {
                        "type": "text",
                        "source": "ammoFormat",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.74,0.9],1],
                        "right": [[0.8,0.9],1],
                        "down": [[0.74,0.96],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|Lines [Indent level: 5],
                    "lines": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.87,0.18],1],[[0.85,0.18],1],[[0.85,0.34],1],[[0.87,0.34],1],[],[[0.87,0.3],1],[[0.85,0.3],1],[],[[0.87,0.26],1],[[0.85,0.26],1],[],[[0.87,0.22],1],[[0.85,0.22],1],[],["LarTargetDist",-0.16,[0.83,0.36],1],["LarTargetDist",-0.16,[0.85,0.34],1],["LarTargetDist",-0.16,[0.83,0.32],1],[]]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|Poly [Indent level: 5],
                    "poly": {
                        "type": "polygon",
                        "points": [[["LarAmmoMin",-0.16,[0.851,0.34],1],["LarAmmoMax",-0.16,[0.851,0.34],1],["LarAmmoMax",-0.16,[0.868,0.34],1],["LarAmmoMin",-0.16,[0.868,0.34],1]]]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|TopText [Indent level: 5],
                    "toptext": {
                        "type": "text",
                        "source": "LarTop",
                        "sourcescale": 0.001,
                        "scale": 1,
                        "pos": [[0.88,0.16],1],
                        "right": [[0.92,0.16],1],
                        "down": [[0.88,0.2],1],
                        "align": "right"
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|MiddleText [Indent level: 5],
                    "middletext": {
                        "source": "LarTop",
                        "sourceprecision": -1,
                        "sourcescale": 0.0005,
                        "pos": [[0.88,0.24],1],
                        "right": [[0.92,0.24],1],
                        "down": [[0.88,0.28],1],
                        "type": "text",
                        "scale": 1,
                        "align": "right"
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|SpeedText [Indent level: 5],
                    "speedtext": {
                        "source": "LarTargetSpeed",
                        "align": "left",
                        "sourcescale": 3.6,
                        "pos": ["LarTargetDist",-0.16,[0.82,0.32],1],
                        "right": ["LarTargetDist",-0.16,[0.86,0.32],1],
                        "down": ["LarTargetDist",-0.16,[0.82,0.36],1],
                        "type": "text",
                        "scale": 1
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|BombCrosshairGroup [Indent level: 4],
                "bombcrosshairgroup": {
                    "type": "group",
                    "condition": "bomb",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|BombCrosshairGroup|BombCrosshair [Indent level: 5],
                    "bombcrosshair": {
                        "width": 4,
                        "type": "line",
                        "points": [["ImpactPoint",[0,0.0803571],1],["ImpactPoint",[0,0.0714286],1],[],["ImpactPoint",[-0.09,0],1],["ImpactPoint",[-0.08,0],1],[],["ImpactPoint",[0.09,0],1],["ImpactPoint",[0.08,0],1],[],["ImpactPoint",[0,-0.00178571],1],["ImpactPoint",[0,0.00178571],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[],["ImpactPoint",[0,-0.0714286],1],["ImpactPoint",[0.013888,-0.0703429],1],["ImpactPoint",[0.02736,-0.0671214],1],["ImpactPoint",[0.04,-0.0618571],1],["ImpactPoint",[0.051424,-0.0547143],1],["ImpactPoint",[0.06128,-0.0459143],1],["ImpactPoint",[0.06928,-0.0357143],1],["ImpactPoint",[0.075176,-0.0244286],1],["ImpactPoint",[0.078784,-0.0124],1],["ImpactPoint",[0.08,0],1],["ImpactPoint",[0.078784,0.0124],1],["ImpactPoint",[0.075176,0.0244286],1],["ImpactPoint",[0.06928,0.0357143],1],["ImpactPoint",[0.06128,0.0459143],1],["ImpactPoint",[0.051424,0.0547143],1],["ImpactPoint",[0.04,0.0618571],1],["ImpactPoint",[0.02736,0.0671214],1],["ImpactPoint",[0.013888,0.0703429],1],["ImpactPoint",[0,0.0714286],1],["ImpactPoint",[-0.013888,0.0703429],1],["ImpactPoint",[-0.02736,0.0671214],1],["ImpactPoint",[-0.04,0.0618571],1],["ImpactPoint",[-0.051424,0.0547143],1],["ImpactPoint",[-0.06128,0.0459143],1],["ImpactPoint",[-0.06928,0.0357143],1],["ImpactPoint",[-0.075176,0.0244286],1],["ImpactPoint",[-0.078784,0.0124],1],["ImpactPoint",[-0.08,0],1],["ImpactPoint",[-0.078784,-0.0124],1],["ImpactPoint",[-0.075176,-0.0244286],1],["ImpactPoint",[-0.06928,-0.0357143],1],["ImpactPoint",[-0.06128,-0.0459143],1],["ImpactPoint",[-0.051424,-0.0547143],1],["ImpactPoint",[-0.04,-0.0618571],1],["ImpactPoint",[-0.02736,-0.0671214],1],["ImpactPoint",[-0.013888,-0.0703429],1],["ImpactPoint",[0,-0.0714286],1],[],[],["ImpactPoint",-1,"Velocity",1,"NormalizeBombCircle",1,"ImpactPoint",1,[0,0],1],["Velocity",1,"Limit0109",1,[0,0],1]]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|BombCrosshairGroup|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "width": 6,
                        "points": [["ImpactPoint",[0,-0.0571429],1],["ImpactPoint",[0,-0.0714286],1],["MissileFlightTimeRot1",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot18",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot19",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.064],1,"ImpactPoint",1]]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|BombCrosshairGroup|Distance [Indent level: 5],
                    "distance": {
                        "type": "text",
                        "source": "ImpactDistance",
                        "sourcescale": 0.001,
                        "sourceprecision": 1,
                        "max": 15,
                        "align": "center",
                        "scale": 1,
                        "pos": ["ImpactPoint",[-0.002,0.11],1],
                        "right": ["ImpactPoint",[0.045,0.11],1],
                        "down": ["ImpactPoint",[-0.002,0.15],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|MGun [Indent level: 4],
                "mgun": {
                    "condition": "(mgun+rocket)",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|MGun|ModeText [Indent level: 5],
                    "modetext": {
                        "type": "text",
                        "source": "static",
                        "align": "left",
                        "text": "GUN",
                        "scale": 1,
                        "pos": [[0.15,0.85],1],
                        "right": [[0.2,0.85],1],
                        "down": [[0.15,0.9],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|MGun|AmmoCounter [Indent level: 5],
                    "ammocounter": {
                        "type": "text",
                        "source": "ammo",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.78,0.9],1],
                        "right": [[0.84,0.9],1],
                        "down": [[0.78,0.96],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|MGunCross [Indent level: 4],
                "mguncross": {
                    "condition": "-1+(mgun+rocket)*impactDistance",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|MGunCross|Cross [Indent level: 5],
                    "cross": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPointRelative",[0,-0.07],1],["ImpactPointRelative",[0,-0.03],1],[],["ImpactPointRelative",[0,0.045],1],["ImpactPointRelative",[0,0.03],1],[],["ImpactPointRelative",[-0.045,0],1],["ImpactPointRelative",[-0.03,0],1],[],["ImpactPointRelative",[0.045,0],1],["ImpactPointRelative",[0.03,0],1],[],["ImpactPointRelative",[0,-0.002],1],["ImpactPointRelative",[0,0.002],1],[],["ImpactPointRelative",[-0.002,0],1],["ImpactPointRelative",[0.002,0],1],[]]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|MGunCross|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "width": 6,
                        "points": [["ImpactPointRelative",[0,-0.0357143],1],["ImpactPointRelative",[0,-0.0446429],1],["MissileFlightTimeRot1",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot2",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot3",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot4",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot5",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot6",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot7",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot8",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot9",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot10",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot11",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot12",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot13",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot14",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot15",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot16",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot17",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot18",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot19",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot20",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot20",[0,0.04],1,"ImpactPointRelative",1]]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|MGunCross|Circle_LAR [Indent level: 5],
                    "circle_lar": {
                        "type": "line",
                        "width": 5,
                        "points": [["ImpactPointRelative",1,["LarAmmoMGunMin",0,-0.0535714],1],["ImpactPointRelative",1,["LarAmmoMGunMin",0,-0.0446429],1],[],["ImpactPointRelative",1,["LarAmmoMGunMax",0,-0.0535714],1],["ImpactPointRelative",1,["LarAmmoMGunMax",0,-0.0446429],1],[]]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|MGunCross|Distance [Indent level: 5],
                    "distance": {
                        "type": "text",
                        "source": "ImpactDistance",
                        "sourcescale": 0.001,
                        "sourceprecision": 1,
                        "max": 15,
                        "align": "center",
                        "scale": 1,
                        "pos": ["ImpactPointRelative",[-0.002,-0.1],1],
                        "right": ["ImpactPointRelative",[0.045,-0.1],1],
                        "down": ["ImpactPointRelative",[-0.002,-0.06],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|TargetInfo [Indent level: 4],
                "targetinfo": {
                    "condition": "targetDist",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|TargetInfo|TargetDist [Indent level: 5],
                    "targetdist": {
                        "type": "text",
                        "source": "targetDist",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.83,0.86],1],
                        "right": [[0.89,0.86],1],
                        "down": [[0.83,0.92],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|TargetInfo|TargetHeight [Indent level: 5],
                    "targetheight": {
                        "type": "text",
                        "source": "targetHeight",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.83,0.82],1],
                        "right": [[0.89,0.82],1],
                        "down": [[0.83,0.88],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|StallGroup [Indent level: 4],
                "stallgroup": {
                    "condition": "stall",
                    "blinkingpattern": [0.2,0.2],
                    "blinkingstartson": 1,
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|StallGroup|StallText [Indent level: 5],
                    "stalltext": {
                        "type": "text",
                        "source": "static",
                        "text": "STALL",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,0.32],1],
                        "right": [[0.57,0.32],1],
                        "down": [[0.5,0.39],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|WeaponsLocking [Indent level: 4],
                "weaponslocking": {
                    "condition": "missilelocking",
                    "blinkingpattern": [0.2,0.2],
                    "blinkingstartson": 1,
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|WeaponsLocking|Text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "LOCKING",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,0.87],1],
                        "right": [[0.57,0.87],1],
                        "down": [[0.5,0.94],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|WeaponsLocked [Indent level: 4],
                "weaponslocked": {
                    "condition": "missilelocked",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|WeaponsLocked|Text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "SHOOT",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,0.87],1],
                        "right": [[0.57,0.87],1],
                        "down": [[0.5,0.94],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|IncomingMissile [Indent level: 4],
                "incomingmissile": {
                    "condition": "incomingmissile",
                    "blinkingpattern": [0.3,0.3],
                    "blinkingstartson": 1,
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|IncomingMissile|Text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "INCOMING MISSILE",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,0.32],1],
                        "right": [[0.57,0.32],1],
                        "down": [[0.5,0.39],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarGroup [Indent level: 4],
                "radargroup": {
                    "condition": "activeSensorsOn",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarGroup|Text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "RADAR",
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.94,0.62],1],
                        "right": [[1,0.62],1],
                        "down": [[0.94,0.68],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|FlapsGroup [Indent level: 4],
                "flapsgroup": {
                    "condition": "flaps",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|FlapsGroup|GearText [Indent level: 5],
                    "geartext": {
                        "type": "text",
                        "source": "static",
                        "text": "FLAPS",
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.94,0.7],1],
                        "right": [[1,0.7],1],
                        "down": [[0.94,0.76],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|ILS [Indent level: 4],
                "ils": {
                    "condition": "ils",
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|ILS|GearText [Indent level: 5],
                    "geartext": {
                        "type": "text",
                        "source": "static",
                        "text": "GEAR",
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.94,0.66],1],
                        "right": [[1,0.66],1],
                        "down": [[0.94,0.72],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|ILS|Glideslope [Indent level: 5],
                    "glideslope": {
                        "cliptl": [0,0],
                        "clipbr": [1,1],
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 6],
                        "ils": {
                            "type": "line",
                            "width": 2,
                            "points": [["ILS_W",[-0.12,0],1],["ILS_W",[0.12,0],1],[],["ILS_W",[-0.12,-0.0107143],1],["ILS_W",[-0.12,0.0107143],1],[],["ILS_W",[-0.06,-0.00803571],1],["ILS_W",[-0.06,0.00803571],1],[],["ILS_W",[0,-0.0107143],1],["ILS_W",[0,0.0107143],1],[],["ILS_W",[0.06,-0.00803571],1],["ILS_W",[0.06,0.00803571],1],[],["ILS_W",[0.12,-0.0107143],1],["ILS_W",[0.12,0.0107143],1],[],["ILS_H",[0,-0.107143],1],["ILS_H",[0,0.107143],1],[],["ILS_H",[-0.012,-0.107143],1],["ILS_H",[0.012,-0.107143],1],[],["ILS_H",[-0.009,-0.0535714],1],["ILS_H",[0.009,-0.0535714],1],[],["ILS_H",[-0.012,0],1],["ILS_H",[0.012,0],1],[],["ILS_H",[-0.009,0.0535714],1],["ILS_H",[0.009,0.0535714],1],[],["ILS_H",[-0.012,0.107143],1],["ILS_H",[0.012,0.107143],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|ILS|Glideslope|airport [Indent level: 6],
                        "airport": {
                            "type": "line",
                            "points": [["airport1",1],["airport2",1],["airport4",1],["airport3",1],["airport1",1]]
                        }
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes [Indent level: 4],
                "radarboxes": {
                    "type": "radar",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785],
                    "width": 4,
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|points [Indent level: 5],
                    "points": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|points|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "linetype": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknown [Indent level: 5],
                    "pointsunknown": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknown|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,-0.01],1],[[0.02,-0.01],1],[[0.02,0.01],1],[[0,0.01],1]]],
                            "width": 4,
                            "linetype": 2
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownEnemy [Indent level: 5],
                    "pointsunknownenemy": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownEnemy|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,-0.01],1],[[0.02,-0.01],1],[[0.02,0.01],1],[[0,0.01],1]]],
                            "width": 4,
                            "linetype": 2
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownFriend [Indent level: 5],
                    "pointsunknownfriend": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownFriend|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,-0.01],1],[[0.02,-0.01],1],[[0.02,0.01],1],[[0,0.01],1]]],
                            "width": 4,
                            "linetype": 2
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownCiv [Indent level: 5],
                    "pointsunknownciv": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownCiv|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,-0.01],1],[[0.02,-0.01],1],[[0.02,0.01],1],[[0,0.01],1]]],
                            "width": 4,
                            "linetype": 2
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCar [Indent level: 5],
                    "pointscar": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCar|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.00260472,-0.0131894],1],[[0.0051303,-0.0125852],1],[[0.0075,-0.0115986],1]],[[[0,0],1],[[0.0075,-0.0115986],1],[[0.00964181,-0.0102595],1],[[0.0114907,-0.00860876],1]],[[[0,0],1],[[0.0114907,-0.00860876],1],[[0.0129904,-0.00669643],1],[[0.0140954,-0.00458063],1]],[[[0,0],1],[[0.0140954,-0.00458063],1],[[0.0147721,-0.00232564],1],[[0.015,5.8542e-010],1]],[[[0,0],1],[[0.015,5.8542e-010],1],[[0.0147721,0.00232565],1],[[0.0140954,0.00458063],1]],[[[0,0],1],[[0.0140954,0.00458063],1],[[0.0129904,0.00669643],1],[[0.0114907,0.00860876],1]],[[[0,0],1],[[0.0114907,0.00860876],1],[[0.00964181,0.0102595],1],[[0.0075,0.0115986],1]],[[[0,0],1],[[0.0075,0.0115986],1],[[0.0051303,0.0125852],1],[[0.00260472,0.0131894],1]],[[[0,0],1],[[0.00260472,0.0131894],1],[[-1.31134e-009,0.0133929],1],[[-0.00260473,0.0131894],1]],[[[0,0],1],[[-0.00260473,0.0131894],1],[[-0.0051303,0.0125852],1],[[-0.0075,0.0115986],1]],[[[0,0],1],[[-0.0075,0.0115986],1],[[-0.00964181,0.0102595],1],[[-0.0114907,0.00860876],1]],[[[0,0],1],[[-0.0114907,0.00860876],1],[[-0.0129904,0.00669643],1],[[-0.0140954,0.00458063],1]],[[[0,0],1],[[-0.0140954,0.00458063],1],[[-0.0147721,0.00232564],1],[[-0.015,-1.59708e-010],1]],[[[0,0],1],[[-0.015,-1.59708e-010],1],[[-0.0147721,-0.00232565],1],[[-0.0140954,-0.00458063],1]],[[[0,0],1],[[-0.0140954,-0.00458063],1],[[-0.0129904,-0.00669643],1],[[-0.0114907,-0.00860876],1]],[[[0,0],1],[[-0.0114907,-0.00860876],1],[[-0.00964181,-0.0102595],1],[[-0.0075,-0.0115986],1]],[[[0,0],1],[[-0.0075,-0.0115986],1],[[-0.00513031,-0.0125852],1],[[-0.00260472,-0.0131894],1]],[[[0,0],1],[[-0.00260472,-0.0131894],1],[[2.62268e-009,-0.0133929],1],[[0.00260472,-0.0131894],1]]],
                            "width": 4,
                            "linetype": 2
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarEnemy [Indent level: 5],
                    "pointscarenemy": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarEnemy|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.00260472,-0.0131894],1],[[0.0051303,-0.0125852],1],[[0.0075,-0.0115986],1]],[[[0,0],1],[[0.0075,-0.0115986],1],[[0.00964181,-0.0102595],1],[[0.0114907,-0.00860876],1]],[[[0,0],1],[[0.0114907,-0.00860876],1],[[0.0129904,-0.00669643],1],[[0.0140954,-0.00458063],1]],[[[0,0],1],[[0.0140954,-0.00458063],1],[[0.0147721,-0.00232564],1],[[0.015,5.8542e-010],1]],[[[0,0],1],[[0.015,5.8542e-010],1],[[0.0147721,0.00232565],1],[[0.0140954,0.00458063],1]],[[[0,0],1],[[0.0140954,0.00458063],1],[[0.0129904,0.00669643],1],[[0.0114907,0.00860876],1]],[[[0,0],1],[[0.0114907,0.00860876],1],[[0.00964181,0.0102595],1],[[0.0075,0.0115986],1]],[[[0,0],1],[[0.0075,0.0115986],1],[[0.0051303,0.0125852],1],[[0.00260472,0.0131894],1]],[[[0,0],1],[[0.00260472,0.0131894],1],[[-1.31134e-009,0.0133929],1],[[-0.00260473,0.0131894],1]],[[[0,0],1],[[-0.00260473,0.0131894],1],[[-0.0051303,0.0125852],1],[[-0.0075,0.0115986],1]],[[[0,0],1],[[-0.0075,0.0115986],1],[[-0.00964181,0.0102595],1],[[-0.0114907,0.00860876],1]],[[[0,0],1],[[-0.0114907,0.00860876],1],[[-0.0129904,0.00669643],1],[[-0.0140954,0.00458063],1]],[[[0,0],1],[[-0.0140954,0.00458063],1],[[-0.0147721,0.00232564],1],[[-0.015,-1.59708e-010],1]],[[[0,0],1],[[-0.015,-1.59708e-010],1],[[-0.0147721,-0.00232565],1],[[-0.0140954,-0.00458063],1]],[[[0,0],1],[[-0.0140954,-0.00458063],1],[[-0.0129904,-0.00669643],1],[[-0.0114907,-0.00860876],1]],[[[0,0],1],[[-0.0114907,-0.00860876],1],[[-0.00964181,-0.0102595],1],[[-0.0075,-0.0115986],1]],[[[0,0],1],[[-0.0075,-0.0115986],1],[[-0.00513031,-0.0125852],1],[[-0.00260472,-0.0131894],1]],[[[0,0],1],[[-0.00260472,-0.0131894],1],[[2.62268e-009,-0.0133929],1],[[0.00260472,-0.0131894],1]]],
                            "width": 4,
                            "linetype": 2
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarFriend [Indent level: 5],
                    "pointscarfriend": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarFriend|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.00260472,-0.0131894],1],[[0.0051303,-0.0125852],1],[[0.0075,-0.0115986],1]],[[[0,0],1],[[0.0075,-0.0115986],1],[[0.00964181,-0.0102595],1],[[0.0114907,-0.00860876],1]],[[[0,0],1],[[0.0114907,-0.00860876],1],[[0.0129904,-0.00669643],1],[[0.0140954,-0.00458063],1]],[[[0,0],1],[[0.0140954,-0.00458063],1],[[0.0147721,-0.00232564],1],[[0.015,5.8542e-010],1]],[[[0,0],1],[[0.015,5.8542e-010],1],[[0.0147721,0.00232565],1],[[0.0140954,0.00458063],1]],[[[0,0],1],[[0.0140954,0.00458063],1],[[0.0129904,0.00669643],1],[[0.0114907,0.00860876],1]],[[[0,0],1],[[0.0114907,0.00860876],1],[[0.00964181,0.0102595],1],[[0.0075,0.0115986],1]],[[[0,0],1],[[0.0075,0.0115986],1],[[0.0051303,0.0125852],1],[[0.00260472,0.0131894],1]],[[[0,0],1],[[0.00260472,0.0131894],1],[[-1.31134e-009,0.0133929],1],[[-0.00260473,0.0131894],1]],[[[0,0],1],[[-0.00260473,0.0131894],1],[[-0.0051303,0.0125852],1],[[-0.0075,0.0115986],1]],[[[0,0],1],[[-0.0075,0.0115986],1],[[-0.00964181,0.0102595],1],[[-0.0114907,0.00860876],1]],[[[0,0],1],[[-0.0114907,0.00860876],1],[[-0.0129904,0.00669643],1],[[-0.0140954,0.00458063],1]],[[[0,0],1],[[-0.0140954,0.00458063],1],[[-0.0147721,0.00232564],1],[[-0.015,-1.59708e-010],1]],[[[0,0],1],[[-0.015,-1.59708e-010],1],[[-0.0147721,-0.00232565],1],[[-0.0140954,-0.00458063],1]],[[[0,0],1],[[-0.0140954,-0.00458063],1],[[-0.0129904,-0.00669643],1],[[-0.0114907,-0.00860876],1]],[[[0,0],1],[[-0.0114907,-0.00860876],1],[[-0.00964181,-0.0102595],1],[[-0.0075,-0.0115986],1]],[[[0,0],1],[[-0.0075,-0.0115986],1],[[-0.00513031,-0.0125852],1],[[-0.00260472,-0.0131894],1]],[[[0,0],1],[[-0.00260472,-0.0131894],1],[[2.62268e-009,-0.0133929],1],[[0.00260472,-0.0131894],1]]],
                            "width": 4,
                            "linetype": 2
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarCiv [Indent level: 5],
                    "pointscarciv": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarCiv|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.00260472,-0.0131894],1],[[0.0051303,-0.0125852],1],[[0.0075,-0.0115986],1]],[[[0,0],1],[[0.0075,-0.0115986],1],[[0.00964181,-0.0102595],1],[[0.0114907,-0.00860876],1]],[[[0,0],1],[[0.0114907,-0.00860876],1],[[0.0129904,-0.00669643],1],[[0.0140954,-0.00458063],1]],[[[0,0],1],[[0.0140954,-0.00458063],1],[[0.0147721,-0.00232564],1],[[0.015,5.8542e-010],1]],[[[0,0],1],[[0.015,5.8542e-010],1],[[0.0147721,0.00232565],1],[[0.0140954,0.00458063],1]],[[[0,0],1],[[0.0140954,0.00458063],1],[[0.0129904,0.00669643],1],[[0.0114907,0.00860876],1]],[[[0,0],1],[[0.0114907,0.00860876],1],[[0.00964181,0.0102595],1],[[0.0075,0.0115986],1]],[[[0,0],1],[[0.0075,0.0115986],1],[[0.0051303,0.0125852],1],[[0.00260472,0.0131894],1]],[[[0,0],1],[[0.00260472,0.0131894],1],[[-1.31134e-009,0.0133929],1],[[-0.00260473,0.0131894],1]],[[[0,0],1],[[-0.00260473,0.0131894],1],[[-0.0051303,0.0125852],1],[[-0.0075,0.0115986],1]],[[[0,0],1],[[-0.0075,0.0115986],1],[[-0.00964181,0.0102595],1],[[-0.0114907,0.00860876],1]],[[[0,0],1],[[-0.0114907,0.00860876],1],[[-0.0129904,0.00669643],1],[[-0.0140954,0.00458063],1]],[[[0,0],1],[[-0.0140954,0.00458063],1],[[-0.0147721,0.00232564],1],[[-0.015,-1.59708e-010],1]],[[[0,0],1],[[-0.015,-1.59708e-010],1],[[-0.0147721,-0.00232565],1],[[-0.0140954,-0.00458063],1]],[[[0,0],1],[[-0.0140954,-0.00458063],1],[[-0.0129904,-0.00669643],1],[[-0.0114907,-0.00860876],1]],[[[0,0],1],[[-0.0114907,-0.00860876],1],[[-0.00964181,-0.0102595],1],[[-0.0075,-0.0115986],1]],[[[0,0],1],[[-0.0075,-0.0115986],1],[[-0.00513031,-0.0125852],1],[[-0.00260472,-0.0131894],1]],[[[0,0],1],[[-0.00260472,-0.0131894],1],[[2.62268e-009,-0.0133929],1],[[0.00260472,-0.0131894],1]]],
                            "width": 4,
                            "linetype": 2
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarNeutral [Indent level: 5],
                    "pointscarneutral": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarNeutral|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.00260472,-0.0131894],1],[[0.0051303,-0.0125852],1],[[0.0075,-0.0115986],1]],[[[0,0],1],[[0.0075,-0.0115986],1],[[0.00964181,-0.0102595],1],[[0.0114907,-0.00860876],1]],[[[0,0],1],[[0.0114907,-0.00860876],1],[[0.0129904,-0.00669643],1],[[0.0140954,-0.00458063],1]],[[[0,0],1],[[0.0140954,-0.00458063],1],[[0.0147721,-0.00232564],1],[[0.015,5.8542e-010],1]],[[[0,0],1],[[0.015,5.8542e-010],1],[[0.0147721,0.00232565],1],[[0.0140954,0.00458063],1]],[[[0,0],1],[[0.0140954,0.00458063],1],[[0.0129904,0.00669643],1],[[0.0114907,0.00860876],1]],[[[0,0],1],[[0.0114907,0.00860876],1],[[0.00964181,0.0102595],1],[[0.0075,0.0115986],1]],[[[0,0],1],[[0.0075,0.0115986],1],[[0.0051303,0.0125852],1],[[0.00260472,0.0131894],1]],[[[0,0],1],[[0.00260472,0.0131894],1],[[-1.31134e-009,0.0133929],1],[[-0.00260473,0.0131894],1]],[[[0,0],1],[[-0.00260473,0.0131894],1],[[-0.0051303,0.0125852],1],[[-0.0075,0.0115986],1]],[[[0,0],1],[[-0.0075,0.0115986],1],[[-0.00964181,0.0102595],1],[[-0.0114907,0.00860876],1]],[[[0,0],1],[[-0.0114907,0.00860876],1],[[-0.0129904,0.00669643],1],[[-0.0140954,0.00458063],1]],[[[0,0],1],[[-0.0140954,0.00458063],1],[[-0.0147721,0.00232564],1],[[-0.015,-1.59708e-010],1]],[[[0,0],1],[[-0.015,-1.59708e-010],1],[[-0.0147721,-0.00232565],1],[[-0.0140954,-0.00458063],1]],[[[0,0],1],[[-0.0140954,-0.00458063],1],[[-0.0129904,-0.00669643],1],[[-0.0114907,-0.00860876],1]],[[[0,0],1],[[-0.0114907,-0.00860876],1],[[-0.00964181,-0.0102595],1],[[-0.0075,-0.0115986],1]],[[[0,0],1],[[-0.0075,-0.0115986],1],[[-0.00513031,-0.0125852],1],[[-0.00260472,-0.0131894],1]],[[[0,0],1],[[-0.00260472,-0.0131894],1],[[2.62268e-009,-0.0133929],1],[[0.00260472,-0.0131894],1]]],
                            "width": 4,
                            "linetype": 2
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTank [Indent level: 5],
                    "pointstank": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTank|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "linetype": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankEnemy [Indent level: 5],
                    "pointstankenemy": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankEnemy|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "linetype": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankFriend [Indent level: 5],
                    "pointstankfriend": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankFriend|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "linetype": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankCiv [Indent level: 5],
                    "pointstankciv": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankCiv|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "linetype": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankNeutral [Indent level: 5],
                    "pointstankneutral": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankNeutral|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "linetype": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplane [Indent level: 5],
                    "pointsairplane": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplane|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "linetype": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplaneEnemy [Indent level: 5],
                    "pointsairplaneenemy": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplaneEnemy|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "points": [[[0.03,0],1],[[0,0.0267857],1],[[-0.03,0],1],[[0,-0.0267857],1],[[0.03,0],1]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplaneFriend [Indent level: 5],
                    "pointsairplanefriend": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplaneFriend|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[],[[0.0212132,-0.0189404],1],[[-0.0212132,0.0189404],1],[],[[0.0212132,0.0189404],1],[[-0.0212132,-0.0189404],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeli [Indent level: 5],
                    "pointsheli": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeli|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1],[],[[0,0],1],[[0.01,-0.015],1],[[-0.01,-0.015],1]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeliEnemy [Indent level: 5],
                    "pointshelienemy": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeliEnemy|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]],[[[0,0],1],[[0.01,-0.015],1],[[-0.01,-0.015],1]]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeliFriend [Indent level: 5],
                    "pointshelifriend": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeliFriend|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]],[[[0,0],1],[[0.01,-0.015],1],[[-0.01,-0.015],1]]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeliFriend|DrawLine [Indent level: 6],
                        "drawline": {
                            "type": "line",
                            "width": 4,
                            "points": []
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeliFriend|IFF_Text [Indent level: 6],
                        "iff_text": {
                            "type": "text",
                            "source": "static",
                            "text": "ALLY",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0,0.01],1],
                            "right": [[0.04,0.01],1],
                            "down": [[0,0.05],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsLaser [Indent level: 5],
                    "pointslaser": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsLaser|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "points": [[[0,-0.0178571],1],[[-1.74846e-009,0.0178571],1],[],[[0.02,7.80561e-010],1],[[-0.02,-2.12944e-010],1],[],[[0.0106066,-0.00947018],1],[[-0.0106066,0.00947018],1],[],[[0.0106066,0.00947018],1],[[-0.0106066,-0.00947018],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsNVG [Indent level: 5],
                    "pointsnvg": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsLaser|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 4,
                            "points": [[[0,-0.0178571],1],[[-1.74846e-009,0.0178571],1],[],[[0.02,7.80561e-010],1],[[-0.02,-2.12944e-010],1],[],[[0.0106066,-0.00947018],1],[[-0.0106066,0.00947018],1],[],[[0.0106066,0.00947018],1],[[-0.0106066,-0.00947018],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStatic [Indent level: 5],
                    "pointsstatic": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStatic|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticEnemy [Indent level: 5],
                    "pointsstaticenemy": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStatic|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticFriend [Indent level: 5],
                    "pointsstaticfriend": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStatic|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticCiv [Indent level: 5],
                    "pointsstaticciv": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStatic|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticNeutral [Indent level: 5],
                    "pointsstaticneutral": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStatic|Draw [Indent level: 6]
                        "draw": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]]]
                        }
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|TargetDiamond [Indent level: 4],
                "targetdiamond": {
                    # Class: CfgVehicles|rhsusf_f22|MFD|AirplaneHUD|Draw|TargetDiamond|shape [Indent level: 5]
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",[-0.002,-0.00178571],1],["Target",1,"Limit0109",[0.002,-0.00178571],1],["Target",1,"Limit0109",[0.002,0.00178571],1],["Target",1,"Limit0109",[-0.002,0.00178571],1],["Target",1,"Limit0109",[-0.002,-0.00178571],1],[],["Target",1,"Limit0109",1,[0.02,0.0178571],1],["Target",1,"Limit0109",1,[-0.02,0.0178571],1],["Target",1,"Limit0109",1,[-0.02,-0.0178571],1],["Target",1,"Limit0109",1,[0.02,-0.0178571],1],["Target",1,"Limit0109",1,[0.02,0.0178571],1]]
                    }
                }
            }
        },
        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1 [Indent level: 2],
        "mfd_1": {
            "topleft": "MFD_1_TL",
            "topright": "MFD_1_TR",
            "bottomleft": "MFD_1_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0.03,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "rhsusf_digital_font_var",
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|material [Indent level: 3],
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw [Indent level: 3],
            "draw": {
                "condition": "on",
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|UHF1_Text [Indent level: 4],
                "uhf1_text": {
                    "type": "text",
                    "source": "static",
                    "text": "UHF-1",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.04,0.13],1],
                    "right": [[0.11,0.13],1],
                    "down": [[0.04,0.2],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|UHF1_Text2 [Indent level: 4],
                "uhf1_text2": {
                    "type": "text",
                    "source": "static",
                    "text": ":",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.04,0.22],1],
                    "right": [[0.11,0.22],1],
                    "down": [[0.04,0.29],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|UHF1_Value [Indent level: 4],
                "uhf1_value": {
                    "type": "text",
                    "source": "userText",
                    "sourcescale": 1,
                    "sourceindex": 0,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.1,0.22],1],
                    "right": [[0.17,0.22],1],
                    "down": [[0.1,0.29],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|VHF1_Text [Indent level: 4],
                "vhf1_text": {
                    "type": "text",
                    "source": "static",
                    "text": "VHF-1",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.96,0.13],1],
                    "right": [[1.03,0.13],1],
                    "down": [[0.96,0.2],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|VHF1_Text2 [Indent level: 4],
                "vhf1_text2": {
                    "type": "text",
                    "source": "static",
                    "text": ":",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.96,0.22],1],
                    "right": [[1.03,0.22],1],
                    "down": [[0.96,0.29],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|VHF1_Value [Indent level: 4],
                "vhf1_value": {
                    "type": "text",
                    "source": "userText",
                    "sourcescale": 1,
                    "sourceindex": 1,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.9,0.22],1],
                    "right": [[0.97,0.22],1],
                    "down": [[0.9,0.29],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|TCN_Text [Indent level: 4],
                "tcn_text": {
                    "type": "text",
                    "source": "static",
                    "text": "TCN 004X T/R",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.04,0.49],1],
                    "right": [[0.11,0.49],1],
                    "down": [[0.04,0.56],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|ILS [Indent level: 4],
                "ils": {
                    "condition": "1-ils",
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|ILS|ILS_Text [Indent level: 5],
                    "ils_text": {
                        "type": "text",
                        "source": "static",
                        "text": "ILS OFF",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.04,0.58],1],
                        "right": [[0.11,0.58],1],
                        "down": [[0.04,0.65],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|ILS_Off [Indent level: 4],
                "ils_off": {
                    "condition": "ils",
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|ILS_Off|ILS_Text [Indent level: 5],
                    "ils_text": {
                        "type": "text",
                        "source": "static",
                        "text": "ILS ON",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.04,0.58],1],
                        "right": [[0.11,0.58],1],
                        "down": [[0.04,0.65],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|STPT_Text [Indent level: 4],
                "stpt_text": {
                    "type": "text",
                    "source": "static",
                    "text": "STPT 01/A",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.04,0.67],1],
                    "right": [[0.11,0.67],1],
                    "down": [[0.04,0.74],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|IFF_Text [Indent level: 4],
                "iff_text": {
                    "type": "text",
                    "source": "static",
                    "text": "IFF M3/A",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.04,0.76],1],
                    "right": [[0.11,0.76],1],
                    "down": [[0.04,0.83],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|IFF_Text2 [Indent level: 4],
                "iff_text2": {
                    "type": "text",
                    "source": "static",
                    "text": " :",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.04,0.85],1],
                    "right": [[0.11,0.85],1],
                    "down": [[0.04,0.92],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|IDK_Text [Indent level: 4],
                "idk_text": {
                    "type": "text",
                    "source": "static",
                    "text": "DK 04",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.96,0.49],1],
                    "right": [[1.03,0.49],1],
                    "down": [[0.96,0.56],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|STR_Text [Indent level: 4],
                "str_text": {
                    "type": "text",
                    "source": "static",
                    "text": "STR",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.96,0.58],1],
                    "right": [[1.03,0.58],1],
                    "down": [[0.96,0.65],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|AP_Text [Indent level: 4],
                "ap_text": {
                    "type": "text",
                    "source": "static",
                    "text": "A/P ON",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.96,0.67],1],
                    "right": [[1.03,0.67],1],
                    "down": [[0.96,0.74],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|CurrentTime [Indent level: 4],
                "currenttime": {
                    "type": "text",
                    "source": "time",
                    "text": "%X",
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.96,"0.13+0.09*7"],1],
                    "right": [[1.03,"0.13+0.09*7"],1],
                    "down": [[0.96,0.83],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|ING_Text [Indent level: 4],
                "ing_text": {
                    "type": "text",
                    "source": "static",
                    "text": "INS NAV",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.96,0.87],1],
                    "right": [[1.03,0.87],1],
                    "down": [[0.96,0.94],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|UHF_Text [Indent level: 4],
                "uhf_text": {
                    "type": "text",
                    "source": "static",
                    "text": "UHF",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.25,0.94],1],
                    "right": [[0.32,0.94],1],
                    "down": [[0.25,1.01],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|VHF_Text [Indent level: 4],
                "vhf_text": {
                    "type": "text",
                    "source": "static",
                    "text": "VHF",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.51,0.94],1],
                    "right": [[0.58,0.94],1],
                    "down": [[0.51,1.01],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_1|Draw|TIME_Text [Indent level: 4],
                "time_text": {
                    "type": "text",
                    "source": "static",
                    "text": "TIME",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.75,0.94],1],
                    "right": [[0.82,0.94],1],
                    "down": [[0.75,1.01],1]
                }
            }
        },
        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2 [Indent level: 2],
        "mfd_2": {
            "topleft": "MFD_2_TL",
            "topright": "MFD_2_TR",
            "bottomleft": "MFD_2_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1,1],
            "enableparallax": 0,
            "font": "rhsusf_digital_font_var",
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|material [Indent level: 3],
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|Center [Indent level: 4]
                "center": {
                    "type": "fixed",
                    "pos": [0.35,0.475]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|Level0 [Indent level: 4],
                "level0": {
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|Level0_Background [Indent level: 4],
                "level0_background": {
                    "pos0": [0,0],
                    "pos10": [0.68,0.89],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP5 [Indent level: 4],
                "levelp5": {
                    "angle": 5,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM5 [Indent level: 4],
                "levelm5": {
                    "angle": -5,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": 10,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": -10,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": 15,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": -15,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": 20,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": -20,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": 25,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": -25,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": 30,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": -30,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": 35,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": -35,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": 40,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": -40,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": 45,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": -45,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP50 [Indent level: 4],
                "levelp50": {
                    "angle": 50,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM50 [Indent level: 4],
                "levelm50": {
                    "angle": -50,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP60 [Indent level: 4],
                "levelp60": {
                    "angle": 60,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM60 [Indent level: 4],
                "levelm60": {
                    "angle": -60,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP70 [Indent level: 4],
                "levelp70": {
                    "angle": 70,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM70 [Indent level: 4],
                "levelm70": {
                    "angle": -70,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP80 [Indent level: 4],
                "levelp80": {
                    "angle": 80,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM80 [Indent level: 4],
                "levelm80": {
                    "angle": -80,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelP90 [Indent level: 4],
                "levelp90": {
                    "angle": 90,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Bones|LevelM90 [Indent level: 4],
                "levelm90": {
                    "angle": -90,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw [Indent level: 3],
            "draw": {
                "condition": "on",
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground [Indent level: 4],
                "horizontbackground": {
                    "color": [0.1,0.3,0.7],
                    "alpha": 0.8,
                    "cliptl": [0.018,0.085],
                    "clipbr": [0.69,0.88],
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|Static [Indent level: 5],
                    "static": {
                        "type": "polygon",
                        "points": [[["Level0",[-10,-19.99],1],["Level0",[10,-19.99],1],["Level0",[10,0.0100002],1],["Level0",[-10,0.0100002],1]]]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|StaticBlack [Indent level: 5],
                    "staticblack": {
                        "color": [0,0,0],
                        "alpha": 1,
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|StaticBlack|Static [Indent level: 6],
                        "static": {
                            "type": "polygon",
                            "points": [[["Level0",[-10,0.01],1],["Level0",[10,0.01],1],["Level0",[10,20.01],1],["Level0",[-10,20.01],1]]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite [Indent level: 5],
                    "horizontwhite": {
                        "color": [0,0,0],
                        "alpha": 0.9,
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|Dimmed [Indent level: 6],
                        "dimmed": {
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|Dimmed|Level0 [Indent level: 7]
                            "level0": {
                                "type": "line",
                                "width": 7,
                                "points": [["Level0",[0.25,0],1],["Level0",[0.065,0],1],[],["Level0",[-0.065,0],1],["Level0",[-0.25,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|Level0 [Indent level: 6],
                        "level0": {
                            "type": "line",
                            "width": 16,
                            "points": []
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP5 [Indent level: 6],
                        "levelp5": {
                            "type": "line",
                            "points": [["LevelP5",["-0.16-0.015",0.02],1],["LevelP5",["-0.16-0.015",0],1],["LevelP5",[-0.06,"0.001*9"],1],[],["LevelP5",[0.06,"0.001*9"],1],["LevelP5",["+0.16+0.015",0],1],["LevelP5",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_5 [Indent level: 6],
                        "valp_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP5",[-0.19,-0.017],1],
                            "right": ["LevelP5",[-0.13,-0.017],1],
                            "down": ["LevelP5",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_5_R [Indent level: 6],
                        "valp_1_5_r": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP5",[0.19,-0.017],1],
                            "right": ["LevelP5",[0.25,-0.017],1],
                            "down": ["LevelP5",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP10 [Indent level: 6],
                        "levelp10": {
                            "type": "line",
                            "points": [["LevelP10",["-0.16-0.015",0.02],1],["LevelP10",["-0.16-0.015",0],1],["LevelP10",[-0.06,"0.001*9"],1],[],["LevelP10",[0.06,"0.001*9"],1],["LevelP10",["+0.16+0.015",0],1],["LevelP10",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_10 [Indent level: 6],
                        "valp_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP10",[-0.19,-0.017],1],
                            "right": ["LevelP10",[-0.13,-0.017],1],
                            "down": ["LevelP10",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_10_R [Indent level: 6],
                        "valp_1_10_r": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP10",[0.19,-0.017],1],
                            "right": ["LevelP10",[0.25,-0.017],1],
                            "down": ["LevelP10",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP15 [Indent level: 6],
                        "levelp15": {
                            "type": "line",
                            "points": [["LevelP15",["-0.16-0.015",0.02],1],["LevelP15",["-0.16-0.015",0],1],["LevelP15",[-0.06,"0.001*9"],1],[],["LevelP15",[0.06,"0.001*9"],1],["LevelP15",["+0.16+0.015",0],1],["LevelP15",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_15 [Indent level: 6],
                        "valp_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP15",[-0.19,-0.017],1],
                            "right": ["LevelP15",[-0.13,-0.017],1],
                            "down": ["LevelP15",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_15_R [Indent level: 6],
                        "valp_1_15_r": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP15",[0.19,-0.017],1],
                            "right": ["LevelP15",[0.25,-0.017],1],
                            "down": ["LevelP15",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP20 [Indent level: 6],
                        "levelp20": {
                            "type": "line",
                            "points": [["LevelP20",["-0.16-0.015",0.02],1],["LevelP20",["-0.16-0.015",0],1],["LevelP20",[-0.06,"0.001*9"],1],[],["LevelP20",[0.06,"0.001*9"],1],["LevelP20",["+0.16+0.015",0],1],["LevelP20",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_20 [Indent level: 6],
                        "valp_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP20",[-0.19,-0.017],1],
                            "right": ["LevelP20",[-0.13,-0.017],1],
                            "down": ["LevelP20",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_20_R [Indent level: 6],
                        "valp_1_20_r": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP20",[0.19,-0.017],1],
                            "right": ["LevelP20",[0.25,-0.017],1],
                            "down": ["LevelP20",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP25 [Indent level: 6],
                        "levelp25": {
                            "type": "line",
                            "points": [["LevelP25",["-0.16-0.015",0.02],1],["LevelP25",["-0.16-0.015",0],1],["LevelP25",[-0.06,"0.001*9"],1],[],["LevelP25",[0.06,"0.001*9"],1],["LevelP25",["+0.16+0.015",0],1],["LevelP25",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_25 [Indent level: 6],
                        "valp_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP25",[-0.19,-0.017],1],
                            "right": ["LevelP25",[-0.13,-0.017],1],
                            "down": ["LevelP25",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_25_R [Indent level: 6],
                        "valp_1_25_r": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP25",[0.19,-0.017],1],
                            "right": ["LevelP25",[0.25,-0.017],1],
                            "down": ["LevelP25",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP30 [Indent level: 6],
                        "levelp30": {
                            "type": "line",
                            "points": [["LevelP30",["-0.16-0.015",0.02],1],["LevelP30",["-0.16-0.015",0],1],["LevelP30",[-0.06,"0.001*9"],1],[],["LevelP30",[0.06,"0.001*9"],1],["LevelP30",["+0.16+0.015",0],1],["LevelP30",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_30 [Indent level: 6],
                        "valp_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP30",[-0.19,-0.017],1],
                            "right": ["LevelP30",[-0.13,-0.017],1],
                            "down": ["LevelP30",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_30_R [Indent level: 6],
                        "valp_1_30_r": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP30",[0.19,-0.017],1],
                            "right": ["LevelP30",[0.25,-0.017],1],
                            "down": ["LevelP30",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP35 [Indent level: 6],
                        "levelp35": {
                            "type": "line",
                            "points": [["LevelP35",["-0.16-0.015",0.02],1],["LevelP35",["-0.16-0.015",0],1],["LevelP35",[-0.06,"0.001*9"],1],[],["LevelP35",[0.06,"0.001*9"],1],["LevelP35",["+0.16+0.015",0],1],["LevelP35",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_35 [Indent level: 6],
                        "valp_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP35",[-0.19,-0.017],1],
                            "right": ["LevelP35",[-0.13,-0.017],1],
                            "down": ["LevelP35",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_35_R [Indent level: 6],
                        "valp_1_35_r": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP35",[0.19,-0.017],1],
                            "right": ["LevelP35",[0.25,-0.017],1],
                            "down": ["LevelP35",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP40 [Indent level: 6],
                        "levelp40": {
                            "type": "line",
                            "points": [["LevelP40",["-0.16-0.015",0.02],1],["LevelP40",["-0.16-0.015",0],1],["LevelP40",[-0.06,"0.001*9"],1],[],["LevelP40",[0.06,"0.001*9"],1],["LevelP40",["+0.16+0.015",0],1],["LevelP40",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_40 [Indent level: 6],
                        "valp_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP40",[-0.19,-0.017],1],
                            "right": ["LevelP40",[-0.13,-0.017],1],
                            "down": ["LevelP40",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_40_R [Indent level: 6],
                        "valp_1_40_r": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP40",[0.19,-0.017],1],
                            "right": ["LevelP40",[0.25,-0.017],1],
                            "down": ["LevelP40",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP45 [Indent level: 6],
                        "levelp45": {
                            "type": "line",
                            "points": [["LevelP45",["-0.16-0.015",0.02],1],["LevelP45",["-0.16-0.015",0],1],["LevelP45",[-0.06,"0.001*9"],1],[],["LevelP45",[0.06,"0.001*9"],1],["LevelP45",["+0.16+0.015",0],1],["LevelP45",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_45 [Indent level: 6],
                        "valp_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP45",[-0.19,-0.017],1],
                            "right": ["LevelP45",[-0.13,-0.017],1],
                            "down": ["LevelP45",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_45_R [Indent level: 6],
                        "valp_1_45_r": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP45",[0.19,-0.017],1],
                            "right": ["LevelP45",[0.25,-0.017],1],
                            "down": ["LevelP45",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP50 [Indent level: 6],
                        "levelp50": {
                            "type": "line",
                            "points": [["LevelP50",["-0.16-0.015",0.02],1],["LevelP50",["-0.16-0.015",0],1],["LevelP50",[-0.06,"0.001*9"],1],[],["LevelP50",[0.06,"0.001*9"],1],["LevelP50",["+0.16+0.015",0],1],["LevelP50",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_50 [Indent level: 6],
                        "valp_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP50",[-0.19,-0.017],1],
                            "right": ["LevelP50",[-0.13,-0.017],1],
                            "down": ["LevelP50",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_50_R [Indent level: 6],
                        "valp_1_50_r": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP50",[0.19,-0.017],1],
                            "right": ["LevelP50",[0.25,-0.017],1],
                            "down": ["LevelP50",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP60 [Indent level: 6],
                        "levelp60": {
                            "type": "line",
                            "points": [["LevelP60",["-0.16-0.015",0.02],1],["LevelP60",["-0.16-0.015",0],1],["LevelP60",[-0.06,"0.001*9"],1],[],["LevelP60",[0.06,"0.001*9"],1],["LevelP60",["+0.16+0.015",0],1],["LevelP60",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_60 [Indent level: 6],
                        "valp_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP60",[-0.19,-0.017],1],
                            "right": ["LevelP60",[-0.13,-0.017],1],
                            "down": ["LevelP60",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_60_R [Indent level: 6],
                        "valp_1_60_r": {
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP60",[0.19,-0.017],1],
                            "right": ["LevelP60",[0.25,-0.017],1],
                            "down": ["LevelP60",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP70 [Indent level: 6],
                        "levelp70": {
                            "type": "line",
                            "points": [["LevelP70",["-0.16-0.015",0.02],1],["LevelP70",["-0.16-0.015",0],1],["LevelP70",[-0.06,"0.001*9"],1],[],["LevelP70",[0.06,"0.001*9"],1],["LevelP70",["+0.16+0.015",0],1],["LevelP70",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_70 [Indent level: 6],
                        "valp_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": "70",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP70",[-0.19,-0.017],1],
                            "right": ["LevelP70",[-0.13,-0.017],1],
                            "down": ["LevelP70",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_70_R [Indent level: 6],
                        "valp_1_70_r": {
                            "type": "text",
                            "source": "static",
                            "text": "70",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP70",[0.19,-0.017],1],
                            "right": ["LevelP70",[0.25,-0.017],1],
                            "down": ["LevelP70",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP80 [Indent level: 6],
                        "levelp80": {
                            "type": "line",
                            "points": [["LevelP80",["-0.16-0.015",0.02],1],["LevelP80",["-0.16-0.015",0],1],["LevelP80",[-0.06,"0.001*9"],1],[],["LevelP80",[0.06,"0.001*9"],1],["LevelP80",["+0.16+0.015",0],1],["LevelP80",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_80 [Indent level: 6],
                        "valp_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": "80",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP80",[-0.19,-0.017],1],
                            "right": ["LevelP80",[-0.13,-0.017],1],
                            "down": ["LevelP80",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_80_R [Indent level: 6],
                        "valp_1_80_r": {
                            "type": "text",
                            "source": "static",
                            "text": "80",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP80",[0.19,-0.017],1],
                            "right": ["LevelP80",[0.25,-0.017],1],
                            "down": ["LevelP80",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|LevelP90 [Indent level: 6],
                        "levelp90": {
                            "type": "line",
                            "points": [["LevelP90",["-0.16-0.015",0.02],1],["LevelP90",["-0.16-0.015",0],1],["LevelP90",[-0.06,"0.001*9"],1],[],["LevelP90",[0.06,"0.001*9"],1],["LevelP90",["+0.16+0.015",0],1],["LevelP90",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_90 [Indent level: 6],
                        "valp_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": "90",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP90",[-0.19,-0.017],1],
                            "right": ["LevelP90",[-0.13,-0.017],1],
                            "down": ["LevelP90",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontWhite|VALP_1_90_R [Indent level: 6],
                        "valp_1_90_r": {
                            "type": "text",
                            "source": "static",
                            "text": "90",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP90",[0.19,-0.017],1],
                            "right": ["LevelP90",[0.25,-0.017],1],
                            "down": ["LevelP90",[0.19,0.033],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack [Indent level: 5],
                    "horizontblack": {
                        "color": [1,1,1],
                        "alpha": 0.9,
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|Level0 [Indent level: 6],
                        "level0": {
                            "type": "line",
                            "width": 7,
                            "points": []
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM5 [Indent level: 6],
                        "levelm5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.175,-0.02],1],["LevelM5",[-0.175,0],1],[],["LevelM5",[-0.16,"-0.001*1"],1],["LevelM5",[-0.145,"-0.001*2"],1],[],["LevelM5",[-0.13,"-0.001*3"],1],["LevelM5",[-0.115,"-0.001*4"],1],[],["LevelM5",[-0.1,"-0.001*5"],1],["LevelM5",[-0.085,"-0.001*6"],1],[],["LevelM5",[-0.07,"-0.001*7"],1],["LevelM5",[-0.055,"-0.001*8"],1],[],["LevelM5",[-0.04,"-0.001*9"],1],[],["LevelM5",[0.175,-0.02],1],["LevelM5",[0.175,0],1],[],["LevelM5",[0.16,"-0.001*1"],1],["LevelM5",[0.145,"-0.001*2"],1],[],["LevelM5",[0.13,"-0.001*3"],1],["LevelM5",[0.115,"-0.001*4"],1],[],["LevelM5",[0.1,"-0.001*5"],1],["LevelM5",[0.085,"-0.001*6"],1],[],["LevelM5",[0.07,"-0.001*7"],1],["LevelM5",[0.055,"-0.001*8"],1],[],["LevelM5",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_5 [Indent level: 6],
                        "valm_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM5",[-0.19,-0.032],1],
                            "right": ["LevelM5",[-0.13,-0.032],1],
                            "down": ["LevelM5",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_5_R [Indent level: 6],
                        "valm_1_5_r": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM5",[0.19,-0.032],1],
                            "right": ["LevelM5",[0.25,-0.032],1],
                            "down": ["LevelM5",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM10 [Indent level: 6],
                        "levelm10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.175,-0.02],1],["LevelM10",[-0.175,0],1],[],["LevelM10",[-0.16,"-0.001*1"],1],["LevelM10",[-0.145,"-0.001*2"],1],[],["LevelM10",[-0.13,"-0.001*3"],1],["LevelM10",[-0.115,"-0.001*4"],1],[],["LevelM10",[-0.1,"-0.001*5"],1],["LevelM10",[-0.085,"-0.001*6"],1],[],["LevelM10",[-0.07,"-0.001*7"],1],["LevelM10",[-0.055,"-0.001*8"],1],[],["LevelM10",[-0.04,"-0.001*9"],1],[],["LevelM10",[0.175,-0.02],1],["LevelM10",[0.175,0],1],[],["LevelM10",[0.16,"-0.001*1"],1],["LevelM10",[0.145,"-0.001*2"],1],[],["LevelM10",[0.13,"-0.001*3"],1],["LevelM10",[0.115,"-0.001*4"],1],[],["LevelM10",[0.1,"-0.001*5"],1],["LevelM10",[0.085,"-0.001*6"],1],[],["LevelM10",[0.07,"-0.001*7"],1],["LevelM10",[0.055,"-0.001*8"],1],[],["LevelM10",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_10 [Indent level: 6],
                        "valm_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM10",[-0.19,-0.032],1],
                            "right": ["LevelM10",[-0.13,-0.032],1],
                            "down": ["LevelM10",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_10_R [Indent level: 6],
                        "valm_1_10_r": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM10",[0.19,-0.032],1],
                            "right": ["LevelM10",[0.25,-0.032],1],
                            "down": ["LevelM10",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM15 [Indent level: 6],
                        "levelm15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.175,-0.02],1],["LevelM15",[-0.175,0],1],[],["LevelM15",[-0.16,"-0.001*1"],1],["LevelM15",[-0.145,"-0.001*2"],1],[],["LevelM15",[-0.13,"-0.001*3"],1],["LevelM15",[-0.115,"-0.001*4"],1],[],["LevelM15",[-0.1,"-0.001*5"],1],["LevelM15",[-0.085,"-0.001*6"],1],[],["LevelM15",[-0.07,"-0.001*7"],1],["LevelM15",[-0.055,"-0.001*8"],1],[],["LevelM15",[-0.04,"-0.001*9"],1],[],["LevelM15",[0.175,-0.02],1],["LevelM15",[0.175,0],1],[],["LevelM15",[0.16,"-0.001*1"],1],["LevelM15",[0.145,"-0.001*2"],1],[],["LevelM15",[0.13,"-0.001*3"],1],["LevelM15",[0.115,"-0.001*4"],1],[],["LevelM15",[0.1,"-0.001*5"],1],["LevelM15",[0.085,"-0.001*6"],1],[],["LevelM15",[0.07,"-0.001*7"],1],["LevelM15",[0.055,"-0.001*8"],1],[],["LevelM15",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_15 [Indent level: 6],
                        "valm_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM15",[-0.19,-0.032],1],
                            "right": ["LevelM15",[-0.13,-0.032],1],
                            "down": ["LevelM15",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_15_R [Indent level: 6],
                        "valm_1_15_r": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM15",[0.19,-0.032],1],
                            "right": ["LevelM15",[0.25,-0.032],1],
                            "down": ["LevelM15",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM20 [Indent level: 6],
                        "levelm20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.175,-0.02],1],["LevelM20",[-0.175,0],1],[],["LevelM20",[-0.16,"-0.001*1"],1],["LevelM20",[-0.145,"-0.001*2"],1],[],["LevelM20",[-0.13,"-0.001*3"],1],["LevelM20",[-0.115,"-0.001*4"],1],[],["LevelM20",[-0.1,"-0.001*5"],1],["LevelM20",[-0.085,"-0.001*6"],1],[],["LevelM20",[-0.07,"-0.001*7"],1],["LevelM20",[-0.055,"-0.001*8"],1],[],["LevelM20",[-0.04,"-0.001*9"],1],[],["LevelM20",[0.175,-0.02],1],["LevelM20",[0.175,0],1],[],["LevelM20",[0.16,"-0.001*1"],1],["LevelM20",[0.145,"-0.001*2"],1],[],["LevelM20",[0.13,"-0.001*3"],1],["LevelM20",[0.115,"-0.001*4"],1],[],["LevelM20",[0.1,"-0.001*5"],1],["LevelM20",[0.085,"-0.001*6"],1],[],["LevelM20",[0.07,"-0.001*7"],1],["LevelM20",[0.055,"-0.001*8"],1],[],["LevelM20",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_20 [Indent level: 6],
                        "valm_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM20",[-0.19,-0.032],1],
                            "right": ["LevelM20",[-0.13,-0.032],1],
                            "down": ["LevelM20",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_20_R [Indent level: 6],
                        "valm_1_20_r": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM20",[0.19,-0.032],1],
                            "right": ["LevelM20",[0.25,-0.032],1],
                            "down": ["LevelM20",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM25 [Indent level: 6],
                        "levelm25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.175,-0.02],1],["LevelM25",[-0.175,0],1],[],["LevelM25",[-0.16,"-0.001*1"],1],["LevelM25",[-0.145,"-0.001*2"],1],[],["LevelM25",[-0.13,"-0.001*3"],1],["LevelM25",[-0.115,"-0.001*4"],1],[],["LevelM25",[-0.1,"-0.001*5"],1],["LevelM25",[-0.085,"-0.001*6"],1],[],["LevelM25",[-0.07,"-0.001*7"],1],["LevelM25",[-0.055,"-0.001*8"],1],[],["LevelM25",[-0.04,"-0.001*9"],1],[],["LevelM25",[0.175,-0.02],1],["LevelM25",[0.175,0],1],[],["LevelM25",[0.16,"-0.001*1"],1],["LevelM25",[0.145,"-0.001*2"],1],[],["LevelM25",[0.13,"-0.001*3"],1],["LevelM25",[0.115,"-0.001*4"],1],[],["LevelM25",[0.1,"-0.001*5"],1],["LevelM25",[0.085,"-0.001*6"],1],[],["LevelM25",[0.07,"-0.001*7"],1],["LevelM25",[0.055,"-0.001*8"],1],[],["LevelM25",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_25 [Indent level: 6],
                        "valm_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM25",[-0.19,-0.032],1],
                            "right": ["LevelM25",[-0.13,-0.032],1],
                            "down": ["LevelM25",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_25_R [Indent level: 6],
                        "valm_1_25_r": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM25",[0.19,-0.032],1],
                            "right": ["LevelM25",[0.25,-0.032],1],
                            "down": ["LevelM25",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM30 [Indent level: 6],
                        "levelm30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.175,-0.02],1],["LevelM30",[-0.175,0],1],[],["LevelM30",[-0.16,"-0.001*1"],1],["LevelM30",[-0.145,"-0.001*2"],1],[],["LevelM30",[-0.13,"-0.001*3"],1],["LevelM30",[-0.115,"-0.001*4"],1],[],["LevelM30",[-0.1,"-0.001*5"],1],["LevelM30",[-0.085,"-0.001*6"],1],[],["LevelM30",[-0.07,"-0.001*7"],1],["LevelM30",[-0.055,"-0.001*8"],1],[],["LevelM30",[-0.04,"-0.001*9"],1],[],["LevelM30",[0.175,-0.02],1],["LevelM30",[0.175,0],1],[],["LevelM30",[0.16,"-0.001*1"],1],["LevelM30",[0.145,"-0.001*2"],1],[],["LevelM30",[0.13,"-0.001*3"],1],["LevelM30",[0.115,"-0.001*4"],1],[],["LevelM30",[0.1,"-0.001*5"],1],["LevelM30",[0.085,"-0.001*6"],1],[],["LevelM30",[0.07,"-0.001*7"],1],["LevelM30",[0.055,"-0.001*8"],1],[],["LevelM30",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_30 [Indent level: 6],
                        "valm_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM30",[-0.19,-0.032],1],
                            "right": ["LevelM30",[-0.13,-0.032],1],
                            "down": ["LevelM30",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_30_R [Indent level: 6],
                        "valm_1_30_r": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM30",[0.19,-0.032],1],
                            "right": ["LevelM30",[0.25,-0.032],1],
                            "down": ["LevelM30",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM35 [Indent level: 6],
                        "levelm35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.175,-0.02],1],["LevelM35",[-0.175,0],1],[],["LevelM35",[-0.16,"-0.001*1"],1],["LevelM35",[-0.145,"-0.001*2"],1],[],["LevelM35",[-0.13,"-0.001*3"],1],["LevelM35",[-0.115,"-0.001*4"],1],[],["LevelM35",[-0.1,"-0.001*5"],1],["LevelM35",[-0.085,"-0.001*6"],1],[],["LevelM35",[-0.07,"-0.001*7"],1],["LevelM35",[-0.055,"-0.001*8"],1],[],["LevelM35",[-0.04,"-0.001*9"],1],[],["LevelM35",[0.175,-0.02],1],["LevelM35",[0.175,0],1],[],["LevelM35",[0.16,"-0.001*1"],1],["LevelM35",[0.145,"-0.001*2"],1],[],["LevelM35",[0.13,"-0.001*3"],1],["LevelM35",[0.115,"-0.001*4"],1],[],["LevelM35",[0.1,"-0.001*5"],1],["LevelM35",[0.085,"-0.001*6"],1],[],["LevelM35",[0.07,"-0.001*7"],1],["LevelM35",[0.055,"-0.001*8"],1],[],["LevelM35",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_35 [Indent level: 6],
                        "valm_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM35",[-0.19,-0.032],1],
                            "right": ["LevelM35",[-0.13,-0.032],1],
                            "down": ["LevelM35",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_35_R [Indent level: 6],
                        "valm_1_35_r": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM35",[0.19,-0.032],1],
                            "right": ["LevelM35",[0.25,-0.032],1],
                            "down": ["LevelM35",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM40 [Indent level: 6],
                        "levelm40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.175,-0.02],1],["LevelM40",[-0.175,0],1],[],["LevelM40",[-0.16,"-0.001*1"],1],["LevelM40",[-0.145,"-0.001*2"],1],[],["LevelM40",[-0.13,"-0.001*3"],1],["LevelM40",[-0.115,"-0.001*4"],1],[],["LevelM40",[-0.1,"-0.001*5"],1],["LevelM40",[-0.085,"-0.001*6"],1],[],["LevelM40",[-0.07,"-0.001*7"],1],["LevelM40",[-0.055,"-0.001*8"],1],[],["LevelM40",[-0.04,"-0.001*9"],1],[],["LevelM40",[0.175,-0.02],1],["LevelM40",[0.175,0],1],[],["LevelM40",[0.16,"-0.001*1"],1],["LevelM40",[0.145,"-0.001*2"],1],[],["LevelM40",[0.13,"-0.001*3"],1],["LevelM40",[0.115,"-0.001*4"],1],[],["LevelM40",[0.1,"-0.001*5"],1],["LevelM40",[0.085,"-0.001*6"],1],[],["LevelM40",[0.07,"-0.001*7"],1],["LevelM40",[0.055,"-0.001*8"],1],[],["LevelM40",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_40 [Indent level: 6],
                        "valm_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM40",[-0.19,-0.032],1],
                            "right": ["LevelM40",[-0.13,-0.032],1],
                            "down": ["LevelM40",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_40_R [Indent level: 6],
                        "valm_1_40_r": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM40",[0.19,-0.032],1],
                            "right": ["LevelM40",[0.25,-0.032],1],
                            "down": ["LevelM40",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM45 [Indent level: 6],
                        "levelm45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.175,-0.02],1],["LevelM45",[-0.175,0],1],[],["LevelM45",[-0.16,"-0.001*1"],1],["LevelM45",[-0.145,"-0.001*2"],1],[],["LevelM45",[-0.13,"-0.001*3"],1],["LevelM45",[-0.115,"-0.001*4"],1],[],["LevelM45",[-0.1,"-0.001*5"],1],["LevelM45",[-0.085,"-0.001*6"],1],[],["LevelM45",[-0.07,"-0.001*7"],1],["LevelM45",[-0.055,"-0.001*8"],1],[],["LevelM45",[-0.04,"-0.001*9"],1],[],["LevelM45",[0.175,-0.02],1],["LevelM45",[0.175,0],1],[],["LevelM45",[0.16,"-0.001*1"],1],["LevelM45",[0.145,"-0.001*2"],1],[],["LevelM45",[0.13,"-0.001*3"],1],["LevelM45",[0.115,"-0.001*4"],1],[],["LevelM45",[0.1,"-0.001*5"],1],["LevelM45",[0.085,"-0.001*6"],1],[],["LevelM45",[0.07,"-0.001*7"],1],["LevelM45",[0.055,"-0.001*8"],1],[],["LevelM45",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_45 [Indent level: 6],
                        "valm_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM45",[-0.19,-0.032],1],
                            "right": ["LevelM45",[-0.13,-0.032],1],
                            "down": ["LevelM45",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_45_R [Indent level: 6],
                        "valm_1_45_r": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM45",[0.19,-0.032],1],
                            "right": ["LevelM45",[0.25,-0.032],1],
                            "down": ["LevelM45",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM50 [Indent level: 6],
                        "levelm50": {
                            "type": "line",
                            "points": [["LevelM50",[-0.175,-0.02],1],["LevelM50",[-0.175,0],1],[],["LevelM50",[-0.16,"-0.001*1"],1],["LevelM50",[-0.145,"-0.001*2"],1],[],["LevelM50",[-0.13,"-0.001*3"],1],["LevelM50",[-0.115,"-0.001*4"],1],[],["LevelM50",[-0.1,"-0.001*5"],1],["LevelM50",[-0.085,"-0.001*6"],1],[],["LevelM50",[-0.07,"-0.001*7"],1],["LevelM50",[-0.055,"-0.001*8"],1],[],["LevelM50",[-0.04,"-0.001*9"],1],[],["LevelM50",[0.175,-0.02],1],["LevelM50",[0.175,0],1],[],["LevelM50",[0.16,"-0.001*1"],1],["LevelM50",[0.145,"-0.001*2"],1],[],["LevelM50",[0.13,"-0.001*3"],1],["LevelM50",[0.115,"-0.001*4"],1],[],["LevelM50",[0.1,"-0.001*5"],1],["LevelM50",[0.085,"-0.001*6"],1],[],["LevelM50",[0.07,"-0.001*7"],1],["LevelM50",[0.055,"-0.001*8"],1],[],["LevelM50",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_50 [Indent level: 6],
                        "valm_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM50",[-0.19,-0.032],1],
                            "right": ["LevelM50",[-0.13,-0.032],1],
                            "down": ["LevelM50",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_50_R [Indent level: 6],
                        "valm_1_50_r": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM50",[0.19,-0.032],1],
                            "right": ["LevelM50",[0.25,-0.032],1],
                            "down": ["LevelM50",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM60 [Indent level: 6],
                        "levelm60": {
                            "type": "line",
                            "points": [["LevelM60",[-0.175,-0.02],1],["LevelM60",[-0.175,0],1],[],["LevelM60",[-0.16,"-0.001*1"],1],["LevelM60",[-0.145,"-0.001*2"],1],[],["LevelM60",[-0.13,"-0.001*3"],1],["LevelM60",[-0.115,"-0.001*4"],1],[],["LevelM60",[-0.1,"-0.001*5"],1],["LevelM60",[-0.085,"-0.001*6"],1],[],["LevelM60",[-0.07,"-0.001*7"],1],["LevelM60",[-0.055,"-0.001*8"],1],[],["LevelM60",[-0.04,"-0.001*9"],1],[],["LevelM60",[0.175,-0.02],1],["LevelM60",[0.175,0],1],[],["LevelM60",[0.16,"-0.001*1"],1],["LevelM60",[0.145,"-0.001*2"],1],[],["LevelM60",[0.13,"-0.001*3"],1],["LevelM60",[0.115,"-0.001*4"],1],[],["LevelM60",[0.1,"-0.001*5"],1],["LevelM60",[0.085,"-0.001*6"],1],[],["LevelM60",[0.07,"-0.001*7"],1],["LevelM60",[0.055,"-0.001*8"],1],[],["LevelM60",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_60 [Indent level: 6],
                        "valm_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM60",[-0.19,-0.032],1],
                            "right": ["LevelM60",[-0.13,-0.032],1],
                            "down": ["LevelM60",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_60_R [Indent level: 6],
                        "valm_1_60_r": {
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM60",[0.19,-0.032],1],
                            "right": ["LevelM60",[0.25,-0.032],1],
                            "down": ["LevelM60",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM70 [Indent level: 6],
                        "levelm70": {
                            "type": "line",
                            "points": [["LevelM70",[-0.175,-0.02],1],["LevelM70",[-0.175,0],1],[],["LevelM70",[-0.16,"-0.001*1"],1],["LevelM70",[-0.145,"-0.001*2"],1],[],["LevelM70",[-0.13,"-0.001*3"],1],["LevelM70",[-0.115,"-0.001*4"],1],[],["LevelM70",[-0.1,"-0.001*5"],1],["LevelM70",[-0.085,"-0.001*6"],1],[],["LevelM70",[-0.07,"-0.001*7"],1],["LevelM70",[-0.055,"-0.001*8"],1],[],["LevelM70",[-0.04,"-0.001*9"],1],[],["LevelM70",[0.175,-0.02],1],["LevelM70",[0.175,0],1],[],["LevelM70",[0.16,"-0.001*1"],1],["LevelM70",[0.145,"-0.001*2"],1],[],["LevelM70",[0.13,"-0.001*3"],1],["LevelM70",[0.115,"-0.001*4"],1],[],["LevelM70",[0.1,"-0.001*5"],1],["LevelM70",[0.085,"-0.001*6"],1],[],["LevelM70",[0.07,"-0.001*7"],1],["LevelM70",[0.055,"-0.001*8"],1],[],["LevelM70",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_70 [Indent level: 6],
                        "valm_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM70",[-0.19,-0.032],1],
                            "right": ["LevelM70",[-0.13,-0.032],1],
                            "down": ["LevelM70",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_70_R [Indent level: 6],
                        "valm_1_70_r": {
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM70",[0.19,-0.032],1],
                            "right": ["LevelM70",[0.25,-0.032],1],
                            "down": ["LevelM70",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM80 [Indent level: 6],
                        "levelm80": {
                            "type": "line",
                            "points": [["LevelM80",[-0.175,-0.02],1],["LevelM80",[-0.175,0],1],[],["LevelM80",[-0.16,"-0.001*1"],1],["LevelM80",[-0.145,"-0.001*2"],1],[],["LevelM80",[-0.13,"-0.001*3"],1],["LevelM80",[-0.115,"-0.001*4"],1],[],["LevelM80",[-0.1,"-0.001*5"],1],["LevelM80",[-0.085,"-0.001*6"],1],[],["LevelM80",[-0.07,"-0.001*7"],1],["LevelM80",[-0.055,"-0.001*8"],1],[],["LevelM80",[-0.04,"-0.001*9"],1],[],["LevelM80",[0.175,-0.02],1],["LevelM80",[0.175,0],1],[],["LevelM80",[0.16,"-0.001*1"],1],["LevelM80",[0.145,"-0.001*2"],1],[],["LevelM80",[0.13,"-0.001*3"],1],["LevelM80",[0.115,"-0.001*4"],1],[],["LevelM80",[0.1,"-0.001*5"],1],["LevelM80",[0.085,"-0.001*6"],1],[],["LevelM80",[0.07,"-0.001*7"],1],["LevelM80",[0.055,"-0.001*8"],1],[],["LevelM80",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_80 [Indent level: 6],
                        "valm_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM80",[-0.19,-0.032],1],
                            "right": ["LevelM80",[-0.13,-0.032],1],
                            "down": ["LevelM80",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_80_R [Indent level: 6],
                        "valm_1_80_r": {
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM80",[0.19,-0.032],1],
                            "right": ["LevelM80",[0.25,-0.032],1],
                            "down": ["LevelM80",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|LevelM90 [Indent level: 6],
                        "levelm90": {
                            "type": "line",
                            "points": [["LevelM90",[-0.175,-0.02],1],["LevelM90",[-0.175,0],1],[],["LevelM90",[-0.16,"-0.001*1"],1],["LevelM90",[-0.145,"-0.001*2"],1],[],["LevelM90",[-0.13,"-0.001*3"],1],["LevelM90",[-0.115,"-0.001*4"],1],[],["LevelM90",[-0.1,"-0.001*5"],1],["LevelM90",[-0.085,"-0.001*6"],1],[],["LevelM90",[-0.07,"-0.001*7"],1],["LevelM90",[-0.055,"-0.001*8"],1],[],["LevelM90",[-0.04,"-0.001*9"],1],[],["LevelM90",[0.175,-0.02],1],["LevelM90",[0.175,0],1],[],["LevelM90",[0.16,"-0.001*1"],1],["LevelM90",[0.145,"-0.001*2"],1],[],["LevelM90",[0.13,"-0.001*3"],1],["LevelM90",[0.115,"-0.001*4"],1],[],["LevelM90",[0.1,"-0.001*5"],1],["LevelM90",[0.085,"-0.001*6"],1],[],["LevelM90",[0.07,"-0.001*7"],1],["LevelM90",[0.055,"-0.001*8"],1],[],["LevelM90",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_90 [Indent level: 6],
                        "valm_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": -90,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM90",[-0.19,-0.032],1],
                            "right": ["LevelM90",[-0.13,-0.032],1],
                            "down": ["LevelM90",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HorizontBackground|HorizontBlack|VALM_1_90_R [Indent level: 6],
                        "valm_1_90_r": {
                            "type": "text",
                            "source": "static",
                            "text": -90,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM90",[0.19,-0.032],1],
                            "right": ["LevelM90",[0.25,-0.032],1],
                            "down": ["LevelM90",[0.19,0.018],1]
                        }
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|BlackBackground [Indent level: 4],
                "blackbackground": {
                    "color": [0,0,0],
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|BlackBackground|Static [Indent level: 5],
                    "static": {
                        "type": "polygon",
                        "points": [[[[0.01,0.08],1],[[0.18,0.08],1],[[0.18,0.25],1],[[0.01,0.25],1]],[[[0.27,0.08],1],[[0.41,0.08],1],[[0.41,0.17],1],[[0.27,0.17],1]],[[[0.51,0.08],1],[[0.69,0.08],1],[[0.69,0.25],1],[[0.51,0.25],1]],[[[0.01,0.42],1],[[0.14,0.42],1],[[0.14,0.53],1],[[0.01,0.53],1]],[[[0.51,0.42],1],[[0.69,0.42],1],[[0.69,0.53],1],[[0.51,0.53],1]],[[[0.52,0.79],1],[[0.69,0.79],1],[[0.69,0.88],1],[[0.52,0.88],1]]]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|HeadingText [Indent level: 4],
                "headingtext": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "refreshrate": 0.1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.29,0.09],1],
                    "right": [[0.36,0.09],1],
                    "down": [[0.29,0.16],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green [Indent level: 4],
                "green": {
                    "color": [0.15,1,0.15,1],
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|Throttle1 [Indent level: 5],
                    "throttle1": {
                        "type": "text",
                        "source": "throttle",
                        "sourcescale": 100,
                        "sourcelength": 1,
                        "refreshrate": 0.07,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.12,0.09],1],
                        "right": [[0.17,0.09],1],
                        "down": [[0.12,0.16],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|Throttle1Static_Text [Indent level: 5],
                    "throttle1static_text": {
                        "type": "text",
                        "source": "static",
                        "text": "%",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.14,0.09],1],
                        "right": [[0.19,0.09],1],
                        "down": [[0.14,0.16],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|Throttle2 [Indent level: 5],
                    "throttle2": {
                        "type": "text",
                        "source": "throttle",
                        "sourcescale": 100,
                        "sourcelength": 1,
                        "refreshrate": 0.07,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.62,0.09],1],
                        "right": [[0.67,0.09],1],
                        "down": [[0.62,0.16],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|Throttle2Static_Text [Indent level: 5],
                    "throttle2static_text": {
                        "type": "text",
                        "source": "static",
                        "text": "%",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.64,0.09],1],
                        "right": [[0.69,0.09],1],
                        "down": [[0.64,0.16],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|temp1 [Indent level: 5],
                    "temp1": {
                        "type": "text",
                        "source": "rpm",
                        "sourcescale": 645,
                        "sourcelength": 1,
                        "refreshrate": 0.07,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.12,0.17],1],
                        "right": [[0.17,0.17],1],
                        "down": [[0.12,0.24],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|temp1Static_Text [Indent level: 5],
                    "temp1static_text": {
                        "type": "text",
                        "source": "static",
                        "text": "o",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.14,0.15],1],
                        "right": [[0.19,0.15],1],
                        "down": [[0.14,0.22],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|temp2 [Indent level: 5],
                    "temp2": {
                        "type": "text",
                        "source": "rpm",
                        "sourcescale": 673,
                        "sourcelength": 1,
                        "refreshrate": 0.07,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.62,0.17],1],
                        "right": [[0.67,0.17],1],
                        "down": [[0.62,0.24],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|temp2Static_Text [Indent level: 5],
                    "temp2static_text": {
                        "type": "text",
                        "source": "static",
                        "text": "o",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.64,0.15],1],
                        "right": [[0.69,0.15],1],
                        "down": [[0.64,0.22],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|BaroStatic_Text [Indent level: 5],
                    "barostatic_text": {
                        "type": "text",
                        "source": "static",
                        "text": "BARO",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.06,0.89],1],
                        "right": [[0.12,0.89],1],
                        "down": [[0.06,0.96],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|BaroSource_Text [Indent level: 5],
                    "barosource_text": {
                        "type": "text",
                        "source": "altitudeAGL",
                        "sourcescale": 1,
                        "sourceprecision": 1,
                        "sourceoffset": -2.5,
                        "sourcelength": 5,
                        "refreshrate": 0.07,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.2,0.89],1],
                        "right": [[0.25,0.89],1],
                        "down": [[0.2,0.96],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|Cord_Text [Indent level: 5],
                    "cord_text": {
                        "type": "text",
                        "source": "static",
                        "text": "POS:",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.4,0.89],1],
                        "right": [[0.45,0.89],1],
                        "down": [[0.4,0.96],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|CordX [Indent level: 5],
                    "cordx": {
                        "type": "text",
                        "source": "coordinateX",
                        "sourcescale": 0.01,
                        "sourcelength": 3,
                        "sourceoffset": -0.5,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.5,0.89],1],
                        "right": [[0.55,0.89],1],
                        "down": [[0.5,0.96],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|CordY [Indent level: 5],
                    "cordy": {
                        "source": "coordinateY",
                        "pos": [["0.5+0.07",0.89],1],
                        "right": [[0.62,0.89],1],
                        "down": [["0.5+0.07",0.96],1],
                        "type": "text",
                        "sourcescale": 0.01,
                        "sourcelength": 3,
                        "sourceoffset": -0.5,
                        "align": "right",
                        "scale": 1
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|FuelRemaining_Text [Indent level: 5],
                    "fuelremaining_text": {
                        "type": "text",
                        "source": "static",
                        "text": "I:",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.73,0.09],1],
                        "right": [[0.79,0.09],1],
                        "down": [[0.73,0.17],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|FuelRemaining_Source [Indent level: 5],
                    "fuelremaining_source": {
                        "type": "text",
                        "source": "fuel",
                        "sourcescale": 20,
                        "sourceprecision": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.79,0.09],1],
                        "right": [[0.85,0.09],1],
                        "down": [[0.79,0.17],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|TimeRemaining_Text [Indent level: 5],
                    "timeremaining_text": {
                        "type": "text",
                        "source": "static",
                        "text": "T:",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.73,0.17],1],
                        "right": [[0.79,0.17],1],
                        "down": [[0.73,0.25],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|TimeRemaining_Source [Indent level: 5],
                    "timeremaining_source": {
                        "type": "text",
                        "source": "fuel",
                        "sourcescale": 2.4,
                        "sourceprecision": 2,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.79,0.17],1],
                        "right": [[0.85,0.17],1],
                        "down": [[0.79,0.25],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|FuelSt20_Text [Indent level: 5],
                    "fuelst20_text": {
                        "type": "text",
                        "source": "static",
                        "text": "20",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [[0.92,0.27],1],
                        "right": [[0.98,0.27],1],
                        "down": [[0.92,0.33],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|FuelSt10_Text [Indent level: 5],
                    "fuelst10_text": {
                        "type": "text",
                        "source": "static",
                        "text": "10",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [[0.92,0.46],1],
                        "right": [[0.98,0.46],1],
                        "down": [[0.92,0.52],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|FuelSt8_Text [Indent level: 5],
                    "fuelst8_text": {
                        "type": "text",
                        "source": "static",
                        "text": "8",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [[0.92,0.55],1],
                        "right": [[0.98,0.55],1],
                        "down": [[0.92,0.61],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|FuelSt6_Text [Indent level: 5],
                    "fuelst6_text": {
                        "type": "text",
                        "source": "static",
                        "text": "6",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [[0.92,0.65],1],
                        "right": [[0.98,0.65],1],
                        "down": [[0.92,0.71],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|FuelSt4_Text [Indent level: 5],
                    "fuelst4_text": {
                        "type": "text",
                        "source": "static",
                        "text": "4",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [[0.92,0.75],1],
                        "right": [[0.98,0.75],1],
                        "down": [[0.92,0.81],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|Green|FuelSt2_Text [Indent level: 5],
                    "fuelst2_text": {
                        "type": "text",
                        "source": "static",
                        "text": "2",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [[0.92,0.82],1],
                        "right": [[0.98,0.82],1],
                        "down": [[0.92,0.88],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|SpeedSource [Indent level: 4],
                "speedsource": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 3.6,
                    "sourcelength": 3,
                    "refreshrate": 0.1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.03,0.44],1],
                    "right": [[0.1,0.44],1],
                    "down": [[0.03,0.52],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|RadarHeightSource [Indent level: 4],
                "radarheightsource": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 1,
                    "sourcelength": 5,
                    "refreshrate": 0.1,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.68,0.44],1],
                    "right": [[0.75,0.44],1],
                    "down": [[0.68,0.52],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|ClimbSource [Indent level: 4],
                "climbsource": {
                    "type": "text",
                    "source": "vspeed",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "refreshrate": 0.1,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.68,0.8],1],
                    "right": [[0.75,0.8],1],
                    "down": [[0.68,0.88],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_2|Draw|StaticDraw [Indent level: 4],
                "staticdraw": {
                    "type": "line",
                    "width": 10,
                    "points": [["Center",[0,-0.0392647],1],["Center",[0.005208,-0.0386679],1],["Center",[0.01026,-0.036897],1],["Center",[0.015,-0.0340032],1],["Center",[0.019284,-0.0300768],1],["Center",[0.02298,-0.0252394],1],["Center",[0.02598,-0.0196324],1],["Center",[0.028191,-0.0134285],1],["Center",[0.029544,-0.00681635],1],["Center",[0.03,0],1],["Center",[0.029544,0.00681635],1],["Center",[0.028191,0.0134285],1],["Center",[0.02598,0.0196324],1],["Center",[0.02298,0.0252394],1],["Center",[0.019284,0.0300768],1],["Center",[0.015,0.0340032],1],["Center",[0.01026,0.036897],1],["Center",[0.005208,0.0386679],1],["Center",[0,0.0392647],1],["Center",[-0.005208,0.0386679],1],["Center",[-0.01026,0.036897],1],["Center",[-0.015,0.0340032],1],["Center",[-0.019284,0.0300768],1],["Center",[-0.02298,0.0252394],1],["Center",[-0.02598,0.0196324],1],["Center",[-0.028191,0.0134285],1],["Center",[-0.029544,0.00681635],1],["Center",[-0.03,0],1],["Center",[-0.029544,-0.00681635],1],["Center",[-0.028191,-0.0134285],1],["Center",[-0.02598,-0.0196324],1],["Center",[-0.02298,-0.0252394],1],["Center",[-0.019284,-0.0300768],1],["Center",[-0.015,-0.0340032],1],["Center",[-0.01026,-0.036897],1],["Center",[-0.005208,-0.0386679],1],["Center",[0,-0.0392647],1]]
                }
            }
        },
        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3 [Indent level: 2],
        "mfd_3": {
            "topleft": "MFD_3_TL",
            "topright": "MFD_3_TR",
            "bottomleft": "MFD_3_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|material [Indent level: 3],
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw [Indent level: 3],
            "draw": {
                "condition": "on",
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|Rpm1Source [Indent level: 4],
                "rpm1source": {
                    "type": "text",
                    "source": "rpm",
                    "sourcescale": 100,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.3,0.135],1],
                    "right": [[0.34,0.135],1],
                    "down": [[0.3,0.175],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|Rpm2Source [Indent level: 4],
                "rpm2source": {
                    "pos": [[0.64,0.135],1],
                    "right": [[0.68,0.135],1],
                    "down": [[0.64,0.175],1],
                    "type": "text",
                    "source": "rpm",
                    "sourcescale": 100,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|EGT1Source [Indent level: 4],
                "egt1source": {
                    "type": "text",
                    "source": "rpm",
                    "sourcescale": 380,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.3,0.29],1],
                    "right": [[0.34,0.29],1],
                    "down": [[0.3,0.33],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|EGT2Source [Indent level: 4],
                "egt2source": {
                    "pos": [[0.64,0.29],1],
                    "right": [[0.68,0.29],1],
                    "down": [[0.64,0.33],1],
                    "type": "text",
                    "source": "rpm",
                    "sourcescale": 380,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|noz1Source [Indent level: 4],
                "noz1source": {
                    "type": "text",
                    "source": "throttle",
                    "sourcescale": 100,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.33,0.475],1],
                    "right": [[0.36,0.475],1],
                    "down": [[0.33,0.505],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|noz2Source [Indent level: 4],
                "noz2source": {
                    "pos": [[0.66,0.475],1],
                    "right": [[0.69,0.475],1],
                    "down": [[0.66,0.505],1],
                    "type": "text",
                    "source": "throttle",
                    "sourcescale": 100,
                    "align": "center",
                    "scale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|oil1Source [Indent level: 4],
                "oil1source": {
                    "type": "text",
                    "source": "rpm",
                    "sourcescale": 235,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.31,0.58],1],
                    "right": [[0.35,0.58],1],
                    "down": [[0.31,0.62],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|oil2Source [Indent level: 4],
                "oil2source": {
                    "pos": [[0.65,0.58],1],
                    "right": [[0.69,0.58],1],
                    "down": [[0.65,0.62],1],
                    "type": "text",
                    "source": "rpm",
                    "sourcescale": 235,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|hyd1Source [Indent level: 4],
                "hyd1source": {
                    "type": "text",
                    "source": "rpm",
                    "sourcescale": 210,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.13,0.81],1],
                    "right": [[0.16,0.81],1],
                    "down": [[0.13,0.84],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|hyd2Source [Indent level: 4],
                "hyd2source": {
                    "pos": [[0.38,0.81],1],
                    "right": [[0.41,0.81],1],
                    "down": [[0.38,0.84],1],
                    "type": "text",
                    "source": "rpm",
                    "sourcescale": 210,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_3|Draw|FuelLeftSource [Indent level: 4],
                "fuelleftsource": {
                    "type": "text",
                    "source": "fuel",
                    "sourcescale": 2000,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.8,0.92],1],
                    "right": [[0.85,0.92],1],
                    "down": [[0.8,0.97],1]
                }
            }
        },
        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4 [Indent level: 2],
        "mfd_4": {
            "topleft": "MFD_4_TL",
            "topright": "MFD_4_TR",
            "bottomleft": "MFD_4_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|material [Indent level: 3],
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Sensor_Offset [Indent level: 4]
                "sensor_offset": {
                    "type": "fixed",
                    "pos": [0,0.33]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Static_Offset [Indent level: 4],
                "static_offset": {
                    "type": "fixed",
                    "pos": [0.5,0.85]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Static_Offset2 [Indent level: 4],
                "static_offset2": {
                    "pos": [0.5,0.83],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_0 [Indent level: 4],
                "rotation_0": {
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "minangle": 0,
                    "maxangle": -360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_10 [Indent level: 4],
                "rotation_10": {
                    "minangle": 10,
                    "maxangle": -350,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_20 [Indent level: 4],
                "rotation_20": {
                    "minangle": 20,
                    "maxangle": -340,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_30 [Indent level: 4],
                "rotation_30": {
                    "minangle": 30,
                    "maxangle": -330,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_40 [Indent level: 4],
                "rotation_40": {
                    "minangle": 40,
                    "maxangle": -320,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_50 [Indent level: 4],
                "rotation_50": {
                    "minangle": 50,
                    "maxangle": -310,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_60 [Indent level: 4],
                "rotation_60": {
                    "minangle": 60,
                    "maxangle": -300,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_70 [Indent level: 4],
                "rotation_70": {
                    "minangle": 70,
                    "maxangle": -290,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_80 [Indent level: 4],
                "rotation_80": {
                    "minangle": 80,
                    "maxangle": -280,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_90 [Indent level: 4],
                "rotation_90": {
                    "minangle": 90,
                    "maxangle": -270,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_100 [Indent level: 4],
                "rotation_100": {
                    "minangle": 100,
                    "maxangle": -260,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_110 [Indent level: 4],
                "rotation_110": {
                    "minangle": 110,
                    "maxangle": -250,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_120 [Indent level: 4],
                "rotation_120": {
                    "minangle": 120,
                    "maxangle": -240,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_130 [Indent level: 4],
                "rotation_130": {
                    "minangle": 130,
                    "maxangle": -230,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_140 [Indent level: 4],
                "rotation_140": {
                    "minangle": 140,
                    "maxangle": -220,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_150 [Indent level: 4],
                "rotation_150": {
                    "minangle": 150,
                    "maxangle": -210,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_160 [Indent level: 4],
                "rotation_160": {
                    "minangle": 160,
                    "maxangle": -200,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_170 [Indent level: 4],
                "rotation_170": {
                    "minangle": 170,
                    "maxangle": -190,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_180 [Indent level: 4],
                "rotation_180": {
                    "minangle": 180,
                    "maxangle": -180,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_190 [Indent level: 4],
                "rotation_190": {
                    "minangle": 190,
                    "maxangle": -170,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_200 [Indent level: 4],
                "rotation_200": {
                    "minangle": 200,
                    "maxangle": -160,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_210 [Indent level: 4],
                "rotation_210": {
                    "minangle": 210,
                    "maxangle": -150,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_220 [Indent level: 4],
                "rotation_220": {
                    "minangle": 220,
                    "maxangle": -140,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_230 [Indent level: 4],
                "rotation_230": {
                    "minangle": 230,
                    "maxangle": -130,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_240 [Indent level: 4],
                "rotation_240": {
                    "minangle": 240,
                    "maxangle": -120,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_250 [Indent level: 4],
                "rotation_250": {
                    "minangle": 250,
                    "maxangle": -110,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_260 [Indent level: 4],
                "rotation_260": {
                    "minangle": 260,
                    "maxangle": -100,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_270 [Indent level: 4],
                "rotation_270": {
                    "minangle": 270,
                    "maxangle": -90,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_280 [Indent level: 4],
                "rotation_280": {
                    "minangle": 280,
                    "maxangle": -80,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_290 [Indent level: 4],
                "rotation_290": {
                    "minangle": 290,
                    "maxangle": -70,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_300 [Indent level: 4],
                "rotation_300": {
                    "minangle": 300,
                    "maxangle": -60,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_310 [Indent level: 4],
                "rotation_310": {
                    "minangle": 310,
                    "maxangle": -50,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_320 [Indent level: 4],
                "rotation_320": {
                    "minangle": 320,
                    "maxangle": -40,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_330 [Indent level: 4],
                "rotation_330": {
                    "minangle": 330,
                    "maxangle": -30,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_340 [Indent level: 4],
                "rotation_340": {
                    "minangle": 340,
                    "maxangle": -20,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_350 [Indent level: 4],
                "rotation_350": {
                    "minangle": 350,
                    "maxangle": -10,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_0 [Indent level: 4],
                "rotation_inv_0": {
                    "min": 0,
                    "max": 360,
                    "minangle": 180,
                    "maxangle": -180,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_30 [Indent level: 4],
                "rotation_inv_30": {
                    "minangle": 210,
                    "maxangle": -150,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_60 [Indent level: 4],
                "rotation_inv_60": {
                    "minangle": 240,
                    "maxangle": -120,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_90 [Indent level: 4],
                "rotation_inv_90": {
                    "minangle": 270,
                    "maxangle": -90,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_120 [Indent level: 4],
                "rotation_inv_120": {
                    "minangle": 300,
                    "maxangle": -60,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_150 [Indent level: 4],
                "rotation_inv_150": {
                    "minangle": 330,
                    "maxangle": -30,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_180 [Indent level: 4],
                "rotation_inv_180": {
                    "minangle": 360,
                    "maxangle": 0,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_210 [Indent level: 4],
                "rotation_inv_210": {
                    "minangle": 390,
                    "maxangle": 30,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_240 [Indent level: 4],
                "rotation_inv_240": {
                    "minangle": 420,
                    "maxangle": 60,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_270 [Indent level: 4],
                "rotation_inv_270": {
                    "minangle": 450,
                    "maxangle": 90,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_300 [Indent level: 4],
                "rotation_inv_300": {
                    "minangle": 480,
                    "maxangle": 120,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|Rotation_Inv_330 [Indent level: 4],
                "rotation_inv_330": {
                    "minangle": 510,
                    "maxangle": 150,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|MovementY [Indent level: 4],
                "movementy": {
                    "type": "linear",
                    "source": "user",
                    "sourceindex": 5,
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|MovementX [Indent level: 4],
                "movementx": {
                    "sourceindex": 4,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|PlaneDirection [Indent level: 4],
                "planedirection": {
                    "type": "rotational",
                    "source": "heading",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 360,
                    "minangle": 0,
                    "maxangle": 360,
                    "aspectratio": 1.02865
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP1_PosX [Indent level: 4],
                "wp1_posx": {
                    "sourceindex": 6,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP1_PosY [Indent level: 4],
                "wp1_posy": {
                    "sourceindex": 7,
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP2_PosX [Indent level: 4],
                "wp2_posx": {
                    "sourceindex": 8,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP2_PosY [Indent level: 4],
                "wp2_posy": {
                    "sourceindex": 9,
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP3_PosX [Indent level: 4],
                "wp3_posx": {
                    "sourceindex": 10,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP3_PosY [Indent level: 4],
                "wp3_posy": {
                    "sourceindex": 11,
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP4_PosX [Indent level: 4],
                "wp4_posx": {
                    "sourceindex": 12,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP4_PosY [Indent level: 4],
                "wp4_posy": {
                    "sourceindex": 13,
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP5_PosX [Indent level: 4],
                "wp5_posx": {
                    "sourceindex": 14,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP5_PosY [Indent level: 4],
                "wp5_posy": {
                    "sourceindex": 15,
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP6_PosX [Indent level: 4],
                "wp6_posx": {
                    "sourceindex": 16,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP6_PosY [Indent level: 4],
                "wp6_posy": {
                    "sourceindex": 17,
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP7_PosX [Indent level: 4],
                "wp7_posx": {
                    "sourceindex": 18,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP7_PosY [Indent level: 4],
                "wp7_posy": {
                    "sourceindex": 19,
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP8_PosX [Indent level: 4],
                "wp8_posx": {
                    "sourceindex": 20,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP8_PosY [Indent level: 4],
                "wp8_posy": {
                    "sourceindex": 21,
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP9_PosX [Indent level: 4],
                "wp9_posx": {
                    "sourceindex": 22,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP9_PosY [Indent level: 4],
                "wp9_posy": {
                    "sourceindex": 23,
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP10_PosX [Indent level: 4],
                "wp10_posx": {
                    "sourceindex": 24,
                    "maxpos": [-10,0],
                    "minpos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Bones|WP10_PosY [Indent level: 4],
                "wp10_posy": {
                    "sourceindex": 25,
                    "type": "linear",
                    "source": "user",
                    "refreshrate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourcescale": 1,
                    "maxpos": [0,10],
                    "minpos": [0,-10]
                }
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw [Indent level: 3],
            "draw": {
                "condition": "on",
                "alpha": 0.3,
                "color": [0,0.03,0.17],
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Static [Indent level: 4],
                "draw_static": {
                    "type": "line",
                    "width": 10,
                    "points": [["Static_Offset",[0,-0.699479],1],["Static_Offset",[0.118048,-0.688847],1],["Static_Offset",[0.23256,-0.657301],1],["Static_Offset",[0.34,-0.605749],1],["Static_Offset",[0.437104,-0.535801],1],["Static_Offset",[0.52088,-0.449625],1],["Static_Offset",[0.58888,-0.34974],1],["Static_Offset",[0.638996,-0.239222],1],["Static_Offset",[0.669664,-0.12143],1],["Static_Offset",[0.68,0],1],["Static_Offset",[0.669664,0.12143],1],["Static_Offset",[0.638996,0.239222],1],["Static_Offset",[0.58888,0.34974],1],["Static_Offset",[0.52088,0.449625],1],["Static_Offset",[0.437104,0.535801],1],["Static_Offset",[0.34,0.605749],1],["Static_Offset",[0.23256,0.657301],1],["Static_Offset",[0.118048,0.688847],1],["Static_Offset",[0,0.699479],1],["Static_Offset",[-0.118048,0.688847],1],["Static_Offset",[-0.23256,0.657301],1],["Static_Offset",[-0.34,0.605749],1],["Static_Offset",[-0.437104,0.535801],1],["Static_Offset",[-0.52088,0.449625],1],["Static_Offset",[-0.58888,0.34974],1],["Static_Offset",[-0.638996,0.239222],1],["Static_Offset",[-0.669664,0.12143],1],["Static_Offset",[-0.68,0],1],["Static_Offset",[-0.669664,-0.12143],1],["Static_Offset",[-0.638996,-0.239222],1],["Static_Offset",[-0.58888,-0.34974],1],["Static_Offset",[-0.52088,-0.449625],1],["Static_Offset",[-0.437104,-0.535801],1],["Static_Offset",[-0.34,-0.605749],1],["Static_Offset",[-0.23256,-0.657301],1],["Static_Offset",[-0.118048,-0.688847],1],["Static_Offset",[0,-0.699479],1],[],["Static_Offset",[0,-0.34974],1],["Static_Offset",[0.059024,-0.344424],1],["Static_Offset",[0.11628,-0.32865],1],["Static_Offset",[0.17,-0.302874],1],["Static_Offset",[0.218552,-0.267901],1],["Static_Offset",[0.26044,-0.224813],1],["Static_Offset",[0.29444,-0.17487],1],["Static_Offset",[0.319498,-0.119611],1],["Static_Offset",[0.334832,-0.0607148],1],["Static_Offset",[0.34,0],1],["Static_Offset",[0.334832,0.0607148],1],["Static_Offset",[0.319498,0.119611],1],["Static_Offset",[0.29444,0.17487],1],["Static_Offset",[0.26044,0.224813],1],["Static_Offset",[0.218552,0.267901],1],["Static_Offset",[0.17,0.302874],1],["Static_Offset",[0.11628,0.32865],1],["Static_Offset",[0.059024,0.344424],1],["Static_Offset",[0,0.34974],1],["Static_Offset",[-0.059024,0.344424],1],["Static_Offset",[-0.11628,0.32865],1],["Static_Offset",[-0.17,0.302874],1],["Static_Offset",[-0.218552,0.267901],1],["Static_Offset",[-0.26044,0.224813],1],["Static_Offset",[-0.29444,0.17487],1],["Static_Offset",[-0.319498,0.119611],1],["Static_Offset",[-0.334832,0.0607148],1],["Static_Offset",[-0.34,0],1],["Static_Offset",[-0.334832,-0.0607148],1],["Static_Offset",[-0.319498,-0.119611],1],["Static_Offset",[-0.29444,-0.17487],1],["Static_Offset",[-0.26044,-0.224813],1],["Static_Offset",[-0.218552,-0.267901],1],["Static_Offset",[-0.17,-0.302874],1],["Static_Offset",[-0.11628,-0.32865],1],["Static_Offset",[-0.059024,-0.344424],1],["Static_Offset",[0,-0.34974],1],[],["Static_Offset",[0,-0.7],1],["Static_Offset",[0,-0.76],1],["Static_Offset",[0.07,-0.76],1],["Static_Offset",[0.07,-0.83],1],["Static_Offset",[-0.07,-0.83],1],["Static_Offset",[-0.07,-0.76],1],["Static_Offset",[0,-0.76],1],[],["Static_Offset",1,["Rotation_0",0,0.695],1],["Static_Offset",1,["Rotation_0",0,0.655],1],[],["Static_Offset",1,["Rotation_10",0,0.695],1],["Static_Offset",1,["Rotation_10",0,0.67],1],[],["Static_Offset",1,["Rotation_20",0,0.695],1],["Static_Offset",1,["Rotation_20",0,0.67],1],[],["Static_Offset",1,["Rotation_30",0,0.695],1],["Static_Offset",1,["Rotation_30",0,0.655],1],[],["Static_Offset",1,["Rotation_40",0,0.695],1],["Static_Offset",1,["Rotation_40",0,0.67],1],[],["Static_Offset",1,["Rotation_50",0,0.695],1],["Static_Offset",1,["Rotation_50",0,0.67],1],[],["Static_Offset",1,["Rotation_60",0,0.695],1],["Static_Offset",1,["Rotation_60",0,0.655],1],[],["Static_Offset",1,["Rotation_70",0,0.695],1],["Static_Offset",1,["Rotation_70",0,0.67],1],[],["Static_Offset",1,["Rotation_80",0,0.695],1],["Static_Offset",1,["Rotation_80",0,0.67],1],[],["Static_Offset",1,["Rotation_90",0,0.695],1],["Static_Offset",1,["Rotation_90",0,0.655],1],[],["Static_Offset",1,["Rotation_100",0,0.695],1],["Static_Offset",1,["Rotation_100",0,0.67],1],[],["Static_Offset",1,["Rotation_110",0,0.695],1],["Static_Offset",1,["Rotation_110",0,0.67],1],[],["Static_Offset",1,["Rotation_120",0,0.695],1],["Static_Offset",1,["Rotation_120",0,0.655],1],[],["Static_Offset",1,["Rotation_130",0,0.695],1],["Static_Offset",1,["Rotation_130",0,0.67],1],[],["Static_Offset",1,["Rotation_140",0,0.695],1],["Static_Offset",1,["Rotation_140",0,0.67],1],[],["Static_Offset",1,["Rotation_150",0,0.695],1],["Static_Offset",1,["Rotation_150",0,0.655],1],[],["Static_Offset",1,["Rotation_160",0,0.695],1],["Static_Offset",1,["Rotation_160",0,0.67],1],[],["Static_Offset",1,["Rotation_170",0,0.695],1],["Static_Offset",1,["Rotation_170",0,0.67],1],[],["Static_Offset",1,["Rotation_180",0,0.695],1],["Static_Offset",1,["Rotation_180",0,0.655],1],[],["Static_Offset",1,["Rotation_190",0,0.695],1],["Static_Offset",1,["Rotation_190",0,0.67],1],[],["Static_Offset",1,["Rotation_200",0,0.695],1],["Static_Offset",1,["Rotation_200",0,0.67],1],[],["Static_Offset",1,["Rotation_210",0,0.695],1],["Static_Offset",1,["Rotation_210",0,0.655],1],[],["Static_Offset",1,["Rotation_220",0,0.695],1],["Static_Offset",1,["Rotation_220",0,0.67],1],[],["Static_Offset",1,["Rotation_230",0,0.695],1],["Static_Offset",1,["Rotation_230",0,0.67],1],[],["Static_Offset",1,["Rotation_240",0,0.695],1],["Static_Offset",1,["Rotation_240",0,0.655],1],[],["Static_Offset",1,["Rotation_250",0,0.695],1],["Static_Offset",1,["Rotation_250",0,0.67],1],[],["Static_Offset",1,["Rotation_260",0,0.695],1],["Static_Offset",1,["Rotation_260",0,0.67],1],[],["Static_Offset",1,["Rotation_270",0,0.695],1],["Static_Offset",1,["Rotation_270",0,0.655],1],[],["Static_Offset",1,["Rotation_280",0,0.695],1],["Static_Offset",1,["Rotation_280",0,0.67],1],[],["Static_Offset",1,["Rotation_290",0,0.695],1],["Static_Offset",1,["Rotation_290",0,0.67],1],[],["Static_Offset",1,["Rotation_300",0,0.695],1],["Static_Offset",1,["Rotation_300",0,0.655],1],[],["Static_Offset",1,["Rotation_310",0,0.695],1],["Static_Offset",1,["Rotation_310",0,0.67],1],[],["Static_Offset",1,["Rotation_320",0,0.695],1],["Static_Offset",1,["Rotation_320",0,0.67],1],[],["Static_Offset",1,["Rotation_330",0,0.695],1],["Static_Offset",1,["Rotation_330",0,0.655],1],[],["Static_Offset",1,["Rotation_340",0,0.695],1],["Static_Offset",1,["Rotation_340",0,0.67],1],[],["Static_Offset",1,["Rotation_350",0,0.695],1],["Static_Offset",1,["Rotation_350",0,0.67],1],[],[]]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_0_Text [Indent level: 4],
                "rotation_0_text": {
                    "type": "text",
                    "source": "static",
                    "text": "N",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_0",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_0",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_0",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_30_Text [Indent level: 4],
                "rotation_30_text": {
                    "type": "text",
                    "source": "static",
                    "text": "03",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_30",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_30",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_30",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_60_Text [Indent level: 4],
                "rotation_60_text": {
                    "type": "text",
                    "source": "static",
                    "text": "06",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_60",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_60",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_60",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_90_Text [Indent level: 4],
                "rotation_90_text": {
                    "type": "text",
                    "source": "static",
                    "text": "E",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_90",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_90",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_90",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_120_Text [Indent level: 4],
                "rotation_120_text": {
                    "type": "text",
                    "source": "static",
                    "text": "12",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_120",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_120",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_120",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_150_Text [Indent level: 4],
                "rotation_150_text": {
                    "type": "text",
                    "source": "static",
                    "text": "15",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_150",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_150",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_150",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_180_Text [Indent level: 4],
                "rotation_180_text": {
                    "type": "text",
                    "source": "static",
                    "text": "S",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_180",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_180",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_180",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_210_Text [Indent level: 4],
                "rotation_210_text": {
                    "type": "text",
                    "source": "static",
                    "text": "21",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_210",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_210",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_210",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_240_Text [Indent level: 4],
                "rotation_240_text": {
                    "type": "text",
                    "source": "static",
                    "text": "24",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_240",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_240",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_240",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_270_Text [Indent level: 4],
                "rotation_270_text": {
                    "type": "text",
                    "source": "static",
                    "text": "W",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_270",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_270",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_270",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_300_Text [Indent level: 4],
                "rotation_300_text": {
                    "type": "text",
                    "source": "static",
                    "text": "30",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_300",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_300",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_300",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Rotation_330_Text [Indent level: 4],
                "rotation_330_text": {
                    "type": "text",
                    "source": "static",
                    "text": "33",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_330",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_330",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_330",0,-0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|BackgroundBlack [Indent level: 4],
                "backgroundblack": {
                    "color": [0,0,0],
                    "alpha": 1,
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|BackgroundBlack|Static [Indent level: 5],
                    "static": {
                        "type": "polygon",
                        "points": [[[[0.68,0.55],1],[[0.75,0.55],1],[[0.75,0.6],1],[[0.68,0.6],1]],[[[0.83,0.2],1],[[0.92,0.2],1],[[0.92,0.3],1],[[0.83,0.3],1]]]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White [Indent level: 4],
                "draw_white": {
                    "color": [1,1,1],
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|HeadingText [Indent level: 5],
                    "headingtext": {
                        "type": "text",
                        "source": "heading",
                        "sourcescale": 1,
                        "sourcelength": 3,
                        "refreshrate": 0.1,
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,0.03],1],
                        "right": [[0.56,0.03],1],
                        "down": [[0.5,0.09],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|Range_Text [Indent level: 5],
                    "range_text": {
                        "type": "text",
                        "source": "static",
                        "text": "36",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [[0.92,0.23],1],
                        "right": [[0.99,0.23],1],
                        "down": [[0.92,0.3],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|MFlare_Text [Indent level: 5],
                    "mflare_text": {
                        "type": "text",
                        "source": "static",
                        "text": "LPE4",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.86,0.03],1],
                        "right": [[0.91,0.03],1],
                        "down": [[0.86,0.08],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|RangesData1_Text [Indent level: 5],
                    "rangesdata1_text": {
                        "type": "text",
                        "source": "static",
                        "text": "346/97",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.01,0.07],1],
                        "right": [[0.05,0.07],1],
                        "down": [[0.01,0.11],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|Pos_Text [Indent level: 5],
                    "pos_text": {
                        "type": "text",
                        "source": "static",
                        "text": "GRID",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.79,0.84],1],
                        "right": [[0.83,0.84],1],
                        "down": [[0.79,0.88],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|CordX [Indent level: 5],
                    "cordx": {
                        "type": "text",
                        "source": "coordinateX",
                        "sourcescale": 0.01,
                        "sourcelength": 3,
                        "sourceoffset": -0.5,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.79,0.88],1],
                        "right": [[0.83,0.88],1],
                        "down": [[0.79,0.92],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|CordY [Indent level: 5],
                    "cordy": {
                        "source": "coordinateY",
                        "pos": [["0.79+0.07",0.88],1],
                        "right": [[0.9,0.88],1],
                        "down": [["0.79+0.07",0.92],1],
                        "type": "text",
                        "sourcescale": 0.01,
                        "sourcelength": 3,
                        "sourceoffset": -0.5,
                        "align": "right",
                        "scale": 1
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP [Indent level: 5],
                    "wp": {
                        "condition": "wpvalid",
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WPdist [Indent level: 6],
                        "wpdist": {
                            "type": "text",
                            "source": "wpdist",
                            "sourcescale": 0.001,
                            "sourceprecision": 1,
                            "align": "left",
                            "scale": 1,
                            "pos": [["0.79+0.15",0.915],1],
                            "right": [[0.98,0.915],1],
                            "down": [["0.79+0.15",0.955],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WPIndex [Indent level: 6],
                        "wpindex": {
                            "type": "text",
                            "source": "wpIndex",
                            "sourcescale": 1,
                            "sourcelength": 2,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.83,0.915],1],
                            "right": [[0.87,0.915],1],
                            "down": [[0.83,0.955],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WPstatic [Indent level: 6],
                        "wpstatic": {
                            "type": "text",
                            "source": "static",
                            "text": "W",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "right",
                            "pos": [[0.79,0.915],1],
                            "right": [[0.83,0.915],1],
                            "down": [[0.79,0.955],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WPAuto [Indent level: 6],
                        "wpauto": {
                            "type": "text",
                            "source": "static",
                            "text": "A",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "right",
                            "pos": [["0.790 +0.035",0.95],1],
                            "right": [[0.865,0.95],1],
                            "down": [["0.790 +0.035",0.99],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WPKM [Indent level: 6],
                        "wpkm": {
                            "type": "text",
                            "source": "static",
                            "text": "KM",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "right",
                            "pos": [["0.790 +0.16",0.915],1],
                            "right": [[0.99,0.915],1],
                            "down": [["0.790 +0.16",0.955],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WPTime [Indent level: 6],
                        "wptime": {
                            "type": "text",
                            "source": "static",
                            "text": "-:--",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "right",
                            "pos": [["0.790 +0.11",0.95],1],
                            "right": [[0.94,0.95],1],
                            "down": [["0.790 +0.11",0.99],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP1 [Indent level: 6],
                        "wp1": {
                            "condition": "user6>=0",
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP1|CurrentWaypoint [Indent level: 7],
                            "currentwaypoint": {
                                "color": [0.9,0,0],
                                "condition": "1-WPIndex",
                                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP1|CurrentWaypoint|WaypointShape [Indent level: 8],
                                "waypointshape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP1|WaypointShape [Indent level: 7],
                            "waypointshape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0,-0.0205729],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.02,0],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01,0.0178161],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0,0.0205729],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.02,0],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP2 [Indent level: 6],
                        "wp2": {
                            "condition": "user8>=0",
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP2|CurrentWaypoint [Indent level: 7],
                            "currentwaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=1)*(WPIndex<=1)",
                                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP2|CurrentWaypoint|WaypointShape [Indent level: 8],
                                "waypointshape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP2|WaypointShape [Indent level: 7],
                            "waypointshape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP1_PosX",1,"WP1_PosY",1,["PlaneDirection",0,0],1],["WP2_PosX",1,"WP2_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP3 [Indent level: 6],
                        "wp3": {
                            "condition": "user10>=0",
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP3|CurrentWaypoint [Indent level: 7],
                            "currentwaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=2)*(WPIndex<=2)",
                                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP3|CurrentWaypoint|WaypointShape [Indent level: 8],
                                "waypointshape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,-0.0205729],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.02,0],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01,0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,0.0205729],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.02,0],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP3|WaypointShape [Indent level: 7],
                            "waypointshape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,-0.0205729],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.02,0],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01,0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,0.0205729],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.02,0],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP2_PosX",1,"WP2_PosY",1,["PlaneDirection",0,0],1],["WP3_PosX",1,"WP3_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP4 [Indent level: 6],
                        "wp4": {
                            "condition": "user12>=0",
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP4|CurrentWaypoint [Indent level: 7],
                            "currentwaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=3)*(WPIndex<=3)",
                                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP4|CurrentWaypoint|WaypointShape [Indent level: 8],
                                "waypointshape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,-0.0205729],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.02,0],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01,0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,0.0205729],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.02,0],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP4|WaypointShape [Indent level: 7],
                            "waypointshape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,-0.0205729],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.02,0],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01,0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,0.0205729],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.02,0],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP3_PosX",1,"WP3_PosY",1,["PlaneDirection",0,0],1],["WP4_PosX",1,"WP4_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP5 [Indent level: 6],
                        "wp5": {
                            "condition": "user14>=0",
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP5|CurrentWaypoint [Indent level: 7],
                            "currentwaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=4)*(WPIndex<=4)",
                                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP5|CurrentWaypoint|WaypointShape [Indent level: 8],
                                "waypointshape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP5|WaypointShape [Indent level: 7],
                            "waypointshape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP4_PosX",1,"WP4_PosY",1,["PlaneDirection",0,0],1],["WP5_PosX",1,"WP5_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP6 [Indent level: 6],
                        "wp6": {
                            "condition": "user16>=0",
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP6|CurrentWaypoint [Indent level: 7],
                            "currentwaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=5)*(WPIndex<=5)",
                                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP6|CurrentWaypoint|WaypointShape [Indent level: 8],
                                "waypointshape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP6|WaypointShape [Indent level: 7],
                            "waypointshape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0,-0.0205729],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.02,0],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01,0.0178161],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0,0.0205729],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.02,0],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP5_PosX",1,"WP5_PosY",1,["PlaneDirection",0,0],1],["WP6_PosX",1,"WP6_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP7 [Indent level: 6],
                        "wp7": {
                            "condition": "user18>=0",
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP7|CurrentWaypoint [Indent level: 7],
                            "currentwaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=6)*(WPIndex<=6)",
                                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP7|CurrentWaypoint|WaypointShape [Indent level: 8],
                                "waypointshape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,-0.0205729],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.02,0],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01,0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,0.0205729],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.02,0],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP7|WaypointShape [Indent level: 7],
                            "waypointshape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,-0.0205729],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.02,0],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01,0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,0.0205729],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.02,0],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP6_PosX",1,"WP6_PosY",1,["PlaneDirection",0,0],1],["WP7_PosX",1,"WP7_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP8 [Indent level: 6],
                        "wp8": {
                            "condition": "user20>=0",
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP8|CurrentWaypoint [Indent level: 7],
                            "currentwaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=7)*(WPIndex<=7)",
                                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP8|CurrentWaypoint|WaypointShape [Indent level: 8],
                                "waypointshape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,-0.0205729],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.02,0],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01,0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,0.0205729],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.02,0],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP8|WaypointShape [Indent level: 7],
                            "waypointshape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,-0.0205729],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.02,0],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01,0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,0.0205729],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.02,0],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP7_PosX",1,"WP7_PosY",1,["PlaneDirection",0,0],1],["WP8_PosX",1,"WP8_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP9 [Indent level: 6],
                        "wp9": {
                            "condition": "user22>=0",
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP9|CurrentWaypoint [Indent level: 7],
                            "currentwaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=8)*(WPIndex<=8)",
                                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP9|CurrentWaypoint|WaypointShape [Indent level: 8],
                                "waypointshape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,-0.0205729],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.02,0],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01,0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,0.0205729],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.02,0],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP9|WaypointShape [Indent level: 7],
                            "waypointshape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,-0.0205729],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.02,0],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01,0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,0.0205729],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.02,0],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP8_PosX",1,"WP8_PosY",1,["PlaneDirection",0,0],1],["WP9_PosX",1,"WP9_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP10 [Indent level: 6],
                        "wp10": {
                            "condition": "user24>=0",
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP10|CurrentWaypoint [Indent level: 7],
                            "currentwaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=9)*(WPIndex<=9)",
                                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP10|CurrentWaypoint|WaypointShape [Indent level: 8],
                                "waypointshape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,-0.0205729],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.02,0],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01,0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,0.0205729],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.02,0],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_White|WP|WP10|WaypointShape [Indent level: 7],
                            "waypointshape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,-0.0205729],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.02,0],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01,0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,0.0205729],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.02,0],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP9_PosX",1,"WP9_PosY",1,["PlaneDirection",0,0],1],["WP10_PosX",1,"WP10_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        }
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Purple [Indent level: 4],
                "draw_purple": {
                    "color": [0.67,0.06,0.32],
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Purple|RangesData1_Text [Indent level: 5],
                    "rangesdata1_text": {
                        "type": "text",
                        "source": "static",
                        "text": "348/111 BE1",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.01,0.03],1],
                        "right": [[0.05,0.03],1],
                        "down": [[0.01,0.07],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Yellow [Indent level: 4],
                "draw_yellow": {
                    "color": [0.99,0.86,0.14],
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Yellow|NoTarget [Indent level: 5],
                    "notarget": {
                        "condition": "targetDist<=0",
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Yellow|NoTarget|Target_Text [Indent level: 6],
                        "target_text": {
                            "type": "text",
                            "source": "static",
                            "text": "NO TARGET",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0.18,0.85],1],
                            "right": [[0.22,0.85],1],
                            "down": [[0.18,0.89],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Yellow|TargetInfo [Indent level: 5],
                    "targetinfo": {
                        "condition": "targetDist>=1",
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Yellow|TargetInfo|Dist_Text [Indent level: 6],
                        "dist_text": {
                            "type": "text",
                            "source": "static",
                            "text": "DIST:",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "right",
                            "pos": [[0.02,0.85],1],
                            "right": [[0.06,0.85],1],
                            "down": [[0.02,0.89],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Yellow|TargetInfo|CordX [Indent level: 6],
                        "cordx": {
                            "type": "text",
                            "source": "targetDist",
                            "sourcescale": 0.001,
                            "sourceprecision": 1,
                            "sourcelength": 1,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.15,0.85],1],
                            "right": [[0.19,0.85],1],
                            "down": [[0.15,0.89],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Yellow|TargetInfo|SPD_Text [Indent level: 6],
                        "spd_text": {
                            "type": "text",
                            "source": "static",
                            "text": "SPD:",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "right",
                            "pos": [[0.02,0.89],1],
                            "right": [[0.06,0.89],1],
                            "down": [[0.02,0.93],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Yellow|TargetInfo|SpeedSource [Indent level: 6],
                        "speedsource": {
                            "type": "text",
                            "source": "LarTargetSpeed",
                            "sourcescale": 1,
                            "sourceprecision": 0,
                            "sourcelength": 1,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.15,0.89],1],
                            "right": [[0.19,0.89],1],
                            "down": [[0.15,0.93],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Yellow|TargetInfo|ATL_Text [Indent level: 6],
                        "atl_text": {
                            "type": "text",
                            "source": "static",
                            "text": "ATL:",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "right",
                            "pos": [[0.02,0.93],1],
                            "right": [[0.06,0.93],1],
                            "down": [[0.02,0.97],1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Draw_Yellow|TargetInfo|HeightSource [Indent level: 6],
                        "heightsource": {
                            "type": "text",
                            "source": "targetHeight",
                            "sourcescale": 1,
                            "sourceprecision": 0,
                            "sourcelength": 1,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.15,0.93],1],
                            "right": [[0.19,0.93],1],
                            "down": [[0.15,0.97],1]
                        }
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|Range_Text [Indent level: 4],
                "range_text": {
                    "type": "text",
                    "source": "static",
                    "text": "18",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.74,0.55],1],
                    "right": [[0.79,0.55],1],
                    "down": [[0.74,0.6],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|RadarOn [Indent level: 4],
                "radaron": {
                    "condition": "activeSensorsOn",
                    "color": [1,1,1],
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|RadarOn|Draw_Static [Indent level: 5],
                    "draw_static": {
                        "type": "line",
                        "width": 6,
                        "points": [[[0.5,0.83],1],[[0.681865,0.721992],1],["Static_Offset2",[0.172022,-0.123901],1],["Static_Offset2",[0.160869,-0.138852],1],["Static_Offset2",[0.148492,-0.152746],1],["Static_Offset2",[0.134985,-0.165478],1],["Static_Offset2",[0.120451,-0.17695],1],[[0.605,0.642925],1],[[0.815,0.268775],1],["Static_Offset2",[0.26625,-0.58733],1],["Static_Offset2",[0.215473,-0.608965],1],["Static_Offset2",[0.163056,-0.625965],1],["Static_Offset2",[0.109398,-0.638202],1],["Static_Offset2",[0.0549081,-0.645581],1],["Static_Offset2",[0,-0.648047],1],["Static_Offset2",[-0.0549081,-0.645581],1],["Static_Offset2",[-0.109398,-0.638202],1],["Static_Offset2",[-0.163056,-0.625965],1],["Static_Offset2",[-0.215473,-0.608965],1],["Static_Offset2",[-0.26625,-0.58733],1],["Static_Offset2",[-0.315,-0.561225],1],[[0.395,0.642925],1],[[0.185,0.268775],1],[],["Static_Offset2",[-0.105,-0.187075],1],["Static_Offset2",[-0.120451,-0.17695],1],["Static_Offset2",[-0.134985,-0.165478],1],["Static_Offset2",[-0.148492,-0.152746],1],["Static_Offset2",[-0.160869,-0.138852],1],["Static_Offset2",[-0.172022,-0.123901],1],["Static_Offset2",[-0.181865,-0.108008],1],[],[[0.5,0.83],1],[[0.318135,0.721992],1],[]]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup [Indent level: 4],
                "sensorgroup": {
                    "color": [1,1,1],
                    "alpha": 1,
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor [Indent level: 5],
                    "sensor": {
                        "type": "sensor",
                        "pos": ["Sensor_Offset",["0+-0.17","0+-0.17"],1],
                        "down": ["Sensor_Offset",["1--0.17","1--0.17"],1],
                        "showtargettypes": "2+4+8+16+32+64+128+256+512+1024",
                        "width": 4,
                        "sensorlinetype": 0,
                        "sensorlinewidth": 3,
                        "targetlinewidth": -0.00192,
                        "targetlinelength": 0.02,
                        "range": 36000,
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|MissileThreat [Indent level: 6],
                        "missilethreat": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|MissileThreat|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0205729],1],[[0.003472,-0.0202602],1],[[0.00684,-0.0193324],1],[[0.01,-0.0178161],1],[[0.012856,-0.0157589],1],[[0.01532,-0.0132243],1],[[0.01732,-0.0102865],1],[[0.018794,-0.00703594],1],[[0.019696,-0.00357146],1],[[0.02,0],1],[[0.019696,0.00357146],1],[[0.018794,0.00703594],1],[[0.01732,0.0102865],1],[[0.01532,0.0132243],1],[[0.012856,0.0157589],1],[[0.01,0.0178161],1],[[0.00684,0.0193324],1],[[0.003472,0.0202602],1],[[0,0.0205729],1],[[-0.003472,0.0202602],1],[[-0.00684,0.0193324],1],[[-0.01,0.0178161],1],[[-0.012856,0.0157589],1],[[-0.01532,0.0132243],1],[[-0.01732,0.0102865],1],[[-0.018794,0.00703594],1],[[-0.019696,0.00357146],1],[[-0.02,0],1],[[-0.019696,-0.00357146],1],[[-0.018794,-0.00703594],1],[[-0.01732,-0.0102865],1],[[-0.01532,-0.0132243],1],[[-0.012856,-0.0157589],1],[[-0.01,-0.0178161],1],[[-0.00684,-0.0193324],1],[[-0.003472,-0.0202602],1],[[0,-0.0205729],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|MissileThreat|TextM [Indent level: 7],
                            "textm": {
                                "type": "text",
                                "source": "static",
                                "text": "M",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.01],1],
                                "right": [[0.02,-0.01],1],
                                "down": [[0,0.01],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|lockingThreat [Indent level: 6],
                        "lockingthreat": {
                            "color": [1,0.3,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|lockingThreat|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|markingThreat [Indent level: 6],
                        "markingthreat": {
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|markingThreat|TargetLines [Indent level: 7]
                            "targetlines": {
                                "type": "line",
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            },
                            "color": [1,0.3,0]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|rwr [Indent level: 6],
                        "rwr": {
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|rwr|TargetLines [Indent level: 7]
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|rwrFriendly [Indent level: 6],
                        "rwrfriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|rwrFriendly|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|rwrEnemy [Indent level: 6],
                        "rwrenemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|rwrEnemy|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|rwrGroup [Indent level: 6],
                        "rwrgroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|rwrGroup|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|rwrDestroyed [Indent level: 6],
                        "rwrdestroyed": {
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|markedTarget [Indent level: 6],
                        "markedtarget": {
                            "color": [1,0.3,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|markedTarget|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 3,
                                "points": [[[-0.017,-0.017487],1],[[-0.01,-0.017487],1],[],[[0.017,-0.017487],1],[[0.01,-0.017487],1],[],[[-0.017,-0.017487],1],[[-0.017,-0.0102865],1],[],[[0.017,-0.017487],1],[[0.017,-0.0102865],1],[],[[-0.017,0.017487],1],[[-0.01,0.017487],1],[],[[0.017,0.017487],1],[[0.01,0.017487],1],[],[[-0.017,0.017487],1],[[-0.017,0.0102865],1],[],[[0.017,0.017487],1],[[0.017,0.0102865],1],[]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|assignedTarget [Indent level: 6],
                        "assignedtarget": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|assignedTarget|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 3,
                                "points": [[[-0.017,-0.017487],1],[[-0.01,-0.017487],1],[],[[0.017,-0.017487],1],[[0.01,-0.017487],1],[],[[-0.017,-0.017487],1],[[-0.017,-0.0102865],1],[],[[0.017,-0.017487],1],[[0.017,-0.0102865],1],[],[[-0.017,0.017487],1],[[-0.01,0.017487],1],[],[[0.017,0.017487],1],[[0.01,0.017487],1],[],[[-0.017,0.017487],1],[[-0.017,0.0102865],1],[],[[0.017,0.017487],1],[[0.017,0.0102865],1],[]]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|target [Indent level: 6],
                        "target": {
                            "color": [1,1,1],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|target|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|target|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetFriendly [Indent level: 6],
                        "targetfriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetFriendly|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetFriendly|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "G",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetEnemy [Indent level: 6],
                        "targetenemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetEnemy|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetEnemy|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroup [Indent level: 6],
                        "targetgroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroup|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroup|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetDestroyed [Indent level: 6],
                        "targetdestroyed": {
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGround [Indent level: 6],
                        "targetground": {
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGround|TargetLines [Indent level: 7]
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGround|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            },
                            "color": [1,1,1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundFriendly [Indent level: 6],
                        "targetgroundfriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundFriendly|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundFriendly|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundEnemy [Indent level: 6],
                        "targetgroundenemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundEnemy|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundEnemy|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundGroup [Indent level: 6],
                        "targetgroundgroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundGroup|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundGroup|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundDestroyed [Indent level: 6],
                        "targetgrounddestroyed": {
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemote [Indent level: 6],
                        "targetgroundremote": {
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemote|TargetLines [Indent level: 7]
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemote|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "G",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            },
                            "color": [1,1,1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemoteFriendly [Indent level: 6],
                        "targetgroundremotefriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemoteFriendly|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemoteFriendly|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "G",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemoteEnemy [Indent level: 6],
                        "targetgroundremoteenemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemoteEnemy|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemoteEnemy|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "G",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemoteGroup [Indent level: 6],
                        "targetgroundremotegroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemoteGroup|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemoteGroup|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "G",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetGroundRemoteDestroyed [Indent level: 6],
                        "targetgroundremotedestroyed": {
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaser [Indent level: 6],
                        "targetlaser": {
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaser|TargetLines [Indent level: 7]
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaser|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            },
                            "color": [1,1,1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaserFriendly [Indent level: 6],
                        "targetlaserfriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaserFriendly|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaserFriendly|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaserEnemy [Indent level: 6],
                        "targetlaserenemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaserEnemy|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaserEnemy|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaserGroup [Indent level: 6],
                        "targetlasergroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaserGroup|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetLaserGroup|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVG [Indent level: 6],
                        "targetnvg": {
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVG|TargetLines [Indent level: 7]
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVG|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            },
                            "color": [1,1,1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVGFriendly [Indent level: 6],
                        "targetnvgfriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVGFriendly|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVGFriendly|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVGEnemy [Indent level: 6],
                        "targetnvgenemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVGEnemy|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVGEnemy|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVGGroup [Indent level: 6],
                        "targetnvggroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVGGroup|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetNVGGroup|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetMan [Indent level: 6],
                        "targetman": {
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetMan|TargetLines [Indent level: 7]
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetMan|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            },
                            "color": [1,1,1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManFriendly [Indent level: 6],
                        "targetmanfriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManFriendly|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManFriendly|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManEnemy [Indent level: 6],
                        "targetmanenemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManEnemy|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManEnemy|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManGroup [Indent level: 6],
                        "targetmangroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManGroup|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManGroup|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemote [Indent level: 6],
                        "targetmanremote": {
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemote|TargetLines [Indent level: 7]
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemote|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            },
                            "color": [1,1,1]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemoteFriendly [Indent level: 6],
                        "targetmanremotefriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemoteFriendly|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemoteFriendly|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemoteEnemy [Indent level: 6],
                        "targetmanremoteenemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemoteEnemy|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemoteEnemy|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemoteGroup [Indent level: 6],
                        "targetmanremotegroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemoteGroup|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetManRemoteGroup|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "U",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAir [Indent level: 6],
                        "targetair": {
                            "color": [1,1,1],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAir|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAir|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "A",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirFriendly [Indent level: 6],
                        "targetairfriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirFriendly|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirFriendly|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "A",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirEnemy [Indent level: 6],
                        "targetairenemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirEnemy|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirEnemy|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "A",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirGroup [Indent level: 6],
                        "targetairgroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirGroup|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirGroup|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "A",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirDestroyed [Indent level: 6],
                        "targetairdestroyed": {
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemote [Indent level: 6],
                        "targetairremote": {
                            "color": [1,1,1],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemote|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemote|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "R",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemoteFriendly [Indent level: 6],
                        "targetairremotefriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemoteFriendly|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemoteFriendly|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "R",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemoteEnemy [Indent level: 6],
                        "targetairremoteenemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemoteEnemy|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemoteEnemy|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "R",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemoteGroup [Indent level: 6],
                        "targetairremotegroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemoteGroup|TargetLines [Indent level: 7],
                            "targetlines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemoteGroup|TextA [Indent level: 7],
                            "texta": {
                                "type": "text",
                                "source": "static",
                                "text": "R",
                                "align": "center",
                                "scale": 1,
                                "pos": [[0,-0.009],1],
                                "right": [[0.02,-0.009],1],
                                "down": [[0,0.011],1]
                            }
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_4|Draw|SensorGroup|Sensor|targetAirRemoteDestroyed [Indent level: 6],
                        "targetairremotedestroyed": {
                        }
                    }
                }
            }
        },
        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5 [Indent level: 2],
        "mfd_5": {
            "topleft": "MFD_5_TL",
            "topright": "MFD_5_TR",
            "bottomleft": "MFD_5_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|material [Indent level: 3],
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Sensor_Offset [Indent level: 4]
                "sensor_offset": {
                    "type": "fixed",
                    "pos": [0,0.03]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Static_Offset [Indent level: 4],
                "static_offset": {
                    "type": "fixed",
                    "pos": [0.5,0.53]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_0 [Indent level: 4],
                "rotation_0": {
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "minangle": 0,
                    "maxangle": -360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_30 [Indent level: 4],
                "rotation_30": {
                    "minangle": 30,
                    "maxangle": -330,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_60 [Indent level: 4],
                "rotation_60": {
                    "minangle": 60,
                    "maxangle": -300,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_90 [Indent level: 4],
                "rotation_90": {
                    "minangle": 90,
                    "maxangle": -270,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_120 [Indent level: 4],
                "rotation_120": {
                    "minangle": 120,
                    "maxangle": -240,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_150 [Indent level: 4],
                "rotation_150": {
                    "minangle": 150,
                    "maxangle": -210,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_180 [Indent level: 4],
                "rotation_180": {
                    "minangle": 180,
                    "maxangle": -180,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_210 [Indent level: 4],
                "rotation_210": {
                    "minangle": 210,
                    "maxangle": -150,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_240 [Indent level: 4],
                "rotation_240": {
                    "minangle": 240,
                    "maxangle": -120,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_270 [Indent level: 4],
                "rotation_270": {
                    "minangle": 270,
                    "maxangle": -90,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_300 [Indent level: 4],
                "rotation_300": {
                    "minangle": 300,
                    "maxangle": -60,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_330 [Indent level: 4],
                "rotation_330": {
                    "minangle": 330,
                    "maxangle": -30,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_Inv_0 [Indent level: 4],
                "rotation_inv_0": {
                    "min": 0,
                    "max": 360,
                    "minangle": 180,
                    "maxangle": -180,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_Inv_90 [Indent level: 4],
                "rotation_inv_90": {
                    "minangle": 270,
                    "maxangle": -90,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_Inv_180 [Indent level: 4],
                "rotation_inv_180": {
                    "minangle": 360,
                    "maxangle": 0,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1.08148
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Bones|Rotation_Inv_270 [Indent level: 4],
                "rotation_inv_270": {
                    "minangle": 450,
                    "maxangle": 90,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectratio": 1.08148
                }
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw [Indent level: 3],
            "draw": {
                "condition": "on",
                "alpha": 0.5,
                "color": [1,1,1],
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|Draw_Blue [Indent level: 4],
                "draw_blue": {
                    "color": [0,0.03,0.17],
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|Draw_Blue|Draw_Static [Indent level: 5],
                    "draw_static": {
                        "type": "line",
                        "width": 10,
                        "points": [["Static_Offset",[0,-0.410963],1],["Static_Offset",[0.065968,-0.404716],1],["Static_Offset",[0.12996,-0.386182],1],["Static_Offset",[0.19,-0.355894],1],["Static_Offset",[0.244264,-0.314798],1],["Static_Offset",[0.29108,-0.264167],1],["Static_Offset",[0.32908,-0.205481],1],["Static_Offset",[0.357086,-0.140549],1],["Static_Offset",[0.374224,-0.0713432],1],["Static_Offset",[0.38,0],1],["Static_Offset",[0.374224,0.0713432],1],["Static_Offset",[0.357086,0.140549],1],["Static_Offset",[0.32908,0.205481],1],["Static_Offset",[0.29108,0.264167],1],["Static_Offset",[0.244264,0.314798],1],["Static_Offset",[0.19,0.355894],1],["Static_Offset",[0.12996,0.386182],1],["Static_Offset",[0.065968,0.404716],1],["Static_Offset",[0,0.410963],1],["Static_Offset",[-0.065968,0.404716],1],["Static_Offset",[-0.12996,0.386182],1],["Static_Offset",[-0.19,0.355894],1],["Static_Offset",[-0.244264,0.314798],1],["Static_Offset",[-0.29108,0.264167],1],["Static_Offset",[-0.32908,0.205481],1],["Static_Offset",[-0.357086,0.140549],1],["Static_Offset",[-0.374224,0.0713432],1],["Static_Offset",[-0.38,0],1],["Static_Offset",[-0.374224,-0.0713432],1],["Static_Offset",[-0.357086,-0.140549],1],["Static_Offset",[-0.32908,-0.205481],1],["Static_Offset",[-0.29108,-0.264167],1],["Static_Offset",[-0.244264,-0.314798],1],["Static_Offset",[-0.19,-0.355894],1],["Static_Offset",[-0.12996,-0.386182],1],["Static_Offset",[-0.065968,-0.404716],1],["Static_Offset",[0,-0.410963],1],[],["Static_Offset",[0,-0.173037],1],["Static_Offset",[0.027776,-0.170407],1],["Static_Offset",[0.05472,-0.162603],1],["Static_Offset",[0.08,-0.14985],1],["Static_Offset",[0.102848,-0.132546],1],["Static_Offset",[0.12256,-0.111228],1],["Static_Offset",[0.13856,-0.0865185],1],["Static_Offset",[0.150352,-0.0591787],1],["Static_Offset",[0.157568,-0.0300392],1],["Static_Offset",[0.16,0],1],["Static_Offset",[0.157568,0.0300392],1],["Static_Offset",[0.150352,0.0591787],1],["Static_Offset",[0.13856,0.0865185],1],["Static_Offset",[0.12256,0.111228],1],["Static_Offset",[0.102848,0.132546],1],["Static_Offset",[0.08,0.14985],1],["Static_Offset",[0.05472,0.162603],1],["Static_Offset",[0.027776,0.170407],1],["Static_Offset",[0,0.173037],1],["Static_Offset",[-0.027776,0.170407],1],["Static_Offset",[-0.05472,0.162603],1],["Static_Offset",[-0.08,0.14985],1],["Static_Offset",[-0.102848,0.132546],1],["Static_Offset",[-0.12256,0.111228],1],["Static_Offset",[-0.13856,0.0865185],1],["Static_Offset",[-0.150352,0.0591787],1],["Static_Offset",[-0.157568,0.0300392],1],["Static_Offset",[-0.16,0],1],["Static_Offset",[-0.157568,-0.0300392],1],["Static_Offset",[-0.150352,-0.0591787],1],["Static_Offset",[-0.13856,-0.0865185],1],["Static_Offset",[-0.12256,-0.111228],1],["Static_Offset",[-0.102848,-0.132546],1],["Static_Offset",[-0.08,-0.14985],1],["Static_Offset",[-0.05472,-0.162603],1],["Static_Offset",[-0.027776,-0.170407],1],["Static_Offset",[0,-0.173037],1],[],["Static_Offset",[0,-0.41],1],["Static_Offset",[0,-0.44],1],["Static_Offset",[0.07,-0.44],1],["Static_Offset",[0.07,-0.51],1],["Static_Offset",[-0.07,-0.51],1],["Static_Offset",[-0.07,-0.44],1],["Static_Offset",[0,-0.44],1],[],["Static_Offset",1,["Rotation_0",0,0.383926],1],["Static_Offset",1,["Rotation_0",0,0.340667],1],[],["Static_Offset",1,["Rotation_30",0,0.383926],1],["Static_Offset",1,["Rotation_30",0,0.340667],1],[],["Static_Offset",1,["Rotation_60",0,0.383926],1],["Static_Offset",1,["Rotation_60",0,0.340667],1],[],["Static_Offset",1,["Rotation_90",0,0.383926],1],["Static_Offset",1,["Rotation_90",0,0.340667],1],[],["Static_Offset",1,["Rotation_120",0,0.383926],1],["Static_Offset",1,["Rotation_120",0,0.340667],1],[],["Static_Offset",1,["Rotation_150",0,0.383926],1],["Static_Offset",1,["Rotation_150",0,0.340667],1],[],["Static_Offset",1,["Rotation_180",0,0.383926],1],["Static_Offset",1,["Rotation_180",0,0.340667],1],[],["Static_Offset",1,["Rotation_210",0,0.383926],1],["Static_Offset",1,["Rotation_210",0,0.340667],1],[],["Static_Offset",1,["Rotation_240",0,0.383926],1],["Static_Offset",1,["Rotation_240",0,0.340667],1],[],["Static_Offset",1,["Rotation_270",0,0.383926],1],["Static_Offset",1,["Rotation_270",0,0.340667],1],[],["Static_Offset",1,["Rotation_300",0,0.383926],1],["Static_Offset",1,["Rotation_300",0,0.340667],1],[],["Static_Offset",1,["Rotation_330",0,0.383926],1],["Static_Offset",1,["Rotation_330",0,0.340667],1],[],[]]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|Draw_Blue|Rotation_0_Text [Indent level: 5],
                    "rotation_0_text": {
                        "type": "text",
                        "source": "static",
                        "text": "N",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": ["Static_Offset",1,["Rotation_Inv_0",0,-0.345],1],
                        "right": ["Static_Offset",1,["Rotation_Inv_0",-0.04,-0.345],1],
                        "down": ["Static_Offset",1,["Rotation_Inv_0",0,-0.295],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|Draw_Blue|Rotation_90_Text [Indent level: 5],
                    "rotation_90_text": {
                        "type": "text",
                        "source": "static",
                        "text": "E",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": ["Static_Offset",1,["Rotation_Inv_90",0,-0.345],1],
                        "right": ["Static_Offset",1,["Rotation_Inv_90",-0.04,-0.345],1],
                        "down": ["Static_Offset",1,["Rotation_Inv_90",0,-0.295],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|Draw_Blue|Rotation_180_Text [Indent level: 5],
                    "rotation_180_text": {
                        "type": "text",
                        "source": "static",
                        "text": "S",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": ["Static_Offset",1,["Rotation_Inv_180",0,-0.345],1],
                        "right": ["Static_Offset",1,["Rotation_Inv_180",-0.04,-0.345],1],
                        "down": ["Static_Offset",1,["Rotation_Inv_180",0,-0.295],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|Draw_Blue|Rotation_270_Text [Indent level: 5],
                    "rotation_270_text": {
                        "type": "text",
                        "source": "static",
                        "text": "W",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": ["Static_Offset",1,["Rotation_Inv_270",0,-0.345],1],
                        "right": ["Static_Offset",1,["Rotation_Inv_270",-0.04,-0.345],1],
                        "down": ["Static_Offset",1,["Rotation_Inv_270",0,-0.295],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|BackgroundBlack [Indent level: 4],
                "backgroundblack": {
                    "color": [0,0,0],
                    "alpha": 1,
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|BackgroundBlack|Static [Indent level: 5],
                    "static": {
                        "type": "polygon",
                        "points": [[[[0.6,0.4],1],[[0.67,0.4],1],[[0.67,0.45],1],[[0.6,0.45],1]],[[[0.68,0.21],1],[[0.81,0.21],1],[[0.81,0.29],1],[[0.68,0.29],1]]]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|HeadingText [Indent level: 4],
                "headingtext": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "refreshrate": 0.1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.5,0.03],1],
                    "right": [[0.56,0.03],1],
                    "down": [[0.5,0.09],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|Range_Text [Indent level: 4],
                "range_text": {
                    "type": "text",
                    "source": "static",
                    "text": "18A",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.81,0.22],1],
                    "right": [[0.88,0.22],1],
                    "down": [[0.81,0.29],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|MFD1_Text [Indent level: 4],
                "mfd1_text": {
                    "type": "text",
                    "source": "static",
                    "text": "LPE4",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.86,0.03],1],
                    "right": [[0.91,0.03],1],
                    "down": [[0.86,0.08],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|Draw_Blue2 [Indent level: 4],
                "draw_blue2": {
                    "color": [0,0.03,0.17],
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|Draw_Blue2|Range_Text [Indent level: 5],
                    "range_text": {
                        "type": "text",
                        "source": "static",
                        "text": "9",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [[0.64,0.4],1],
                        "right": [[0.69,0.4],1],
                        "down": [[0.64,0.45],1]
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR [Indent level: 4],
                "rwr": {
                    "type": "sensor",
                    "pos": ["Sensor_Offset",["0+-0.32","0+-0.32"],1],
                    "down": ["Sensor_Offset",["1--0.32","1--0.32"],1],
                    "showtargettypes": "2 + 4 + 8 + 32 + 64 + 128 + 256",
                    "width": 4,
                    "sensorlinetype": 1,
                    "sensorlinewidth": 3,
                    "targetlinewidth": -0.0016,
                    "targetlinelength": 0.02,
                    "range": 36000,
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|MissileThreat [Indent level: 5],
                    "missilethreat": {
                        "color": [1,0,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|MissileThreat|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0216296],1],[[0.003472,-0.0213009],1],[[0.00684,-0.0203254],1],[[0.01,-0.0187313],1],[[0.012856,-0.0165683],1],[[0.01532,-0.0139035],1],[[0.01732,-0.0108148],1],[[0.018794,-0.00739733],1],[[0.019696,-0.0037549],1],[[0.02,0],1],[[0.019696,0.0037549],1],[[0.018794,0.00739733],1],[[0.01732,0.0108148],1],[[0.01532,0.0139035],1],[[0.012856,0.0165683],1],[[0.01,0.0187313],1],[[0.00684,0.0203254],1],[[0.003472,0.0213009],1],[[0,0.0216296],1],[[-0.003472,0.0213009],1],[[-0.00684,0.0203254],1],[[-0.01,0.0187313],1],[[-0.012856,0.0165683],1],[[-0.01532,0.0139035],1],[[-0.01732,0.0108148],1],[[-0.018794,0.00739733],1],[[-0.019696,0.0037549],1],[[-0.02,0],1],[[-0.019696,-0.0037549],1],[[-0.018794,-0.00739733],1],[[-0.01732,-0.0108148],1],[[-0.01532,-0.0139035],1],[[-0.012856,-0.0165683],1],[[-0.01,-0.0187313],1],[[-0.00684,-0.0203254],1],[[-0.003472,-0.0213009],1],[[0,-0.0216296],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|MissileThreat|TextM [Indent level: 6],
                        "textm": {
                            "type": "text",
                            "source": "static",
                            "text": "M",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.01],1],
                            "right": [[0.02,-0.01],1],
                            "down": [[0,0.01],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|lockingThreat [Indent level: 5],
                    "lockingthreat": {
                        "color": [1,0.3,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|lockingThreat|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|rwr [Indent level: 5],
                    "rwr": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|rwr|TargetLines [Indent level: 6]
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|rwr|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "A",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.01],1],
                            "right": [[0.02,-0.01],1],
                            "down": [[0,0.01],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|rwrFriendly [Indent level: 5],
                    "rwrfriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|rwrFriendly|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|rwrFriendly|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "A",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.01],1],
                            "right": [[0.02,-0.01],1],
                            "down": [[0,0.01],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|rwrEnemy [Indent level: 5],
                    "rwrenemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|rwrEnemy|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|rwrEnemy|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "A",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.01],1],
                            "right": [[0.02,-0.01],1],
                            "down": [[0,0.01],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|markedTarget [Indent level: 5],
                    "markedtarget": {
                        "color": [1,0.3,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|markedTarget|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 3,
                            "points": [[[-0.017,-0.0183852],1],[[-0.01,-0.0183852],1],[],[[0.017,-0.0183852],1],[[0.01,-0.0183852],1],[],[[-0.017,-0.0183852],1],[[-0.017,-0.0108148],1],[],[[0.017,-0.0183852],1],[[0.017,-0.0108148],1],[],[[-0.017,0.0183852],1],[[-0.01,0.0183852],1],[],[[0.017,0.0183852],1],[[0.01,0.0183852],1],[],[[-0.017,0.0183852],1],[[-0.017,0.0108148],1],[],[[0.017,0.0183852],1],[[0.017,0.0108148],1],[]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|assignedTarget [Indent level: 5],
                    "assignedtarget": {
                        "color": [1,0.3,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|assignedTarget|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 7,
                            "points": [[[0,-0.0194667],1],[[0.0031248,-0.0191708],1],[[0.006156,-0.0182928],1],[[0.009,-0.0168581],1],[[0.0115704,-0.0149115],1],[[0.013788,-0.0125132],1],[[0.015588,-0.00973333],1],[[0.0169146,-0.0066576],1],[[0.0177264,-0.00337941],1],[[0.018,0],1],[[0.0177264,0.00337941],1],[[0.0169146,0.0066576],1],[[0.015588,0.00973333],1],[[0.013788,0.0125132],1],[[0.0115704,0.0149115],1],[[0.009,0.0168581],1],[[0.006156,0.0182928],1],[[0.0031248,0.0191708],1],[[0,0.0194667],1],[[-0.0031248,0.0191708],1],[[-0.006156,0.0182928],1],[[-0.009,0.0168581],1],[[-0.0115704,0.0149115],1],[[-0.013788,0.0125132],1],[[-0.015588,0.00973333],1],[[-0.0169146,0.0066576],1],[[-0.0177264,0.00337941],1],[[-0.018,0],1],[[-0.0177264,-0.00337941],1],[[-0.0169146,-0.0066576],1],[[-0.015588,-0.00973333],1],[[-0.013788,-0.0125132],1],[[-0.0115704,-0.0149115],1],[[-0.009,-0.0168581],1],[[-0.006156,-0.0182928],1],[[-0.0031248,-0.0191708],1],[[0,-0.0194667],1]]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|target [Indent level: 5],
                    "target": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|target|TargetLines [Indent level: 6]
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|target|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "T",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.008],1],
                            "right": [[0.02,-0.008],1],
                            "down": [[0,0.012],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetFriendly [Indent level: 5],
                    "targetfriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetFriendly|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetFriendly|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "T",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.008],1],
                            "right": [[0.02,-0.008],1],
                            "down": [[0,0.012],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetEnemy [Indent level: 5],
                    "targetenemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetEnemy|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetEnemy|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "T",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.008],1],
                            "right": [[0.02,-0.008],1],
                            "down": [[0,0.012],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGround [Indent level: 5],
                    "targetground": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGround|TargetLines [Indent level: 6]
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGround|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "G",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundFriendly [Indent level: 5],
                    "targetgroundfriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundFriendly|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundFriendly|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "G",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundEnemy [Indent level: 5],
                    "targetgroundenemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundEnemy|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundEnemy|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "G",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundRemote [Indent level: 5],
                    "targetgroundremote": {
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundRemote|TargetLines [Indent level: 6]
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundRemote|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "G",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundRemoteFriendly [Indent level: 5],
                    "targetgroundremotefriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundRemoteFriendly|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundRemoteFriendly|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "G",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundRemoteEnemy [Indent level: 5],
                    "targetgroundremoteenemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundRemoteEnemy|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetGroundRemoteEnemy|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "G",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAir [Indent level: 5],
                    "targetair": {
                        "color": [1,1,1],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAir|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAir|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "A",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirFriendly [Indent level: 5],
                    "targetairfriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirFriendly|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirFriendly|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "A",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirEnemy [Indent level: 5],
                    "targetairenemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirEnemy|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirEnemy|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "A",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirRemote [Indent level: 5],
                    "targetairremote": {
                        "color": [1,1,1],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirRemote|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirRemote|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "R",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirRemoteFriendly [Indent level: 5],
                    "targetairremotefriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirRemoteFriendly|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirRemoteFriendly|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "R",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirRemoteEnemy [Indent level: 5],
                    "targetairremoteenemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirRemoteEnemy|TargetLines [Indent level: 6],
                        "targetlines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|RWR|targetAirRemoteEnemy|TextA [Indent level: 6],
                        "texta": {
                            "type": "text",
                            "source": "static",
                            "text": "R",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.009],1],
                            "right": [[0.02,-0.009],1],
                            "down": [[0,0.011],1]
                        }
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|MChaff_Text [Indent level: 4],
                "mchaff_text": {
                    "type": "text",
                    "source": "static",
                    "text": "M CHAFF",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.77,0.85],1],
                    "right": [[0.8,0.85],1],
                    "down": [[0.77,0.89],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|MFlare_Text [Indent level: 4],
                "mflare_text": {
                    "type": "text",
                    "source": "static",
                    "text": "M FLARE",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.77,0.89],1],
                    "right": [[0.8,0.89],1],
                    "down": [[0.77,0.93],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|Prog_Text [Indent level: 4],
                "prog_text": {
                    "type": "text",
                    "source": "static",
                    "text": "1 PROG",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.77,0.93],1],
                    "right": [[0.8,0.93],1],
                    "down": [[0.77,0.97],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|ChaffSource [Indent level: 4],
                "chaffsource": {
                    "type": "text",
                    "source": "cmammo",
                    "sourcescale": 1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.93,0.85],1],
                    "right": [[0.96,0.85],1],
                    "down": [[0.93,0.89],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|FlareSource [Indent level: 4],
                "flaresource": {
                    "pos": [[0.93,0.89],1],
                    "right": [[0.96,0.89],1],
                    "down": [[0.93,0.93],1],
                    "type": "text",
                    "source": "cmammo",
                    "sourcescale": 1,
                    "align": "right",
                    "scale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_5|Draw|ProgS_Text [Indent level: 4],
                "progs_text": {
                    "type": "text",
                    "source": "static",
                    "text": "10",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.93,0.93],1],
                    "right": [[0.96,0.93],1],
                    "down": [[0.93,0.97],1]
                }
            }
        },
        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6 [Indent level: 2],
        "mfd_6": {
            "topleft": "MFD_6_TL",
            "topright": "MFD_6_TR",
            "bottomleft": "MFD_6_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|material [Indent level: 3],
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw [Indent level: 3],
            "draw": {
                "condition": "on",
                "color": [0.15,1,0.15],
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|CurrentWeapon [Indent level: 4],
                "currentweapon": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourcescale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.51,0.24],1],
                    "right": [[0.57,0.24],1],
                    "down": [[0.51,0.3],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|MGAmmo [Indent level: 4],
                "mgammo": {
                    "type": "text",
                    "source": "ammo",
                    "sourceindex": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.51,0.415],1],
                    "right": [[0.54,0.415],1],
                    "down": [[0.51,0.455],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|MGAmmo_Text [Indent level: 4],
                "mgammo_text": {
                    "type": "text",
                    "source": "static",
                    "text": "GUN-",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.43,0.415],1],
                    "right": [[0.46,0.415],1],
                    "down": [[0.43,0.455],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|thrust1Source [Indent level: 4],
                "thrust1source": {
                    "type": "text",
                    "source": "throttle",
                    "sourcescale": 100,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.3,0.08],1],
                    "right": [[0.34,0.08],1],
                    "down": [[0.3,0.12],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|thrust2Source [Indent level: 4],
                "thrust2source": {
                    "pos": [[0.61,0.08],1],
                    "right": [[0.65,0.08],1],
                    "down": [[0.61,0.12],1],
                    "type": "text",
                    "source": "throttle",
                    "sourcescale": 100,
                    "align": "center",
                    "scale": 1
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|White [Indent level: 4],
                "white": {
                    "color": [1,1,15],
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|White|ChaffSource [Indent level: 5],
                    "chaffsource": {
                        "type": "text",
                        "source": "cmammo",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.26,0.78],1],
                        "right": [[0.29,0.78],1],
                        "down": [[0.26,0.82],1]
                    },
                    # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|White|FlareSource [Indent level: 5],
                    "flaresource": {
                        "pos": [[0.68,0.78],1],
                        "right": [[0.71,0.78],1],
                        "down": [[0.68,0.82],1],
                        "type": "text",
                        "source": "cmammo",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1
                    }
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|Pylon1 [Indent level: 4],
                "pylon1": {
                    "type": "pylonicon",
                    "pos": [[0.35,0.48],1],
                    "pylon": 1,
                    "name": "rhs_f22_pylon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|Pylon2 [Indent level: 4],
                "pylon2": {
                    "pos": [[0.37,0.58],1],
                    "pylon": 2,
                    "type": "pylonicon",
                    "name": "rhs_f22_pylon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|Pylon3 [Indent level: 4],
                "pylon3": {
                    "pos": [[0.445,0.58],1],
                    "pylon": 3,
                    "type": "pylonicon",
                    "name": "rhs_f22_pylon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|Pylon4 [Indent level: 4],
                "pylon4": {
                    "pos": [[0.555,0.58],1],
                    "pylon": 4,
                    "type": "pylonicon",
                    "name": "rhs_f22_pylon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|Pylon5 [Indent level: 4],
                "pylon5": {
                    "pos": [[0.63,0.58],1],
                    "pylon": 5,
                    "type": "pylonicon",
                    "name": "rhs_f22_pylon"
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_6|Draw|Pylon6 [Indent level: 4],
                "pylon6": {
                    "pos": [[0.65,0.48],1],
                    "pylon": 6,
                    "type": "pylonicon",
                    "name": "rhs_f22_pylon"
                }
            }
        },
        # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7 [Indent level: 2],
        "mfd_7": {
            "topleft": "MFD_7_TL",
            "topright": "MFD_7_TR",
            "bottomleft": "MFD_7_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0.03,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "rhsusf_digital_font_var",
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|material [Indent level: 3],
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|Draw [Indent level: 3],
            "draw": {
                "condition": "on",
                "color": [0.15,1,0.15],
                "alpha": 0.5,
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|Draw|C1_Text [Indent level: 4],
                "c1_text": {
                    "type": "text",
                    "source": "static",
                    "text": "C1: ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.06,0.24],1],
                    "right": [[0.12,0.24],1],
                    "down": [[0.06,0.31],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|Draw|C1_Value [Indent level: 4],
                "c1_value": {
                    "type": "text",
                    "source": "userText",
                    "sourcescale": 1,
                    "sourceindex": 0,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.16,0.24],1],
                    "right": [[0.22,0.24],1],
                    "down": [[0.16,0.31],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|Draw|COM1_Text1 [Indent level: 4],
                "com1_text1": {
                    "type": "text",
                    "source": "static",
                    "text": "COM1",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.51,0.26],1],
                    "right": [[0.57,0.26],1],
                    "down": [[0.51,0.33],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|Draw|COM1_Text2 [Indent level: 4],
                "com1_text2": {
                    "type": "text",
                    "source": "static",
                    "text": "1/1",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.81,0.26],1],
                    "right": [[0.87,0.26],1],
                    "down": [[0.81,0.33],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|Draw|Vol_Text [Indent level: 4],
                "vol_text": {
                    "type": "text",
                    "source": "static",
                    "text": "C1 VOL 100%",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.51,0.405],1],
                    "right": [[0.57,0.405],1],
                    "down": [[0.51,0.475],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|Draw|VolAdj_Text [Indent level: 4],
                "voladj_text": {
                    "type": "text",
                    "source": "static",
                    "text": "> VOL ADJ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.51,0.55],1],
                    "right": [[0.57,0.55],1],
                    "down": [[0.51,0.62],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|Draw|Em_Text [Indent level: 4],
                "em_text": {
                    "type": "text",
                    "source": "static",
                    "text": "  - - - -",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.51,0.705],1],
                    "right": [[0.57,0.705],1],
                    "down": [[0.51,0.775],1]
                },
                # Class: CfgVehicles|rhsusf_f22|MFD|MFD_7|Draw|FreqAdj_Text [Indent level: 4],
                "freqadj_text": {
                    "type": "text",
                    "source": "static",
                    "text": "> FREQ ADJ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.51,0.88],1],
                    "right": [[0.57,0.88],1],
                    "down": [[0.51,0.95],1]
                }
            }
        }
    },
    "airbrake": 1,
    "airbrakefrictioncoef": 2.4,
    "flaps": 1,
    "flapsfrictioncoef": 0.36,
    "gearsupfrictioncoef": 0.8,
    "brakedistance": 250,
    "wheelsteeringsensitivity": 4,
    "maxspeed": 1800,
    "rhs_afterburner_maxspeed": 2000,
    "rhs_afterburner_boost": 0.18,
    "rhs_afterburner_fueldrag": 0.19,
    "altfullforce": 5000,
    "altnoforce": 15000,
    "rudderinfluence": 0.766,
    "nosedowncoef": 0,
    "aileronsensitivity": 1.2,
    "elevatorsensitivity": 1.4,
    "elevatorcontrolssensitivitycoef": 4,
    "aileroncontrolssensitivitycoef": 3.5,
    "ruddercontrolssensitivitycoef": 4,
    "envelope": [0,0.11,0.83,1.97,2.42,2.69,3.87,5.27,6.89,8.72,9.7,9.6,9.2,8.5,8.2,8],
    "thrustcoef": [1.76,1.69,1.62,1.68,1.74,1.81,1.89,1.95,1.96,1.96,1.92,1.4,0.4,0,0,0],
    "elevatorcoef": [0.3,0.5,0.66,0.52,0.49,0.46,0.43,0.4,0.35,0.3,0.25,0.18,0.17,0.16,0.15,0.15],
    "aileroncoef": [0.4,0.5,0.8,0.95,1.02,1.04,1.03,1.01,1,0.7,0.6,0.55,0.5,0.45,0.4,0.35],
    "ruddercoef": [0.5,1.8,2.6,2.75,2.8,2.85,2.9,2.95,2.98,3.01,2.7,1.1,0.9,0.7,0.5,0.3],
    "angleofindicence": 0.04,
    "draconicforcexcoef": 8,
    "draconicforceycoef": 1.2,
    "draconicforcezcoef": 1,
    "draconictorquexcoef": [4,5.1,6.1,7,7.7,8.3,9,9.1,9.2,9.2,9.2],
    "draconictorqueycoef": [6.8,5.5,4,1.5,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "airfrictioncoefs0": [0,0,0],
    "airfrictioncoefs1": [0.1,0.5,0.0075],
    "airfrictioncoefs2": [0.001,0.005,6.7e-005],
    "landingspeed": 275,
    "stallspeed": 250,
    "stallwarningtreshold": 0.5,
    "acceleration": 200,
    "landingaoa": 0.108207,
    "maxomega": 4000,
    "enginemoi": 9,
    # Class: CfgVehicles|rhsusf_f22|Wheels [Indent level: 1],
    "wheels": {
        "disablewheelswhendestroyed": 1,
        # Class: CfgVehicles|rhsusf_f22|Wheels|Wheel_1 [Indent level: 2],
        "wheel_1": {
            "steering": 1,
            "side": "left",
            "bonename": "Wheel_1",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 150,
            "moi": 3,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "suspforceapppointoffset": "Wheel_1_center",
            "tireforceapppointoffset": "Wheel_1_center",
            "maxcompression": 0.15,
            "maxdroop": 0.1,
            "sprungmass": 11400,
            "springstrength": 1.2e+006,
            "springdamperrate": 128000,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|rhsusf_f22|Wheels|Wheel_1_fake [Indent level: 2],
        "wheel_1_fake": {
            "steering": 1,
            "side": "left",
            "bonename": "Wheel_1",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 150,
            "moi": 3,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "suspforceapppointoffset": "Wheel_1_center",
            "tireforceapppointoffset": "Wheel_1_center",
            "maxcompression": 0.15,
            "maxdroop": 0.1,
            "sprungmass": 11400,
            "springstrength": 1.2e+006,
            "springdamperrate": 128000,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|rhsusf_f22|Wheels|Wheel_2 [Indent level: 2],
        "wheel_2": {
            "steering": 0,
            "bonename": "Wheel_2",
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "suspforceapppointoffset": "Wheel_2_center",
            "tireforceapppointoffset": "Wheel_2_center",
            "width": 0.28,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "sprungmass": 3200,
            "springstrength": 1.58e+006,
            "springdamperrate": 512000,
            "side": "left",
            "mass": 150,
            "moi": 3,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|rhsusf_f22|Wheels|Wheel_3 [Indent level: 2],
        "wheel_3": {
            "side": "right",
            "bonename": "Wheel_3",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspforceapppointoffset": "Wheel_3_center",
            "tireforceapppointoffset": "Wheel_3_center",
            "steering": 0,
            "width": 0.28,
            "maxcompression": 0.15,
            "maxdroop": 0.15,
            "sprungmass": 3200,
            "springstrength": 1.58e+006,
            "springdamperrate": 512000,
            "mass": 150,
            "moi": 3,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    # Class: CfgVehicles|rhsusf_f22|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_f22|data|body.rvmat","rhsusf|addons|rhsusf_f22|data|body_damage.rvmat","rhsusf|addons|rhsusf_f22|data|body_destruct.rvmat","rhsusf|addons|rhsusf_f22|data|wing.rvmat","rhsusf|addons|rhsusf_f22|data|wing_damage.rvmat","rhsusf|addons|rhsusf_f22|data|wing_destruct.rvmat","rhsusf|addons|rhsusf_f22|data|kolo1.rvmat","rhsusf|addons|rhsusf_f22|data|kolo1.rvmat","rhsusf|addons|rhsusf_f22|data|kolo_destruct.rvmat"]
    },
    # Class: CfgVehicles|rhsusf_f22|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhsusf_f22|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["|rhsusf|addons|rhsusf_f22|data|f22_b1.paa","|rhsusf|addons|rhsusf_f22|data|f22_wing_spads.paa"],
            "factions": ["rhs_faction_usaf"]
        }
    },
    "texturelist": ["standard",1],
    # Class: CfgVehicles|rhsusf_f22|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|rhsusf_f22|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|rhsusf_f22|compartmentsLights|Comp1|Light_General [Indent level: 3]
            "light_general": {
                "color": [20,30,30],
                "ambient": [0,0,0],
                "intensity": 3.05,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 1,
                "blinking": 0,
                # Class: CfgVehicles|rhsusf_f22|compartmentsLights|Comp1|Light_General|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 1.45,
                    "hardlimitend": 2.45
                },
                "point": "light_general"
            }
        }
    },
    # Class: CfgVehicles|rhsusf_f22|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhsusf_f22|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "selection": "l svetlo",
            "position": "light_1_pos",
            "direction": "light_1_dir",
            "hitpoint": "light_1_hit",
            "innerangle": 15,
            "outerangle": 40,
            "conefadecoef": 10,
            "intensity": 50,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            "size": 1,
            # Class: CfgVehicles|rhsusf_f22|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardlimitstart": 150,
                "hardlimitend": 300
            }
        },
        # Class: CfgVehicles|rhsusf_f22|Reflectors|Left_Flare [Indent level: 2],
        "left_flare": {
            "color": [70,75,100,1],
            "position": "light_1_pos_flare",
            "useflare": 1,
            "outerangle": 160,
            "ambient": [100,100,100],
            "selection": "l svetlo",
            "direction": "light_1_dir",
            "hitpoint": "light_1_hit",
            "innerangle": 15,
            "conefadecoef": 10,
            "intensity": 50,
            "daylight": 0,
            "flaresize": 1,
            "size": 1,
            # Class: CfgVehicles|rhsusf_f22|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardlimitstart": 150,
                "hardlimitend": 300
            }
        },
        # Class: CfgVehicles|rhsusf_f22|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "light_2_pos",
            "direction": "light_2_dir",
            "hitpoint": "light_2_hit",
            "selection": "p svetlo",
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "innerangle": 15,
            "outerangle": 40,
            "conefadecoef": 10,
            "intensity": 50,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1,
            "size": 1,
            # Class: CfgVehicles|rhsusf_f22|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardlimitstart": 150,
                "hardlimitend": 300
            }
        },
        # Class: CfgVehicles|rhsusf_f22|Reflectors|Right_Flare [Indent level: 2],
        "right_flare": {
            "color": [70,75,100,1],
            "position": "light_2_pos_flare",
            "useflare": 1,
            "outerangle": 160,
            "direction": "light_2_dir",
            "hitpoint": "light_2_hit",
            "selection": "p svetlo",
            "ambient": [100,100,100],
            "innerangle": 15,
            "conefadecoef": 10,
            "intensity": 50,
            "daylight": 0,
            "flaresize": 1,
            "size": 1,
            # Class: CfgVehicles|rhsusf_f22|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardlimitstart": 150,
                "hardlimitend": 300
            }
        }
    },
    "aggregatereflectors": [["Left","Left_Flare","Right","Right_Flare"]],
    "features": "Randomization: No						<br />Camo selections: 2 - the main body, wings and lower part of body						<br />Script door sources: None						<br />Script animations: AddScalpel, AddAsraam_out, AddAsraam_mid, AddMk82, AddGbu12, AddZephyr, AddDar						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: None",
    "mapsize": 13.02,
    "_generalmacro": "Plane_Fighter_03_base_F",
    "editorsubcategory": "EdSubcat_Planes",
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "armorlights": 0.1,
    "mintotaldamagethreshold": 0.008,
    "waterleakiness": 1.5,
    "destrtype": "DestructWreck",
    "slingloadcargomemorypoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "viewdrivershadowdiff": 0.5,
    "viewdrivershadowamb": 0.5,
    # Class: CfgVehicles|Plane_Fighter_03_base_F|Turrets [Indent level: 1],
    "turrets": {
    },
    # Class: CfgVehicles|Plane_Fighter_03_base_F|TransportItems [Indent level: 1],
    "transportitems": {
    },
    "attenuationeffecttype": "PlaneAttenuation",
    "soundgetin": ["A3|Sounds_F|air|Plane_Fighter_03|buzzard_getin",1,1,40],
    "soundgetout": ["A3|Sounds_F|air|Plane_Fighter_03|getout",1,1,40],
    "cabinopensound": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinOpen",1.77828,1,40],
    "cabinclosesound": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinClose",1.77828,1,40],
    "cabinopensoundinternal": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinOpen",10,1,40],
    "cabinclosesoundinternal": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinClose",10,1,40],
    "sounddammage": ["A3|Sounds_F|debugsound",1.77828,1,100],
    "buildcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "buildcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "buildcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "buildcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundbuildingcrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "woodcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_1",3.16228,1,900],
    "woodcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_2",3.16228,1,900],
    "woodcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_6",3.16228,1,900],
    "woodcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_8",3.16228,1,900],
    "soundwoodcrash": ["woodCrash0",0.25,"woodCrash1",0.25,"woodCrash2",0.25,"woodCrash3",0.25],
    "armorcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "armorcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "armorcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "armorcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundarmorcrash": ["ArmorCrash0",0.25,"ArmorCrash1",0.25,"ArmorCrash2",0.25,"ArmorCrash3",0.25],
    "crash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "crash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "crash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "crash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundcrashes": ["Crash0",0.25,"Crash1",0.25,"Crash2",0.25,"Crash3",0.25],
    "soundwatercollision1": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_1",1.41254,1,500],
    "soundwatercollision2": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_2",1.41254,1,500],
    "soundwatercrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "landingsoundint0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int1",1,1,100],
    "landingsoundint1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int2",1,1,100],
    "landingsoundint": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingsoundout0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext1",1.77828,1,100],
    "landingsoundout1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext2",1.77828,1,100],
    "landingsoundout": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    # Class: CfgVehicles|Plane_Fighter_03_base_F|scrubLandInt [Indent level: 1],
    "scrublandint": {
        "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
        "frequency": 1,
        "volume": "(scrubLand factor[0.01, 0.20])"
    },
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 0,
    "antirollbarspeedmin": 50,
    "antirollbarspeedmax": 300,
    "irscanrangemin": 500,
    "irscanrangemax": 5000,
    "irscantoeyefactor": 2,
    "showalltargets": 4,
    # Class: CfgVehicles|Plane_Fighter_03_base_F|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -3,
        "initfov": 0.75,
        "minfov": 0.25,
        "maxfov": 1.25,
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
    "memorypointdriveroptics": "PilotCamera_pos",
    "driverweaponsinfotype": "RscOptics_CAS_01_TGP",
    # Class: CfgVehicles|Plane_Fighter_03_base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": "The A-143 Buzzard is a single seat light multi-purpose combat aircraft able to carry a wide range of equipment and weaponry. A-143 has seven weapon hardpoints, three under each wing and one under the fuselage. Standard armament consists of 20mm cannon, and a mixture of AA and AG rockets."
    },
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "driverrighthandanimname": "stick_pilot",
    "waterlineardampingcoefy": 0,
    "waterlineardampingcoefx": 5,
    "waterresistancecoef": 0.04,
    "ejectspeed": [0,60,0],
    "transportmaxweapons": 6,
    "transportmaxmagazines": 24,
    "transportmaxbackpacks": 6,
    "maximumload": 500,
    "supplyradius": 2,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Plane_Base_F|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
    # Class: CfgVehicles|Plane_Base_F|TransportMagazines [Indent level: 1],
    "transportmagazines": {
    },
    # Class: CfgVehicles|Plane_Base_F|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|Plane_Base_F|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minspeed": 1
    },
    "mingforce": 0.3,
    "maxgforce": 3,
    "gforceshakeattenuation": 0.5,
    # Class: CfgVehicles|Plane_Base_F|NewTurret [Indent level: 1],
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
    "formationx": 200,
    "formationz": 300,
    "precision": 200,
    "steeraheadsimul": 1,
    "steeraheadplan": 2,
    "gearretracting": 1,
    "cabinopening": 1,
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "vtol": 0,
    "tailhook": 0,
    "lightongear": 1,
    "gearuptime": 3.33,
    "geardowntime": 2,
    "simulation": "airplanex",
    "mingunelev": 0,
    "maxgunelev": 0,
    "mingunturn": 0,
    "maxgunturn": 0,
    "vtolyawinfluence": 2,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
    # Class: CfgVehicles|Plane|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initanglex": 0,
        "minanglex": 0,
        "maxanglex": 0,
        "initangley": 0,
        "minangley": 0,
        "maxangley": 0,
        "initfov": 0.5,
        "minfov": 0.5,
        "maxfov": 0.5,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "selectionrotorstill": "vrtule staticka",
    "selectionrotormove": "vrtule blur",
    "memorypointldust": "levy prach",
    "memorypointrdust": "pravy prach",
    "selectionfireanim": "zasleh",
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
    # Class: CfgVehicles|Plane|GunFire [Indent level: 1],
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
    # Class: CfgVehicles|Plane|GunClouds [Indent level: 1],
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
    # Class: CfgVehicles|Plane|MGunFire [Indent level: 1],
    "mgunfire": {
        "cloudletduration": 0,
        "cloudletgrowup": 0.06,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.12,
        "interval": 0.005,
        "size": 0.12,
        "sourcesize": 0.01,
        "initt": 3200,
        "deltat": -4000,
        "access": 0,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletFire",
        "cloudletcolor": [1,1,1,0],
        "timetolive": 0,
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
    # Class: CfgVehicles|Plane|MGunClouds [Indent level: 1],
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
    "numberphysicalwheels": 3,
    # Class: CfgVehicles|Plane|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Plane|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_air_plane_s"],
            "speechplural": ["veh_air_plane_p"]
        }
    },
    "textsingular": "fast mover",
    "textplural": "fast movers",
    "namesound": "veh_air_plane_s",
    "memorypointgun": "kulomet",
    "fuelexplosionpower": 10,
    "crewcrashprotection": 0.15,
    "damageeffect": "AirDestructionEffects",
    "getinaction": "GetInHigh",
    "getoutaction": "GetOutHigh",
    "cargogetinaction": ["GetInHigh"],
    "cargogetoutaction": ["GetOutHigh"],
    "gunnergetinaction": "GetInHigh",
    "gunnergetoutaction": "GetOutHigh",
    "getinradius": 1.2,
    # Class: CfgVehicles|Plane|CamShake [Indent level: 1],
    "camshake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minspeed": 200
    },
    "explosionshielding": 2,
    # Class: CfgVehicles|Plane|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "formationtime": 10,
    "fuelcapacity": 1000,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "nightvision": 0,
    "cargocompartments": [0],
    "enablegps": 1,
    "weaponsgroup1": "1 + 		2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    "maxfordingdepth": 0.001,
    "waterresistance": 1,
    "impacteffectssea": "ImpactEffectsAir",
    "flarevelocity": 100,
    "enableradio": 1,
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "countermeasureactivationradius": 10000,
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
    "tracksspeed": 0,
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    # Class: CfgVehicles|AllVehicles|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    "cargoproxyindexes": [],
    "driverdoor": "",
    "cargodoors": [],
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
    "availableforsupporttypes": [],
    "waterppinvehicle": 1,
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
    "slowspeedforwardcoef": 0.3,
    "normalspeedforwardcoef": 0.85,
    "gunnerhasflares": 1,
    "enablemanualfire": 1,
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "portrait": "",
    "ghostpreview": "",
    "crewvulnerable": 1,
    "replacedamaged": "",
    "replacedamagedlimit": 0.9,
    "replacedamagedhitpoints": [],
    "keepinepesceneafterdeath": 0,
    "fuelconsumptionrate": 0.01,
    "groupcameraposition": [0,5,-30],
    "extcameraparams": [1],
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
    "nvtarget": 0,
    "nvscanner": 0,
    "artillerytarget": 0,
    "artilleryscanner": 0,
    "canusescanners": 1,
    "preferroads": 0,
    "unitinfotypelite": 0,
    "hideunitinfo": 0,
    "limitedspeedcoef": 0.22,
    "hasdriver": 1,
    "driverforceoptics": 0,
    "hideweaponsdriver": 1,
    "hideweaponscargo": 0,
    "enablewatch": 0,
    "useprecisegetinaction": 0,
    "allowtablock": 1,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "wheelcircumference": 1,
    "waterangulardampingcoef": 0,
    "shownvgdriver": 0,
    "shownvgcommander": 0,
    "shownvggunner": 0,
    "shownvgcargo": [0],
    "soundattenuationcargo": [1],
    "countsforscoreboard": 1,
    "hulldamagecauseexplosion": 0,
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
    "soundlandcrashes": ["soundLandCrash",1],
    "emptysound": ["",0,1],
    "soundbushcrash": ["emptySound",0],
    "driverinaction": "",
    "cargoaction": [],
    "cargoiscodriver": [0],
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "hideproxyincombat": 0,
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
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
    "slingloadcargomemorypointsdir": [],
    "damagehalf": [],
    "damagefull": [],
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "insidedetectcoef": 0.05,
}