RHS_CH_47F_10 = {
    "faction": "rhs_faction_usarmy_d",
    "vehicleClass": "rhs_vehclass_helicopter",
    "crew": "rhsusf_army_ocp_helipilot",
    "typicalCargo": ["rhsusf_army_ocp_helicrew"],
    "author": "Red Hammer Studios",
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|RHS_CH_47F_10.paa",
    "accuracy": 1000,
    "scope": 2,
    "ace_fastroping_enabled": 1,
    "ace_fastroping_ropeOrigins": [[0.5,-7.15,-0.95],[-0.5,-7.15,-0.95]],
    "ace_fastroping_onCut": "ace_compat_rhs_usf3_fnc_onCut",
    "ace_fastroping_onPrepare": "ace_compat_rhs_usf3_fnc_onPrepare",
    # Class: CfgVehicles\RHS_CH_47F\UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles\RHS_CH_47F\UserActions\CloseCargoDoor [Indent level: 2]
        "CloseCargoDoor": {
            "condition": "[this,'ramp_anim'] call ace_compat_rhs_usf3_fnc_canCloseDoor",
            "displayName": "Open Ramp",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "statement": "this animateSource ['ramp_anim', 1];{if(not(_x isKindOf 'Man'))then{detach _x}}foreach attachedObjects this;",
            "onlyforplayer": 1,
            "shortcut": "user12"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\UserActions\OpenCargoDoor [Indent level: 2],
        "OpenCargoDoor": {
            "displayName": "Open Ramp",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "this animationSourcePhase 'ramp_anim' < 1 and (alive this) and ({player == _x} count [driver this,  this turretUnit [3], this turretUnit [4]] > 0)",
            "statement": "this animateSource ['ramp_anim', 1];{if(not(_x isKindOf 'Man'))then{detach _x}}foreach attachedObjects this;",
            "onlyforplayer": 1,
            "shortcut": "user12"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\UserActions\LevelRamp [Indent level: 2],
        "LevelRamp": {
            "displayName": "Level Ramp",
            "condition": "this animationSourcePhase 'ramp_anim' != 0.6 and (alive this) and (alive this) and ({player == _x} count [driver this,  this turretUnit [3], this turretUnit [4]] > 0);",
            "statement": "this animateSource ['ramp_anim', 0.6];",
            "shortcut": "user13",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1
        },
        # Class: CfgVehicles\RHS_CH_47F_base\UserActions\VehicleParadrop [Indent level: 2],
        "VehicleParadrop": {
            "displayName": "Paradrop cargo",
            "condition": "(count (attachedObjects this) > 0) AND ('man' countType (attachedObjects this) == 0) AND Alive(this)",
            "statement": "[this] spawn rhs_fnc_vehPara",
            "shortcut": "",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1
        },
        # Class: CfgVehicles\RHS_CH_47F_base\UserActions\ToggleLight [Indent level: 2],
        "ToggleLight": {
            "displayName": "Toggle interior light",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "player in this;",
            "statement": "[this,'cargolights_hide'] call rhs_fnc_toggleIntLight",
            "onlyforplayer": 1
        },
        # Class: CfgVehicles\RHS_CH_47F_base\UserActions\WheelBrakes [Indent level: 2],
        "WheelBrakes": {
            "displayName": "Toggle Wheel Brakes",
            "shortcut": "binocular",
            "condition": "!difficultyEnabledRTD && (call rhs_fnc_findPlayer) isEqualTo (driver this)",
            "statement": "[this] call rhs_fnc_heli_wheelBrakes",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1
        }
    },
    "rhs_paraRamp": "ramp_anim",
    "rhs_paraOff": -8.5,
    "rhs_rampAnim": "ramp",
    "rhs_paraScript": "rhs_fnc_vehPara",
    "dlc": "RHS_USAF",
    "rhs_hasNoRadar": 1,
    "LESH_canBeTowed": 1,
    "LESH_towFromFront": 0,
    "LESH_AxisOffsetTarget": [0,-8,-2.5],
    "LESH_WheelOffset": [0,3],
    "category": "Air",
    "maxOmega": 2000,
    "numberPhysicalWheels": 4,
    # Class: CfgVehicles\RHS_CH_47F_base\Wheels [Indent level: 1],
    "Wheels": {
        "disableWheelsWhenDestroyed": 1,
        # Class: CfgVehicles\RHS_CH_47F_base\Wheels\Wheel_1_1 [Indent level: 2],
        "Wheel_1_1": {
            "steering": 0,
            "side": "left",
            "boneName": "Wheel_1_1_axis_damper",
            "suspForceAppPointOffset": "Wheel_1_1_axis",
            "tireForceAppPointOffset": "Wheel_1_1_axis",
            "center": "Wheel_1_1_axis",
            "boundary": "Wheel_1_1_bound",
            "suspTravelDirection": [0,-1,0],
            "width": 0.565,
            "mass": 15,
            "MOI": 0.768,
            "dampingRate": 0.25,
            "dampingRateDamaged": 2,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 2000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.14,
            "maxDroop": 0,
            "sprungMass": 2500,
            "springStrength": 12000,
            "springDamperRate": 1280,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Wheels\Wheel_2_1 [Indent level: 2],
        "Wheel_2_1": {
            "boneName": "Wheel_2_1_axis_damper",
            "side": "right",
            "suspForceAppPointOffset": "Wheel_2_1_axis",
            "tireForceAppPointOffset": "Wheel_2_1_axis",
            "center": "Wheel_2_1_axis",
            "boundary": "Wheel_2_1_bound",
            "steering": 0,
            "suspTravelDirection": [0,-1,0],
            "width": 0.565,
            "mass": 15,
            "MOI": 0.768,
            "dampingRate": 0.25,
            "dampingRateDamaged": 2,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 2000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.14,
            "maxDroop": 0,
            "sprungMass": 2500,
            "springStrength": 12000,
            "springDamperRate": 1280,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Wheels\Wheel_1_2 [Indent level: 2],
        "Wheel_1_2": {
            "steering": 1,
            "side": "left",
            "boneName": "Wheel_1_2_axis_damper",
            "suspForceAppPointOffset": "Wheel_1_2_axis",
            "tireForceAppPointOffset": "Wheel_1_2_axis",
            "center": "Wheel_1_2_axis",
            "boundary": "Wheel_1_2_bound",
            "width": 0.21,
            "maxCompression": 0.15,
            "suspTravelDirection": [0,-1,0],
            "mass": 15,
            "MOI": 0.768,
            "dampingRate": 0.25,
            "dampingRateDamaged": 2,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 2000,
            "maxHandBrakeTorque": 0,
            "maxDroop": 0,
            "sprungMass": 2500,
            "springStrength": 12000,
            "springDamperRate": 1280,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Wheels\Wheel_2_2 [Indent level: 2],
        "Wheel_2_2": {
            "boneName": "Wheel_2_2_axis_damper",
            "side": "right",
            "suspForceAppPointOffset": "Wheel_2_2_axis",
            "tireForceAppPointOffset": "Wheel_2_2_axis",
            "center": "Wheel_2_2_axis",
            "boundary": "Wheel_2_2_bound",
            "steering": 1,
            "width": 0.21,
            "maxCompression": 0.15,
            "suspTravelDirection": [0,-1,0],
            "mass": 15,
            "MOI": 0.768,
            "dampingRate": 0.25,
            "dampingRateDamaged": 2,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 2000,
            "maxHandBrakeTorque": 0,
            "maxDroop": 0,
            "sprungMass": 2500,
            "springStrength": 12000,
            "springDamperRate": 1280,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    "gearRetracting": 0,
    "driveOnComponent": ["wheels"],
    # Class: CfgVehicles\RHS_CH_47F_base\RotorLibHelicopterProperties [Indent level: 1],
    "RotorLibHelicopterProperties": {
        "RTDconfig": "rhsusf|addons|rhsusf_c_a2port_air|CH47|Rotorlib_CH47.xml",
        "autoHoverCorrection": [4.7,3.8,0],
        "defaultCollective": 0.665,
        "retreatBladeStallWarningSpeed": 92.583,
        "maxTorque": 4014,
        "stressDamagePerSec": 0.00333333,
        "maxHorizontalStabilizerLeftStress": 10000,
        "maxHorizontalStabilizerRightStress": 10000,
        "maxVerticalStabilizerStress": 10000,
        "horizontalWingsAngleCollMin": 0,
        "horizontalWingsAngleCollMax": 0,
        "maxMainRotorStress": 185000,
        "maxTailRotorStress": 185000
    },
    "availableForSupportTypes": ["Drop","Transport"],
    # Class: CfgVehicles\RHS_CH_47F_base\pilotCamera [Indent level: 1],
    "pilotCamera": {
    },
    "unitInfoType": "RHSUSF_RscUnitInfoAir_CH47",
    "unitInfoTypeRTD": "RHSUSF_RscUnitInfoAirRTDFullDigital",
    "selectionFireAnim": "",
    "destrType": "DestructWreck",
    "displayName": "CH-47F",
    "side": 1,
    "showNVGCargo": [1],
    "maxSpeed": 293,
    "nameSound": "veh_helicopter",
    "model": "rhsusf|addons|rhsusf_a2port_air|CH47|CH_47F",
    "picture": "rhsusf|addons|rhsusf_a2port_air|data|ico|rhs_ch47_pic_ca.paa",
    "icon": "rhsusf|addons|rhsusf_a2port_air|data|mapico|Icon_ch47f_CA.paa",
    "mapSize": 25,
    "driverAction": "RHS_CH47_Pilot",
    "reportOwnPosition": 1,
    "irTarget": 1,
    "irTargetSize": 1.2,
    "visualTarget": 1,
    "visualTargetSize": 1.3,
    "radarTarget": 1,
    "radarTargetSize": 1.12,
    "radarType": 4,
    "LockDetectionSystem": "8",
    "incomingMissileDetectionSystem": "2 + 8 + 16",
    # Class: CfgVehicles\RHS_CH_47F_base\Components [Indent level: 1],
    "Components": {
        # Class: CfgVehicles\RHS_CH_47F_base\Components\TransportPylonsComponent [Indent level: 2]
        "TransportPylonsComponent": {
            "UIPicture": "rhsusf|addons|rhsusf_a2port_air|data|loadouts|RHS_CH47_EDEN_CA.paa",
            # Class: CfgVehicles\RHS_CH_47F_base\Components\TransportPylonsComponent\pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles\RHS_CH_47F_base\Components\TransportPylonsComponent\pylons\cmDispenser [Indent level: 4]
                "cmDispenser": {
                    "hardpoints": ["RHSUSF_cm_M130","RHSUSF_cm_M130_x2","RHSUSF_cm_M130_x4","RHSUSF_cm_M130_x8"],
                    "priority": 1,
                    "attachment": "rhsusf_M130_CMFlare_Chaff_Magazine_x8",
                    "maxweight": 800,
                    "UIposition": [0.33,0]
                }
            }
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Components\SensorsManagerComponent [Indent level: 2],
        "SensorsManagerComponent": {
            # Class: CfgVehicles\RHS_CH_47F_base\Components\SensorsManagerComponent\Components [Indent level: 3]
            "Components": {
                # Class: CfgVehicles\RHS_CH_47F_base\Components\SensorsManagerComponent\Components\PassiveRadarSensorComponent [Indent level: 4]
                "PassiveRadarSensorComponent": {
                    "componentType": "PassiveRadarSensorComponent",
                    # Class: SensorTemplatePassiveRadar\AirTarget [Indent level: 0],
                    "AirTarget": {
                        "minRange": 16000,
                        "maxRange": 16000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: SensorTemplatePassiveRadar\GroundTarget [Indent level: 0],
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
        # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components [Indent level: 3]
            "Components": {
                # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay [Indent level: 4]
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\MinimapDisplay [Indent level: 4],
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay [Indent level: 4],
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SlingLoadDisplay [Indent level: 4],
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SensorDisplay [Indent level: 4],
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
        # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "VehicleSystemsDisplayManagerComponentRight": {
            "defaultDisplay": "SensorDisplay",
            # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentRight\Components [Indent level: 3],
            "Components": {
                # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay [Indent level: 4]
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\MinimapDisplay [Indent level: 4],
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay [Indent level: 4],
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\SlingLoadDisplay [Indent level: 4],
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\SensorDisplay [Indent level: 4],
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
        # Class: CfgVehicles\Air\Components\TransportCountermeasuresComponent [Indent level: 2],
        "TransportCountermeasuresComponent": {
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\Turrets [Indent level: 1],
    "Turrets": {
        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CopilotTurret [Indent level: 2]
        "CopilotTurret": {
            "isCopilot": 1,
            "CanEject": 0,
            "gunnerAction": "RHS_CH47_Pilot",
            "gunnerInAction": "RHS_CH47_Pilot",
            "memoryPointsGetInGunner": "pos codriver",
            "memoryPointsGetInGunnerDir": "pos codriver dir",
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "GetOutLow",
            "gunnerName": "Co-Pilot",
            "preciseGetInOut": 0,
            "GunnerDoor": "",
            "gunnerLeftHandAnimName": "lever_copilot",
            "gunnerRightHandAnimName": "stick_copilot",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "proxyIndex": 4,
            "gunnerCompartments": "Compartment3",
            "commanding": -3,
            "selectionFireAnim": "",
            # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CopilotTurret\Reflectors [Indent level: 3],
            "Reflectors": {
                # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CopilotTurret\Reflectors\cabin [Indent level: 4]
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
                    # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CopilotTurret\Reflectors\cabin\Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 50,
                        "hardLimitStart": 1,
                        "hardLimitEnd": 1.5
                    }
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CopilotTurret\Reflectors\cargo_light_1 [Indent level: 4],
                "cargo_light_1": {
                    "color": [830,100,100],
                    "position": "cargo_light_1",
                    "direction": "cargo_light_1_dir",
                    "hitpoint": "cargo_light_1",
                    "selection": "cargo_light_1",
                    "intensity": 21,
                    "useFlare": 0,
                    "coneFadeCoef": 0.1,
                    # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CopilotTurret\Reflectors\cargo_light_1\Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardLimitStart": 2,
                        "hardLimitEnd": 2.5
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
                # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CopilotTurret\Reflectors\cargo_light_2 [Indent level: 4],
                "cargo_light_2": {
                    "position": "cargo_light_2",
                    "direction": "cargo_light_2_dir",
                    "hitpoint": "cargo_light_2",
                    "selection": "cargo_light_2",
                    "color": [830,100,100],
                    "intensity": 21,
                    "useFlare": 0,
                    "coneFadeCoef": 0.1,
                    # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CopilotTurret\Reflectors\cargo_light_1\Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardLimitStart": 2,
                        "hardLimitEnd": 2.5
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
                # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CopilotTurret\Reflectors\cargo_light_3 [Indent level: 4],
                "cargo_light_3": {
                    "position": "cargo_light_3",
                    "direction": "cargo_light_3_dir",
                    "hitpoint": "cargo_light_3",
                    "selection": "cargo_light_3",
                    "color": [830,100,100],
                    "intensity": 21,
                    "useFlare": 0,
                    "coneFadeCoef": 0.1,
                    # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CopilotTurret\Reflectors\cargo_light_1\Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardLimitStart": 2,
                        "hardLimitEnd": 2.5
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
            "memoryPointsGetInGunnerPrecise": "GetIn_Turret",
            # Class: CfgVehicles\Heli_Transport_02_base_F\Turrets\CopilotTurret\ViewGunner [Indent level: 3],
            "ViewGunner": {
                "initFov": 1,
                "minFov": 0.3,
                "maxFov": 1.2,
                "initAngleX": 0,
                "minAngleX": -75,
                "maxAngleX": 85,
                "initAngleY": 0,
                "minAngleY": -170,
                "maxAngleY": 170,
                "minMoveX": -0.35,
                "maxMoveX": 0.35,
                "minMoveY": -0.025,
                "maxMoveY": 0.2,
                "minMoveZ": -0.3,
                "maxMoveZ": 0.55,
                "speedZoomMaxSpeed": 0,
                "speedZoomMaxFOV": 1
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\Turrets\CopilotTurret\Components [Indent level: 3],
            "Components": {
                # Class: CfgVehicles\Heli_Transport_02_base_F\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: VehicleSystemsTemplateLeftPilot\Components [Indent level: 0]
                    "Components": {
                        # Class: VehicleSystemsTemplateLeftPilot\Components\EmptyDisplay [Indent level: 1]
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\MinimapDisplay [Indent level: 1],
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\CrewDisplay [Indent level: 1],
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\SlingLoadDisplay [Indent level: 1],
                        "SlingLoadDisplay": {
                            "componentType": "SlingLoadDisplayComponent",
                            "resource": "RscCustomInfoSlingLoad"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\UAVDisplay [Indent level: 1],
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\VehicleDriverDisplay [Indent level: 1],
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\SensorDisplay [Indent level: 1],
                        "SensorDisplay": {
                            "componentType": "SensorsDisplayComponent",
                            "range": [4000,2000,16000,8000],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultDisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "VehicleSystemsDisplayManagerComponentRight": {
                    "defaultDisplay": "SensorDisplay",
                    # Class: VehicleSystemsTemplateRightPilot\Components [Indent level: 0],
                    "Components": {
                        # Class: VehicleSystemsTemplateRightPilot\Components\EmptyDisplay [Indent level: 1]
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\MinimapDisplay [Indent level: 1],
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\CrewDisplay [Indent level: 1],
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\SlingLoadDisplay [Indent level: 1],
                        "SlingLoadDisplay": {
                            "componentType": "SlingLoadDisplayComponent",
                            "resource": "RscCustomInfoSlingLoad"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\UAVDisplay [Indent level: 1],
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\VehicleDriverDisplay [Indent level: 1],
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\SensorDisplay [Indent level: 1],
                        "SensorDisplay": {
                            "componentType": "SensorsDisplayComponent",
                            "range": [4000,2000,16000,8000],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "showHMD": 1,
            "primaryGunner": 0,
            "body": "",
            "gun": "",
            "animationSourceBody": "",
            "animationSourceGun": "",
            "weapons": [],
            "magazines": [],
            "gunnerNotSpawned": 1,
            "minElev": -50,
            "maxElev": 30,
            "initElev": 11,
            "minTurn": -170,
            "maxTurn": 170,
            "initTurn": 0,
            "maxHorizontalRotSpeed": 3,
            "maxVerticalRotSpeed": 3,
            "turretCanSee": "1 + 2 + 4 + 8 + 32",
            "gunnerOpticsModel": "",
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\TurretSpec [Indent level: 3],
            "TurretSpec": {
                "showHeadPhones": 1
            },
            "startEngine": 0,
            "outGunnerMayFire": 1,
            "memoryPointGun": "machinegun",
            "memoryPointGunnerOptics": "gunnerview",
            "castGunnerShadow": 1,
            "viewGunnerShadow": 1,
            "gunnerForceOptics": 0,
            "enableManualFire": 0,
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\HitPoints [Indent level: 3],
            "HitPoints": {
                # Class: CfgVehicles\Helicopter\Turrets\MainTurret\HitPoints\HitTurret [Indent level: 4]
                "HitTurret": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "vez",
                    "visual": "vez",
                    "passThrough": 0.3
                },
                # Class: CfgVehicles\Helicopter\Turrets\MainTurret\HitPoints\HitGun [Indent level: 4],
                "HitGun": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "zbran",
                    "visual": "zbran",
                    "passThrough": 0.1
                }
            },
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
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
            "hasGunner": 1,
            "canUseScanners": 1,
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
            "gunnerUsesPilotView": 0,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "forceHideGunner": 0,
            "inGunnerMayFire": 1,
            "viewGunnerInExternal": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "LODTurnedIn": -1,
            "LODTurnedOut": -1,
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            "aggregateReflectors": [],
            # Class: CfgVehicles\AllVehicles\NewTurret\GunFire [Indent level: 2],
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
                # Class: WeaponFireGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponFireGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun\Table\T1 [Indent level: 1],
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun\Table\T2 [Indent level: 1],
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun\Table\T3 [Indent level: 1],
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun\Table\T4 [Indent level: 1],
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun\Table\T5 [Indent level: 1],
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun\Table\T6 [Indent level: 1],
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun\Table\T7 [Indent level: 1],
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun\Table\T8 [Indent level: 1],
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun\Table\T9 [Indent level: 1],
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun\Table\T10 [Indent level: 1],
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T11 [Indent level: 1],
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun\Table\T12 [Indent level: 1],
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T13 [Indent level: 1],
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T14 [Indent level: 1],
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun\Table\T15 [Indent level: 1],
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun\Table\T16 [Indent level: 1],
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun\Table\T17 [Indent level: 1],
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun\Table\T18 [Indent level: 1],
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun\Table\T19 [Indent level: 1],
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun\Table\T20 [Indent level: 1],
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun\Table\T21 [Indent level: 1],
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun\Table\T22 [Indent level: 1],
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds [Indent level: 2],
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
                # Class: WeaponCloudsGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds [Indent level: 2],
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
                # Class: WeaponCloudsMGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\Turrets [Indent level: 2],
            "Turrets": {
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics [Indent level: 2],
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
            "turretFollowFreeLook": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "dontCreateAI": 0,
            "disableSoundAttenuation": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn [Indent level: 2],
            "TurnIn": {
                "turnOffset": 0
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
            "TurnOut": {
                "turnOffset": 0
            },
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret [Indent level: 2],
        "MainTurret": {
            "isCopilot": 0,
            "body": "mainTurret",
            "gun": "mainGun",
            "minElev": -30,
            "maxElev": 30,
            "initElev": -10,
            "minTurn": 36,
            "maxTurn": 140,
            "initTurn": 0,
            "soundServo": ["",0.01,1],
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGun": "machinegun_1",
            "animationSourceHatch": "",
            "stabilizedInAxes": "StabilizedInAxesNone",
            "selectionFireAnim": "zasleh",
            "animationSourceBody": "MainTurret",
            "animationSourceGun": "MainGun",
            "gunBeg": "muzzle_1",
            "gunEnd": "chamber_1",
            "weapons": ["rhs_weap_m134_minigun_1"],
            "magazines": ["rhs_mag_762x51_m80a1_4000"],
            "gunnerName": "Crew Chief",
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "gunnerOutOpticsShowCursor": 1,
            "gunnerOpticsShowCursor": 1,
            "gunnerAction": "RHS_CH47_Gunner",
            "gunnerInAction": "RHS_CH47_Gunner",
            "gunnerLeftHandAnimName": "OtocHlaven",
            "gunnerRightHandAnimName": "OtocHlaven",
            "gunnerLeftLegAnimName": "gunner1_leg_left",
            "gunnerRightLegAnimName": "gunner1_leg_right",
            "gunnerForceOptics": 0,
            "commanding": -1,
            "primaryGunner": 1,
            "outGunnerMayFire": 1,
            # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\ViewOptics [Indent level: 3],
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.7,
                "minFov": 0.25,
                "maxFov": 1.1
            },
            "gunnerCompartments": "Compartment2",
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components [Indent level: 3],
            "Components": {
                # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components [Indent level: 5]
                    "Components": {
                        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay [Indent level: 6]
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay [Indent level: 6],
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultDisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "VehicleSystemsDisplayManagerComponentRight": {
                    "defaultDisplay": "SensorDisplay",
                    # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components [Indent level: 5],
                    "Components": {
                        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay [Indent level: 6]
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay [Indent level: 6],
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Hitpoints [Indent level: 3],
            "Hitpoints": {
            },
            "turretCanSee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\TurretSpec [Indent level: 3],
            "TurretSpec": {
                "showHeadPhones": 1
            },
            "startEngine": 0,
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "castGunnerShadow": 1,
            "viewGunnerShadow": 1,
            "enableManualFire": 0,
            "canEject": 0,
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerType": "",
            "primaryObserver": 0,
            "soundElevation": ["",0.00316228,1],
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
            "primary": 1,
            "hasGunner": 1,
            "canUseScanners": 1,
            # Class: CfgVehicles\AllVehicles\NewTurret\ViewGunner [Indent level: 2],
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
            "gunnerOpticsColor": [0,0,0,1],
            "turretInfoType": "",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOpticsEffect": [],
            "gunnerOutOpticsEffect": [],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "forceHideGunner": 0,
            "inGunnerMayFire": 1,
            "showHMD": 0,
            "viewGunnerInExternal": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "LODTurnedIn": -1,
            "LODTurnedOut": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors [Indent level: 2],
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles\AllVehicles\NewTurret\GunFire [Indent level: 2],
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
                # Class: WeaponFireGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponFireGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun\Table\T1 [Indent level: 1],
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun\Table\T2 [Indent level: 1],
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun\Table\T3 [Indent level: 1],
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun\Table\T4 [Indent level: 1],
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun\Table\T5 [Indent level: 1],
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun\Table\T6 [Indent level: 1],
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun\Table\T7 [Indent level: 1],
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun\Table\T8 [Indent level: 1],
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun\Table\T9 [Indent level: 1],
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun\Table\T10 [Indent level: 1],
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T11 [Indent level: 1],
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun\Table\T12 [Indent level: 1],
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T13 [Indent level: 1],
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T14 [Indent level: 1],
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun\Table\T15 [Indent level: 1],
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun\Table\T16 [Indent level: 1],
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun\Table\T17 [Indent level: 1],
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun\Table\T18 [Indent level: 1],
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun\Table\T19 [Indent level: 1],
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun\Table\T20 [Indent level: 1],
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun\Table\T21 [Indent level: 1],
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun\Table\T22 [Indent level: 1],
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds [Indent level: 2],
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
                # Class: WeaponCloudsGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds [Indent level: 2],
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
                # Class: WeaponCloudsMGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\Turrets [Indent level: 2],
            "Turrets": {
            },
            "forceNVG": 0,
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
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn [Indent level: 2],
            "TurnIn": {
                "turnOffset": 0
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
            "TurnOut": {
                "turnOffset": 0
            },
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\RightDoorGun [Indent level: 2],
        "RightDoorGun": {
            "isCopilot": 0,
            "body": "Turret2",
            "gun": "Gun_2",
            "minTurn": -140,
            "maxTurn": -36,
            "initTurn": 0,
            "animationSourceBody": "Turret_2",
            "animationSourceGun": "Gun_2",
            "stabilizedInAxes": "StabilizedInAxesNone",
            "selectionFireAnim": "zasleh_1",
            "proxyIndex": 2,
            "weapons": ["rhs_weap_m134_minigun_2"],
            "magazines": ["rhs_mag_762x51_m80a1_4000"],
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "gunnerOutOpticsShowCursor": 1,
            "gunnerOpticsShowCursor": 1,
            "gunnerName": "Door Gunner",
            "gunnerLeftHandAnimName": "otochlaven_2",
            "gunnerRightHandAnimName": "otochlaven_2",
            "gunnerLeftLegAnimName": "gunner2_leg_left",
            "gunnerRightLegAnimName": "gunner2_leg_right",
            "commanding": -2,
            "gunBeg": "muzzle_2",
            "gunEnd": "chamber_2",
            "primaryGunner": 0,
            "preciseGetInOut": 1,
            "memoryPointGun": "machinegun_2",
            "memoryPointGunnerOptics": "gunnerview_2",
            "gunnerCompartments": "Compartment2",
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "minElev": -30,
            "maxElev": 30,
            "initElev": -10,
            "soundServo": ["",0.01,1],
            "animationSourceHatch": "",
            "gunnerAction": "RHS_CH47_Gunner",
            "gunnerInAction": "RHS_CH47_Gunner",
            "gunnerForceOptics": 0,
            "outGunnerMayFire": 1,
            # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\ViewOptics [Indent level: 3],
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.7,
                "minFov": 0.25,
                "maxFov": 1.1
            },
            # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components [Indent level: 3],
            "Components": {
                # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components [Indent level: 5]
                    "Components": {
                        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay [Indent level: 6]
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay [Indent level: 6],
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultDisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "VehicleSystemsDisplayManagerComponentRight": {
                    "defaultDisplay": "SensorDisplay",
                    # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components [Indent level: 5],
                    "Components": {
                        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay [Indent level: 6]
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay [Indent level: 6],
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            # Class: CfgVehicles\RHS_CH_47F_base\Turrets\MainTurret\Hitpoints [Indent level: 3],
            "Hitpoints": {
            },
            "turretCanSee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\TurretSpec [Indent level: 3],
            "TurretSpec": {
                "showHeadPhones": 1
            },
            "startEngine": 0,
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "castGunnerShadow": 1,
            "viewGunnerShadow": 1,
            "enableManualFire": 0,
            "canEject": 0,
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "gunnerType": "",
            "primaryObserver": 0,
            "soundElevation": ["",0.00316228,1],
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
            "primary": 1,
            "hasGunner": 1,
            "canUseScanners": 1,
            # Class: CfgVehicles\AllVehicles\NewTurret\ViewGunner [Indent level: 2],
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
            "gunnerOpticsColor": [0,0,0,1],
            "turretInfoType": "",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOpticsEffect": [],
            "gunnerOutOpticsEffect": [],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "forceHideGunner": 0,
            "inGunnerMayFire": 1,
            "showHMD": 0,
            "viewGunnerInExternal": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "LODTurnedIn": -1,
            "LODTurnedOut": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors [Indent level: 2],
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles\AllVehicles\NewTurret\GunFire [Indent level: 2],
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
                # Class: WeaponFireGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponFireGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun\Table\T1 [Indent level: 1],
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun\Table\T2 [Indent level: 1],
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun\Table\T3 [Indent level: 1],
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun\Table\T4 [Indent level: 1],
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun\Table\T5 [Indent level: 1],
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun\Table\T6 [Indent level: 1],
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun\Table\T7 [Indent level: 1],
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun\Table\T8 [Indent level: 1],
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun\Table\T9 [Indent level: 1],
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun\Table\T10 [Indent level: 1],
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T11 [Indent level: 1],
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun\Table\T12 [Indent level: 1],
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T13 [Indent level: 1],
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T14 [Indent level: 1],
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun\Table\T15 [Indent level: 1],
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun\Table\T16 [Indent level: 1],
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun\Table\T17 [Indent level: 1],
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun\Table\T18 [Indent level: 1],
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun\Table\T19 [Indent level: 1],
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun\Table\T20 [Indent level: 1],
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun\Table\T21 [Indent level: 1],
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun\Table\T22 [Indent level: 1],
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds [Indent level: 2],
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
                # Class: WeaponCloudsGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds [Indent level: 2],
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
                # Class: WeaponCloudsMGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\Turrets [Indent level: 2],
            "Turrets": {
            },
            "forceNVG": 0,
            "gunnerDoor": "",
            "turretFollowFreeLook": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "dontCreateAI": 0,
            "disableSoundAttenuation": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn [Indent level: 2],
            "TurnIn": {
                "turnOffset": 0
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
            "TurnOut": {
                "turnOffset": 0
            },
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CargoTurret_01 [Indent level: 2],
        "CargoTurret_01": {
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "passenger_inside_1",
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "RHS_HIND_Cargo_Exit",
            "memoryPointsGetInGunner": "pos cargo L",
            "memoryPointsGetInGunnerDir": "pos cargo L dir",
            "gunnerName": "Passenger (Left Ramp)",
            "gunnerCompartments": "Compartment1",
            "proxyIndex": 21,
            "maxElev": 6,
            "minElev": -25,
            "maxTurn": -37,
            "minTurn": -95,
            "isPersonTurret": 1,
            "gunnerUsesPilotView": 1,
            "gunnerDoor": "Door_Cargo",
            "selectionFireAnim": "",
            "playerPosition": 2,
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            "memoryPointGunnerOptics": "",
            "enabledByAnimationSource": "ramp_anim",
            # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
            "Hitpoints": {
            },
            # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner [Indent level: 2],
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
            "animationSourceBody": "",
            "animationSourceGun": "",
            "body": "",
            "canEject": 1,
            "commanding": 0,
            "dontCreateAI": 1,
            "gun": "",
            "hideWeaponsGunner": 0,
            "isCopilot": 0,
            "primaryGunner": 0,
            "proxyType": "CPCargo",
            "startEngine": 0,
            "turretFollowFreeLook": 0,
            "viewGunnerInExternal": 1,
            "outGunnerMayFire": 1,
            "showAsCargo": 1,
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "gunnerType": "",
            "primaryObserver": 0,
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
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
            "LODTurnedIn": -1,
            "LODTurnedOut": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors [Indent level: 2],
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles\AllVehicles\NewTurret\GunFire [Indent level: 2],
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
                # Class: WeaponFireGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponFireGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun\Table\T1 [Indent level: 1],
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun\Table\T2 [Indent level: 1],
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun\Table\T3 [Indent level: 1],
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun\Table\T4 [Indent level: 1],
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun\Table\T5 [Indent level: 1],
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun\Table\T6 [Indent level: 1],
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun\Table\T7 [Indent level: 1],
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun\Table\T8 [Indent level: 1],
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun\Table\T9 [Indent level: 1],
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun\Table\T10 [Indent level: 1],
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T11 [Indent level: 1],
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun\Table\T12 [Indent level: 1],
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T13 [Indent level: 1],
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T14 [Indent level: 1],
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun\Table\T15 [Indent level: 1],
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun\Table\T16 [Indent level: 1],
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun\Table\T17 [Indent level: 1],
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun\Table\T18 [Indent level: 1],
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun\Table\T19 [Indent level: 1],
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun\Table\T20 [Indent level: 1],
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun\Table\T21 [Indent level: 1],
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun\Table\T22 [Indent level: 1],
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds [Indent level: 2],
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
                # Class: WeaponCloudsGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds [Indent level: 2],
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
                # Class: WeaponCloudsMGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\Turrets [Indent level: 2],
            "Turrets": {
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics [Indent level: 2],
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
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn [Indent level: 2],
            "TurnIn": {
                "turnOffset": 0
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
            "TurnOut": {
                "turnOffset": 0
            },
            "gunnerInAction": "ManActTestDriver",
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CargoTurret_02 [Indent level: 2],
        "CargoTurret_02": {
            "gunnerName": "Passenger (Right Ramp)",
            "memoryPointsGetInGunner": "pos cargo R",
            "memoryPointsGetInGunnerDir": "pos cargo R dir",
            "proxyIndex": 13,
            "maxTurn": 84,
            "minTurn": 37,
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "passenger_inside_1",
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "RHS_HIND_Cargo_Exit",
            "gunnerCompartments": "Compartment1",
            "maxElev": 6,
            "minElev": -25,
            "isPersonTurret": 1,
            "gunnerUsesPilotView": 1,
            "gunnerDoor": "Door_Cargo",
            "selectionFireAnim": "",
            "playerPosition": 2,
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            "memoryPointGunnerOptics": "",
            "enabledByAnimationSource": "ramp_anim",
            # Class: CfgVehicles\RHS_CH_47F_base\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
            "Hitpoints": {
            },
            # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner [Indent level: 2],
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
            "animationSourceBody": "",
            "animationSourceGun": "",
            "body": "",
            "canEject": 1,
            "commanding": 0,
            "dontCreateAI": 1,
            "gun": "",
            "hideWeaponsGunner": 0,
            "isCopilot": 0,
            "primaryGunner": 0,
            "proxyType": "CPCargo",
            "startEngine": 0,
            "turretFollowFreeLook": 0,
            "viewGunnerInExternal": 1,
            "outGunnerMayFire": 1,
            "showAsCargo": 1,
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "gunnerType": "",
            "primaryObserver": 0,
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
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
            "LODTurnedIn": -1,
            "LODTurnedOut": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors [Indent level: 2],
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles\AllVehicles\NewTurret\GunFire [Indent level: 2],
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
                # Class: WeaponFireGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponFireGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun\Table\T1 [Indent level: 1],
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun\Table\T2 [Indent level: 1],
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun\Table\T3 [Indent level: 1],
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun\Table\T4 [Indent level: 1],
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun\Table\T5 [Indent level: 1],
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun\Table\T6 [Indent level: 1],
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun\Table\T7 [Indent level: 1],
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun\Table\T8 [Indent level: 1],
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun\Table\T9 [Indent level: 1],
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun\Table\T10 [Indent level: 1],
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T11 [Indent level: 1],
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun\Table\T12 [Indent level: 1],
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T13 [Indent level: 1],
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T14 [Indent level: 1],
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun\Table\T15 [Indent level: 1],
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun\Table\T16 [Indent level: 1],
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun\Table\T17 [Indent level: 1],
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun\Table\T18 [Indent level: 1],
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun\Table\T19 [Indent level: 1],
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun\Table\T20 [Indent level: 1],
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun\Table\T21 [Indent level: 1],
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun\Table\T22 [Indent level: 1],
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds [Indent level: 2],
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
                # Class: WeaponCloudsGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds [Indent level: 2],
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
                # Class: WeaponCloudsMGun\Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\Turrets [Indent level: 2],
            "Turrets": {
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics [Indent level: 2],
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
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn [Indent level: 2],
            "TurnIn": {
                "turnOffset": 0
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
            "TurnOut": {
                "turnOffset": 0
            },
            "gunnerInAction": "ManActTestDriver",
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\Helicopter_Base_F\Turrets\NewTurret [Indent level: 2],
        "NewTurret": {
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\cargolights_hide [Indent level: 2]
        "cargolights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Gatling_1 [Indent level: 2],
        "Gatling_1": {
            "source": "revolving",
            "weapon": "rhs_weap_m134_minigun_1"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Gatling_2 [Indent level: 2],
        "Gatling_2": {
            "source": "revolving",
            "weapon": "rhs_weap_m134_minigun_2"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m134_minigun_1"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\muzzle_rot_hmg2 [Indent level: 2],
        "muzzle_rot_hmg2": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m134_minigun_2"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\ramp_anim [Indent level: 2],
        "ramp_anim": {
            "sound": "ServoRampSound_2",
            "soundPosition": "osa_ramp",
            "source": "user",
            "animPeriod": 5,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\hide_cargo [Indent level: 2],
        "hide_cargo": {
            "source": "user",
            "mass": -20,
            "displayName": "hide cargo benches",
            "animPeriod": 1e-005,
            "initPhase": 0,
            "onPhaseChanged": "(_this select 0) lockCargo ((_this select 1)==1)"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Damper_1_1_source [Indent level: 2],
        "Damper_1_1_source": {
            "source": "damper",
            "wheel": "Wheel_1_1"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Damper_1_2_source [Indent level: 2],
        "Damper_1_2_source": {
            "source": "damper",
            "wheel": "Wheel_1_2"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Damper_2_1_source [Indent level: 2],
        "Damper_2_1_source": {
            "source": "damper",
            "wheel": "Wheel_2_1"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Damper_2_2_source [Indent level: 2],
        "Damper_2_2_source": {
            "source": "damper",
            "wheel": "Wheel_2_2"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Wheel_1_1_source [Indent level: 2],
        "Wheel_1_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1_1"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Wheel_1_2_source [Indent level: 2],
        "Wheel_1_2_source": {
            "source": "wheel",
            "wheel": "Wheel_1_2"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Wheel_2_1_source [Indent level: 2],
        "Wheel_2_1_source": {
            "source": "wheel",
            "wheel": "Wheel_2_1"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Wheel_2_2_source [Indent level: 2],
        "Wheel_2_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2_2"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\AnimationSources\Helicopter_Brakes [Indent level: 2],
        "Helicopter_Brakes": {
            "source": "user",
            "animPeriod": 0.01,
            "initPhase": 1
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\CargoRamp_Open [Indent level: 2],
        "CargoRamp_Open": {
            "source": "door",
            "animPeriod": 5,
            "initPhase": 0,
            "sound": "ServoRampSound_2"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\Door_Back_L [Indent level: 2],
        "Door_Back_L": {
            "source": "door",
            "animPeriod": 0.6,
            "sound": "ServoDoorsSound"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\Door_Back_R [Indent level: 2],
        "Door_Back_R": {
            "source": "door",
            "animPeriod": 0.6,
            "sound": "ServoDoorsSound"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\AddGunHolder [Indent level: 2],
        "AddGunHolder": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\Gun_HRot [Indent level: 2],
        "Gun_HRot": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\Gun_VRot [Indent level: 2],
        "Gun_VRot": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass1"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass2"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass3 [Indent level: 2],
        "HitGlass3": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass3"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass4 [Indent level: 2],
        "HitGlass4": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass4"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass5 [Indent level: 2],
        "HitGlass5": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass5"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass6 [Indent level: 2],
        "HitGlass6": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass6"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass7 [Indent level: 2],
        "HitGlass7": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass7"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass8 [Indent level: 2],
        "HitGlass8": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass8"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass9 [Indent level: 2],
        "HitGlass9": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass9"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass10 [Indent level: 2],
        "HitGlass10": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass10"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass11 [Indent level: 2],
        "HitGlass11": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass11"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass12 [Indent level: 2],
        "HitGlass12": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass12"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass13 [Indent level: 2],
        "HitGlass13": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass13"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass14 [Indent level: 2],
        "HitGlass14": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass14"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass15 [Indent level: 2],
        "HitGlass15": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass15"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass16 [Indent level: 2],
        "HitGlass16": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass16"
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\AnimationSources\HitGlass17 [Indent level: 2],
        "HitGlass17": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass17"
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\AddCargoHook [Indent level: 2],
        "AddCargoHook": {
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 0,
            "isComponent": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\AddCargoHook_COver [Indent level: 2],
        "AddCargoHook_COver": {
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 1,
            "isComponent": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitHRotor [Indent level: 2],
        "HitHRotor": {
            "source": "hit",
            "hitpoint": "HitHRotor",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitVRotor [Indent level: 2],
        "HitVRotor": {
            "source": "hit",
            "hitpoint": "HitVRotor",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitEngine [Indent level: 2],
        "HitEngine": {
            "source": "hit",
            "hitpoint": "HitEngine",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitEngine2 [Indent level: 2],
        "HitEngine2": {
            "source": "hit",
            "hitpoint": "HitEngine2",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitBatteries [Indent level: 2],
        "HitBatteries": {
            "source": "hit",
            "hitpoint": "HitBatteries",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitTransmission [Indent level: 2],
        "HitTransmission": {
            "source": "hit",
            "hitpoint": "HitTransmission",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitHydraulics [Indent level: 2],
        "HitHydraulics": {
            "source": "hit",
            "hitpoint": "HitHydraulics",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitFuel [Indent level: 2],
        "HitFuel": {
            "source": "hit",
            "hitpoint": "HitFuel",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter\AnimationSources\HitEngine1 [Indent level: 2],
        "HitEngine1": {
            "source": "hit",
            "hitpoint": "HitEngine1",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter\AnimationSources\HitWinch_Source [Indent level: 2],
        "HitWinch_Source": {
            "source": "hit",
            "hitpoint": "HitWinch",
            "raw": 1
        },
        # Class: CfgVehicles\Air\AnimationSources\CollisionLightRed_source [Indent level: 2],
        "CollisionLightRed_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionRed"
        },
        # Class: CfgVehicles\Air\AnimationSources\CollisionLightWhite_source [Indent level: 2],
        "CollisionLightWhite_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionWhite"
        }
    },
    "gearUpTime": 1,
    "gearDownTime": 1,
    "backRotorForceCoef": 0.9,
    "mainRotorSpeed": 1,
    "backRotorSpeed": 1,
    "mainBladeRadius": 9.2,
    "liftForceCoef": 1.7,
    "cyclicAsideForceCoef": 1,
    "cyclicForwardForceCoef": 1,
    "bodyFrictionCoef": 0.9,
    "useRoadwayForVehicles": 1,
    "armor": 30,
    "armorStructural": 2,
    "damageResistance": 0.001,
    "driverLeftHandAnimName": "lever_pilot",
    "driverRightHandAnimName": "stick_pilot",
    "fuelCapacity": 3200,
    "fuelConsumptionRate": 0.398,
    "slingLoadMaxCargoMass": 12700,
    "canFloat": 1,
    "waterLeakiness": 0.02,
    "maxFordingDepth": 1.5,
    "waterResistanceCoef": 0.5,
    "waterResistance": 10,
    "waterLinearDampingCoefY": 5,
    "waterLinearDampingCoefX": 2,
    "waterAngularDampingCoef": 5,
    "memoryPointsGetInCargo": ["pos cargo"],
    "memoryPointsGetInCargoDir": ["pos cargo dir"],
    "cargoaction": ["RHS_CH47_Cargo01","RHS_CH47_Cargo01","RHS_CH47_Cargo01","RHS_CH47_Cargo02","RHS_CH47_Cargo03","RHS_CH47_Cargo01","RHS_CH47_Cargo03","RHS_CH47_Cargo02","RHS_CH47_Cargo01","RHS_CH47_Cargo03","RHS_CH47_Cargo02","RHS_CH47_Cargo03","RHS_CH47_Cargo02","RHS_CH47_Cargo03","RHS_CH47_Cargo01","RHS_CH47_Cargo02","RHS_CH47_Cargo01","RHS_CH47_Cargo03","RHS_CH47_Cargo02","RHS_CH47_Cargo01","RHS_CH47_Cargo03","RHS_CH47_Cargo02","RHS_CH47_Cargo01","RHS_CH47_Cargo03","RHS_CH47_Cargo02"],
    "cargoiscodriver": [0],
    "cargoCompartments": ["Compartment1"],
    "transportSoldier": 22,
    "cargoProxyIndexes": [1,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,22,23,24,25],
    "getInProxyOrder": [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],
    "transportMaxBackpacks": 10,
    "weapons": ["rhsusf_weap_ANALQ212"],
    "magazines": ["rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM"],
    "memoryPointCM": ["flare_launcher1","flare_launcher2"],
    "memoryPointCMDir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "selectionHRotorStill": "velka vrtule staticka",
    "selectionHRotorMove": "velka vrtule blur",
    "selectionVRotorStill": "mala vrtule staticka",
    "selectionVRotorMove": "mala vrtule blur",
    "selectionDamage": "trup",
    "selectionShowDamage": "poskozeni",
    "memoryPointLRocket": "l raketa",
    "memoryPointRRocket": "p raketa",
    "memoryPointLMissile": "l strela",
    "memoryPointRMissile": "p strela",
    "enableManualFire": 0,
    "threat": [0.8,1,0.6],
    "helmetMountedDisplay": 0,
    "cargoCanEject": 1,
    "driverCanEject": 0,
    # Class: CfgVehicles\RHS_CH_47F_base\MFD [Indent level: 1],
    "MFD": {
    },
    # Class: CfgVehicles\RHS_CH_47F_base\TransportMagazines [Indent level: 1],
    "TransportMagazines": {
        # Class: CfgVehicles\RHS_CH_47F_base\TransportMagazines\_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 12
        },
        # Class: CfgVehicles\RHS_CH_47F_base\TransportMagazines\_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 4
        },
        # Class: CfgVehicles\RHS_CH_47F_base\TransportMagazines\_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 2
        },
        # Class: CfgVehicles\RHS_CH_47F_base\TransportMagazines\_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 2
        },
        # Class: CfgVehicles\RHS_CH_47F_base\TransportMagazines\_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 4
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\TransportItems [Indent level: 1],
    "TransportItems": {
        # Class: CfgVehicles\RHS_CH_47F_base\TransportItems\_xx_FirstAidKit [Indent level: 2]
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles\RHS_CH_47F_base\TransportItems\_xx_Medikit [Indent level: 2],
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 2
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\TransportWeapons [Indent level: 1],
    "TransportWeapons": {
        # Class: CfgVehicles\RHS_CH_47F_base\TransportWeapons\_xx_rhs_weap_m4_carryhandle [Indent level: 2]
        "_xx_rhs_weap_m4_carryhandle": {
            "weapon": "rhs_weap_m4_carryhandle",
            "count": 2
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\TransportBackpacks [Indent level: 1],
    "TransportBackpacks": {
        # Class: CfgVehicles\RHS_CH_47F_base\TransportBackpacks\_xx_B_Parachute [Indent level: 2]
        "_xx_B_Parachute": {
            "backpack": "B_Parachute",
            "count": 4
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\HitPoints [Indent level: 1],
    "HitPoints": {
        # Class: CfgVehicles\RHS_CH_47F_base\HitPoints\HitVRotor [Indent level: 2]
        "HitVRotor": {
            "armor": 1,
            "material": 51,
            "name": "mala vrtule",
            "visual": "mala vrtule staticka",
            "passThrough": 0.5
        },
        # Class: CfgVehicles\RHS_CH_47F_base\HitPoints\HitHRotor [Indent level: 2],
        "HitHRotor": {
            "armor": 1,
            "material": 51,
            "name": "velka vrtule",
            "visual": "velka vrtule staticka",
            "passThrough": 0.5
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitHull [Indent level: 2],
        "HitHull": {
            "armor": 999,
            "visual": "zbytek",
            "minimalHit": 0.05,
            "depends": "Total",
            "radius": 0.01,
            "name": "hull_hit",
            "convexComponent": "hull_hit",
            "explosionShielding": 1,
            "material": 51,
            "passThrough": 1
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitFuel [Indent level: 2],
        "HitFuel": {
            "armor": 0.7,
            "radius": 0.125,
            "minimalHit": 0.05,
            "explosionShielding": 2,
            "name": "fuel_hit",
            "convexComponent": "fuel_hit",
            "visual": "zbytek",
            "material": 51,
            "passThrough": 1
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitAvionics [Indent level: 2],
        "HitAvionics": {
            "armor": 1.3,
            "radius": 0.25,
            "minimalHit": 0.05,
            "explosionShielding": 1.5,
            "visual": "podsvit pristroju",
            "name": "avionics_hit",
            "convexComponent": "avionics_hit",
            "material": 51,
            "passThrough": 1
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitEngine1 [Indent level: 2],
        "HitEngine1": {
            "armor": 0.7,
            "radius": 0.25,
            "name": "engine_1_hit",
            "explosionShielding": 3,
            "minimalHit": 0.1,
            "visual": "motor",
            "passThrough": 1,
            "convexComponent": "engine_1_hit",
            "material": 51
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitEngine2 [Indent level: 2],
        "HitEngine2": {
            "armor": 0.7,
            "minimalHit": 0.1,
            "name": "engine_2_hit",
            "convexComponent": "engine_2_hit",
            "radius": 0.25,
            "explosionShielding": 3,
            "visual": "motor",
            "passThrough": 1,
            "material": 51
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitEngine [Indent level: 2],
        "HitEngine": {
            "armor": 999,
            "radius": 0.05,
            "minimalHit": 1,
            "depends": "0.5 * (HitEngine1 + HitEngine2)",
            "name": "engine_hit",
            "convexComponent": "engine_hit",
            "explosionShielding": 1,
            "material": 51,
            "visual": "motor",
            "passThrough": 1
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "name": "glass1",
            "visual": "glass1",
            "radius": 0.37,
            "armor": 1,
            "explosionShielding": 2,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A [Indent level: 2],
        "HitGlass1A": {
            "armor": 999,
            "depends": "HitGlass1",
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1A\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects1A",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            },
            "name": "glass1",
            "visual": "glass1",
            "radius": 0.37,
            "explosionShielding": 2,
            "minimalHit": 0.025,
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B [Indent level: 2],
        "HitGlass1B": {
            "armor": 999,
            "depends": "HitGlass1",
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass1B\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects1B",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            },
            "name": "glass1",
            "visual": "glass1",
            "radius": 0.37,
            "explosionShielding": 2,
            "minimalHit": 0.025,
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "name": "glass2",
            "visual": "glass2",
            "radius": 0.37,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3 [Indent level: 2],
        "HitGlass3": {
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.25,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4 [Indent level: 2],
        "HitGlass4": {
            "name": "glass4",
            "visual": "glass4",
            "radius": 0.25,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5 [Indent level: 2],
        "HitGlass5": {
            "name": "glass5",
            "visual": "glass5",
            "radius": 0.34,
            "armor": 1,
            "explosionShielding": 2,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6 [Indent level: 2],
        "HitGlass6": {
            "name": "glass6",
            "visual": "glass6",
            "radius": 0.34,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7 [Indent level: 2],
        "HitGlass7": {
            "name": "glass7",
            "visual": "glass7",
            "radius": 0.34,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass7\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects7",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8 [Indent level: 2],
        "HitGlass8": {
            "name": "glass8",
            "visual": "glass8",
            "radius": 0.34,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9 [Indent level: 2],
        "HitGlass9": {
            "name": "glass9",
            "visual": "glass9",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10 [Indent level: 2],
        "HitGlass10": {
            "name": "glass10",
            "visual": "glass10",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11 [Indent level: 2],
        "HitGlass11": {
            "name": "glass11",
            "visual": "glass11",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass11\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects11",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12 [Indent level: 2],
        "HitGlass12": {
            "name": "glass12",
            "visual": "glass12",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass12\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects12",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13 [Indent level: 2],
        "HitGlass13": {
            "name": "glass13",
            "visual": "glass13",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass13\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects13",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14 [Indent level: 2],
        "HitGlass14": {
            "name": "glass14",
            "visual": "glass14",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass14\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects14",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15 [Indent level: 2],
        "HitGlass15": {
            "name": "glass15",
            "visual": "glass15",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass15\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects15",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16 [Indent level: 2],
        "HitGlass16": {
            "name": "glass16",
            "visual": "glass16",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass16\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects16",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17 [Indent level: 2],
        "HitGlass17": {
            "name": "glass17",
            "visual": "glass17",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects\BrokenGlass1 [Indent level: 4],
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects\BrokenGlass2 [Indent level: 4],
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects\BrokenGlass3 [Indent level: 4],
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects\BrokenGlass4 [Indent level: 4],
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects\BrokenGlass5 [Indent level: 4],
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects\BrokenGlass1S [Indent level: 4],
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects\BrokenGlass2S [Indent level: 4],
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects\BrokenGlass3S [Indent level: 4],
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects\BrokenGlass4S [Indent level: 4],
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_Transport_02_base_F\HitPoints\HitGlass17\DestructionEffects\BrokenGlass5S [Indent level: 4],
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5SS",
                    "position": "GlassEffects17",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                }
            }
        },
        # Class: CfgVehicles\Helicopter_Base_F\HitPoints\HitMissiles [Indent level: 2],
        "HitMissiles": {
            "name": "ammo_hit",
            "convexComponent": "ammo_hit",
            "explosionShielding": 1,
            "armor": 0.1,
            "material": 51,
            "visual": "munice",
            "passThrough": 0.5
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitRGlass [Indent level: 2],
        "HitRGlass": {
            "convexComponent": "sklo predni P",
            "explosionShielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni P",
            "visual": "sklo predni P",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitLGlass [Indent level: 2],
        "HitLGlass": {
            "convexComponent": "sklo predni L",
            "explosionShielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni L",
            "visual": "sklo predni L",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitEngine3 [Indent level: 2],
        "HitEngine3": {
            "name": "engine_3_hit",
            "convexComponent": "engine_3_hit",
            "explosionShielding": 1,
            "armor": 0.25,
            "material": 51,
            "visual": "motor",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitWinch [Indent level: 2],
        "HitWinch": {
            "armor": -40,
            "material": 51,
            "name": "slingLoad0",
            "visual": "",
            "passThrough": 0,
            "radius": 0.1,
            # Class: CfgVehicles\Helicopter\HitPoints\HitWinch\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Helicopter\HitPoints\HitWinch\DestructionEffects\Explo [Indent level: 4],
                "Explo": {
                    "simulation": "particles",
                    "type": "WinchDestructionExplo",
                    "position": "slingLoad0",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.06
                },
                # Class: CfgVehicles\Helicopter\HitPoints\HitWinch\DestructionEffects\Sparks [Indent level: 4],
                "Sparks": {
                    "simulation": "particles",
                    "type": "WinchDestructionSparks",
                    "position": "slingLoad0",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.1
                }
            }
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitTransmission [Indent level: 2],
        "HitTransmission": {
            "armor": 0.8,
            "material": -1,
            "name": "transmission",
            "passThrough": 0.8
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitLight [Indent level: 2],
        "HitLight": {
            "armor": 0.1,
            "material": -1,
            "name": "light",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitHydraulics [Indent level: 2],
        "HitHydraulics": {
            "armor": 0.8,
            "material": -1,
            "name": "hydraulics",
            "passThrough": 0.8
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitGear [Indent level: 2],
        "HitGear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitHStabilizerL1 [Indent level: 2],
        "HitHStabilizerL1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerL1",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitHStabilizerR1 [Indent level: 2],
        "HitHStabilizerR1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerR1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitVStabilizer1 [Indent level: 2],
        "HitVStabilizer1": {
            "armor": 0.8,
            "material": -1,
            "name": "VStabilizer1",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitTail [Indent level: 2],
        "HitTail": {
            "armor": 0.8,
            "material": -1,
            "name": "tail boom",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitPitotTube [Indent level: 2],
        "HitPitotTube": {
            "armor": 0.5,
            "material": -1,
            "name": "pitot tube",
            "passThrough": 0.2
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStaticPort [Indent level: 2],
        "HitStaticPort": {
            "armor": 0.1,
            "material": -1,
            "name": "static port",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStarter1 [Indent level: 2],
        "HitStarter1": {
            "armor": 0.1,
            "material": -1,
            "name": "starter1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStarter2 [Indent level: 2],
        "HitStarter2": {
            "armor": 0.1,
            "material": -1,
            "name": "starter2",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStarter3 [Indent level: 2],
        "HitStarter3": {
            "armor": 0.1,
            "material": -1,
            "name": "starter3",
            "passThrough": 0
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\Library [Indent level: 1],
    "Library": {
        "libTextDesc": "CH-47F"
    },
    "attenuationEffectType": "HeliAttenuation",
    "soundGetIn": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|close",0.316228,1],
    "soundGetOut": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|open",0.316228,1,40],
    "soundDammage": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|int-alarm_loop",0.562341,1],
    "soundEngineOnInt": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_start_int",0.1,1],
    "soundEngineOnExt": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_start_ext",0.562341,1,800],
    "soundEngineOffInt": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_stop_int",0.1,1],
    "soundEngineOffExt": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_stop_ext",0.562341,1,800],
    "occludeSoundsWhenIn": 0.562341,
    "obstructSoundsWhenIn": 0.316228,
    "soundLocked": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_1",0.1,1],
    "soundIncommingMissile": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_2",0.1,1],
    # Class: CfgVehicles\RHS_CH_47F_base\Sounds [Indent level: 1],
    "Sounds": {
        # Class: CfgVehicles\RHS_CH_47F_base\Sounds\Engine [Indent level: 2]
        "Engine": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_engine_high_ext",1,1,800],
            "frequency": "rotorSpeed",
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Sounds\RotorLowOut [Indent level: 2],
        "RotorLowOut": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_rotor_ext.ogg",8.16228,1,3500],
            "frequency": "rotorSpeed",
            "volume": "camPos*(0 max (rotorSpeed-0.1))",
            "cone": [1.8,3.14,2,0.09]
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Sounds\RotorHighOut [Indent level: 2],
        "RotorHighOut": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_rotor_forsage_ext",6.16228,1,2200],
            "frequency": "rotorSpeed",
            "volume": "camPos*10*(0 max (rotorThrust-0.95))",
            "cone": [1.8,3.14,2,0.09]
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Sounds\EngineIn [Indent level: 2],
        "EngineIn": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_engine_high_int",1.77828,1],
            "frequency": "rotorSpeed",
            "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Sounds\RotorLowIn [Indent level: 2],
        "RotorLowIn": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_rotor_ext.ogg",2.77828,1],
            "frequency": "rotorSpeed",
            "volume": "2*(1-camPos)*((rotorSpeed factor[0.3, 1.1]) min (rotorSpeed factor[1.1, 0.3]))"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Sounds\RotorHighIn [Indent level: 2],
        "RotorHighIn": {
            "sound": ["rhsusf|addons|rhsusf_a2port_air|data|sounds|CH47_rotor_forsage_int",2.77828,1],
            "frequency": "rotorSpeed",
            "volume": "(1-camPos)*3*(rotorThrust-0.9)"
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\MarkerLights [Indent level: 1],
    "MarkerLights": {
        # Class: CfgVehicles\RHS_CH_47F_base\MarkerLights\WhiteStill [Indent level: 2]
        "WhiteStill": {
            "name": "bily pozicni",
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "blinking": 1,
            "intensity": 75,
            "blinkingPattern": [0.1,0.09],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.2,
            "drawLightCenterSize": 0.04
        },
        # Class: CfgVehicles\RHS_CH_47F_base\MarkerLights\RedStill [Indent level: 2],
        "RedStill": {
            "name": "cerveny pozicni",
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 75,
            "drawLight": 1,
            "drawLightSize": 0.15,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0
        },
        # Class: CfgVehicles\RHS_CH_47F_base\MarkerLights\GreenStill [Indent level: 2],
        "GreenStill": {
            "name": "zeleny pozicni",
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "intensity": 75,
            "drawLight": 1,
            "drawLightSize": 0.15,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0
        },
        # Class: CfgVehicles\RHS_CH_47F_base\MarkerLights\RedBlinking [Indent level: 2],
        "RedBlinking": {
            "name": "bily pozicni blik",
            "color": [0.09,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 75,
            "blinking": 1,
            "blinkingPattern": [0.1,0.09],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.2,
            "drawLightCenterSize": 0.04
        },
        # Class: CfgVehicles\RHS_CH_47F_base\MarkerLights\WhiteBlinking [Indent level: 2],
        "WhiteBlinking": {
            "name": "cerveny pozicni blik",
            "color": [0.09,0.15,0.1],
            "intensity": 75,
            "ambient": [0.09,0.015,0.01],
            "blinking": 1,
            "blinkingPattern": [0.2,1.3],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.08
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles\RHS_CH_47F_base\Reflectors\Middle [Indent level: 2]
        "Middle": {
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100,0],
            "position": "svetlo",
            "direction": "svetlo konec",
            "hitpoint": "svetlo",
            "selection": "svetlo",
            "size": 1,
            "innerAngle": 20,
            "outerAngle": 60,
            "coneFadeCoef": 10,
            "intensity": 50,
            "useFlare": 1,
            "dayLight": 0,
            "FlareSize": 6,
            # Class: CfgVehicles\RHS_CH_47F_base\Reflectors\Middle\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 4
            }
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles\RHS_CH_47F_base\Exhausts\Exhaust1 [Indent level: 2]
        "Exhaust1": {
            "direction": "exhaust1_dir",
            "effect": "ExhaustEffectHeli",
            "position": "exhaust1"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Exhausts\Exhaust2 [Indent level: 2],
        "Exhaust2": {
            "direction": "exhaust2_dir",
            "effect": "ExhaustEffectHeli",
            "position": "exhaust2"
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\Damage [Indent level: 1],
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1_int.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1_int.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_1_int_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2_int.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2_int.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_2_int_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo_in.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|CH47|data|ch47_sklo_damage.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    "irScanRangeMin": 0,
    "irScanRangeMax": 1000,
    "irScanToEyeFactor": 2,
    "gunnerCanSee": "2+4+8+16",
    "driverCanSee": "2+4+8+16",
    "hiddenSelections": ["camo1","camo2","camo3","camo4"],
    "hiddenSelectionsTextures": ["rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_1_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_2_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47f_nalepky_ca.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_mlod_co.paa"],
    # Class: CfgVehicles\RHS_CH_47F_base\textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles\RHS_CH_47F_base\textureSources\standard [Indent level: 2]
        "standard": {
            "displayName": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_1_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_2_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47f_nalepky_ca.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_mlod_co.paa"],
            "factions": ["rhs_faction_usarmy_wd","rhs_faction_usarmy_d"]
        },
        # Class: CfgVehicles\RHS_CH_47F_base\textureSources\Desert [Indent level: 2],
        "Desert": {
            "displayName": "Desert",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_1_light_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_2_light_co.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47f_nalepky_ca.paa","rhsusf|addons|rhsusf_a2port_air|ch47|data|ch47_ext_light_mlod_co.paa"],
            "factions": ["rhs_faction_usarmy_wd","rhs_faction_usarmy_d"]
        }
    },
    "textureList": [],
    # Class: CfgVehicles\RHS_CH_47F_base\Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles\RHS_CH_47F_base\Attributes\ObjectTexture [Indent level: 2]
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Attributes\ramp_anim [Indent level: 2],
        "ramp_anim": {
            "displayName": "Open ramp",
            "property": "ramp_anim",
            "control": "slider",
            "defaultValue": "0",
            "expression": "_this animateSource ['%s',_value,true]"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Attributes\hide_cargo [Indent level: 2],
        "hide_cargo": {
            "displayName": "Hide cargo benches",
            "property": "hide_cargo",
            "control": "CheckboxNumber",
            "expression": "_this animate ['%s',_value,true];_this lockCargo (_value == 1)",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\RHS_CH_47F_base\Attributes\rhs_attachCargo [Indent level: 2],
        "rhs_attachCargo": {
            "displayName": "Attach cargo",
            "tooltip": "Attaching cargo (using attachTo command) just like when you use ramp action",
            "property": "rhs_attachCargo",
            "expression": "if(_value == 1)then{[_this] spawn rhs_fnc_cargoAttach}else{{if(not(_x isKindOf 'Man'))then{detach _x}}foreach attachedObjects _this};",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        }
    },
    # Class: CfgVehicles\RHS_CH_47F_base\VehicleTransport [Indent level: 1],
    "VehicleTransport": {
        # Class: CfgVehicles\RHS_CH_47F_base\VehicleTransport\Carrier [Indent level: 2]
        "Carrier": {
            "cargoBayDimensions": ["VTV_limit_1","VTV_limit_2"],
            "disableHeightLimit": 1,
            "maxLoadMass": 9000,
            "cargoAlignment": ["front","center"],
            "cargoSpacing": [0.075,0.075,0.075],
            "exits": ["VTV_exit_1"],
            "unloadingInterval": 2,
            "loadingDistance": 15,
            "loadingAngle": 60,
            "parachuteClassDefault": "B_Parachute_02_F",
            "parachuteHeightLimitDefault": 25
        }
    },
    "ace_refuel_fuelCapacity": 3914,
    "features": "Randomization: No						<br />Camo selections: 3 - main body, tail various attachments, engine						<br />Script door sources: CargoRamp_Open, Door_Back_L, Door_Back_R						<br />Script animations: None						<br />Executed scripts: None						<br />Firing from vehicles: No						<br />Slingload: Slingloads up to 4000 kg						<br />Cargo proxy indexes: 1 to 16",
    "_generalMacro": "Heli_Transport_02_base_F",
    "editorSubcategory": "EdSubcat_Helicopters",
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "usePreciseGetInAction": 0,
    "memoryPointsGetInDriverPrecise": "GetIn_Pilot",
    "memoryPointsGetInCargoPrecise": ["GetIn_Cargo"],
    "getInRadius": 1.7,
    "preciseGetInOut": 0,
    "cargoPreciseGetInOut": [0],
    "getInAction": "GetInLow",
    "getOutAction": "GetOutLow",
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "driverDoor": "",
    "cargoDoors": [],
    "castCargoShadow": 1,
    "hideWeaponsCargo": 1,
    "ejectDeadCargo": 0,
    "maximumLoad": 5000,
    "supplyRadius": -0.3,
    "cost": 700000,
    "tailBladeRadius": 1.5,
    "enableSweep": 0,
    "extCameraPosition": [0,5,-30],
    # Class: CfgVehicles\Heli_Transport_02_base_F\ViewPilot [Indent level: 1],
    "ViewPilot": {
        "initFov": 1,
        "minFov": 0.3,
        "maxFov": 1.2,
        "initAngleX": 0,
        "minAngleX": -75,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -170,
        "maxAngleY": 170,
        "minMoveX": -0.35,
        "maxMoveX": 0.35,
        "minMoveY": -0.025,
        "maxMoveY": 0.2,
        "minMoveZ": -0.3,
        "maxMoveZ": 0.55,
        "speedZoomMaxSpeed": 0,
        "speedZoomMaxFOV": 1
    },
    "emptySound": ["",0,1],
    "soundGeneralCollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_1",1,1,100],
    "soundGeneralCollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_2",1,1,100],
    "soundGeneralCollision3": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_3",1,1,100],
    "soundCrashes": ["soundGeneralCollision1",0.33,"soundGeneralCollision2",0.33,"soundGeneralCollision3",0.33],
    "soundLandCrashes": ["emptySound",0],
    "soundBuildingCrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundArmorCrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundWoodCrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundBushCollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_1",1,1,100],
    "soundBushCollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_2",1,1,100],
    "soundBushCollision3": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_3",1,1,100],
    "soundBushCrash": ["soundBushCollision1",0.33,"soundBushCollision2",0.33,"soundBushCollision3",0.33],
    "soundWaterCollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_water_ext_1",1,1,100],
    "soundWaterCollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_water_ext_2",1,1,100],
    "soundWaterCrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "rotorDamageInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|heli_damage_rotor_int.ogg",0.75,1],
    "rotorDamageOut": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|heli_damage_rotor_ext.ogg",2,1,300],
    "rotorDamage": ["rotordamageint","rotordamageout"],
    "tailDamageInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|heli_damage_tail.ogg",0.75,1],
    "tailDamageOut": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|heli_damage_tail.ogg",2,1,300],
    "tailDamage": ["taildamageint","taildamageout"],
    "landingSoundInt0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|landing_skids_int1_open.ogg",0.75,1],
    "landingSoundInt1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|landing_skids_int1_open.ogg",0.75,1],
    "landingSoundInt": ["landingsoundint0",0.5,"landingsoundint1",0.5],
    "landingSoundOut0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|landing_skids_ext1.ogg",1,1,300],
    "landingSoundOut1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|landing_skids_ext1.ogg",1,1,300],
    "landingSoundOut": ["landingsoundout0",0.5,"landingsoundout1",0.5],
    "slingCargoAttach0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|sl_1hooklock.ogg",1.35,1],
    "slingCargoAttach1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|sl_1hooklock.ogg",1,1,300],
    "slingCargoAttach": ["slingcargoattach0","slingcargoattach1"],
    "slingCargoDetach0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|sl_1hookunlock.ogg",1.5,1],
    "slingCargoDetach1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|sl_1hookunlock.ogg",1,1,300],
    "slingCargoDetach": ["slingcargodetach0","slingcargodetach1"],
    "slingCargoDetachAir0": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_int",1,1],
    "slingCargoDetachAir1": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_ext",1,1,300],
    "slingCargoDetachAir": ["slingCargoDetach0","slingCargoDetach1"],
    "slingCargoRopeBreak0": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_int",1,1],
    "slingCargoRopeBreak1": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_ext",1,1,200],
    "slingCargoRopeBreak": ["slingCargoDetach0","slingCargoDetach1"],
    "gearUpExt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|gear_up_out.ogg",1.5,1,700],
    "gearUpInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|gear_up_in.ogg",1.5,1],
    "gearUp": ["gearupint","gearupext"],
    "gearDownInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|gear_down_in.ogg",1.5,1],
    "gearDownExt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|gear_down_out.ogg",1.5,1,700],
    "gearDown": ["geardownint","geardownext"],
    # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt [Indent level: 1],
    "SoundsExt": {
        # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\SoundEvents [Indent level: 2]
        "SoundEvents": {
        },
        # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds [Indent level: 2],
        "Sounds": {
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\EngineExt [Indent level: 3]
            "EngineExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|ch49_mohawk|engine_close.ogg",1.5,1,300],
                "frequency": "rotorspeed",
                "volume": "campos *1.5* (rotorspeed factor [0.6, 1]) * (1 + rotorthrust)"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\RotorExt [Indent level: 3],
            "RotorExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|ch49_mohawk|rotor_close.ogg",1.6,1,300],
                "cone": [1.6,3.14,1.6,0.95],
                "frequency": "(rotorspeed factor [0.3, 0.7]) * (rotorspeed factor [0.3, 1]) * (1 - rotorthrust/4)",
                "volume": "campos *1.5* (rotorspeed factor [0.6, 1]) * (1 + rotorthrust)"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\RotorNoiseExt [Indent level: 3],
            "RotorNoiseExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|rotor|rotor_normal.ogg",0.5,1,200],
                "cone": [1.6,3.14,2,0.95],
                "frequency": 1,
                "volume": "(campos*(rotorspeed factor [0.6, 0.85]))"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\EngineInt [Indent level: 3],
            "EngineInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|ch49_mohawk|int_main.ogg",1,1],
                "frequency": "rotorspeed",
                "volume": "1*(1-campos)*(0 max (rotorspeed-0.4))"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\RotorInt [Indent level: 3],
            "RotorInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|ch49_mohawk|int_rotor.ogg",1,1],
                "frequency": "(rotorspeed factor [0.3, 0.7]) * (rotorspeed factor [0.3, 1]) * (1 - rotorthrust/4)",
                "volume": "(1 - campos) * (rotorspeed factor [0.3, 0.7]) * (1 + rotorthrust) * 0.7"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\TransmissionDamageExt_phase1 [Indent level: 3],
            "TransmissionDamageExt_phase1": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|heli_damage_transmission_int_1.ogg",1,1,300],
                "frequency": "0.66 + rotorspeed / 3",
                "volume": "campos * (transmissiondamage factor [0.3, 0.35]) * (transmissiondamage factor [0.5, 0.45]) * (rotorspeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\TransmissionDamageExt_phase2 [Indent level: 3],
            "TransmissionDamageExt_phase2": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|heli_damage_transmission_int_1.ogg",1,1,300],
                "frequency": "0.66 + rotorspeed / 3",
                "volume": "campos * (transmissiondamage factor [0.45, 0.5]) * (rotorspeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\TransmissionDamageInt_phase1 [Indent level: 3],
            "TransmissionDamageInt_phase1": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|heli_damage_transmission_int_1.ogg",0.75,1],
                "frequency": "0.66 + rotorspeed / 3",
                "volume": "(1 - campos) * (transmissiondamage factor [0.3, 0.35]) * (transmissiondamage factor [0.5, 0.45]) * (rotorspeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\TransmissionDamageInt_phase2 [Indent level: 3],
            "TransmissionDamageInt_phase2": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|heli_damage_transmission_int_1.ogg",0.75,1],
                "frequency": "0.66 + rotorspeed / 3",
                "volume": "(1 - campos) * (transmissiondamage factor [0.45, 0.5]) * (rotorspeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\damageAlarmInt [Indent level: 3],
            "damageAlarmInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|damagealarm.ogg",0.75,1],
                "frequency": 1,
                "volume": "engineon * (1 - campos) * ( 1 - ((transmissiondamage factor [0.61, 0.60]) * (motordamage factor [0.61, 0.60]) * (rotordamage factor [0.51, 0.50]))) * (rotorspeed factor [0.0, 0.001])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\damageAlarmExt [Indent level: 3],
            "damageAlarmExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|damagealarm.ogg",1,1,100],
                "frequency": 1,
                "volume": "engineon * campos * ( 1 - ((transmissiondamage factor [0.61, 0.60]) * (motordamage factor [0.61, 0.60]) * (rotordamage factor [0.51, 0.50]))) * (rotorspeed factor [0, 0.001])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\rotorLowAlarmInt [Indent level: 3],
            "rotorLowAlarmInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|lowrotoralarmint.ogg",0.75,1],
                "frequency": 1,
                "volume": "engineon * (1 - campos) * (rotorspeed factor [0.9, 0.8999]) * (rotorspeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\rotorLowAlarmExt [Indent level: 3],
            "rotorLowAlarmExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|lowrotoralarmint.ogg",1,1,75],
                "frequency": 1,
                "volume": "engineon * campos * (rotorspeed factor [0.9, 0.8999]) * (rotorspeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\scrubLandInt [Indent level: 3],
            "scrubLandInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|scrublandint_open.ogg",0.75,1],
                "frequency": 1,
                "volume": "2 * (1-campos) * (scrubland factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\scrubLandExt [Indent level: 3],
            "scrubLandExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|scrublandext.ogg",1,1,500],
                "frequency": 1,
                "volume": "campos * (scrubland factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\scrubBuildingInt [Indent level: 3],
            "scrubBuildingInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|scrubbuilding.ogg",0.75,1],
                "frequency": 1,
                "volume": "2 * (1 - campos) * (scrubbuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\scrubBuildingExt [Indent level: 3],
            "scrubBuildingExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|scrubbuilding.ogg",1,1,500],
                "frequency": 1,
                "volume": "campos * (scrubbuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\scrubTreeInt [Indent level: 3],
            "scrubTreeInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|scrubtree.ogg",0.75,1],
                "frequency": 1,
                "volume": "(1 - campos) * ((scrubtree) factor [0, 0.01])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\scrubTreeExt [Indent level: 3],
            "scrubTreeExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|scrubtree.ogg",1,1,500],
                "frequency": 1,
                "volume": "campos * (scrubtree factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\RainExt [Indent level: 3],
            "RainExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|rain1_ext.ogg",1,1,100],
                "frequency": 1,
                "volume": "campos * (rain - rotorspeed/2) * 2"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\RainInt [Indent level: 3],
            "RainInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|rain1_int_open.ogg",0.5,1],
                "frequency": 1,
                "volume": "(1-campos)*(rain - rotorspeed/2)*2"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\SlingLoadDownExt [Indent level: 3],
            "SlingLoadDownExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|sl_enginedownext.ogg",1,1,500],
                "frequency": 1,
                "volume": "campos*(slingloadactive factor [0,-1])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\SlingLoadUpExt [Indent level: 3],
            "SlingLoadUpExt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|sl_engineupext.ogg",1,1,500],
                "frequency": 1,
                "volume": "campos*(slingloadactive factor [0,1])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\SlingLoadDownInt [Indent level: 3],
            "SlingLoadDownInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|sl_enginedownint.ogg",0.75,1],
                "frequency": 1,
                "volume": "(1-campos)*(slingloadactive factor [0,-1])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\SlingLoadUpInt [Indent level: 3],
            "SlingLoadUpInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|sl_engineupint.ogg",0.75,1],
                "frequency": 1,
                "volume": "(1-campos)*(slingloadactive factor [0,1])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\WindInt [Indent level: 3],
            "WindInt": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|wind_close_in.ogg",0.5,1],
                "frequency": 1,
                "volume": "(1-campos)*(speed factor[5, 50])*(speed factor[5, 50])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\GStress [Indent level: 3],
            "GStress": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|vehicle_stress2b.ogg",0.75,1],
                "frequency": 1,
                "volume": "engineon * (1-campos) * ((gmeterz factor[1.5, 2.5]) + (gmeterz factor[0.5, -0.5]))"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\SpeedStress [Indent level: 3],
            "SpeedStress": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|vehicle_stress2b.ogg",0.75,1],
                "frequency": 1,
                "volume": "(1-campos)*(speed factor[40,80])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\rotorswist [Indent level: 3],
            "rotorswist": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|ch49_mohawk|tail_rotor.ogg",1,1,200],
                "frequency": 1,
                "volume": "campos * (rotorthrust factor [0.7, 0.9])"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\rotorbench [Indent level: 3],
            "rotorbench": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|rotor|rotor_normal.ogg",0.5,1],
                "frequency": "(rotorspeed factor [0.3, 0.7]) * (rotorspeed factor [0.3, 1]) * (1 - rotorthrust/4)",
                "volume": "(playerpos factor [3.9, 4]) * (1 - campos) * (rotorspeed factor [0.3, 1]) * (1 + rotorthrust) * 0.4",
                "cone": [1.6,3.14,1.6,0.95]
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\enginebench [Indent level: 3],
            "enginebench": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|rotor|rotor_normal.ogg",0.5,1],
                "frequency": "rotorspeed",
                "volume": "(playerpos factor [3.9, 4]) * (1 - campos) * (0 max (rotorspeed-0.4))"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\distance [Indent level: 3],
            "distance": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|ch49_mohawk|engine_far.ogg",1,1,1000],
                "frequency": "rotorspeed",
                "volume": "2 * campos * (0 max (rotorspeed-0.4))"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\fardistance [Indent level: 3],
            "fardistance": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|ch49_mohawk|rotor_far.ogg",1,1,4000],
                "frequency": "rotorspeed",
                "volume": "campos *3* (rotorspeed factor [0.6, 1]) * (1 + rotorthrust)"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\windbench [Indent level: 3],
            "windbench": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|wind_close_in.ogg",0.5,1],
                "frequency": 1,
                "volume": "4 * (playerpos factor [3.9, 4]) * (1 - campos) * ((speed factor[0, 30]) + (speed factor[0, -30]))"
            },
            # Class: CfgVehicles\Heli_Transport_02_base_F\SoundsExt\Sounds\windlateralmovementint [Indent level: 3],
            "windlateralmovementint": {
                "sound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|air_vehicles|shared|wind_close_in.ogg",0.5,1,50],
                "frequency": 1,
                "volume": "(1-campos)*lateralmovement*((speed factor [5,40]) + (speed factor [-5,-40]))"
            }
        }
    },
    # Class: CfgVehicles\Heli_Transport_02_base_F\Armory [Indent level: 1],
    "Armory": {
        "description": "A successor to the wide-spread Merlin helicopter, the CH-49 Mohawk is a primary transport used by the AAF. It can carry up to 16 soldiers plus crew. Besides the transport version, many other versions of the Mohawk exist, serving as evac, anti-submarine warfare or armed air support. Upgrades over its predecessor consist of more powerful engines and construction changes fully utilizing modern materials."
    },
    "memoryPointDriverOptics": "slingCamera",
    "tf_isolatedAmount": 0.8,
    "ace_cargo_space": 20,
    # Class: CfgVehicles\Helicopter_Base_H\PilotSpec [Indent level: 1],
    "PilotSpec": {
        "showHeadPhones": 1
    },
    # Class: CfgVehicles\Helicopter_Base_H\CargoSpec [Indent level: 1],
    "CargoSpec": {
        # Class: CfgVehicles\Helicopter_Base_H\CargoSpec\Cargo1 [Indent level: 2]
        "Cargo1": {
            "showHeadPhones": 1
        }
    },
    "transportMaxWeapons": 12,
    "transportMaxMagazines": 48,
    "memoryPointSupply": "doplnovani",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "washDownStrength": "1.0f",
    "washDownDiameter": "40.0f",
    "minSmokeDamage": 0.3,
    "maxSmokeDamage": 0.99,
    "driverLeftLegAnimName": "pedalL",
    "driverRightLegAnimName": "pedalR",
    # Class: CfgVehicles\Helicopter_Base_F\CamShake [Indent level: 1],
    "CamShake": {
        "power": 30,
        "frequency": 20,
        "distance": 50,
        "minSpeed": 50
    },
    "camShakeCoef": 0,
    # Class: CfgVehicles\Helicopter_Base_F\EventHandlers [Indent level: 1],
    "EventHandlers": {
        "fired": "",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers [Indent level: 0],
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        },
        # Class: DefaultEventHandlers\CBA_Extended_EventHandlers [Indent level: 0],
        "CBA_Extended_EventHandlers": {
            "init": "call cba_xeh_fnc_init",
            "fired": "call cba_xeh_fnc_fired",
            "animChanged": "call cba_xeh_fnc_animChanged",
            "animDone": "call cba_xeh_fnc_animDone",
            "animStateChanged": "call cba_xeh_fnc_animStateChanged",
            "containerClosed": "call cba_xeh_fnc_containerClosed",
            "containerOpened": "call cba_xeh_fnc_containerOpened",
            "controlsShifted": "call cba_xeh_fnc_controlsShifted",
            "dammaged": "call cba_xeh_fnc_dammaged",
            "engine": "call cba_xeh_fnc_engine",
            "epeContact": "call cba_xeh_fnc_epeContact",
            "epeContactEnd": "call cba_xeh_fnc_epeContactEnd",
            "epeContactStart": "call cba_xeh_fnc_epeContactStart",
            "explosion": "call cba_xeh_fnc_explosion",
            "firedNear": "call cba_xeh_fnc_firedNear",
            "fuel": "call cba_xeh_fnc_cba_xeh_fuel",
            "gear": "call cba_xeh_fnc_gear",
            "getIn": "call cba_xeh_fnc_getIn",
            "getInMan": "call cba_xeh_fnc_getInMan",
            "getOut": "call cba_xeh_fnc_getOut",
            "getOutMan": "call cba_xeh_fnc_getOutMan",
            "handleHeal": "call cba_xeh_fnc_handleHeal",
            "hit": "call cba_xeh_fnc_hit",
            "hitPart": "call cba_xeh_fnc_hitPart",
            "incomingMissile": "call cba_xeh_fnc_incomingMissile",
            "inventoryClosed": "call cba_xeh_fnc_inventoryClosed",
            "inventoryOpened": "call cba_xeh_fnc_inventoryOpened",
            "killed": "call cba_xeh_fnc_killed",
            "landedTouchDown": "call cba_xeh_fnc_landedTouchDown",
            "landedStopped": "call cba_xeh_fnc_landedStopped",
            "local": "call cba_xeh_fnc_local",
            "respawn": "call cba_xeh_fnc_respawn",
            "put": "call cba_xeh_fnc_put",
            "take": "call cba_xeh_fnc_take",
            "seatSwitched": "call cba_xeh_fnc_seatSwitched",
            "seatSwitchedMan": "call cba_xeh_fnc_seatSwitchedMan",
            "soundPlayed": "call cba_xeh_fnc_soundPlayed",
            "weaponAssembled": "call cba_xeh_fnc_weaponAssembled",
            "weaponDisassembled": "call cba_xeh_fnc_weaponDisassembled",
            "weaponDeployed": "call cba_xeh_fnc_weaponDeployed",
            "weaponRested": "call cba_xeh_fnc_weaponRested",
            "reloaded": "call cba_xeh_fnc_reloaded",
            "firedMan": "call cba_xeh_fnc_firedMan",
            "turnIn": "call cba_xeh_fnc_turnIn",
            "turnOut": "call cba_xeh_fnc_turnOut",
            "deleted": "call cba_xeh_fnc_deleted"
        }
    },
    "simulation": "helicopterrtd",
    "unitInfoTypeLite": "RscUnitInfoAirRTDBasic",
    # Class: CfgVehicles\Helicopter_Base_F\ACE_Actions [Indent level: 1],
    "ACE_Actions": {
        # Class: CfgVehicles\Helicopter_Base_F\ACE_Actions\ACE_MainActions [Indent level: 2]
        "ACE_MainActions": {
            "displayName": "Interactions",
            "position": "[_target,ace_interact_menu_cameraPosASL] call ace_interaction_fnc_getVehiclePosComplex",
            "selection": "",
            "distance": 4,
            "condition": "true",
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\ACE_Passengers [Indent level: 3],
            "ACE_Passengers": {
                "displayName": "Passengers",
                "condition": "alive _target",
                "statement": "",
                "exceptions": ["isNotSwimming"],
                "insertChildren": "_this call ace_interaction_fnc_addPassengersActions"
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\ace_quickmount_GetIn [Indent level: 3],
            "ace_quickmount_GetIn": {
                "displayName": "Get In",
                "condition": "call ace_quickmount_fnc_canShowFreeSeats",
                "statement": "call ace_quickmount_fnc_getInNearest",
                "exceptions": ["isNotSwimming"],
                "insertChildren": "(_this select 2) param [0,[]]"
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\ace_rearm_Rearm [Indent level: 3],
            "ace_rearm_Rearm": {
                "displayName": "Rearm",
                "distance": 9,
                "condition": "_this call ace_rearm_fnc_canRearm",
                "statement": "_this call ace_rearm_fnc_rearm",
                "exceptions": ["isNotInside"],
                "icon": "z|ace|addons|rearm|ui|icon_rearm_interact.paa"
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\ace_repair_Repair [Indent level: 3],
            "ace_repair_Repair": {
                "displayName": "Repair",
                "condition": "true",
                "statement": "",
                "runOnHover": 1,
                "showDisabled": 0,
                "icon": "A3|ui_f|data|igui|cfg|actions|repair_ca.paa",
                "distance": 4,
                "exceptions": ["isNotSwimming","isNotOnLadder"]
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\ACE_unlockVehicle [Indent level: 3],
            "ACE_unlockVehicle": {
                "displayName": "Unlock Vehicle",
                "distance": 4,
                "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [2, 3]}",
                "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,false],[_target]] call CBA_fnc_targetEvent",
                "exceptions": ["isNotSwimming"],
                "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\ACE_lockVehicle [Indent level: 3],
            "ACE_lockVehicle": {
                "displayName": "Lock Vehicle",
                "distance": 4,
                "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [0, 1]}",
                "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,true],[_target]] call CBA_fnc_targetEvent",
                "exceptions": ["isNotSwimming"],
                "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\ACE_lockpickVehicle [Indent level: 3],
            "ACE_lockpickVehicle": {
                "displayName": "Lockpick Vehicle",
                "distance": 4,
                "condition": "[_player,_target,'canLockpick'] call ace_vehiclelock_fnc_lockpick",
                "statement": "[_player,_target,'startLockpick'] call ace_vehiclelock_fnc_lockpick",
                "exceptions": ["isNotSwimming"]
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\AIME_vehicle_seats_getInAction [Indent level: 3],
            "AIME_vehicle_seats_getInAction": {
                "displayName": "Get In",
                "condition": "call AIME_vehicle_seats_fnc_getin_condition",
                "statement": "call AIME_vehicle_seats_fnc_getin_run",
                "icon": "a3|ui_f|data|igui|cfg|actions|obsolete|ui_action_getin_ca.paa",
                "insertChildren": "call AIME_vehicle_seats_fnc_change_submenus"
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\ace_attach_AttachVehicle [Indent level: 3],
            "ace_attach_AttachVehicle": {
                "displayName": "Attach item",
                "condition": "_this call ace_attach_fnc_canAttach",
                "insertChildren": "_this call ace_attach_fnc_getChildrenActions",
                "exceptions": ["isNotSwimming"],
                "showDisabled": 0,
                "icon": "z|ace|addons|attach|UI|attach_ca.paa"
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\ace_attach_DetachVehicle [Indent level: 3],
            "ace_attach_DetachVehicle": {
                "displayName": "Detach item",
                "condition": "_this call ace_attach_fnc_canDetach",
                "statement": "_this call ace_attach_fnc_detach",
                "exceptions": ["isNotSwimming"],
                "showDisabled": 0,
                "icon": "z|ace|addons|attach|UI|detach_ca.paa"
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\ace_captives_LoadCaptive [Indent level: 3],
            "ace_captives_LoadCaptive": {
                "displayName": "Load Captive",
                "distance": 4,
                "condition": "[_player,objNull,_target] call ace_captives_fnc_canLoadCaptive",
                "statement": "[_player,objNull,_target] call ace_captives_fnc_doLoadCaptive",
                "exceptions": ["isNotEscorting","isNotSwimming"]
            },
            # Class: CfgVehicles\Helicopter\ACE_Actions\ACE_MainActions\AIME_inventory_openAction [Indent level: 3],
            "AIME_inventory_openAction": {
                "displayName": "Inventory",
                "condition": "AIME_inventory_settingOpenAction				 && { alive _target }				 && { _target call AIME_inventory_fnc_has_inventory }",
                "statement": "_player action [`Gear`, _target]",
                "icon": "A3|ui_f|data|igui|cfg|actions|gear_ca.paa",
                "exceptions": ["isNotSwimming"]
            }
        }
    },
    # Class: CfgVehicles\Helicopter_Base_F\DefaultEventhandlers [Indent level: 1],
    "DefaultEventhandlers": {
    },
    "dustEffect": "HeliDust",
    "waterEffect": "HeliWater",
    "gearMinAlt": 0.5,
    "startDuration": 20,
    "maxMainRotorDive": 0,
    "maxBackRotorDive": 0,
    "minMainRotorDive": 0,
    "minBackRotorDive": 0,
    "neutralBackRotorDive": 0,
    "neutralMainRotorDive": 0,
    "memoryPointGun": "",
    "memoryPointPilot": "pilot",
    "_mainBladeCenter": "rotor_center",
    "envelope": [0,0.2,0.9,2.1,2.5,3.3,3.5,3.6,3.7,3.8,3.8,3,0.9,0.7,0.5],
    "minFireTime": 20,
    "steerAheadSimul": 0.5,
    "steerAheadPlan": 0.7,
    # Class: CfgVehicles\Helicopter\ViewOptics [Indent level: 1],
    "ViewOptics": {
        "initAngleX": 0,
        "minAngleX": -40,
        "maxAngleX": 17,
        "initAngleY": 0,
        "minAngleY": -100,
        "maxAngleY": 100,
        "initFov": 0.5,
        "minFov": 0.3,
        "maxFov": 1.2,
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": 0,
        "maxMoveY": 0,
        "minMoveZ": 0,
        "maxMoveZ": 0,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    "soundLandingGear": ["",1,1],
    "slingLoadMemoryPoint": "slingLoad0",
    # Class: CfgVehicles\Helicopter\SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles\Helicopter\SpeechVariants\Default [Indent level: 2]
        "Default": {
            "speechSingular": ["veh_air_helicopter_s"],
            "speechPlural": ["veh_air_helicopter_p"]
        }
    },
    "extCameraParams": [-1],
    "textSingular": "helicopter",
    "textPlural": "helicopters",
    "camouflage": 100,
    "audible": 50,
    "epeImpulseDamageCoef": 50,
    "crewCrashProtection": 0.25,
    "headGforceLeaningFactor": [0.01,0.0025,0.01],
    "damageEffect": "AirDestructionEffects",
    "type": 2,
    "dammageHalf": [],
    "dammageFull": [],
    "crewVulnerable": 1,
    "explosionShielding": 4,
    "minTotalDamageThreshold": 0.005,
    # Class: CfgVehicles\Helicopter\DestructionEffects [Indent level: 1],
    "DestructionEffects": {
    },
    "mainBladeCenter": "rotor_center",
    "tailBladeCenter": "rotor_02_center",
    "tailBladeVertical": 1,
    "slingLoadMinCargoMass": 0,
    "ace_interaction_bodyWidth": 3,
    # Class: CfgVehicles\Helicopter\ACE_SelfActions [Indent level: 1],
    "ACE_SelfActions": {
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_Passengers [Indent level: 2]
        "ACE_Passengers": {
            "displayName": "Passengers",
            "condition": "alive _target",
            "statement": "",
            "insertChildren": "_this call ace_interaction_fnc_addPassengersActions"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ace_quickmount_ChangeSeat [Indent level: 2],
        "ace_quickmount_ChangeSeat": {
            "displayName": "Change seat",
            "condition": "call ace_quickmount_fnc_canShowFreeSeats",
            "statement": "",
            "insertChildren": "(_this select 2) param [0,[]]"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_unlockVehicle [Indent level: 2],
        "ACE_unlockVehicle": {
            "displayName": "Unlock Vehicle",
            "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [2, 3]}",
            "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,false],[_target]] call CBA_fnc_targetEvent",
            "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_lockVehicle [Indent level: 2],
        "ACE_lockVehicle": {
            "displayName": "Lock Vehicle",
            "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [0, 1]}",
            "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,true],[_target]] call CBA_fnc_targetEvent",
            "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_lockpickVehicle [Indent level: 2],
        "ACE_lockpickVehicle": {
            "displayName": "Lockpick Vehicle",
            "condition": "[_player,_target,'canLockpick'] call ace_vehiclelock_fnc_lockpick",
            "statement": "[_player,_target,'startLockpick'] call ace_vehiclelock_fnc_lockpick"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_prepareFRIES [Indent level: 2],
        "ACE_prepareFRIES": {
            "displayName": "Prepare fast roping system",
            "condition": "[_target] call ace_fastroping_fnc_canPrepareFRIES",
            "statement": "[_target] call ace_fastroping_fnc_prepareFRIES"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_stowFRIES [Indent level: 2],
        "ACE_stowFRIES": {
            "displayName": "Stow fast roping system",
            "condition": "[_target] call ace_fastroping_fnc_canStowFRIES",
            "statement": "[_target] call ace_fastroping_fnc_stowFRIES"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_deployRopes12 [Indent level: 2],
        "ACE_deployRopes12": {
            "displayName": "Deploy 12m ropes",
            "condition": "[_target,_player,'ACE_rope12'] call ace_fastroping_fnc_canDeployRopes",
            "statement": "[`ace_fastroping_deployRopes`,[_target,_player,'ACE_rope12']] call CBA_fnc_serverEvent"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_deployRopes15 [Indent level: 2],
        "ACE_deployRopes15": {
            "displayName": "Deploy 15m ropes",
            "condition": "[_target,_player,'ACE_rope15'] call ace_fastroping_fnc_canDeployRopes",
            "statement": "[`ace_fastroping_deployRopes`,[_target,_player,'ACE_rope15']] call CBA_fnc_serverEvent"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_deployRopes18 [Indent level: 2],
        "ACE_deployRopes18": {
            "displayName": "Deploy 18m ropes",
            "condition": "[_target,_player,'ACE_rope18'] call ace_fastroping_fnc_canDeployRopes",
            "statement": "[`ace_fastroping_deployRopes`,[_target,_player,'ACE_rope18']] call CBA_fnc_serverEvent"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_deployRopes27 [Indent level: 2],
        "ACE_deployRopes27": {
            "displayName": "Deploy 27m ropes",
            "condition": "[_target,_player,'ACE_rope27'] call ace_fastroping_fnc_canDeployRopes",
            "statement": "[`ace_fastroping_deployRopes`,[_target,_player,'ACE_rope27']] call CBA_fnc_serverEvent"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_deployRopes36 [Indent level: 2],
        "ACE_deployRopes36": {
            "displayName": "Deploy 36m ropes",
            "condition": "[_target,_player,'ACE_rope36',true] call ace_fastroping_fnc_canDeployRopes",
            "statement": "[`ace_fastroping_deployRopes`,[_target,_player,'ACE_rope36']] call CBA_fnc_serverEvent"
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_cutRopes [Indent level: 2],
        "ACE_cutRopes": {
            "displayName": "Cut ropes",
            "condition": "true",
            "statement": "",
            # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_cutRopes\confirmCutRopes [Indent level: 3],
            "confirmCutRopes": {
                "displayName": "Confirm",
                "condition": "[_target] call ace_fastroping_fnc_canCutRopes",
                "statement": "[_target] call ace_fastroping_fnc_cutRopes"
            }
        },
        # Class: CfgVehicles\Helicopter\ACE_SelfActions\ACE_fastRope [Indent level: 2],
        "ACE_fastRope": {
            "displayName": "Fast rope",
            "condition": "[_player, _target] call ace_fastroping_fnc_canFastRope",
            "statement": "[_player, _target] call ace_fastroping_fnc_fastRope"
        }
    },
    "ace_refuel_canReceive": 1,
    "ace_cargo_hasCargo": 1,
    "formationX": 50,
    "formationZ": 100,
    "precision": 100,
    "brakeDistance": 200,
    "formationTime": 10,
    "gearsUpFrictionCoef": 0.5,
    "airBrakeFrictionCoef": 3,
    "airFrictionCoefs2": [0.001,0.0005,6e-005],
    "airFrictionCoefs1": [0.1,0.05,0.006],
    "airFrictionCoefs0": [0,0,0],
    "altFullForce": 2000,
    "altNoForce": 6000,
    "insideSoundCoef": 0.0316228,
    "outsideSoundFilter": 1,
    "nightVision": 0,
    "driverCompartments": 0,
    "enableGPS": 1,
    "weaponsGroup1": "1 + 		2",
    "weaponsGroup2": 4,
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    "impactEffectsSea": "ImpactEffectsAir",
    "flareVelocity": 100,
    "enableRadio": 1,
    "countermeasureActivationRadius": 10000,
    # Class: CfgVehicles\Air\camShakeGForce [Indent level: 1],
    "camShakeGForce": {
        "power": 0.2,
        "frequency": 3,
        "distance": 0,
        "minSpeed": 1
    },
    # Class: CfgVehicles\Air\camShakeDamage [Indent level: 1],
    "camShakeDamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minSpeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "minGForce": 0.2,
    "maxGForce": 2,
    "gForceShakeAttenuation": 0.5,
    "secondaryExplosion": -1,
    "fuelExplosionPower": 1,
    "tf_hasLRradio": 1,
    "ace_refuel_flowRate": 8,
    # Class: CfgVehicles\AllVehicles\SquadTitles [Indent level: 1],
    "SquadTitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memoryPointsGetInDriver": "pos driver",
    "memoryPointsGetInDriverDir": "pos driver dir",
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
    "selectionBackLights": "zadni svetlo",
    # Class: CfgVehicles\AllVehicles\NewTurret [Indent level: 1],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewGunner [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors [Indent level: 2],
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire [Indent level: 2],
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
            # Class: WeaponFireGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponFireGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1 [Indent level: 1],
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2 [Indent level: 1],
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3 [Indent level: 1],
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4 [Indent level: 1],
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5 [Indent level: 1],
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6 [Indent level: 1],
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7 [Indent level: 1],
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8 [Indent level: 1],
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9 [Indent level: 1],
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10 [Indent level: 1],
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11 [Indent level: 1],
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12 [Indent level: 1],
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13 [Indent level: 1],
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14 [Indent level: 1],
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15 [Indent level: 1],
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16 [Indent level: 1],
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17 [Indent level: 1],
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18 [Indent level: 1],
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19 [Indent level: 1],
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20 [Indent level: 1],
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21 [Indent level: 1],
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22 [Indent level: 1],
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds [Indent level: 2],
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
            # Class: WeaponCloudsGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds [Indent level: 2],
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
            # Class: WeaponCloudsMGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints [Indent level: 2],
        "HitPoints": {
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitTurret [Indent level: 3]
            "HitTurret": {
                "armor": 0.8,
                "material": 51,
                "name": "turret",
                "visual": "turret",
                "passThrough": 1,
                "explosionShielding": 1
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitGun [Indent level: 3],
            "HitGun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passThrough": 1,
                "explosionShielding": 1
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets [Indent level: 2],
        "Turrets": {
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn [Indent level: 2],
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
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
        "showCrewAim": 0,
        "ace_fcs_Enabled": 0,
        "ace_fcs_MinDistance": 200,
        "ace_fcs_MaxDistance": 5500,
        "ace_fcs_DistanceInterval": 5
    },
    # Class: CfgVehicles\AllVehicles\ViewCargo [Indent level: 1],
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
    # Class: CfgVehicles\AllVehicles\SoundEvents [Indent level: 1],
    "SoundEvents": {
    },
    "tracksSpeed": 0,
    "selectionLeftOffset": "",
    "selectionRightOffset": "",
    # Class: CfgVehicles\AllVehicles\RenderTargets [Indent level: 1],
    "RenderTargets": {
    },
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "waterPPInVehicle": 1,
    "impactEffectSpeedLimit": 8,
    "showCrewAim": 0,
    # Class: CfgVehicles\AllVehicles\CargoTurret [Indent level: 1],
    "CargoTurret": {
        # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner [Indent level: 2]
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
        # Class: CfgVehicles\AllVehicles\CargoTurret\Hitpoints [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors [Indent level: 2],
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire [Indent level: 2],
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
            # Class: WeaponFireGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponFireGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1 [Indent level: 1],
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2 [Indent level: 1],
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3 [Indent level: 1],
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4 [Indent level: 1],
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5 [Indent level: 1],
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6 [Indent level: 1],
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7 [Indent level: 1],
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8 [Indent level: 1],
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9 [Indent level: 1],
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10 [Indent level: 1],
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11 [Indent level: 1],
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12 [Indent level: 1],
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13 [Indent level: 1],
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14 [Indent level: 1],
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15 [Indent level: 1],
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16 [Indent level: 1],
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17 [Indent level: 1],
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18 [Indent level: 1],
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19 [Indent level: 1],
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20 [Indent level: 1],
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21 [Indent level: 1],
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22 [Indent level: 1],
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds [Indent level: 2],
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
            # Class: WeaponCloudsGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds [Indent level: 2],
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
            # Class: WeaponCloudsMGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets [Indent level: 2],
        "Turrets": {
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn [Indent level: 2],
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
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
        "showCrewAim": 0,
        "ace_fcs_Enabled": 0,
        "ace_fcs_MinDistance": 200,
        "ace_fcs_MaxDistance": 5500,
        "ace_fcs_DistanceInterval": 5
    },
    "curatorInfoType": "RscDisplayAttributesVehicle",
    "curatorInfoTypeEmpty": "RscDisplayAttributesVehicleEmpty",
    "htMin": 60,
    "htMax": 1800,
    "afMax": 70,
    "mfMax": 50,
    "mFact": 0,
    "tBody": 0,
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
    "sensitivity": 2.5,
    "sensitivityEar": 0.0075,
    "portrait": "",
    "ghostPreview": "",
    "armorLights": 0.4,
    "replaceDamaged": "",
    "replaceDamagedLimit": 0.9,
    "replaceDamagedHitpoints": [],
    "keepInEPESceneAfterDeath": 0,
    "groupCameraPosition": [0,5,-30],
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
    "hideUnitInfo": 0,
    "limitedSpeedCoef": 0.22,
    "hasDriver": 1,
    "driverForceOptics": 0,
    "hideWeaponsDriver": 1,
    "enableWatch": 0,
    "allowTabLock": 1,
    "showAllTargets": 0,
    "dustFrontLeftPos": "dustFrontLeft",
    "dustFrontRightPos": "dustFrontRight",
    "dustBackLeftPos": "dustBackLeft",
    "dustBackRightPos": "dustBackRight",
    "wheelCircumference": 1,
    "showNVGDriver": 0,
    "showNVGCommander": 0,
    "showNVGGunner": 0,
    "soundAttenuationCargo": [1],
    "countsForScoreboard": 1,
    "hullDamageCauseExplosion": 0,
    # Class: CfgVehicles\All\NVGMarkers [Indent level: 1],
    "NVGMarkers": {
    },
    # Class: CfgVehicles\All\NVGMarker [Indent level: 1],
    "NVGMarker": {
        "diffuse": [1,1,1,1],
        "ambient": [1,1,1,1],
        "brightness": 1,
        "blinking": 0,
        "onlyInNvg": 0
    },
    # Class: CfgVehicles\All\HeadLimits [Indent level: 1],
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
    # Class: CfgVehicles\All\SoundEnvironExt [Indent level: 1],
    "SoundEnvironExt": {
    },
    # Class: CfgVehicles\All\SoundEquipment [Indent level: 1],
    "SoundEquipment": {
    },
    # Class: CfgVehicles\All\SoundGear [Indent level: 1],
    "SoundGear": {
    },
    # Class: CfgVehicles\All\SoundBreath [Indent level: 1],
    "SoundBreath": {
    },
    # Class: CfgVehicles\All\SoundBreathSwimming [Indent level: 1],
    "SoundBreathSwimming": {
    },
    # Class: CfgVehicles\All\SoundBreathInjured [Indent level: 1],
    "SoundBreathInjured": {
    },
    # Class: CfgVehicles\All\SoundHitScream [Indent level: 1],
    "SoundHitScream": {
    },
    # Class: CfgVehicles\All\SoundInjured [Indent level: 1],
    "SoundInjured": {
    },
    # Class: CfgVehicles\All\SoundBreathAutomatic [Indent level: 1],
    "SoundBreathAutomatic": {
    },
    # Class: CfgVehicles\All\SoundDrown [Indent level: 1],
    "SoundDrown": {
    },
    # Class: CfgVehicles\All\SoundChoke [Indent level: 1],
    "SoundChoke": {
    },
    # Class: CfgVehicles\All\SoundRecovered [Indent level: 1],
    "SoundRecovered": {
    },
    # Class: CfgVehicles\All\SoundBurning [Indent level: 1],
    "SoundBurning": {
    },
    # Class: CfgVehicles\All\PulsationSound [Indent level: 1],
    "PulsationSound": {
    },
    # Class: CfgVehicles\All\SoundDrowning [Indent level: 1],
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
    "aggregateReflectors": [],
    "driverInAction": "",
    "driverOpticsModel": "",
    "driverOpticsEffect": [],
    "driverOpticsColor": [1,1,1,1],
    "hideProxyInCombat": 0,
    "forceHideDriver": 0,
    "canHideDriver": -1,
    "castDriverShadow": 0,
    "viewDriverShadow": 1,
    "viewDriverShadowDiff": 1,
    "viewDriverShadowAmb": 1,
    "viewCargoShadow": 1,
    "viewCargoShadowDiff": 1,
    "viewCargoShadowAmb": 1,
    "ejectDeadDriver": 0,
    "hiddenSelectionsMaterials": [],
    "hiddenUnderwaterSelections": [],
    "shownUnderWaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    # Class: CfgVehicles\All\FxExplo [Indent level: 1],
    "FxExplo": {
        "access": 1
    },
    # Class: CfgVehicles\All\GunFire [Indent level: 1],
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
        # Class: WeaponFireGun\Table [Indent level: 0],
        "Table": {
            # Class: WeaponFireGun\Table\T0 [Indent level: 1]
            "T0": {
                "maxT": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun\Table\T1 [Indent level: 1],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun\Table\T2 [Indent level: 1],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun\Table\T3 [Indent level: 1],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun\Table\T4 [Indent level: 1],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun\Table\T5 [Indent level: 1],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun\Table\T6 [Indent level: 1],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun\Table\T7 [Indent level: 1],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun\Table\T8 [Indent level: 1],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun\Table\T9 [Indent level: 1],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun\Table\T10 [Indent level: 1],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun\Table\T11 [Indent level: 1],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun\Table\T12 [Indent level: 1],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun\Table\T13 [Indent level: 1],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun\Table\T14 [Indent level: 1],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun\Table\T15 [Indent level: 1],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun\Table\T16 [Indent level: 1],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun\Table\T17 [Indent level: 1],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun\Table\T18 [Indent level: 1],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun\Table\T19 [Indent level: 1],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun\Table\T20 [Indent level: 1],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun\Table\T21 [Indent level: 1],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun\Table\T22 [Indent level: 1],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\All\GunClouds [Indent level: 1],
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
        # Class: WeaponCloudsGun\Table [Indent level: 0],
        "Table": {
            # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\All\MGunClouds [Indent level: 1],
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
        # Class: WeaponCloudsMGun\Table [Indent level: 0],
        "Table": {
            # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "HeadAimDown": 0,
    "fireResistance": 10,
    "airCapacity": 10,
    "waterDamageEngine": 0.2,
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "slingLoadCargoMemoryPoints": [],
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    "soundTurnIn": ["",0.000316228,1],
    "soundTurnOut": ["",0.000316228,1],
    "soundTurnInInternal": ["",0.000316228,1],
    "soundTurnOutInternal": ["",0.000316228,1],
    "insideDetectCoef": 0.05,
    "coefSpeedInside": 1,
    "windSockExist": 0,
    "SLX_XEH_DISABLED": 0,
}