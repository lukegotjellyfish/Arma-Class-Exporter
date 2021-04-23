rhs_ka52_upk23_vvs = {
    "editorpreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_Ka52_UPK23_vvs.paa",
    "author": "Red Hammer Studios",
    "scope": 1,
    "scopecurator": 2,
    "displayname": "Ka-52 (UPK)",
    # Class: CfgVehicles|RHS_Ka52_UPK23_vvs|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|RHS_Ka52_UPK23_vvs|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            # Class: CfgVehicles|RHS_Ka52_UPK23_vvs|Components|TransportPylonsComponent|pylons [Indent level: 3]
            "pylons": {
                # Class: CfgVehicles|RHS_Ka52_UPK23_vvs|Components|TransportPylonsComponent|pylons|pylon1 [Indent level: 4]
                "pylon1": {
                    "attachment": "rhs_mag_upk23_ka52_mixed",
                    "turret": [],
                    "hardpoints": ["RHS_HP_FAB250_KA52","RHS_HP_FAB500_KA52","RHS_HP_KMGU2_KA52","RHS_HP_B13L1_KA52","RHS_HP_B8V20_KA52","RHS_HP_UB16_KA52","RHS_HP_UB32_KA52","RHS_HP_UPK23_KA52"],
                    "priority": 1,
                    "maxweight": 650,
                    "uiposition": [0.504,0.4],
                    "hitpoint": "HitPylon1"
                },
                # Class: CfgVehicles|RHS_Ka52_UPK23_vvs|Components|TransportPylonsComponent|pylons|pylon2 [Indent level: 4],
                "pylon2": {
                    "attachment": "rhs_mag_upk23_ka52_mixed",
                    "turret": [],
                    "uiposition": [0.165,0.4],
                    "mirroredmissilepos": 1,
                    "hitpoint": "HitPylon2",
                    "hardpoints": ["RHS_HP_FAB250_KA52","RHS_HP_FAB500_KA52","RHS_HP_KMGU2_KA52","RHS_HP_B13L1_KA52","RHS_HP_B8V20_KA52","RHS_HP_UB16_KA52","RHS_HP_UB32_KA52","RHS_HP_UPK23_KA52"],
                    "priority": 1,
                    "maxweight": 650
                },
                # Class: CfgVehicles|RHS_Ka52_UPK23_vvs|Components|TransportPylonsComponent|pylons|pylon3 [Indent level: 4],
                "pylon3": {
                    "attachment": "rhs_mag_apu6_9m127m_ka52",
                    "turret": [0],
                    "hardpoints": ["RHS_HP_FAB250","RHS_HP_B13L1_KA52","RHS_HP_B8V20_KA52","RHS_HP_UB16_KA52","RHS_HP_UB32_KA52","RHS_HP_UPK23_KA52","RHS_HP_APU6_9m127_KA52"],
                    "maxweight": 450,
                    "priority": 2,
                    "uiposition": [0.584,0.35],
                    "hitpoint": "HitPylon3"
                },
                # Class: CfgVehicles|RHS_Ka52_UPK23_vvs|Components|TransportPylonsComponent|pylons|pylon4 [Indent level: 4],
                "pylon4": {
                    "attachment": "rhs_mag_apu6_9m127m_ka52",
                    "turret": [0],
                    "uiposition": [0.085,0.35],
                    "mirroredmissilepos": 3,
                    "hitpoint": "HitPylon4",
                    "hardpoints": ["RHS_HP_FAB250","RHS_HP_B13L1_KA52","RHS_HP_B8V20_KA52","RHS_HP_UB16_KA52","RHS_HP_UB32_KA52","RHS_HP_UPK23_KA52","RHS_HP_APU6_9m127_KA52"],
                    "maxweight": 450,
                    "priority": 2
                },
                # Class: CfgVehicles|RHS_Ka52_UPK23_vvs|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4],
                "cmdispenser": {
                    "hardpoints": ["RHS_cm_UV26","RHS_cm_UV26_x2","RHS_cm_UV26_x4"],
                    "priority": 1,
                    "attachment": "rhs_UV26_CMFlare_Chaff_Magazine_x4",
                    "maxweight": 800,
                    "uiposition": [0.33,0]
                }
            },
            "uipicture": "rhsafrf|addons|rhs_a2port_air|data|loadouts|RHS_Ka52_EDEN_CA.paa",
            # Class: CfgVehicles|RHS_Ka52_base|Components|TransportPylonsComponent|Presets [Indent level: 3],
            "presets": {
                # Class: CfgVehicles|RHS_Ka52_base|Components|TransportPylonsComponent|Presets|Bomb [Indent level: 4]
                "bomb": {
                    "attachment": ["rhs_mag_fab250_ka52","rhs_mag_fab250_ka52","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Bomb"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|TransportPylonsComponent|Presets|ClusterMine [Indent level: 4],
                "clustermine": {
                    "attachment": ["rhs_mag_kmgu2_pfm1_ka52","rhs_mag_kmgu2_pfm1_ka52","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "KMGU-2 (AP Mines)"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|TransportPylonsComponent|Presets|ClusterHE [Indent level: 4],
                "clusterhe": {
                    "attachment": ["rhs_mag_kmgu2_ao25_ka52","rhs_mag_kmgu2_ao25_ka52","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "KMGU-2 (HE)"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|TransportPylonsComponent|Presets|UPK [Indent level: 4],
                "upk": {
                    "attachment": ["rhs_mag_upk23_ka52_mixed","rhs_mag_upk23_ka52_mixed","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "UPK-23-250"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|TransportPylonsComponent|Presets|CAS [Indent level: 4],
                "cas": {
                    "attachment": ["rhs_mag_b8v20a_ka52_s8kom","rhs_mag_b8v20a_ka52_s8kom","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Close Air Support"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|TransportPylonsComponent|Presets|HeavyCAS [Indent level: 4],
                "heavycas": {
                    "attachment": ["rhs_mag_b13l1_ka52_s13b","rhs_mag_b13l1_ka52_s13b","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Close Air Support (S-13)"
                }
            }
        },
        # Class: CfgVehicles|RHS_Ka52_base|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|RHS_Ka52_base|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_Ka52_base|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4]
                "lasersensorcomponent": {
                    # Class: CfgVehicles|RHS_Ka52_base|Components|SensorsManagerComponent|Components|LaserSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 9000,
                        "maxrange": 9000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|RHS_Ka52_base|Components|SensorsManagerComponent|Components|LaserSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 9000,
                        "maxrange": 9000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 75,
                    "anglerangevertical": 75,
                    "typerecognitiondistance": -1,
                    "maxgroundnoisedistance": 0,
                    "maxfogseethrough": 0.3,
                    "animdirection": "mainGun",
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
                # Class: CfgVehicles|RHS_Ka52_base|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4],
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
                # Class: CfgVehicles|RHS_Ka52_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent [Indent level: 4],
                "activeradarsensorcomponent": {
                    # Class: CfgVehicles|RHS_Ka52_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 11000,
                        "maxrange": 11000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|RHS_Ka52_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 11000,
                        "maxrange": 11000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 120,
                    "anglerangevertical": 100,
                    "typerecognitiondistance": 4000,
                    "maxfogseethrough": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "maxtrackablespeed": 125,
                    "componenttype": "ActiveRadarSensorComponent",
                    "color": [0,1,1,1],
                    "allowsmarking": 1,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|SensorsManagerComponent|Components|DataLinkSensorComponent [Indent level: 4],
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
        # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|UAVDisplay [Indent level: 4],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [8000,16000,24000,4000],
                    "resource": "RscCustomInfoSensors"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
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
        # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 4],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|UAVDisplay [Indent level: 4],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [8000,16000,24000,4000],
                    "resource": "RscCustomInfoSensors"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
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
    "faction": "rhs_faction_vvs",
    "availableforsupporttypes": ["CAS_Heli"],
    "accuracy": 0.5,
    "hiddenselectionstextures": ["|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01_co.paa","|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02_co.paa","a3|data_f|clear_empty.paa","a3|data_f|clear_empty.paa","rhsafrf|addons|rhs_decals|data|labels|aviation|vvs_ca.paa","|rhsafrf|addons|rhs_a2port_air|Ka52|Data|rhs_ka52_samshin_wfov.paa"],
    "dlc": "RHS_AFRF",
    "rhs_decalparameters": ["['Number',cRHSAIRKA52NumberPlaces,'AviaYellow']"],
    "category": "Air",
    # Class: CfgVehicles|RHS_Ka52_base|RotorLibHelicopterProperties [Indent level: 1],
    "rotorlibhelicopterproperties": {
        "rtdconfig": "rhsafrf|addons|rhs_c_a2port_air|ka52|RTD_Heli_Attack_02.xml",
        "autohovercorrection": [3.2,0,0],
        "defaultcollective": 0.805,
        "retreatbladestallwarningspeed": 83,
        "maxtorque": 3300,
        "stressdamagepersec": 0.01,
        "maxhorizontalstabilizerleftstress": 8000,
        "maxhorizontalstabilizerrightstress": 8000,
        "maxverticalstabilizerstress": 4000,
        "horizontalwingsanglecollmin": 0,
        "horizontalwingsanglecollmax": 0,
        "maxmainrotorstress": 225000,
        "maxtailrotorstress": 225000
    },
    "numberphysicalwheels": 3,
    "maxspeed": 395,
    "bodyfrictioncoef": 0.426,
    "liftforcecoef": 6,
    "cyclicforwardforcecoef": 1,
    "backrotorforcecoef": 1.35,
    "maxmainrotordive": 7,
    "minmainrotordive": -7,
    "neutralmainrotordive": 0,
    "gearretracting": 1,
    "mainrotorspeed": 1,
    "backrotorspeed": 1,
    "mainbladeradius": 6.9,
    "tailbladeradius": 6.9,
    "tailbladecenter": "tail_blade_center",
    "mainbladecenter": "main_blade_center",
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_axisoffsettarget": [0,6.5,-1.05],
    "lesh_wheeloffset": [0,-1],
    "side": 0,
    "crew": "rhs_pilot_combat_heli",
    "typicalcargo": ["rhs_pilot_combat_heli"],
    "fuelcapacity": 1870,
    "rhs_fuelcapacity": 1870,
    "drivercaneject": 1,
    "drivercompartments": 1,
    "ejectspeed": [1,0,11],
    "destrtype": "DestructWreck",
    "vehicleclass": "rhs_vehclass_helicopter",
    "editorsubcategory": "rhs_EdSubcat_helicopter",
    "model": "rhsafrf|addons|rhs_a2port_air|ka52|KA52.p3d",
    "icon": "rhsafrf|addons|rhs_a2port_air|data|map_ico|Icon_ka52_CA.paa",
    "picture": "rhsafrf|addons|rhs_a2port_air|data|ico|rhs_ka52_pic_ca.paa",
    "mapsize": 15,
    "castdrivershadow": 1,
    "viewcargoshadow": 1,
    "camshakecoef": 0.8,
    "transportsoldier": 0,
    "driverdoor": "DoorL",
    "driverlefthandanimname": "lever_pilot",
    "driverrighthandanimname": "stick_pilot",
    "driveoncomponent": ["F_gear_d3","L_gear_d3","R_gear_d3"],
    "getinradius": 1.5,
    "precisegetinout": 1,
    "memorypointsgetindriverprecise": "pos driver",
    "getinaction": "Heli_Attack_01_Pilot_Enter",
    "getoutaction": "Heli_Attack_01_Pilot_Exit",
    "selectionhrotorstill": "velka vrtule staticka",
    "selectionhrotormove": "velka vrtule blur",
    "selectionvrotorstill": "mala vrtule staticka",
    "selectionvrotormove": "mala vrtule blur",
    "memorypointlrocket": "l raketa",
    "memorypointrrocket": "p raketa",
    "memorypointlmissile": "l strela",
    "memorypointrmissile": "p strela",
    "memorypointgun": ["chase01","chase02","chase03","chase04"],
    "gunbeg": ["chase01dir","chase02dir","chase03dir","chase04dir"],
    "gunend": ["chase01","chase02","chase03","chase04"],
    # Class: CfgVehicles|RHS_Ka52_base|PilotCamera [Indent level: 1],
    "pilotcamera": {
    },
    "unitinfotype": "RHS_RscUnitInfoAir_Ka52",
    "receiveremotetargets": 1,
    "reportremotetargets": 1,
    "reportownposition": 1,
    "irtarget": 1,
    "irtargetsize": 0.9,
    "visualtarget": 1,
    "visualtargetsize": 0.9,
    "radartarget": 1,
    "radartargetsize": 1,
    "threat": [0.6,1,0.8],
    "weapons": ["rhs_weap_MASTERSAFE","rhs_weap_DIRCM_Vitebsk"],
    "magazines": ["rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk"],
    "weaponsgroup1": 128,
    "weaponsgroup4": 64,
    "driveraction": "RHS_KA52_Pilot",
    "driverinaction": "RHS_KA52_Pilot",
    "armor": 45,
    "armorstructural": 20,
    "damageresistance": 0.00555,
    "hulldamagecauseexplosion": 1,
    "epeimpulsedamagecoef": 1,
    "hullexplosiondelay": [10,20],
    # Class: CfgVehicles|RHS_Ka52_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "simulation": "RHS_Hull_Helicopter",
            "armor": -150,
            "minimalhit": -0.2,
            "radius": 0.1,
            "name": "hull_hit",
            "armorcomponent": "Hit_Hull",
            "visual": "zbytek",
            "passthrough": 1,
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitHull|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Smoke [Indent level: 0]
                "rhs_hull_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Fire [Indent level: 0],
                "rhs_hull_fire": {
                    "type": "MediumDestructionFire",
                    "simulation": "particles",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Sparks [Indent level: 0],
                "rhs_hull_sparks": {
                    "type": "AirFireSparks",
                    "simulation": "particles",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Sounds [Indent level: 0],
                "rhs_hull_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "hull_fire_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Smoke_small1 [Indent level: 0],
                "rhs_hull_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "hull_fire_2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Smoke_small2 [Indent level: 0],
                "rhs_hull_smoke_small2": {
                    "position": "hull_fire_3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Fire_2 [Indent level: 0],
                "rhs_hull_fire_2": {
                    "type": "MediumDestructionFire",
                    "position": "hull_fire_2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: RHS_Effects_Helicopter_Hull_Destruction|RHS_Hull_Fire_3 [Indent level: 0],
                "rhs_hull_fire_3": {
                    "type": "MediumDestructionFire",
                    "position": "hull_fire_3",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1
            },
            "depends": "Total",
            "convexcomponent": "hull_hit",
            "explosionshielding": 1,
            "material": 51
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitHRotor [Indent level: 2],
        "hithrotor": {
            "armor": 0.3,
            "radius": 0.4,
            "minimalhit": 0.1,
            "explosionshielding": 2,
            "name": "main_rotor_hit",
            "convexcomponent": "main_rotor_hit",
            "visual": "main rotor static",
            "material": 51,
            "passthrough": 0.1
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 3,
            "name": "glass1",
            "visual": "glass1",
            "radius": 0.2,
            "explosionshielding": 2,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": 3,
            "name": "glass2",
            "visual": "glass2",
            "radius": 0.35,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "armor": 1,
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass6 [Indent level: 4],
                "brokenglass6": {
                    "simulation": "particles",
                    "type": "BrokenGlass6N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass7 [Indent level: 4],
                "brokenglass7": {
                    "simulation": "particles",
                    "type": "BrokenGlass7N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass6S [Indent level: 4],
                "brokenglass6s": {
                    "simulation": "particles",
                    "type": "BrokenGlass6S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|BrokenGlass7S [Indent level: 4],
                "brokenglass7s": {
                    "simulation": "particles",
                    "type": "BrokenGlass7S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "glass3_effect",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "glass3_effect",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass3|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "glass3_effect",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                }
            },
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "armor": 1,
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass6 [Indent level: 4],
                "brokenglass6": {
                    "simulation": "particles",
                    "type": "BrokenGlass6N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass7 [Indent level: 4],
                "brokenglass7": {
                    "simulation": "particles",
                    "type": "BrokenGlass7N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass6S [Indent level: 4],
                "brokenglass6s": {
                    "simulation": "particles",
                    "type": "BrokenGlass6S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|BrokenGlass7S [Indent level: 4],
                "brokenglass7s": {
                    "simulation": "particles",
                    "type": "BrokenGlass7S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "glass4_effect",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "glass4_effect",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitGlass4|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "glass4_effect",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                }
            },
            "name": "glass4",
            "visual": "glass4",
            "radius": 0.22,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor1 [Indent level: 2],
        "hitrotor1": {
            "armor": 1,
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor1|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "rotor1_pos",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor1|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "rotor1_pos",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor1|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "rotor1_pos",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                }
            },
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor2 [Indent level: 2],
        "hitrotor2": {
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor2|DestructionEffects [Indent level: 3]
            "destructioneffects": {
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor2|DestructionEffects|RHS_ERA_Flash [Indent level: 4]
                "rhs_era_flash": {
                    "position": "rotor2_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor2|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "position": "rotor2_pos",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor2|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "position": "rotor2_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                "ammoexplosioneffect": ""
            },
            "armor": 1,
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor3 [Indent level: 2],
        "hitrotor3": {
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor3|DestructionEffects [Indent level: 3]
            "destructioneffects": {
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor3|DestructionEffects|RHS_ERA_Flash [Indent level: 4]
                "rhs_era_flash": {
                    "position": "rotor3_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor3|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "position": "rotor3_pos",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor3|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "position": "rotor3_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                "ammoexplosioneffect": ""
            },
            "armor": 1,
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor4 [Indent level: 2],
        "hitrotor4": {
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor4|DestructionEffects [Indent level: 3]
            "destructioneffects": {
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor4|DestructionEffects|RHS_ERA_Flash [Indent level: 4]
                "rhs_era_flash": {
                    "position": "rotor4_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor4|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "position": "rotor4_pos",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor4|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "position": "rotor4_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                "ammoexplosioneffect": ""
            },
            "armor": 1,
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor5 [Indent level: 2],
        "hitrotor5": {
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor5|DestructionEffects [Indent level: 3]
            "destructioneffects": {
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor5|DestructionEffects|RHS_ERA_Flash [Indent level: 4]
                "rhs_era_flash": {
                    "position": "rotor5_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor5|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "position": "rotor5_pos",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor5|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "position": "rotor5_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                "ammoexplosioneffect": ""
            },
            "armor": 1,
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor6 [Indent level: 2],
        "hitrotor6": {
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor6|DestructionEffects [Indent level: 3]
            "destructioneffects": {
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor6|DestructionEffects|RHS_ERA_Flash [Indent level: 4]
                "rhs_era_flash": {
                    "position": "rotor6_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor6|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "position": "rotor6_pos",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitRotor6|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "position": "rotor6_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                "ammoexplosioneffect": ""
            },
            "armor": 1,
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon1 [Indent level: 2],
        "hitpylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon2 [Indent level: 2],
        "hitpylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon3 [Indent level: 2],
        "hitpylon3": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_3",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon3|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon4 [Indent level: 2],
        "hitpylon4": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_4",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon4|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_Ka52_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 2,
            "radius": 0.125,
            "minimalhit": 0.05,
            "explosionshielding": 2,
            "name": "fuel_hit",
            "convexcomponent": "fuel_hit",
            "visual": "zbytek",
            "material": 51,
            "passthrough": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 1.5,
            "radius": 0.4,
            "minimalhit": 0.15,
            "explosionshielding": 1.5,
            "visual": "podsvit pristroju",
            "name": "avionics_hit",
            "convexcomponent": "avionics_hit",
            "material": 51,
            "passthrough": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitEngine1 [Indent level: 2],
        "hitengine1": {
            "armor": 3,
            "radius": 0.35,
            "name": "engine_1_hit",
            "explosionshielding": 3,
            "minimalhit": 0.1,
            "visual": "motor",
            "passthrough": 1,
            "convexcomponent": "engine_1_hit",
            "material": 51
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "name": "engine_2_hit",
            "convexcomponent": "engine_2_hit",
            "armor": 3,
            "radius": 0.35,
            "explosionshielding": 3,
            "minimalhit": 0.1,
            "visual": "motor",
            "passthrough": 1,
            "material": 51
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 999,
            "radius": 0.05,
            "minimalhit": 1,
            "visual": "camo2",
            "depends": "0.5 * (HitEngine1 + HitEngine2)",
            "name": "engine_hit",
            "convexcomponent": "engine_hit",
            "explosionshielding": 1,
            "material": 51,
            "passthrough": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitVRotor [Indent level: 2],
        "hitvrotor": {
            "armor": 2.6,
            "radius": 0.4,
            "minimalhit": 0.1,
            "explosionshielding": 2,
            "name": "tail_rotor_hit",
            "convexcomponent": "tail_rotor_hit",
            "visual": "tail rotor static",
            "material": 51,
            "passthrough": 0.3
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "name": "glass7",
            "visual": "glass7",
            "radius": 0.35,
            "armor": 3,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "name": "glass5",
            "visual": "glass5",
            "radius": 0.25,
            "armor": 4.5,
            "explosionshielding": 2,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "name": "glass6",
            "visual": "glass6",
            "radius": 0.18,
            "armor": 3,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass8 [Indent level: 2],
        "hitglass8": {
            "name": "glass8",
            "visual": "glass8",
            "radius": 0.34,
            "armor": 3,
            "explosionshielding": 1.5,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass9 [Indent level: 2],
        "hitglass9": {
            "name": "glass9",
            "visual": "glass9",
            "radius": 0.24,
            "armor": 0.8,
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass10 [Indent level: 2],
        "hitglass10": {
            "name": "glass10",
            "visual": "glass10",
            "radius": 0.24,
            "armor": 0.8,
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass11 [Indent level: 2],
        "hitglass11": {
            "name": "glass11",
            "visual": "glass11",
            "radius": 0.24,
            "armor": 0.8,
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass12 [Indent level: 2],
        "hitglass12": {
            "name": "glass12",
            "visual": "glass12",
            "radius": 0.24,
            "armor": 0.8,
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass13 [Indent level: 2],
        "hitglass13": {
            "name": "glass13",
            "visual": "glass13",
            "radius": 0.24,
            "armor": 0.8,
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass14 [Indent level: 2],
        "hitglass14": {
            "name": "glass14",
            "visual": "glass14",
            "radius": 0.24,
            "armor": 0.8,
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitGlass15 [Indent level: 2],
        "hitglass15": {
            "name": "glass15",
            "visual": "glass15",
            "radius": 0.24,
            "armor": 0.8,
            "explosionshielding": 1,
            "minimalhit": 0.05,
            "material": -1,
            "convexcomponent": "glass1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitWinch [Indent level: 2],
        "hitwinch": {
            # Class: CfgVehicles|Heli_Attack_02_base_F|HitPoints|HitWinch|DestructionEffects [Indent level: 3]
            "destructioneffects": {
            },
            "armor": -40,
            "material": 51,
            "name": "slingLoad0",
            "visual": "",
            "passthrough": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles|Helicopter_Base_F|HitPoints|HitMissiles [Indent level: 2],
        "hitmissiles": {
            "name": "ammo_hit",
            "convexcomponent": "ammo_hit",
            "explosionshielding": 1,
            "armor": 0.1,
            "material": 51,
            "visual": "munice",
            "passthrough": 0.5
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitRGlass [Indent level: 2],
        "hitrglass": {
            "convexcomponent": "sklo predni P",
            "explosionshielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni P",
            "visual": "sklo predni P",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitLGlass [Indent level: 2],
        "hitlglass": {
            "convexcomponent": "sklo predni L",
            "explosionshielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni L",
            "visual": "sklo predni L",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitEngine3 [Indent level: 2],
        "hitengine3": {
            "name": "engine_3_hit",
            "convexcomponent": "engine_3_hit",
            "explosionshielding": 1,
            "armor": 0.25,
            "material": 51,
            "visual": "motor",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitTransmission [Indent level: 2],
        "hittransmission": {
            "armor": 0.8,
            "material": -1,
            "name": "transmission",
            "passthrough": 0.8
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitLight [Indent level: 2],
        "hitlight": {
            "armor": 0.1,
            "material": -1,
            "name": "light",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitHydraulics [Indent level: 2],
        "hithydraulics": {
            "armor": 0.8,
            "material": -1,
            "name": "hydraulics",
            "passthrough": 0.8
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitGear [Indent level: 2],
        "hitgear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitHStabilizerL1 [Indent level: 2],
        "hithstabilizerl1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerL1",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitHStabilizerR1 [Indent level: 2],
        "hithstabilizerr1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerR1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitVStabilizer1 [Indent level: 2],
        "hitvstabilizer1": {
            "armor": 0.8,
            "material": -1,
            "name": "VStabilizer1",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitTail [Indent level: 2],
        "hittail": {
            "armor": 0.8,
            "material": -1,
            "name": "tail boom",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitPitotTube [Indent level: 2],
        "hitpitottube": {
            "armor": 0.5,
            "material": -1,
            "name": "pitot tube",
            "passthrough": 0.2
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStaticPort [Indent level: 2],
        "hitstaticport": {
            "armor": 0.1,
            "material": -1,
            "name": "static port",
            "passthrough": 1
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStarter1 [Indent level: 2],
        "hitstarter1": {
            "armor": 0.1,
            "material": -1,
            "name": "starter1",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStarter2 [Indent level: 2],
        "hitstarter2": {
            "armor": 0.1,
            "material": -1,
            "name": "starter2",
            "passthrough": 0
        },
        # Class: CfgVehicles|Helicopter|HitPoints|HitStarter3 [Indent level: 2],
        "hitstarter3": {
            "armor": 0.1,
            "material": -1,
            "name": "starter3",
            "passthrough": 0
        }
    },
    # Class: CfgVehicles|RHS_Ka52_base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|RHS_Ka52_base|TransportMagazines|_xx_rhs_30Rnd_545x39_7N10_AK [Indent level: 2]
        "_xx_rhs_30rnd_545x39_7n10_ak": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": 6
        },
        # Class: CfgVehicles|RHS_Ka52_base|TransportMagazines|_xx_rhs_mag_rgd5 [Indent level: 2],
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 2
        },
        # Class: CfgVehicles|RHS_Ka52_base|TransportMagazines|_xx_rhs_mag_nspn_red [Indent level: 2],
        "_xx_rhs_mag_nspn_red": {
            "magazine": "rhs_mag_nspn_red",
            "count": 4
        },
        # Class: CfgVehicles|RHS_Ka52_base|TransportMagazines|_xx_rhs_mag_rdg2_white [Indent level: 2],
        "_xx_rhs_mag_rdg2_white": {
            "magazine": "rhs_mag_rdg2_white",
            "count": 4
        }
    },
    # Class: CfgVehicles|RHS_Ka52_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|RHS_Ka52_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 2
        }
    },
    # Class: CfgVehicles|RHS_Ka52_base|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|RHS_Ka52_base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
    "gunnercansee": 55,
    "drivercansee": 55,
    "laserscanner": 1,
    "lockdetectionsystem": "8 + 4",
    "incomingmissiledetectionsystem": "8 + 16",
    # Class: CfgVehicles|RHS_Ka52_base|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -4,
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
        "maxmovez": 0.1
    },
    # Class: CfgVehicles|RHS_Ka52_base|Viewoptics [Indent level: 1],
    "viewoptics": {
        "initanglex": 0,
        "minanglex": 0,
        "maxanglex": 0,
        "initangley": 0,
        "minangley": 0,
        "maxangley": 0,
        "initfov": 0.1,
        "minfov": 0.1,
        "maxfov": 1.2
    },
    "hiddenselections": ["camo1","camo2","n1","n2","tail_decals","mfd_gun_tex"],
    # Class: CfgVehicles|RHS_Ka52_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|RHS_Ka52_base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Grey",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01_co.paa","|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02_co.paa"],
            "factions": ["rhs_faction_vvs_c","rhs_faction_vvs"]
        },
        # Class: CfgVehicles|RHS_Ka52_base|textureSources|Camo [Indent level: 2],
        "camo": {
            "displayname": "Camo",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01_RU_co.paa","|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02_RU_co.paa"],
            "factions": ["rhs_faction_vvs_c","rhs_faction_vvs"]
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|RHS_Ka52_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|RHS_Ka52_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of side number",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHSAIRKA52NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|AviaYellow [Indent level: 4],
                "aviayellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|AviaBlue [Indent level: 4],
                "aviablue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultvalue": "AviaBlue"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|AviaRed [Indent level: 4],
                "aviared": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|AviaWhiteOut [Indent level: 4],
                "aviawhiteout": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|AviaCDF [Indent level: 4],
                "aviacdf": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "displayname": "Set side number",
            "tooltip": "Set side number. 2 numbers are required. Type 0 to hide numbers completly",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRKA52NumberPlaces}else{[_this, [['Number', cRHSAIRKA52NumberPlaces, _this getVariable ['rhs_decalNumber_type','AviaYellow'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalTail [Indent level: 2],
        "rhs_decaltail": {
            "displayname": "Define tail decal",
            "tooltip": "Define tail decalthat will be drawn on vehicle",
            "property": "rhs_decalTail",
            "control": "Combo",
            "expression": "[_this,[['Label', cRHSAIRKA52TailPlaces, 'Aviation',_value]]] call rhs_fnc_decalsInit",
            "defaultvalue": -1,
            "typename": "Number",
            # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalTail|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalTail|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": -1
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalTail|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|RHS_Ka52_base|Attributes|rhs_decalTail|values|VVS [Indent level: 4],
                "vvs": {
                    "name": "VVS Russia",
                    "value": 3,
                    "defaultvalue": 3
                }
            }
        }
    },
    # Class: CfgVehicles|RHS_Ka52_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|DoorL [Indent level: 2]
        "doorl": {
            "source": "door",
            "animperiod": 1.4
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|DoorR [Indent level: 2],
        "doorr": {
            "source": "door",
            "animperiod": 1.4
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|landingLights [Indent level: 2],
        "landinglights": {
            "source": "door",
            "animperiod": 1.4
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|eject [Indent level: 2],
        "eject": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|k37_pilot_rocket_hide [Indent level: 2],
        "k37_pilot_rocket_hide": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|k37_gunner_rocket_hide [Indent level: 2],
        "k37_gunner_rocket_hide": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|elev [Indent level: 2],
        "elev": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|elev_bank [Indent level: 2],
        "elev_bank": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|offset [Indent level: 2],
        "offset": {
            "source": "user",
            "animperiod": 0.0002
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|mfd_right_gun_tg [Indent level: 2],
        "mfd_right_gun_tg": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 1
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|mfd_right_gun_ta [Indent level: 2],
        "mfd_right_gun_ta": {
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 1
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|mfd_left_toggle [Indent level: 2],
        "mfd_left_toggle": {
            "initphase": 0,
            "source": "user",
            "animperiod": 1e-007
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|muzzle_rot_cannon [Indent level: 2],
        "muzzle_rot_cannon": {
            "weapon": "rhs_weap_2a42",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|muzzle_hide_upk23 [Indent level: 2],
        "muzzle_hide_upk23": {
            "weapon": "RHS_Weap_GSh23Lx2",
            "source": "reload"
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|muzzle_rot_upk23 [Indent level: 2],
        "muzzle_rot_upk23": {
            "weapon": "RHS_Weap_GSh23Lx2",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|hit_pylon_1_source [Indent level: 2],
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|hit_pylon_2_source [Indent level: 2],
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|hit_pylon_3_source [Indent level: 2],
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles|RHS_Ka52_base|AnimationSources|hit_pylon_4_source [Indent level: 2],
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "hitpoint": "HitGlass7",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass8 [Indent level: 2],
        "hitglass8": {
            "hitpoint": "HitGlass8",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass9 [Indent level: 2],
        "hitglass9": {
            "hitpoint": "HitGlass9",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass10 [Indent level: 2],
        "hitglass10": {
            "hitpoint": "HitGlass10",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass11 [Indent level: 2],
        "hitglass11": {
            "hitpoint": "HitGlass11",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass12 [Indent level: 2],
        "hitglass12": {
            "hitpoint": "HitGlass12",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass13 [Indent level: 2],
        "hitglass13": {
            "hitpoint": "HitGlass13",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HitGlass14 [Indent level: 2],
        "hitglass14": {
            "hitpoint": "HitGlass14",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|Gatling [Indent level: 2],
        "gatling": {
            "source": "revolving",
            "weapon": "gatling_30mm"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|Muzzle_flash [Indent level: 2],
        "muzzle_flash": {
            "source": "ammorandom",
            "weapon": "gatling_30mm"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|Missiles_revolving [Indent level: 2],
        "missiles_revolving": {
            "source": "revolving",
            "weapon": "rockets_Skyfire"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|Hide [Indent level: 2],
        "hide": {
            "source": "user",
            "animperiod": 0,
            "initphase": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|door_L [Indent level: 2],
        "door_l": {
            "source": "door",
            "animperiod": 1,
            "initphase": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|door_R [Indent level: 2],
        "door_r": {
            "source": "door",
            "animperiod": 1,
            "initphase": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|door_L_pop [Indent level: 2],
        "door_l_pop": {
            "source": "door",
            "animperiod": 1,
            "initphase": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|door_R_pop [Indent level: 2],
        "door_r_pop": {
            "source": "door",
            "animperiod": 1,
            "initphase": 0
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|AnimationSources|HideWeapons [Indent level: 2],
        "hideweapons": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitEngine1 [Indent level: 2],
        "hitengine1": {
            "source": "hit",
            "hitpoint": "HitEngine1",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "source": "hit",
            "hitpoint": "HitEngine2",
            "raw": 1
        },
        # Class: CfgVehicles|Helicopter|AnimationSources|HitWinch_Source [Indent level: 2],
        "hitwinch_source": {
            "source": "hit",
            "hitpoint": "HitWinch",
            "raw": 1
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
    # Class: CfgVehicles|RHS_Ka52_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|RHS_Ka52_base|UserActions|SAFEMODE [Indent level: 2]
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
        # Class: CfgVehicles|RHS_Ka52_base|UserActions|MFD_Left_Toggle [Indent level: 2],
        "mfd_left_toggle": {
            "displayname": "Toggle MFD",
            "position": "",
            "priority": 0.01,
            "radius": 3,
            "onlyforplayer": 1,
            "showwindow": 0,
            "condition": "(call rhs_fnc_findPlayer) isEqualTo (driver this)",
            "statement": "this animateSource ['mfd_left_toggle',1-(this animationSourcePhase 'mfd_left_toggle')]"
        },
        # Class: CfgVehicles|RHS_Ka52_base|UserActions|openDoor [Indent level: 2],
        "opendoor": {
            "displayname": "Lights up",
            "position": "",
            "priority": 0.01,
            "radius": 3,
            "onlyforplayer": 1,
            "showwindow": 0,
            "condition": "this doorPhase 'landingLights' < 0.5 AND alive this",
            "statement": "this animateDoor ['landingLights',1]"
        },
        # Class: CfgVehicles|RHS_Ka52_base|UserActions|closeDoor [Indent level: 2],
        "closedoor": {
            "displayname": "Lights down",
            "condition": "this doorPhase 'landingLights' > 0.5 AND alive this",
            "statement": "this animateDoor ['landingLights',0]",
            "position": "",
            "priority": 0.01,
            "radius": 3,
            "onlyforplayer": 1,
            "showwindow": 0
        }
    },
    "enablemanualfire": 1,
    # Class: CfgVehicles|RHS_Ka52_base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "gunnerdoor": "doorR",
            "gunnerlefthandanimname": "lever_gunner",
            "gunnerrighthandanimname": "stick_gunner",
            "gunnerleftleganimname": "pedalL",
            "gunnerrightleganimname": "pedalR",
            "gunneraction": "RHS_KA52_Gunner",
            "gunnerinaction": "RHS_KA52_Gunner",
            "gunnergetinaction": "pilot_Heli_Light_02_Enter",
            "gunnergetoutaction": "pilot_Heli_Light_02_exit",
            "iscopilot": 1,
            "startengine": 0,
            "outgunnermayfire": 1,
            "commanding": -1,
            "primarygunner": 1,
            "usepip": 1,
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "caneject": 1,
            "memorypointsgetingunner": "Pos_Gunner",
            "memorypointsgetingunnerdir": "Pos_Gunner_dir",
            "memorypointsgetingunnerprecise": "pos gunner",
            "precisegetinout": 1,
            "minelev": -80,
            "maxelev": 15,
            "initelev": 0,
            "minturn": -120,
            "maxturn": 120,
            "initturn": 0,
            "gunbeg": "gunstart",
            "gunend": "gunend",
            "body": "MainTurret",
            "gun": "MainGun",
            "memorypointgun": "machinegun",
            "memorypointgunneroptics": "pilotview",
            "selectionfireanim": "zasleh",
            "turretinfotype": "RHS_RscWeaponKa52_FCS",
            "canusescanners": 0,
            "allowtablock": 0,
            # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Viewoptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "initfov": 0.067,
                "minfov": 0.019,
                "maxfov": 0.067
            },
            "gunneropticseffect": ["TankCommanderOptics1"],
            # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|OpticsIn|Samshin_WFOV [Indent level: 4]
                "samshin_wfov": {
                    "opticsdisplayname": "3",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_samshin_WFOV",
                    "initanglex": 0,
                    "initangley": 0,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "minanglex": -30,
                    "minangley": -100,
                    "initfov": 0.233333,
                    "maxfov": 0.233333,
                    "minfov": 0.233333,
                    "thermalmode": [0,1],
                    "visionmode": ["Normal","TI"]
                },
                # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|OpticsIn|Samshin_NFOV [Indent level: 4],
                "samshin_nfov": {
                    "opticsdisplayname": "15",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_samshin",
                    "initfov": 0.0466667,
                    "maxfov": 0.0466667,
                    "minfov": 0.0466667,
                    "initanglex": 0,
                    "initangley": 0,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "minanglex": -30,
                    "minangley": -100,
                    "thermalmode": [0,1],
                    "visionmode": ["Normal","TI"]
                },
                # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|OpticsIn|Samshin_NFOV_Stabilised [Indent level: 4],
                "samshin_nfov_stabilised": {
                    "opticsdisplayname": "22",
                    "initfov": 0.0318182,
                    "maxfov": 0.0318182,
                    "minfov": 0.0318182,
                    "directionstabilized": 1,
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_samshin",
                    "initanglex": 0,
                    "initangley": 0,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "minanglex": -30,
                    "minangley": -100,
                    "thermalmode": [0,1],
                    "visionmode": ["Normal","TI"]
                }
            },
            # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 6],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|UAVDisplay [Indent level: 6],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 6],
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "range": [8000,16000,24000,4000],
                            "resource": "RscCustomInfoSensors"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
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
                # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    "defaultdisplay": "SensorDisplay",
                    # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 6],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|UAVDisplay [Indent level: 6],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 6],
                        "sensordisplay": {
                            "componenttype": "SensorsDisplayComponent",
                            "resource": "RscCustomInfoSensors",
                            "range": [8000,16000,24000,4000]
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "gunnerforceoptics": 0,
            "weapons": ["rhs_weap_MASTERSAFE_Holdster15","rhs_weap_fcs_mi24","rhs_weap_2a42"],
            "magazines": ["rhs_laserfcsmag","rhs_mag_3uor6_230","rhs_mag_3ubr8_230"],
            # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|HitTurret [Indent level: 3],
            "hitturret": {
                "armor": 0.8,
                "material": -1,
                "name": "gun1",
                "visual": "gun1",
                "passthrough": 0.5
            },
            # Class: CfgVehicles|RHS_Ka52_base|Turrets|MainTurret|HitGun [Indent level: 3],
            "hitgun": {
                "armor": 0.4,
                "material": -1,
                "name": "gun2",
                "visual": "gun2",
                "passthrough": 0.2
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|Turrets|MainTurret|OpticsOut [Indent level: 3],
            "opticsout": {
                # Class: CfgVehicles|Heli_Attack_02_base_F|Turrets|MainTurret|OpticsOut|Monocular [Indent level: 4]
                "monocular": {
                    "initfov": 0.9,
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
                    "visionmode": ["Normal","NVG"],
                    "gunneropticsmodel": "",
                    "gunneropticseffect": []
                }
            },
            "soundservo": ["",0.01,1],
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "discretedistance": [100,200,300,400,500,600,700,800,1000,1200,1500,1800,2100,2500],
            "discretedistanceinitindex": 5,
            "showhmd": 0,
            "showalltargets": 4,
            "maxhorizontalrotspeed": 1.8,
            "maxverticalrotspeed": 1.5,
            # Class: CfgVehicles|Heli_Attack_02_base_F|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|Heli_Attack_02_base_F|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 1,
                    "material": -1,
                    "name": "main_turret_hit",
                    "visual": "gun",
                    "passthrough": 0.3,
                    "radius": 0.35
                },
                # Class: CfgVehicles|Heli_Attack_02_base_F|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 1,
                    "material": -1,
                    "name": "main_gun_hit",
                    "visual": "gun",
                    "passthrough": 0.3,
                    "radius": 0.35
                }
            },
            "turretcansee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles|Helicopter|Turrets|MainTurret|TurretSpec [Indent level: 3],
            "turretspec": {
                "showheadphones": 1
            },
            "enablemanualfire": 0,
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
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
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
            "gunneropticscolor": [0,0,0,1],
            "gunneropticsshowcursor": 0,
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
            "gunneroutopticseffect": [],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunneroutopticsshowcursor": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "gunnerusespilotview": 0,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
            "gunnercompartments": "Compartment1",
            "lodturnedin": -1,
            "lodturnedout": -1,
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
            "turretfollowfreelook": 0,
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
        # Class: CfgVehicles|Helicopter_Base_F|Turrets|CopilotTurret [Indent level: 2],
        "copilotturret": {
        }
    },
    # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights|Comp1|Light_Pilot [Indent level: 3]
            "light_pilot": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights|Comp1|Light_Pilot|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.5,
                    "hardlimitend": 0.6
                },
                "point": "light_pilot"
            },
            # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights|Comp1|Light_Gunner [Indent level: 3],
            "light_gunner": {
                "point": "light_gunner",
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights|Comp1|Light_Pilot|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.5,
                    "hardlimitend": 0.6
                }
            }
        },
        # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights|Comp2 [Indent level: 2],
        "comp2": {
            # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights|Comp2|Light_Pilot [Indent level: 3]
            "light_pilot": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights|Comp1|Light_Pilot|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.5,
                    "hardlimitend": 0.6
                },
                "point": "light_pilot"
            },
            # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights|Comp2|Light_Gunner [Indent level: 3],
            "light_gunner": {
                "point": "light_gunner",
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|RHS_Ka52_base|compartmentsLights|Comp1|Light_Pilot|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.5,
                    "hardlimitend": 0.6
                }
            }
        }
    },
    # Class: CfgVehicles|RHS_Ka52_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|RHS_Ka52_base|Reflectors|LSvetla [Indent level: 2]
        "lsvetla": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "intensity": 50,
            "size": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "useflare": 0,
            "daylight": 0,
            "flaresize": 0.75,
            # Class: CfgVehicles|RHS_Ka52_base|Reflectors|LSvetla|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 200,
                "hardlimitend": 250
            }
        },
        # Class: CfgVehicles|RHS_Ka52_base|Reflectors|LSvetlaFlare [Indent level: 2],
        "lsvetlaflare": {
            "position": "L_Flare",
            "useflare": 1,
            "color": [10,10,9],
            "ambient": [10,10,9],
            "intensity": 50,
            "size": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "daylight": 0,
            "flaresize": 0.75,
            # Class: CfgVehicles|RHS_Ka52_base|Reflectors|LSvetla|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 200,
                "hardlimitend": 250
            }
        },
        # Class: CfgVehicles|RHS_Ka52_base|Reflectors|RSvetla [Indent level: 2],
        "rsvetla": {
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "intensity": 50,
            "size": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 0.75,
            # Class: CfgVehicles|RHS_Ka52_base|Reflectors|LSvetla|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 200,
                "hardlimitend": 250
            }
        },
        # Class: CfgVehicles|RHS_Ka52_base|Reflectors|RSvetlaFlare [Indent level: 2],
        "rsvetlaflare": {
            "position": "R_Flare",
            "useflare": 1,
            "color": [10,10,9],
            "ambient": [10,10,9],
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "intensity": 50,
            "size": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            "daylight": 0,
            "flaresize": 0.75,
            # Class: CfgVehicles|RHS_Ka52_base|Reflectors|LSvetla|Attenuation [Indent level: 3],
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
    # Class: CfgVehicles|RHS_Ka52_base|markerlights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|RHS_Ka52_base|markerlights|GreenStill [Indent level: 2]
        "greenstill": {
            "activelight": 0,
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "intensity": 55,
            "blinking": 0,
            "brightness": 0.01,
            "flaresize": 0.5,
            "name": "zeleny pozicni",
            "useflare": 1,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        },
        # Class: CfgVehicles|RHS_Ka52_base|markerlights|RedStill [Indent level: 2],
        "redstill": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "name": "cerveny pozicni",
            "activelight": 0,
            "intensity": 55,
            "blinking": 0,
            "brightness": 0.01,
            "flaresize": 0.5,
            "useflare": 1,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        },
        # Class: CfgVehicles|RHS_Ka52_base|markerlights|WhiteStill [Indent level: 2],
        "whitestill": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "bily pozicni",
            "activelight": 0,
            "intensity": 55,
            "blinking": 0,
            "brightness": 0.01,
            "flaresize": 0.5,
            "useflare": 1,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        },
        # Class: CfgVehicles|RHS_Ka52_base|markerlights|WhiteBlicking [Indent level: 2],
        "whiteblicking": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "blinking": 1,
            "name": "bily pozicni blik",
            "activelight": 0,
            "intensity": 55,
            "brightness": 0.01,
            "flaresize": 0.5,
            "useflare": 1,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        },
        # Class: CfgVehicles|RHS_Ka52_base|markerlights|RedBlinking [Indent level: 2],
        "redblinking": {
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "name": "cerveny pozicni blik",
            "blinking": 1,
            "activelight": 0,
            "intensity": 55,
            "brightness": 0.01,
            "flaresize": 0.5,
            "useflare": 1,
            "drawlight": 1,
            "drawlightsize": 0.25,
            "drawlightcentersize": 0.08
        }
    },
    "dammagehalf": ["|rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_cauges_CO.paa","|rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_caugesmf_CO.paa"],
    "dammagefull": ["|rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_cauges_CO.paa","|rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_caugesmf_CO.paa"],
    # Class: CfgVehicles|RHS_Ka52_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01_destruct.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02_destruct.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass_in.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass_in_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass_in_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_cauges_light.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_cauges_bug.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_cauges_bug.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_weapons.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_weapons_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_weapons_destruct.rvmat"]
    },
    # Class: CfgVehicles|RHS_Ka52_base|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Left_Compass [Indent level: 2]
        "mfd_left_compass": {
            "topleft": "mfd_2_nav_tl",
            "topright": "mfd_2_nav_tr",
            "bottomleft": "mfd_2_nav_bl",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_var",
            "enableparallax": 0,
            # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Left_Compass|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Left_Compass|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Left_Compass|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.95,
                "color": [0,0.83,0.83],
                "condition": "on",
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Left_Compass|Draw|Text [Indent level: 4],
                "text": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "Heading",
                    "sourcescale": 1,
                    "pos": [[0.498,0.19],1],
                    "right": [[0.543,0.19],1],
                    "down": [[0.498,0.24],1]
                }
            }
        },
        # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Right_Gun [Indent level: 2],
        "mfd_right_gun": {
            "topleft": "mfd_3_gun_tl",
            "topright": "mfd_3_gun_tr",
            "bottomleft": "mfd_3_gun_bl",
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_var",
            "turret": [0],
            # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Right_Gun|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Right_Gun|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.95,
                "color": [0.45,0.7,0.29],
                "condition": "on",
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Right_Gun|Draw|Speed [Indent level: 4],
                "speed": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "sourcelength": 1,
                    "pos": [[0.425,0.165],1],
                    "right": [[0.46,0.165],1],
                    "down": [[0.425,0.21],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Right_Gun|Draw|Height [Indent level: 4],
                "height": {
                    "source": "altitudeAGL",
                    "sourceoffset": -2,
                    "sourcescale": 1,
                    "sourcelength": 1,
                    "pos": [[0.625,0.165],1],
                    "right": [[0.66,0.165],1],
                    "down": [[0.625,0.21],1],
                    "type": "text",
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Right_Gun|Draw|TurretDirection [Indent level: 4],
                "turretdirection": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "userText",
                    "sourceindex": 2,
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "pos": [[0.515,0.165],1],
                    "right": [[0.55,0.165],1],
                    "down": [[0.515,0.21],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Right_Gun|Draw|TurretElevation [Indent level: 4],
                "turretelevation": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "userText",
                    "sourceindex": 3,
                    "sourcescale": 1,
                    "sourcelength": 1,
                    "sourceprecision": 1,
                    "pos": [[0.88,0.385],1],
                    "right": [[0.895,0.385],1],
                    "down": [[0.88,0.405],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Right_Gun|Draw|DistanceToTarget [Indent level: 4],
                "distancetotarget": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "userText",
                    "sourceindex": 1,
                    "sourcescale": 1,
                    "sourcelength": 1,
                    "sourceprecision": 1,
                    "pos": [[0.515,0.74],1],
                    "right": [[0.55,0.74],1],
                    "down": [[0.515,0.785],1]
                }
            },
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "enableparallax": 0,
            # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Left_Compass|Bones [Indent level: 3],
            "bones": {
            }
        },
        # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_left_Gun [Indent level: 2],
        "mfd_left_gun": {
            "topleft": "mfd_2_gun_tl",
            "topright": "mfd_2_gun_tr",
            "bottomleft": "mfd_2_gun_bl",
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_left_Gun|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_left_Gun|Draw [Indent level: 3],
            "draw": {
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_left_Gun|Draw|Speed [Indent level: 4]
                "speed": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "sourcelength": 1,
                    "pos": [[0.425,0.165],1],
                    "right": [[0.46,0.165],1],
                    "down": [[0.425,0.21],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_left_Gun|Draw|Height [Indent level: 4],
                "height": {
                    "source": "altitudeAGL",
                    "sourceoffset": -2,
                    "sourcescale": 1,
                    "sourcelength": 1,
                    "pos": [[0.625,0.165],1],
                    "right": [[0.66,0.165],1],
                    "down": [[0.625,0.21],1],
                    "type": "text",
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_left_Gun|Draw|TurretDirection [Indent level: 4],
                "turretdirection": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "userText",
                    "sourceindex": 2,
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "pos": [[0.515,0.165],1],
                    "right": [[0.55,0.165],1],
                    "down": [[0.515,0.21],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_left_Gun|Draw|TurretElevation [Indent level: 4],
                "turretelevation": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "userText",
                    "sourceindex": 3,
                    "sourcescale": 1,
                    "sourcelength": 1,
                    "sourceprecision": 1,
                    "pos": [[0.88,0.385],1],
                    "right": [[0.895,0.385],1],
                    "down": [[0.88,0.405],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_left_Gun|Draw|DistanceToTarget [Indent level: 4],
                "distancetotarget": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "userText",
                    "sourceindex": 1,
                    "sourcescale": 1,
                    "sourcelength": 1,
                    "sourceprecision": 1,
                    "pos": [[0.515,0.74],1],
                    "right": [[0.55,0.74],1],
                    "down": [[0.515,0.785],1]
                },
                "alpha": 0.95,
                "color": [0.45,0.7,0.29],
                "condition": "on"
            },
            "turret": [0],
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "enableparallax": 0,
            # Class: CfgVehicles|RHS_Ka52_base|MFD|MFD_Left_Compass|Bones [Indent level: 3],
            "bones": {
            }
        },
        # Class: CfgVehicles|RHS_Ka52_base|MFD|CrossGunner [Indent level: 2],
        "crossgunner": {
            "topleft": "HUD LH",
            "topright": "HUD PH",
            "bottomleft": "HUD LD",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "enableparallax": 1,
            "turret": [0],
            # Class: CfgVehicles|RHS_Ka52_base|MFD|CrossGunner|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|RHS_Ka52_base|MFD|CrossGunner|Bones|WeaponAim [Indent level: 4]
                "weaponaim": {
                    "type": "vector",
                    "source": "turretworld",
                    "pos0": [0.5,0.41],
                    "pos10": [1.15,1.75]
                }
            },
            # Class: CfgVehicles|RHS_Ka52_base|MFD|CrossGunner|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.95,
                "color": [0,0.3,0.05],
                "condition": "on",
                # Class: CfgVehicles|RHS_Ka52_base|MFD|CrossGunner|Draw|MGun [Indent level: 4],
                "mgun": {
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|CrossGunner|Draw|MGun|Circle [Indent level: 5]
                    "circle": {
                        "type": "line",
                        "width": 4,
                        "points": [["WeaponAim",[0,0.02],1],["WeaponAim",[0,0.01],1],[],["WeaponAim",[0,-0.01],1],["WeaponAim",[0,-0.02],1],[],["WeaponAim",[0.02,0],1],["WeaponAim",[0.01,0],1],[],["WeaponAim",[-0.01,0],1],["WeaponAim",[-0.02,0],1],[]]
                    }
                }
            }
        },
        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD [Indent level: 2],
        "airplanehud": {
            # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Pos10Vector [Indent level: 3]
            "pos10vector": {
                "type": "vector",
                "pos0": [0.502,0.49],
                "pos10": [1.112,1.03]
            },
            "topleft": "HUD LH",
            "topright": "HUD PH",
            "bottomleft": "HUD LD",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "enableparallax": 1,
            "turret": [-1],
            "font": "rhs_digital_font_rus",
            # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.502,0.49]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|ImpactPoint [Indent level: 4],
                "impactpoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.39],
                    "pos10": [1.134,0.96]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|Limit0109 [Indent level: 4],
                "limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot1 [Indent level: 4],
                "missileflighttimerot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minangle": 0,
                    "maxangle": 18,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot2 [Indent level: 4],
                "missileflighttimerot2": {
                    "maxangle": 37,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot3 [Indent level: 4],
                "missileflighttimerot3": {
                    "maxangle": 55.5,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot4 [Indent level: 4],
                "missileflighttimerot4": {
                    "maxangle": 74,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot5 [Indent level: 4],
                "missileflighttimerot5": {
                    "maxangle": 92.5,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot6 [Indent level: 4],
                "missileflighttimerot6": {
                    "maxangle": 111,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot7 [Indent level: 4],
                "missileflighttimerot7": {
                    "maxangle": 129.5,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot8 [Indent level: 4],
                "missileflighttimerot8": {
                    "maxangle": 148,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot9 [Indent level: 4],
                "missileflighttimerot9": {
                    "maxangle": 166.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot10 [Indent level: 4],
                "missileflighttimerot10": {
                    "maxangle": 185,
                    "max": 10,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot11 [Indent level: 4],
                "missileflighttimerot11": {
                    "maxangle": 203.5,
                    "max": 11,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot12 [Indent level: 4],
                "missileflighttimerot12": {
                    "maxangle": 222,
                    "max": 12,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot13 [Indent level: 4],
                "missileflighttimerot13": {
                    "maxangle": 240.5,
                    "max": 13,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot14 [Indent level: 4],
                "missileflighttimerot14": {
                    "maxangle": 259,
                    "max": 14,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot15 [Indent level: 4],
                "missileflighttimerot15": {
                    "maxangle": 277.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot16 [Indent level: 4],
                "missileflighttimerot16": {
                    "maxangle": 296,
                    "max": 16,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot17 [Indent level: 4],
                "missileflighttimerot17": {
                    "maxangle": 314.5,
                    "max": 17,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot18 [Indent level: 4],
                "missileflighttimerot18": {
                    "maxangle": 333,
                    "max": 18,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot19 [Indent level: 4],
                "missileflighttimerot19": {
                    "maxangle": 351.5,
                    "max": 19,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot20 [Indent level: 4],
                "missileflighttimerot20": {
                    "maxangle": 370,
                    "max": 20,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.899054
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|ForwardVector [Indent level: 4],
                "forwardvector": {
                    "type": "vector",
                    "source": "forward",
                    "pos0": [0,0],
                    "pos10": [0.347,0.345]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|Target [Indent level: 4],
                "target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.39],
                    "pos10": [1.134,0.96]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.502,0.49],
                    "pos10": [0.563,0.544]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|SliderSpeedSource [Indent level: 4],
                "sliderspeedsource": {
                    "type": "linear",
                    "source": "speed",
                    "min": 0,
                    "max": 138.889,
                    "minpos": [0.255,0.2],
                    "maxpos": [0.255,0.525]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|AGLMove [Indent level: 4],
                "aglmove": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "min": 0,
                    "max": 50,
                    "minpos": [0,"0.15*0.65"],
                    "maxpos": [0,"0.65*0.65"]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|Heading [Indent level: 4],
                "heading": {
                    "type": "linear",
                    "source": "Heading",
                    "min": -36,
                    "max": 36,
                    "minpos": [0,0],
                    "maxpos": [1,0]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|TargetDistanceMissile [Indent level: 4],
                "targetdistancemissile": {
                    "type": "rotational",
                    "source": "targetDist",
                    "center": [0,0],
                    "min": 100,
                    "max": 3000,
                    "minangle": -120,
                    "maxangle": 120
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|vspeed [Indent level: 4],
                "vspeed": {
                    "source": "vspeed",
                    "type": "linear",
                    "min": -30,
                    "max": 30,
                    "minpos": [0,0.06],
                    "maxpos": [0,0.3]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|HorizonBankMGun [Indent level: 4],
                "horizonbankmgun": {
                    "type": "rotational",
                    "source": "HorizonBank",
                    "center": [0,0],
                    "min": -6.28319,
                    "max": 6.28319,
                    "minangle": -360,
                    "maxangle": 360,
                    "aspectratio": 0.885246
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|HorizonDive [Indent level: 4],
                "horizondive": {
                    "source": "horizonDive",
                    "type": "linear",
                    "min": -1,
                    "max": 1,
                    "minpos": [0.502,2.49],
                    "maxpos": [0.502,-1.51]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|HorizonBankReverted [Indent level: 4],
                "horizonbankreverted": {
                    "center": [0.5,0.6016],
                    "type": "rotational",
                    "source": "HorizonBank",
                    "min": "-3.14159265*2",
                    "max": "3.14159265*2",
                    "minangle": 360,
                    "maxangle": -360,
                    "aspectratio": 0.8
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],
                "level0": {
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelP5 [Indent level: 4],
                "levelp5": {
                    "angle": 5,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelM5 [Indent level: 4],
                "levelm5": {
                    "angle": -5,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": 10,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": -10,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": 15,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": -15,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": 20,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": -20,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": 25,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": -25,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": 30,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": -30,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": 35,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": -35,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": 40,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": -40,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": 45,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": -45,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.95,
                "color": [0,0.3,0.05],
                "condition": "on",
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|MGunD [Indent level: 4],
                "mgund": {
                    "condition": "mgun+rocket+bomb",
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|MGunD|Cross [Indent level: 5],
                    "cross": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0269716],1],["ImpactPoint",[0,-0.0359621],1],[],["ImpactPoint",[0.02,-0.024],1],["ImpactPoint",[0.025,-0.031],1],[],["ImpactPoint",[0,-0.002],1],["ImpactPoint",[0,0.002],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[]]
                    },
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|MGunD|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0314669],1],["MissileFlightTimeRot1",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot18",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot19",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.035],1,"ImpactPoint",1]]
                    },
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|MGunD|Circle_Min_Range [Indent level: 5],
                    "circle_min_range": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0269716],1],["ImpactPoint",[0.005208,-0.0265616],1],["ImpactPoint",[0.01026,-0.0253452],1],["ImpactPoint",[0.015,-0.0233574],1],["ImpactPoint",[0.019284,-0.0206603],1],["ImpactPoint",[0.02298,-0.0173373],1],["ImpactPoint",[0.02598,-0.0134858],1],["ImpactPoint",[0.028191,-0.00922429],1],["ImpactPoint",[0.029544,-0.00468227],1],["ImpactPoint",[0.03,0],1],["ImpactPoint",[0.029544,0.00468227],1],["ImpactPoint",[0.028191,0.00922429],1],["ImpactPoint",[0.02598,0.0134858],1],["ImpactPoint",[0.02298,0.0173373],1],["ImpactPoint",[0.019284,0.0206603],1],["ImpactPoint",[0.015,0.0233574],1],["ImpactPoint",[0.01026,0.0253452],1],["ImpactPoint",[0.005208,0.0265616],1],["ImpactPoint",[0,0.0269716],1],["ImpactPoint",[-0.005208,0.0265616],1],["ImpactPoint",[-0.01026,0.0253452],1],["ImpactPoint",[-0.015,0.0233574],1],["ImpactPoint",[-0.019284,0.0206603],1],["ImpactPoint",[-0.02298,0.0173373],1],["ImpactPoint",[-0.02598,0.0134858],1],["ImpactPoint",[-0.028191,0.00922429],1],["ImpactPoint",[-0.029544,0.00468227],1],["ImpactPoint",[-0.03,0],1],["ImpactPoint",[-0.029544,-0.00468227],1],["ImpactPoint",[-0.028191,-0.00922429],1],["ImpactPoint",[-0.02598,-0.0134858],1],["ImpactPoint",[-0.02298,-0.0173373],1],["ImpactPoint",[-0.019284,-0.0206603],1],["ImpactPoint",[-0.015,-0.0233574],1],["ImpactPoint",[-0.01026,-0.0253452],1],["ImpactPoint",[-0.005208,-0.0265616],1],["ImpactPoint",[0,-0.0269716],1]]
                    },
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|MGunD|Distance [Indent level: 5],
                    "distance": {
                        "type": "text",
                        "source": "ImpactDistance",
                        "sourcescale": 0.001,
                        "sourceprecision": 1,
                        "max": 15,
                        "align": "center",
                        "scale": 1,
                        "pos": ["ImpactPoint",[-0.002,-0.08],1],
                        "right": ["ImpactPoint",[0.045,-0.08],1],
                        "down": ["ImpactPoint",[-0.002,-0.04],1]
                    }
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Static2 [Indent level: 4],
                "static2": {
                    "cliptl": [0,0.5],
                    "clipbr": [1,0],
                    "points": [["PlaneW",[-0.21,"7.34351e-009--0.12"],1],["PlaneW",[-0.28,"9.79135e-009--0.12"],1],[],["PlaneW",[0.21,"-2.00338e-009--0.12"],1],["PlaneW",[0.28,"-2.67117e-009--0.12"],1],[],["PlaneW",[-0.105,"0.145492--0.12"],1],["PlaneW",[-0.14,"0.19399--0.12"],1],[],["PlaneW",[0.105,"0.145492--0.12"],1],["PlaneW",[0.14,"0.19399--0.12"],1],[],["PlaneW",[-0.181865,"0.084--0.12"],1],["PlaneW",[-0.242487,"0.112--0.12"],1],[],["PlaneW",[0.181865,"0.084--0.12"],1],["PlaneW",[0.242487,"0.112--0.12"],1],[],["PlaneW",[-0.202844,"0.0434816--0.12"],1],["PlaneW",[-0.270459,"0.0579755--0.12"],1],[],["PlaneW",[0.202844,"0.0434816--0.12"],1],["PlaneW",[0.270459,"0.0579755--0.12"],1],[],["PlaneW",[-0.209201,"0.0146422--0.12"],1],["PlaneW",[-0.244068,"0.0170825--0.12"],1],[],["PlaneW",[-0.20681,"0.0291729--0.12"],1],["PlaneW",[-0.241278,"0.034035--0.12"],1],[],["PlaneW",[0.20681,"0.0291729--0.12"],1],["PlaneW",[0.241278,"0.034035--0.12"],1],[],["PlaneW",[0.209201,"0.0146422--0.12"],1],["PlaneW",[0.244068,"0.0170825--0.12"],1],[]],
                    "type": "line"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|HorizonBank [Indent level: 4],
                "horizonbank": {
                    "points": [["PlaneW",1,"HorizonBankReverted",["0.21-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.14-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.11-0.50","-0.035-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.08-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.03-0.50","0-0.50"],1],[],["PlaneW",1,"HorizonBankReverted",["-0.21-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.14-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.11-0.50","-0.035-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.08-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.03-0.50","0-0.50"],1],[],["PlaneW",1,"HorizonBankReverted",["0-0.50","-0.004-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0-0.50","0.004-0.50"],1]],
                    "type": "line"
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|CollectiveGroup [Indent level: 4],
                "collectivegroup": {
                    "condition": "simulRTD",
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|CollectiveGroup|CollectiveText [Indent level: 5],
                    "collectivetext": {
                        "type": "text",
                        "source": "static",
                        "text": "%",
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.2,0.2],1],
                        "right": [[0.26,0.2],1],
                        "down": [[0.2,0.25],1]
                    },
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|CollectiveGroup|CollectiveNumber [Indent level: 5],
                    "collectivenumber": {
                        "type": "text",
                        "source": "rtdCollective",
                        "sourcescale": 100,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.2,0.2],1],
                        "right": [[0.26,0.2],1],
                        "down": [[0.2,0.25],1]
                    }
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0.25,0.25],
                    "clipbr": [0.75,0.75],
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "level0": {
                            "type": "line",
                            "width": 4,
                            "points": [["Level0",[-0.28,0],1],["Level0",[-0.175,0],1],[],["Level0",[-0.063,0],1],["Level0",[-0.007,0],1],[],["Level0",[0.007,0],1],["Level0",[0.063,0],1],[],["Level0",[0.175,0],1],["Level0",[0.28,0],1]]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM5 [Indent level: 6],
                        "levelm5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.32,0],1],["LevelM5",[-0.22,0],1],[],["LevelM5",[0.22,0],1],["LevelM5",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_5 [Indent level: 6],
                        "valm_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM5",[-0.21,-0.021],1],
                            "right": ["LevelM5",[-0.15,-0.021],1],
                            "down": ["LevelM5",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_5L [Indent level: 6],
                        "valm_1_5l": {
                            "align": "left",
                            "pos": ["LevelM5",[0.21,-0.021],1],
                            "right": ["LevelM5",[0.27,-0.021],1],
                            "down": ["LevelM5",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP5 [Indent level: 6],
                        "levelp5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.32,0],1],["LevelP5",[-0.22,0],1],[],["LevelP5",[0.22,0],1],["LevelP5",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_5 [Indent level: 6],
                        "valp_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP5",[-0.21,-0.021],1],
                            "right": ["LevelP5",[-0.15,-0.021],1],
                            "down": ["LevelP5",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_5L [Indent level: 6],
                        "valp_1_5l": {
                            "align": "left",
                            "pos": ["LevelP5",[0.21,-0.021],1],
                            "right": ["LevelP5",[0.27,-0.021],1],
                            "down": ["LevelP5",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM10 [Indent level: 6],
                        "levelm10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.32,0],1],["LevelM10",[-0.22,0],1],[],["LevelM10",[0.22,0],1],["LevelM10",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_10 [Indent level: 6],
                        "valm_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM10",[-0.21,-0.021],1],
                            "right": ["LevelM10",[-0.15,-0.021],1],
                            "down": ["LevelM10",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_10L [Indent level: 6],
                        "valm_1_10l": {
                            "align": "left",
                            "pos": ["LevelM10",[0.21,-0.021],1],
                            "right": ["LevelM10",[0.27,-0.021],1],
                            "down": ["LevelM10",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP10 [Indent level: 6],
                        "levelp10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.32,0],1],["LevelP10",[-0.22,0],1],[],["LevelP10",[0.22,0],1],["LevelP10",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_10 [Indent level: 6],
                        "valp_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP10",[-0.21,-0.021],1],
                            "right": ["LevelP10",[-0.15,-0.021],1],
                            "down": ["LevelP10",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_10L [Indent level: 6],
                        "valp_1_10l": {
                            "align": "left",
                            "pos": ["LevelP10",[0.21,-0.021],1],
                            "right": ["LevelP10",[0.27,-0.021],1],
                            "down": ["LevelP10",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM15 [Indent level: 6],
                        "levelm15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.32,0],1],["LevelM15",[-0.22,0],1],[],["LevelM15",[0.22,0],1],["LevelM15",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_15 [Indent level: 6],
                        "valm_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM15",[-0.21,-0.021],1],
                            "right": ["LevelM15",[-0.15,-0.021],1],
                            "down": ["LevelM15",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_15L [Indent level: 6],
                        "valm_1_15l": {
                            "align": "left",
                            "pos": ["LevelM15",[0.21,-0.021],1],
                            "right": ["LevelM15",[0.27,-0.021],1],
                            "down": ["LevelM15",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP15 [Indent level: 6],
                        "levelp15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.32,0],1],["LevelP15",[-0.22,0],1],[],["LevelP15",[0.22,0],1],["LevelP15",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_15 [Indent level: 6],
                        "valp_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP15",[-0.21,-0.021],1],
                            "right": ["LevelP15",[-0.15,-0.021],1],
                            "down": ["LevelP15",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_15L [Indent level: 6],
                        "valp_1_15l": {
                            "align": "left",
                            "pos": ["LevelP15",[0.21,-0.021],1],
                            "right": ["LevelP15",[0.27,-0.021],1],
                            "down": ["LevelP15",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM20 [Indent level: 6],
                        "levelm20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.32,0],1],["LevelM20",[-0.22,0],1],[],["LevelM20",[0.22,0],1],["LevelM20",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_20 [Indent level: 6],
                        "valm_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM20",[-0.21,-0.021],1],
                            "right": ["LevelM20",[-0.15,-0.021],1],
                            "down": ["LevelM20",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_20L [Indent level: 6],
                        "valm_1_20l": {
                            "align": "left",
                            "pos": ["LevelM20",[0.21,-0.021],1],
                            "right": ["LevelM20",[0.27,-0.021],1],
                            "down": ["LevelM20",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP20 [Indent level: 6],
                        "levelp20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.32,0],1],["LevelP20",[-0.22,0],1],[],["LevelP20",[0.22,0],1],["LevelP20",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_20 [Indent level: 6],
                        "valp_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP20",[-0.21,-0.021],1],
                            "right": ["LevelP20",[-0.15,-0.021],1],
                            "down": ["LevelP20",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_20L [Indent level: 6],
                        "valp_1_20l": {
                            "align": "left",
                            "pos": ["LevelP20",[0.21,-0.021],1],
                            "right": ["LevelP20",[0.27,-0.021],1],
                            "down": ["LevelP20",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM25 [Indent level: 6],
                        "levelm25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.32,0],1],["LevelM25",[-0.22,0],1],[],["LevelM25",[0.22,0],1],["LevelM25",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_25 [Indent level: 6],
                        "valm_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM25",[-0.21,-0.021],1],
                            "right": ["LevelM25",[-0.15,-0.021],1],
                            "down": ["LevelM25",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_25L [Indent level: 6],
                        "valm_1_25l": {
                            "align": "left",
                            "pos": ["LevelM25",[0.21,-0.021],1],
                            "right": ["LevelM25",[0.27,-0.021],1],
                            "down": ["LevelM25",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP25 [Indent level: 6],
                        "levelp25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.32,0],1],["LevelP25",[-0.22,0],1],[],["LevelP25",[0.22,0],1],["LevelP25",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_25 [Indent level: 6],
                        "valp_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP25",[-0.21,-0.021],1],
                            "right": ["LevelP25",[-0.15,-0.021],1],
                            "down": ["LevelP25",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_25L [Indent level: 6],
                        "valp_1_25l": {
                            "align": "left",
                            "pos": ["LevelP25",[0.21,-0.021],1],
                            "right": ["LevelP25",[0.27,-0.021],1],
                            "down": ["LevelP25",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM30 [Indent level: 6],
                        "levelm30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.32,0],1],["LevelM30",[-0.22,0],1],[],["LevelM30",[0.22,0],1],["LevelM30",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_30 [Indent level: 6],
                        "valm_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM30",[-0.21,-0.021],1],
                            "right": ["LevelM30",[-0.15,-0.021],1],
                            "down": ["LevelM30",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_30L [Indent level: 6],
                        "valm_1_30l": {
                            "align": "left",
                            "pos": ["LevelM30",[0.21,-0.021],1],
                            "right": ["LevelM30",[0.27,-0.021],1],
                            "down": ["LevelM30",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP30 [Indent level: 6],
                        "levelp30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.32,0],1],["LevelP30",[-0.22,0],1],[],["LevelP30",[0.22,0],1],["LevelP30",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_30 [Indent level: 6],
                        "valp_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP30",[-0.21,-0.021],1],
                            "right": ["LevelP30",[-0.15,-0.021],1],
                            "down": ["LevelP30",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_30L [Indent level: 6],
                        "valp_1_30l": {
                            "align": "left",
                            "pos": ["LevelP30",[0.21,-0.021],1],
                            "right": ["LevelP30",[0.27,-0.021],1],
                            "down": ["LevelP30",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM35 [Indent level: 6],
                        "levelm35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.32,0],1],["LevelM35",[-0.22,0],1],[],["LevelM35",[0.22,0],1],["LevelM35",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_35 [Indent level: 6],
                        "valm_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM35",[-0.21,-0.021],1],
                            "right": ["LevelM35",[-0.15,-0.021],1],
                            "down": ["LevelM35",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_35L [Indent level: 6],
                        "valm_1_35l": {
                            "align": "left",
                            "pos": ["LevelM35",[0.21,-0.021],1],
                            "right": ["LevelM35",[0.27,-0.021],1],
                            "down": ["LevelM35",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP35 [Indent level: 6],
                        "levelp35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.32,0],1],["LevelP35",[-0.22,0],1],[],["LevelP35",[0.22,0],1],["LevelP35",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_35 [Indent level: 6],
                        "valp_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP35",[-0.21,-0.021],1],
                            "right": ["LevelP35",[-0.15,-0.021],1],
                            "down": ["LevelP35",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_35L [Indent level: 6],
                        "valp_1_35l": {
                            "align": "left",
                            "pos": ["LevelP35",[0.21,-0.021],1],
                            "right": ["LevelP35",[0.27,-0.021],1],
                            "down": ["LevelP35",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM40 [Indent level: 6],
                        "levelm40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.32,0],1],["LevelM40",[-0.22,0],1],[],["LevelM40",[0.22,0],1],["LevelM40",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_40 [Indent level: 6],
                        "valm_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM40",[-0.21,-0.021],1],
                            "right": ["LevelM40",[-0.15,-0.021],1],
                            "down": ["LevelM40",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_40L [Indent level: 6],
                        "valm_1_40l": {
                            "align": "left",
                            "pos": ["LevelM40",[0.21,-0.021],1],
                            "right": ["LevelM40",[0.27,-0.021],1],
                            "down": ["LevelM40",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP40 [Indent level: 6],
                        "levelp40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.32,0],1],["LevelP40",[-0.22,0],1],[],["LevelP40",[0.22,0],1],["LevelP40",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_40 [Indent level: 6],
                        "valp_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP40",[-0.21,-0.021],1],
                            "right": ["LevelP40",[-0.15,-0.021],1],
                            "down": ["LevelP40",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_40L [Indent level: 6],
                        "valp_1_40l": {
                            "align": "left",
                            "pos": ["LevelP40",[0.21,-0.021],1],
                            "right": ["LevelP40",[0.27,-0.021],1],
                            "down": ["LevelP40",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM45 [Indent level: 6],
                        "levelm45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.32,0],1],["LevelM45",[-0.22,0],1],[],["LevelM45",[0.22,0],1],["LevelM45",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_45 [Indent level: 6],
                        "valm_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM45",[-0.21,-0.021],1],
                            "right": ["LevelM45",[-0.15,-0.021],1],
                            "down": ["LevelM45",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_45L [Indent level: 6],
                        "valm_1_45l": {
                            "align": "left",
                            "pos": ["LevelM45",[0.21,-0.021],1],
                            "right": ["LevelM45",[0.27,-0.021],1],
                            "down": ["LevelM45",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "scale": 1,
                            "sourcescale": 1
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP45 [Indent level: 6],
                        "levelp45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.32,0],1],["LevelP45",[-0.22,0],1],[],["LevelP45",[0.22,0],1],["LevelP45",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_45 [Indent level: 6],
                        "valp_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP45",[-0.21,-0.021],1],
                            "right": ["LevelP45",[-0.15,-0.021],1],
                            "down": ["LevelP45",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_45L [Indent level: 6],
                        "valp_1_45l": {
                            "align": "left",
                            "pos": ["LevelP45",[0.21,-0.021],1],
                            "right": ["LevelP45",[0.27,-0.021],1],
                            "down": ["LevelP45",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "scale": 1,
                            "sourcescale": 1
                        }
                    }
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|Static [Indent level: 4],
                "static": {
                    "type": "line",
                    "width": 4,
                    "points": [["vspeed",[0.22,0.56],1],["vspeed",[0.205,0.55],1],["vspeed",[0.22,0.54],1],["vspeed",[0.22,0.56],1],[],[[0.2,0.598],1],[[0.2,0.782],1],[],[[0.2,0.61],1],[[0.18,0.61],1],[],[[0.195,0.77],1],[[0.18,0.77],1],[],[[0.195,0.65],1],[[0.18,0.65],1],[],[[0.195,0.69],1],[[0.18,0.69],1],[],[[0.195,0.73],1],[[0.18,0.73],1],[],["vspeed",[0.78,0.56],1],["vspeed",[0.795,0.55],1],["vspeed",[0.78,0.54],1],["vspeed",[0.78,0.56],1],[],[[0.8,0.598],1],[[0.8,0.862],1],[],[[0.8,0.61],1],[[0.83,0.61],1],[],[[0.805,0.85],1],[[0.83,0.85],1],[],[[0.805,0.65],1],[[0.82,0.65],1],[],[[0.805,0.69],1],[[0.82,0.69],1],[],[[0.805,0.73],1],[[0.83,0.73],1],[],[[0.805,0.77],1],[[0.82,0.77],1],[],[[0.805,0.81],1],[[0.82,0.81],1],[],[[0.52,0.14],1],[[0.5,0.12],1],[[0.48,0.14],1],[],[[0.3,0.115],1],[[0.7,0.115],1],[]]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|SpeedGroup [Indent level: 4],
                "speedgroup": {
                    "condition": "speed-2.78",
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|SpeedGroup|Static [Indent level: 5],
                    "static": {
                        "type": "line",
                        "width": 4,
                        "points": [["SliderSpeedSource",["0.015-0.03",0.01],1],["SliderSpeedSource",["0.000-0.03",0],1],["SliderSpeedSource",["0.015-0.03",-0.01],1],["SliderSpeedSource",["0.015-0.03",0.01],1],[],[["0.25-0.03",0.2],1],[["0.25-0.03",0.525],1],[],[["0.25-0.03",0.2],1],[["0.23-0.03",0.2],1],[],[["0.24-0.03",0.265],1],[["0.23-0.03",0.265],1],[],[["0.24-0.03",0.33],1],[["0.23-0.03",0.33],1],[],[["0.24-0.03",0.395],1],[["0.23-0.03",0.395],1],[],[["0.24-0.03",0.46],1],[["0.23-0.03",0.46],1],[],[["0.25-0.03",0.525],1],[["0.23-0.03",0.525],1],[]]
                    },
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|SpeedGroup|SpeedStatic500 [Indent level: 5],
                    "speedstatic500": {
                        "type": "text",
                        "source": "static",
                        "text": "500",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [["0.220-0.03",0.183],1],
                        "right": [[0.23,0.183],1],
                        "down": [["0.220-0.03",0.213],1]
                    },
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|SpeedGroup|SpeedStatic0 [Indent level: 5],
                    "speedstatic0": {
                        "type": "text",
                        "source": "static",
                        "text": "0",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "left",
                        "pos": [["0.220-0.03",0.508],1],
                        "right": [[0.23,0.508],1],
                        "down": [["0.220-0.03",0.538],1]
                    }
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|AGL_Radar [Indent level: 4],
                "agl_radar": {
                    "condition": "50-altitudeAGL",
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|AGL_Radar|Panel [Indent level: 5],
                    "panel": {
                        "width": 4,
                        "type": "line",
                        "points": [["AGLMove",[0.73,0.11],1],["AGLMove",[0.745,0.1],1],["AGLMove",[0.73,0.09],1],["AGLMove",[0.73,0.11],1],[],[[0.75,0.1975],1],[[0.75,0.5225],1],[],[[0.75,0.1975],1],[[0.77,0.1975],1],[],[[0.725,0.5225],1],[[0.775,0.5225],1],[],[[0.755,0.2625],1],[[0.77,0.2625],1],[],[[0.755,0.3275],1],[[0.77,0.3275],1],[],[[0.755,0.3925],1],[[0.77,0.3925],1],[],[[0.755,0.4575],1],[[0.77,0.4575],1],[]]
                    },
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|AGL_Radar|AltStatic50 [Indent level: 5],
                    "altstatic50": {
                        "type": "text",
                        "source": "static",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "text": 50,
                        "pos": [[0.79,0.17],1],
                        "right": [[0.83,0.17],1],
                        "down": [[0.79,0.205],1]
                    }
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|RadarBoxes [Indent level: 4],
                "radarboxes": {
                    "type": "radar",
                    "pos0": [0.5,0.39],
                    "pos10": [1.134,0.96],
                    "width": 4,
                    "points": [[[-0.002,-0.00179811],1],[[0.002,-0.00179811],1],[[0.002,0.00179811],1],[[-0.002,0.00179811],1],[[-0.002,-0.00179811],1]]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|TargetDiamond [Indent level: 4],
                "targetdiamond": {
                    # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|TargetDiamond|shape [Indent level: 5]
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0.02,0.0179811],1],["Target",1,"Limit0109",1,[-0.02,0.0179811],1],["Target",1,"Limit0109",1,[-0.02,-0.0179811],1],["Target",1,"Limit0109",1,[0.02,-0.0179811],1],["Target",1,"Limit0109",1,[0.02,0.0179811],1]]
                    }
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|SpeedNumber [Indent level: 4],
                "speednumber": {
                    "type": "text",
                    "align": "right",
                    "source": "speed",
                    "sourcescale": 3.6,
                    "sourcelength": 3,
                    "scale": 1,
                    "pos": [[0.07,0.07],1],
                    "right": [[0.15,0.07],1],
                    "down": [[0.07,0.12],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|AltNumber [Indent level: 4],
                "altnumber": {
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "sourceoffset": -2,
                    "align": "right",
                    "pos": [[0.76,0.07],1],
                    "right": [[0.84,0.07],1],
                    "down": [[0.76,0.12],1],
                    "type": "text",
                    "scale": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|AltNumberStatic [Indent level: 4],
                "altnumberstatic": {
                    "type": "text",
                    "source": "static",
                    "align": "right",
                    "text": "р",
                    "scale": 1,
                    "sourcescale": 1,
                    "pos": [[0.88,0.09],1],
                    "right": [[0.93,0.09],1],
                    "down": [[0.88,0.13],1],
                    "sourcelength": 3,
                    "sourceoffset": -2
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|VspeedNumber [Indent level: 4],
                "vspeednumber": {
                    "source": "vspeed",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "align": "left",
                    "pos": [[0.81,0.55],1],
                    "right": [[0.89,0.55],1],
                    "down": [[0.81,0.6],1],
                    "type": "text",
                    "scale": 1
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|VspeedNumberStaticP30 [Indent level: 4],
                "vspeednumberstaticp30": {
                    "type": "text",
                    "source": "static",
                    "text": "+30",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.835,0.59],1],
                    "right": [[0.885,0.59],1],
                    "down": [[0.835,0.63],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|VspeedNumberStaticZERO [Indent level: 4],
                "vspeednumberstaticzero": {
                    "type": "text",
                    "source": "static",
                    "text": "0",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.835,0.71],1],
                    "right": [[0.885,0.71],1],
                    "down": [[0.835,0.75],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|VspeedNumberStaticM30 [Indent level: 4],
                "vspeednumberstaticm30": {
                    "type": "text",
                    "source": "static",
                    "text": "-30",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.835,0.83],1],
                    "right": [[0.885,0.83],1],
                    "down": [[0.835,0.87],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|NevimStatic3 [Indent level: 4],
                "nevimstatic3": {
                    "type": "text",
                    "source": "static",
                    "text": "3",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.14,0.59],1],
                    "right": [[0.19,0.59],1],
                    "down": [[0.14,0.63],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|NevimStaticZERO [Indent level: 4],
                "nevimstaticzero": {
                    "type": "text",
                    "source": "static",
                    "text": "0",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.14,0.71],1],
                    "right": [[0.19,0.71],1],
                    "down": [[0.14,0.75],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|NevimStatic1 [Indent level: 4],
                "nevimstatic1": {
                    "type": "text",
                    "source": "static",
                    "text": "1",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0.14,0.75],1],
                    "right": [[0.19,0.75],1],
                    "down": [[0.14,0.79],1]
                },
                # Class: CfgVehicles|RHS_Ka52_base|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],
                "headingscale": {
                    "type": "scale",
                    "source": "heading",
                    "horizontal": 1,
                    "sourcescale": 0.1,
                    "width": 4,
                    "top": 0.3,
                    "center": 0.5,
                    "bottom": 0.7,
                    "linexleft": 0.11,
                    "lineyright": 0.1,
                    "linexleftmajor": 0.11,
                    "lineyrightmajor": 0.09,
                    "majorlineeach": 2,
                    "numbereach": 2,
                    "step": 0.5,
                    "stepsize": 0.0555556,
                    "align": "center",
                    "scale": 1,
                    "pos": ["0.32-0.01","0.0+0.05"],
                    "right": ["0.38-0.01","0.0+0.05"],
                    "down": ["0.32-0.01","0.04+0.05"]
                }
            }
        }
    },
    # Class: CfgVehicles|RHS_Ka52_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        "hit": "",
        # Class: CfgVehicles|RHS_Ka52_base|EventHandlers|RHS_EventHandlers [Indent level: 2],
        "rhs_eventhandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "init": "_this call rhs_fnc_air_init",
            "getout": "_this spawn rhs_fnc_ka52_ejection",
            "engine": "_this call rhs_fnc_addParachutes;"
        },
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "features": "Randomization: No						<br />Camo selections: 2 - main body, turret with engines and wings						<br />Script door sources: door_L, door_R, door_L_pop, door_R_pop						<br />Script animations: None 						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: No						<br />Cargo proxy indexes: 1 to 8",
    # Class: CfgVehicles|Heli_Attack_02_base_F|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Heli_Attack_02_base_F|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_air_gunship_s"],
            "speechplural": ["veh_air_gunship_p"]
        }
    },
    "textsingular": "gunship",
    "textplural": "gunships",
    "namesound": "veh_air_gunship_s",
    "_generalmacro": "Heli_Attack_02_base_F",
    "fuelconsumptionrate": 0.138,
    "altfullforce": 4000,
    "altnoforce": 6000,
    "crewvulnerable": 0,
    # Class: CfgVehicles|Heli_Attack_02_base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": "A multi-purpose successor to the Mi-24, the Mi-48 Kajman (BLUFOR designation `Hornet`) is a large gunship and attack helicopter with troop transport capacity for 8 passengers. The front part of the helicopter is based on the Mi-28 attack helicopter, but the hull is modified for passenger transport. The Kajman has a coaxial rotor providing increased stability. It is armed with a 30mm three-barrel Minigun, unguided Skyfire rockets and guided Skalpel AT missiles."
    },
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "maxfordingdepth": 0.75,
    "tailbladevertical": 0,
    "supplyradius": 2.5,
    "maximumload": 2000,
    "cargocaneject": 1,
    "cost": 3e+006,
    "showalltargets": 4,
    "cargoaction": ["passenger_generic01_leanleft","passenger_generic01_foldhands","passenger_generic01_leanright","passenger_generic01_leanleft","passenger_generic01_leanright","passenger_generic01_leanleft","passenger_generic01_foldhands","passenger_generic01_leanleft"],
    "cargodoors": [],
    "memorypointdriveroptics": "PilotCamera_pos",
    "driverweaponsinfotype": "RscOptics_Heli_Attack_02_pilot",
    "attenuationeffecttype": "HeliAttenuation",
    "emptysound": ["",0,1],
    "soundgeneralcollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_1",3.16228,1,500],
    "soundgeneralcollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_2",3.16228,1,500],
    "soundgeneralcollision3": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_3",3.16228,1,500],
    "soundcrashes": ["soundGeneralCollision1",0.33,"soundGeneralCollision2",0.33,"soundGeneralCollision3",0.33],
    "soundlandcrashes": ["emptySound",0],
    "soundbuildingcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundarmorcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundwoodcrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundbushcollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_1",3.16228,1,500],
    "soundbushcollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_2",3.16228,1,500],
    "soundbushcollision3": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_3",3.16228,1,500],
    "soundbushcrash": ["soundBushCollision1",0.33,"soundBushCollision2",0.33,"soundBushCollision3",0.33],
    "soundwatercollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_water_ext_1",3.16228,1,300],
    "soundwatercollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_water_ext_2",3.16228,1,300],
    "soundwatercrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "sounddammage": ["A3|Sounds_F|vehicles|crashes|helis|Heli_crash_default_int_1",10,1],
    "soundgetin": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_door",1,1],
    "soundgetout": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_door",1,1,50],
    "soundengineonint": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_start2",0.158489,1],
    "soundengineonext": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_start2",0.794328,1,600],
    "soundengineoffint": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_stop2",0.199526,1],
    "soundengineoffext": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_stop2",0.794328,1,600],
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",1,1],
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_4",0.398107,1],
    "rotordamageint": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_int_2",1,1],
    "rotordamageout": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_ext_2",2.51189,1,300],
    "rotordamage": ["rotorDamageInt","rotorDamageOut"],
    "taildamageint": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1],
    "taildamageout": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1,300],
    "taildamage": ["tailDamageInt","tailDamageOut"],
    "landingsoundint0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int1",1,1,100],
    "landingsoundint1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int2",1,1,100],
    "landingsoundint": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingsoundout0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext1",5.62341,1,500],
    "landingsoundout1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext2",5.62341,1,500],
    "landingsoundout": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    "slingcargoattach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEndINT",1,1],
    "slingcargoattach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookLock",1.77828,1,200],
    "slingcargoattach": ["slingCargoAttach0","slingCargoAttach1"],
    "slingcargodetach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEndINT",1,1],
    "slingcargodetach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookUnlock",1.77828,1,200],
    "slingcargodetach": ["slingCargoDetach0","slingCargoDetach1"],
    "slingcargodetachair0": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_int",1,1],
    "slingcargodetachair1": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_ext",1,1,300],
    "slingcargodetachair": ["slingCargoDetach0","slingCargoDetach1"],
    "slingcargoropebreak0": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_int",1,1],
    "slingcargoropebreak1": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_ext",1,1,200],
    "slingcargoropebreak": ["slingCargoDetach0","slingCargoDetach1"],
    # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|EngineExt [Indent level: 2]
        "engineext": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_engine",1.77828,1,900],
            "frequency": "rotorSpeed",
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|RotorExt [Indent level: 2],
        "rotorext": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_rotor",1.12202,1,2000],
            "frequency": "rotorSpeed*(1-rotorThrust/8)*1.2",
            "volume": "2*camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)",
            "cone": [1.6,3.14,1.6,0.95]
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|RotorNoiseExt [Indent level: 2],
        "rotornoiseext": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|rotor_swist",1,1,400],
            "frequency": 1,
            "volume": "camPos * (rotorThrust factor [0.7, 0.9])",
            "cone": [0.7,1.3,1,0]
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|EngineInt [Indent level: 2],
        "engineint": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_engine",1.12202,1],
            "frequency": "rotorSpeed",
            "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|RotorInt [Indent level: 2],
        "rotorint": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_rotor",0.891251,1],
            "frequency": "rotorSpeed*(1-rotorThrust/8)*1.2",
            "volume": "(1-camPos)*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|TransmissionDamageExt_phase1 [Indent level: 2],
        "transmissiondamageext_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|TransmissionDamageExt_phase2 [Indent level: 2],
        "transmissiondamageext_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|TransmissionDamageInt_phase1 [Indent level: 2],
        "transmissiondamageint_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|TransmissionDamageInt_phase2 [Indent level: 2],
        "transmissiondamageint_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|damageAlarmInt [Indent level: 2],
        "damagealarmint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|damageAlarmExt [Indent level: 2],
        "damagealarmext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|rotorLowAlarmInt [Indent level: 2],
        "rotorlowalarmint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|rotorLowAlarmExt [Indent level: 2],
        "rotorlowalarmext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|scrubLandInt [Indent level: 2],
        "scrublandint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
            "frequency": 1,
            "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|scrubLandExt [Indent level: 2],
        "scrublandext": {
            "sound": ["A3|Sounds_F|dummysound",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|scrubBuildingInt [Indent level: 2],
        "scrubbuildingint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos) * (scrubBuilding factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|scrubBuildingExt [Indent level: 2],
        "scrubbuildingext": {
            "sound": ["A3|Sounds_F|dummysound",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|scrubTreeInt [Indent level: 2],
        "scrubtreeint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeInt",1,1,100],
            "frequency": 1,
            "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|scrubTreeExt [Indent level: 2],
        "scrubtreeext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|RainExt [Indent level: 2],
        "rainext": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
            "frequency": 1,
            "volume": "camPos * (rain - rotorSpeed/2) * 2"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|RainInt [Indent level: 2],
        "rainint": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|SlingLoadDownExt [Indent level: 2],
        "slingloaddownext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1.25893,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|SlingLoadUpExt [Indent level: 2],
        "slingloadupext": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1.25893,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|SlingLoadDownInt [Indent level: 2],
        "slingloaddownint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|SlingLoadUpInt [Indent level: 2],
        "slingloadupint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|WindInt [Indent level: 2],
        "windint": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wind_closed",0.562341,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|GStress [Indent level: 2],
        "gstress": {
            "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2e",0.501187,1,50],
            "frequency": 1,
            "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Sounds|SpeedStress [Indent level: 2],
        "speedstress": {
            "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress3",1,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*(speed factor[40,60])"
        }
    },
    # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt [Indent level: 1],
    "soundsext": {
        # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|SoundEvents [Indent level: 2]
        "soundevents": {
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds [Indent level: 2],
        "sounds": {
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|EngineExt [Indent level: 3]
            "engineext": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_engine",1.77828,1,900],
                "frequency": "rotorSpeed",
                "volume": "camPos*((rotorSpeed-0.72)*4)"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|RotorExt [Indent level: 3],
            "rotorext": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_rotor",1.12202,1,2000],
                "frequency": "rotorSpeed*(1-rotorThrust/8)*1.2",
                "volume": "2*camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)",
                "cone": [1.6,3.14,1.6,0.95]
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|RotorNoiseExt [Indent level: 3],
            "rotornoiseext": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|rotor_swist",1,1,400],
                "frequency": 1,
                "volume": "camPos * (rotorThrust factor [0.7, 0.9])",
                "cone": [0.7,1.3,1,0]
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|EngineInt [Indent level: 3],
            "engineint": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_engine",1.12202,1],
                "frequency": "rotorSpeed",
                "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|RotorInt [Indent level: 3],
            "rotorint": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_rotor",0.891251,1],
                "frequency": "rotorSpeed*(1-rotorThrust/8)*1.2",
                "volume": "(1-camPos)*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|TransmissionDamageExt_phase1 [Indent level: 3],
            "transmissiondamageext_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|TransmissionDamageExt_phase2 [Indent level: 3],
            "transmissiondamageext_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|TransmissionDamageInt_phase1 [Indent level: 3],
            "transmissiondamageint_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|TransmissionDamageInt_phase2 [Indent level: 3],
            "transmissiondamageint_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|damageAlarmInt [Indent level: 3],
            "damagealarmint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|damageAlarmExt [Indent level: 3],
            "damagealarmext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|rotorLowAlarmInt [Indent level: 3],
            "rotorlowalarmint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|rotorLowAlarmExt [Indent level: 3],
            "rotorlowalarmext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|scrubLandInt [Indent level: 3],
            "scrublandint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
                "frequency": 1,
                "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|scrubLandExt [Indent level: 3],
            "scrublandext": {
                "sound": ["A3|Sounds_F|dummysound",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|scrubBuildingInt [Indent level: 3],
            "scrubbuildingint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos) * (scrubBuilding factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|scrubBuildingExt [Indent level: 3],
            "scrubbuildingext": {
                "sound": ["A3|Sounds_F|dummysound",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|scrubTreeInt [Indent level: 3],
            "scrubtreeint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeInt",1,1,100],
                "frequency": 1,
                "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|scrubTreeExt [Indent level: 3],
            "scrubtreeext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|RainExt [Indent level: 3],
            "rainext": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
                "frequency": 1,
                "volume": "camPos * (rain - rotorSpeed/2) * 2"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|RainInt [Indent level: 3],
            "rainint": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|SlingLoadDownExt [Indent level: 3],
            "slingloaddownext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|SlingLoadUpExt [Indent level: 3],
            "slingloadupext": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|SlingLoadDownInt [Indent level: 3],
            "slingloaddownint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|SlingLoadUpInt [Indent level: 3],
            "slingloadupint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|WindInt [Indent level: 3],
            "windint": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wind_closed",0.562341,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|GStress [Indent level: 3],
            "gstress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2e",0.501187,1,50],
                "frequency": 1,
                "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
            },
            # Class: CfgVehicles|Heli_Attack_02_base_F|SoundsExt|Sounds|SpeedStress [Indent level: 3],
            "speedstress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress3",1,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[40,60])"
            }
        }
    },
    # Class: CfgVehicles|Heli_Attack_02_base_F|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|Heli_Attack_02_base_F|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaust1",
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectHeliBig"
        },
        # Class: CfgVehicles|Heli_Attack_02_base_F|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "exhaust2",
            "direction": "exhaust2_dir",
            "effect": "ExhaustsEffectHeliBig"
        }
    },
    "defaultusermfdvalues": [0.25,1,0.25,1],
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "washdownstrength": "1.0f",
    "washdowndiameter": "40.0f",
    "minsmokedamage": 0.3,
    "maxsmokedamage": 0.99,
    "driverleftleganimname": "pedalL",
    "driverrightleganimname": "pedalR",
    # Class: CfgVehicles|Helicopter_Base_F|CamShake [Indent level: 1],
    "camshake": {
        "power": 30,
        "frequency": 20,
        "distance": 50,
        "minspeed": 50
    },
    "simulation": "helicopterrtd",
    "unitinfotypertd": "RscUnitInfoAirRTDFullDigital",
    "unitinfotypelite": "RscUnitInfoAirRTDBasic",
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
    "gearuptime": 3.33,
    "geardowntime": 2,
    "gearminalt": 0.5,
    # Class: CfgVehicles|Helicopter|CargoSpec [Indent level: 1],
    "cargospec": {
        # Class: CfgVehicles|Helicopter|CargoSpec|Cargo1 [Indent level: 2]
        "cargo1": {
            "showheadphones": 1
        },
        # Class: CfgVehicles|Helicopter|CargoSpec|Cargo2 [Indent level: 2],
        "cargo2": {
            "showheadphones": 0
        }
    },
    "startduration": 20,
    "maxbackrotordive": 0,
    "minbackrotordive": 0,
    "neutralbackrotordive": 0,
    "cyclicasideforcecoef": 1,
    "memorypointpilot": "pilot",
    "_mainbladecenter": "rotor_center",
    "selectionfireanim": "zasleh",
    "enablesweep": 1,
    "envelope": [0,0.2,0.9,2.1,2.5,3.3,3.5,3.6,3.7,3.8,3.8,3,0.9,0.7,0.5],
    "minfiretime": 20,
    "steeraheadsimul": 0.5,
    "steeraheadplan": 0.7,
    "soundlandinggear": ["",1,1],
    "slingloadmemorypoint": "slingLoad0",
    "slingloadmaxcargomass": 0,
    "extcameraparams": [-1],
    "camouflage": 100,
    "audible": 50,
    "crewcrashprotection": 0.25,
    "headgforceleaningfactor": [0.01,0.0025,0.01],
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "damageeffect": "AirDestructionEffects",
    "type": 2,
    "transportmaxbackpacks": 1,
    "explosionshielding": 4,
    "mintotaldamagethreshold": 0.005,
    # Class: CfgVehicles|Helicopter|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "slingloadmincargomass": 0,
    "formationx": 50,
    "formationz": 100,
    "precision": 100,
    "brakedistance": 200,
    "formationtime": 10,
    "gearsupfrictioncoef": 0.5,
    "airbrakefrictioncoef": 3,
    "airfrictioncoefs2": [0.001,0.0005,6e-005],
    "airfrictioncoefs1": [0.1,0.05,0.006],
    "airfrictioncoefs0": [0,0,0],
    "insidesoundcoef": 0.0316228,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "irscanrangemin": 2000,
    "irscanrangemax": 10000,
    "irscantoeyefactor": 2,
    "nightvision": 0,
    "cargocompartments": [0],
    "transportmaxmagazines": 20,
    "transportmaxweapons": 3,
    "enablegps": 1,
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
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
    "waterleakiness": 100,
    "waterresistance": 1,
    "impacteffectssea": "ImpactEffectsAir",
    "flarevelocity": 100,
    "enableradio": 1,
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "radartype": 4,
    "countermeasureactivationradius": 10000,
    # Class: CfgVehicles|Air|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 0.2,
        "frequency": 3,
        "distance": 0,
        "minspeed": 1
    },
    # Class: CfgVehicles|Air|camShakeDamage [Indent level: 1],
    "camshakedamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minspeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "mingforce": 0.2,
    "maxgforce": 2,
    "gforceshakeattenuation": 0.5,
    "secondaryexplosion": -1,
    "fuelexplosionpower": 1,
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
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "portrait": "",
    "ghostpreview": "",
    "armorlights": 0.4,
    "replacedamaged": "",
    "replacedamagedlimit": 0.9,
    "replacedamagedhitpoints": [],
    "keepinepesceneafterdeath": 0,
    "extcameraposition": [0,2,-20],
    "groupcameraposition": [0,5,-30],
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
    "hideunitinfo": 0,
    "limitedspeedcoef": 0.22,
    "hasdriver": 1,
    "driverforceoptics": 0,
    "hideweaponsdriver": 1,
    "hideweaponscargo": 0,
    "memorypointsupply": "doplnovani",
    "enablewatch": 0,
    "useprecisegetinaction": 0,
    "allowtablock": 1,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "wheelcircumference": 1,
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
    "aggregatereflectors": [],
    "cargoiscodriver": [0],
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "hideproxyincombat": 0,
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
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