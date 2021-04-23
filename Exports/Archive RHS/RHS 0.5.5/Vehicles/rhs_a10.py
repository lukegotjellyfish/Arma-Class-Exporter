rhs_a10 = {
    "rhs_gearanim": "Gear_1",
    "dlc": "RHS_USAF",
    "editorpreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhs_a10.paa",
    "scope": 2,
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_axisoffsettarget": [0,8,0.27],
    "lesh_wheeloffset": [0,0],
    "category": "Air",
    "side": 1,
    "crew": "rhsusf_airforce_jetpilot",
    "typicalcargo": ["rhsusf_airforce_jetpilot"],
    "vehicleclass": "rhs_vehclass_aircraft",
    "faction": "rhs_faction_usaf",
    "displayname": "A-10A",
    "author": "Red Hammer Studios",
    "model": "rhsusf|addons|rhsusf_a2port_air|a10|A10.p3d",
    "picture": "rhsusf|addons|rhsusf_a2port_air|data|ico|rhs_a10a_pic_ca.paa",
    "icon": "rhsusf|addons|rhsusf_a2port_air|data|mapico|icon_a10_ca.paa",
    "mapsize": 17,
    "hiddenselections": ["Camo1","Camo2","screen","pip"],
    "hiddenselectionstextures": ["|rhsusf|addons|rhsusf_a2port_air|a10|data|a10_01_co.paa","|rhsusf|addons|rhsusf_a2port_air|a10|data|a10_02_co.paa","",""],
    "drivercaneject": 1,
    "ejectdamagelimit": 1,
    "drivercompartments": 1,
    "camouflage": 10,
    "audible": 6,
    "accuracy": 0.2,
    "supplyradius": 8,
    "lockdetectionsystem": "8 + 4",
    "incomingmissiledetectionsystem": "8",
    "radartype": 4,
    "laserscanner": 1,
    "irscanrangemin": 100,
    "irscanrangemax": 10500,
    "irscantoeyefactor": 2,
    "irscanground": 1,
    "minfiretime": 10,
    "headaimdown": 0,
    "camshakecoef": 0.6,
    "headgforceleaningfactor": [0.005,0.001,0.015],
    "allowtablock": 0,
    # Class: CfgVehicles|RHS_A10|EjectionSystem [Indent level: 1],
    "ejectionsystem": {
    },
    "soundlocked": ["a3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",1.12202,1],
    "irtarget": 1,
    "irtargetsize": 1,
    "visualtarget": 1,
    "visualtargetsize": 1,
    "radartarget": 1,
    "radartargetsize": 1,
    "unitinfotype": "RHSUSF_RscUnitInfoJet",
    "driverweaponsinfotype": "RHSUSF_RscOptics_A10A_TVM",
    "driveraction": "rhs_A10_Pilot",
    "driverlefthandanimname": "lever_pilot",
    "driverrighthandanimname": "stick_pilot",
    "driverleftleganimname": "pedal_l",
    "driverrightleganimname": "pedal_r",
    "cabinopening": 1,
    "precisegetinout": 1,
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetindriverprecise": "pos driver",
    "selectionfireanim": "zasleh",
    "memorypointlrocket": "L Raketa",
    "memorypointrrocket": "P Raketa",
    "memorypointldust": "levy prach",
    "memorypointrdust": "pravy prach",
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "weapons": ["rhs_weap_MASTERSAFE","RHS_weap_gau8"],
    "magazines": ["rhs_mag_1150Rnd_30x173_mixed"],
    "threat": [1,1,1],
    # Class: CfgVehicles|RHS_A10|Turrets [Indent level: 1],
    "turrets": {
    },
    # Class: CfgVehicles|RHS_A10|pilotCamera [Indent level: 1],
    "pilotcamera": {
        # Class: CfgVehicles|RHS_A10|pilotCamera|OpticsIn [Indent level: 2]
        "opticsin": {
            # Class: CfgVehicles|RHS_A10|pilotCamera|OpticsIn|Wide [Indent level: 3]
            "wide": {
                "opticsdisplayname": "DEFAULT",
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.116667,
                "minfov": 0.116667,
                "maxfov": 0.116667,
                "directionstabilized": 0,
                "visionmode": ["Ti"],
                "thermalmode": [0],
                "gunneropticsmodel": "rhsusf|addons|rhsusf_a2port_air|A10|rhs_tvm_3x.p3d"
            },
            # Class: CfgVehicles|RHS_A10|pilotCamera|OpticsIn|Narrow [Indent level: 3],
            "narrow": {
                "opticsdisplayname": "ZOOM",
                "initfov": 0.0583333,
                "minfov": 0.0583333,
                "maxfov": 0.0583333,
                "gunneropticsmodel": "rhsusf|addons|rhsusf_a2port_air|A10|rhs_tvm_6x.p3d",
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "directionstabilized": 0,
                "visionmode": ["Ti"],
                "thermalmode": [0]
            }
        },
        "minelev": -60,
        "maxelev": 60,
        "initelev": 0,
        "minturn": -60,
        "maxturn": 60,
        "maxxrotspeed": 0.25,
        "maxyrotspeed": 0.25,
        "pilotopticsshowcursor": 0,
        "controllable": 1
    },
    "memorypointdriveroptics": "tvm1",
    # Class: CfgVehicles|RHS_A10|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            "uipicture": "rhsusf|addons|rhsusf_a2port_air|data|loadouts|RHS_A10_EDEN_CA.paa",
            # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon1 [Indent level: 4]
                "pylon1": {
                    "hardpoints": ["RHS_HP_AIM9_2x","RHS_HP_LGB_500","RHS_HP_ECM"],
                    "priority": 5,
                    "maxweight": 1200,
                    "uiposition": [0.3,0.55],
                    "bay": -1,
                    "attachment": "rhs_mag_ANALQ131",
                    "hitpoint": "HitPylon1"
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon2 [Indent level: 4],
                "pylon2": {
                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF"],
                    "priority": 4,
                    "maxweight": 1200,
                    "uiposition": [0.3,0.5],
                    "bay": -1,
                    "attachment": "rhs_mag_M151_7_USAF_LAU131",
                    "hitpoint": "HitPylon2"
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon3 [Indent level: 4],
                "pylon3": {
                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_FFAR_USAF_3x","RHS_HP_HYDRA_USAF","RHS_HP_HYDRA_USAF_3x","RHS_HP_AGM65_3x","RHS_HP_BOMB_500_3x"],
                    "priority": 3,
                    "maxweight": 1200,
                    "uiposition": [0.3,0.45],
                    "bay": -1,
                    "attachment": "rhs_mag_agm65d",
                    "hitpoint": "HitPylon3"
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon4 [Indent level: 4],
                "pylon4": {
                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF","RHS_HP_FFAR_USAF_3x","RHS_HP_HYDRA_USAF_3x","RHS_HP_BOMB_500_3x"],
                    "priority": 2,
                    "maxweight": 1200,
                    "uiposition": [0.35,0.375],
                    "bay": -1,
                    "attachment": "rhs_mag_gbu12",
                    "hitpoint": "HitPylon4"
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon5 [Indent level: 4],
                "pylon5": {
                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF"],
                    "priority": 1,
                    "maxweight": 1200,
                    "uiposition": [0.35,0.325],
                    "bay": -1,
                    "attachment": "rhs_mag_gbu12",
                    "hitpoint": "HitPylon5"
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon6 [Indent level: 4],
                "pylon6": {
                    "hardpoints": [],
                    "priority": 1,
                    "maxweight": 1200,
                    "uiposition": [0.35,0.275],
                    "bay": -1,
                    "attachment": "",
                    "hitpoint": "HitPylon6"
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon7 [Indent level: 4],
                "pylon7": {
                    "uiposition": [0.35,0.225],
                    "mirroredmissilepos": 5,
                    "hitpoint": "HitPylon7",
                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF"],
                    "priority": 1,
                    "maxweight": 1200,
                    "bay": -1,
                    "attachment": "rhs_mag_gbu12"
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon8 [Indent level: 4],
                "pylon8": {
                    "uiposition": [0.35,0.175],
                    "mirroredmissilepos": 4,
                    "hitpoint": "HitPylon8",
                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_HYDRA_USAF","RHS_HP_FFAR_USAF_3x","RHS_HP_HYDRA_USAF_3x","RHS_HP_BOMB_500_3x"],
                    "priority": 2,
                    "maxweight": 1200,
                    "bay": -1,
                    "attachment": "rhs_mag_gbu12"
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon9 [Indent level: 4],
                "pylon9": {
                    "uiposition": [0.3,0.1],
                    "mirroredmissilepos": 3,
                    "hitpoint": "HitPylon9",
                    "hardpoints": ["RHS_HP_LGB_500","RHS_HP_LGB_1000","RHS_HP_FFAR_USAF","RHS_HP_FFAR_USAF_3x","RHS_HP_HYDRA_USAF","RHS_HP_HYDRA_USAF_3x","RHS_HP_AGM65_3x","RHS_HP_BOMB_500_3x"],
                    "priority": 3,
                    "maxweight": 1200,
                    "bay": -1,
                    "attachment": "rhs_mag_agm65d"
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|pylon10 [Indent level: 4],
                "pylon10": {
                    "uiposition": [0.3,0.05],
                    "mirroredmissilepos": 2,
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
                    "uiposition": [0.3,0],
                    "attachment": "rhs_mag_aim9m_2",
                    "mirroredmissilepos": 1,
                    "hitpoint": "HitPylon11",
                    "priority": 5,
                    "maxweight": 1200,
                    "bay": -1
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4],
                "cmdispenser": {
                    "hardpoints": ["RHSUSF_cm_ANALE40_x2","RHSUSF_cm_ANALE40_x4","RHSUSF_cm_ANALE40_x8","RHSUSF_cm_ANALE40_x16"],
                    "priority": 1,
                    "attachment": "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x16",
                    "maxweight": 800,
                    "uiposition": [0.625,0.275]
                }
            },
            # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|Presets [Indent level: 3],
            "presets": {
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|Presets|AT [Indent level: 4]
                "at": {
                    "attachment": ["rhs_mag_ANALQ131","rhs_mag_M151_7_USAF_LAU131","rhs_mag_agm65d_3","rhs_mag_gbu12","rhs_mag_gbu12","","rhs_mag_gbu12","rhs_mag_gbu12","rhs_mag_agm65d_3","rhs_mag_M151_7_USAF_LAU131","rhs_mag_aim9m_2","rhsusf_ANALE40_CMFlare_Chaff_Magazine_x16"],
                    "displayname": "Anti-Tank"
                },
                # Class: CfgVehicles|RHS_A10|Components|TransportPylonsComponent|Presets|CAS [Indent level: 4],
                "cas": {
                    "attachment": ["rhs_mag_ANALQ131","rhs_mag_M151_7_USAF_LAU131","rhs_mag_agm65d","rhs_mag_gbu12","rhs_mag_gbu12","","rhs_mag_gbu12","rhs_mag_gbu12","rhs_mag_agm65d","rhs_mag_M151_7_USAF_LAU131","rhs_mag_aim9m_2","rhsusf_ANALE40_CMFlare_Chaff_Magazine_x16"],
                    "displayname": "Close Air Support"
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|VisualSensorComponent [Indent level: 4]
                "visualsensorcomponent": {
                    # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|VisualSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 500,
                        "maxrange": 4000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|VisualSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 500,
                        "maxrange": 4000,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "anglerangehorizontal": 25,
                    "anglerangevertical": 20,
                    "typerecognitiondistance": -1,
                    "groundnoisedistancecoef": 0.07,
                    "maxgroundnoisedistance": 0,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "maxfogseethrough": 0.95,
                    "mintrackablespeed": 0,
                    "maxtrackablespeed": 695,
                    "animdirection": "PilotCamera_V",
                    "componenttype": "VisualSensorComponent",
                    "nightrangecoef": 0,
                    "color": [1,1,0.5,0.8],
                    "allowsmarking": 1,
                    "aimdown": 0,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4],
                "lasersensorcomponent": {
                    # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|LaserSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 10000,
                        "maxrange": 10000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|LaserSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 10000,
                        "maxrange": 10000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 25,
                    "anglerangevertical": 20,
                    "typerecognitiondistance": -1,
                    "maxgroundnoisedistance": 0,
                    "maxfogseethrough": 0.3,
                    "animdirection": "PilotCamera_V",
                    "componenttype": "LaserSensorComponent",
                    "color": [1,1,1,0],
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|RHS_A10|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4],
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
        # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_A10|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|RHS_A10|Components|ForcedCam [Indent level: 2],
        "forcedcam": {
            "componenttype": "VehicleSystemsDisplayManager",
            "defaultdisplay": "VehicleDriverDisplay",
            "x": 11,
            "y": 11,
            # Class: CfgVehicles|RHS_A10|Components|ForcedCam|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_A10|Components|ForcedCam|Components|VehicleDriverDisplay [Indent level: 4]
                "vehicledriverdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Driver"
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    # Class: CfgVehicles|RHS_A10|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|RHS_A10|AnimationSources|gatling [Indent level: 2]
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
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|eject_hide [Indent level: 2],
        "eject_hide": {
            "source": "user",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Hide_Monitor [Indent level: 2],
        "hide_monitor": {
            "source": "user",
            "animperiod": 1e-005,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|tvm_locked [Indent level: 2],
        "tvm_locked": {
            "source": "user",
            "animperiod": 1e-005,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|ind_beacon_source [Indent level: 2],
        "ind_beacon_source": {
            "source": "user",
            "animperiod": 1e-005,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|throttle_source [Indent level: 2],
        "throttle_source": {
            "animperiod": 10,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|HitFuel_1_source [Indent level: 2],
        "hitfuel_1_source": {
            "source": "hit",
            "hitpoint": "HitFuel"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|HitFuel_2_source [Indent level: 2],
        "hitfuel_2_source": {
            "source": "hit",
            "hitpoint": "HitFuel2"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Damper_1_source [Indent level: 2],
        "damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Damper_2_source [Indent level: 2],
        "damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Damper_3_source [Indent level: 2],
        "damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Wheel_1_source [Indent level: 2],
        "wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Wheel_2_source [Indent level: 2],
        "wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|Wheel_3_source [Indent level: 2],
        "wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|RHS_A10|AnimationSources|mirror_fold [Indent level: 2],
        "mirror_fold": {
            "source": "user",
            "animperiod": 0.6,
            "initphase": 0
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
        "gatling_30mm_ammorandom": {
            "source": "ammorandom",
            "weapon": "Gatling_30mm_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Gatling_30mm_reload [Indent level: 2],
        "gatling_30mm_reload": {
            "source": "reload",
            "weapon": "Gatling_30mm_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Gatling_30mm_revolving [Indent level: 2],
        "gatling_30mm_revolving": {
            "source": "revolving",
            "weapon": "Gatling_30mm_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Missile_AA_04_revolving [Indent level: 2],
        "missile_aa_04_revolving": {
            "source": "revolving",
            "weapon": "Missile_AA_04_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Missile_AGM_02_revolving [Indent level: 2],
        "missile_agm_02_revolving": {
            "source": "revolving",
            "weapon": "Missile_AGM_02_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Rocket_04_HE_revolving [Indent level: 2],
        "rocket_04_he_revolving": {
            "source": "revolving",
            "weapon": "Rocket_04_HE_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Rocket_04_AP_revolving [Indent level: 2],
        "rocket_04_ap_revolving": {
            "source": "revolving",
            "weapon": "Rocket_04_AP_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|Bomb_04_revolving [Indent level: 2],
        "bomb_04_revolving": {
            "source": "revolving",
            "weapon": "Bomb_04_Plane_CAS_01_F"
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|HitAvionics [Indent level: 2],
        "hitavionics": {
            "source": "Hit",
            "hitpoint": "HitAvionics",
            "raw": 1
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|HideWeapons [Indent level: 2],
        "hideweapons": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|HideMFD [Indent level: 2],
        "hidemfd": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 1
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|canopy_hide [Indent level: 2],
        "canopy_hide": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|ejection_seat_hide [Indent level: 2],
        "ejection_seat_hide": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|AnimationSources|ejection_seat_motion [Indent level: 2],
        "ejection_seat_motion": {
            "source": "user",
            "animperiod": 0.25,
            "initphase": 0
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightRed_source [Indent level: 2],
        "collisionlightred_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionRed"
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightWhite_source [Indent level: 2],
        "collisionlightwhite_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionWhite"
        }
    },
    # Class: CfgVehicles|RHS_A10|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|RHS_A10|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|RHS_A10|compartmentsLights|Comp1|Light_General [Indent level: 3]
            "light_general": {
                "color": [20,30,30],
                "ambient": [0,0,0],
                "intensity": 8.05,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 1,
                "blinking": 0,
                # Class: CfgVehicles|RHS_A10|compartmentsLights|Comp1|Light_General|Attenuation [Indent level: 4],
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
    # Class: CfgVehicles|RHS_A10|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|RHS_A10|Reflectors|Gear_Light [Indent level: 2]
        "gear_light": {
            "color": [70,75,100,1],
            "ambient": [1,1,1,0],
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerangle": 20,
            "outerangle": 50,
            "conefadecoef": 3,
            "intensity": 1000,
            "useflare": 0,
            "daylight": 1,
            "flaresize": 4,
            # Class: CfgVehicles|RHS_A10|Reflectors|Gear_Light|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.15,
                "hardlimitstart": 55,
                "hardlimitend": 100
            }
        },
        # Class: CfgVehicles|RHS_A10|Reflectors|Gear_Light_Flare [Indent level: 2],
        "gear_light_flare": {
            "outerangle": 179,
            "useflare": 1,
            "intensity": 50,
            "conefadecoef": 13,
            # Class: CfgVehicles|RHS_A10|Reflectors|Gear_Light_Flare|Attenuation [Indent level: 3],
            "attenuation": {
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
            "innerangle": 20,
            "daylight": 1,
            "flaresize": 4
        }
    },
    "aggregatereflectors": [["Gear_Light"],["Gear_Light_Flare"]],
    # Class: CfgVehicles|RHS_A10|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionRed [Indent level: 2]
        "collisionred": {
            "color": [0.8,0,0],
            "ambient": [0.09,0,0],
            "intensity": 75,
            "name": "cerveny pozicni",
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.05,
            "activelight": 0,
            "blinking": 1,
            "daylight": 0,
            "useflare": 0,
            "blinkingpattern": [0.2,1.3],
            "blinkingpatternguarantee": 0,
            # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionGreen [Indent level: 2],
        "collisiongreen": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "zeleny pozicni",
            "blinkingpattern": [0.2,0.9],
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.05,
            "activelight": 0,
            "blinking": 1,
            "daylight": 0,
            "useflare": 0,
            "blinkingpatternguarantee": 0,
            # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|RHS_A10|MarkerLights|PositionWhiteTop [Indent level: 2],
        "positionwhitetop": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "bily pozicni",
            "drawlightsize": 0.2,
            "blinking": 0,
            "intensity": 75,
            "drawlight": 1,
            "drawlightcentersize": 0.05,
            "activelight": 0,
            "daylight": 0,
            "useflare": 0,
            "blinkingpattern": [0.2,1.3],
            "blinkingpatternguarantee": 0,
            # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionWhiteRear [Indent level: 2],
        "collisionwhiterear": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "cerveny pozicni blik",
            "blinkingpatternguarantee": 0,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.04,
            "intensity": 75,
            "drawlight": 1,
            "activelight": 0,
            "blinking": 1,
            "daylight": 0,
            "useflare": 0,
            "blinkingpattern": [0.2,1.3],
            # Class: CfgVehicles|RHS_A10|MarkerLights|CollisionRed|Attenuation [Indent level: 3],
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
    # Class: CfgVehicles|RHS_A10|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|RHS_A10|RenderTargets|Mirror [Indent level: 2]
        "mirror": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|RHS_A10|RenderTargets|Mirror|CameraView1 [Indent level: 3],
            "cameraview1": {
                "pointposition": "PIP_mirror_0",
                "pointdirection": "PIP_mirror_0_dir",
                "renderquality": 0,
                "rendervisionmode": 0,
                "fov": 1
            },
            "bboxes": ["PIP_0_TL","PIP_0_TR","PIP_0_BL","PIP_0_BR"]
        }
    },
    "damageresistance": 0.0048,
    "epeimpulsedamagecoef": 1,
    "maxspeed": 834,
    "landingaoa": "rad 10",
    "landingspeed": 220,
    "gearuptime": 4.5,
    "geardowntime": 3,
    "angleofindicence": 0.0523599,
    "draconicforcexcoef": 7.2,
    "draconicforceycoef": 2.6,
    "draconicforcezcoef": 0.15,
    "draconictorquexcoef": 1.29,
    "draconictorqueycoef": 3.1,
    "thrustcoef": [0.91,0.84,0.9,1.3,1.2,1.2,1.1,1,0.93,0.2,0.1,0,0],
    "envelope": [0,0.1,0.61,2.2,3.7,4.9,6,5.5,5.8,4.7,3.4,1.8,0],
    "aileroncontrolssensitivitycoef": 3,
    "elevatorcontrolssensitivity": 2,
    "ruddercontrolssensitivitycoef": 4,
    "elevatorcoef": [0.7,0.9,0.55,0.4,0.39,0.3,0.3],
    "aileroncoef": [0.6,1,0.97,0.9,0.85,0.87,0.75],
    "ruddercoef": [0.7,1,1,0.9,0.82,0.73,0.6],
    "brakedistance": 85,
    "aileronsensitivity": 0.75,
    "elevatorsensitivity": 1.9,
    "wheelsteeringsensitivity": 1.6,
    "flapsfrictioncoef": 0.6,
    "airfriction0": [100,60,12],
    "airfriction1": [100,60,12],
    "airfriction2": [100,60,12],
    # Class: CfgVehicles|RHS_A10|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|RHS_A10|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
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
    "transportitems": {
        # Class: CfgVehicles|RHS_A10|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 2
        }
    },
    # Class: CfgVehicles|RHS_A10|WingVortices [Indent level: 1],
    "wingvortices": {
        # Class: CfgVehicles|RHS_A10|WingVortices|WingTipLeft [Indent level: 2]
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "body_vapour_L_E"
        },
        # Class: CfgVehicles|RHS_A10|WingVortices|WingTipRight [Indent level: 2],
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "body_vapour_R_E"
        },
        # Class: CfgVehicles|RHS_A10|WingVortices|BodyLeft [Indent level: 2],
        "bodyleft": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles|RHS_A10|WingVortices|BodyRight [Indent level: 2],
        "bodyright": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_S"
        }
    },
    "attenuationeffecttype": "HeliAttenuation",
    # Class: CfgVehicles|RHS_A10|Damage [Indent level: 1],
    "damage": {
        "tex": ["rhsusf|addons|rhsusf_a2port_air|a10|data|rhs_a10_warning_lights_off_ca.paa","rhsusf|addons|rhsusf_a2port_air|a10|data|rhs_a10_warning_lights_ca.paa"],
        "mat": ["rhsusf|addons|rhsusf_a2port_air|a10|data|a10_skla.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|a10_skla_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|a10_skla_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|a10_cockpit_glass_in.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|a10_cockpit_glass_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|a10_cockpit_glass_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_01.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_01_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_01_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_02.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_02_damage.rvmat","rhsusf|addons|rhsusf_a2port_air|a10|data|A10_02_destruct.rvmat"]
    },
    # Class: CfgVehicles|RHS_A10|Library [Indent level: 1],
    "library": {
        "libenable": 1,
        "libtextdesc": "The Fairchild Republic A-10 Thunderbolt II is an American twin/single-seat, twin-engine, straight-wing jet aircraft developed by Fairchild-Republic in the early 1970s. The A-10 was designed around the GAU-8 Avenger, a rotary cannon that is the airplane's primary armament and the heaviest such cannon mounted on an aircraft. The A-10's airframe was designed for survivability, with protective measures such as 1,200 pounds (540 kg) of armor to enable the aircraft to continue flying after taking significant damage."
    },
    "availableforsupporttypes": ["CAS_Bombing"],
    "armor": 60,
    "armorstructural": 2,
    # Class: CfgVehicles|RHS_A10|Hitpoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitHull [Indent level: 2]
        "hithull": {
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0.01,
            "minimalhit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull",
            "visual": "-",
            "depends": "Total"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 0.2,
            "explosionshielding": 0.6,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.5,
            "explosionshielding": 0.25,
            "passthrough": 0.2,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_l",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "armor": 0.5,
            "explosionshielding": 0.25,
            "passthrough": 0.2,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_r",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 1,
            "explosionshielding": 0.2,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel",
            "visual": "vis_fuel",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitFuel_left [Indent level: 2],
        "hitfuel_left": {
            "armor": 0.5,
            "explosionshielding": 0.7,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_fuel_wing_l",
            "visual": "vis_wing_l",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitFuel_right [Indent level: 2],
        "hitfuel_right": {
            "armor": 0.5,
            "explosionshielding": 0.7,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_fuel_wing_r",
            "visual": "vis_wing_r",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitFuel2 [Indent level: 2],
        "hitfuel2": {
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0.1,
            "minimalhit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "-",
            "depends": "(HitFuel_left+HitFuel_right)*0.5"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitLAileron_link [Indent level: 2],
        "hitlaileron_link": {
            "armor": 0.6,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_l",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitRAileron_link [Indent level: 2],
        "hitraileron_link": {
            "armor": 0.6,
            "explosionshielding": 0.6,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_r",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitLAileron [Indent level: 2],
        "hitlaileron": {
            "armor": 0.6,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "visual": "vis_wing_l",
            "depends": "HitLAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitRAileron [Indent level: 2],
        "hitraileron": {
            "armor": 0.6,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "visual": "vis_wing_r",
            "depends": "HitRAileron_link*0.7"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitControlRear [Indent level: 2],
        "hitcontrolrear": {
            "armor": 0.6,
            "explosionshielding": 0.1,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.17,
            "material": -1,
            "name": "hit_control_rear",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitLCElevator [Indent level: 2],
        "hitlcelevator": {
            "armor": 0.6,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitRElevator [Indent level: 2],
        "hitrelevator": {
            "armor": 0.6,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitLCRudder [Indent level: 2],
        "hitlcrudder": {
            "armor": 0.7,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.02,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder_l",
            "visual": "vis_rudder_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitRRudder [Indent level: 2],
        "hitrrudder": {
            "armor": 0.7,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.02,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder_r",
            "visual": "vis_rudder_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 0.6,
            "explosionshielding": 0.7,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "glass_1",
            "visual": "glass_1",
            "depends": "0"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|WarningElevator [Indent level: 2],
        "warningelevator": {
            "armor": 9999,
            "explosionshielding": 0,
            "passthrough": 0,
            "minimalhit": 1,
            "radius": 0,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "ind_elevator",
            "depends": "HitLCElevator+HitRElevator"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|WarningAileron [Indent level: 2],
        "warningaileron": {
            "armor": 9999,
            "explosionshielding": 0,
            "passthrough": 0,
            "minimalhit": 1,
            "radius": 0,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "ind_aileron",
            "depends": "HitLAileron+HitRAileron"
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1 [Indent level: 2],
        "hitpylon1": {
            "armor": -30,
            "name": "hit_pylon_1",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2 [Indent level: 2],
        "hitpylon2": {
            "armor": -30,
            "name": "hit_pylon_2",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3 [Indent level: 2],
        "hitpylon3": {
            "armor": -30,
            "name": "hit_pylon_3",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4 [Indent level: 2],
        "hitpylon4": {
            "armor": -30,
            "name": "hit_pylon_4",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5 [Indent level: 2],
        "hitpylon5": {
            "armor": -30,
            "name": "hit_pylon_5",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6 [Indent level: 2],
        "hitpylon6": {
            "armor": -30,
            "name": "hit_pylon_6",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7 [Indent level: 2],
        "hitpylon7": {
            "armor": -30,
            "name": "hit_pylon_7",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8 [Indent level: 2],
        "hitpylon8": {
            "armor": -30,
            "name": "hit_pylon_8",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_8",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_8",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_8",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon8|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_8",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9 [Indent level: 2],
        "hitpylon9": {
            "armor": -30,
            "name": "hit_pylon_9",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_9",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_9",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_9",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon9|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_9",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10 [Indent level: 2],
        "hitpylon10": {
            "armor": -30,
            "name": "hit_pylon_10",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_10",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_10",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_10",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon10|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_10",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11 [Indent level: 2],
        "hitpylon11": {
            "armor": -30,
            "name": "hit_pylon_11",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_11",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_11",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_11",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_A10|Hitpoints|HitPylon11|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_11",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        }
    },
    # Class: CfgVehicles|RHS_A10|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|RHS_A10|UserActions|SAFEMODE [Indent level: 2]
        "safemode": {
            "displayname": "<t color='#00FF7F'>MASTERSAFE</t>",
            "condition": "(call rhsusf_fnc_findPlayer) in this",
            "statement": "(call rhsusf_fnc_findPlayer) action ['SwitchWeapon', this, (call rhsusf_fnc_findPlayer), -1];",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showwindow": 0,
            "shortcut": "user13",
            "hideonuse": 1
        },
        # Class: CfgVehicles|RHS_A10|UserActions|Toggle_LandingMode [Indent level: 2],
        "toggle_landingmode": {
            "displayname": "Toggle Landing Mode",
            "condition": "(call rhsusf_fnc_findPlayer) in this && currentWeapon this == ''",
            "statement": "this setUserMFDvalue [4, abs(((getUserMFDvalue this) select 4)-1)]",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showwindow": 0,
            "shortcut": "user14",
            "hideonuse": 1
        },
        # Class: CfgVehicles|RHS_A10|UserActions|Mirrors [Indent level: 2],
        "mirrors": {
            "displayname": "<t color='#FBB829'>Toggle mirrors</t>",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showwindow": 0,
            "hideonuse": 1,
            "condition": "(call rhs_fnc_findPlayer) in this",
            "shortcut": "",
            "statement": "this animateSource ['mirror_fold',abs((this animationSourcePhase 'mirror_fold') -1)]"
        }
    },
    # Class: CfgVehicles|RHS_A10|EventHandlers [Indent level: 1],
    "eventhandlers": {
        "hit": "",
        # Class: CfgVehicles|RHS_A10|EventHandlers|RHSUSF_EventHandlers [Indent level: 2],
        "rhsusf_eventhandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "getout": "[_this select 0, _this select 2,'rhs_a10_canopy'] call rhs_fnc_ACESII_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes;"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "defaultusermfdvalues": [0.15,1,0.15,1,0],
    # Class: CfgVehicles|RHS_A10|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD [Indent level: 2]
        "airplanehud": {
            "topleft": "HUD LH",
            "topright": "HUD PH",
            "bottomleft": "HUD LD",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0.2,
            "color": [0.15,1,0.15,1],
            "enableparallax": 1,
            "font": "rhsusf_digital_font_usa",
            # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|PlaneOrientation [Indent level: 4]
                "planeorientation": {
                    "type": "fixed",
                    "pos": [0.498,0.48]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|WeaponAim [Indent level: 4],
                "weaponaim": {
                    "type": "vector",
                    "source": "weapon",
                    "pos0": [0.498,0.485],
                    "pos10": [1.256,1.41]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|WeaponAimAA [Indent level: 4],
                "weaponaimaa": {
                    "type": "vector",
                    "source": "weapon",
                    "pos0": [0.498,0.085],
                    "pos10": [1.256,1.11]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|Target [Indent level: 4],
                "target": {
                    "type": "vector",
                    "source": "target",
                    "pos0": [0.498,0.535],
                    "pos10": [1.256,1.56]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|TargetingPodDir [Indent level: 4],
                "targetingpoddir": {
                    "source": "pilotcamera",
                    "type": "vector",
                    "pos0": [0.498,0.435],
                    "pos10": [1.306,1.56]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|TargetingPodTarget [Indent level: 4],
                "targetingpodtarget": {
                    "source": "pilotcameratarget",
                    "pos0": [0.498,0.535],
                    "pos10": [1.256,1.56],
                    "type": "vector"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|ImpactPoint [Indent level: 4],
                "impactpoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.485],
                    "pos10": [1.258,1.41]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|NormalizeBombCircle [Indent level: 4],
                "normalizebombcircle": {
                    "type": "normalizedorsmaller",
                    "limit": 0.08,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.498,0.485],
                    "pos10": [1.256,1.41]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],
                "level0": {
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP05 [Indent level: 4],
                "levelp05": {
                    "angle": 5,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM05 [Indent level: 4],
                "levelm05": {
                    "angle": -5,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": 10,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": -10,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": 15,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": -15,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": 20,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": -20,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": 25,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": -25,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": 30,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": -30,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": 35,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": -35,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": 40,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": -40,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": 45,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": -45,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP50 [Indent level: 4],
                "levelp50": {
                    "angle": 50,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM50 [Indent level: 4],
                "levelm50": {
                    "angle": -50,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP60 [Indent level: 4],
                "levelp60": {
                    "angle": 60,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM60 [Indent level: 4],
                "levelm60": {
                    "angle": -60,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP70 [Indent level: 4],
                "levelp70": {
                    "angle": 70,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM70 [Indent level: 4],
                "levelm70": {
                    "angle": -70,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP80 [Indent level: 4],
                "levelp80": {
                    "angle": 80,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM80 [Indent level: 4],
                "levelm80": {
                    "angle": -80,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelP90 [Indent level: 4],
                "levelp90": {
                    "angle": 90,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LevelM90 [Indent level: 4],
                "levelm90": {
                    "angle": -90,
                    "pos0": [0.498,0.48],
                    "pos10": [1.7292,1.884],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|Limit0109 [Indent level: 4],
                "limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LimitWaypoint [Indent level: 4],
                "limitwaypoint": {
                    "type": "limit",
                    "limits": [0.2,0.97,0.8,0.97]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|WPPoint [Indent level: 4],
                "wppoint": {
                    "type": "vector",
                    "source": "WPPoint",
                    "pos0": [0.5,0.485],
                    "pos10": [1.258,1.41]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|VerticalSpeed [Indent level: 4],
                "verticalspeed": {
                    "type": "linear",
                    "source": "vspeed",
                    "sourcescale": 1,
                    "min": -100,
                    "max": 100,
                    "minpos": [0,0.15],
                    "maxpos": [0,-0.15]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|HorizonIndicatorBank [Indent level: 4],
                "horizonindicatorbank": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "sourcescale": 1,
                    "center": [0.065,0.12],
                    "min": -3.14159,
                    "max": 3.14159,
                    "minangle": 0,
                    "maxangle": 360,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|HorizonIndicatorDive [Indent level: 4],
                "horizonindicatordive": {
                    "source": "horizonDive",
                    "min": -1.5708,
                    "max": 1.5708,
                    "minangle": 90,
                    "maxangle": -90,
                    "type": "rotational",
                    "sourcescale": 1,
                    "center": [0.065,0.12],
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|TerrainBone [Indent level: 4],
                "terrainbone": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "sourceoffset": -1,
                    "min": 0,
                    "max": 500,
                    "minpos": [0,-0.195],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|TerrainBone2 [Indent level: 4],
                "terrainbone2": {
                    "sourceoffset": 0,
                    "min": 500,
                    "max": 1500,
                    "minpos": [0,-0.078],
                    "maxpos": [0,0],
                    "type": "linear",
                    "source": "altitudeAGL",
                    "sourcescale": 1
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|VerticalSpeedBone [Indent level: 4],
                "verticalspeedbone": {
                    "type": "linear",
                    "source": "vspeed",
                    "sourcescale": 1,
                    "min": -10,
                    "max": 10,
                    "minpos": [0,-0.32],
                    "maxpos": [0,0.32]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot1 [Indent level: 4],
                "missileflighttimerot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minangle": 0,
                    "maxangle": 18,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot2 [Indent level: 4],
                "missileflighttimerot2": {
                    "maxangle": 37,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot3 [Indent level: 4],
                "missileflighttimerot3": {
                    "maxangle": 55.5,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot4 [Indent level: 4],
                "missileflighttimerot4": {
                    "maxangle": 74,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot5 [Indent level: 4],
                "missileflighttimerot5": {
                    "maxangle": 92.5,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot6 [Indent level: 4],
                "missileflighttimerot6": {
                    "maxangle": 111,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot7 [Indent level: 4],
                "missileflighttimerot7": {
                    "maxangle": 129.5,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot8 [Indent level: 4],
                "missileflighttimerot8": {
                    "maxangle": 148,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot9 [Indent level: 4],
                "missileflighttimerot9": {
                    "maxangle": 166.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot10 [Indent level: 4],
                "missileflighttimerot10": {
                    "maxangle": 185,
                    "max": 10,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot11 [Indent level: 4],
                "missileflighttimerot11": {
                    "maxangle": 203.5,
                    "max": 11,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot12 [Indent level: 4],
                "missileflighttimerot12": {
                    "maxangle": 222,
                    "max": 12,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot13 [Indent level: 4],
                "missileflighttimerot13": {
                    "maxangle": 240.5,
                    "max": 13,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot14 [Indent level: 4],
                "missileflighttimerot14": {
                    "maxangle": 259,
                    "max": 14,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot15 [Indent level: 4],
                "missileflighttimerot15": {
                    "maxangle": 277.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot16 [Indent level: 4],
                "missileflighttimerot16": {
                    "maxangle": 296,
                    "max": 16,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot17 [Indent level: 4],
                "missileflighttimerot17": {
                    "maxangle": 314.5,
                    "max": 17,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot18 [Indent level: 4],
                "missileflighttimerot18": {
                    "maxangle": 333,
                    "max": 18,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot19 [Indent level: 4],
                "missileflighttimerot19": {
                    "maxangle": 351.5,
                    "max": 19,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|MissileFlightTimeRot20 [Indent level: 4],
                "missileflighttimerot20": {
                    "maxangle": 370,
                    "max": 20,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.22032
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|ILS_H [Indent level: 4],
                "ils_h": {
                    "type": "ils",
                    "pos0": [0.5,0.485],
                    "pos3": [0.7274,0.485]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|ILS_W [Indent level: 4],
                "ils_w": {
                    "pos3": [0.5,0.7625],
                    "type": "ils",
                    "pos0": [0.5,0.485]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LarAmmoMax [Indent level: 4],
                "larammomax": {
                    "type": "linear",
                    "source": "LarAmmoMax",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LarAmmoMin [Indent level: 4],
                "larammomin": {
                    "source": "LarAmmoMin",
                    "type": "linear",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Bones|LarTargetDist [Indent level: 4],
                "lartargetdist": {
                    "source": "LarTargetDist",
                    "type": "linear",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                }
            },
            # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw [Indent level: 3],
            "draw": {
                "alpha": "user3",
                "color": ["user0","user1","user2"],
                "condition": "on",
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|PlaneOrientationCrosshair [Indent level: 4],
                "planeorientationcrosshair": {
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "type": "line",
                    "width": 4,
                    "points": [["PlaneOrientation",[-0.01,0],1],["PlaneOrientation",[0.01,0],1],[],["PlaneOrientation",[0,-0.0122032],1],["PlaneOrientation",[0,0.0122032],1],[]]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|PlaneMovementCrosshair [Indent level: 4],
                "planemovementcrosshair": {
                    "cliptl": [0,1],
                    "clipbr": [1,0],
                    "type": "line",
                    "width": 4,
                    "points": [["Velocity",[0,-0.0244063],1],["Velocity",[0.01,-0.0211359],1],["Velocity",[0.01732,-0.0122032],1],["Velocity",[0.02,0],1],["Velocity",[0.01732,0.0122032],1],["Velocity",[0.01,0.0211359],1],["Velocity",[0,0.0244063],1],["Velocity",[-0.01,0.0211359],1],["Velocity",[-0.01732,0.0122032],1],["Velocity",[-0.02,0],1],["Velocity",[-0.01732,-0.0122032],1],["Velocity",[-0.01,-0.0211359],1],["Velocity",[0,-0.0244063],1],[],["Velocity",[0.04,0],1],["Velocity",[0.02,0],1],[],["Velocity",[-0.04,0],1],["Velocity",[-0.02,0],1],[],["Velocity",[0,-0.0488127],1],["Velocity",[0,-0.0244063],1],[]]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BaroStatic [Indent level: 4],
                "barostatic": {
                    "type": "text",
                    "source": "static",
                    "text": "BARO",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.06,0.68],1],
                    "right": [[0.12,0.68],1],
                    "down": [[0.06,0.74],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WeaponGroup [Indent level: 4],
                "weapongroup": {
                    "condition": "mgun + ATmissile + bomb + rocket",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WeaponGroup|SlantRange [Indent level: 5],
                    "slantrange": {
                        "type": "text",
                        "source": "ImpactDistance",
                        "sourcescale": 1,
                        "sourcelength": 4,
                        "refreshrate": 0.1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.04,0.86],1],
                        "right": [[0.1,0.86],1],
                        "down": [[0.04,0.92],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WeaponGroup|SlantRangeText [Indent level: 5],
                    "slantrangetext": {
                        "type": "text",
                        "source": "static",
                        "text": "M",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.155,0.86],1],
                        "right": [[0.215,0.86],1],
                        "down": [[0.155,0.92],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WeaponGroup|ValidTarget [Indent level: 5],
                    "validtarget": {
                        "condition": "targetDist>=1",
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WeaponGroup|ValidTarget|ImpactHeight [Indent level: 6],
                        "impactheight": {
                            "type": "text",
                            "source": "targetHeight",
                            "sourcescale": 1,
                            "sourcelength": 1,
                            "refreshrate": 0.1,
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.04,0.81],1],
                            "right": [[0.1,0.81],1],
                            "down": [[0.04,0.87],1]
                        }
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode [Indent level: 4],
                "navigationmode": {
                    "condition": "1 - (mgun + AAmissile + ATmissile + bomb + rocket + user4)",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|VerticalSpeedScale [Indent level: 5],
                    "verticalspeedscale": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.755,0.422],1],[[0.775,0.422],1],[],[[0.755,0.461],1],[[0.775,0.461],1],[],[[0.755,0.5],1],[[0.775,0.5],1],[],[[0.755,0.695],1],[[0.775,0.695],1],[],[[0.755,0.656],1],[[0.775,0.656],1],[],[[0.755,0.617],1],[[0.775,0.617],1],[],[[0.755,0.578],1],[[0.775,0.578],1],[],[[0.755,0.539],1],[[0.775,0.539],1],[],[[0.755,0.5],1],[[0.755,0.695],1],[],["TerrainBone2",1,"TerrainBone",[0.755,0.695],1],["TerrainBone2",1,"TerrainBone",[0.735,0.695],1],[],["TerrainBone2",1,"TerrainBone",[0.735,0.7106],1],["TerrainBone2",1,"TerrainBone",[0.735,0.6794],1],[]]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText0 [Indent level: 5],
                    "alttext0": {
                        "type": "text",
                        "source": "static",
                        "text": "0",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.91-0.12",0.668],1],
                        "right": [[0.84,0.668],1],
                        "down": [["0.91-0.12",0.718],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText1 [Indent level: 5],
                    "alttext1": {
                        "type": "text",
                        "source": "static",
                        "text": "1",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.91-0.12",0.629],1],
                        "right": [[0.84,0.629],1],
                        "down": [["0.91-0.12",0.679],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText2 [Indent level: 5],
                    "alttext2": {
                        "type": "text",
                        "source": "static",
                        "text": "2",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.91-0.12",0.59],1],
                        "right": [[0.84,0.59],1],
                        "down": [["0.91-0.12",0.64],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText3 [Indent level: 5],
                    "alttext3": {
                        "type": "text",
                        "source": "static",
                        "text": "3",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.91-0.12",0.551],1],
                        "right": [[0.84,0.551],1],
                        "down": [["0.91-0.12",0.601],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText4 [Indent level: 5],
                    "alttext4": {
                        "type": "text",
                        "source": "static",
                        "text": "4",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.91-0.12",0.512],1],
                        "right": [[0.84,0.512],1],
                        "down": [["0.91-0.12",0.562],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText5 [Indent level: 5],
                    "alttext5": {
                        "type": "text",
                        "source": "static",
                        "text": "5",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.91-0.12",0.473],1],
                        "right": [[0.84,0.473],1],
                        "down": [["0.91-0.12",0.523],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText10 [Indent level: 5],
                    "alttext10": {
                        "type": "text",
                        "source": "static",
                        "text": "10",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.91-0.12",0.434],1],
                        "right": [[0.84,0.434],1],
                        "down": [["0.91-0.12",0.484],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|NavigationMode|AltText15 [Indent level: 5],
                    "alttext15": {
                        "type": "text",
                        "source": "static",
                        "text": "15",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.91-0.12",0.395],1],
                        "right": [[0.84,0.395],1],
                        "down": [["0.91-0.12",0.445],1]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup [Indent level: 4],
                "machineguncrosshairgroup": {
                    "type": "group",
                    "condition": "mgun",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|WeaponName [Indent level: 5],
                    "weaponname": {
                        "type": "text",
                        "source": "weapon",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.04,0.76],1],
                        "right": [[0.1,0.76],1],
                        "down": [[0.04,0.82],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|AmmoCount [Indent level: 5],
                    "ammocount": {
                        "type": "text",
                        "source": "ammo",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.13,0.76],1],
                        "right": [[0.19,0.76],1],
                        "down": [[0.13,0.82],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|AmmoStatic [Indent level: 5],
                    "ammostatic": {
                        "type": "text",
                        "source": "static",
                        "text": "/",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.1,0.76],1],
                        "right": [[0.16,0.76],1],
                        "down": [[0.1,0.82],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|MachineGunCrosshair [Indent level: 5],
                    "machineguncrosshair": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.109829],1],["ImpactPoint",[0,-0.0976253],1],[],["ImpactPoint",[0,0.109829],1],["ImpactPoint",[0,0.0976253],1],[],["ImpactPoint",[-0.09,0],1],["ImpactPoint",[-0.08,0],1],[],["ImpactPoint",[0.09,0],1],["ImpactPoint",[0.08,0],1],[],["ImpactPoint",[0,-0.00244063],1],["ImpactPoint",[0,0.00244063],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[]]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "width": 9,
                        "points": [["ImpactPoint",[0,-0.0781003],1],["ImpactPoint",[0,-0.0976253],1],["MissileFlightTimeRot1",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot18",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot19",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.064],1,"ImpactPoint",1]]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|Circle_Min_Range [Indent level: 5],
                    "circle_min_range": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0976253],1],["ImpactPoint",[0.013888,-0.0961414],1],["ImpactPoint",[0.02736,-0.0917385],1],["ImpactPoint",[0.04,-0.0845435],1],["ImpactPoint",[0.051424,-0.074781],1],["ImpactPoint",[0.06128,-0.0627536],1],["ImpactPoint",[0.06928,-0.0488127],1],["ImpactPoint",[0.075176,-0.0333879],1],["ImpactPoint",[0.078784,-0.0169478],1],["ImpactPoint",[0.08,0],1],["ImpactPoint",[0.078784,0.0169478],1],["ImpactPoint",[0.075176,0.0333879],1],["ImpactPoint",[0.06928,0.0488127],1],["ImpactPoint",[0.06128,0.0627536],1],["ImpactPoint",[0.051424,0.074781],1],["ImpactPoint",[0.04,0.0845435],1],["ImpactPoint",[0.02736,0.0917385],1],["ImpactPoint",[0.013888,0.0961414],1],["ImpactPoint",[0,0.0976253],1],["ImpactPoint",[-0.013888,0.0961414],1],["ImpactPoint",[-0.02736,0.0917385],1],["ImpactPoint",[-0.04,0.0845435],1],["ImpactPoint",[-0.051424,0.074781],1],["ImpactPoint",[-0.06128,0.0627536],1],["ImpactPoint",[-0.06928,0.0488127],1],["ImpactPoint",[-0.075176,0.0333879],1],["ImpactPoint",[-0.078784,0.0169478],1],["ImpactPoint",[-0.08,0],1],["ImpactPoint",[-0.078784,-0.0169478],1],["ImpactPoint",[-0.075176,-0.0333879],1],["ImpactPoint",[-0.06928,-0.0488127],1],["ImpactPoint",[-0.06128,-0.0627536],1],["ImpactPoint",[-0.051424,-0.074781],1],["ImpactPoint",[-0.04,-0.0845435],1],["ImpactPoint",[-0.02736,-0.0917385],1],["ImpactPoint",[-0.013888,-0.0961414],1],["ImpactPoint",[0,-0.0976253],1]]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|MachineGunCrosshairGroup|Distance [Indent level: 5],
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
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup [Indent level: 4],
                "aamissilecrosshairgroup": {
                    "type": "group",
                    "condition": "AAmissile",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|AAMissileCrosshair [Indent level: 5],
                    "aamissilecrosshair": {
                        "type": "line",
                        "width": 4,
                        "points": [["WeaponAimAA",[0,-0.0488127],1],["WeaponAimAA",[0.006944,-0.0480707],1],["WeaponAimAA",[0.01368,-0.0458693],1],["WeaponAimAA",[0.02,-0.0422718],1],["WeaponAimAA",[0.025712,-0.0373905],1],["WeaponAimAA",[0.03064,-0.0313768],1],["WeaponAimAA",[0.03464,-0.0244063],1],["WeaponAimAA",[0.037588,-0.0166939],1],["WeaponAimAA",[0.039392,-0.00847388],1],["WeaponAimAA",[0.04,0],1],["WeaponAimAA",[0.039392,0.00847388],1],["WeaponAimAA",[0.037588,0.0166939],1],["WeaponAimAA",[0.03464,0.0244063],1],["WeaponAimAA",[0.03064,0.0313768],1],["WeaponAimAA",[0.025712,0.0373905],1],["WeaponAimAA",[0.02,0.0422718],1],["WeaponAimAA",[0.01368,0.0458693],1],["WeaponAimAA",[0.006944,0.0480707],1],["WeaponAimAA",[0,0.0488127],1],["WeaponAimAA",[-0.006944,0.0480707],1],["WeaponAimAA",[-0.01368,0.0458693],1],["WeaponAimAA",[-0.02,0.0422718],1],["WeaponAimAA",[-0.025712,0.0373905],1],["WeaponAimAA",[-0.03064,0.0313768],1],["WeaponAimAA",[-0.03464,0.0244063],1],["WeaponAimAA",[-0.037588,0.0166939],1],["WeaponAimAA",[-0.039392,0.00847388],1],["WeaponAimAA",[-0.04,0],1],["WeaponAimAA",[-0.039392,-0.00847388],1],["WeaponAimAA",[-0.037588,-0.0166939],1],["WeaponAimAA",[-0.03464,-0.0244063],1],["WeaponAimAA",[-0.03064,-0.0313768],1],["WeaponAimAA",[-0.025712,-0.0373905],1],["WeaponAimAA",[-0.02,-0.0422718],1],["WeaponAimAA",[-0.01368,-0.0458693],1],["WeaponAimAA",[-0.006944,-0.0480707],1],["WeaponAimAA",[0,-0.0488127],1]]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|AAMissileCrosshairGroup|AmmoCount [Indent level: 5],
                    "ammocount": {
                        "type": "text",
                        "source": "ammoFormat",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.04,0.76],1],
                        "right": [[0.1,0.76],1],
                        "down": [[0.04,0.82],1]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup [Indent level: 4],
                "atmissilecrosshairgroup": {
                    "condition": "ATmissile",
                    "type": "group",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroup [Indent level: 5],
                    "targetingpodgroup": {
                        "condition": "1-pilotcameralock-missilelocked",
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroup|TargetingPodDir [Indent level: 6],
                        "targetingpoddir": {
                            "type": "line",
                            "width": 3,
                            "points": [["TargetingPodDir",[0.01197,-0.0401356],1],["TargetingPodDir",[0.0175,-0.0369878],1],["TargetingPodDir",[0.022498,-0.0327167],1],["TargetingPodDir",[0.02681,-0.0274547],1],["TargetingPodDir",[0.03031,-0.0213555],1],["TargetingPodDir",[0.0328895,-0.0146072],1],[],["TargetingPodDir",[0.0328895,0.0146072],1],["TargetingPodDir",[0.03031,0.0213555],1],["TargetingPodDir",[0.02681,0.0274547],1],["TargetingPodDir",[0.022498,0.0327167],1],["TargetingPodDir",[0.0175,0.0369878],1],["TargetingPodDir",[0.01197,0.0401356],1],[],["TargetingPodDir",[-0.01197,0.0401356],1],["TargetingPodDir",[-0.0175,0.0369878],1],["TargetingPodDir",[-0.022498,0.0327167],1],["TargetingPodDir",[-0.02681,0.0274547],1],["TargetingPodDir",[-0.03031,0.0213555],1],["TargetingPodDir",[-0.0328895,0.0146072],1],[],["TargetingPodDir",[-0.0328895,-0.0146072],1],["TargetingPodDir",[-0.03031,-0.0213555],1],["TargetingPodDir",[-0.02681,-0.0274547],1],["TargetingPodDir",[-0.022498,-0.0327167],1],["TargetingPodDir",[-0.0175,-0.0369878],1],["TargetingPodDir",[-0.01197,-0.0401356],1],[],["TargetingPodDir",[0,-0.00244063],1],["TargetingPodDir",[0,0.00244063],1],[],["TargetingPodDir",[-0.002,0],1],["TargetingPodDir",[0.002,0],1],[]]
                        },
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroup|Distance [Indent level: 6],
                        "distance": {
                            "type": "text",
                            "source": "targetDist",
                            "sourcescale": 0.001,
                            "sourceprecision": 1,
                            "max": 15,
                            "align": "center",
                            "scale": 1,
                            "pos": ["TargetingPodDir",[-0.002,0.045],1],
                            "right": ["TargetingPodDir",[0.045,0.045],1],
                            "down": ["TargetingPodDir",[-0.002,0.085],1]
                        }
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroupOn [Indent level: 5],
                    "targetingpodgroupon": {
                        "condition": "pilotcameralock-missilelocked",
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroupOn|TargetingPodDir [Indent level: 6],
                        "targetingpoddir": {
                            "type": "line",
                            "width": 3,
                            "points": [["TargetingPodTarget",1,"Limit0109",[0,-0.0427111],1],["TargetingPodTarget",1,"Limit0109",[0.006076,-0.0420619],1],["TargetingPodTarget",1,"Limit0109",[0.01197,-0.0401356],1],["TargetingPodTarget",1,"Limit0109",[0.0175,-0.0369878],1],["TargetingPodTarget",1,"Limit0109",[0.022498,-0.0327167],1],["TargetingPodTarget",1,"Limit0109",[0.02681,-0.0274547],1],["TargetingPodTarget",1,"Limit0109",[0.03031,-0.0213555],1],["TargetingPodTarget",1,"Limit0109",[0.0328895,-0.0146072],1],["TargetingPodTarget",1,"Limit0109",[0.034468,-0.00741464],1],["TargetingPodTarget",1,"Limit0109",[0.035,0],1],["TargetingPodTarget",1,"Limit0109",[0.034468,0.00741464],1],["TargetingPodTarget",1,"Limit0109",[0.0328895,0.0146072],1],["TargetingPodTarget",1,"Limit0109",[0.03031,0.0213555],1],["TargetingPodTarget",1,"Limit0109",[0.02681,0.0274547],1],["TargetingPodTarget",1,"Limit0109",[0.022498,0.0327167],1],["TargetingPodTarget",1,"Limit0109",[0.0175,0.0369878],1],["TargetingPodTarget",1,"Limit0109",[0.01197,0.0401356],1],["TargetingPodTarget",1,"Limit0109",[0.006076,0.0420619],1],["TargetingPodTarget",1,"Limit0109",[0,0.0427111],1],["TargetingPodTarget",1,"Limit0109",[-0.006076,0.0420619],1],["TargetingPodTarget",1,"Limit0109",[-0.01197,0.0401356],1],["TargetingPodTarget",1,"Limit0109",[-0.0175,0.0369878],1],["TargetingPodTarget",1,"Limit0109",[-0.022498,0.0327167],1],["TargetingPodTarget",1,"Limit0109",[-0.02681,0.0274547],1],["TargetingPodTarget",1,"Limit0109",[-0.03031,0.0213555],1],["TargetingPodTarget",1,"Limit0109",[-0.0328895,0.0146072],1],["TargetingPodTarget",1,"Limit0109",[-0.034468,0.00741464],1],["TargetingPodTarget",1,"Limit0109",[-0.035,0],1],["TargetingPodTarget",1,"Limit0109",[-0.034468,-0.00741464],1],["TargetingPodTarget",1,"Limit0109",[-0.0328895,-0.0146072],1],["TargetingPodTarget",1,"Limit0109",[-0.03031,-0.0213555],1],["TargetingPodTarget",1,"Limit0109",[-0.02681,-0.0274547],1],["TargetingPodTarget",1,"Limit0109",[-0.022498,-0.0327167],1],["TargetingPodTarget",1,"Limit0109",[-0.0175,-0.0369878],1],["TargetingPodTarget",1,"Limit0109",[-0.01197,-0.0401356],1],["TargetingPodTarget",1,"Limit0109",[-0.006076,-0.0420619],1],["TargetingPodTarget",1,"Limit0109",[0,-0.0427111],1],[],["TargetingPodTarget",[0,-0.0427111],1],["TargetingPodTarget",[0,-0.0244063],1],[],["TargetingPodTarget",[0,0.0427111],1],["TargetingPodTarget",[0,0.0244063],1],[],["TargetingPodTarget",[-0.035,0],1],["TargetingPodTarget",[-0.02,0],1],[],["TargetingPodTarget",[0.035,0],1],["TargetingPodTarget",[0.02,0],1],[],["TargetingPodTarget",[0,-0.00244063],1],["TargetingPodTarget",[0,0.00244063],1],[],["TargetingPodTarget",[-0.002,0],1],["TargetingPodTarget",[0.002,0],1],[]]
                        },
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetingPodGroupOn|Distance [Indent level: 6],
                        "distance": {
                            "type": "text",
                            "source": "targetDist",
                            "sourcescale": 0.001,
                            "sourceprecision": 1,
                            "max": 15,
                            "align": "center",
                            "scale": 1,
                            "pos": ["TargetingPodTarget",[-0.002,0.045],1],
                            "right": ["TargetingPodTarget",[0.045,0.045],1],
                            "down": ["TargetingPodTarget",[-0.002,0.085],1]
                        }
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetLocked [Indent level: 5],
                    "targetlocked": {
                        "condition": "missilelocked",
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetLocked|TargetingPodDir [Indent level: 6],
                        "targetingpoddir": {
                            "type": "line",
                            "width": 3,
                            "points": [["Target",1,"Limit0109",[0,-0.0427111],1],["Target",1,"Limit0109",[0.006076,-0.0420619],1],["Target",1,"Limit0109",[0.01197,-0.0401356],1],["Target",1,"Limit0109",[0.0175,-0.0369878],1],["Target",1,"Limit0109",[0.022498,-0.0327167],1],["Target",1,"Limit0109",[0.02681,-0.0274547],1],["Target",1,"Limit0109",[0.03031,-0.0213555],1],["Target",1,"Limit0109",[0.0328895,-0.0146072],1],["Target",1,"Limit0109",[0.034468,-0.00741464],1],["Target",1,"Limit0109",[0.035,0],1],["Target",1,"Limit0109",[0.034468,0.00741464],1],["Target",1,"Limit0109",[0.0328895,0.0146072],1],["Target",1,"Limit0109",[0.03031,0.0213555],1],["Target",1,"Limit0109",[0.02681,0.0274547],1],["Target",1,"Limit0109",[0.022498,0.0327167],1],["Target",1,"Limit0109",[0.0175,0.0369878],1],["Target",1,"Limit0109",[0.01197,0.0401356],1],["Target",1,"Limit0109",[0.006076,0.0420619],1],["Target",1,"Limit0109",[0,0.0427111],1],["Target",1,"Limit0109",[-0.006076,0.0420619],1],["Target",1,"Limit0109",[-0.01197,0.0401356],1],["Target",1,"Limit0109",[-0.0175,0.0369878],1],["Target",1,"Limit0109",[-0.022498,0.0327167],1],["Target",1,"Limit0109",[-0.02681,0.0274547],1],["Target",1,"Limit0109",[-0.03031,0.0213555],1],["Target",1,"Limit0109",[-0.0328895,0.0146072],1],["Target",1,"Limit0109",[-0.034468,0.00741464],1],["Target",1,"Limit0109",[-0.035,0],1],["Target",1,"Limit0109",[-0.034468,-0.00741464],1],["Target",1,"Limit0109",[-0.0328895,-0.0146072],1],["Target",1,"Limit0109",[-0.03031,-0.0213555],1],["Target",1,"Limit0109",[-0.02681,-0.0274547],1],["Target",1,"Limit0109",[-0.022498,-0.0327167],1],["Target",1,"Limit0109",[-0.0175,-0.0369878],1],["Target",1,"Limit0109",[-0.01197,-0.0401356],1],["Target",1,"Limit0109",[-0.006076,-0.0420619],1],["Target",1,"Limit0109",[0,-0.0427111],1],[],["Target",[0,-0.0427111],1],["Target",[0,-0.0244063],1],[],["Target",[0,0.0427111],1],["Target",[0,0.0244063],1],[],["Target",[-0.035,0],1],["Target",[-0.02,0],1],[],["Target",[0.035,0],1],["Target",[0.02,0],1],[],["Target",[0,-0.00244063],1],["Target",[0,0.00244063],1],[],["Target",[-0.002,0],1],["Target",[0.002,0],1],[]]
                        },
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|TargetLocked|Distance [Indent level: 6],
                        "distance": {
                            "type": "text",
                            "source": "targetDist",
                            "sourcescale": 0.001,
                            "sourceprecision": 1,
                            "max": 15,
                            "align": "center",
                            "scale": 1,
                            "pos": ["Target",[-0.002,0.045],1],
                            "right": ["Target",[0.045,0.045],1],
                            "down": ["Target",[-0.002,0.085],1]
                        }
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ATMissileCrosshairGroup|AmmoCount [Indent level: 5],
                    "ammocount": {
                        "type": "text",
                        "source": "ammoFormat",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.04,0.76],1],
                        "right": [[0.1,0.76],1],
                        "down": [[0.04,0.82],1]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RocketCrosshairGroup [Indent level: 4],
                "rocketcrosshairgroup": {
                    "type": "group",
                    "condition": "Rocket",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RocketCrosshairGroup|MachineGunCrosshair [Indent level: 5],
                    "machineguncrosshair": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0488127],1],["ImpactPoint",[0,-0.0244063],1],[],["ImpactPoint",[0,0.0488127],1],["ImpactPoint",[0,0.0244063],1],[],["ImpactPoint",[-0.04,0],1],["ImpactPoint",[-0.02,0],1],[],["ImpactPoint",[0.04,0],1],["ImpactPoint",[0.02,0],1],[],["ImpactPoint",[0.01,-0.0488127],1],["ImpactPoint",[-0.01,-0.0488127],1],[],["ImpactPoint",[0,-0.00244063],1],["ImpactPoint",[0,0.00244063],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[]]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RocketCrosshairGroup|Distance [Indent level: 5],
                    "distance": {
                        "type": "text",
                        "source": "ImpactDistance",
                        "sourcescale": 0.001,
                        "sourceprecision": 1,
                        "max": 15,
                        "align": "center",
                        "scale": 1,
                        "pos": ["ImpactPoint",[-0.002,0.07],1],
                        "right": ["ImpactPoint",[0.045,0.07],1],
                        "down": ["ImpactPoint",[-0.002,0.11],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RocketCrosshairGroup|AmmoCount [Indent level: 5],
                    "ammocount": {
                        "type": "text",
                        "source": "ammoFormat",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.04,0.76],1],
                        "right": [[0.1,0.76],1],
                        "down": [[0.04,0.82],1]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BombCrosshairGroup [Indent level: 4],
                "bombcrosshairgroup": {
                    "type": "group",
                    "condition": "bomb",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BombCrosshairGroup|BombCrosshair [Indent level: 5],
                    "bombcrosshair": {
                        "width": 4,
                        "type": "line",
                        "points": [["ImpactPoint",[0,0.109829],1],["ImpactPoint",[0,0.0976253],1],[],["ImpactPoint",[-0.09,0],1],["ImpactPoint",[-0.08,0],1],[],["ImpactPoint",[0.09,0],1],["ImpactPoint",[0.08,0],1],[],["ImpactPoint",[0,-0.00244063],1],["ImpactPoint",[0,0.00244063],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[],["ImpactPoint",[0,-0.0976253],1],["ImpactPoint",[0.013888,-0.0961414],1],["ImpactPoint",[0.02736,-0.0917385],1],["ImpactPoint",[0.04,-0.0845435],1],["ImpactPoint",[0.051424,-0.074781],1],["ImpactPoint",[0.06128,-0.0627536],1],["ImpactPoint",[0.06928,-0.0488127],1],["ImpactPoint",[0.075176,-0.0333879],1],["ImpactPoint",[0.078784,-0.0169478],1],["ImpactPoint",[0.08,0],1],["ImpactPoint",[0.078784,0.0169478],1],["ImpactPoint",[0.075176,0.0333879],1],["ImpactPoint",[0.06928,0.0488127],1],["ImpactPoint",[0.06128,0.0627536],1],["ImpactPoint",[0.051424,0.074781],1],["ImpactPoint",[0.04,0.0845435],1],["ImpactPoint",[0.02736,0.0917385],1],["ImpactPoint",[0.013888,0.0961414],1],["ImpactPoint",[0,0.0976253],1],["ImpactPoint",[-0.013888,0.0961414],1],["ImpactPoint",[-0.02736,0.0917385],1],["ImpactPoint",[-0.04,0.0845435],1],["ImpactPoint",[-0.051424,0.074781],1],["ImpactPoint",[-0.06128,0.0627536],1],["ImpactPoint",[-0.06928,0.0488127],1],["ImpactPoint",[-0.075176,0.0333879],1],["ImpactPoint",[-0.078784,0.0169478],1],["ImpactPoint",[-0.08,0],1],["ImpactPoint",[-0.078784,-0.0169478],1],["ImpactPoint",[-0.075176,-0.0333879],1],["ImpactPoint",[-0.06928,-0.0488127],1],["ImpactPoint",[-0.06128,-0.0627536],1],["ImpactPoint",[-0.051424,-0.074781],1],["ImpactPoint",[-0.04,-0.0845435],1],["ImpactPoint",[-0.02736,-0.0917385],1],["ImpactPoint",[-0.013888,-0.0961414],1],["ImpactPoint",[0,-0.0976253],1],[],[],["ImpactPoint",-1,"Velocity",1,"NormalizeBombCircle",1,"ImpactPoint",1,[0,0],1],["Velocity",1,"Limit0109",1,[0,0],1]]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BombCrosshairGroup|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "width": 6,
                        "points": [["ImpactPoint",[0,-0.0781003],1],["ImpactPoint",[0,-0.0976253],1],["MissileFlightTimeRot1",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot18",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot19",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.08],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.064],1,"ImpactPoint",1]]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BombCrosshairGroup|Distance [Indent level: 5],
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
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BombCrosshairGroup|AmmoCount [Indent level: 5],
                    "ammocount": {
                        "type": "text",
                        "source": "ammoFormat",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.04,0.76],1],
                        "right": [[0.1,0.76],1],
                        "down": [[0.04,0.82],1]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|PitchNumber [Indent level: 4],
                "pitchnumber": {
                    "type": "text",
                    "source": "horizonDive",
                    "sourcescale": 57.2958,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.84,0.56],1],
                    "right": [[0.91,0.56],1],
                    "down": [[0.84,0.63],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|BaroNumber [Indent level: 4],
                "baronumber": {
                    "type": "text",
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "sourcelength": 1,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.84,0.5],1],
                    "right": [[0.91,0.5],1],
                    "down": [[0.84,0.57],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|SpeedNumber [Indent level: 4],
                "speednumber": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 3.6,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.1,0.5],1],
                    "right": [[0.17,0.5],1],
                    "down": [[0.1,0.57],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LandingMode [Indent level: 4],
                "landingmode": {
                    "condition": "user4 - (mgun + AAmissile + ATmissile + bomb + rocket)",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LandingMode|VerticalSpeedScale [Indent level: 5],
                    "verticalspeedscale": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.73,0.305],1],[[0.76,0.305],1],[],[[0.735,0.344],1],[[0.745,0.344],1],[],[[0.735,0.383],1],[[0.745,0.383],1],[],[[0.735,0.422],1],[[0.745,0.422],1],[],[[0.735,0.461],1],[[0.745,0.461],1],[],[[0.73,0.5],1],[[0.79,0.5],1],[],[[0.73,0.695],1],[[0.76,0.695],1],[],[[0.735,0.656],1],[[0.745,0.656],1],[],[[0.735,0.617],1],[[0.745,0.617],1],[],[[0.735,0.578],1],[[0.745,0.578],1],[],[[0.735,0.539],1],[[0.745,0.539],1],[],[[0.73,0.5],1],[[0.79,0.5],1],["VerticalSpeedBone",[0.79,0.5],1],["VerticalSpeedBone",[0.76,0.5],1],[]]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LandingMode|VerticalSpeedArrow [Indent level: 5],
                    "verticalspeedarrow": {
                        "type": "polygon",
                        "points": [[["VerticalSpeedBone",[0.77,0.492],1],["VerticalSpeedBone",[0.76,0.5],1],["VerticalSpeedBone",[0.77,0.508],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ILS [Indent level: 4],
                "ils": {
                    "condition": "ils",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ILS|Glideslope [Indent level: 5],
                    "glideslope": {
                        "cliptl": [0,0],
                        "clipbr": [1,1],
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 6],
                        "ils": {
                            "type": "line",
                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[-0.24,-0.0292876],1],["ILS_W",[-0.24,0.0292876],1],[],["ILS_W",[-0.12,-0.0219657],1],["ILS_W",[-0.12,0.0219657],1],[],["ILS_W",[0,-0.0292876],1],["ILS_W",[0,0.0292876],1],[],["ILS_W",[0.12,-0.0219657],1],["ILS_W",[0.12,0.0219657],1],[],["ILS_W",[0.24,-0.0292876],1],["ILS_W",[0.24,0.0292876],1],[],["ILS_H",[0,-0.292876],1],["ILS_H",[0,0.292876],1],[],["ILS_H",[-0.024,-0.292876],1],["ILS_H",[0.024,-0.292876],1],[],["ILS_H",[-0.018,-0.146438],1],["ILS_H",[0.018,-0.146438],1],[],["ILS_H",[-0.024,0],1],["ILS_H",[0.024,0],1],[],["ILS_H",[-0.018,0.146438],1],["ILS_H",[0.018,0.146438],1],[],["ILS_H",[-0.024,0.292876],1],["ILS_H",[0.024,0.292876],1]]
                        }
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HeadingArrows [Indent level: 4],
                "headingarrows": {
                    "type": "line",
                    "width": 3,
                    "points": [[[0.486,0.957],1],[[0.5,0.935],1],[[0.514,0.957],1],[[0.486,0.957],1],[],["WPPoint",1,"LimitWaypoint",1,[-0.011,0],1],["WPPoint",1,"LimitWaypoint",1,[-0.011,0.022],1],[],["WPPoint",1,"LimitWaypoint",1,[0.011,0],1],["WPPoint",1,"LimitWaypoint",1,[0.011,0.022],1]]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],
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
                    "linexleft": 0.92,
                    "lineyright": 0.9,
                    "linexleftmajor": 0.93,
                    "lineyrightmajor": 0.9,
                    "majorlineeach": 2,
                    "numbereach": 2,
                    "step": 0.5,
                    "stepsize": 0.0555556,
                    "align": "center",
                    "scale": 1,
                    "pos": [0.295,0.865],
                    "right": [0.335,0.865],
                    "down": [0.295,0.905]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarNumber [Indent level: 4],
                "radarnumber": {
                    "type": "text",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "sourceoffset": -0.5,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.725,0.775],1],
                    "right": [[0.785,0.775],1],
                    "down": [[0.725,0.835],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarText [Indent level: 4],
                "radartext": {
                    "type": "text",
                    "source": "static",
                    "text": "R",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.825,0.775],1],
                    "right": [[0.885,0.775],1],
                    "down": [[0.825,0.835],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WPdist [Indent level: 4],
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
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WPIndex [Indent level: 4],
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
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WPstatic [Indent level: 4],
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
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WPTime [Indent level: 4],
                "wptime": {
                    "type": "text",
                    "source": "static",
                    "text": ":11:34/-00:0",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.725,0.865],1],
                    "right": [[0.785,0.865],1],
                    "down": [[0.725,0.925],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WPCurrentTime [Indent level: 4],
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
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WaypointGroup [Indent level: 4],
                "waypointgroup": {
                    "condition": "wpvalid",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|WaypointGroup|Tadpol [Indent level: 5],
                    "tadpol": {
                        "type": "line",
                        "width": 3,
                        "points": []
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine [Indent level: 4],
                "horizontalline": {
                    "cliptl": [0.2,0],
                    "clipbr": [0.8,0.96],
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|Level0 [Indent level: 5],
                    "level0": {
                        "type": "line",
                        "source": "Level0",
                        "width": 3,
                        "points": [["Level0",[-0.27,0],1],["Level0",[-0.0675,0],1],[],["Level0",[0.0675,0],1],["Level0",[0.27,0],1]]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM05 [Indent level: 5],
                    "levelm05": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM05",[-0.166,-0.04],1],["LevelM05",[-0.166,0],1],["LevelM05",[-0.138,0],1],[],["LevelM05",[-0.124,0],1],["LevelM05",[-0.096,0],1],[],["LevelM05",[-0.082,0],1],["LevelM05",[-0.054,0],1],[],[],["LevelM05",[0.166,-0.04],1],["LevelM05",[0.166,0],1],["LevelM05",[0.138,0],1],[],["LevelM05",[0.124,0],1],["LevelM05",[0.096,0],1],[],["LevelM05",[0.082,0],1],["LevelM05",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_05 [Indent level: 5],
                    "valm_1_05": {
                        "type": "text",
                        "source": "static",
                        "text": 5,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM05",[-0.18,-0.052],1],
                        "right": ["LevelM05",[-0.1,-0.052],1],
                        "down": ["LevelM05",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_05_R [Indent level: 5],
                    "valm_1_05_r": {
                        "type": "text",
                        "source": "static",
                        "text": 5,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM05",[0.18,-0.052],1],
                        "right": ["LevelM05",[0.26,-0.052],1],
                        "down": ["LevelM05",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP05 [Indent level: 5],
                    "levelp05": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP05",[-0.166,0.04],1],["LevelP05",[-0.166,0],1],["LevelP05",[-0.04,0],1],[],["LevelP05",[0.054,0],1],["LevelP05",[0.194,0],1],["LevelP05",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_05 [Indent level: 5],
                    "valp_1_05": {
                        "type": "text",
                        "source": "static",
                        "text": "05",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP05",[-0.19,-0.017],1],
                        "right": ["LevelP05",[-0.11,-0.017],1],
                        "down": ["LevelP05",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_05_R [Indent level: 5],
                    "valp_1_05_r": {
                        "type": "text",
                        "source": "static",
                        "text": "05",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP05",[0.21,-0.017],1],
                        "right": ["LevelP05",[0.29,-0.017],1],
                        "down": ["LevelP05",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM10 [Indent level: 5],
                    "levelm10": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM10",[-0.166,-0.04],1],["LevelM10",[-0.166,0],1],["LevelM10",[-0.138,0],1],[],["LevelM10",[-0.124,0],1],["LevelM10",[-0.096,0],1],[],["LevelM10",[-0.082,0],1],["LevelM10",[-0.054,0],1],[],[],["LevelM10",[0.166,-0.04],1],["LevelM10",[0.166,0],1],["LevelM10",[0.138,0],1],[],["LevelM10",[0.124,0],1],["LevelM10",[0.096,0],1],[],["LevelM10",[0.082,0],1],["LevelM10",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_10 [Indent level: 5],
                    "valm_1_10": {
                        "type": "text",
                        "source": "static",
                        "text": 10,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM10",[-0.18,-0.052],1],
                        "right": ["LevelM10",[-0.1,-0.052],1],
                        "down": ["LevelM10",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_10_R [Indent level: 5],
                    "valm_1_10_r": {
                        "type": "text",
                        "source": "static",
                        "text": 10,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM10",[0.18,-0.052],1],
                        "right": ["LevelM10",[0.26,-0.052],1],
                        "down": ["LevelM10",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP10 [Indent level: 5],
                    "levelp10": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP10",[-0.166,0.04],1],["LevelP10",[-0.166,0],1],["LevelP10",[-0.04,0],1],[],["LevelP10",[0.054,0],1],["LevelP10",[0.194,0],1],["LevelP10",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_10 [Indent level: 5],
                    "valp_1_10": {
                        "type": "text",
                        "source": "static",
                        "text": "10",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP10",[-0.19,-0.017],1],
                        "right": ["LevelP10",[-0.11,-0.017],1],
                        "down": ["LevelP10",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_10_R [Indent level: 5],
                    "valp_1_10_r": {
                        "type": "text",
                        "source": "static",
                        "text": "10",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP10",[0.21,-0.017],1],
                        "right": ["LevelP10",[0.29,-0.017],1],
                        "down": ["LevelP10",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM15 [Indent level: 5],
                    "levelm15": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM15",[-0.166,-0.04],1],["LevelM15",[-0.166,0],1],["LevelM15",[-0.138,0],1],[],["LevelM15",[-0.124,0],1],["LevelM15",[-0.096,0],1],[],["LevelM15",[-0.082,0],1],["LevelM15",[-0.054,0],1],[],[],["LevelM15",[0.166,-0.04],1],["LevelM15",[0.166,0],1],["LevelM15",[0.138,0],1],[],["LevelM15",[0.124,0],1],["LevelM15",[0.096,0],1],[],["LevelM15",[0.082,0],1],["LevelM15",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_15 [Indent level: 5],
                    "valm_1_15": {
                        "type": "text",
                        "source": "static",
                        "text": 15,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM15",[-0.18,-0.052],1],
                        "right": ["LevelM15",[-0.1,-0.052],1],
                        "down": ["LevelM15",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_15_R [Indent level: 5],
                    "valm_1_15_r": {
                        "type": "text",
                        "source": "static",
                        "text": 15,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM15",[0.18,-0.052],1],
                        "right": ["LevelM15",[0.26,-0.052],1],
                        "down": ["LevelM15",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP15 [Indent level: 5],
                    "levelp15": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP15",[-0.166,0.04],1],["LevelP15",[-0.166,0],1],["LevelP15",[-0.04,0],1],[],["LevelP15",[0.054,0],1],["LevelP15",[0.194,0],1],["LevelP15",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_15 [Indent level: 5],
                    "valp_1_15": {
                        "type": "text",
                        "source": "static",
                        "text": "15",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP15",[-0.19,-0.017],1],
                        "right": ["LevelP15",[-0.11,-0.017],1],
                        "down": ["LevelP15",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_15_R [Indent level: 5],
                    "valp_1_15_r": {
                        "type": "text",
                        "source": "static",
                        "text": "15",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP15",[0.21,-0.017],1],
                        "right": ["LevelP15",[0.29,-0.017],1],
                        "down": ["LevelP15",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM20 [Indent level: 5],
                    "levelm20": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM20",[-0.166,-0.04],1],["LevelM20",[-0.166,0],1],["LevelM20",[-0.138,0],1],[],["LevelM20",[-0.124,0],1],["LevelM20",[-0.096,0],1],[],["LevelM20",[-0.082,0],1],["LevelM20",[-0.054,0],1],[],[],["LevelM20",[0.166,-0.04],1],["LevelM20",[0.166,0],1],["LevelM20",[0.138,0],1],[],["LevelM20",[0.124,0],1],["LevelM20",[0.096,0],1],[],["LevelM20",[0.082,0],1],["LevelM20",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_20 [Indent level: 5],
                    "valm_1_20": {
                        "type": "text",
                        "source": "static",
                        "text": 20,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM20",[-0.18,-0.052],1],
                        "right": ["LevelM20",[-0.1,-0.052],1],
                        "down": ["LevelM20",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_20_R [Indent level: 5],
                    "valm_1_20_r": {
                        "type": "text",
                        "source": "static",
                        "text": 20,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM20",[0.18,-0.052],1],
                        "right": ["LevelM20",[0.26,-0.052],1],
                        "down": ["LevelM20",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP20 [Indent level: 5],
                    "levelp20": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP20",[-0.166,0.04],1],["LevelP20",[-0.166,0],1],["LevelP20",[-0.04,0],1],[],["LevelP20",[0.054,0],1],["LevelP20",[0.194,0],1],["LevelP20",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_20 [Indent level: 5],
                    "valp_1_20": {
                        "type": "text",
                        "source": "static",
                        "text": "20",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP20",[-0.19,-0.017],1],
                        "right": ["LevelP20",[-0.11,-0.017],1],
                        "down": ["LevelP20",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_20_R [Indent level: 5],
                    "valp_1_20_r": {
                        "type": "text",
                        "source": "static",
                        "text": "20",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP20",[0.21,-0.017],1],
                        "right": ["LevelP20",[0.29,-0.017],1],
                        "down": ["LevelP20",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM25 [Indent level: 5],
                    "levelm25": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM25",[-0.166,-0.04],1],["LevelM25",[-0.166,0],1],["LevelM25",[-0.138,0],1],[],["LevelM25",[-0.124,0],1],["LevelM25",[-0.096,0],1],[],["LevelM25",[-0.082,0],1],["LevelM25",[-0.054,0],1],[],[],["LevelM25",[0.166,-0.04],1],["LevelM25",[0.166,0],1],["LevelM25",[0.138,0],1],[],["LevelM25",[0.124,0],1],["LevelM25",[0.096,0],1],[],["LevelM25",[0.082,0],1],["LevelM25",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_25 [Indent level: 5],
                    "valm_1_25": {
                        "type": "text",
                        "source": "static",
                        "text": 25,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM25",[-0.18,-0.052],1],
                        "right": ["LevelM25",[-0.1,-0.052],1],
                        "down": ["LevelM25",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_25_R [Indent level: 5],
                    "valm_1_25_r": {
                        "type": "text",
                        "source": "static",
                        "text": 25,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM25",[0.18,-0.052],1],
                        "right": ["LevelM25",[0.26,-0.052],1],
                        "down": ["LevelM25",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP25 [Indent level: 5],
                    "levelp25": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP25",[-0.166,0.04],1],["LevelP25",[-0.166,0],1],["LevelP25",[-0.04,0],1],[],["LevelP25",[0.054,0],1],["LevelP25",[0.194,0],1],["LevelP25",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_25 [Indent level: 5],
                    "valp_1_25": {
                        "type": "text",
                        "source": "static",
                        "text": "25",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP25",[-0.19,-0.017],1],
                        "right": ["LevelP25",[-0.11,-0.017],1],
                        "down": ["LevelP25",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_25_R [Indent level: 5],
                    "valp_1_25_r": {
                        "type": "text",
                        "source": "static",
                        "text": "25",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP25",[0.21,-0.017],1],
                        "right": ["LevelP25",[0.29,-0.017],1],
                        "down": ["LevelP25",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM30 [Indent level: 5],
                    "levelm30": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM30",[-0.166,-0.04],1],["LevelM30",[-0.166,0],1],["LevelM30",[-0.138,0],1],[],["LevelM30",[-0.124,0],1],["LevelM30",[-0.096,0],1],[],["LevelM30",[-0.082,0],1],["LevelM30",[-0.054,0],1],[],[],["LevelM30",[0.166,-0.04],1],["LevelM30",[0.166,0],1],["LevelM30",[0.138,0],1],[],["LevelM30",[0.124,0],1],["LevelM30",[0.096,0],1],[],["LevelM30",[0.082,0],1],["LevelM30",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_30 [Indent level: 5],
                    "valm_1_30": {
                        "type": "text",
                        "source": "static",
                        "text": 30,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM30",[-0.18,-0.052],1],
                        "right": ["LevelM30",[-0.1,-0.052],1],
                        "down": ["LevelM30",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_30_R [Indent level: 5],
                    "valm_1_30_r": {
                        "type": "text",
                        "source": "static",
                        "text": 30,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM30",[0.18,-0.052],1],
                        "right": ["LevelM30",[0.26,-0.052],1],
                        "down": ["LevelM30",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP30 [Indent level: 5],
                    "levelp30": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP30",[-0.166,0.04],1],["LevelP30",[-0.166,0],1],["LevelP30",[-0.04,0],1],[],["LevelP30",[0.054,0],1],["LevelP30",[0.194,0],1],["LevelP30",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_30 [Indent level: 5],
                    "valp_1_30": {
                        "type": "text",
                        "source": "static",
                        "text": "30",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP30",[-0.19,-0.017],1],
                        "right": ["LevelP30",[-0.11,-0.017],1],
                        "down": ["LevelP30",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_30_R [Indent level: 5],
                    "valp_1_30_r": {
                        "type": "text",
                        "source": "static",
                        "text": "30",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP30",[0.21,-0.017],1],
                        "right": ["LevelP30",[0.29,-0.017],1],
                        "down": ["LevelP30",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM35 [Indent level: 5],
                    "levelm35": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM35",[-0.166,-0.04],1],["LevelM35",[-0.166,0],1],["LevelM35",[-0.138,0],1],[],["LevelM35",[-0.124,0],1],["LevelM35",[-0.096,0],1],[],["LevelM35",[-0.082,0],1],["LevelM35",[-0.054,0],1],[],[],["LevelM35",[0.166,-0.04],1],["LevelM35",[0.166,0],1],["LevelM35",[0.138,0],1],[],["LevelM35",[0.124,0],1],["LevelM35",[0.096,0],1],[],["LevelM35",[0.082,0],1],["LevelM35",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_35 [Indent level: 5],
                    "valm_1_35": {
                        "type": "text",
                        "source": "static",
                        "text": 35,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM35",[-0.18,-0.052],1],
                        "right": ["LevelM35",[-0.1,-0.052],1],
                        "down": ["LevelM35",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_35_R [Indent level: 5],
                    "valm_1_35_r": {
                        "type": "text",
                        "source": "static",
                        "text": 35,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM35",[0.18,-0.052],1],
                        "right": ["LevelM35",[0.26,-0.052],1],
                        "down": ["LevelM35",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP35 [Indent level: 5],
                    "levelp35": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP35",[-0.166,0.04],1],["LevelP35",[-0.166,0],1],["LevelP35",[-0.04,0],1],[],["LevelP35",[0.054,0],1],["LevelP35",[0.194,0],1],["LevelP35",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_35 [Indent level: 5],
                    "valp_1_35": {
                        "type": "text",
                        "source": "static",
                        "text": "35",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP35",[-0.19,-0.017],1],
                        "right": ["LevelP35",[-0.11,-0.017],1],
                        "down": ["LevelP35",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_35_R [Indent level: 5],
                    "valp_1_35_r": {
                        "type": "text",
                        "source": "static",
                        "text": "35",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP35",[0.21,-0.017],1],
                        "right": ["LevelP35",[0.29,-0.017],1],
                        "down": ["LevelP35",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM40 [Indent level: 5],
                    "levelm40": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM40",[-0.166,-0.04],1],["LevelM40",[-0.166,0],1],["LevelM40",[-0.138,0],1],[],["LevelM40",[-0.124,0],1],["LevelM40",[-0.096,0],1],[],["LevelM40",[-0.082,0],1],["LevelM40",[-0.054,0],1],[],[],["LevelM40",[0.166,-0.04],1],["LevelM40",[0.166,0],1],["LevelM40",[0.138,0],1],[],["LevelM40",[0.124,0],1],["LevelM40",[0.096,0],1],[],["LevelM40",[0.082,0],1],["LevelM40",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_40 [Indent level: 5],
                    "valm_1_40": {
                        "type": "text",
                        "source": "static",
                        "text": 40,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM40",[-0.18,-0.052],1],
                        "right": ["LevelM40",[-0.1,-0.052],1],
                        "down": ["LevelM40",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_40_R [Indent level: 5],
                    "valm_1_40_r": {
                        "type": "text",
                        "source": "static",
                        "text": 40,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM40",[0.18,-0.052],1],
                        "right": ["LevelM40",[0.26,-0.052],1],
                        "down": ["LevelM40",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP40 [Indent level: 5],
                    "levelp40": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP40",[-0.166,0.04],1],["LevelP40",[-0.166,0],1],["LevelP40",[-0.04,0],1],[],["LevelP40",[0.054,0],1],["LevelP40",[0.194,0],1],["LevelP40",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_40 [Indent level: 5],
                    "valp_1_40": {
                        "type": "text",
                        "source": "static",
                        "text": "40",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP40",[-0.19,-0.017],1],
                        "right": ["LevelP40",[-0.11,-0.017],1],
                        "down": ["LevelP40",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_40_R [Indent level: 5],
                    "valp_1_40_r": {
                        "type": "text",
                        "source": "static",
                        "text": "40",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP40",[0.21,-0.017],1],
                        "right": ["LevelP40",[0.29,-0.017],1],
                        "down": ["LevelP40",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM45 [Indent level: 5],
                    "levelm45": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM45",[-0.166,-0.04],1],["LevelM45",[-0.166,0],1],["LevelM45",[-0.138,0],1],[],["LevelM45",[-0.124,0],1],["LevelM45",[-0.096,0],1],[],["LevelM45",[-0.082,0],1],["LevelM45",[-0.054,0],1],[],[],["LevelM45",[0.166,-0.04],1],["LevelM45",[0.166,0],1],["LevelM45",[0.138,0],1],[],["LevelM45",[0.124,0],1],["LevelM45",[0.096,0],1],[],["LevelM45",[0.082,0],1],["LevelM45",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_45 [Indent level: 5],
                    "valm_1_45": {
                        "type": "text",
                        "source": "static",
                        "text": 45,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM45",[-0.18,-0.052],1],
                        "right": ["LevelM45",[-0.1,-0.052],1],
                        "down": ["LevelM45",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_45_R [Indent level: 5],
                    "valm_1_45_r": {
                        "type": "text",
                        "source": "static",
                        "text": 45,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM45",[0.18,-0.052],1],
                        "right": ["LevelM45",[0.26,-0.052],1],
                        "down": ["LevelM45",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP45 [Indent level: 5],
                    "levelp45": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP45",[-0.166,0.04],1],["LevelP45",[-0.166,0],1],["LevelP45",[-0.04,0],1],[],["LevelP45",[0.054,0],1],["LevelP45",[0.194,0],1],["LevelP45",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_45 [Indent level: 5],
                    "valp_1_45": {
                        "type": "text",
                        "source": "static",
                        "text": "45",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP45",[-0.19,-0.017],1],
                        "right": ["LevelP45",[-0.11,-0.017],1],
                        "down": ["LevelP45",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_45_R [Indent level: 5],
                    "valp_1_45_r": {
                        "type": "text",
                        "source": "static",
                        "text": "45",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP45",[0.21,-0.017],1],
                        "right": ["LevelP45",[0.29,-0.017],1],
                        "down": ["LevelP45",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM50 [Indent level: 5],
                    "levelm50": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM50",[-0.166,-0.04],1],["LevelM50",[-0.166,0],1],["LevelM50",[-0.138,0],1],[],["LevelM50",[-0.124,0],1],["LevelM50",[-0.096,0],1],[],["LevelM50",[-0.082,0],1],["LevelM50",[-0.054,0],1],[],[],["LevelM50",[0.166,-0.04],1],["LevelM50",[0.166,0],1],["LevelM50",[0.138,0],1],[],["LevelM50",[0.124,0],1],["LevelM50",[0.096,0],1],[],["LevelM50",[0.082,0],1],["LevelM50",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_50 [Indent level: 5],
                    "valm_1_50": {
                        "type": "text",
                        "source": "static",
                        "text": 50,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM50",[-0.18,-0.052],1],
                        "right": ["LevelM50",[-0.1,-0.052],1],
                        "down": ["LevelM50",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_50_R [Indent level: 5],
                    "valm_1_50_r": {
                        "type": "text",
                        "source": "static",
                        "text": 50,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM50",[0.18,-0.052],1],
                        "right": ["LevelM50",[0.26,-0.052],1],
                        "down": ["LevelM50",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP50 [Indent level: 5],
                    "levelp50": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP50",[-0.166,0.04],1],["LevelP50",[-0.166,0],1],["LevelP50",[-0.04,0],1],[],["LevelP50",[0.054,0],1],["LevelP50",[0.194,0],1],["LevelP50",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_50 [Indent level: 5],
                    "valp_1_50": {
                        "type": "text",
                        "source": "static",
                        "text": "50",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP50",[-0.19,-0.017],1],
                        "right": ["LevelP50",[-0.11,-0.017],1],
                        "down": ["LevelP50",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_50_R [Indent level: 5],
                    "valp_1_50_r": {
                        "type": "text",
                        "source": "static",
                        "text": "50",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP50",[0.21,-0.017],1],
                        "right": ["LevelP50",[0.29,-0.017],1],
                        "down": ["LevelP50",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM60 [Indent level: 5],
                    "levelm60": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM60",[-0.166,-0.04],1],["LevelM60",[-0.166,0],1],["LevelM60",[-0.138,0],1],[],["LevelM60",[-0.124,0],1],["LevelM60",[-0.096,0],1],[],["LevelM60",[-0.082,0],1],["LevelM60",[-0.054,0],1],[],[],["LevelM60",[0.166,-0.04],1],["LevelM60",[0.166,0],1],["LevelM60",[0.138,0],1],[],["LevelM60",[0.124,0],1],["LevelM60",[0.096,0],1],[],["LevelM60",[0.082,0],1],["LevelM60",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_60 [Indent level: 5],
                    "valm_1_60": {
                        "type": "text",
                        "source": "static",
                        "text": 60,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM60",[-0.18,-0.052],1],
                        "right": ["LevelM60",[-0.1,-0.052],1],
                        "down": ["LevelM60",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_60_R [Indent level: 5],
                    "valm_1_60_r": {
                        "type": "text",
                        "source": "static",
                        "text": 60,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM60",[0.18,-0.052],1],
                        "right": ["LevelM60",[0.26,-0.052],1],
                        "down": ["LevelM60",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP60 [Indent level: 5],
                    "levelp60": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP60",[-0.166,0.04],1],["LevelP60",[-0.166,0],1],["LevelP60",[-0.04,0],1],[],["LevelP60",[0.054,0],1],["LevelP60",[0.194,0],1],["LevelP60",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_60 [Indent level: 5],
                    "valp_1_60": {
                        "type": "text",
                        "source": "static",
                        "text": "60",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP60",[-0.19,-0.017],1],
                        "right": ["LevelP60",[-0.11,-0.017],1],
                        "down": ["LevelP60",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_60_R [Indent level: 5],
                    "valp_1_60_r": {
                        "type": "text",
                        "source": "static",
                        "text": "60",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP60",[0.21,-0.017],1],
                        "right": ["LevelP60",[0.29,-0.017],1],
                        "down": ["LevelP60",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM70 [Indent level: 5],
                    "levelm70": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM70",[-0.166,-0.04],1],["LevelM70",[-0.166,0],1],["LevelM70",[-0.138,0],1],[],["LevelM70",[-0.124,0],1],["LevelM70",[-0.096,0],1],[],["LevelM70",[-0.082,0],1],["LevelM70",[-0.054,0],1],[],[],["LevelM70",[0.166,-0.04],1],["LevelM70",[0.166,0],1],["LevelM70",[0.138,0],1],[],["LevelM70",[0.124,0],1],["LevelM70",[0.096,0],1],[],["LevelM70",[0.082,0],1],["LevelM70",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_70 [Indent level: 5],
                    "valm_1_70": {
                        "type": "text",
                        "source": "static",
                        "text": 70,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM70",[-0.18,-0.052],1],
                        "right": ["LevelM70",[-0.1,-0.052],1],
                        "down": ["LevelM70",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_70_R [Indent level: 5],
                    "valm_1_70_r": {
                        "type": "text",
                        "source": "static",
                        "text": 70,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM70",[0.18,-0.052],1],
                        "right": ["LevelM70",[0.26,-0.052],1],
                        "down": ["LevelM70",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP70 [Indent level: 5],
                    "levelp70": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP70",[-0.166,0.04],1],["LevelP70",[-0.166,0],1],["LevelP70",[-0.04,0],1],[],["LevelP70",[0.054,0],1],["LevelP70",[0.194,0],1],["LevelP70",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_70 [Indent level: 5],
                    "valp_1_70": {
                        "type": "text",
                        "source": "static",
                        "text": "70",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP70",[-0.19,-0.017],1],
                        "right": ["LevelP70",[-0.11,-0.017],1],
                        "down": ["LevelP70",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_70_R [Indent level: 5],
                    "valp_1_70_r": {
                        "type": "text",
                        "source": "static",
                        "text": "70",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP70",[0.21,-0.017],1],
                        "right": ["LevelP70",[0.29,-0.017],1],
                        "down": ["LevelP70",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM80 [Indent level: 5],
                    "levelm80": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM80",[-0.166,-0.04],1],["LevelM80",[-0.166,0],1],["LevelM80",[-0.138,0],1],[],["LevelM80",[-0.124,0],1],["LevelM80",[-0.096,0],1],[],["LevelM80",[-0.082,0],1],["LevelM80",[-0.054,0],1],[],[],["LevelM80",[0.166,-0.04],1],["LevelM80",[0.166,0],1],["LevelM80",[0.138,0],1],[],["LevelM80",[0.124,0],1],["LevelM80",[0.096,0],1],[],["LevelM80",[0.082,0],1],["LevelM80",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_80 [Indent level: 5],
                    "valm_1_80": {
                        "type": "text",
                        "source": "static",
                        "text": 80,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM80",[-0.18,-0.052],1],
                        "right": ["LevelM80",[-0.1,-0.052],1],
                        "down": ["LevelM80",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_80_R [Indent level: 5],
                    "valm_1_80_r": {
                        "type": "text",
                        "source": "static",
                        "text": 80,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM80",[0.18,-0.052],1],
                        "right": ["LevelM80",[0.26,-0.052],1],
                        "down": ["LevelM80",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP80 [Indent level: 5],
                    "levelp80": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP80",[-0.166,0.04],1],["LevelP80",[-0.166,0],1],["LevelP80",[-0.04,0],1],[],["LevelP80",[0.054,0],1],["LevelP80",[0.194,0],1],["LevelP80",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_80 [Indent level: 5],
                    "valp_1_80": {
                        "type": "text",
                        "source": "static",
                        "text": "80",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP80",[-0.19,-0.017],1],
                        "right": ["LevelP80",[-0.11,-0.017],1],
                        "down": ["LevelP80",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_80_R [Indent level: 5],
                    "valp_1_80_r": {
                        "type": "text",
                        "source": "static",
                        "text": "80",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP80",[0.21,-0.017],1],
                        "right": ["LevelP80",[0.29,-0.017],1],
                        "down": ["LevelP80",[0.21,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelM90 [Indent level: 5],
                    "levelm90": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelM90",[-0.166,-0.04],1],["LevelM90",[-0.166,0],1],["LevelM90",[-0.138,0],1],[],["LevelM90",[-0.124,0],1],["LevelM90",[-0.096,0],1],[],["LevelM90",[-0.082,0],1],["LevelM90",[-0.054,0],1],[],[],["LevelM90",[0.166,-0.04],1],["LevelM90",[0.166,0],1],["LevelM90",[0.138,0],1],[],["LevelM90",[0.124,0],1],["LevelM90",[0.096,0],1],[],["LevelM90",[0.082,0],1],["LevelM90",[0.054,0],1],[]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_90 [Indent level: 5],
                    "valm_1_90": {
                        "type": "text",
                        "source": "static",
                        "text": 90,
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM90",[-0.18,-0.052],1],
                        "right": ["LevelM90",[-0.1,-0.052],1],
                        "down": ["LevelM90",[-0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALM_1_90_R [Indent level: 5],
                    "valm_1_90_r": {
                        "type": "text",
                        "source": "static",
                        "text": 90,
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "sourcelength": 2,
                        "pos": ["LevelM90",[0.18,-0.052],1],
                        "right": ["LevelM90",[0.26,-0.052],1],
                        "down": ["LevelM90",[0.18,0.008],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|LevelP90 [Indent level: 5],
                    "levelp90": {
                        "type": "line",
                        "width": 3,
                        "points": [["LevelP90",[-0.166,0.04],1],["LevelP90",[-0.166,0],1],["LevelP90",[-0.04,0],1],[],["LevelP90",[0.054,0],1],["LevelP90",[0.194,0],1],["LevelP90",[0.194,0.04],1]],
                        "source": "Level0"
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_90 [Indent level: 5],
                    "valp_1_90": {
                        "type": "text",
                        "source": "static",
                        "text": "90",
                        "align": "left",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP90",[-0.19,-0.017],1],
                        "right": ["LevelP90",[-0.11,-0.017],1],
                        "down": ["LevelP90",[-0.19,0.043],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|HorizontalLine|VALP_1_90_R [Indent level: 5],
                    "valp_1_90_r": {
                        "type": "text",
                        "source": "static",
                        "text": "90",
                        "align": "right",
                        "scale": 1,
                        "sourcescale": 1,
                        "pos": ["LevelP90",[0.21,-0.017],1],
                        "right": ["LevelP90",[0.29,-0.017],1],
                        "down": ["LevelP90",[0.21,0.043],1]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare [Indent level: 4],
                "lockingsquare": {
                    "condition": "bomb + AAmissile",
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetDiamond [Indent level: 5],
                    "targetdiamond": {
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetDiamond|shape [Indent level: 6]
                        "shape": {
                            "type": "line",
                            "width": 4,
                            "points": [["Target",1,"Limit0109",1,[0.02,0.0244063],1],["Target",1,"Limit0109",1,[-0.02,0.0244063],1],["Target",1,"Limit0109",1,[-0.02,-0.0244063],1],["Target",1,"Limit0109",1,[0.02,-0.0244063],1],["Target",1,"Limit0109",1,[0.02,0.0244063],1]]
                        }
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetLocking [Indent level: 5],
                    "targetlocking": {
                        "condition": "missileLocking",
                        "blinkingpattern": [0.3,0.3],
                        "blinkingstartson": 1,
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetLocking|shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 4,
                            "points": [["Target",1,"Limit0109",1,[0,-0.0366095],1],["Target",1,"Limit0109",1,[0.03,0],1],["Target",1,"Limit0109",1,[0,0.0366095],1],["Target",1,"Limit0109",1,[-0.03,0],1],["Target",1,"Limit0109",1,[0,-0.0366095],1]]
                        }
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|LockingSquare|TargetLocked [Indent level: 5],
                    "targetlocked": {
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
                "radarboxes": {
                    "type": "radar",
                    "pos0": [0.498,0.485],
                    "pos10": [1.256,1.41],
                    "width": 4,
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|points [Indent level: 5],
                    "points": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknown [Indent level: 5],
                    "pointsunknown": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownEnemy [Indent level: 5],
                    "pointsunknownenemy": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownFriend [Indent level: 5],
                    "pointsunknownfriend": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsUnknownCiv [Indent level: 5],
                    "pointsunknownciv": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCar [Indent level: 5],
                    "pointscar": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarEnemy [Indent level: 5],
                    "pointscarenemy": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarFriend [Indent level: 5],
                    "pointscarfriend": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarCiv [Indent level: 5],
                    "pointscarciv": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsCarNeutral [Indent level: 5],
                    "pointscarneutral": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTank [Indent level: 5],
                    "pointstank": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankEnemy [Indent level: 5],
                    "pointstankenemy": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankFriend [Indent level: 5],
                    "pointstankfriend": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankCiv [Indent level: 5],
                    "pointstankciv": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsTankNeutral [Indent level: 5],
                    "pointstankneutral": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplane [Indent level: 5],
                    "pointsairplane": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplaneEnemy [Indent level: 5],
                    "pointsairplaneenemy": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsAirplaneFriend [Indent level: 5],
                    "pointsairplanefriend": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeli [Indent level: 5],
                    "pointsheli": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeliEnemy [Indent level: 5],
                    "pointshelienemy": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsHeliFriend [Indent level: 5],
                    "pointshelifriend": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsLaser [Indent level: 5],
                    "pointslaser": {
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsLaser|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 3,
                            "points": [[[0,-0.0183048],1],[[0.015,8.00126e-010],1],[[-1.31134e-009,0.0183048],1],[[-0.015,-2.18282e-010],1],[[0,-0.0183048],1],[],[[0.00707107,-0.00862894],1],[[0.0148492,-0.0181208],1],[],[[0.00707107,0.00862894],1],[[0.0148492,0.0181208],1],[],[[-0.00707107,0.00862894],1],[[-0.0148492,0.0181208],1],[],[[-0.00707107,-0.00862894],1],[[-0.0148492,-0.0181208],1],[]]
                        }
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsNVG [Indent level: 5],
                    "pointsnvg": {
                        # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsLaser|Draw [Indent level: 6]
                        "draw": {
                            "type": "line",
                            "width": 3,
                            "points": [[[0,-0.0183048],1],[[0.015,8.00126e-010],1],[[-1.31134e-009,0.0183048],1],[[-0.015,-2.18282e-010],1],[[0,-0.0183048],1],[],[[0.00707107,-0.00862894],1],[[0.0148492,-0.0181208],1],[],[[0.00707107,0.00862894],1],[[0.0148492,0.0181208],1],[],[[-0.00707107,0.00862894],1],[[-0.0148492,0.0181208],1],[],[[-0.00707107,-0.00862894],1],[[-0.0148492,-0.0181208],1],[]]
                        }
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStatic [Indent level: 5],
                    "pointsstatic": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticEnemy [Indent level: 5],
                    "pointsstaticenemy": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticFriend [Indent level: 5],
                    "pointsstaticfriend": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticCiv [Indent level: 5],
                    "pointsstaticciv": {
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|AirplaneHUD|Draw|RadarBoxes|pointsStaticNeutral [Indent level: 5],
                    "pointsstaticneutral": {
                    }
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_1 [Indent level: 2],
        "mfd_1": {
            "topleft": "MFD_Ammo_TL",
            "topright": "MFD_Ammo_TR",
            "bottomleft": "MFD_Ammo_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0.2,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "rhsusf_digital_font_var",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_1|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_1|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.5,
                "color": [0,1,0.5],
                # Class: CfgVehicles|RHS_A10|MFD|MFD_1|Draw|ammoCounter [Indent level: 4],
                "ammocounter": {
                    "type": "text",
                    "source": "ammo",
                    "sourceindex": 1,
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.78,0.42],1],
                    "right": [[1.09,0.42],1],
                    "down": [[0.78,0.97],1]
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_2 [Indent level: 2],
        "mfd_2": {
            "topleft": "MFD_WP_TL",
            "topright": "MFD_WP_TR",
            "bottomleft": "MFD_WP_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0.2,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.5,
                "color": [1,1,1],
                # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|heading [Indent level: 4],
                "heading": {
                    "type": "text",
                    "source": "head",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.98,0.22],1],
                    "right": [[0.98,0.22],1],
                    "down": [[0.98,0.22],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|HeadingText [Indent level: 4],
                "headingtext": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "refreshrate": 0.1,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.922,0.185],1],
                    "right": [[0.977,0.185],1],
                    "down": [[0.922,0.245],1]
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|AltitudeBox [Indent level: 4],
                "altitudebox": {
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|AltitudeBox|Number [Indent level: 5]
                    "number": {
                        "type": "text",
                        "source": "wpdist",
                        "sourcescale": 5.39957e-005,
                        "sourcelength": 3,
                        "sourceoffset": 0,
                        "align": "left",
                        "scale": 3,
                        "pos": [[0.142,0.195],1],
                        "right": [[0.187,0.195],1],
                        "down": [[0.142,0.245],1]
                    },
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|AltitudeBox|ClipScale [Indent level: 5],
                    "clipscale": {
                        "cliptlparallax": [0.15,0.14],
                        "clipbrparallax": [0.17,0.28],
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_2|Draw|AltitudeBox|ClipScale|Scale [Indent level: 6],
                        "scale": {
                            "type": "scale",
                            "horizontal": 0,
                            "source": "wpdist",
                            "sourcescale": 0.000539957,
                            "sourcelength": 5,
                            "width": 4,
                            "top": 0.4,
                            "center": 0.2,
                            "bottom": 0,
                            "linexleft": -1,
                            "lineyright": -1,
                            "linexleftmajor": -1,
                            "lineyrightmajor": -1,
                            "majorlineeach": 1,
                            "numbereach": 1,
                            "step": 10,
                            "stepsize": 0.055,
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
        "mfd_3": {
            "topleft": "MFD_Fuel_TL",
            "topright": "MFD_Fuel_TR",
            "bottomleft": "MFD_Fuel_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0.2,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_3|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_3|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.5,
                "color": [1,1,1],
                # Class: CfgVehicles|RHS_A10|MFD|MFD_3|Draw|FuelNumber [Indent level: 4],
                "fuelnumber": {
                    "type": "text",
                    "source": "fuel",
                    "sourcescale": 12000,
                    "sourcelength": 5,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.8,0.1],1],
                    "right": [[1.05,0.1],1],
                    "down": [[0.8,1.05],1]
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_4 [Indent level: 2],
        "mfd_4": {
            "topleft": "MFD_WB_TL",
            "topright": "MFD_WB_TR",
            "bottomleft": "MFD_WB_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.5,
                "color": [1,1,1],
                "condition": "1",
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon1 [Indent level: 4],
                "pylon1": {
                    "type": "pylonicon",
                    "pos": [[0.03,0.83],1],
                    "pylon": 1,
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon2 [Indent level: 4],
                "pylon2": {
                    "pylon": 2,
                    "pos": [[0.159,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon3 [Indent level: 4],
                "pylon3": {
                    "pylon": 3,
                    "pos": [[0.288,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon4 [Indent level: 4],
                "pylon4": {
                    "pylon": 4,
                    "pos": [[0.422,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon5 [Indent level: 4],
                "pylon5": {
                    "pylon": 5,
                    "pos": [[0.347,0.06],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon6 [Indent level: 4],
                "pylon6": {
                    "pylon": 6,
                    "pos": [[0.486,0.06],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon7 [Indent level: 4],
                "pylon7": {
                    "pylon": 7,
                    "pos": [[0.625,0.06],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon8 [Indent level: 4],
                "pylon8": {
                    "pylon": 8,
                    "pos": [[0.546,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon9 [Indent level: 4],
                "pylon9": {
                    "pylon": 9,
                    "pos": [[0.678,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon10 [Indent level: 4],
                "pylon10": {
                    "pylon": 10,
                    "pos": [[0.809,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|Pylon11 [Indent level: 4],
                "pylon11": {
                    "pylon": 11,
                    "pos": [[0.942,0.83],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_box"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty1 [Indent level: 4],
                "pylonempty1": {
                    "condition": "pylonEmpty1",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty1|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.05,0.885],1],[[0.08,0.885],1],[[0.08,0.965],1],[[0.05,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty2 [Indent level: 4],
                "pylonempty2": {
                    "condition": "pylonEmpty2",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty2|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.179,0.885],1],[[0.209,0.885],1],[[0.209,0.965],1],[[0.179,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty3 [Indent level: 4],
                "pylonempty3": {
                    "condition": "pylonEmpty3",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty3|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.308,0.885],1],[[0.338,0.885],1],[[0.338,0.965],1],[[0.308,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty4 [Indent level: 4],
                "pylonempty4": {
                    "condition": "pylonEmpty4",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty4|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.442,0.885],1],[[0.472,0.885],1],[[0.472,0.965],1],[[0.442,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty5 [Indent level: 4],
                "pylonempty5": {
                    "condition": "pylonEmpty5",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty5|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.367,0.115],1],[[0.397,0.115],1],[[0.397,0.195],1],[[0.367,0.195],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty6 [Indent level: 4],
                "pylonempty6": {
                    "condition": "pylonEmpty6",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty6|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.506,0.115],1],[[0.536,0.115],1],[[0.536,0.195],1],[[0.506,0.195],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty7 [Indent level: 4],
                "pylonempty7": {
                    "condition": "pylonEmpty7",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty7|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.645,0.115],1],[[0.675,0.115],1],[[0.675,0.195],1],[[0.645,0.195],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty8 [Indent level: 4],
                "pylonempty8": {
                    "condition": "pylonEmpty8",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty8|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.566,0.885],1],[[0.596,0.885],1],[[0.596,0.965],1],[[0.566,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty9 [Indent level: 4],
                "pylonempty9": {
                    "condition": "pylonEmpty9",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty9|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.698,0.885],1],[[0.728,0.885],1],[[0.728,0.965],1],[[0.698,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty10 [Indent level: 4],
                "pylonempty10": {
                    "condition": "pylonEmpty10",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty10|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.829,0.885],1],[[0.859,0.885],1],[[0.859,0.965],1],[[0.829,0.965],1]]]
                    }
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty11 [Indent level: 4],
                "pylonempty11": {
                    "condition": "pylonEmpty11",
                    "color": [0.87,0,0],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_4|Draw|PylonEmpty11|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.962,0.885],1],[[0.992,0.885],1],[[0.992,0.965],1],[[0.962,0.965],1]]]
                    }
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_5 [Indent level: 2],
        "mfd_5": {
            "topleft": "MFD_WN_TL",
            "topright": "MFD_WN_TR",
            "bottomleft": "MFD_WN_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.5,
                "color": [1,1,1],
                "condition": "1",
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon1 [Indent level: 4],
                "pylon1": {
                    "type": "pylonicon",
                    "pos": [[0.07,0.88],1],
                    "pylon": 1,
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon2 [Indent level: 4],
                "pylon2": {
                    "pylon": 2,
                    "pos": [[0.189,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon3 [Indent level: 4],
                "pylon3": {
                    "pylon": 3,
                    "pos": [[0.308,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon4 [Indent level: 4],
                "pylon4": {
                    "pylon": 4,
                    "pos": [[0.432,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon5 [Indent level: 4],
                "pylon5": {
                    "pylon": 5,
                    "pos": [[0.377,0.05],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon6 [Indent level: 4],
                "pylon6": {
                    "pylon": 6,
                    "pos": [[0.486,0.05],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon7 [Indent level: 4],
                "pylon7": {
                    "pylon": 7,
                    "pos": [[0.625,0.05],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon8 [Indent level: 4],
                "pylon8": {
                    "pylon": 8,
                    "pos": [[0.556,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon9 [Indent level: 4],
                "pylon9": {
                    "pylon": 9,
                    "pos": [[0.668,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon10 [Indent level: 4],
                "pylon10": {
                    "pylon": 10,
                    "pos": [[0.799,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                },
                # Class: CfgVehicles|RHS_A10|MFD|MFD_5|Draw|Pylon11 [Indent level: 4],
                "pylon11": {
                    "pylon": 11,
                    "pos": [[0.912,0.88],1],
                    "type": "pylonicon",
                    "name": "rhs_a10a_ammoname"
                }
            }
        },
        # Class: CfgVehicles|RHS_A10|MFD|MFD_6 [Indent level: 2],
        "mfd_6": {
            "topleft": "MFD_ALT_TL",
            "topright": "MFD_ALT_TR",
            "bottomleft": "MFD_ALT_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_6|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_6|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.7,
                "color": [0,0,0],
                "condition": "altitudeASL>=1000",
                # Class: CfgVehicles|RHS_A10|MFD|MFD_6|Draw|AltGrp [Indent level: 4],
                "altgrp": {
                    "color": [1,1,1],
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_6|Draw|AltGrp|AltText [Indent level: 5],
                    "alttext": {
                        "type": "text",
                        "source": "altitudeASL",
                        "sourcescale": 0.001,
                        "sourcelength": 1,
                        "sourceoffset": -0.5,
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
        "mfd_rwr": {
            "topleft": "MFD_RWR_TL",
            "topright": "MFD_RWR_TR",
            "bottomleft": "MFD_RWR_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.15,1,0.15,1],
            "enableparallax": 0,
            "font": "LucidaConsoleB",
            # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.3,
                "color": [0.7,0.7,0.7],
                # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR [Indent level: 4],
                "rwr": {
                    "type": "sensor",
                    "pos": [[0.07,0.07],1],
                    "down": [[0.93,0.93],1],
                    "showtargettypes": "2 + 8 + 64 + 128 + 256",
                    "width": 4,
                    "sensorlinetype": 3,
                    "sensorlinewidth": 0,
                    "range": 16000,
                    # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|MissileThreat [Indent level: 5],
                    "missilethreat": {
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|MissileThreat|TargetLines [Indent level: 6]
                        "targetlines": {
                            "type": "line",
                            "width": 4,
                            "points": [[[0,-0.0610158],1],[[0.00868,-0.0600884],1],[[0.0171,-0.0573366],1],[[0.025,-0.0528397],1],[[0.03214,-0.0467381],1],[[0.0383,-0.039221],1],[[0.0433,-0.0305079],1],[[0.046985,-0.0208674],1],[[0.04924,-0.0105923],1],[[0.05,0],1],[[0.04924,0.0105923],1],[[0.046985,0.0208674],1],[[0.0433,0.0305079],1],[[0.0383,0.039221],1],[[0.03214,0.0467381],1],[[0.025,0.0528397],1],[[0.0171,0.0573366],1],[[0.00868,0.0600884],1],[[0,0.0610158],1],[[-0.00868,0.0600884],1],[[-0.0171,0.0573366],1],[[-0.025,0.0528397],1],[[-0.03214,0.0467381],1],[[-0.0383,0.039221],1],[[-0.0433,0.0305079],1],[[-0.046985,0.0208674],1],[[-0.04924,0.0105923],1],[[-0.05,0],1],[[-0.04924,-0.0105923],1],[[-0.046985,-0.0208674],1],[[-0.0433,-0.0305079],1],[[-0.0383,-0.039221],1],[[-0.03214,-0.0467381],1],[[-0.025,-0.0528397],1],[[-0.0171,-0.0573366],1],[[-0.00868,-0.0600884],1],[[0,-0.0610158],1]]
                        },
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|MissileThreat|TextM [Indent level: 6],
                        "textm": {
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
                    "lockingthreat": {
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|lockingThreat|TargetLines [Indent level: 6]
                        "targetlines": {
                            "type": "line",
                            "points": [[[0,-0.0610158],1],[[0.00868,-0.0600884],1],[[0.0171,-0.0573366],1],[[0.025,-0.0528397],1],[[0.03214,-0.0467381],1],[[0.0383,-0.039221],1],[[0.0433,-0.0305079],1],[[0.046985,-0.0208674],1],[[0.04924,-0.0105923],1],[[0.05,0],1],[[0.04924,0.0105923],1],[[0.046985,0.0208674],1],[[0.0433,0.0305079],1],[[0.0383,0.039221],1],[[0.03214,0.0467381],1],[[0.025,0.0528397],1],[[0.0171,0.0573366],1],[[0.00868,0.0600884],1],[[0,0.0610158],1],[[-0.00868,0.0600884],1],[[-0.0171,0.0573366],1],[[-0.025,0.0528397],1],[[-0.03214,0.0467381],1],[[-0.0383,0.039221],1],[[-0.0433,0.0305079],1],[[-0.046985,0.0208674],1],[[-0.04924,0.0105923],1],[[-0.05,0],1],[[-0.04924,-0.0105923],1],[[-0.046985,-0.0208674],1],[[-0.0433,-0.0305079],1],[[-0.0383,-0.039221],1],[[-0.03214,-0.0467381],1],[[-0.025,-0.0528397],1],[[-0.0171,-0.0573366],1],[[-0.00868,-0.0600884],1],[[0,-0.0610158],1],[[0.06,0],1],[[0,0.0610158],1],[[-0.06,0],1],[[0,-0.0610158],1],[[0.06,0],1]]
                        },
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|lockingThreat|TextL [Indent level: 6],
                        "textl": {
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
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|rwr|TargetLines [Indent level: 6]
                        "targetlines": {
                            "type": "line",
                            "points": [[[0.06,0],1],[[0,0.0610158],1],[[-0.06,0],1],[[0,-0.0610158],1],[[0.06,0],1]]
                        },
                        # Class: CfgVehicles|RHS_A10|MFD|MFD_RWR|Draw|RWR|rwr|TextA [Indent level: 6],
                        "texta": {
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
    "maxomega": 2000,
    "accelaidforcecoef": 1,
    "accelaidforceyoffset": -1,
    "accelaidforcespd": 1,
    "turncoef": 0.05,
    # Class: CfgVehicles|RHS_A10|Wheels [Indent level: 1],
    "wheels": {
        "disablewheelswhendestroyed": 1,
        # Class: CfgVehicles|RHS_A10|Wheels|Wheel_1 [Indent level: 2],
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
            "maxdroop": 0.05,
            "sprungmass": 11400,
            "springstrength": 1.2e+006,
            "springdamperrate": 128000,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 3,
            "latstiffy": 21,
            "frictionvsslipgraph": [[0,1],[0.5,1.4],[1,0.6]]
        },
        # Class: CfgVehicles|RHS_A10|Wheels|Wheel_1_fake [Indent level: 2],
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
            "maxdroop": 0.05,
            "sprungmass": 11400,
            "springstrength": 1.2e+006,
            "springdamperrate": 128000,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 3,
            "latstiffy": 21,
            "frictionvsslipgraph": [[0,1],[0.5,1.4],[1,0.6]]
        },
        # Class: CfgVehicles|RHS_A10|Wheels|Wheel_2 [Indent level: 2],
        "wheel_2": {
            "steering": 0,
            "bonename": "Wheel_2",
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "suspforceapppointoffset": "Wheel_2_center",
            "tireforceapppointoffset": "Wheel_2_center",
            "width": 0.28,
            "maxcompression": 0.25,
            "maxdroop": 0.1,
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
            "latstiffx": 3,
            "latstiffy": 21,
            "frictionvsslipgraph": [[0,1],[0.5,1.4],[1,0.6]]
        },
        # Class: CfgVehicles|RHS_A10|Wheels|Wheel_3 [Indent level: 2],
        "wheel_3": {
            "steering": 0,
            "side": "right",
            "bonename": "Wheel_3",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspforceapppointoffset": "Wheel_3_center",
            "tireforceapppointoffset": "Wheel_3_center",
            "width": 0.28,
            "maxcompression": 0.25,
            "maxdroop": 0.1,
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
            "latstiffx": 3,
            "latstiffy": 21,
            "frictionvsslipgraph": [[0,1],[0.5,1.4],[1,0.6]]
        }
    },
    "soundgetin": ["A3|Sounds_F|vehicles|air|CAS_01|getin_wipeout",1,1,40],
    "soundgetout": ["A3|Sounds_F|air|Plane_Fighter_03|getout",1,1,40],
    "cabinopensound": ["A3|Sounds_F|air|noises|Plane_CAS01_CabinOpen",3.16228,1,40],
    "cabinclosesound": ["A3|Sounds_F|air|noises|Plane_CAS01_CabinClose",3.16228,1,40],
    "cabinopensoundinternal": ["A3|Sounds_F|air|noises|Plane_CAS01_CabinOpen",10,1,40],
    "cabinclosesoundinternal": ["A3|Sounds_F|air|noises|Plane_CAS01_CabinClose",10,1,40],
    "sounddammage": ["",1,1],
    "soundengineonint": ["A3|Sounds_F|vehicles|air|CAS_01|CAS_01_start_int",1,1],
    "soundengineonext": ["A3|Sounds_F|vehicles|air|CAS_01|CAS_01_start_ext",1.41254,1,500],
    "soundengineoffint": ["A3|Sounds_F|vehicles|air|CAS_01|CAS_01_stop_int",1,1],
    "soundengineoffext": ["A3|Sounds_F|vehicles|air|CAS_01|CAS_01_stop_ext",1.41254,1,500],
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_1",0.316228,1],
    "soundwatercollision1": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_1",1.41254,1,500],
    "soundwatercollision2": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_2",1.41254,1,500],
    "soundwatercrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "soundgearup": ["A3|Sounds_F|vehicles|air|CAS_01|gear_up",0.794328,1,150],
    "soundgeardown": ["A3|Sounds_F|vehicles|air|CAS_01|gear_down",0.794328,1,150],
    "soundflapsup": ["A3|Sounds_F|vehicles|air|CAS_01|Flaps_Up",0.630957,1,100],
    "soundflapsdown": ["A3|Sounds_F|vehicles|air|CAS_01|Flaps_Down",0.630957,1,100],
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
    # Class: CfgVehicles|Plane_CAS_01_base_F|scrubLandInt [Indent level: 1],
    "scrublandint": {
        "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
        "frequency": 1,
        "volume": "(scrubLand factor[0.01, 0.20])"
    },
    # Class: CfgVehicles|Plane_CAS_01_base_F|Sounds [Indent level: 1],
    "sounds": {
        "soundsets": ["Plane_CAS_01_EngineLowExt_SoundSet","Plane_CAS_01_EngineHighExt_SoundSet","Plane_CAS_01_ForsageExt_SoundSet","Plane_CAS_01_WindNoiseExt_SoundSet","Plane_CAS_01_EngineLowInt_SoundSet","Plane_CAS_01_EngineHighInt_SoundSet","Plane_CAS_01_ForsageInt_SoundSet","Plane_CAS_01_WindNoiseInt_SoundSet","Plane_CAS_01_EngineExt_Dist_Rear_SoundSet","Plane_CAS_01_EngineExt_Dist_Front_SoundSet","Plane_CAS_01_EngineExt_Middle_SoundSet","Plane_CAS_01_EngineExt_Middle_SoundSet","Plane_CAS_01_EngineExt_Dist_Front_SoundSet","Plane_CAS_01_EngineExt_Dist_Rear_SoundSet"]
    },
    "features": "Randomization: No						<br />Camo selections: 2 - the main body, wings and gear						<br />Script door sources: None						<br />Script animations: None						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: No						<br />Cargo proxy indexes: None",
    "_generalmacro": "Plane_CAS_01_base_F",
    "editorsubcategory": "EdSubcat_Planes",
    "destrtype": "DestructWreck",
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "getinaction": "pilot_plane_cas_01_Enter",
    "getoutaction": "pilot_plane_cas_01_Exit",
    "viewdrivershadowdiff": 0.5,
    "viewdrivershadowamb": 0.5,
    "clutchstrength": 100,
    "dampingratefullthrottle": 0.5,
    "stallspeed": 210,
    "stallwarningtreshold": 0.04,
    "airbrake": 1,
    "airbrakefrictioncoef": 2.6,
    "flaps": 1,
    "gearsupfrictioncoef": 0.55,
    "airfrictioncoefs0": [0,0,0],
    "airfrictioncoefs1": [0.1,0.6,0.0067],
    "airfrictioncoefs2": [0.001,0.006,7e-005],
    "altnoforce": 13000,
    "altfullforce": 2000,
    "rudderinfluence": 0.866,
    "elevatorcontrolssensitivitycoef": 4,
    "showalltargets": 4,
    "extcameraposition": [0,3.8,-20],
    # Class: CfgVehicles|Plane_CAS_01_base_F|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -2.5,
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
    "memorypointgun": "Gatling_barrels_end",
    "gunaimdown": 0,
    "driveoncomponent": [],
    # Class: CfgVehicles|Plane_CAS_01_base_F|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|Plane_CAS_01_base_F|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "Exhaust_1_pos",
            "direction": "Exhaust_1_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 0
        },
        # Class: CfgVehicles|Plane_CAS_01_base_F|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "Exhaust_2_pos",
            "direction": "Exhaust_2_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineindex": 1
        }
    },
    "explosionshielding": 1,
    "armorlights": 1,
    "waterleakiness": 1.15,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "waterlineardampingcoefy": 0,
    "waterlineardampingcoefx": 5,
    "waterresistancecoef": 0.04,
    "ejectspeed": [0,60,0],
    "transportmaxweapons": 6,
    "transportmaxmagazines": 24,
    "transportmaxbackpacks": 6,
    "maximumload": 500,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Plane_Base_F|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
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
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "vtol": 0,
    "tailhook": 0,
    "lightongear": 1,
    "cost": 2e+006,
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
    "type": 2,
    "fuelexplosionpower": 10,
    "crewcrashprotection": 0.15,
    "damageeffect": "AirDestructionEffects",
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
    "mintotaldamagethreshold": 0.005,
    # Class: CfgVehicles|Plane|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "formationtime": 10,
    "fuelcapacity": 1000,
    "insidesoundcoef": 0.0316228,
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
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
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
    "cargoproxyindexes": [],
    "driverdoor": "",
    "cargodoors": [],
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "cargoprecisegetinout": [0],
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
    "cargocaneject": 1,
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
    "insidedetectcoef": 0.05,
}