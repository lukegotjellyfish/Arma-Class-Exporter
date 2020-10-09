RHS_C130J = {
    "author": "Red Hammer Studios",
    "scope": 2,
    "side": 1,
    "rhs_paraRamp": "ramp",
    "rhs_paraOff": -7,
    "rhs_rampAnim": "ramp_bottom",
    "rhs_gearAnim": "Gear_1_1",
    "rhs_paraScript": "rhs_fnc_vehPara",
    "dlc": "RHS_USAF",
    "LESH_canBeTowed": 1,
    "LESH_towFromFront": 1,
    "LESH_AxisOffsetTarget": [0,15,1.17],
    "LESH_WheelOffset": [0,2],
    "irTarget": 1,
    "irTargetSize": 1.2,
    "visualTarget": 1,
    "visualTargetSize": 1.5,
    "radarTarget": 1,
    "radarTargetSize": 1.5,
    "LockDetectionSystem": "8",
    "incomingMissileDetectionSystem": "2 + 8 + 16",
    "destrType": "DestructWreck",
    "unitInfoType": "RHSUSF_RscUnitInfoAirPlane",
    "displayname": "C-130J",
    "category": "Air",
    "vehicleClass": "rhs_vehclass_aircraft",
    "faction": "rhs_faction_usaf",
    "crew": "rhsusf_airforce_pilot",
    "typicalCargo": ["rhsusf_airforce_pilot","rhsusf_airforce_pilot"],
    "model": "rhsusf|addons|rhsusf_a2port_air|C130J|c130j.p3d",
    "picture": "rhsusf|addons|rhsusf_a2port_air|data|ico|rhs_c130j_pic_ca.paa",
    "icon": "rhsusf|addons|rhsusf_a2port_air|data|mapico|icon_c130j_CA.paa",
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|RHS_C130J.paa",
    "mapSize": 25,
    "accuracy": 0.15,
    "cost": 20000,
    "getInRadius": 2.5,
    "showNVGCargo": [1],
    "cabinOpening": 0,
    "driverDoor": "Door_1",
    "getinaction": "GetInLow",
    "getoutaction": "GetInLow",
    "driverAction": "RHS_C130_Pilot",
    "driverRightHandAnimName": "pilot_control",
    "driverLeftHandAnimName": "pilot_control",
    "altFullForce": 8535,
    "altNoForce": 17000,
    "maxSpeed": 648,
    "stallSpeed": 180,
    "stallWarningTreshold": 0.5,
    "envelope": [0.1,0.1,0.9,2.8,3.5,3.7,3.8,3.8,3.6,3.3,2.7],
    "thrustCoef": [0.9,0.8,0.9,1.3,1.2,1.2,1.1,1,0.9,0.2,0.1,0,0],
    "angleOfIndicence": -0.0174533,
    "rudderInfluence": 0.866,
    "rudderControlsSensitivityCoef": 1.5,
    "rudderCoef": [0,0.4,1,1.4,1.8,2,2.2,2.3,2.4,2.5,2.5,2.5,2.6],
    "aileronSensitivity": 1,
    "aileronControlsSensitivityCoef": 1,
    "aileronCoef": [0,0.5,1,1.2,1.4,1.5,1.6],
    "elevatorSensitivity": 1,
    "elevatorControlsSensitivityCoef": 3,
    "elevatorCoef": [0,1,1.2,1.4,1.5,1.6,1.6],
    "flapsFrictionCoef": 0.2,
    "wheelSteeringSensitivity": 2,
    "draconicForceXCoef": 4.3,
    "draconicForceYCoef": 0.5,
    "draconicForceZCoef": 0.2,
    "draconicTorqueXCoef": [16,15.5,15,14.5,14,14,14.5,15,16,17,18],
    "draconicTorqueYCoef": [3.2,2.5,1,"",0,0,0,0,0,0,0,0,0,0,0],
    "cargocaneject": 1,
    "cargoIsCoDriver": [0,0],
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "memoryPointsGetInCargo": ["pos driver","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2"],
    "memoryPointsGetInCargoDir": ["pos driver dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir"],
    "cargoDoors": ["Door_1","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2"],
    "cargoAction": ["Truck_Cargo01","Truck_Cargo04","Truck_Cargo04","Truck_Cargo02","Truck_Cargo01","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo01","Truck_Cargo02","Truck_Cargo01","Truck_Cargo04","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo04","Truck_Cargo01","Truck_Cargo04","Truck_Cargo02","Truck_Cargo04","Truck_Cargo02","Truck_Cargo01","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo01","Truck_Cargo02","Truck_Cargo01","Truck_Cargo04","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo04","Truck_Cargo01","Truck_Cargo04","Truck_Cargo02"],
    "transportSoldier": 25,
    "gunnerUsesPilotView": 1,
    "driverCompartments": "Compartment1",
    "cargoCompartments": ["Compartment1"],
    "attenuationEffectType": "OpenHeliAttenuation",
    # Class: CfgVehicles|RHS_C130J_Base|Damage [Indent level: 1],
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo_in.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_body.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_body_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_body_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_interior.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_interior_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_interior_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_wings.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_wings_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_wings_destruct.rvmat"]
    },
    "selectionDamage": "zbytek",
    "selectionShowDamage": "zbytek",
    "reportOwnPosition": 1,
    # Class: CfgVehicles|RHS_C130J_Base|Components [Indent level: 1],
    "Components": {
        # Class: CfgVehicles|RHS_C130J_Base|Components|TransportPylonsComponent [Indent level: 2]
        "TransportPylonsComponent": {
            "UIPicture": "rhsusf|addons|rhsusf_a2port_air|data|loadouts|RHS_C130_EDEN_CA.paa",
            # Class: CfgVehicles|RHS_C130J_Base|Components|TransportPylonsComponent|pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles|RHS_C130J_Base|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4]
                "cmDispenser": {
                    "hardpoints": ["RHSUSF_cm_ANALE40_x2","RHSUSF_cm_ANALE40_x4","RHSUSF_cm_ANALE40_x8","RHSUSF_cm_ANALE40_x16"],
                    "priority": 1,
                    "attachment": "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x16",
                    "maxweight": 800,
                    "UIposition": [0.33,0]
                }
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Components|SensorsManagerComponent [Indent level: 2],
        "SensorsManagerComponent": {
            # Class: CfgVehicles|RHS_C130J_Base|Components|SensorsManagerComponent|Components [Indent level: 3]
            "Components": {
                # Class: CfgVehicles|RHS_C130J_Base|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4]
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
        # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "Components": {
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 4],
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4],
                "SensorDisplay": {
                    "componentType": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [3000,8000,16000,35000]
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultDisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "VehicleSystemsDisplayManagerComponentRight": {
            "defaultDisplay": "SensorDisplay",
            # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "Components": {
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 4],
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4],
                "SensorDisplay": {
                    "componentType": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [3000,8000,16000,35000]
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Air|Components|TransportCountermeasuresComponent [Indent level: 2],
        "TransportCountermeasuresComponent": {
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|EventHandlers [Indent level: 1],
    "EventHandlers": {
        # Class: CfgVehicles|RHS_C130J_Base|EventHandlers|RHSUSF_EventHandlers [Indent level: 2]
        "RHSUSF_EventHandlers": {
            "getIn": "_this call rhs_fnc_C130_doors",
            "getOut": "_this call rhs_fnc_C130_doors"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines [Indent level: 1],
    "TransportMagazines": {
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 30
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhsusf_100Rnd_556x45_soft_pouch [Indent level: 2],
        "_xx_rhsusf_100Rnd_556x45_soft_pouch": {
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch",
            "count": 8
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_M441_HE [Indent level: 2],
        "_xx_rhs_mag_M441_HE": {
            "magazine": "rhs_mag_M441_HE",
            "count": 16
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_M714_white [Indent level: 2],
        "_xx_rhs_mag_M714_white": {
            "magazine": "rhs_mag_M714_white",
            "count": 4
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_M662_red [Indent level: 2],
        "_xx_rhs_mag_M662_red": {
            "magazine": "rhs_mag_M662_red",
            "count": 2
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 4
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 2
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 2
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 4
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|TransportItems [Indent level: 1],
    "TransportItems": {
        # Class: CfgVehicles|RHS_C130J_Base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 20
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 4
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_Toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|TransportWeapons [Indent level: 1],
    "TransportWeapons": {
        # Class: CfgVehicles|RHS_C130J_Base|TransportWeapons|_xx_rhs_weap_m4_carryhandle [Indent level: 2]
        "_xx_rhs_weap_m4_carryhandle": {
            "weapon": "rhs_weap_m4_carryhandle",
            "count": 2
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|TransportBackpacks [Indent level: 1],
    "TransportBackpacks": {
        # Class: CfgVehicles|RHS_C130J_Base|TransportBackpacks|_xx_B_Parachute [Indent level: 2]
        "_xx_B_Parachute": {
            "backpack": "B_Parachute",
            "count": 14
        }
    },
    "soundGetIn": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|close",0.316228,1],
    "soundGetOut": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|open",0.316228,1,40],
    "soundDammage": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|int-alarm_loop",0.562341,1],
    "soundEngineOnInt": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int_start_1",0.398107,1],
    "soundEngineOnExt": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext_start_1",0.398107,1,700],
    "soundEngineOffInt": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int_stop_1",0.398107,1],
    "soundEngineOffExt": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext_stop_1",0.398107,1,700],
    "soundIncommingMissile": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.1,1.5],
    # Class: CfgVehicles|RHS_C130J_Base|Sounds [Indent level: 1],
    "Sounds": {
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|EngineLowOut [Indent level: 2]
        "EngineLowOut": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext_engine_low",1.77828,1,900],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "camPos*engineOn*(rpm factor[0.85, 0])"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|EngineHighOut [Indent level: 2],
        "EngineHighOut": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext_engine_hi",1.77828,1,1100],
            "frequency": "1",
            "volume": "camPos*engineOn*(rpm factor[0.55, 1.0])"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|ForsageOut [Indent level: 2],
        "ForsageOut": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext_forsage_1",1.41254,1,1500],
            "frequency": "1",
            "volume": "camPos*engineOn*(thrust factor[0.5, 1.0])",
            "cone": [1.14,3.92,2,0.4]
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|WindNoiseOut [Indent level: 2],
        "WindNoiseOut": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext-wind1",0.001,0.6,150],
            "frequency": "(0.1+(1.2*(speed factor[1, 100])))",
            "volume": "camPos*(speed factor[1, 100])"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|EngineLowIn [Indent level: 2],
        "EngineLowIn": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int_engine_low",1,1],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.85, 0]))"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|EngineHighIn [Indent level: 2],
        "EngineHighIn": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int_engine_hi",1,1],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.55, 1.0]))"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|ForsageIn [Indent level: 2],
        "ForsageIn": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int_forsage_1",1.41254,1.1],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.5, 1.0]))"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|WindNoiseIn [Indent level: 2],
        "WindNoiseIn": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int-wind1",0.001,0.6],
            "frequency": "(0.1+(1.2*(speed factor[1, 100])))",
            "volume": "(1-camPos)*(speed factor[1, 100])"
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Left [Indent level: 2]
        "Left": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "brightness": 50,
            "useFlare": 1,
            "innerAngle": 5,
            "outerAngle": 75,
            "coneFadeCoef": 10,
            # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Left|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardLimitStart": 200,
                "hardLimitEnd": 250
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Right [Indent level: 2],
        "Right": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "size": 1,
            "brightness": 1,
            "useFlare": 1,
            "innerAngle": 5,
            "outerAngle": 75,
            "coneFadeCoef": 10,
            # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Right|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardLimitStart": 200,
                "hardLimitEnd": 250
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Left2 [Indent level: 2],
        "Left2": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "position": "L2 svetlo",
            "direction": "konec L2 svetla",
            "hitpoint": "L2 svetlo",
            "selection": "L2 svetlo",
            "size": 1,
            "brightness": 1,
            "useFlare": 1,
            "innerAngle": 5,
            "outerAngle": 75,
            "coneFadeCoef": 10,
            # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Left2|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardLimitStart": 200,
                "hardLimitEnd": 250
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Right2 [Indent level: 2],
        "Right2": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "position": "P2 svetlo",
            "direction": "konec P2 svetla",
            "hitpoint": "P2 svetlo",
            "selection": "P2 svetlo",
            "size": 1,
            "brightness": 1,
            "useFlare": 1,
            "innerAngle": 5,
            "outerAngle": 75,
            "coneFadeCoef": 10,
            # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Right2|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardLimitStart": 200,
                "hardLimitEnd": 250
            }
        }
    },
    "weapons": ["rhsusf_weap_ANAAQ24"],
    "magazines": ["rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM"],
    "threat": [0.1,0.5,0.8],
    "ejectSpeed": [0,0,0],
    "landingAoa": "rad 7",
    "landingSpeed": 200,
    "extCameraPosition": [0,5,-40],
    "gearUpTime": 4.5,
    "gearDownTime": 3,
    "driveOnComponent": [],
    "canFloat": "false",
    "waterResistanceCoef": 0.004,
    "waterLeakiness": 25,
    # Class: CfgVehicles|RHS_C130J_Base|AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|jumplight [Indent level: 2]
        "jumplight": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|cargolights_hide [Indent level: 2],
        "cargolights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|ramp [Indent level: 2],
        "ramp": {
            "source": "user",
            "initPhase": 0,
            "animPeriod": 5,
            "sound": "ServoRampSound_2",
            "soundPosition": "ramp_bottom_axis"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|hide_cargo [Indent level: 2],
        "hide_cargo": {
            "source": "user",
            "mass": -20,
            "displayName": "hide cargo benches",
            "animPeriod": 1e-005,
            "initPhase": 0,
            "onPhaseChanged": "for '_i' from 1 to 24 do {(_this select 0) lockCargo [_i,(_this select 1)==1]}"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|door_2_2 [Indent level: 2],
        "door_2_2": {
            "animPeriod": 4,
            "source": "door",
            "sound": "ServoRampSound_2",
            "soundPosition": "door_2_2_axis2",
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|door_2_1 [Indent level: 2],
        "door_2_1": {
            "soundPosition": "door_2_1_axis2",
            "animPeriod": 4,
            "source": "door",
            "sound": "ServoRampSound_2",
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|door_1 [Indent level: 2],
        "door_1": {
            "soundPosition": "Door_1_axis",
            "animPeriod": 4,
            "source": "door",
            "sound": "ServoRampSound_2",
            "initPhase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|CollisionLightRed_source [Indent level: 2],
        "CollisionLightRed_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionRed"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|CollisionLightWhite_source [Indent level: 2],
        "CollisionLightWhite_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionWhite"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Damper_1_1_source [Indent level: 2],
        "Damper_1_1_source": {
            "source": "damper",
            "wheel": "Wheel_1_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Damper_2_1_source [Indent level: 2],
        "Damper_2_1_source": {
            "source": "damper",
            "wheel": "Wheel_2_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Damper_2_2_source [Indent level: 2],
        "Damper_2_2_source": {
            "source": "damper",
            "wheel": "Wheel_2_2"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Damper_3_1_source [Indent level: 2],
        "Damper_3_1_source": {
            "source": "damper",
            "wheel": "Wheel_3_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Damper_3_2_source [Indent level: 2],
        "Damper_3_2_source": {
            "source": "damper",
            "wheel": "Wheel_3_2"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Wheel_1_1_source [Indent level: 2],
        "Wheel_1_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Wheel_2_1_source [Indent level: 2],
        "Wheel_2_1_source": {
            "source": "wheel",
            "wheel": "Wheel_2_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Wheel_2_2_source [Indent level: 2],
        "Wheel_2_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2_2"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Wheel_3_1_source [Indent level: 2],
        "Wheel_3_1_source": {
            "source": "wheel",
            "wheel": "Wheel_3_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Wheel_3_2_source [Indent level: 2],
        "Wheel_3_2_source": {
            "source": "wheel",
            "wheel": "Wheel_3_2"
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles|RHS_C130J_Base|UserActions|OpenRamp [Indent level: 2]
        "OpenRamp": {
            "displayName": "Open Cargo Ramp",
            "position": "pos_gunner",
            "onlyforplayer": 1,
            "showWindow": 0,
            "radius": 6,
            "condition": "(this animationSourcePhase 'ramp' <= 0.65) AND Alive(this)",
            "statement": "this animateSource ['ramp',1];{if(not(_x isKindOf 'Man'))then{detach _x}}foreach attachedObjects this",
            "shortcut": "user12"
        },
        # Class: CfgVehicles|RHS_C130J_Base|UserActions|LevelRamp [Indent level: 2],
        "LevelRamp": {
            "displayName": "Level Ramp",
            "condition": "this animationSourcePhase 'ramp' != 0.65 and (alive this)",
            "statement": "this animateSource ['ramp', 0.65];",
            "shortcut": "user13",
            "position": "pos_gunner",
            "onlyforplayer": 1,
            "showWindow": 0,
            "radius": 6
        },
        # Class: CfgVehicles|RHS_C130J_Base|UserActions|CloseRamp [Indent level: 2],
        "CloseRamp": {
            "displayName": "Close Cargo Ramp",
            "condition": "(this animationSourcePhase 'ramp' >= 0.65) AND Alive(this)",
            "statement": "this animateSource ['ramp',0];[this] call rhs_fnc_cargoAttach",
            "shortcut": "user12",
            "position": "pos_gunner",
            "onlyforplayer": 1,
            "showWindow": 0,
            "radius": 6
        },
        # Class: CfgVehicles|RHS_C130J_Base|UserActions|VehicleParadrop [Indent level: 2],
        "VehicleParadrop": {
            "displayName": "Paradrop cargo",
            "condition": "(count (attachedObjects this) > 0) AND ('man' countType (attachedObjects this) == 0) AND Alive(this)",
            "statement": "[this] spawn rhs_fnc_vehPara",
            "shortcut": "",
            "position": "pos_gunner",
            "onlyforplayer": 1,
            "showWindow": 0,
            "radius": 6
        },
        # Class: CfgVehicles|RHS_C130J_Base|UserActions|OpenMenu [Indent level: 2],
        "OpenMenu": {
            "userActionID": 74,
            "priority": 11.008,
            "displayName": "<t color='#FDDE00'>Open control panel</t>",
            "position": "pos_gunner",
            "radius": 10,
            "animPeriod": 2,
            "onlyForplayer": 1,
            "condition": "((call rhsusf_fnc_findPlayer) in this)",
            "statement": "[this] call rhs_fnc_c130j_openMenu"
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|MarkerLights [Indent level: 1],
    "MarkerLights": {
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionRed [Indent level: 2]
        "PositionRed": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 75,
            "name": "PositionLight_Red_1_pos",
            "drawLight": 1,
            "drawLightSize": 0.4,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 1,
            "useFlare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionGreen [Indent level: 2],
        "PositionGreen": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "PositionLight_Green_1_pos",
            "intensity": 75,
            "drawLight": 1,
            "drawLightSize": 0.4,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 1,
            "useFlare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionWhite [Indent level: 2],
        "PositionWhite": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "PositionLight_White_1_pos",
            "drawLightSize": 0.4,
            "intensity": 75,
            "drawLight": 1,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 1,
            "useFlare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionWhite2 [Indent level: 2],
        "PositionWhite2": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "PositionLight_White_2_pos",
            "drawLightSize": 0.4,
            "intensity": 75,
            "drawLight": 1,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 1,
            "useFlare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionWhite3 [Indent level: 2],
        "PositionWhite3": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "PositionLight_White_3_pos",
            "drawLightSize": 0.4,
            "intensity": 75,
            "drawLight": 1,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 1,
            "useFlare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionWhite4 [Indent level: 2],
        "PositionWhite4": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "PositionLight_White_4_pos",
            "drawLightSize": 0.4,
            "intensity": 75,
            "drawLight": 1,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 1,
            "useFlare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|CollisionRed [Indent level: 2],
        "CollisionRed": {
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "name": "CollisionLight_Red_1_pos",
            "blinking": 1,
            "blinkingPattern": [0.2,1.3],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.4,
            "drawLightCenterSize": 0.08,
            "intensity": 75,
            "drawLight": 1,
            "activeLight": 0,
            "dayLight": 1,
            "useFlare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|CollisionWhite [Indent level: 2],
        "CollisionWhite": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "CollisionLight_White_1_pos",
            "blinking": 1,
            "blinkingPattern": [0.1,0.9],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.4,
            "drawLightCenterSize": 0.04,
            "intensity": 75,
            "drawLight": 1,
            "activeLight": 0,
            "dayLight": 1,
            "useFlare": 0
        }
    },
    "armor": 50,
    # Class: CfgVehicles|RHS_C130J_Base|Hitpoints [Indent level: 1],
    "Hitpoints": {
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitHull [Indent level: 2]
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
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitAvionics [Indent level: 2],
        "HitAvionics": {
            "armor": 1,
            "explosionShielding": 0.6,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1 [Indent level: 2],
        "HitEngine_L1": {
            "armor": 0.5,
            "explosionShielding": 1.25,
            "passThrough": 0.01,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l1",
            "visual": "vis_engine_l",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2 [Indent level: 2],
        "HitEngine_L2": {
            "armor": 0.5,
            "explosionShielding": 1.25,
            "passThrough": 0.01,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l2",
            "visual": "vis_engine_2",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1 [Indent level: 2],
        "HitEngine_R1": {
            "armor": 0.5,
            "explosionShielding": 1.25,
            "passThrough": 0.01,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r1",
            "visual": "vis_engine_3",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2 [Indent level: 2],
        "HitEngine_R2": {
            "armor": 0.5,
            "explosionShielding": 1.25,
            "passThrough": 0.01,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r2",
            "visual": "vis_engine_4",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine [Indent level: 2],
        "HitEngine": {
            "armor": 999,
            "explosionShielding": 0.25,
            "passThrough": 0.01,
            "minimalHit": 0.01,
            "radius": 0.01,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_1",
            "depends": "(HitEngine_L1 + HitEngine_L1)*0.5"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine2 [Indent level: 2],
        "HitEngine2": {
            "armor": 999,
            "explosionShielding": 0.25,
            "passThrough": 0.01,
            "minimalHit": 0.01,
            "radius": 0.01,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_3",
            "depends": "(HitEngine_R1 + HitEngine_R1)*0.5"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitFuel [Indent level: 2],
        "HitFuel": {
            "armor": 0.3,
            "explosionShielding": 0.2,
            "passThrough": 0.01,
            "minimalHit": 0.05,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel_l",
            "visual": "vis_wing_l",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitFuel2 [Indent level: 2],
        "HitFuel2": {
            "armor": 0.3,
            "explosionShielding": 0.2,
            "passThrough": 0.01,
            "minimalHit": 0.05,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel_r",
            "visual": "vis_wing_r",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLAileron_link [Indent level: 2],
        "HitLAileron_link": {
            "armor": 0.3,
            "explosionShielding": 0.9,
            "passThrough": 0.01,
            "minimalHit": 0.03,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_l",
            "visual": "",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitRAileron_link [Indent level: 2],
        "HitRAileron_link": {
            "armor": 0.3,
            "explosionShielding": 0.9,
            "passThrough": 0.01,
            "minimalHit": 0.03,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_r",
            "visual": "",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLAileron [Indent level: 2],
        "HitLAileron": {
            "armor": 0.3,
            "explosionShielding": 1.6,
            "passThrough": 0.01,
            "minimalHit": 0.03,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "visual": "vis_wing_l",
            "depends": "HitLAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitRAileron [Indent level: 2],
        "HitRAileron": {
            "armor": 0.3,
            "explosionShielding": 1.6,
            "passThrough": 0.01,
            "minimalHit": 0.03,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "visual": "vis_wing_r",
            "depends": "HitRAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitControlRear [Indent level: 2],
        "HitControlRear": {
            "armor": 0.3,
            "explosionShielding": 0.1,
            "passThrough": 0.01,
            "minimalHit": 0.03,
            "radius": 0.17,
            "material": -1,
            "name": "hit_control_rear",
            "visual": "",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLCElevator [Indent level: 2],
        "HitLCElevator": {
            "armor": 0.3,
            "explosionShielding": 2,
            "passThrough": 0.01,
            "minimalHit": 0.03,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitRElevator [Indent level: 2],
        "HitRElevator": {
            "armor": 0.3,
            "explosionShielding": 2,
            "passThrough": 0.01,
            "minimalHit": 0.03,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLCRudder [Indent level: 2],
        "HitLCRudder": {
            "armor": 0.35,
            "explosionShielding": 2,
            "passThrough": 0.01,
            "minimalHit": 0.02,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder",
            "visual": "vis_rudder",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLFWheel [Indent level: 2],
        "HitLFWheel": {
            "armor": 1,
            "explosionShielding": 1,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "wheel_1_1",
            "visual": "wheel_1_1",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLF2Wheel [Indent level: 2],
        "HitLF2Wheel": {
            "armor": 1,
            "explosionShielding": 1,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "wheel_2_1",
            "visual": "wheel_2_1",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLRF2Wheel [Indent level: 2],
        "HitLRF2Wheel": {
            "armor": 1,
            "explosionShielding": 1,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "wheel_2_2",
            "visual": "wheel_2_2",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLBWheel [Indent level: 2],
        "HitLBWheel": {
            "armor": 1,
            "explosionShielding": 1,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "wheel_3_1",
            "visual": "wheel_3_1",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitRBWheel [Indent level: 2],
        "HitRBWheel": {
            "armor": 1,
            "explosionShielding": 1,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "wheel_3_2",
            "visual": "wheel_3_2",
            "depends": "0"
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|MFD [Indent level: 1],
    "MFD": {
        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD [Indent level: 2]
        "AirplaneHUD": {
            "borderLeft": 0.09,
            "borderRight": 0.02,
            "borderTop": 0.02,
            "borderBottom": 0.1,
            "helmetMountedDisplay": 0,
            "helmetPosition": [-0.025,0.025,0.1],
            "helmetRight": [0.05,0,0],
            "helmetDown": [0,-0.05,0],
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Pos10Vector [Indent level: 3],
            "Pos10Vector": {
                "type": "vector",
                "pos0": [0.5,0.3],
                "pos10": [0.9,0.75]
            },
            "topLeft": "HUD LH",
            "topRight": "HUD PH",
            "bottomLeft": "HUD LD",
            "color": [0,1,0,0.1],
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones [Indent level: 3],
            "Bones": {
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|PlaneW [Indent level: 4]
                "PlaneW": {
                    "type": "fixed",
                    "pos": [0.5,0.34]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|WeaponAim [Indent level: 4],
                "WeaponAim": {
                    "source": "weapon",
                    "type": "vector",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Target [Indent level: 4],
                "Target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],
                "Velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|ILS_H [Indent level: 4],
                "ILS_H": {
                    "type": "ils",
                    "pos0": [0.5,0.3],
                    "pos3": [0.62,0.3]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|ILS_W [Indent level: 4],
                "ILS_W": {
                    "pos3": [0.5,0.435],
                    "type": "ils",
                    "pos0": [0.5,0.3]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],
                "Level0": {
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP5 [Indent level: 4],
                "LevelP5": {
                    "angle": 5,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM5 [Indent level: 4],
                "LevelM5": {
                    "angle": -5,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP10 [Indent level: 4],
                "LevelP10": {
                    "angle": 10,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM10 [Indent level: 4],
                "LevelM10": {
                    "angle": -10,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP15 [Indent level: 4],
                "LevelP15": {
                    "angle": 15,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM15 [Indent level: 4],
                "LevelM15": {
                    "angle": -15,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP20 [Indent level: 4],
                "LevelP20": {
                    "angle": 20,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM20 [Indent level: 4],
                "LevelM20": {
                    "angle": -20,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP25 [Indent level: 4],
                "LevelP25": {
                    "angle": 25,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM25 [Indent level: 4],
                "LevelM25": {
                    "angle": -25,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP30 [Indent level: 4],
                "LevelP30": {
                    "angle": 30,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM30 [Indent level: 4],
                "LevelM30": {
                    "angle": -30,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP35 [Indent level: 4],
                "LevelP35": {
                    "angle": 35,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM35 [Indent level: 4],
                "LevelM35": {
                    "angle": -35,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP40 [Indent level: 4],
                "LevelP40": {
                    "angle": 40,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM40 [Indent level: 4],
                "LevelM40": {
                    "angle": -40,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP45 [Indent level: 4],
                "LevelP45": {
                    "angle": 45,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM45 [Indent level: 4],
                "LevelM45": {
                    "angle": -45,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP50 [Indent level: 4],
                "LevelP50": {
                    "angle": 50,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM50 [Indent level: 4],
                "LevelM50": {
                    "angle": -50,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw [Indent level: 3],
            "Draw": {
                "alpha": 0.95,
                "color": [0,0.3,0.05],
                "condition": "on",
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|PlaneW [Indent level: 4],
                "PlaneW": {
                    "clipTL": [0,1],
                    "clipBR": [1,0],
                    "type": "line",
                    "points": [["PlaneW",[-0.08,0],1],["PlaneW",[-0.03,0],1],["PlaneW",[-0.015,0.03375],1],["PlaneW",[0,0],1],["PlaneW",[0.015,0.03375],1],["PlaneW",[0.03,0],1],["PlaneW",[0.08,0],1]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|PlaneHeading [Indent level: 4],
                "PlaneHeading": {
                    "clipTL": [0,1],
                    "clipBR": [1,0],
                    "type": "line",
                    "points": [["Velocity",[0,-0.0225],1],["Velocity",[0.014,-0.01575],1],["Velocity",[0.02,0],1],["Velocity",[0.014,0.01575],1],["Velocity",[0,0.0225],1],["Velocity",[-0.014,0.01575],1],["Velocity",[-0.02,0],1],["Velocity",[-0.014,-0.01575],1],["Velocity",[0,-0.0225],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.045],1],["Velocity",[0,-0.0225],1],[]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Static [Indent level: 4],
                "Static": {
                    "clipTL": [0,0.1],
                    "clipBR": [1,0],
                    "type": "line",
                    "points": [[[0.21,0.52],1],[[0.19,0.5],1],[[0.21,0.48],1],[],[[0.18,0.2],1],[[0.18,0.85],1],[],[[0.79,0.52],1],[[0.81,0.5],1],[[0.79,0.48],1],[],[[0.82,0.2],1],[[0.82,0.85],1],[],[[0.52,0.09],1],[[0.5,0.07],1],[[0.48,0.09],1],[],[[0.2,0.065],1],[[0.8,0.065],1],[]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont [Indent level: 4],
                "Horizont": {
                    "clipTL": [0,0],
                    "clipBR": [1,1],
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed [Indent level: 5],
                    "Dimmed": {
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "Level0": {
                            "type": "line",
                            "points": [["Level0",[-0.2,0],1],["Level0",[-0.05,0],1],[],["Level0",[0.05,0],1],["Level0",[0.2,0],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_0 [Indent level: 6],
                        "VALM_1_0": {
                            "type": "text",
                            "source": "static",
                            "text": 0,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[-0.23,-0.025],1],
                            "right": ["Level0",[-0.13,-0.025],1],
                            "down": ["Level0",[-0.23,0.025],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_0 [Indent level: 6],
                        "VALM_2_0": {
                            "align": "right",
                            "pos": ["Level0",[0.22,-0.025],1],
                            "right": ["Level0",[0.32,-0.025],1],
                            "down": ["Level0",[0.22,0.025],1],
                            "type": "text",
                            "source": "static",
                            "text": 0,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM5 [Indent level: 6],
                        "LevelM5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.2,-0.03],1],["LevelM5",[-0.2,0],1],["LevelM5",[-0.15,0],1],[],["LevelM5",[-0.1,0],1],["LevelM5",[-0.05,0],1],[],["LevelM5",[0.05,0],1],["LevelM5",[0.1,0],1],[],["LevelM5",[0.15,0],1],["LevelM5",[0.2,0],1],["LevelM5",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_5 [Indent level: 6],
                        "VALM_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM5",[-0.23,-0.085],1],
                            "right": ["LevelM5",[-0.13,-0.085],1],
                            "down": ["LevelM5",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_5 [Indent level: 6],
                        "VALM_2_5": {
                            "align": "right",
                            "pos": ["LevelM5",[0.22,-0.085],1],
                            "right": ["LevelM5",[0.32,-0.085],1],
                            "down": ["LevelM5",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP5 [Indent level: 6],
                        "LevelP5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.2,0.03],1],["LevelP5",[-0.2,0],1],["LevelP5",[-0.05,0],1],[],["LevelP5",[0.05,0],1],["LevelP5",[0.2,0],1],["LevelP5",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_5 [Indent level: 6],
                        "VALP_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP5",[-0.23,0.035],1],
                            "right": ["LevelP5",[-0.13,0.035],1],
                            "down": ["LevelP5",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_5 [Indent level: 6],
                        "VALP_2_5": {
                            "align": "right",
                            "pos": ["LevelP5",[0.22,0.035],1],
                            "right": ["LevelP5",[0.32,0.035],1],
                            "down": ["LevelP5",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM10 [Indent level: 6],
                        "LevelM10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.2,-0.03],1],["LevelM10",[-0.2,0],1],["LevelM10",[-0.15,0],1],[],["LevelM10",[-0.1,0],1],["LevelM10",[-0.05,0],1],[],["LevelM10",[0.05,0],1],["LevelM10",[0.1,0],1],[],["LevelM10",[0.15,0],1],["LevelM10",[0.2,0],1],["LevelM10",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_10 [Indent level: 6],
                        "VALM_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM10",[-0.23,-0.085],1],
                            "right": ["LevelM10",[-0.13,-0.085],1],
                            "down": ["LevelM10",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_10 [Indent level: 6],
                        "VALM_2_10": {
                            "align": "right",
                            "pos": ["LevelM10",[0.22,-0.085],1],
                            "right": ["LevelM10",[0.32,-0.085],1],
                            "down": ["LevelM10",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP10 [Indent level: 6],
                        "LevelP10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.2,0.03],1],["LevelP10",[-0.2,0],1],["LevelP10",[-0.05,0],1],[],["LevelP10",[0.05,0],1],["LevelP10",[0.2,0],1],["LevelP10",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_10 [Indent level: 6],
                        "VALP_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP10",[-0.23,0.035],1],
                            "right": ["LevelP10",[-0.13,0.035],1],
                            "down": ["LevelP10",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_10 [Indent level: 6],
                        "VALP_2_10": {
                            "align": "right",
                            "pos": ["LevelP10",[0.22,0.035],1],
                            "right": ["LevelP10",[0.32,0.035],1],
                            "down": ["LevelP10",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM15 [Indent level: 6],
                        "LevelM15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.2,-0.03],1],["LevelM15",[-0.2,0],1],["LevelM15",[-0.15,0],1],[],["LevelM15",[-0.1,0],1],["LevelM15",[-0.05,0],1],[],["LevelM15",[0.05,0],1],["LevelM15",[0.1,0],1],[],["LevelM15",[0.15,0],1],["LevelM15",[0.2,0],1],["LevelM15",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_15 [Indent level: 6],
                        "VALM_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM15",[-0.23,-0.085],1],
                            "right": ["LevelM15",[-0.13,-0.085],1],
                            "down": ["LevelM15",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_15 [Indent level: 6],
                        "VALM_2_15": {
                            "align": "right",
                            "pos": ["LevelM15",[0.22,-0.085],1],
                            "right": ["LevelM15",[0.32,-0.085],1],
                            "down": ["LevelM15",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP15 [Indent level: 6],
                        "LevelP15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.2,0.03],1],["LevelP15",[-0.2,0],1],["LevelP15",[-0.05,0],1],[],["LevelP15",[0.05,0],1],["LevelP15",[0.2,0],1],["LevelP15",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_15 [Indent level: 6],
                        "VALP_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP15",[-0.23,0.035],1],
                            "right": ["LevelP15",[-0.13,0.035],1],
                            "down": ["LevelP15",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_15 [Indent level: 6],
                        "VALP_2_15": {
                            "align": "right",
                            "pos": ["LevelP15",[0.22,0.035],1],
                            "right": ["LevelP15",[0.32,0.035],1],
                            "down": ["LevelP15",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM20 [Indent level: 6],
                        "LevelM20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.2,-0.03],1],["LevelM20",[-0.2,0],1],["LevelM20",[-0.15,0],1],[],["LevelM20",[-0.1,0],1],["LevelM20",[-0.05,0],1],[],["LevelM20",[0.05,0],1],["LevelM20",[0.1,0],1],[],["LevelM20",[0.15,0],1],["LevelM20",[0.2,0],1],["LevelM20",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_20 [Indent level: 6],
                        "VALM_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM20",[-0.23,-0.085],1],
                            "right": ["LevelM20",[-0.13,-0.085],1],
                            "down": ["LevelM20",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_20 [Indent level: 6],
                        "VALM_2_20": {
                            "align": "right",
                            "pos": ["LevelM20",[0.22,-0.085],1],
                            "right": ["LevelM20",[0.32,-0.085],1],
                            "down": ["LevelM20",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP20 [Indent level: 6],
                        "LevelP20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.2,0.03],1],["LevelP20",[-0.2,0],1],["LevelP20",[-0.05,0],1],[],["LevelP20",[0.05,0],1],["LevelP20",[0.2,0],1],["LevelP20",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_20 [Indent level: 6],
                        "VALP_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP20",[-0.23,0.035],1],
                            "right": ["LevelP20",[-0.13,0.035],1],
                            "down": ["LevelP20",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_20 [Indent level: 6],
                        "VALP_2_20": {
                            "align": "right",
                            "pos": ["LevelP20",[0.22,0.035],1],
                            "right": ["LevelP20",[0.32,0.035],1],
                            "down": ["LevelP20",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM25 [Indent level: 6],
                        "LevelM25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.2,-0.03],1],["LevelM25",[-0.2,0],1],["LevelM25",[-0.15,0],1],[],["LevelM25",[-0.1,0],1],["LevelM25",[-0.05,0],1],[],["LevelM25",[0.05,0],1],["LevelM25",[0.1,0],1],[],["LevelM25",[0.15,0],1],["LevelM25",[0.2,0],1],["LevelM25",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_25 [Indent level: 6],
                        "VALM_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM25",[-0.23,-0.085],1],
                            "right": ["LevelM25",[-0.13,-0.085],1],
                            "down": ["LevelM25",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_25 [Indent level: 6],
                        "VALM_2_25": {
                            "align": "right",
                            "pos": ["LevelM25",[0.22,-0.085],1],
                            "right": ["LevelM25",[0.32,-0.085],1],
                            "down": ["LevelM25",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP25 [Indent level: 6],
                        "LevelP25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.2,0.03],1],["LevelP25",[-0.2,0],1],["LevelP25",[-0.05,0],1],[],["LevelP25",[0.05,0],1],["LevelP25",[0.2,0],1],["LevelP25",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_25 [Indent level: 6],
                        "VALP_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP25",[-0.23,0.035],1],
                            "right": ["LevelP25",[-0.13,0.035],1],
                            "down": ["LevelP25",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_25 [Indent level: 6],
                        "VALP_2_25": {
                            "align": "right",
                            "pos": ["LevelP25",[0.22,0.035],1],
                            "right": ["LevelP25",[0.32,0.035],1],
                            "down": ["LevelP25",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM30 [Indent level: 6],
                        "LevelM30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.2,-0.03],1],["LevelM30",[-0.2,0],1],["LevelM30",[-0.15,0],1],[],["LevelM30",[-0.1,0],1],["LevelM30",[-0.05,0],1],[],["LevelM30",[0.05,0],1],["LevelM30",[0.1,0],1],[],["LevelM30",[0.15,0],1],["LevelM30",[0.2,0],1],["LevelM30",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_30 [Indent level: 6],
                        "VALM_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM30",[-0.23,-0.085],1],
                            "right": ["LevelM30",[-0.13,-0.085],1],
                            "down": ["LevelM30",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_30 [Indent level: 6],
                        "VALM_2_30": {
                            "align": "right",
                            "pos": ["LevelM30",[0.22,-0.085],1],
                            "right": ["LevelM30",[0.32,-0.085],1],
                            "down": ["LevelM30",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP30 [Indent level: 6],
                        "LevelP30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.2,0.03],1],["LevelP30",[-0.2,0],1],["LevelP30",[-0.05,0],1],[],["LevelP30",[0.05,0],1],["LevelP30",[0.2,0],1],["LevelP30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_30 [Indent level: 6],
                        "VALP_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP30",[-0.23,0.035],1],
                            "right": ["LevelP30",[-0.13,0.035],1],
                            "down": ["LevelP30",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_30 [Indent level: 6],
                        "VALP_2_30": {
                            "align": "right",
                            "pos": ["LevelP30",[0.22,0.035],1],
                            "right": ["LevelP30",[0.32,0.035],1],
                            "down": ["LevelP30",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM35 [Indent level: 6],
                        "LevelM35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.2,-0.03],1],["LevelM35",[-0.2,0],1],["LevelM35",[-0.15,0],1],[],["LevelM35",[-0.1,0],1],["LevelM35",[-0.05,0],1],[],["LevelM35",[0.05,0],1],["LevelM35",[0.1,0],1],[],["LevelM35",[0.15,0],1],["LevelM35",[0.2,0],1],["LevelM35",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_35 [Indent level: 6],
                        "VALM_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM35",[-0.23,-0.085],1],
                            "right": ["LevelM35",[-0.13,-0.085],1],
                            "down": ["LevelM35",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_35 [Indent level: 6],
                        "VALM_2_35": {
                            "align": "right",
                            "pos": ["LevelM35",[0.22,-0.085],1],
                            "right": ["LevelM35",[0.32,-0.085],1],
                            "down": ["LevelM35",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP35 [Indent level: 6],
                        "LevelP35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.2,0.03],1],["LevelP35",[-0.2,0],1],["LevelP35",[-0.05,0],1],[],["LevelP35",[0.05,0],1],["LevelP35",[0.2,0],1],["LevelP35",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_35 [Indent level: 6],
                        "VALP_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP35",[-0.23,0.035],1],
                            "right": ["LevelP35",[-0.13,0.035],1],
                            "down": ["LevelP35",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_35 [Indent level: 6],
                        "VALP_2_35": {
                            "align": "right",
                            "pos": ["LevelP35",[0.22,0.035],1],
                            "right": ["LevelP35",[0.32,0.035],1],
                            "down": ["LevelP35",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM40 [Indent level: 6],
                        "LevelM40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.2,-0.03],1],["LevelM40",[-0.2,0],1],["LevelM40",[-0.15,0],1],[],["LevelM40",[-0.1,0],1],["LevelM40",[-0.05,0],1],[],["LevelM40",[0.05,0],1],["LevelM40",[0.1,0],1],[],["LevelM40",[0.15,0],1],["LevelM40",[0.2,0],1],["LevelM40",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_40 [Indent level: 6],
                        "VALM_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM40",[-0.23,-0.085],1],
                            "right": ["LevelM40",[-0.13,-0.085],1],
                            "down": ["LevelM40",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_40 [Indent level: 6],
                        "VALM_2_40": {
                            "align": "right",
                            "pos": ["LevelM40",[0.22,-0.085],1],
                            "right": ["LevelM40",[0.32,-0.085],1],
                            "down": ["LevelM40",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP40 [Indent level: 6],
                        "LevelP40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.2,0.03],1],["LevelP40",[-0.2,0],1],["LevelP40",[-0.05,0],1],[],["LevelP40",[0.05,0],1],["LevelP40",[0.2,0],1],["LevelP40",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_40 [Indent level: 6],
                        "VALP_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP40",[-0.23,0.035],1],
                            "right": ["LevelP40",[-0.13,0.035],1],
                            "down": ["LevelP40",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_40 [Indent level: 6],
                        "VALP_2_40": {
                            "align": "right",
                            "pos": ["LevelP40",[0.22,0.035],1],
                            "right": ["LevelP40",[0.32,0.035],1],
                            "down": ["LevelP40",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM45 [Indent level: 6],
                        "LevelM45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.2,-0.03],1],["LevelM45",[-0.2,0],1],["LevelM45",[-0.15,0],1],[],["LevelM45",[-0.1,0],1],["LevelM45",[-0.05,0],1],[],["LevelM45",[0.05,0],1],["LevelM45",[0.1,0],1],[],["LevelM45",[0.15,0],1],["LevelM45",[0.2,0],1],["LevelM45",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_45 [Indent level: 6],
                        "VALM_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM45",[-0.23,-0.085],1],
                            "right": ["LevelM45",[-0.13,-0.085],1],
                            "down": ["LevelM45",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_45 [Indent level: 6],
                        "VALM_2_45": {
                            "align": "right",
                            "pos": ["LevelM45",[0.22,-0.085],1],
                            "right": ["LevelM45",[0.32,-0.085],1],
                            "down": ["LevelM45",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP45 [Indent level: 6],
                        "LevelP45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.2,0.03],1],["LevelP45",[-0.2,0],1],["LevelP45",[-0.05,0],1],[],["LevelP45",[0.05,0],1],["LevelP45",[0.2,0],1],["LevelP45",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_45 [Indent level: 6],
                        "VALP_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP45",[-0.23,0.035],1],
                            "right": ["LevelP45",[-0.13,0.035],1],
                            "down": ["LevelP45",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_45 [Indent level: 6],
                        "VALP_2_45": {
                            "align": "right",
                            "pos": ["LevelP45",[0.22,0.035],1],
                            "right": ["LevelP45",[0.32,0.035],1],
                            "down": ["LevelP45",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM50 [Indent level: 6],
                        "LevelM50": {
                            "type": "line",
                            "points": [["LevelM50",[-0.2,-0.03],1],["LevelM50",[-0.2,0],1],["LevelM50",[-0.15,0],1],[],["LevelM50",[-0.1,0],1],["LevelM50",[-0.05,0],1],[],["LevelM50",[0.05,0],1],["LevelM50",[0.1,0],1],[],["LevelM50",[0.15,0],1],["LevelM50",[0.2,0],1],["LevelM50",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_50 [Indent level: 6],
                        "VALM_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM50",[-0.23,-0.085],1],
                            "right": ["LevelM50",[-0.13,-0.085],1],
                            "down": ["LevelM50",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_50 [Indent level: 6],
                        "VALM_2_50": {
                            "align": "right",
                            "pos": ["LevelM50",[0.22,-0.085],1],
                            "right": ["LevelM50",[0.32,-0.085],1],
                            "down": ["LevelM50",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP50 [Indent level: 6],
                        "LevelP50": {
                            "type": "line",
                            "points": [["LevelP50",[-0.2,0.03],1],["LevelP50",[-0.2,0],1],["LevelP50",[-0.05,0],1],[],["LevelP50",[0.05,0],1],["LevelP50",[0.2,0],1],["LevelP50",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_50 [Indent level: 6],
                        "VALP_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP50",[-0.23,0.035],1],
                            "right": ["LevelP50",[-0.13,0.035],1],
                            "down": ["LevelP50",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_50 [Indent level: 6],
                        "VALP_2_50": {
                            "align": "right",
                            "pos": ["LevelP50",[0.22,0.035],1],
                            "right": ["LevelP50",[0.32,0.035],1],
                            "down": ["LevelP50",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "scale": 1,
                            "sourceScale": 1
                        }
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|MGun [Indent level: 4],
                "MGun": {
                    "condition": "mgun",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|MGun|Circle [Indent level: 5],
                    "Circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0.01,0],1],["WeaponAim",[-0.01,0],1],[],["WeaponAim",[0,0.01125],1],["WeaponAim",[0,-0.01125],1],[],["WeaponAim",[0,-0.07875],1],["WeaponAim",[0.049,-0.055125],1],["WeaponAim",[0.07,0],1],["WeaponAim",[0.049,0.055125],1],["WeaponAim",[0,0.07875],1],["WeaponAim",[-0.049,0.055125],1],["WeaponAim",[-0.07,0],1],["WeaponAim",[-0.049,-0.055125],1],["WeaponAim",[0,-0.07875],1],[],["WeaponAim",[0,-0.1575],1],["WeaponAim",[0.07,-0.137025],1],["WeaponAim",[0.1218,-0.07875],1],["WeaponAim",[0.14,0],1],["WeaponAim",[0.1218,0.07875],1],["WeaponAim",[0.07,0.137025],1],["WeaponAim",[0,0.1575],1],["WeaponAim",[-0.07,0.137025],1],["WeaponAim",[-0.1218,0.07875],1],["WeaponAim",[-0.14,0],1],["WeaponAim",[-0.1218,-0.07875],1],["WeaponAim",[-0.07,-0.137025],1],["WeaponAim",[0,-0.1575],1],[],["WeaponAim",[0,-0.1575],1],["WeaponAim",[0,-0.18],1],[],["WeaponAim",[-0.07,-0.136399],1],["WeaponAim",[-0.08,-0.155885],1],[],["WeaponAim",[-0.121244,-0.07875],1],["WeaponAim",[-0.138564,-0.09],1],[],["WeaponAim",[-0.14,6.88454e-009],1],["WeaponAim",[-0.16,7.86805e-009],1],[],["WeaponAim",[-0.121244,0.07875],1],["WeaponAim",[-0.138564,0.09],1],[],["WeaponAim",[-0.07,0.136399],1],["WeaponAim",[-0.08,0.155885],1],[],["WeaponAim",[1.22392e-008,0.1575],1],["WeaponAim",[1.39876e-008,0.18],1],[],["WeaponAim",[0.07,0.136399],1],["WeaponAim",[0.08,0.155885],1],[],["WeaponAim",[0.121244,0.07875],1],["WeaponAim",[0.138564,0.09],1],[],["WeaponAim",[0.14,-1.87817e-009],1],["WeaponAim",[0.16,-2.14648e-009],1],[],["WeaponAim",[0.121244,-0.07875],1],["WeaponAim",[0.138564,-0.09],1],[],["WeaponAim",[0.07,-0.136399],1],["WeaponAim",[0.08,-0.155885],1],[]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Bomb [Indent level: 4],
                "Bomb": {
                    "condition": "bomb",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Bomb|Circle [Indent level: 5],
                    "Circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.1125],1],["WeaponAim",[0.05,-0.097875],1],["WeaponAim",[0.087,-0.05625],1],["WeaponAim",[0.1,0],1],["WeaponAim",[0.087,0.05625],1],["WeaponAim",[0.05,0.097875],1],["WeaponAim",[0,0.1125],1],["WeaponAim",[-0.05,0.097875],1],["WeaponAim",[-0.087,0.05625],1],["WeaponAim",[-0.1,0],1],["WeaponAim",[-0.087,-0.05625],1],["WeaponAim",[-0.05,-0.097875],1],["WeaponAim",[0,-0.1125],1],[],["Velocity",0.001,"WeaponAim",[0,0],1],["Velocity",[0,0],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AAMissile [Indent level: 4],
                "AAMissile": {
                    "condition": "AAmissile",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AAMissile|Circle [Indent level: 5],
                    "Circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.28125],1],["WeaponAim",[0.125,-0.244687],1],["WeaponAim",[0.2175,-0.140625],1],["WeaponAim",[0.25,0],1],["WeaponAim",[0.2175,0.140625],1],["WeaponAim",[0.125,0.244687],1],["WeaponAim",[0,0.28125],1],["WeaponAim",[-0.125,0.244687],1],["WeaponAim",[-0.2175,0.140625],1],["WeaponAim",[-0.25,0],1],["WeaponAim",[-0.2175,-0.140625],1],["WeaponAim",[-0.125,-0.244687],1],["WeaponAim",[0,-0.28125],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ATMissile [Indent level: 4],
                "ATMissile": {
                    "condition": "ATmissile",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ATMissile|Circle [Indent level: 5],
                    "Circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.2025],1],["WeaponAim",[0.09,-0.176175],1],["WeaponAim",[0.1566,-0.10125],1],["WeaponAim",[0.18,0],1],["WeaponAim",[0.1566,0.10125],1],["WeaponAim",[0.09,0.176175],1],["WeaponAim",[0,0.2025],1],["WeaponAim",[-0.09,0.176175],1],["WeaponAim",[-0.1566,0.10125],1],["WeaponAim",[-0.18,0],1],["WeaponAim",[-0.1566,-0.10125],1],["WeaponAim",[-0.09,-0.176175],1],["WeaponAim",[0,-0.2025],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Rockets [Indent level: 4],
                "Rockets": {
                    "condition": "Rocket",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Rockets|Circle [Indent level: 5],
                    "Circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0.01,0],1],["WeaponAim",[-0.01,0],1],[],["WeaponAim",[0,0.01125],1],["WeaponAim",[0,-0.01125],1],[],["WeaponAim",[0,-0.135],1],["WeaponAim",[0.06,-0.11745],1],["WeaponAim",[0.1044,-0.0675],1],["WeaponAim",[0.12,0],1],["WeaponAim",[0.1044,0.0675],1],["WeaponAim",[0.06,0.11745],1],["WeaponAim",[0,0.135],1],["WeaponAim",[-0.06,0.11745],1],["WeaponAim",[-0.1044,0.0675],1],["WeaponAim",[-0.12,0],1],["WeaponAim",[-0.1044,-0.0675],1],["WeaponAim",[-0.06,-0.11745],1],["WeaponAim",[0,-0.135],1],[]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AltScale [Indent level: 4],
                "AltScale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "altitudeASL",
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [0.86,0.82],
                    "right": [0.94,0.82],
                    "down": [0.86,0.87],
                    "lineXleft": 0.825,
                    "lineYright": 0.835,
                    "lineXleftMajor": 0.825,
                    "lineYrightMajor": 0.845,
                    "bottom": 0.2,
                    "top": 0.85,
                    "center": 0.5,
                    "step": 20,
                    "StepSize": 0.0325,
                    "horizontal": "false",
                    "min": "none",
                    "max": "none",
                    "numberEach": 5,
                    "majorLineEach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|SpeedScale [Indent level: 4],
                "SpeedScale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "speed",
                    "sourceScale": 3.6,
                    "align": "right",
                    "pos": [0.06,0.17],
                    "right": [0.14,0.17],
                    "down": [0.06,0.22],
                    "lineXleft": 0.175,
                    "lineYright": 0.165,
                    "lineXleftMajor": 0.175,
                    "lineYrightMajor": 0.155,
                    "bottom": 0.85,
                    "center": 0.5,
                    "top": 0.2,
                    "step": 20,
                    "StepSize": 0.0325,
                    "horizontal": "false",
                    "min": "none",
                    "max": "none",
                    "numberEach": 5,
                    "majorLineEach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Gear [Indent level: 4],
                "Gear": {
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Gear|text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "GEAR",
                        "align": "right",
                        "scale": 0.5,
                        "sourceScale": 1,
                        "pos": [[0.84,0.88],1],
                        "right": [[0.9,0.88],1],
                        "down": [[0.84,0.92],1]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Flaps [Indent level: 4],
                "Flaps": {
                    "condition": "flaps",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Flaps|text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "FLAPS",
                        "align": "right",
                        "scale": 0.5,
                        "sourceScale": 1,
                        "pos": [[0.84,0.93],1],
                        "right": [[0.9,0.93],1],
                        "down": [[0.84,0.97],1]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|weapons [Indent level: 4],
                "weapons": {
                    "type": "text",
                    "source": "weapon",
                    "align": "right",
                    "scale": 0.5,
                    "sourceScale": 1,
                    "pos": [[0.1,0.88],1],
                    "right": [[0.16,0.88],1],
                    "down": [[0.1,0.92],1]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ammo [Indent level: 4],
                "ammo": {
                    "type": "text",
                    "source": "ammo",
                    "align": "right",
                    "scale": 0.5,
                    "sourceScale": 1,
                    "pos": [[0.1,0.93],1],
                    "right": [[0.16,0.93],1],
                    "down": [[0.1,0.97],1]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|VspeedNumber [Indent level: 4],
                "VspeedNumber": {
                    "type": "text",
                    "align": "right",
                    "scale": 1,
                    "source": "vspeed",
                    "sourceScale": 1,
                    "pos": [[0.86,0.12],1],
                    "right": [[0.94,0.12],1],
                    "down": [[0.86,0.17],1]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],
                "HeadingScale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "Heading",
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [0.2,0],
                    "right": [0.28,0],
                    "down": [0.2,0.05],
                    "lineXleft": 0.06,
                    "lineYright": 0.05,
                    "lineXleftMajor": 0.06,
                    "lineYrightMajor": 0.04,
                    "bottom": 0.8,
                    "center": 0.5,
                    "top": 0.2,
                    "step": 2,
                    "StepSize": 0.03,
                    "horizontal": "true",
                    "min": "none",
                    "max": "none",
                    "numberEach": 5,
                    "majorLineEach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS [Indent level: 4],
                "ILS": {
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS|Glideslope [Indent level: 5],
                    "Glideslope": {
                        "clipTL": [0,0],
                        "clipBR": [1,1],
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 6],
                        "ILS": {
                            "type": "line",
                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[0,0.027],1],["ILS_W",[0,-0.027],1],[],["ILS_W",[0.12,0.027],1],["ILS_W",[0.12,-0.027],1],[],["ILS_W",[0.24,0.027],1],["ILS_W",[0.24,-0.027],1],[],["ILS_W",[-0.12,0.027],1],["ILS_W",[-0.12,-0.027],1],[],["ILS_W",[-0.24,0.027],1],["ILS_W",[-0.24,-0.027],1],[],["ILS_H",[0,-0.27],1],["ILS_H",[0,0.27],1],[],["ILS_H",[0.024,0],1],["ILS_H",[-0.024,0],1],[],["ILS_H",[0.024,0.135],1],["ILS_H",[-0.024,0.135],1],[],["ILS_H",[0.024,0.27],1],["ILS_H",[-0.024,0.27],1],[],["ILS_H",[0.024,-0.135],1],["ILS_H",[-0.024,-0.135],1],[],["ILS_H",[0.024,-0.27],1],["ILS_H",[-0.024,-0.27],1]]
                        }
                    }
                }
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD2 [Indent level: 2],
        "AirplaneHUD2": {
            "topLeft": "HUD2 LH",
            "topRight": "HUD2 PH",
            "bottomLeft": "HUD2 LD",
            "bottomRight": "HUD2 PD",
            "borderLeft": 0.09,
            "borderRight": 0.02,
            "borderTop": 0.02,
            "borderBottom": 0.1,
            "helmetMountedDisplay": 0,
            "helmetPosition": [-0.025,0.025,0.1],
            "helmetRight": [0.05,0,0],
            "helmetDown": [0,-0.05,0],
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Pos10Vector [Indent level: 3],
            "Pos10Vector": {
                "type": "vector",
                "pos0": [0.5,0.3],
                "pos10": [0.9,0.75]
            },
            "color": [0,1,0,0.1],
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones [Indent level: 3],
            "Bones": {
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|PlaneW [Indent level: 4]
                "PlaneW": {
                    "type": "fixed",
                    "pos": [0.5,0.34]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|WeaponAim [Indent level: 4],
                "WeaponAim": {
                    "source": "weapon",
                    "type": "vector",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Target [Indent level: 4],
                "Target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],
                "Velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|ILS_H [Indent level: 4],
                "ILS_H": {
                    "type": "ils",
                    "pos0": [0.5,0.3],
                    "pos3": [0.62,0.3]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|ILS_W [Indent level: 4],
                "ILS_W": {
                    "pos3": [0.5,0.435],
                    "type": "ils",
                    "pos0": [0.5,0.3]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],
                "Level0": {
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP5 [Indent level: 4],
                "LevelP5": {
                    "angle": 5,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM5 [Indent level: 4],
                "LevelM5": {
                    "angle": -5,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP10 [Indent level: 4],
                "LevelP10": {
                    "angle": 10,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM10 [Indent level: 4],
                "LevelM10": {
                    "angle": -10,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP15 [Indent level: 4],
                "LevelP15": {
                    "angle": 15,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM15 [Indent level: 4],
                "LevelM15": {
                    "angle": -15,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP20 [Indent level: 4],
                "LevelP20": {
                    "angle": 20,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM20 [Indent level: 4],
                "LevelM20": {
                    "angle": -20,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP25 [Indent level: 4],
                "LevelP25": {
                    "angle": 25,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM25 [Indent level: 4],
                "LevelM25": {
                    "angle": -25,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP30 [Indent level: 4],
                "LevelP30": {
                    "angle": 30,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM30 [Indent level: 4],
                "LevelM30": {
                    "angle": -30,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP35 [Indent level: 4],
                "LevelP35": {
                    "angle": 35,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM35 [Indent level: 4],
                "LevelM35": {
                    "angle": -35,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP40 [Indent level: 4],
                "LevelP40": {
                    "angle": 40,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM40 [Indent level: 4],
                "LevelM40": {
                    "angle": -40,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP45 [Indent level: 4],
                "LevelP45": {
                    "angle": 45,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM45 [Indent level: 4],
                "LevelM45": {
                    "angle": -45,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP50 [Indent level: 4],
                "LevelP50": {
                    "angle": 50,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM50 [Indent level: 4],
                "LevelM50": {
                    "angle": -50,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw [Indent level: 3],
            "Draw": {
                "alpha": 0.95,
                "color": [0,0.3,0.05],
                "condition": "on",
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|PlaneW [Indent level: 4],
                "PlaneW": {
                    "clipTL": [0,1],
                    "clipBR": [1,0],
                    "type": "line",
                    "points": [["PlaneW",[-0.08,0],1],["PlaneW",[-0.03,0],1],["PlaneW",[-0.015,0.03375],1],["PlaneW",[0,0],1],["PlaneW",[0.015,0.03375],1],["PlaneW",[0.03,0],1],["PlaneW",[0.08,0],1]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|PlaneHeading [Indent level: 4],
                "PlaneHeading": {
                    "clipTL": [0,1],
                    "clipBR": [1,0],
                    "type": "line",
                    "points": [["Velocity",[0,-0.0225],1],["Velocity",[0.014,-0.01575],1],["Velocity",[0.02,0],1],["Velocity",[0.014,0.01575],1],["Velocity",[0,0.0225],1],["Velocity",[-0.014,0.01575],1],["Velocity",[-0.02,0],1],["Velocity",[-0.014,-0.01575],1],["Velocity",[0,-0.0225],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.045],1],["Velocity",[0,-0.0225],1],[]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Static [Indent level: 4],
                "Static": {
                    "clipTL": [0,0.1],
                    "clipBR": [1,0],
                    "type": "line",
                    "points": [[[0.21,0.52],1],[[0.19,0.5],1],[[0.21,0.48],1],[],[[0.18,0.2],1],[[0.18,0.85],1],[],[[0.79,0.52],1],[[0.81,0.5],1],[[0.79,0.48],1],[],[[0.82,0.2],1],[[0.82,0.85],1],[],[[0.52,0.09],1],[[0.5,0.07],1],[[0.48,0.09],1],[],[[0.2,0.065],1],[[0.8,0.065],1],[]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont [Indent level: 4],
                "Horizont": {
                    "clipTL": [0,0],
                    "clipBR": [1,1],
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed [Indent level: 5],
                    "Dimmed": {
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "Level0": {
                            "type": "line",
                            "points": [["Level0",[-0.2,0],1],["Level0",[-0.05,0],1],[],["Level0",[0.05,0],1],["Level0",[0.2,0],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_0 [Indent level: 6],
                        "VALM_1_0": {
                            "type": "text",
                            "source": "static",
                            "text": 0,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[-0.23,-0.025],1],
                            "right": ["Level0",[-0.13,-0.025],1],
                            "down": ["Level0",[-0.23,0.025],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_0 [Indent level: 6],
                        "VALM_2_0": {
                            "align": "right",
                            "pos": ["Level0",[0.22,-0.025],1],
                            "right": ["Level0",[0.32,-0.025],1],
                            "down": ["Level0",[0.22,0.025],1],
                            "type": "text",
                            "source": "static",
                            "text": 0,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM5 [Indent level: 6],
                        "LevelM5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.2,-0.03],1],["LevelM5",[-0.2,0],1],["LevelM5",[-0.15,0],1],[],["LevelM5",[-0.1,0],1],["LevelM5",[-0.05,0],1],[],["LevelM5",[0.05,0],1],["LevelM5",[0.1,0],1],[],["LevelM5",[0.15,0],1],["LevelM5",[0.2,0],1],["LevelM5",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_5 [Indent level: 6],
                        "VALM_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM5",[-0.23,-0.085],1],
                            "right": ["LevelM5",[-0.13,-0.085],1],
                            "down": ["LevelM5",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_5 [Indent level: 6],
                        "VALM_2_5": {
                            "align": "right",
                            "pos": ["LevelM5",[0.22,-0.085],1],
                            "right": ["LevelM5",[0.32,-0.085],1],
                            "down": ["LevelM5",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP5 [Indent level: 6],
                        "LevelP5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.2,0.03],1],["LevelP5",[-0.2,0],1],["LevelP5",[-0.05,0],1],[],["LevelP5",[0.05,0],1],["LevelP5",[0.2,0],1],["LevelP5",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_5 [Indent level: 6],
                        "VALP_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP5",[-0.23,0.035],1],
                            "right": ["LevelP5",[-0.13,0.035],1],
                            "down": ["LevelP5",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_5 [Indent level: 6],
                        "VALP_2_5": {
                            "align": "right",
                            "pos": ["LevelP5",[0.22,0.035],1],
                            "right": ["LevelP5",[0.32,0.035],1],
                            "down": ["LevelP5",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM10 [Indent level: 6],
                        "LevelM10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.2,-0.03],1],["LevelM10",[-0.2,0],1],["LevelM10",[-0.15,0],1],[],["LevelM10",[-0.1,0],1],["LevelM10",[-0.05,0],1],[],["LevelM10",[0.05,0],1],["LevelM10",[0.1,0],1],[],["LevelM10",[0.15,0],1],["LevelM10",[0.2,0],1],["LevelM10",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_10 [Indent level: 6],
                        "VALM_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM10",[-0.23,-0.085],1],
                            "right": ["LevelM10",[-0.13,-0.085],1],
                            "down": ["LevelM10",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_10 [Indent level: 6],
                        "VALM_2_10": {
                            "align": "right",
                            "pos": ["LevelM10",[0.22,-0.085],1],
                            "right": ["LevelM10",[0.32,-0.085],1],
                            "down": ["LevelM10",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP10 [Indent level: 6],
                        "LevelP10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.2,0.03],1],["LevelP10",[-0.2,0],1],["LevelP10",[-0.05,0],1],[],["LevelP10",[0.05,0],1],["LevelP10",[0.2,0],1],["LevelP10",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_10 [Indent level: 6],
                        "VALP_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP10",[-0.23,0.035],1],
                            "right": ["LevelP10",[-0.13,0.035],1],
                            "down": ["LevelP10",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_10 [Indent level: 6],
                        "VALP_2_10": {
                            "align": "right",
                            "pos": ["LevelP10",[0.22,0.035],1],
                            "right": ["LevelP10",[0.32,0.035],1],
                            "down": ["LevelP10",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM15 [Indent level: 6],
                        "LevelM15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.2,-0.03],1],["LevelM15",[-0.2,0],1],["LevelM15",[-0.15,0],1],[],["LevelM15",[-0.1,0],1],["LevelM15",[-0.05,0],1],[],["LevelM15",[0.05,0],1],["LevelM15",[0.1,0],1],[],["LevelM15",[0.15,0],1],["LevelM15",[0.2,0],1],["LevelM15",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_15 [Indent level: 6],
                        "VALM_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM15",[-0.23,-0.085],1],
                            "right": ["LevelM15",[-0.13,-0.085],1],
                            "down": ["LevelM15",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_15 [Indent level: 6],
                        "VALM_2_15": {
                            "align": "right",
                            "pos": ["LevelM15",[0.22,-0.085],1],
                            "right": ["LevelM15",[0.32,-0.085],1],
                            "down": ["LevelM15",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP15 [Indent level: 6],
                        "LevelP15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.2,0.03],1],["LevelP15",[-0.2,0],1],["LevelP15",[-0.05,0],1],[],["LevelP15",[0.05,0],1],["LevelP15",[0.2,0],1],["LevelP15",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_15 [Indent level: 6],
                        "VALP_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP15",[-0.23,0.035],1],
                            "right": ["LevelP15",[-0.13,0.035],1],
                            "down": ["LevelP15",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_15 [Indent level: 6],
                        "VALP_2_15": {
                            "align": "right",
                            "pos": ["LevelP15",[0.22,0.035],1],
                            "right": ["LevelP15",[0.32,0.035],1],
                            "down": ["LevelP15",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM20 [Indent level: 6],
                        "LevelM20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.2,-0.03],1],["LevelM20",[-0.2,0],1],["LevelM20",[-0.15,0],1],[],["LevelM20",[-0.1,0],1],["LevelM20",[-0.05,0],1],[],["LevelM20",[0.05,0],1],["LevelM20",[0.1,0],1],[],["LevelM20",[0.15,0],1],["LevelM20",[0.2,0],1],["LevelM20",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_20 [Indent level: 6],
                        "VALM_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM20",[-0.23,-0.085],1],
                            "right": ["LevelM20",[-0.13,-0.085],1],
                            "down": ["LevelM20",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_20 [Indent level: 6],
                        "VALM_2_20": {
                            "align": "right",
                            "pos": ["LevelM20",[0.22,-0.085],1],
                            "right": ["LevelM20",[0.32,-0.085],1],
                            "down": ["LevelM20",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP20 [Indent level: 6],
                        "LevelP20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.2,0.03],1],["LevelP20",[-0.2,0],1],["LevelP20",[-0.05,0],1],[],["LevelP20",[0.05,0],1],["LevelP20",[0.2,0],1],["LevelP20",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_20 [Indent level: 6],
                        "VALP_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP20",[-0.23,0.035],1],
                            "right": ["LevelP20",[-0.13,0.035],1],
                            "down": ["LevelP20",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_20 [Indent level: 6],
                        "VALP_2_20": {
                            "align": "right",
                            "pos": ["LevelP20",[0.22,0.035],1],
                            "right": ["LevelP20",[0.32,0.035],1],
                            "down": ["LevelP20",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM25 [Indent level: 6],
                        "LevelM25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.2,-0.03],1],["LevelM25",[-0.2,0],1],["LevelM25",[-0.15,0],1],[],["LevelM25",[-0.1,0],1],["LevelM25",[-0.05,0],1],[],["LevelM25",[0.05,0],1],["LevelM25",[0.1,0],1],[],["LevelM25",[0.15,0],1],["LevelM25",[0.2,0],1],["LevelM25",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_25 [Indent level: 6],
                        "VALM_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM25",[-0.23,-0.085],1],
                            "right": ["LevelM25",[-0.13,-0.085],1],
                            "down": ["LevelM25",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_25 [Indent level: 6],
                        "VALM_2_25": {
                            "align": "right",
                            "pos": ["LevelM25",[0.22,-0.085],1],
                            "right": ["LevelM25",[0.32,-0.085],1],
                            "down": ["LevelM25",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP25 [Indent level: 6],
                        "LevelP25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.2,0.03],1],["LevelP25",[-0.2,0],1],["LevelP25",[-0.05,0],1],[],["LevelP25",[0.05,0],1],["LevelP25",[0.2,0],1],["LevelP25",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_25 [Indent level: 6],
                        "VALP_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP25",[-0.23,0.035],1],
                            "right": ["LevelP25",[-0.13,0.035],1],
                            "down": ["LevelP25",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_25 [Indent level: 6],
                        "VALP_2_25": {
                            "align": "right",
                            "pos": ["LevelP25",[0.22,0.035],1],
                            "right": ["LevelP25",[0.32,0.035],1],
                            "down": ["LevelP25",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM30 [Indent level: 6],
                        "LevelM30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.2,-0.03],1],["LevelM30",[-0.2,0],1],["LevelM30",[-0.15,0],1],[],["LevelM30",[-0.1,0],1],["LevelM30",[-0.05,0],1],[],["LevelM30",[0.05,0],1],["LevelM30",[0.1,0],1],[],["LevelM30",[0.15,0],1],["LevelM30",[0.2,0],1],["LevelM30",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_30 [Indent level: 6],
                        "VALM_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM30",[-0.23,-0.085],1],
                            "right": ["LevelM30",[-0.13,-0.085],1],
                            "down": ["LevelM30",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_30 [Indent level: 6],
                        "VALM_2_30": {
                            "align": "right",
                            "pos": ["LevelM30",[0.22,-0.085],1],
                            "right": ["LevelM30",[0.32,-0.085],1],
                            "down": ["LevelM30",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP30 [Indent level: 6],
                        "LevelP30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.2,0.03],1],["LevelP30",[-0.2,0],1],["LevelP30",[-0.05,0],1],[],["LevelP30",[0.05,0],1],["LevelP30",[0.2,0],1],["LevelP30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_30 [Indent level: 6],
                        "VALP_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP30",[-0.23,0.035],1],
                            "right": ["LevelP30",[-0.13,0.035],1],
                            "down": ["LevelP30",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_30 [Indent level: 6],
                        "VALP_2_30": {
                            "align": "right",
                            "pos": ["LevelP30",[0.22,0.035],1],
                            "right": ["LevelP30",[0.32,0.035],1],
                            "down": ["LevelP30",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM35 [Indent level: 6],
                        "LevelM35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.2,-0.03],1],["LevelM35",[-0.2,0],1],["LevelM35",[-0.15,0],1],[],["LevelM35",[-0.1,0],1],["LevelM35",[-0.05,0],1],[],["LevelM35",[0.05,0],1],["LevelM35",[0.1,0],1],[],["LevelM35",[0.15,0],1],["LevelM35",[0.2,0],1],["LevelM35",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_35 [Indent level: 6],
                        "VALM_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM35",[-0.23,-0.085],1],
                            "right": ["LevelM35",[-0.13,-0.085],1],
                            "down": ["LevelM35",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_35 [Indent level: 6],
                        "VALM_2_35": {
                            "align": "right",
                            "pos": ["LevelM35",[0.22,-0.085],1],
                            "right": ["LevelM35",[0.32,-0.085],1],
                            "down": ["LevelM35",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP35 [Indent level: 6],
                        "LevelP35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.2,0.03],1],["LevelP35",[-0.2,0],1],["LevelP35",[-0.05,0],1],[],["LevelP35",[0.05,0],1],["LevelP35",[0.2,0],1],["LevelP35",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_35 [Indent level: 6],
                        "VALP_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP35",[-0.23,0.035],1],
                            "right": ["LevelP35",[-0.13,0.035],1],
                            "down": ["LevelP35",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_35 [Indent level: 6],
                        "VALP_2_35": {
                            "align": "right",
                            "pos": ["LevelP35",[0.22,0.035],1],
                            "right": ["LevelP35",[0.32,0.035],1],
                            "down": ["LevelP35",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM40 [Indent level: 6],
                        "LevelM40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.2,-0.03],1],["LevelM40",[-0.2,0],1],["LevelM40",[-0.15,0],1],[],["LevelM40",[-0.1,0],1],["LevelM40",[-0.05,0],1],[],["LevelM40",[0.05,0],1],["LevelM40",[0.1,0],1],[],["LevelM40",[0.15,0],1],["LevelM40",[0.2,0],1],["LevelM40",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_40 [Indent level: 6],
                        "VALM_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM40",[-0.23,-0.085],1],
                            "right": ["LevelM40",[-0.13,-0.085],1],
                            "down": ["LevelM40",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_40 [Indent level: 6],
                        "VALM_2_40": {
                            "align": "right",
                            "pos": ["LevelM40",[0.22,-0.085],1],
                            "right": ["LevelM40",[0.32,-0.085],1],
                            "down": ["LevelM40",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP40 [Indent level: 6],
                        "LevelP40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.2,0.03],1],["LevelP40",[-0.2,0],1],["LevelP40",[-0.05,0],1],[],["LevelP40",[0.05,0],1],["LevelP40",[0.2,0],1],["LevelP40",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_40 [Indent level: 6],
                        "VALP_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP40",[-0.23,0.035],1],
                            "right": ["LevelP40",[-0.13,0.035],1],
                            "down": ["LevelP40",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_40 [Indent level: 6],
                        "VALP_2_40": {
                            "align": "right",
                            "pos": ["LevelP40",[0.22,0.035],1],
                            "right": ["LevelP40",[0.32,0.035],1],
                            "down": ["LevelP40",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM45 [Indent level: 6],
                        "LevelM45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.2,-0.03],1],["LevelM45",[-0.2,0],1],["LevelM45",[-0.15,0],1],[],["LevelM45",[-0.1,0],1],["LevelM45",[-0.05,0],1],[],["LevelM45",[0.05,0],1],["LevelM45",[0.1,0],1],[],["LevelM45",[0.15,0],1],["LevelM45",[0.2,0],1],["LevelM45",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_45 [Indent level: 6],
                        "VALM_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM45",[-0.23,-0.085],1],
                            "right": ["LevelM45",[-0.13,-0.085],1],
                            "down": ["LevelM45",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_45 [Indent level: 6],
                        "VALM_2_45": {
                            "align": "right",
                            "pos": ["LevelM45",[0.22,-0.085],1],
                            "right": ["LevelM45",[0.32,-0.085],1],
                            "down": ["LevelM45",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP45 [Indent level: 6],
                        "LevelP45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.2,0.03],1],["LevelP45",[-0.2,0],1],["LevelP45",[-0.05,0],1],[],["LevelP45",[0.05,0],1],["LevelP45",[0.2,0],1],["LevelP45",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_45 [Indent level: 6],
                        "VALP_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP45",[-0.23,0.035],1],
                            "right": ["LevelP45",[-0.13,0.035],1],
                            "down": ["LevelP45",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_45 [Indent level: 6],
                        "VALP_2_45": {
                            "align": "right",
                            "pos": ["LevelP45",[0.22,0.035],1],
                            "right": ["LevelP45",[0.32,0.035],1],
                            "down": ["LevelP45",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM50 [Indent level: 6],
                        "LevelM50": {
                            "type": "line",
                            "points": [["LevelM50",[-0.2,-0.03],1],["LevelM50",[-0.2,0],1],["LevelM50",[-0.15,0],1],[],["LevelM50",[-0.1,0],1],["LevelM50",[-0.05,0],1],[],["LevelM50",[0.05,0],1],["LevelM50",[0.1,0],1],[],["LevelM50",[0.15,0],1],["LevelM50",[0.2,0],1],["LevelM50",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_50 [Indent level: 6],
                        "VALM_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM50",[-0.23,-0.085],1],
                            "right": ["LevelM50",[-0.13,-0.085],1],
                            "down": ["LevelM50",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_50 [Indent level: 6],
                        "VALM_2_50": {
                            "align": "right",
                            "pos": ["LevelM50",[0.22,-0.085],1],
                            "right": ["LevelM50",[0.32,-0.085],1],
                            "down": ["LevelM50",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP50 [Indent level: 6],
                        "LevelP50": {
                            "type": "line",
                            "points": [["LevelP50",[-0.2,0.03],1],["LevelP50",[-0.2,0],1],["LevelP50",[-0.05,0],1],[],["LevelP50",[0.05,0],1],["LevelP50",[0.2,0],1],["LevelP50",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_50 [Indent level: 6],
                        "VALP_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "left",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP50",[-0.23,0.035],1],
                            "right": ["LevelP50",[-0.13,0.035],1],
                            "down": ["LevelP50",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_50 [Indent level: 6],
                        "VALP_2_50": {
                            "align": "right",
                            "pos": ["LevelP50",[0.22,0.035],1],
                            "right": ["LevelP50",[0.32,0.035],1],
                            "down": ["LevelP50",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "scale": 1,
                            "sourceScale": 1
                        }
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|MGun [Indent level: 4],
                "MGun": {
                    "condition": "mgun",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|MGun|Circle [Indent level: 5],
                    "Circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0.01,0],1],["WeaponAim",[-0.01,0],1],[],["WeaponAim",[0,0.01125],1],["WeaponAim",[0,-0.01125],1],[],["WeaponAim",[0,-0.07875],1],["WeaponAim",[0.049,-0.055125],1],["WeaponAim",[0.07,0],1],["WeaponAim",[0.049,0.055125],1],["WeaponAim",[0,0.07875],1],["WeaponAim",[-0.049,0.055125],1],["WeaponAim",[-0.07,0],1],["WeaponAim",[-0.049,-0.055125],1],["WeaponAim",[0,-0.07875],1],[],["WeaponAim",[0,-0.1575],1],["WeaponAim",[0.07,-0.137025],1],["WeaponAim",[0.1218,-0.07875],1],["WeaponAim",[0.14,0],1],["WeaponAim",[0.1218,0.07875],1],["WeaponAim",[0.07,0.137025],1],["WeaponAim",[0,0.1575],1],["WeaponAim",[-0.07,0.137025],1],["WeaponAim",[-0.1218,0.07875],1],["WeaponAim",[-0.14,0],1],["WeaponAim",[-0.1218,-0.07875],1],["WeaponAim",[-0.07,-0.137025],1],["WeaponAim",[0,-0.1575],1],[],["WeaponAim",[0,-0.1575],1],["WeaponAim",[0,-0.18],1],[],["WeaponAim",[-0.07,-0.136399],1],["WeaponAim",[-0.08,-0.155885],1],[],["WeaponAim",[-0.121244,-0.07875],1],["WeaponAim",[-0.138564,-0.09],1],[],["WeaponAim",[-0.14,6.88454e-009],1],["WeaponAim",[-0.16,7.86805e-009],1],[],["WeaponAim",[-0.121244,0.07875],1],["WeaponAim",[-0.138564,0.09],1],[],["WeaponAim",[-0.07,0.136399],1],["WeaponAim",[-0.08,0.155885],1],[],["WeaponAim",[1.22392e-008,0.1575],1],["WeaponAim",[1.39876e-008,0.18],1],[],["WeaponAim",[0.07,0.136399],1],["WeaponAim",[0.08,0.155885],1],[],["WeaponAim",[0.121244,0.07875],1],["WeaponAim",[0.138564,0.09],1],[],["WeaponAim",[0.14,-1.87817e-009],1],["WeaponAim",[0.16,-2.14648e-009],1],[],["WeaponAim",[0.121244,-0.07875],1],["WeaponAim",[0.138564,-0.09],1],[],["WeaponAim",[0.07,-0.136399],1],["WeaponAim",[0.08,-0.155885],1],[]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Bomb [Indent level: 4],
                "Bomb": {
                    "condition": "bomb",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Bomb|Circle [Indent level: 5],
                    "Circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.1125],1],["WeaponAim",[0.05,-0.097875],1],["WeaponAim",[0.087,-0.05625],1],["WeaponAim",[0.1,0],1],["WeaponAim",[0.087,0.05625],1],["WeaponAim",[0.05,0.097875],1],["WeaponAim",[0,0.1125],1],["WeaponAim",[-0.05,0.097875],1],["WeaponAim",[-0.087,0.05625],1],["WeaponAim",[-0.1,0],1],["WeaponAim",[-0.087,-0.05625],1],["WeaponAim",[-0.05,-0.097875],1],["WeaponAim",[0,-0.1125],1],[],["Velocity",0.001,"WeaponAim",[0,0],1],["Velocity",[0,0],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AAMissile [Indent level: 4],
                "AAMissile": {
                    "condition": "AAmissile",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AAMissile|Circle [Indent level: 5],
                    "Circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.28125],1],["WeaponAim",[0.125,-0.244687],1],["WeaponAim",[0.2175,-0.140625],1],["WeaponAim",[0.25,0],1],["WeaponAim",[0.2175,0.140625],1],["WeaponAim",[0.125,0.244687],1],["WeaponAim",[0,0.28125],1],["WeaponAim",[-0.125,0.244687],1],["WeaponAim",[-0.2175,0.140625],1],["WeaponAim",[-0.25,0],1],["WeaponAim",[-0.2175,-0.140625],1],["WeaponAim",[-0.125,-0.244687],1],["WeaponAim",[0,-0.28125],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ATMissile [Indent level: 4],
                "ATMissile": {
                    "condition": "ATmissile",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ATMissile|Circle [Indent level: 5],
                    "Circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.2025],1],["WeaponAim",[0.09,-0.176175],1],["WeaponAim",[0.1566,-0.10125],1],["WeaponAim",[0.18,0],1],["WeaponAim",[0.1566,0.10125],1],["WeaponAim",[0.09,0.176175],1],["WeaponAim",[0,0.2025],1],["WeaponAim",[-0.09,0.176175],1],["WeaponAim",[-0.1566,0.10125],1],["WeaponAim",[-0.18,0],1],["WeaponAim",[-0.1566,-0.10125],1],["WeaponAim",[-0.09,-0.176175],1],["WeaponAim",[0,-0.2025],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Rockets [Indent level: 4],
                "Rockets": {
                    "condition": "Rocket",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Rockets|Circle [Indent level: 5],
                    "Circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0.01,0],1],["WeaponAim",[-0.01,0],1],[],["WeaponAim",[0,0.01125],1],["WeaponAim",[0,-0.01125],1],[],["WeaponAim",[0,-0.135],1],["WeaponAim",[0.06,-0.11745],1],["WeaponAim",[0.1044,-0.0675],1],["WeaponAim",[0.12,0],1],["WeaponAim",[0.1044,0.0675],1],["WeaponAim",[0.06,0.11745],1],["WeaponAim",[0,0.135],1],["WeaponAim",[-0.06,0.11745],1],["WeaponAim",[-0.1044,0.0675],1],["WeaponAim",[-0.12,0],1],["WeaponAim",[-0.1044,-0.0675],1],["WeaponAim",[-0.06,-0.11745],1],["WeaponAim",[0,-0.135],1],[]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AltScale [Indent level: 4],
                "AltScale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "altitudeASL",
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [0.86,0.82],
                    "right": [0.94,0.82],
                    "down": [0.86,0.87],
                    "lineXleft": 0.825,
                    "lineYright": 0.835,
                    "lineXleftMajor": 0.825,
                    "lineYrightMajor": 0.845,
                    "bottom": 0.2,
                    "top": 0.85,
                    "center": 0.5,
                    "step": 20,
                    "StepSize": 0.0325,
                    "horizontal": "false",
                    "min": "none",
                    "max": "none",
                    "numberEach": 5,
                    "majorLineEach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|SpeedScale [Indent level: 4],
                "SpeedScale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "speed",
                    "sourceScale": 3.6,
                    "align": "right",
                    "pos": [0.06,0.17],
                    "right": [0.14,0.17],
                    "down": [0.06,0.22],
                    "lineXleft": 0.175,
                    "lineYright": 0.165,
                    "lineXleftMajor": 0.175,
                    "lineYrightMajor": 0.155,
                    "bottom": 0.85,
                    "center": 0.5,
                    "top": 0.2,
                    "step": 20,
                    "StepSize": 0.0325,
                    "horizontal": "false",
                    "min": "none",
                    "max": "none",
                    "numberEach": 5,
                    "majorLineEach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Gear [Indent level: 4],
                "Gear": {
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Gear|text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "GEAR",
                        "align": "right",
                        "scale": 0.5,
                        "sourceScale": 1,
                        "pos": [[0.84,0.88],1],
                        "right": [[0.9,0.88],1],
                        "down": [[0.84,0.92],1]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Flaps [Indent level: 4],
                "Flaps": {
                    "condition": "flaps",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Flaps|text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "FLAPS",
                        "align": "right",
                        "scale": 0.5,
                        "sourceScale": 1,
                        "pos": [[0.84,0.93],1],
                        "right": [[0.9,0.93],1],
                        "down": [[0.84,0.97],1]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|weapons [Indent level: 4],
                "weapons": {
                    "type": "text",
                    "source": "weapon",
                    "align": "right",
                    "scale": 0.5,
                    "sourceScale": 1,
                    "pos": [[0.1,0.88],1],
                    "right": [[0.16,0.88],1],
                    "down": [[0.1,0.92],1]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ammo [Indent level: 4],
                "ammo": {
                    "type": "text",
                    "source": "ammo",
                    "align": "right",
                    "scale": 0.5,
                    "sourceScale": 1,
                    "pos": [[0.1,0.93],1],
                    "right": [[0.16,0.93],1],
                    "down": [[0.1,0.97],1]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|VspeedNumber [Indent level: 4],
                "VspeedNumber": {
                    "type": "text",
                    "align": "right",
                    "scale": 1,
                    "source": "vspeed",
                    "sourceScale": 1,
                    "pos": [[0.86,0.12],1],
                    "right": [[0.94,0.12],1],
                    "down": [[0.86,0.17],1]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],
                "HeadingScale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "Heading",
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [0.2,0],
                    "right": [0.28,0],
                    "down": [0.2,0.05],
                    "lineXleft": 0.06,
                    "lineYright": 0.05,
                    "lineXleftMajor": 0.06,
                    "lineYrightMajor": 0.04,
                    "bottom": 0.8,
                    "center": 0.5,
                    "top": 0.2,
                    "step": 2,
                    "StepSize": 0.03,
                    "horizontal": "true",
                    "min": "none",
                    "max": "none",
                    "numberEach": 5,
                    "majorLineEach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS [Indent level: 4],
                "ILS": {
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS|Glideslope [Indent level: 5],
                    "Glideslope": {
                        "clipTL": [0,0],
                        "clipBR": [1,1],
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 6],
                        "ILS": {
                            "type": "line",
                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[0,0.027],1],["ILS_W",[0,-0.027],1],[],["ILS_W",[0.12,0.027],1],["ILS_W",[0.12,-0.027],1],[],["ILS_W",[0.24,0.027],1],["ILS_W",[0.24,-0.027],1],[],["ILS_W",[-0.12,0.027],1],["ILS_W",[-0.12,-0.027],1],[],["ILS_W",[-0.24,0.027],1],["ILS_W",[-0.24,-0.027],1],[],["ILS_H",[0,-0.27],1],["ILS_H",[0,0.27],1],[],["ILS_H",[0.024,0],1],["ILS_H",[-0.024,0],1],[],["ILS_H",[0.024,0.135],1],["ILS_H",[-0.024,0.135],1],[],["ILS_H",[0.024,0.27],1],["ILS_H",[-0.024,0.27],1],[],["ILS_H",[0.024,-0.135],1],["ILS_H",[-0.024,-0.135],1],[],["ILS_H",[0.024,-0.27],1],["ILS_H",[-0.024,-0.27],1]]
                        }
                    }
                }
            }
        }
    },
    "maxOmega": 2000,
    # Class: CfgVehicles|RHS_C130J_Base|Wheels [Indent level: 1],
    "Wheels": {
        "disableWheelsWhenDestroyed": 1,
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_1_1 [Indent level: 2],
        "Wheel_1_1": {
            "steering": 1,
            "side": "left",
            "boneName": "Wheel_1_1",
            "center": "Wheel_1_1_center",
            "boundary": "Wheel_1_1_rim",
            "width": 0.16,
            "mass": 150,
            "MOI": 3,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 2000,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "suspForceAppPointOffset": "Wheel_1_1_center",
            "tireForceAppPointOffset": "Wheel_1_1_center",
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": 6400,
            "springStrength": 120000,
            "springDamperRate": 128000,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 25,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_1_1_fake [Indent level: 2],
        "Wheel_1_1_fake": {
            "steering": 1,
            "side": "left",
            "boneName": "Wheel_1_1",
            "center": "Wheel_1_1_center",
            "boundary": "Wheel_1_1_rim",
            "width": 0.16,
            "mass": 150,
            "MOI": 3,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 2000,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "suspForceAppPointOffset": "Wheel_1_1_center",
            "tireForceAppPointOffset": "Wheel_1_1_center",
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": 6400,
            "springStrength": 120000,
            "springDamperRate": 128000,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 25,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_2_1 [Indent level: 2],
        "Wheel_2_1": {
            "steering": 0,
            "boneName": "Wheel_2_1",
            "center": "Wheel_2_1_center",
            "boundary": "Wheel_2_1_rim",
            "suspForceAppPointOffset": "Wheel_2_1_center",
            "tireForceAppPointOffset": "Wheel_2_1_center",
            "width": 0.28,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": 3200,
            "springDamperRate": 51200,
            "springStrength": 1.58e+006,
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
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_2_2 [Indent level: 2],
        "Wheel_2_2": {
            "side": "right",
            "boneName": "Wheel_2_2",
            "center": "Wheel_2_2_center",
            "boundary": "Wheel_2_2_rim",
            "suspForceAppPointOffset": "Wheel_2_2_center",
            "tireForceAppPointOffset": "Wheel_2_2_center",
            "steering": 0,
            "width": 0.28,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": 3200,
            "springDamperRate": 51200,
            "springStrength": 1.58e+006,
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
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_3_1 [Indent level: 2],
        "Wheel_3_1": {
            "boneName": "Wheel_3_1",
            "center": "Wheel_3_1_center",
            "boundary": "Wheel_3_1_rim",
            "suspForceAppPointOffset": "Wheel_3_1_center",
            "tireForceAppPointOffset": "Wheel_3_1_center",
            "steering": 0,
            "width": 0.28,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": 3200,
            "springDamperRate": 51200,
            "springStrength": 1.58e+006,
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
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_3_2 [Indent level: 2],
        "Wheel_3_2": {
            "side": "right",
            "boneName": "Wheel_3_2",
            "center": "Wheel_3_2_center",
            "boundary": "Wheel_3_2_rim",
            "suspForceAppPointOffset": "Wheel_3_2_center",
            "tireForceAppPointOffset": "Wheel_3_2_center",
            "steering": 0,
            "width": 0.28,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": 3200,
            "springDamperRate": 51200,
            "springStrength": 1.58e+006,
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
    # Class: CfgVehicles|RHS_C130J_Base|Turrets [Indent level: 1],
    "Turrets": {
        # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret [Indent level: 2]
        "CopilotTurret": {
            "isCopilot": 1,
            "primaryGunner": 0,
            "canEject": 0,
            "body": "",
            "gun": "",
            "animationSourceBody": "",
            "animationSourceGun": "",
            "weapons": [],
            "magazines": [],
            "gunnerAction": "RHS_C130_Pilot",
            "gunnerInAction": "RHS_C130_Pilot",
            "gunnerName": "Copilot",
            "gunnerDoor": "Door_1",
            "gunnerNotSpawned": 0,
            "gunnerUsesPilotView": 1,
            "hasGunner": 1,
            "memoryPointsGetInGunner": "pos driver",
            "memoryPointsGetInGunnerDir": "pos driver dir",
            "minElev": -50,
            "maxElev": 30,
            "initElev": 11,
            "minTurn": -170,
            "maxTurn": 170,
            "initTurn": 0,
            "maxHorizontalRotSpeed": 3,
            "maxVerticalRotSpeed": 3,
            # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|ViewGunner [Indent level: 3],
            "ViewGunner": {
                "initAngleX": -5,
                "initAngleY": 0,
                "initFov": 0.9,
                "minFov": 0.25,
                "maxFov": 1.25,
                "minAngleX": -65,
                "maxAngleX": 85,
                "minAngleY": -150,
                "maxAngleY": 150,
                "minMoveX": -0.075,
                "maxMoveX": 0.075,
                "minMoveY": -0.075,
                "maxMoveY": 0.075,
                "minMoveZ": -0.075,
                "maxMoveZ": 0.1,
                "continuous": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "commanding": -1,
            "gunnerLeftHandAnimName": "copilot_control",
            "gunnerRightHandAnimName": "copilot_control",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "gunnerForceOptics": 0,
            "turretCanSee": 15,
            # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors [Indent level: 3],
            "Reflectors": {
                # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cabin [Indent level: 4]
                "cabin": {
                    "color": [830,100,100],
                    "ambient": [5,0,0],
                    "intensity": 9,
                    "size": 1,
                    "innerAngle": 90,
                    "outerAngle": 165,
                    "coneFadeCoef": 1,
                    "position": "cabin_light",
                    "direction": "cabin_light_dir",
                    "hitpoint": "cabin_light",
                    "selection": "cabin_light",
                    "useFlare": 1,
                    "flareSize": 1,
                    "flareMaxDistance": 5,
                    "dayLight": 1,
                    "blinking": 0,
                    # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cabin|Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 50,
                        "hardLimitStart": 3,
                        "hardLimitEnd": 3.5
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_1 [Indent level: 4],
                "cargo_light_1": {
                    "color": [830,100,100],
                    "position": "cargo_light_1",
                    "direction": "cargo_light_1_dir",
                    "hitpoint": "cargo_light_1",
                    "selection": "cargo_light_1",
                    "intensity": 21,
                    "useFlare": 0,
                    "coneFadeCoef": 0.1,
                    # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardLimitStart": 3,
                        "hardLimitEnd": 3.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerAngle": 90,
                    "outerAngle": 165,
                    "flareSize": 1,
                    "flareMaxDistance": 5,
                    "dayLight": 1,
                    "blinking": 0
                },
                # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_2 [Indent level: 4],
                "cargo_light_2": {
                    "position": "cargo_light_2",
                    "direction": "cargo_light_2_dir",
                    "hitpoint": "cargo_light_2",
                    "selection": "cargo_light_2",
                    "color": [830,100,100],
                    "intensity": 21,
                    "useFlare": 0,
                    "coneFadeCoef": 0.1,
                    # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardLimitStart": 3,
                        "hardLimitEnd": 3.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerAngle": 90,
                    "outerAngle": 165,
                    "flareSize": 1,
                    "flareMaxDistance": 5,
                    "dayLight": 1,
                    "blinking": 0
                },
                # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_3 [Indent level: 4],
                "cargo_light_3": {
                    "position": "cargo_light_3",
                    "direction": "cargo_light_3_dir",
                    "hitpoint": "cargo_light_3",
                    "selection": "cargo_light_3",
                    "color": [830,100,100],
                    "intensity": 21,
                    "useFlare": 0,
                    "coneFadeCoef": 0.1,
                    # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardLimitStart": 3,
                        "hardLimitEnd": 3.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerAngle": 90,
                    "outerAngle": 165,
                    "flareSize": 1,
                    "flareMaxDistance": 5,
                    "dayLight": 1,
                    "blinking": 0
                },
                # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_4 [Indent level: 4],
                "cargo_light_4": {
                    "position": "cargo_light_4",
                    "direction": "cargo_light_4_dir",
                    "hitpoint": "cargo_light_4",
                    "selection": "cargo_light_4",
                    "color": [830,100,100],
                    "intensity": 21,
                    "useFlare": 0,
                    "coneFadeCoef": 0.1,
                    # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardLimitStart": 3,
                        "hardLimitEnd": 3.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerAngle": 90,
                    "outerAngle": 165,
                    "flareSize": 1,
                    "flareMaxDistance": 5,
                    "dayLight": 1,
                    "blinking": 0
                }
            },
            # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Hitpoints [Indent level: 3],
            "Hitpoints": {
            },
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerType": "",
            "primaryObserver": 0,
            "soundServo": ["",0.00316228,1],
            "soundElevation": ["",0.00316228,1],
            "minOutElev": -4,
            "maxOutElev": 20,
            "initOutElev": 0,
            "minOutTurn": -60,
            "maxOutTurn": 60,
            "initOutTurn": 0,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "stabilizedInAxes": 3,
            "primary": 1,
            "gunnerGetInAction": "",
            "gunnerGetOutAction": "",
            "canUseScanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsModel": "",
            "gunnerOpticsColor": [0,0,0,1],
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
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        }
    },
    "hiddenSelections": ["camo1","camo2"],
    "hiddenSelectionsTextures": ["rhsusf|addons|rhsusf_a2port_air|c130j|data|c130j_body_co.paa","rhsusf|addons|rhsusf_a2port_air|c130j|data|c130j_wings_co.paa"],
    # Class: CfgVehicles|RHS_C130J_Base|textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles|RHS_C130J_Base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayName": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_a2port_air|c130j|data|c130j_body_co.paa","rhsusf|addons|rhsusf_a2port_air|c130j|data|c130j_wings_co.paa"],
            "factions": ["rhs_faction_usaf"]
        }
    },
    "textureList": ["standard",1],
    # Class: CfgVehicles|RHS_C130J_Base|Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|ObjectTexture [Indent level: 2]
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|door_1 [Indent level: 2],
        "door_1": {
            "displayName": "Open crew door",
            "property": "door_1",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|door_2_1 [Indent level: 2],
        "door_2_1": {
            "displayName": "Open left door",
            "property": "door_2_1",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|door_2_2 [Indent level: 2],
        "door_2_2": {
            "displayName": "Open right door",
            "property": "door_2_2",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|Ramp [Indent level: 2],
        "Ramp": {
            "displayName": "Open cargo bay",
            "property": "Ramp",
            "control": "slider",
            "expression": "_this animateSource ['%s',_value,true]",
            "defaultValue": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|hide_cargo [Indent level: 2],
        "hide_cargo": {
            "displayName": "Hide cargo benches",
            "property": "hide_cargo",
            "expression": "_this animate ['%s',_value,true];for '_i' from 1 to 24 do {_this lockCargo [_i,(_value == 1)]}",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|rhs_attachCargo [Indent level: 2],
        "rhs_attachCargo": {
            "displayName": "Attach cargo",
            "tooltip": "Attaching cargo (using attachTo command) just like when you use ramp action",
            "property": "rhs_attachCargo",
            "expression": "if(_value == 1)then{[_this] spawn rhs_fnc_cargoAttach}else{{if(not(_x isKindOf 'Man'))then{detach _x}}foreach attachedObjects _this};",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|VehicleTransport [Indent level: 1],
    "VehicleTransport": {
        # Class: CfgVehicles|RHS_C130J_Base|VehicleTransport|Carrier [Indent level: 2]
        "Carrier": {
            "cargoBayDimensions": ["VTV_limit_1","VTV_limit_2_mini"],
            "disableHeightLimit": 0,
            "maxLoadMass": 28000,
            "cargoAlignment": ["front","center"],
            "cargoSpacing": [0,0.1,0],
            "exits": ["VTV_exit_1"],
            "unloadingInterval": 2,
            "loadingDistance": 15,
            "loadingAngle": 60,
            "parachuteClassDefault": "B_Parachute_02_F",
            "parachuteHeightLimitDefault": 25
        }
    },
    "_generalMacro": "Plane_Base_F",
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "waterLinearDampingCoefY": 0,
    "waterLinearDampingCoefX": 5,
    "transportMaxWeapons": 6,
    "transportMaxMagazines": 24,
    "transportMaxBackpacks": 6,
    "maximumLoad": 500,
    "supplyRadius": 2,
    "memoryPointSupply": "doplnovani",
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
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints [Indent level: 2],
        "HitPoints": {
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitTurret [Indent level: 3]
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
    "brakeDistance": 500,
    "steerAheadSimul": 1,
    "steerAheadPlan": 2,
    "gearRetracting": 1,
    "durationGetIn": 0.99,
    "durationGetOut": 0.99,
    "flaps": 1,
    "airBrake": 1,
    "vtol": 0,
    "tailHook": 0,
    "lightOnGear": 1,
    "ejectDamageLimit": 0.45,
    "minFireTime": 60,
    "simulation": "airplanex",
    "minGunElev": 0,
    "maxGunElev": 0,
    "minGunTurn": 0,
    "maxGunTurn": 0,
    "gunAimDown": 0,
    "VTOLYawInfluence": 2,
    "VTOLPitchInfluence": 2,
    "VTOLRollInfluence": 2,
    # Class: CfgVehicles|Plane|ViewPilot [Indent level: 1],
    "ViewPilot": {
        "initFov": 0.75,
        "minFov": 0.25,
        "maxFov": 1.25,
        "initAngleX": 0,
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
    "memoryPointLRocket": "L raketa",
    "memoryPointRRocket": "P raketa",
    "memoryPointLDust": "levy prach",
    "memoryPointRDust": "pravy prach",
    "selectionFireAnim": "zasleh",
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "dustEffect": "HeliDust",
    "waterEffect": "HeliWater",
    # Class: CfgVehicles|Plane|WingVortices [Indent level: 1],
    "WingVortices": {
        # Class: CfgVehicles|Plane|WingVortices|WingTipLeft [Indent level: 2]
        "WingTipLeft": {
            "effectName": "WingVortices",
            "position": "cerveny pozicni"
        },
        # Class: CfgVehicles|Plane|WingVortices|WingTipRight [Indent level: 2],
        "WingTipRight": {
            "effectName": "WingVortices",
            "position": "zeleny pozicni"
        }
    },
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
            # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
            # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
            # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
            # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "numberPhysicalWheels": 3,
    # Class: CfgVehicles|Plane|SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles|Plane|SpeechVariants|Default [Indent level: 2]
        "Default": {
            "speechSingular": ["veh_air_plane_s"],
            "speechPlural": ["veh_air_plane_p"]
        }
    },
    "textSingular": "fast mover",
    "textPlural": "fast movers",
    "nameSound": "veh_air_plane_s",
    "type": 2,
    "memoryPointGun": "kulomet",
    "fuelExplosionPower": 10,
    "epeImpulseDamageCoef": 10,
    "crewCrashProtection": 0.15,
    "damageEffect": "AirDestructionEffects",
    "gunnerGetInAction": "GetInHigh",
    "gunnerGetOutAction": "GetOutHigh",
    "camouflage": 100,
    "audible": 60,
    # Class: CfgVehicles|Plane|CamShake [Indent level: 1],
    "CamShake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minSpeed": 200
    },
    "camShakeCoef": 0,
    "headGforceLeaningFactor": [0.005,0.001,0.025],
    "armorStructural": 1,
    "explosionShielding": 2,
    "minTotalDamageThreshold": 0.005,
    # Class: CfgVehicles|Plane|DestructionEffects [Indent level: 1],
    "DestructionEffects": {
    },
    "formationTime": 10,
    "gearsUpFrictionCoef": 0.5,
    "airBrakeFrictionCoef": 3,
    "airFrictionCoefs2": [0.001,0.0005,6e-005],
    "airFrictionCoefs1": [0.1,0.05,0.006],
    "airFrictionCoefs0": [0,0,0],
    "fuelCapacity": 1000,
    "insideSoundCoef": 0.0316228,
    "outsideSoundFilter": 1,
    "occludeSoundsWhenIn": 0.316228,
    "obstructSoundsWhenIn": 0.316228,
    "irScanRangeMin": 2000,
    "irScanRangeMax": 10000,
    "irScanToEyeFactor": 2,
    "nightVision": 0,
    "enableGPS": 1,
    "weaponsGroup1": "1 + 		2",
    "weaponsGroup2": 4,
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    "editorSubcategory": "EdSubcat_Planes",
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
    "radarType": 4,
    "countermeasureActivationRadius": 10000,
    # Class: CfgVehicles|Air|Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles|Air|Exhausts|Exhaust1 [Indent level: 2]
        "Exhaust1": {
            "position": "exhaust1",
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectPlane"
        },
        # Class: CfgVehicles|Air|Exhausts|Exhaust2 [Indent level: 2],
        "Exhaust2": {
            "position": "exhaust2",
            "direction": "exhaust2_dir",
            "effect": "ExhaustsEffectPlane"
        }
    },
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
    "memoryPointDriverOptics": ["driverview","pilot"],
    "memoryPointsGetInDriver": "pos driver",
    "memoryPointsGetInDriverDir": "pos driver dir",
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInDriverPrecise": "pos driver",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "memoryPointTaskMarker": "",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
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
        # Class: CfgVehicles|AllVehicles|CargoSpec|Cargo1 [Indent level: 2]
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
    # Class: CfgVehicles|AllVehicles|RenderTargets [Indent level: 1],
    "RenderTargets": {
    },
    "cargoProxyIndexes": [],
    "driverLeftLegAnimName": "",
    "driverRightLegAnimName": "",
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "preciseGetInOut": 0,
    "cargoPreciseGetInOut": [0],
    "availableForSupportTypes": [],
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
        # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2]
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
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
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
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
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
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
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
    "armorLights": 0.4,
    "crewVulnerable": 1,
    "damageResistance": 0.004,
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
    "laserScanner": 0,
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
    "showAllTargets": 0,
    "dustFrontLeftPos": "dustFrontLeft",
    "dustFrontRightPos": "dustFrontRight",
    "dustBackLeftPos": "dustBackLeft",
    "dustBackRightPos": "dustBackRight",
    "wheelCircumference": 1,
    "waterAngularDampingCoef": 0,
    "showNVGDriver": 0,
    "showNVGCommander": 0,
    "showNVGGunner": 0,
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
    "soundGearUp": ["",1,1],
    "soundGearDown": ["",1,1],
    "soundFlapsUp": ["",1,1],
    "soundFlapsDown": ["",1,1],
    "cabinOpenSound": ["",1,1],
    "cabinCloseSound": ["",1,1],
    "cabinOpenSoundInternal": ["",1,1],
    "cabinCloseSoundInternal": ["",1,1],
    "soundCrashes": ["soundCrash",1],
    "soundLandCrashes": ["soundLandCrash",1],
    "soundWaterCrashes": ["soundWaterCrash",1],
    "emptySound": ["",0,1],
    "soundWoodCrash": ["emptySound",0],
    "soundBushCrash": ["emptySound",0],
    "soundBuildingCrash": ["emptySound",0],
    "soundArmorCrash": ["emptySound",0],
    "soundLocked": ["",1,1],
    "aggregateReflectors": [],
    "driverInAction": "",
    "driverOpticsModel": "",
    "driverOpticsEffect": [],
    "driverOpticsColor": [1,1,1,1],
    "hideProxyInCombat": 0,
    "forceHideDriver": 0,
    "canHideDriver": -1,
    "castDriverShadow": 0,
    "castCargoShadow": 0,
    "viewDriverShadow": 1,
    "viewDriverShadowDiff": 1,
    "viewDriverShadowAmb": 1,
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
    "HeadAimDown": 0,
    "driverCanEject": 1,
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
    "features": "",
    "insideDetectCoef": 0.05,
}