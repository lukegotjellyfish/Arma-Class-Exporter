RHS_A10 = {
    "rhs_gearAnim": "Gear_1",
    "dlc": "RHS_USAF",
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhs_a10.paa",
    "scope": 2,
    "LESH_canBeTowed": 1,
    "LESH_towFromFront": 1,
    "LESH_AxisOffsetTarget": [0,8,0.27],
    "LESH_WheelOffset": [0,0],
    "category": "Air",
    "side": 1,
    "crew": "rhsusf_airforce_jetpilot",
    "typicalCargo": ["rhsusf_airforce_jetpilot"],
    "vehicleClass": "rhs_vehclass_aircraft",
    "faction": "rhs_faction_usaf",
    "displayName": "A-10A",
    "author": "Red Hammer Studios",
    "model": "rhsusf|addons|rhsusf_a2port_air|a10|A10.p3d",
    "picture": "rhsusf|addons|rhsusf_a2port_air|data|ico|rhs_a10a_pic_ca.paa",
    "icon": "rhsusf|addons|rhsusf_a2port_air|data|mapico|icon_a10_ca.paa",
    "mapSize": 17,
    "hiddenSelections": ["Camo1","Camo2","screen","pip"],
    "hiddenSelectionsTextures": ["|rhsusf|addons|rhsusf_a2port_air|a10|data|a10_01_co.paa","|rhsusf|addons|rhsusf_a2port_air|a10|data|a10_02_co.paa","",""],
    "driverCanEject": 1,
    "ejectDamageLimit": 1,
    "driverCompartments": 1,
    "camouflage": 10,
    "audible": 6,
    "accuracy": 0.2,
    "supplyRadius": 8,
    "LockDetectionSystem": "8 + 4",
    "incomingMissileDetectionSystem": "8",
    "radarType": 4,
    "laserScanner": 1,
    "irScanRangeMin": 100,
    "irScanRangeMax": 10500,
    "irScanToEyeFactor": 2,
    "irScanGround": 1,
    "minFireTime": 10,
    "HeadAimDown": 0,
    "camShakeCoef": 0.6,
    "headGforceLeaningFactor": [0.005,0.001,0.015],
    "allowTabLock": 0,
    # Class: CfgVehicles|RHS_A10|EjectionSystem [Indent level: 1],
    "EjectionSystem": {
    },
    "soundLocked": ["a3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",1.12202,1],
    "irTarget": 1,
    "irTargetSize": 1,
    "visualTarget": 1,
    "visualTargetSize": 1,
    "radarTarget": 1,
    "radarTargetSize": 1,
    "unitInfoType": "RHSUSF_RscUnitInfoJet",
    "driverWeaponsInfoType": "RHSUSF_RscOptics_A10A_TVM",
    "driverAction": "rhs_A10_Pilot",
    "driverLeftHandAnimName": "lever_pilot",
    "driverRightHandAnimName": "stick_pilot",
    "driverLeftLegAnimName": "pedal_l",
    "driverRightLegAnimName": "pedal_r",
    "cabinOpening": 1,
    "precisegetinout": 1,
    "memoryPointsGetInDriver": "pos driver",
    "memoryPointsGetInDriverDir": "pos driver dir",
    "memoryPointsGetInDriverPrecise": "pos driver",
    "selectionFireAnim": "zasleh",
    "memoryPointLRocket": "L Raketa",
    "memoryPointRRocket": "P Raketa",
    "memoryPointLDust": "levy prach",
    "memoryPointRDust": "pravy prach",
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "weapons": ["rhs_weap_MASTERSAFE","RHS_weap_gau8"],
    "magazines": ["rhs_mag_1150Rnd_30x173_mixed"],
    "threat": [1,1,1],
    # Class: CfgVehicles|RHS_A10|Turrets [Indent level: 1],
    "Turrets": {
    },
    # Class: CfgVehicles|RHS_A10|pilotCamera [Indent level: 1],
    "pilotCamera": {
        # Class: CfgVehicles|RHS_A10|pilotCamera|OpticsIn [Indent level: 2],

        "OpticsIn": {

            # Class: CfgVehicles|RHS_A10|pilotCamera|OpticsIn|Wide [Indent level: 3],


            "Wide": {


                "opticsDisplayName": "DEFAULT",


                "initAngleX": 0,


                "minAngleX": -30,


                "maxAngleX": 30,


                "initAngleY": 0,


                "minAngleY": -100,


                "maxAngleY": 100,


                "initFov": 0.116667,


                "minFov": 0.116667,


                "maxFov": 0.116667,


                "directionStabilized": 0,


                "visionMode": ["Ti"],


                "thermalMode": [0],


                "gunnerOpticsModel": "rhsusf|addons|rhsusf_a2port_air|A10|rhs_tvm_3x.p3d"
            },

            # Class: CfgVehicles|RHS_A10|pilotCamera|OpticsIn|Narrow [Indent level: 3],

            "Narrow": {

                "opticsDisplayName": "ZOOM",

                "initFov": 0.0583333,

                "minFov": 0.0583333,

                "maxFov": 0.0583333,

                "gunnerOpticsModel": "rhsusf|addons|rhsusf_a2port_air|A10|rhs_tvm_6x.p3d",

                "initAngleX": 0,

                "minAngleX": -30,

                "maxAngleX": 30,

                "initAngleY": 0,

                "minAngleY": -100,

                "maxAngleY": 100,

                "directionStabilized": 0,

                "visionMode": ["Ti"],

                "thermalMode": [0]
            }
        },
        "minElev": -60,
        "maxElev": 60,
        "initElev": 0,
        "minTurn": -60,
        "maxTurn": 60,
        "maxXRotSpeed": 0.25,
        "maxYRotSpeed": 0.25,
        "pilotOpticsShowCursor": 0,
        "controllable": 1
    },
    "memoryPointDriverOptics": "tvm1",
    # Class: CfgVehicles|RHS_A10|Components [Indent level: 1],
    "Components": {
        # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent [Indent level: 2],

        "TransportPylonsComponent": {

            "UIPicture": "rhsusf|addons|rhsusf_a2port_air|data|loadouts|RHS_A10_EDEN_CA.paa",

            # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons [Indent level: 3],

            "pylons": {

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon1 [Indent level: 4],


                "pylon1": {


                    "hardpoints": ["RHS_HP_AIM9_2x","RHS_HP_LGB_500","RHS_HP_ECM"],


                    "priority": 5,


                    "maxweight": 1200,


                    "UIposition": [0.3,0.55],


                    "bay": -1,


                    "attachment": "rhs_mag_ANALQ131",


                    "hitpoint": "HitPylon1"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon2 [Indent level: 4],

                "pylon2": {

                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF"],

                    "priority": 4,

                    "maxweight": 1200,

                    "UIposition": [0.3,0.5],

                    "bay": -1,

                    "attachment": "rhs_mag_M151_7_USAF_LAU131",

                    "hitpoint": "HitPylon2"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon3 [Indent level: 4],

                "pylon3": {

                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_FFAR_USAF_3x","RHS_HP_HYDRA_USAF","RHS_HP_HYDRA_USAF_3x","RHS_HP_AGM65_3x","RHS_HP_BOMB_500_3x"],

                    "priority": 3,

                    "maxweight": 1200,

                    "UIposition": [0.3,0.45],

                    "bay": -1,

                    "attachment": "rhs_mag_agm65d",

                    "hitpoint": "HitPylon3"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon4 [Indent level: 4],

                "pylon4": {

                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF","RHS_HP_FFAR_USAF_3x","RHS_HP_HYDRA_USAF_3x","RHS_HP_BOMB_500_3x"],

                    "priority": 2,

                    "maxweight": 1200,

                    "UIposition": [0.35,0.375],

                    "bay": -1,

                    "attachment": "rhs_mag_gbu12",

                    "hitpoint": "HitPylon4"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon5 [Indent level: 4],

                "pylon5": {

                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF"],

                    "priority": 1,

                    "maxweight": 1200,

                    "UIposition": [0.35,0.325],

                    "bay": -1,

                    "attachment": "rhs_mag_gbu12",

                    "hitpoint": "HitPylon5"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon6 [Indent level: 4],

                "pylon6": {

                    "hardpoints": [],

                    "priority": 1,

                    "maxweight": 1200,

                    "UIposition": [0.35,0.275],

                    "bay": -1,

                    "attachment": "",

                    "hitpoint": "HitPylon6"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon7 [Indent level: 4],

                "pylon7": {

                    "UIposition": [0.35,0.225],

                    "mirroredMissilePos": 5,

                    "hitpoint": "HitPylon7",

                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF"],

                    "priority": 1,

                    "maxweight": 1200,

                    "bay": -1,

                    "attachment": "rhs_mag_gbu12"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon8 [Indent level: 4],

                "pylon8": {

                    "UIposition": [0.35,0.175],

                    "mirroredMissilePos": 4,

                    "hitpoint": "HitPylon8",

                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF","RHS_HP_FFAR_USAF_3x","RHS_HP_HYDRA_USAF_3x","RHS_HP_BOMB_500_3x"],

                    "priority": 2,

                    "maxweight": 1200,

                    "bay": -1,

                    "attachment": "rhs_mag_gbu12"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon9 [Indent level: 4],

                "pylon9": {

                    "UIposition": [0.3,0.1],

                    "mirroredMissilePos": 3,

                    "hitpoint": "HitPylon9",

                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_FFAR_USAF_3x","RHS_HP_HYDRA_USAF","RHS_HP_HYDRA_USAF_3x","RHS_HP_AGM65_3x","RHS_HP_BOMB_500_3x"],

                    "priority": 3,

                    "maxweight": 1200,

                    "bay": -1,

                    "attachment": "rhs_mag_agm65d"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon10 [Indent level: 4],

                "pylon10": {

                    "UIposition": [0.3,0.05],

                    "mirroredMissilePos": 2,

                    "hitpoint": "HitPylon10",

                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF"],

                    "priority": 4,

                    "maxweight": 1200,

                    "bay": -1,

                    "attachment": "rhs_mag_M151_7_USAF_LAU131"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon11 [Indent level: 4],

                "pylon11": {

                    "hardpoints": ["RHS_HP_AIM9_2x","RHS_HP_LGB_500"],

                    "UIposition": [0.3,0],

                    "attachment": "rhs_mag_aim9m_2",

                    "mirroredMissilePos": 1,

                    "hitpoint": "HitPylon11",

                    "priority": 5,

                    "maxweight": 1200,

                    "bay": -1
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4],

                "cmDispenser": {

                    "hardpoints": ["RHSUSF_cm_ANALE40_x2","RHSUSF_cm_ANALE40_x4","RHSUSF_cm_ANALE40_x8","RHSUSF_cm_ANALE40_x16"],

                    "priority": 1,

                    "attachment": "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x16",

                    "maxweight": 800,

                    "UIposition": [0.625,0.275]
                }
            },

            # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|Presets [Indent level: 3],

            "Presets": {

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|Presets|AT [Indent level: 4],


                "AT": {


                    "attachment": ["rhs_mag_ANALQ131","rhs_mag_M151_7_USAF_LAU131","rhs_mag_agm65d_3","rhs_mag_gbu12","rhs_mag_gbu12","","rhs_mag_gbu12","rhs_mag_gbu12","rhs_mag_agm65d_3","rhs_mag_M151_7_USAF_LAU131","rhs_mag_aim9m_2","rhsusf_ANALE40_CMFlare_Chaff_Magazine_x16"],


                    "displayname": "Anti-Tank"
                },

                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|Presets|CAS [Indent level: 4],

                "CAS": {

                    "attachment": ["rhs_mag_ANALQ131","rhs_mag_M151_7_USAF_LAU131","rhs_mag_agm65d","rhs_mag_gbu12","rhs_mag_gbu12","","rhs_mag_gbu12","rhs_mag_gbu12","rhs_mag_agm65d","rhs_mag_M151_7_USAF_LAU131","rhs_mag_aim9m_2","rhsusf_ANALE40_CMFlare_Chaff_Magazine_x16"],

                    "displayname": "Close Air Support"
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent [Indent level: 2],
        "SensorsManagerComponent": {
            # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components [Indent level: 3],

            "Components": {

                # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|VisualSensorComponent [Indent level: 4],


                "VisualSensorComponent": {


                    # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|VisualSensorComponent|AirTarget [Indent level: 5],



                    "AirTarget": {



                        "minRange": 500,



                        "maxRange": 4000,



                        "objectDistanceLimitCoef": -1,



                        "viewDistanceLimitCoef": 1
                    },


                    # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|VisualSensorComponent|GroundTarget [Indent level: 5],


                    "GroundTarget": {


                        "minRange": 500,


                        "maxRange": 4000,


                        "objectDistanceLimitCoef": 1,


                        "viewDistanceLimitCoef": 1
                    },


                    "angleRangeHorizontal": 25,


                    "angleRangeVertical": 20,


                    "typeRecognitionDistance": -1,


                    "groundNoiseDistanceCoef": 0.07,


                    "maxGroundNoiseDistance": 0,


                    "minSpeedThreshold": 0,


                    "maxSpeedThreshold": 0,


                    "maxFogSeeThrough": 0.95,


                    "minTrackableSpeed": 0,


                    "maxTrackableSpeed": 695,


                    "animDirection": "PilotCamera_V",


                    "componentType": "VisualSensorComponent",


                    "nightRangeCoef": 0,


                    "color": [1,1,0.5,0.8],


                    "allowsMarking": 1,


                    "aimDown": 0,


                    "minTrackableATL": -1e+010,


                    "maxTrackableATL": 1e+010
                },

                # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4],

                "LaserSensorComponent": {

                    # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|LaserSensorComponent|AirTarget [Indent level: 5],


                    "AirTarget": {


                        "minRange": 10000,


                        "maxRange": 10000,


                        "objectDistanceLimitCoef": -1,


                        "viewDistanceLimitCoef": -1
                    },

                    # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|LaserSensorComponent|GroundTarget [Indent level: 5],

                    "GroundTarget": {

                        "minRange": 10000,

                        "maxRange": 10000,

                        "objectDistanceLimitCoef": -1,

                        "viewDistanceLimitCoef": -1
                    },

                    "angleRangeHorizontal": 25,

                    "angleRangeVertical": 20,

                    "typeRecognitionDistance": -1,

                    "maxGroundNoiseDistance": 0,

                    "maxFogSeeThrough": 0.3,

                    "animDirection": "PilotCamera_V",

                    "componentType": "LaserSensorComponent",

                    "color": [1,1,1,0],

                    "allowsMarking": 1,

                    "groundNoiseDistanceCoef": -1,

                    "minSpeedThreshold": 0,

                    "maxSpeedThreshold": 0,

                    "aimDown": 0,

                    "minTrackableSpeed": -1e+010,

                    "maxTrackableSpeed": 1e+010,

                    "minTrackableATL": -1e+010,

                    "maxTrackableATL": 1e+010
                },

                # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4],

                "PassiveRadarSensorComponent": {

                    "componentType": "PassiveRadarSensorComponent",

                    # Class: SensorTemplatePassiveRadar|AirTarget [Indent level: 0],

                    "AirTarget": {

                        "minRange": 16000,

                        "maxRange": 16000,

                        "objectDistanceLimitCoef": -1,

                        "viewDistanceLimitCoef": -1
                    },

                    # Class: SensorTemplatePassiveRadar|GroundTarget [Indent level: 0],

                    "GroundTarget": {

                        "minRange": 16000,

                        "maxRange": 16000,

                        "objectDistanceLimitCoef": -1,

                        "viewDistanceLimitCoef": -1
                    },

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
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3],

            "Components": {

                # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4],


                "EmptyDisplay": {


                    "componentType": "EmptyDisplayComponent"
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultDisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "VehicleSystemsDisplayManagerComponentRight": {
            "defaultDisplay": "SensorDisplay",
            # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "Components": {
                # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4],

                "EmptyDisplay": {

                    "componentType": "EmptyDisplayComponent"
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|RHS_A10|Components|ForcedCam [Indent level: 2],
        "ForcedCam": {
            "componentType": "VehicleSystemsDisplayManager",
            "defaultDisplay": "VehicleDriverDisplay",
            "x": 11,
            "y": 11,
            # Class: CfgVehicles|RHS_A10|Components|ForcedCam|Components [Indent level: 3],
            "Components": {
                # Class: CfgVehicles|RHS_A10|Components|ForcedCam|Components|VehicleDriverDisplay [Indent level: 4],

                "VehicleDriverDisplay": {

                    "componentType": "TransportFeedDisplayComponent",

                    "source": "Driver"
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Components|TransportCountermeasuresComponent [Indent level: 2],
        "TransportCountermeasuresComponent": {
        }
    },
    # Class: CfgVehicles|RHS_A10|AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles|RHS_A10|AnimationSources|gatling [Indent level: 2],

        "gatling": {

            "weapon": "RHS_weap_GAU8",

            "source": "revolving"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "weapon": "RHS_weap_GAU8",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|eject [Indent level: 2],
        "eject": {
            "source": "door",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|eject_hide [Indent level: 2],
        "eject_hide": {
            "source": "user",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Hide_Monitor [Indent level: 2],
        "Hide_Monitor": {
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|tvm_locked [Indent level: 2],
        "tvm_locked": {
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|ind_beacon_source [Indent level: 2],
        "ind_beacon_source": {
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|throttle_source [Indent level: 2],
        "throttle_source": {
            "animPeriod": 10,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|HitFuel_1_source [Indent level: 2],
        "HitFuel_1_source": {
            "source": "hit",
            "hitpoint": "HitFuel"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|HitFuel_2_source [Indent level: 2],
        "HitFuel_2_source": {
            "source": "hit",
            "hitpoint": "HitFuel2"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Damper_1_source [Indent level: 2],
        "Damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Damper_2_source [Indent level: 2],
        "Damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Damper_3_source [Indent level: 2],
        "Damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Wheel_1_source [Indent level: 2],
        "Wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Wheel_2_source [Indent level: 2],
        "Wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Wheel_3_source [Indent level: 2],
        "Wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|mirror_fold [Indent level: 2],
        "mirror_fold": {
            "source": "user",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_1_source [Indent level: 2],
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_2_source [Indent level: 2],
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_3_source [Indent level: 2],
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_4_source [Indent level: 2],
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_5_source [Indent level: 2],
        "hit_pylon_5_source": {
            "source": "Hit",
            "hitpoint": "HitPylon5"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_6_source [Indent level: 2],
        "hit_pylon_6_source": {
            "source": "Hit",
            "hitpoint": "HitPylon6"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_7_source [Indent level: 2],
        "hit_pylon_7_source": {
            "source": "Hit",
            "hitpoint": "HitPylon7"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_8_source [Indent level: 2],
        "hit_pylon_8_source": {
            "source": "Hit",
            "hitpoint": "HitPylon8"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_9_source [Indent level: 2],
        "hit_pylon_9_source": {
            "source": "Hit",
            "hitpoint": "HitPylon9"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_10_source [Indent level: 2],
        "hit_pylon_10_source": {
            "source": "Hit",
            "hitpoint": "HitPylon10"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|hit_pylon_11_source [Indent level: 2],
        "hit_pylon_11_source": {
            "source": "Hit",
            "hitpoint": "HitPylon11"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Gatling_30mm_ammorandom [Indent level: 2],
        "Gatling_30mm_ammorandom": {
            "source": "ammorandom",
            "weapon": "Gatling_30mm_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Gatling_30mm_reload [Indent level: 2],
        "Gatling_30mm_reload": {
            "source": "reload",
            "weapon": "Gatling_30mm_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Gatling_30mm_revolving [Indent level: 2],
        "Gatling_30mm_revolving": {
            "source": "revolving",
            "weapon": "Gatling_30mm_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Missile_AA_04_revolving [Indent level: 2],
        "Missile_AA_04_revolving": {
            "source": "revolving",
            "weapon": "Missile_AA_04_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Missile_AGM_02_revolving [Indent level: 2],
        "Missile_AGM_02_revolving": {
            "source": "revolving",
            "weapon": "Missile_AGM_02_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Rocket_04_HE_revolving [Indent level: 2],
        "Rocket_04_HE_revolving": {
            "source": "revolving",
            "weapon": "Rocket_04_HE_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Rocket_04_AP_revolving [Indent level: 2],
        "Rocket_04_AP_revolving": {
            "source": "revolving",
            "weapon": "Rocket_04_AP_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Bomb_04_revolving [Indent level: 2],
        "Bomb_04_revolving": {
            "source": "revolving",
            "weapon": "Bomb_04_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|HitAvionics [Indent level: 2],
        "HitAvionics": {
            "source": "Hit",
            "hitpoint": "HitAvionics",
            "raw": 1
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|HideWeapons [Indent level: 2],
        "HideWeapons": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|HideMFD [Indent level: 2],
        "HideMFD": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|canopy_hide [Indent level: 2],
        "canopy_hide": {
            "source": "user",
            "animPeriod": 0.001,
            "initPhase": 0
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|ejection_seat_hide [Indent level: 2],
        "ejection_seat_hide": {
            "source": "user",
            "animPeriod": 0.001,
            "initPhase": 0
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|ejection_seat_motion [Indent level: 2],
        "ejection_seat_motion": {
            "source": "user",
            "animPeriod": 0.25,
            "initPhase": 0
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightRed_source [Indent level: 2],
        "CollisionLightRed_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionRed"
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightWhite_source [Indent level: 2],
        "CollisionLightWhite_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionWhite"
        }
    },
    # Class: CfgVehicles|RHS_A10|compartmentsLights [Indent level: 1],
    "compartmentsLights": {
        # Class: CfgVehicles|RHS_A10|compartmentsLights|Comp1 [Indent level: 2],

        "Comp1": {

            # Class: CfgVehicles|RHS_A10|compartmentsLights|Comp1|Light_General [Indent level: 3],


            "Light_General": {


                "color": [20,30,30],


                "ambient": [0,0,0],


                "intensity": 8.05,


                "size": 0,


                "useFlare": 0,


                "flareSize": 0,


                "flareMaxDistance": 0,


                "dayLight": 1,


                "blinking": 0,


                # Class: CfgVehicles|RHS_A10|compartmentsLights|Comp1|Light_General|Attenuation [Indent level: 4],


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
    # Class: CfgVehicles|RHS_A10|Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles|RHS_A10|Reflectors|Gear_Light [Indent level: 2],

        "Gear_Light": {

            "color": [70,75,100,1],

            "ambient": [1,1,1,0],

            "position": "L svetlo",

            "direction": "konec L svetla",

            "hitpoint": "L svetlo",

            "selection": "L svetlo",

            "size": 1,

            "innerAngle": 20,

            "outerAngle": 50,

            "coneFadeCoef": 3,

            "intensity": 1000,

            "useFlare": 0,

            "dayLight": 1,

            "FlareSize": 4,

            # Class: CfgVehicles|RHS_A10|Reflectors|Gear_Light|Attenuation [Indent level: 3],

            "Attenuation": {

                "start": 0,

                "constant": 0,

                "linear": 0,

                "quadratic": 0.15,

                "hardLimitStart": 55,

                "hardLimitEnd": 100
            }
        },
        # Class: CfgVehicles|RHS_A10|Reflectors|Gear_Light_Flare [Indent level: 2],
        "Gear_Light_Flare": {
            "outerAngle": 179,
            "useFlare": 1,
            "intensity": 50,
            "coneFadeCoef": 13,
            # Class: CfgVehicles|RHS_A10|Reflectors|Gear_Light_Flare|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 20
            },
            "color": [70,75,100,1],
            "ambient": [1,1,1,0],
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerAngle": 20,
            "dayLight": 1,
            "FlareSize": 4
        }
    },
    "aggregateReflectors": [["Gear_Light"],["Gear_Light_Flare"]],
    # Class: CfgVehicles|RHS_A10|MarkerLights [Indent level: 1],
    "MarkerLights": {
        # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionRed [Indent level: 2],

        "CollisionRed": {

            "color": [0.8,0,0],

            "ambient": [0.09,0,0],

            "intensity": 75,

            "name": "cerveny pozicni",

            "drawLight": 1,

            "drawLightSize": 0.25,

            "drawLightCenterSize": 0.05,

            "activeLight": 0,

            "blinking": 1,

            "dayLight": 0,

            "useFlare": 0,

            "blinkingPattern": [0.2,1.3],

            "blinkingPatternGuarantee": 0,

            # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionRed|Attenuation [Indent level: 3],

            "Attenuation": {

                "start": 0,

                "constant": 0,

                "linear": 25,

                "quadratic": 50,

                "hardLimitStart": 0.75,

                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionGreen [Indent level: 2],
        "CollisionGreen": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "zeleny pozicni",
            "blinkingPattern": [0.2,0.9],
            "intensity": 75,
            "drawLight": 1,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.05,
            "activeLight": 0,
            "blinking": 1,
            "dayLight": 0,
            "useFlare": 0,
            "blinkingPatternGuarantee": 0,
            # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionRed|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles|RHS_A10|MarkerLights|PositionWhiteTop [Indent level: 2],
        "PositionWhiteTop": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "bily pozicni",
            "drawLightSize": 0.2,
            "blinking": 0,
            "intensity": 75,
            "drawLight": 1,
            "drawLightCenterSize": 0.05,
            "activeLight": 0,
            "dayLight": 0,
            "useFlare": 0,
            "blinkingPattern": [0.2,1.3],
            "blinkingPatternGuarantee": 0,
            # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionRed|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionWhiteRear [Indent level: 2],
        "CollisionWhiteRear": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "cerveny pozicni blik",
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.04,
            "intensity": 75,
            "drawLight": 1,
            "activeLight": 0,
            "blinking": 1,
            "dayLight": 0,
            "useFlare": 0,
            "blinkingPattern": [0.2,1.3],
            # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionRed|Attenuation [Indent level: 3],
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
    # Class: CfgVehicles|RHS_A10|RenderTargets [Indent level: 1],
    "RenderTargets": {
        # Class: CfgVehicles|RHS_A10|RenderTargets|Mirror [Indent level: 2],

        "Mirror": {

            "renderTarget": "rendertarget0",

            # Class: CfgVehicles|RHS_A10|RenderTargets|Mirror|CameraView1 [Indent level: 3],

            "CameraView1": {

                "pointPosition": "PIP_mirror_0",

                "pointDirection": "PIP_mirror_0_dir",

                "renderQuality": 0,

                "renderVisionMode": 0,

                "fov": 1
            },

            "BBoxes": ["PIP_0_TL","PIP_0_TR","PIP_0_BL","PIP_0_BR"]
        }
    },
    "damageResistance": 0.0048,
    "epeImpulseDamageCoef": 1,
    "maxSpeed": 834,
    "landingAoa": "rad 10",
    "landingSpeed": 220,
    "gearUpTime": 4.5,
    "gearDownTime": 3,
    "angleOfIndicence": 0.0523599,
    "draconicForceXCoef": 7.2,
    "draconicForceYCoef": 2.6,
    "draconicForceZCoef": 0.15,
    "draconicTorqueXCoef": 1.29,
    "draconicTorqueYCoef": 3.1,
    "thrustCoef": [0.91,0.84,0.9,1.3,1.2,1.2,1.1,1,0.93,0.2,0.1,0,0],
    "envelope": [0,0.1,0.61,2.2,3.7,4.9,6,5.5,5.8,4.7,3.4,1.8,0],
    "aileronControlsSensitivityCoef": 3,
    "elevatorControlsSensitivity": 2,
    "rudderControlsSensitivityoef": 4,
    "elevatorCoef": [0.7,0.9,0.55,0.4,0.39,0.3,0.3],
    "aileronCoef": [0.6,1,0.97,0.9,0.85,0.87,0.75],
    "rudderCoef": [0.7,1,1,0.9,0.82,0.73,0.6],
    "brakeDistance": 85,
    "aileronSensitivity": 0.75,
    "elevatorSensitivity": 1.9,
    "wheelSteeringSensitivity": 1.6,
    "flapsFrictionCoef": 0.6,
    "airFriction0": [100,60,12],
    "airFriction1": [100,60,12],
    "airFriction2": [100,60,12],
    # Class: CfgVehicles|RHS_A10|TransportMagazines [Indent level: 1],
    "TransportMagazines": {
        # Class: CfgVehicles|RHS_A10|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2],

        "_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag": {

            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",

            "count": 4
        },
        # Class: CfgVehicles|RHS_A10|TransportMagazines|_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 2
        },
        # Class: CfgVehicles|RHS_A10|TransportMagazines|_xx_rhs_mag_m18_yellow [Indent level: 2],
        "_xx_rhs_mag_m18_yellow": {
            "magazine": "rhs_mag_m18_yellow",
            "count": 2
        },
        # Class: CfgVehicles|RHS_A10|TransportMagazines|_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 2
        },
        # Class: CfgVehicles|RHS_A10|TransportMagazines|_xx_rhs_mag_m18_purple [Indent level: 2],
        "_xx_rhs_mag_m18_purple": {
            "magazine": "rhs_mag_m18_purple",
            "count": 2
        },
        # Class: CfgVehicles|RHS_A10|TransportMagazines|_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 2
        }
    },
    # Class: CfgVehicles|RHS_A10|TransportItems [Indent level: 1],
    "TransportItems": {
        # Class: CfgVehicles|RHS_A10|TransportItems|_xx_FirstAidKit [Indent level: 2],

        "_xx_FirstAidKit": {

            "name": "FirstAidKit",

            "count": 2
        }
    },
    # Class: CfgVehicles|RHS_A10|WingVortices [Indent level: 1],
    "WingVortices": {
        # Class: CfgVehicles|RHS_A10|WingVortices|WingTipLeft [Indent level: 2],

        "WingTipLeft": {

            "effectName": "WingVortices",

            "position": "body_vapour_L_E"
        },
        # Class: CfgVehicles|RHS_A10|WingVortices|WingTipRight [Indent level: 2],
        "WingTipRight": {
            "effectName": "WingVortices",
            "position": "body_vapour_R_E"
        },
        # Class: CfgVehicles|RHS_A10|WingVortices|BodyLeft [Indent level: 2],
        "BodyLeft": {
            "effectName": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles|RHS_A10|WingVortices|BodyRight [Indent level: 2],
        "BodyRight": {
            "effectName": "BodyVortices",
            "position": "body_vapour_R_S"
        }
    },
    "attenuationEffectType": "HeliAttenuation",
    # Class: CfgVehicles|RHS_A10|Damage [Indent level: 1],
    "Damage": {
        "tex": ["rhsusf|addons|rhsusf_a2port_air|a10|data|rhs_a10_warning_lights_off_ca.paa","rhsusf|addons|rhsusf_a2port_air|a10|data|rhs_a10_warning_lights_ca.paa"],
        "mat": ["rhsusf|addons|rhsusf_a2port_air|a10|data|a10_skla.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|a10_skla_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|a10_skla_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|a10_cockpit_glass_in.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|a10_cockpit_glass_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|a10_cockpit_glass_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_01.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_01_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_01_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_02.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_02_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_02_destruct.rvmat"]
    },
    # Class: CfgVehicles|RHS_A10|Library [Indent level: 1],
    "Library": {
        "libEnable": 1,
        "libTextDesc": "The Fairchild Republic A-10 Thunderbolt II is an American twin/single-seat, twin-engine, straight-wing jet aircraft developed by Fairchild-Republic in the early 1970s. The A-10 was designed around the GAU-8 Avenger, a rotary cannon that is the airplane's primary armament and the heaviest such cannon mounted on an aircraft. The A-10's airframe was designed for survivability, with protective measures such as 1,200 pounds (540 kg) of armor to enable the aircraft to continue flying after taking significant damage."
    },
    "availableForSupportTypes": ["CAS_Bombing"],
    "armor": 60,
    "armorStructural": 2,
    # Class: CfgVehicles|RHS_A10|Hitpoints [Indent level: 1],
    "Hitpoints": {
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitHull [Indent level: 2],

        "HitHull": {

            "armor": 999,

            "explosionShielding": 0,

            "passThrough": 0.01,

            "minimalHit": 1,

            "radius": 0.15,

            "material": -1,

            "name": "hit_hull",

            "visual": "-",

            "depends": "Total"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitAvionics [Indent level: 2],
        "HitAvionics": {
            "armor": 0.2,
            "explosionShielding": 0.6,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitEngine [Indent level: 2],
        "HitEngine": {
            "armor": 0.5,
            "explosionShielding": 0.25,
            "passThrough": 0.2,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_l",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitEngine2 [Indent level: 2],
        "HitEngine2": {
            "armor": 0.5,
            "explosionShielding": 0.25,
            "passThrough": 0.2,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_r",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitFuel [Indent level: 2],
        "HitFuel": {
            "armor": 1,
            "explosionShielding": 0.2,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel",
            "visual": "vis_fuel",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitFuel_left [Indent level: 2],
        "HitFuel_left": {
            "armor": 0.5,
            "explosionShielding": 0.7,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_fuel_wing_l",
            "visual": "vis_wing_l",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitFuel_right [Indent level: 2],
        "HitFuel_right": {
            "armor": 0.5,
            "explosionShielding": 0.7,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_fuel_wing_r",
            "visual": "vis_wing_r",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitFuel2 [Indent level: 2],
        "HitFuel2": {
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0.1,
            "minimalHit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "-",
            "depends": "(HitFuel_left+HitFuel_right)*0.5"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitLAileron_link [Indent level: 2],
        "HitLAileron_link": {
            "armor": 0.6,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_l",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitRAileron_link [Indent level: 2],
        "HitRAileron_link": {
            "armor": 0.6,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_r",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitLAileron [Indent level: 2],
        "HitLAileron": {
            "armor": 0.6,
            "explosionShielding": 0.5,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "visual": "vis_wing_l",
            "depends": "HitLAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitRAileron [Indent level: 2],
        "HitRAileron": {
            "armor": 0.6,
            "explosionShielding": 0.5,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "visual": "vis_wing_r",
            "depends": "HitRAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitControlRear [Indent level: 2],
        "HitControlRear": {
            "armor": 0.6,
            "explosionShielding": 0.1,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.17,
            "material": -1,
            "name": "hit_control_rear",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitLCElevator [Indent level: 2],
        "HitLCElevator": {
            "armor": 0.6,
            "explosionShielding": 0.5,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitRElevator [Indent level: 2],
        "HitRElevator": {
            "armor": 0.6,
            "explosionShielding": 0.5,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitLCRudder [Indent level: 2],
        "HitLCRudder": {
            "armor": 0.7,
            "explosionShielding": 0.5,
            "passThrough": 0.1,
            "minimalHit": 0.02,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder_l",
            "visual": "vis_rudder_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitRRudder [Indent level: 2],
        "HitRRudder": {
            "armor": 0.7,
            "explosionShielding": 0.5,
            "passThrough": 0.1,
            "minimalHit": 0.02,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder_r",
            "visual": "vis_rudder_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "armor": 0.6,
            "explosionShielding": 0.7,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "glass_1",
            "visual": "glass_1",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|WarningElevator [Indent level: 2],
        "WarningElevator": {
            "armor": 9999,
            "explosionShielding": 0,
            "passThrough": 0,
            "minimalHit": 1,
            "radius": 0,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "ind_elevator",
            "depends": "HitLCElevator+HitRElevator"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|WarningAileron [Indent level: 2],
        "WarningAileron": {
            "armor": 9999,
            "explosionShielding": 0,
            "passThrough": 0,
            "minimalHit": 1,
            "radius": 0,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "ind_aileron",
            "depends": "HitLAileron+HitRAileron"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1 [Indent level: 2],
        "HitPylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2 [Indent level: 2],
        "HitPylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3 [Indent level: 2],
        "HitPylon3": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_3",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4 [Indent level: 2],
        "HitPylon4": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_4",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5 [Indent level: 2],
        "HitPylon5": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_5",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6 [Indent level: 2],
        "HitPylon6": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_6",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7 [Indent level: 2],
        "HitPylon7": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_7",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8 [Indent level: 2],
        "HitPylon8": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_8",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_8",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_8",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_8",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_8",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9 [Indent level: 2],
        "HitPylon9": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_9",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_9",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_9",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_9",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_9",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10 [Indent level: 2],
        "HitPylon10": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_10",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_10",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_10",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_10",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_10",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11 [Indent level: 2],
        "HitPylon11": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_11",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_11",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_11",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_11",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_11",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        }
    },
    # Class: CfgVehicles|RHS_A10|UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles|RHS_A10|UserActions|SAFEMODE [Indent level: 2],

        "SAFEMODE": {

            "displayName": "<t color='#00FF7F'>MASTERSAFE</t>",

            "condition": "(call rhsusf_fnc_findPlayer) in this",

            "statement": "(call rhsusf_fnc_findPlayer) action ['SwitchWeapon', this, (call rhsusf_fnc_findPlayer), -1];",

            "position": "",

            "radius": 10,

            "priority": 10.5,

            "onlyforplayer": 1,

            "showWindow": 0,

            "shortcut": "user13",

            "hideOnUse": 1
        },
        # Class: CfgVehicles|RHS_A10|UserActions|Toggle_LandingMode [Indent level: 2],
        "Toggle_LandingMode": {
            "displayName": "Toggle Landing Mode",
            "condition": "(call rhsusf_fnc_findPlayer) in this && currentWeapon this == ''",
            "statement": "this setUserMFDvalue [4, abs(((getUserMFDvalue this) select 4)-1)]",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showWindow": 0,
            "shortcut": "user14",
            "hideOnUse": 1
        },
        # Class: CfgVehicles|RHS_A10|UserActions|Mirrors [Indent level: 2],
        "Mirrors": {
            "displayName": "<t color='#FBB829'>Toggle mirrors</t>",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showWindow": 0,
            "hideOnUse": 1,
            "condition": "(call rhs_fnc_findPlayer) in this",
            "shortcut": "",
            "statement": "this animateSource ['mirror_fold',abs((this animationSourcePhase 'mirror_fold') -1)]"
        }
    },
    # Class: CfgVehicles|RHS_A10|EventHandlers [Indent level: 1],
    "EventHandlers": {
        "hit": "",
        # Class: CfgVehicles|RHS_A10|EventHandlers|RHSUSF_EventHandlers [Indent level: 2],
        "RHSUSF_EventHandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "getout": "[_this select 0, _this select 2,'rhs_a10_canopy'] call rhs_fnc_ACESII_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes;"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "defaultUserMFDvalues": [0.15,1,0.15,1,0],
    # Class: CfgVehicles|RHS_A10|MFD [Indent level: 1],
    "MFD": {
        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD [Indent level: 2],

        "AirplaneHUD": {

            "topLeft": "HUD LH",

            "topRight": "HUD PH",

            "bottomLeft": "HUD LD",

            "borderLeft": 0,

            "borderRight": 0,

            "borderTop": 0,

            "borderBottom": 0.2,

            "color": [0.15,1,0.15,1],

            "enableParallax": 1,

            "font": "rhsusf_digital_font_usa",

            # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones [Indent level: 3],

            "Bones": {

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|PlaneOrientation [Indent level: 4],


                "PlaneOrientation": {


                    "type": "fixed",


                    "pos": [0.498,0.48]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|WeaponAim [Indent level: 4],

                "WeaponAim": {

                    "type": "vector",

                    "source": "weapon",

                    "pos0": [0.498,0.485],

                    "pos10": [1.256,1.41]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|WeaponAimAA [Indent level: 4],

                "WeaponAimAA": {

                    "type": "vector",

                    "source": "weapon",

                    "pos0": [0.498,0.085],

                    "pos10": [1.256,1.11]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|Target [Indent level: 4],

                "Target": {

                    "type": "vector",

                    "source": "target",

                    "pos0": [0.498,0.535],

                    "pos10": [1.256,1.56]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|TargetingPodDir [Indent level: 4],

                "TargetingPodDir": {

                    "source": "pilotcamera",

                    "type": "vector",

                    "pos0": [0.498,0.435],

                    "pos10": [1.306,1.56]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|TargetingPodTarget [Indent level: 4],

                "TargetingPodTarget": {

                    "source": "pilotcameratarget",

                    "pos0": [0.498,0.535],

                    "pos10": [1.256,1.56],

                    "type": "vector"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|ImpactPoint [Indent level: 4],

                "ImpactPoint": {

                    "type": "vector",

                    "source": "ImpactPoint",

                    "pos0": [0.5,0.485],

                    "pos10": [1.258,1.41]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|NormalizeBombCircle [Indent level: 4],

                "NormalizeBombCircle": {

                    "type": "normalizedorsmaller",

                    "limit": 0.08,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],

                "Velocity": {

                    "type": "vector",

                    "source": "velocity",

                    "pos0": [0.498,0.485],

                    "pos10": [1.256,1.41]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],

                "Level0": {

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon",

                    "angle": 0
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP05 [Indent level: 4],

                "LevelP05": {

                    "angle": 5,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM05 [Indent level: 4],

                "LevelM05": {

                    "angle": -5,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP10 [Indent level: 4],

                "LevelP10": {

                    "angle": 10,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM10 [Indent level: 4],

                "LevelM10": {

                    "angle": -10,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP15 [Indent level: 4],

                "LevelP15": {

                    "angle": 15,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM15 [Indent level: 4],

                "LevelM15": {

                    "angle": -15,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP20 [Indent level: 4],

                "LevelP20": {

                    "angle": 20,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM20 [Indent level: 4],

                "LevelM20": {

                    "angle": -20,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP25 [Indent level: 4],

                "LevelP25": {

                    "angle": 25,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM25 [Indent level: 4],

                "LevelM25": {

                    "angle": -25,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP30 [Indent level: 4],

                "LevelP30": {

                    "angle": 30,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM30 [Indent level: 4],

                "LevelM30": {

                    "angle": -30,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP35 [Indent level: 4],

                "LevelP35": {

                    "angle": 35,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM35 [Indent level: 4],

                "LevelM35": {

                    "angle": -35,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP40 [Indent level: 4],

                "LevelP40": {

                    "angle": 40,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM40 [Indent level: 4],

                "LevelM40": {

                    "angle": -40,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP45 [Indent level: 4],

                "LevelP45": {

                    "angle": 45,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM45 [Indent level: 4],

                "LevelM45": {

                    "angle": -45,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP50 [Indent level: 4],

                "LevelP50": {

                    "angle": 50,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM50 [Indent level: 4],

                "LevelM50": {

                    "angle": -50,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP60 [Indent level: 4],

                "LevelP60": {

                    "angle": 60,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM60 [Indent level: 4],

                "LevelM60": {

                    "angle": -60,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP70 [Indent level: 4],

                "LevelP70": {

                    "angle": 70,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM70 [Indent level: 4],

                "LevelM70": {

                    "angle": -70,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP80 [Indent level: 4],

                "LevelP80": {

                    "angle": 80,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM80 [Indent level: 4],

                "LevelM80": {

                    "angle": -80,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP90 [Indent level: 4],

                "LevelP90": {

                    "angle": 90,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM90 [Indent level: 4],

                "LevelM90": {

                    "angle": -90,

                    "pos0": [0.498,0.48],

                    "pos10": [1.7292,1.884],

                    "type": "horizon"
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|Limit0109 [Indent level: 4],

                "Limit0109": {

                    "type": "limit",

                    "limits": [0.1,0.1,0.9,0.9]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LimitWaypoint [Indent level: 4],

                "LimitWaypoint": {

                    "type": "limit",

                    "limits": [0.2,0.97,0.8,0.97]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|WPPoint [Indent level: 4],

                "WPPoint": {

                    "type": "vector",

                    "source": "WPPoint",

                    "pos0": [0.5,0.485],

                    "pos10": [1.258,1.41]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|VerticalSpeed [Indent level: 4],

                "VerticalSpeed": {

                    "type": "linear",

                    "source": "vspeed",

                    "sourceScale": 1,

                    "min": -100,

                    "max": 100,

                    "minPos": [0,0.15],

                    "maxPos": [0,-0.15]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|HorizonIndicatorBank [Indent level: 4],

                "HorizonIndicatorBank": {

                    "type": "rotational",

                    "source": "horizonBank",

                    "sourceScale": 1,

                    "center": [0.065,0.12],

                    "min": -3.14159,

                    "max": 3.14159,

                    "minAngle": 0,

                    "maxAngle": 360,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|HorizonIndicatorDive [Indent level: 4],

                "HorizonIndicatorDive": {

                    "source": "horizonDive",

                    "min": -1.5708,

                    "max": 1.5708,

                    "minAngle": 90,

                    "maxAngle": -90,

                    "type": "rotational",

                    "sourceScale": 1,

                    "center": [0.065,0.12],

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|TerrainBone [Indent level: 4],

                "TerrainBone": {

                    "type": "linear",

                    "source": "altitudeAGL",

                    "sourceScale": 1,

                    "sourceOffset": -1,

                    "min": 0,

                    "max": 500,

                    "minPos": [0,-0.195],

                    "maxPos": [0,0]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|TerrainBone2 [Indent level: 4],

                "TerrainBone2": {

                    "sourceOffset": 0,

                    "min": 500,

                    "max": 1500,

                    "minPos": [0,-0.078],

                    "maxPos": [0,0],

                    "type": "linear",

                    "source": "altitudeAGL",

                    "sourceScale": 1
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|VerticalSpeedBone [Indent level: 4],

                "VerticalSpeedBone": {

                    "type": "linear",

                    "source": "vspeed",

                    "sourceScale": 1,

                    "min": -10,

                    "max": 10,

                    "minPos": [0,-0.32],

                    "maxPos": [0,0.32]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot1 [Indent level: 4],

                "MissileFlightTimeRot1": {

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "max": 0.5,

                    "minAngle": 0,

                    "maxAngle": 18,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot2 [Indent level: 4],

                "MissileFlightTimeRot2": {

                    "maxAngle": 37,

                    "max": 2,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot3 [Indent level: 4],

                "MissileFlightTimeRot3": {

                    "maxAngle": 55.5,

                    "max": 3,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot4 [Indent level: 4],

                "MissileFlightTimeRot4": {

                    "maxAngle": 74,

                    "max": 4,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot5 [Indent level: 4],

                "MissileFlightTimeRot5": {

                    "maxAngle": 92.5,

                    "max": 5,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot6 [Indent level: 4],

                "MissileFlightTimeRot6": {

                    "maxAngle": 111,

                    "max": 6,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot7 [Indent level: 4],

                "MissileFlightTimeRot7": {

                    "maxAngle": 129.5,

                    "max": 7,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot8 [Indent level: 4],

                "MissileFlightTimeRot8": {

                    "maxAngle": 148,

                    "max": 8,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot9 [Indent level: 4],

                "MissileFlightTimeRot9": {

                    "maxAngle": 166.5,

                    "max": 9,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot10 [Indent level: 4],

                "MissileFlightTimeRot10": {

                    "maxAngle": 185,

                    "max": 10,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot11 [Indent level: 4],

                "MissileFlightTimeRot11": {

                    "maxAngle": 203.5,

                    "max": 11,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot12 [Indent level: 4],

                "MissileFlightTimeRot12": {

                    "maxAngle": 222,

                    "max": 12,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot13 [Indent level: 4],

                "MissileFlightTimeRot13": {

                    "maxAngle": 240.5,

                    "max": 13,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot14 [Indent level: 4],

                "MissileFlightTimeRot14": {

                    "maxAngle": 259,

                    "max": 14,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot15 [Indent level: 4],

                "MissileFlightTimeRot15": {

                    "maxAngle": 277.5,

                    "max": 15,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot16 [Indent level: 4],

                "MissileFlightTimeRot16": {

                    "maxAngle": 296,

                    "max": 16,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot17 [Indent level: 4],

                "MissileFlightTimeRot17": {

                    "maxAngle": 314.5,

                    "max": 17,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot18 [Indent level: 4],

                "MissileFlightTimeRot18": {

                    "maxAngle": 333,

                    "max": 18,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot19 [Indent level: 4],

                "MissileFlightTimeRot19": {

                    "maxAngle": 351.5,

                    "max": 19,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot20 [Indent level: 4],

                "MissileFlightTimeRot20": {

                    "maxAngle": 370,

                    "max": 20,

                    "type": "rotational",

                    "source": "MissileFlightTime",

                    "sourceScale": 1,

                    "center": [0,0],

                    "min": 0,

                    "minAngle": 0,

                    "aspectRatio": 1.22032
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|ILS_H [Indent level: 4],

                "ILS_H": {

                    "type": "ils",

                    "pos0": [0.5,0.485],

                    "pos3": [0.7274,0.485]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|ILS_W [Indent level: 4],

                "ILS_W": {

                    "pos3": [0.5,0.7625],

                    "type": "ils",

                    "pos0": [0.5,0.485]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LarAmmoMax [Indent level: 4],

                "LarAmmoMax": {

                    "type": "linear",

                    "source": "LarAmmoMax",

                    "sourceScale": 1,

                    "min": 0,

                    "max": 1,

                    "minPos": [0,1],

                    "maxPos": [0,0]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LarAmmoMin [Indent level: 4],

                "LarAmmoMin": {

                    "source": "LarAmmoMin",

                    "type": "linear",

                    "sourceScale": 1,

                    "min": 0,

                    "max": 1,

                    "minPos": [0,1],

                    "maxPos": [0,0]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LarTargetDist [Indent level: 4],

                "LarTargetDist": {

                    "source": "LarTargetDist",

                    "type": "linear",

                    "sourceScale": 1,

                    "min": 0,

                    "max": 1,

                    "minPos": [0,1],

                    "maxPos": [0,0]
                }
            },

            # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw [Indent level: 3],

            "Draw": {

                "alpha": "user3",

                "color": ["user0","user1","user2"],

                "condition": "on",

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|PlaneOrientationCrosshair [Indent level: 4],

                "PlaneOrientationCrosshair": {

                    "clipTL": [0,1],

                    "clipBR": [1,0],

                    "type": "line",

                    "width": 4,

                    "points": [["PlaneOrientation",[-0.01,0],1],["PlaneOrientation",[0.01,0],1],[],["PlaneOrientation",[0,-0.0122032],1],["PlaneOrientation",[0,0.0122032],1],[]]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|PlaneMovementCrosshair [Indent level: 4],

                "PlaneMovementCrosshair": {

                    "clipTL": [0,1],

                    "clipBR": [1,0],

                    "type": "line",

                    "width": 4,

                    "points": [["Velocity",[0,-0.0244063],1],["Velocity",[0.01,-0.0211359],1],["Velocity",[0.01732,-0.0122032],1],["Velocity",[0.02,0],1],["Velocity",[0.01732,0.0122032],1],["Velocity",[0.01,0.0211359],1],["Velocity",[0,0.0244063],1],["Velocity",[-0.01,0.0211359],1],["Velocity",[-0.01732,0.0122032],1],["Velocity",[-0.02,0],1],["Velocity",[-0.01732,-0.0122032],1],["Velocity",[-0.01,-0.0211359],1],["Velocity",[0,-0.0244063],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.0488127],1],["Velocity",[0,-0.0244063],1],[]]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BaroStatic [Indent level: 4],

                "BaroStatic": {

                    "type": "text",

                    "source": "static",

                    "text": "BARO",

                    "scale": 1,

                    "sourceScale": 1,

                    "align": "right",

                    "pos": [[0.06,0.68],1],

                    "right": [[0.12,0.68],1],

                    "down": [[0.06,0.74],1]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WeaponGroup [Indent level: 4],

                "WeaponGroup": {

                    "condition": "mgun + ATmissile + bomb + rocket",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WeaponGroup|SlantRange [Indent level: 5],

                    "SlantRange": {

                        "type": "text",

                        "source": "ImpactDistance",

                        "sourceScale": 1,

                        "sourceLength": 4,

                        "refreshRate": 0.1,

                        "align": "right",

                        "scale": 1,

                        "pos": [[0.04,0.86],1],

                        "right": [[0.1,0.86],1],

                        "down": [[0.04,0.92],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WeaponGroup|SlantRangeText [Indent level: 5],

                    "SlantRangeText": {

                        "type": "text",

                        "source": "static",

                        "text": "M",

                        "scale": 1,

                        "sourceScale": 1,

                        "align": "right",

                        "pos": [[0.155,0.86],1],

                        "right": [[0.215,0.86],1],

                        "down": [[0.155,0.92],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WeaponGroup|ValidTarget [Indent level: 5],

                    "ValidTarget": {

                        "condition": "targetDist>=1",

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WeaponGroup|ValidTarget|ImpactHeight [Indent level: 6],

                        "ImpactHeight": {

                            "type": "text",

                            "source": "targetHeight",

                            "sourceScale": 1,

                            "sourceLength": 1,

                            "refreshRate": 0.1,

                            "align": "right",

                            "scale": 1,

                            "pos": [[0.04,0.81],1],

                            "right": [[0.1,0.81],1],

                            "down": [[0.04,0.87],1]
                        }
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode [Indent level: 4],

                "NavigationMode": {

                    "condition": "1 - (mgun + AAmissile + ATmissile + bomb + rocket + user4)",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|VerticalSpeedScale [Indent level: 5],

                    "VerticalSpeedScale": {

                        "type": "line",

                        "width": 4,

                        "points": [[[0.755,0.422],1],[[0.775,0.422],1],[],[[0.755,0.461],1],[[0.775,0.461],1],[],[[0.755,0.5],1],[[0.775,0.5],1],[],[[0.755,0.695],1],[[0.775,0.695],1],[],[[0.755,0.656],1],[[0.775,0.656],1],[],[[0.755,0.617],1],[[0.775,0.617],1],[],[[0.755,0.578],1],[[0.775,0.578],1],[],[[0.755,0.539],1],[[0.775,0.539],1],[],[[0.755,0.5],1],[[0.755,0.695],1],[],["TerrainBone2",1,"TerrainBone",[0.755,0.695],1],["TerrainBone2",1,"TerrainBone",[0.735,0.695],1],[],["TerrainBone2",1,"TerrainBone",[0.735,0.7106],1],["TerrainBone2",1,"TerrainBone",[0.735,0.6794],1],[]]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText0 [Indent level: 5],

                    "AltText0": {

                        "type": "text",

                        "source": "static",

                        "text": "0",

                        "scale": 1,

                        "sourceScale": 1,

                        "align": "center",

                        "pos": [["0.91-0.12",0.668],1],

                        "right": [[0.84,0.668],1],

                        "down": [["0.91-0.12",0.718],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText1 [Indent level: 5],

                    "AltText1": {

                        "type": "text",

                        "source": "static",

                        "text": "1",

                        "scale": 1,

                        "sourceScale": 1,

                        "align": "center",

                        "pos": [["0.91-0.12",0.629],1],

                        "right": [[0.84,0.629],1],

                        "down": [["0.91-0.12",0.679],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText2 [Indent level: 5],

                    "AltText2": {

                        "type": "text",

                        "source": "static",

                        "text": "2",

                        "scale": 1,

                        "sourceScale": 1,

                        "align": "center",

                        "pos": [["0.91-0.12",0.59],1],

                        "right": [[0.84,0.59],1],

                        "down": [["0.91-0.12",0.64],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText3 [Indent level: 5],

                    "AltText3": {

                        "type": "text",

                        "source": "static",

                        "text": "3",

                        "scale": 1,

                        "sourceScale": 1,

                        "align": "center",

                        "pos": [["0.91-0.12",0.551],1],

                        "right": [[0.84,0.551],1],

                        "down": [["0.91-0.12",0.601],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText4 [Indent level: 5],

                    "AltText4": {

                        "type": "text",

                        "source": "static",

                        "text": "4",

                        "scale": 1,

                        "sourceScale": 1,

                        "align": "center",

                        "pos": [["0.91-0.12",0.512],1],

                        "right": [[0.84,0.512],1],

                        "down": [["0.91-0.12",0.562],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText5 [Indent level: 5],

                    "AltText5": {

                        "type": "text",

                        "source": "static",

                        "text": "5",

                        "scale": 1,

                        "sourceScale": 1,

                        "align": "center",

                        "pos": [["0.91-0.12",0.473],1],

                        "right": [[0.84,0.473],1],

                        "down": [["0.91-0.12",0.523],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText10 [Indent level: 5],

                    "AltText10": {

                        "type": "text",

                        "source": "static",

                        "text": "10",

                        "scale": 1,

                        "sourceScale": 1,

                        "align": "center",

                        "pos": [["0.91-0.12",0.434],1],

                        "right": [[0.84,0.434],1],

                        "down": [["0.91-0.12",0.484],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText15 [Indent level: 5],

                    "AltText15": {

                        "type": "text",

                        "source": "static",

                        "text": "15",

                        "scale": 1,

                        "sourceScale": 1,

                        "align": "center",

                        "pos": [["0.91-0.12",0.395],1],

                        "right": [[0.84,0.395],1],

                        "down": [["0.91-0.12",0.445],1]
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup [Indent level: 4],

                "MachineGunCrosshairGroup": {

                    "type": "group",

                    "condition": "mgun",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|WeaponName [Indent level: 5],

                    "WeaponName": {

                        "type": "text",

                        "source": "weapon",

                        "sourceScale": 1,

                        "align": "right",

                        "scale": 1,

                        "pos": [[0.04,0.76],1],

                        "right": [[0.1,0.76],1],

                        "down": [[0.04,0.82],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|AmmoCount [Indent level: 5],

                    "AmmoCount": {

                        "type": "text",

                        "source": "ammo",

                        "sourceScale": 1,

                        "align": "right",

                        "scale": 1,

                        "pos": [[0.13,0.76],1],

                        "right": [[0.19,0.76],1],

                        "down": [[0.13,0.82],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|AmmoStatic [Indent level: 5],

                    "AmmoStatic": {

                        "type": "text",

                        "source": "static",

                        "text": "/",

                        "scale": 1,

                        "sourceScale": 1,

                        "align": "right",

                        "pos": [[0.1,0.76],1],

                        "right": [[0.16,0.76],1],

                        "down": [[0.1,0.82],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|MachineGunCrosshair [Indent level: 5],

                    "MachineGunCrosshair": {

                        "type": "line",

                        "width": 3,

                        "points": [["ImpactPoint",[0,-0.109829],1],["ImpactPoint",[0,-0.0976253],1],[],["ImpactPoint",[0,0.109829],1],["ImpactPoint",[0,0.0976253],1],[],["ImpactPoint",[-0.09,0],1],["ImpactPoint",[-0.08,0],1],[],["ImpactPoint",[0.09,0],1],["ImpactPoint",[0.08,0],1],[],["ImpactPoint",[0,-0.00244063],1],["ImpactPoint",[0,0.00244063],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[]]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|Circle [Indent level: 5],

                    "Circle": {

                        "type": "line",

                        "width": 9,

                        "points": [["ImpactPoint",[0,-0.0781003],1],["ImpactPoint",[0,-0.0976253],1],["MissileFlightTimeRot1",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot18",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot19",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.064],1,"ImpactPoint",1]]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|Circle_Min_Range [Indent level: 5],

                    "Circle_Min_Range": {

                        "type": "line",

                        "width": 3,

                        "points": [["ImpactPoint",[0,-0.0976253],1],["ImpactPoint",[0.013888,-0.0961414],1],["ImpactPoint",[0.02736,-0.0917385],1],["ImpactPoint",[0.04,-0.0845435],1],["ImpactPoint",[0.051424,-0.074781],1],["ImpactPoint",[0.06128,-0.0627536],1],["ImpactPoint",[0.06928,-0.0488127],1],["ImpactPoint",[0.075176,-0.0333879],1],["ImpactPoint",[0.078784,-0.0169478],1],["ImpactPoint",[0.08,0],1],["ImpactPoint",[0.078784,0.0169478],1],["ImpactPoint",[0.075176,0.0333879],1],["ImpactPoint",[0.06928,0.0488127],1],["ImpactPoint",[0.06128,0.0627536],1],["ImpactPoint",[0.051424,0.074781],1],["ImpactPoint",[0.04,0.0845435],1],["ImpactPoint",[0.02736,0.0917385],1],["ImpactPoint",[0.013888,0.0961414],1],["ImpactPoint",[0,0.0976253],1],["ImpactPoint",[-0.013888,0.0961414],1],["ImpactPoint",[-0.02736,0.0917385],1],["ImpactPoint",[-0.04,0.0845435],1],["ImpactPoint",[-0.051424,0.074781],1],["ImpactPoint",[-0.06128,0.0627536],1],["ImpactPoint",[-0.06928,0.0488127],1],["ImpactPoint",[-0.075176,0.0333879],1],["ImpactPoint",[-0.078784,0.0169478],1],["ImpactPoint",[-0.08,0],1],["ImpactPoint",[-0.078784,-0.0169478],1],["ImpactPoint",[-0.075176,-0.0333879],1],["ImpactPoint",[-0.06928,-0.0488127],1],["ImpactPoint",[-0.06128,-0.0627536],1],["ImpactPoint",[-0.051424,-0.074781],1],["ImpactPoint",[-0.04,-0.0845435],1],["ImpactPoint",[-0.02736,-0.0917385],1],["ImpactPoint",[-0.013888,-0.0961414],1],["ImpactPoint",[0,-0.0976253],1]]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|Distance [Indent level: 5],

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

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup [Indent level: 4],

                "AAMissileCrosshairGroup": {

                    "type": "group",

                    "condition": "AAmissile",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|AAMissileCrosshair [Indent level: 5],

                    "AAMissileCrosshair": {

                        "type": "line",

                        "width": 4,

                        "points": [["WeaponAimAA",[0,-0.0488127],1],["WeaponAimAA",[0.006944,-0.0480707],1],["WeaponAimAA",[0.01368,-0.0458693],1],["WeaponAimAA",[0.02,-0.0422718],1],["WeaponAimAA",[0.025712,-0.0373905],1],["WeaponAimAA",[0.03064,-0.0313768],1],["WeaponAimAA",[0.03464,-0.0244063],1],["WeaponAimAA",[0.037588,-0.0166939],1],["WeaponAimAA",[0.039392,-0.00847388],1],["WeaponAimAA",[0.04,0],1],["WeaponAimAA",[0.039392,0.00847388],1],["WeaponAimAA",[0.037588,0.0166939],1],["WeaponAimAA",[0.03464,0.0244063],1],["WeaponAimAA",[0.03064,0.0313768],1],["WeaponAimAA",[0.025712,0.0373905],1],["WeaponAimAA",[0.02,0.0422718],1],["WeaponAimAA",[0.01368,0.0458693],1],["WeaponAimAA",[0.006944,0.0480707],1],["WeaponAimAA",[0,0.0488127],1],["WeaponAimAA",[-0.006944,0.0480707],1],["WeaponAimAA",[-0.01368,0.0458693],1],["WeaponAimAA",[-0.02,0.0422718],1],["WeaponAimAA",[-0.025712,0.0373905],1],["WeaponAimAA",[-0.03064,0.0313768],1],["WeaponAimAA",[-0.03464,0.0244063],1],["WeaponAimAA",[-0.037588,0.0166939],1],["WeaponAimAA",[-0.039392,0.00847388],1],["WeaponAimAA",[-0.04,0],1],["WeaponAimAA",[-0.039392,-0.00847388],1],["WeaponAimAA",[-0.037588,-0.0166939],1],["WeaponAimAA",[-0.03464,-0.0244063],1],["WeaponAimAA",[-0.03064,-0.0313768],1],["WeaponAimAA",[-0.025712,-0.0373905],1],["WeaponAimAA",[-0.02,-0.0422718],1],["WeaponAimAA",[-0.01368,-0.0458693],1],["WeaponAimAA",[-0.006944,-0.0480707],1],["WeaponAimAA",[0,-0.0488127],1]]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|AmmoCount [Indent level: 5],

                    "AmmoCount": {

                        "type": "text",

                        "source": "ammoFormat",

                        "sourceScale": 1,

                        "align": "right",

                        "scale": 1,

                        "pos": [[0.04,0.76],1],

                        "right": [[0.1,0.76],1],

                        "down": [[0.04,0.82],1]
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup [Indent level: 4],

                "ATMissileCrosshairGroup": {

                    "condition": "ATmissile",

                    "type": "group",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroup [Indent level: 5],

                    "TargetingPodGroup": {

                        "condition": "1-pilotcameralock-missilelocked",

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroup|TargetingPodDir [Indent level: 6],

                        "TargetingPodDir": {

                            "type": "line",

                            "width": 3,

                            "points": [["TargetingPodDir",[0.01197,-0.0401356],1],["TargetingPodDir",[0.0175,-0.0369878],1],["TargetingPodDir",[0.022498,-0.0327167],1],["TargetingPodDir",[0.02681,-0.0274547],1],["TargetingPodDir",[0.03031,-0.0213555],1],["TargetingPodDir",[0.0328895,-0.0146072],1],[],["TargetingPodDir",[0.0328895,0.0146072],1],["TargetingPodDir",[0.03031,0.0213555],1],["TargetingPodDir",[0.02681,0.0274547],1],["TargetingPodDir",[0.022498,0.0327167],1],["TargetingPodDir",[0.0175,0.0369878],1],["TargetingPodDir",[0.01197,0.0401356],1],[],["TargetingPodDir",[-0.01197,0.0401356],1],["TargetingPodDir",[-0.0175,0.0369878],1],["TargetingPodDir",[-0.022498,0.0327167],1],["TargetingPodDir",[-0.02681,0.0274547],1],["TargetingPodDir",[-0.03031,0.0213555],1],["TargetingPodDir",[-0.0328895,0.0146072],1],[],["TargetingPodDir",[-0.0328895,-0.0146072],1],["TargetingPodDir",[-0.03031,-0.0213555],1],["TargetingPodDir",[-0.02681,-0.0274547],1],["TargetingPodDir",[-0.022498,-0.0327167],1],["TargetingPodDir",[-0.0175,-0.0369878],1],["TargetingPodDir",[-0.01197,-0.0401356],1],[],["TargetingPodDir",[0,-0.00244063],1],["TargetingPodDir",[0,0.00244063],1],[],["TargetingPodDir",[-0.002,0],1],["TargetingPodDir",[0.002,0],1],[]]
                        },

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroup|Distance [Indent level: 6],

                        "Distance": {

                            "type": "text",

                            "source": "targetDist",

                            "sourceScale": 0.001,

                            "sourcePrecision": 1,

                            "max": 15,

                            "align": "center",

                            "scale": 1,

                            "pos": ["TargetingPodDir",[-0.002,0.045],1],

                            "right": ["TargetingPodDir",[0.045,0.045],1],

                            "down": ["TargetingPodDir",[-0.002,0.085],1]
                        }
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroupOn [Indent level: 5],

                    "TargetingPodGroupOn": {

                        "condition": "pilotcameralock-missilelocked",

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroupOn|TargetingPodDir [Indent level: 6],

                        "TargetingPodDir": {

                            "type": "line",

                            "width": 3,

                            "points": [["TargetingPodTarget",1,"Limit0109",[0,-0.0427111],1],["TargetingPodTarget",1,"Limit0109",[0.006076,-0.0420619],1],["TargetingPodTarget",1,"Limit0109",[0.01197,-0.0401356],1],["TargetingPodTarget",1,"Limit0109",[0.0175,-0.0369878],1],["TargetingPodTarget",1,"Limit0109",[0.022498,-0.0327167],1],["TargetingPodTarget",1,"Limit0109",[0.02681,-0.0274547],1],["TargetingPodTarget",1,"Limit0109",[0.03031,-0.0213555],1],["TargetingPodTarget",1,"Limit0109",[0.0328895,-0.0146072],1],["TargetingPodTarget",1,"Limit0109",[0.034468,-0.00741464],1],["TargetingPodTarget",1,"Limit0109",[0.035,0],1],["TargetingPodTarget",1,"Limit0109",[0.034468,0.00741464],1],["TargetingPodTarget",1,"Limit0109",[0.0328895,0.0146072],1],["TargetingPodTarget",1,"Limit0109",[0.03031,0.0213555],1],["TargetingPodTarget",1,"Limit0109",[0.02681,0.0274547],1],["TargetingPodTarget",1,"Limit0109",[0.022498,0.0327167],1],["TargetingPodTarget",1,"Limit0109",[0.0175,0.0369878],1],["TargetingPodTarget",1,"Limit0109",[0.01197,0.0401356],1],["TargetingPodTarget",1,"Limit0109",[0.006076,0.0420619],1],["TargetingPodTarget",1,"Limit0109",[0,0.0427111],1],["TargetingPodTarget",1,"Limit0109",[-0.006076,0.0420619],1],["TargetingPodTarget",1,"Limit0109",[-0.01197,0.0401356],1],["TargetingPodTarget",1,"Limit0109",[-0.0175,0.0369878],1],["TargetingPodTarget",1,"Limit0109",[-0.022498,0.0327167],1],["TargetingPodTarget",1,"Limit0109",[-0.02681,0.0274547],1],["TargetingPodTarget",1,"Limit0109",[-0.03031,0.0213555],1],["TargetingPodTarget",1,"Limit0109",[-0.0328895,0.0146072],1],["TargetingPodTarget",1,"Limit0109",[-0.034468,0.00741464],1],["TargetingPodTarget",1,"Limit0109",[-0.035,0],1],["TargetingPodTarget",1,"Limit0109",[-0.034468,-0.00741464],1],["TargetingPodTarget",1,"Limit0109",[-0.0328895,-0.0146072],1],["TargetingPodTarget",1,"Limit0109",[-0.03031,-0.0213555],1],["TargetingPodTarget",1,"Limit0109",[-0.02681,-0.0274547],1],["TargetingPodTarget",1,"Limit0109",[-0.022498,-0.0327167],1],["TargetingPodTarget",1,"Limit0109",[-0.0175,-0.0369878],1],["TargetingPodTarget",1,"Limit0109",[-0.01197,-0.0401356],1],["TargetingPodTarget",1,"Limit0109",[-0.006076,-0.0420619],1],["TargetingPodTarget",1,"Limit0109",[0,-0.0427111],1],[],["TargetingPodTarget",[0,-0.0427111],1],["TargetingPodTarget",[0,-0.0244063],1],[],["TargetingPodTarget",[0,0.0427111],1],["TargetingPodTarget",[0,0.0244063],1],[],["TargetingPodTarget",[-0.035,0],1],["TargetingPodTarget",[-0.02,0],1],[],["TargetingPodTarget",[0.035,0],1],["TargetingPodTarget",[0.02,0],1],[],["TargetingPodTarget",[0,-0.00244063],1],["TargetingPodTarget",[0,0.00244063],1],[],["TargetingPodTarget",[-0.002,0],1],["TargetingPodTarget",[0.002,0],1],[]]
                        },

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroupOn|Distance [Indent level: 6],

                        "Distance": {

                            "type": "text",

                            "source": "targetDist",

                            "sourceScale": 0.001,

                            "sourcePrecision": 1,

                            "max": 15,

                            "align": "center",

                            "scale": 1,

                            "pos": ["TargetingPodTarget",[-0.002,0.045],1],

                            "right": ["TargetingPodTarget",[0.045,0.045],1],

                            "down": ["TargetingPodTarget",[-0.002,0.085],1]
                        }
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetLocked [Indent level: 5],

                    "TargetLocked": {

                        "condition": "missilelocked",

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetLocked|TargetingPodDir [Indent level: 6],

                        "TargetingPodDir": {

                            "type": "line",

                            "width": 3,

                            "points": [["Target",1,"Limit0109",[0,-0.0427111],1],["Target",1,"Limit0109",[0.006076,-0.0420619],1],["Target",1,"Limit0109",[0.01197,-0.0401356],1],["Target",1,"Limit0109",[0.0175,-0.0369878],1],["Target",1,"Limit0109",[0.022498,-0.0327167],1],["Target",1,"Limit0109",[0.02681,-0.0274547],1],["Target",1,"Limit0109",[0.03031,-0.0213555],1],["Target",1,"Limit0109",[0.0328895,-0.0146072],1],["Target",1,"Limit0109",[0.034468,-0.00741464],1],["Target",1,"Limit0109",[0.035,0],1],["Target",1,"Limit0109",[0.034468,0.00741464],1],["Target",1,"Limit0109",[0.0328895,0.0146072],1],["Target",1,"Limit0109",[0.03031,0.0213555],1],["Target",1,"Limit0109",[0.02681,0.0274547],1],["Target",1,"Limit0109",[0.022498,0.0327167],1],["Target",1,"Limit0109",[0.0175,0.0369878],1],["Target",1,"Limit0109",[0.01197,0.0401356],1],["Target",1,"Limit0109",[0.006076,0.0420619],1],["Target",1,"Limit0109",[0,0.0427111],1],["Target",1,"Limit0109",[-0.006076,0.0420619],1],["Target",1,"Limit0109",[-0.01197,0.0401356],1],["Target",1,"Limit0109",[-0.0175,0.0369878],1],["Target",1,"Limit0109",[-0.022498,0.0327167],1],["Target",1,"Limit0109",[-0.02681,0.0274547],1],["Target",1,"Limit0109",[-0.03031,0.0213555],1],["Target",1,"Limit0109",[-0.0328895,0.0146072],1],["Target",1,"Limit0109",[-0.034468,0.00741464],1],["Target",1,"Limit0109",[-0.035,0],1],["Target",1,"Limit0109",[-0.034468,-0.00741464],1],["Target",1,"Limit0109",[-0.0328895,-0.0146072],1],["Target",1,"Limit0109",[-0.03031,-0.0213555],1],["Target",1,"Limit0109",[-0.02681,-0.0274547],1],["Target",1,"Limit0109",[-0.022498,-0.0327167],1],["Target",1,"Limit0109",[-0.0175,-0.0369878],1],["Target",1,"Limit0109",[-0.01197,-0.0401356],1],["Target",1,"Limit0109",[-0.006076,-0.0420619],1],["Target",1,"Limit0109",[0,-0.0427111],1],[],["Target",[0,-0.0427111],1],["Target",[0,-0.0244063],1],[],["Target",[0,0.0427111],1],["Target",[0,0.0244063],1],[],["Target",[-0.035,0],1],["Target",[-0.02,0],1],[],["Target",[0.035,0],1],["Target",[0.02,0],1],[],["Target",[0,-0.00244063],1],["Target",[0,0.00244063],1],[],["Target",[-0.002,0],1],["Target",[0.002,0],1],[]]
                        },

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetLocked|Distance [Indent level: 6],

                        "Distance": {

                            "type": "text",

                            "source": "targetDist",

                            "sourceScale": 0.001,

                            "sourcePrecision": 1,

                            "max": 15,

                            "align": "center",

                            "scale": 1,

                            "pos": ["Target",[-0.002,0.045],1],

                            "right": ["Target",[0.045,0.045],1],

                            "down": ["Target",[-0.002,0.085],1]
                        }
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|AmmoCount [Indent level: 5],

                    "AmmoCount": {

                        "type": "text",

                        "source": "ammoFormat",

                        "sourceScale": 1,

                        "align": "right",

                        "scale": 1,

                        "pos": [[0.04,0.76],1],

                        "right": [[0.1,0.76],1],

                        "down": [[0.04,0.82],1]
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RocketCrosshairGroup [Indent level: 4],

                "RocketCrosshairGroup": {

                    "type": "group",

                    "condition": "Rocket",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RocketCrosshairGroup|MachineGunCrosshair [Indent level: 5],

                    "MachineGunCrosshair": {

                        "type": "line",

                        "width": 3,

                        "points": [["ImpactPoint",[0,-0.0488127],1],["ImpactPoint",[0,-0.0244063],1],[],["ImpactPoint",[0,0.0488127],1],["ImpactPoint",[0,0.0244063],1],[],["ImpactPoint",[-0.04,0],1],["ImpactPoint",[-0.02,0],1],[],["ImpactPoint",[0.04,0],1],["ImpactPoint",[0.02,0],1],[],["ImpactPoint",[0.01,-0.0488127],1],["ImpactPoint",[-0.01,-0.0488127],1],[],["ImpactPoint",[0,-0.00244063],1],["ImpactPoint",[0,0.00244063],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[]]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RocketCrosshairGroup|Distance [Indent level: 5],

                    "Distance": {

                        "type": "text",

                        "source": "ImpactDistance",

                        "sourceScale": 0.001,

                        "sourcePrecision": 1,

                        "max": 15,

                        "align": "center",

                        "scale": 1,

                        "pos": ["ImpactPoint",[-0.002,0.07],1],

                        "right": ["ImpactPoint",[0.045,0.07],1],

                        "down": ["ImpactPoint",[-0.002,0.11],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RocketCrosshairGroup|AmmoCount [Indent level: 5],

                    "AmmoCount": {

                        "type": "text",

                        "source": "ammoFormat",

                        "sourceScale": 1,

                        "align": "right",

                        "scale": 1,

                        "pos": [[0.04,0.76],1],

                        "right": [[0.1,0.76],1],

                        "down": [[0.04,0.82],1]
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BombCrosshairGroup [Indent level: 4],

                "BombCrosshairGroup": {

                    "type": "group",

                    "condition": "bomb",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BombCrosshairGroup|BombCrosshair [Indent level: 5],

                    "BombCrosshair": {

                        "width": 4,

                        "type": "line",

                        "points": [["ImpactPoint",[0,0.109829],1],["ImpactPoint",[0,0.0976253],1],[],["ImpactPoint",[-0.09,0],1],["ImpactPoint",[-0.08,0],1],[],["ImpactPoint",[0.09,0],1],["ImpactPoint",[0.08,0],1],[],["ImpactPoint",[0,-0.00244063],1],["ImpactPoint",[0,0.00244063],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[],["ImpactPoint",[0,-0.0976253],1],["ImpactPoint",[0.013888,-0.0961414],1],["ImpactPoint",[0.02736,-0.0917385],1],["ImpactPoint",[0.04,-0.0845435],1],["ImpactPoint",[0.051424,-0.074781],1],["ImpactPoint",[0.06128,-0.0627536],1],["ImpactPoint",[0.06928,-0.0488127],1],["ImpactPoint",[0.075176,-0.0333879],1],["ImpactPoint",[0.078784,-0.0169478],1],["ImpactPoint",[0.08,0],1],["ImpactPoint",[0.078784,0.0169478],1],["ImpactPoint",[0.075176,0.0333879],1],["ImpactPoint",[0.06928,0.0488127],1],["ImpactPoint",[0.06128,0.0627536],1],["ImpactPoint",[0.051424,0.074781],1],["ImpactPoint",[0.04,0.0845435],1],["ImpactPoint",[0.02736,0.0917385],1],["ImpactPoint",[0.013888,0.0961414],1],["ImpactPoint",[0,0.0976253],1],["ImpactPoint",[-0.013888,0.0961414],1],["ImpactPoint",[-0.02736,0.0917385],1],["ImpactPoint",[-0.04,0.0845435],1],["ImpactPoint",[-0.051424,0.074781],1],["ImpactPoint",[-0.06128,0.0627536],1],["ImpactPoint",[-0.06928,0.0488127],1],["ImpactPoint",[-0.075176,0.0333879],1],["ImpactPoint",[-0.078784,0.0169478],1],["ImpactPoint",[-0.08,0],1],["ImpactPoint",[-0.078784,-0.0169478],1],["ImpactPoint",[-0.075176,-0.0333879],1],["ImpactPoint",[-0.06928,-0.0488127],1],["ImpactPoint",[-0.06128,-0.0627536],1],["ImpactPoint",[-0.051424,-0.074781],1],["ImpactPoint",[-0.04,-0.0845435],1],["ImpactPoint",[-0.02736,-0.0917385],1],["ImpactPoint",[-0.013888,-0.0961414],1],["ImpactPoint",[0,-0.0976253],1],[],[],["ImpactPoint",-1,"Velocity",1,"NormalizeBombCircle",1,"ImpactPoint",1,[0,0],1],["Velocity",1,"Limit0109",1,[0,0],1]]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BombCrosshairGroup|Circle [Indent level: 5],

                    "Circle": {

                        "type": "line",

                        "width": 6,

                        "points": [["ImpactPoint",[0,-0.0781003],1],["ImpactPoint",[0,-0.0976253],1],["MissileFlightTimeRot1",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot18",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot19",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.064],1,"ImpactPoint",1]]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BombCrosshairGroup|Distance [Indent level: 5],

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
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BombCrosshairGroup|AmmoCount [Indent level: 5],

                    "AmmoCount": {

                        "type": "text",

                        "source": "ammoFormat",

                        "sourceScale": 1,

                        "align": "right",

                        "scale": 1,

                        "pos": [[0.04,0.76],1],

                        "right": [[0.1,0.76],1],

                        "down": [[0.04,0.82],1]
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|PitchNumber [Indent level: 4],

                "PitchNumber": {

                    "type": "text",

                    "source": "horizonDive",

                    "sourceScale": 57.2958,

                    "align": "right",

                    "scale": 1,

                    "pos": [[0.84,0.56],1],

                    "right": [[0.91,0.56],1],

                    "down": [[0.84,0.63],1]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BaroNumber [Indent level: 4],

                "BaroNumber": {

                    "type": "text",

                    "source": "altitudeASL",

                    "sourceScale": 1,

                    "sourceLength": 1,

                    "align": "right",

                    "scale": 1,

                    "pos": [[0.84,0.5],1],

                    "right": [[0.91,0.5],1],

                    "down": [[0.84,0.57],1]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|SpeedNumber [Indent level: 4],

                "SpeedNumber": {

                    "type": "text",

                    "source": "speed",

                    "sourceScale": 3.6,

                    "align": "right",

                    "scale": 1,

                    "pos": [[0.1,0.5],1],

                    "right": [[0.17,0.5],1],

                    "down": [[0.1,0.57],1]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LandingMode [Indent level: 4],

                "LandingMode": {

                    "condition": "user4 - (mgun + AAmissile + ATmissile + bomb + rocket)",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LandingMode|VerticalSpeedScale [Indent level: 5],

                    "VerticalSpeedScale": {

                        "type": "line",

                        "width": 4,

                        "points": [[[0.73,0.305],1],[[0.76,0.305],1],[],[[0.735,0.344],1],[[0.745,0.344],1],[],[[0.735,0.383],1],[[0.745,0.383],1],[],[[0.735,0.422],1],[[0.745,0.422],1],[],[[0.735,0.461],1],[[0.745,0.461],1],[],[[0.73,0.5],1],[[0.79,0.5],1],[],[[0.73,0.695],1],[[0.76,0.695],1],[],[[0.735,0.656],1],[[0.745,0.656],1],[],[[0.735,0.617],1],[[0.745,0.617],1],[],[[0.735,0.578],1],[[0.745,0.578],1],[],[[0.735,0.539],1],[[0.745,0.539],1],[],[[0.73,0.5],1],[[0.79,0.5],1],["VerticalSpeedBone",[0.79,0.5],1],["VerticalSpeedBone",[0.76,0.5],1],[]]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LandingMode|VerticalSpeedArrow [Indent level: 5],

                    "VerticalSpeedArrow": {

                        "type": "polygon",

                        "points": [[["VerticalSpeedBone",[0.77,0.492],1],["VerticalSpeedBone",[0.76,0.5],1],["VerticalSpeedBone",[0.77,0.508],1]]]
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ILS [Indent level: 4],

                "ILS": {

                    "condition": "ils",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ILS|Glideslope [Indent level: 5],

                    "Glideslope": {

                        "clipTL": [0,0],

                        "clipBR": [1,1],

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 6],

                        "ILS": {

                            "type": "line",

                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[-0.24,-0.0292876],1],["ILS_W",[-0.24,0.0292876],1],[],["ILS_W",[-0.12,-0.0219657],1],["ILS_W",[-0.12,0.0219657],1],[],["ILS_W",[0,-0.0292876],1],["ILS_W",[0,0.0292876],1],[],["ILS_W",[0.12,-0.0219657],1],["ILS_W",[0.12,0.0219657],1],[],["ILS_W",[0.24,-0.0292876],1],["ILS_W",[0.24,0.0292876],1],[],["ILS_H",[0,-0.292876],1],["ILS_H",[0,0.292876],1],[],["ILS_H",[-0.024,-0.292876],1],["ILS_H",[0.024,-0.292876],1],[],["ILS_H",[-0.018,-0.146438],1],["ILS_H",[0.018,-0.146438],1],[],["ILS_H",[-0.024,0],1],["ILS_H",[0.024,0],1],[],["ILS_H",[-0.018,0.146438],1],["ILS_H",[0.018,0.146438],1],[],["ILS_H",[-0.024,0.292876],1],["ILS_H",[0.024,0.292876],1]]
                        }
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HeadingArrows [Indent level: 4],

                "HeadingArrows": {

                    "type": "line",

                    "width": 3,

                    "points": [[[0.486,0.957],1],[[0.5,0.935],1],[[0.514,0.957],1],[[0.486,0.957],1],[],["WPPoint",1,"LimitWaypoint",1,[-0.011,0],1],["WPPoint",1,"LimitWaypoint",1,[-0.011,0.022],1],[],["WPPoint",1,"LimitWaypoint",1,[0.011,0],1],["WPPoint",1,"LimitWaypoint",1,[0.011,0.022],1]]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],

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

                    "lineXleft": 0.92,

                    "lineYright": 0.9,

                    "lineXleftMajor": 0.93,

                    "lineYrightMajor": 0.9,

                    "majorLineEach": 2,

                    "numberEach": 2,

                    "step": 0.5,

                    "stepSize": 0.0555556,

                    "align": "center",

                    "scale": 1,

                    "pos": [0.295,0.865],

                    "right": [0.335,0.865],

                    "down": [0.295,0.905]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarNumber [Indent level: 4],

                "RadarNumber": {

                    "type": "text",

                    "source": "altitudeAGL",

                    "sourceScale": 1,

                    "sourceLength": 4,

                    "sourceOffset": -0.5,

                    "align": "right",

                    "scale": 1,

                    "pos": [[0.725,0.775],1],

                    "right": [[0.785,0.775],1],

                    "down": [[0.725,0.835],1]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarText [Indent level: 4],

                "RadarText": {

                    "type": "text",

                    "source": "static",

                    "text": "R",

                    "scale": 1,

                    "sourceScale": 1,

                    "align": "right",

                    "pos": [[0.825,0.775],1],

                    "right": [[0.885,0.775],1],

                    "down": [[0.825,0.835],1]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WPdist [Indent level: 4],

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

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WPIndex [Indent level: 4],

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

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WPstatic [Indent level: 4],

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

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WPTime [Indent level: 4],

                "WPTime": {

                    "type": "text",

                    "source": "static",

                    "text": ":11:34/-00:0",

                    "scale": 1,

                    "sourceScale": 1,

                    "align": "right",

                    "pos": [[0.725,0.865],1],

                    "right": [[0.785,0.865],1],

                    "down": [[0.725,0.925],1]
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WPCurrentTime [Indent level: 4],

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

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WaypointGroup [Indent level: 4],

                "WaypointGroup": {

                    "condition": "wpvalid",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WaypointGroup|Tadpol [Indent level: 5],

                    "Tadpol": {

                        "type": "line",

                        "width": 3,

                        "points": []
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine [Indent level: 4],

                "HorizontalLine": {

                    "clipTL": [0.2,0],

                    "clipBR": [0.8,0.96],

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|Level0 [Indent level: 5],

                    "Level0": {

                        "type": "line",

                        "source": "Level0",

                        "width": 3,

                        "points": [["Level0",[-0.27,0],1],["Level0",[-0.0675,0],1],[],["Level0",[0.0675,0],1],["Level0",[0.27,0],1]]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM05 [Indent level: 5],

                    "LevelM05": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM05",[-0.166,-0.04],1],["LevelM05",[-0.166,0],1],["LevelM05",[-0.138,0],1],[],["LevelM05",[-0.124,0],1],["LevelM05",[-0.096,0],1],[],["LevelM05",[-0.082,0],1],["LevelM05",[-0.054,0],1],[],[],["LevelM05",[0.166,-0.04],1],["LevelM05",[0.166,0],1],["LevelM05",[0.138,0],1],[],["LevelM05",[0.124,0],1],["LevelM05",[0.096,0],1],[],["LevelM05",[0.082,0],1],["LevelM05",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_05 [Indent level: 5],

                    "VALM_1_05": {

                        "type": "text",

                        "source": "static",

                        "text": 5,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM05",[-0.18,-0.052],1],

                        "right": ["LevelM05",[-0.1,-0.052],1],

                        "down": ["LevelM05",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_05_R [Indent level: 5],

                    "VALM_1_05_R": {

                        "type": "text",

                        "source": "static",

                        "text": 5,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM05",[0.18,-0.052],1],

                        "right": ["LevelM05",[0.26,-0.052],1],

                        "down": ["LevelM05",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP05 [Indent level: 5],

                    "LevelP05": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP05",[-0.166,0.04],1],["LevelP05",[-0.166,0],1],["LevelP05",[-0.04,0],1],[],["LevelP05",[0.054,0],1],["LevelP05",[0.194,0],1],["LevelP05",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_05 [Indent level: 5],

                    "VALP_1_05": {

                        "type": "text",

                        "source": "static",

                        "text": "05",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP05",[-0.19,-0.017],1],

                        "right": ["LevelP05",[-0.11,-0.017],1],

                        "down": ["LevelP05",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_05_R [Indent level: 5],

                    "VALP_1_05_R": {

                        "type": "text",

                        "source": "static",

                        "text": "05",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP05",[0.21,-0.017],1],

                        "right": ["LevelP05",[0.29,-0.017],1],

                        "down": ["LevelP05",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM10 [Indent level: 5],

                    "LevelM10": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM10",[-0.166,-0.04],1],["LevelM10",[-0.166,0],1],["LevelM10",[-0.138,0],1],[],["LevelM10",[-0.124,0],1],["LevelM10",[-0.096,0],1],[],["LevelM10",[-0.082,0],1],["LevelM10",[-0.054,0],1],[],[],["LevelM10",[0.166,-0.04],1],["LevelM10",[0.166,0],1],["LevelM10",[0.138,0],1],[],["LevelM10",[0.124,0],1],["LevelM10",[0.096,0],1],[],["LevelM10",[0.082,0],1],["LevelM10",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_10 [Indent level: 5],

                    "VALM_1_10": {

                        "type": "text",

                        "source": "static",

                        "text": 10,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM10",[-0.18,-0.052],1],

                        "right": ["LevelM10",[-0.1,-0.052],1],

                        "down": ["LevelM10",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_10_R [Indent level: 5],

                    "VALM_1_10_R": {

                        "type": "text",

                        "source": "static",

                        "text": 10,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM10",[0.18,-0.052],1],

                        "right": ["LevelM10",[0.26,-0.052],1],

                        "down": ["LevelM10",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP10 [Indent level: 5],

                    "LevelP10": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP10",[-0.166,0.04],1],["LevelP10",[-0.166,0],1],["LevelP10",[-0.04,0],1],[],["LevelP10",[0.054,0],1],["LevelP10",[0.194,0],1],["LevelP10",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_10 [Indent level: 5],

                    "VALP_1_10": {

                        "type": "text",

                        "source": "static",

                        "text": "10",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP10",[-0.19,-0.017],1],

                        "right": ["LevelP10",[-0.11,-0.017],1],

                        "down": ["LevelP10",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_10_R [Indent level: 5],

                    "VALP_1_10_R": {

                        "type": "text",

                        "source": "static",

                        "text": "10",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP10",[0.21,-0.017],1],

                        "right": ["LevelP10",[0.29,-0.017],1],

                        "down": ["LevelP10",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM15 [Indent level: 5],

                    "LevelM15": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM15",[-0.166,-0.04],1],["LevelM15",[-0.166,0],1],["LevelM15",[-0.138,0],1],[],["LevelM15",[-0.124,0],1],["LevelM15",[-0.096,0],1],[],["LevelM15",[-0.082,0],1],["LevelM15",[-0.054,0],1],[],[],["LevelM15",[0.166,-0.04],1],["LevelM15",[0.166,0],1],["LevelM15",[0.138,0],1],[],["LevelM15",[0.124,0],1],["LevelM15",[0.096,0],1],[],["LevelM15",[0.082,0],1],["LevelM15",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_15 [Indent level: 5],

                    "VALM_1_15": {

                        "type": "text",

                        "source": "static",

                        "text": 15,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM15",[-0.18,-0.052],1],

                        "right": ["LevelM15",[-0.1,-0.052],1],

                        "down": ["LevelM15",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_15_R [Indent level: 5],

                    "VALM_1_15_R": {

                        "type": "text",

                        "source": "static",

                        "text": 15,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM15",[0.18,-0.052],1],

                        "right": ["LevelM15",[0.26,-0.052],1],

                        "down": ["LevelM15",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP15 [Indent level: 5],

                    "LevelP15": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP15",[-0.166,0.04],1],["LevelP15",[-0.166,0],1],["LevelP15",[-0.04,0],1],[],["LevelP15",[0.054,0],1],["LevelP15",[0.194,0],1],["LevelP15",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_15 [Indent level: 5],

                    "VALP_1_15": {

                        "type": "text",

                        "source": "static",

                        "text": "15",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP15",[-0.19,-0.017],1],

                        "right": ["LevelP15",[-0.11,-0.017],1],

                        "down": ["LevelP15",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_15_R [Indent level: 5],

                    "VALP_1_15_R": {

                        "type": "text",

                        "source": "static",

                        "text": "15",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP15",[0.21,-0.017],1],

                        "right": ["LevelP15",[0.29,-0.017],1],

                        "down": ["LevelP15",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM20 [Indent level: 5],

                    "LevelM20": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM20",[-0.166,-0.04],1],["LevelM20",[-0.166,0],1],["LevelM20",[-0.138,0],1],[],["LevelM20",[-0.124,0],1],["LevelM20",[-0.096,0],1],[],["LevelM20",[-0.082,0],1],["LevelM20",[-0.054,0],1],[],[],["LevelM20",[0.166,-0.04],1],["LevelM20",[0.166,0],1],["LevelM20",[0.138,0],1],[],["LevelM20",[0.124,0],1],["LevelM20",[0.096,0],1],[],["LevelM20",[0.082,0],1],["LevelM20",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_20 [Indent level: 5],

                    "VALM_1_20": {

                        "type": "text",

                        "source": "static",

                        "text": 20,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM20",[-0.18,-0.052],1],

                        "right": ["LevelM20",[-0.1,-0.052],1],

                        "down": ["LevelM20",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_20_R [Indent level: 5],

                    "VALM_1_20_R": {

                        "type": "text",

                        "source": "static",

                        "text": 20,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM20",[0.18,-0.052],1],

                        "right": ["LevelM20",[0.26,-0.052],1],

                        "down": ["LevelM20",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP20 [Indent level: 5],

                    "LevelP20": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP20",[-0.166,0.04],1],["LevelP20",[-0.166,0],1],["LevelP20",[-0.04,0],1],[],["LevelP20",[0.054,0],1],["LevelP20",[0.194,0],1],["LevelP20",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_20 [Indent level: 5],

                    "VALP_1_20": {

                        "type": "text",

                        "source": "static",

                        "text": "20",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP20",[-0.19,-0.017],1],

                        "right": ["LevelP20",[-0.11,-0.017],1],

                        "down": ["LevelP20",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_20_R [Indent level: 5],

                    "VALP_1_20_R": {

                        "type": "text",

                        "source": "static",

                        "text": "20",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP20",[0.21,-0.017],1],

                        "right": ["LevelP20",[0.29,-0.017],1],

                        "down": ["LevelP20",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM25 [Indent level: 5],

                    "LevelM25": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM25",[-0.166,-0.04],1],["LevelM25",[-0.166,0],1],["LevelM25",[-0.138,0],1],[],["LevelM25",[-0.124,0],1],["LevelM25",[-0.096,0],1],[],["LevelM25",[-0.082,0],1],["LevelM25",[-0.054,0],1],[],[],["LevelM25",[0.166,-0.04],1],["LevelM25",[0.166,0],1],["LevelM25",[0.138,0],1],[],["LevelM25",[0.124,0],1],["LevelM25",[0.096,0],1],[],["LevelM25",[0.082,0],1],["LevelM25",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_25 [Indent level: 5],

                    "VALM_1_25": {

                        "type": "text",

                        "source": "static",

                        "text": 25,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM25",[-0.18,-0.052],1],

                        "right": ["LevelM25",[-0.1,-0.052],1],

                        "down": ["LevelM25",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_25_R [Indent level: 5],

                    "VALM_1_25_R": {

                        "type": "text",

                        "source": "static",

                        "text": 25,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM25",[0.18,-0.052],1],

                        "right": ["LevelM25",[0.26,-0.052],1],

                        "down": ["LevelM25",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP25 [Indent level: 5],

                    "LevelP25": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP25",[-0.166,0.04],1],["LevelP25",[-0.166,0],1],["LevelP25",[-0.04,0],1],[],["LevelP25",[0.054,0],1],["LevelP25",[0.194,0],1],["LevelP25",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_25 [Indent level: 5],

                    "VALP_1_25": {

                        "type": "text",

                        "source": "static",

                        "text": "25",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP25",[-0.19,-0.017],1],

                        "right": ["LevelP25",[-0.11,-0.017],1],

                        "down": ["LevelP25",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_25_R [Indent level: 5],

                    "VALP_1_25_R": {

                        "type": "text",

                        "source": "static",

                        "text": "25",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP25",[0.21,-0.017],1],

                        "right": ["LevelP25",[0.29,-0.017],1],

                        "down": ["LevelP25",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM30 [Indent level: 5],

                    "LevelM30": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM30",[-0.166,-0.04],1],["LevelM30",[-0.166,0],1],["LevelM30",[-0.138,0],1],[],["LevelM30",[-0.124,0],1],["LevelM30",[-0.096,0],1],[],["LevelM30",[-0.082,0],1],["LevelM30",[-0.054,0],1],[],[],["LevelM30",[0.166,-0.04],1],["LevelM30",[0.166,0],1],["LevelM30",[0.138,0],1],[],["LevelM30",[0.124,0],1],["LevelM30",[0.096,0],1],[],["LevelM30",[0.082,0],1],["LevelM30",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_30 [Indent level: 5],

                    "VALM_1_30": {

                        "type": "text",

                        "source": "static",

                        "text": 30,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM30",[-0.18,-0.052],1],

                        "right": ["LevelM30",[-0.1,-0.052],1],

                        "down": ["LevelM30",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_30_R [Indent level: 5],

                    "VALM_1_30_R": {

                        "type": "text",

                        "source": "static",

                        "text": 30,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM30",[0.18,-0.052],1],

                        "right": ["LevelM30",[0.26,-0.052],1],

                        "down": ["LevelM30",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP30 [Indent level: 5],

                    "LevelP30": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP30",[-0.166,0.04],1],["LevelP30",[-0.166,0],1],["LevelP30",[-0.04,0],1],[],["LevelP30",[0.054,0],1],["LevelP30",[0.194,0],1],["LevelP30",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_30 [Indent level: 5],

                    "VALP_1_30": {

                        "type": "text",

                        "source": "static",

                        "text": "30",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP30",[-0.19,-0.017],1],

                        "right": ["LevelP30",[-0.11,-0.017],1],

                        "down": ["LevelP30",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_30_R [Indent level: 5],

                    "VALP_1_30_R": {

                        "type": "text",

                        "source": "static",

                        "text": "30",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP30",[0.21,-0.017],1],

                        "right": ["LevelP30",[0.29,-0.017],1],

                        "down": ["LevelP30",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM35 [Indent level: 5],

                    "LevelM35": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM35",[-0.166,-0.04],1],["LevelM35",[-0.166,0],1],["LevelM35",[-0.138,0],1],[],["LevelM35",[-0.124,0],1],["LevelM35",[-0.096,0],1],[],["LevelM35",[-0.082,0],1],["LevelM35",[-0.054,0],1],[],[],["LevelM35",[0.166,-0.04],1],["LevelM35",[0.166,0],1],["LevelM35",[0.138,0],1],[],["LevelM35",[0.124,0],1],["LevelM35",[0.096,0],1],[],["LevelM35",[0.082,0],1],["LevelM35",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_35 [Indent level: 5],

                    "VALM_1_35": {

                        "type": "text",

                        "source": "static",

                        "text": 35,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM35",[-0.18,-0.052],1],

                        "right": ["LevelM35",[-0.1,-0.052],1],

                        "down": ["LevelM35",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_35_R [Indent level: 5],

                    "VALM_1_35_R": {

                        "type": "text",

                        "source": "static",

                        "text": 35,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM35",[0.18,-0.052],1],

                        "right": ["LevelM35",[0.26,-0.052],1],

                        "down": ["LevelM35",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP35 [Indent level: 5],

                    "LevelP35": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP35",[-0.166,0.04],1],["LevelP35",[-0.166,0],1],["LevelP35",[-0.04,0],1],[],["LevelP35",[0.054,0],1],["LevelP35",[0.194,0],1],["LevelP35",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_35 [Indent level: 5],

                    "VALP_1_35": {

                        "type": "text",

                        "source": "static",

                        "text": "35",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP35",[-0.19,-0.017],1],

                        "right": ["LevelP35",[-0.11,-0.017],1],

                        "down": ["LevelP35",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_35_R [Indent level: 5],

                    "VALP_1_35_R": {

                        "type": "text",

                        "source": "static",

                        "text": "35",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP35",[0.21,-0.017],1],

                        "right": ["LevelP35",[0.29,-0.017],1],

                        "down": ["LevelP35",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM40 [Indent level: 5],

                    "LevelM40": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM40",[-0.166,-0.04],1],["LevelM40",[-0.166,0],1],["LevelM40",[-0.138,0],1],[],["LevelM40",[-0.124,0],1],["LevelM40",[-0.096,0],1],[],["LevelM40",[-0.082,0],1],["LevelM40",[-0.054,0],1],[],[],["LevelM40",[0.166,-0.04],1],["LevelM40",[0.166,0],1],["LevelM40",[0.138,0],1],[],["LevelM40",[0.124,0],1],["LevelM40",[0.096,0],1],[],["LevelM40",[0.082,0],1],["LevelM40",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_40 [Indent level: 5],

                    "VALM_1_40": {

                        "type": "text",

                        "source": "static",

                        "text": 40,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM40",[-0.18,-0.052],1],

                        "right": ["LevelM40",[-0.1,-0.052],1],

                        "down": ["LevelM40",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_40_R [Indent level: 5],

                    "VALM_1_40_R": {

                        "type": "text",

                        "source": "static",

                        "text": 40,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM40",[0.18,-0.052],1],

                        "right": ["LevelM40",[0.26,-0.052],1],

                        "down": ["LevelM40",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP40 [Indent level: 5],

                    "LevelP40": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP40",[-0.166,0.04],1],["LevelP40",[-0.166,0],1],["LevelP40",[-0.04,0],1],[],["LevelP40",[0.054,0],1],["LevelP40",[0.194,0],1],["LevelP40",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_40 [Indent level: 5],

                    "VALP_1_40": {

                        "type": "text",

                        "source": "static",

                        "text": "40",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP40",[-0.19,-0.017],1],

                        "right": ["LevelP40",[-0.11,-0.017],1],

                        "down": ["LevelP40",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_40_R [Indent level: 5],

                    "VALP_1_40_R": {

                        "type": "text",

                        "source": "static",

                        "text": "40",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP40",[0.21,-0.017],1],

                        "right": ["LevelP40",[0.29,-0.017],1],

                        "down": ["LevelP40",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM45 [Indent level: 5],

                    "LevelM45": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM45",[-0.166,-0.04],1],["LevelM45",[-0.166,0],1],["LevelM45",[-0.138,0],1],[],["LevelM45",[-0.124,0],1],["LevelM45",[-0.096,0],1],[],["LevelM45",[-0.082,0],1],["LevelM45",[-0.054,0],1],[],[],["LevelM45",[0.166,-0.04],1],["LevelM45",[0.166,0],1],["LevelM45",[0.138,0],1],[],["LevelM45",[0.124,0],1],["LevelM45",[0.096,0],1],[],["LevelM45",[0.082,0],1],["LevelM45",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_45 [Indent level: 5],

                    "VALM_1_45": {

                        "type": "text",

                        "source": "static",

                        "text": 45,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM45",[-0.18,-0.052],1],

                        "right": ["LevelM45",[-0.1,-0.052],1],

                        "down": ["LevelM45",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_45_R [Indent level: 5],

                    "VALM_1_45_R": {

                        "type": "text",

                        "source": "static",

                        "text": 45,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM45",[0.18,-0.052],1],

                        "right": ["LevelM45",[0.26,-0.052],1],

                        "down": ["LevelM45",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP45 [Indent level: 5],

                    "LevelP45": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP45",[-0.166,0.04],1],["LevelP45",[-0.166,0],1],["LevelP45",[-0.04,0],1],[],["LevelP45",[0.054,0],1],["LevelP45",[0.194,0],1],["LevelP45",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_45 [Indent level: 5],

                    "VALP_1_45": {

                        "type": "text",

                        "source": "static",

                        "text": "45",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP45",[-0.19,-0.017],1],

                        "right": ["LevelP45",[-0.11,-0.017],1],

                        "down": ["LevelP45",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_45_R [Indent level: 5],

                    "VALP_1_45_R": {

                        "type": "text",

                        "source": "static",

                        "text": "45",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP45",[0.21,-0.017],1],

                        "right": ["LevelP45",[0.29,-0.017],1],

                        "down": ["LevelP45",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM50 [Indent level: 5],

                    "LevelM50": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM50",[-0.166,-0.04],1],["LevelM50",[-0.166,0],1],["LevelM50",[-0.138,0],1],[],["LevelM50",[-0.124,0],1],["LevelM50",[-0.096,0],1],[],["LevelM50",[-0.082,0],1],["LevelM50",[-0.054,0],1],[],[],["LevelM50",[0.166,-0.04],1],["LevelM50",[0.166,0],1],["LevelM50",[0.138,0],1],[],["LevelM50",[0.124,0],1],["LevelM50",[0.096,0],1],[],["LevelM50",[0.082,0],1],["LevelM50",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_50 [Indent level: 5],

                    "VALM_1_50": {

                        "type": "text",

                        "source": "static",

                        "text": 50,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM50",[-0.18,-0.052],1],

                        "right": ["LevelM50",[-0.1,-0.052],1],

                        "down": ["LevelM50",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_50_R [Indent level: 5],

                    "VALM_1_50_R": {

                        "type": "text",

                        "source": "static",

                        "text": 50,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM50",[0.18,-0.052],1],

                        "right": ["LevelM50",[0.26,-0.052],1],

                        "down": ["LevelM50",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP50 [Indent level: 5],

                    "LevelP50": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP50",[-0.166,0.04],1],["LevelP50",[-0.166,0],1],["LevelP50",[-0.04,0],1],[],["LevelP50",[0.054,0],1],["LevelP50",[0.194,0],1],["LevelP50",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_50 [Indent level: 5],

                    "VALP_1_50": {

                        "type": "text",

                        "source": "static",

                        "text": "50",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP50",[-0.19,-0.017],1],

                        "right": ["LevelP50",[-0.11,-0.017],1],

                        "down": ["LevelP50",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_50_R [Indent level: 5],

                    "VALP_1_50_R": {

                        "type": "text",

                        "source": "static",

                        "text": "50",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP50",[0.21,-0.017],1],

                        "right": ["LevelP50",[0.29,-0.017],1],

                        "down": ["LevelP50",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM60 [Indent level: 5],

                    "LevelM60": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM60",[-0.166,-0.04],1],["LevelM60",[-0.166,0],1],["LevelM60",[-0.138,0],1],[],["LevelM60",[-0.124,0],1],["LevelM60",[-0.096,0],1],[],["LevelM60",[-0.082,0],1],["LevelM60",[-0.054,0],1],[],[],["LevelM60",[0.166,-0.04],1],["LevelM60",[0.166,0],1],["LevelM60",[0.138,0],1],[],["LevelM60",[0.124,0],1],["LevelM60",[0.096,0],1],[],["LevelM60",[0.082,0],1],["LevelM60",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_60 [Indent level: 5],

                    "VALM_1_60": {

                        "type": "text",

                        "source": "static",

                        "text": 60,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM60",[-0.18,-0.052],1],

                        "right": ["LevelM60",[-0.1,-0.052],1],

                        "down": ["LevelM60",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_60_R [Indent level: 5],

                    "VALM_1_60_R": {

                        "type": "text",

                        "source": "static",

                        "text": 60,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM60",[0.18,-0.052],1],

                        "right": ["LevelM60",[0.26,-0.052],1],

                        "down": ["LevelM60",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP60 [Indent level: 5],

                    "LevelP60": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP60",[-0.166,0.04],1],["LevelP60",[-0.166,0],1],["LevelP60",[-0.04,0],1],[],["LevelP60",[0.054,0],1],["LevelP60",[0.194,0],1],["LevelP60",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_60 [Indent level: 5],

                    "VALP_1_60": {

                        "type": "text",

                        "source": "static",

                        "text": "60",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP60",[-0.19,-0.017],1],

                        "right": ["LevelP60",[-0.11,-0.017],1],

                        "down": ["LevelP60",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_60_R [Indent level: 5],

                    "VALP_1_60_R": {

                        "type": "text",

                        "source": "static",

                        "text": "60",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP60",[0.21,-0.017],1],

                        "right": ["LevelP60",[0.29,-0.017],1],

                        "down": ["LevelP60",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM70 [Indent level: 5],

                    "LevelM70": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM70",[-0.166,-0.04],1],["LevelM70",[-0.166,0],1],["LevelM70",[-0.138,0],1],[],["LevelM70",[-0.124,0],1],["LevelM70",[-0.096,0],1],[],["LevelM70",[-0.082,0],1],["LevelM70",[-0.054,0],1],[],[],["LevelM70",[0.166,-0.04],1],["LevelM70",[0.166,0],1],["LevelM70",[0.138,0],1],[],["LevelM70",[0.124,0],1],["LevelM70",[0.096,0],1],[],["LevelM70",[0.082,0],1],["LevelM70",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_70 [Indent level: 5],

                    "VALM_1_70": {

                        "type": "text",

                        "source": "static",

                        "text": 70,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM70",[-0.18,-0.052],1],

                        "right": ["LevelM70",[-0.1,-0.052],1],

                        "down": ["LevelM70",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_70_R [Indent level: 5],

                    "VALM_1_70_R": {

                        "type": "text",

                        "source": "static",

                        "text": 70,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM70",[0.18,-0.052],1],

                        "right": ["LevelM70",[0.26,-0.052],1],

                        "down": ["LevelM70",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP70 [Indent level: 5],

                    "LevelP70": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP70",[-0.166,0.04],1],["LevelP70",[-0.166,0],1],["LevelP70",[-0.04,0],1],[],["LevelP70",[0.054,0],1],["LevelP70",[0.194,0],1],["LevelP70",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_70 [Indent level: 5],

                    "VALP_1_70": {

                        "type": "text",

                        "source": "static",

                        "text": "70",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP70",[-0.19,-0.017],1],

                        "right": ["LevelP70",[-0.11,-0.017],1],

                        "down": ["LevelP70",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_70_R [Indent level: 5],

                    "VALP_1_70_R": {

                        "type": "text",

                        "source": "static",

                        "text": "70",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP70",[0.21,-0.017],1],

                        "right": ["LevelP70",[0.29,-0.017],1],

                        "down": ["LevelP70",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM80 [Indent level: 5],

                    "LevelM80": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM80",[-0.166,-0.04],1],["LevelM80",[-0.166,0],1],["LevelM80",[-0.138,0],1],[],["LevelM80",[-0.124,0],1],["LevelM80",[-0.096,0],1],[],["LevelM80",[-0.082,0],1],["LevelM80",[-0.054,0],1],[],[],["LevelM80",[0.166,-0.04],1],["LevelM80",[0.166,0],1],["LevelM80",[0.138,0],1],[],["LevelM80",[0.124,0],1],["LevelM80",[0.096,0],1],[],["LevelM80",[0.082,0],1],["LevelM80",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_80 [Indent level: 5],

                    "VALM_1_80": {

                        "type": "text",

                        "source": "static",

                        "text": 80,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM80",[-0.18,-0.052],1],

                        "right": ["LevelM80",[-0.1,-0.052],1],

                        "down": ["LevelM80",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_80_R [Indent level: 5],

                    "VALM_1_80_R": {

                        "type": "text",

                        "source": "static",

                        "text": 80,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM80",[0.18,-0.052],1],

                        "right": ["LevelM80",[0.26,-0.052],1],

                        "down": ["LevelM80",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP80 [Indent level: 5],

                    "LevelP80": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP80",[-0.166,0.04],1],["LevelP80",[-0.166,0],1],["LevelP80",[-0.04,0],1],[],["LevelP80",[0.054,0],1],["LevelP80",[0.194,0],1],["LevelP80",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_80 [Indent level: 5],

                    "VALP_1_80": {

                        "type": "text",

                        "source": "static",

                        "text": "80",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP80",[-0.19,-0.017],1],

                        "right": ["LevelP80",[-0.11,-0.017],1],

                        "down": ["LevelP80",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_80_R [Indent level: 5],

                    "VALP_1_80_R": {

                        "type": "text",

                        "source": "static",

                        "text": "80",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP80",[0.21,-0.017],1],

                        "right": ["LevelP80",[0.29,-0.017],1],

                        "down": ["LevelP80",[0.21,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM90 [Indent level: 5],

                    "LevelM90": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelM90",[-0.166,-0.04],1],["LevelM90",[-0.166,0],1],["LevelM90",[-0.138,0],1],[],["LevelM90",[-0.124,0],1],["LevelM90",[-0.096,0],1],[],["LevelM90",[-0.082,0],1],["LevelM90",[-0.054,0],1],[],[],["LevelM90",[0.166,-0.04],1],["LevelM90",[0.166,0],1],["LevelM90",[0.138,0],1],[],["LevelM90",[0.124,0],1],["LevelM90",[0.096,0],1],[],["LevelM90",[0.082,0],1],["LevelM90",[0.054,0],1],[]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_90 [Indent level: 5],

                    "VALM_1_90": {

                        "type": "text",

                        "source": "static",

                        "text": 90,

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM90",[-0.18,-0.052],1],

                        "right": ["LevelM90",[-0.1,-0.052],1],

                        "down": ["LevelM90",[-0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_90_R [Indent level: 5],

                    "VALM_1_90_R": {

                        "type": "text",

                        "source": "static",

                        "text": 90,

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "sourceLength": 2,

                        "pos": ["LevelM90",[0.18,-0.052],1],

                        "right": ["LevelM90",[0.26,-0.052],1],

                        "down": ["LevelM90",[0.18,0.008],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP90 [Indent level: 5],

                    "LevelP90": {

                        "type": "line",

                        "width": 3,

                        "points": [["LevelP90",[-0.166,0.04],1],["LevelP90",[-0.166,0],1],["LevelP90",[-0.04,0],1],[],["LevelP90",[0.054,0],1],["LevelP90",[0.194,0],1],["LevelP90",[0.194,0.04],1]],

                        "source": "Level0"
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_90 [Indent level: 5],

                    "VALP_1_90": {

                        "type": "text",

                        "source": "static",

                        "text": "90",

                        "align": "left",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP90",[-0.19,-0.017],1],

                        "right": ["LevelP90",[-0.11,-0.017],1],

                        "down": ["LevelP90",[-0.19,0.043],1]
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_90_R [Indent level: 5],

                    "VALP_1_90_R": {

                        "type": "text",

                        "source": "static",

                        "text": "90",

                        "align": "right",

                        "scale": 1,

                        "sourceScale": 1,

                        "pos": ["LevelP90",[0.21,-0.017],1],

                        "right": ["LevelP90",[0.29,-0.017],1],

                        "down": ["LevelP90",[0.21,0.043],1]
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare [Indent level: 4],

                "LockingSquare": {

                    "condition": "bomb + AAmissile",

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetDiamond [Indent level: 5],

                    "TargetDiamond": {

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetDiamond|shape [Indent level: 6],


                        "shape": {


                            "type": "line",


                            "width": 4,


                            "points": [["Target",1,"Limit0109",1,[0.02,0.0244063],1],["Target",1,"Limit0109",1,[-0.02,0.0244063],1],["Target",1,"Limit0109",1,[-0.02,-0.0244063],1],["Target",1,"Limit0109",1,[0.02,-0.0244063],1],["Target",1,"Limit0109",1,[0.02,0.0244063],1]]
                        }
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetLocking [Indent level: 5],

                    "TargetLocking": {

                        "condition": "missileLocking",

                        "blinkingPattern": [0.3,0.3],

                        "blinkingStartsOn": 1,

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetLocking|shape [Indent level: 6],

                        "shape": {

                            "type": "line",

                            "width": 4,

                            "points": [["Target",1,"Limit0109",1,[0,-0.0366095],1],["Target",1,"Limit0109",1,[0.03,0],1],["Target",1,"Limit0109",1,[0,0.0366095],1],["Target",1,"Limit0109",1,[-0.03,0],1],["Target",1,"Limit0109",1,[0,-0.0366095],1]]
                        }
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetLocked [Indent level: 5],

                    "TargetLocked": {

                        "condition": "missilelocked",

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetLocked|shape [Indent level: 6],

                        "shape": {

                            "type": "line",

                            "width": 4,

                            "points": [["Target",1,"Limit0109",1,[0,-0.0366095],1],["Target",1,"Limit0109",1,[0.03,0],1],["Target",1,"Limit0109",1,[0,0.0366095],1],["Target",1,"Limit0109",1,[-0.03,0],1],["Target",1,"Limit0109",1,[0,-0.0366095],1]]
                        }
                    }
                },

                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes [Indent level: 4],

                "RadarBoxes": {

                    "type": "radar",

                    "pos0": [0.498,0.485],

                    "pos10": [1.256,1.41],

                    "width": 4,

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|points [Indent level: 5],

                    "points": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknown [Indent level: 5],

                    "pointsUnknown": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownEnemy [Indent level: 5],

                    "pointsUnknownEnemy": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownFriend [Indent level: 5],

                    "pointsUnknownFriend": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownCiv [Indent level: 5],

                    "pointsUnknownCiv": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCar [Indent level: 5],

                    "pointsCar": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarEnemy [Indent level: 5],

                    "pointsCarEnemy": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarFriend [Indent level: 5],

                    "pointsCarFriend": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarCiv [Indent level: 5],

                    "pointsCarCiv": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarNeutral [Indent level: 5],

                    "pointsCarNeutral": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTank [Indent level: 5],

                    "pointsTank": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankEnemy [Indent level: 5],

                    "pointsTankEnemy": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankFriend [Indent level: 5],

                    "pointsTankFriend": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankCiv [Indent level: 5],

                    "pointsTankCiv": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankNeutral [Indent level: 5],

                    "pointsTankNeutral": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplane [Indent level: 5],

                    "pointsAirplane": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplaneEnemy [Indent level: 5],

                    "pointsAirplaneEnemy": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplaneFriend [Indent level: 5],

                    "pointsAirplaneFriend": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeli [Indent level: 5],

                    "pointsHeli": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeliEnemy [Indent level: 5],

                    "pointsHeliEnemy": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeliFriend [Indent level: 5],

                    "pointsHeliFriend": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsLaser [Indent level: 5],

                    "pointsLaser": {

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsLaser|Draw [Indent level: 6],


                        "Draw": {


                            "type": "line",


                            "width": 3,


                            "points": [[[0,-0.0183048],1],[[0.015,8.00126e-010],1],[[-1.31134e-009,0.0183048],1],[[-0.015,-2.18282e-010],1],[[0,-0.0183048],1],[],[[0.00707107,-0.00862894],1],[[0.0148492,-0.0181208],1],[],[[0.00707107,0.00862894],1],[[0.0148492,0.0181208],1],[],[[-0.00707107,0.00862894],1],[[-0.0148492,0.0181208],1],[],[[-0.00707107,-0.00862894],1],[[-0.0148492,-0.0181208],1],[]]
                        }
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsNVG [Indent level: 5],

                    "pointsNVG": {

                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsLaser|Draw [Indent level: 6],


                        "Draw": {


                            "type": "line",


                            "width": 3,


                            "points": [[[0,-0.0183048],1],[[0.015,8.00126e-010],1],[[-1.31134e-009,0.0183048],1],[[-0.015,-2.18282e-010],1],[[0,-0.0183048],1],[],[[0.00707107,-0.00862894],1],[[0.0148492,-0.0181208],1],[],[[0.00707107,0.00862894],1],[[0.0148492,0.0181208],1],[],[[-0.00707107,0.00862894],1],[[-0.0148492,0.0181208],1],[],[[-0.00707107,-0.00862894],1],[[-0.0148492,-0.0181208],1],[]]
                        }
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStatic [Indent level: 5],

                    "pointsStatic": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticEnemy [Indent level: 5],

                    "pointsStaticEnemy": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticFriend [Indent level: 5],

                    "pointsStaticFriend": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticCiv [Indent level: 5],

                    "pointsStaticCiv": {
                    },

                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticNeutral [Indent level: 5],

                    "pointsStaticNeutral": {
                    }
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_1 [Indent level: 2],
        "MFD_1": {
            "topLeft": "MFD_Ammo_TL",
            "topRight": "MFD_Ammo_TR",
            "bottomLeft": "MFD_Ammo_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0.2,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "rhsusf_digital_font_var",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_1|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_1|Draw [Indent level: 3],
            "Draw": {
                "alpha": 0.5,
                "color": [0,1,0.5],
                # Class: CfgVehicles|RHS_A10|MFD|MFD_1|Draw|ammoCounter [Indent level: 4],
                "ammoCounter": {
                    "type": "text",
                    "source": "ammo",
                    "sourceIndex": 1,
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.78,0.42],1],
                    "right": [[1.09,0.42],1],
                    "down": [[0.78,0.97],1]
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_2 [Indent level: 2],
        "MFD_2": {
            "topLeft": "MFD_WP_TL",
            "topRight": "MFD_WP_TR",
            "bottomLeft": "MFD_WP_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0.2,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw [Indent level: 3],
            "Draw": {
                "alpha": 0.5,
                "color": [1,1,1],
                # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|heading [Indent level: 4],
                "heading": {
                    "type": "text",
                    "source": "head",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "left",
                    "pos": [[0.98,0.22],1],
                    "right": [[0.98,0.22],1],
                    "down": [[0.98,0.22],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|HeadingText [Indent level: 4],
                "HeadingText": {
                    "type": "text",
                    "source": "heading",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "refreshRate": 0.1,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.922,0.185],1],
                    "right": [[0.977,0.185],1],
                    "down": [[0.922,0.245],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|AltitudeBox [Indent level: 4],
                "AltitudeBox": {
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|AltitudeBox|Number [Indent level: 5],

                    "Number": {

                        "type": "text",

                        "source": "wpdist",

                        "sourceScale": 5.39957e-005,

                        "sourceLength": 3,

                        "sourceOffset": 0,

                        "align": "left",

                        "scale": 3,

                        "pos": [[0.142,0.195],1],

                        "right": [[0.187,0.195],1],

                        "down": [[0.142,0.245],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|AltitudeBox|ClipScale [Indent level: 5],
                    "ClipScale": {
                        "clipTLParallax": [0.15,0.14],
                        "clipBRParallax": [0.17,0.28],
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|AltitudeBox|ClipScale|Scale [Indent level: 6],
                        "Scale": {
                            "type": "scale",
                            "horizontal": 0,
                            "source": "wpdist",
                            "sourceScale": 0.000539957,
                            "sourceLength": 5,
                            "width": 4,
                            "top": 0.4,
                            "center": 0.2,
                            "bottom": 0,
                            "lineXleft": -1,
                            "lineYright": -1,
                            "lineXleftMajor": -1,
                            "lineYrightMajor": -1,
                            "majorLineEach": 1,
                            "numberEach": 1,
                            "step": 10,
                            "stepSize": 0.055,
                            "align": "left",
                            "scale": 1,
                            "pos": [0.165,0.4],
                            "right": [0.205,0.4],
                            "down": [0.165,0.44]
                        }
                    }
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_3 [Indent level: 2],
        "MFD_3": {
            "topLeft": "MFD_Fuel_TL",
            "topRight": "MFD_Fuel_TR",
            "bottomLeft": "MFD_Fuel_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0.2,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_3|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_3|Draw [Indent level: 3],
            "Draw": {
                "alpha": 0.5,
                "color": [1,1,1],
                # Class: CfgVehicles|RHS_A10|MFD|MFD_3|Draw|FuelNumber [Indent level: 4],
                "FuelNumber": {
                    "type": "text",
                    "source": "fuel",
                    "sourceScale": 12000,
                    "sourceLength": 5,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.8,0.1],1],
                    "right": [[1.05,0.1],1],
                    "down": [[0.8,1.05],1]
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_4 [Indent level: 2],
        "MFD_4": {
            "topLeft": "MFD_WB_TL",
            "topRight": "MFD_WB_TR",
            "bottomLeft": "MFD_WB_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw [Indent level: 3],
            "Draw": {
                "alpha": 0.5,
                "color": [1,1,1],
                "condition": "1",
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon1 [Indent level: 4],
                "Pylon1": {
                    "type": "pylonicon",
                    "pos": [[0.03,0.83],1],
                    "pylon": 1,
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon2 [Indent level: 4],
                "Pylon2": {
                    "pylon": 2,
                    "pos": [[0.159,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon3 [Indent level: 4],
                "Pylon3": {
                    "pylon": 3,
                    "pos": [[0.288,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon4 [Indent level: 4],
                "Pylon4": {
                    "pylon": 4,
                    "pos": [[0.422,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon5 [Indent level: 4],
                "Pylon5": {
                    "pylon": 5,
                    "pos": [[0.347,0.06],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon6 [Indent level: 4],
                "Pylon6": {
                    "pylon": 6,
                    "pos": [[0.486,0.06],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon7 [Indent level: 4],
                "Pylon7": {
                    "pylon": 7,
                    "pos": [[0.625,0.06],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon8 [Indent level: 4],
                "Pylon8": {
                    "pylon": 8,
                    "pos": [[0.546,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon9 [Indent level: 4],
                "Pylon9": {
                    "pylon": 9,
                    "pos": [[0.678,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon10 [Indent level: 4],
                "Pylon10": {
                    "pylon": 10,
                    "pos": [[0.809,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon11 [Indent level: 4],
                "Pylon11": {
                    "pylon": 11,
                    "pos": [[0.942,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty1 [Indent level: 4],
                "PylonEmpty1": {
                    "condition": "pylonEmpty1",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty1|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.05,0.885],1],[[0.08,0.885],1],[[0.08,0.965],1],[[0.05,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty2 [Indent level: 4],
                "PylonEmpty2": {
                    "condition": "pylonEmpty2",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty2|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.179,0.885],1],[[0.209,0.885],1],[[0.209,0.965],1],[[0.179,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty3 [Indent level: 4],
                "PylonEmpty3": {
                    "condition": "pylonEmpty3",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty3|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.308,0.885],1],[[0.338,0.885],1],[[0.338,0.965],1],[[0.308,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty4 [Indent level: 4],
                "PylonEmpty4": {
                    "condition": "pylonEmpty4",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty4|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.442,0.885],1],[[0.472,0.885],1],[[0.472,0.965],1],[[0.442,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty5 [Indent level: 4],
                "PylonEmpty5": {
                    "condition": "pylonEmpty5",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty5|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.367,0.115],1],[[0.397,0.115],1],[[0.397,0.195],1],[[0.367,0.195],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty6 [Indent level: 4],
                "PylonEmpty6": {
                    "condition": "pylonEmpty6",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty6|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.506,0.115],1],[[0.536,0.115],1],[[0.536,0.195],1],[[0.506,0.195],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty7 [Indent level: 4],
                "PylonEmpty7": {
                    "condition": "pylonEmpty7",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty7|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.645,0.115],1],[[0.675,0.115],1],[[0.675,0.195],1],[[0.645,0.195],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty8 [Indent level: 4],
                "PylonEmpty8": {
                    "condition": "pylonEmpty8",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty8|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.566,0.885],1],[[0.596,0.885],1],[[0.596,0.965],1],[[0.566,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty9 [Indent level: 4],
                "PylonEmpty9": {
                    "condition": "pylonEmpty9",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty9|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.698,0.885],1],[[0.728,0.885],1],[[0.728,0.965],1],[[0.698,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty10 [Indent level: 4],
                "PylonEmpty10": {
                    "condition": "pylonEmpty10",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty10|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.829,0.885],1],[[0.859,0.885],1],[[0.859,0.965],1],[[0.829,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty11 [Indent level: 4],
                "PylonEmpty11": {
                    "condition": "pylonEmpty11",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty11|Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.962,0.885],1],[[0.992,0.885],1],[[0.992,0.965],1],[[0.962,0.965],1]]]
                    }
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_5 [Indent level: 2],
        "MFD_5": {
            "topLeft": "MFD_WN_TL",
            "topRight": "MFD_WN_TR",
            "bottomLeft": "MFD_WN_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw [Indent level: 3],
            "Draw": {
                "alpha": 0.5,
                "color": [1,1,1],
                "condition": "1",
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon1 [Indent level: 4],
                "Pylon1": {
                    "type": "pylonicon",
                    "pos": [[0.07,0.88],1],
                    "pylon": 1,
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon2 [Indent level: 4],
                "Pylon2": {
                    "pylon": 2,
                    "pos": [[0.189,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon3 [Indent level: 4],
                "Pylon3": {
                    "pylon": 3,
                    "pos": [[0.308,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon4 [Indent level: 4],
                "Pylon4": {
                    "pylon": 4,
                    "pos": [[0.432,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon5 [Indent level: 4],
                "Pylon5": {
                    "pylon": 5,
                    "pos": [[0.377,0.05],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon6 [Indent level: 4],
                "Pylon6": {
                    "pylon": 6,
                    "pos": [[0.486,0.05],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon7 [Indent level: 4],
                "Pylon7": {
                    "pylon": 7,
                    "pos": [[0.625,0.05],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon8 [Indent level: 4],
                "Pylon8": {
                    "pylon": 8,
                    "pos": [[0.556,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon9 [Indent level: 4],
                "Pylon9": {
                    "pylon": 9,
                    "pos": [[0.668,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon10 [Indent level: 4],
                "Pylon10": {
                    "pylon": 10,
                    "pos": [[0.799,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon11 [Indent level: 4],
                "Pylon11": {
                    "pylon": 11,
                    "pos": [[0.912,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_6 [Indent level: 2],
        "MFD_6": {
            "topLeft": "MFD_ALT_TL",
            "topRight": "MFD_ALT_TR",
            "bottomLeft": "MFD_ALT_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_6|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_6|Draw [Indent level: 3],
            "Draw": {
                "alpha": 0.7,
                "color": [0,0,0],
                "condition": "altitudeASL>=1000",
                # Class: CfgVehicles|RHS_A10|MFD|MFD_6|Draw|AltGrp [Indent level: 4],
                "AltGrp": {
                    "color": [1,1,1],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_6|Draw|AltGrp|AltText [Indent level: 5],
                    "AltText": {
                        "type": "text",
                        "source": "altitudeASL",
                        "sourceScale": 0.001,
                        "sourceLength": 1,
                        "sourceOffset": -0.5,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.343,0.422],1],
                        "right": [[0.478,0.422],1],
                        "down": [[0.343,0.577],1]
                    }
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR [Indent level: 2],
        "MFD_RWR": {
            "topLeft": "MFD_RWR_TL",
            "topRight": "MFD_RWR_TR",
            "bottomLeft": "MFD_RWR_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw [Indent level: 3],
            "Draw": {
                "alpha": 0.3,
                "color": [0.7,0.7,0.7],
                # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR [Indent level: 4],
                "RWR": {
                    "type": "sensor",
                    "pos": [[0.07,0.07],1],
                    "down": [[0.93,0.93],1],
                    "showTargetTypes": "2 + 8 + 64 + 128 + 256",
                    "width": 4,
                    "sensorLineType": 3,
                    "sensorLineWidth": 0,
                    "range": 16000,
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|MissileThreat [Indent level: 5],
                    "MissileThreat": {
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|MissileThreat|TargetLines [Indent level: 6],

                        "TargetLines": {

                            "type": "line",

                            "width": 4,

                            "points": [[[0,-0.0610158],1],[[0.00868,-0.0600884],1],[[0.0171,-0.0573366],1],[[0.025,-0.0528397],1],[[0.03214,-0.0467381],1],[[0.0383,-0.039221],1],[[0.0433,-0.0305079],1],[[0.046985,-0.0208674],1],[[0.04924,-0.0105923],1],[[0.05,0],1],[[0.04924,0.0105923],1],[[0.046985,0.0208674],1],[[0.0433,0.0305079],1],[[0.0383,0.039221],1],[[0.03214,0.0467381],1],[[0.025,0.0528397],1],[[0.0171,0.0573366],1],[[0.00868,0.0600884],1],[[0,0.0610158],1],[[-0.00868,0.0600884],1],[[-0.0171,0.0573366],1],[[-0.025,0.0528397],1],[[-0.03214,0.0467381],1],[[-0.0383,0.039221],1],[[-0.0433,0.0305079],1],[[-0.046985,0.0208674],1],[[-0.04924,0.0105923],1],[[-0.05,0],1],[[-0.04924,-0.0105923],1],[[-0.046985,-0.0208674],1],[[-0.0433,-0.0305079],1],[[-0.0383,-0.039221],1],[[-0.03214,-0.0467381],1],[[-0.025,-0.0528397],1],[[-0.0171,-0.0573366],1],[[-0.00868,-0.0600884],1],[[0,-0.0610158],1]]
                        },
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|MissileThreat|TextM [Indent level: 6],
                        "TextM": {
                            "type": "text",
                            "source": "static",
                            "text": "M",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.04],1],
                            "right": [[0.08,-0.04],1],
                            "down": [[0,0.04],1]
                        }
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|lockingThreat [Indent level: 5],
                    "lockingThreat": {
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|lockingThreat|TargetLines [Indent level: 6],

                        "TargetLines": {

                            "type": "line",

                            "points": [[[0,-0.0610158],1],[[0.00868,-0.0600884],1],[[0.0171,-0.0573366],1],[[0.025,-0.0528397],1],[[0.03214,-0.0467381],1],[[0.0383,-0.039221],1],[[0.0433,-0.0305079],1],[[0.046985,-0.0208674],1],[[0.04924,-0.0105923],1],[[0.05,0],1],[[0.04924,0.0105923],1],[[0.046985,0.0208674],1],[[0.0433,0.0305079],1],[[0.0383,0.039221],1],[[0.03214,0.0467381],1],[[0.025,0.0528397],1],[[0.0171,0.0573366],1],[[0.00868,0.0600884],1],[[0,0.0610158],1],[[-0.00868,0.0600884],1],[[-0.0171,0.0573366],1],[[-0.025,0.0528397],1],[[-0.03214,0.0467381],1],[[-0.0383,0.039221],1],[[-0.0433,0.0305079],1],[[-0.046985,0.0208674],1],[[-0.04924,0.0105923],1],[[-0.05,0],1],[[-0.04924,-0.0105923],1],[[-0.046985,-0.0208674],1],[[-0.0433,-0.0305079],1],[[-0.0383,-0.039221],1],[[-0.03214,-0.0467381],1],[[-0.025,-0.0528397],1],[[-0.0171,-0.0573366],1],[[-0.00868,-0.0600884],1],[[0,-0.0610158],1],[[0.06,0],1],[[0,0.0610158],1],[[-0.06,0],1],[[0,-0.0610158],1],[[0.06,0],1]]
                        },
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|lockingThreat|TextL [Indent level: 6],
                        "TextL": {
                            "type": "text",
                            "source": "static",
                            "text": "L",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.04],1],
                            "right": [[0.08,-0.04],1],
                            "down": [[0,0.04],1]
                        }
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|rwr [Indent level: 5],
                    "rwr": {
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|rwr|TargetLines [Indent level: 6],

                        "TargetLines": {

                            "type": "line",

                            "points": [[[0.06,0],1],[[0,0.0610158],1],[[-0.06,0],1],[[0,-0.0610158],1],[[0.06,0],1]]
                        },
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|rwr|TextA [Indent level: 6],
                        "TextA": {
                            "type": "text",
                            "source": "static",
                            "text": "A",
                            "align": "center",
                            "scale": 1,
                            "pos": [[0,-0.04],1],
                            "right": [[0.08,-0.04],1],
                            "down": [[0,0.04],1]
                        }
                    }
                }
            }
        }
    },
    "maxOmega": 2000,
    "accelAidForceCoef": 1,
    "accelAidForceYOffset": -1,
    "accelAidForceSpd": 1,
    "turnCoef": 0.05,
    # Class: CfgVehicles|RHS_A10|Wheels [Indent level: 1],
    "Wheels": {
        "disableWheelsWhenDestroyed": 1,
        # Class: CfgVehicles|RHS_A10|Wheels|Wheel_1 [Indent level: 2],
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
            "maxDroop": 0.05,
            "sprungMass": 11400,
            "springStrength": 1.2e+006,
            "springDamperRate": 128000,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 3,
            "latStiffY": 21,
            "frictionVsSlipGraph": [[0,1],[0.5,1.4],[1,0.6]]
        },
        # Class: CfgVehicles|RHS_A10|Wheels|Wheel_1_fake [Indent level: 2],
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
            "maxDroop": 0.05,
            "sprungMass": 11400,
            "springStrength": 1.2e+006,
            "springDamperRate": 128000,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 3,
            "latStiffY": 21,
            "frictionVsSlipGraph": [[0,1],[0.5,1.4],[1,0.6]]
        },
        # Class: CfgVehicles|RHS_A10|Wheels|Wheel_2 [Indent level: 2],
        "Wheel_2": {
            "steering": 0,
            "boneName": "Wheel_2",
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "suspForceAppPointOffset": "Wheel_2_center",
            "tireForceAppPointOffset": "Wheel_2_center",
            "width": 0.28,
            "maxCompression": 0.25,
            "maxDroop": 0.1,
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
            "latStiffX": 3,
            "latStiffY": 21,
            "frictionVsSlipGraph": [[0,1],[0.5,1.4],[1,0.6]]
        },
        # Class: CfgVehicles|RHS_A10|Wheels|Wheel_3 [Indent level: 2],
        "Wheel_3": {
            "steering": 0,
            "side": "right",
            "boneName": "Wheel_3",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspForceAppPointOffset": "Wheel_3_center",
            "tireForceAppPointOffset": "Wheel_3_center",
            "width": 0.28,
            "maxCompression": 0.25,
            "maxDroop": 0.1,
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
            "latStiffX": 3,
            "latStiffY": 21,
            "frictionVsSlipGraph": [[0,1],[0.5,1.4],[1,0.6]]
        }
    },
    "soundGetIn": ["A3|Sounds_F|vehicles|air|CAS_01|getin_wipeout",1,1,40],
    "soundGetOut": ["A3|Sounds_F|air|Plane_Fighter_03|getout",1,1,40],
    "cabinOpenSound": ["A3|Sounds_F|air|noises|Plane_CAS01_CabinOpen",3.16228,1,40],
    "cabinCloseSound": ["A3|Sounds_F|air|noises|Plane_CAS01_CabinClose",3.16228,1,40],
    "cabinOpenSoundInternal": ["A3|Sounds_F|air|noises|Plane_CAS01_CabinOpen",10,1,40],
    "cabinCloseSoundInternal": ["A3|Sounds_F|air|noises|Plane_CAS01_CabinClose",10,1,40],
    "soundDammage": ["",1,1],
    "soundEngineOnInt": ["A3|Sounds_F|vehicles|air|CAS_01|CAS_01_start_int",1,1],
    "soundEngineOnExt": ["A3|Sounds_F|vehicles|air|CAS_01|CAS_01_start_ext",1.41254,1,500],
    "soundEngineOffInt": ["A3|Sounds_F|vehicles|air|CAS_01|CAS_01_stop_int",1,1],
    "soundEngineOffExt": ["A3|Sounds_F|vehicles|air|CAS_01|CAS_01_stop_ext",1.41254,1,500],
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_1",0.316228,1],
    "soundWaterCollision1": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_1",1.41254,1,500],
    "soundWaterCollision2": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_2",1.41254,1,500],
    "soundWaterCrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "soundGearUp": ["A3|Sounds_F|vehicles|air|CAS_01|gear_up",0.794328,1,150],
    "soundGearDown": ["A3|Sounds_F|vehicles|air|CAS_01|gear_down",0.794328,1,150],
    "soundFlapsUp": ["A3|Sounds_F|vehicles|air|CAS_01|Flaps_Up",0.630957,1,100],
    "soundFlapsDown": ["A3|Sounds_F|vehicles|air|CAS_01|Flaps_Down",0.630957,1,100],
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
    # Class: CfgVehicles|Plane_CAS_01_base_F|scrubLandInt [Indent level: 1],
    "scrubLandInt": {
        "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
        "frequency": 1,
        "volume": "(scrubLand factor[0.01, 0.20])"
    },
    # Class: CfgVehicles|Plane_CAS_01_base_F|Sounds [Indent level: 1],
    "Sounds": {
        "soundSets": ["Plane_CAS_01_EngineLowExt_SoundSet","Plane_CAS_01_EngineHighExt_SoundSet","Plane_CAS_01_ForsageExt_SoundSet","Plane_CAS_01_WindNoiseExt_SoundSet","Plane_CAS_01_EngineLowInt_SoundSet","Plane_CAS_01_EngineHighInt_SoundSet","Plane_CAS_01_ForsageInt_SoundSet","Plane_CAS_01_WindNoiseInt_SoundSet","Plane_CAS_01_EngineExt_Dist_Rear_SoundSet","Plane_CAS_01_EngineExt_Dist_Front_SoundSet","Plane_CAS_01_EngineExt_Middle_SoundSet","Plane_CAS_01_EngineExt_Middle_SoundSet","Plane_CAS_01_EngineExt_Dist_Front_SoundSet","Plane_CAS_01_EngineExt_Dist_Rear_SoundSet"]
    },
    "features": "Randomization: No						<br />Camo selections: 2 - the main body, wings and gear						<br />Script door sources: None						<br />Script animations: None						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: No						<br />Cargo proxy indexes: None",
    "_generalMacro": "Plane_CAS_01_base_F",
    "editorSubcategory": "EdSubcat_Planes",
    "destrType": "DestructWreck",
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "getinAction": "pilot_plane_cas_01_Enter",
    "getoutaction": "pilot_plane_cas_01_Exit",
    "viewDriverShadowDiff": 0.5,
    "viewDriverShadowAmb": 0.5,
    "clutchStrength": 100,
    "dampingRateFullThrottle": 0.5,
    "stallSpeed": 210,
    "stallWarningTreshold": 0.04,
    "airBrake": 1,
    "airBrakeFrictionCoef": 2.6,
    "flaps": 1,
    "gearsUpFrictionCoef": 0.55,
    "airFrictionCoefs0": [0,0,0],
    "airFrictionCoefs1": [0.1,0.6,0.0067],
    "airFrictionCoefs2": [0.001,0.006,7e-005],
    "altNoForce": 13000,
    "altFullForce": 2000,
    "rudderInfluence": 0.866,
    "elevatorControlsSensitivityCoef": 4,
    "rudderControlsSensitivityCoef": 3,
    "showAllTargets": 4,
    "extCameraPosition": [0,3.8,-20],
    # Class: CfgVehicles|Plane_CAS_01_base_F|ViewPilot [Indent level: 1],
    "ViewPilot": {
        "initAngleX": -2.5,
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
    "memoryPointGun": "Gatling_barrels_end",
    "gunAimDown": 0,
    "driveOnComponent": [],
    # Class: CfgVehicles|Plane_CAS_01_base_F|Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles|Plane_CAS_01_base_F|Exhausts|Exhaust1 [Indent level: 2],

        "Exhaust1": {

            "position": "Exhaust_1_pos",

            "direction": "Exhaust_1_dir",

            "effect": "ExhaustsEffectPlaneHP",

            "engineIndex": 0
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|Exhausts|Exhaust2 [Indent level: 2],
        "Exhaust2": {
            "position": "Exhaust_2_pos",
            "direction": "Exhaust_2_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineIndex": 1
        }
    },
    "explosionShielding": 1,
    "armorLights": 1,
    "waterLeakiness": 1.15,
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "waterLinearDampingCoefY": 0,
    "waterLinearDampingCoefX": 5,
    "waterResistanceCoef": 0.04,
    "ejectSpeed": [0,60,0],
    "transportMaxWeapons": 6,
    "transportMaxMagazines": 24,
    "transportMaxBackpacks": 6,
    "maximumLoad": 500,
    "memoryPointSupply": "doplnovani",
    # Class: CfgVehicles|Plane_Base_F|TransportBackpacks [Indent level: 1],
    "TransportBackpacks": {
    },
    # Class: CfgVehicles|Plane_Base_F|TransportWeapons [Indent level: 1],
    "TransportWeapons": {
    },
    # Class: CfgVehicles|Plane_Base_F|camShakeGForce [Indent level: 1],
    "camShakeGForce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minSpeed": 1
    },
    "minGForce": 0.3,
    "maxGForce": 3,
    "gForceShakeAttenuation": 0.5,
    # Class: CfgVehicles|Plane_Base_F|NewTurret [Indent level: 1],
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
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewGunner [Indent level: 2],
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
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
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
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
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
            # Class: WeaponFireGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
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
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
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
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints [Indent level: 2],
        "HitPoints": {
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitTurret [Indent level: 3],

            "HitTurret": {

                "armor": 0.8,

                "material": 51,

                "name": "turret",

                "visual": "turret",

                "passThrough": 1,

                "explosionShielding": 1
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitGun [Indent level: 3],
            "HitGun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passThrough": 1,
                "explosionShielding": 1
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "Turrets": {
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
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
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
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
    "durationGetIn": 0.99,
    "durationGetOut": 0.99,
    "vtol": 0,
    "tailHook": 0,
    "lightOnGear": 1,
    "cost": 2e+006,
    "simulation": "airplanex",
    "minGunElev": 0,
    "maxGunElev": 0,
    "minGunTurn": 0,
    "maxGunTurn": 0,
    "VTOLYawInfluence": 2,
    "VTOLPitchInfluence": 2,
    "VTOLRollInfluence": 2,
    # Class: CfgVehicles|Plane|ViewOptics [Indent level: 1],
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
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "dustEffect": "HeliDust",
    "waterEffect": "HeliWater",
    # Class: CfgVehicles|Plane|GunFire [Indent level: 1],
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
        # Class: WeaponFireGun|Table [Indent level: 0],
        "Table": {
            # Class: WeaponFireGun|Table|T0 [Indent level: 1],

            "T0": {

                "maxT": 0,

                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun|Table|T1 [Indent level: 1],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun|Table|T2 [Indent level: 1],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun|Table|T3 [Indent level: 1],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun|Table|T4 [Indent level: 1],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun|Table|T5 [Indent level: 1],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun|Table|T6 [Indent level: 1],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun|Table|T7 [Indent level: 1],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun|Table|T8 [Indent level: 1],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun|Table|T9 [Indent level: 1],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun|Table|T10 [Indent level: 1],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun|Table|T11 [Indent level: 1],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun|Table|T12 [Indent level: 1],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun|Table|T13 [Indent level: 1],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun|Table|T14 [Indent level: 1],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun|Table|T15 [Indent level: 1],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun|Table|T16 [Indent level: 1],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun|Table|T17 [Indent level: 1],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun|Table|T18 [Indent level: 1],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun|Table|T19 [Indent level: 1],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun|Table|T20 [Indent level: 1],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun|Table|T21 [Indent level: 1],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun|Table|T22 [Indent level: 1],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|Plane|GunClouds [Indent level: 1],
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
        # Class: WeaponCloudsGun|Table [Indent level: 0],
        "Table": {
            # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

            "T0": {

                "maxT": 0,

                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|Plane|MGunFire [Indent level: 1],
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
        # Class: WeaponFireGun|Table [Indent level: 0],
        "Table": {
            # Class: WeaponFireGun|Table|T0 [Indent level: 1],

            "T0": {

                "maxT": 0,

                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun|Table|T1 [Indent level: 1],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun|Table|T2 [Indent level: 1],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun|Table|T3 [Indent level: 1],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun|Table|T4 [Indent level: 1],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun|Table|T5 [Indent level: 1],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun|Table|T6 [Indent level: 1],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun|Table|T7 [Indent level: 1],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun|Table|T8 [Indent level: 1],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun|Table|T9 [Indent level: 1],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun|Table|T10 [Indent level: 1],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun|Table|T11 [Indent level: 1],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun|Table|T12 [Indent level: 1],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun|Table|T13 [Indent level: 1],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun|Table|T14 [Indent level: 1],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun|Table|T15 [Indent level: 1],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun|Table|T16 [Indent level: 1],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun|Table|T17 [Indent level: 1],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun|Table|T18 [Indent level: 1],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun|Table|T19 [Indent level: 1],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun|Table|T20 [Indent level: 1],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun|Table|T21 [Indent level: 1],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun|Table|T22 [Indent level: 1],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|Plane|MGunClouds [Indent level: 1],
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
        # Class: WeaponCloudsMGun|Table [Indent level: 0],
        "Table": {
            # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

            "T0": {

                "maxT": 0,

                "color": [1,1,1,0]
            }
        }
    },
    "numberPhysicalWheels": 3,
    # Class: CfgVehicles|Plane|SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles|Plane|SpeechVariants|Default [Indent level: 2],

        "Default": {

            "speechSingular": ["veh_air_plane_s"],

            "speechPlural": ["veh_air_plane_p"]
        }
    },
    "textSingular": "fast mover",
    "textPlural": "fast movers",
    "nameSound": "veh_air_plane_s",
    "type": 2,
    "fuelExplosionPower": 10,
    "crewCrashProtection": 0.15,
    "damageEffect": "AirDestructionEffects",
    "cargoGetInAction": ["GetInHigh"],
    "cargoGetOutAction": ["GetOutHigh"],
    "gunnerGetInAction": "GetInHigh",
    "gunnerGetOutAction": "GetOutHigh",
    "getInRadius": 1.2,
    # Class: CfgVehicles|Plane|CamShake [Indent level: 1],
    "CamShake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minSpeed": 200
    },
    "minTotalDamageThreshold": 0.005,
    # Class: CfgVehicles|Plane|DestructionEffects [Indent level: 1],
    "DestructionEffects": {
    },
    "formationTime": 10,
    "fuelCapacity": 1000,
    "insideSoundCoef": 0.0316228,
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
    "countermeasureActivationRadius": 10000,
    # Class: CfgVehicles|Air|camShakeDamage [Indent level: 1],
    "camShakeDamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minSpeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "secondaryExplosion": -1,
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "SquadTitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memoryPointsGetInCargo": "pos cargo",
    "memoryPointsGetInCargoDir": "pos cargo dir",
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
    "selectionShowDamage": "poskozeni",
    "selectionBackLights": "zadni svetlo",
    # Class: CfgVehicles|AllVehicles|ViewCargo [Indent level: 1],
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
    # Class: CfgVehicles|AllVehicles|PilotSpec [Indent level: 1],
    "PilotSpec": {
        "showHeadPhones": 0
    },
    # Class: CfgVehicles|AllVehicles|CargoSpec [Indent level: 1],
    "CargoSpec": {
        # Class: CfgVehicles|AllVehicles|CargoSpec|Cargo1 [Indent level: 2],

        "Cargo1": {

            "showHeadPhones": 0
        }
    },
    # Class: CfgVehicles|AllVehicles|SoundEvents [Indent level: 1],
    "SoundEvents": {
    },
    "tracksSpeed": 0,
    "selectionLeftOffset": "",
    "selectionRightOffset": "",
    "cargoProxyIndexes": [],
    "driverDoor": "",
    "cargoDoors": [],
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "cargoPreciseGetInOut": [0],
    "waterPPInVehicle": 1,
    "htMin": 60,
    "htMax": 1800,
    "afMax": 200,
    "mfMax": 100,
    "mFact": 0.2,
    "tBody": 150,
    "impactEffectSpeedLimit": 8,
    "showCrewAim": 0,
    # Class: CfgVehicles|AllVehicles|CargoTurret [Indent level: 1],
    "CargoTurret": {
        # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2],

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
        # Class: CfgVehicles|AllVehicles|CargoTurret|Hitpoints [Indent level: 2],
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
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
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
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
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
            # Class: WeaponFireGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
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
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
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
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "Turrets": {
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
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
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
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
    "antiRollbarForceCoef": 0,
    "antiRollbarForceLimit": 5,
    "antiRollbarSpeedMin": 20,
    "antiRollbarSpeedMax": 60,
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
    # Class: CfgVehicles|All|NVGMarkers [Indent level: 1],
    "NVGMarkers": {
    },
    # Class: CfgVehicles|All|NVGMarker [Indent level: 1],
    "NVGMarker": {
        "diffuse": [1,1,1,1],
        "ambient": [1,1,1,1],
        "brightness": 1,
        "blinking": 0,
        "onlyInNvg": 0
    },
    # Class: CfgVehicles|All|HeadLimits [Indent level: 1],
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
    # Class: CfgVehicles|All|SoundEnvironExt [Indent level: 1],
    "SoundEnvironExt": {
    },
    # Class: CfgVehicles|All|SoundEquipment [Indent level: 1],
    "SoundEquipment": {
    },
    # Class: CfgVehicles|All|SoundGear [Indent level: 1],
    "SoundGear": {
    },
    # Class: CfgVehicles|All|SoundBreath [Indent level: 1],
    "SoundBreath": {
    },
    # Class: CfgVehicles|All|SoundBreathSwimming [Indent level: 1],
    "SoundBreathSwimming": {
    },
    # Class: CfgVehicles|All|SoundBreathInjured [Indent level: 1],
    "SoundBreathInjured": {
    },
    # Class: CfgVehicles|All|SoundHitScream [Indent level: 1],
    "SoundHitScream": {
    },
    # Class: CfgVehicles|All|SoundInjured [Indent level: 1],
    "SoundInjured": {
    },
    # Class: CfgVehicles|All|SoundBreathAutomatic [Indent level: 1],
    "SoundBreathAutomatic": {
    },
    # Class: CfgVehicles|All|SoundDrown [Indent level: 1],
    "SoundDrown": {
    },
    # Class: CfgVehicles|All|SoundChoke [Indent level: 1],
    "SoundChoke": {
    },
    # Class: CfgVehicles|All|SoundRecovered [Indent level: 1],
    "SoundRecovered": {
    },
    # Class: CfgVehicles|All|SoundBurning [Indent level: 1],
    "SoundBurning": {
    },
    # Class: CfgVehicles|All|PulsationSound [Indent level: 1],
    "PulsationSound": {
    },
    # Class: CfgVehicles|All|SoundDrowning [Indent level: 1],
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
    # Class: CfgVehicles|All|FxExplo [Indent level: 1],
    "FxExplo": {
        "access": 1
    },
    "selectionDamage": "zbytek",
    "cargoCanEject": 1,
    "fireResistance": 10,
    "airCapacity": 10,
    "waterDamageEngine": 0.2,
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "coefSpeedInside": 2,
    "windSockExist": 0,
    "slingLoadCargoMemoryPoints": [],
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    "soundTurnIn": ["",0.000316228,1],
    "soundTurnOut": ["",0.000316228,1],
    "soundTurnInInternal": ["",0.000316228,1],
    "soundTurnOutInternal": ["",0.000316228,1],
    "insideDetectCoef": 0.05,
}