rhssaf_airforce_o_l_18 = {
    "crew": "rhssaf_airforce_o_pilot_mig29",
    "side": 0,
    "faction": "rhssaf_faction_airforce_opfor",
    "editorpreview": "rhssaf|addons|rhssaf_editorpreviews|data|rhssaf_airforce_l_18.paa",
    "dlc": "RHS_SAF",
    "author": "Red Hammer Studios",
    "scope": 2,
    "scopecurator": 2,
    "displayname": "L-18",
    "hiddenselectionstextures": ["rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_01_blue_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_02_blue_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_03_blue_co.paa"],
    "texturelist": ["RHS_SAF_Gray",0.6,"RHS_SAF_Blue",0.4],
    "rhs_decalparameters": ["['Number', cRHSAIRMIG29SerbianTailStaticNumberPlaces,'AviaSerbianTail',  18]","['Number', [cRHSAIRMIG29SerbianTailDynamicNumberPlaces,cRHSAIRMIG29SerbianIntakeNumberPlaces],['AviaSerbianTail','AviaSerbianIntake'],  [102,103,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,124]]"],
    # Class: CfgVehicles|rhssaf_airforce_l_18|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhssaf_airforce_l_18|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            # Class: CfgVehicles|rhssaf_airforce_l_18|Components|TransportPylonsComponent|pylons [Indent level: 3]
            "pylons": {
                # Class: CfgVehicles|rhssaf_airforce_l_18|Components|TransportPylonsComponent|pylons|pylon1 [Indent level: 4]
                "pylon1": {
                    "attachment": "rhs_mag_b8m1_bd3_umk2a_s8kom",
                    "hardpoints": ["RHS_HP_KH25_APU68_MIG29","RHS_HP_KH29_AKU58_MIG29","RHS_HP_FAB100_BD3_UMK2A","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB250_BD3_UMK2A","RHS_HP_FAB500_BD3_UMK2A","RHS_HP_KAB500_BD3_UMK2A","RHS_HP_KMGU2_BD3_UMK2A","RHS_HP_BD3_USK_A_O25L","RHS_HP_APU68_BD3_UMK2A","RHS_HP_B13L_BD3_UMK2A","RHS_HP_B8M1_BD3_UMK2A","RHS_HP_UB16_BD3_UMK2A","RHS_HP_UB32_BD3_UMK2A","RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R27_APU470","RHS_HP_R60_APU60","RHS_HP_R73_APU73","RHS_HP_PTB1150"],
                    "priority": 9,
                    "maxweight": 1200,
                    "uiposition": [0.32,0.2],
                    "hitpoint": "HitPylon1"
                },
                # Class: CfgVehicles|rhssaf_airforce_l_18|Components|TransportPylonsComponent|pylons|pylon2 [Indent level: 4],
                "pylon2": {
                    "attachment": "rhs_mag_b8m1_bd3_umk2a_s8kom",
                    "uiposition": [0.32,0.35],
                    "mirroredmissilepos": 1,
                    "hitpoint": "HitPylon2",
                    "hardpoints": ["RHS_HP_KH25_APU68_MIG29","RHS_HP_KH29_AKU58_MIG29","RHS_HP_FAB100_BD3_UMK2A","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB250_BD3_UMK2A","RHS_HP_FAB500_BD3_UMK2A","RHS_HP_KAB500_BD3_UMK2A","RHS_HP_KMGU2_BD3_UMK2A","RHS_HP_BD3_USK_A_O25L","RHS_HP_APU68_BD3_UMK2A","RHS_HP_B13L_BD3_UMK2A","RHS_HP_B8M1_BD3_UMK2A","RHS_HP_UB16_BD3_UMK2A","RHS_HP_UB32_BD3_UMK2A","RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R27_APU470","RHS_HP_R60_APU60","RHS_HP_R73_APU73","RHS_HP_PTB1150"],
                    "priority": 9,
                    "maxweight": 1200
                },
                # Class: CfgVehicles|rhssaf_airforce_l_18|Components|TransportPylonsComponent|pylons|pylon3 [Indent level: 4],
                "pylon3": {
                    "attachment": "rhs_mag_b8m1_bd3_umk2a_s8df",
                    "hardpoints": ["RHS_HP_KH25_APU68_MIG29","RHS_HP_FAB100_BD3_UMK2A","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB250_BD3_UMK2A","RHS_HP_FAB500_BD3_UMK2A","RHS_HP_KAB500_BD3_UMK2A","RHS_HP_KMGU2_BD3_UMK2A","RHS_HP_BD3_USK_A_O25L","RHS_HP_APU68_BD3_UMK2A","RHS_HP_B13L_BD3_UMK2A","RHS_HP_B8M1_BD3_UMK2A","RHS_HP_UB16_BD3_UMK2A","RHS_HP_UB32_BD3_UMK2A","RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R60_APU60","RHS_HP_R73_APU73"],
                    "priority": 7,
                    "uiposition": [0.33,0.15],
                    "hitpoint": "HitPylon3",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|rhssaf_airforce_l_18|Components|TransportPylonsComponent|pylons|pylon4 [Indent level: 4],
                "pylon4": {
                    "attachment": "rhs_mag_b8m1_bd3_umk2a_s8df",
                    "uiposition": [0.33,0.4],
                    "mirroredmissilepos": 3,
                    "hitpoint": "HitPylon4",
                    "hardpoints": ["RHS_HP_KH25_APU68_MIG29","RHS_HP_FAB100_BD3_UMK2A","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB250_BD3_UMK2A","RHS_HP_FAB500_BD3_UMK2A","RHS_HP_KAB500_BD3_UMK2A","RHS_HP_KMGU2_BD3_UMK2A","RHS_HP_BD3_USK_A_O25L","RHS_HP_APU68_BD3_UMK2A","RHS_HP_B13L_BD3_UMK2A","RHS_HP_B8M1_BD3_UMK2A","RHS_HP_UB16_BD3_UMK2A","RHS_HP_UB32_BD3_UMK2A","RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R60_APU60","RHS_HP_R73_APU73"],
                    "priority": 7,
                    "maxweight": 1200
                },
                # Class: CfgVehicles|rhssaf_airforce_l_18|Components|TransportPylonsComponent|pylons|pylon5 [Indent level: 4],
                "pylon5": {
                    "attachment": "rhs_mag_R60M_APU60",
                    "hardpoints": ["RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R60_APU60","RHS_HP_R73_APU73"],
                    "priority": 10,
                    "maxweight": 1200,
                    "uiposition": [0.34,0.1],
                    "hitpoint": "HitPylon5"
                },
                # Class: CfgVehicles|rhssaf_airforce_l_18|Components|TransportPylonsComponent|pylons|pylon6 [Indent level: 4],
                "pylon6": {
                    "attachment": "rhs_mag_R60M_APU60",
                    "uiposition": [0.34,0.45],
                    "mirroredmissilepos": 5,
                    "hitpoint": "HitPylon6",
                    "hardpoints": ["RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R60_APU60","RHS_HP_R73_APU73"],
                    "priority": 10,
                    "maxweight": 1200
                },
                # Class: CfgVehicles|rhssaf_airforce_l_18|Components|TransportPylonsComponent|pylons|pylon7 [Indent level: 4],
                "pylon7": {
                    "hardpoints": ["RHS_HP_PTB1500"],
                    "priority": 1,
                    "uiposition": [0.33,0.275],
                    "attachment": "",
                    "hitpoint": "HitPylon7",
                    "maxweight": 1200
                },
                # Class: CfgVehicles|rhssaf_airforce_l_18|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4],
                "cmdispenser": {
                    "hardpoints": ["RHS_cm_BVP3026","RHS_cm_BVP3026_x2"],
                    "priority": 1,
                    "attachment": "rhs_BVP3026_CMFlare_Chaff_Magazine_x2",
                    "maxweight": 800,
                    "uiposition": [0.625,0.275]
                }
            },
            "uipicture": "rhsafrf|addons|rhs_mig29|data|loadouts|RHS_MiG29_EDEN_CA.paa",
            # Class: CfgVehicles|rhs_mig29sm_base|Components|TransportPylonsComponent|Presets [Indent level: 3],
            "presets": {
                # Class: CfgVehicles|rhs_mig29sm_base|Components|TransportPylonsComponent|Presets|Bomb [Indent level: 4]
                "bomb": {
                    "attachment": ["rhs_mag_fab500_bd3_umk2a","rhs_mag_fab500_bd3_umk2a","rhs_mag_fab500_bd3_umk2a","rhs_mag_fab500_bd3_umk2a","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "Bomb"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|TransportPylonsComponent|Presets|LaserBomb [Indent level: 4],
                "laserbomb": {
                    "attachment": ["rhs_mag_kab500kr_bd3_umk2a","rhs_mag_kab500kr_bd3_umk2a","rhs_mag_kab500kr_bd3_umk2a","rhs_mag_kab500kr_bd3_umk2a","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "Guided bombs"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|TransportPylonsComponent|Presets|AirToGround [Indent level: 4],
                "airtoground": {
                    "attachment": ["rhs_mag_kh29T_aku58_mig29","rhs_mag_kh29T_aku58_mig29","rhs_mag_b8m1_bd3_umk2a_s8df","rhs_mag_b8m1_bd3_umk2a_s8df","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "Kh-29T"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|TransportPylonsComponent|Presets|KMGU [Indent level: 4],
                "kmgu": {
                    "attachment": ["rhs_mag_kmgu2_ao25_bd3_umk2a","rhs_mag_kmgu2_ao25_bd3_umk2a","rhs_mag_kmgu2_ao25_bd3_umk2a","rhs_mag_kmgu2_ao25_bd3_umk2a","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "KMGU-2 (AO-2.5)"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|TransportPylonsComponent|Presets|AA [Indent level: 4],
                "aa": {
                    "attachment": ["rhs_mag_R27ER_APU470","rhs_mag_R27ER_APU470","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "Anti Air"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|TransportPylonsComponent|Presets|CAS [Indent level: 4],
                "cas": {
                    "attachment": ["rhs_mag_b8m1_bd3_umk2a_s8kom","rhs_mag_b8m1_bd3_umk2a_s8kom","rhs_mag_b8m1_bd3_umk2a_s8df","rhs_mag_b8m1_bd3_umk2a_s8df","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "Close Air Support"
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent|Components|IRSensorComponent [Indent level: 4]
                "irsensorcomponent": {
                    # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent|Components|IRSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 500,
                        "maxrange": 5000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent|Components|IRSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 500,
                        "maxrange": 500,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 120,
                    "maxtrackablespeed": 500,
                    "componenttype": "IRSensorComponent",
                    "typerecognitiondistance": 2000,
                    "maxfogseethrough": 0.995,
                    "color": [1,0,0,1],
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4],
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
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent [Indent level: 4],
                "activeradarsensorcomponent": {
                    # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 23000,
                        "maxrange": 23000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 9000,
                        "maxrange": 9000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "typerecognitiondistance": 6000,
                    "anglerangehorizontal": 60,
                    "anglerangevertical": 60,
                    "groundnoisedistancecoef": 0.1,
                    "componenttype": "ActiveRadarSensorComponent",
                    "maxgroundnoisedistance": 200,
                    "minspeedthreshold": 20.8333,
                    "maxspeedthreshold": 27.7778,
                    "color": [0,1,1,1],
                    "allowsmarking": 1,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4],
                "lasersensorcomponent": {
                    "componenttype": "LaserSensorComponent",
                    # Class: SensorTemplateLaser|AirTarget [Indent level: 0],
                    "airtarget": {
                        "minrange": 6000,
                        "maxrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: SensorTemplateLaser|GroundTarget [Indent level: 0],
                    "groundtarget": {
                        "minrange": 6000,
                        "maxrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 180,
                    "anglerangevertical": 180,
                    "typerecognitiondistance": 0,
                    "color": [1,1,1,0],
                    "allowsmarking": 1,
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
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|SensorsManagerComponent|Components|DataLinkSensorComponent [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mig29sm_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhs_mig29sm_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhs_mig29sm_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [16000,35000,3000,8000],
                    "showtargettypes": "1+2+4+8+32+128+256"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|rhs_mig29sm_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|rhs_mig29sm_base|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhs_mig29sm_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [16000,35000,3000,8000],
                    "showtargettypes": "1+2+4+8+32+128+256"
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
    "model": "rhsafrf|addons|rhs_mig29|mig29sm.p3d",
    # Class: CfgVehicles|rhs_mig29sm_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhs_mig29sm_base|AnimationSources|Hide_TV [Indent level: 2]
        "hide_tv": {
            "source": "user",
            "initphase": 0,
            "animperiod": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|CollisionLightRed_source [Indent level: 2],
        "collisionlightred_source": {
            "source": "MarkerLight",
            "markerlight": "PositionRed"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|CollisionLightGreen_source [Indent level: 2],
        "collisionlightgreen_source": {
            "source": "MarkerLight",
            "markerlight": "PositionGreen"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|CollisionLightWhite_source [Indent level: 2],
        "collisionlightwhite_source": {
            "source": "MarkerLight",
            "markerlight": "PositionWhite"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|UserSunfilter [Indent level: 2],
        "usersunfilter": {
            "source": "user",
            "animperiod": 1,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|fold_mirrors [Indent level: 2],
        "fold_mirrors": {
            "source": "user",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|switch_gear [Indent level: 2],
        "switch_gear": {
            "animperiod": 0.8,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|switch_hud [Indent level: 2],
        "switch_hud": {
            "animperiod": 0.8,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|switch_mastersafe [Indent level: 2],
        "switch_mastersafe": {
            "animperiod": 0.8,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|afterburner_source [Indent level: 2],
        "afterburner_source": {
            "source": "user",
            "initphase": 0,
            "animperiod": 1.5
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|eject [Indent level: 2],
        "eject": {
            "source": "door",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|eject_hide [Indent level: 2],
        "eject_hide": {
            "source": "user",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|rwr_lights_lock [Indent level: 2],
        "rwr_lights_lock": {
            "source": "user",
            "initphase": 0,
            "animperiod": 8
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|rwr_lock_dir_primary [Indent level: 2],
        "rwr_lock_dir_primary": {
            "animperiod": 0.1,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|rwr_lock_primary [Indent level: 2],
        "rwr_lock_primary": {
            "animperiod": 1e-007,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|rwr_signal_strenght [Indent level: 2],
        "rwr_signal_strenght": {
            "animperiod": 1e-007,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|HitEngine_1 [Indent level: 2],
        "hitengine_1": {
            "source": "hit",
            "hitpoint": "HitEngine"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|HitEngine_2 [Indent level: 2],
        "hitengine_2": {
            "source": "hit",
            "hitpoint": "HitEngine2"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|GSh_ammorandom [Indent level: 2],
        "gsh_ammorandom": {
            "source": "ammorandom",
            "weapon": "rhs_weap_GSh301"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|GSh_reload [Indent level: 2],
        "gsh_reload": {
            "source": "reload",
            "weapon": "rhs_weap_GSh301"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|rwr_lights [Indent level: 2],
        "rwr_lights": {
            "animperiod": 1e-007,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|Damper_1_source [Indent level: 2],
        "damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|Damper_2_source [Indent level: 2],
        "damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|Damper_3_source [Indent level: 2],
        "damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|Wheel_1_source [Indent level: 2],
        "wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|Wheel_2_source [Indent level: 2],
        "wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|Wheel_3_source [Indent level: 2],
        "wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|hit_pylon_1_source [Indent level: 2],
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|hit_pylon_2_source [Indent level: 2],
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|hit_pylon_3_source [Indent level: 2],
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|hit_pylon_4_source [Indent level: 2],
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|hit_pylon_5_source [Indent level: 2],
        "hit_pylon_5_source": {
            "source": "Hit",
            "hitpoint": "HitPylon5"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|hit_pylon_6_source [Indent level: 2],
        "hit_pylon_6_source": {
            "source": "Hit",
            "hitpoint": "HitPylon6"
        },
        # Class: CfgVehicles|rhs_mig29s_base|AnimationSources|hit_pylon_7_source [Indent level: 2],
        "hit_pylon_7_source": {
            "source": "Hit",
            "hitpoint": "HitPylon7"
        }
    },
    "unitinfotype": "RHS_RscUnitInfoAir_MiG29SM",
    # Class: CfgVehicles|rhs_mig29sm_base|pilotCamera [Indent level: 1],
    "pilotcamera": {
        # Class: CfgVehicles|rhs_mig29sm_base|pilotCamera|OpticsIn [Indent level: 2]
        "opticsin": {
            # Class: CfgVehicles|rhs_mig29sm_base|pilotCamera|OpticsIn|Wide [Indent level: 3]
            "wide": {
                "opticsdisplayname": "DEFAULT",
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.35,
                "minfov": 0.35,
                "maxfov": 0.35,
                "directionstabilized": 0,
                "visionmode": ["Normal","TI"],
                "thermalmode": [0,1],
                "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mig29sm_tv_1x.p3d"
            },
            # Class: CfgVehicles|rhs_mig29sm_base|pilotCamera|OpticsIn|Narrow [Indent level: 3],
            "narrow": {
                "opticsdisplayname": "ZOOM",
                "initfov": 0.04375,
                "minfov": 0.04375,
                "maxfov": 0.04375,
                "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mig29sm_tv_1x.p3d",
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "directionstabilized": 0,
                "visionmode": ["Normal","TI"],
                "thermalmode": [0,1]
            },
            # Class: CfgVehicles|rhs_mig29sm_base|pilotCamera|OpticsIn|VeryNarrow [Indent level: 3],
            "verynarrow": {
                "opticsdisplayname": "ZOOM",
                "initfov": 0.0152174,
                "minfov": 0.0152174,
                "maxfov": 0.0152174,
                "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mig29sm_tv_1x.p3d",
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "directionstabilized": 0,
                "visionmode": ["Normal","TI"],
                "thermalmode": [0,1]
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
    "memorypointdriveroptics": "pilotCamera",
    "defaultusermfdvalues": [1,0,0,0],
    # Class: CfgVehicles|rhs_mig29sm_base|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD [Indent level: 2]
        "hud": {
            "topleft": "HUD_top_left",
            "topright": "HUD_top_right",
            "bottomleft": "HUD_bottom_left",
            "enableparallax": 1,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_rus",
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|material [Indent level: 3],
            "material": {
                "ambient": [10,10,10,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|PlaneOrientation [Indent level: 4]
                "planeorientation": {
                    "type": "fixed",
                    "refreshrate": 0.1,
                    "pos": [0.5,0.53]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|ClimbFixed [Indent level: 4],
                "climbfixed": {
                    "type": "fixed",
                    "pos": [0.898,0.7]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|ClimbRotate [Indent level: 4],
                "climbrotate": {
                    "type": "rotational",
                    "source": "vspeed",
                    "sourcescale": 1,
                    "center": [0.88,0.7],
                    "min": -30,
                    "max": 30,
                    "minangle": -90,
                    "maxangle": 90,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|WeaponAim [Indent level: 4],
                "weaponaim": {
                    "type": "vector",
                    "source": "weapon",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|HorizonBankSource [Indent level: 4],
                "horizonbanksource": {
                    "type": "rotational",
                    "source": "HorizonBank",
                    "center": [0.5,0.53],
                    "min": -6.2831,
                    "max": 6.2831,
                    "minangle": -360,
                    "maxangle": 360
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|HorizonBankInverted [Indent level: 4],
                "horizonbankinverted": {
                    "type": "rotational",
                    "source": "HorizonBank",
                    "center": [0.5,0.53],
                    "min": -6.2831,
                    "max": 6.2831,
                    "minangle": 360,
                    "maxangle": -360,
                    "refreshrate": 0.1
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|HorizonBankRotFull [Indent level: 4],
                "horizonbankrotfull": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "center": [0,0],
                    "min": -3.1416,
                    "max": 3.1416,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|Level0 [Indent level: 4],
                "level0": {
                    "source": "horizonDive",
                    "type": "linear",
                    "angle": 0,
                    "min": -3.4,
                    "max": 3.4,
                    "minpos": [0.5,4.78],
                    "maxpos": [0.5,-3.72],
                    "refreshrate": 0.1
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|TerrainBone [Indent level: 4],
                "terrainbone": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 200,
                    "minpos": [0,0.666],
                    "maxpos": [0,0.4]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|ImpactPoint [Indent level: 4],
                "impactpoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|ImpactPointRelative [Indent level: 4],
                "impactpointrelative": {
                    "type": "vector",
                    "source": "impactpointweaponRelative",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|Limit0109 [Indent level: 4],
                "limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|Target [Indent level: 4],
                "target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|TargetingPodTarget [Indent level: 4],
                "targetingpodtarget": {
                    "source": "pilotcamera",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|WPPoint [Indent level: 4],
                "wppoint": {
                    "type": "vector",
                    "source": "WPPoint",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot1 [Indent level: 4],
                "missileflighttimerot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minangle": 0,
                    "maxangle": 18,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot2 [Indent level: 4],
                "missileflighttimerot2": {
                    "maxangle": 37,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot3 [Indent level: 4],
                "missileflighttimerot3": {
                    "maxangle": 55.5,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot4 [Indent level: 4],
                "missileflighttimerot4": {
                    "maxangle": 74,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot5 [Indent level: 4],
                "missileflighttimerot5": {
                    "maxangle": 92.5,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot6 [Indent level: 4],
                "missileflighttimerot6": {
                    "maxangle": 111,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot7 [Indent level: 4],
                "missileflighttimerot7": {
                    "maxangle": 129.5,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot8 [Indent level: 4],
                "missileflighttimerot8": {
                    "maxangle": 148,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot9 [Indent level: 4],
                "missileflighttimerot9": {
                    "maxangle": 166.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot10 [Indent level: 4],
                "missileflighttimerot10": {
                    "maxangle": 185,
                    "max": 10,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot11 [Indent level: 4],
                "missileflighttimerot11": {
                    "maxangle": 203.5,
                    "max": 11,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot12 [Indent level: 4],
                "missileflighttimerot12": {
                    "maxangle": 222,
                    "max": 12,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot13 [Indent level: 4],
                "missileflighttimerot13": {
                    "maxangle": 240.5,
                    "max": 13,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot14 [Indent level: 4],
                "missileflighttimerot14": {
                    "maxangle": 259,
                    "max": 14,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot15 [Indent level: 4],
                "missileflighttimerot15": {
                    "maxangle": 277.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot16 [Indent level: 4],
                "missileflighttimerot16": {
                    "maxangle": 296,
                    "max": 16,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot17 [Indent level: 4],
                "missileflighttimerot17": {
                    "maxangle": 314.5,
                    "max": 17,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot18 [Indent level: 4],
                "missileflighttimerot18": {
                    "maxangle": 333,
                    "max": 18,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot19 [Indent level: 4],
                "missileflighttimerot19": {
                    "maxangle": 351.5,
                    "max": 19,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|MissileFlightTimeRot20 [Indent level: 4],
                "missileflighttimerot20": {
                    "maxangle": 370,
                    "max": 20,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|Airport1 [Indent level: 4],
                "airport1": {
                    "type": "vector",
                    "source": "airportCorner1",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|Airport2 [Indent level: 4],
                "airport2": {
                    "source": "airportCorner2",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|Airport3 [Indent level: 4],
                "airport3": {
                    "source": "airportCorner3",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|Airport4 [Indent level: 4],
                "airport4": {
                    "source": "airportCorner4",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|ILS_H [Indent level: 4],
                "ils_h": {
                    "type": "ils",
                    "pos0": [0.5,0.53],
                    "pos3": [0.674,0.53]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|ILS_W [Indent level: 4],
                "ils_w": {
                    "pos3": [0.5,0.707],
                    "type": "ils",
                    "pos0": [0.5,0.53]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|LarAmmoMax [Indent level: 4],
                "larammomax": {
                    "type": "linear",
                    "source": "LarAmmoMax",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|LarAmmoMin [Indent level: 4],
                "larammomin": {
                    "source": "LarAmmoMin",
                    "type": "linear",
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|LarTargetDist [Indent level: 4],
                "lartargetdist": {
                    "source": "LarTargetDist",
                    "sourcescale": 0.65,
                    "type": "linear",
                    "min": 0,
                    "max": 1,
                    "minpos": [0,1],
                    "maxpos": [0,0]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|LarAmmoMGunMax [Indent level: 4],
                "larammomgunmax": {
                    "type": "rotational",
                    "source": "LarAmmoMax",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 1,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 1.01724
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Bones|LarAmmoMGunMin [Indent level: 4],
                "larammomgunmin": {
                    "source": "LarAmmoMin",
                    "type": "rotational",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 1,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 1.01724
                }
            },
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                "condition": "on-user3",
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0.1,0.38],
                    "clipbr": [0.9,0.78],
                    "condition": "1-(bomb+mgun+atmissile+aamissile+rocket)*activeSensorsOn",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level00 [Indent level: 6]
                        "level00": {
                            "type": "line",
                            "width": 5,
                            "points": [["Level0",[0.176,0],1],["Level0",[-0.176,0],1],[]]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2M00 [Indent level: 6],
                        "level2m00": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.224,0],1],["Level0",[0.18,0],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALM2_1_00 [Indent level: 6],
                        "valm2_1_00": {
                            "type": "text",
                            "source": "static",
                            "text": 0,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,-0.036],1],
                            "right": ["Level0",[0.24,-0.036],1],
                            "down": ["Level0",[0.2,-0.004],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2M10 [Indent level: 6],
                        "level2m10": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.224,-0.218519],1],["Level0",[0.18,-0.218519],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALM2_1_10 [Indent level: 6],
                        "valm2_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": 10,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,-0.254519],1],
                            "right": ["Level0",[0.24,-0.254519],1],
                            "down": ["Level0",[0.2,-0.222519],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2P10 [Indent level: 6],
                        "level2p10": {
                            "type": "line",
                            "linetype": 2,
                            "points": [["Level0",[0.224,0.218519],1],["Level0",[0.18,0.218519],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALP2_1_10 [Indent level: 6],
                        "valp2_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,0.182519],1],
                            "right": ["Level0",[0.24,0.182519],1],
                            "down": ["Level0",[0.2,0.214519],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2M20 [Indent level: 6],
                        "level2m20": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.224,-0.437037],1],["Level0",[0.18,-0.437037],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALM2_1_20 [Indent level: 6],
                        "valm2_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": 20,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,-0.473037],1],
                            "right": ["Level0",[0.24,-0.473037],1],
                            "down": ["Level0",[0.2,-0.441037],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2P20 [Indent level: 6],
                        "level2p20": {
                            "type": "line",
                            "linetype": 2,
                            "points": [["Level0",[0.224,0.437037],1],["Level0",[0.18,0.437037],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALP2_1_20 [Indent level: 6],
                        "valp2_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,0.401037],1],
                            "right": ["Level0",[0.24,0.401037],1],
                            "down": ["Level0",[0.2,0.433037],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2M30 [Indent level: 6],
                        "level2m30": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.224,-0.655556],1],["Level0",[0.18,-0.655556],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALM2_1_30 [Indent level: 6],
                        "valm2_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": 30,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,-0.691556],1],
                            "right": ["Level0",[0.24,-0.691556],1],
                            "down": ["Level0",[0.2,-0.659556],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2P30 [Indent level: 6],
                        "level2p30": {
                            "type": "line",
                            "linetype": 2,
                            "points": [["Level0",[0.224,0.655556],1],["Level0",[0.18,0.655556],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALP2_1_30 [Indent level: 6],
                        "valp2_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,0.619556],1],
                            "right": ["Level0",[0.24,0.619556],1],
                            "down": ["Level0",[0.2,0.651556],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2M40 [Indent level: 6],
                        "level2m40": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.224,-0.874074],1],["Level0",[0.18,-0.874074],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALM2_1_40 [Indent level: 6],
                        "valm2_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": 40,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,-0.910074],1],
                            "right": ["Level0",[0.24,-0.910074],1],
                            "down": ["Level0",[0.2,-0.878074],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2P40 [Indent level: 6],
                        "level2p40": {
                            "type": "line",
                            "linetype": 2,
                            "points": [["Level0",[0.224,0.874074],1],["Level0",[0.18,0.874074],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALP2_1_40 [Indent level: 6],
                        "valp2_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,0.838074],1],
                            "right": ["Level0",[0.24,0.838074],1],
                            "down": ["Level0",[0.2,0.870074],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2M50 [Indent level: 6],
                        "level2m50": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.224,-1.09259],1],["Level0",[0.18,-1.09259],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALM2_1_50 [Indent level: 6],
                        "valm2_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": 50,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,-1.12859],1],
                            "right": ["Level0",[0.24,-1.12859],1],
                            "down": ["Level0",[0.2,-1.09659],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2P50 [Indent level: 6],
                        "level2p50": {
                            "type": "line",
                            "linetype": 2,
                            "points": [["Level0",[0.224,1.09259],1],["Level0",[0.18,1.09259],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALP2_1_50 [Indent level: 6],
                        "valp2_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,1.05659],1],
                            "right": ["Level0",[0.24,1.05659],1],
                            "down": ["Level0",[0.2,1.08859],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2M60 [Indent level: 6],
                        "level2m60": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.224,-1.31111],1],["Level0",[0.18,-1.31111],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALM2_1_60 [Indent level: 6],
                        "valm2_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": 60,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,-1.34711],1],
                            "right": ["Level0",[0.24,-1.34711],1],
                            "down": ["Level0",[0.2,-1.31511],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2P60 [Indent level: 6],
                        "level2p60": {
                            "type": "line",
                            "linetype": 2,
                            "points": [["Level0",[0.224,1.31111],1],["Level0",[0.18,1.31111],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALP2_1_60 [Indent level: 6],
                        "valp2_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,1.27511],1],
                            "right": ["Level0",[0.24,1.27511],1],
                            "down": ["Level0",[0.2,1.30711],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2M70 [Indent level: 6],
                        "level2m70": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.224,-1.52963],1],["Level0",[0.18,-1.52963],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALM2_1_70 [Indent level: 6],
                        "valm2_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": 70,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,-1.56563],1],
                            "right": ["Level0",[0.24,-1.56563],1],
                            "down": ["Level0",[0.2,-1.53363],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2P70 [Indent level: 6],
                        "level2p70": {
                            "type": "line",
                            "linetype": 2,
                            "points": [["Level0",[0.224,1.52963],1],["Level0",[0.18,1.52963],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALP2_1_70 [Indent level: 6],
                        "valp2_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,1.49363],1],
                            "right": ["Level0",[0.24,1.49363],1],
                            "down": ["Level0",[0.2,1.52563],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2M80 [Indent level: 6],
                        "level2m80": {
                            "type": "line",
                            "linetype": 0,
                            "points": [["Level0",[0.224,-1.74815],1],["Level0",[0.18,-1.74815],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALM2_1_80 [Indent level: 6],
                        "valm2_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": 80,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,-1.78415],1],
                            "right": ["Level0",[0.24,-1.78415],1],
                            "down": ["Level0",[0.2,-1.75215],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|Level2P80 [Indent level: 6],
                        "level2p80": {
                            "type": "line",
                            "linetype": 2,
                            "points": [["Level0",[0.224,1.74815],1],["Level0",[0.18,1.74815],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|Dimmed|VALP2_1_80 [Indent level: 6],
                        "valp2_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "align": "center",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["Level0",[0.2,1.71215],1],
                            "right": ["Level0",[0.24,1.71215],1],
                            "down": ["Level0",[0.2,1.74415],1]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|BankDetailed [Indent level: 5],
                    "bankdetailed": {
                        "condition": "1-(bomb+mgun+atmissile+aamissile+rocket+missilelocked + missilelocking+activeSensorsOn)",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Horizont|BankDetailed|Level00 [Indent level: 6],
                        "level00": {
                            "type": "line",
                            "width": 5,
                            "points": [["PlaneOrientation",[-0.144889,0.0394922],1],["PlaneOrientation",[-0.164207,0.0447579],1],[],["PlaneOrientation",[-0.129904,0.0762931],1],["PlaneOrientation",[-0.164545,0.0966379],1],[],["PlaneOrientation",[-0.106066,0.107895],1],["PlaneOrientation",[-0.120208,0.122281],1],[],["PlaneOrientation",[-0.075,0.132144],1],["PlaneOrientation",[-0.095,0.167382],1],[],["PlaneOrientation",[0.144889,0.0394922],1],["PlaneOrientation",[0.164207,0.0447578],1],[],["PlaneOrientation",[0.129904,0.0762931],1],["PlaneOrientation",[0.164545,0.0966379],1],[],["PlaneOrientation",[0.106066,0.107895],1],["PlaneOrientation",[0.120208,0.122281],1],[],["PlaneOrientation",[0.075,0.132144],1],["PlaneOrientation",[0.095,0.167382],1],[]]
                        }
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PlaneOrientationCrosshair [Indent level: 4],
                "planeorientationcrosshair": {
                    "type": "line",
                    "width": 3,
                    "points": [["HorizonBankInverted",[-0.1375,0],1],["HorizonBankInverted",[-0.0416667,0],1],[],["HorizonBankInverted",[-0.0833333,0],1],["HorizonBankInverted",[-0.0833333,-0.025],1],[],["HorizonBankInverted",[0.0416667,0],1],["HorizonBankInverted",[0.1375,0],1],[],["HorizonBankInverted",[0.0833333,0],1],["HorizonBankInverted",[0.0833333,-0.025],1],[],["HorizonBankInverted",[-0,0.0333333],1],["HorizonBankInverted",[-0,0.075],1],[],["PlaneOrientation",[-0.170833,0],1],["PlaneOrientation",[-0.145833,0],1],[],["PlaneOrientation",[0.145833,0],1],["PlaneOrientation",[0.170833,0],1],[]]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|GunCross [Indent level: 4],
                "guncross": {
                    "condition": "1-mgun*impactDistance*(altitudeAGL>=5)",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|GunCross|Cross [Indent level: 5],
                    "cross": {
                        "type": "line",
                        "width": 3,
                        "points": [["PlaneOrientation",[0,-0.03],1],["PlaneOrientation",[0,-0.01],1],[],["PlaneOrientation",[0,0.03],1],["PlaneOrientation",[0,0.01],1],[],["PlaneOrientation",[-0.03,0],1],["PlaneOrientation",[-0.01,0],1],[],["PlaneOrientation",[0.03,0],1],["PlaneOrientation",[0.01,0],1],[]]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MissileLocked [Indent level: 4],
                "missilelocked": {
                    "condition": "missilelocked",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MissileLocked|LaunchReady [Indent level: 5],
                    "launchready": {
                        "type": "text",
                        "source": "static",
                        "text": "ПР",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,"0.49+0.19"],1],
                        "right": [[0.58,"0.49+0.19"],1],
                        "down": [[0.5,0.75],1]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MissileLocking [Indent level: 4],
                "missilelocking": {
                    "condition": "missilelocking",
                    "blinkingpattern": [0.2,0.5],
                    "blinkingstartson": 1,
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MissileLocking|LaunchReady [Indent level: 5],
                    "launchready": {
                        "type": "text",
                        "source": "static",
                        "text": "ПР",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,"0.49+0.19"],1],
                        "right": [[0.58,"0.49+0.19"],1],
                        "down": [[0.5,0.75],1]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|SpeedNumber0 [Indent level: 4],
                "speednumber0": {
                    "type": "text",
                    "source": "static",
                    "text": 0,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.31,"0.09+0.19"],1],
                    "right": [[0.375,"0.09+0.19"],1],
                    "down": [[0.31,0.35],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|SpeedNumber [Indent level: 4],
                "speednumber": {
                    "source": "speed",
                    "sourcescale": 0.36,
                    "pos": [[0.275,"0.09+0.19"],1],
                    "right": [[0.34,"0.09+0.19"],1],
                    "down": [[0.275,0.35],1],
                    "type": "text",
                    "text": 0,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AccelerationLine [Indent level: 4],
                "accelerationline": {
                    "type": "line",
                    "width": 4,
                    "points": [[[0.22,0.35],1],[[0.29,0.35],1]]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Acceleration0Group [Indent level: 4],
                "acceleration0group": {
                    "condition": "1-abs(gmeterZ)",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|Acceleration0Group|Acceleration [Indent level: 5],
                    "acceleration": {
                        "type": "line",
                        "width": 2,
                        "points": [[[0.249,0.362],1],[[0.255,0.35],1],[[0.261,0.362],1],[[0.249,0.362],1]]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AccelerationPlusGroup [Indent level: 4],
                "accelerationplusgroup": {
                    "condition": "gmeterZ>=0.5",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AccelerationPlusGroup|Acceleration [Indent level: 5],
                    "acceleration": {
                        "type": "line",
                        "width": 2,
                        "points": [[[0.279,0.362],1],[[0.285,0.35],1],[[0.291,0.362],1],[[0.279,0.362],1]]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AccelerationMinusGroup [Indent level: 4],
                "accelerationminusgroup": {
                    "condition": "gmeterZ<=-0.5",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AccelerationMinusGroup|Acceleration [Indent level: 5],
                    "acceleration": {
                        "type": "line",
                        "width": 2,
                        "points": [[[0.219,0.362],1],[[0.225,0.35],1],[[0.231,0.362],1],[[0.219,0.362],1]]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AltitudeNumber0 [Indent level: 4],
                "altitudenumber0": {
                    "type": "text",
                    "source": "static",
                    "text": 0,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.82,"0.09+0.19"],1],
                    "right": [[0.885,"0.09+0.19"],1],
                    "down": [[0.82,0.35],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AltitudeNumber [Indent level: 4],
                "altitudenumber": {
                    "source": "altitudeASL",
                    "sourcescale": 0.1,
                    "sourcelength": 1,
                    "pos": [[0.785,"0.09+0.19"],1],
                    "right": [[0.85,"0.09+0.19"],1],
                    "down": [[0.785,0.35],1],
                    "type": "text",
                    "text": 0,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|RadarOnGroup [Indent level: 4],
                "radarongroup": {
                    "condition": "activeSensorsOn",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|RadarOnGroup|RadarText [Indent level: 5],
                    "radartext": {
                        "type": "text",
                        "source": "static",
                        "text": "РЛ",
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.18,0.45],1],
                        "right": [[0.23,0.45],1],
                        "down": [[0.18,0.5],1]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup [Indent level: 4],
                "pylongroup": {
                    "condition": "bomb+mgun+atmissile+aamissile+rocket",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon1 [Indent level: 5],
                    "pylon1": {
                        "condition": "1-pylonSelected1",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon1|PylonLine [Indent level: 6],
                        "pylonline": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.509,0.78],1],[[0.541,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon1Selected [Indent level: 5],
                    "pylon1selected": {
                        "condition": "pylonSelected1",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon1Selected|PylonLine [Indent level: 6],
                        "pylonline": {
                            "points": [[[0.509,0.745],1],[[0.541,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon2 [Indent level: 5],
                    "pylon2": {
                        "condition": "1-pylonSelected2",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon2|PylonLine [Indent level: 6],
                        "pylonline": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.434,0.78],1],[[0.466,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon2Selected [Indent level: 5],
                    "pylon2selected": {
                        "condition": "pylonSelected2",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon2Selected|PylonLine [Indent level: 6],
                        "pylonline": {
                            "points": [[[0.434,0.745],1],[[0.466,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon3 [Indent level: 5],
                    "pylon3": {
                        "condition": "1-pylonSelected3",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon3|PylonLine [Indent level: 6],
                        "pylonline": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.559,0.78],1],[[0.591,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon3Selected [Indent level: 5],
                    "pylon3selected": {
                        "condition": "pylonSelected3",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon3Selected|PylonLine [Indent level: 6],
                        "pylonline": {
                            "points": [[[0.559,0.745],1],[[0.591,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon4 [Indent level: 5],
                    "pylon4": {
                        "condition": "1-pylonSelected4",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon4|PylonLine [Indent level: 6],
                        "pylonline": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.384,0.78],1],[[0.416,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon4Selected [Indent level: 5],
                    "pylon4selected": {
                        "condition": "pylonSelected4",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon4Selected|PylonLine [Indent level: 6],
                        "pylonline": {
                            "points": [[[0.384,0.745],1],[[0.416,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon5 [Indent level: 5],
                    "pylon5": {
                        "condition": "1-pylonSelected5",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon5|PylonLine [Indent level: 6],
                        "pylonline": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.609,0.78],1],[[0.641,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon5Selected [Indent level: 5],
                    "pylon5selected": {
                        "condition": "pylonSelected5",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon5Selected|PylonLine [Indent level: 6],
                        "pylonline": {
                            "points": [[[0.609,0.745],1],[[0.641,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon6 [Indent level: 5],
                    "pylon6": {
                        "condition": "1-pylonSelected6",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon6|PylonLine [Indent level: 6],
                        "pylonline": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.334,0.78],1],[[0.366,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon6Selected [Indent level: 5],
                    "pylon6selected": {
                        "condition": "pylonSelected6",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|Pylon6Selected|PylonLine [Indent level: 6],
                        "pylonline": {
                            "points": [[[0.334,0.745],1],[[0.366,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|PylonName1 [Indent level: 5],
                    "pylonname1": {
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "pylon": 1,
                        "name": "rhs_rus_ammoname"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|PylonName2 [Indent level: 5],
                    "pylonname2": {
                        "pylon": 2,
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "name": "rhs_rus_ammoname"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|PylonName3 [Indent level: 5],
                    "pylonname3": {
                        "pylon": 3,
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "name": "rhs_rus_ammoname"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|PylonName4 [Indent level: 5],
                    "pylonname4": {
                        "pylon": 4,
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "name": "rhs_rus_ammoname"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|PylonName5 [Indent level: 5],
                    "pylonname5": {
                        "pylon": 5,
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "name": "rhs_rus_ammoname"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|PylonGroup|PylonName6 [Indent level: 5],
                    "pylonname6": {
                        "pylon": 6,
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "name": "rhs_rus_ammoname"
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|ILS [Indent level: 4],
                "ils": {
                    "condition": "ils",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|ILS|Glideslope [Indent level: 5],
                    "glideslope": {
                        "cliptl": [0,0],
                        "clipbr": [1,1],
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|ILS|Glideslope|ILS [Indent level: 6],
                        "ils": {
                            "type": "line",
                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[-0.24,-0.0244138],1],["ILS_W",[-0.24,0.0244138],1],[],["ILS_W",[-0.12,-0.0183103],1],["ILS_W",[-0.12,0.0183103],1],[],["ILS_W",[0,-0.0244138],1],["ILS_W",[0,0.0244138],1],[],["ILS_W",[0.12,-0.0183103],1],["ILS_W",[0.12,0.0183103],1],[],["ILS_W",[0.24,-0.0244138],1],["ILS_W",[0.24,0.0244138],1],[],["ILS_H",[0,-0.244138],1],["ILS_H",[0,0.244138],1],[],["ILS_H",[-0.024,-0.244138],1],["ILS_H",[0.024,-0.244138],1],[],["ILS_H",[-0.018,-0.122069],1],["ILS_H",[0.018,-0.122069],1],[],["ILS_H",[-0.024,0],1],["ILS_H",[0.024,0],1],[],["ILS_H",[-0.018,0.122069],1],["ILS_H",[0.018,0.122069],1],[],["ILS_H",[-0.024,0.244138],1],["ILS_H",[0.024,0.244138],1]]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|ILS|Glideslope|airport [Indent level: 6],
                        "airport": {
                            "type": "line",
                            "points": [["airport1",1],["airport2",1],["airport4",1],["airport3",1],["airport1",1]]
                        }
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|HeadingArrow [Indent level: 4],
                "headingarrow": {
                    "type": "line",
                    "width": 3,
                    "points": [[[0.48,0.365],1],[[0.5,0.345],1],[[0.52,0.365],1],[[0.48,0.365],1]]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|HeadingLine [Indent level: 4],
                "headingline": {
                    "type": "line",
                    "width": 4,
                    "points": [[[0.35,0.34],1],[[0.65,0.34],1]]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|HeadingScale [Indent level: 4],
                "headingscale": {
                    "type": "scale",
                    "horizontal": 1,
                    "source": "heading",
                    "sourcescale": 0.1,
                    "width": 4,
                    "nevereatseaweed": 0,
                    "refreshrate": 0.1,
                    "top": 0.35,
                    "center": 0.5,
                    "bottom": 0.65,
                    "linexleft": 0.338,
                    "lineyright": 0.328,
                    "linexleftmajor": 0.338,
                    "lineyrightmajor": 0.318,
                    "majorlineeach": 2,
                    "numbereach": 2,
                    "step": 0.5,
                    "stepsize": 0.0526316,
                    "align": "center",
                    "scale": 1,
                    "pos": [0.35,0.27],
                    "right": [0.4,0.27],
                    "down": [0.35,0.31]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MarchGroup [Indent level: 4],
                "marchgroup": {
                    "condition": "1-(bomb+mgun+atmissile+aamissile+rocket)",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MarchGroup|MarchText [Indent level: 5],
                    "marchtext": {
                        "type": "text",
                        "source": "static",
                        "text": "МРШ",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.18,0.75],1],
                        "right": [[0.23,0.75],1],
                        "down": [[0.18,0.8],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MarchGroup|SpeedNumber0 [Indent level: 5],
                    "speednumber0": {
                        "type": "text",
                        "source": "WPDist",
                        "sourcescale": 0.001,
                        "sourceprecision": 1,
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,0.75],1],
                        "right": [[0.55,0.75],1],
                        "down": [[0.5,0.8],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MarchGroup|WP [Indent level: 5],
                    "wp": {
                        "condition": "wpvalid",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MarchGroup|WP|shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 4,
                            "points": [["WPPoint",[0,-0.0406897],1],["WPPoint",[0.006944,-0.0400712],1],["WPPoint",[0.01368,-0.0382361],1],["WPPoint",[0.02,-0.0352372],1],["WPPoint",[0.025712,-0.0311683],1],["WPPoint",[0.03064,-0.0261553],1],["WPPoint",[0.03464,-0.0203448],1],["WPPoint",[0.037588,-0.0139159],1],["WPPoint",[0.039392,-0.00706372],1],["WPPoint",[0.04,0],1],["WPPoint",[0.039392,0.00706372],1],["WPPoint",[0.037588,0.0139159],1],["WPPoint",[0.03464,0.0203448],1],["WPPoint",[0.03064,0.0261553],1],["WPPoint",[0.025712,0.0311683],1],["WPPoint",[0.02,0.0352372],1],["WPPoint",[0.01368,0.0382361],1],["WPPoint",[0.006944,0.0400712],1],["WPPoint",[0,0.0406897],1],["WPPoint",[-0.006944,0.0400712],1],["WPPoint",[-0.01368,0.0382361],1],["WPPoint",[-0.02,0.0352372],1],["WPPoint",[-0.025712,0.0311683],1],["WPPoint",[-0.03064,0.0261553],1],["WPPoint",[-0.03464,0.0203448],1],["WPPoint",[-0.037588,0.0139159],1],["WPPoint",[-0.039392,0.00706372],1],["WPPoint",[-0.04,0],1],["WPPoint",[-0.039392,-0.00706372],1],["WPPoint",[-0.037588,-0.0139159],1],["WPPoint",[-0.03464,-0.0203448],1],["WPPoint",[-0.03064,-0.0261553],1],["WPPoint",[-0.025712,-0.0311683],1],["WPPoint",[-0.02,-0.0352372],1],["WPPoint",[-0.01368,-0.0382361],1],["WPPoint",[-0.006944,-0.0400712],1],["WPPoint",[0,-0.0406897],1],[]]
                        }
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|HelmetModeGroup [Indent level: 4],
                "helmetmodegroup": {
                    "condition": "user2*(bomb+mgun+atmissile+aamissile+rocket)",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|HelmetModeGroup|HelmetText [Indent level: 5],
                    "helmettext": {
                        "type": "text",
                        "source": "static",
                        "text": "ШЛМ",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.18,0.75],1],
                        "right": [[0.23,0.75],1],
                        "down": [[0.18,0.8],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|HelmetModeGroup|BWBText [Indent level: 5],
                    "bwbtext": {
                        "type": "text",
                        "source": "static",
                        "text": "БВБ",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.18,0.79],1],
                        "right": [[0.23,0.79],1],
                        "down": [[0.18,0.84],1]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun [Indent level: 4],
                "mgun": {
                    "condition": "mgun",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|AmmoBox [Indent level: 5],
                    "ammobox": {
                        "type": "line",
                        "width": 3,
                        "points": [[[0.757,0.748],1],[[0.757,0.782],1],[[0.723,0.782],1],[[0.723,0.748],1],[[0.757,0.748],1],[]]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|Full [Indent level: 5],
                    "full": {
                        "condition": "ammo>=113",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|Full|AmmoText [Indent level: 6],
                        "ammotext": {
                            "type": "text",
                            "source": "static",
                            "text": "4",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0.74,0.745],1],
                            "right": [[0.785,0.745],1],
                            "down": [[0.74,0.79],1]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|AlmostFull [Indent level: 5],
                    "almostfull": {
                        "condition": "(ammo>=75)*(ammo<=112)",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|AlmostFull|AmmoText [Indent level: 6],
                        "ammotext": {
                            "type": "text",
                            "source": "static",
                            "text": "3",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0.74,0.74],1],
                            "right": [[0.785,0.74],1],
                            "down": [[0.74,0.785],1]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|Half [Indent level: 5],
                    "half": {
                        "condition": "(ammo>=38)*(ammo<=74)",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|Half|AmmoText [Indent level: 6],
                        "ammotext": {
                            "type": "text",
                            "source": "static",
                            "text": "2",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0.74,0.74],1],
                            "right": [[0.785,0.74],1],
                            "down": [[0.74,0.785],1]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|AlmostEmpty [Indent level: 5],
                    "almostempty": {
                        "condition": "(ammo>=1)*(ammo<=37)",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|AlmostEmpty|AmmoText [Indent level: 6],
                        "ammotext": {
                            "type": "text",
                            "source": "static",
                            "text": "1",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0.74,0.745],1],
                            "right": [[0.785,0.745],1],
                            "down": [[0.74,0.79],1]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|Empty [Indent level: 5],
                    "empty": {
                        "condition": "ammo<=0",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|Empty|AmmoText [Indent level: 6],
                        "ammotext": {
                            "type": "text",
                            "source": "static",
                            "text": "0",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [[0.74,0.745],1],
                            "right": [[0.785,0.745],1],
                            "down": [[0.74,0.79],1]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|CrossCondition [Indent level: 5],
                    "crosscondition": {
                        "condition": "impactDistance*(altitudeAGL>=5)",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|CrossCondition|Cross [Indent level: 6],
                        "cross": {
                            "type": "line",
                            "width": 3,
                            "points": [["ImpactPointRelative",[0,-0.025431],1],["ImpactPointRelative",[0,-0.0152586],1],[],["ImpactPointRelative",[0,0.025431],1],["ImpactPointRelative",[0,0.0152586],1],[],["ImpactPointRelative",[-0.025,0],1],["ImpactPointRelative",[-0.015,0],1],[],["ImpactPointRelative",[0.025,0],1],["ImpactPointRelative",[0.015,0],1],[],["ImpactPointRelative",[0,-0.002],1],["ImpactPointRelative",[0,0.002],1],[],["ImpactPointRelative",[-0.002,0],1],["ImpactPointRelative",[0.002,0],1],[]]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|MGun|CrossCondition|Circle [Indent level: 6],
                        "circle": {
                            "type": "line",
                            "width": 4,
                            "points": [["ImpactPointRelative",[0,-0.0260414],1],["ImpactPointRelative",[0,-0.0325517],1],["MissileFlightTimeRot1",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot2",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot3",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot4",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot5",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot6",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot7",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot8",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot9",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot10",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot11",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot12",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot13",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot14",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot15",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot16",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot17",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot18",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot19",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot20",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot20",[0,0.0256],1,"ImpactPointRelative",1]]
                        }
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|BombCrosshairGroup [Indent level: 4],
                "bombcrosshairgroup": {
                    "type": "group",
                    "condition": "bomb+rocket*impactDistance",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|BombCrosshairGroup|BombCrosshair [Indent level: 5],
                    "bombcrosshair": {
                        "type": "line",
                        "width": 4,
                        "points": [["ImpactPoint",[0,-0.0406897],1],["ImpactPoint",[0.006944,-0.0400712],1],["ImpactPoint",[0.01368,-0.0382361],1],["ImpactPoint",[0.02,-0.0352372],1],["ImpactPoint",[0.025712,-0.0311683],1],["ImpactPoint",[0.03064,-0.0261553],1],["ImpactPoint",[0.03464,-0.0203448],1],["ImpactPoint",[0.037588,-0.0139159],1],["ImpactPoint",[0.039392,-0.00706372],1],["ImpactPoint",[0.04,0],1],["ImpactPoint",[0.039392,0.00706372],1],["ImpactPoint",[0.037588,0.0139159],1],["ImpactPoint",[0.03464,0.0203448],1],["ImpactPoint",[0.03064,0.0261553],1],["ImpactPoint",[0.025712,0.0311683],1],["ImpactPoint",[0.02,0.0352372],1],["ImpactPoint",[0.01368,0.0382361],1],["ImpactPoint",[0.006944,0.0400712],1],["ImpactPoint",[0,0.0406897],1],["ImpactPoint",[-0.006944,0.0400712],1],["ImpactPoint",[-0.01368,0.0382361],1],["ImpactPoint",[-0.02,0.0352372],1],["ImpactPoint",[-0.025712,0.0311683],1],["ImpactPoint",[-0.03064,0.0261553],1],["ImpactPoint",[-0.03464,0.0203448],1],["ImpactPoint",[-0.037588,0.0139159],1],["ImpactPoint",[-0.039392,0.00706372],1],["ImpactPoint",[-0.04,0],1],["ImpactPoint",[-0.039392,-0.00706372],1],["ImpactPoint",[-0.037588,-0.0139159],1],["ImpactPoint",[-0.03464,-0.0203448],1],["ImpactPoint",[-0.03064,-0.0261553],1],["ImpactPoint",[-0.025712,-0.0311683],1],["ImpactPoint",[-0.02,-0.0352372],1],["ImpactPoint",[-0.01368,-0.0382361],1],["ImpactPoint",[-0.006944,-0.0400712],1],["ImpactPoint",[0,-0.0406897],1],[],[],["ImpactPoint",[0,0.005],1],["ImpactPoint",[0.005,-0],1],["ImpactPoint",[0,-0.005],1],["ImpactPoint",[-0.005,-0],1],["ImpactPoint",[0,0.005],1]]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AAMissilesGroup [Indent level: 4],
                "aamissilesgroup": {
                    "type": "group",
                    "condition": "aamissile",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AAMissilesGroup|PPSGroup [Indent level: 5],
                    "ppsgroup": {
                        "condition": "1",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AAMissilesGroup|PPSGroup|GText [Indent level: 6],
                        "gtext": {
                            "type": "text",
                            "source": "static",
                            "text": "ППС",
                            "align": "left",
                            "scale": 1,
                            "pos": [[0.18,0.39],1],
                            "right": [[0.23,0.39],1],
                            "down": [[0.18,0.44],1]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AAMissilesGroup|ZPSGroup [Indent level: 5],
                    "zpsgroup": {
                        "condition": "0",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|AAMissilesGroup|ZPSGroup|GText [Indent level: 6],
                        "gtext": {
                            "text": "ЗПС",
                            "type": "text",
                            "source": "static",
                            "align": "left",
                            "scale": 1,
                            "pos": [[0.18,0.39],1],
                            "right": [[0.23,0.39],1],
                            "down": [[0.18,0.44],1]
                        }
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|TargetDiamond [Indent level: 4],
                "targetdiamond": {
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|TargetDiamond|shape [Indent level: 5]
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0,-0.015],1],["Target",1,"Limit0109",1,[-0.0075,0],1],["Target",1,"Limit0109",1,[0,0.0125],1],["Target",1,"Limit0109",1,[0.0075,0],1],["Target",1,"Limit0109",1,[0,-0.0125],1]]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|TargetLocked [Indent level: 4],
                "targetlocked": {
                    "condition": "TargetHeight>=1",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|TargetLocked|TargetSquare [Indent level: 5],
                    "targetsquare": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0,-0.0508621],1],["Target",1,"Limit0109",1,[0.05,0],1],["Target",1,"Limit0109",1,[0,0.0508621],1],["Target",1,"Limit0109",1,[-0.05,0],1],["Target",1,"Limit0109",1,[0,-0.0508621],1]]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|TargetLocked|TargetSpeed0 [Indent level: 5],
                    "targetspeed0": {
                        "type": "text",
                        "source": "static",
                        "text": 0,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.31,"0.09+0.15"],1],
                        "right": [[0.35,"0.09+0.15"],1],
                        "down": [[0.31,0.285],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|TargetLocked|TargetSpeed [Indent level: 5],
                    "targetspeed": {
                        "source": "LarTargetSpeed",
                        "sourcescale": 0.36,
                        "pos": [[0.29,"0.09+0.15"],1],
                        "right": [[0.33,"0.09+0.15"],1],
                        "down": [[0.29,0.285],1],
                        "type": "text",
                        "text": 0,
                        "align": "left",
                        "scale": 1
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|TargetLocked|TargetHeight0 [Indent level: 5],
                    "targetheight0": {
                        "type": "text",
                        "source": "static",
                        "text": 0,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.82,"0.09+0.15"],1],
                        "right": [[0.86,"0.09+0.15"],1],
                        "down": [[0.82,0.285],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|TargetLocked|TargetHeight [Indent level: 5],
                    "targetheight": {
                        "source": "TargetHeight",
                        "sourcescale": 0.1,
                        "sourcelength": 1,
                        "pos": [[0.8,"0.09+0.15"],1],
                        "right": [[0.84,"0.09+0.15"],1],
                        "down": [[0.8,0.285],1],
                        "type": "text",
                        "text": 0,
                        "align": "left",
                        "scale": 1
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR [Indent level: 4],
                "lar": {
                    "type": "group",
                    "condition": "bomb+mgun+atmissile+aamissile+rocket",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|Lines [Indent level: 5],
                    "lines": {
                        "type": "line",
                        "width": 3,
                        "points": [[[0.24,0.375],1],[[0.26,0.375],1],[[0.26,0.695],1],[[0.24,0.695],1],[],[[0.24,0.631],1],[[0.26,0.631],1],[],[[0.24,0.567],1],[[0.26,0.567],1],[],[[0.24,0.503],1],[[0.26,0.503],1],[],[[0.24,0.439],1],[[0.26,0.439],1],[],["LarTargetDist",-0.32,[0.272,0.707],1],["LarTargetDist",-0.32,[0.26,0.695],1],["LarTargetDist",-0.32,[0.272,0.683],1],["LarTargetDist",-0.32,[0.272,0.692],1],["LarTargetDist",-0.32,[0.282,0.692],1],["LarTargetDist",-0.32,[0.282,0.698],1],["LarTargetDist",-0.32,[0.272,0.698],1],["LarTargetDist",-0.32,[0.272,0.707],1]]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|RadarSearch [Indent level: 5],
                    "radarsearch": {
                        "condition": "activeSensorsOn - missilelocked - missilelocking",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|RadarSearch|Shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 3,
                            "points": [[[0.725,0.375],1],[[0.74,0.375],1],[[0.74,0.695],1],[[0.725,0.695],1],[],[[0.74,0.535],1],[[0.725,0.535],1],[],[[0.76,0.519],1],[[0.76,0.551],1],[],[[0.755,0.5222],1],[[0.74,0.5222],1],[],[[0.74,0.5478],1],[[0.755,0.5478],1],[],[[0.47,0.715],1],[[0.53,0.715],1]]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|RadarSearch|RadarTopText [Indent level: 6],
                        "radartoptext": {
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.96-0.26",0.35625],1],
                            "right": [[0.735,0.35625],1],
                            "down": [["0.96-0.26",0.39125],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|RadarSearch|RadarElevText [Indent level: 6],
                        "radarelevtext": {
                            "type": "text",
                            "source": "static",
                            "text": "0",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["1.035-0.26",0.519],1],
                            "right": [[0.81,0.519],1],
                            "down": [["1.035-0.26",0.554],1]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|Poly [Indent level: 5],
                    "poly": {
                        "type": "polygon",
                        "points": [[["LarAmmoMin",-0.32,[0.261,0.695],1],["LarAmmoMin",-0.32,[0.261,0.7],1],["LarAmmoMin",-0.32,[0.272,0.7],1],["LarAmmoMin",-0.32,[0.272,0.695],1]],[["LarAmmoMin",-0.32,[0.261,0.62],1],["LarAmmoMin",-0.32,[0.261,0.63],1],["LarAmmoMin",-0.32,[0.272,0.63],1],["LarAmmoMin",-0.32,[0.272,0.62],1]],[["LarAmmoMax",-0.32,[0.261,0.785],1],["LarAmmoMax",-0.32,[0.261,0.79],1],["LarAmmoMax",-0.32,[0.272,0.79],1],["LarAmmoMax",-0.32,[0.272,0.785],1]]]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|LARText1 [Indent level: 5],
                    "lartext1": {
                        "type": "text",
                        "source": "LarTop",
                        "sourcescale": "0.001*1.5",
                        "scale": 1,
                        "pos": [[0.235,0.361],1],
                        "right": [[0.27,0.361],1],
                        "down": [[0.235,0.389],1],
                        "align": "left"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|LARText2 [Indent level: 5],
                    "lartext2": {
                        "source": "LarTop",
                        "sourceprecision": -1,
                        "sourcescale": "0.0008*1.5",
                        "pos": [[0.235,0.425],1],
                        "right": [[0.27,0.425],1],
                        "down": [[0.235,0.453],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|LARText3 [Indent level: 5],
                    "lartext3": {
                        "source": "LarTop",
                        "sourceprecision": -1,
                        "sourcescale": "0.0006*1.5",
                        "pos": [[0.235,0.489],1],
                        "right": [[0.27,0.489],1],
                        "down": [[0.235,0.517],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|LARText4 [Indent level: 5],
                    "lartext4": {
                        "source": "LarTop",
                        "sourceprecision": -1,
                        "sourcescale": "0.0004*1.5",
                        "pos": [[0.235,0.553],1],
                        "right": [[0.27,0.553],1],
                        "down": [[0.235,0.581],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|LARText5 [Indent level: 5],
                    "lartext5": {
                        "source": "LarTop",
                        "sourceprecision": -1,
                        "sourcescale": "0.0002*1.5",
                        "pos": [[0.235,0.617],1],
                        "right": [[0.27,0.617],1],
                        "down": [[0.235,0.645],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|LAR|LARText6 [Indent level: 5],
                    "lartext6": {
                        "source": "static",
                        "text": 0,
                        "sourceprecision": -1,
                        "sourcescale": "0.0002*1.5",
                        "pos": [[0.235,0.681],1],
                        "right": [[0.27,0.681],1],
                        "down": [[0.235,0.709],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD|Draw|RadarBoxes [Indent level: 4],
                "radarboxes": {
                    "type": "radar",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12],
                    "width": 4,
                    "points": [[[0,-0.0406897],1],[[0.006944,-0.0400712],1],[[0.01368,-0.0382361],1],[[0.02,-0.0352372],1],[[0.025712,-0.0311683],1],[[0.03064,-0.0261553],1],[[0.03464,-0.0203448],1],[[0.037588,-0.0139159],1],[[0.039392,-0.00706372],1],[[0.04,0],1],[[0.039392,0.00706372],1],[[0.037588,0.0139159],1],[[0.03464,0.0203448],1],[[0.03064,0.0261553],1],[[0.025712,0.0311683],1],[[0.02,0.0352372],1],[[0.01368,0.0382361],1],[[0.006944,0.0400712],1],[[0,0.0406897],1],[[-0.006944,0.0400712],1],[[-0.01368,0.0382361],1],[[-0.02,0.0352372],1],[[-0.025712,0.0311683],1],[[-0.03064,0.0261553],1],[[-0.03464,0.0203448],1],[[-0.037588,0.0139159],1],[[-0.039392,0.00706372],1],[[-0.04,0],1],[[-0.039392,-0.00706372],1],[[-0.037588,-0.0139159],1],[[-0.03464,-0.0203448],1],[[-0.03064,-0.0261553],1],[[-0.025712,-0.0311683],1],[[-0.02,-0.0352372],1],[[-0.01368,-0.0382361],1],[[-0.006944,-0.0400712],1],[[0,-0.0406897],1],[]]
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD_static [Indent level: 2],
        "hud_static": {
            "topleft": "HUD_top_left",
            "topright": "HUD_top_right",
            "bottomleft": "HUD_bottom_left",
            "enableparallax": 1,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_rus",
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD_static|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD_static|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                "condition": "user3*on",
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HUD_static|Draw|Shape [Indent level: 4],
                "shape": {
                    "type": "polygon",
                    "texture": "rhsafrf|addons|rhs_c_a2port_air|Su25|rhs_su25_reticle_static_ca.paa",
                    "points": [[[[0.225,0.415],1],[[0.785,0.415],1],[[0.785,0.915],1],[[0.225,0.915],1]]]
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1 [Indent level: 2],
        "mfd_1": {
            "topleft": "MFD_1_TL",
            "topright": "MFD_1_TR",
            "bottomleft": "MFD_1_BL",
            "enableparallax": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,0,0,0.1],
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Bones|Pylon1 [Indent level: 4]
                "pylon1": {
                    "type": "fixed",
                    "pos": [0.682,0.633577]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Bones|Pylon2 [Indent level: 4],
                "pylon2": {
                    "pos": [0.324,0.633577],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Bones|Pylon3 [Indent level: 4],
                "pylon3": {
                    "pos": [0.789,0.633577],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Bones|Pylon4 [Indent level: 4],
                "pylon4": {
                    "pos": [0.217,0.633577],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Bones|Pylon5 [Indent level: 4],
                "pylon5": {
                    "pos": [0.896,0.633577],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Bones|Pylon6 [Indent level: 4],
                "pylon6": {
                    "pos": [0.11,0.633577],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Bones|Pylon7 [Indent level: 4],
                "pylon7": {
                    "pos": [0.503,0.633577],
                    "type": "fixed"
                }
            },
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 0.22,
                "condition": "on",
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_TV [Indent level: 4],
                "group_tv": {
                    "condition": "user45<=0"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_NAV [Indent level: 4],
                "group_nav": {
                    "condition": "(user45 >= 1)*(user45<=1)"
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP [Indent level: 4],
                "group_weap": {
                    "condition": "(user45 >= 2)*(user45<=2)+1",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|AmmoGunText [Indent level: 5],
                    "ammoguntext": {
                        "type": "text",
                        "source": "static",
                        "text": "ВПУ",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.04,0.15],1],
                        "right": [[0.1,0.15],1],
                        "down": [[0.04,0.21],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|AmmoValue [Indent level: 5],
                    "ammovalue": {
                        "type": "text",
                        "source": "ammo",
                        "sourceindex": 1,
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.04,0.22],1],
                        "right": [[0.1,0.22],1],
                        "down": [[0.04,0.28],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|CMGunText [Indent level: 5],
                    "cmguntext": {
                        "type": "text",
                        "source": "static",
                        "text": "ЛТЦ",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [[0.95,0.15],1],
                        "right": [[1.01,0.15],1],
                        "down": [[0.95,0.21],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|CMValue [Indent level: 5],
                    "cmvalue": {
                        "type": "text",
                        "source": "cmAmmo",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [[0.95,0.22],1],
                        "right": [[1.01,0.22],1],
                        "down": [[0.95,0.28],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon1_empty [Indent level: 5],
                    "pylon1_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty1",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon1_empty|Shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon1",[-0.02,0.0226277],1],["Pylon1",[0.02,-0.0226277],1],[],["Pylon1",[-0.02,-0.0226277],1],["Pylon1",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon2_empty [Indent level: 5],
                    "pylon2_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty2",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon2_empty|Shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon2",[-0.02,0.0226277],1],["Pylon2",[0.02,-0.0226277],1],[],["Pylon2",[-0.02,-0.0226277],1],["Pylon2",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon3_empty [Indent level: 5],
                    "pylon3_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty3",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon3_empty|Shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon3",[-0.02,0.0226277],1],["Pylon3",[0.02,-0.0226277],1],[],["Pylon3",[-0.02,-0.0226277],1],["Pylon3",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon4_empty [Indent level: 5],
                    "pylon4_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty4",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon4_empty|Shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon4",[-0.02,0.0226277],1],["Pylon4",[0.02,-0.0226277],1],[],["Pylon4",[-0.02,-0.0226277],1],["Pylon4",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon5_empty [Indent level: 5],
                    "pylon5_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty5",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon5_empty|Shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon5",[-0.02,0.0226277],1],["Pylon5",[0.02,-0.0226277],1],[],["Pylon5",[-0.02,-0.0226277],1],["Pylon5",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon6_empty [Indent level: 5],
                    "pylon6_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty6",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon6_empty|Shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon6",[-0.02,0.0226277],1],["Pylon6",[0.02,-0.0226277],1],[],["Pylon6",[-0.02,-0.0226277],1],["Pylon6",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon7_empty [Indent level: 5],
                    "pylon7_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty7",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|Pylon7_empty|Shape [Indent level: 6],
                        "shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon7",[-0.02,0.0226277],1],["Pylon7",[0.02,-0.0226277],1],[],["Pylon7",[-0.02,-0.0226277],1],["Pylon7",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|PylonName1 [Indent level: 5],
                    "pylonname1": {
                        "type": "pylonicon",
                        "pos": ["Pylon1",[0,0],1],
                        "pylon": 1,
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|PylonName2 [Indent level: 5],
                    "pylonname2": {
                        "pos": ["Pylon2",[0,0],1],
                        "pylon": 2,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|PylonName3 [Indent level: 5],
                    "pylonname3": {
                        "pos": ["Pylon3",[0,0],1],
                        "pylon": 3,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|PylonName4 [Indent level: 5],
                    "pylonname4": {
                        "pos": ["Pylon4",[0,0],1],
                        "pylon": 4,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|PylonName5 [Indent level: 5],
                    "pylonname5": {
                        "pos": ["Pylon5",[0,0],1],
                        "pylon": 5,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|PylonName6 [Indent level: 5],
                    "pylonname6": {
                        "pos": ["Pylon6",[0,0],1],
                        "pylon": 6,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_1|Draw|Group_WEAP|PylonName7 [Indent level: 5],
                    "pylonname7": {
                        "pos": ["Pylon7",[0,0],1],
                        "pylon": 7,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    }
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2 [Indent level: 2],
        "mfd_2": {
            "topleft": "MFD_2_TL",
            "topright": "MFD_2_TR",
            "bottomleft": "MFD_2_BL",
            "enableparallax": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,0,0,0.1],
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw [Indent level: 3],
            "draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|RadioFQ_1 [Indent level: 4],
                "radiofq_1": {
                    "type": "text",
                    "source": "static",
                    "text": "КСБ 08.125.000.000",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.74,0.1],1],
                    "right": [[0.785,0.1],1],
                    "down": [[0.74,0.145],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|RadioFQ_2 [Indent level: 4],
                "radiofq_2": {
                    "type": "text",
                    "source": "static",
                    "text": "КСД 08.312.522.000",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.74,0.17],1],
                    "right": [[0.785,0.17],1],
                    "down": [[0.74,0.215],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|RadioFQ_3 [Indent level: 4],
                "radiofq_3": {
                    "type": "text",
                    "source": "static",
                    "text": "НВГ 12.541.100.000",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.74,0.28],1],
                    "right": [[0.785,0.28],1],
                    "down": [[0.74,0.325],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|RadioFQ_4 [Indent level: 4],
                "radiofq_4": {
                    "type": "text",
                    "source": "static",
                    "text": "ИРГ 00.101.512.000",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.74,0.35],1],
                    "right": [[0.785,0.35],1],
                    "down": [[0.74,0.395],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|FuelText [Indent level: 4],
                "fueltext": {
                    "type": "text",
                    "source": "static",
                    "text": "ТОПЛИВО",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.04,0.1],1],
                    "right": [[0.085,0.1],1],
                    "down": [[0.04,0.145],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|FuelSource [Indent level: 4],
                "fuelsource": {
                    "type": "text",
                    "source": "fuel",
                    "sourcescale": 4400,
                    "sourceprecision": 0,
                    "sourcelength": 3,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.04,"0.1+0.07"],1],
                    "right": [[0.09,"0.1+0.07"],1],
                    "down": [[0.04,0.22],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|FuelText2 [Indent level: 4],
                "fueltext2": {
                    "type": "text",
                    "source": "static",
                    "text": "Л",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [["0.04+0.11",0.17],1],
                    "right": [[0.195,0.17],1],
                    "down": [["0.04+0.11",0.215],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Time [Indent level: 4],
                "time": {
                    "type": "text",
                    "source": "time",
                    "text": "%X",
                    "sourcescale": 1,
                    "align": "right",
                    "scale": 1,
                    "pos": [["0.04+0.27",0.1],1],
                    "right": [[0.355,0.1],1],
                    "down": [["0.04+0.27",0.145],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Date [Indent level: 4],
                "date": {
                    "text": "%x",
                    "pos": [["0.04+0.27","0.1+0.07"],1],
                    "right": [[0.355,"0.1+0.07"],1],
                    "down": [["0.04+0.27",0.215],1],
                    "type": "text",
                    "source": "time",
                    "sourcescale": 1,
                    "align": "right",
                    "scale": 1
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|NavigationText [Indent level: 4],
                "navigationtext": {
                    "type": "text",
                    "source": "static",
                    "text": "НАВИГАЦИЯ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.04,0.62],1],
                    "right": [[0.1,0.62],1],
                    "down": [[0.04,0.68],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|PositionText [Indent level: 4],
                "positiontext": {
                    "type": "text",
                    "source": "static",
                    "text": "ПОЗИЦИЯ:",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.04,0.69],1],
                    "right": [[0.09,0.69],1],
                    "down": [[0.04,0.74],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|CordX [Indent level: 4],
                "cordx": {
                    "type": "text",
                    "source": "coordinateX",
                    "sourcescale": 0.01,
                    "sourcelength": 3,
                    "sourceoffset": -0.5,
                    "align": "right",
                    "scale": 1,
                    "pos": [["0.04+0.22","0.62+0.07"],1],
                    "right": [[0.31,"0.62+0.07"],1],
                    "down": [["0.04+0.22",0.74],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|CordY [Indent level: 4],
                "cordy": {
                    "source": "coordinateY",
                    "pos": [["0.04+0.22+0.07","0.62+0.07"],1],
                    "right": [[0.38,"0.62+0.07"],1],
                    "down": [["0.04+0.22+0.07",0.74],1],
                    "type": "text",
                    "sourcescale": 0.01,
                    "sourcelength": 3,
                    "sourceoffset": -0.5,
                    "align": "right",
                    "scale": 1
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|ATLText [Indent level: 4],
                "atltext": {
                    "type": "text",
                    "source": "static",
                    "text": "ВЫСОТА:",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [["0.04+0.03",0.76],1],
                    "right": [[0.12,0.76],1],
                    "down": [["0.04+0.03",0.81],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|ATLValue [Indent level: 4],
                "atlvalue": {
                    "type": "text",
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "sourceoffset": -2.1,
                    "align": "right",
                    "scale": 1,
                    "pos": [["0.04+0.22","0.62+0.14"],1],
                    "right": [[0.31,"0.62+0.14"],1],
                    "down": [["0.04+0.22",0.81],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|ATLText2 [Indent level: 4],
                "atltext2": {
                    "type": "text",
                    "source": "static",
                    "text": "м",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [["0.04+0.32",0.77],1],
                    "right": [[0.41,0.77],1],
                    "down": [["0.04+0.32",0.805],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|DirectionText [Indent level: 4],
                "directiontext": {
                    "type": "text",
                    "source": "static",
                    "text": "КУРС:",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [["0.04+0.075",0.83],1],
                    "right": [[0.165,0.83],1],
                    "down": [["0.04+0.075",0.88],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|DirectionValue [Indent level: 4],
                "directionvalue": {
                    "type": "text",
                    "source": "heading",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [["0.04+0.22",0.83],1],
                    "right": [[0.31,0.83],1],
                    "down": [["0.04+0.22",0.88],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Waypoints [Indent level: 4],
                "waypoints": {
                    "condition": "wpvalid",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Waypoints|WPIndexText [Indent level: 5],
                    "wpindextext": {
                        "type": "text",
                        "source": "static",
                        "text": "ИНДЕКС ППМ:",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [["0.84-0.04",0.69],1],
                        "right": [[0.85,0.69],1],
                        "down": [["0.84-0.04",0.74],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Waypoints|WPIndexValue [Indent level: 5],
                    "wpindexvalue": {
                        "type": "text",
                        "source": "wpindex",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [["0.87-0.04",0.69],1],
                        "right": [[0.88,0.69],1],
                        "down": [["0.87-0.04",0.74],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Waypoints|WPDistText [Indent level: 5],
                    "wpdisttext": {
                        "type": "text",
                        "source": "static",
                        "text": "РАССТОЯНИЕ:",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [["0.84-0.04",0.76],1],
                        "right": [[0.85,0.76],1],
                        "down": [["0.84-0.04",0.81],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Waypoints|WPDistText2 [Indent level: 5],
                    "wpdisttext2": {
                        "type": "text",
                        "source": "static",
                        "text": "км",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "pos": [[0.94,0.77],1],
                        "right": [[0.99,0.77],1],
                        "down": [[0.94,0.805],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Waypoints|WPDistValue [Indent level: 5],
                    "wpdistvalue": {
                        "type": "text",
                        "source": "WPDist",
                        "sourcescale": 0.001,
                        "sourcelength": 1,
                        "sourceprecision": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [["0.87-0.04","0.62+0.07*2"],1],
                        "right": [[0.88,"0.62+0.07*2"],1],
                        "down": [["0.87-0.04",0.81],1]
                    },
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Waypoints|Waypoints [Indent level: 5],
                    "waypoints": {
                        "condition": "user40",
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Waypoints|Waypoints|WPHeadingText [Indent level: 6],
                        "wpheadingtext": {
                            "type": "text",
                            "source": "static",
                            "text": "КУРС ДО ППМ:",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "left",
                            "pos": [[0.84,0.83],1],
                            "right": [[0.89,0.83],1],
                            "down": [[0.84,0.88],1]
                        },
                        # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|Waypoints|Waypoints|WPHeadingValue [Indent level: 6],
                        "wpheadingvalue": {
                            "type": "text",
                            "source": "user",
                            "sourceindex": 40,
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "right",
                            "pos": [[0.87,0.83],1],
                            "right": [[0.92,0.83],1],
                            "down": [[0.87,0.88],1]
                        }
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|NoWaypoints [Indent level: 4],
                "nowaypoints": {
                    "condition": "1- wpvalid",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|NoWaypoints|PrevText [Indent level: 5],
                    "prevtext": {
                        "type": "text",
                        "source": "static",
                        "text": "ВЫБЕРИ МАРШРУТ",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.76,0.73],1],
                        "right": [[0.83,0.73],1],
                        "down": [[0.76,0.8],1]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|PrevText [Indent level: 4],
                "prevtext": {
                    "type": "text",
                    "source": "static",
                    "text": "ПОВОРОТ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.02,0.94],1],
                    "right": [[0.07,0.94],1],
                    "down": [[0.02,0.99],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|MinusText [Indent level: 4],
                "minustext": {
                    "type": "text",
                    "source": "static",
                    "text": "-",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.69,0.94],1],
                    "right": [[0.76,0.94],1],
                    "down": [[0.69,1.01],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|MFD_2|Draw|PlusText [Indent level: 4],
                "plustext": {
                    "type": "text",
                    "source": "static",
                    "text": "+",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.9,0.94],1],
                    "right": [[0.97,0.94],1],
                    "down": [[0.9,1.01],1]
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD [Indent level: 2],
        "hmd": {
            "topleft": "HUD_top_left",
            "topright": "HUD_top_right",
            "bottomleft": "HUD_bottom_left",
            "helmetmounteddisplay": 1,
            "helmetposition": [-0.0325,0.0325,0.1],
            "helmetright": [0.065,0,0],
            "helmetdown": [0,-0.065,0],
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_rus",
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.5,0.5],
                    "pos10": [0.774,0.77]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Bones|Target [Indent level: 4],
                "target": {
                    "source": "targettoview",
                    "type": "vector",
                    "pos0": [0.5,0.5],
                    "pos10": [0.774,0.77]
                }
            },
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                "condition": "user2",
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Draw|SearchMode [Indent level: 4],
                "searchmode": {
                    "condition": "1-missileLocked - missileLocking",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Draw|SearchMode|CircleLock [Indent level: 5],
                    "circlelock": {
                        "type": "line",
                        "width": 12,
                        "points": [["PlaneW",[0,-0.0591241],1],["PlaneW",[0.010416,-0.0582254],1],["PlaneW",[0.02052,-0.0555589],1],["PlaneW",[0.03,-0.0512015],1],["PlaneW",[0.038568,-0.0452891],1],["PlaneW",[0.04596,-0.038005],1],["PlaneW",[0.05196,-0.029562],1],["PlaneW",[0.056382,-0.0202204],1],["PlaneW",[0.059088,-0.0102639],1],["PlaneW",[0.06,0],1],["PlaneW",[0.059088,0.0102639],1],["PlaneW",[0.056382,0.0202204],1],["PlaneW",[0.05196,0.029562],1],["PlaneW",[0.04596,0.038005],1],["PlaneW",[0.038568,0.0452891],1],["PlaneW",[0.03,0.0512015],1],["PlaneW",[0.02052,0.0555589],1],["PlaneW",[0.010416,0.0582254],1],["PlaneW",[0,0.0591241],1],["PlaneW",[-0.010416,0.0582254],1],["PlaneW",[-0.02052,0.0555589],1],["PlaneW",[-0.03,0.0512015],1],["PlaneW",[-0.038568,0.0452891],1],["PlaneW",[-0.04596,0.038005],1],["PlaneW",[-0.05196,0.029562],1],["PlaneW",[-0.056382,0.0202204],1],["PlaneW",[-0.059088,0.0102639],1],["PlaneW",[-0.06,0],1],["PlaneW",[-0.059088,-0.0102639],1],["PlaneW",[-0.056382,-0.0202204],1],["PlaneW",[-0.05196,-0.029562],1],["PlaneW",[-0.04596,-0.038005],1],["PlaneW",[-0.038568,-0.0452891],1],["PlaneW",[-0.03,-0.0512015],1],["PlaneW",[-0.02052,-0.0555589],1],["PlaneW",[-0.010416,-0.0582254],1],["PlaneW",[0,-0.0591241],1],[]]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Draw|InvalidLock [Indent level: 4],
                "invalidlock": {
                    "condition": "abs(cameraHeadingDiff) > 70 - missileLocked - missileLocking",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Draw|InvalidLock|CircleLock [Indent level: 5],
                    "circlelock": {
                        "type": "line",
                        "width": 12,
                        "points": [["PlaneW",[-0.0707107,0.0696784],1],["PlaneW",[0.0707107,-0.0696784],1],[],["PlaneW",[-0.0707107,-0.0696784],1],["PlaneW",[0.0707107,0.0696784],1]]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Draw|Locking [Indent level: 4],
                "locking": {
                    "blinkingpattern": [0.2,0.2],
                    "blinkingstartson": 1,
                    "condition": "missileLocking",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Draw|Locking|CircleLock [Indent level: 5],
                    "circlelock": {
                        "type": "line",
                        "width": 12,
                        "points": [["Target",[0,-0.0591241],1],["Target",[0.010416,-0.0582254],1],["Target",[0.02052,-0.0555589],1],["Target",[0.03,-0.0512015],1],["Target",[0.038568,-0.0452891],1],["Target",[0.04596,-0.038005],1],["Target",[0.05196,-0.029562],1],["Target",[0.056382,-0.0202204],1],["Target",[0.059088,-0.0102639],1],["Target",[0.06,0],1],["Target",[0.059088,0.0102639],1],["Target",[0.056382,0.0202204],1],["Target",[0.05196,0.029562],1],["Target",[0.04596,0.038005],1],["Target",[0.038568,0.0452891],1],["Target",[0.03,0.0512015],1],["Target",[0.02052,0.0555589],1],["Target",[0.010416,0.0582254],1],["Target",[0,0.0591241],1],["Target",[-0.010416,0.0582254],1],["Target",[-0.02052,0.0555589],1],["Target",[-0.03,0.0512015],1],["Target",[-0.038568,0.0452891],1],["Target",[-0.04596,0.038005],1],["Target",[-0.05196,0.029562],1],["Target",[-0.056382,0.0202204],1],["Target",[-0.059088,0.0102639],1],["Target",[-0.06,0],1],["Target",[-0.059088,-0.0102639],1],["Target",[-0.056382,-0.0202204],1],["Target",[-0.05196,-0.029562],1],["Target",[-0.04596,-0.038005],1],["Target",[-0.038568,-0.0452891],1],["Target",[-0.03,-0.0512015],1],["Target",[-0.02052,-0.0555589],1],["Target",[-0.010416,-0.0582254],1],["Target",[0,-0.0591241],1],[]]
                    }
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Draw|Locked [Indent level: 4],
                "locked": {
                    "condition": "missileLocked",
                    # Class: CfgVehicles|rhs_mig29sm_base|MFD|HMD|Draw|Locked|CircleLock [Indent level: 5],
                    "circlelock": {
                        "type": "line",
                        "width": 12,
                        "points": [["Target",[0,-0.0591241],1],["Target",[0.010416,-0.0582254],1],["Target",[0.02052,-0.0555589],1],["Target",[0.03,-0.0512015],1],["Target",[0.038568,-0.0452891],1],["Target",[0.04596,-0.038005],1],["Target",[0.05196,-0.029562],1],["Target",[0.056382,-0.0202204],1],["Target",[0.059088,-0.0102639],1],["Target",[0.06,0],1],["Target",[0.059088,0.0102639],1],["Target",[0.056382,0.0202204],1],["Target",[0.05196,0.029562],1],["Target",[0.04596,0.038005],1],["Target",[0.038568,0.0452891],1],["Target",[0.03,0.0512015],1],["Target",[0.02052,0.0555589],1],["Target",[0.010416,0.0582254],1],["Target",[0,0.0591241],1],["Target",[-0.010416,0.0582254],1],["Target",[-0.02052,0.0555589],1],["Target",[-0.03,0.0512015],1],["Target",[-0.038568,0.0452891],1],["Target",[-0.04596,0.038005],1],["Target",[-0.05196,0.029562],1],["Target",[-0.056382,0.0202204],1],["Target",[-0.059088,0.0102639],1],["Target",[-0.06,0],1],["Target",[-0.059088,-0.0102639],1],["Target",[-0.056382,-0.0202204],1],["Target",[-0.05196,-0.029562],1],["Target",[-0.04596,-0.038005],1],["Target",[-0.038568,-0.0452891],1],["Target",[-0.03,-0.0512015],1],["Target",[-0.02052,-0.0555589],1],["Target",[-0.010416,-0.0582254],1],["Target",[0,-0.0591241],1],[]]
                    }
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29sm_base|MFD|CM_Counter [Indent level: 2],
        "cm_counter": {
            "topleft": "MFD_CM_TL",
            "topright": "MFD_CM_TR",
            "bottomleft": "MFD_CM_BL",
            "enableparallax": 0,
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|CM_Counter|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|CM_Counter|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 0.06,
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|CM_Counter|Draw|CMcount [Indent level: 4],
                "cmcount": {
                    "type": "text",
                    "source": "cmammo",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.5,0.2],1],
                    "right": [[0.8,0.2],1],
                    "down": [[0.5,0.7],1]
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29sm_base|MFD|EKRAN [Indent level: 2],
        "ekran": {
            "topleft": "MFD_Ekran_TL",
            "topright": "MFD_Ekran_TR",
            "bottomleft": "MFD_Ekran_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|EKRAN|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|rhs_mig29sm_base|MFD|EKRAN|Draw [Indent level: 3],
            "draw": {
                "color": [0.98,0.63,0],
                "alpha": 0.66,
                "condition": "gmeter>=9",
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|EKRAN|Draw|CMcount [Indent level: 4],
                "cmcount": {
                    "type": "text",
                    "source": "static",
                    "text": "Вибрация",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.5,0.2],1],
                    "right": [[0.7,0.2],1],
                    "down": [[0.5,0.4],1]
                },
                # Class: CfgVehicles|rhs_mig29sm_base|MFD|EKRAN|Draw|WarText2 [Indent level: 4],
                "wartext2": {
                    "type": "text",
                    "source": "static",
                    "text": "двиг.",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.5,0.6],1],
                    "right": [[0.7,0.6],1],
                    "down": [[0.5,0.8],1]
                }
            }
        }
    },
    "picture": "rhsafrf|addons|rhs_mig29|data|ui|picture_mig29s_ca.paa",
    "icon": "rhsafrf|addons|rhs_mig29|data|ui|icon_mig29s_co.paa",
    "mapsize": 20,
    "vehicleclass": "rhs_vehclass_aircraft",
    "destrtype": "DestructWreck",
    "cost": 2e+007,
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "extcameraposition": [0,0,-15],
    "fuelcapacity": 500,
    "canfloat": 0,
    "waterleakiness": 25,
    "waterresistancecoef": 0.004,
    # Class: CfgVehicles|rhs_mig29s_base|Library [Indent level: 1],
    "library": {
        "libenable": 0,
        "libtextdesc": ""
    },
    "irtarget": 1,
    "irtargetsize": 1,
    "irscanground": 1,
    "irscanrangemin": 100,
    "irscanrangemax": 60000,
    "irscantoeyefactor": 2,
    "visualtarget": 1,
    "visualtargetsize": 0.9,
    "radartarget": 1,
    "radartargetsize": 1,
    "receiveremotetargets": 1,
    "reportremotetargets": 1,
    "reportownposition": 1,
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_axisoffsettarget": [0,6.8,-2.04],
    "lesh_wheeloffset": [0,-0.7],
    "selectionfireanim": "",
    "memorypointgun": ["machinegun"],
    "gunbeg": ["muzzle_1"],
    "gunend": ["chamber_1"],
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "gunaimdown": 0,
    "weapons": ["rhs_weap_MASTERSAFE","rhs_weap_GSh301"],
    "magazines": ["rhs_mag_gsh30_mixed_150"],
    "lockdetectionsystem": 8,
    "incommingmissliedetectionsystem": 8,
    "soundlocked": ["|rhsafrf|addons|rhs_mig29|sound|locking",0.000316228,1],
    "soundincommingmissile": ["|rhsafrf|addons|rhs_mig29|sound|incomingmissile",0.8,1],
    "weaponsgroup1": 128,
    "weaponsgroup4": 64,
    "threat": [1,1,1],
    "type": 2,
    "minfiretime": 30,
    "camouflage": 8,
    "audible": 5,
    "accuracy": 0.2,
    "ejectdamagelimit": 1,
    "availableforsupporttypes": ["CAS_Bombing"],
    # Class: CfgVehicles|rhs_mig29s_base|Turrets [Indent level: 1],
    "turrets": {
    },
    # Class: CfgVehicles|rhs_mig29s_base|EjectionSystem [Indent level: 1],
    "ejectionsystem": {
    },
    "armor": 60,
    "damageresistance": 0.00336,
    "armorstructural": 3,
    # Class: CfgVehicles|rhs_mig29s_base|Hitpoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitHull [Indent level: 2]
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
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 0.2,
            "explosionshielding": 0.2,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.7,
            "explosionshielding": 0.65,
            "passthrough": 0.01,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_l",
            "depends": "0"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "armor": 0.7,
            "explosionshielding": 0.65,
            "passthrough": 0.01,
            "minimalhit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_r",
            "depends": "0"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 1.1,
            "explosionshielding": 0.4,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel",
            "visual": "vis_fuel",
            "depends": "0"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitLAileron_link [Indent level: 2],
        "hitlaileron_link": {
            "armor": 0.7,
            "explosionshielding": 0.7,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_l",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitRAileron_link [Indent level: 2],
        "hitraileron_link": {
            "armor": 0.7,
            "explosionshielding": 0.7,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_r",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitLAileron [Indent level: 2],
        "hitlaileron": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "visual": "vis_wing_l",
            "depends": "HitLAileron_link*0.7"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitRAileron [Indent level: 2],
        "hitraileron": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "visual": "vis_wing_r",
            "depends": "HitRAileron_link*0.7"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitControlRear [Indent level: 2],
        "hitcontrolrear": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.04,
            "material": -1,
            "name": "hit_control_rear",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitLCElevator [Indent level: 2],
        "hitlcelevator": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitRElevator [Indent level: 2],
        "hitrelevator": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitLCRudder [Indent level: 2],
        "hitlcrudder": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_rudder_l",
            "visual": "vis_rudder_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitRightRudder [Indent level: 2],
        "hitrightrudder": {
            "armor": 0.2,
            "explosionshielding": 0.3,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_rudder_r",
            "visual": "vis_rudder_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 0.2,
            "explosionshielding": 0.6,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.3,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "depends": "0"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": 0.2,
            "explosionshielding": 0.6,
            "passthrough": 0.01,
            "minimalhit": 0.1,
            "radius": 0.3,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "depends": "0"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|IndicatorEng1 [Indent level: 2],
        "indicatoreng1": {
            "visual": "ind_eng_l_dam",
            "depends": "HitEngine",
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0.01,
            "minimalhit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|IndicatorEng2 [Indent level: 2],
        "indicatoreng2": {
            "visual": "ind_eng_r_dam",
            "depends": "HitEngine2",
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0.01,
            "minimalhit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|IndicatorOil1 [Indent level: 2],
        "indicatoroil1": {
            "visual": "ind_oil_l",
            "depends": "HitLAileron+HitLAileron_link+HitControlRear+HitLCElevator+HitLCRudder",
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0.01,
            "minimalhit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|IndicatorOil2 [Indent level: 2],
        "indicatoroil2": {
            "visual": "ind_oil_r",
            "depends": "HitRAileron+HitRAileron_link+HitControlRear+HitRElevator+HitRightRudder",
            "armor": 999,
            "explosionshielding": 0,
            "passthrough": 0.01,
            "minimalhit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon1 [Indent level: 2],
        "hitpylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon1|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon2 [Indent level: 2],
        "hitpylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon2|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon3 [Indent level: 2],
        "hitpylon3": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_3",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon3|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon3|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon4 [Indent level: 2],
        "hitpylon4": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_4",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon4|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon4|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon5 [Indent level: 2],
        "hitpylon5": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_5",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon5|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon5|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon6 [Indent level: 2],
        "hitpylon6": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_6",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon6|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon6|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon7 [Indent level: 2],
        "hitpylon7": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_7",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon7|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mig29s_base|Hitpoints|HitPylon7|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        }
    },
    "maxspeed": 1300,
    "landingaoa": "5*3.1415/180",
    "landingspeed": 190,
    "stallspeed": 170,
    "stallwarningtreshold": 0.5,
    "wheelsteeringsensitivity": 2,
    "airbrake": 1,
    "airbrakefrictioncoef": 3.3,
    "flaps": 1,
    "flapsfrictioncoef": 0.32,
    "gearsupfrictioncoef": 0.5,
    "airfrictioncoefs0": [0,0,0],
    "airfrictioncoefs1": [0.1,0.5,0.0082],
    "airfrictioncoefs2": [0.001,0.005,7.5e-005],
    "angleofindicence": "1*3.1415/180",
    "envelope": [0,0.02,0.6,1.19,1.45,2.2,2.7,3.1,4.2,4.9,5.1,5,5.6,5.75,5.82,5.9,5.95,6,6.03,6.05,6.07,6.08,6.09,4,1.5],
    "altnoforce": 14000,
    "altfullforce": 6000,
    "thrustcoef": [1.54,1.46,1.37,1.35,1.21,1.17,1.02,0.97,0.92,0.85,0.7,0.3,0,0,0,0],
    "aileronsensitivity": 1.1,
    "aileroncoef": [0,0.15,0.4,0.85,1.2,1.3,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.1,0.6],
    "elevatorsensitivity": 1.6,
    "elevatorcoef": [0,0.2,0.55,0.8,1.02,1.04,1.05,1.06,1.07,1.07,1.06,1.04,1.02,1,0.9,0.6],
    "rudderinfluence": 0.866,
    "ruddercoef": [0,0.6,1,1.5,2,2.2,2.3,2.3,2,1.6,1],
    "aileroncontrolssensitivitycoef": 4,
    "elevatorcontrolssensitivitycoef": 3.5,
    "ruddercontrolssensitivitycoef": 4,
    "draconicforcexcoef": 9,
    "draconicforceycoef": 1.9,
    "draconicforcezcoef": 1,
    "draconictorquexcoef": [4.8,5,5.5,6.2,7,7.7,8.4,10.1,11,12,13],
    "draconictorqueycoef": [12,10,6,2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
    "gearretracting": 1,
    "gearuptime": 4.5,
    "geardowntime": 3,
    "rhs_afterburner_fueldrag": 0.3,
    "category": "Air",
    "driveraction": "rhs_Mig29_Pilot",
    "driverlefthandanimname": "lever_pilot",
    "driverrighthandanimname": "stick_pilot",
    "driverleftleganimname": "pedal_L",
    "driverrightleganimname": "pedal_R",
    "viewdrivershadow": 1,
    "castdrivershadow": 1,
    "haddriver": 1,
    "hasgunner": 0,
    "hascommander": 1,
    "driveriscommander": 1,
    "drivercompartments": 1,
    "headaimdown": 3,
    "camshakecoef": 0.6,
    "headgforceleaningfactor": [0.005,0.001,0.015],
    "attenuationeffecttype": "PlaneAttenuation",
    "insidesoundcoef": 1,
    "soundgetin": ["A3|Sounds_F|vehicles|air|CAS_01|getin_wipeout",1,1,40],
    "soundgetout": ["A3|Sounds_F|air|Plane_Fighter_03|getout",1,1,40],
    "soundengineonint": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_start_int",1,1],
    "soundengineonext": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_start_ext",1.75,1,300],
    "soundengineoffint": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_shut_int",1,1],
    "soundengineoffext": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_shut_ext",1.75,1,300],
    "cabinopensound": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_open_ext",3.16228,1,40],
    "cabinclosesound": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_close_ext",3.16228,1,40],
    "cabinopensoundinternal": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_open_int",10,1,40],
    "cabinclosesoundinternal": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_close_int",10,1,40],
    "soundlandcrash": ["|rhsafrf|addons|rhs_mig29|sound|touch",1,1.1],
    "soundservo": ["|rhsafrf|addons|rhs_mig29|sound|gear",10,0.5],
    "soundgear": ["|rhsafrf|addons|rhs_mig29|sound|gear",10,0.5],
    "sounddammage": ["|rhsafrf|addons|rhs_mig29|sound|warn",0.562341,1],
    "soundgearup": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_gear_up",2.25,1,250],
    "soundgeardown": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_gear_down",2.25,1,250],
    "soundflapsup": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_Flaps_Up",1.5,1,150],
    "soundflapsdown": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_Flaps_Down",1.5,1,150],
    "soundsetsonicboom": ["Plane_Fighter_SonicBoom_SoundSet"],
    # Class: CfgVehicles|rhs_mig29s_base|Sounds [Indent level: 1],
    "sounds": {
        "soundsets": ["Plane_Fighter_02_EngineLowExt_SoundSet","Plane_Fighter_02_EngineHighExt_SoundSet","Plane_Fighter_02_ForsageExt_SoundSet","Plane_Fighter_02_WindNoiseExt_SoundSet","Plane_Fighter_02_EngineExt_Dist_Front_SoundSet","Plane_Fighter_02_EngineExt_Middle_SoundSet","Plane_Fighter_02_EngineExt_Dist_Rear_SoundSet","Plane_Fighter_02_EngineLowInt_SoundSet","Plane_Fighter_02_EngineHighInt_SoundSet","Plane_Fighter_02_ForsageInt_SoundSet","Plane_Fighter_02_WindNoiseInt_SoundSet","Plane_Fighter_02_VelocityInt_SoundSet"],
        # Class: CfgVehicles|rhs_mig29s_base|Sounds|EngineLowOut [Indent level: 2],
        "enginelowout": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|ext",10,1,1600],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "engineOn*camPos*(rpm factor[0.85, 0])"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Sounds|EngineHighOut [Indent level: 2],
        "enginehighout": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|ext",10,1.3,1800],
            "frequency": "1",
            "volume": "engineOn*camPos*(rpm factor[0.55, 1.0])"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Sounds|ForsageOut [Indent level: 2],
        "forsageout": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|ext-aft",3.16228,0.8,2000],
            "frequency": "1",
            "volume": "engineOn*camPos*(thrust factor[0.5, 1.0])",
            "cone": [3.14,3.92,2,0.4]
        },
        # Class: CfgVehicles|rhs_mig29s_base|Sounds|WindNoiseOut [Indent level: 2],
        "windnoiseout": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|ext-wind",1,1,150],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "camPos*(speed factor[1, 150])"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Sounds|EngineLowIn [Indent level: 2],
        "enginelowin": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|int",3.16228,1],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.85, 0]))"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Sounds|EngineHighIn [Indent level: 2],
        "enginehighin": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|int",3.16228,1],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.55, 1.0]))"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Sounds|ForsageIn [Indent level: 2],
        "forsagein": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|int-aft",1.77828,0.8],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.5, 1.0]))"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Sounds|WindNoiseIn [Indent level: 2],
        "windnoisein": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|int-wind",1,1],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "(1-camPos)*(speed factor[1, 150])"
        }
    },
    # Class: CfgVehicles|rhs_mig29s_base|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initfov": 1,
        "minfov": 0.3,
        "maxfov": 1.2,
        "initanglex": 0,
        "minanglex": -65,
        "maxanglex": 85,
        "initangley": 0,
        "minangley": -125,
        "maxangley": 125,
        "minmovex": -0.2,
        "maxmovex": 0.2,
        "minmovey": -0.1,
        "maxmovey": 0.1,
        "minmovez": -0.1,
        "maxmovez": 0.2,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|rhs_mig29s_base|Eventhandlers [Indent level: 1],
    "eventhandlers": {
        "hit": "",
        # Class: CfgVehicles|rhs_mig29s_base|Eventhandlers|RHS_EventHandlers [Indent level: 2],
        "rhs_eventhandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "init": "_this call rhs_fnc_air_init",
            "postinit": "_this call rhs_fnc_reapplyTextures",
            "fired": "[_this select 0,_this select 1,'RHS_Weap_GSh301',1] call rhs_fnc_burstLimiter",
            "getout": "[_this select 0, _this select 2,'rhs_mig29s_canopy'] call rhs_fnc_K36D_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes;"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Eventhandlers|BIS_Randomisation [Indent level: 2],
        "bis_randomisation": {
            "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;}"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    # Class: CfgVehicles|rhs_mig29s_base|Damage [Indent level: 1],
    "damage": {
        "tex": ["rhsafrf|addons|rhs_air|t50|data|afterburner_ca.paa","#(argb,8,8,3)color(0,0,0,0,co)","rhsafrf|addons|rhs_mig29|data|rhs_mig29_warnings_empty_ca.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_warnings_ca.paa"],
        "mat": ["rhsafrf|addons|rhs_mig29|data|mig29s_glass.rvmat","rhsafrf|addons|rhs_mig29|data|mig29s_glass_damage.rvmat","rhsafrf|addons|rhs_mig29|data|mig29s_glass_damage.rvmat","rhsafrf|addons|rhs_mig29|data|skin1.rvmat","rhsafrf|addons|rhs_mig29|data|skin1_damage.rvmat","rhsafrf|addons|rhs_mig29|data|mig29s_destruct.rvmat","rhsafrf|addons|rhs_mig29|data|skin2.rvmat","rhsafrf|addons|rhs_mig29|data|skin2_damage.rvmat","rhsafrf|addons|rhs_mig29|data|mig29s_destruct.rvmat","rhsafrf|addons|rhs_mig29|data|skin3.rvmat","rhsafrf|addons|rhs_mig29|data|skin3_damage.rvmat","rhsafrf|addons|rhs_mig29|data|mig29s_destruct.rvmat"]
    },
    "hiddenselections": ["camo1","camo2","camo3","n1","n2","i1","nt1","nt2","ntt1","ntt2","nts1","nts2","nts3","nts4","nts5","ns1","ns2","ns3","it1","in1","gps_map"],
    # Class: CfgVehicles|rhs_mig29s_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Standard [Indent level: 2]
        "standard": {
            "author": "Red Hammer Studios",
            "displayname": "Blue",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Gray [Indent level: 2],
        "gray": {
            "displayname": "Gray",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_gray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_gray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_gray_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|LightGray [Indent level: 2],
        "lightgray": {
            "displayname": "Light Gray",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_lgray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_lgray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_lgray_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|LightGray2 [Indent level: 2],
        "lightgray2": {
            "displayname": "Light Gray 2",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_lgray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_lgray2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_lgray_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Gray_camo [Indent level: 2],
        "gray_camo": {
            "displayname": "Gray Camo",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_gray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_gray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_gray_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo [Indent level: 2],
        "green_camo": {
            "displayname": "Green Camo 1",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo2 [Indent level: 2],
        "green_camo2": {
            "displayname": "Green Camo 2",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo3 [Indent level: 2],
        "green_camo3": {
            "displayname": "Green Camo 3",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green22_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo4 [Indent level: 2],
        "green_camo4": {
            "displayname": "Green Camo 4",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green23_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo5 [Indent level: 2],
        "green_camo5": {
            "displayname": "Green Camo 5",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green24_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo6 [Indent level: 2],
        "green_camo6": {
            "displayname": "Green Camo 6",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green25_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo7 [Indent level: 2],
        "green_camo7": {
            "displayname": "Green Camo 7",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green3_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green3_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green3_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo_kubinka [Indent level: 2],
        "green_camo_kubinka": {
            "displayname": "Green Camo Kubinka",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green_kubinka.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green_kubinka.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green_kubinka.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo_lipetsk [Indent level: 2],
        "green_camo_lipetsk": {
            "displayname": "Green Camo Lipetsk",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green_lipetsk_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green24_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green_lipetsk_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo_aggressor1 [Indent level: 2],
        "green_camo_aggressor1": {
            "displayname": "Aggressor 1",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green_aggressor1_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green_aggressor1_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|Green_camo_aggressor2 [Indent level: 2],
        "green_camo_aggressor2": {
            "displayname": "Aggressor 2",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green_aggressor2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green_aggressor2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green_aggressor2_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|RHS_SAF_Gray [Indent level: 2],
        "rhs_saf_gray": {
            "displayname": "SAF (Gray)",
            "author": "Red Hammer Studios",
            "textures": ["rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_01_gray_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_02_gray_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_03_gray_co.paa"],
            "factions": ["rhssaf_faction_airforce"]
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|RHS_SAF_Blue [Indent level: 2],
        "rhs_saf_blue": {
            "displayname": "SAF (Blue-Gray)",
            "author": "Red Hammer Studios",
            "textures": ["rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_01_blue_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_02_blue_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_03_blue_co.paa"],
            "factions": ["rhssaf_faction_airforce"]
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|RHS_CDF1 [Indent level: 2],
        "rhs_cdf1": {
            "displayname": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_01_cdf1_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_02_cdf1_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_03_cdf1_co.paa"],
            "factions": ["rhsgref_faction_cdf_air","rhsgref_faction_cdf_air_b"],
            "materials": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_01_cdf1.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_02_cdf1.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_03_cdf1.rvmat"]
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|RHS_CDF2 [Indent level: 2],
        "rhs_cdf2": {
            "displayname": "CDF (Summer)",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_01_cdf2_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_02_cdf2_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_03_cdf2_co.paa"],
            "factions": ["rhsgref_faction_cdf_air","rhsgref_faction_cdf_air_b"]
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|RHS_CDF3 [Indent level: 2],
        "rhs_cdf3": {
            "displayname": "CDF (Winter)",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_01_cdf3_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_02_cdf3_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_03_cdf3_co.paa"],
            "factions": ["rhsgref_faction_cdf_air","rhsgref_faction_cdf_air_b"]
        },
        # Class: CfgVehicles|rhs_mig29s_base|textureSources|RHS_TKA [Indent level: 2],
        "rhs_tka": {
            "displayname": "Takistan",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_01_tka_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_02_tka_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_03_tka_co.paa"],
            "factions": [""]
        }
    },
    # Class: CfgVehicles|rhs_mig29s_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhs_mig29s_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of intake number",
            "tooltip": "Define kind of font that will be drawn on vehicle intake",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', [cRHSAIRMIG29NumberPlaces,cRHSAIRMIG29TailNumberPlaces, cRHSAIRMIG29TailTopNumberPlaces], [_value,_this getVariable ['rhs_decalTailNumber_type',['AviaWhite','AviaYellow','Empty']],['AviaWhite','Empty']]]]] call rhs_fnc_decalsInit}",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|Hidden [Indent level: 4],
                "hidden": {
                    "name": "Hidden",
                    "value": "Empty"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|AviaYellow [Indent level: 4],
                "aviayellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|AviaBlue [Indent level: 4],
                "aviablue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultvalue": "AviaBlue"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|AviaRed [Indent level: 4],
                "aviared": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|AviaWhiteOut [Indent level: 4],
                "aviawhiteout": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|AviaWhite [Indent level: 4],
                "aviawhite": {
                    "name": "Aviation White",
                    "value": "AviaWhite"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|AviaWhiteShadow [Indent level: 4],
                "aviawhiteshadow": {
                    "name": "Aviation White Shadow",
                    "value": "AviaWhiteShadow"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|AviaOrange [Indent level: 4],
                "aviaorange": {
                    "name": "Aviation Orange",
                    "value": "AviaOrange"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|AviaCDF [Indent level: 4],
                "aviacdf": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type [Indent level: 2],
        "rhs_decaltailnumber_type": {
            "displayname": "Define font type of tail number",
            "tooltip": "Define kind of font that will be drawn on vehicle tail",
            "property": "rhs_decalTailNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', [cRHSAIRMIG29NumberPlaces,cRHSAIRMIG29TailNumberPlaces, cRHSAIRMIG29TailTopNumberPlaces], [_this getVariable ['rhs_decalNumber_type',['AviaWhite','AviaRed','AviaBlue','AviaOrange','AviaWhiteShadow']],_value,['AviaWhite','Empty']]]]] call rhs_fnc_decalsInit}",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|Hidden [Indent level: 4],
                "hidden": {
                    "name": "Hidden",
                    "value": "Empty"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|AviaYellow [Indent level: 4],
                "aviayellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|AviaBlue [Indent level: 4],
                "aviablue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultvalue": "AviaBlue"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|AviaRed [Indent level: 4],
                "aviared": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|AviaWhiteOut [Indent level: 4],
                "aviawhiteout": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|AviaWhite [Indent level: 4],
                "aviawhite": {
                    "name": "Aviation White",
                    "value": "AviaWhite"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|AviaWhiteShadow [Indent level: 4],
                "aviawhiteshadow": {
                    "name": "Aviation White Shadow",
                    "value": "AviaWhiteShadow"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|AviaOrange [Indent level: 4],
                "aviaorange": {
                    "name": "Aviation Orange",
                    "value": "AviaOrange"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|AviaCDF [Indent level: 4],
                "aviacdf": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTailNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "displayname": "Set side number",
            "tooltip": "Set side number. 2 numbers are required. Type 0 to hide numbers completly",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "defaultvalue": "-1",
            "typename": "Number",
            "expression": "if(_value >= 0)then{if(_value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRMIG29NumberPlaces;{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRMIG29TailNumberPlaces;{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRMIG29TailTopNumberPlaces}else{[_this, [['Number', [cRHSAIRMIG29NumberPlaces,cRHSAIRMIG29TailNumberPlaces, cRHSAIRMIG29TailTopNumberPlaces], [_this getVariable ['rhs_decalNumber_type',['AviaWhite','AviaRed','AviaBlue','AviaOrange','AviaWhiteShadow']],_this getVariable ['rhs_decalTailNumber_type',['AviaWhite','AviaYellow','Empty']],['AviaWhite','Empty']], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalRoundel [Indent level: 2],
        "rhs_decalroundel": {
            "displayname": "Define Roundel",
            "tooltip": "Define Roundel texture located on the wings and tail.",
            "property": "rhs_decalRoundel",
            "control": "Combo",
            "expression": "if(_value >= 0)then{ [_this, [[ 'Label', cRHSAIRMIG29StarPlaces, 'Aviation', _value ]]] call rhs_fnc_decalsInit};",
            "defaultvalue": "-1",
            "typename": "Number",
            # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalRoundel|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalRoundel|values|Random [Indent level: 4]
                "random": {
                    "name": "Random",
                    "value": -1,
                    "defaultvalue": -1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalRoundel|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalRoundel|values|RU_Star_Old [Indent level: 4],
                "ru_star_old": {
                    "name": "Russia",
                    "value": 2
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalRoundel|values|RU_Star_New2 [Indent level: 4],
                "ru_star_new2": {
                    "name": "Russia (New)",
                    "value": 7
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalRoundel|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "Chernarus",
                    "value": 4
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalRoundel|values|CDF_New [Indent level: 4],
                "cdf_new": {
                    "name": "Chernarus (Gray)",
                    "value": 5
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalRoundel|values|Takistan [Indent level: 4],
                "takistan": {
                    "name": "Takistan",
                    "value": 6
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt [Indent level: 2],
        "rhs_decalnoseart": {
            "displayname": "Define Nose Art",
            "tooltip": "Define Nose Art texture located near the cabin.",
            "property": "rhs_decalNoseArt",
            "control": "Combo",
            "expression": "if(_value >= 0)then{ [_this, [[ 'Label', cRHSAIRMIG29NosePlaces, 'Mig29NoseArt', _value ]]] call rhs_fnc_decalsInit};",
            "defaultvalue": "-1",
            "typename": "Number",
            # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Random [Indent level: 4]
                "random": {
                    "name": "Random",
                    "value": -1,
                    "defaultvalue": -1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|VvsRandom [Indent level: 4],
                "vvsrandom": {
                    "name": "VVS Random",
                    "value": 1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Vmf [Indent level: 4],
                "vmf": {
                    "name": "VMF Flag",
                    "value": 2
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Excellence [Indent level: 4],
                "excellence": {
                    "name": "Aircraft of Excellence",
                    "value": 8
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Mig787 [Indent level: 4],
                "mig787": {
                    "name": "787th IAP (MiG Logo)",
                    "value": 3
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Shark1 [Indent level: 4],
                "shark1": {
                    "name": "Shark Mouth 1",
                    "value": 4
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Shark2 [Indent level: 4],
                "shark2": {
                    "name": "Shark Mouth 2",
                    "value": 5
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Iap33 [Indent level: 4],
                "iap33": {
                    "name": "33rd IAP",
                    "value": 6
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Osad21 [Indent level: 4],
                "osad21": {
                    "name": "21st OSAD",
                    "value": 7
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Iap968 [Indent level: 4],
                "iap968": {
                    "name": "968th IAP",
                    "value": 9
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Iap960 [Indent level: 4],
                "iap960": {
                    "name": "960th IAP",
                    "value": 10
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalNoseArt|values|Gvardiya [Indent level: 4],
                "gvardiya": {
                    "name": "Guards Regiment",
                    "value": 11
                }
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail [Indent level: 2],
        "rhs_decaltail": {
            "displayname": "Define Tail Art",
            "tooltip": "Define tail decal that will be drawn on vehicle",
            "property": "rhs_decalTail",
            "control": "Combo",
            "expression": "if(_value >= 0)then{[_this,[['Label', cRHSAIRMIG29TailPlaces, 'Mig29TailSign',_value]]] call rhs_fnc_decalsInit};",
            "defaultvalue": -1,
            "typename": "Number",
            # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": -1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|VMF [Indent level: 4],
                "vmf": {
                    "name": "VMF Russia",
                    "value": 1,
                    "defaultvalue": 1
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|VVS [Indent level: 4],
                "vvs": {
                    "name": "VVS Russia",
                    "value": 2
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|VvsRandom [Indent level: 4],
                "vvsrandom": {
                    "name": "VVS Random",
                    "value": 3
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|Mary1st [Indent level: 4],
                "mary1st": {
                    "name": "Mary 1st AB Bee",
                    "value": 4
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|Iap33 [Indent level: 4],
                "iap33": {
                    "name": "33rd IAP",
                    "value": 5
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|Iap120 [Indent level: 4],
                "iap120": {
                    "name": "120th IAP",
                    "value": 6
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|Iap404 [Indent level: 4],
                "iap404": {
                    "name": "404th IAP",
                    "value": 7
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|Ab1521 [Indent level: 4],
                "ab1521": {
                    "name": "1521st AB",
                    "value": 8
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|Mig [Indent level: 4],
                "mig": {
                    "name": "787th IAP (MiG Logo)",
                    "value": 9
                },
                # Class: CfgVehicles|rhs_mig29s_base|Attributes|rhs_decalTail|values|Rusavia [Indent level: 4],
                "rusavia": {
                    "name": "787th IAP (Rusavia)",
                    "value": 10
                }
            }
        }
    },
    # Class: CfgVehicles|rhs_mig29s_base|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|rhs_mig29s_base|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|rhs_mig29s_base|compartmentsLights|Comp1|Light_General [Indent level: 3]
            "light_general": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.15,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|rhs_mig29s_base|compartmentsLights|Comp1|Light_General|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.65,
                    "hardlimitend": 0.95
                },
                "point": "light_general"
            }
        }
    },
    # Class: CfgVehicles|rhs_mig29s_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "position": "light_l_source",
            "direction": "light_l_target",
            "hitpoint": "light_l",
            "selection": "light_l",
            "size": 1,
            "brightness": 1,
            "intensity": 5e+006,
            "innerangle": 20,
            "outerangle": 120,
            "conefadecoef": 50,
            "useflare": 0,
            # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Left_flare [Indent level: 2],
        "left_flare": {
            "innerangle": 10,
            "outerangle": 170,
            "useflare": 1,
            "intensity": 111,
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "position": "light_l_source",
            "direction": "light_l_target",
            "hitpoint": "light_l",
            "selection": "light_l",
            "size": 1,
            "brightness": 1,
            "conefadecoef": 50,
            # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "light_r_source",
            "direction": "light_r_target",
            "hitpoint": "light_r",
            "selection": "light_r",
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "size": 1,
            "brightness": 1,
            "intensity": 5e+006,
            "innerangle": 20,
            "outerangle": 120,
            "conefadecoef": 50,
            "useflare": 0,
            # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Right_flare [Indent level: 2],
        "right_flare": {
            "innerangle": 120,
            "outerangle": 170,
            "useflare": 1,
            "intensity": 111,
            "position": "light_r_source",
            "direction": "light_r_target",
            "hitpoint": "light_r",
            "selection": "light_r",
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "size": 1,
            "brightness": 1,
            "conefadecoef": 50,
            # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Center [Indent level: 2],
        "center": {
            "position": "light_f_source",
            "direction": "light_f_target",
            "hitpoint": "light_f",
            "selection": "light_f",
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "size": 1,
            "brightness": 1,
            "intensity": 5e+006,
            "innerangle": 20,
            "outerangle": 120,
            "conefadecoef": 50,
            "useflare": 0,
            # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Center_flare [Indent level: 2],
        "center_flare": {
            "innerangle": 120,
            "outerangle": 170,
            "useflare": 1,
            "intensity": 111,
            "position": "light_f_source",
            "direction": "light_f_target",
            "hitpoint": "light_f",
            "selection": "light_f",
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "size": 1,
            "brightness": 1,
            "conefadecoef": 50,
            # Class: CfgVehicles|rhs_mig29s_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardlimitstart": 0,
                "hardlimitend": 3
            }
        }
    },
    "aggregatereflectors": [["Left"],["Left_flare"],["Right"],["Right_flare"],["Center"],["Center_flare"]],
    # Class: CfgVehicles|rhs_mig29s_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhs_mig29s_base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaust_l_axis_base",
            "direction": "exhaust_l_axis_end",
            "effect": "RHS_ExhaustsEffectPlaneHP",
            "engineindex": 0
        },
        # Class: CfgVehicles|rhs_mig29s_base|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "exhaust_r_axis_base",
            "direction": "exhaust_r_axis_end",
            "effect": "RHS_ExhaustsEffectPlaneHP",
            "engineindex": 1
        }
    },
    # Class: CfgVehicles|rhs_mig29s_base|WingVortices [Indent level: 1],
    "wingvortices": {
        # Class: CfgVehicles|rhs_mig29s_base|WingVortices|WingTipLeft [Indent level: 2]
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "light_nav_left"
        },
        # Class: CfgVehicles|rhs_mig29s_base|WingVortices|WingTipRight [Indent level: 2],
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "light_nav_right"
        },
        # Class: CfgVehicles|rhs_mig29s_base|WingVortices|BodyLeft [Indent level: 2],
        "bodyleft": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles|rhs_mig29s_base|WingVortices|BodyRight [Indent level: 2],
        "bodyright": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_S"
        }
    },
    "maxomega": 2000,
    # Class: CfgVehicles|rhs_mig29s_base|Wheels [Indent level: 1],
    "wheels": {
        "disablewheelswhendestroyed": 1,
        # Class: CfgVehicles|rhs_mig29s_base|Wheels|Wheel_1 [Indent level: 2],
        "wheel_1": {
            "bonename": "fg_damper",
            "steering": 1,
            "side": "left",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "suspforceapppointoffset": "Wheel_1_center",
            "tireforceapppointoffset": "Wheel_1_center",
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "sprungmass": 3966,
            "springstrength": 56600,
            "springdamperrate": 215570,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|rhs_mig29s_base|Wheels|Wheel_1_fake [Indent level: 2],
        "wheel_1_fake": {
            "bonename": "fg_damper",
            "steering": 1,
            "side": "left",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "suspforceapppointoffset": "Wheel_1_center",
            "tireforceapppointoffset": "Wheel_1_center",
            "maxcompression": 0.18,
            "maxdroop": 0.18,
            "sprungmass": 3966,
            "springstrength": 56600,
            "springdamperrate": 215570,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|rhs_mig29s_base|Wheels|Wheel_2 [Indent level: 2],
        "wheel_2": {
            "bonename": "lg_damper",
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "suspforceapppointoffset": "Wheel_2_center",
            "tireforceapppointoffset": "Wheel_2_center",
            "steering": 0,
            "width": 0.28,
            "maxcompression": 0.13,
            "maxdroop": 0.13,
            "sprungmass": 4652,
            "springdamperrate": 220570,
            "springstrength": 151000,
            "side": "left",
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|rhs_mig29s_base|Wheels|Wheel_3 [Indent level: 2],
        "wheel_3": {
            "bonename": "rg_damper",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspforceapppointoffset": "Wheel_3_center",
            "tireforceapppointoffset": "Wheel_3_center",
            "side": "right",
            "steering": 0,
            "width": 0.28,
            "maxcompression": 0.13,
            "maxdroop": 0.13,
            "sprungmass": 4652,
            "springdamperrate": 220570,
            "springstrength": 151000,
            "mass": 150,
            "moi": 40,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 21500,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    # Class: CfgVehicles|rhs_mig29s_base|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|rhs_mig29s_base|MarkerLights|PositionRed [Indent level: 2]
        "positionred": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 500,
            "name": "light_nav_left",
            "drawlight": 1.5,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|rhs_mig29s_base|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|MarkerLights|PositionGreen [Indent level: 2],
        "positiongreen": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "light_nav_right",
            "intensity": 500,
            "drawlight": 1.5,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|rhs_mig29s_base|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|rhs_mig29s_base|MarkerLights|PositionWhite [Indent level: 2],
        "positionwhite": {
            "color": [1,1,1],
            "ambient": [0.08,0.08,0.08],
            "name": "light_nav_back",
            "intensity": 500,
            "drawlight": 1.5,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|rhs_mig29s_base|MarkerLights|PositionRed|Attenuation [Indent level: 3],
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
    # Class: CfgVehicles|rhs_mig29s_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhs_mig29s_base|UserActions|SAFEMODE [Indent level: 2]
        "safemode": {
            "displayname": "<t color='#00FF7F'>MASTERSAFE</t>",
            "condition": "(call rhs_fnc_findPlayer) in this",
            "statement": "(call rhs_fnc_findPlayer) action ['SwitchWeapon', this, (call rhs_fnc_findPlayer), (weapons this) find 'rhs_weap_MASTERSAFE'];",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showwindow": 0,
            "shortcut": "user13",
            "hideonuse": 1
        },
        # Class: CfgVehicles|rhs_mig29s_base|UserActions|FilterOn [Indent level: 2],
        "filteron": {
            "displayname": "Sunfilter on",
            "condition": "(call rhs_fnc_findPlayer) in this && (this animationPhase 'AnimateSunfilter' == 0)",
            "statement": "this animate ['AnimateSunfilter',1];",
            "priority": 0.5,
            "position": "",
            "radius": 10,
            "onlyforplayer": 1,
            "showwindow": 0,
            "shortcut": "user13",
            "hideonuse": 1
        },
        # Class: CfgVehicles|rhs_mig29s_base|UserActions|FilterOff [Indent level: 2],
        "filteroff": {
            "displayname": "Sunfilter off",
            "condition": "(this animationPhase 'AnimateSunfilter' == 1)",
            "statement": "this animate ['AnimateSunfilter',0];",
            "priority": 0.5,
            "position": "",
            "radius": 10,
            "onlyforplayer": 1,
            "showwindow": 0,
            "shortcut": "user13",
            "hideonuse": 1
        },
        # Class: CfgVehicles|rhs_mig29s_base|UserActions|Helmet [Indent level: 2],
        "helmet": {
            "displayname": "Toggle HMD",
            "shortcut": "user14",
            "statement": "if(this getVariable ['rhs_mfd_2',false])then{this setUserMFDvalue [2,0];this setVariable ['rhs_mfd_2',false]}else{this setUserMFDvalue [2,1];this setVariable ['rhs_mfd_2',true]}",
            "condition": "(call rhs_fnc_findPlayer) in this",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showwindow": 0,
            "hideonuse": 1
        },
        # Class: CfgVehicles|rhs_mig29s_base|UserActions|Reticle [Indent level: 2],
        "reticle": {
            "displayname": "<t color='#FBB829'>Toggle reticle</t>",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showwindow": 0,
            "hideonuse": 1,
            "condition": "(call rhs_fnc_findPlayer) in this",
            "shortcut": "user10",
            "statement": "if(((getUserMFDvalue this) select 3) isEqualTo 0)then{this setUserMFDvalue [3,1];}else{this setUserMFDvalue [3,0];}"
        },
        # Class: CfgVehicles|rhs_mig29s_base|UserActions|Mirrors [Indent level: 2],
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
            "statement": "this animateSource ['fold_mirrors',abs((this animationSourcePhase 'fold_mirrors') -1)]"
        }
    },
    # Class: CfgVehicles|rhs_mig29s_base|RenderTargets [Indent level: 1],
    "rendertargets": {
        # Class: CfgVehicles|rhs_mig29s_base|RenderTargets|Mirror [Indent level: 2]
        "mirror": {
            "rendertarget": "rendertarget0",
            # Class: CfgVehicles|rhs_mig29s_base|RenderTargets|Mirror|CameraView1 [Indent level: 3],
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
    "defaultusermfdstrings": ["rhsafrf|addons|rhs_c_a2port_air|Su25|rhs_su25_reticle_static_ca.paa"],
    "_generalmacro": "Plane_Base_F",
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "waterlineardampingcoefy": 0,
    "waterlineardampingcoefx": 5,
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
    # Class: CfgVehicles|Plane_Base_F|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|Plane_Base_F|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 4
        },
        # Class: CfgVehicles|Plane_Base_F|TransportItems|_xx_ItemGPS [Indent level: 2],
        "_xx_itemgps": {
            "name": "ItemGPS",
            "count": 1
        },
        # Class: CfgVehicles|Plane_Base_F|TransportItems|_xx_ItemRadio [Indent level: 2],
        "_xx_itemradio": {
            "name": "ItemRadio",
            "count": 1
        }
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
    "brakedistance": 500,
    "steeraheadsimul": 1,
    "steeraheadplan": 2,
    "cabinopening": 1,
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "vtol": 0,
    "tailhook": 0,
    "lightongear": 1,
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
    "memorypointlrocket": "L raketa",
    "memorypointrrocket": "P raketa",
    "memorypointldust": "levy prach",
    "memorypointrdust": "pravy prach",
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
    "fuelexplosionpower": 10,
    "epeimpulsedamagecoef": 10,
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
    "mintotaldamagethreshold": 0.005,
    # Class: CfgVehicles|Plane|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "formationtime": 10,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "nightvision": 0,
    "cargocompartments": [0],
    "typicalcargo": ["Soldier"],
    "enablegps": 1,
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
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
    "radartype": 4,
    "incomingmissiledetectionsystem": "8 + 16",
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
    "memorypointtaskmarker": "",
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
    "precisegetinout": 0,
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
    "armorlights": 0.4,
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
    "soundwatercrash": ["",0.177828,1],
    "soundelevation": ["",0.00316228,0.5],
    "sounddamage": ["",1,1],
    "soundcrashes": ["soundCrash",1],
    "soundlandcrashes": ["soundLandCrash",1],
    "soundwatercrashes": ["soundWaterCrash",1],
    "emptysound": ["",0,1],
    "soundwoodcrash": ["emptySound",0],
    "soundbushcrash": ["emptySound",0],
    "soundbuildingcrash": ["emptySound",0],
    "soundarmorcrash": ["emptySound",0],
    "driverinaction": "",
    "cargoaction": [],
    "cargoiscodriver": [0],
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "hideproxyincombat": 0,
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castcargoshadow": 0,
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
    "selectiondamage": "zbytek",
    "cargocaneject": 1,
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