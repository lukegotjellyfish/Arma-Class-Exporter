rhs_c130j_cargo_base = {
    "displayname": "C-130J (Cargo)",
    # Class: CfgVehicles|RHS_C130J_Cargo_Base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|RHS_C130J_Cargo_Base|AnimationSources|hide_cargo [Indent level: 2]
        "hide_cargo": {
            "displayname": "",
            "initphase": 1,
            "source": "user",
            "mass": -20,
            "animperiod": 1e-005,
            "onphasechanged": "for '_i' from 1 to 24 do {(_this select 0) lockCargo [_i,(_this select 1)==1]}"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|jumplight [Indent level: 2],
        "jumplight": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|cargolights_hide [Indent level: 2],
        "cargolights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|ramp [Indent level: 2],
        "ramp": {
            "source": "user",
            "initphase": 0,
            "animperiod": 5,
            "sound": "ServoRampSound_2",
            "soundposition": "ramp_bottom_axis"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|door_2_2 [Indent level: 2],
        "door_2_2": {
            "animperiod": 4,
            "source": "door",
            "sound": "ServoRampSound_2",
            "soundposition": "door_2_2_axis2",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|door_2_1 [Indent level: 2],
        "door_2_1": {
            "soundposition": "door_2_1_axis2",
            "animperiod": 4,
            "source": "door",
            "sound": "ServoRampSound_2",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|door_1 [Indent level: 2],
        "door_1": {
            "soundposition": "Door_1_axis",
            "animperiod": 4,
            "source": "door",
            "sound": "ServoRampSound_2",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|CollisionLightRed_source [Indent level: 2],
        "collisionlightred_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionRed"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|CollisionLightWhite_source [Indent level: 2],
        "collisionlightwhite_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionWhite"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Damper_1_1_source [Indent level: 2],
        "damper_1_1_source": {
            "source": "damper",
            "wheel": "Wheel_1_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Damper_2_1_source [Indent level: 2],
        "damper_2_1_source": {
            "source": "damper",
            "wheel": "Wheel_2_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Damper_2_2_source [Indent level: 2],
        "damper_2_2_source": {
            "source": "damper",
            "wheel": "Wheel_2_2"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Damper_3_1_source [Indent level: 2],
        "damper_3_1_source": {
            "source": "damper",
            "wheel": "Wheel_3_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Damper_3_2_source [Indent level: 2],
        "damper_3_2_source": {
            "source": "damper",
            "wheel": "Wheel_3_2"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Wheel_1_1_source [Indent level: 2],
        "wheel_1_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Wheel_2_1_source [Indent level: 2],
        "wheel_2_1_source": {
            "source": "wheel",
            "wheel": "Wheel_2_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Wheel_2_2_source [Indent level: 2],
        "wheel_2_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2_2"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Wheel_3_1_source [Indent level: 2],
        "wheel_3_1_source": {
            "source": "wheel",
            "wheel": "Wheel_3_1"
        },
        # Class: CfgVehicles|RHS_C130J_Base|AnimationSources|Wheel_3_2_source [Indent level: 2],
        "wheel_3_2_source": {
            "source": "wheel",
            "wheel": "Wheel_3_2"
        }
    },
    "transportsoldier": 1,
    # Class: CfgVehicles|RHS_C130J_Cargo_Base|VehicleTransport [Indent level: 1],
    "vehicletransport": {
        # Class: CfgVehicles|RHS_C130J_Cargo_Base|VehicleTransport|Carrier [Indent level: 2]
        "carrier": {
            "cargobaydimensions": ["VTV_limit_1","VTV_limit_2"],
            "disableheightlimit": 0,
            "maxloadmass": 28000,
            "cargoalignment": ["front","center"],
            "cargospacing": [0,0.1,0],
            "exits": ["VTV_exit_1"],
            "unloadinginterval": 2,
            "loadingdistance": 15,
            "loadingangle": 60,
            "parachuteclassdefault": "B_Parachute_02_F",
            "parachuteheightlimitdefault": 25
        }
    },
    "rhs_pararamp": "ramp",
    "rhs_paraoff": -7,
    "rhs_rampanim": "ramp_bottom",
    "rhs_gearanim": "Gear_1_1",
    "rhs_parascript": "rhs_fnc_vehPara",
    "dlc": "RHS_USAF",
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_axisoffsettarget": [0,15,1.17],
    "lesh_wheeloffset": [0,2],
    "enablesweep": 0,
    "irtarget": 1,
    "irtargetsize": 1.2,
    "visualtarget": 1,
    "visualtargetsize": 1.5,
    "radartarget": 1,
    "radartargetsize": 1.5,
    "lockdetectionsystem": "8",
    "incomingmissiledetectionsystem": "2 + 8 + 16",
    "destrtype": "DestructWreck",
    "unitinfotype": "RHSUSF_RscUnitInfoAirPlane",
    "category": "Air",
    "vehicleclass": "rhs_vehclass_aircraft",
    "faction": "rhs_faction_usaf",
    "crew": "rhsusf_airforce_pilot",
    "typicalcargo": ["rhsusf_airforce_pilot","rhsusf_airforce_pilot"],
    "model": "rhsusf|addons|rhsusf_a2port_air|C130J|c130j.p3d",
    "picture": "rhsusf|addons|rhsusf_a2port_air|data|ico|rhs_c130j_pic_ca.paa",
    "icon": "rhsusf|addons|rhsusf_a2port_air|data|mapico|icon_c130j_CA.paa",
    "editorpreview": "rhsusf|addons|rhsusf_editorPreviews|data|RHS_C130J.paa",
    "mapsize": 25,
    "accuracy": 0.15,
    "cost": 20000,
    "getinradius": 2.5,
    "shownvgcargo": [1],
    "cabinopening": 0,
    "driverdoor": "Door_1",
    "getinaction": "GetInLow",
    "getoutaction": "GetInLow",
    "driveraction": "RHS_C130_Pilot",
    "driverrighthandanimname": "pilot_control",
    "driverlefthandanimname": "pilot_control",
    "maximumload": 15000,
    "altfullforce": 8535,
    "altnoforce": 17000,
    "maxspeed": 648,
    "stallspeed": 180,
    "stallwarningtreshold": 0.5,
    "envelope": [0.1,0.1,0.9,2.8,3.5,3.7,3.8,3.8,3.6,3.3,2.7],
    "thrustcoef": [0.9,0.8,0.9,1.3,1.2,1.2,1.1,1,0.9,0.2,0.1,0,0],
    "angleofindicence": -0.0174533,
    "rudderinfluence": 0.866,
    "ruddercontrolssensitivitycoef": 1.5,
    "ruddercoef": [0,0.4,1,1.4,1.8,2,2.2,2.3,2.4,2.5,2.5,2.5,2.6],
    "aileronsensitivity": 1,
    "aileroncontrolssensitivitycoef": 1,
    "aileroncoef": [0,0.5,1,1.2,1.4,1.5,1.6],
    "elevatorsensitivity": 1,
    "elevatorcontrolssensitivitycoef": 3,
    "elevatorcoef": [0,1,1.2,1.4,1.5,1.6,1.6],
    "flapsfrictioncoef": 0.2,
    "wheelsteeringsensitivity": 2,
    "draconicforcexcoef": 4.3,
    "draconicforceycoef": 0.5,
    "draconicforcezcoef": 0.2,
    "draconictorquexcoef": [16,15.5,15,14.5,14,14,14.5,15,16,17,18],
    "draconictorqueycoef": [3.2,2.5,1,"",0,0,0,0,0,0,0,0,0,0,0],
    # Class: CfgVehicles|RHS_C130J_Base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|RHS_C130J_Base|Exhausts|Engine_L1 [Indent level: 2]
        "engine_l1": {
            "position": "fx_engine_l1_pos",
            "direction": "fx_engine_l1_dir",
            "effect": "RHS_EngineEffectAirPlaneHP",
            "engineindex": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|Exhausts|Engine_L2 [Indent level: 2],
        "engine_l2": {
            "position": "fx_engine_l2_pos",
            "direction": "fx_engine_l2_dir",
            "effect": "RHS_EngineEffectAirPlaneHP",
            "engineindex": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|Exhausts|Engine_R1 [Indent level: 2],
        "engine_r1": {
            "position": "fx_engine_r1_pos",
            "direction": "fx_engine_r1_dir",
            "effect": "RHS_EngineEffectAirPlaneHP",
            "engineindex": 1
        },
        # Class: CfgVehicles|RHS_C130J_Base|Exhausts|Engine_R2 [Indent level: 2],
        "engine_r2": {
            "position": "fx_engine_r2_pos",
            "direction": "fx_engine_r2_dir",
            "effect": "RHS_EngineEffectAirPlaneHP",
            "engineindex": 1
        }
    },
    "cargocaneject": 1,
    "cargoiscodriver": [0,0],
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "memorypointsgetincargo": ["pos driver","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2","pos cargo1","pos cargo2"],
    "memorypointsgetincargodir": ["pos driver dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir","pos cargo1 dir","pos cargo2 dir"],
    "cargodoors": ["Door_1","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2","Door_2_1","Door_2_2"],
    "cargoaction": ["Truck_Cargo01","Truck_Cargo04","Truck_Cargo04","Truck_Cargo02","Truck_Cargo01","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo01","Truck_Cargo02","Truck_Cargo01","Truck_Cargo04","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo04","Truck_Cargo01","Truck_Cargo04","Truck_Cargo02","Truck_Cargo04","Truck_Cargo02","Truck_Cargo01","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo01","Truck_Cargo02","Truck_Cargo01","Truck_Cargo04","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo02","Truck_Cargo04","Truck_Cargo01","Truck_Cargo04","Truck_Cargo01","Truck_Cargo04","Truck_Cargo02"],
    "gunnerusespilotview": 1,
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
    "attenuationeffecttype": "OpenHeliAttenuation",
    # Class: CfgVehicles|RHS_C130J_Base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo_in.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_sklo_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_body.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_body_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_body_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_interior.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_interior_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_interior_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_wings.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_wings_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|C130J|data|c130j_wings_destruct.rvmat"]
    },
    "selectiondamage": "zbytek",
    "selectionshowdamage": "zbytek",
    "reportownposition": 1,
    # Class: CfgVehicles|RHS_C130J_Base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|RHS_C130J_Base|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            "uipicture": "rhsusf|addons|rhsusf_a2port_air|data|loadouts|RHS_C130_EDEN_CA.paa",
            # Class: CfgVehicles|RHS_C130J_Base|Components|TransportPylonsComponent|pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles|RHS_C130J_Base|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4]
                "cmdispenser": {
                    "hardpoints": ["RHSUSF_cm_ANALE40_x2","RHSUSF_cm_ANALE40_x4","RHSUSF_cm_ANALE40_x8","RHSUSF_cm_ANALE40_x16"],
                    "priority": 1,
                    "attachment": "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x16",
                    "maxweight": 800,
                    "uiposition": [0.33,0]
                }
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|RHS_C130J_Base|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_C130J_Base|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4]
                "passiveradarsensorcomponent": {
                    "componenttype": "PassiveRadarSensorComponent",
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
                }
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [3000,8000,16000,35000]
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|RHS_C130J_Base|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [3000,8000,16000,35000]
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
    # Class: CfgVehicles|RHS_C130J_Base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|RHS_C130J_Base|EventHandlers|RHSUSF_EventHandlers [Indent level: 2]
        "rhsusf_eventhandlers": {
            "postinit": "_this call rhs_fnc_reapplyTextures",
            "getin": "_this call rhs_fnc_C130_doors",
            "getout": "_this call rhs_fnc_C130_doors"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 30
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhsusf_100Rnd_556x45_soft_pouch [Indent level: 2],
        "_xx_rhsusf_100rnd_556x45_soft_pouch": {
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch",
            "count": 8
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_M441_HE [Indent level: 2],
        "_xx_rhs_mag_m441_he": {
            "magazine": "rhs_mag_M441_HE",
            "count": 16
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_M714_white [Indent level: 2],
        "_xx_rhs_mag_m714_white": {
            "magazine": "rhs_mag_M714_white",
            "count": 4
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportMagazines|_xx_rhs_mag_M662_red [Indent level: 2],
        "_xx_rhs_mag_m662_red": {
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
    "transportitems": {
        # Class: CfgVehicles|RHS_C130J_Base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 20
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 4
        },
        # Class: CfgVehicles|RHS_C130J_Base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|TransportWeapons [Indent level: 1],
    "transportweapons": {
        # Class: CfgVehicles|RHS_C130J_Base|TransportWeapons|_xx_rhs_weap_m4_carryhandle [Indent level: 2]
        "_xx_rhs_weap_m4_carryhandle": {
            "weapon": "rhs_weap_m4_carryhandle",
            "count": 2
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|RHS_C130J_Base|TransportBackpacks|_xx_B_Parachute [Indent level: 2]
        "_xx_b_parachute": {
            "backpack": "B_Parachute",
            "count": 14
        }
    },
    "soundgetin": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|close",0.316228,1],
    "soundgetout": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|open",0.316228,1,40],
    "sounddammage": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|int-alarm_loop",0.562341,1],
    "soundengineonint": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int_start_1",0.398107,1],
    "soundengineonext": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext_start_1",0.398107,1,700],
    "soundengineoffint": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int_stop_1",0.398107,1],
    "soundengineoffext": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext_stop_1",0.398107,1,700],
    "soundincommingmissile": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.1,1.5],
    # Class: CfgVehicles|RHS_C130J_Base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|EngineLowOut [Indent level: 2]
        "enginelowout": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext_engine_low",1.77828,1,900],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "camPos*engineOn*(rpm factor[0.85, 0])"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|EngineHighOut [Indent level: 2],
        "enginehighout": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext_engine_hi",1.77828,1,1100],
            "frequency": "1",
            "volume": "camPos*engineOn*(rpm factor[0.55, 1.0])"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|ForsageOut [Indent level: 2],
        "forsageout": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext_forsage_1",1.41254,1,1500],
            "frequency": "1",
            "volume": "camPos*engineOn*(thrust factor[0.5, 1.0])",
            "cone": [1.14,3.92,2,0.4]
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|WindNoiseOut [Indent level: 2],
        "windnoiseout": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|ext-wind1",0.001,0.6,150],
            "frequency": "(0.1+(1.2*(speed factor[1, 100])))",
            "volume": "camPos*(speed factor[1, 100])"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|EngineLowIn [Indent level: 2],
        "enginelowin": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int_engine_low",1,1],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.85, 0]))"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|EngineHighIn [Indent level: 2],
        "enginehighin": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int_engine_hi",1,1],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.55, 1.0]))"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|ForsageIn [Indent level: 2],
        "forsagein": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int_forsage_1",1.41254,1.1],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.5, 1.0]))"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Sounds|WindNoiseIn [Indent level: 2],
        "windnoisein": {
            "sound": ["|rhsusf|addons|rhsusf_a2port_air|data|sounds|c130|int-wind1",0.001,0.6],
            "frequency": "(0.1+(1.2*(speed factor[1, 100])))",
            "volume": "(1-camPos)*(speed factor[1, 100])"
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "brightness": 50,
            "useflare": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 200,
                "hardlimitend": 250
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Right [Indent level: 2],
        "right": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "size": 1,
            "brightness": 1,
            "useflare": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Right|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 200,
                "hardlimitend": 250
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Left2 [Indent level: 2],
        "left2": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "position": "L2 svetlo",
            "direction": "konec L2 svetla",
            "hitpoint": "L2 svetlo",
            "selection": "L2 svetlo",
            "size": 1,
            "brightness": 1,
            "useflare": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Left2|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 200,
                "hardlimitend": 250
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Right2 [Indent level: 2],
        "right2": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "position": "P2 svetlo",
            "direction": "konec P2 svetla",
            "hitpoint": "P2 svetlo",
            "selection": "P2 svetlo",
            "size": 1,
            "brightness": 1,
            "useflare": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            # Class: CfgVehicles|RHS_C130J_Base|Reflectors|Right2|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 200,
                "hardlimitend": 250
            }
        }
    },
    "weapons": ["rhsusf_weap_ANAAQ24"],
    "magazines": ["rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM","rhsusf_mag_DIRCM"],
    "threat": [0.1,0.5,0.8],
    "ejectspeed": [0,0,0],
    "landingaoa": "rad 7",
    "landingspeed": 200,
    "extcameraposition": [0,5,-40],
    "gearuptime": 4.5,
    "geardowntime": 3,
    "driveoncomponent": [],
    "canfloat": "false",
    "waterresistancecoef": 0.004,
    "waterleakiness": 25,
    # Class: CfgVehicles|RHS_C130J_Base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|RHS_C130J_Base|UserActions|OpenRamp [Indent level: 2]
        "openramp": {
            "displayname": "Open Cargo Ramp",
            "position": "pos_gunner",
            "onlyforplayer": 1,
            "showwindow": 0,
            "radius": 6,
            "condition": "(this animationSourcePhase 'ramp' <= 0.65) AND Alive(this)",
            "statement": "this animateSource ['ramp',1];[this] call rhs_fnc_cargoDetach",
            "shortcut": "user12"
        },
        # Class: CfgVehicles|RHS_C130J_Base|UserActions|LevelRamp [Indent level: 2],
        "levelramp": {
            "displayname": "Level Ramp",
            "condition": "this animationSourcePhase 'ramp' != 0.65 and (alive this)",
            "statement": "this animateSource ['ramp', 0.65];",
            "shortcut": "user13",
            "position": "pos_gunner",
            "onlyforplayer": 1,
            "showwindow": 0,
            "radius": 6
        },
        # Class: CfgVehicles|RHS_C130J_Base|UserActions|CloseRamp [Indent level: 2],
        "closeramp": {
            "displayname": "Close Cargo Ramp",
            "condition": "(this animationSourcePhase 'ramp' >= 0.65) AND Alive(this)",
            "statement": "this animateSource ['ramp',0];[this] call rhs_fnc_cargoAttach",
            "shortcut": "user12",
            "position": "pos_gunner",
            "onlyforplayer": 1,
            "showwindow": 0,
            "radius": 6
        },
        # Class: CfgVehicles|RHS_C130J_Base|UserActions|VehicleParadrop [Indent level: 2],
        "vehicleparadrop": {
            "displayname": "Paradrop cargo",
            "condition": "(count (attachedObjects this) > 0) AND ('man' countType (attachedObjects this) == 0) AND Alive(this)",
            "statement": "[this] spawn rhs_fnc_vehPara",
            "shortcut": "",
            "position": "pos_gunner",
            "onlyforplayer": 1,
            "showwindow": 0,
            "radius": 6
        },
        # Class: CfgVehicles|RHS_C130J_Base|UserActions|OpenMenu [Indent level: 2],
        "openmenu": {
            "useractionid": 74,
            "priority": 11.008,
            "displayname": "<t color='#FDDE00'>Open control panel</t>",
            "position": "pos_gunner",
            "radius": 10,
            "animperiod": 2,
            "onlyforplayer": 1,
            "condition": "((call rhsusf_fnc_findPlayer) in this)",
            "statement": "[this] call rhs_fnc_c130j_openMenu"
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionRed [Indent level: 2]
        "positionred": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 75,
            "name": "PositionLight_Red_1_pos",
            "drawlight": 1,
            "drawlightsize": 0.4,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 1,
            "useflare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionGreen [Indent level: 2],
        "positiongreen": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "PositionLight_Green_1_pos",
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.4,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 1,
            "useflare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionWhite [Indent level: 2],
        "positionwhite": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "PositionLight_White_1_pos",
            "drawlightsize": 0.4,
            "intensity": 75,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 1,
            "useflare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionWhite2 [Indent level: 2],
        "positionwhite2": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "PositionLight_White_2_pos",
            "drawlightsize": 0.4,
            "intensity": 75,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 1,
            "useflare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionWhite3 [Indent level: 2],
        "positionwhite3": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "PositionLight_White_3_pos",
            "drawlightsize": 0.4,
            "intensity": 75,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 1,
            "useflare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|PositionWhite4 [Indent level: 2],
        "positionwhite4": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "PositionLight_White_4_pos",
            "drawlightsize": 0.4,
            "intensity": 75,
            "drawlight": 1,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 1,
            "useflare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|CollisionRed [Indent level: 2],
        "collisionred": {
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "name": "CollisionLight_Red_1_pos",
            "blinking": 1,
            "blinkingpattern": [0.2,1.3],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.4,
            "drawlightcentersize": 0.08,
            "intensity": 75,
            "drawlight": 1,
            "activelight": 0,
            "daylight": 1,
            "useflare": 0
        },
        # Class: CfgVehicles|RHS_C130J_Base|MarkerLights|CollisionWhite [Indent level: 2],
        "collisionwhite": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "CollisionLight_White_1_pos",
            "blinking": 1,
            "blinkingpattern": [0.1,0.9],
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.4,
            "drawlightcentersize": 0.04,
            "intensity": 75,
            "drawlight": 1,
            "activelight": 0,
            "daylight": 1,
            "useflare": 0
        }
    },
    "armor": 250,
    "armorstructural": 4,
    "epeimpulsedamagecoef": 1,
    # Class: CfgVehicles|RHS_C130J_Base|Hitpoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": -380,
            "explosionshielding": 0.7,
            "passthrough": 1,
            "minimalhit": -0.05,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull",
            "armorcomponent": "hit_hull",
            "visual": "zbytek",
            "depends": "Total"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": -80,
            "explosionshielding": 0.6,
            "passthrough": 0.01,
            "minimalhit": -0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1 [Indent level: 2],
        "hitengine_l1": {
            "armor": -80,
            "explosionshielding": 1.25,
            "passthrough": 0.01,
            "minimalhit": -0.05,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l1",
            "armorcomponent": "hit_engine_l1",
            "visual": "vis_engine_l",
            "depends": "0",
            # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1|DestructionEffects|RHS_Hull_Smoke [Indent level: 4]
                "rhs_hull_smoke": {
                    "position": "fx_engine_l1_fire",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1|DestructionEffects|RHS_Hull_Fire [Indent level: 4],
                "rhs_hull_fire": {
                    "position": "fx_engine_l1_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1|DestructionEffects|RHS_Hull_Sparks [Indent level: 4],
                "rhs_hull_sparks": {
                    "position": "fx_engine_l1_fire",
                    "type": "AirFireSparks",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1|DestructionEffects|RHS_Hull_Sounds [Indent level: 4],
                "rhs_hull_sounds": {
                    "position": "fx_engine_l1_fire",
                    "simulation": "sound",
                    "type": "Fire",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1|DestructionEffects|RHS_Hull_Smoke_small1 [Indent level: 4],
                "rhs_hull_smoke_small1": {
                    "position": "fx_engine_l1_fire",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1|DestructionEffects|RHS_Hull_Smoke_small2 [Indent level: 4],
                "rhs_hull_smoke_small2": {
                    "position": "fx_engine_l1_fire",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1|DestructionEffects|RHS_Hull_Fire_2 [Indent level: 4],
                "rhs_hull_fire_2": {
                    "position": "fx_engine_l1_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L1|DestructionEffects|RHS_Hull_Fire_3 [Indent level: 4],
                "rhs_hull_fire_3": {
                    "position": "fx_engine_l1_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2 [Indent level: 2],
        "hitengine_l2": {
            "armor": -80,
            "explosionshielding": 1.25,
            "passthrough": 0.01,
            "minimalhit": -0.05,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l2",
            "armorcomponent": "hit_engine_l2",
            "visual": "vis_engine_2",
            "depends": "0",
            # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2|DestructionEffects|RHS_Hull_Smoke [Indent level: 4]
                "rhs_hull_smoke": {
                    "position": "fx_engine_l2_fire",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2|DestructionEffects|RHS_Hull_Fire [Indent level: 4],
                "rhs_hull_fire": {
                    "position": "fx_engine_l2_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2|DestructionEffects|RHS_Hull_Sparks [Indent level: 4],
                "rhs_hull_sparks": {
                    "position": "fx_engine_l2_fire",
                    "type": "AirFireSparks",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2|DestructionEffects|RHS_Hull_Sounds [Indent level: 4],
                "rhs_hull_sounds": {
                    "position": "fx_engine_l2_fire",
                    "simulation": "sound",
                    "type": "Fire",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2|DestructionEffects|RHS_Hull_Smoke_small1 [Indent level: 4],
                "rhs_hull_smoke_small1": {
                    "position": "fx_engine_l2_fire",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2|DestructionEffects|RHS_Hull_Smoke_small2 [Indent level: 4],
                "rhs_hull_smoke_small2": {
                    "position": "fx_engine_l2_fire",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2|DestructionEffects|RHS_Hull_Fire_2 [Indent level: 4],
                "rhs_hull_fire_2": {
                    "position": "fx_engine_l2_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_L2|DestructionEffects|RHS_Hull_Fire_3 [Indent level: 4],
                "rhs_hull_fire_3": {
                    "position": "fx_engine_l2_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1 [Indent level: 2],
        "hitengine_r1": {
            "armor": -80,
            "explosionshielding": 1.25,
            "passthrough": 0.01,
            "minimalhit": -0.05,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r1",
            "armorcomponent": "hit_engine_r1",
            "visual": "vis_engine_3",
            "depends": "0",
            # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1|DestructionEffects|RHS_Hull_Smoke [Indent level: 4]
                "rhs_hull_smoke": {
                    "position": "fx_engine_r1_fire",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1|DestructionEffects|RHS_Hull_Fire [Indent level: 4],
                "rhs_hull_fire": {
                    "position": "fx_engine_r1_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1|DestructionEffects|RHS_Hull_Sparks [Indent level: 4],
                "rhs_hull_sparks": {
                    "position": "fx_engine_r1_fire",
                    "type": "AirFireSparks",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1|DestructionEffects|RHS_Hull_Sounds [Indent level: 4],
                "rhs_hull_sounds": {
                    "position": "fx_engine_r1_fire",
                    "simulation": "sound",
                    "type": "Fire",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1|DestructionEffects|RHS_Hull_Smoke_small1 [Indent level: 4],
                "rhs_hull_smoke_small1": {
                    "position": "fx_engine_r1_fire",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1|DestructionEffects|RHS_Hull_Smoke_small2 [Indent level: 4],
                "rhs_hull_smoke_small2": {
                    "position": "fx_engine_r1_fire",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1|DestructionEffects|RHS_Hull_Fire_2 [Indent level: 4],
                "rhs_hull_fire_2": {
                    "position": "fx_engine_r1_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R1|DestructionEffects|RHS_Hull_Fire_3 [Indent level: 4],
                "rhs_hull_fire_3": {
                    "position": "fx_engine_r1_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2 [Indent level: 2],
        "hitengine_r2": {
            "armor": -80,
            "explosionshielding": 1.25,
            "passthrough": 0.01,
            "minimalhit": -0.05,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r2",
            "armorcomponent": "hit_engine_r2",
            "visual": "vis_engine_4",
            "depends": "0",
            # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2|DestructionEffects|RHS_Hull_Smoke [Indent level: 4]
                "rhs_hull_smoke": {
                    "position": "fx_engine_r2_fire",
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2|DestructionEffects|RHS_Hull_Fire [Indent level: 4],
                "rhs_hull_fire": {
                    "position": "fx_engine_r2_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2|DestructionEffects|RHS_Hull_Sparks [Indent level: 4],
                "rhs_hull_sparks": {
                    "position": "fx_engine_r2_fire",
                    "type": "AirFireSparks",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2|DestructionEffects|RHS_Hull_Sounds [Indent level: 4],
                "rhs_hull_sounds": {
                    "position": "fx_engine_r2_fire",
                    "simulation": "sound",
                    "type": "Fire",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2|DestructionEffects|RHS_Hull_Smoke_small1 [Indent level: 4],
                "rhs_hull_smoke_small1": {
                    "position": "fx_engine_r2_fire",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2|DestructionEffects|RHS_Hull_Smoke_small2 [Indent level: 4],
                "rhs_hull_smoke_small2": {
                    "position": "fx_engine_r2_fire",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2|DestructionEffects|RHS_Hull_Fire_2 [Indent level: 4],
                "rhs_hull_fire_2": {
                    "position": "fx_engine_r2_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine_R2|DestructionEffects|RHS_Hull_Fire_3 [Indent level: 4],
                "rhs_hull_fire_3": {
                    "position": "fx_engine_r2_fire",
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 999,
            "explosionshielding": 0.25,
            "passthrough": 0.01,
            "minimalhit": -0.01,
            "radius": 0.01,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_1",
            "depends": "(HitEngine_L1 + HitEngine_L1)*0.5"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "armor": 999,
            "explosionshielding": 0.25,
            "passthrough": 0.01,
            "minimalhit": -0.01,
            "radius": 0.01,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_3",
            "depends": "(HitEngine_R1 + HitEngine_R1)*0.5"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": -60,
            "explosionshielding": 0.2,
            "passthrough": 0.01,
            "minimalhit": -0.05,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel_l",
            "visual": "vis_wing_l",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitFuel2 [Indent level: 2],
        "hitfuel2": {
            "armor": -60,
            "explosionshielding": 0.2,
            "passthrough": 0.01,
            "minimalhit": -0.05,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel_r",
            "visual": "vis_wing_r",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLAileron_link [Indent level: 2],
        "hitlaileron_link": {
            "armor": -40,
            "explosionshielding": 0.9,
            "passthrough": 0.01,
            "minimalhit": -0.03,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_l",
            "visual": "",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitRAileron_link [Indent level: 2],
        "hitraileron_link": {
            "armor": -40,
            "explosionshielding": 0.9,
            "passthrough": 0.01,
            "minimalhit": -0.03,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_r",
            "visual": "",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLAileron [Indent level: 2],
        "hitlaileron": {
            "armor": -40,
            "explosionshielding": 1.6,
            "passthrough": 0.01,
            "minimalhit": -0.03,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "armorcomponent": "hit_wing_l",
            "visual": "vis_wing_l",
            "depends": "HitLAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitRAileron [Indent level: 2],
        "hitraileron": {
            "armor": -40,
            "explosionshielding": 1.6,
            "passthrough": 0.01,
            "minimalhit": -0.03,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "armorcomponent": "hit_wing_r",
            "visual": "vis_wing_r",
            "depends": "HitRAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitControlRear [Indent level: 2],
        "hitcontrolrear": {
            "armor": -40,
            "explosionshielding": 0.1,
            "passthrough": 0.01,
            "minimalhit": -0.03,
            "radius": 0.17,
            "material": -1,
            "name": "hit_control_rear",
            "visual": "",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLCElevator [Indent level: 2],
        "hitlcelevator": {
            "armor": -60,
            "explosionshielding": 2,
            "passthrough": 0.01,
            "minimalhit": -0.03,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_l",
            "armorcomponent": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitRElevator [Indent level: 2],
        "hitrelevator": {
            "armor": -60,
            "explosionshielding": 2,
            "passthrough": 0.01,
            "minimalhit": -0.03,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_r",
            "armorcomponent": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLCRudder [Indent level: 2],
        "hitlcrudder": {
            "armor": -70,
            "explosionshielding": 2,
            "passthrough": 0.01,
            "minimalhit": -0.02,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder",
            "armorcomponent": "hit_rudder",
            "visual": "vis_rudder",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLFWheel [Indent level: 2],
        "hitlfwheel": {
            "armor": 1,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.12,
            "material": -1,
            "name": "wheel_1_1",
            "visual": "wheel_1_1",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLF2Wheel [Indent level: 2],
        "hitlf2wheel": {
            "armor": 1,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.12,
            "material": -1,
            "name": "wheel_2_1",
            "visual": "wheel_2_1",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLRF2Wheel [Indent level: 2],
        "hitlrf2wheel": {
            "armor": 1,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.12,
            "material": -1,
            "name": "wheel_2_2",
            "visual": "wheel_2_2",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitLBWheel [Indent level: 2],
        "hitlbwheel": {
            "armor": 1,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.12,
            "material": -1,
            "name": "wheel_3_1",
            "visual": "wheel_3_1",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Hitpoints|HitRBWheel [Indent level: 2],
        "hitrbwheel": {
            "armor": 1,
            "explosionshielding": 1,
            "passthrough": 0,
            "minimalhit": -0.1,
            "radius": 0.12,
            "material": -1,
            "name": "wheel_3_2",
            "visual": "wheel_3_2",
            "depends": "0"
        }
    },
    # Class: CfgVehicles|RHS_C130J_Base|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD [Indent level: 2]
        "airplanehud": {
            "borderleft": 0.09,
            "borderright": 0.02,
            "bordertop": 0.02,
            "borderbottom": 0.1,
            "helmetmounteddisplay": 0,
            "helmetposition": [-0.025,0.025,0.1],
            "helmetright": [0.05,0,0],
            "helmetdown": [0,-0.05,0],
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Pos10Vector [Indent level: 3],
            "pos10vector": {
                "type": "vector",
                "pos0": [0.5,0.3],
                "pos10": [0.9,0.75]
            },
            "topleft": "HUD LH",
            "topright": "HUD PH",
            "bottomleft": "HUD LD",
            "color": [0,1,0,0.1],
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.5,0.34]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|WeaponAim [Indent level: 4],
                "weaponaim": {
                    "source": "weapon",
                    "type": "vector",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Target [Indent level: 4],
                "target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|ILS_H [Indent level: 4],
                "ils_h": {
                    "type": "ils",
                    "pos0": [0.5,0.3],
                    "pos3": [0.62,0.3]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|ILS_W [Indent level: 4],
                "ils_w": {
                    "pos3": [0.5,0.435],
                    "type": "ils",
                    "pos0": [0.5,0.3]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],
                "level0": {
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP5 [Indent level: 4],
                "levelp5": {
                    "angle": 5,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM5 [Indent level: 4],
                "levelm5": {
                    "angle": -5,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": 10,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": -10,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": 15,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": -15,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": 20,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": -20,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": 25,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": -25,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": 30,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": -30,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": 35,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": -35,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": 40,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": -40,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": 45,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": -45,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP50 [Indent level: 4],
                "levelp50": {
                    "angle": 50,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM50 [Indent level: 4],
                "levelm50": {
                    "angle": -50,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.95,
                "color": [0,0.3,0.05],
                "condition": "on",
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|PlaneW [Indent level: 4],
                "planew": {
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "type": "line",
                    "points": [["PlaneW",[-0.08,0],1],["PlaneW",[-0.03,0],1],["PlaneW",[-0.015,0.03375],1],["PlaneW",[0,0],1],["PlaneW",[0.015,0.03375],1],["PlaneW",[0.03,0],1],["PlaneW",[0.08,0],1]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|PlaneHeading [Indent level: 4],
                "planeheading": {
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "type": "line",
                    "points": [["Velocity",[0,-0.0225],1],["Velocity",[0.014,-0.01575],1],["Velocity",[0.02,0],1],["Velocity",[0.014,0.01575],1],["Velocity",[0,0.0225],1],["Velocity",[-0.014,0.01575],1],["Velocity",[-0.02,0],1],["Velocity",[-0.014,-0.01575],1],["Velocity",[0,-0.0225],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.045],1],["Velocity",[0,-0.0225],1],[]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Static [Indent level: 4],
                "static": {
                    "cliptl": [0,0.1],
                    "clipbr": [1,0],
                    "type": "line",
                    "points": [[[0.21,0.52],1],[[0.19,0.5],1],[[0.21,0.48],1],[],[[0.18,0.2],1],[[0.18,0.85],1],[],[[0.79,0.52],1],[[0.81,0.5],1],[[0.79,0.48],1],[],[[0.82,0.2],1],[[0.82,0.85],1],[],[[0.52,0.09],1],[[0.5,0.07],1],[[0.48,0.09],1],[],[[0.2,0.065],1],[[0.8,0.065],1],[]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0,0],
                    "clipbr": [1,1],
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "level0": {
                            "type": "line",
                            "points": [["Level0",[-0.2,0],1],["Level0",[-0.05,0],1],[],["Level0",[0.05,0],1],["Level0",[0.2,0],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_0 [Indent level: 6],
                        "valm_1_0": {
                            "type": "text",
                            "source": "static",
                            "text": 0,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[-0.23,-0.025],1],
                            "right": ["Level0",[-0.13,-0.025],1],
                            "down": ["Level0",[-0.23,0.025],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_0 [Indent level: 6],
                        "valm_2_0": {
                            "align": "right",
                            "pos": ["Level0",[0.22,-0.025],1],
                            "right": ["Level0",[0.32,-0.025],1],
                            "down": ["Level0",[0.22,0.025],1],
                            "type": "text",
                            "source": "static",
                            "text": 0,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM5 [Indent level: 6],
                        "levelm5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.2,-0.03],1],["LevelM5",[-0.2,0],1],["LevelM5",[-0.15,0],1],[],["LevelM5",[-0.1,0],1],["LevelM5",[-0.05,0],1],[],["LevelM5",[0.05,0],1],["LevelM5",[0.1,0],1],[],["LevelM5",[0.15,0],1],["LevelM5",[0.2,0],1],["LevelM5",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_5 [Indent level: 6],
                        "valm_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM5",[-0.23,-0.085],1],
                            "right": ["LevelM5",[-0.13,-0.085],1],
                            "down": ["LevelM5",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_5 [Indent level: 6],
                        "valm_2_5": {
                            "align": "right",
                            "pos": ["LevelM5",[0.22,-0.085],1],
                            "right": ["LevelM5",[0.32,-0.085],1],
                            "down": ["LevelM5",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP5 [Indent level: 6],
                        "levelp5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.2,0.03],1],["LevelP5",[-0.2,0],1],["LevelP5",[-0.05,0],1],[],["LevelP5",[0.05,0],1],["LevelP5",[0.2,0],1],["LevelP5",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_5 [Indent level: 6],
                        "valp_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP5",[-0.23,0.035],1],
                            "right": ["LevelP5",[-0.13,0.035],1],
                            "down": ["LevelP5",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_5 [Indent level: 6],
                        "valp_2_5": {
                            "align": "right",
                            "pos": ["LevelP5",[0.22,0.035],1],
                            "right": ["LevelP5",[0.32,0.035],1],
                            "down": ["LevelP5",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM10 [Indent level: 6],
                        "levelm10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.2,-0.03],1],["LevelM10",[-0.2,0],1],["LevelM10",[-0.15,0],1],[],["LevelM10",[-0.1,0],1],["LevelM10",[-0.05,0],1],[],["LevelM10",[0.05,0],1],["LevelM10",[0.1,0],1],[],["LevelM10",[0.15,0],1],["LevelM10",[0.2,0],1],["LevelM10",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_10 [Indent level: 6],
                        "valm_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM10",[-0.23,-0.085],1],
                            "right": ["LevelM10",[-0.13,-0.085],1],
                            "down": ["LevelM10",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_10 [Indent level: 6],
                        "valm_2_10": {
                            "align": "right",
                            "pos": ["LevelM10",[0.22,-0.085],1],
                            "right": ["LevelM10",[0.32,-0.085],1],
                            "down": ["LevelM10",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP10 [Indent level: 6],
                        "levelp10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.2,0.03],1],["LevelP10",[-0.2,0],1],["LevelP10",[-0.05,0],1],[],["LevelP10",[0.05,0],1],["LevelP10",[0.2,0],1],["LevelP10",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_10 [Indent level: 6],
                        "valp_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP10",[-0.23,0.035],1],
                            "right": ["LevelP10",[-0.13,0.035],1],
                            "down": ["LevelP10",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_10 [Indent level: 6],
                        "valp_2_10": {
                            "align": "right",
                            "pos": ["LevelP10",[0.22,0.035],1],
                            "right": ["LevelP10",[0.32,0.035],1],
                            "down": ["LevelP10",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM15 [Indent level: 6],
                        "levelm15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.2,-0.03],1],["LevelM15",[-0.2,0],1],["LevelM15",[-0.15,0],1],[],["LevelM15",[-0.1,0],1],["LevelM15",[-0.05,0],1],[],["LevelM15",[0.05,0],1],["LevelM15",[0.1,0],1],[],["LevelM15",[0.15,0],1],["LevelM15",[0.2,0],1],["LevelM15",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_15 [Indent level: 6],
                        "valm_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM15",[-0.23,-0.085],1],
                            "right": ["LevelM15",[-0.13,-0.085],1],
                            "down": ["LevelM15",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_15 [Indent level: 6],
                        "valm_2_15": {
                            "align": "right",
                            "pos": ["LevelM15",[0.22,-0.085],1],
                            "right": ["LevelM15",[0.32,-0.085],1],
                            "down": ["LevelM15",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP15 [Indent level: 6],
                        "levelp15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.2,0.03],1],["LevelP15",[-0.2,0],1],["LevelP15",[-0.05,0],1],[],["LevelP15",[0.05,0],1],["LevelP15",[0.2,0],1],["LevelP15",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_15 [Indent level: 6],
                        "valp_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP15",[-0.23,0.035],1],
                            "right": ["LevelP15",[-0.13,0.035],1],
                            "down": ["LevelP15",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_15 [Indent level: 6],
                        "valp_2_15": {
                            "align": "right",
                            "pos": ["LevelP15",[0.22,0.035],1],
                            "right": ["LevelP15",[0.32,0.035],1],
                            "down": ["LevelP15",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM20 [Indent level: 6],
                        "levelm20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.2,-0.03],1],["LevelM20",[-0.2,0],1],["LevelM20",[-0.15,0],1],[],["LevelM20",[-0.1,0],1],["LevelM20",[-0.05,0],1],[],["LevelM20",[0.05,0],1],["LevelM20",[0.1,0],1],[],["LevelM20",[0.15,0],1],["LevelM20",[0.2,0],1],["LevelM20",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_20 [Indent level: 6],
                        "valm_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM20",[-0.23,-0.085],1],
                            "right": ["LevelM20",[-0.13,-0.085],1],
                            "down": ["LevelM20",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_20 [Indent level: 6],
                        "valm_2_20": {
                            "align": "right",
                            "pos": ["LevelM20",[0.22,-0.085],1],
                            "right": ["LevelM20",[0.32,-0.085],1],
                            "down": ["LevelM20",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP20 [Indent level: 6],
                        "levelp20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.2,0.03],1],["LevelP20",[-0.2,0],1],["LevelP20",[-0.05,0],1],[],["LevelP20",[0.05,0],1],["LevelP20",[0.2,0],1],["LevelP20",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_20 [Indent level: 6],
                        "valp_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP20",[-0.23,0.035],1],
                            "right": ["LevelP20",[-0.13,0.035],1],
                            "down": ["LevelP20",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_20 [Indent level: 6],
                        "valp_2_20": {
                            "align": "right",
                            "pos": ["LevelP20",[0.22,0.035],1],
                            "right": ["LevelP20",[0.32,0.035],1],
                            "down": ["LevelP20",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM25 [Indent level: 6],
                        "levelm25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.2,-0.03],1],["LevelM25",[-0.2,0],1],["LevelM25",[-0.15,0],1],[],["LevelM25",[-0.1,0],1],["LevelM25",[-0.05,0],1],[],["LevelM25",[0.05,0],1],["LevelM25",[0.1,0],1],[],["LevelM25",[0.15,0],1],["LevelM25",[0.2,0],1],["LevelM25",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_25 [Indent level: 6],
                        "valm_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM25",[-0.23,-0.085],1],
                            "right": ["LevelM25",[-0.13,-0.085],1],
                            "down": ["LevelM25",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_25 [Indent level: 6],
                        "valm_2_25": {
                            "align": "right",
                            "pos": ["LevelM25",[0.22,-0.085],1],
                            "right": ["LevelM25",[0.32,-0.085],1],
                            "down": ["LevelM25",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP25 [Indent level: 6],
                        "levelp25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.2,0.03],1],["LevelP25",[-0.2,0],1],["LevelP25",[-0.05,0],1],[],["LevelP25",[0.05,0],1],["LevelP25",[0.2,0],1],["LevelP25",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_25 [Indent level: 6],
                        "valp_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP25",[-0.23,0.035],1],
                            "right": ["LevelP25",[-0.13,0.035],1],
                            "down": ["LevelP25",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_25 [Indent level: 6],
                        "valp_2_25": {
                            "align": "right",
                            "pos": ["LevelP25",[0.22,0.035],1],
                            "right": ["LevelP25",[0.32,0.035],1],
                            "down": ["LevelP25",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM30 [Indent level: 6],
                        "levelm30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.2,-0.03],1],["LevelM30",[-0.2,0],1],["LevelM30",[-0.15,0],1],[],["LevelM30",[-0.1,0],1],["LevelM30",[-0.05,0],1],[],["LevelM30",[0.05,0],1],["LevelM30",[0.1,0],1],[],["LevelM30",[0.15,0],1],["LevelM30",[0.2,0],1],["LevelM30",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_30 [Indent level: 6],
                        "valm_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM30",[-0.23,-0.085],1],
                            "right": ["LevelM30",[-0.13,-0.085],1],
                            "down": ["LevelM30",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_30 [Indent level: 6],
                        "valm_2_30": {
                            "align": "right",
                            "pos": ["LevelM30",[0.22,-0.085],1],
                            "right": ["LevelM30",[0.32,-0.085],1],
                            "down": ["LevelM30",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP30 [Indent level: 6],
                        "levelp30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.2,0.03],1],["LevelP30",[-0.2,0],1],["LevelP30",[-0.05,0],1],[],["LevelP30",[0.05,0],1],["LevelP30",[0.2,0],1],["LevelP30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_30 [Indent level: 6],
                        "valp_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP30",[-0.23,0.035],1],
                            "right": ["LevelP30",[-0.13,0.035],1],
                            "down": ["LevelP30",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_30 [Indent level: 6],
                        "valp_2_30": {
                            "align": "right",
                            "pos": ["LevelP30",[0.22,0.035],1],
                            "right": ["LevelP30",[0.32,0.035],1],
                            "down": ["LevelP30",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM35 [Indent level: 6],
                        "levelm35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.2,-0.03],1],["LevelM35",[-0.2,0],1],["LevelM35",[-0.15,0],1],[],["LevelM35",[-0.1,0],1],["LevelM35",[-0.05,0],1],[],["LevelM35",[0.05,0],1],["LevelM35",[0.1,0],1],[],["LevelM35",[0.15,0],1],["LevelM35",[0.2,0],1],["LevelM35",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_35 [Indent level: 6],
                        "valm_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM35",[-0.23,-0.085],1],
                            "right": ["LevelM35",[-0.13,-0.085],1],
                            "down": ["LevelM35",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_35 [Indent level: 6],
                        "valm_2_35": {
                            "align": "right",
                            "pos": ["LevelM35",[0.22,-0.085],1],
                            "right": ["LevelM35",[0.32,-0.085],1],
                            "down": ["LevelM35",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP35 [Indent level: 6],
                        "levelp35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.2,0.03],1],["LevelP35",[-0.2,0],1],["LevelP35",[-0.05,0],1],[],["LevelP35",[0.05,0],1],["LevelP35",[0.2,0],1],["LevelP35",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_35 [Indent level: 6],
                        "valp_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP35",[-0.23,0.035],1],
                            "right": ["LevelP35",[-0.13,0.035],1],
                            "down": ["LevelP35",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_35 [Indent level: 6],
                        "valp_2_35": {
                            "align": "right",
                            "pos": ["LevelP35",[0.22,0.035],1],
                            "right": ["LevelP35",[0.32,0.035],1],
                            "down": ["LevelP35",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM40 [Indent level: 6],
                        "levelm40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.2,-0.03],1],["LevelM40",[-0.2,0],1],["LevelM40",[-0.15,0],1],[],["LevelM40",[-0.1,0],1],["LevelM40",[-0.05,0],1],[],["LevelM40",[0.05,0],1],["LevelM40",[0.1,0],1],[],["LevelM40",[0.15,0],1],["LevelM40",[0.2,0],1],["LevelM40",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_40 [Indent level: 6],
                        "valm_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM40",[-0.23,-0.085],1],
                            "right": ["LevelM40",[-0.13,-0.085],1],
                            "down": ["LevelM40",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_40 [Indent level: 6],
                        "valm_2_40": {
                            "align": "right",
                            "pos": ["LevelM40",[0.22,-0.085],1],
                            "right": ["LevelM40",[0.32,-0.085],1],
                            "down": ["LevelM40",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP40 [Indent level: 6],
                        "levelp40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.2,0.03],1],["LevelP40",[-0.2,0],1],["LevelP40",[-0.05,0],1],[],["LevelP40",[0.05,0],1],["LevelP40",[0.2,0],1],["LevelP40",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_40 [Indent level: 6],
                        "valp_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP40",[-0.23,0.035],1],
                            "right": ["LevelP40",[-0.13,0.035],1],
                            "down": ["LevelP40",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_40 [Indent level: 6],
                        "valp_2_40": {
                            "align": "right",
                            "pos": ["LevelP40",[0.22,0.035],1],
                            "right": ["LevelP40",[0.32,0.035],1],
                            "down": ["LevelP40",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM45 [Indent level: 6],
                        "levelm45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.2,-0.03],1],["LevelM45",[-0.2,0],1],["LevelM45",[-0.15,0],1],[],["LevelM45",[-0.1,0],1],["LevelM45",[-0.05,0],1],[],["LevelM45",[0.05,0],1],["LevelM45",[0.1,0],1],[],["LevelM45",[0.15,0],1],["LevelM45",[0.2,0],1],["LevelM45",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_45 [Indent level: 6],
                        "valm_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM45",[-0.23,-0.085],1],
                            "right": ["LevelM45",[-0.13,-0.085],1],
                            "down": ["LevelM45",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_45 [Indent level: 6],
                        "valm_2_45": {
                            "align": "right",
                            "pos": ["LevelM45",[0.22,-0.085],1],
                            "right": ["LevelM45",[0.32,-0.085],1],
                            "down": ["LevelM45",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP45 [Indent level: 6],
                        "levelp45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.2,0.03],1],["LevelP45",[-0.2,0],1],["LevelP45",[-0.05,0],1],[],["LevelP45",[0.05,0],1],["LevelP45",[0.2,0],1],["LevelP45",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_45 [Indent level: 6],
                        "valp_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP45",[-0.23,0.035],1],
                            "right": ["LevelP45",[-0.13,0.035],1],
                            "down": ["LevelP45",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_45 [Indent level: 6],
                        "valp_2_45": {
                            "align": "right",
                            "pos": ["LevelP45",[0.22,0.035],1],
                            "right": ["LevelP45",[0.32,0.035],1],
                            "down": ["LevelP45",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM50 [Indent level: 6],
                        "levelm50": {
                            "type": "line",
                            "points": [["LevelM50",[-0.2,-0.03],1],["LevelM50",[-0.2,0],1],["LevelM50",[-0.15,0],1],[],["LevelM50",[-0.1,0],1],["LevelM50",[-0.05,0],1],[],["LevelM50",[0.05,0],1],["LevelM50",[0.1,0],1],[],["LevelM50",[0.15,0],1],["LevelM50",[0.2,0],1],["LevelM50",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_50 [Indent level: 6],
                        "valm_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM50",[-0.23,-0.085],1],
                            "right": ["LevelM50",[-0.13,-0.085],1],
                            "down": ["LevelM50",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_50 [Indent level: 6],
                        "valm_2_50": {
                            "align": "right",
                            "pos": ["LevelM50",[0.22,-0.085],1],
                            "right": ["LevelM50",[0.32,-0.085],1],
                            "down": ["LevelM50",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP50 [Indent level: 6],
                        "levelp50": {
                            "type": "line",
                            "points": [["LevelP50",[-0.2,0.03],1],["LevelP50",[-0.2,0],1],["LevelP50",[-0.05,0],1],[],["LevelP50",[0.05,0],1],["LevelP50",[0.2,0],1],["LevelP50",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_50 [Indent level: 6],
                        "valp_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP50",[-0.23,0.035],1],
                            "right": ["LevelP50",[-0.13,0.035],1],
                            "down": ["LevelP50",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_50 [Indent level: 6],
                        "valp_2_50": {
                            "align": "right",
                            "pos": ["LevelP50",[0.22,0.035],1],
                            "right": ["LevelP50",[0.32,0.035],1],
                            "down": ["LevelP50",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "scale": 1,
                            "sourcescale": 1
                        }
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|MGun [Indent level: 4],
                "mgun": {
                    "condition": "mgun",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|MGun|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0.01,0],1],["WeaponAim",[-0.01,0],1],[],["WeaponAim",[0,0.01125],1],["WeaponAim",[0,-0.01125],1],[],["WeaponAim",[0,-0.07875],1],["WeaponAim",[0.049,-0.055125],1],["WeaponAim",[0.07,0],1],["WeaponAim",[0.049,0.055125],1],["WeaponAim",[0,0.07875],1],["WeaponAim",[-0.049,0.055125],1],["WeaponAim",[-0.07,0],1],["WeaponAim",[-0.049,-0.055125],1],["WeaponAim",[0,-0.07875],1],[],["WeaponAim",[0,-0.1575],1],["WeaponAim",[0.07,-0.137025],1],["WeaponAim",[0.1218,-0.07875],1],["WeaponAim",[0.14,0],1],["WeaponAim",[0.1218,0.07875],1],["WeaponAim",[0.07,0.137025],1],["WeaponAim",[0,0.1575],1],["WeaponAim",[-0.07,0.137025],1],["WeaponAim",[-0.1218,0.07875],1],["WeaponAim",[-0.14,0],1],["WeaponAim",[-0.1218,-0.07875],1],["WeaponAim",[-0.07,-0.137025],1],["WeaponAim",[0,-0.1575],1],[],["WeaponAim",[0,-0.1575],1],["WeaponAim",[0,-0.18],1],[],["WeaponAim",[-0.07,-0.136399],1],["WeaponAim",[-0.08,-0.155885],1],[],["WeaponAim",[-0.121244,-0.07875],1],["WeaponAim",[-0.138564,-0.09],1],[],["WeaponAim",[-0.14,6.88454e-009],1],["WeaponAim",[-0.16,7.86805e-009],1],[],["WeaponAim",[-0.121244,0.07875],1],["WeaponAim",[-0.138564,0.09],1],[],["WeaponAim",[-0.07,0.136399],1],["WeaponAim",[-0.08,0.155885],1],[],["WeaponAim",[1.22392e-008,0.1575],1],["WeaponAim",[1.39876e-008,0.18],1],[],["WeaponAim",[0.07,0.136399],1],["WeaponAim",[0.08,0.155885],1],[],["WeaponAim",[0.121244,0.07875],1],["WeaponAim",[0.138564,0.09],1],[],["WeaponAim",[0.14,-1.87817e-009],1],["WeaponAim",[0.16,-2.14648e-009],1],[],["WeaponAim",[0.121244,-0.07875],1],["WeaponAim",[0.138564,-0.09],1],[],["WeaponAim",[0.07,-0.136399],1],["WeaponAim",[0.08,-0.155885],1],[]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Bomb [Indent level: 4],
                "bomb": {
                    "condition": "bomb",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Bomb|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.1125],1],["WeaponAim",[0.05,-0.097875],1],["WeaponAim",[0.087,-0.05625],1],["WeaponAim",[0.1,0],1],["WeaponAim",[0.087,0.05625],1],["WeaponAim",[0.05,0.097875],1],["WeaponAim",[0,0.1125],1],["WeaponAim",[-0.05,0.097875],1],["WeaponAim",[-0.087,0.05625],1],["WeaponAim",[-0.1,0],1],["WeaponAim",[-0.087,-0.05625],1],["WeaponAim",[-0.05,-0.097875],1],["WeaponAim",[0,-0.1125],1],[],["Velocity",0.001,"WeaponAim",[0,0],1],["Velocity",[0,0],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AAMissile [Indent level: 4],
                "aamissile": {
                    "condition": "AAmissile",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AAMissile|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.28125],1],["WeaponAim",[0.125,-0.244687],1],["WeaponAim",[0.2175,-0.140625],1],["WeaponAim",[0.25,0],1],["WeaponAim",[0.2175,0.140625],1],["WeaponAim",[0.125,0.244687],1],["WeaponAim",[0,0.28125],1],["WeaponAim",[-0.125,0.244687],1],["WeaponAim",[-0.2175,0.140625],1],["WeaponAim",[-0.25,0],1],["WeaponAim",[-0.2175,-0.140625],1],["WeaponAim",[-0.125,-0.244687],1],["WeaponAim",[0,-0.28125],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ATMissile [Indent level: 4],
                "atmissile": {
                    "condition": "ATmissile",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ATMissile|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.2025],1],["WeaponAim",[0.09,-0.176175],1],["WeaponAim",[0.1566,-0.10125],1],["WeaponAim",[0.18,0],1],["WeaponAim",[0.1566,0.10125],1],["WeaponAim",[0.09,0.176175],1],["WeaponAim",[0,0.2025],1],["WeaponAim",[-0.09,0.176175],1],["WeaponAim",[-0.1566,0.10125],1],["WeaponAim",[-0.18,0],1],["WeaponAim",[-0.1566,-0.10125],1],["WeaponAim",[-0.09,-0.176175],1],["WeaponAim",[0,-0.2025],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Rockets [Indent level: 4],
                "rockets": {
                    "condition": "Rocket",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Rockets|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0.01,0],1],["WeaponAim",[-0.01,0],1],[],["WeaponAim",[0,0.01125],1],["WeaponAim",[0,-0.01125],1],[],["WeaponAim",[0,-0.135],1],["WeaponAim",[0.06,-0.11745],1],["WeaponAim",[0.1044,-0.0675],1],["WeaponAim",[0.12,0],1],["WeaponAim",[0.1044,0.0675],1],["WeaponAim",[0.06,0.11745],1],["WeaponAim",[0,0.135],1],["WeaponAim",[-0.06,0.11745],1],["WeaponAim",[-0.1044,0.0675],1],["WeaponAim",[-0.12,0],1],["WeaponAim",[-0.1044,-0.0675],1],["WeaponAim",[-0.06,-0.11745],1],["WeaponAim",[0,-0.135],1],[]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AltScale [Indent level: 4],
                "altscale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [0.86,0.82],
                    "right": [0.94,0.82],
                    "down": [0.86,0.87],
                    "linexleft": 0.825,
                    "lineyright": 0.835,
                    "linexleftmajor": 0.825,
                    "lineyrightmajor": 0.845,
                    "bottom": 0.2,
                    "top": 0.85,
                    "center": 0.5,
                    "step": 20,
                    "stepsize": 0.0325,
                    "horizontal": "false",
                    "min": "none",
                    "max": "none",
                    "numbereach": 5,
                    "majorlineeach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|SpeedScale [Indent level: 4],
                "speedscale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "align": "right",
                    "pos": [0.06,0.17],
                    "right": [0.14,0.17],
                    "down": [0.06,0.22],
                    "linexleft": 0.175,
                    "lineyright": 0.165,
                    "linexleftmajor": 0.175,
                    "lineyrightmajor": 0.155,
                    "bottom": 0.85,
                    "center": 0.5,
                    "top": 0.2,
                    "step": 20,
                    "stepsize": 0.0325,
                    "horizontal": "false",
                    "min": "none",
                    "max": "none",
                    "numbereach": 5,
                    "majorlineeach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Gear [Indent level: 4],
                "gear": {
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Gear|text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "GEAR",
                        "align": "right",
                        "scale": 0.5,
                        "sourcescale": 1,
                        "pos": [[0.84,0.88],1],
                        "right": [[0.9,0.88],1],
                        "down": [[0.84,0.92],1]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Flaps [Indent level: 4],
                "flaps": {
                    "condition": "flaps",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Flaps|text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "FLAPS",
                        "align": "right",
                        "scale": 0.5,
                        "sourcescale": 1,
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
                    "sourcescale": 1,
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
                    "sourcescale": 1,
                    "pos": [[0.1,0.93],1],
                    "right": [[0.16,0.93],1],
                    "down": [[0.1,0.97],1]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|VspeedNumber [Indent level: 4],
                "vspeednumber": {
                    "type": "text",
                    "align": "right",
                    "scale": 1,
                    "source": "vspeed",
                    "sourcescale": 1,
                    "pos": [[0.86,0.12],1],
                    "right": [[0.94,0.12],1],
                    "down": [[0.86,0.17],1]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],
                "headingscale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "Heading",
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [0.2,0],
                    "right": [0.28,0],
                    "down": [0.2,0.05],
                    "linexleft": 0.06,
                    "lineyright": 0.05,
                    "linexleftmajor": 0.06,
                    "lineyrightmajor": 0.04,
                    "bottom": 0.8,
                    "center": 0.5,
                    "top": 0.2,
                    "step": 2,
                    "stepsize": 0.03,
                    "horizontal": "true",
                    "min": "none",
                    "max": "none",
                    "numbereach": 5,
                    "majorlineeach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS [Indent level: 4],
                "ils": {
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS|Glideslope [Indent level: 5],
                    "glideslope": {
                        "cliptl": [0,0],
                        "clipbr": [1,1],
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 6],
                        "ils": {
                            "type": "line",
                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[0,0.027],1],["ILS_W",[0,-0.027],1],[],["ILS_W",[0.12,0.027],1],["ILS_W",[0.12,-0.027],1],[],["ILS_W",[0.24,0.027],1],["ILS_W",[0.24,-0.027],1],[],["ILS_W",[-0.12,0.027],1],["ILS_W",[-0.12,-0.027],1],[],["ILS_W",[-0.24,0.027],1],["ILS_W",[-0.24,-0.027],1],[],["ILS_H",[0,-0.27],1],["ILS_H",[0,0.27],1],[],["ILS_H",[0.024,0],1],["ILS_H",[-0.024,0],1],[],["ILS_H",[0.024,0.135],1],["ILS_H",[-0.024,0.135],1],[],["ILS_H",[0.024,0.27],1],["ILS_H",[-0.024,0.27],1],[],["ILS_H",[0.024,-0.135],1],["ILS_H",[-0.024,-0.135],1],[],["ILS_H",[0.024,-0.27],1],["ILS_H",[-0.024,-0.27],1]]
                        }
                    }
                }
            }
        },
        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD2 [Indent level: 2],
        "airplanehud2": {
            "topleft": "HUD2 LH",
            "topright": "HUD2 PH",
            "bottomleft": "HUD2 LD",
            "bottomright": "HUD2 PD",
            "borderleft": 0.09,
            "borderright": 0.02,
            "bordertop": 0.02,
            "borderbottom": 0.1,
            "helmetmounteddisplay": 0,
            "helmetposition": [-0.025,0.025,0.1],
            "helmetright": [0.05,0,0],
            "helmetdown": [0,-0.05,0],
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Pos10Vector [Indent level: 3],
            "pos10vector": {
                "type": "vector",
                "pos0": [0.5,0.3],
                "pos10": [0.9,0.75]
            },
            "color": [0,1,0,0.1],
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.5,0.34]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|WeaponAim [Indent level: 4],
                "weaponaim": {
                    "source": "weapon",
                    "type": "vector",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Target [Indent level: 4],
                "target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.3],
                    "pos10": [0.9,0.75]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|ILS_H [Indent level: 4],
                "ils_h": {
                    "type": "ils",
                    "pos0": [0.5,0.3],
                    "pos3": [0.62,0.3]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|ILS_W [Indent level: 4],
                "ils_w": {
                    "pos3": [0.5,0.435],
                    "type": "ils",
                    "pos0": [0.5,0.3]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],
                "level0": {
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP5 [Indent level: 4],
                "levelp5": {
                    "angle": 5,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM5 [Indent level: 4],
                "levelm5": {
                    "angle": -5,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": 10,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": -10,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": 15,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": -15,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": 20,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": -20,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": 25,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": -25,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": 30,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": -30,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": 35,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": -35,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": 40,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": -40,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": 45,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": -45,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelP50 [Indent level: 4],
                "levelp50": {
                    "angle": 50,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Bones|LevelM50 [Indent level: 4],
                "levelm50": {
                    "angle": -50,
                    "pos0": [0.5,0.34],
                    "pos10": [0.9,0.79],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.95,
                "color": [0,0.3,0.05],
                "condition": "on",
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|PlaneW [Indent level: 4],
                "planew": {
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "type": "line",
                    "points": [["PlaneW",[-0.08,0],1],["PlaneW",[-0.03,0],1],["PlaneW",[-0.015,0.03375],1],["PlaneW",[0,0],1],["PlaneW",[0.015,0.03375],1],["PlaneW",[0.03,0],1],["PlaneW",[0.08,0],1]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|PlaneHeading [Indent level: 4],
                "planeheading": {
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "type": "line",
                    "points": [["Velocity",[0,-0.0225],1],["Velocity",[0.014,-0.01575],1],["Velocity",[0.02,0],1],["Velocity",[0.014,0.01575],1],["Velocity",[0,0.0225],1],["Velocity",[-0.014,0.01575],1],["Velocity",[-0.02,0],1],["Velocity",[-0.014,-0.01575],1],["Velocity",[0,-0.0225],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.045],1],["Velocity",[0,-0.0225],1],[]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Static [Indent level: 4],
                "static": {
                    "cliptl": [0,0.1],
                    "clipbr": [1,0],
                    "type": "line",
                    "points": [[[0.21,0.52],1],[[0.19,0.5],1],[[0.21,0.48],1],[],[[0.18,0.2],1],[[0.18,0.85],1],[],[[0.79,0.52],1],[[0.81,0.5],1],[[0.79,0.48],1],[],[[0.82,0.2],1],[[0.82,0.85],1],[],[[0.52,0.09],1],[[0.5,0.07],1],[[0.48,0.09],1],[],[[0.2,0.065],1],[[0.8,0.065],1],[]]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0,0],
                    "clipbr": [1,1],
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "level0": {
                            "type": "line",
                            "points": [["Level0",[-0.2,0],1],["Level0",[-0.05,0],1],[],["Level0",[0.05,0],1],["Level0",[0.2,0],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_0 [Indent level: 6],
                        "valm_1_0": {
                            "type": "text",
                            "source": "static",
                            "text": 0,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[-0.23,-0.025],1],
                            "right": ["Level0",[-0.13,-0.025],1],
                            "down": ["Level0",[-0.23,0.025],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_0 [Indent level: 6],
                        "valm_2_0": {
                            "align": "right",
                            "pos": ["Level0",[0.22,-0.025],1],
                            "right": ["Level0",[0.32,-0.025],1],
                            "down": ["Level0",[0.22,0.025],1],
                            "type": "text",
                            "source": "static",
                            "text": 0,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM5 [Indent level: 6],
                        "levelm5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.2,-0.03],1],["LevelM5",[-0.2,0],1],["LevelM5",[-0.15,0],1],[],["LevelM5",[-0.1,0],1],["LevelM5",[-0.05,0],1],[],["LevelM5",[0.05,0],1],["LevelM5",[0.1,0],1],[],["LevelM5",[0.15,0],1],["LevelM5",[0.2,0],1],["LevelM5",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_5 [Indent level: 6],
                        "valm_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM5",[-0.23,-0.085],1],
                            "right": ["LevelM5",[-0.13,-0.085],1],
                            "down": ["LevelM5",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_5 [Indent level: 6],
                        "valm_2_5": {
                            "align": "right",
                            "pos": ["LevelM5",[0.22,-0.085],1],
                            "right": ["LevelM5",[0.32,-0.085],1],
                            "down": ["LevelM5",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP5 [Indent level: 6],
                        "levelp5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.2,0.03],1],["LevelP5",[-0.2,0],1],["LevelP5",[-0.05,0],1],[],["LevelP5",[0.05,0],1],["LevelP5",[0.2,0],1],["LevelP5",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_5 [Indent level: 6],
                        "valp_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP5",[-0.23,0.035],1],
                            "right": ["LevelP5",[-0.13,0.035],1],
                            "down": ["LevelP5",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_5 [Indent level: 6],
                        "valp_2_5": {
                            "align": "right",
                            "pos": ["LevelP5",[0.22,0.035],1],
                            "right": ["LevelP5",[0.32,0.035],1],
                            "down": ["LevelP5",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM10 [Indent level: 6],
                        "levelm10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.2,-0.03],1],["LevelM10",[-0.2,0],1],["LevelM10",[-0.15,0],1],[],["LevelM10",[-0.1,0],1],["LevelM10",[-0.05,0],1],[],["LevelM10",[0.05,0],1],["LevelM10",[0.1,0],1],[],["LevelM10",[0.15,0],1],["LevelM10",[0.2,0],1],["LevelM10",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_10 [Indent level: 6],
                        "valm_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM10",[-0.23,-0.085],1],
                            "right": ["LevelM10",[-0.13,-0.085],1],
                            "down": ["LevelM10",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_10 [Indent level: 6],
                        "valm_2_10": {
                            "align": "right",
                            "pos": ["LevelM10",[0.22,-0.085],1],
                            "right": ["LevelM10",[0.32,-0.085],1],
                            "down": ["LevelM10",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP10 [Indent level: 6],
                        "levelp10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.2,0.03],1],["LevelP10",[-0.2,0],1],["LevelP10",[-0.05,0],1],[],["LevelP10",[0.05,0],1],["LevelP10",[0.2,0],1],["LevelP10",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_10 [Indent level: 6],
                        "valp_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP10",[-0.23,0.035],1],
                            "right": ["LevelP10",[-0.13,0.035],1],
                            "down": ["LevelP10",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_10 [Indent level: 6],
                        "valp_2_10": {
                            "align": "right",
                            "pos": ["LevelP10",[0.22,0.035],1],
                            "right": ["LevelP10",[0.32,0.035],1],
                            "down": ["LevelP10",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM15 [Indent level: 6],
                        "levelm15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.2,-0.03],1],["LevelM15",[-0.2,0],1],["LevelM15",[-0.15,0],1],[],["LevelM15",[-0.1,0],1],["LevelM15",[-0.05,0],1],[],["LevelM15",[0.05,0],1],["LevelM15",[0.1,0],1],[],["LevelM15",[0.15,0],1],["LevelM15",[0.2,0],1],["LevelM15",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_15 [Indent level: 6],
                        "valm_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM15",[-0.23,-0.085],1],
                            "right": ["LevelM15",[-0.13,-0.085],1],
                            "down": ["LevelM15",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_15 [Indent level: 6],
                        "valm_2_15": {
                            "align": "right",
                            "pos": ["LevelM15",[0.22,-0.085],1],
                            "right": ["LevelM15",[0.32,-0.085],1],
                            "down": ["LevelM15",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP15 [Indent level: 6],
                        "levelp15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.2,0.03],1],["LevelP15",[-0.2,0],1],["LevelP15",[-0.05,0],1],[],["LevelP15",[0.05,0],1],["LevelP15",[0.2,0],1],["LevelP15",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_15 [Indent level: 6],
                        "valp_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP15",[-0.23,0.035],1],
                            "right": ["LevelP15",[-0.13,0.035],1],
                            "down": ["LevelP15",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_15 [Indent level: 6],
                        "valp_2_15": {
                            "align": "right",
                            "pos": ["LevelP15",[0.22,0.035],1],
                            "right": ["LevelP15",[0.32,0.035],1],
                            "down": ["LevelP15",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM20 [Indent level: 6],
                        "levelm20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.2,-0.03],1],["LevelM20",[-0.2,0],1],["LevelM20",[-0.15,0],1],[],["LevelM20",[-0.1,0],1],["LevelM20",[-0.05,0],1],[],["LevelM20",[0.05,0],1],["LevelM20",[0.1,0],1],[],["LevelM20",[0.15,0],1],["LevelM20",[0.2,0],1],["LevelM20",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_20 [Indent level: 6],
                        "valm_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM20",[-0.23,-0.085],1],
                            "right": ["LevelM20",[-0.13,-0.085],1],
                            "down": ["LevelM20",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_20 [Indent level: 6],
                        "valm_2_20": {
                            "align": "right",
                            "pos": ["LevelM20",[0.22,-0.085],1],
                            "right": ["LevelM20",[0.32,-0.085],1],
                            "down": ["LevelM20",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP20 [Indent level: 6],
                        "levelp20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.2,0.03],1],["LevelP20",[-0.2,0],1],["LevelP20",[-0.05,0],1],[],["LevelP20",[0.05,0],1],["LevelP20",[0.2,0],1],["LevelP20",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_20 [Indent level: 6],
                        "valp_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP20",[-0.23,0.035],1],
                            "right": ["LevelP20",[-0.13,0.035],1],
                            "down": ["LevelP20",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_20 [Indent level: 6],
                        "valp_2_20": {
                            "align": "right",
                            "pos": ["LevelP20",[0.22,0.035],1],
                            "right": ["LevelP20",[0.32,0.035],1],
                            "down": ["LevelP20",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM25 [Indent level: 6],
                        "levelm25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.2,-0.03],1],["LevelM25",[-0.2,0],1],["LevelM25",[-0.15,0],1],[],["LevelM25",[-0.1,0],1],["LevelM25",[-0.05,0],1],[],["LevelM25",[0.05,0],1],["LevelM25",[0.1,0],1],[],["LevelM25",[0.15,0],1],["LevelM25",[0.2,0],1],["LevelM25",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_25 [Indent level: 6],
                        "valm_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM25",[-0.23,-0.085],1],
                            "right": ["LevelM25",[-0.13,-0.085],1],
                            "down": ["LevelM25",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_25 [Indent level: 6],
                        "valm_2_25": {
                            "align": "right",
                            "pos": ["LevelM25",[0.22,-0.085],1],
                            "right": ["LevelM25",[0.32,-0.085],1],
                            "down": ["LevelM25",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP25 [Indent level: 6],
                        "levelp25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.2,0.03],1],["LevelP25",[-0.2,0],1],["LevelP25",[-0.05,0],1],[],["LevelP25",[0.05,0],1],["LevelP25",[0.2,0],1],["LevelP25",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_25 [Indent level: 6],
                        "valp_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP25",[-0.23,0.035],1],
                            "right": ["LevelP25",[-0.13,0.035],1],
                            "down": ["LevelP25",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_25 [Indent level: 6],
                        "valp_2_25": {
                            "align": "right",
                            "pos": ["LevelP25",[0.22,0.035],1],
                            "right": ["LevelP25",[0.32,0.035],1],
                            "down": ["LevelP25",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM30 [Indent level: 6],
                        "levelm30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.2,-0.03],1],["LevelM30",[-0.2,0],1],["LevelM30",[-0.15,0],1],[],["LevelM30",[-0.1,0],1],["LevelM30",[-0.05,0],1],[],["LevelM30",[0.05,0],1],["LevelM30",[0.1,0],1],[],["LevelM30",[0.15,0],1],["LevelM30",[0.2,0],1],["LevelM30",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_30 [Indent level: 6],
                        "valm_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM30",[-0.23,-0.085],1],
                            "right": ["LevelM30",[-0.13,-0.085],1],
                            "down": ["LevelM30",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_30 [Indent level: 6],
                        "valm_2_30": {
                            "align": "right",
                            "pos": ["LevelM30",[0.22,-0.085],1],
                            "right": ["LevelM30",[0.32,-0.085],1],
                            "down": ["LevelM30",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP30 [Indent level: 6],
                        "levelp30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.2,0.03],1],["LevelP30",[-0.2,0],1],["LevelP30",[-0.05,0],1],[],["LevelP30",[0.05,0],1],["LevelP30",[0.2,0],1],["LevelP30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_30 [Indent level: 6],
                        "valp_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP30",[-0.23,0.035],1],
                            "right": ["LevelP30",[-0.13,0.035],1],
                            "down": ["LevelP30",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_30 [Indent level: 6],
                        "valp_2_30": {
                            "align": "right",
                            "pos": ["LevelP30",[0.22,0.035],1],
                            "right": ["LevelP30",[0.32,0.035],1],
                            "down": ["LevelP30",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM35 [Indent level: 6],
                        "levelm35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.2,-0.03],1],["LevelM35",[-0.2,0],1],["LevelM35",[-0.15,0],1],[],["LevelM35",[-0.1,0],1],["LevelM35",[-0.05,0],1],[],["LevelM35",[0.05,0],1],["LevelM35",[0.1,0],1],[],["LevelM35",[0.15,0],1],["LevelM35",[0.2,0],1],["LevelM35",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_35 [Indent level: 6],
                        "valm_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM35",[-0.23,-0.085],1],
                            "right": ["LevelM35",[-0.13,-0.085],1],
                            "down": ["LevelM35",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_35 [Indent level: 6],
                        "valm_2_35": {
                            "align": "right",
                            "pos": ["LevelM35",[0.22,-0.085],1],
                            "right": ["LevelM35",[0.32,-0.085],1],
                            "down": ["LevelM35",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP35 [Indent level: 6],
                        "levelp35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.2,0.03],1],["LevelP35",[-0.2,0],1],["LevelP35",[-0.05,0],1],[],["LevelP35",[0.05,0],1],["LevelP35",[0.2,0],1],["LevelP35",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_35 [Indent level: 6],
                        "valp_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP35",[-0.23,0.035],1],
                            "right": ["LevelP35",[-0.13,0.035],1],
                            "down": ["LevelP35",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_35 [Indent level: 6],
                        "valp_2_35": {
                            "align": "right",
                            "pos": ["LevelP35",[0.22,0.035],1],
                            "right": ["LevelP35",[0.32,0.035],1],
                            "down": ["LevelP35",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM40 [Indent level: 6],
                        "levelm40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.2,-0.03],1],["LevelM40",[-0.2,0],1],["LevelM40",[-0.15,0],1],[],["LevelM40",[-0.1,0],1],["LevelM40",[-0.05,0],1],[],["LevelM40",[0.05,0],1],["LevelM40",[0.1,0],1],[],["LevelM40",[0.15,0],1],["LevelM40",[0.2,0],1],["LevelM40",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_40 [Indent level: 6],
                        "valm_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM40",[-0.23,-0.085],1],
                            "right": ["LevelM40",[-0.13,-0.085],1],
                            "down": ["LevelM40",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_40 [Indent level: 6],
                        "valm_2_40": {
                            "align": "right",
                            "pos": ["LevelM40",[0.22,-0.085],1],
                            "right": ["LevelM40",[0.32,-0.085],1],
                            "down": ["LevelM40",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP40 [Indent level: 6],
                        "levelp40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.2,0.03],1],["LevelP40",[-0.2,0],1],["LevelP40",[-0.05,0],1],[],["LevelP40",[0.05,0],1],["LevelP40",[0.2,0],1],["LevelP40",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_40 [Indent level: 6],
                        "valp_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP40",[-0.23,0.035],1],
                            "right": ["LevelP40",[-0.13,0.035],1],
                            "down": ["LevelP40",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_40 [Indent level: 6],
                        "valp_2_40": {
                            "align": "right",
                            "pos": ["LevelP40",[0.22,0.035],1],
                            "right": ["LevelP40",[0.32,0.035],1],
                            "down": ["LevelP40",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM45 [Indent level: 6],
                        "levelm45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.2,-0.03],1],["LevelM45",[-0.2,0],1],["LevelM45",[-0.15,0],1],[],["LevelM45",[-0.1,0],1],["LevelM45",[-0.05,0],1],[],["LevelM45",[0.05,0],1],["LevelM45",[0.1,0],1],[],["LevelM45",[0.15,0],1],["LevelM45",[0.2,0],1],["LevelM45",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_45 [Indent level: 6],
                        "valm_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM45",[-0.23,-0.085],1],
                            "right": ["LevelM45",[-0.13,-0.085],1],
                            "down": ["LevelM45",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_45 [Indent level: 6],
                        "valm_2_45": {
                            "align": "right",
                            "pos": ["LevelM45",[0.22,-0.085],1],
                            "right": ["LevelM45",[0.32,-0.085],1],
                            "down": ["LevelM45",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP45 [Indent level: 6],
                        "levelp45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.2,0.03],1],["LevelP45",[-0.2,0],1],["LevelP45",[-0.05,0],1],[],["LevelP45",[0.05,0],1],["LevelP45",[0.2,0],1],["LevelP45",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_45 [Indent level: 6],
                        "valp_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP45",[-0.23,0.035],1],
                            "right": ["LevelP45",[-0.13,0.035],1],
                            "down": ["LevelP45",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_45 [Indent level: 6],
                        "valp_2_45": {
                            "align": "right",
                            "pos": ["LevelP45",[0.22,0.035],1],
                            "right": ["LevelP45",[0.32,0.035],1],
                            "down": ["LevelP45",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM50 [Indent level: 6],
                        "levelm50": {
                            "type": "line",
                            "points": [["LevelM50",[-0.2,-0.03],1],["LevelM50",[-0.2,0],1],["LevelM50",[-0.15,0],1],[],["LevelM50",[-0.1,0],1],["LevelM50",[-0.05,0],1],[],["LevelM50",[0.05,0],1],["LevelM50",[0.1,0],1],[],["LevelM50",[0.15,0],1],["LevelM50",[0.2,0],1],["LevelM50",[0.2,-0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_50 [Indent level: 6],
                        "valm_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM50",[-0.23,-0.085],1],
                            "right": ["LevelM50",[-0.13,-0.085],1],
                            "down": ["LevelM50",[-0.23,-0.035],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_2_50 [Indent level: 6],
                        "valm_2_50": {
                            "align": "right",
                            "pos": ["LevelM50",[0.22,-0.085],1],
                            "right": ["LevelM50",[0.32,-0.085],1],
                            "down": ["LevelM50",[0.22,-0.035],1],
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP50 [Indent level: 6],
                        "levelp50": {
                            "type": "line",
                            "points": [["LevelP50",[-0.2,0.03],1],["LevelP50",[-0.2,0],1],["LevelP50",[-0.05,0],1],[],["LevelP50",[0.05,0],1],["LevelP50",[0.2,0],1],["LevelP50",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_50 [Indent level: 6],
                        "valp_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "left",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP50",[-0.23,0.035],1],
                            "right": ["LevelP50",[-0.13,0.035],1],
                            "down": ["LevelP50",[-0.23,0.085],1]
                        },
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_2_50 [Indent level: 6],
                        "valp_2_50": {
                            "align": "right",
                            "pos": ["LevelP50",[0.22,0.035],1],
                            "right": ["LevelP50",[0.32,0.035],1],
                            "down": ["LevelP50",[0.22,0.085],1],
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "scale": 1,
                            "sourcescale": 1
                        }
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|MGun [Indent level: 4],
                "mgun": {
                    "condition": "mgun",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|MGun|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0.01,0],1],["WeaponAim",[-0.01,0],1],[],["WeaponAim",[0,0.01125],1],["WeaponAim",[0,-0.01125],1],[],["WeaponAim",[0,-0.07875],1],["WeaponAim",[0.049,-0.055125],1],["WeaponAim",[0.07,0],1],["WeaponAim",[0.049,0.055125],1],["WeaponAim",[0,0.07875],1],["WeaponAim",[-0.049,0.055125],1],["WeaponAim",[-0.07,0],1],["WeaponAim",[-0.049,-0.055125],1],["WeaponAim",[0,-0.07875],1],[],["WeaponAim",[0,-0.1575],1],["WeaponAim",[0.07,-0.137025],1],["WeaponAim",[0.1218,-0.07875],1],["WeaponAim",[0.14,0],1],["WeaponAim",[0.1218,0.07875],1],["WeaponAim",[0.07,0.137025],1],["WeaponAim",[0,0.1575],1],["WeaponAim",[-0.07,0.137025],1],["WeaponAim",[-0.1218,0.07875],1],["WeaponAim",[-0.14,0],1],["WeaponAim",[-0.1218,-0.07875],1],["WeaponAim",[-0.07,-0.137025],1],["WeaponAim",[0,-0.1575],1],[],["WeaponAim",[0,-0.1575],1],["WeaponAim",[0,-0.18],1],[],["WeaponAim",[-0.07,-0.136399],1],["WeaponAim",[-0.08,-0.155885],1],[],["WeaponAim",[-0.121244,-0.07875],1],["WeaponAim",[-0.138564,-0.09],1],[],["WeaponAim",[-0.14,6.88454e-009],1],["WeaponAim",[-0.16,7.86805e-009],1],[],["WeaponAim",[-0.121244,0.07875],1],["WeaponAim",[-0.138564,0.09],1],[],["WeaponAim",[-0.07,0.136399],1],["WeaponAim",[-0.08,0.155885],1],[],["WeaponAim",[1.22392e-008,0.1575],1],["WeaponAim",[1.39876e-008,0.18],1],[],["WeaponAim",[0.07,0.136399],1],["WeaponAim",[0.08,0.155885],1],[],["WeaponAim",[0.121244,0.07875],1],["WeaponAim",[0.138564,0.09],1],[],["WeaponAim",[0.14,-1.87817e-009],1],["WeaponAim",[0.16,-2.14648e-009],1],[],["WeaponAim",[0.121244,-0.07875],1],["WeaponAim",[0.138564,-0.09],1],[],["WeaponAim",[0.07,-0.136399],1],["WeaponAim",[0.08,-0.155885],1],[]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Bomb [Indent level: 4],
                "bomb": {
                    "condition": "bomb",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Bomb|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.1125],1],["WeaponAim",[0.05,-0.097875],1],["WeaponAim",[0.087,-0.05625],1],["WeaponAim",[0.1,0],1],["WeaponAim",[0.087,0.05625],1],["WeaponAim",[0.05,0.097875],1],["WeaponAim",[0,0.1125],1],["WeaponAim",[-0.05,0.097875],1],["WeaponAim",[-0.087,0.05625],1],["WeaponAim",[-0.1,0],1],["WeaponAim",[-0.087,-0.05625],1],["WeaponAim",[-0.05,-0.097875],1],["WeaponAim",[0,-0.1125],1],[],["Velocity",0.001,"WeaponAim",[0,0],1],["Velocity",[0,0],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AAMissile [Indent level: 4],
                "aamissile": {
                    "condition": "AAmissile",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AAMissile|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.28125],1],["WeaponAim",[0.125,-0.244687],1],["WeaponAim",[0.2175,-0.140625],1],["WeaponAim",[0.25,0],1],["WeaponAim",[0.2175,0.140625],1],["WeaponAim",[0.125,0.244687],1],["WeaponAim",[0,0.28125],1],["WeaponAim",[-0.125,0.244687],1],["WeaponAim",[-0.2175,0.140625],1],["WeaponAim",[-0.25,0],1],["WeaponAim",[-0.2175,-0.140625],1],["WeaponAim",[-0.125,-0.244687],1],["WeaponAim",[0,-0.28125],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ATMissile [Indent level: 4],
                "atmissile": {
                    "condition": "ATmissile",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ATMissile|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0,-0.2025],1],["WeaponAim",[0.09,-0.176175],1],["WeaponAim",[0.1566,-0.10125],1],["WeaponAim",[0.18,0],1],["WeaponAim",[0.1566,0.10125],1],["WeaponAim",[0.09,0.176175],1],["WeaponAim",[0,0.2025],1],["WeaponAim",[-0.09,0.176175],1],["WeaponAim",[-0.1566,0.10125],1],["WeaponAim",[-0.18,0],1],["WeaponAim",[-0.1566,-0.10125],1],["WeaponAim",[-0.09,-0.176175],1],["WeaponAim",[0,-0.2025],1],[],["Target",[0,-0.07875],1],["Target",[0.07,0],1],["Target",[0,0.07875],1],["Target",[-0.07,0],1],["Target",[0,-0.07875],1]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Rockets [Indent level: 4],
                "rockets": {
                    "condition": "Rocket",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Rockets|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["WeaponAim",[0.01,0],1],["WeaponAim",[-0.01,0],1],[],["WeaponAim",[0,0.01125],1],["WeaponAim",[0,-0.01125],1],[],["WeaponAim",[0,-0.135],1],["WeaponAim",[0.06,-0.11745],1],["WeaponAim",[0.1044,-0.0675],1],["WeaponAim",[0.12,0],1],["WeaponAim",[0.1044,0.0675],1],["WeaponAim",[0.06,0.11745],1],["WeaponAim",[0,0.135],1],["WeaponAim",[-0.06,0.11745],1],["WeaponAim",[-0.1044,0.0675],1],["WeaponAim",[-0.12,0],1],["WeaponAim",[-0.1044,-0.0675],1],["WeaponAim",[-0.06,-0.11745],1],["WeaponAim",[0,-0.135],1],[]]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|AltScale [Indent level: 4],
                "altscale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [0.86,0.82],
                    "right": [0.94,0.82],
                    "down": [0.86,0.87],
                    "linexleft": 0.825,
                    "lineyright": 0.835,
                    "linexleftmajor": 0.825,
                    "lineyrightmajor": 0.845,
                    "bottom": 0.2,
                    "top": 0.85,
                    "center": 0.5,
                    "step": 20,
                    "stepsize": 0.0325,
                    "horizontal": "false",
                    "min": "none",
                    "max": "none",
                    "numbereach": 5,
                    "majorlineeach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|SpeedScale [Indent level: 4],
                "speedscale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "align": "right",
                    "pos": [0.06,0.17],
                    "right": [0.14,0.17],
                    "down": [0.06,0.22],
                    "linexleft": 0.175,
                    "lineyright": 0.165,
                    "linexleftmajor": 0.175,
                    "lineyrightmajor": 0.155,
                    "bottom": 0.85,
                    "center": 0.5,
                    "top": 0.2,
                    "step": 20,
                    "stepsize": 0.0325,
                    "horizontal": "false",
                    "min": "none",
                    "max": "none",
                    "numbereach": 5,
                    "majorlineeach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Gear [Indent level: 4],
                "gear": {
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Gear|text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "GEAR",
                        "align": "right",
                        "scale": 0.5,
                        "sourcescale": 1,
                        "pos": [[0.84,0.88],1],
                        "right": [[0.9,0.88],1],
                        "down": [[0.84,0.92],1]
                    }
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Flaps [Indent level: 4],
                "flaps": {
                    "condition": "flaps",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|Flaps|text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "FLAPS",
                        "align": "right",
                        "scale": 0.5,
                        "sourcescale": 1,
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
                    "sourcescale": 1,
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
                    "sourcescale": 1,
                    "pos": [[0.1,0.93],1],
                    "right": [[0.16,0.93],1],
                    "down": [[0.1,0.97],1]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|VspeedNumber [Indent level: 4],
                "vspeednumber": {
                    "type": "text",
                    "align": "right",
                    "scale": 1,
                    "source": "vspeed",
                    "sourcescale": 1,
                    "pos": [[0.86,0.12],1],
                    "right": [[0.94,0.12],1],
                    "down": [[0.86,0.17],1]
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],
                "headingscale": {
                    "type": "scale",
                    "scale": 1,
                    "source": "Heading",
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [0.2,0],
                    "right": [0.28,0],
                    "down": [0.2,0.05],
                    "linexleft": 0.06,
                    "lineyright": 0.05,
                    "linexleftmajor": 0.06,
                    "lineyrightmajor": 0.04,
                    "bottom": 0.8,
                    "center": 0.5,
                    "top": 0.2,
                    "step": 2,
                    "stepsize": 0.03,
                    "horizontal": "true",
                    "min": "none",
                    "max": "none",
                    "numbereach": 5,
                    "majorlineeach": 5
                },
                # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS [Indent level: 4],
                "ils": {
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS|Glideslope [Indent level: 5],
                    "glideslope": {
                        "cliptl": [0,0],
                        "clipbr": [1,1],
                        # Class: CfgVehicles|RHS_C130J_Base|MFD|AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 6],
                        "ils": {
                            "type": "line",
                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[0,0.027],1],["ILS_W",[0,-0.027],1],[],["ILS_W",[0.12,0.027],1],["ILS_W",[0.12,-0.027],1],[],["ILS_W",[0.24,0.027],1],["ILS_W",[0.24,-0.027],1],[],["ILS_W",[-0.12,0.027],1],["ILS_W",[-0.12,-0.027],1],[],["ILS_W",[-0.24,0.027],1],["ILS_W",[-0.24,-0.027],1],[],["ILS_H",[0,-0.27],1],["ILS_H",[0,0.27],1],[],["ILS_H",[0.024,0],1],["ILS_H",[-0.024,0],1],[],["ILS_H",[0.024,0.135],1],["ILS_H",[-0.024,0.135],1],[],["ILS_H",[0.024,0.27],1],["ILS_H",[-0.024,0.27],1],[],["ILS_H",[0.024,-0.135],1],["ILS_H",[-0.024,-0.135],1],[],["ILS_H",[0.024,-0.27],1],["ILS_H",[-0.024,-0.27],1]]
                        }
                    }
                }
            }
        }
    },
    "maxomega": 2000,
    # Class: CfgVehicles|RHS_C130J_Base|Wheels [Indent level: 1],
    "wheels": {
        "disablewheelswhendestroyed": 1,
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_1_1 [Indent level: 2],
        "wheel_1_1": {
            "steering": 1,
            "side": "left",
            "bonename": "Wheel_1_1",
            "center": "Wheel_1_1_center",
            "boundary": "Wheel_1_1_rim",
            "width": 0.9,
            "mass": 150,
            "moi": 3,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "suspforceapppointoffset": "Wheel_1_1_center",
            "tireforceapppointoffset": "Wheel_1_1_center",
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "sprungmass": 7400,
            "springstrength": 120000,
            "springdamperrate": 128000,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_1_1_fake [Indent level: 2],
        "wheel_1_1_fake": {
            "steering": 1,
            "side": "left",
            "bonename": "Wheel_1_1",
            "center": "Wheel_1_1_center",
            "boundary": "Wheel_1_1_rim",
            "width": 0.9,
            "mass": 150,
            "moi": 3,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "suspforceapppointoffset": "Wheel_1_1_center",
            "tireforceapppointoffset": "Wheel_1_1_center",
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "sprungmass": 7400,
            "springstrength": 120000,
            "springdamperrate": 128000,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 25,
            "latstiffy": 180,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_2_1 [Indent level: 2],
        "wheel_2_1": {
            "steering": 0,
            "bonename": "Wheel_2_1",
            "center": "Wheel_2_1_center",
            "boundary": "Wheel_2_1_rim",
            "suspforceapppointoffset": "Wheel_2_1_center",
            "tireforceapppointoffset": "Wheel_2_1_center",
            "width": 0.48,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "sprungmass": 7200,
            "springdamperrate": 51200,
            "springstrength": 1.58e+006,
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
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_2_2 [Indent level: 2],
        "wheel_2_2": {
            "side": "right",
            "bonename": "Wheel_2_2",
            "center": "Wheel_2_2_center",
            "boundary": "Wheel_2_2_rim",
            "suspforceapppointoffset": "Wheel_2_2_center",
            "tireforceapppointoffset": "Wheel_2_2_center",
            "steering": 0,
            "width": 0.48,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "sprungmass": 7200,
            "springdamperrate": 51200,
            "springstrength": 1.58e+006,
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
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_3_1 [Indent level: 2],
        "wheel_3_1": {
            "bonename": "Wheel_3_1",
            "center": "Wheel_3_1_center",
            "boundary": "Wheel_3_1_rim",
            "suspforceapppointoffset": "Wheel_3_1_center",
            "tireforceapppointoffset": "Wheel_3_1_center",
            "steering": 0,
            "width": 0.48,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "sprungmass": 7200,
            "springdamperrate": 51200,
            "springstrength": 1.58e+006,
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
        # Class: CfgVehicles|RHS_C130J_Base|Wheels|Wheel_3_2 [Indent level: 2],
        "wheel_3_2": {
            "side": "right",
            "bonename": "Wheel_3_2",
            "center": "Wheel_3_2_center",
            "boundary": "Wheel_3_2_rim",
            "suspforceapppointoffset": "Wheel_3_2_center",
            "tireforceapppointoffset": "Wheel_3_2_center",
            "steering": 0,
            "width": 0.48,
            "maxcompression": 0.2,
            "maxdroop": 0.2,
            "sprungmass": 7200,
            "springdamperrate": 51200,
            "springstrength": 1.58e+006,
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
    # Class: CfgVehicles|RHS_C130J_Base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret [Indent level: 2]
        "copilotturret": {
            "iscopilot": 1,
            "primarygunner": 0,
            "caneject": 0,
            "body": "",
            "gun": "",
            "animationsourcebody": "",
            "animationsourcegun": "",
            "weapons": [],
            "magazines": [],
            "gunneraction": "RHS_C130_Pilot",
            "gunnerinaction": "RHS_C130_Pilot",
            "gunnername": "Copilot",
            "gunnerdoor": "Door_1",
            "gunnernotspawned": 0,
            "gunnerusespilotview": 1,
            "hasgunner": 1,
            "memorypointsgetingunner": "pos driver",
            "memorypointsgetingunnerdir": "pos driver dir",
            "minelev": -50,
            "maxelev": 30,
            "initelev": 11,
            "minturn": -170,
            "maxturn": 170,
            "initturn": 0,
            "maxhorizontalrotspeed": 3,
            "maxverticalrotspeed": 3,
            # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initanglex": -5,
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
                "continuous": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "commanding": -1,
            "gunnerlefthandanimname": "copilot_control",
            "gunnerrighthandanimname": "copilot_control",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "gunnerforceoptics": 0,
            "turretcansee": 15,
            # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors [Indent level: 3],
            "reflectors": {
                # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cabin [Indent level: 4]
                "cabin": {
                    "color": [830,100,100],
                    "ambient": [5,0,0],
                    "intensity": 9,
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
                    # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cabin|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 50,
                        "hardlimitstart": 3,
                        "hardlimitend": 3.5
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
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 3,
                        "hardlimitend": 3.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerangle": 90,
                    "outerangle": 165,
                    "flaresize": 1,
                    "flaremaxdistance": 5,
                    "daylight": 1,
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
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 3,
                        "hardlimitend": 3.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerangle": 90,
                    "outerangle": 165,
                    "flaresize": 1,
                    "flaremaxdistance": 5,
                    "daylight": 1,
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
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 3,
                        "hardlimitend": 3.5
                    },
                    "ambient": [5,0,0],
                    "size": 1,
                    "innerangle": 90,
                    "outerangle": 165,
                    "flaresize": 1,
                    "flaremaxdistance": 5,
                    "daylight": 1,
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
                    "useflare": 0,
                    "conefadecoef": 0.1,
                    # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Reflectors|cargo_light_1|Attenuation [Indent level: 5],
                    "attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardlimitstart": 3,
                        "hardlimitend": 3.5
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
            # Class: CfgVehicles|RHS_C130J_Base|Turrets|CopilotTurret|Hitpoints [Indent level: 3],
            "hitpoints": {
            },
            "animationsourcehatch": "hatchGunner",
            "animationsourcecamelev": "camElev",
            "proxytype": "CPGunner",
            "proxyindex": 1,
            "gunnertype": "",
            "primaryobserver": 0,
            "soundservo": ["",0.00316228,1],
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
            "stabilizedinaxes": 3,
            "primary": 1,
            "gunnergetinaction": "",
            "gunnergetoutaction": "",
            "canusescanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "turretspec": {
                "showheadphones": 0
            },
            "gunneropticsmodel": "",
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
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "memorypointgunneroptics": "gunnerview",
            "memorypointgun": "kulas",
            "selectionfireanim": "zasleh",
            "showcrewaim": 0
        }
    },
    "hiddenselections": ["camo1","camo2"],
    "hiddenselectionstextures": ["rhsusf|addons|rhsusf_a2port_air|c130j|data|c130j_body_co.paa","rhsusf|addons|rhsusf_a2port_air|c130j|data|c130j_wings_co.paa"],
    # Class: CfgVehicles|RHS_C130J_Base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|RHS_C130J_Base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_a2port_air|c130j|data|c130j_body_co.paa","rhsusf|addons|rhsusf_a2port_air|c130j|data|c130j_wings_co.paa"],
            "factions": ["rhs_faction_usaf"]
        }
    },
    "texturelist": ["standard",1],
    # Class: CfgVehicles|RHS_C130J_Base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|door_1 [Indent level: 2],
        "door_1": {
            "displayname": "Open crew door",
            "property": "door_1",
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|door_2_1 [Indent level: 2],
        "door_2_1": {
            "displayname": "Open left door",
            "property": "door_2_1",
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|door_2_2 [Indent level: 2],
        "door_2_2": {
            "displayname": "Open right door",
            "property": "door_2_2",
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|Ramp [Indent level: 2],
        "ramp": {
            "displayname": "Open cargo bay",
            "property": "Ramp",
            "control": "slider",
            "expression": "_this animateSource ['%s',_value,true]",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|hide_cargo [Indent level: 2],
        "hide_cargo": {
            "displayname": "Hide cargo benches",
            "property": "hide_cargo",
            "expression": "_this animate ['%s',_value,true];for '_i' from 1 to 24 do {_this lockCargo [_i,(_value == 1)]}",
            "control": "CheckboxNumber",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|RHS_C130J_Base|Attributes|rhs_attachCargo [Indent level: 2],
        "rhs_attachcargo": {
            "displayname": "Attach cargo",
            "tooltip": "Attaching cargo (using attachTo command) just like when you use ramp action",
            "property": "rhs_attachCargo",
            "expression": "if(_value == 1)then{[_this] spawn rhs_fnc_cargoAttach}else{{if(not(_x isKindOf 'Man'))then{detach _x}}foreach attachedObjects _this};",
            "control": "CheckboxNumber",
            "defaultvalue": "0"
        }
    },
    "author": "Bohemia Interactive",
    "_generalmacro": "Plane_Base_F",
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "waterlineardampingcoefy": 0,
    "waterlineardampingcoefx": 5,
    "transportmaxweapons": 6,
    "transportmaxmagazines": 24,
    "transportmaxbackpacks": 6,
    "supplyradius": 2,
    "memorypointsupply": "doplnovani",
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
    "brakedistance": 500,
    "steeraheadsimul": 1,
    "steeraheadplan": 2,
    "gearretracting": 1,
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "flaps": 1,
    "airbrake": 1,
    "vtol": 0,
    "tailhook": 0,
    "lightongear": 1,
    "ejectdamagelimit": 0.45,
    "minfiretime": 60,
    "simulation": "airplanex",
    "mingunelev": 0,
    "maxgunelev": 0,
    "mingunturn": 0,
    "maxgunturn": 0,
    "gunaimdown": 0,
    "vtolyawinfluence": 2,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
    # Class: CfgVehicles|Plane|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initfov": 0.75,
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
    "memorypointlrocket": "L raketa",
    "memorypointrrocket": "P raketa",
    "memorypointldust": "levy prach",
    "memorypointrdust": "pravy prach",
    "selectionfireanim": "zasleh",
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
    # Class: CfgVehicles|Plane|WingVortices [Indent level: 1],
    "wingvortices": {
        # Class: CfgVehicles|Plane|WingVortices|WingTipLeft [Indent level: 2]
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "cerveny pozicni"
        },
        # Class: CfgVehicles|Plane|WingVortices|WingTipRight [Indent level: 2],
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "zeleny pozicni"
        }
    },
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
    "type": 2,
    "memorypointgun": "kulomet",
    "fuelexplosionpower": 10,
    "crewcrashprotection": 0.15,
    "damageeffect": "AirDestructionEffects",
    "gunnergetinaction": "GetInHigh",
    "gunnergetoutaction": "GetOutHigh",
    "camouflage": 100,
    "audible": 60,
    # Class: CfgVehicles|Plane|CamShake [Indent level: 1],
    "camshake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minspeed": 200
    },
    "camshakecoef": 0,
    "headgforceleaningfactor": [0.005,0.001,0.025],
    "explosionshielding": 2,
    "mintotaldamagethreshold": 0.005,
    # Class: CfgVehicles|Plane|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "formationtime": 10,
    "gearsupfrictioncoef": 0.5,
    "airbrakefrictioncoef": 3,
    "airfrictioncoefs2": [0.001,0.0005,6e-005],
    "airfrictioncoefs1": [0.1,0.05,0.006],
    "airfrictioncoefs0": [0,0,0],
    "fuelcapacity": 1000,
    "insidesoundcoef": 0.0316228,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "irscanrangemin": 2000,
    "irscanrangemax": 10000,
    "irscantoeyefactor": 2,
    "nightvision": 0,
    "enablegps": 1,
    "weaponsgroup1": "1 + 		2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
    "editorsubcategory": "EdSubcat_Planes",
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    # Class: CfgVehicles|Air|DustEffects [Indent level: 1],
    "dusteffects": {
        # Class: CfgDustEffectsAir|Both [Indent level: 0]
        "both": {
        },
        # Class: CfgDustEffectsAir|Left [Indent level: 0],
        "left": {
            "default": ["LDustEffectsAir"],
            "gdtstratisconcrete": ["LDustEffectsAir","LDirtEffects"],
            "gdtstratisbeach": ["LDustEffectsAir","LStonesEffects"],
            "gdtstratisdirt": ["LDustEffectsAir","LDirtEffects"],
            "gdtstratisseabedcluttered": ["LDustEffectsAir"],
            "gdtstratisseabed": ["LDustEffectsAir"],
            "gdtstratisdrygrass": ["LDustEffectsAir","LGrassDryEffects","LDirtEffects"],
            "gdtstratisgreengrass": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstratisrocky": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstratisthistles": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtconcrete": ["LDustEffectsAir","LDirtEffects"],
            "gdtasphalt": ["LDustEffectsAir","LDirtEffects"],
            "gdtrubble": ["LDustEffectsAir","LDirtEffects"],
            "gdtsoil": ["LDustEffectsAir","LDirtEffects"],
            "gdtbeach": ["LDustEffectsAir","LStonesEffects"],
            "gdtrock": ["LDustEffectsAir","LDirtEffects"],
            "gdtdead": ["LDustEffectsAir","LDirtEffects"],
            "gdtdesert1": ["LDustEffectsAir","LSandEffects","LDirtEffects","LStonesEffects"],
            "gdtdesert2": ["LDustEffectsAir","LSandEffects","LGrassEffects","LDirtEffects"],
            "gdtdirt": ["LDustEffectsAir","LDirtEffects"],
            "gdtgrassgreen": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtgrassdry": ["LDustEffectsAir","LGrassDryEffects","LDirtEffects"],
            "gdtgrasswild": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtwildfield": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtweed1": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtweed2": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtthorn": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstony": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstonygreen": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstonythistle": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtseabeddeep": ["LDustEffectsAir"],
            "gdtseabed": ["LDustEffectsAir"],
            "surfroaddirt": ["LDustEffectsAir"],
            "surfroadconcrete": ["LDustEffectsAir"],
            "surfroadtarmac": ["LDustEffectsAir"],
            "surfwood": ["LDustEffectsAir"],
            "surfmetal": ["LDustEffectsAir"],
            "surfrooftin": ["LDustEffectsAir"],
            "surfrooftiles": ["LDustEffectsAir"],
            "surfintwood": ["LDustEffectsAir"],
            "surfintconcrete": ["LDustEffectsAir"],
            "surfinttiles": ["LDustEffectsAir"],
            "surfintmetal": ["LDustEffectsAir"],
            "gdtgrassshort": ["LDustEffectsAir","LGrassEffects"],
            "gdtgrasstall": ["LDustEffectsAir","LGrassEffects"],
            "gdtreddirt": ["LDustEffectsAirRed"],
            "gdtfield": ["LDustEffectsAir"],
            "gdtforest": ["LDustEffectsAir"],
            "gdtvolcano": ["LDustEffectsAir","LStonesEffects"],
            "gdtcliff": ["LDustEffectsAir"],
            "gdtvolcanobeach": ["LDustEffectsAir"],
            "surfroaddirt_exp": ["LDustEffectsAirRed"],
            "surfroadconcrete_exp": ["LDustEffectsAir"],
            "surfroadtarmac_exp": ["LDustEffectsAir"],
            "gdtkldirt": ["LDustEffectsAir"],
            "gdtklgrass1": ["LDustEffectsAir","LGrassEffects"],
            "gdtklgrass2": ["LDustEffectsAir","LGrassEffects"],
            "gdtklforestcon": ["LDustEffectsAir"],
            "gdtklforestdec": ["LDustEffectsAir"],
            "gdtklmud": ["LDustEffectsAir"],
            "gdtklsoil": ["LDustEffectsAir"],
            "gdtkltarmac": ["LDustEffectsAir"],
            "gdtklstubble": ["LDustEffectsAir"],
            "gdtklstones": ["LDustEffectsAir"],
            "surfroaddirt_enoch": ["LDustEffectsAir"],
            "surftraildirt_enoch": ["LDustEffectsAir"],
            "surfroadtarmac1_enoch": ["LDustEffectsAir"],
            "surfroadtarmac2_enoch": ["LDustEffectsAir"],
            "surfroadtarmac3_enoch": ["LDustEffectsAir"]
        },
        # Class: CfgDustEffectsAir|Right [Indent level: 0],
        "right": {
            "default": ["RDustEffectsAir"],
            "gdtstratisconcrete": ["RDustEffectsAir","RDirtEffects"],
            "gdtstratisbeach": ["RDustEffectsAir","RStonesEffects"],
            "gdtstratisdirt": ["RDustEffectsAir","RDirtEffects"],
            "gdtstratisseabedcluttered": ["RDustEffectsAir"],
            "gdtstratisseabed": ["RDustEffectsAir"],
            "gdtstratisdrygrass": ["RDustEffectsAir","RGrassDryEffects","RDirtEffects"],
            "gdtstratisgreengrass": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstratisrocky": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstratisthistles": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtconcrete": ["RDustEffectsAir","RDirtEffects"],
            "gdtasphalt": ["RDustEffectsAir","RDirtEffects"],
            "gdtrubble": ["RDustEffectsAir","RDirtEffects"],
            "gdtsoil": ["RDustEffectsAir","RDirtEffects"],
            "gdtbeach": ["RDustEffectsAir","RStonesEffects"],
            "gdtrock": ["RDustEffectsAir","RDirtEffects"],
            "gdtdead": ["RDustEffectsAir","RDirtEffects"],
            "gdtdesert1": ["RDustEffectsAir","RSandEffects","RDirtEffects","RStonesEffects"],
            "gdtdesert2": ["RDustEffectsAir","RSandEffects","RGrassEffects","RDirtEffects"],
            "gdtdirt": ["RDustEffectsAir","RDirtEffects"],
            "gdtgrassgreen": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtgrassdry": ["RDustEffectsAir","RGrassDryEffects","RDirtEffects"],
            "gdtgrasswild": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtwildfield": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtweed1": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtweed2": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtthorn": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstony": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstonygreen": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstonythistle": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtseabeddeep": ["RDustEffectsAir"],
            "gdtseabed": ["RDustEffectsAir"],
            "surfroaddirt": ["RDustEffectsAir"],
            "surfroadconcrete": ["RDustEffectsAir"],
            "surfroadtarmac": ["RDustEffectsAir"],
            "surfwood": ["RDustEffectsAir"],
            "surfmetal": ["RDustEffectsAir"],
            "surfrooftin": ["RDustEffectsAir"],
            "surfrooftiles": ["RDustEffectsAir"],
            "surfintwood": ["RDustEffectsAir"],
            "surfintconcrete": ["RDustEffectsAir"],
            "surfinttiles": ["RDustEffectsAir"],
            "surfintmetal": ["RDustEffectsAir"],
            "gdtgrassshort": ["RDustEffectsAir","RGrassEffects"],
            "gdtgrasstall": ["RDustEffectsAir","RGrassEffects"],
            "gdtreddirt": ["RDustEffectsAirRed"],
            "gdtfield": ["RDustEffectsAir"],
            "gdtforest": ["RDustEffectsAir"],
            "gdtvolcano": ["RDustEffectsAir","RStonesEffects"],
            "gdtcliff": ["RDustEffectsAir"],
            "gdtvolcanobeach": ["RDustEffectsAir"],
            "surfroaddirt_exp": ["RDustEffectsAirRed"],
            "surfroadconcrete_exp": ["RDustEffectsAir"],
            "surfroadtarmac_exp": ["RDustEffectsAir"],
            "gdtkldirt": ["RDustEffectsAir"],
            "gdtklgrass1": ["RDustEffectsAir","RGrassEffects"],
            "gdtklgrass2": ["RDustEffectsAir","RGrassEffects"],
            "gdtklforestcon": ["RDustEffectsAir"],
            "gdtklforestdec": ["RDustEffectsAir"],
            "gdtklmud": ["RDustEffectsAir"],
            "gdtklsoil": ["RDustEffectsAir"],
            "gdtkltarmac": ["RDustEffectsAir"],
            "gdtklstubble": ["RDustEffectsAir"],
            "gdtklstones": ["RDustEffectsAir"],
            "surfroaddirt_enoch": ["RDustEffectsAir"],
            "surftraildirt_enoch": ["RDustEffectsAir"],
            "surfroadtarmac1_enoch": ["RDustEffectsAir"],
            "surfroadtarmac2_enoch": ["RDustEffectsAir"],
            "surfroadtarmac3_enoch": ["RDustEffectsAir"]
        }
    },
    "maxfordingdepth": 0.001,
    "waterresistance": 1,
    "impacteffectssea": "ImpactEffectsAir",
    "flarevelocity": 100,
    "enableradio": 1,
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "radartype": 4,
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
    "memorypointdriveroptics": ["driverview","pilot"],
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
    "driverleftleganimname": "",
    "driverrightleganimname": "",
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
    "availableforsupporttypes": [],
    "waterppinvehicle": 1,
    "htmin": 60,
    "htmax": 1800,
    "afmax": 200,
    "mfmax": 100,
    "mfact": 0.2,
    "tbody": 150,
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
    "scope": 0,
    "reversed": 1,
    "autocenter": 1,
    "animated": 1,
    "shadow": 1,
    "featuretype": 0,
    "side": 4,
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
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 5,
    "antirollbarspeedmin": 20,
    "antirollbarspeedmax": 60,
    "slowspeedforwardcoef": 0.3,
    "normalspeedforwardcoef": 0.85,
    "gunnerhasflares": 1,
    "enablemanualfire": 1,
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "portrait": "",
    "ghostpreview": "",
    "armorlights": 0.4,
    "crewvulnerable": 1,
    "damageresistance": 0.004,
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
    "laserscanner": 0,
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
    "showalltargets": 0,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "wheelcircumference": 1,
    "waterangulardampingcoef": 0,
    "shownvgdriver": 0,
    "shownvgcommander": 0,
    "shownvggunner": 0,
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
    "soundwoodcrash": ["emptySound",0],
    "soundbushcrash": ["emptySound",0],
    "soundbuildingcrash": ["emptySound",0],
    "soundarmorcrash": ["emptySound",0],
    "soundlocked": ["",1,1],
    "aggregatereflectors": [],
    "driverinaction": "",
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "hideproxyincombat": 0,
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
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
    "headaimdown": 0,
    "drivercaneject": 1,
    "fireresistance": 10,
    "aircapacity": 10,
    "waterdamageengine": 0.2,
    "damagetexdelay": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "windsockexist": 0,
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "damagehalf": [],
    "damagefull": [],
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "features": "",
    "insidedetectcoef": 0.05,
}