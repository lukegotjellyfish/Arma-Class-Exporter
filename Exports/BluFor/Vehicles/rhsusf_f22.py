rhsusf_f22 = {
    "rhs_gearAnim": "fold_gear_F",
    "scope": 2,
    "dlc": "RHS_USAF",
    "author": "Red Hammer Studios",
    "category": "Air",
    "side": 1,
    "crew": "rhsusf_airforce_jetpilot",
    "typicalCargo": ["rhsusf_airforce_jetpilot"],
    "unitInfoType": "RHSUSF_RscUnitInfoJet_F22",
    "vehicleClass": "rhs_vehclass_aircraft",
    "faction": "rhs_faction_usaf",
    # Class: CfgVehicles\rhsusf_f22\pilotCamera,
    "pilotCamera": {
    },
    # Class: CfgVehicles\rhsusf_f22\EjectionSystem,
    "EjectionSystem": {
    },
    "model": "rhsusf|addons|rhsusf_f22|rhsusf_f22",
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_f22.paa",
    "displayName": "F-22A",
    "driverAction": "RHS_F22_Pilot",
    "driverLeftHandAnimName": "stick_thrust",
    "driverLeftLegAnimName": "pedal_L",
    "driverRightLegAnimName": "pedal_R",
    "driverCanEject": 1,
    "driverCompartments": 1,
    "htMin": 6,
    "htMax": 18,
    "afMax": 10,
    "mfMax": 30,
    "mFact": 10.02,
    "tBody": 150,
    "irTarget": 1,
    "irTargetSize": 0.5,
    "visualTarget": 1,
    "visualTargetSize": 1,
    "radarTarget": 1,
    "radarTargetSize": 0.3,
    "radarType": 4,
    "LockDetectionSystem": 8,
    "incomingMissileDetectionSystem": 16,
    "receiveRemoteTargets": 1,
    "reportRemoteTargets": 1,
    "reportOwnPosition": 1,
    "laserScanner": 1,
    # Class: CfgVehicles\rhsusf_f22\Components,
    "Components": {
        # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent
        "TransportPylonsComponent": {
            "UIPicture": "rhsusf|addons|rhsusf_f22|data|loadouts|RHS_F22_EDEN_CA.paa",
            # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\pylons,
            "pylons": {
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\pylons\pylonBayLeft1
                "pylonBayLeft1": {
                    "hardpoints": ["RHS_HP_AIM9_int"],
                    "priority": 2,
                    "attachment": "rhs_mag_Sidewinder_int",
                    "maxweight": 1200,
                    "UIposition": [0.36,0.4],
                    "bay": 1
                },
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\pylons\pylonBayCenter1,
                "pylonBayCenter1": {
                    "hardpoints": ["RHS_HP_aim120_int"],
                    "priority": 1,
                    "attachment": "rhs_mag_aim120d_int",
                    "maxweight": 1200,
                    "UIposition": [0.36,0.35],
                    "bay": 2
                },
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\pylons\pylonBayCenter2,
                "pylonBayCenter2": {
                    "hardpoints": ["RHS_HP_aim120_int","RHS_HP_F22_lBay","RHS_HP_JDAM_500","RHS_HP_JDAM_1000"],
                    "attachment": "rhs_mag_aim120d_2_F22_l",
                    "UIposition": [0.36,0.3],
                    "priority": 1,
                    "maxweight": 1200,
                    "bay": 2
                },
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\pylons\pylonBayCenter3,
                "pylonBayCenter3": {
                    "hardpoints": ["RHS_HP_aim120_int","RHS_HP_F22_rBay","RHS_HP_JDAM_500","RHS_HP_JDAM_1000"],
                    "attachment": "rhs_mag_aim120d_2_F22_r",
                    "UIposition": [0.36,0.25],
                    "bay": 3,
                    "priority": 1,
                    "maxweight": 1200
                },
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\pylons\pylonBayCenter4,
                "pylonBayCenter4": {
                    "hardpoints": ["RHS_HP_aim120_int"],
                    "attachment": "rhs_mag_aim120d_int",
                    "UIposition": [0.36,0.2],
                    "mirroredMissilePos": 2,
                    "bay": 3,
                    "priority": 1,
                    "maxweight": 1200
                },
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\pylons\pylonBayRight1,
                "pylonBayRight1": {
                    "UIposition": [0.36,0.15],
                    "mirroredMissilePos": 1,
                    "bay": 4,
                    "hardpoints": ["RHS_HP_AIM9_int"],
                    "priority": 2,
                    "attachment": "rhs_mag_Sidewinder_int",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\pylons\cmDispenser,
                "cmDispenser": {
                    "hardpoints": ["RHSUSF_cm_ANALE52","RHSUSF_cm_ANALE52_x2","RHSUSF_cm_ANALE52_x4","RHSUSF_cm_ANALE52_x6"],
                    "priority": 1,
                    "attachment": "rhsusf_ANALE52_CMFlare_Chaff_Magazine_x4",
                    "maxweight": 800,
                    "UIposition": [0.625,0.275]
                }
            },
            # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\Bays,
            "Bays": {
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\Bays\BayLeft1
                "BayLeft1": {
                    "bayOpenTime": 0.5,
                    "openBayWhenWeaponSelected": 1,
                    "autoCloseWhenEmptyDelay": 1
                },
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\Bays\BayCenter1,
                "BayCenter1": {
                    "bayOpenTime": 0.5,
                    "openBayWhenWeaponSelected": 0,
                    "autoCloseWhenEmptyDelay": 4.5
                },
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\Bays\BayCenter2,
                "BayCenter2": {
                    "bayOpenTime": 0.5,
                    "openBayWhenWeaponSelected": 0,
                    "autoCloseWhenEmptyDelay": 4.5
                },
                # Class: CfgVehicles\rhsusf_f22\Components\TransportPylonsComponent\Bays\BayRight1,
                "BayRight1": {
                    "bayOpenTime": 0.5,
                    "openBayWhenWeaponSelected": 1,
                    "autoCloseWhenEmptyDelay": 1
                }
            }
        },
        # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent,
        "SensorsManagerComponent": {
            # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components
            "Components": {
                # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components\PassiveRadarSensorComponent
                "PassiveRadarSensorComponent": {
                    # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components\PassiveRadarSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 18000,
                        "maxRange": 18000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components\PassiveRadarSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 18000,
                        "maxRange": 18000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "componentType": "PassiveRadarSensorComponent",
                    "typeRecognitionDistance": 12000,
                    "angleRangeHorizontal": 360,
                    "angleRangeVertical": 360,
                    "groundNoiseDistanceCoef": -1,
                    "maxGroundNoiseDistance": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "animDirection": "",
                    "aimDown": 0,
                    "color": [0.5,1,0.5,0.5],
                    "minTrackableSpeed": -1e+010,
                    "maxTrackableSpeed": 1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010,
                    "allowsMarking": 0
                },
                # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent,
                "ActiveRadarSensorComponent": {
                    # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 35000,
                        "maxRange": 35000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 10000,
                        "maxRange": 10000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "groundNoiseDistanceCoef": 0.0005,
                    "maxGroundNoiseDistance": 50,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "angleRangeHorizontal": 60,
                    "angleRangeVertical": 60,
                    "typeRecognitionDistance": 20000,
                    "maxFogSeeThrough": 1,
                    "maxTrackableSpeed": 830,
                    "componentType": "ActiveRadarSensorComponent",
                    "color": [0,1,1,1],
                    "allowsMarking": 1,
                    "animDirection": "",
                    "aimDown": 0,
                    "minTrackableSpeed": -1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent_Wide,
                "ActiveRadarSensorComponent_Wide": {
                    # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent_Wide\AirTarget
                    "AirTarget": {
                        "minRange": 10000,
                        "maxRange": 10000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent_Wide\GroundTarget,
                    "GroundTarget": {
                        "minRange": 10000,
                        "maxRange": 10000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "groundNoiseDistanceCoef": 0.0005,
                    "maxGroundNoiseDistance": 50,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "angleRangeHorizontal": 110,
                    "angleRangeVertical": 110,
                    "typeRecognitionDistance": 10000,
                    "maxFogSeeThrough": 1,
                    "maxTrackableSpeed": 830,
                    "componentType": "ActiveRadarSensorComponent",
                    "color": [0,1,1,1],
                    "allowsMarking": 1,
                    "animDirection": "",
                    "aimDown": 0,
                    "minTrackableSpeed": -1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\rhsusf_f22\Components\SensorsManagerComponent\Components\DataLinkSensorComponent,
                "DataLinkSensorComponent": {
                    "componentType": "DataLinkSensorComponent",
                    "allowsMarking": 1,
                    "typeRecognitionDistance": 0,
                    "color": [1,1,1,0],
                    # Class: SensorTemplatePassiveRadar\AirTarget,
                    "AirTarget": {
                        "minRange": 16000,
                        "maxRange": 16000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: SensorTemplatePassiveRadar\GroundTarget,
                    "GroundTarget": {
                        "minRange": 16000,
                        "maxRange": 16000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "angleRangeHorizontal": 360,
                    "angleRangeVertical": 360,
                    "groundNoiseDistanceCoef": -1,
                    "maxGroundNoiseDistance": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "animDirection": "",
                    "aimDown": 0,
                    "minTrackableSpeed": -1e+010,
                    "maxTrackableSpeed": 1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                }
            }
        },
        # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentLeft,
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentLeft\Components
            "Components": {
                # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentLeft\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentLeft\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SensorDisplay,
                "SensorDisplay": {
                    "componentType": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [16000,35000,3000,8000]
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultDisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentRight,
        "VehicleSystemsDisplayManagerComponentRight": {
            "defaultDisplay": "SensorDisplay",
            # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentRight\Components,
            "Components": {
                # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentRight\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentRight\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles\rhsusf_f22\Components\VehicleSystemsDisplayManagerComponentRight\Components\SensorDisplay,
                "SensorDisplay": {
                    "componentType": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [16000,35000,3000,8000]
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles\Air\Components\TransportCountermeasuresComponent,
        "TransportCountermeasuresComponent": {
        }
    },
    "icon": "rhsusf|addons|rhsusf_f22|data|f22_icon.paa",
    "picture": "rhsusf|addons|rhsusf_f22|data|f22_pic.paa",
    "weapons": ["rhs_weap_MASTERSAFE_Holdster15","rhsusf_M61A2"],
    "magazines": ["rhsusf_20mm_M61A2"],
    "insideSoundCoef": 0.2,
    "hiddenSelections": ["tex1","tex2","tex3","tex4","tex5","tex6","tex7","tex8","tex9"],
    "hiddenSelectionsTextures": ["|rhsusf|addons|rhsusf_f22|data|f22_b1.paa","|rhsusf|addons|rhsusf_f22|data|f22_wing_spads.paa","|rhsusf|addons|rhsusf_f22|data|1stfw.paa","|rhsusf|addons|rhsusf_f22|data|94fs.paa","|rhsusf|addons|rhsusf_f22|data|acc.paa","|rhsusf|addons|rhsusf_f22|data|af04-066.paa","|rhsusf|addons|rhsusf_f22|data|ff.paa","|rhsusf|addons|rhsusf_f22|data|marking1.paa","|rhsusf|addons|rhsusf_f22|data|star1.paa"],
    "camouflage": 18,
    "audible": 6,
    "accuracy": 0.2,
    "gunAimDown": 0.045,
    "memoryPointLRocket": "Rocket_1",
    "memoryPointRRocket": "Rocket_2",
    "gunBeg": ["muzzle_1"],
    "gunEnd": ["chamber_1"],
    "camShakeCoef": 0.6,
    "headGforceLeaningFactor": [0.005,0.001,0.015],
    "extCameraPosition": [0,3.8,-23],
    "minFireTime": 30,
    "cost": 8e+007,
    "type": 2,
    "threat": [1,1,0.7],
    "driveOnComponent": [],
    "armor": 80,
    "armorStructural": 3,
    "ejectDamageLimit": 1,
    "epeImpulseDamageCoef": 1,
    "damageResistance": 0.00336,
    # Class: CfgVehicles\rhsusf_f22\Hitpoints,
    "Hitpoints": {
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitHull
        "HitHull": {
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0.01,
            "minimalHit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull",
            "visual": "",
            "depends": "Total"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitAvionics,
        "HitAvionics": {
            "armor": 0.5,
            "explosionShielding": 0.6,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitEngine,
        "HitEngine": {
            "armor": 0.7,
            "explosionShielding": 0.25,
            "passThrough": 0.01,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_l",
            "depends": "0"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitEngine2,
        "HitEngine2": {
            "armor": 0.7,
            "explosionShielding": 0.25,
            "passThrough": 0.01,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_r",
            "depends": "0"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitFuel,
        "HitFuel": {
            "armor": 0.75,
            "explosionShielding": 0.2,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel",
            "visual": "vis_fuel",
            "depends": "0"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitLAileron,
        "HitLAileron": {
            "armor": 0.5,
            "explosionShielding": 0.6,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "visual": "vis_wing_l",
            "depends": "0"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitRAileron,
        "HitRAileron": {
            "armor": 0.5,
            "explosionShielding": 0.6,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "visual": "vis_wing_r",
            "depends": "0"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitControlRear,
        "HitControlRear": {
            "armor": 0.5,
            "explosionShielding": 0.1,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.17,
            "material": -1,
            "name": "hit_control_rear",
            "visual": "",
            "depends": "0"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitLCElevator,
        "HitLCElevator": {
            "armor": 0.5,
            "explosionShielding": 0.5,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitRElevator,
        "HitRElevator": {
            "armor": 0.5,
            "explosionShielding": 0.5,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitLCRudder,
        "HitLCRudder": {
            "armor": 0.5,
            "explosionShielding": 0.5,
            "passThrough": 0.01,
            "minimalHit": 0.02,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder_l",
            "visual": "vis_rudder_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitRRudder,
        "HitRRudder": {
            "armor": 0.5,
            "explosionShielding": 0.5,
            "passThrough": 0.01,
            "minimalHit": 0.02,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder_r",
            "visual": "vis_rudder_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\rhsusf_f22\Hitpoints\HitGlass1,
        "HitGlass1": {
            "armor": 0.4,
            "explosionShielding": 0.5,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "glass_1",
            "visual": "glass_1",
            "depends": "0"
        }
    },
    "soundEngineOnInt": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_01|B_PLANE_FIGHTER_01_engine_start_int",1,1],
    "soundEngineOnExt": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_01|B_PLANE_FIGHTER_01_engine_start_ext",1.75,1,300],
    "soundEngineOffInt": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_01|B_PLANE_FIGHTER_01_engine_shut_int",1,1],
    "soundEngineOffExt": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_01|B_PLANE_FIGHTER_01_engine_shut_ext",1.75,1,300],
    "soundLocked": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_lockedOn1",1,1],
    "soundIncommingMissile": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_lockedon2",1,1.5],
    "soundGearUp": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_gear_up",2.25,1,250],
    "soundGearDown": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_gear_down",2.25,1,250],
    "soundFlapsUp": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_Flaps_Up",1.5,1,150],
    "soundFlapsDown": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_Flaps_Down",1.5,1,150],
    "soundSetSonicBoom": ["Plane_Fighter_SonicBoom_SoundSet"],
    # Class: CfgVehicles\rhsusf_f22\Sounds,
    "Sounds": {
        "soundSets": ["Plane_Fighter_01_EngineLowExt_SoundSet","Plane_Fighter_01_EngineHighExt_SoundSet","Plane_Fighter_01_ForsageExt_SoundSet","Plane_Fighter_01_WindNoiseExt_SoundSet","Plane_Fighter_01_EngineExt_Dist_Front_SoundSet","Plane_Fighter_01_EngineExt_Middle_SoundSet","Plane_Fighter_01_EngineExt_Dist_Rear_SoundSet","Plane_Fighter_01_EngineLowInt_SoundSet","Plane_Fighter_01_EngineHighInt_SoundSet","Plane_Fighter_01_ForsageInt_SoundSet","Plane_Fighter_01_WindNoiseInt_SoundSet","Plane_Fighter_01_VelocityInt_SoundSet"]
    },
    # Class: CfgVehicles\rhsusf_f22\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\rhsusf_f22\Exhausts\Exhaust1
        "Exhaust1": {
            "position": "rightengine",
            "direction": "rightengine_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineIndex": 1
        },
        # Class: CfgVehicles\rhsusf_f22\Exhausts\Exhaust2,
        "Exhaust2": {
            "position": "leftengine",
            "direction": "leftengine_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineIndex": 0
        }
    },
    # Class: CfgVehicles\rhsusf_f22\WingVortices,
    "WingVortices": {
        # Class: CfgVehicles\rhsusf_f22\WingVortices\WingTipLeft
        "WingTipLeft": {
            "effectName": "WingVortices",
            "position": "wing_vortex_l"
        },
        # Class: CfgVehicles\rhsusf_f22\WingVortices\WingTipRight,
        "WingTipRight": {
            "effectName": "WingVortices",
            "position": "wing_vortex_r"
        },
        # Class: CfgVehicles\rhsusf_f22\WingVortices\BodyLeft,
        "BodyLeft": {
            "effectName": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles\rhsusf_f22\WingVortices\BodyRight,
        "BodyRight": {
            "effectName": "BodyVortices",
            "position": "body_vapour_R_S"
        },
        # Class: CfgVehicles\rhsusf_f22\WingVortices\BodyLeft2,
        "BodyLeft2": {
            "effectName": "BodyVortices",
            "position": "body_vapour_L_E"
        },
        # Class: CfgVehicles\rhsusf_f22\WingVortices\BodyRight2,
        "BodyRight2": {
            "effectName": "BodyVortices",
            "position": "body_vapour_R_E"
        }
    },
    # Class: CfgVehicles\rhsusf_f22\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\rhsusf_f22\AnimationSources\afterburner_source
        "afterburner_source": {
            "source": "user",
            "initPhase": 0,
            "animPeriod": 1.5
        },
        # Class: CfgVehicles\rhsusf_f22\AnimationSources\eject,
        "eject": {
            "source": "door",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_f22\AnimationSources\eject_hide,
        "eject_hide": {
            "source": "user",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_f22\AnimationSources\CollisionLights_source,
        "CollisionLights_source": {
            "source": "MarkerLight",
            "markerLight": "PositionLeft"
        },
        # Class: CfgVehicles\rhsusf_f22\AnimationSources\CollisionBlinking_source,
        "CollisionBlinking_source": {
            "markerLight": "CollisionLeft",
            "source": "MarkerLight"
        },
        # Class: CfgVehicles\rhsusf_f22\AnimationSources\Wheel_1_source,
        "Wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles\rhsusf_f22\AnimationSources\Wheel_2_source,
        "Wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles\rhsusf_f22\AnimationSources\Wheel_3_source,
        "Wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        }
    },
    # Class: CfgVehicles\rhsusf_f22\MarkerLights,
    "MarkerLights": {
        # Class: CfgVehicles\rhsusf_f22\MarkerLights\PositionLeft
        "PositionLeft": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "intensity": 750,
            "name": "PositionLight_Left_1_pos",
            "drawLight": 1,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.08,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\rhsusf_f22\MarkerLights\PositionLeft\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\rhsusf_f22\MarkerLights\PositionRight,
        "PositionRight": {
            "name": "PositionLight_Right_1_pos",
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "intensity": 750,
            "drawLight": 1,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.08,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\rhsusf_f22\MarkerLights\PositionLeft\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\rhsusf_f22\MarkerLights\CollisionLeft,
        "CollisionLeft": {
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 2750,
            "blinking": 1,
            "blinkingPattern": [0.2,1.3],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.35,
            "drawLightCenterSize": 0.18,
            "name": "PositionLight_Left_1_pos",
            "drawLight": 1,
            "activeLight": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\rhsusf_f22\MarkerLights\PositionLeft\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\rhsusf_f22\MarkerLights\CollisionRight,
        "CollisionRight": {
            "name": "PositionLight_Right_1_pos",
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 2750,
            "blinking": 1,
            "blinkingPattern": [0.2,1.3],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.35,
            "drawLightCenterSize": 0.18,
            "drawLight": 1,
            "activeLight": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\rhsusf_f22\MarkerLights\PositionLeft\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        }
    },
    # Class: CfgVehicles\rhsusf_f22\UserActions,
    "UserActions": {
        # Class: CfgVehicles\rhsusf_f22\UserActions\SAFEMODE
        "SAFEMODE": {
            "displayName": "<t color='#00FF7F'>MASTERSAFE</t>",
            "condition": "(call rhsusf_fnc_findPlayer) in this",
            "statement": "(call rhsusf_fnc_findPlayer) action ['SwitchWeapon', this, (call rhsusf_fnc_findPlayer), (weapons this) find 'rhs_weap_MASTERSAFE'];",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showWindow": 0,
            "shortcut": "user13",
            "hideOnUse": 1
        }
    },
    # Class: CfgVehicles\rhsusf_f22\Eventhandlers,
    "Eventhandlers": {
        "hit": "",
        # Class: CfgVehicles\rhsusf_f22\Eventhandlers\RHSUSF_EventHandlers,
        "RHSUSF_EventHandlers": {
            "init": "_this execVM '|rhsusf|addons|rhsusf_c_f22|scripts|rhs_f22_mfdHandler.sqf'",
            "hit": "_this call RHS_fnc_AI_eject",
            "getout": "[_this select 0, _this select 2,'rhs_f22_canopy'] call rhs_fnc_ACESII_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes;"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "defaultUserMFDvalues": [0.082,0.408,0.039,0.8],
    "defaultUserMFDtext": ["test"],
    # Class: CfgVehicles\rhsusf_f22\MFD,
    "MFD": {
        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD
        "AirplaneHUD": {
            "topLeft": "HUD LH",
            "topRight": "HUD PH",
            "bottomLeft": "HUD LD",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 1,
            "font": "rhsusf_digital_font_usa",
            # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones,
            "Bones": {
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\PlaneW
                "PlaneW": {
                    "type": "fixed",
                    "pos": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\PlaneOrientation,
                "PlaneOrientation": {
                    "type": "vector",
                    "source": "forward",
                    "pos": [0.495,0.546],
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\Velocity,
                "Velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\WeaponAim,
                "WeaponAim": {
                    "type": "vector",
                    "source": "weapon",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\ImpactPoint,
                "ImpactPoint": {
                    "type": "vector",
                    "source": "ImpactPointWeaponRelative",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\NormalizeBombCircle,
                "NormalizeBombCircle": {
                    "type": "normalizedorsmaller",
                    "limit": 0.08,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\ImpactPointRelative,
                "ImpactPointRelative": {
                    "type": "vector",
                    "source": "impactpointweaponRelative",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\Target,
                "Target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\TargetingPodDir,
                "TargetingPodDir": {
                    "source": "pilotcamera",
                    "type": "vector",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\TargetingPodTarget,
                "TargetingPodTarget": {
                    "source": "pilotcameratarget",
                    "type": "vector",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\Limit0109,
                "Limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LimitWaypoint,
                "LimitWaypoint": {
                    "type": "limit",
                    "limits": [0.33,0.1,0.67,0.1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\WPPoint,
                "WPPoint": {
                    "type": "vector",
                    "source": "WPPoint",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\ASL_Instrument,
                "ASL_Instrument": {
                    "type": "rotational",
                    "source": "altitudeASL",
                    "center": [0.9,0.446429],
                    "min": 0,
                    "max": 20000,
                    "minAngle": 0,
                    "maxAngle": 72000,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\Speed_Instrument,
                "Speed_Instrument": {
                    "source": "speed",
                    "center": [0.1,0.446429],
                    "max": 555.556,
                    "maxAngle": 7200,
                    "type": "rotational",
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\Airport1,
                "Airport1": {
                    "type": "vector",
                    "source": "airportCorner1",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\Airport2,
                "Airport2": {
                    "source": "airportCorner2",
                    "type": "vector",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\Airport3,
                "Airport3": {
                    "source": "airportCorner3",
                    "type": "vector",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\Airport4,
                "Airport4": {
                    "source": "airportCorner4",
                    "type": "vector",
                    "pos0": [0.5,0.536],
                    "pos10": [1.1076,1.0785]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\ILS_H,
                "ILS_H": {
                    "type": "ils",
                    "pos0": [0.5,0.536],
                    "pos3": [0.68228,0.536]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\ILS_W,
                "ILS_W": {
                    "pos3": [0.5,0.69875],
                    "type": "ils",
                    "pos0": [0.5,0.536]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\HorizonBankRot,
                "HorizonBankRot": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "center": [0.5,0.5],
                    "min": "-rad(45)",
                    "max": "rad(45)",
                    "minAngle": "180.25-35.5",
                    "maxAngle": "180.75+35.5",
                    "aspectRatio": 0.8
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\HorizonBankRotFull,
                "HorizonBankRotFull": {
                    "center": [0,0],
                    "min": -3.1416,
                    "max": 3.1416,
                    "minAngle": -180,
                    "maxAngle": 180,
                    "aspectRatio": 1,
                    "type": "rotational",
                    "source": "horizonBank"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\Level0,
                "Level0": {
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP5,
                "LevelP5": {
                    "angle": "1.0*5",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM5,
                "LevelM5": {
                    "angle": "1.0*-5",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP10,
                "LevelP10": {
                    "angle": "1.0*10",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM10,
                "LevelM10": {
                    "angle": "1.0*-10",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP15,
                "LevelP15": {
                    "angle": "1.0*15",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM15,
                "LevelM15": {
                    "angle": "1.0*-15",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP20,
                "LevelP20": {
                    "angle": "1.0*20",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM20,
                "LevelM20": {
                    "angle": "1.0*-20",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP25,
                "LevelP25": {
                    "angle": "1.0*25",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM25,
                "LevelM25": {
                    "angle": "1.0*-25",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP30,
                "LevelP30": {
                    "angle": "1.0*30",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM30,
                "LevelM30": {
                    "angle": "1.0*-30",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP35,
                "LevelP35": {
                    "angle": "1.0*35",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM35,
                "LevelM35": {
                    "angle": "1.0*-35",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP40,
                "LevelP40": {
                    "angle": "1.0*40",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM40,
                "LevelM40": {
                    "angle": "1.0*-40",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP45,
                "LevelP45": {
                    "angle": "1.0*45",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM45,
                "LevelM45": {
                    "angle": "1.0*-45",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP50,
                "LevelP50": {
                    "angle": "1.0*50",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM50,
                "LevelM50": {
                    "angle": "1.0*-50",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP60,
                "LevelP60": {
                    "angle": "1.0*60",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM60,
                "LevelM60": {
                    "angle": "1.0*-60",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP70,
                "LevelP70": {
                    "angle": "1.0*70",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM70,
                "LevelM70": {
                    "angle": "1.0*-70",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP80,
                "LevelP80": {
                    "angle": "1.0*80",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM80,
                "LevelM80": {
                    "angle": "1.0*-80",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelP90,
                "LevelP90": {
                    "angle": "1.0*90",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LevelM90,
                "LevelM90": {
                    "angle": "1.0*-90",
                    "pos0": [0.495,0.546],
                    "pos10": [1.263,1.306],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot1,
                "MissileFlightTimeRot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minAngle": 0,
                    "maxAngle": 18,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot2,
                "MissileFlightTimeRot2": {
                    "maxAngle": 36,
                    "max": 1,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot3,
                "MissileFlightTimeRot3": {
                    "maxAngle": 54,
                    "max": 1.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot4,
                "MissileFlightTimeRot4": {
                    "maxAngle": 72,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot5,
                "MissileFlightTimeRot5": {
                    "maxAngle": 90,
                    "max": 2.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot6,
                "MissileFlightTimeRot6": {
                    "maxAngle": 108,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot7,
                "MissileFlightTimeRot7": {
                    "maxAngle": 126,
                    "max": 3.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot8,
                "MissileFlightTimeRot8": {
                    "maxAngle": 144,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot9,
                "MissileFlightTimeRot9": {
                    "maxAngle": 162,
                    "max": 4.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot10,
                "MissileFlightTimeRot10": {
                    "maxAngle": 180,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot11,
                "MissileFlightTimeRot11": {
                    "maxAngle": 198,
                    "max": 5.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot12,
                "MissileFlightTimeRot12": {
                    "maxAngle": 216,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot13,
                "MissileFlightTimeRot13": {
                    "maxAngle": 234,
                    "max": 6.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot14,
                "MissileFlightTimeRot14": {
                    "maxAngle": 252,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot15,
                "MissileFlightTimeRot15": {
                    "maxAngle": 270,
                    "max": 7.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot16,
                "MissileFlightTimeRot16": {
                    "maxAngle": 288,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot17,
                "MissileFlightTimeRot17": {
                    "maxAngle": 306,
                    "max": 8.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot18,
                "MissileFlightTimeRot18": {
                    "maxAngle": 324,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot19,
                "MissileFlightTimeRot19": {
                    "maxAngle": 342,
                    "max": 9.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\MissileFlightTimeRot20,
                "MissileFlightTimeRot20": {
                    "maxAngle": 360,
                    "max": 10,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LarAmmoMax,
                "LarAmmoMax": {
                    "type": "linear",
                    "source": "LarAmmoMax",
                    "sourceScale": 1,
                    "min": 0,
                    "max": 1,
                    "minPos": [0,1],
                    "maxPos": [0,0]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LarAmmoMin,
                "LarAmmoMin": {
                    "source": "LarAmmoMin",
                    "type": "linear",
                    "sourceScale": 1,
                    "min": 0,
                    "max": 1,
                    "minPos": [0,1],
                    "maxPos": [0,0]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LarTargetDist,
                "LarTargetDist": {
                    "source": "LarTargetDist",
                    "type": "linear",
                    "sourceScale": 1,
                    "min": 0,
                    "max": 1,
                    "minPos": [0,1],
                    "maxPos": [0,0]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LarAmmoMGunMax,
                "LarAmmoMGunMax": {
                    "type": "rotational",
                    "source": "LarAmmoMax",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 1,
                    "minAngle": -180,
                    "maxAngle": 180,
                    "aspectRatio": 0.892857
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Bones\LarAmmoMGunMin,
                "LarAmmoMGunMin": {
                    "source": "LarAmmoMin",
                    "type": "rotational",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 1,
                    "minAngle": -180,
                    "maxAngle": 180,
                    "aspectRatio": 0.892857
                }
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw,
            "Draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\PlaneW,
                "PlaneW": {
                    "type": "line",
                    "width": 3,
                    "points": [["PlaneW",[-0.02,0],1],["PlaneW",[0.02,0],1],[],["PlaneW",[0,-0.0178571],1],["PlaneW",[0,0.0178571],1],[],[[0.11,0.777],1],[[0.09,0.76],1],[[0.085,0.758],1],[[0.08,0.758],1],[[0.075,0.76],1],[[0.073,0.767],1],[[0.075,0.774],1],[[0.08,0.776],1],[[0.085,0.776],1],[[0.09,0.774],1],[[0.11,0.757],1],[],["PlaneW",["-0.4-0.01",-0.25],1],["PlaneW",["-0.4-0",-0.241071],1],["PlaneW",["-0.4-0.01",-0.232143],1],[],[],[[0.805,0.779407],1],[[0.815,0.794872],1],[],[[0.732264,0.811433],1],[[0.739917,0.827931],1],[],[[0.655468,0.834709],1],[[0.660644,0.851958],1],[],[[0.575926,0.848836],1],[[0.578537,0.86654],1],[],[[0.495,0.853571],1],[[0.495,0.871429],1],[],[[0.414074,0.848836],1],[[0.411463,0.86654],1],[],[[0.334532,0.834709],1],[[0.329356,0.851958],1],[],[[0.257736,0.811433],1],[[0.250082,0.827931],1],[],[[0.185,0.779407],1],[[0.175,0.794872],1],[],["HorizonBankRot",[0,0.4375],1],["HorizonBankRot",[0.01,0.419643],1],["HorizonBankRot",[-0.01,0.419643],1],["HorizonBankRot",[0,0.4375],1],[],["Velocity",[0,-0.02],1],["Velocity",[0.01,-0.01732],1],["Velocity",[0.01732,-0.01],1],["Velocity",[0.02,0],1],["Velocity",[0.01732,0.01],1],["Velocity",[0.01,0.01732],1],["Velocity",[0,0.02],1],["Velocity",[-0.01,0.01732],1],["Velocity",[-0.01732,0.01],1],["Velocity",[-0.02,0],1],["Velocity",[-0.01732,-0.01],1],["Velocity",[-0.01,-0.01732],1],["Velocity",[0,-0.02],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.04],1],["Velocity",[0,-0.02],1]]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Static_Bold,
                "Static_Bold": {
                    "type": "line",
                    "width": 5,
                    "points": [[[0.0965,0.511161],1],[[0.1035,0.511161],1],[],[[0.1,0.508036],1],[[0.1,0.514286],1],[],[[0.139114,0.498798],1],[[0.146114,0.498798],1],[],[[0.142614,0.495673],1],[[0.142614,0.501923],1],[],[[0.165452,0.466432],1],[[0.172452,0.466432],1],[],[[0.168952,0.463307],1],[[0.168952,0.469557],1],[],[[0.165452,0.426425],1],[[0.172452,0.426425],1],[],[[0.168952,0.4233],1],[[0.168952,0.42955],1],[],[[0.139114,0.394059],1],[[0.146114,0.394059],1],[],[[0.142614,0.390934],1],[[0.142614,0.397184],1],[],[[0.0965,0.381696],1],[[0.1035,0.381696],1],[],[[0.1,0.378571],1],[[0.1,0.384821],1],[],[[0.0538856,0.394059],1],[[0.0608856,0.394059],1],[],[[0.0573856,0.390934],1],[[0.0573856,0.397184],1],[],[[0.0275484,0.426425],1],[[0.0345484,0.426425],1],[],[[0.0310484,0.4233],1],[[0.0310484,0.42955],1],[],[[0.0275484,0.466432],1],[[0.0345484,0.466432],1],[],[[0.0310484,0.463307],1],[[0.0310484,0.469557],1],[],[[0.0538856,0.498798],1],[[0.0608856,0.498798],1],[],[[0.0573856,0.495673],1],[[0.0573856,0.501923],1],[],["Speed_Instrument",[0,0.055],1],["Speed_Instrument",[0,0.075],1],[],[[0.8965,0.511161],1],[[0.9035,0.511161],1],[],[[0.9,0.508036],1],[[0.9,0.514286],1],[],[[0.939114,0.498798],1],[[0.946114,0.498798],1],[],[[0.942614,0.495673],1],[[0.942614,0.501923],1],[],[[0.965452,0.466432],1],[[0.972452,0.466432],1],[],[[0.968952,0.463307],1],[[0.968952,0.469557],1],[],[[0.965452,0.426425],1],[[0.972452,0.426425],1],[],[[0.968952,0.4233],1],[[0.968952,0.42955],1],[],[[0.939114,0.394059],1],[[0.946114,0.394059],1],[],[[0.942614,0.390934],1],[[0.942614,0.397184],1],[],[[0.8965,0.381696],1],[[0.9035,0.381696],1],[],[[0.9,0.378571],1],[[0.9,0.384821],1],[],[[0.853886,0.394059],1],[[0.860886,0.394059],1],[],[[0.857386,0.390934],1],[[0.857386,0.397184],1],[],[[0.827548,0.426425],1],[[0.834548,0.426425],1],[],[[0.831048,0.4233],1],[[0.831048,0.42955],1],[],[[0.827548,0.466432],1],[[0.834548,0.466432],1],[],[[0.831048,0.463307],1],[[0.831048,0.469557],1],[],[[0.853886,0.498798],1],[[0.860886,0.498798],1],[],[[0.857386,0.495673],1],[[0.857386,0.501923],1],[],["ASL_Instrument",[0,0.055],1],["ASL_Instrument",[0,0.075],1],[]]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AfterBurner,
                "AfterBurner": {
                    "condition": "throttle >=1",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AfterBurner\PlaneW,
                    "PlaneW": {
                        "type": "line",
                        "width": 3,
                        "points": [["PlaneW",["-0.38-0.01",-0.25],1],["PlaneW",["-0.38-0",-0.241071],1],["PlaneW",["-0.38-0.01",-0.232143],1],[]]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont,
                "Horizont": {
                    "clipTL": [0.1,0.15],
                    "clipBR": [0.85,0.99],
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\Dimmed,
                    "Dimmed": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\Dimmed\Level0
                        "Level0": {
                            "type": "line",
                            "width": 3,
                            "points": [["Level0",[0.25,0],1],["Level0",[0.065,0],1],[],["Level0",[-0.065,0],1],["Level0",[-0.25,0],1]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\Level0,
                    "Level0": {
                        "type": "line",
                        "width": 2,
                        "points": []
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM5,
                    "LevelM5": {
                        "type": "line",
                        "points": [["LevelM5",[-0.175,-0.02],1],["LevelM5",[-0.175,0],1],[],["LevelM5",[-0.16,"-0.001*1"],1],["LevelM5",[-0.145,"-0.001*2"],1],[],["LevelM5",[-0.13,"-0.001*3"],1],["LevelM5",[-0.115,"-0.001*4"],1],[],["LevelM5",[-0.1,"-0.001*5"],1],["LevelM5",[-0.085,"-0.001*6"],1],[],["LevelM5",[-0.07,"-0.001*7"],1],["LevelM5",[-0.055,"-0.001*8"],1],[],["LevelM5",[-0.04,"-0.001*9"],1],[],["LevelM5",[0.175,-0.02],1],["LevelM5",[0.175,0],1],[],["LevelM5",[0.16,"-0.001*1"],1],["LevelM5",[0.145,"-0.001*2"],1],[],["LevelM5",[0.13,"-0.001*3"],1],["LevelM5",[0.115,"-0.001*4"],1],[],["LevelM5",[0.1,"-0.001*5"],1],["LevelM5",[0.085,"-0.001*6"],1],[],["LevelM5",[0.07,"-0.001*7"],1],["LevelM5",[0.055,"-0.001*8"],1],[],["LevelM5",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_5,
                    "VALM_1_5": {
                        "type": "text",
                        "source": "static",
                        "text": -5,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM5",[-0.19,-0.032],1],
                        "right": ["LevelM5",[-0.13,-0.032],1],
                        "down": ["LevelM5",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_5_R,
                    "VALM_1_5_R": {
                        "type": "text",
                        "source": "static",
                        "text": -5,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM5",[0.19,-0.032],1],
                        "right": ["LevelM5",[0.25,-0.032],1],
                        "down": ["LevelM5",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP5,
                    "LevelP5": {
                        "type": "line",
                        "points": [["LevelP5",["-0.16-0.015",0.02],1],["LevelP5",["-0.16-0.015",0],1],["LevelP5",[-0.06,"0.001*9"],1],[],["LevelP5",[0.06,"0.001*9"],1],["LevelP5",["+0.16+0.015",0],1],["LevelP5",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_5,
                    "VALP_1_5": {
                        "type": "text",
                        "source": "static",
                        "text": "5",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP5",[-0.19,-0.017],1],
                        "right": ["LevelP5",[-0.13,-0.017],1],
                        "down": ["LevelP5",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_5_R,
                    "VALP_1_5_R": {
                        "type": "text",
                        "source": "static",
                        "text": "5",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP5",[0.19,-0.017],1],
                        "right": ["LevelP5",[0.25,-0.017],1],
                        "down": ["LevelP5",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM10,
                    "LevelM10": {
                        "type": "line",
                        "points": [["LevelM10",[-0.175,-0.02],1],["LevelM10",[-0.175,0],1],[],["LevelM10",[-0.16,"-0.001*1"],1],["LevelM10",[-0.145,"-0.001*2"],1],[],["LevelM10",[-0.13,"-0.001*3"],1],["LevelM10",[-0.115,"-0.001*4"],1],[],["LevelM10",[-0.1,"-0.001*5"],1],["LevelM10",[-0.085,"-0.001*6"],1],[],["LevelM10",[-0.07,"-0.001*7"],1],["LevelM10",[-0.055,"-0.001*8"],1],[],["LevelM10",[-0.04,"-0.001*9"],1],[],["LevelM10",[0.175,-0.02],1],["LevelM10",[0.175,0],1],[],["LevelM10",[0.16,"-0.001*1"],1],["LevelM10",[0.145,"-0.001*2"],1],[],["LevelM10",[0.13,"-0.001*3"],1],["LevelM10",[0.115,"-0.001*4"],1],[],["LevelM10",[0.1,"-0.001*5"],1],["LevelM10",[0.085,"-0.001*6"],1],[],["LevelM10",[0.07,"-0.001*7"],1],["LevelM10",[0.055,"-0.001*8"],1],[],["LevelM10",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_10,
                    "VALM_1_10": {
                        "type": "text",
                        "source": "static",
                        "text": -10,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM10",[-0.19,-0.032],1],
                        "right": ["LevelM10",[-0.13,-0.032],1],
                        "down": ["LevelM10",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_10_R,
                    "VALM_1_10_R": {
                        "type": "text",
                        "source": "static",
                        "text": -10,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM10",[0.19,-0.032],1],
                        "right": ["LevelM10",[0.25,-0.032],1],
                        "down": ["LevelM10",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP10,
                    "LevelP10": {
                        "type": "line",
                        "points": [["LevelP10",["-0.16-0.015",0.02],1],["LevelP10",["-0.16-0.015",0],1],["LevelP10",[-0.06,"0.001*9"],1],[],["LevelP10",[0.06,"0.001*9"],1],["LevelP10",["+0.16+0.015",0],1],["LevelP10",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_10,
                    "VALP_1_10": {
                        "type": "text",
                        "source": "static",
                        "text": "10",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP10",[-0.19,-0.017],1],
                        "right": ["LevelP10",[-0.13,-0.017],1],
                        "down": ["LevelP10",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_10_R,
                    "VALP_1_10_R": {
                        "type": "text",
                        "source": "static",
                        "text": "10",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP10",[0.19,-0.017],1],
                        "right": ["LevelP10",[0.25,-0.017],1],
                        "down": ["LevelP10",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM15,
                    "LevelM15": {
                        "type": "line",
                        "points": [["LevelM15",[-0.175,-0.02],1],["LevelM15",[-0.175,0],1],[],["LevelM15",[-0.16,"-0.001*1"],1],["LevelM15",[-0.145,"-0.001*2"],1],[],["LevelM15",[-0.13,"-0.001*3"],1],["LevelM15",[-0.115,"-0.001*4"],1],[],["LevelM15",[-0.1,"-0.001*5"],1],["LevelM15",[-0.085,"-0.001*6"],1],[],["LevelM15",[-0.07,"-0.001*7"],1],["LevelM15",[-0.055,"-0.001*8"],1],[],["LevelM15",[-0.04,"-0.001*9"],1],[],["LevelM15",[0.175,-0.02],1],["LevelM15",[0.175,0],1],[],["LevelM15",[0.16,"-0.001*1"],1],["LevelM15",[0.145,"-0.001*2"],1],[],["LevelM15",[0.13,"-0.001*3"],1],["LevelM15",[0.115,"-0.001*4"],1],[],["LevelM15",[0.1,"-0.001*5"],1],["LevelM15",[0.085,"-0.001*6"],1],[],["LevelM15",[0.07,"-0.001*7"],1],["LevelM15",[0.055,"-0.001*8"],1],[],["LevelM15",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_15,
                    "VALM_1_15": {
                        "type": "text",
                        "source": "static",
                        "text": -15,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM15",[-0.19,-0.032],1],
                        "right": ["LevelM15",[-0.13,-0.032],1],
                        "down": ["LevelM15",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_15_R,
                    "VALM_1_15_R": {
                        "type": "text",
                        "source": "static",
                        "text": -15,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM15",[0.19,-0.032],1],
                        "right": ["LevelM15",[0.25,-0.032],1],
                        "down": ["LevelM15",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP15,
                    "LevelP15": {
                        "type": "line",
                        "points": [["LevelP15",["-0.16-0.015",0.02],1],["LevelP15",["-0.16-0.015",0],1],["LevelP15",[-0.06,"0.001*9"],1],[],["LevelP15",[0.06,"0.001*9"],1],["LevelP15",["+0.16+0.015",0],1],["LevelP15",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_15,
                    "VALP_1_15": {
                        "type": "text",
                        "source": "static",
                        "text": "15",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP15",[-0.19,-0.017],1],
                        "right": ["LevelP15",[-0.13,-0.017],1],
                        "down": ["LevelP15",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_15_R,
                    "VALP_1_15_R": {
                        "type": "text",
                        "source": "static",
                        "text": "15",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP15",[0.19,-0.017],1],
                        "right": ["LevelP15",[0.25,-0.017],1],
                        "down": ["LevelP15",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM20,
                    "LevelM20": {
                        "type": "line",
                        "points": [["LevelM20",[-0.175,-0.02],1],["LevelM20",[-0.175,0],1],[],["LevelM20",[-0.16,"-0.001*1"],1],["LevelM20",[-0.145,"-0.001*2"],1],[],["LevelM20",[-0.13,"-0.001*3"],1],["LevelM20",[-0.115,"-0.001*4"],1],[],["LevelM20",[-0.1,"-0.001*5"],1],["LevelM20",[-0.085,"-0.001*6"],1],[],["LevelM20",[-0.07,"-0.001*7"],1],["LevelM20",[-0.055,"-0.001*8"],1],[],["LevelM20",[-0.04,"-0.001*9"],1],[],["LevelM20",[0.175,-0.02],1],["LevelM20",[0.175,0],1],[],["LevelM20",[0.16,"-0.001*1"],1],["LevelM20",[0.145,"-0.001*2"],1],[],["LevelM20",[0.13,"-0.001*3"],1],["LevelM20",[0.115,"-0.001*4"],1],[],["LevelM20",[0.1,"-0.001*5"],1],["LevelM20",[0.085,"-0.001*6"],1],[],["LevelM20",[0.07,"-0.001*7"],1],["LevelM20",[0.055,"-0.001*8"],1],[],["LevelM20",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_20,
                    "VALM_1_20": {
                        "type": "text",
                        "source": "static",
                        "text": -20,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM20",[-0.19,-0.032],1],
                        "right": ["LevelM20",[-0.13,-0.032],1],
                        "down": ["LevelM20",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_20_R,
                    "VALM_1_20_R": {
                        "type": "text",
                        "source": "static",
                        "text": -20,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM20",[0.19,-0.032],1],
                        "right": ["LevelM20",[0.25,-0.032],1],
                        "down": ["LevelM20",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP20,
                    "LevelP20": {
                        "type": "line",
                        "points": [["LevelP20",["-0.16-0.015",0.02],1],["LevelP20",["-0.16-0.015",0],1],["LevelP20",[-0.06,"0.001*9"],1],[],["LevelP20",[0.06,"0.001*9"],1],["LevelP20",["+0.16+0.015",0],1],["LevelP20",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_20,
                    "VALP_1_20": {
                        "type": "text",
                        "source": "static",
                        "text": "20",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP20",[-0.19,-0.017],1],
                        "right": ["LevelP20",[-0.13,-0.017],1],
                        "down": ["LevelP20",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_20_R,
                    "VALP_1_20_R": {
                        "type": "text",
                        "source": "static",
                        "text": "20",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP20",[0.19,-0.017],1],
                        "right": ["LevelP20",[0.25,-0.017],1],
                        "down": ["LevelP20",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM25,
                    "LevelM25": {
                        "type": "line",
                        "points": [["LevelM25",[-0.175,-0.02],1],["LevelM25",[-0.175,0],1],[],["LevelM25",[-0.16,"-0.001*1"],1],["LevelM25",[-0.145,"-0.001*2"],1],[],["LevelM25",[-0.13,"-0.001*3"],1],["LevelM25",[-0.115,"-0.001*4"],1],[],["LevelM25",[-0.1,"-0.001*5"],1],["LevelM25",[-0.085,"-0.001*6"],1],[],["LevelM25",[-0.07,"-0.001*7"],1],["LevelM25",[-0.055,"-0.001*8"],1],[],["LevelM25",[-0.04,"-0.001*9"],1],[],["LevelM25",[0.175,-0.02],1],["LevelM25",[0.175,0],1],[],["LevelM25",[0.16,"-0.001*1"],1],["LevelM25",[0.145,"-0.001*2"],1],[],["LevelM25",[0.13,"-0.001*3"],1],["LevelM25",[0.115,"-0.001*4"],1],[],["LevelM25",[0.1,"-0.001*5"],1],["LevelM25",[0.085,"-0.001*6"],1],[],["LevelM25",[0.07,"-0.001*7"],1],["LevelM25",[0.055,"-0.001*8"],1],[],["LevelM25",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_25,
                    "VALM_1_25": {
                        "type": "text",
                        "source": "static",
                        "text": -25,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM25",[-0.19,-0.032],1],
                        "right": ["LevelM25",[-0.13,-0.032],1],
                        "down": ["LevelM25",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_25_R,
                    "VALM_1_25_R": {
                        "type": "text",
                        "source": "static",
                        "text": -25,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM25",[0.19,-0.032],1],
                        "right": ["LevelM25",[0.25,-0.032],1],
                        "down": ["LevelM25",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP25,
                    "LevelP25": {
                        "type": "line",
                        "points": [["LevelP25",["-0.16-0.015",0.02],1],["LevelP25",["-0.16-0.015",0],1],["LevelP25",[-0.06,"0.001*9"],1],[],["LevelP25",[0.06,"0.001*9"],1],["LevelP25",["+0.16+0.015",0],1],["LevelP25",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_25,
                    "VALP_1_25": {
                        "type": "text",
                        "source": "static",
                        "text": "25",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP25",[-0.19,-0.017],1],
                        "right": ["LevelP25",[-0.13,-0.017],1],
                        "down": ["LevelP25",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_25_R,
                    "VALP_1_25_R": {
                        "type": "text",
                        "source": "static",
                        "text": "25",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP25",[0.19,-0.017],1],
                        "right": ["LevelP25",[0.25,-0.017],1],
                        "down": ["LevelP25",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM30,
                    "LevelM30": {
                        "type": "line",
                        "points": [["LevelM30",[-0.175,-0.02],1],["LevelM30",[-0.175,0],1],[],["LevelM30",[-0.16,"-0.001*1"],1],["LevelM30",[-0.145,"-0.001*2"],1],[],["LevelM30",[-0.13,"-0.001*3"],1],["LevelM30",[-0.115,"-0.001*4"],1],[],["LevelM30",[-0.1,"-0.001*5"],1],["LevelM30",[-0.085,"-0.001*6"],1],[],["LevelM30",[-0.07,"-0.001*7"],1],["LevelM30",[-0.055,"-0.001*8"],1],[],["LevelM30",[-0.04,"-0.001*9"],1],[],["LevelM30",[0.175,-0.02],1],["LevelM30",[0.175,0],1],[],["LevelM30",[0.16,"-0.001*1"],1],["LevelM30",[0.145,"-0.001*2"],1],[],["LevelM30",[0.13,"-0.001*3"],1],["LevelM30",[0.115,"-0.001*4"],1],[],["LevelM30",[0.1,"-0.001*5"],1],["LevelM30",[0.085,"-0.001*6"],1],[],["LevelM30",[0.07,"-0.001*7"],1],["LevelM30",[0.055,"-0.001*8"],1],[],["LevelM30",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_30,
                    "VALM_1_30": {
                        "type": "text",
                        "source": "static",
                        "text": -30,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM30",[-0.19,-0.032],1],
                        "right": ["LevelM30",[-0.13,-0.032],1],
                        "down": ["LevelM30",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_30_R,
                    "VALM_1_30_R": {
                        "type": "text",
                        "source": "static",
                        "text": -30,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM30",[0.19,-0.032],1],
                        "right": ["LevelM30",[0.25,-0.032],1],
                        "down": ["LevelM30",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP30,
                    "LevelP30": {
                        "type": "line",
                        "points": [["LevelP30",["-0.16-0.015",0.02],1],["LevelP30",["-0.16-0.015",0],1],["LevelP30",[-0.06,"0.001*9"],1],[],["LevelP30",[0.06,"0.001*9"],1],["LevelP30",["+0.16+0.015",0],1],["LevelP30",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_30,
                    "VALP_1_30": {
                        "type": "text",
                        "source": "static",
                        "text": "30",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP30",[-0.19,-0.017],1],
                        "right": ["LevelP30",[-0.13,-0.017],1],
                        "down": ["LevelP30",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_30_R,
                    "VALP_1_30_R": {
                        "type": "text",
                        "source": "static",
                        "text": "30",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP30",[0.19,-0.017],1],
                        "right": ["LevelP30",[0.25,-0.017],1],
                        "down": ["LevelP30",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM35,
                    "LevelM35": {
                        "type": "line",
                        "points": [["LevelM35",[-0.175,-0.02],1],["LevelM35",[-0.175,0],1],[],["LevelM35",[-0.16,"-0.001*1"],1],["LevelM35",[-0.145,"-0.001*2"],1],[],["LevelM35",[-0.13,"-0.001*3"],1],["LevelM35",[-0.115,"-0.001*4"],1],[],["LevelM35",[-0.1,"-0.001*5"],1],["LevelM35",[-0.085,"-0.001*6"],1],[],["LevelM35",[-0.07,"-0.001*7"],1],["LevelM35",[-0.055,"-0.001*8"],1],[],["LevelM35",[-0.04,"-0.001*9"],1],[],["LevelM35",[0.175,-0.02],1],["LevelM35",[0.175,0],1],[],["LevelM35",[0.16,"-0.001*1"],1],["LevelM35",[0.145,"-0.001*2"],1],[],["LevelM35",[0.13,"-0.001*3"],1],["LevelM35",[0.115,"-0.001*4"],1],[],["LevelM35",[0.1,"-0.001*5"],1],["LevelM35",[0.085,"-0.001*6"],1],[],["LevelM35",[0.07,"-0.001*7"],1],["LevelM35",[0.055,"-0.001*8"],1],[],["LevelM35",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_35,
                    "VALM_1_35": {
                        "type": "text",
                        "source": "static",
                        "text": -35,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM35",[-0.19,-0.032],1],
                        "right": ["LevelM35",[-0.13,-0.032],1],
                        "down": ["LevelM35",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_35_R,
                    "VALM_1_35_R": {
                        "type": "text",
                        "source": "static",
                        "text": -35,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM35",[0.19,-0.032],1],
                        "right": ["LevelM35",[0.25,-0.032],1],
                        "down": ["LevelM35",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP35,
                    "LevelP35": {
                        "type": "line",
                        "points": [["LevelP35",["-0.16-0.015",0.02],1],["LevelP35",["-0.16-0.015",0],1],["LevelP35",[-0.06,"0.001*9"],1],[],["LevelP35",[0.06,"0.001*9"],1],["LevelP35",["+0.16+0.015",0],1],["LevelP35",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_35,
                    "VALP_1_35": {
                        "type": "text",
                        "source": "static",
                        "text": "35",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP35",[-0.19,-0.017],1],
                        "right": ["LevelP35",[-0.13,-0.017],1],
                        "down": ["LevelP35",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_35_R,
                    "VALP_1_35_R": {
                        "type": "text",
                        "source": "static",
                        "text": "35",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP35",[0.19,-0.017],1],
                        "right": ["LevelP35",[0.25,-0.017],1],
                        "down": ["LevelP35",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM40,
                    "LevelM40": {
                        "type": "line",
                        "points": [["LevelM40",[-0.175,-0.02],1],["LevelM40",[-0.175,0],1],[],["LevelM40",[-0.16,"-0.001*1"],1],["LevelM40",[-0.145,"-0.001*2"],1],[],["LevelM40",[-0.13,"-0.001*3"],1],["LevelM40",[-0.115,"-0.001*4"],1],[],["LevelM40",[-0.1,"-0.001*5"],1],["LevelM40",[-0.085,"-0.001*6"],1],[],["LevelM40",[-0.07,"-0.001*7"],1],["LevelM40",[-0.055,"-0.001*8"],1],[],["LevelM40",[-0.04,"-0.001*9"],1],[],["LevelM40",[0.175,-0.02],1],["LevelM40",[0.175,0],1],[],["LevelM40",[0.16,"-0.001*1"],1],["LevelM40",[0.145,"-0.001*2"],1],[],["LevelM40",[0.13,"-0.001*3"],1],["LevelM40",[0.115,"-0.001*4"],1],[],["LevelM40",[0.1,"-0.001*5"],1],["LevelM40",[0.085,"-0.001*6"],1],[],["LevelM40",[0.07,"-0.001*7"],1],["LevelM40",[0.055,"-0.001*8"],1],[],["LevelM40",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_40,
                    "VALM_1_40": {
                        "type": "text",
                        "source": "static",
                        "text": -40,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM40",[-0.19,-0.032],1],
                        "right": ["LevelM40",[-0.13,-0.032],1],
                        "down": ["LevelM40",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_40_R,
                    "VALM_1_40_R": {
                        "type": "text",
                        "source": "static",
                        "text": -40,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM40",[0.19,-0.032],1],
                        "right": ["LevelM40",[0.25,-0.032],1],
                        "down": ["LevelM40",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP40,
                    "LevelP40": {
                        "type": "line",
                        "points": [["LevelP40",["-0.16-0.015",0.02],1],["LevelP40",["-0.16-0.015",0],1],["LevelP40",[-0.06,"0.001*9"],1],[],["LevelP40",[0.06,"0.001*9"],1],["LevelP40",["+0.16+0.015",0],1],["LevelP40",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_40,
                    "VALP_1_40": {
                        "type": "text",
                        "source": "static",
                        "text": "40",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP40",[-0.19,-0.017],1],
                        "right": ["LevelP40",[-0.13,-0.017],1],
                        "down": ["LevelP40",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_40_R,
                    "VALP_1_40_R": {
                        "type": "text",
                        "source": "static",
                        "text": "40",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP40",[0.19,-0.017],1],
                        "right": ["LevelP40",[0.25,-0.017],1],
                        "down": ["LevelP40",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM45,
                    "LevelM45": {
                        "type": "line",
                        "points": [["LevelM45",[-0.175,-0.02],1],["LevelM45",[-0.175,0],1],[],["LevelM45",[-0.16,"-0.001*1"],1],["LevelM45",[-0.145,"-0.001*2"],1],[],["LevelM45",[-0.13,"-0.001*3"],1],["LevelM45",[-0.115,"-0.001*4"],1],[],["LevelM45",[-0.1,"-0.001*5"],1],["LevelM45",[-0.085,"-0.001*6"],1],[],["LevelM45",[-0.07,"-0.001*7"],1],["LevelM45",[-0.055,"-0.001*8"],1],[],["LevelM45",[-0.04,"-0.001*9"],1],[],["LevelM45",[0.175,-0.02],1],["LevelM45",[0.175,0],1],[],["LevelM45",[0.16,"-0.001*1"],1],["LevelM45",[0.145,"-0.001*2"],1],[],["LevelM45",[0.13,"-0.001*3"],1],["LevelM45",[0.115,"-0.001*4"],1],[],["LevelM45",[0.1,"-0.001*5"],1],["LevelM45",[0.085,"-0.001*6"],1],[],["LevelM45",[0.07,"-0.001*7"],1],["LevelM45",[0.055,"-0.001*8"],1],[],["LevelM45",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_45,
                    "VALM_1_45": {
                        "type": "text",
                        "source": "static",
                        "text": -45,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM45",[-0.19,-0.032],1],
                        "right": ["LevelM45",[-0.13,-0.032],1],
                        "down": ["LevelM45",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_45_R,
                    "VALM_1_45_R": {
                        "type": "text",
                        "source": "static",
                        "text": -45,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM45",[0.19,-0.032],1],
                        "right": ["LevelM45",[0.25,-0.032],1],
                        "down": ["LevelM45",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP45,
                    "LevelP45": {
                        "type": "line",
                        "points": [["LevelP45",["-0.16-0.015",0.02],1],["LevelP45",["-0.16-0.015",0],1],["LevelP45",[-0.06,"0.001*9"],1],[],["LevelP45",[0.06,"0.001*9"],1],["LevelP45",["+0.16+0.015",0],1],["LevelP45",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_45,
                    "VALP_1_45": {
                        "type": "text",
                        "source": "static",
                        "text": "45",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP45",[-0.19,-0.017],1],
                        "right": ["LevelP45",[-0.13,-0.017],1],
                        "down": ["LevelP45",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_45_R,
                    "VALP_1_45_R": {
                        "type": "text",
                        "source": "static",
                        "text": "45",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP45",[0.19,-0.017],1],
                        "right": ["LevelP45",[0.25,-0.017],1],
                        "down": ["LevelP45",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM50,
                    "LevelM50": {
                        "type": "line",
                        "points": [["LevelM50",[-0.175,-0.02],1],["LevelM50",[-0.175,0],1],[],["LevelM50",[-0.16,"-0.001*1"],1],["LevelM50",[-0.145,"-0.001*2"],1],[],["LevelM50",[-0.13,"-0.001*3"],1],["LevelM50",[-0.115,"-0.001*4"],1],[],["LevelM50",[-0.1,"-0.001*5"],1],["LevelM50",[-0.085,"-0.001*6"],1],[],["LevelM50",[-0.07,"-0.001*7"],1],["LevelM50",[-0.055,"-0.001*8"],1],[],["LevelM50",[-0.04,"-0.001*9"],1],[],["LevelM50",[0.175,-0.02],1],["LevelM50",[0.175,0],1],[],["LevelM50",[0.16,"-0.001*1"],1],["LevelM50",[0.145,"-0.001*2"],1],[],["LevelM50",[0.13,"-0.001*3"],1],["LevelM50",[0.115,"-0.001*4"],1],[],["LevelM50",[0.1,"-0.001*5"],1],["LevelM50",[0.085,"-0.001*6"],1],[],["LevelM50",[0.07,"-0.001*7"],1],["LevelM50",[0.055,"-0.001*8"],1],[],["LevelM50",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_50,
                    "VALM_1_50": {
                        "type": "text",
                        "source": "static",
                        "text": -50,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM50",[-0.19,-0.032],1],
                        "right": ["LevelM50",[-0.13,-0.032],1],
                        "down": ["LevelM50",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_50_R,
                    "VALM_1_50_R": {
                        "type": "text",
                        "source": "static",
                        "text": -50,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM50",[0.19,-0.032],1],
                        "right": ["LevelM50",[0.25,-0.032],1],
                        "down": ["LevelM50",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP50,
                    "LevelP50": {
                        "type": "line",
                        "points": [["LevelP50",["-0.16-0.015",0.02],1],["LevelP50",["-0.16-0.015",0],1],["LevelP50",[-0.06,"0.001*9"],1],[],["LevelP50",[0.06,"0.001*9"],1],["LevelP50",["+0.16+0.015",0],1],["LevelP50",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_50,
                    "VALP_1_50": {
                        "type": "text",
                        "source": "static",
                        "text": "50",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP50",[-0.19,-0.017],1],
                        "right": ["LevelP50",[-0.13,-0.017],1],
                        "down": ["LevelP50",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_50_R,
                    "VALP_1_50_R": {
                        "type": "text",
                        "source": "static",
                        "text": "50",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP50",[0.19,-0.017],1],
                        "right": ["LevelP50",[0.25,-0.017],1],
                        "down": ["LevelP50",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM60,
                    "LevelM60": {
                        "type": "line",
                        "points": [["LevelM60",[-0.175,-0.02],1],["LevelM60",[-0.175,0],1],[],["LevelM60",[-0.16,"-0.001*1"],1],["LevelM60",[-0.145,"-0.001*2"],1],[],["LevelM60",[-0.13,"-0.001*3"],1],["LevelM60",[-0.115,"-0.001*4"],1],[],["LevelM60",[-0.1,"-0.001*5"],1],["LevelM60",[-0.085,"-0.001*6"],1],[],["LevelM60",[-0.07,"-0.001*7"],1],["LevelM60",[-0.055,"-0.001*8"],1],[],["LevelM60",[-0.04,"-0.001*9"],1],[],["LevelM60",[0.175,-0.02],1],["LevelM60",[0.175,0],1],[],["LevelM60",[0.16,"-0.001*1"],1],["LevelM60",[0.145,"-0.001*2"],1],[],["LevelM60",[0.13,"-0.001*3"],1],["LevelM60",[0.115,"-0.001*4"],1],[],["LevelM60",[0.1,"-0.001*5"],1],["LevelM60",[0.085,"-0.001*6"],1],[],["LevelM60",[0.07,"-0.001*7"],1],["LevelM60",[0.055,"-0.001*8"],1],[],["LevelM60",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_60,
                    "VALM_1_60": {
                        "type": "text",
                        "source": "static",
                        "text": -60,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM60",[-0.19,-0.032],1],
                        "right": ["LevelM60",[-0.13,-0.032],1],
                        "down": ["LevelM60",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_60_R,
                    "VALM_1_60_R": {
                        "type": "text",
                        "source": "static",
                        "text": -60,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM60",[0.19,-0.032],1],
                        "right": ["LevelM60",[0.25,-0.032],1],
                        "down": ["LevelM60",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP60,
                    "LevelP60": {
                        "type": "line",
                        "points": [["LevelP60",["-0.16-0.015",0.02],1],["LevelP60",["-0.16-0.015",0],1],["LevelP60",[-0.06,"0.001*9"],1],[],["LevelP60",[0.06,"0.001*9"],1],["LevelP60",["+0.16+0.015",0],1],["LevelP60",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_60,
                    "VALP_1_60": {
                        "type": "text",
                        "source": "static",
                        "text": "60",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP60",[-0.19,-0.017],1],
                        "right": ["LevelP60",[-0.13,-0.017],1],
                        "down": ["LevelP60",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_60_R,
                    "VALP_1_60_R": {
                        "type": "text",
                        "source": "static",
                        "text": "60",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP60",[0.19,-0.017],1],
                        "right": ["LevelP60",[0.25,-0.017],1],
                        "down": ["LevelP60",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM70,
                    "LevelM70": {
                        "type": "line",
                        "points": [["LevelM70",[-0.175,-0.02],1],["LevelM70",[-0.175,0],1],[],["LevelM70",[-0.16,"-0.001*1"],1],["LevelM70",[-0.145,"-0.001*2"],1],[],["LevelM70",[-0.13,"-0.001*3"],1],["LevelM70",[-0.115,"-0.001*4"],1],[],["LevelM70",[-0.1,"-0.001*5"],1],["LevelM70",[-0.085,"-0.001*6"],1],[],["LevelM70",[-0.07,"-0.001*7"],1],["LevelM70",[-0.055,"-0.001*8"],1],[],["LevelM70",[-0.04,"-0.001*9"],1],[],["LevelM70",[0.175,-0.02],1],["LevelM70",[0.175,0],1],[],["LevelM70",[0.16,"-0.001*1"],1],["LevelM70",[0.145,"-0.001*2"],1],[],["LevelM70",[0.13,"-0.001*3"],1],["LevelM70",[0.115,"-0.001*4"],1],[],["LevelM70",[0.1,"-0.001*5"],1],["LevelM70",[0.085,"-0.001*6"],1],[],["LevelM70",[0.07,"-0.001*7"],1],["LevelM70",[0.055,"-0.001*8"],1],[],["LevelM70",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_70,
                    "VALM_1_70": {
                        "type": "text",
                        "source": "static",
                        "text": -70,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM70",[-0.19,-0.032],1],
                        "right": ["LevelM70",[-0.13,-0.032],1],
                        "down": ["LevelM70",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_70_R,
                    "VALM_1_70_R": {
                        "type": "text",
                        "source": "static",
                        "text": -70,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM70",[0.19,-0.032],1],
                        "right": ["LevelM70",[0.25,-0.032],1],
                        "down": ["LevelM70",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP70,
                    "LevelP70": {
                        "type": "line",
                        "points": [["LevelP70",["-0.16-0.015",0.02],1],["LevelP70",["-0.16-0.015",0],1],["LevelP70",[-0.06,"0.001*9"],1],[],["LevelP70",[0.06,"0.001*9"],1],["LevelP70",["+0.16+0.015",0],1],["LevelP70",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_70,
                    "VALP_1_70": {
                        "type": "text",
                        "source": "static",
                        "text": "70",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP70",[-0.19,-0.017],1],
                        "right": ["LevelP70",[-0.13,-0.017],1],
                        "down": ["LevelP70",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_70_R,
                    "VALP_1_70_R": {
                        "type": "text",
                        "source": "static",
                        "text": "70",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP70",[0.19,-0.017],1],
                        "right": ["LevelP70",[0.25,-0.017],1],
                        "down": ["LevelP70",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM80,
                    "LevelM80": {
                        "type": "line",
                        "points": [["LevelM80",[-0.175,-0.02],1],["LevelM80",[-0.175,0],1],[],["LevelM80",[-0.16,"-0.001*1"],1],["LevelM80",[-0.145,"-0.001*2"],1],[],["LevelM80",[-0.13,"-0.001*3"],1],["LevelM80",[-0.115,"-0.001*4"],1],[],["LevelM80",[-0.1,"-0.001*5"],1],["LevelM80",[-0.085,"-0.001*6"],1],[],["LevelM80",[-0.07,"-0.001*7"],1],["LevelM80",[-0.055,"-0.001*8"],1],[],["LevelM80",[-0.04,"-0.001*9"],1],[],["LevelM80",[0.175,-0.02],1],["LevelM80",[0.175,0],1],[],["LevelM80",[0.16,"-0.001*1"],1],["LevelM80",[0.145,"-0.001*2"],1],[],["LevelM80",[0.13,"-0.001*3"],1],["LevelM80",[0.115,"-0.001*4"],1],[],["LevelM80",[0.1,"-0.001*5"],1],["LevelM80",[0.085,"-0.001*6"],1],[],["LevelM80",[0.07,"-0.001*7"],1],["LevelM80",[0.055,"-0.001*8"],1],[],["LevelM80",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_80,
                    "VALM_1_80": {
                        "type": "text",
                        "source": "static",
                        "text": -80,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM80",[-0.19,-0.032],1],
                        "right": ["LevelM80",[-0.13,-0.032],1],
                        "down": ["LevelM80",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_80_R,
                    "VALM_1_80_R": {
                        "type": "text",
                        "source": "static",
                        "text": -80,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM80",[0.19,-0.032],1],
                        "right": ["LevelM80",[0.25,-0.032],1],
                        "down": ["LevelM80",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP80,
                    "LevelP80": {
                        "type": "line",
                        "points": [["LevelP80",["-0.16-0.015",0.02],1],["LevelP80",["-0.16-0.015",0],1],["LevelP80",[-0.06,"0.001*9"],1],[],["LevelP80",[0.06,"0.001*9"],1],["LevelP80",["+0.16+0.015",0],1],["LevelP80",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_80,
                    "VALP_1_80": {
                        "type": "text",
                        "source": "static",
                        "text": "80",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP80",[-0.19,-0.017],1],
                        "right": ["LevelP80",[-0.13,-0.017],1],
                        "down": ["LevelP80",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_80_R,
                    "VALP_1_80_R": {
                        "type": "text",
                        "source": "static",
                        "text": "80",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP80",[0.19,-0.017],1],
                        "right": ["LevelP80",[0.25,-0.017],1],
                        "down": ["LevelP80",[0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelM90,
                    "LevelM90": {
                        "type": "line",
                        "points": [["LevelM90",[-0.175,-0.02],1],["LevelM90",[-0.175,0],1],[],["LevelM90",[-0.16,"-0.001*1"],1],["LevelM90",[-0.145,"-0.001*2"],1],[],["LevelM90",[-0.13,"-0.001*3"],1],["LevelM90",[-0.115,"-0.001*4"],1],[],["LevelM90",[-0.1,"-0.001*5"],1],["LevelM90",[-0.085,"-0.001*6"],1],[],["LevelM90",[-0.07,"-0.001*7"],1],["LevelM90",[-0.055,"-0.001*8"],1],[],["LevelM90",[-0.04,"-0.001*9"],1],[],["LevelM90",[0.175,-0.02],1],["LevelM90",[0.175,0],1],[],["LevelM90",[0.16,"-0.001*1"],1],["LevelM90",[0.145,"-0.001*2"],1],[],["LevelM90",[0.13,"-0.001*3"],1],["LevelM90",[0.115,"-0.001*4"],1],[],["LevelM90",[0.1,"-0.001*5"],1],["LevelM90",[0.085,"-0.001*6"],1],[],["LevelM90",[0.07,"-0.001*7"],1],["LevelM90",[0.055,"-0.001*8"],1],[],["LevelM90",[0.04,"-0.001*9"],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_90,
                    "VALM_1_90": {
                        "type": "text",
                        "source": "static",
                        "text": -90,
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM90",[-0.19,-0.032],1],
                        "right": ["LevelM90",[-0.13,-0.032],1],
                        "down": ["LevelM90",[-0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALM_1_90_R,
                    "VALM_1_90_R": {
                        "type": "text",
                        "source": "static",
                        "text": -90,
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelM90",[0.19,-0.032],1],
                        "right": ["LevelM90",[0.25,-0.032],1],
                        "down": ["LevelM90",[0.19,0.018],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\LevelP90,
                    "LevelP90": {
                        "type": "line",
                        "points": [["LevelP90",["-0.16-0.015",0.02],1],["LevelP90",["-0.16-0.015",0],1],["LevelP90",[-0.06,"0.001*9"],1],[],["LevelP90",[0.06,"0.001*9"],1],["LevelP90",["+0.16+0.015",0],1],["LevelP90",["+0.16+0.015",0.02],1]],
                        "width": 2
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_90,
                    "VALP_1_90": {
                        "type": "text",
                        "source": "static",
                        "text": "90",
                        "align": "left",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP90",[-0.19,-0.017],1],
                        "right": ["LevelP90",[-0.13,-0.017],1],
                        "down": ["LevelP90",[-0.19,0.033],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\Horizont\VALP_1_90_R,
                    "VALP_1_90_R": {
                        "type": "text",
                        "source": "static",
                        "text": "90",
                        "align": "right",
                        "scale": 1,
                        "sourceScale": 1,
                        "pos": ["LevelP90",[0.19,-0.017],1],
                        "right": ["LevelP90",[0.25,-0.017],1],
                        "down": ["LevelP90",[0.19,0.033],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\SpeedNumber,
                "SpeedNumber": {
                    "type": "text",
                    "source": "speed",
                    "sourceScale": 3.6,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.1,0.424107],1],
                    "right": [[0.16,0.424107],1],
                    "down": [[0.1,0.46875],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AltNumber,
                "AltNumber": {
                    "source": "altitudeASL",
                    "sourceScale": 1,
                    "pos": [[0.9,0.424107],1],
                    "right": [[0.96,0.424107],1],
                    "down": [[0.9,0.46875],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\MachText,
                "MachText": {
                    "type": "text",
                    "source": "static",
                    "align": "left",
                    "text": "M",
                    "scale": 1,
                    "pos": [[0.1,0.63],1],
                    "right": [[0.15,0.63],1],
                    "down": [[0.1,0.68],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\MachNumber,
                "MachNumber": {
                    "type": "text",
                    "source": "speed",
                    "sourceScale": 0.002939,
                    "sourcePrecision": 2,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.12,0.63],1],
                    "right": [[0.17,0.63],1],
                    "down": [[0.12,0.68],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\GmeterText,
                "GmeterText": {
                    "type": "text",
                    "source": "static",
                    "align": "left",
                    "text": "G",
                    "scale": 1,
                    "pos": [[0.1,0.7],1],
                    "right": [[0.15,0.7],1],
                    "down": [[0.1,0.75],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\GmeterNumber,
                "GmeterNumber": {
                    "type": "text",
                    "source": "gmeter",
                    "sourceScale": 0.3,
                    "sourcePrecision": 1,
                    "refreshRate": 0.4,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.12,0.7],1],
                    "right": [[0.17,0.7],1],
                    "down": [[0.12,0.75],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\PitchNumber,
                "PitchNumber": {
                    "type": "text",
                    "source": "aoa",
                    "sourceScale": 57.2958,
                    "sourcePrecision": 1,
                    "refreshRate": 0.4,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.12,0.74],1],
                    "right": [[0.17,0.74],1],
                    "down": [[0.12,0.79],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarATLText,
                "RadarATLText": {
                    "type": "text",
                    "source": "static",
                    "align": "left",
                    "text": "R",
                    "scale": 1,
                    "pos": [[0.85,0.55],1],
                    "right": [[0.9,0.55],1],
                    "down": [[0.85,0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarATLNumber,
                "RadarATLNumber": {
                    "type": "text",
                    "source": "altitudeAGL",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "sourceOffset": -2,
                    "sourcePrecision": 0,
                    "refreshRate": 0.01,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.87,0.55],1],
                    "right": [[0.92,0.55],1],
                    "down": [[0.87,0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\HeadingNumber,
                "HeadingNumber": {
                    "type": "text",
                    "source": "heading",
                    "sourceScale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.5,0.14],1],
                    "right": [[0.57,0.14],1],
                    "down": [[0.5,0.21],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\HeadingArrows,
                "HeadingArrows": {
                    "type": "line",
                    "width": 3,
                    "points": [[[0.45,0.2],1],[[0.55,0.2],1],[[0.55,0.157143],1],[[0.45,0.157143],1],[[0.45,0.2],1],[],["WPPoint",1,"LimitWaypoint",1,[-0.011,0.13],1],["WPPoint",1,"LimitWaypoint",1,[-0.011,0.152],1],[],["WPPoint",1,"LimitWaypoint",1,[0.011,0.13],1],["WPPoint",1,"LimitWaypoint",1,[0.011,0.152],1]]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\HeadingScale,
                "HeadingScale": {
                    "type": "scale",
                    "horizontal": 1,
                    "source": "heading",
                    "sourceScale": 0.1,
                    "sourceLength": 2,
                    "width": 4,
                    "top": 0.3,
                    "center": 0.5,
                    "bottom": 0.7,
                    "lineXleft": 0.22,
                    "lineYright": 0.2,
                    "lineXleftMajor": 0.23,
                    "lineYrightMajor": 0.2,
                    "majorLineEach": 2,
                    "numberEach": 0,
                    "step": 0.5,
                    "stepSize": 0.0555556,
                    "align": "center",
                    "scale": 1,
                    "pos": [0.295,0.165],
                    "right": [0.335,0.165],
                    "down": [0.295,0.205]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\HeadingScale_Left,
                "HeadingScale_Left": {
                    "clipTL": [0,0],
                    "clipBR": [0.45,1],
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\HeadingScale_Left\HeadingScale,
                    "HeadingScale": {
                        "lineXleft": 0,
                        "lineYright": 0,
                        "lineXleftMajor": 0,
                        "lineYrightMajor": 0,
                        "numberEach": 2,
                        "type": "scale",
                        "horizontal": 1,
                        "source": "heading",
                        "sourceScale": 0.1,
                        "sourceLength": 2,
                        "width": 4,
                        "top": 0.3,
                        "center": 0.5,
                        "bottom": 0.7,
                        "majorLineEach": 2,
                        "step": 0.5,
                        "stepSize": 0.0555556,
                        "align": "center",
                        "scale": 1,
                        "pos": [0.295,0.165],
                        "right": [0.335,0.165],
                        "down": [0.295,0.205]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\HeadingScale_Right,
                "HeadingScale_Right": {
                    "clipTL": [0.55,0],
                    "clipBR": [1,1],
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\HeadingScale_Right\HeadingScale,
                    "HeadingScale": {
                        "lineXleft": 0,
                        "lineYright": 0,
                        "lineXleftMajor": 0,
                        "lineYrightMajor": 0,
                        "numberEach": 2,
                        "type": "scale",
                        "horizontal": 1,
                        "source": "heading",
                        "sourceScale": 0.1,
                        "sourceLength": 2,
                        "width": 4,
                        "top": 0.3,
                        "center": 0.5,
                        "bottom": 0.7,
                        "majorLineEach": 2,
                        "step": 0.5,
                        "stepSize": 0.0555556,
                        "align": "center",
                        "scale": 1,
                        "pos": [0.295,0.165],
                        "right": [0.335,0.165],
                        "down": [0.295,0.205]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\ThrustNumber,
                "ThrustNumber": {
                    "type": "text",
                    "source": "throttle",
                    "sourceScale": 100,
                    "sourceLength": 3,
                    "sourceOffset": 0,
                    "sourcePrecision": 0,
                    "refreshRate": 0.01,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.15,0.89],1],
                    "right": [[0.2,0.89],1],
                    "down": [[0.15,0.94],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\NavigationMode,
                "NavigationMode": {
                    "condition": "1-(AAmissile+mgun+bomb)",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\NavigationMode\ModeText,
                    "ModeText": {
                        "type": "text",
                        "source": "static",
                        "align": "left",
                        "text": "NAV",
                        "scale": 1,
                        "pos": [[0.15,0.85],1],
                        "right": [[0.2,0.85],1],
                        "down": [[0.15,0.9],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\NavigationMode\WP,
                    "WP": {
                        "condition": "wpvalid",
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\NavigationMode\WP\WPdist,
                        "WPdist": {
                            "type": "text",
                            "source": "wpdist",
                            "sourceScale": 0.001,
                            "sourcePrecision": 1,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.795,0.82],1],
                            "right": [[0.855,0.82],1],
                            "down": [[0.795,0.88],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\NavigationMode\WP\WPIndex,
                        "WPIndex": {
                            "type": "text",
                            "source": "wpIndex",
                            "sourceScale": 1,
                            "sourceLength": 2,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.725,0.82],1],
                            "right": [[0.785,0.82],1],
                            "down": [[0.725,0.88],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\NavigationMode\WP\WPstatic,
                        "WPstatic": {
                            "type": "text",
                            "source": "static",
                            "text": "/",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "right",
                            "pos": [[0.765,0.82],1],
                            "right": [[0.825,0.82],1],
                            "down": [[0.765,0.88],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\NavigationMode\WP\WPTime,
                        "WPTime": {
                            "type": "text",
                            "source": "static",
                            "text": ":14:36/-00:0",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "right",
                            "pos": [[0.725,0.865],1],
                            "right": [[0.785,0.865],1],
                            "down": [[0.725,0.925],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\NavigationMode\WP\WPCurrentTime,
                        "WPCurrentTime": {
                            "source": "time",
                            "text": "%X",
                            "align": "right",
                            "pos": [[0.725,0.91],1],
                            "right": [[0.785,0.91],1],
                            "down": [[0.725,0.97],1],
                            "type": "text",
                            "sourceScale": 0.001,
                            "sourcePrecision": 1,
                            "scale": 1
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\NavigationMode\WP\WP,
                        "WP": {
                            "width": 1,
                            "type": "line",
                            "points": [["wppoint",[0,-0.00892857],1],["wppoint",[0.005,-0.00773214],1],["wppoint",[0.00866,-0.00446429],1],["wppoint",[0.01,0],1],["wppoint",[0.00866,0.00446429],1],["wppoint",[0.005,0.00773214],1],["wppoint",[0,0.00892857],1],["wppoint",[-0.005,0.00773214],1],["wppoint",[-0.00866,0.00446429],1],["wppoint",[-0.01,0],1],["wppoint",[-0.00866,-0.00446429],1],["wppoint",[-0.005,-0.00773214],1],["wppoint",[0,-0.00892857],1],[],["wppoint",1,["HorizonBankRotFull",0,-0.01],1],["wppoint",1,["HorizonBankRotFull",0,-0.023],1]]
                        }
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AAMissileCrosshairGroup,
                "AAMissileCrosshairGroup": {
                    "type": "group",
                    "condition": "AAmissile",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AAMissileCrosshairGroup\ModeText,
                    "ModeText": {
                        "type": "text",
                        "source": "static",
                        "align": "left",
                        "text": "MSL",
                        "scale": 1,
                        "pos": [[0.15,0.85],1],
                        "right": [[0.2,0.85],1],
                        "down": [[0.15,0.9],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AAMissileCrosshairGroup\AAMissileCrosshair,
                    "AAMissileCrosshair": {
                        "type": "line",
                        "width": 4,
                        "points": [["PlaneW",[0,-0.25],1],["PlaneW",[0.048608,-0.2462],1],["PlaneW",[0.09576,-0.234925],1],["PlaneW",[0.14,-0.2165],1],[],["PlaneW",[0.179984,-0.1915],1],["PlaneW",[0.21448,-0.1607],1],["PlaneW",[0.24248,-0.125],1],["PlaneW",[0.263116,-0.0855],1],[],["PlaneW",[0.275744,-0.0434],1],["PlaneW",[0.28,0],1],["PlaneW",[0.275744,0.0434],1],["PlaneW",[0.263116,0.0855],1],[],["PlaneW",[0.24248,0.125],1],["PlaneW",[0.21448,0.1607],1],["PlaneW",[0.179984,0.1915],1],["PlaneW",[0.14,0.2165],1],[],["PlaneW",[0.09576,0.234925],1],["PlaneW",[0.048608,0.2462],1],["PlaneW",[0,0.25],1],["PlaneW",[-0.048608,0.2462],1],[],["PlaneW",[-0.09576,0.234925],1],["PlaneW",[-0.14,0.2165],1],["PlaneW",[-0.179984,0.1915],1],["PlaneW",[-0.21448,0.1607],1],[],["PlaneW",[-0.24248,0.125],1],["PlaneW",[-0.263116,0.0855],1],["PlaneW",[-0.275744,0.0434],1],["PlaneW",[-0.28,0],1],[],["PlaneW",[-0.275744,-0.0434],1],["PlaneW",[-0.263116,-0.0855],1],["PlaneW",[-0.24248,-0.125],1],["PlaneW",[-0.21448,-0.1607],1],[],["PlaneW",[-0.179984,-0.1915],1],["PlaneW",[-0.14,-0.2165],1],["PlaneW",[-0.09576,-0.234925],1],["PlaneW",[-0.048608,-0.2462],1],[],["PlaneW",[0,-0.25],1]]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AAMissileCrosshairGroup\AmmoCount,
                    "AmmoCount": {
                        "type": "text",
                        "source": "ammoFormat",
                        "sourceScale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.74,0.9],1],
                        "right": [[0.8,0.9],1],
                        "down": [[0.74,0.96],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AAMissileCrosshairGroup\Lines,
                    "Lines": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.87,0.18],1],[[0.85,0.18],1],[[0.85,0.34],1],[[0.87,0.34],1],[],[[0.87,0.3],1],[[0.85,0.3],1],[],[[0.87,0.26],1],[[0.85,0.26],1],[],[[0.87,0.22],1],[[0.85,0.22],1],[],["LarTargetDist",-0.16,[0.83,0.36],1],["LarTargetDist",-0.16,[0.85,0.34],1],["LarTargetDist",-0.16,[0.83,0.32],1],[]]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AAMissileCrosshairGroup\Poly,
                    "Poly": {
                        "type": "polygon",
                        "points": [[["LarAmmoMin",-0.16,[0.851,0.34],1],["LarAmmoMax",-0.16,[0.851,0.34],1],["LarAmmoMax",-0.16,[0.868,0.34],1],["LarAmmoMin",-0.16,[0.868,0.34],1]]]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AAMissileCrosshairGroup\TopText,
                    "TopText": {
                        "type": "text",
                        "source": "LarTop",
                        "sourceScale": 0.001,
                        "scale": 1,
                        "pos": [[0.88,0.16],1],
                        "right": [[0.92,0.16],1],
                        "down": [[0.88,0.2],1],
                        "align": "right"
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AAMissileCrosshairGroup\MiddleText,
                    "MiddleText": {
                        "source": "LarTop",
                        "sourcePrecision": -1,
                        "sourceScale": 0.0005,
                        "pos": [[0.88,0.24],1],
                        "right": [[0.92,0.24],1],
                        "down": [[0.88,0.28],1],
                        "type": "text",
                        "scale": 1,
                        "align": "right"
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\AAMissileCrosshairGroup\SpeedText,
                    "SpeedText": {
                        "source": "LarTargetSpeed",
                        "align": "left",
                        "sourceScale": 3.6,
                        "pos": ["LarTargetDist",-0.16,[0.82,0.32],1],
                        "right": ["LarTargetDist",-0.16,[0.86,0.32],1],
                        "down": ["LarTargetDist",-0.16,[0.82,0.36],1],
                        "type": "text",
                        "scale": 1
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\BombCrosshairGroup,
                "BombCrosshairGroup": {
                    "type": "group",
                    "condition": "bomb",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\BombCrosshairGroup\BombCrosshair,
                    "BombCrosshair": {
                        "width": 4,
                        "type": "line",
                        "points": [["ImpactPoint",[0,0.0803571],1],["ImpactPoint",[0,0.0714286],1],[],["ImpactPoint",[-0.09,0],1],["ImpactPoint",[-0.08,0],1],[],["ImpactPoint",[0.09,0],1],["ImpactPoint",[0.08,0],1],[],["ImpactPoint",[0,-0.00178571],1],["ImpactPoint",[0,0.00178571],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[],["ImpactPoint",[0,-0.0714286],1],["ImpactPoint",[0.013888,-0.0703429],1],["ImpactPoint",[0.02736,-0.0671214],1],["ImpactPoint",[0.04,-0.0618571],1],["ImpactPoint",[0.051424,-0.0547143],1],["ImpactPoint",[0.06128,-0.0459143],1],["ImpactPoint",[0.06928,-0.0357143],1],["ImpactPoint",[0.075176,-0.0244286],1],["ImpactPoint",[0.078784,-0.0124],1],["ImpactPoint",[0.08,0],1],["ImpactPoint",[0.078784,0.0124],1],["ImpactPoint",[0.075176,0.0244286],1],["ImpactPoint",[0.06928,0.0357143],1],["ImpactPoint",[0.06128,0.0459143],1],["ImpactPoint",[0.051424,0.0547143],1],["ImpactPoint",[0.04,0.0618571],1],["ImpactPoint",[0.02736,0.0671214],1],["ImpactPoint",[0.013888,0.0703429],1],["ImpactPoint",[0,0.0714286],1],["ImpactPoint",[-0.013888,0.0703429],1],["ImpactPoint",[-0.02736,0.0671214],1],["ImpactPoint",[-0.04,0.0618571],1],["ImpactPoint",[-0.051424,0.0547143],1],["ImpactPoint",[-0.06128,0.0459143],1],["ImpactPoint",[-0.06928,0.0357143],1],["ImpactPoint",[-0.075176,0.0244286],1],["ImpactPoint",[-0.078784,0.0124],1],["ImpactPoint",[-0.08,0],1],["ImpactPoint",[-0.078784,-0.0124],1],["ImpactPoint",[-0.075176,-0.0244286],1],["ImpactPoint",[-0.06928,-0.0357143],1],["ImpactPoint",[-0.06128,-0.0459143],1],["ImpactPoint",[-0.051424,-0.0547143],1],["ImpactPoint",[-0.04,-0.0618571],1],["ImpactPoint",[-0.02736,-0.0671214],1],["ImpactPoint",[-0.013888,-0.0703429],1],["ImpactPoint",[0,-0.0714286],1],[],[],["ImpactPoint",-1,"Velocity",1,"NormalizeBombCircle",1,"ImpactPoint",1,[0,0],1],["Velocity",1,"Limit0109",1,[0,0],1]]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\BombCrosshairGroup\Circle,
                    "Circle": {
                        "type": "line",
                        "width": 6,
                        "points": [["ImpactPoint",[0,-0.0571429],1],["ImpactPoint",[0,-0.0714286],1],["MissileFlightTimeRot1",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot18",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot19",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.064],1,"ImpactPoint",1]]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\BombCrosshairGroup\Distance,
                    "Distance": {
                        "type": "text",
                        "source": "ImpactDistance",
                        "sourceScale": 0.001,
                        "sourcePrecision": 1,
                        "max": 15,
                        "align": "center",
                        "scale": 1,
                        "pos": ["ImpactPoint",[-0.002,0.11],1],
                        "right": ["ImpactPoint",[0.045,0.11],1],
                        "down": ["ImpactPoint",[-0.002,0.15],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\MGun,
                "MGun": {
                    "condition": "(mgun+rocket)",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\MGun\ModeText,
                    "ModeText": {
                        "type": "text",
                        "source": "static",
                        "align": "left",
                        "text": "GUN",
                        "scale": 1,
                        "pos": [[0.15,0.85],1],
                        "right": [[0.2,0.85],1],
                        "down": [[0.15,0.9],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\MGun\AmmoCounter,
                    "AmmoCounter": {
                        "type": "text",
                        "source": "ammo",
                        "sourceScale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.78,0.9],1],
                        "right": [[0.84,0.9],1],
                        "down": [[0.78,0.96],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\MGunCross,
                "MGunCross": {
                    "condition": "-1+(mgun+rocket)*impactDistance",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\MGunCross\Cross,
                    "Cross": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPointRelative",[0,-0.07],1],["ImpactPointRelative",[0,-0.03],1],[],["ImpactPointRelative",[0,0.045],1],["ImpactPointRelative",[0,0.03],1],[],["ImpactPointRelative",[-0.045,0],1],["ImpactPointRelative",[-0.03,0],1],[],["ImpactPointRelative",[0.045,0],1],["ImpactPointRelative",[0.03,0],1],[],["ImpactPointRelative",[0,-0.002],1],["ImpactPointRelative",[0,0.002],1],[],["ImpactPointRelative",[-0.002,0],1],["ImpactPointRelative",[0.002,0],1],[]]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\MGunCross\Circle,
                    "Circle": {
                        "type": "line",
                        "width": 6,
                        "points": [["ImpactPointRelative",[0,-0.0357143],1],["ImpactPointRelative",[0,-0.0446429],1],["MissileFlightTimeRot1",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot2",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot3",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot4",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot5",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot6",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot7",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot8",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot9",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot10",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot11",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot12",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot13",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot14",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot15",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot16",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot17",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot18",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot19",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot20",[0,0.05],1,"ImpactPointRelative",1],["MissileFlightTimeRot20",[0,0.04],1,"ImpactPointRelative",1]]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\MGunCross\Circle_LAR,
                    "Circle_LAR": {
                        "type": "line",
                        "width": 5,
                        "points": [["ImpactPointRelative",1,["LarAmmoMGunMin",0,-0.0535714],1],["ImpactPointRelative",1,["LarAmmoMGunMin",0,-0.0446429],1],[],["ImpactPointRelative",1,["LarAmmoMGunMax",0,-0.0535714],1],["ImpactPointRelative",1,["LarAmmoMGunMax",0,-0.0446429],1],[]]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\MGunCross\Distance,
                    "Distance": {
                        "type": "text",
                        "source": "ImpactDistance",
                        "sourceScale": 0.001,
                        "sourcePrecision": 1,
                        "max": 15,
                        "align": "center",
                        "scale": 1,
                        "pos": ["ImpactPointRelative",[-0.002,-0.1],1],
                        "right": ["ImpactPointRelative",[0.045,-0.1],1],
                        "down": ["ImpactPointRelative",[-0.002,-0.06],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\TargetInfo,
                "TargetInfo": {
                    "condition": "targetDist",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\TargetInfo\TargetDist,
                    "TargetDist": {
                        "type": "text",
                        "source": "targetDist",
                        "sourceScale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.83,0.86],1],
                        "right": [[0.89,0.86],1],
                        "down": [[0.83,0.92],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\TargetInfo\TargetHeight,
                    "TargetHeight": {
                        "type": "text",
                        "source": "targetHeight",
                        "sourceScale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.83,0.82],1],
                        "right": [[0.89,0.82],1],
                        "down": [[0.83,0.88],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\StallGroup,
                "StallGroup": {
                    "condition": "stall",
                    "blinkingPattern": [0.2,0.2],
                    "blinkingStartsOn": 1,
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\StallGroup\StallText,
                    "StallText": {
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
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\WeaponsLocking,
                "WeaponsLocking": {
                    "condition": "missilelocking",
                    "blinkingPattern": [0.2,0.2],
                    "blinkingStartsOn": 1,
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\WeaponsLocking\Text,
                    "Text": {
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
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\WeaponsLocked,
                "WeaponsLocked": {
                    "condition": "missilelocked",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\WeaponsLocked\Text,
                    "Text": {
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
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\IncomingMissile,
                "IncomingMissile": {
                    "condition": "incomingmissile",
                    "blinkingPattern": [0.3,0.3],
                    "blinkingStartsOn": 1,
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\IncomingMissile\Text,
                    "Text": {
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
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarGroup,
                "RadarGroup": {
                    "condition": "activeSensorsOn",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarGroup\Text,
                    "Text": {
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
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\FlapsGroup,
                "FlapsGroup": {
                    "condition": "flaps",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\FlapsGroup\GearText,
                    "GearText": {
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
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\ILS,
                "ILS": {
                    "condition": "ils",
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\ILS\GearText,
                    "GearText": {
                        "type": "text",
                        "source": "static",
                        "text": "GEAR",
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.94,0.66],1],
                        "right": [[1,0.66],1],
                        "down": [[0.94,0.72],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\ILS\Glideslope,
                    "Glideslope": {
                        "clipTL": [0,0],
                        "clipBR": [1,1],
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\ILS\Glideslope\ILS,
                        "ILS": {
                            "type": "line",
                            "width": 2,
                            "points": [["ILS_W",[-0.12,0],1],["ILS_W",[0.12,0],1],[],["ILS_W",[-0.12,-0.0107143],1],["ILS_W",[-0.12,0.0107143],1],[],["ILS_W",[-0.06,-0.00803571],1],["ILS_W",[-0.06,0.00803571],1],[],["ILS_W",[0,-0.0107143],1],["ILS_W",[0,0.0107143],1],[],["ILS_W",[0.06,-0.00803571],1],["ILS_W",[0.06,0.00803571],1],[],["ILS_W",[0.12,-0.0107143],1],["ILS_W",[0.12,0.0107143],1],[],["ILS_H",[0,-0.107143],1],["ILS_H",[0,0.107143],1],[],["ILS_H",[-0.012,-0.107143],1],["ILS_H",[0.012,-0.107143],1],[],["ILS_H",[-0.009,-0.0535714],1],["ILS_H",[0.009,-0.0535714],1],[],["ILS_H",[-0.012,0],1],["ILS_H",[0.012,0],1],[],["ILS_H",[-0.009,0.0535714],1],["ILS_H",[0.009,0.0535714],1],[],["ILS_H",[-0.012,0.107143],1],["ILS_H",[0.012,0.107143],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\ILS\Glideslope\airport,
                        "airport": {
                            "type": "line",
                            "points": [["airport1",1],["airport2",1],["airport4",1],["airport3",1],["airport1",1]]
                        }
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes,
                "RadarBoxes": {
                    "type": "radar",
                    "pos0": [0.495,0.536],
                    "pos10": [1.1026,1.0785],
                    "width": 4,
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\points,
                    "points": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\points\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "lineType": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsUnknown,
                    "pointsUnknown": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsUnknown\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,-0.01],1],[[0.02,-0.01],1],[[0.02,0.01],1],[[0,0.01],1]]],
                            "width": 4,
                            "lineType": 2
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsUnknownEnemy,
                    "pointsUnknownEnemy": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsUnknownEnemy\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,-0.01],1],[[0.02,-0.01],1],[[0.02,0.01],1],[[0,0.01],1]]],
                            "width": 4,
                            "lineType": 2
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsUnknownFriend,
                    "pointsUnknownFriend": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsUnknownFriend\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,-0.01],1],[[0.02,-0.01],1],[[0.02,0.01],1],[[0,0.01],1]]],
                            "width": 4,
                            "lineType": 2
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsUnknownCiv,
                    "pointsUnknownCiv": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsUnknownCiv\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,-0.01],1],[[0.02,-0.01],1],[[0.02,0.01],1],[[0,0.01],1]]],
                            "width": 4,
                            "lineType": 2
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsCar,
                    "pointsCar": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsCar\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.00260472,-0.0131894],1],[[0.0051303,-0.0125852],1],[[0.0075,-0.0115986],1]],[[[0,0],1],[[0.0075,-0.0115986],1],[[0.00964181,-0.0102595],1],[[0.0114907,-0.00860876],1]],[[[0,0],1],[[0.0114907,-0.00860876],1],[[0.0129904,-0.00669643],1],[[0.0140954,-0.00458063],1]],[[[0,0],1],[[0.0140954,-0.00458063],1],[[0.0147721,-0.00232564],1],[[0.015,5.8542e-010],1]],[[[0,0],1],[[0.015,5.8542e-010],1],[[0.0147721,0.00232565],1],[[0.0140954,0.00458063],1]],[[[0,0],1],[[0.0140954,0.00458063],1],[[0.0129904,0.00669643],1],[[0.0114907,0.00860876],1]],[[[0,0],1],[[0.0114907,0.00860876],1],[[0.00964181,0.0102595],1],[[0.0075,0.0115986],1]],[[[0,0],1],[[0.0075,0.0115986],1],[[0.0051303,0.0125852],1],[[0.00260472,0.0131894],1]],[[[0,0],1],[[0.00260472,0.0131894],1],[[-1.31134e-009,0.0133929],1],[[-0.00260473,0.0131894],1]],[[[0,0],1],[[-0.00260473,0.0131894],1],[[-0.0051303,0.0125852],1],[[-0.0075,0.0115986],1]],[[[0,0],1],[[-0.0075,0.0115986],1],[[-0.00964181,0.0102595],1],[[-0.0114907,0.00860876],1]],[[[0,0],1],[[-0.0114907,0.00860876],1],[[-0.0129904,0.00669643],1],[[-0.0140954,0.00458063],1]],[[[0,0],1],[[-0.0140954,0.00458063],1],[[-0.0147721,0.00232564],1],[[-0.015,-1.59708e-010],1]],[[[0,0],1],[[-0.015,-1.59708e-010],1],[[-0.0147721,-0.00232565],1],[[-0.0140954,-0.00458063],1]],[[[0,0],1],[[-0.0140954,-0.00458063],1],[[-0.0129904,-0.00669643],1],[[-0.0114907,-0.00860876],1]],[[[0,0],1],[[-0.0114907,-0.00860876],1],[[-0.00964181,-0.0102595],1],[[-0.0075,-0.0115986],1]],[[[0,0],1],[[-0.0075,-0.0115986],1],[[-0.00513031,-0.0125852],1],[[-0.00260472,-0.0131894],1]],[[[0,0],1],[[-0.00260472,-0.0131894],1],[[2.62268e-009,-0.0133929],1],[[0.00260472,-0.0131894],1]]],
                            "width": 4,
                            "lineType": 2
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsCarEnemy,
                    "pointsCarEnemy": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsCarEnemy\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.00260472,-0.0131894],1],[[0.0051303,-0.0125852],1],[[0.0075,-0.0115986],1]],[[[0,0],1],[[0.0075,-0.0115986],1],[[0.00964181,-0.0102595],1],[[0.0114907,-0.00860876],1]],[[[0,0],1],[[0.0114907,-0.00860876],1],[[0.0129904,-0.00669643],1],[[0.0140954,-0.00458063],1]],[[[0,0],1],[[0.0140954,-0.00458063],1],[[0.0147721,-0.00232564],1],[[0.015,5.8542e-010],1]],[[[0,0],1],[[0.015,5.8542e-010],1],[[0.0147721,0.00232565],1],[[0.0140954,0.00458063],1]],[[[0,0],1],[[0.0140954,0.00458063],1],[[0.0129904,0.00669643],1],[[0.0114907,0.00860876],1]],[[[0,0],1],[[0.0114907,0.00860876],1],[[0.00964181,0.0102595],1],[[0.0075,0.0115986],1]],[[[0,0],1],[[0.0075,0.0115986],1],[[0.0051303,0.0125852],1],[[0.00260472,0.0131894],1]],[[[0,0],1],[[0.00260472,0.0131894],1],[[-1.31134e-009,0.0133929],1],[[-0.00260473,0.0131894],1]],[[[0,0],1],[[-0.00260473,0.0131894],1],[[-0.0051303,0.0125852],1],[[-0.0075,0.0115986],1]],[[[0,0],1],[[-0.0075,0.0115986],1],[[-0.00964181,0.0102595],1],[[-0.0114907,0.00860876],1]],[[[0,0],1],[[-0.0114907,0.00860876],1],[[-0.0129904,0.00669643],1],[[-0.0140954,0.00458063],1]],[[[0,0],1],[[-0.0140954,0.00458063],1],[[-0.0147721,0.00232564],1],[[-0.015,-1.59708e-010],1]],[[[0,0],1],[[-0.015,-1.59708e-010],1],[[-0.0147721,-0.00232565],1],[[-0.0140954,-0.00458063],1]],[[[0,0],1],[[-0.0140954,-0.00458063],1],[[-0.0129904,-0.00669643],1],[[-0.0114907,-0.00860876],1]],[[[0,0],1],[[-0.0114907,-0.00860876],1],[[-0.00964181,-0.0102595],1],[[-0.0075,-0.0115986],1]],[[[0,0],1],[[-0.0075,-0.0115986],1],[[-0.00513031,-0.0125852],1],[[-0.00260472,-0.0131894],1]],[[[0,0],1],[[-0.00260472,-0.0131894],1],[[2.62268e-009,-0.0133929],1],[[0.00260472,-0.0131894],1]]],
                            "width": 4,
                            "lineType": 2
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsCarFriend,
                    "pointsCarFriend": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsCarFriend\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.00260472,-0.0131894],1],[[0.0051303,-0.0125852],1],[[0.0075,-0.0115986],1]],[[[0,0],1],[[0.0075,-0.0115986],1],[[0.00964181,-0.0102595],1],[[0.0114907,-0.00860876],1]],[[[0,0],1],[[0.0114907,-0.00860876],1],[[0.0129904,-0.00669643],1],[[0.0140954,-0.00458063],1]],[[[0,0],1],[[0.0140954,-0.00458063],1],[[0.0147721,-0.00232564],1],[[0.015,5.8542e-010],1]],[[[0,0],1],[[0.015,5.8542e-010],1],[[0.0147721,0.00232565],1],[[0.0140954,0.00458063],1]],[[[0,0],1],[[0.0140954,0.00458063],1],[[0.0129904,0.00669643],1],[[0.0114907,0.00860876],1]],[[[0,0],1],[[0.0114907,0.00860876],1],[[0.00964181,0.0102595],1],[[0.0075,0.0115986],1]],[[[0,0],1],[[0.0075,0.0115986],1],[[0.0051303,0.0125852],1],[[0.00260472,0.0131894],1]],[[[0,0],1],[[0.00260472,0.0131894],1],[[-1.31134e-009,0.0133929],1],[[-0.00260473,0.0131894],1]],[[[0,0],1],[[-0.00260473,0.0131894],1],[[-0.0051303,0.0125852],1],[[-0.0075,0.0115986],1]],[[[0,0],1],[[-0.0075,0.0115986],1],[[-0.00964181,0.0102595],1],[[-0.0114907,0.00860876],1]],[[[0,0],1],[[-0.0114907,0.00860876],1],[[-0.0129904,0.00669643],1],[[-0.0140954,0.00458063],1]],[[[0,0],1],[[-0.0140954,0.00458063],1],[[-0.0147721,0.00232564],1],[[-0.015,-1.59708e-010],1]],[[[0,0],1],[[-0.015,-1.59708e-010],1],[[-0.0147721,-0.00232565],1],[[-0.0140954,-0.00458063],1]],[[[0,0],1],[[-0.0140954,-0.00458063],1],[[-0.0129904,-0.00669643],1],[[-0.0114907,-0.00860876],1]],[[[0,0],1],[[-0.0114907,-0.00860876],1],[[-0.00964181,-0.0102595],1],[[-0.0075,-0.0115986],1]],[[[0,0],1],[[-0.0075,-0.0115986],1],[[-0.00513031,-0.0125852],1],[[-0.00260472,-0.0131894],1]],[[[0,0],1],[[-0.00260472,-0.0131894],1],[[2.62268e-009,-0.0133929],1],[[0.00260472,-0.0131894],1]]],
                            "width": 4,
                            "lineType": 2
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsCarCiv,
                    "pointsCarCiv": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsCarCiv\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.00260472,-0.0131894],1],[[0.0051303,-0.0125852],1],[[0.0075,-0.0115986],1]],[[[0,0],1],[[0.0075,-0.0115986],1],[[0.00964181,-0.0102595],1],[[0.0114907,-0.00860876],1]],[[[0,0],1],[[0.0114907,-0.00860876],1],[[0.0129904,-0.00669643],1],[[0.0140954,-0.00458063],1]],[[[0,0],1],[[0.0140954,-0.00458063],1],[[0.0147721,-0.00232564],1],[[0.015,5.8542e-010],1]],[[[0,0],1],[[0.015,5.8542e-010],1],[[0.0147721,0.00232565],1],[[0.0140954,0.00458063],1]],[[[0,0],1],[[0.0140954,0.00458063],1],[[0.0129904,0.00669643],1],[[0.0114907,0.00860876],1]],[[[0,0],1],[[0.0114907,0.00860876],1],[[0.00964181,0.0102595],1],[[0.0075,0.0115986],1]],[[[0,0],1],[[0.0075,0.0115986],1],[[0.0051303,0.0125852],1],[[0.00260472,0.0131894],1]],[[[0,0],1],[[0.00260472,0.0131894],1],[[-1.31134e-009,0.0133929],1],[[-0.00260473,0.0131894],1]],[[[0,0],1],[[-0.00260473,0.0131894],1],[[-0.0051303,0.0125852],1],[[-0.0075,0.0115986],1]],[[[0,0],1],[[-0.0075,0.0115986],1],[[-0.00964181,0.0102595],1],[[-0.0114907,0.00860876],1]],[[[0,0],1],[[-0.0114907,0.00860876],1],[[-0.0129904,0.00669643],1],[[-0.0140954,0.00458063],1]],[[[0,0],1],[[-0.0140954,0.00458063],1],[[-0.0147721,0.00232564],1],[[-0.015,-1.59708e-010],1]],[[[0,0],1],[[-0.015,-1.59708e-010],1],[[-0.0147721,-0.00232565],1],[[-0.0140954,-0.00458063],1]],[[[0,0],1],[[-0.0140954,-0.00458063],1],[[-0.0129904,-0.00669643],1],[[-0.0114907,-0.00860876],1]],[[[0,0],1],[[-0.0114907,-0.00860876],1],[[-0.00964181,-0.0102595],1],[[-0.0075,-0.0115986],1]],[[[0,0],1],[[-0.0075,-0.0115986],1],[[-0.00513031,-0.0125852],1],[[-0.00260472,-0.0131894],1]],[[[0,0],1],[[-0.00260472,-0.0131894],1],[[2.62268e-009,-0.0133929],1],[[0.00260472,-0.0131894],1]]],
                            "width": 4,
                            "lineType": 2
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsCarNeutral,
                    "pointsCarNeutral": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsCarNeutral\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.00260472,-0.0131894],1],[[0.0051303,-0.0125852],1],[[0.0075,-0.0115986],1]],[[[0,0],1],[[0.0075,-0.0115986],1],[[0.00964181,-0.0102595],1],[[0.0114907,-0.00860876],1]],[[[0,0],1],[[0.0114907,-0.00860876],1],[[0.0129904,-0.00669643],1],[[0.0140954,-0.00458063],1]],[[[0,0],1],[[0.0140954,-0.00458063],1],[[0.0147721,-0.00232564],1],[[0.015,5.8542e-010],1]],[[[0,0],1],[[0.015,5.8542e-010],1],[[0.0147721,0.00232565],1],[[0.0140954,0.00458063],1]],[[[0,0],1],[[0.0140954,0.00458063],1],[[0.0129904,0.00669643],1],[[0.0114907,0.00860876],1]],[[[0,0],1],[[0.0114907,0.00860876],1],[[0.00964181,0.0102595],1],[[0.0075,0.0115986],1]],[[[0,0],1],[[0.0075,0.0115986],1],[[0.0051303,0.0125852],1],[[0.00260472,0.0131894],1]],[[[0,0],1],[[0.00260472,0.0131894],1],[[-1.31134e-009,0.0133929],1],[[-0.00260473,0.0131894],1]],[[[0,0],1],[[-0.00260473,0.0131894],1],[[-0.0051303,0.0125852],1],[[-0.0075,0.0115986],1]],[[[0,0],1],[[-0.0075,0.0115986],1],[[-0.00964181,0.0102595],1],[[-0.0114907,0.00860876],1]],[[[0,0],1],[[-0.0114907,0.00860876],1],[[-0.0129904,0.00669643],1],[[-0.0140954,0.00458063],1]],[[[0,0],1],[[-0.0140954,0.00458063],1],[[-0.0147721,0.00232564],1],[[-0.015,-1.59708e-010],1]],[[[0,0],1],[[-0.015,-1.59708e-010],1],[[-0.0147721,-0.00232565],1],[[-0.0140954,-0.00458063],1]],[[[0,0],1],[[-0.0140954,-0.00458063],1],[[-0.0129904,-0.00669643],1],[[-0.0114907,-0.00860876],1]],[[[0,0],1],[[-0.0114907,-0.00860876],1],[[-0.00964181,-0.0102595],1],[[-0.0075,-0.0115986],1]],[[[0,0],1],[[-0.0075,-0.0115986],1],[[-0.00513031,-0.0125852],1],[[-0.00260472,-0.0131894],1]],[[[0,0],1],[[-0.00260472,-0.0131894],1],[[2.62268e-009,-0.0133929],1],[[0.00260472,-0.0131894],1]]],
                            "width": 4,
                            "lineType": 2
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsTank,
                    "pointsTank": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsTank\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "lineType": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsTankEnemy,
                    "pointsTankEnemy": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsTankEnemy\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "lineType": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsTankFriend,
                    "pointsTankFriend": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsTankFriend\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "lineType": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsTankCiv,
                    "pointsTankCiv": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsTankCiv\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "lineType": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsTankNeutral,
                    "pointsTankNeutral": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsTankNeutral\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "lineType": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsAirplane,
                    "pointsAirplane": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsAirplane\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "lineType": 2,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsAirplaneEnemy,
                    "pointsAirplaneEnemy": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsAirplaneEnemy\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "points": [[[0.03,0],1],[[0,0.0267857],1],[[-0.03,0],1],[[0,-0.0267857],1],[[0.03,0],1]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsAirplaneFriend,
                    "pointsAirplaneFriend": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsAirplaneFriend\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "points": [[[0,-0.0267857],1],[[0.005208,-0.0263786],1],[[0.01026,-0.0251705],1],[[0.015,-0.0231964],1],[[0.019284,-0.0205179],1],[[0.02298,-0.0172179],1],[[0.02598,-0.0133929],1],[[0.028191,-0.00916071],1],[[0.029544,-0.00465],1],[[0.03,0],1],[[0.029544,0.00465],1],[[0.028191,0.00916071],1],[[0.02598,0.0133929],1],[[0.02298,0.0172179],1],[[0.019284,0.0205179],1],[[0.015,0.0231964],1],[[0.01026,0.0251705],1],[[0.005208,0.0263786],1],[[0,0.0267857],1],[[-0.005208,0.0263786],1],[[-0.01026,0.0251705],1],[[-0.015,0.0231964],1],[[-0.019284,0.0205179],1],[[-0.02298,0.0172179],1],[[-0.02598,0.0133929],1],[[-0.028191,0.00916071],1],[[-0.029544,0.00465],1],[[-0.03,0],1],[[-0.029544,-0.00465],1],[[-0.028191,-0.00916071],1],[[-0.02598,-0.0133929],1],[[-0.02298,-0.0172179],1],[[-0.019284,-0.0205179],1],[[-0.015,-0.0231964],1],[[-0.01026,-0.0251705],1],[[-0.005208,-0.0263786],1],[[0,-0.0267857],1],[],[[0.0212132,-0.0189404],1],[[-0.0212132,0.0189404],1],[],[[0.0212132,0.0189404],1],[[-0.0212132,-0.0189404],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsHeli,
                    "pointsHeli": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsHeli\Draw
                        "Draw": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1],[],[[0,0],1],[[0.01,-0.015],1],[[-0.01,-0.015],1]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsHeliEnemy,
                    "pointsHeliEnemy": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsHeliEnemy\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]],[[[0,0],1],[[0.01,-0.015],1],[[-0.01,-0.015],1]]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsHeliFriend,
                    "pointsHeliFriend": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsHeliFriend\Draw
                        "Draw": {
                            "type": "polygon",
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]],[[[0,0],1],[[0.01,-0.015],1],[[-0.01,-0.015],1]]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsHeliFriend\DrawLine,
                        "DrawLine": {
                            "type": "line",
                            "width": 4,
                            "points": []
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsHeliFriend\IFF_Text,
                        "IFF_Text": {
                            "type": "text",
                            "source": "static",
                            "text": "ALLY",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0,0.01],1],
                            "right": [[0.04,0.01],1],
                            "down": [[0,0.05],1]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsLaser,
                    "pointsLaser": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsLaser\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "points": [[[0,-0.0178571],1],[[-1.74846e-009,0.0178571],1],[],[[0.02,7.80561e-010],1],[[-0.02,-2.12944e-010],1],[],[[0.0106066,-0.00947018],1],[[-0.0106066,0.00947018],1],[],[[0.0106066,0.00947018],1],[[-0.0106066,-0.00947018],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsNVG,
                    "pointsNVG": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsLaser\Draw
                        "Draw": {
                            "type": "line",
                            "width": 4,
                            "points": [[[0,-0.0178571],1],[[-1.74846e-009,0.0178571],1],[],[[0.02,7.80561e-010],1],[[-0.02,-2.12944e-010],1],[],[[0.0106066,-0.00947018],1],[[-0.0106066,0.00947018],1],[],[[0.0106066,0.00947018],1],[[-0.0106066,-0.00947018],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsStatic,
                    "pointsStatic": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsStatic\Draw
                        "Draw": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsStaticEnemy,
                    "pointsStaticEnemy": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsStatic\Draw
                        "Draw": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsStaticFriend,
                    "pointsStaticFriend": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsStatic\Draw
                        "Draw": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsStaticCiv,
                    "pointsStaticCiv": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsStatic\Draw
                        "Draw": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsStaticNeutral,
                    "pointsStaticNeutral": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\RadarBoxes\pointsStatic\Draw
                        "Draw": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0,0],1],[[0.01,0.015],1],[[-0.01,0.015],1]]]
                        }
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\TargetDiamond,
                "TargetDiamond": {
                    # Class: CfgVehicles\rhsusf_f22\MFD\AirplaneHUD\Draw\TargetDiamond\shape
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",[-0.002,-0.00178571],1],["Target",1,"Limit0109",[0.002,-0.00178571],1],["Target",1,"Limit0109",[0.002,0.00178571],1],["Target",1,"Limit0109",[-0.002,0.00178571],1],["Target",1,"Limit0109",[-0.002,-0.00178571],1],[],["Target",1,"Limit0109",1,[0.02,0.0178571],1],["Target",1,"Limit0109",1,[-0.02,0.0178571],1],["Target",1,"Limit0109",1,[-0.02,-0.0178571],1],["Target",1,"Limit0109",1,[0.02,-0.0178571],1],["Target",1,"Limit0109",1,[0.02,0.0178571],1]]
                    }
                }
            }
        },
        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1,
        "MFD_1": {
            "topLeft": "MFD_1_TL",
            "topRight": "MFD_1_TR",
            "bottomLeft": "MFD_1_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0.03,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "rhsusf_digital_font_var",
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\material,
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw,
            "Draw": {
                "condition": "on",
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\UHF1_Text,
                "UHF1_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "UHF-1",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.04,0.13],1],
                    "right": [[0.11,0.13],1],
                    "down": [[0.04,0.2],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\UHF1_Text2,
                "UHF1_Text2": {
                    "type": "text",
                    "source": "static",
                    "text": ":",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.04,0.22],1],
                    "right": [[0.11,0.22],1],
                    "down": [[0.04,0.29],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\UHF1_Value,
                "UHF1_Value": {
                    "type": "text",
                    "source": "userText",
                    "sourceScale": 1,
                    "sourceIndex": 0,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.1,0.22],1],
                    "right": [[0.17,0.22],1],
                    "down": [[0.1,0.29],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\VHF1_Text,
                "VHF1_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "VHF-1",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.96,0.13],1],
                    "right": [[1.03,0.13],1],
                    "down": [[0.96,0.2],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\VHF1_Text2,
                "VHF1_Text2": {
                    "type": "text",
                    "source": "static",
                    "text": ":",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.96,0.22],1],
                    "right": [[1.03,0.22],1],
                    "down": [[0.96,0.29],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\VHF1_Value,
                "VHF1_Value": {
                    "type": "text",
                    "source": "userText",
                    "sourceScale": 1,
                    "sourceIndex": 1,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.9,0.22],1],
                    "right": [[0.97,0.22],1],
                    "down": [[0.9,0.29],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\TCN_Text,
                "TCN_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "TCN 004X T/R",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.04,0.49],1],
                    "right": [[0.11,0.49],1],
                    "down": [[0.04,0.56],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\ILS,
                "ILS": {
                    "condition": "1-ils",
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\ILS\ILS_Text,
                    "ILS_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "ILS OFF",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.04,0.58],1],
                        "right": [[0.11,0.58],1],
                        "down": [[0.04,0.65],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\ILS_Off,
                "ILS_Off": {
                    "condition": "ils",
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\ILS_Off\ILS_Text,
                    "ILS_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "ILS ON",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.04,0.58],1],
                        "right": [[0.11,0.58],1],
                        "down": [[0.04,0.65],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\STPT_Text,
                "STPT_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "STPT 01/A",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.04,0.67],1],
                    "right": [[0.11,0.67],1],
                    "down": [[0.04,0.74],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\IFF_Text,
                "IFF_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "IFF M3/A",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.04,0.76],1],
                    "right": [[0.11,0.76],1],
                    "down": [[0.04,0.83],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\IFF_Text2,
                "IFF_Text2": {
                    "type": "text",
                    "source": "static",
                    "text": " :",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.04,0.85],1],
                    "right": [[0.11,0.85],1],
                    "down": [[0.04,0.92],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\IDK_Text,
                "IDK_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "DK 04",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.96,0.49],1],
                    "right": [[1.03,0.49],1],
                    "down": [[0.96,0.56],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\STR_Text,
                "STR_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "STR",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.96,0.58],1],
                    "right": [[1.03,0.58],1],
                    "down": [[0.96,0.65],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\AP_Text,
                "AP_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "A/P ON",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.96,0.67],1],
                    "right": [[1.03,0.67],1],
                    "down": [[0.96,0.74],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\CurrentTime,
                "CurrentTime": {
                    "type": "text",
                    "source": "time",
                    "text": "%X",
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.96,"0.13+0.09*7"],1],
                    "right": [[1.03,"0.13+0.09*7"],1],
                    "down": [[0.96,0.83],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\ING_Text,
                "ING_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "INS NAV",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.96,0.87],1],
                    "right": [[1.03,0.87],1],
                    "down": [[0.96,0.94],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\UHF_Text,
                "UHF_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "UHF",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.25,0.94],1],
                    "right": [[0.32,0.94],1],
                    "down": [[0.25,1.01],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\VHF_Text,
                "VHF_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "VHF",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.51,0.94],1],
                    "right": [[0.58,0.94],1],
                    "down": [[0.51,1.01],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_1\Draw\TIME_Text,
                "TIME_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "TIME",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.75,0.94],1],
                    "right": [[0.82,0.94],1],
                    "down": [[0.75,1.01],1]
                }
            }
        },
        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2,
        "MFD_2": {
            "topLeft": "MFD_2_TL",
            "topRight": "MFD_2_TR",
            "bottomLeft": "MFD_2_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1,1],
            "enableParallax": 0,
            "font": "rhsusf_digital_font_var",
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\material,
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones,
            "Bones": {
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\Center
                "Center": {
                    "type": "fixed",
                    "pos": [0.35,0.475]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\Level0,
                "Level0": {
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\Level0_Background,
                "Level0_Background": {
                    "pos0": [0,0],
                    "pos10": [0.68,0.89],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP5,
                "LevelP5": {
                    "angle": 5,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM5,
                "LevelM5": {
                    "angle": -5,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP10,
                "LevelP10": {
                    "angle": 10,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM10,
                "LevelM10": {
                    "angle": -10,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP15,
                "LevelP15": {
                    "angle": 15,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM15,
                "LevelM15": {
                    "angle": -15,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP20,
                "LevelP20": {
                    "angle": 20,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM20,
                "LevelM20": {
                    "angle": -20,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP25,
                "LevelP25": {
                    "angle": 25,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM25,
                "LevelM25": {
                    "angle": -25,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP30,
                "LevelP30": {
                    "angle": 30,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM30,
                "LevelM30": {
                    "angle": -30,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP35,
                "LevelP35": {
                    "angle": 35,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM35,
                "LevelM35": {
                    "angle": -35,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP40,
                "LevelP40": {
                    "angle": 40,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM40,
                "LevelM40": {
                    "angle": -40,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP45,
                "LevelP45": {
                    "angle": 45,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM45,
                "LevelM45": {
                    "angle": -45,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP50,
                "LevelP50": {
                    "angle": 50,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM50,
                "LevelM50": {
                    "angle": -50,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP60,
                "LevelP60": {
                    "angle": 60,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM60,
                "LevelM60": {
                    "angle": -60,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP70,
                "LevelP70": {
                    "angle": 70,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM70,
                "LevelM70": {
                    "angle": -70,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP80,
                "LevelP80": {
                    "angle": 80,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM80,
                "LevelM80": {
                    "angle": -80,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelP90,
                "LevelP90": {
                    "angle": 90,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Bones\LevelM90,
                "LevelM90": {
                    "angle": -90,
                    "pos0": ["0.498-0.15",0.47],
                    "pos10": [0.838,0.915],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw,
            "Draw": {
                "condition": "on",
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground,
                "HorizontBackground": {
                    "color": [0.1,0.3,0.7],
                    "alpha": 0.8,
                    "clipTL": [0.018,0.085],
                    "clipBR": [0.69,0.88],
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\Static,
                    "Static": {
                        "type": "polygon",
                        "points": [[["Level0",[-10,-19.99],1],["Level0",[10,-19.99],1],["Level0",[10,0.0100002],1],["Level0",[-10,0.0100002],1]]]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\StaticBlack,
                    "StaticBlack": {
                        "color": [0,0,0],
                        "alpha": 1,
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\StaticBlack\Static,
                        "Static": {
                            "type": "polygon",
                            "points": [[["Level0",[-10,0.01],1],["Level0",[10,0.01],1],["Level0",[10,20.01],1],["Level0",[-10,20.01],1]]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite,
                    "HorizontWhite": {
                        "color": [0,0,0],
                        "alpha": 0.9,
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\Dimmed,
                        "Dimmed": {
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\Dimmed\Level0
                            "Level0": {
                                "type": "line",
                                "width": 7,
                                "points": [["Level0",[0.25,0],1],["Level0",[0.065,0],1],[],["Level0",[-0.065,0],1],["Level0",[-0.25,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\Level0,
                        "Level0": {
                            "type": "line",
                            "width": 16,
                            "points": []
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP5,
                        "LevelP5": {
                            "type": "line",
                            "points": [["LevelP5",["-0.16-0.015",0.02],1],["LevelP5",["-0.16-0.015",0],1],["LevelP5",[-0.06,"0.001*9"],1],[],["LevelP5",[0.06,"0.001*9"],1],["LevelP5",["+0.16+0.015",0],1],["LevelP5",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_5,
                        "VALP_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP5",[-0.19,-0.017],1],
                            "right": ["LevelP5",[-0.13,-0.017],1],
                            "down": ["LevelP5",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_5_R,
                        "VALP_1_5_R": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP5",[0.19,-0.017],1],
                            "right": ["LevelP5",[0.25,-0.017],1],
                            "down": ["LevelP5",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP10,
                        "LevelP10": {
                            "type": "line",
                            "points": [["LevelP10",["-0.16-0.015",0.02],1],["LevelP10",["-0.16-0.015",0],1],["LevelP10",[-0.06,"0.001*9"],1],[],["LevelP10",[0.06,"0.001*9"],1],["LevelP10",["+0.16+0.015",0],1],["LevelP10",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_10,
                        "VALP_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP10",[-0.19,-0.017],1],
                            "right": ["LevelP10",[-0.13,-0.017],1],
                            "down": ["LevelP10",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_10_R,
                        "VALP_1_10_R": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP10",[0.19,-0.017],1],
                            "right": ["LevelP10",[0.25,-0.017],1],
                            "down": ["LevelP10",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP15,
                        "LevelP15": {
                            "type": "line",
                            "points": [["LevelP15",["-0.16-0.015",0.02],1],["LevelP15",["-0.16-0.015",0],1],["LevelP15",[-0.06,"0.001*9"],1],[],["LevelP15",[0.06,"0.001*9"],1],["LevelP15",["+0.16+0.015",0],1],["LevelP15",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_15,
                        "VALP_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP15",[-0.19,-0.017],1],
                            "right": ["LevelP15",[-0.13,-0.017],1],
                            "down": ["LevelP15",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_15_R,
                        "VALP_1_15_R": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP15",[0.19,-0.017],1],
                            "right": ["LevelP15",[0.25,-0.017],1],
                            "down": ["LevelP15",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP20,
                        "LevelP20": {
                            "type": "line",
                            "points": [["LevelP20",["-0.16-0.015",0.02],1],["LevelP20",["-0.16-0.015",0],1],["LevelP20",[-0.06,"0.001*9"],1],[],["LevelP20",[0.06,"0.001*9"],1],["LevelP20",["+0.16+0.015",0],1],["LevelP20",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_20,
                        "VALP_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP20",[-0.19,-0.017],1],
                            "right": ["LevelP20",[-0.13,-0.017],1],
                            "down": ["LevelP20",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_20_R,
                        "VALP_1_20_R": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP20",[0.19,-0.017],1],
                            "right": ["LevelP20",[0.25,-0.017],1],
                            "down": ["LevelP20",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP25,
                        "LevelP25": {
                            "type": "line",
                            "points": [["LevelP25",["-0.16-0.015",0.02],1],["LevelP25",["-0.16-0.015",0],1],["LevelP25",[-0.06,"0.001*9"],1],[],["LevelP25",[0.06,"0.001*9"],1],["LevelP25",["+0.16+0.015",0],1],["LevelP25",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_25,
                        "VALP_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP25",[-0.19,-0.017],1],
                            "right": ["LevelP25",[-0.13,-0.017],1],
                            "down": ["LevelP25",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_25_R,
                        "VALP_1_25_R": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP25",[0.19,-0.017],1],
                            "right": ["LevelP25",[0.25,-0.017],1],
                            "down": ["LevelP25",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP30,
                        "LevelP30": {
                            "type": "line",
                            "points": [["LevelP30",["-0.16-0.015",0.02],1],["LevelP30",["-0.16-0.015",0],1],["LevelP30",[-0.06,"0.001*9"],1],[],["LevelP30",[0.06,"0.001*9"],1],["LevelP30",["+0.16+0.015",0],1],["LevelP30",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_30,
                        "VALP_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP30",[-0.19,-0.017],1],
                            "right": ["LevelP30",[-0.13,-0.017],1],
                            "down": ["LevelP30",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_30_R,
                        "VALP_1_30_R": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP30",[0.19,-0.017],1],
                            "right": ["LevelP30",[0.25,-0.017],1],
                            "down": ["LevelP30",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP35,
                        "LevelP35": {
                            "type": "line",
                            "points": [["LevelP35",["-0.16-0.015",0.02],1],["LevelP35",["-0.16-0.015",0],1],["LevelP35",[-0.06,"0.001*9"],1],[],["LevelP35",[0.06,"0.001*9"],1],["LevelP35",["+0.16+0.015",0],1],["LevelP35",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_35,
                        "VALP_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP35",[-0.19,-0.017],1],
                            "right": ["LevelP35",[-0.13,-0.017],1],
                            "down": ["LevelP35",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_35_R,
                        "VALP_1_35_R": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP35",[0.19,-0.017],1],
                            "right": ["LevelP35",[0.25,-0.017],1],
                            "down": ["LevelP35",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP40,
                        "LevelP40": {
                            "type": "line",
                            "points": [["LevelP40",["-0.16-0.015",0.02],1],["LevelP40",["-0.16-0.015",0],1],["LevelP40",[-0.06,"0.001*9"],1],[],["LevelP40",[0.06,"0.001*9"],1],["LevelP40",["+0.16+0.015",0],1],["LevelP40",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_40,
                        "VALP_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP40",[-0.19,-0.017],1],
                            "right": ["LevelP40",[-0.13,-0.017],1],
                            "down": ["LevelP40",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_40_R,
                        "VALP_1_40_R": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP40",[0.19,-0.017],1],
                            "right": ["LevelP40",[0.25,-0.017],1],
                            "down": ["LevelP40",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP45,
                        "LevelP45": {
                            "type": "line",
                            "points": [["LevelP45",["-0.16-0.015",0.02],1],["LevelP45",["-0.16-0.015",0],1],["LevelP45",[-0.06,"0.001*9"],1],[],["LevelP45",[0.06,"0.001*9"],1],["LevelP45",["+0.16+0.015",0],1],["LevelP45",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_45,
                        "VALP_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP45",[-0.19,-0.017],1],
                            "right": ["LevelP45",[-0.13,-0.017],1],
                            "down": ["LevelP45",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_45_R,
                        "VALP_1_45_R": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP45",[0.19,-0.017],1],
                            "right": ["LevelP45",[0.25,-0.017],1],
                            "down": ["LevelP45",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP50,
                        "LevelP50": {
                            "type": "line",
                            "points": [["LevelP50",["-0.16-0.015",0.02],1],["LevelP50",["-0.16-0.015",0],1],["LevelP50",[-0.06,"0.001*9"],1],[],["LevelP50",[0.06,"0.001*9"],1],["LevelP50",["+0.16+0.015",0],1],["LevelP50",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_50,
                        "VALP_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP50",[-0.19,-0.017],1],
                            "right": ["LevelP50",[-0.13,-0.017],1],
                            "down": ["LevelP50",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_50_R,
                        "VALP_1_50_R": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP50",[0.19,-0.017],1],
                            "right": ["LevelP50",[0.25,-0.017],1],
                            "down": ["LevelP50",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP60,
                        "LevelP60": {
                            "type": "line",
                            "points": [["LevelP60",["-0.16-0.015",0.02],1],["LevelP60",["-0.16-0.015",0],1],["LevelP60",[-0.06,"0.001*9"],1],[],["LevelP60",[0.06,"0.001*9"],1],["LevelP60",["+0.16+0.015",0],1],["LevelP60",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_60,
                        "VALP_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP60",[-0.19,-0.017],1],
                            "right": ["LevelP60",[-0.13,-0.017],1],
                            "down": ["LevelP60",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_60_R,
                        "VALP_1_60_R": {
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP60",[0.19,-0.017],1],
                            "right": ["LevelP60",[0.25,-0.017],1],
                            "down": ["LevelP60",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP70,
                        "LevelP70": {
                            "type": "line",
                            "points": [["LevelP70",["-0.16-0.015",0.02],1],["LevelP70",["-0.16-0.015",0],1],["LevelP70",[-0.06,"0.001*9"],1],[],["LevelP70",[0.06,"0.001*9"],1],["LevelP70",["+0.16+0.015",0],1],["LevelP70",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_70,
                        "VALP_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": "70",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP70",[-0.19,-0.017],1],
                            "right": ["LevelP70",[-0.13,-0.017],1],
                            "down": ["LevelP70",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_70_R,
                        "VALP_1_70_R": {
                            "type": "text",
                            "source": "static",
                            "text": "70",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP70",[0.19,-0.017],1],
                            "right": ["LevelP70",[0.25,-0.017],1],
                            "down": ["LevelP70",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP80,
                        "LevelP80": {
                            "type": "line",
                            "points": [["LevelP80",["-0.16-0.015",0.02],1],["LevelP80",["-0.16-0.015",0],1],["LevelP80",[-0.06,"0.001*9"],1],[],["LevelP80",[0.06,"0.001*9"],1],["LevelP80",["+0.16+0.015",0],1],["LevelP80",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_80,
                        "VALP_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": "80",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP80",[-0.19,-0.017],1],
                            "right": ["LevelP80",[-0.13,-0.017],1],
                            "down": ["LevelP80",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_80_R,
                        "VALP_1_80_R": {
                            "type": "text",
                            "source": "static",
                            "text": "80",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP80",[0.19,-0.017],1],
                            "right": ["LevelP80",[0.25,-0.017],1],
                            "down": ["LevelP80",[0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\LevelP90,
                        "LevelP90": {
                            "type": "line",
                            "points": [["LevelP90",["-0.16-0.015",0.02],1],["LevelP90",["-0.16-0.015",0],1],["LevelP90",[-0.06,"0.001*9"],1],[],["LevelP90",[0.06,"0.001*9"],1],["LevelP90",["+0.16+0.015",0],1],["LevelP90",["+0.16+0.015",0.02],1]],
                            "width": 16
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_90,
                        "VALP_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": "90",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP90",[-0.19,-0.017],1],
                            "right": ["LevelP90",[-0.13,-0.017],1],
                            "down": ["LevelP90",[-0.19,0.033],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontWhite\VALP_1_90_R,
                        "VALP_1_90_R": {
                            "type": "text",
                            "source": "static",
                            "text": "90",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP90",[0.19,-0.017],1],
                            "right": ["LevelP90",[0.25,-0.017],1],
                            "down": ["LevelP90",[0.19,0.033],1]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack,
                    "HorizontBlack": {
                        "color": [1,1,1],
                        "alpha": 0.9,
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\Level0,
                        "Level0": {
                            "type": "line",
                            "width": 7,
                            "points": []
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM5,
                        "LevelM5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.175,-0.02],1],["LevelM5",[-0.175,0],1],[],["LevelM5",[-0.16,"-0.001*1"],1],["LevelM5",[-0.145,"-0.001*2"],1],[],["LevelM5",[-0.13,"-0.001*3"],1],["LevelM5",[-0.115,"-0.001*4"],1],[],["LevelM5",[-0.1,"-0.001*5"],1],["LevelM5",[-0.085,"-0.001*6"],1],[],["LevelM5",[-0.07,"-0.001*7"],1],["LevelM5",[-0.055,"-0.001*8"],1],[],["LevelM5",[-0.04,"-0.001*9"],1],[],["LevelM5",[0.175,-0.02],1],["LevelM5",[0.175,0],1],[],["LevelM5",[0.16,"-0.001*1"],1],["LevelM5",[0.145,"-0.001*2"],1],[],["LevelM5",[0.13,"-0.001*3"],1],["LevelM5",[0.115,"-0.001*4"],1],[],["LevelM5",[0.1,"-0.001*5"],1],["LevelM5",[0.085,"-0.001*6"],1],[],["LevelM5",[0.07,"-0.001*7"],1],["LevelM5",[0.055,"-0.001*8"],1],[],["LevelM5",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_5,
                        "VALM_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM5",[-0.19,-0.032],1],
                            "right": ["LevelM5",[-0.13,-0.032],1],
                            "down": ["LevelM5",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_5_R,
                        "VALM_1_5_R": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM5",[0.19,-0.032],1],
                            "right": ["LevelM5",[0.25,-0.032],1],
                            "down": ["LevelM5",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM10,
                        "LevelM10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.175,-0.02],1],["LevelM10",[-0.175,0],1],[],["LevelM10",[-0.16,"-0.001*1"],1],["LevelM10",[-0.145,"-0.001*2"],1],[],["LevelM10",[-0.13,"-0.001*3"],1],["LevelM10",[-0.115,"-0.001*4"],1],[],["LevelM10",[-0.1,"-0.001*5"],1],["LevelM10",[-0.085,"-0.001*6"],1],[],["LevelM10",[-0.07,"-0.001*7"],1],["LevelM10",[-0.055,"-0.001*8"],1],[],["LevelM10",[-0.04,"-0.001*9"],1],[],["LevelM10",[0.175,-0.02],1],["LevelM10",[0.175,0],1],[],["LevelM10",[0.16,"-0.001*1"],1],["LevelM10",[0.145,"-0.001*2"],1],[],["LevelM10",[0.13,"-0.001*3"],1],["LevelM10",[0.115,"-0.001*4"],1],[],["LevelM10",[0.1,"-0.001*5"],1],["LevelM10",[0.085,"-0.001*6"],1],[],["LevelM10",[0.07,"-0.001*7"],1],["LevelM10",[0.055,"-0.001*8"],1],[],["LevelM10",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_10,
                        "VALM_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM10",[-0.19,-0.032],1],
                            "right": ["LevelM10",[-0.13,-0.032],1],
                            "down": ["LevelM10",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_10_R,
                        "VALM_1_10_R": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM10",[0.19,-0.032],1],
                            "right": ["LevelM10",[0.25,-0.032],1],
                            "down": ["LevelM10",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM15,
                        "LevelM15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.175,-0.02],1],["LevelM15",[-0.175,0],1],[],["LevelM15",[-0.16,"-0.001*1"],1],["LevelM15",[-0.145,"-0.001*2"],1],[],["LevelM15",[-0.13,"-0.001*3"],1],["LevelM15",[-0.115,"-0.001*4"],1],[],["LevelM15",[-0.1,"-0.001*5"],1],["LevelM15",[-0.085,"-0.001*6"],1],[],["LevelM15",[-0.07,"-0.001*7"],1],["LevelM15",[-0.055,"-0.001*8"],1],[],["LevelM15",[-0.04,"-0.001*9"],1],[],["LevelM15",[0.175,-0.02],1],["LevelM15",[0.175,0],1],[],["LevelM15",[0.16,"-0.001*1"],1],["LevelM15",[0.145,"-0.001*2"],1],[],["LevelM15",[0.13,"-0.001*3"],1],["LevelM15",[0.115,"-0.001*4"],1],[],["LevelM15",[0.1,"-0.001*5"],1],["LevelM15",[0.085,"-0.001*6"],1],[],["LevelM15",[0.07,"-0.001*7"],1],["LevelM15",[0.055,"-0.001*8"],1],[],["LevelM15",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_15,
                        "VALM_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM15",[-0.19,-0.032],1],
                            "right": ["LevelM15",[-0.13,-0.032],1],
                            "down": ["LevelM15",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_15_R,
                        "VALM_1_15_R": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM15",[0.19,-0.032],1],
                            "right": ["LevelM15",[0.25,-0.032],1],
                            "down": ["LevelM15",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM20,
                        "LevelM20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.175,-0.02],1],["LevelM20",[-0.175,0],1],[],["LevelM20",[-0.16,"-0.001*1"],1],["LevelM20",[-0.145,"-0.001*2"],1],[],["LevelM20",[-0.13,"-0.001*3"],1],["LevelM20",[-0.115,"-0.001*4"],1],[],["LevelM20",[-0.1,"-0.001*5"],1],["LevelM20",[-0.085,"-0.001*6"],1],[],["LevelM20",[-0.07,"-0.001*7"],1],["LevelM20",[-0.055,"-0.001*8"],1],[],["LevelM20",[-0.04,"-0.001*9"],1],[],["LevelM20",[0.175,-0.02],1],["LevelM20",[0.175,0],1],[],["LevelM20",[0.16,"-0.001*1"],1],["LevelM20",[0.145,"-0.001*2"],1],[],["LevelM20",[0.13,"-0.001*3"],1],["LevelM20",[0.115,"-0.001*4"],1],[],["LevelM20",[0.1,"-0.001*5"],1],["LevelM20",[0.085,"-0.001*6"],1],[],["LevelM20",[0.07,"-0.001*7"],1],["LevelM20",[0.055,"-0.001*8"],1],[],["LevelM20",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_20,
                        "VALM_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM20",[-0.19,-0.032],1],
                            "right": ["LevelM20",[-0.13,-0.032],1],
                            "down": ["LevelM20",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_20_R,
                        "VALM_1_20_R": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM20",[0.19,-0.032],1],
                            "right": ["LevelM20",[0.25,-0.032],1],
                            "down": ["LevelM20",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM25,
                        "LevelM25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.175,-0.02],1],["LevelM25",[-0.175,0],1],[],["LevelM25",[-0.16,"-0.001*1"],1],["LevelM25",[-0.145,"-0.001*2"],1],[],["LevelM25",[-0.13,"-0.001*3"],1],["LevelM25",[-0.115,"-0.001*4"],1],[],["LevelM25",[-0.1,"-0.001*5"],1],["LevelM25",[-0.085,"-0.001*6"],1],[],["LevelM25",[-0.07,"-0.001*7"],1],["LevelM25",[-0.055,"-0.001*8"],1],[],["LevelM25",[-0.04,"-0.001*9"],1],[],["LevelM25",[0.175,-0.02],1],["LevelM25",[0.175,0],1],[],["LevelM25",[0.16,"-0.001*1"],1],["LevelM25",[0.145,"-0.001*2"],1],[],["LevelM25",[0.13,"-0.001*3"],1],["LevelM25",[0.115,"-0.001*4"],1],[],["LevelM25",[0.1,"-0.001*5"],1],["LevelM25",[0.085,"-0.001*6"],1],[],["LevelM25",[0.07,"-0.001*7"],1],["LevelM25",[0.055,"-0.001*8"],1],[],["LevelM25",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_25,
                        "VALM_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM25",[-0.19,-0.032],1],
                            "right": ["LevelM25",[-0.13,-0.032],1],
                            "down": ["LevelM25",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_25_R,
                        "VALM_1_25_R": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM25",[0.19,-0.032],1],
                            "right": ["LevelM25",[0.25,-0.032],1],
                            "down": ["LevelM25",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM30,
                        "LevelM30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.175,-0.02],1],["LevelM30",[-0.175,0],1],[],["LevelM30",[-0.16,"-0.001*1"],1],["LevelM30",[-0.145,"-0.001*2"],1],[],["LevelM30",[-0.13,"-0.001*3"],1],["LevelM30",[-0.115,"-0.001*4"],1],[],["LevelM30",[-0.1,"-0.001*5"],1],["LevelM30",[-0.085,"-0.001*6"],1],[],["LevelM30",[-0.07,"-0.001*7"],1],["LevelM30",[-0.055,"-0.001*8"],1],[],["LevelM30",[-0.04,"-0.001*9"],1],[],["LevelM30",[0.175,-0.02],1],["LevelM30",[0.175,0],1],[],["LevelM30",[0.16,"-0.001*1"],1],["LevelM30",[0.145,"-0.001*2"],1],[],["LevelM30",[0.13,"-0.001*3"],1],["LevelM30",[0.115,"-0.001*4"],1],[],["LevelM30",[0.1,"-0.001*5"],1],["LevelM30",[0.085,"-0.001*6"],1],[],["LevelM30",[0.07,"-0.001*7"],1],["LevelM30",[0.055,"-0.001*8"],1],[],["LevelM30",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_30,
                        "VALM_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM30",[-0.19,-0.032],1],
                            "right": ["LevelM30",[-0.13,-0.032],1],
                            "down": ["LevelM30",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_30_R,
                        "VALM_1_30_R": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM30",[0.19,-0.032],1],
                            "right": ["LevelM30",[0.25,-0.032],1],
                            "down": ["LevelM30",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM35,
                        "LevelM35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.175,-0.02],1],["LevelM35",[-0.175,0],1],[],["LevelM35",[-0.16,"-0.001*1"],1],["LevelM35",[-0.145,"-0.001*2"],1],[],["LevelM35",[-0.13,"-0.001*3"],1],["LevelM35",[-0.115,"-0.001*4"],1],[],["LevelM35",[-0.1,"-0.001*5"],1],["LevelM35",[-0.085,"-0.001*6"],1],[],["LevelM35",[-0.07,"-0.001*7"],1],["LevelM35",[-0.055,"-0.001*8"],1],[],["LevelM35",[-0.04,"-0.001*9"],1],[],["LevelM35",[0.175,-0.02],1],["LevelM35",[0.175,0],1],[],["LevelM35",[0.16,"-0.001*1"],1],["LevelM35",[0.145,"-0.001*2"],1],[],["LevelM35",[0.13,"-0.001*3"],1],["LevelM35",[0.115,"-0.001*4"],1],[],["LevelM35",[0.1,"-0.001*5"],1],["LevelM35",[0.085,"-0.001*6"],1],[],["LevelM35",[0.07,"-0.001*7"],1],["LevelM35",[0.055,"-0.001*8"],1],[],["LevelM35",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_35,
                        "VALM_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM35",[-0.19,-0.032],1],
                            "right": ["LevelM35",[-0.13,-0.032],1],
                            "down": ["LevelM35",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_35_R,
                        "VALM_1_35_R": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM35",[0.19,-0.032],1],
                            "right": ["LevelM35",[0.25,-0.032],1],
                            "down": ["LevelM35",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM40,
                        "LevelM40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.175,-0.02],1],["LevelM40",[-0.175,0],1],[],["LevelM40",[-0.16,"-0.001*1"],1],["LevelM40",[-0.145,"-0.001*2"],1],[],["LevelM40",[-0.13,"-0.001*3"],1],["LevelM40",[-0.115,"-0.001*4"],1],[],["LevelM40",[-0.1,"-0.001*5"],1],["LevelM40",[-0.085,"-0.001*6"],1],[],["LevelM40",[-0.07,"-0.001*7"],1],["LevelM40",[-0.055,"-0.001*8"],1],[],["LevelM40",[-0.04,"-0.001*9"],1],[],["LevelM40",[0.175,-0.02],1],["LevelM40",[0.175,0],1],[],["LevelM40",[0.16,"-0.001*1"],1],["LevelM40",[0.145,"-0.001*2"],1],[],["LevelM40",[0.13,"-0.001*3"],1],["LevelM40",[0.115,"-0.001*4"],1],[],["LevelM40",[0.1,"-0.001*5"],1],["LevelM40",[0.085,"-0.001*6"],1],[],["LevelM40",[0.07,"-0.001*7"],1],["LevelM40",[0.055,"-0.001*8"],1],[],["LevelM40",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_40,
                        "VALM_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM40",[-0.19,-0.032],1],
                            "right": ["LevelM40",[-0.13,-0.032],1],
                            "down": ["LevelM40",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_40_R,
                        "VALM_1_40_R": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM40",[0.19,-0.032],1],
                            "right": ["LevelM40",[0.25,-0.032],1],
                            "down": ["LevelM40",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM45,
                        "LevelM45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.175,-0.02],1],["LevelM45",[-0.175,0],1],[],["LevelM45",[-0.16,"-0.001*1"],1],["LevelM45",[-0.145,"-0.001*2"],1],[],["LevelM45",[-0.13,"-0.001*3"],1],["LevelM45",[-0.115,"-0.001*4"],1],[],["LevelM45",[-0.1,"-0.001*5"],1],["LevelM45",[-0.085,"-0.001*6"],1],[],["LevelM45",[-0.07,"-0.001*7"],1],["LevelM45",[-0.055,"-0.001*8"],1],[],["LevelM45",[-0.04,"-0.001*9"],1],[],["LevelM45",[0.175,-0.02],1],["LevelM45",[0.175,0],1],[],["LevelM45",[0.16,"-0.001*1"],1],["LevelM45",[0.145,"-0.001*2"],1],[],["LevelM45",[0.13,"-0.001*3"],1],["LevelM45",[0.115,"-0.001*4"],1],[],["LevelM45",[0.1,"-0.001*5"],1],["LevelM45",[0.085,"-0.001*6"],1],[],["LevelM45",[0.07,"-0.001*7"],1],["LevelM45",[0.055,"-0.001*8"],1],[],["LevelM45",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_45,
                        "VALM_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM45",[-0.19,-0.032],1],
                            "right": ["LevelM45",[-0.13,-0.032],1],
                            "down": ["LevelM45",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_45_R,
                        "VALM_1_45_R": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM45",[0.19,-0.032],1],
                            "right": ["LevelM45",[0.25,-0.032],1],
                            "down": ["LevelM45",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM50,
                        "LevelM50": {
                            "type": "line",
                            "points": [["LevelM50",[-0.175,-0.02],1],["LevelM50",[-0.175,0],1],[],["LevelM50",[-0.16,"-0.001*1"],1],["LevelM50",[-0.145,"-0.001*2"],1],[],["LevelM50",[-0.13,"-0.001*3"],1],["LevelM50",[-0.115,"-0.001*4"],1],[],["LevelM50",[-0.1,"-0.001*5"],1],["LevelM50",[-0.085,"-0.001*6"],1],[],["LevelM50",[-0.07,"-0.001*7"],1],["LevelM50",[-0.055,"-0.001*8"],1],[],["LevelM50",[-0.04,"-0.001*9"],1],[],["LevelM50",[0.175,-0.02],1],["LevelM50",[0.175,0],1],[],["LevelM50",[0.16,"-0.001*1"],1],["LevelM50",[0.145,"-0.001*2"],1],[],["LevelM50",[0.13,"-0.001*3"],1],["LevelM50",[0.115,"-0.001*4"],1],[],["LevelM50",[0.1,"-0.001*5"],1],["LevelM50",[0.085,"-0.001*6"],1],[],["LevelM50",[0.07,"-0.001*7"],1],["LevelM50",[0.055,"-0.001*8"],1],[],["LevelM50",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_50,
                        "VALM_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM50",[-0.19,-0.032],1],
                            "right": ["LevelM50",[-0.13,-0.032],1],
                            "down": ["LevelM50",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_50_R,
                        "VALM_1_50_R": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM50",[0.19,-0.032],1],
                            "right": ["LevelM50",[0.25,-0.032],1],
                            "down": ["LevelM50",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM60,
                        "LevelM60": {
                            "type": "line",
                            "points": [["LevelM60",[-0.175,-0.02],1],["LevelM60",[-0.175,0],1],[],["LevelM60",[-0.16,"-0.001*1"],1],["LevelM60",[-0.145,"-0.001*2"],1],[],["LevelM60",[-0.13,"-0.001*3"],1],["LevelM60",[-0.115,"-0.001*4"],1],[],["LevelM60",[-0.1,"-0.001*5"],1],["LevelM60",[-0.085,"-0.001*6"],1],[],["LevelM60",[-0.07,"-0.001*7"],1],["LevelM60",[-0.055,"-0.001*8"],1],[],["LevelM60",[-0.04,"-0.001*9"],1],[],["LevelM60",[0.175,-0.02],1],["LevelM60",[0.175,0],1],[],["LevelM60",[0.16,"-0.001*1"],1],["LevelM60",[0.145,"-0.001*2"],1],[],["LevelM60",[0.13,"-0.001*3"],1],["LevelM60",[0.115,"-0.001*4"],1],[],["LevelM60",[0.1,"-0.001*5"],1],["LevelM60",[0.085,"-0.001*6"],1],[],["LevelM60",[0.07,"-0.001*7"],1],["LevelM60",[0.055,"-0.001*8"],1],[],["LevelM60",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_60,
                        "VALM_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM60",[-0.19,-0.032],1],
                            "right": ["LevelM60",[-0.13,-0.032],1],
                            "down": ["LevelM60",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_60_R,
                        "VALM_1_60_R": {
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM60",[0.19,-0.032],1],
                            "right": ["LevelM60",[0.25,-0.032],1],
                            "down": ["LevelM60",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM70,
                        "LevelM70": {
                            "type": "line",
                            "points": [["LevelM70",[-0.175,-0.02],1],["LevelM70",[-0.175,0],1],[],["LevelM70",[-0.16,"-0.001*1"],1],["LevelM70",[-0.145,"-0.001*2"],1],[],["LevelM70",[-0.13,"-0.001*3"],1],["LevelM70",[-0.115,"-0.001*4"],1],[],["LevelM70",[-0.1,"-0.001*5"],1],["LevelM70",[-0.085,"-0.001*6"],1],[],["LevelM70",[-0.07,"-0.001*7"],1],["LevelM70",[-0.055,"-0.001*8"],1],[],["LevelM70",[-0.04,"-0.001*9"],1],[],["LevelM70",[0.175,-0.02],1],["LevelM70",[0.175,0],1],[],["LevelM70",[0.16,"-0.001*1"],1],["LevelM70",[0.145,"-0.001*2"],1],[],["LevelM70",[0.13,"-0.001*3"],1],["LevelM70",[0.115,"-0.001*4"],1],[],["LevelM70",[0.1,"-0.001*5"],1],["LevelM70",[0.085,"-0.001*6"],1],[],["LevelM70",[0.07,"-0.001*7"],1],["LevelM70",[0.055,"-0.001*8"],1],[],["LevelM70",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_70,
                        "VALM_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM70",[-0.19,-0.032],1],
                            "right": ["LevelM70",[-0.13,-0.032],1],
                            "down": ["LevelM70",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_70_R,
                        "VALM_1_70_R": {
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM70",[0.19,-0.032],1],
                            "right": ["LevelM70",[0.25,-0.032],1],
                            "down": ["LevelM70",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM80,
                        "LevelM80": {
                            "type": "line",
                            "points": [["LevelM80",[-0.175,-0.02],1],["LevelM80",[-0.175,0],1],[],["LevelM80",[-0.16,"-0.001*1"],1],["LevelM80",[-0.145,"-0.001*2"],1],[],["LevelM80",[-0.13,"-0.001*3"],1],["LevelM80",[-0.115,"-0.001*4"],1],[],["LevelM80",[-0.1,"-0.001*5"],1],["LevelM80",[-0.085,"-0.001*6"],1],[],["LevelM80",[-0.07,"-0.001*7"],1],["LevelM80",[-0.055,"-0.001*8"],1],[],["LevelM80",[-0.04,"-0.001*9"],1],[],["LevelM80",[0.175,-0.02],1],["LevelM80",[0.175,0],1],[],["LevelM80",[0.16,"-0.001*1"],1],["LevelM80",[0.145,"-0.001*2"],1],[],["LevelM80",[0.13,"-0.001*3"],1],["LevelM80",[0.115,"-0.001*4"],1],[],["LevelM80",[0.1,"-0.001*5"],1],["LevelM80",[0.085,"-0.001*6"],1],[],["LevelM80",[0.07,"-0.001*7"],1],["LevelM80",[0.055,"-0.001*8"],1],[],["LevelM80",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_80,
                        "VALM_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM80",[-0.19,-0.032],1],
                            "right": ["LevelM80",[-0.13,-0.032],1],
                            "down": ["LevelM80",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_80_R,
                        "VALM_1_80_R": {
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM80",[0.19,-0.032],1],
                            "right": ["LevelM80",[0.25,-0.032],1],
                            "down": ["LevelM80",[0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\LevelM90,
                        "LevelM90": {
                            "type": "line",
                            "points": [["LevelM90",[-0.175,-0.02],1],["LevelM90",[-0.175,0],1],[],["LevelM90",[-0.16,"-0.001*1"],1],["LevelM90",[-0.145,"-0.001*2"],1],[],["LevelM90",[-0.13,"-0.001*3"],1],["LevelM90",[-0.115,"-0.001*4"],1],[],["LevelM90",[-0.1,"-0.001*5"],1],["LevelM90",[-0.085,"-0.001*6"],1],[],["LevelM90",[-0.07,"-0.001*7"],1],["LevelM90",[-0.055,"-0.001*8"],1],[],["LevelM90",[-0.04,"-0.001*9"],1],[],["LevelM90",[0.175,-0.02],1],["LevelM90",[0.175,0],1],[],["LevelM90",[0.16,"-0.001*1"],1],["LevelM90",[0.145,"-0.001*2"],1],[],["LevelM90",[0.13,"-0.001*3"],1],["LevelM90",[0.115,"-0.001*4"],1],[],["LevelM90",[0.1,"-0.001*5"],1],["LevelM90",[0.085,"-0.001*6"],1],[],["LevelM90",[0.07,"-0.001*7"],1],["LevelM90",[0.055,"-0.001*8"],1],[],["LevelM90",[0.04,"-0.001*9"],1]],
                            "width": 7
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_90,
                        "VALM_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": -90,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM90",[-0.19,-0.032],1],
                            "right": ["LevelM90",[-0.13,-0.032],1],
                            "down": ["LevelM90",[-0.19,0.018],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HorizontBackground\HorizontBlack\VALM_1_90_R,
                        "VALM_1_90_R": {
                            "type": "text",
                            "source": "static",
                            "text": -90,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM90",[0.19,-0.032],1],
                            "right": ["LevelM90",[0.25,-0.032],1],
                            "down": ["LevelM90",[0.19,0.018],1]
                        }
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\BlackBackground,
                "BlackBackground": {
                    "color": [0,0,0],
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\BlackBackground\Static,
                    "Static": {
                        "type": "polygon",
                        "points": [[[[0.01,0.08],1],[[0.18,0.08],1],[[0.18,0.25],1],[[0.01,0.25],1]],[[[0.27,0.08],1],[[0.41,0.08],1],[[0.41,0.17],1],[[0.27,0.17],1]],[[[0.51,0.08],1],[[0.69,0.08],1],[[0.69,0.25],1],[[0.51,0.25],1]],[[[0.01,0.42],1],[[0.14,0.42],1],[[0.14,0.53],1],[[0.01,0.53],1]],[[[0.51,0.42],1],[[0.69,0.42],1],[[0.69,0.53],1],[[0.51,0.53],1]],[[[0.52,0.79],1],[[0.69,0.79],1],[[0.69,0.88],1],[[0.52,0.88],1]]]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\HeadingText,
                "HeadingText": {
                    "type": "text",
                    "source": "heading",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "refreshRate": 0.1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.29,0.09],1],
                    "right": [[0.36,0.09],1],
                    "down": [[0.29,0.16],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green,
                "Green": {
                    "color": [0.15,1,0.15,1],
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\Throttle1,
                    "Throttle1": {
                        "type": "text",
                        "source": "throttle",
                        "sourceScale": 100,
                        "sourceLength": 1,
                        "refreshRate": 0.07,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.12,0.09],1],
                        "right": [[0.17,0.09],1],
                        "down": [[0.12,0.16],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\Throttle1Static_Text,
                    "Throttle1Static_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "%",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.14,0.09],1],
                        "right": [[0.19,0.09],1],
                        "down": [[0.14,0.16],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\Throttle2,
                    "Throttle2": {
                        "type": "text",
                        "source": "throttle",
                        "sourceScale": 100,
                        "sourceLength": 1,
                        "refreshRate": 0.07,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.62,0.09],1],
                        "right": [[0.67,0.09],1],
                        "down": [[0.62,0.16],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\Throttle2Static_Text,
                    "Throttle2Static_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "%",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.64,0.09],1],
                        "right": [[0.69,0.09],1],
                        "down": [[0.64,0.16],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\temp1,
                    "temp1": {
                        "type": "text",
                        "source": "rpm",
                        "sourceScale": 645,
                        "sourceLength": 1,
                        "refreshRate": 0.07,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.12,0.17],1],
                        "right": [[0.17,0.17],1],
                        "down": [[0.12,0.24],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\temp1Static_Text,
                    "temp1Static_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "o",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.14,0.15],1],
                        "right": [[0.19,0.15],1],
                        "down": [[0.14,0.22],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\temp2,
                    "temp2": {
                        "type": "text",
                        "source": "rpm",
                        "sourceScale": 673,
                        "sourceLength": 1,
                        "refreshRate": 0.07,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.62,0.17],1],
                        "right": [[0.67,0.17],1],
                        "down": [[0.62,0.24],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\temp2Static_Text,
                    "temp2Static_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "o",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.64,0.15],1],
                        "right": [[0.69,0.15],1],
                        "down": [[0.64,0.22],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\BaroStatic_Text,
                    "BaroStatic_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "BARO",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.06,0.89],1],
                        "right": [[0.12,0.89],1],
                        "down": [[0.06,0.96],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\BaroSource_Text,
                    "BaroSource_Text": {
                        "type": "text",
                        "source": "altitudeAGL",
                        "sourceScale": 1,
                        "sourcePrecision": 1,
                        "sourceOffset": -2.5,
                        "sourceLength": 5,
                        "refreshRate": 0.07,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.2,0.89],1],
                        "right": [[0.25,0.89],1],
                        "down": [[0.2,0.96],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\Cord_Text,
                    "Cord_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "POS:",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.4,0.89],1],
                        "right": [[0.45,0.89],1],
                        "down": [[0.4,0.96],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\CordX,
                    "CordX": {
                        "type": "text",
                        "source": "coordinateX",
                        "sourceScale": 0.01,
                        "sourceLength": 3,
                        "sourceOffset": -0.5,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.5,0.89],1],
                        "right": [[0.55,0.89],1],
                        "down": [[0.5,0.96],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\CordY,
                    "CordY": {
                        "source": "coordinateY",
                        "pos": [["0.5+0.07",0.89],1],
                        "right": [[0.62,0.89],1],
                        "down": [["0.5+0.07",0.96],1],
                        "type": "text",
                        "sourceScale": 0.01,
                        "sourceLength": 3,
                        "sourceOffset": -0.5,
                        "align": "right",
                        "scale": 1
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\FuelRemaining_Text,
                    "FuelRemaining_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "I:",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.73,0.09],1],
                        "right": [[0.79,0.09],1],
                        "down": [[0.73,0.17],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\FuelRemaining_Source,
                    "FuelRemaining_Source": {
                        "type": "text",
                        "source": "fuel",
                        "sourceScale": 20,
                        "sourcePrecision": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.79,0.09],1],
                        "right": [[0.85,0.09],1],
                        "down": [[0.79,0.17],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\TimeRemaining_Text,
                    "TimeRemaining_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "T:",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.73,0.17],1],
                        "right": [[0.79,0.17],1],
                        "down": [[0.73,0.25],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\TimeRemaining_Source,
                    "TimeRemaining_Source": {
                        "type": "text",
                        "source": "fuel",
                        "sourceScale": 2.4,
                        "sourcePrecision": 2,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.79,0.17],1],
                        "right": [[0.85,0.17],1],
                        "down": [[0.79,0.25],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\FuelSt20_Text,
                    "FuelSt20_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "20",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.92,0.27],1],
                        "right": [[0.98,0.27],1],
                        "down": [[0.92,0.33],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\FuelSt10_Text,
                    "FuelSt10_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "10",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.92,0.46],1],
                        "right": [[0.98,0.46],1],
                        "down": [[0.92,0.52],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\FuelSt8_Text,
                    "FuelSt8_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "8",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.92,0.55],1],
                        "right": [[0.98,0.55],1],
                        "down": [[0.92,0.61],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\FuelSt6_Text,
                    "FuelSt6_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "6",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.92,0.65],1],
                        "right": [[0.98,0.65],1],
                        "down": [[0.92,0.71],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\FuelSt4_Text,
                    "FuelSt4_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "4",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.92,0.75],1],
                        "right": [[0.98,0.75],1],
                        "down": [[0.92,0.81],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\Green\FuelSt2_Text,
                    "FuelSt2_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "2",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.92,0.82],1],
                        "right": [[0.98,0.82],1],
                        "down": [[0.92,0.88],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\SpeedSource,
                "SpeedSource": {
                    "type": "text",
                    "source": "speed",
                    "sourceScale": 3.6,
                    "sourceLength": 3,
                    "refreshRate": 0.1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.03,0.44],1],
                    "right": [[0.1,0.44],1],
                    "down": [[0.03,0.52],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\RadarHeightSource,
                "RadarHeightSource": {
                    "type": "text",
                    "source": "speed",
                    "sourceScale": 1,
                    "sourceLength": 5,
                    "refreshRate": 0.1,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.68,0.44],1],
                    "right": [[0.75,0.44],1],
                    "down": [[0.68,0.52],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\ClimbSource,
                "ClimbSource": {
                    "type": "text",
                    "source": "vspeed",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "refreshRate": 0.1,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.68,0.8],1],
                    "right": [[0.75,0.8],1],
                    "down": [[0.68,0.88],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_2\Draw\StaticDraw,
                "StaticDraw": {
                    "type": "line",
                    "width": 10,
                    "points": [["Center",[0,-0.0392647],1],["Center",[0.005208,-0.0386679],1],["Center",[0.01026,-0.036897],1],["Center",[0.015,-0.0340032],1],["Center",[0.019284,-0.0300768],1],["Center",[0.02298,-0.0252394],1],["Center",[0.02598,-0.0196324],1],["Center",[0.028191,-0.0134285],1],["Center",[0.029544,-0.00681635],1],["Center",[0.03,0],1],["Center",[0.029544,0.00681635],1],["Center",[0.028191,0.0134285],1],["Center",[0.02598,0.0196324],1],["Center",[0.02298,0.0252394],1],["Center",[0.019284,0.0300768],1],["Center",[0.015,0.0340032],1],["Center",[0.01026,0.036897],1],["Center",[0.005208,0.0386679],1],["Center",[0,0.0392647],1],["Center",[-0.005208,0.0386679],1],["Center",[-0.01026,0.036897],1],["Center",[-0.015,0.0340032],1],["Center",[-0.019284,0.0300768],1],["Center",[-0.02298,0.0252394],1],["Center",[-0.02598,0.0196324],1],["Center",[-0.028191,0.0134285],1],["Center",[-0.029544,0.00681635],1],["Center",[-0.03,0],1],["Center",[-0.029544,-0.00681635],1],["Center",[-0.028191,-0.0134285],1],["Center",[-0.02598,-0.0196324],1],["Center",[-0.02298,-0.0252394],1],["Center",[-0.019284,-0.0300768],1],["Center",[-0.015,-0.0340032],1],["Center",[-0.01026,-0.036897],1],["Center",[-0.005208,-0.0386679],1],["Center",[0,-0.0392647],1]]
                }
            }
        },
        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3,
        "MFD_3": {
            "topLeft": "MFD_3_TL",
            "topRight": "MFD_3_TR",
            "bottomLeft": "MFD_3_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\material,
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw,
            "Draw": {
                "condition": "on",
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw\Rpm1Source,
                "Rpm1Source": {
                    "type": "text",
                    "source": "rpm",
                    "sourceScale": 100,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.3,0.135],1],
                    "right": [[0.34,0.135],1],
                    "down": [[0.3,0.175],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw\Rpm2Source,
                "Rpm2Source": {
                    "pos": [[0.64,0.135],1],
                    "right": [[0.68,0.135],1],
                    "down": [[0.64,0.175],1],
                    "type": "text",
                    "source": "rpm",
                    "sourceScale": 100,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw\EGT1Source,
                "EGT1Source": {
                    "type": "text",
                    "source": "rpm",
                    "sourceScale": 380,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.3,0.29],1],
                    "right": [[0.34,0.29],1],
                    "down": [[0.3,0.33],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw\EGT2Source,
                "EGT2Source": {
                    "pos": [[0.64,0.29],1],
                    "right": [[0.68,0.29],1],
                    "down": [[0.64,0.33],1],
                    "type": "text",
                    "source": "rpm",
                    "sourceScale": 380,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw
oz1Source,
                "noz1Source": {
                    "type": "text",
                    "source": "throttle",
                    "sourceScale": 100,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.33,0.475],1],
                    "right": [[0.36,0.475],1],
                    "down": [[0.33,0.505],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw
oz2Source,
                "noz2Source": {
                    "pos": [[0.66,0.475],1],
                    "right": [[0.69,0.475],1],
                    "down": [[0.66,0.505],1],
                    "type": "text",
                    "source": "throttle",
                    "sourceScale": 100,
                    "align": "center",
                    "scale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw\oil1Source,
                "oil1Source": {
                    "type": "text",
                    "source": "rpm",
                    "sourceScale": 235,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.31,0.58],1],
                    "right": [[0.35,0.58],1],
                    "down": [[0.31,0.62],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw\oil2Source,
                "oil2Source": {
                    "pos": [[0.65,0.58],1],
                    "right": [[0.69,0.58],1],
                    "down": [[0.65,0.62],1],
                    "type": "text",
                    "source": "rpm",
                    "sourceScale": 235,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw\hyd1Source,
                "hyd1Source": {
                    "type": "text",
                    "source": "rpm",
                    "sourceScale": 210,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.13,0.81],1],
                    "right": [[0.16,0.81],1],
                    "down": [[0.13,0.84],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw\hyd2Source,
                "hyd2Source": {
                    "pos": [[0.38,0.81],1],
                    "right": [[0.41,0.81],1],
                    "down": [[0.38,0.84],1],
                    "type": "text",
                    "source": "rpm",
                    "sourceScale": 210,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_3\Draw\FuelLeftSource,
                "FuelLeftSource": {
                    "type": "text",
                    "source": "fuel",
                    "sourceScale": 2000,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.8,0.92],1],
                    "right": [[0.85,0.92],1],
                    "down": [[0.8,0.97],1]
                }
            }
        },
        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4,
        "MFD_4": {
            "topLeft": "MFD_4_TL",
            "topRight": "MFD_4_TR",
            "bottomLeft": "MFD_4_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\material,
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones,
            "Bones": {
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Sensor_Offset
                "Sensor_Offset": {
                    "type": "fixed",
                    "pos": [0,0.33]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Static_Offset,
                "Static_Offset": {
                    "type": "fixed",
                    "pos": [0.5,0.85]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Static_Offset2,
                "Static_Offset2": {
                    "pos": [0.5,0.83],
                    "type": "fixed"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_0,
                "Rotation_0": {
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "minAngle": 0,
                    "maxAngle": -360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_10,
                "Rotation_10": {
                    "minAngle": 10,
                    "maxAngle": -350,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_20,
                "Rotation_20": {
                    "minAngle": 20,
                    "maxAngle": -340,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_30,
                "Rotation_30": {
                    "minAngle": 30,
                    "maxAngle": -330,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_40,
                "Rotation_40": {
                    "minAngle": 40,
                    "maxAngle": -320,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_50,
                "Rotation_50": {
                    "minAngle": 50,
                    "maxAngle": -310,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_60,
                "Rotation_60": {
                    "minAngle": 60,
                    "maxAngle": -300,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_70,
                "Rotation_70": {
                    "minAngle": 70,
                    "maxAngle": -290,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_80,
                "Rotation_80": {
                    "minAngle": 80,
                    "maxAngle": -280,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_90,
                "Rotation_90": {
                    "minAngle": 90,
                    "maxAngle": -270,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_100,
                "Rotation_100": {
                    "minAngle": 100,
                    "maxAngle": -260,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_110,
                "Rotation_110": {
                    "minAngle": 110,
                    "maxAngle": -250,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_120,
                "Rotation_120": {
                    "minAngle": 120,
                    "maxAngle": -240,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_130,
                "Rotation_130": {
                    "minAngle": 130,
                    "maxAngle": -230,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_140,
                "Rotation_140": {
                    "minAngle": 140,
                    "maxAngle": -220,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_150,
                "Rotation_150": {
                    "minAngle": 150,
                    "maxAngle": -210,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_160,
                "Rotation_160": {
                    "minAngle": 160,
                    "maxAngle": -200,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_170,
                "Rotation_170": {
                    "minAngle": 170,
                    "maxAngle": -190,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_180,
                "Rotation_180": {
                    "minAngle": 180,
                    "maxAngle": -180,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_190,
                "Rotation_190": {
                    "minAngle": 190,
                    "maxAngle": -170,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_200,
                "Rotation_200": {
                    "minAngle": 200,
                    "maxAngle": -160,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_210,
                "Rotation_210": {
                    "minAngle": 210,
                    "maxAngle": -150,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_220,
                "Rotation_220": {
                    "minAngle": 220,
                    "maxAngle": -140,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_230,
                "Rotation_230": {
                    "minAngle": 230,
                    "maxAngle": -130,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_240,
                "Rotation_240": {
                    "minAngle": 240,
                    "maxAngle": -120,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_250,
                "Rotation_250": {
                    "minAngle": 250,
                    "maxAngle": -110,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_260,
                "Rotation_260": {
                    "minAngle": 260,
                    "maxAngle": -100,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_270,
                "Rotation_270": {
                    "minAngle": 270,
                    "maxAngle": -90,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_280,
                "Rotation_280": {
                    "minAngle": 280,
                    "maxAngle": -80,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_290,
                "Rotation_290": {
                    "minAngle": 290,
                    "maxAngle": -70,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_300,
                "Rotation_300": {
                    "minAngle": 300,
                    "maxAngle": -60,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_310,
                "Rotation_310": {
                    "minAngle": 310,
                    "maxAngle": -50,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_320,
                "Rotation_320": {
                    "minAngle": 320,
                    "maxAngle": -40,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_330,
                "Rotation_330": {
                    "minAngle": 330,
                    "maxAngle": -30,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_340,
                "Rotation_340": {
                    "minAngle": 340,
                    "maxAngle": -20,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_350,
                "Rotation_350": {
                    "minAngle": 350,
                    "maxAngle": -10,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_0,
                "Rotation_Inv_0": {
                    "min": 0,
                    "max": 360,
                    "minAngle": 180,
                    "maxAngle": -180,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_30,
                "Rotation_Inv_30": {
                    "minAngle": 210,
                    "maxAngle": -150,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_60,
                "Rotation_Inv_60": {
                    "minAngle": 240,
                    "maxAngle": -120,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_90,
                "Rotation_Inv_90": {
                    "minAngle": 270,
                    "maxAngle": -90,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_120,
                "Rotation_Inv_120": {
                    "minAngle": 300,
                    "maxAngle": -60,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_150,
                "Rotation_Inv_150": {
                    "minAngle": 330,
                    "maxAngle": -30,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_180,
                "Rotation_Inv_180": {
                    "minAngle": 360,
                    "maxAngle": 0,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_210,
                "Rotation_Inv_210": {
                    "minAngle": 390,
                    "maxAngle": 30,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_240,
                "Rotation_Inv_240": {
                    "minAngle": 420,
                    "maxAngle": 60,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_270,
                "Rotation_Inv_270": {
                    "minAngle": 450,
                    "maxAngle": 90,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_300,
                "Rotation_Inv_300": {
                    "minAngle": 480,
                    "maxAngle": 120,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\Rotation_Inv_330,
                "Rotation_Inv_330": {
                    "minAngle": 510,
                    "maxAngle": 150,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\MovementY,
                "MovementY": {
                    "type": "linear",
                    "source": "user",
                    "sourceIndex": 5,
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\MovementX,
                "MovementX": {
                    "sourceIndex": 4,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\PlaneDirection,
                "PlaneDirection": {
                    "type": "rotational",
                    "source": "heading",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 360,
                    "minAngle": 0,
                    "maxAngle": 360,
                    "aspectRatio": 1.02865
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP1_PosX,
                "WP1_PosX": {
                    "sourceIndex": 6,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP1_PosY,
                "WP1_PosY": {
                    "sourceIndex": 7,
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP2_PosX,
                "WP2_PosX": {
                    "sourceIndex": 8,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP2_PosY,
                "WP2_PosY": {
                    "sourceIndex": 9,
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP3_PosX,
                "WP3_PosX": {
                    "sourceIndex": 10,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP3_PosY,
                "WP3_PosY": {
                    "sourceIndex": 11,
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP4_PosX,
                "WP4_PosX": {
                    "sourceIndex": 12,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP4_PosY,
                "WP4_PosY": {
                    "sourceIndex": 13,
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP5_PosX,
                "WP5_PosX": {
                    "sourceIndex": 14,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP5_PosY,
                "WP5_PosY": {
                    "sourceIndex": 15,
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP6_PosX,
                "WP6_PosX": {
                    "sourceIndex": 16,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP6_PosY,
                "WP6_PosY": {
                    "sourceIndex": 17,
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP7_PosX,
                "WP7_PosX": {
                    "sourceIndex": 18,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP7_PosY,
                "WP7_PosY": {
                    "sourceIndex": 19,
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP8_PosX,
                "WP8_PosX": {
                    "sourceIndex": 20,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP8_PosY,
                "WP8_PosY": {
                    "sourceIndex": 21,
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP9_PosX,
                "WP9_PosX": {
                    "sourceIndex": 22,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP9_PosY,
                "WP9_PosY": {
                    "sourceIndex": 23,
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP10_PosX,
                "WP10_PosX": {
                    "sourceIndex": 24,
                    "maxPos": [-10,0],
                    "minPos": [10,0],
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Bones\WP10_PosY,
                "WP10_PosY": {
                    "sourceIndex": 25,
                    "type": "linear",
                    "source": "user",
                    "refreshRate": 0.1,
                    "min": 0,
                    "max": 1,
                    "sourceScale": 1,
                    "maxPos": [0,10],
                    "minPos": [0,-10]
                }
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw,
            "Draw": {
                "condition": "on",
                "alpha": 0.3,
                "color": [0,0.03,0.17],
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Static,
                "Draw_Static": {
                    "type": "line",
                    "width": 10,
                    "points": [["Static_Offset",[0,-0.699479],1],["Static_Offset",[0.118048,-0.688847],1],["Static_Offset",[0.23256,-0.657301],1],["Static_Offset",[0.34,-0.605749],1],["Static_Offset",[0.437104,-0.535801],1],["Static_Offset",[0.52088,-0.449625],1],["Static_Offset",[0.58888,-0.34974],1],["Static_Offset",[0.638996,-0.239222],1],["Static_Offset",[0.669664,-0.12143],1],["Static_Offset",[0.68,0],1],["Static_Offset",[0.669664,0.12143],1],["Static_Offset",[0.638996,0.239222],1],["Static_Offset",[0.58888,0.34974],1],["Static_Offset",[0.52088,0.449625],1],["Static_Offset",[0.437104,0.535801],1],["Static_Offset",[0.34,0.605749],1],["Static_Offset",[0.23256,0.657301],1],["Static_Offset",[0.118048,0.688847],1],["Static_Offset",[0,0.699479],1],["Static_Offset",[-0.118048,0.688847],1],["Static_Offset",[-0.23256,0.657301],1],["Static_Offset",[-0.34,0.605749],1],["Static_Offset",[-0.437104,0.535801],1],["Static_Offset",[-0.52088,0.449625],1],["Static_Offset",[-0.58888,0.34974],1],["Static_Offset",[-0.638996,0.239222],1],["Static_Offset",[-0.669664,0.12143],1],["Static_Offset",[-0.68,0],1],["Static_Offset",[-0.669664,-0.12143],1],["Static_Offset",[-0.638996,-0.239222],1],["Static_Offset",[-0.58888,-0.34974],1],["Static_Offset",[-0.52088,-0.449625],1],["Static_Offset",[-0.437104,-0.535801],1],["Static_Offset",[-0.34,-0.605749],1],["Static_Offset",[-0.23256,-0.657301],1],["Static_Offset",[-0.118048,-0.688847],1],["Static_Offset",[0,-0.699479],1],[],["Static_Offset",[0,-0.34974],1],["Static_Offset",[0.059024,-0.344424],1],["Static_Offset",[0.11628,-0.32865],1],["Static_Offset",[0.17,-0.302874],1],["Static_Offset",[0.218552,-0.267901],1],["Static_Offset",[0.26044,-0.224813],1],["Static_Offset",[0.29444,-0.17487],1],["Static_Offset",[0.319498,-0.119611],1],["Static_Offset",[0.334832,-0.0607148],1],["Static_Offset",[0.34,0],1],["Static_Offset",[0.334832,0.0607148],1],["Static_Offset",[0.319498,0.119611],1],["Static_Offset",[0.29444,0.17487],1],["Static_Offset",[0.26044,0.224813],1],["Static_Offset",[0.218552,0.267901],1],["Static_Offset",[0.17,0.302874],1],["Static_Offset",[0.11628,0.32865],1],["Static_Offset",[0.059024,0.344424],1],["Static_Offset",[0,0.34974],1],["Static_Offset",[-0.059024,0.344424],1],["Static_Offset",[-0.11628,0.32865],1],["Static_Offset",[-0.17,0.302874],1],["Static_Offset",[-0.218552,0.267901],1],["Static_Offset",[-0.26044,0.224813],1],["Static_Offset",[-0.29444,0.17487],1],["Static_Offset",[-0.319498,0.119611],1],["Static_Offset",[-0.334832,0.0607148],1],["Static_Offset",[-0.34,0],1],["Static_Offset",[-0.334832,-0.0607148],1],["Static_Offset",[-0.319498,-0.119611],1],["Static_Offset",[-0.29444,-0.17487],1],["Static_Offset",[-0.26044,-0.224813],1],["Static_Offset",[-0.218552,-0.267901],1],["Static_Offset",[-0.17,-0.302874],1],["Static_Offset",[-0.11628,-0.32865],1],["Static_Offset",[-0.059024,-0.344424],1],["Static_Offset",[0,-0.34974],1],[],["Static_Offset",[0,-0.7],1],["Static_Offset",[0,-0.76],1],["Static_Offset",[0.07,-0.76],1],["Static_Offset",[0.07,-0.83],1],["Static_Offset",[-0.07,-0.83],1],["Static_Offset",[-0.07,-0.76],1],["Static_Offset",[0,-0.76],1],[],["Static_Offset",1,["Rotation_0",0,0.695],1],["Static_Offset",1,["Rotation_0",0,0.655],1],[],["Static_Offset",1,["Rotation_10",0,0.695],1],["Static_Offset",1,["Rotation_10",0,0.67],1],[],["Static_Offset",1,["Rotation_20",0,0.695],1],["Static_Offset",1,["Rotation_20",0,0.67],1],[],["Static_Offset",1,["Rotation_30",0,0.695],1],["Static_Offset",1,["Rotation_30",0,0.655],1],[],["Static_Offset",1,["Rotation_40",0,0.695],1],["Static_Offset",1,["Rotation_40",0,0.67],1],[],["Static_Offset",1,["Rotation_50",0,0.695],1],["Static_Offset",1,["Rotation_50",0,0.67],1],[],["Static_Offset",1,["Rotation_60",0,0.695],1],["Static_Offset",1,["Rotation_60",0,0.655],1],[],["Static_Offset",1,["Rotation_70",0,0.695],1],["Static_Offset",1,["Rotation_70",0,0.67],1],[],["Static_Offset",1,["Rotation_80",0,0.695],1],["Static_Offset",1,["Rotation_80",0,0.67],1],[],["Static_Offset",1,["Rotation_90",0,0.695],1],["Static_Offset",1,["Rotation_90",0,0.655],1],[],["Static_Offset",1,["Rotation_100",0,0.695],1],["Static_Offset",1,["Rotation_100",0,0.67],1],[],["Static_Offset",1,["Rotation_110",0,0.695],1],["Static_Offset",1,["Rotation_110",0,0.67],1],[],["Static_Offset",1,["Rotation_120",0,0.695],1],["Static_Offset",1,["Rotation_120",0,0.655],1],[],["Static_Offset",1,["Rotation_130",0,0.695],1],["Static_Offset",1,["Rotation_130",0,0.67],1],[],["Static_Offset",1,["Rotation_140",0,0.695],1],["Static_Offset",1,["Rotation_140",0,0.67],1],[],["Static_Offset",1,["Rotation_150",0,0.695],1],["Static_Offset",1,["Rotation_150",0,0.655],1],[],["Static_Offset",1,["Rotation_160",0,0.695],1],["Static_Offset",1,["Rotation_160",0,0.67],1],[],["Static_Offset",1,["Rotation_170",0,0.695],1],["Static_Offset",1,["Rotation_170",0,0.67],1],[],["Static_Offset",1,["Rotation_180",0,0.695],1],["Static_Offset",1,["Rotation_180",0,0.655],1],[],["Static_Offset",1,["Rotation_190",0,0.695],1],["Static_Offset",1,["Rotation_190",0,0.67],1],[],["Static_Offset",1,["Rotation_200",0,0.695],1],["Static_Offset",1,["Rotation_200",0,0.67],1],[],["Static_Offset",1,["Rotation_210",0,0.695],1],["Static_Offset",1,["Rotation_210",0,0.655],1],[],["Static_Offset",1,["Rotation_220",0,0.695],1],["Static_Offset",1,["Rotation_220",0,0.67],1],[],["Static_Offset",1,["Rotation_230",0,0.695],1],["Static_Offset",1,["Rotation_230",0,0.67],1],[],["Static_Offset",1,["Rotation_240",0,0.695],1],["Static_Offset",1,["Rotation_240",0,0.655],1],[],["Static_Offset",1,["Rotation_250",0,0.695],1],["Static_Offset",1,["Rotation_250",0,0.67],1],[],["Static_Offset",1,["Rotation_260",0,0.695],1],["Static_Offset",1,["Rotation_260",0,0.67],1],[],["Static_Offset",1,["Rotation_270",0,0.695],1],["Static_Offset",1,["Rotation_270",0,0.655],1],[],["Static_Offset",1,["Rotation_280",0,0.695],1],["Static_Offset",1,["Rotation_280",0,0.67],1],[],["Static_Offset",1,["Rotation_290",0,0.695],1],["Static_Offset",1,["Rotation_290",0,0.67],1],[],["Static_Offset",1,["Rotation_300",0,0.695],1],["Static_Offset",1,["Rotation_300",0,0.655],1],[],["Static_Offset",1,["Rotation_310",0,0.695],1],["Static_Offset",1,["Rotation_310",0,0.67],1],[],["Static_Offset",1,["Rotation_320",0,0.695],1],["Static_Offset",1,["Rotation_320",0,0.67],1],[],["Static_Offset",1,["Rotation_330",0,0.695],1],["Static_Offset",1,["Rotation_330",0,0.655],1],[],["Static_Offset",1,["Rotation_340",0,0.695],1],["Static_Offset",1,["Rotation_340",0,0.67],1],[],["Static_Offset",1,["Rotation_350",0,0.695],1],["Static_Offset",1,["Rotation_350",0,0.67],1],[],[]]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_0_Text,
                "Rotation_0_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "N",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_0",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_0",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_0",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_30_Text,
                "Rotation_30_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "03",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_30",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_30",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_30",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_60_Text,
                "Rotation_60_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "06",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_60",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_60",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_60",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_90_Text,
                "Rotation_90_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "E",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_90",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_90",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_90",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_120_Text,
                "Rotation_120_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "12",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_120",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_120",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_120",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_150_Text,
                "Rotation_150_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "15",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_150",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_150",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_150",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_180_Text,
                "Rotation_180_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "S",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_180",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_180",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_180",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_210_Text,
                "Rotation_210_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "21",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_210",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_210",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_210",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_240_Text,
                "Rotation_240_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "24",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_240",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_240",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_240",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_270_Text,
                "Rotation_270_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "W",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_270",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_270",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_270",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_300_Text,
                "Rotation_300_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "30",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_300",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_300",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_300",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Rotation_330_Text,
                "Rotation_330_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "33",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": ["Static_Offset",1,["Rotation_Inv_330",0,-0.65],1],
                    "right": ["Static_Offset",1,["Rotation_Inv_330",-0.04,-0.65],1],
                    "down": ["Static_Offset",1,["Rotation_Inv_330",0,-0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\BackgroundBlack,
                "BackgroundBlack": {
                    "color": [0,0,0],
                    "alpha": 1,
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\BackgroundBlack\Static,
                    "Static": {
                        "type": "polygon",
                        "points": [[[[0.68,0.55],1],[[0.75,0.55],1],[[0.75,0.6],1],[[0.68,0.6],1]],[[[0.83,0.2],1],[[0.92,0.2],1],[[0.92,0.3],1],[[0.83,0.3],1]]]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White,
                "Draw_White": {
                    "color": [1,1,1],
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\HeadingText,
                    "HeadingText": {
                        "type": "text",
                        "source": "heading",
                        "sourceScale": 1,
                        "sourceLength": 3,
                        "refreshRate": 0.1,
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,0.03],1],
                        "right": [[0.56,0.03],1],
                        "down": [[0.5,0.09],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\Range_Text,
                    "Range_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "36",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.92,0.23],1],
                        "right": [[0.99,0.23],1],
                        "down": [[0.92,0.3],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\MFlare_Text,
                    "MFlare_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "LPE4",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.86,0.03],1],
                        "right": [[0.91,0.03],1],
                        "down": [[0.86,0.08],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\RangesData1_Text,
                    "RangesData1_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "346/97",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.01,0.07],1],
                        "right": [[0.05,0.07],1],
                        "down": [[0.01,0.11],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\Pos_Text,
                    "Pos_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "GRID",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.79,0.84],1],
                        "right": [[0.83,0.84],1],
                        "down": [[0.79,0.88],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\CordX,
                    "CordX": {
                        "type": "text",
                        "source": "coordinateX",
                        "sourceScale": 0.01,
                        "sourceLength": 3,
                        "sourceOffset": -0.5,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.79,0.88],1],
                        "right": [[0.83,0.88],1],
                        "down": [[0.79,0.92],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\CordY,
                    "CordY": {
                        "source": "coordinateY",
                        "pos": [["0.79+0.07",0.88],1],
                        "right": [[0.9,0.88],1],
                        "down": [["0.79+0.07",0.92],1],
                        "type": "text",
                        "sourceScale": 0.01,
                        "sourceLength": 3,
                        "sourceOffset": -0.5,
                        "align": "right",
                        "scale": 1
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP,
                    "WP": {
                        "condition": "wpvalid",
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WPdist,
                        "WPdist": {
                            "type": "text",
                            "source": "wpdist",
                            "sourceScale": 0.001,
                            "sourcePrecision": 1,
                            "align": "left",
                            "scale": 1,
                            "pos": [["0.79+0.15",0.915],1],
                            "right": [[0.98,0.915],1],
                            "down": [["0.79+0.15",0.955],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WPIndex,
                        "WPIndex": {
                            "type": "text",
                            "source": "wpIndex",
                            "sourceScale": 1,
                            "sourceLength": 2,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.83,0.915],1],
                            "right": [[0.87,0.915],1],
                            "down": [[0.83,0.955],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WPstatic,
                        "WPstatic": {
                            "type": "text",
                            "source": "static",
                            "text": "W",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "right",
                            "pos": [[0.79,0.915],1],
                            "right": [[0.83,0.915],1],
                            "down": [[0.79,0.955],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WPAuto,
                        "WPAuto": {
                            "type": "text",
                            "source": "static",
                            "text": "A",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "right",
                            "pos": [["0.790 +0.035",0.95],1],
                            "right": [[0.865,0.95],1],
                            "down": [["0.790 +0.035",0.99],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WPKM,
                        "WPKM": {
                            "type": "text",
                            "source": "static",
                            "text": "KM",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "right",
                            "pos": [["0.790 +0.16",0.915],1],
                            "right": [[0.99,0.915],1],
                            "down": [["0.790 +0.16",0.955],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WPTime,
                        "WPTime": {
                            "type": "text",
                            "source": "static",
                            "text": "-:--",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "right",
                            "pos": [["0.790 +0.11",0.95],1],
                            "right": [[0.94,0.95],1],
                            "down": [["0.790 +0.11",0.99],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP1,
                        "WP1": {
                            "condition": "user6>=0",
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP1\CurrentWaypoint,
                            "CurrentWaypoint": {
                                "color": [0.9,0,0],
                                "condition": "1-WPIndex",
                                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP1\CurrentWaypoint\WaypointShape,
                                "WaypointShape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP1\WaypointShape,
                            "WaypointShape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0,-0.0205729],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.02,0],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.01,0.0178161],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0,0.0205729],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.02,0],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP1_PosX",1,"WP1_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP2,
                        "WP2": {
                            "condition": "user8>=0",
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP2\CurrentWaypoint,
                            "CurrentWaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=1)*(WPIndex<=1)",
                                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP2\CurrentWaypoint\WaypointShape,
                                "WaypointShape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP2\WaypointShape,
                            "WaypointShape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,0.0205729],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.02,0],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP2_PosX",1,"WP2_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP1_PosX",1,"WP1_PosY",1,["PlaneDirection",0,0],1],["WP2_PosX",1,"WP2_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP3,
                        "WP3": {
                            "condition": "user10>=0",
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP3\CurrentWaypoint,
                            "CurrentWaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=2)*(WPIndex<=2)",
                                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP3\CurrentWaypoint\WaypointShape,
                                "WaypointShape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,-0.0205729],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.02,0],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01,0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,0.0205729],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.02,0],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP3\WaypointShape,
                            "WaypointShape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,-0.0205729],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.02,0],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.01,0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,0.0205729],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.02,0],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP3_PosX",1,"WP3_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP2_PosX",1,"WP2_PosY",1,["PlaneDirection",0,0],1],["WP3_PosX",1,"WP3_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP4,
                        "WP4": {
                            "condition": "user12>=0",
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP4\CurrentWaypoint,
                            "CurrentWaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=3)*(WPIndex<=3)",
                                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP4\CurrentWaypoint\WaypointShape,
                                "WaypointShape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,-0.0205729],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.02,0],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01,0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,0.0205729],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.02,0],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP4\WaypointShape,
                            "WaypointShape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,-0.0205729],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.02,0],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.01,0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,0.0205729],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.02,0],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP4_PosX",1,"WP4_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP3_PosX",1,"WP3_PosY",1,["PlaneDirection",0,0],1],["WP4_PosX",1,"WP4_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP5,
                        "WP5": {
                            "condition": "user14>=0",
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP5\CurrentWaypoint,
                            "CurrentWaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=4)*(WPIndex<=4)",
                                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP5\CurrentWaypoint\WaypointShape,
                                "WaypointShape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP5\WaypointShape,
                            "WaypointShape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP4_PosX",1,"WP4_PosY",1,["PlaneDirection",0,0],1],["WP5_PosX",1,"WP5_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP6,
                        "WP6": {
                            "condition": "user16>=0",
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP6\CurrentWaypoint,
                            "CurrentWaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=5)*(WPIndex<=5)",
                                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP6\CurrentWaypoint\WaypointShape,
                                "WaypointShape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,0.0205729],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.02,0],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP5_PosX",1,"WP5_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP6\WaypointShape,
                            "WaypointShape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0,-0.0205729],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.02,0],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.01,0.0178161],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0,0.0205729],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.02,0],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP6_PosX",1,"WP6_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP5_PosX",1,"WP5_PosY",1,["PlaneDirection",0,0],1],["WP6_PosX",1,"WP6_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP7,
                        "WP7": {
                            "condition": "user18>=0",
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP7\CurrentWaypoint,
                            "CurrentWaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=6)*(WPIndex<=6)",
                                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP7\CurrentWaypoint\WaypointShape,
                                "WaypointShape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,-0.0205729],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.02,0],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01,0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,0.0205729],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.02,0],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP7\WaypointShape,
                            "WaypointShape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,-0.0205729],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.02,0],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.01,0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,0.0205729],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.02,0],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP7_PosX",1,"WP7_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP6_PosX",1,"WP6_PosY",1,["PlaneDirection",0,0],1],["WP7_PosX",1,"WP7_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP8,
                        "WP8": {
                            "condition": "user20>=0",
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP8\CurrentWaypoint,
                            "CurrentWaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=7)*(WPIndex<=7)",
                                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP8\CurrentWaypoint\WaypointShape,
                                "WaypointShape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,-0.0205729],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.02,0],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01,0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,0.0205729],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.02,0],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP8\WaypointShape,
                            "WaypointShape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,-0.0205729],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.02,0],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.01,0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,0.0205729],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.02,0],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP8_PosX",1,"WP8_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP7_PosX",1,"WP7_PosY",1,["PlaneDirection",0,0],1],["WP8_PosX",1,"WP8_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP9,
                        "WP9": {
                            "condition": "user22>=0",
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP9\CurrentWaypoint,
                            "CurrentWaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=8)*(WPIndex<=8)",
                                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP9\CurrentWaypoint\WaypointShape,
                                "WaypointShape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,-0.0205729],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.02,0],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01,0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,0.0205729],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.02,0],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP9\WaypointShape,
                            "WaypointShape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,-0.0205729],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.02,0],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.01,0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,0.0205729],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.02,0],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP9_PosX",1,"WP9_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP8_PosX",1,"WP8_PosY",1,["PlaneDirection",0,0],1],["WP9_PosX",1,"WP9_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP10,
                        "WP10": {
                            "condition": "user24>=0",
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP10\CurrentWaypoint,
                            "CurrentWaypoint": {
                                "color": [0.9,0,0],
                                "condition": "(WPIndex>=9)*(WPIndex<=9)",
                                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP10\CurrentWaypoint\WaypointShape,
                                "WaypointShape": {
                                    "width": 22,
                                    "type": "line",
                                    "points": [["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,-0.0205729],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.02,0],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01,0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,0.0205729],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.02,0],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,-0.0205729],1],[]]
                                }
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_White\WP\WP10\WaypointShape,
                            "WaypointShape": {
                                "width": 6,
                                "type": "line",
                                "points": [["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,-0.0205729],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.003472,-0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.00684,-0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01,-0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.012856,-0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01532,-0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01732,-0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.018794,-0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.019696,-0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.02,0],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.019696,0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.018794,0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01732,0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01532,0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.012856,0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.01,0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.00684,0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0.003472,0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,0.0205729],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.003472,0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.00684,0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01,0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.012856,0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01532,0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01732,0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.018794,0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.019696,0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.02,0],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.019696,-0.00357146],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.018794,-0.00703594],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01732,-0.0102865],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01532,-0.0132243],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.012856,-0.0157589],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.01,-0.0178161],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.00684,-0.0193324],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",-0.003472,-0.0202602],1],["WP10_PosX",1,"WP10_PosY",["PlaneDirection",0,-0.0205729],1],[],["WP9_PosX",1,"WP9_PosY",1,["PlaneDirection",0,0],1],["WP10_PosX",1,"WP10_PosY",1,["PlaneDirection",0,0],1]]
                            }
                        }
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Purple,
                "Draw_Purple": {
                    "color": [0.67,0.06,0.32],
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Purple\RangesData1_Text,
                    "RangesData1_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "348/111 BE1",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.01,0.03],1],
                        "right": [[0.05,0.03],1],
                        "down": [[0.01,0.07],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Yellow,
                "Draw_Yellow": {
                    "color": [0.99,0.86,0.14],
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Yellow\NoTarget,
                    "NoTarget": {
                        "condition": "targetDist<=0",
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Yellow\NoTarget\Target_Text,
                        "Target_Text": {
                            "type": "text",
                            "source": "static",
                            "text": "NO TARGET",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0.18,0.85],1],
                            "right": [[0.22,0.85],1],
                            "down": [[0.18,0.89],1]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Yellow\TargetInfo,
                    "TargetInfo": {
                        "condition": "targetDist>=1",
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Yellow\TargetInfo\Dist_Text,
                        "Dist_Text": {
                            "type": "text",
                            "source": "static",
                            "text": "DIST:",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "right",
                            "pos": [[0.02,0.85],1],
                            "right": [[0.06,0.85],1],
                            "down": [[0.02,0.89],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Yellow\TargetInfo\CordX,
                        "CordX": {
                            "type": "text",
                            "source": "targetDist",
                            "sourceScale": 0.001,
                            "sourcePrecision": 1,
                            "sourceLength": 1,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.15,0.85],1],
                            "right": [[0.19,0.85],1],
                            "down": [[0.15,0.89],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Yellow\TargetInfo\SPD_Text,
                        "SPD_Text": {
                            "type": "text",
                            "source": "static",
                            "text": "SPD:",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "right",
                            "pos": [[0.02,0.89],1],
                            "right": [[0.06,0.89],1],
                            "down": [[0.02,0.93],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Yellow\TargetInfo\SpeedSource,
                        "SpeedSource": {
                            "type": "text",
                            "source": "LarTargetSpeed",
                            "sourceScale": 1,
                            "sourcePrecision": 0,
                            "sourceLength": 1,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.15,0.89],1],
                            "right": [[0.19,0.89],1],
                            "down": [[0.15,0.93],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Yellow\TargetInfo\ATL_Text,
                        "ATL_Text": {
                            "type": "text",
                            "source": "static",
                            "text": "ATL:",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "right",
                            "pos": [[0.02,0.93],1],
                            "right": [[0.06,0.93],1],
                            "down": [[0.02,0.97],1]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Draw_Yellow\TargetInfo\HeightSource,
                        "HeightSource": {
                            "type": "text",
                            "source": "targetHeight",
                            "sourceScale": 1,
                            "sourcePrecision": 0,
                            "sourceLength": 1,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.15,0.93],1],
                            "right": [[0.19,0.93],1],
                            "down": [[0.15,0.97],1]
                        }
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\Range_Text,
                "Range_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "18",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.74,0.55],1],
                    "right": [[0.79,0.55],1],
                    "down": [[0.74,0.6],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\RadarOn,
                "RadarOn": {
                    "condition": "activeSensorsOn",
                    "color": [1,1,1],
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\RadarOn\Draw_Static,
                    "Draw_Static": {
                        "type": "line",
                        "width": 6,
                        "points": [[[0.5,0.83],1],[[0.681865,0.721992],1],["Static_Offset2",[0.172022,-0.123901],1],["Static_Offset2",[0.160869,-0.138852],1],["Static_Offset2",[0.148492,-0.152746],1],["Static_Offset2",[0.134985,-0.165478],1],["Static_Offset2",[0.120451,-0.17695],1],[[0.605,0.642925],1],[[0.815,0.268775],1],["Static_Offset2",[0.26625,-0.58733],1],["Static_Offset2",[0.215473,-0.608965],1],["Static_Offset2",[0.163056,-0.625965],1],["Static_Offset2",[0.109398,-0.638202],1],["Static_Offset2",[0.0549081,-0.645581],1],["Static_Offset2",[0,-0.648047],1],["Static_Offset2",[-0.0549081,-0.645581],1],["Static_Offset2",[-0.109398,-0.638202],1],["Static_Offset2",[-0.163056,-0.625965],1],["Static_Offset2",[-0.215473,-0.608965],1],["Static_Offset2",[-0.26625,-0.58733],1],["Static_Offset2",[-0.315,-0.561225],1],[[0.395,0.642925],1],[[0.185,0.268775],1],[],["Static_Offset2",[-0.105,-0.187075],1],["Static_Offset2",[-0.120451,-0.17695],1],["Static_Offset2",[-0.134985,-0.165478],1],["Static_Offset2",[-0.148492,-0.152746],1],["Static_Offset2",[-0.160869,-0.138852],1],["Static_Offset2",[-0.172022,-0.123901],1],["Static_Offset2",[-0.181865,-0.108008],1],[],[[0.5,0.83],1],[[0.318135,0.721992],1],[]]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup,
                "SensorGroup": {
                    "color": [1,1,1],
                    "alpha": 1,
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor,
                    "Sensor": {
                        "type": "sensor",
                        "pos": ["Sensor_Offset",["0+-0.17","0+-0.17"],1],
                        "down": ["Sensor_Offset",["1--0.17","1--0.17"],1],
                        "showTargetTypes": "2+4+8+16+32+64+128+256+512+1024",
                        "width": 4,
                        "sensorLineType": 0,
                        "sensorLineWidth": 3,
                        "targetLineWidth": -0.00192,
                        "targetLineLength": 0.02,
                        "range": 36000,
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\MissileThreat,
                        "MissileThreat": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\MissileThreat\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0205729],1],[[0.003472,-0.0202602],1],[[0.00684,-0.0193324],1],[[0.01,-0.0178161],1],[[0.012856,-0.0157589],1],[[0.01532,-0.0132243],1],[[0.01732,-0.0102865],1],[[0.018794,-0.00703594],1],[[0.019696,-0.00357146],1],[[0.02,0],1],[[0.019696,0.00357146],1],[[0.018794,0.00703594],1],[[0.01732,0.0102865],1],[[0.01532,0.0132243],1],[[0.012856,0.0157589],1],[[0.01,0.0178161],1],[[0.00684,0.0193324],1],[[0.003472,0.0202602],1],[[0,0.0205729],1],[[-0.003472,0.0202602],1],[[-0.00684,0.0193324],1],[[-0.01,0.0178161],1],[[-0.012856,0.0157589],1],[[-0.01532,0.0132243],1],[[-0.01732,0.0102865],1],[[-0.018794,0.00703594],1],[[-0.019696,0.00357146],1],[[-0.02,0],1],[[-0.019696,-0.00357146],1],[[-0.018794,-0.00703594],1],[[-0.01732,-0.0102865],1],[[-0.01532,-0.0132243],1],[[-0.012856,-0.0157589],1],[[-0.01,-0.0178161],1],[[-0.00684,-0.0193324],1],[[-0.003472,-0.0202602],1],[[0,-0.0205729],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\MissileThreat\TextM,
                            "TextM": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\lockingThreat,
                        "lockingThreat": {
                            "color": [1,0.3,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\lockingThreat\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\markingThreat,
                        "markingThreat": {
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\markingThreat\TargetLines
                            "TargetLines": {
                                "type": "line",
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            },
                            "color": [1,0.3,0]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\rwr,
                        "rwr": {
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\rwr\TargetLines
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\rwrFriendly,
                        "rwrFriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\rwrFriendly\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\rwrEnemy,
                        "rwrEnemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\rwrEnemy\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\rwrGroup,
                        "rwrGroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\rwrGroup\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0.02,0],1],[[0,0.0205729],1],[[-0.02,0],1],[[0,-0.0205729],1],[[0.02,0],1]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\rwrDestroyed,
                        "rwrDestroyed": {
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\markedTarget,
                        "markedTarget": {
                            "color": [1,0.3,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\markedTarget\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 3,
                                "points": [[[-0.017,-0.017487],1],[[-0.01,-0.017487],1],[],[[0.017,-0.017487],1],[[0.01,-0.017487],1],[],[[-0.017,-0.017487],1],[[-0.017,-0.0102865],1],[],[[0.017,-0.017487],1],[[0.017,-0.0102865],1],[],[[-0.017,0.017487],1],[[-0.01,0.017487],1],[],[[0.017,0.017487],1],[[0.01,0.017487],1],[],[[-0.017,0.017487],1],[[-0.017,0.0102865],1],[],[[0.017,0.017487],1],[[0.017,0.0102865],1],[]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\assignedTarget,
                        "assignedTarget": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\assignedTarget\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 3,
                                "points": [[[-0.017,-0.017487],1],[[-0.01,-0.017487],1],[],[[0.017,-0.017487],1],[[0.01,-0.017487],1],[],[[-0.017,-0.017487],1],[[-0.017,-0.0102865],1],[],[[0.017,-0.017487],1],[[0.017,-0.0102865],1],[],[[-0.017,0.017487],1],[[-0.01,0.017487],1],[],[[0.017,0.017487],1],[[0.01,0.017487],1],[],[[-0.017,0.017487],1],[[-0.017,0.0102865],1],[],[[0.017,0.017487],1],[[0.017,0.0102865],1],[]]
                            }
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\target,
                        "target": {
                            "color": [1,1,1],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\target\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\target\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetFriendly,
                        "targetFriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetFriendly\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetFriendly\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetEnemy,
                        "targetEnemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetEnemy\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetEnemy\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroup,
                        "targetGroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroup\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroup\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetDestroyed,
                        "targetDestroyed": {
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGround,
                        "targetGround": {
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGround\TargetLines
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGround\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundFriendly,
                        "targetGroundFriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundFriendly\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundFriendly\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundEnemy,
                        "targetGroundEnemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundEnemy\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundEnemy\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundGroup,
                        "targetGroundGroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundGroup\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundGroup\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundDestroyed,
                        "targetGroundDestroyed": {
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemote,
                        "targetGroundRemote": {
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemote\TargetLines
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemote\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemoteFriendly,
                        "targetGroundRemoteFriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemoteFriendly\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemoteFriendly\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemoteEnemy,
                        "targetGroundRemoteEnemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemoteEnemy\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemoteEnemy\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemoteGroup,
                        "targetGroundRemoteGroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemoteGroup\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemoteGroup\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetGroundRemoteDestroyed,
                        "targetGroundRemoteDestroyed": {
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaser,
                        "targetLaser": {
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaser\TargetLines
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaser\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaserFriendly,
                        "targetLaserFriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaserFriendly\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaserFriendly\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaserEnemy,
                        "targetLaserEnemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaserEnemy\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaserEnemy\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaserGroup,
                        "targetLaserGroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaserGroup\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetLaserGroup\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVG,
                        "targetNVG": {
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVG\TargetLines
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVG\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVGFriendly,
                        "targetNVGFriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVGFriendly\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVGFriendly\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVGEnemy,
                        "targetNVGEnemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVGEnemy\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVGEnemy\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVGGroup,
                        "targetNVGGroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVGGroup\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetNVGGroup\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetMan,
                        "targetMan": {
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetMan\TargetLines
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetMan\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManFriendly,
                        "targetManFriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManFriendly\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManFriendly\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManEnemy,
                        "targetManEnemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManEnemy\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManEnemy\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManGroup,
                        "targetManGroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManGroup\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManGroup\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemote,
                        "targetManRemote": {
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemote\TargetLines
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemote\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemoteFriendly,
                        "targetManRemoteFriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemoteFriendly\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemoteFriendly\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemoteEnemy,
                        "targetManRemoteEnemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemoteEnemy\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemoteEnemy\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemoteGroup,
                        "targetManRemoteGroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemoteGroup\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetManRemoteGroup\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAir,
                        "targetAir": {
                            "color": [1,1,1],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAir\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAir\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirFriendly,
                        "targetAirFriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirFriendly\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirFriendly\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirEnemy,
                        "targetAirEnemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirEnemy\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirEnemy\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirGroup,
                        "targetAirGroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirGroup\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirGroup\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirDestroyed,
                        "targetAirDestroyed": {
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemote,
                        "targetAirRemote": {
                            "color": [1,1,1],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemote\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemote\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemoteFriendly,
                        "targetAirRemoteFriendly": {
                            "color": [0,1,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemoteFriendly\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemoteFriendly\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemoteEnemy,
                        "targetAirRemoteEnemy": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemoteEnemy\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemoteEnemy\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemoteGroup,
                        "targetAirRemoteGroup": {
                            "color": [1,0,0],
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemoteGroup\TargetLines,
                            "TargetLines": {
                                "type": "line",
                                "width": 2,
                                "points": [[[0,-0.0133724],1],[[0.0022568,-0.0131691],1],[[0.004446,-0.012566],1],[[0.0065,-0.0115805],1],[[0.0083564,-0.0102433],1],[[0.009958,-0.00859578],1],[[0.011258,-0.0066862],1],[[0.0122161,-0.00457336],1],[[0.0128024,-0.00232145],1],[[0.013,0],1],[[0.0128024,0.00232145],1],[[0.0122161,0.00457336],1],[[0.011258,0.0066862],1],[[0.009958,0.00859578],1],[[0.0083564,0.0102433],1],[[0.0065,0.0115805],1],[[0.004446,0.012566],1],[[0.0022568,0.0131691],1],[[0,0.0133724],1],[[-0.0022568,0.0131691],1],[[-0.004446,0.012566],1],[[-0.0065,0.0115805],1],[[-0.0083564,0.0102433],1],[[-0.009958,0.00859578],1],[[-0.011258,0.0066862],1],[[-0.0122161,0.00457336],1],[[-0.0128024,0.00232145],1],[[-0.013,0],1],[[-0.0128024,-0.00232145],1],[[-0.0122161,-0.00457336],1],[[-0.011258,-0.0066862],1],[[-0.009958,-0.00859578],1],[[-0.0083564,-0.0102433],1],[[-0.0065,-0.0115805],1],[[-0.004446,-0.012566],1],[[-0.0022568,-0.0131691],1],[[0,-0.0133724],1]]
                            },
                            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemoteGroup\TextA,
                            "TextA": {
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
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_4\Draw\SensorGroup\Sensor\targetAirRemoteDestroyed,
                        "targetAirRemoteDestroyed": {
                        }
                    }
                }
            }
        },
        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5,
        "MFD_5": {
            "topLeft": "MFD_5_TL",
            "topRight": "MFD_5_TR",
            "bottomLeft": "MFD_5_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\material,
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones,
            "Bones": {
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Sensor_Offset
                "Sensor_Offset": {
                    "type": "fixed",
                    "pos": [0,0.03]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Static_Offset,
                "Static_Offset": {
                    "type": "fixed",
                    "pos": [0.5,0.53]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_0,
                "Rotation_0": {
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "minAngle": 0,
                    "maxAngle": -360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_30,
                "Rotation_30": {
                    "minAngle": 30,
                    "maxAngle": -330,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_60,
                "Rotation_60": {
                    "minAngle": 60,
                    "maxAngle": -300,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_90,
                "Rotation_90": {
                    "minAngle": 90,
                    "maxAngle": -270,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_120,
                "Rotation_120": {
                    "minAngle": 120,
                    "maxAngle": -240,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_150,
                "Rotation_150": {
                    "minAngle": 150,
                    "maxAngle": -210,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_180,
                "Rotation_180": {
                    "minAngle": 180,
                    "maxAngle": -180,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_210,
                "Rotation_210": {
                    "minAngle": 210,
                    "maxAngle": -150,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_240,
                "Rotation_240": {
                    "minAngle": 240,
                    "maxAngle": -120,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_270,
                "Rotation_270": {
                    "minAngle": 270,
                    "maxAngle": -90,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_300,
                "Rotation_300": {
                    "minAngle": 300,
                    "maxAngle": -60,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_330,
                "Rotation_330": {
                    "minAngle": 330,
                    "maxAngle": -30,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "min": 0,
                    "max": 360,
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_Inv_0,
                "Rotation_Inv_0": {
                    "min": 0,
                    "max": 360,
                    "minAngle": 180,
                    "maxAngle": -180,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_Inv_90,
                "Rotation_Inv_90": {
                    "minAngle": 270,
                    "maxAngle": -90,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_Inv_180,
                "Rotation_Inv_180": {
                    "minAngle": 360,
                    "maxAngle": 0,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1.08148
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Bones\Rotation_Inv_270,
                "Rotation_Inv_270": {
                    "minAngle": 450,
                    "maxAngle": 90,
                    "min": 0,
                    "max": 360,
                    "pos0": [0,0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "heading",
                    "aspectRatio": 1.08148
                }
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw,
            "Draw": {
                "condition": "on",
                "alpha": 0.5,
                "color": [1,1,1],
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\Draw_Blue,
                "Draw_Blue": {
                    "color": [0,0.03,0.17],
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\Draw_Blue\Draw_Static,
                    "Draw_Static": {
                        "type": "line",
                        "width": 10,
                        "points": [["Static_Offset",[0,-0.410963],1],["Static_Offset",[0.065968,-0.404716],1],["Static_Offset",[0.12996,-0.386182],1],["Static_Offset",[0.19,-0.355894],1],["Static_Offset",[0.244264,-0.314798],1],["Static_Offset",[0.29108,-0.264167],1],["Static_Offset",[0.32908,-0.205481],1],["Static_Offset",[0.357086,-0.140549],1],["Static_Offset",[0.374224,-0.0713432],1],["Static_Offset",[0.38,0],1],["Static_Offset",[0.374224,0.0713432],1],["Static_Offset",[0.357086,0.140549],1],["Static_Offset",[0.32908,0.205481],1],["Static_Offset",[0.29108,0.264167],1],["Static_Offset",[0.244264,0.314798],1],["Static_Offset",[0.19,0.355894],1],["Static_Offset",[0.12996,0.386182],1],["Static_Offset",[0.065968,0.404716],1],["Static_Offset",[0,0.410963],1],["Static_Offset",[-0.065968,0.404716],1],["Static_Offset",[-0.12996,0.386182],1],["Static_Offset",[-0.19,0.355894],1],["Static_Offset",[-0.244264,0.314798],1],["Static_Offset",[-0.29108,0.264167],1],["Static_Offset",[-0.32908,0.205481],1],["Static_Offset",[-0.357086,0.140549],1],["Static_Offset",[-0.374224,0.0713432],1],["Static_Offset",[-0.38,0],1],["Static_Offset",[-0.374224,-0.0713432],1],["Static_Offset",[-0.357086,-0.140549],1],["Static_Offset",[-0.32908,-0.205481],1],["Static_Offset",[-0.29108,-0.264167],1],["Static_Offset",[-0.244264,-0.314798],1],["Static_Offset",[-0.19,-0.355894],1],["Static_Offset",[-0.12996,-0.386182],1],["Static_Offset",[-0.065968,-0.404716],1],["Static_Offset",[0,-0.410963],1],[],["Static_Offset",[0,-0.173037],1],["Static_Offset",[0.027776,-0.170407],1],["Static_Offset",[0.05472,-0.162603],1],["Static_Offset",[0.08,-0.14985],1],["Static_Offset",[0.102848,-0.132546],1],["Static_Offset",[0.12256,-0.111228],1],["Static_Offset",[0.13856,-0.0865185],1],["Static_Offset",[0.150352,-0.0591787],1],["Static_Offset",[0.157568,-0.0300392],1],["Static_Offset",[0.16,0],1],["Static_Offset",[0.157568,0.0300392],1],["Static_Offset",[0.150352,0.0591787],1],["Static_Offset",[0.13856,0.0865185],1],["Static_Offset",[0.12256,0.111228],1],["Static_Offset",[0.102848,0.132546],1],["Static_Offset",[0.08,0.14985],1],["Static_Offset",[0.05472,0.162603],1],["Static_Offset",[0.027776,0.170407],1],["Static_Offset",[0,0.173037],1],["Static_Offset",[-0.027776,0.170407],1],["Static_Offset",[-0.05472,0.162603],1],["Static_Offset",[-0.08,0.14985],1],["Static_Offset",[-0.102848,0.132546],1],["Static_Offset",[-0.12256,0.111228],1],["Static_Offset",[-0.13856,0.0865185],1],["Static_Offset",[-0.150352,0.0591787],1],["Static_Offset",[-0.157568,0.0300392],1],["Static_Offset",[-0.16,0],1],["Static_Offset",[-0.157568,-0.0300392],1],["Static_Offset",[-0.150352,-0.0591787],1],["Static_Offset",[-0.13856,-0.0865185],1],["Static_Offset",[-0.12256,-0.111228],1],["Static_Offset",[-0.102848,-0.132546],1],["Static_Offset",[-0.08,-0.14985],1],["Static_Offset",[-0.05472,-0.162603],1],["Static_Offset",[-0.027776,-0.170407],1],["Static_Offset",[0,-0.173037],1],[],["Static_Offset",[0,-0.41],1],["Static_Offset",[0,-0.44],1],["Static_Offset",[0.07,-0.44],1],["Static_Offset",[0.07,-0.51],1],["Static_Offset",[-0.07,-0.51],1],["Static_Offset",[-0.07,-0.44],1],["Static_Offset",[0,-0.44],1],[],["Static_Offset",1,["Rotation_0",0,0.383926],1],["Static_Offset",1,["Rotation_0",0,0.340667],1],[],["Static_Offset",1,["Rotation_30",0,0.383926],1],["Static_Offset",1,["Rotation_30",0,0.340667],1],[],["Static_Offset",1,["Rotation_60",0,0.383926],1],["Static_Offset",1,["Rotation_60",0,0.340667],1],[],["Static_Offset",1,["Rotation_90",0,0.383926],1],["Static_Offset",1,["Rotation_90",0,0.340667],1],[],["Static_Offset",1,["Rotation_120",0,0.383926],1],["Static_Offset",1,["Rotation_120",0,0.340667],1],[],["Static_Offset",1,["Rotation_150",0,0.383926],1],["Static_Offset",1,["Rotation_150",0,0.340667],1],[],["Static_Offset",1,["Rotation_180",0,0.383926],1],["Static_Offset",1,["Rotation_180",0,0.340667],1],[],["Static_Offset",1,["Rotation_210",0,0.383926],1],["Static_Offset",1,["Rotation_210",0,0.340667],1],[],["Static_Offset",1,["Rotation_240",0,0.383926],1],["Static_Offset",1,["Rotation_240",0,0.340667],1],[],["Static_Offset",1,["Rotation_270",0,0.383926],1],["Static_Offset",1,["Rotation_270",0,0.340667],1],[],["Static_Offset",1,["Rotation_300",0,0.383926],1],["Static_Offset",1,["Rotation_300",0,0.340667],1],[],["Static_Offset",1,["Rotation_330",0,0.383926],1],["Static_Offset",1,["Rotation_330",0,0.340667],1],[],[]]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\Draw_Blue\Rotation_0_Text,
                    "Rotation_0_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "N",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": ["Static_Offset",1,["Rotation_Inv_0",0,-0.345],1],
                        "right": ["Static_Offset",1,["Rotation_Inv_0",-0.04,-0.345],1],
                        "down": ["Static_Offset",1,["Rotation_Inv_0",0,-0.295],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\Draw_Blue\Rotation_90_Text,
                    "Rotation_90_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "E",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": ["Static_Offset",1,["Rotation_Inv_90",0,-0.345],1],
                        "right": ["Static_Offset",1,["Rotation_Inv_90",-0.04,-0.345],1],
                        "down": ["Static_Offset",1,["Rotation_Inv_90",0,-0.295],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\Draw_Blue\Rotation_180_Text,
                    "Rotation_180_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "S",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": ["Static_Offset",1,["Rotation_Inv_180",0,-0.345],1],
                        "right": ["Static_Offset",1,["Rotation_Inv_180",-0.04,-0.345],1],
                        "down": ["Static_Offset",1,["Rotation_Inv_180",0,-0.295],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\Draw_Blue\Rotation_270_Text,
                    "Rotation_270_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "W",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": ["Static_Offset",1,["Rotation_Inv_270",0,-0.345],1],
                        "right": ["Static_Offset",1,["Rotation_Inv_270",-0.04,-0.345],1],
                        "down": ["Static_Offset",1,["Rotation_Inv_270",0,-0.295],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\BackgroundBlack,
                "BackgroundBlack": {
                    "color": [0,0,0],
                    "alpha": 1,
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\BackgroundBlack\Static,
                    "Static": {
                        "type": "polygon",
                        "points": [[[[0.6,0.4],1],[[0.67,0.4],1],[[0.67,0.45],1],[[0.6,0.45],1]],[[[0.68,0.21],1],[[0.81,0.21],1],[[0.81,0.29],1],[[0.68,0.29],1]]]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\HeadingText,
                "HeadingText": {
                    "type": "text",
                    "source": "heading",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "refreshRate": 0.1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.5,0.03],1],
                    "right": [[0.56,0.03],1],
                    "down": [[0.5,0.09],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\Range_Text,
                "Range_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "18A",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.81,0.22],1],
                    "right": [[0.88,0.22],1],
                    "down": [[0.81,0.29],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\MFD1_Text,
                "MFD1_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "LPE4",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.86,0.03],1],
                    "right": [[0.91,0.03],1],
                    "down": [[0.86,0.08],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\Draw_Blue2,
                "Draw_Blue2": {
                    "color": [0,0.03,0.17],
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\Draw_Blue2\Range_Text,
                    "Range_Text": {
                        "type": "text",
                        "source": "static",
                        "text": "9",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.64,0.4],1],
                        "right": [[0.69,0.4],1],
                        "down": [[0.64,0.45],1]
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR,
                "RWR": {
                    "type": "sensor",
                    "pos": ["Sensor_Offset",["0+-0.32","0+-0.32"],1],
                    "down": ["Sensor_Offset",["1--0.32","1--0.32"],1],
                    "showTargetTypes": "2 + 4 + 8 + 32 + 64 + 128 + 256",
                    "width": 4,
                    "sensorLineType": 1,
                    "sensorLineWidth": 3,
                    "targetLineWidth": -0.0016,
                    "targetLineLength": 0.02,
                    "range": 36000,
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\MissileThreat,
                    "MissileThreat": {
                        "color": [1,0,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\MissileThreat\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0216296],1],[[0.003472,-0.0213009],1],[[0.00684,-0.0203254],1],[[0.01,-0.0187313],1],[[0.012856,-0.0165683],1],[[0.01532,-0.0139035],1],[[0.01732,-0.0108148],1],[[0.018794,-0.00739733],1],[[0.019696,-0.0037549],1],[[0.02,0],1],[[0.019696,0.0037549],1],[[0.018794,0.00739733],1],[[0.01732,0.0108148],1],[[0.01532,0.0139035],1],[[0.012856,0.0165683],1],[[0.01,0.0187313],1],[[0.00684,0.0203254],1],[[0.003472,0.0213009],1],[[0,0.0216296],1],[[-0.003472,0.0213009],1],[[-0.00684,0.0203254],1],[[-0.01,0.0187313],1],[[-0.012856,0.0165683],1],[[-0.01532,0.0139035],1],[[-0.01732,0.0108148],1],[[-0.018794,0.00739733],1],[[-0.019696,0.0037549],1],[[-0.02,0],1],[[-0.019696,-0.0037549],1],[[-0.018794,-0.00739733],1],[[-0.01732,-0.0108148],1],[[-0.01532,-0.0139035],1],[[-0.012856,-0.0165683],1],[[-0.01,-0.0187313],1],[[-0.00684,-0.0203254],1],[[-0.003472,-0.0213009],1],[[0,-0.0216296],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\MissileThreat\TextM,
                        "TextM": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\lockingThreat,
                    "lockingThreat": {
                        "color": [1,0.3,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\lockingThreat\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\rwr,
                    "rwr": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\rwr\TargetLines
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\rwr\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\rwrFriendly,
                    "rwrFriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\rwrFriendly\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\rwrFriendly\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\rwrEnemy,
                    "rwrEnemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\rwrEnemy\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\rwrEnemy\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\markedTarget,
                    "markedTarget": {
                        "color": [1,0.3,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\markedTarget\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 3,
                            "points": [[[-0.017,-0.0183852],1],[[-0.01,-0.0183852],1],[],[[0.017,-0.0183852],1],[[0.01,-0.0183852],1],[],[[-0.017,-0.0183852],1],[[-0.017,-0.0108148],1],[],[[0.017,-0.0183852],1],[[0.017,-0.0108148],1],[],[[-0.017,0.0183852],1],[[-0.01,0.0183852],1],[],[[0.017,0.0183852],1],[[0.01,0.0183852],1],[],[[-0.017,0.0183852],1],[[-0.017,0.0108148],1],[],[[0.017,0.0183852],1],[[0.017,0.0108148],1],[]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\assignedTarget,
                    "assignedTarget": {
                        "color": [1,0.3,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\assignedTarget\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 7,
                            "points": [[[0,-0.0194667],1],[[0.0031248,-0.0191708],1],[[0.006156,-0.0182928],1],[[0.009,-0.0168581],1],[[0.0115704,-0.0149115],1],[[0.013788,-0.0125132],1],[[0.015588,-0.00973333],1],[[0.0169146,-0.0066576],1],[[0.0177264,-0.00337941],1],[[0.018,0],1],[[0.0177264,0.00337941],1],[[0.0169146,0.0066576],1],[[0.015588,0.00973333],1],[[0.013788,0.0125132],1],[[0.0115704,0.0149115],1],[[0.009,0.0168581],1],[[0.006156,0.0182928],1],[[0.0031248,0.0191708],1],[[0,0.0194667],1],[[-0.0031248,0.0191708],1],[[-0.006156,0.0182928],1],[[-0.009,0.0168581],1],[[-0.0115704,0.0149115],1],[[-0.013788,0.0125132],1],[[-0.015588,0.00973333],1],[[-0.0169146,0.0066576],1],[[-0.0177264,0.00337941],1],[[-0.018,0],1],[[-0.0177264,-0.00337941],1],[[-0.0169146,-0.0066576],1],[[-0.015588,-0.00973333],1],[[-0.013788,-0.0125132],1],[[-0.0115704,-0.0149115],1],[[-0.009,-0.0168581],1],[[-0.006156,-0.0182928],1],[[-0.0031248,-0.0191708],1],[[0,-0.0194667],1]]
                        }
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\target,
                    "target": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\target\TargetLines
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\target\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetFriendly,
                    "targetFriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetFriendly\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetFriendly\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetEnemy,
                    "targetEnemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetEnemy\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetEnemy\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGround,
                    "targetGround": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGround\TargetLines
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGround\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundFriendly,
                    "targetGroundFriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundFriendly\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundFriendly\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundEnemy,
                    "targetGroundEnemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundEnemy\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundEnemy\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundRemote,
                    "targetGroundRemote": {
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundRemote\TargetLines
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundRemote\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundRemoteFriendly,
                    "targetGroundRemoteFriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundRemoteFriendly\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundRemoteFriendly\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundRemoteEnemy,
                    "targetGroundRemoteEnemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundRemoteEnemy\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0.02,0],1],[[0,0.0216296],1],[[-0.02,0],1],[[0,-0.0216296],1],[[0.02,0],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetGroundRemoteEnemy\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAir,
                    "targetAir": {
                        "color": [1,1,1],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAir\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAir\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirFriendly,
                    "targetAirFriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirFriendly\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirFriendly\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirEnemy,
                    "targetAirEnemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirEnemy\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirEnemy\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirRemote,
                    "targetAirRemote": {
                        "color": [1,1,1],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirRemote\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirRemote\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirRemoteFriendly,
                    "targetAirRemoteFriendly": {
                        "color": [0,1,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirRemoteFriendly\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirRemoteFriendly\TextA,
                        "TextA": {
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
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirRemoteEnemy,
                    "targetAirRemoteEnemy": {
                        "color": [1,0,0],
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirRemoteEnemy\TargetLines,
                        "TargetLines": {
                            "type": "line",
                            "width": 2,
                            "points": [[[0,-0.0140593],1],[[0.0022568,-0.0138456],1],[[0.004446,-0.0132115],1],[[0.0065,-0.0121753],1],[[0.0083564,-0.0107694],1],[[0.009958,-0.00903729],1],[[0.011258,-0.00702963],1],[[0.0122161,-0.00480827],1],[[0.0128024,-0.00244069],1],[[0.013,0],1],[[0.0128024,0.00244069],1],[[0.0122161,0.00480827],1],[[0.011258,0.00702963],1],[[0.009958,0.00903729],1],[[0.0083564,0.0107694],1],[[0.0065,0.0121753],1],[[0.004446,0.0132115],1],[[0.0022568,0.0138456],1],[[0,0.0140593],1],[[-0.0022568,0.0138456],1],[[-0.004446,0.0132115],1],[[-0.0065,0.0121753],1],[[-0.0083564,0.0107694],1],[[-0.009958,0.00903729],1],[[-0.011258,0.00702963],1],[[-0.0122161,0.00480827],1],[[-0.0128024,0.00244069],1],[[-0.013,0],1],[[-0.0128024,-0.00244069],1],[[-0.0122161,-0.00480827],1],[[-0.011258,-0.00702963],1],[[-0.009958,-0.00903729],1],[[-0.0083564,-0.0107694],1],[[-0.0065,-0.0121753],1],[[-0.004446,-0.0132115],1],[[-0.0022568,-0.0138456],1],[[0,-0.0140593],1]]
                        },
                        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\RWR\targetAirRemoteEnemy\TextA,
                        "TextA": {
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
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\MChaff_Text,
                "MChaff_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "M CHAFF",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.77,0.85],1],
                    "right": [[0.8,0.85],1],
                    "down": [[0.77,0.89],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\MFlare_Text,
                "MFlare_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "M FLARE",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.77,0.89],1],
                    "right": [[0.8,0.89],1],
                    "down": [[0.77,0.93],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\Prog_Text,
                "Prog_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "1 PROG",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.77,0.93],1],
                    "right": [[0.8,0.93],1],
                    "down": [[0.77,0.97],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\ChaffSource,
                "ChaffSource": {
                    "type": "text",
                    "source": "cmammo",
                    "sourceScale": 1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.93,0.85],1],
                    "right": [[0.96,0.85],1],
                    "down": [[0.93,0.89],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\FlareSource,
                "FlareSource": {
                    "pos": [[0.93,0.89],1],
                    "right": [[0.96,0.89],1],
                    "down": [[0.93,0.93],1],
                    "type": "text",
                    "source": "cmammo",
                    "sourceScale": 1,
                    "align": "right",
                    "scale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_5\Draw\ProgS_Text,
                "ProgS_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "10",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.93,0.93],1],
                    "right": [[0.96,0.93],1],
                    "down": [[0.93,0.97],1]
                }
            }
        },
        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6,
        "MFD_6": {
            "topLeft": "MFD_6_TL",
            "topRight": "MFD_6_TR",
            "bottomLeft": "MFD_6_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\material,
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw,
            "Draw": {
                "condition": "on",
                "color": [0.15,1,0.15],
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\CurrentWeapon,
                "CurrentWeapon": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourceScale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.51,0.24],1],
                    "right": [[0.57,0.24],1],
                    "down": [[0.51,0.3],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\MGAmmo,
                "MGAmmo": {
                    "type": "text",
                    "source": "ammo",
                    "sourceIndex": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.51,0.415],1],
                    "right": [[0.54,0.415],1],
                    "down": [[0.51,0.455],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\MGAmmo_Text,
                "MGAmmo_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "GUN-",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.43,0.415],1],
                    "right": [[0.46,0.415],1],
                    "down": [[0.43,0.455],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\thrust1Source,
                "thrust1Source": {
                    "type": "text",
                    "source": "throttle",
                    "sourceScale": 100,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.3,0.08],1],
                    "right": [[0.34,0.08],1],
                    "down": [[0.3,0.12],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\thrust2Source,
                "thrust2Source": {
                    "pos": [[0.61,0.08],1],
                    "right": [[0.65,0.08],1],
                    "down": [[0.61,0.12],1],
                    "type": "text",
                    "source": "throttle",
                    "sourceScale": 100,
                    "align": "center",
                    "scale": 1
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\White,
                "White": {
                    "color": [1,1,15],
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\White\ChaffSource,
                    "ChaffSource": {
                        "type": "text",
                        "source": "cmammo",
                        "sourceScale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.26,0.78],1],
                        "right": [[0.29,0.78],1],
                        "down": [[0.26,0.82],1]
                    },
                    # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\White\FlareSource,
                    "FlareSource": {
                        "pos": [[0.68,0.78],1],
                        "right": [[0.71,0.78],1],
                        "down": [[0.68,0.82],1],
                        "type": "text",
                        "source": "cmammo",
                        "sourceScale": 1,
                        "align": "right",
                        "scale": 1
                    }
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\Pylon1,
                "Pylon1": {
                    "type": "pylonicon",
                    "pos": [[0.35,0.48],1],
                    "pylon": 1,
                    "name": "rhs_f22_pylon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\Pylon2,
                "Pylon2": {
                    "pos": [[0.37,0.58],1],
                    "pylon": 2,
                    "type": "pylonicon",
                    "name": "rhs_f22_pylon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\Pylon3,
                "Pylon3": {
                    "pos": [[0.445,0.58],1],
                    "pylon": 3,
                    "type": "pylonicon",
                    "name": "rhs_f22_pylon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\Pylon4,
                "Pylon4": {
                    "pos": [[0.555,0.58],1],
                    "pylon": 4,
                    "type": "pylonicon",
                    "name": "rhs_f22_pylon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\Pylon5,
                "Pylon5": {
                    "pos": [[0.63,0.58],1],
                    "pylon": 5,
                    "type": "pylonicon",
                    "name": "rhs_f22_pylon"
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_6\Draw\Pylon6,
                "Pylon6": {
                    "pos": [[0.65,0.48],1],
                    "pylon": 6,
                    "type": "pylonicon",
                    "name": "rhs_f22_pylon"
                }
            }
        },
        # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7,
        "MFD_7": {
            "topLeft": "MFD_7_TL",
            "topRight": "MFD_7_TR",
            "bottomLeft": "MFD_7_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0.03,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "rhsusf_digital_font_var",
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\material,
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\Draw,
            "Draw": {
                "condition": "on",
                "color": [0.15,1,0.15],
                "alpha": 0.5,
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\Draw\C1_Text,
                "C1_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "C1: ",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.06,0.24],1],
                    "right": [[0.12,0.24],1],
                    "down": [[0.06,0.31],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\Draw\C1_Value,
                "C1_Value": {
                    "type": "text",
                    "source": "userText",
                    "sourceScale": 1,
                    "sourceIndex": 0,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.16,0.24],1],
                    "right": [[0.22,0.24],1],
                    "down": [[0.16,0.31],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\Draw\COM1_Text1,
                "COM1_Text1": {
                    "type": "text",
                    "source": "static",
                    "text": "COM1",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.51,0.26],1],
                    "right": [[0.57,0.26],1],
                    "down": [[0.51,0.33],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\Draw\COM1_Text2,
                "COM1_Text2": {
                    "type": "text",
                    "source": "static",
                    "text": "1/1",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.81,0.26],1],
                    "right": [[0.87,0.26],1],
                    "down": [[0.81,0.33],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\Draw\Vol_Text,
                "Vol_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "C1 VOL 100%",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.51,0.405],1],
                    "right": [[0.57,0.405],1],
                    "down": [[0.51,0.475],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\Draw\VolAdj_Text,
                "VolAdj_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "> VOL ADJ",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.51,0.55],1],
                    "right": [[0.57,0.55],1],
                    "down": [[0.51,0.62],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\Draw\Em_Text,
                "Em_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "  - - - -",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.51,0.705],1],
                    "right": [[0.57,0.705],1],
                    "down": [[0.51,0.775],1]
                },
                # Class: CfgVehicles\rhsusf_f22\MFD\MFD_7\Draw\FreqAdj_Text,
                "FreqAdj_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "> FREQ ADJ",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.51,0.88],1],
                    "right": [[0.57,0.88],1],
                    "down": [[0.51,0.95],1]
                }
            }
        }
    },
    "airBrake": 1,
    "airBrakeFrictionCoef": 2.4,
    "flaps": 1,
    "flapsFrictionCoef": 0.36,
    "gearsUpFrictionCoef": 0.8,
    "brakeDistance": 250,
    "wheelSteeringSensitivity": 4,
    "maxSpeed": 1800,
    "RHS_AfterBurner_MaxSpeed": 2000,
    "RHS_AfterBurner_Boost": 0.18,
    "RHS_AfterBurner_FuelDrag": 0.19,
    "altFullForce": 5000,
    "altNoForce": 15000,
    "rudderInfluence": 0.766,
    "noseDownCoef": 0,
    "aileronSensitivity": 1.2,
    "elevatorSensitivity": 1.4,
    "elevatorControlsSensitivityCoef": 4,
    "aileronControlsSensitivityCoef": 3.5,
    "rudderControlsSensitivityCoef": 4,
    "envelope": [0,0.11,0.83,1.97,2.42,2.69,3.87,5.27,6.89,8.72,9.7,9.6,9.2,8.5,8.2,8],
    "thrustCoef": [1.76,1.69,1.62,1.68,1.74,1.81,1.89,1.95,1.96,1.96,1.92,1.4,0.4,0,0,0],
    "elevatorCoef": [0.3,0.5,0.66,0.52,0.49,0.46,0.43,0.4,0.35,0.3,0.25,0.18,0.17,0.16,0.15,0.15],
    "aileronCoef": [0.4,0.5,0.8,0.95,1.02,1.04,1.03,1.01,1,0.7,0.6,0.55,0.5,0.45,0.4,0.35],
    "rudderCoef": [0.5,1.8,2.6,2.75,2.8,2.85,2.9,2.95,2.98,3.01,2.7,1.1,0.9,0.7,0.5,0.3],
    "angleOfIndicence": 0.04,
    "draconicForceXCoef": 8,
    "draconicForceYCoef": 1.2,
    "draconicForceZCoef": 1,
    "draconicTorqueXCoef": [4,5.1,6.1,7,7.7,8.3,9,9.1,9.2,9.2,9.2],
    "draconicTorqueYCoef": [6.8,5.5,4,1.5,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "airFrictionCoefs0": [0,0,0],
    "airFrictionCoefs1": [0.1,0.5,0.0075],
    "airFrictionCoefs2": [0.001,0.005,6.7e-005],
    "landingSpeed": 275,
    "stallSpeed": 250,
    "stallWarningTreshold": 0.5,
    "acceleration": 200,
    "landingAoa": 0.108207,
    "maxOmega": 4000,
    "engineMOI": 9,
    # Class: CfgVehicles\rhsusf_f22\Wheels,
    "Wheels": {
        "disableWheelsWhenDestroyed": 1,
        # Class: CfgVehicles\rhsusf_f22\Wheels\Wheel_1,
        "Wheel_1": {
            "steering": 1,
            "side": "left",
            "boneName": "Wheel_1",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 150,
            "MOI": 3,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 2000,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "suspForceAppPointOffset": "Wheel_1_center",
            "tireForceAppPointOffset": "Wheel_1_center",
            "maxCompression": 0.15,
            "maxDroop": 0.1,
            "sprungMass": 11400,
            "springStrength": 1.2e+006,
            "springDamperRate": 128000,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 25,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\rhsusf_f22\Wheels\Wheel_1_fake,
        "Wheel_1_fake": {
            "steering": 1,
            "side": "left",
            "boneName": "Wheel_1",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 150,
            "MOI": 3,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 2000,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "suspForceAppPointOffset": "Wheel_1_center",
            "tireForceAppPointOffset": "Wheel_1_center",
            "maxCompression": 0.15,
            "maxDroop": 0.1,
            "sprungMass": 11400,
            "springStrength": 1.2e+006,
            "springDamperRate": 128000,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 25,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\rhsusf_f22\Wheels\Wheel_2,
        "Wheel_2": {
            "steering": 0,
            "boneName": "Wheel_2",
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "suspForceAppPointOffset": "Wheel_2_center",
            "tireForceAppPointOffset": "Wheel_2_center",
            "width": 0.28,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": 3200,
            "springStrength": 1.58e+006,
            "springDamperRate": 512000,
            "side": "left",
            "mass": 150,
            "MOI": 3,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 2000,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 25,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\rhsusf_f22\Wheels\Wheel_3,
        "Wheel_3": {
            "side": "right",
            "boneName": "Wheel_3",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspForceAppPointOffset": "Wheel_3_center",
            "tireForceAppPointOffset": "Wheel_3_center",
            "steering": 0,
            "width": 0.28,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": 3200,
            "springStrength": 1.58e+006,
            "springDamperRate": 512000,
            "mass": 150,
            "MOI": 3,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 2000,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 25,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    # Class: CfgVehicles\rhsusf_f22\Damage,
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_f22|data|body.rvmat","rhsusf|addons|rhsusf_f22|data|body_damage.rvmat","rhsusf|addons|rhsusf_f22|data|body_destruct.rvmat","rhsusf|addons|rhsusf_f22|data|wing.rvmat","rhsusf|addons|rhsusf_f22|data|wing_damage.rvmat","rhsusf|addons|rhsusf_f22|data|wing_destruct.rvmat","rhsusf|addons|rhsusf_f22|data|kolo1.rvmat","rhsusf|addons|rhsusf_f22|data|kolo1.rvmat","rhsusf|addons|rhsusf_f22|data|kolo_destruct.rvmat"]
    },
    # Class: CfgVehicles\rhsusf_f22\textureSources,
    "textureSources": {
        # Class: CfgVehicles\rhsusf_f22\textureSources\standard
        "standard": {
            "displayName": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["|rhsusf|addons|rhsusf_f22|data|f22_b1.paa","|rhsusf|addons|rhsusf_f22|data|f22_wing_spads.paa"],
            "factions": ["rhs_faction_usaf"]
        }
    },
    "textureList": ["standard",1],
    # Class: CfgVehicles\rhsusf_f22\compartmentsLights,
    "compartmentsLights": {
        # Class: CfgVehicles\rhsusf_f22\compartmentsLights\Comp1
        "Comp1": {
            # Class: CfgVehicles\rhsusf_f22\compartmentsLights\Comp1\Light_General
            "Light_General": {
                "color": [20,30,30],
                "ambient": [0,0,0],
                "intensity": 3.05,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 1,
                "blinking": 0,
                # Class: CfgVehicles\rhsusf_f22\compartmentsLights\Comp1\Light_General\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 1.45,
                    "hardLimitEnd": 2.45
                },
                "point": "light_general"
            }
        }
    },
    # Class: CfgVehicles\rhsusf_f22\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\rhsusf_f22\Reflectors\Left
        "Left": {
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "selection": "l svetlo",
            "position": "light_1_pos",
            "direction": "light_1_dir",
            "hitpoint": "light_1_hit",
            "innerAngle": 15,
            "outerAngle": 40,
            "coneFadeCoef": 10,
            "intensity": 50,
            "useFlare": 0,
            "dayLight": 0,
            "FlareSize": 1,
            "size": 1,
            # Class: CfgVehicles\rhsusf_f22\Reflectors\Left\Attenuation,
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardLimitStart": 150,
                "hardLimitEnd": 300
            }
        },
        # Class: CfgVehicles\rhsusf_f22\Reflectors\Left_Flare,
        "Left_Flare": {
            "color": [70,75,100,1],
            "position": "light_1_pos_flare",
            "useFlare": 1,
            "outerAngle": 160,
            "ambient": [100,100,100],
            "selection": "l svetlo",
            "direction": "light_1_dir",
            "hitpoint": "light_1_hit",
            "innerAngle": 15,
            "coneFadeCoef": 10,
            "intensity": 50,
            "dayLight": 0,
            "FlareSize": 1,
            "size": 1,
            # Class: CfgVehicles\rhsusf_f22\Reflectors\Left\Attenuation,
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardLimitStart": 150,
                "hardLimitEnd": 300
            }
        },
        # Class: CfgVehicles\rhsusf_f22\Reflectors\Right,
        "Right": {
            "position": "light_2_pos",
            "direction": "light_2_dir",
            "hitpoint": "light_2_hit",
            "selection": "p svetlo",
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "innerAngle": 15,
            "outerAngle": 40,
            "coneFadeCoef": 10,
            "intensity": 50,
            "useFlare": 0,
            "dayLight": 0,
            "FlareSize": 1,
            "size": 1,
            # Class: CfgVehicles\rhsusf_f22\Reflectors\Left\Attenuation,
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardLimitStart": 150,
                "hardLimitEnd": 300
            }
        },
        # Class: CfgVehicles\rhsusf_f22\Reflectors\Right_Flare,
        "Right_Flare": {
            "color": [70,75,100,1],
            "position": "light_2_pos_flare",
            "useFlare": 1,
            "outerAngle": 160,
            "direction": "light_2_dir",
            "hitpoint": "light_2_hit",
            "selection": "p svetlo",
            "ambient": [100,100,100],
            "innerAngle": 15,
            "coneFadeCoef": 10,
            "intensity": 50,
            "dayLight": 0,
            "FlareSize": 1,
            "size": 1,
            # Class: CfgVehicles\rhsusf_f22\Reflectors\Left\Attenuation,
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardLimitStart": 150,
                "hardLimitEnd": 300
            }
        }
    },
    "aggregateReflectors": [["Left","Left_Flare","Right","Right_Flare"]],
    "features": "Randomization: No						<br />Camo selections: 2 - the main body, wings and lower part of body						<br />Script door sources: None						<br />Script animations: AddScalpel, AddAsraam_out, AddAsraam_mid, AddMk82, AddGbu12, AddZephyr, AddDar						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: None",
    "mapSize": 13.02,
    "_generalMacro": "Plane_Fighter_03_base_F",
    "editorSubcategory": "EdSubcat_Planes",
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "armorLights": 0.1,
    "minTotalDamageThreshold": 0.008,
    "waterLeakiness": 1.5,
    "destrType": "DestructWreck",
    "slingLoadCargoMemoryPoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "viewDriverShadowDiff": 0.5,
    "viewDriverShadowAmb": 0.5,
    # Class: CfgVehicles\Plane_Fighter_03_base_F\Turrets,
    "Turrets": {
    },
    # Class: CfgVehicles\Plane_Fighter_03_base_F\TransportItems,
    "TransportItems": {
    },
    "attenuationEffectType": "PlaneAttenuation",
    "soundGetIn": ["A3|Sounds_F|air|Plane_Fighter_03|buzzard_getin",1,1,40],
    "soundGetOut": ["A3|Sounds_F|air|Plane_Fighter_03|getout",1,1,40],
    "cabinOpenSound": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinOpen",1.77828,1,40],
    "cabinCloseSound": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinClose",1.77828,1,40],
    "cabinOpenSoundInternal": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinOpen",10,1,40],
    "cabinCloseSoundInternal": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinClose",10,1,40],
    "soundDammage": ["A3|Sounds_F|debugsound",1.77828,1,100],
    "buildCrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "buildCrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "buildCrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "buildCrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundBuildingCrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "WoodCrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_1",3.16228,1,900],
    "WoodCrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_2",3.16228,1,900],
    "WoodCrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_6",3.16228,1,900],
    "WoodCrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_8",3.16228,1,900],
    "soundWoodCrash": ["woodCrash0",0.25,"woodCrash1",0.25,"woodCrash2",0.25,"woodCrash3",0.25],
    "armorCrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "armorCrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "armorCrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "armorCrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundArmorCrash": ["ArmorCrash0",0.25,"ArmorCrash1",0.25,"ArmorCrash2",0.25,"ArmorCrash3",0.25],
    "Crash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "Crash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "Crash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "Crash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundCrashes": ["Crash0",0.25,"Crash1",0.25,"Crash2",0.25,"Crash3",0.25],
    "soundWaterCollision1": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_1",1.41254,1,500],
    "soundWaterCollision2": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_2",1.41254,1,500],
    "soundWaterCrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "landingSoundInt0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int1",1,1,100],
    "landingSoundInt1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int2",1,1,100],
    "landingSoundInt": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingSoundOut0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext1",1.77828,1,100],
    "landingSoundOut1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext2",1.77828,1,100],
    "landingSoundOut": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    # Class: CfgVehicles\Plane_Fighter_03_base_F\scrubLandInt,
    "scrubLandInt": {
        "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
        "frequency": 1,
        "volume": "(scrubLand factor[0.01, 0.20])"
    },
    "antiRollbarForceCoef": 0,
    "antiRollbarForceLimit": 0,
    "antiRollbarSpeedMin": 50,
    "antiRollbarSpeedMax": 300,
    "irScanRangeMin": 500,
    "irScanRangeMax": 5000,
    "irScanToEyeFactor": 2,
    "showAllTargets": 4,
    # Class: CfgVehicles\Plane_Fighter_03_base_F\ViewPilot,
    "ViewPilot": {
        "initAngleX": -3,
        "initFov": 0.75,
        "minFov": 0.25,
        "maxFov": 1.25,
        "initAngleY": 0,
        "minAngleX": -65,
        "maxAngleX": 85,
        "minAngleY": -150,
        "maxAngleY": 150,
        "minMoveX": -0.2,
        "maxMoveX": 0.2,
        "minMoveY": -0.1,
        "maxMoveY": 0.1,
        "minMoveZ": -0.1,
        "maxMoveZ": 0.2,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    "memoryPointDriverOptics": "PilotCamera_pos",
    "driverWeaponsInfoType": "RscOptics_CAS_01_TGP",
    # Class: CfgVehicles\Plane_Fighter_03_base_F\Library,
    "Library": {
        "libTextDesc": "The A-143 Buzzard is a single seat light multi-purpose combat aircraft able to carry a wide range of equipment and weaponry. A-143 has seven weapon hardpoints, three under each wing and one under the fuselage. Standard armament consists of 20mm cannon, and a mixture of AA and AG rockets."
    },
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "driverRightHandAnimName": "stick_pilot",
    "waterLinearDampingCoefY": 0,
    "waterLinearDampingCoefX": 5,
    "waterResistanceCoef": 0.04,
    "ejectSpeed": [0,60,0],
    "transportMaxWeapons": 6,
    "transportMaxMagazines": 24,
    "transportMaxBackpacks": 6,
    "maximumLoad": 500,
    "supplyRadius": 2,
    "memoryPointSupply": "doplnovani",
    # Class: CfgVehicles\Plane_Base_F\TransportBackpacks,
    "TransportBackpacks": {
    },
    # Class: CfgVehicles\Plane_Base_F\TransportMagazines,
    "TransportMagazines": {
    },
    # Class: CfgVehicles\Plane_Base_F\TransportWeapons,
    "TransportWeapons": {
    },
    # Class: CfgVehicles\Plane_Base_F\camShakeGForce,
    "camShakeGForce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minSpeed": 1
    },
    "minGForce": 0.3,
    "maxGForce": 3,
    "gForceShakeAttenuation": 0.5,
    # Class: CfgVehicles\Plane_Base_F\NewTurret,
    "NewTurret": {
        "body": "mainTurret",
        "gun": "mainGun",
        "animationSourceBody": "mainTurret",
        "animationSourceGun": "mainGun",
        "animationSourceHatch": "hatchGunner",
        "animationSourceCamElev": "camElev",
        "proxyType": "CPGunner",
        "proxyIndex": 1,
        "gunnerName": "Gunner",
        "gunnerType": "",
        "primaryGunner": 1,
        "primaryObserver": 0,
        "weapons": [],
        "magazines": [],
        "soundServo": ["",0.00316228,1],
        "soundElevation": ["",0.00316228,1],
        "minElev": -4,
        "maxElev": 20,
        "initElev": 0,
        "minTurn": -360,
        "maxTurn": 360,
        "initTurn": 0,
        "minOutElev": -4,
        "maxOutElev": 20,
        "initOutElev": 0,
        "minOutTurn": -60,
        "maxOutTurn": 60,
        "initOutTurn": 0,
        "maxHorizontalRotSpeed": 1.2,
        "maxVerticalRotSpeed": 1.2,
        "minCamElev": -90,
        "maxCamElev": 90,
        "initCamElev": 0,
        "stabilizedInAxes": 3,
        "primary": 1,
        "hasGunner": 1,
        "commanding": 1,
        "gunnerGetInAction": "",
        "gunnerGetOutAction": "",
        "turretCanSee": 0,
        "canUseScanners": 1,
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewGunner,
        "ViewGunner": {
            "initAngleX": 5,
            "minAngleX": -75,
            "maxAngleX": 85,
            "initAngleY": 0,
            "minAngleY": -150,
            "maxAngleY": 150,
            "minFov": 0.25,
            "maxFov": 1.25,
            "initFov": 0.75,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "continuous": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
        "TurretSpec": {
            "showHeadPhones": 0
        },
        "gunnerOpticsModel": "",
        "gunnerOpticsColor": [0,0,0,1],
        "gunnerForceOptics": 1,
        "gunnerOpticsShowCursor": 0,
        "turretInfoType": "",
        "gunnerOutOpticsModel": "",
        "gunnerOutOpticsColor": [0,0,0,1],
        "gunnerOpticsEffect": [],
        "gunnerOutOpticsEffect": [],
        "memoryPointGunnerOutOptics": "",
        "gunnerOutForceOptics": 0,
        "gunnerOutOpticsShowCursor": 0,
        "gunnerFireAlsoInInternalCamera": 1,
        "gunnerOutFireAlsoInInternalCamera": 1,
        "gunnerUsesPilotView": 0,
        "castGunnerShadow": 0,
        "viewGunnerShadow": 1,
        "viewGunnerShadowDiff": 1,
        "viewGunnerShadowAmb": 1,
        "ejectDeadGunner": 0,
        "hideWeaponsGunner": 1,
        "canHideGunner": -1,
        "forceHideGunner": 0,
        "outGunnerMayFire": 0,
        "inGunnerMayFire": 1,
        "showHMD": 0,
        "viewGunnerInExternal": 0,
        "lockWhenDriverOut": 0,
        "lockWhenVehicleSpeed": -1,
        "gunnerCompartments": "Compartment1",
        "LODTurnedIn": -1,
        "LODTurnedOut": -1,
        "startEngine": 1,
        "memoryPointsGetInGunnerPrecise": "",
        "missileBeg": "spice rakety",
        "missileEnd": "konec rakety",
        "armorLights": 0.4,
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
        "GunFire": {
            "access": 0,
            "cloudletDuration": 0.2,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 0.2,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 0.5,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletFire",
            "cloudletColor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 4500,
            "deltaT": -3000,
            # Class: WeaponFireGun\Table,
            "Table": {
                # Class: WeaponFireGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1,
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2,
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3,
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4,
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5,
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6,
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7,
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8,
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9,
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10,
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11,
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12,
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13,
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14,
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15,
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16,
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17,
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18,
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19,
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20,
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21,
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22,
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
        "GunClouds": {
            "access": 0,
            "cloudletDuration": 0.3,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 1,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 1,
            "cloudletAccY": 0.4,
            "cloudletMinYSpeed": 0.2,
            "cloudletMaxYSpeed": 0.8,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsGun\Table,
            "Table": {
                # Class: WeaponCloudsGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
        "MGunClouds": {
            "access": 0,
            "cloudletGrowUp": 0.05,
            "cloudletFadeIn": 0,
            "cloudletFadeOut": 0.1,
            "cloudletDuration": 0.05,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 0.3,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "timeToLive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourceSize": 0.02,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsMGun\Table,
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints,
        "HitPoints": {
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitTurret
            "HitTurret": {
                "armor": 0.8,
                "material": 51,
                "name": "turret",
                "visual": "turret",
                "passThrough": 1,
                "explosionShielding": 1
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitGun,
            "HitGun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passThrough": 1,
                "explosionShielding": 1
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets,
        "Turrets": {
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics,
        "ViewOptics": {
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "initFov": 0.3,
            "minFov": 0.07,
            "maxFov": 0.35,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        "forceNVG": 0,
        "isCopilot": 0,
        "canEject": 1,
        "gunnerLeftHandAnimName": "",
        "gunnerRightHandAnimName": "",
        "gunnerLeftLegAnimName": "",
        "gunnerRightLegAnimName": "",
        "gunnerDoor": "",
        "preciseGetInOut": 0,
        "turretFollowFreeLook": 0,
        "allowTabLock": 1,
        "showAllTargets": 0,
        "dontCreateAI": 0,
        "disableSoundAttenuation": 0,
        "slingLoadOperator": 0,
        "playerPosition": 0,
        "allowLauncherIn": 0,
        "allowLauncherOut": 0,
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
        "TurnOut": {
            "turnOffset": 0
        },
        "gunnerInAction": "ManActTestDriver",
        "gunnerAction": "ManActTestDriver",
        "gunBeg": "usti hlavne",
        "gunEnd": "konec hlavne",
        "memoryPointGunnerOptics": "gunnerview",
        "memoryPointsGetInGunner": "pos gunner",
        "memoryPointsGetInGunnerDir": "pos gunner dir",
        "memoryPointGun": "kulas",
        "selectionFireAnim": "zasleh",
        "showCrewAim": 0
    },
    "formationX": 200,
    "formationZ": 300,
    "precision": 200,
    "steerAheadSimul": 1,
    "steerAheadPlan": 2,
    "gearRetracting": 1,
    "cabinOpening": 1,
    "durationGetIn": 0.99,
    "durationGetOut": 0.99,
    "vtol": 0,
    "tailHook": 0,
    "lightOnGear": 1,
    "gearUpTime": 3.33,
    "gearDownTime": 2,
    "simulation": "airplanex",
    "minGunElev": 0,
    "maxGunElev": 0,
    "minGunTurn": 0,
    "maxGunTurn": 0,
    "VTOLYawInfluence": 2,
    "VTOLPitchInfluence": 2,
    "VTOLRollInfluence": 2,
    # Class: CfgVehicles\Plane\ViewOptics,
    "ViewOptics": {
        "initAngleX": 0,
        "minAngleX": 0,
        "maxAngleX": 0,
        "initAngleY": 0,
        "minAngleY": 0,
        "maxAngleY": 0,
        "initFov": 0.5,
        "minFov": 0.5,
        "maxFov": 0.5,
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": 0,
        "maxMoveY": 0,
        "minMoveZ": 0,
        "maxMoveZ": 0,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    "selectionRotorStill": "vrtule staticka",
    "selectionRotorMove": "vrtule blur",
    "memoryPointLDust": "levy prach",
    "memoryPointRDust": "pravy prach",
    "selectionFireAnim": "zasleh",
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "dustEffect": "HeliDust",
    "waterEffect": "HeliWater",
    # Class: CfgVehicles\Plane\GunFire,
    "GunFire": {
        "access": 0,
        "cloudletDuration": 0.2,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 1,
        "cloudletGrowUp": 0.2,
        "cloudletFadeIn": 0.01,
        "cloudletFadeOut": 0.5,
        "cloudletAccY": 0,
        "cloudletMinYSpeed": -100,
        "cloudletMaxYSpeed": 100,
        "cloudletShape": "cloudletFire",
        "cloudletColor": [1,1,1,0],
        "interval": 0.01,
        "size": 3,
        "sourceSize": 0.5,
        "timeToLive": 0,
        "initT": 4500,
        "deltaT": -3000,
        # Class: WeaponFireGun\Table,
        "Table": {
            # Class: WeaponFireGun\Table\T0
            "T0": {
                "maxT": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun\Table\T1,
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun\Table\T2,
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun\Table\T3,
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun\Table\T4,
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun\Table\T5,
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun\Table\T6,
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun\Table\T7,
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun\Table\T8,
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun\Table\T9,
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun\Table\T10,
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun\Table\T11,
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun\Table\T12,
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun\Table\T13,
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun\Table\T14,
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun\Table\T15,
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun\Table\T16,
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun\Table\T17,
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun\Table\T18,
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun\Table\T19,
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun\Table\T20,
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun\Table\T21,
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun\Table\T22,
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\Plane\GunClouds,
    "GunClouds": {
        "access": 0,
        "cloudletDuration": 0.3,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 1,
        "cloudletGrowUp": 1,
        "cloudletFadeIn": 0.01,
        "cloudletFadeOut": 1,
        "cloudletAccY": 0.4,
        "cloudletMinYSpeed": 0.2,
        "cloudletMaxYSpeed": 0.8,
        "cloudletShape": "cloudletClouds",
        "cloudletColor": [1,1,1,0],
        "interval": 0.05,
        "size": 3,
        "sourceSize": 0.5,
        "timeToLive": 0,
        "initT": 0,
        "deltaT": 0,
        # Class: WeaponCloudsGun\Table,
        "Table": {
            # Class: WeaponCloudsGun\Table\T0
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\Plane\MGunFire,
    "MGunFire": {
        "cloudletDuration": 0,
        "cloudletGrowUp": 0.06,
        "cloudletFadeIn": 0,
        "cloudletFadeOut": 0.12,
        "interval": 0.005,
        "size": 0.12,
        "sourceSize": 0.01,
        "initT": 3200,
        "deltaT": -4000,
        "access": 0,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 1,
        "cloudletAccY": 0,
        "cloudletMinYSpeed": -100,
        "cloudletMaxYSpeed": 100,
        "cloudletShape": "cloudletFire",
        "cloudletColor": [1,1,1,0],
        "timeToLive": 0,
        # Class: WeaponFireGun\Table,
        "Table": {
            # Class: WeaponFireGun\Table\T0
            "T0": {
                "maxT": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun\Table\T1,
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun\Table\T2,
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun\Table\T3,
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun\Table\T4,
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun\Table\T5,
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun\Table\T6,
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun\Table\T7,
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun\Table\T8,
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun\Table\T9,
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun\Table\T10,
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun\Table\T11,
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun\Table\T12,
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun\Table\T13,
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun\Table\T14,
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun\Table\T15,
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun\Table\T16,
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun\Table\T17,
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun\Table\T18,
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun\Table\T19,
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun\Table\T20,
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun\Table\T21,
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun\Table\T22,
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\Plane\MGunClouds,
    "MGunClouds": {
        "access": 0,
        "cloudletGrowUp": 0.05,
        "cloudletFadeIn": 0,
        "cloudletFadeOut": 0.1,
        "cloudletDuration": 0.05,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 0.3,
        "cloudletAccY": 0,
        "cloudletMinYSpeed": -100,
        "cloudletMaxYSpeed": 100,
        "cloudletShape": "cloudletClouds",
        "cloudletColor": [1,1,1,0],
        "timeToLive": 0,
        "interval": 0.02,
        "size": 0.3,
        "sourceSize": 0.02,
        "initT": 0,
        "deltaT": 0,
        # Class: WeaponCloudsMGun\Table,
        "Table": {
            # Class: WeaponCloudsMGun\Table\T0
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "numberPhysicalWheels": 3,
    # Class: CfgVehicles\Plane\SpeechVariants,
    "SpeechVariants": {
        # Class: CfgVehicles\Plane\SpeechVariants\Default
        "Default": {
            "speechSingular": ["veh_air_plane_s"],
            "speechPlural": ["veh_air_plane_p"]
        }
    },
    "textSingular": "fast mover",
    "textPlural": "fast movers",
    "nameSound": "veh_air_plane_s",
    "memoryPointGun": "kulomet",
    "fuelExplosionPower": 10,
    "crewCrashProtection": 0.15,
    "damageEffect": "AirDestructionEffects",
    "getInAction": "GetInHigh",
    "getOutAction": "GetOutHigh",
    "cargoGetInAction": ["GetInHigh"],
    "cargoGetOutAction": ["GetOutHigh"],
    "gunnerGetInAction": "GetInHigh",
    "gunnerGetOutAction": "GetOutHigh",
    "getInRadius": 1.2,
    # Class: CfgVehicles\Plane\CamShake,
    "CamShake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minSpeed": 200
    },
    "explosionShielding": 2,
    # Class: CfgVehicles\Plane\DestructionEffects,
    "DestructionEffects": {
    },
    "formationTime": 10,
    "fuelCapacity": 1000,
    "outsideSoundFilter": 1,
    "occludeSoundsWhenIn": 0.316228,
    "obstructSoundsWhenIn": 0.316228,
    "nightVision": 0,
    "cargoCompartments": [0],
    "enableGPS": 1,
    "weaponsGroup1": "1 + 		2",
    "weaponsGroup2": 4,
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    "maxFordingDepth": 0.001,
    "waterResistance": 1,
    "impactEffectsSea": "ImpactEffectsAir",
    "flareVelocity": 100,
    "enableRadio": 1,
    "memoryPointCM": ["flare_launcher1","flare_launcher2"],
    "memoryPointCMDir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "countermeasureActivationRadius": 10000,
    # Class: CfgVehicles\Air\camShakeDamage,
    "camShakeDamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minSpeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "secondaryExplosion": -1,
    # Class: CfgVehicles\AllVehicles\SquadTitles,
    "SquadTitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memoryPointsGetInDriver": "pos driver",
    "memoryPointsGetInDriverDir": "pos driver dir",
    "memoryPointsGetInCargo": "pos cargo",
    "memoryPointsGetInCargoDir": "pos cargo dir",
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInDriverPrecise": "pos driver",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
    "selectionShowDamage": "poskozeni",
    "selectionBackLights": "zadni svetlo",
    # Class: CfgVehicles\AllVehicles\ViewCargo,
    "ViewCargo": {
        "initAngleX": 5,
        "minAngleX": -75,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -150,
        "maxAngleY": 150,
        "minFov": 0.25,
        "maxFov": 1.25,
        "initFov": 0.75,
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": 0,
        "maxMoveY": 0,
        "minMoveZ": 0,
        "maxMoveZ": 0,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    # Class: CfgVehicles\AllVehicles\PilotSpec,
    "PilotSpec": {
        "showHeadPhones": 0
    },
    # Class: CfgVehicles\AllVehicles\CargoSpec,
    "CargoSpec": {
        # Class: CfgVehicles\AllVehicles\CargoSpec\Cargo1
        "Cargo1": {
            "showHeadPhones": 0
        }
    },
    # Class: CfgVehicles\AllVehicles\SoundEvents,
    "SoundEvents": {
    },
    "tracksSpeed": 0,
    "selectionLeftOffset": "",
    "selectionRightOffset": "",
    # Class: CfgVehicles\AllVehicles\RenderTargets,
    "RenderTargets": {
    },
    "cargoProxyIndexes": [],
    "driverDoor": "",
    "cargoDoors": [],
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "preciseGetInOut": 0,
    "cargoPreciseGetInOut": [0],
    "availableForSupportTypes": [],
    "waterPPInVehicle": 1,
    "impactEffectSpeedLimit": 8,
    "showCrewAim": 0,
    # Class: CfgVehicles\AllVehicles\CargoTurret,
    "CargoTurret": {
        # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner
        "ViewGunner": {
            "initAngleX": 5,
            "minAngleX": -75,
            "maxAngleX": 85,
            "initAngleY": 0,
            "minAngleY": -150,
            "maxAngleY": 150,
            "minFov": 0.25,
            "maxFov": 1.25,
            "initFov": 0.75,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles\AllVehicles\CargoTurret\Hitpoints,
        "Hitpoints": {
        },
        "animationSourceBody": "",
        "animationSourceGun": "",
        "body": "",
        "canEject": 1,
        "commanding": 0,
        "dontCreateAI": 1,
        "gun": "",
        "gunnerGetInAction": "GetInLow",
        "gunnerGetOutAction": "GetOutLow",
        "gunnerName": "cargo",
        "hideWeaponsGunner": 0,
        "isCopilot": 0,
        "memoryPointsGetInGunner": "pos cargo",
        "memoryPointsGetInGunnerDir": "pos cargo dir",
        "primaryGunner": 0,
        "proxyType": "CPCargo",
        "startEngine": 0,
        "turretFollowFreeLook": 0,
        "viewGunnerInExternal": 1,
        "disableSoundAttenuation": 1,
        "outGunnerMayFire": 1,
        "isPersonTurret": 1,
        "showAsCargo": 1,
        "maxElev": 45,
        "minElev": -45,
        "maxTurn": 95,
        "minTurn": -95,
        "animationSourceHatch": "hatchGunner",
        "animationSourceCamElev": "camElev",
        "proxyIndex": 1,
        "gunnerType": "",
        "primaryObserver": 0,
        "weapons": [],
        "magazines": [],
        "soundServo": ["",0.00316228,1],
        "soundElevation": ["",0.00316228,1],
        "initElev": 0,
        "initTurn": 0,
        "minOutElev": -4,
        "maxOutElev": 20,
        "initOutElev": 0,
        "minOutTurn": -60,
        "maxOutTurn": 60,
        "initOutTurn": 0,
        "maxHorizontalRotSpeed": 1.2,
        "maxVerticalRotSpeed": 1.2,
        "minCamElev": -90,
        "maxCamElev": 90,
        "initCamElev": 0,
        "stabilizedInAxes": 3,
        "primary": 1,
        "hasGunner": 1,
        "turretCanSee": 0,
        "canUseScanners": 1,
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
        "TurretSpec": {
            "showHeadPhones": 0
        },
        "gunnerOpticsModel": "",
        "gunnerOpticsColor": [0,0,0,1],
        "gunnerForceOptics": 1,
        "gunnerOpticsShowCursor": 0,
        "turretInfoType": "",
        "gunnerOutOpticsModel": "",
        "gunnerOutOpticsColor": [0,0,0,1],
        "gunnerOpticsEffect": [],
        "gunnerOutOpticsEffect": [],
        "memoryPointGunnerOutOptics": "",
        "gunnerOutForceOptics": 0,
        "gunnerOutOpticsShowCursor": 0,
        "gunnerFireAlsoInInternalCamera": 1,
        "gunnerOutFireAlsoInInternalCamera": 1,
        "gunnerUsesPilotView": 0,
        "castGunnerShadow": 0,
        "viewGunnerShadow": 1,
        "viewGunnerShadowDiff": 1,
        "viewGunnerShadowAmb": 1,
        "ejectDeadGunner": 0,
        "canHideGunner": -1,
        "forceHideGunner": 0,
        "inGunnerMayFire": 1,
        "showHMD": 0,
        "lockWhenDriverOut": 0,
        "lockWhenVehicleSpeed": -1,
        "gunnerCompartments": "Compartment1",
        "LODTurnedIn": -1,
        "LODTurnedOut": -1,
        "memoryPointsGetInGunnerPrecise": "",
        "missileBeg": "spice rakety",
        "missileEnd": "konec rakety",
        "armorLights": 0.4,
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
        "GunFire": {
            "access": 0,
            "cloudletDuration": 0.2,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 0.2,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 0.5,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletFire",
            "cloudletColor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 4500,
            "deltaT": -3000,
            # Class: WeaponFireGun\Table,
            "Table": {
                # Class: WeaponFireGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1,
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2,
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3,
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4,
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5,
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6,
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7,
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8,
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9,
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10,
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11,
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12,
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13,
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14,
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15,
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16,
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17,
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18,
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19,
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20,
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21,
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22,
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
        "GunClouds": {
            "access": 0,
            "cloudletDuration": 0.3,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 1,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 1,
            "cloudletAccY": 0.4,
            "cloudletMinYSpeed": 0.2,
            "cloudletMaxYSpeed": 0.8,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsGun\Table,
            "Table": {
                # Class: WeaponCloudsGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
        "MGunClouds": {
            "access": 0,
            "cloudletGrowUp": 0.05,
            "cloudletFadeIn": 0,
            "cloudletFadeOut": 0.1,
            "cloudletDuration": 0.05,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 0.3,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "timeToLive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourceSize": 0.02,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsMGun\Table,
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets,
        "Turrets": {
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics,
        "ViewOptics": {
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "initFov": 0.3,
            "minFov": 0.07,
            "maxFov": 0.35,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        "forceNVG": 0,
        "gunnerLeftHandAnimName": "",
        "gunnerRightHandAnimName": "",
        "gunnerLeftLegAnimName": "",
        "gunnerRightLegAnimName": "",
        "gunnerDoor": "",
        "preciseGetInOut": 0,
        "allowTabLock": 1,
        "showAllTargets": 0,
        "slingLoadOperator": 0,
        "playerPosition": 0,
        "allowLauncherIn": 0,
        "allowLauncherOut": 0,
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
        "TurnOut": {
            "turnOffset": 0
        },
        "gunnerInAction": "ManActTestDriver",
        "gunnerAction": "ManActTestDriver",
        "gunBeg": "usti hlavne",
        "gunEnd": "konec hlavne",
        "memoryPointGunnerOptics": "gunnerview",
        "memoryPointGun": "kulas",
        "selectionFireAnim": "zasleh",
        "showCrewAim": 0
    },
    "curatorInfoType": "RscDisplayAttributesVehicle",
    "curatorInfoTypeEmpty": "RscDisplayAttributesVehicleEmpty",
    "access": 0,
    "reversed": 1,
    "autocenter": 1,
    "animated": 1,
    "shadow": 1,
    "featureType": 0,
    "speechSingular": [],
    "speechPlural": [],
    "maxDetectRange": 20,
    "detectSkill": 20,
    "mineAlertIconRange": 200,
    "killFriendlyExpCoef": 1,
    "weaponSlots": 0,
    "spotableDarkNightLightsOff": 0.001,
    "spotableNightLightsOff": 0.02,
    "spotableNightLightsOn": 4,
    "accuracyDarkNightLightsOff": 0.001,
    "accuracyNightLightsOff": 0.006,
    "accuracyNightLightsOn": 0.1,
    "obstructSoundLFRatio": 0,
    "occludeSoundLFRatio": 0.25,
    "unloadInCombat": 0,
    "slowSpeedForwardCoef": 0.3,
    "normalSpeedForwardCoef": 0.85,
    "gunnerHasFlares": 1,
    "enableManualFire": 1,
    "sensitivity": 2.5,
    "sensitivityEar": 0.0075,
    "portrait": "",
    "ghostPreview": "",
    "crewVulnerable": 1,
    "replaceDamaged": "",
    "replaceDamagedLimit": 0.9,
    "replaceDamagedHitpoints": [],
    "keepInEPESceneAfterDeath": 0,
    "fuelConsumptionRate": 0.01,
    "groupCameraPosition": [0,5,-30],
    "extCameraParams": [1],
    "cameraSmoothSpeed": 5,
    "predictTurnSimul": 1.2,
    "predictTurnPlan": 1,
    "indirectHitEnemyCoefAI": 10,
    "indirectHitFriendlyCoefAI": -20,
    "indirectHitCivilianCoefAI": -20,
    "indirectHitUnknownCoefAI": -0.5,
    "alwaysTarget": 0,
    "irScanGround": 1,
    "laserTarget": 0,
    "nvTarget": 0,
    "nvScanner": 0,
    "artilleryTarget": 0,
    "artilleryScanner": 0,
    "canUseScanners": 1,
    "preferRoads": 0,
    "unitInfoTypeLite": 0,
    "hideUnitInfo": 0,
    "limitedSpeedCoef": 0.22,
    "hasDriver": 1,
    "driverForceOptics": 0,
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 0,
    "enableWatch": 0,
    "usePreciseGetInAction": 0,
    "allowTabLock": 1,
    "dustFrontLeftPos": "dustFrontLeft",
    "dustFrontRightPos": "dustFrontRight",
    "dustBackLeftPos": "dustBackLeft",
    "dustBackRightPos": "dustBackRight",
    "wheelCircumference": 1,
    "waterAngularDampingCoef": 0,
    "showNVGDriver": 0,
    "showNVGCommander": 0,
    "showNVGGunner": 0,
    "showNVGCargo": [0],
    "soundAttenuationCargo": [1],
    "countsForScoreboard": 1,
    "hullDamageCauseExplosion": 0,
    # Class: CfgVehicles\All\NVGMarkers,
    "NVGMarkers": {
    },
    # Class: CfgVehicles\All\NVGMarker,
    "NVGMarker": {
        "diffuse": [1,1,1,1],
        "ambient": [1,1,1,1],
        "brightness": 1,
        "blinking": 0,
        "onlyInNvg": 0
    },
    # Class: CfgVehicles\All\HeadLimits,
    "HeadLimits": {
        "initAngleX": 5,
        "minAngleX": -30,
        "maxAngleX": 40,
        "initAngleY": 0,
        "minAngleY": -90,
        "maxAngleY": 90,
        "minAngleZ": -45,
        "maxAngleZ": 45,
        "rotZRadius": 0.2
    },
    "transportSoldier": 0,
    "transportAmmo": 0,
    "isbackpack": 0,
    "transportFuel": 0,
    "transportRepair": 0,
    "transportVehiclesCount": 0,
    "transportVehiclesMass": 0,
    "attendant": 0,
    "engineer": 0,
    "uavHacker": 0,
    "soundEngine": ["",1,1],
    "soundEnviron": ["",1,1],
    # Class: CfgVehicles\All\SoundEnvironExt,
    "SoundEnvironExt": {
    },
    # Class: CfgVehicles\All\SoundEquipment,
    "SoundEquipment": {
    },
    # Class: CfgVehicles\All\SoundGear,
    "SoundGear": {
    },
    # Class: CfgVehicles\All\SoundBreath,
    "SoundBreath": {
    },
    # Class: CfgVehicles\All\SoundBreathSwimming,
    "SoundBreathSwimming": {
    },
    # Class: CfgVehicles\All\SoundBreathInjured,
    "SoundBreathInjured": {
    },
    # Class: CfgVehicles\All\SoundHitScream,
    "SoundHitScream": {
    },
    # Class: CfgVehicles\All\SoundInjured,
    "SoundInjured": {
    },
    # Class: CfgVehicles\All\SoundBreathAutomatic,
    "SoundBreathAutomatic": {
    },
    # Class: CfgVehicles\All\SoundDrown,
    "SoundDrown": {
    },
    # Class: CfgVehicles\All\SoundChoke,
    "SoundChoke": {
    },
    # Class: CfgVehicles\All\SoundRecovered,
    "SoundRecovered": {
    },
    # Class: CfgVehicles\All\SoundBurning,
    "SoundBurning": {
    },
    # Class: CfgVehicles\All\PulsationSound,
    "PulsationSound": {
    },
    # Class: CfgVehicles\All\SoundDrowning,
    "SoundDrowning": {
    },
    "soundCrash": ["",0.316228,1],
    "soundLandCrash": ["",1,1],
    "soundWaterCrash": ["",0.177828,1],
    "soundServo": ["",0.00316228,0.5],
    "soundElevation": ["",0.00316228,0.5],
    "sounddamage": ["",1,1],
    "soundLandCrashes": ["soundLandCrash",1],
    "emptySound": ["",0,1],
    "soundBushCrash": ["emptySound",0],
    "driverInAction": "",
    "cargoAction": [],
    "cargoIsCoDriver": [0],
    "driverOpticsModel": "",
    "driverOpticsEffect": [],
    "driverOpticsColor": [1,1,1,1],
    "hideProxyInCombat": 0,
    "forceHideDriver": 0,
    "canHideDriver": -1,
    "castDriverShadow": 0,
    "castCargoShadow": 0,
    "viewDriverShadow": 1,
    "viewCargoShadow": 1,
    "viewCargoShadowDiff": 1,
    "viewCargoShadowAmb": 1,
    "ejectDeadDriver": 0,
    "ejectDeadCargo": 0,
    "hiddenSelectionsMaterials": [],
    "hiddenUnderwaterSelections": [],
    "shownUnderWaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    # Class: CfgVehicles\All\FxExplo,
    "FxExplo": {
        "access": 1
    },
    "selectionDamage": "zbytek",
    "HeadAimDown": 0,
    "cargoCanEject": 1,
    "fireResistance": 10,
    "airCapacity": 10,
    "waterDamageEngine": 0.2,
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "coefSpeedInside": 2,
    "windSockExist": 0,
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    "soundTurnIn": ["",0.000316228,1],
    "soundTurnOut": ["",0.000316228,1],
    "soundTurnInInternal": ["",0.000316228,1],
    "soundTurnOutInternal": ["",0.000316228,1],
    "insideDetectCoef": 0.05,
}