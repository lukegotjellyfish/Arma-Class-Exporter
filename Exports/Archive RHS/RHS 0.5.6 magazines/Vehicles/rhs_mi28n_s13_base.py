rhs_mi28n_s13_base = {
    "editorpreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_mi28n_Base.paa",
    "displayname": "Mi-28N (S-13)",
    # Class: CfgVehicles|rhs_mi28n_S13_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhs_mi28n_S13_base|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            # Class: CfgVehicles|rhs_mi28n_S13_base|Components|TransportPylonsComponent|pylons [Indent level: 3]
            "pylons": {
                # Class: CfgVehicles|rhs_mi28n_S13_base|Components|TransportPylonsComponent|pylons|pylon1 [Indent level: 4]
                "pylon1": {
                    "attachment": "rhs_mag_b13l_s13b",
                    "turret": [],
                    "hardpoints": ["RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_B13L1","RHS_HP_B8V20","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_UPK23"],
                    "priority": 1,
                    "maxweight": 550,
                    "uiposition": [0.54,0.4],
                    "hitpoint": "HitPylon1"
                },
                # Class: CfgVehicles|rhs_mi28n_S13_base|Components|TransportPylonsComponent|pylons|pylon2 [Indent level: 4],
                "pylon2": {
                    "attachment": "rhs_mag_b13l_s13b",
                    "turret": [],
                    "uiposition": [0.12,0.4],
                    "mirroredmissilepos": 1,
                    "hitpoint": "HitPylon2",
                    "hardpoints": ["RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_B13L1","RHS_HP_B8V20","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_UPK23"],
                    "priority": 1,
                    "maxweight": 550
                },
                # Class: CfgVehicles|rhs_mi28n_S13_base|Components|TransportPylonsComponent|pylons|pylon3 [Indent level: 4],
                "pylon3": {
                    "attachment": "rhs_mag_9M120M_Mi28_8x",
                    "turret": [0],
                    "hardpoints": ["RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_B13L1","RHS_HP_B8V20","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_9m120_Mi28"],
                    "maxweight": 400,
                    "priority": 2,
                    "uiposition": [0.6,0.45],
                    "hitpoint": "HitPylon3"
                },
                # Class: CfgVehicles|rhs_mi28n_S13_base|Components|TransportPylonsComponent|pylons|pylon4 [Indent level: 4],
                "pylon4": {
                    "attachment": "rhs_mag_9M120M_Mi28_8x",
                    "turret": [0],
                    "uiposition": [0.06,0.45],
                    "mirroredmissilepos": 3,
                    "hitpoint": "HitPylon4",
                    "hardpoints": ["RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_B13L1","RHS_HP_B8V20","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_9m120_Mi28"],
                    "maxweight": 400,
                    "priority": 2
                },
                # Class: CfgVehicles|rhs_mi28n_S13_base|Components|TransportPylonsComponent|pylons|cmDispenser [Indent level: 4],
                "cmdispenser": {
                    "hardpoints": ["RHS_cm_UV26","RHS_cm_UV26_x2","RHS_cm_UV26_x4"],
                    "priority": 1,
                    "attachment": "rhs_UV26_CMFlare_Chaff_Magazine_x4",
                    "maxweight": 800,
                    "uiposition": [0.33,0]
                }
            },
            "uipicture": "rhsafrf|addons|rhs_mi28|data|loadouts|RHS_Mi28_EDEN_CA.paa",
            # Class: CfgVehicles|rhs_mi28_base|Components|TransportPylonsComponent|Presets [Indent level: 3],
            "presets": {
                # Class: CfgVehicles|rhs_mi28_base|Components|TransportPylonsComponent|Presets|Bomb [Indent level: 4]
                "bomb": {
                    "attachment": ["rhs_mag_fab250","rhs_mag_fab250","rhs_mag_9M120M_Mi28_8x","rhs_mag_9M120M_Mi28_8x","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Bomb"
                },
                # Class: CfgVehicles|rhs_mi28_base|Components|TransportPylonsComponent|Presets|HeavyBomb [Indent level: 4],
                "heavybomb": {
                    "attachment": ["rhs_mag_fab500","rhs_mag_fab500","rhs_mag_9M120M_Mi28_8x","rhs_mag_9M120M_Mi28_8x","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Heavy Bomb"
                },
                # Class: CfgVehicles|rhs_mi28_base|Components|TransportPylonsComponent|Presets|ClusterMine [Indent level: 4],
                "clustermine": {
                    "attachment": ["rhs_mag_kmgu2_pfm1","rhs_mag_kmgu2_pfm1","rhs_mag_9M120M_Mi28_8x","rhs_mag_9M120M_Mi28_8x","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "KMGU-2 (AP Mines)"
                },
                # Class: CfgVehicles|rhs_mi28_base|Components|TransportPylonsComponent|Presets|ClusterHE [Indent level: 4],
                "clusterhe": {
                    "attachment": ["rhs_mag_kmgu2_ao25","rhs_mag_kmgu2_ao25","rhs_mag_9M120M_Mi28_8x","rhs_mag_9M120M_Mi28_8x","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "KMGU-2 (HE)"
                },
                # Class: CfgVehicles|rhs_mi28_base|Components|TransportPylonsComponent|Presets|UPK [Indent level: 4],
                "upk": {
                    "attachment": ["rhs_mag_upk23_mixed","rhs_mag_upk23_mixed","rhs_mag_9M120M_Mi28_8x","rhs_mag_9M120M_Mi28_8x","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "UPK-23-250"
                },
                # Class: CfgVehicles|rhs_mi28_base|Components|TransportPylonsComponent|Presets|CAS [Indent level: 4],
                "cas": {
                    "attachment": ["rhs_mag_b8v20a_s8kom","rhs_mag_b8v20a_s8kom","rhs_mag_9M120M_Mi28_8x","rhs_mag_9M120M_Mi28_8x","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Close Air Support"
                },
                # Class: CfgVehicles|rhs_mi28_base|Components|TransportPylonsComponent|Presets|HeavyCAS [Indent level: 4],
                "heavycas": {
                    "attachment": ["rhs_mag_b13l1_s13b","rhs_mag_b13l1_s13b","rhs_mag_9M120M_Mi28_8x","rhs_mag_9M120M_Mi28_8x","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Close Air Support (S-13)"
                },
                # Class: CfgVehicles|rhs_mi28_base|Components|TransportPylonsComponent|Presets|Rockets [Indent level: 4],
                "rockets": {
                    "attachment": ["rhs_mag_b8v20a_s8kom","rhs_mag_b8v20a_s8kom","rhs_mag_b8v20a_s8df","rhs_mag_b8v20a_s8df","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Rockets"
                }
            }
        },
        # Class: CfgVehicles|rhs_mi28n_base|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|rhs_mi28n_base|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhs_mi28n_base|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4]
                "lasersensorcomponent": {
                    # Class: CfgVehicles|rhs_mi28n_base|Components|SensorsManagerComponent|Components|LaserSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 9000,
                        "maxrange": 9000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|rhs_mi28n_base|Components|SensorsManagerComponent|Components|LaserSensorComponent|GroundTarget [Indent level: 5],
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
                # Class: CfgVehicles|rhs_mi28n_base|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28n_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent [Indent level: 4],
                "activeradarsensorcomponent": {
                    # Class: CfgVehicles|rhs_mi28n_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 11000,
                        "maxrange": 11000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|rhs_mi28n_base|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 11000,
                        "maxrange": 11000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "anglerangehorizontal": 120,
                    "anglerangevertical": 100,
                    "typerecognitiondistance": 4000,
                    "maxfogseethrough": 1,
                    "maxtrackablespeed": 555,
                    "componenttype": "ActiveRadarSensorComponent",
                    "minspeedthreshold": 20.8333,
                    "maxspeedthreshold": 27.7778,
                    "color": [0,1,1,1],
                    "allowsmarking": 1,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|rhs_mi28n_base|Components|SensorsManagerComponent|Components|DataLinkSensorComponent [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mi28n_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhs_mi28n_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|rhs_mi28n_base|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4]
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [4000,8000,16000,25000],
                    "resource": "RscCustomInfoSensors"
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
        # Class: CfgVehicles|rhs_mi28n_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|rhs_mi28n_base|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhs_mi28n_base|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4]
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [4000,8000,16000,25000],
                    "resource": "RscCustomInfoSensors"
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
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Air|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    "selectionfireanim": "",
    "side": 0,
    "tf_isolatedamount_api": 0.6,
    "destrtype": "DestructWreck",
    "maxomega": 2000,
    "enginemoi": 10,
    # Class: CfgVehicles|rhs_mi28_base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhs_mi28_base|Wheels|Wheel_1_1 [Indent level: 2]
        "wheel_1_1": {
            "steering": 0,
            "side": "left",
            "bonename": "Wheel_1_1_axis_damper",
            "suspforceapppointoffset": "Wheel_1_1_axis",
            "tireforceapppointoffset": "Wheel_1_1_axis",
            "center": "Wheel_1_1_axis",
            "boundary": "Wheel_1_1_bound",
            "susptraveldirection": [0,-1,0],
            "width": 0.234,
            "mass": 15,
            "moi": 0.768,
            "dampingrate": 1,
            "dampingratedamaged": 2,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "maxcompression": 0.11,
            "maxdroop": 0.15,
            "sprungmass": 240,
            "springstrength": 42000,
            "springdamperrate": 99280,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.3],[0.5,1],[1,1.6]]
        },
        # Class: CfgVehicles|rhs_mi28_base|Wheels|Wheel_1_2 [Indent level: 2],
        "wheel_1_2": {
            "bonename": "Wheel_1_2_axis_damper",
            "side": "right",
            "suspforceapppointoffset": "Wheel_1_2_axis",
            "tireforceapppointoffset": "Wheel_1_2_axis",
            "center": "Wheel_1_2_axis",
            "boundary": "Wheel_1_2_bound",
            "steering": 0,
            "susptraveldirection": [0,-1,0],
            "width": 0.234,
            "mass": 15,
            "moi": 0.768,
            "dampingrate": 1,
            "dampingratedamaged": 2,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "maxcompression": 0.11,
            "maxdroop": 0.15,
            "sprungmass": 240,
            "springstrength": 42000,
            "springdamperrate": 99280,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.3],[0.5,1],[1,1.6]]
        },
        # Class: CfgVehicles|rhs_mi28_base|Wheels|Wheel_2_1 [Indent level: 2],
        "wheel_2_1": {
            "steering": 1,
            "bonename": "Wheel_2_1_axis_damper",
            "suspforceapppointoffset": "Wheel_2_1_axis",
            "tireforceapppointoffset": "Wheel_2_1_axis",
            "center": "Wheel_2_1_axis",
            "boundary": "Wheel_2_1_bound",
            "width": 0.186,
            "susptraveldirection": [0,-1,0],
            "maxcompression": 0.18,
            "maxdroop": 0.12,
            "sprungmass": 100,
            "springstrength": 1580,
            "springdamperrate": 95120,
            "side": "left",
            "mass": 15,
            "moi": 0.768,
            "dampingrate": 1,
            "dampingratedamaged": 2,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 2000,
            "maxhandbraketorque": 0,
            "longitudinalstiffnessperunitgravity": 5000,
            "latstiffx": 2.5,
            "latstiffy": 18,
            "frictionvsslipgraph": [[0,1.3],[0.5,1],[1,1.6]]
        }
    },
    "gearretracting": 0,
    "driveoncomponent": ["wheels"],
    "lesh_canbetowed": 1,
    "lesh_towfromfront": 1,
    "lesh_axisoffsettarget": [-0.12,8.5,-2.21],
    "lesh_wheeloffset": [-0.12,1],
    "rhs_decalparameters": ["['Number',cRHSAIRMI28NumberPlaces,'AviaYellow']"],
    "dlc": "RHS_AFRF",
    "category": "Air",
    "crew": "rhs_pilot_combat_heli",
    "typicalcargo": ["rhs_pilot_combat_heli"],
    "maxspeed": 395,
    "fuelcapacity": 2130,
    "agm_fuelcapacity": 2130,
    "fuelconsumptionrate": 0.5,
    "mainbladeradius": 8.5,
    "tailbladeradius": 1.95,
    "tailbladevertical": 1,
    "tailbladecenter": "mala osa",
    "mainbladecenter": "rotor_center",
    "bodyfrictioncoef": 0.52,
    "backrotorforcecoef": 1,
    "liftforcecoef": 2,
    "altfullforce": 4000,
    "altnoforce": 6000,
    "mainrotorspeed": -1,
    "backrotorspeed": -1,
    "numberphysicalwheels": 3,
    # Class: CfgVehicles|rhs_mi28_base|RotorLibHelicopterProperties [Indent level: 1],
    "rotorlibhelicopterproperties": {
        "rtd_center": "rtd_center",
        "rtdconfig": "rhsafrf|addons|rhs_c_mi28|rotorlib|RTD_Mi28.xml",
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
    "availableforsupporttypes": ["CAS_Heli"],
    "audible": 7,
    "camshakecoef": 0.6,
    "scope": 1,
    "mapsize": 16,
    "vehicleclass": "rhs_vehclass_helicopter",
    "editorsubcategory": "rhs_EdSubcat_helicopter",
    "model": "rhsafrf|addons|rhs_mi28|rhs_mi28",
    "icon": "rhsafrf|addons|rhs_a2port_air|data|map_ico|icon_mi24_ca.paa",
    "picture": "rhsafrf|addons|rhs_a2port_air|data|ico|rhs_mi24p_pic_ca.paa",
    "getinradius": 2,
    "gunnerusespilotview": 1,
    "allowtablock": 0,
    # Class: CfgVehicles|rhs_mi28_base|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass [Indent level: 2]
        "mfd_left_compass": {
            "topleft": "mfd_left_compass_lt",
            "topright": "mfd_left_compass_rt",
            "bottomleft": "mfd_left_compass_lb",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "enableparallax": 0,
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Bones|Compass_text [Indent level: 4]
                "compass_text": {
                    "type": "fixed",
                    "pos": [0.5,0.53]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Bones|Speed_text [Indent level: 4],
                "speed_text": {
                    "pos": [0.192,0.225],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Bones|VSpeed_text [Indent level: 4],
                "vspeed_text": {
                    "pos": [0.812,0.225],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Bones|Alt_radar_text [Indent level: 4],
                "alt_radar_text": {
                    "pos": [0.192,0.599],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Bones|Alt_baro_text [Indent level: 4],
                "alt_baro_text": {
                    "pos": [0.812,0.592],
                    "type": "fixed"
                }
            },
            # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.95,
                "color": [1,1,1],
                "condition": "on",
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Draw|Compass [Indent level: 4],
                "compass": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "Heading",
                    "sourcescale": 1,
                    "pos": ["Compass_text",[-0,-0.015],1],
                    "right": ["Compass_text",[0.025,-0.015],1],
                    "down": ["Compass_text",[-0,0.015],1]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Draw|Speed [Indent level: 4],
                "speed": {
                    "source": "speed",
                    "sourcescale": 3.6,
                    "pos": ["Speed_text",[-0,-0.015],1],
                    "right": ["Speed_text",[0.025,-0.015],1],
                    "down": ["Speed_text",[-0,0.015],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Draw|VSpeed [Indent level: 4],
                "vspeed": {
                    "source": "vspeed",
                    "pos": ["VSpeed_text",[-0,-0.015],1],
                    "right": ["VSpeed_text",[0.025,-0.015],1],
                    "down": ["VSpeed_text",[-0,0.015],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Draw|Alt_Radar [Indent level: 4],
                "alt_radar": {
                    "source": "altitudeAGL",
                    "max": 300,
                    "pos": ["Alt_radar_text",[-0,-0.015],1],
                    "right": ["Alt_radar_text",[0.025,-0.015],1],
                    "down": ["Alt_radar_text",[-0,0.015],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Left_Compass|Draw|Alt_Baro [Indent level: 4],
                "alt_baro": {
                    "source": "altitudeASL",
                    "max": 10000,
                    "pos": ["Alt_baro_text",[-0,-0.015],1],
                    "right": ["Alt_baro_text",[0.025,-0.015],1],
                    "down": ["Alt_baro_text",[-0,0.015],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "sourcescale": 1
                }
            }
        },
        # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass [Indent level: 2],
        "mfd_gunner_left_compass": {
            "topleft": "mfd_gunner_left_compass_lt",
            "topright": "mfd_gunner_left_compass_rt",
            "bottomleft": "mfd_gunner_left_compass_lb",
            # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Bones|Compass_text [Indent level: 4]
                "compass_text": {
                    "type": "fixed",
                    "pos": [0.5,0.53]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Bones|Speed_text [Indent level: 4],
                "speed_text": {
                    "pos": [0.192,0.225],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Bones|VSpeed_text [Indent level: 4],
                "vspeed_text": {
                    "pos": [0.812,0.225],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Bones|Alt_radar_text [Indent level: 4],
                "alt_radar_text": {
                    "pos": [0.192,0.599],
                    "type": "fixed"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Bones|Alt_baro_text [Indent level: 4],
                "alt_baro_text": {
                    "pos": [0.812,0.592],
                    "type": "fixed"
                }
            },
            # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.95,
                "color": [1,1,1],
                "condition": "on",
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Draw|Compass [Indent level: 4],
                "compass": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "Heading",
                    "sourcescale": 1,
                    "pos": ["Compass_text",[-0,-0.015],1],
                    "right": ["Compass_text",[0.025,-0.015],1],
                    "down": ["Compass_text",[-0,0.015],1]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Draw|Speed [Indent level: 4],
                "speed": {
                    "source": "speed",
                    "sourcescale": 3.6,
                    "pos": ["Speed_text",[-0,-0.015],1],
                    "right": ["Speed_text",[0.025,-0.015],1],
                    "down": ["Speed_text",[-0,0.015],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Draw|VSpeed [Indent level: 4],
                "vspeed": {
                    "source": "vspeed",
                    "pos": ["VSpeed_text",[-0,-0.015],1],
                    "right": ["VSpeed_text",[0.025,-0.015],1],
                    "down": ["VSpeed_text",[-0,0.015],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Draw|Alt_Radar [Indent level: 4],
                "alt_radar": {
                    "source": "altitudeAGL",
                    "max": 300,
                    "pos": ["Alt_radar_text",[-0,-0.015],1],
                    "right": ["Alt_radar_text",[0.025,-0.015],1],
                    "down": ["Alt_radar_text",[-0,0.015],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "sourcescale": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Left_Compass|Draw|Alt_Baro [Indent level: 4],
                "alt_baro": {
                    "source": "altitudeASL",
                    "max": 10000,
                    "pos": ["Alt_baro_text",[-0,-0.015],1],
                    "right": ["Alt_baro_text",[0.025,-0.015],1],
                    "down": ["Alt_baro_text",[-0,0.015],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "sourcescale": 1
                }
            },
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,1,0,0.1],
            "enableparallax": 0,
            "font": "rhs_digital_font_var"
        },
        # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Right_Gun [Indent level: 2],
        "mfd_right_gun": {
            "topleft": "mfd_right_gun_lt",
            "topright": "mfd_right_gun_rt",
            "bottomleft": "mfd_right_gun_lb",
            "color": [0,1,0,0.1],
            # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Right_Gun|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Right_Gun|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.5,0.65]
                }
            },
            # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Right_Gun|Draw [Indent level: 3],
            "draw": {
                "alpha": 1,
                "color": [0.1,0.8,0],
                "condition": "on",
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Right_Gun|Draw|Speed [Indent level: 4],
                "speed": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "pos": ["PlaneW",[-0.3,"-0.53+-0.2."],1],
                    "right": ["PlaneW",["-0.3+0.16","-0.53+-0.2"],1],
                    "down": ["PlaneW",[-0.3,"0.43+-0.2"],1]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Right_Gun|Draw|Height [Indent level: 4],
                "height": {
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "format": "%3.0f",
                    "pos": ["PlaneW",[0.39,"-0.53+-0.2"],1],
                    "right": ["PlaneW",["0.39+0.16","-0.53+-0.2"],1],
                    "down": ["PlaneW",[0.39,"0.43+-0.2"],1],
                    "type": "text",
                    "align": "left",
                    "scale": 1
                }
            },
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "enableparallax": 0,
            "font": "rhs_digital_font_var"
        },
        # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Right_Gun [Indent level: 2],
        "mfd_gunner_right_gun": {
            "topleft": "mfd_gunner_right_gun_lt",
            "topright": "mfd_gunner_right_gun_rt",
            "bottomleft": "mfd_gunner_right_gun_lb",
            # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Right_Gun|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Right_Gun|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.5,0.65]
                }
            },
            # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Right_Gun|Draw [Indent level: 3],
            "draw": {
                "alpha": 1,
                "color": [0.1,0.8,0],
                "condition": "on",
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Right_Gun|Draw|Speed [Indent level: 4],
                "speed": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "speed",
                    "sourcescale": 3.6,
                    "pos": ["PlaneW",[-0.3,"-0.53+-0.2."],1],
                    "right": ["PlaneW",["-0.3+0.16","-0.53+-0.2"],1],
                    "down": ["PlaneW",[-0.3,"0.43+-0.2"],1]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|MFD_Gunner_Right_Gun|Draw|Height [Indent level: 4],
                "height": {
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "format": "%3.0f",
                    "pos": ["PlaneW",[0.39,"-0.53+-0.2"],1],
                    "right": ["PlaneW",["0.39+0.16","-0.53+-0.2"],1],
                    "down": ["PlaneW",[0.39,"0.43+-0.2"],1],
                    "type": "text",
                    "align": "left",
                    "scale": 1
                }
            },
            "color": [0,1,0,0.1],
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "enableparallax": 0,
            "font": "rhs_digital_font_var"
        },
        # Class: CfgVehicles|rhs_mi28_base|MFD|CrossGunner [Indent level: 2],
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
            # Class: CfgVehicles|rhs_mi28_base|MFD|CrossGunner|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhs_mi28_base|MFD|CrossGunner|Bones|WeaponAim [Indent level: 4]
                "weaponaim": {
                    "type": "vector",
                    "source": "weapon",
                    "pos0": ["0.50  - 0.02","0.31  + 0.03"],
                    "pos10": [1.126,0.9138]
                }
            },
            # Class: CfgVehicles|rhs_mi28_base|MFD|CrossGunner|Draw [Indent level: 3],
            "draw": {
                "alpha": 0.95,
                "color": [0.15,1,0.15],
                "condition": "on",
                # Class: CfgVehicles|rhs_mi28_base|MFD|CrossGunner|Draw|MGun [Indent level: 4],
                "mgun": {
                    # Class: CfgVehicles|rhs_mi28_base|MFD|CrossGunner|Draw|MGun|Circle [Indent level: 5]
                    "circle": {
                        "type": "line",
                        "width": 4,
                        "points": [["WeaponAim",[0,0.02],1],["WeaponAim",[0,0.01],1],[],["WeaponAim",[0,-0.01],1],["WeaponAim",[0,-0.02],1],[],["WeaponAim",[0.02,0],1],["WeaponAim",[0.01,0],1],[],["WeaponAim",[-0.01,0],1],["WeaponAim",[-0.02,0],1],[]]
                    }
                }
            }
        },
        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD [Indent level: 2],
        "airplanehud": {
            # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Pos10Vector [Indent level: 3]
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
            # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.502,0.49]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|ImpactPoint [Indent level: 4],
                "impactpoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.31],
                    "pos10": [1.146,0.8838]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|Limit0109 [Indent level: 4],
                "limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot1 [Indent level: 4],
                "missileflighttimerot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minangle": 0,
                    "maxangle": 18,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot2 [Indent level: 4],
                "missileflighttimerot2": {
                    "maxangle": 37,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot3 [Indent level: 4],
                "missileflighttimerot3": {
                    "maxangle": 55.5,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot4 [Indent level: 4],
                "missileflighttimerot4": {
                    "maxangle": 74,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot5 [Indent level: 4],
                "missileflighttimerot5": {
                    "maxangle": 92.5,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot6 [Indent level: 4],
                "missileflighttimerot6": {
                    "maxangle": 111,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot7 [Indent level: 4],
                "missileflighttimerot7": {
                    "maxangle": 129.5,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot8 [Indent level: 4],
                "missileflighttimerot8": {
                    "maxangle": 148,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot9 [Indent level: 4],
                "missileflighttimerot9": {
                    "maxangle": 166.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot10 [Indent level: 4],
                "missileflighttimerot10": {
                    "maxangle": 185,
                    "max": 10,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot11 [Indent level: 4],
                "missileflighttimerot11": {
                    "maxangle": 203.5,
                    "max": 11,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot12 [Indent level: 4],
                "missileflighttimerot12": {
                    "maxangle": 222,
                    "max": 12,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot13 [Indent level: 4],
                "missileflighttimerot13": {
                    "maxangle": 240.5,
                    "max": 13,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot14 [Indent level: 4],
                "missileflighttimerot14": {
                    "maxangle": 259,
                    "max": 14,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot15 [Indent level: 4],
                "missileflighttimerot15": {
                    "maxangle": 277.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot16 [Indent level: 4],
                "missileflighttimerot16": {
                    "maxangle": 296,
                    "max": 16,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot17 [Indent level: 4],
                "missileflighttimerot17": {
                    "maxangle": 314.5,
                    "max": 17,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot18 [Indent level: 4],
                "missileflighttimerot18": {
                    "maxangle": 333,
                    "max": 18,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot19 [Indent level: 4],
                "missileflighttimerot19": {
                    "maxangle": 351.5,
                    "max": 19,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|MissileFlightTimeRot20 [Indent level: 4],
                "missileflighttimerot20": {
                    "maxangle": 370,
                    "max": 20,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 0.888235
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|ForwardVector [Indent level: 4],
                "forwardvector": {
                    "type": "vector",
                    "source": "forward",
                    "pos0": [0,0],
                    "pos10": [0.347,0.345]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|Target [Indent level: 4],
                "target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.31],
                    "pos10": [1.146,0.8838]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.502,0.49],
                    "pos10": [0.563,0.544]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|SliderSpeedSource [Indent level: 4],
                "sliderspeedsource": {
                    "type": "linear",
                    "source": "speed",
                    "min": 0,
                    "max": 138.889,
                    "minpos": [0.255,0.2],
                    "maxpos": [0.255,0.525]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|AGLMove [Indent level: 4],
                "aglmove": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "min": 0,
                    "max": 1000,
                    "minpos": [0,"0.15*0.65"],
                    "maxpos": [0,"0.65*0.65"]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|Heading_number_anchor [Indent level: 4],
                "heading_number_anchor": {
                    "type": "fixed",
                    "pos": [0.498,0.035]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|Heading [Indent level: 4],
                "heading": {
                    "type": "linear",
                    "source": "Heading",
                    "min": -36,
                    "max": 36,
                    "minpos": [0,0],
                    "maxpos": [1,0]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|TargetDistanceMissile [Indent level: 4],
                "targetdistancemissile": {
                    "type": "rotational",
                    "source": "targetDist",
                    "center": [0,0],
                    "min": 100,
                    "max": 3000,
                    "minangle": -120,
                    "maxangle": 120
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|vspeed [Indent level: 4],
                "vspeed": {
                    "source": "vspeed",
                    "type": "linear",
                    "min": -30,
                    "max": 30,
                    "minpos": [0,0.06],
                    "maxpos": [0,0.3]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|HorizonBankMGun [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|HorizonDive [Indent level: 4],
                "horizondive": {
                    "source": "horizonDive",
                    "type": "linear",
                    "min": -1,
                    "max": 1,
                    "minpos": [0.502,2.49],
                    "maxpos": [0.502,-1.51]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|HorizonBankReverted [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],
                "level0": {
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelP5 [Indent level: 4],
                "levelp5": {
                    "angle": 5,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelM5 [Indent level: 4],
                "levelm5": {
                    "angle": -5,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": 10,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": -10,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": 15,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": -15,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": 20,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": -20,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": 25,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": -25,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": 30,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": -30,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": 35,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": -35,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": 40,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": -40,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": 45,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": -45,
                    "pos0": [0.5,0.46],
                    "pos10": [1.384,1.2452],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw [Indent level: 3],
            "draw": {
                "alpha": 1,
                "color": [0.15,1,0.15],
                "condition": "on",
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|MGunD [Indent level: 4],
                "mgund": {
                    "condition": "mgun+rocket+bomb",
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|MGunD|Cross [Indent level: 5],
                    "cross": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0266471],1],["ImpactPoint",[0,-0.0355294],1],[],["ImpactPoint",[0.02,-0.024],1],["ImpactPoint",[0.025,-0.031],1],[],["ImpactPoint",[0,-0.002],1],["ImpactPoint",[0,0.002],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[]]
                    },
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|MGunD|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0310882],1],["MissileFlightTimeRot1",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot18",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot19",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.035],1,"ImpactPoint",1]]
                    },
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|MGunD|Circle_Min_Range [Indent level: 5],
                    "circle_min_range": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0266471],1],["ImpactPoint",[0.005208,-0.026242],1],["ImpactPoint",[0.01026,-0.0250402],1],["ImpactPoint",[0.015,-0.0230763],1],["ImpactPoint",[0.019284,-0.0204116],1],["ImpactPoint",[0.02298,-0.0171287],1],["ImpactPoint",[0.02598,-0.0133235],1],["ImpactPoint",[0.028191,-0.00911329],1],["ImpactPoint",[0.029544,-0.00462593],1],["ImpactPoint",[0.03,0],1],["ImpactPoint",[0.029544,0.00462593],1],["ImpactPoint",[0.028191,0.00911329],1],["ImpactPoint",[0.02598,0.0133235],1],["ImpactPoint",[0.02298,0.0171287],1],["ImpactPoint",[0.019284,0.0204116],1],["ImpactPoint",[0.015,0.0230763],1],["ImpactPoint",[0.01026,0.0250402],1],["ImpactPoint",[0.005208,0.026242],1],["ImpactPoint",[0,0.0266471],1],["ImpactPoint",[-0.005208,0.026242],1],["ImpactPoint",[-0.01026,0.0250402],1],["ImpactPoint",[-0.015,0.0230763],1],["ImpactPoint",[-0.019284,0.0204116],1],["ImpactPoint",[-0.02298,0.0171287],1],["ImpactPoint",[-0.02598,0.0133235],1],["ImpactPoint",[-0.028191,0.00911329],1],["ImpactPoint",[-0.029544,0.00462593],1],["ImpactPoint",[-0.03,0],1],["ImpactPoint",[-0.029544,-0.00462593],1],["ImpactPoint",[-0.028191,-0.00911329],1],["ImpactPoint",[-0.02598,-0.0133235],1],["ImpactPoint",[-0.02298,-0.0171287],1],["ImpactPoint",[-0.019284,-0.0204116],1],["ImpactPoint",[-0.015,-0.0230763],1],["ImpactPoint",[-0.01026,-0.0250402],1],["ImpactPoint",[-0.005208,-0.026242],1],["ImpactPoint",[0,-0.0266471],1]]
                    },
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|MGunD|Distance [Indent level: 5],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Static2 [Indent level: 4],
                "static2": {
                    "cliptl": [0,0.5],
                    "clipbr": [1,0],
                    "points": [["PlaneW",[-0.21,"7.34351e-009--0.12"],1],["PlaneW",[-0.28,"9.79135e-009--0.12"],1],[],["PlaneW",[0.21,"-2.00338e-009--0.12"],1],["PlaneW",[0.28,"-2.67117e-009--0.12"],1],[],["PlaneW",[-0.105,"0.145492--0.12"],1],["PlaneW",[-0.14,"0.19399--0.12"],1],[],["PlaneW",[0.105,"0.145492--0.12"],1],["PlaneW",[0.14,"0.19399--0.12"],1],[],["PlaneW",[-0.181865,"0.084--0.12"],1],["PlaneW",[-0.242487,"0.112--0.12"],1],[],["PlaneW",[0.181865,"0.084--0.12"],1],["PlaneW",[0.242487,"0.112--0.12"],1],[],["PlaneW",[-0.202844,"0.0434816--0.12"],1],["PlaneW",[-0.270459,"0.0579755--0.12"],1],[],["PlaneW",[0.202844,"0.0434816--0.12"],1],["PlaneW",[0.270459,"0.0579755--0.12"],1],[],["PlaneW",[-0.209201,"0.0146422--0.12"],1],["PlaneW",[-0.244068,"0.0170825--0.12"],1],[],["PlaneW",[-0.20681,"0.0291729--0.12"],1],["PlaneW",[-0.241278,"0.034035--0.12"],1],[],["PlaneW",[0.20681,"0.0291729--0.12"],1],["PlaneW",[0.241278,"0.034035--0.12"],1],[],["PlaneW",[0.209201,"0.0146422--0.12"],1],["PlaneW",[0.244068,"0.0170825--0.12"],1],[]],
                    "type": "line"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|HorizonBank [Indent level: 4],
                "horizonbank": {
                    "points": [["PlaneW",1,"HorizonBankReverted",["0.21-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.14-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.11-0.50","-0.035-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.08-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.03-0.50","0-0.50"],1],[],["PlaneW",1,"HorizonBankReverted",["-0.21-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.14-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.11-0.50","-0.035-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.08-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.03-0.50","0-0.50"],1],[],["PlaneW",1,"HorizonBankReverted",["0-0.50","-0.004-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0-0.50","0.004-0.50"],1]],
                    "type": "line"
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|CollectiveGroup [Indent level: 4],
                "collectivegroup": {
                    "condition": "simulRTD",
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|CollectiveGroup|CollectiveText [Indent level: 5],
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
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|CollectiveGroup|CollectiveNumber [Indent level: 5],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0.25,0.25],
                    "clipbr": [0.75,0.75],
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "level0": {
                            "type": "line",
                            "width": 4,
                            "points": [["Level0",[-0.28,0],1],["Level0",[-0.175,0],1],[],["Level0",[-0.063,0],1],["Level0",[-0.007,0],1],[],["Level0",[0.007,0],1],["Level0",[0.063,0],1],[],["Level0",[0.175,0],1],["Level0",[0.28,0],1]]
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM5 [Indent level: 6],
                        "levelm5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.32,0],1],["LevelM5",[-0.22,0],1],[],["LevelM5",[0.22,0],1],["LevelM5",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_5 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_5L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP5 [Indent level: 6],
                        "levelp5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.32,0],1],["LevelP5",[-0.22,0],1],[],["LevelP5",[0.22,0],1],["LevelP5",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_5 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_5L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM10 [Indent level: 6],
                        "levelm10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.32,0],1],["LevelM10",[-0.22,0],1],[],["LevelM10",[0.22,0],1],["LevelM10",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_10 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_10L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP10 [Indent level: 6],
                        "levelp10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.32,0],1],["LevelP10",[-0.22,0],1],[],["LevelP10",[0.22,0],1],["LevelP10",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_10 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_10L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM15 [Indent level: 6],
                        "levelm15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.32,0],1],["LevelM15",[-0.22,0],1],[],["LevelM15",[0.22,0],1],["LevelM15",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_15 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_15L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP15 [Indent level: 6],
                        "levelp15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.32,0],1],["LevelP15",[-0.22,0],1],[],["LevelP15",[0.22,0],1],["LevelP15",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_15 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_15L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM20 [Indent level: 6],
                        "levelm20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.32,0],1],["LevelM20",[-0.22,0],1],[],["LevelM20",[0.22,0],1],["LevelM20",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_20 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_20L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP20 [Indent level: 6],
                        "levelp20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.32,0],1],["LevelP20",[-0.22,0],1],[],["LevelP20",[0.22,0],1],["LevelP20",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_20 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_20L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM25 [Indent level: 6],
                        "levelm25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.32,0],1],["LevelM25",[-0.22,0],1],[],["LevelM25",[0.22,0],1],["LevelM25",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_25 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_25L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP25 [Indent level: 6],
                        "levelp25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.32,0],1],["LevelP25",[-0.22,0],1],[],["LevelP25",[0.22,0],1],["LevelP25",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_25 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_25L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM30 [Indent level: 6],
                        "levelm30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.32,0],1],["LevelM30",[-0.22,0],1],[],["LevelM30",[0.22,0],1],["LevelM30",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_30 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_30L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP30 [Indent level: 6],
                        "levelp30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.32,0],1],["LevelP30",[-0.22,0],1],[],["LevelP30",[0.22,0],1],["LevelP30",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_30 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_30L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM35 [Indent level: 6],
                        "levelm35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.32,0],1],["LevelM35",[-0.22,0],1],[],["LevelM35",[0.22,0],1],["LevelM35",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_35 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_35L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP35 [Indent level: 6],
                        "levelp35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.32,0],1],["LevelP35",[-0.22,0],1],[],["LevelP35",[0.22,0],1],["LevelP35",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_35 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_35L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM40 [Indent level: 6],
                        "levelm40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.32,0],1],["LevelM40",[-0.22,0],1],[],["LevelM40",[0.22,0],1],["LevelM40",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_40 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_40L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP40 [Indent level: 6],
                        "levelp40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.32,0],1],["LevelP40",[-0.22,0],1],[],["LevelP40",[0.22,0],1],["LevelP40",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_40 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_40L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM45 [Indent level: 6],
                        "levelm45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.32,0],1],["LevelM45",[-0.22,0],1],[],["LevelM45",[0.22,0],1],["LevelM45",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_45 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_45L [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP45 [Indent level: 6],
                        "levelp45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.32,0],1],["LevelP45",[-0.22,0],1],[],["LevelP45",[0.22,0],1],["LevelP45",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_45 [Indent level: 6],
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
                        # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_45L [Indent level: 6],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|Static [Indent level: 4],
                "static": {
                    "type": "line",
                    "width": 4,
                    "points": [["vspeed",[0.22,0.56],1],["vspeed",[0.205,0.55],1],["vspeed",[0.22,0.54],1],["vspeed",[0.22,0.56],1],[],[[0.2,0.598],1],[[0.2,0.782],1],[],[[0.2,0.61],1],[[0.18,0.61],1],[],[[0.195,0.77],1],[[0.18,0.77],1],[],[[0.195,0.65],1],[[0.18,0.65],1],[],[[0.195,0.69],1],[[0.18,0.69],1],[],[[0.195,0.73],1],[[0.18,0.73],1],[],["vspeed",[0.78,0.56],1],["vspeed",[0.795,0.55],1],["vspeed",[0.78,0.54],1],["vspeed",[0.78,0.56],1],[],[[0.8,0.598],1],[[0.8,0.862],1],[],[[0.8,0.61],1],[[0.83,0.61],1],[],[[0.805,0.85],1],[[0.83,0.85],1],[],[[0.805,0.65],1],[[0.82,0.65],1],[],[[0.805,0.69],1],[[0.82,0.69],1],[],[[0.805,0.73],1],[[0.83,0.73],1],[],[[0.805,0.77],1],[[0.82,0.77],1],[],[[0.805,0.81],1],[[0.82,0.81],1],[]]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|SpeedGroup [Indent level: 4],
                "speedgroup": {
                    "condition": "speed-2.78",
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|SpeedGroup|Static [Indent level: 5],
                    "static": {
                        "type": "line",
                        "width": 4,
                        "points": [["SliderSpeedSource",["0.015-0.03",0.01],1],["SliderSpeedSource",["0.000-0.03",0],1],["SliderSpeedSource",["0.015-0.03",-0.01],1],["SliderSpeedSource",["0.015-0.03",0.01],1],[],[["0.25-0.03",0.2],1],[["0.25-0.03",0.525],1],[],[["0.25-0.03",0.2],1],[["0.23-0.03",0.2],1],[],[["0.24-0.03",0.265],1],[["0.23-0.03",0.265],1],[],[["0.24-0.03",0.33],1],[["0.23-0.03",0.33],1],[],[["0.24-0.03",0.395],1],[["0.23-0.03",0.395],1],[],[["0.24-0.03",0.46],1],[["0.23-0.03",0.46],1],[],[["0.25-0.03",0.525],1],[["0.23-0.03",0.525],1],[]]
                    },
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|SpeedGroup|SpeedStatic500 [Indent level: 5],
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
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|SpeedGroup|SpeedStatic0 [Indent level: 5],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|AGL_Radar [Indent level: 4],
                "agl_radar": {
                    "condition": "1000-altitudeAGL",
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|AGL_Radar|Panel [Indent level: 5],
                    "panel": {
                        "width": 4,
                        "type": "line",
                        "points": [["AGLMove",[0.73,0.11],1],["AGLMove",[0.745,0.1],1],["AGLMove",[0.73,0.09],1],["AGLMove",[0.73,0.11],1],[],[[0.75,0.1975],1],[[0.75,0.5225],1],[],[[0.75,0.1975],1],[[0.77,0.1975],1],[],[[0.725,0.5225],1],[[0.775,0.5225],1],[],[[0.755,0.2625],1],[[0.77,0.2625],1],[],[[0.755,0.3275],1],[[0.77,0.3275],1],[],[[0.755,0.3925],1],[[0.77,0.3925],1],[],[[0.755,0.4575],1],[[0.77,0.4575],1],[]]
                    },
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|AGL_Radar|AltStatic50 [Indent level: 5],
                    "altstatic50": {
                        "type": "text",
                        "source": "static",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "right",
                        "text": 1000,
                        "pos": [[0.79,0.17],1],
                        "right": [[0.83,0.17],1],
                        "down": [[0.79,0.205],1]
                    }
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|RadarBoxes [Indent level: 4],
                "radarboxes": {
                    "type": "radar",
                    "pos0": [0.5,0.31],
                    "pos10": [1.146,0.8838],
                    "width": 4,
                    "points": [[[-0.002,-0.00177647],1],[[0.002,-0.00177647],1],[[0.002,0.00177647],1],[[-0.002,0.00177647],1],[[-0.002,-0.00177647],1]]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|TargetDiamond [Indent level: 4],
                "targetdiamond": {
                    # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|TargetDiamond|shape [Indent level: 5]
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0.02,0.0177647],1],["Target",1,"Limit0109",1,[-0.02,0.0177647],1],["Target",1,"Limit0109",1,[-0.02,-0.0177647],1],["Target",1,"Limit0109",1,[0.02,-0.0177647],1],["Target",1,"Limit0109",1,[0.02,0.0177647],1]]
                    }
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|SpeedNumber [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|AltNumber [Indent level: 4],
                "altnumber": {
                    "source": "altitudeAGL",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "sourceoffset": 0,
                    "align": "right",
                    "pos": [[0.76,0.07],1],
                    "right": [[0.84,0.07],1],
                    "down": [[0.76,0.12],1],
                    "type": "text",
                    "scale": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|AltNumberStatic [Indent level: 4],
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
                    "sourceoffset": 0
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|VspeedNumber [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|VspeedNumberStaticP30 [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|VspeedNumberStaticZERO [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|VspeedNumberStaticM30 [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|NevimStatic3 [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|NevimStaticZERO [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|NevimStatic1 [Indent level: 4],
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
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|HeadingArrows [Indent level: 4],
                "headingarrows": {
                    "type": "line",
                    "width": 4,
                    "points": [[["0.25","0.055+0.01+0.025"],1],[[0.75,"0.055+0.01+0.025"],1],[],[["0.5 - 0.016","0.09 - 0.018"],1],[[0.5,0.09],1],[["0.5 + 0.016","0.09 - 0.018"],1],[],[["0.5 - 0.035","0.055 - 0.018"],1],[["0.5 + 0.035","0.055 - 0.018"],1],[["0.5 + 0.035","0.055 + 0.018"],1],[["0.5 - 0.035","0.055 + 0.018"],1],[["0.5 - 0.035","0.055 - 0.018"],1],[]]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|HeadingText [Indent level: 4],
                "headingtext": {
                    "type": "text",
                    "source": "heading",
                    "align": "center",
                    "sourcescale": 1,
                    "scale": 1,
                    "pos": ["Heading_number_anchor",[0,0],1],
                    "right": ["Heading_number_anchor",["0 + 0.041",0],1],
                    "down": ["Heading_number_anchor",[0,"0  + 0.04"],1]
                },
                # Class: CfgVehicles|rhs_mi28_base|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],
                "headingscale": {
                    "type": "scale",
                    "source": "heading",
                    "horizontal": 1,
                    "sourcescale": 0.1,
                    "width": 3,
                    "top": 0.25,
                    "center": 0.5,
                    "bottom": 0.75,
                    "linexleft": 0.1,
                    "lineyright": 0.09,
                    "linexleftmajor": 0.11,
                    "lineyrightmajor": 0.09,
                    "majorlineeach": 2,
                    "numbereach": 2,
                    "step": 0.5,
                    "stepsize": 0.0555556,
                    "align": "center",
                    "scale": 1,
                    "pos": ["0.32-0.072","0.0+0.11"],
                    "right": ["0.35-0.072","0.0+0.11"],
                    "down": ["0.32-0.072","0.03+0.11"]
                }
            }
        }
    },
    "unitinfotype": "RHS_RscUnitInfoAir_Mi28",
    "hideweaponscargo": 1,
    "receiveremotetargets": 1,
    "reportremotetargets": 1,
    "reportownposition": 1,
    "irtarget": 1,
    "irtargetsize": 1,
    "visualtarget": 1,
    "visualtargetsize": 0.9,
    "radartarget": 1,
    "radartargetsize": 1,
    "lockdetectionsystem": "8",
    "incomingmissiledetectionsystem": "8+16",
    "gunnercansee": 55,
    "drivercansee": 55,
    # Class: CfgVehicles|rhs_mi28_base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|rhs_mi28_base|TransportMagazines|_xx_rhs_mag_nspn_red [Indent level: 2]
        "_xx_rhs_mag_nspn_red": {
            "magazine": "rhs_mag_nspn_red",
            "count": 10
        },
        # Class: CfgVehicles|rhs_mi28_base|TransportMagazines|_xx_rhs_mag_rdg2_white [Indent level: 2],
        "_xx_rhs_mag_rdg2_white": {
            "magazine": "rhs_mag_rdg2_white",
            "count": 4
        }
    },
    # Class: CfgVehicles|rhs_mi28_base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhs_mi28_base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 8
        },
        # Class: CfgVehicles|rhs_mi28_base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhs_mi28_base|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|rhs_mi28_base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
    "driverdoor": "Door_Pilot",
    "memorypointsgetincargo": "pos_cargo",
    "memorypointsgetincargodir": "pos_cargo_dir",
    "cargoaction": ["passenger_flatground_generic04"],
    "cargodoors": ["Hatch_Cargo"],
    "cargocompartments": ["Compartment3"],
    "viewcargoshadow": 1,
    "drivercaneject": 1,
    "drivercompartments": 1,
    "ejectspeed": [1,0,11],
    "cargogetinaction": ["GetInHeli_Transport_01Cargo"],
    "cargogetoutaction": ["RHS_HIND_Cargo_Exit"],
    "hiddenselections": ["camo1","camo2","camo3","tail_decals","n1","n2"],
    "hiddenselectionstextures": ["|rhsafrf|addons|rhs_mi28|data|rhs_mi28_01_grey_co.paa","|rhsafrf|addons|rhs_mi28|data|rhs_mi28_02_grey_co.paa","|rhsafrf|addons|rhs_mi28|data|rhs_mi28_03_exterior_grey_co.paa","rhsafrf|addons|rhs_decals|data|labels|aviation|vvs_ca.paa"],
    # Class: CfgVehicles|rhs_mi28_base|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhs_mi28_base|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Grey",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_mi28|data|rhs_mi28_01_grey_co.paa","|rhsafrf|addons|rhs_mi28|data|rhs_mi28_02_grey_co.paa","|rhsafrf|addons|rhs_mi28|data|rhs_mi28_03_exterior_grey_co.paa","rhsafrf|addons|rhs_decals|data|labels|aviation|vvs_ca.paa"],
            "factions": ["rhs_faction_vvs_c","rhs_faction_vvs"]
        },
        # Class: CfgVehicles|rhs_mi28_base|textureSources|Camo [Indent level: 2],
        "camo": {
            "displayname": "Camo",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_mi28|data|rhs_mi28_01_camo_co.paa","|rhsafrf|addons|rhs_mi28|data|rhs_mi28_02_camo_co.paa","|rhsafrf|addons|rhs_mi28|data|rhs_mi28_03_exterior_camo_co.paa","rhsafrf|addons|rhs_decals|data|labels|aviation|vvs_ca.paa"],
            "factions": ["rhs_faction_vvs_c","rhs_faction_vvs"]
        }
    },
    "texturelist": [],
    # Class: CfgVehicles|rhs_mi28_base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhs_mi28_base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_hideRadome [Indent level: 2],
        "rhs_hideradome": {
            "displayname": "Hide radome",
            "tooltip": "Hide the rotor-mounted radome",
            "property": "rhs_hideRadome",
            "control": "CheckboxNumber",
            "expression": "_this animate ['radome_hide',_value,true]",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "displayname": "Define font type of side number",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHSAIRMI28NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|NoChange [Indent level: 4]
                "nochange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|AviaYellow [Indent level: 4],
                "aviayellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|AviaBlue [Indent level: 4],
                "aviablue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultvalue": "AviaBlue"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|AviaRed [Indent level: 4],
                "aviared": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|AviaWhiteOut [Indent level: 4],
                "aviawhiteout": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|AviaCDF [Indent level: 4],
                "aviacdf": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4],
                "default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "displayname": "Set side number",
            "tooltip": "Set side number. 2 numbers are required. Type 0 to hide numbers completly",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRMI28NumberPlaces}else{[_this, [['Number', cRHSAIRMI28NumberPlaces, _this getVariable ['rhs_decalNumber_type','AviaYellow'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalTail [Indent level: 2],
        "rhs_decaltail": {
            "displayname": "Define tail decal",
            "tooltip": "Define tail decal that will be drawn on vehicle",
            "property": "rhs_decalTail",
            "control": "Combo",
            "expression": "[_this,[['Label', cRHSAIRMI28TailPlaces, 'Aviation',_value]]] call rhs_fnc_decalsInit",
            "defaultvalue": -1,
            "typename": "Number",
            # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalTail|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalTail|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": -1
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalTail|values|Empty [Indent level: 4],
                "empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles|rhs_mi28_base|Attributes|rhs_decalTail|values|VVS [Indent level: 4],
                "vvs": {
                    "name": "VVS Russia",
                    "value": 3,
                    "defaultvalue": 3
                }
            }
        }
    },
    "selectionhrotorstill": "velka vrtule staticka",
    "selectionhrotormove": "velka vrtule blur",
    "selectionvrotorstill": "mala vrtule staticka",
    "selectionvrotormove": "mala vrtule blur",
    "selectiondamage": "trup",
    "selectionshowdamage": "poskozeni",
    "slingloadmaxcargomass": 0,
    "precisegetinout": 1,
    "driveraction": "rhs_mi28_pilot",
    "driverinaction": "rhs_mi28_pilot",
    "getinaction": "pilot_Heli_Light_02_Enter",
    "getoutaction": "pilot_Heli_Light_02_Exit",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "driverlefthandanimname": "lever_pilot",
    "driverrighthandanimname": "stick_pilot",
    "driverleftleganimname": "pedalR",
    "driverrightleganimname": "pedalL",
    "memorypointlrocket": "rocket_1",
    "memorypointrrocket": "rocket_2",
    "memorypointlmissile": "missile_1",
    "memorypointrmissile": "missile_2",
    "memorypointgun": ["machinegun","machinegun2"],
    "gunbeg": ["muzzle_1","muzzle_2"],
    "gunend": ["chamber_1","chamber_2"],
    "particlespos": "chamber_1",
    "particlesdir": "muzzle_1",
    "primarygunner": 2,
    "weaponsgroup1": 128,
    "weaponsgroup4": 64,
    "weapons": ["rhs_weap_MASTERSAFE"],
    "magazines": [],
    "transportsoldier": 3,
    # Class: CfgVehicles|rhs_mi28_base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "body": "mainTurret",
            "gun": "mainGun",
            "weapons": ["rhs_weap_MASTERSAFE","rhs_weap_2a42"],
            "magazines": ["rhs_mag_3ubr11_125","rhs_mag_3uof8_125"],
            "gunbeg": "muzzle_1",
            "gunend": "chamber_1",
            "memorypointgun": "muzzle_1",
            "particlespos": "chamber_1",
            "particlesdir": "muzzle_1",
            "selectionfireanim": "zasleh",
            "maxhorizontalrotspeed": 1.6,
            "maxverticalrotspeed": 1.6,
            "initelev": 4,
            "initturn": 0,
            "maxelev": 13,
            "minelev": -40,
            "maxturn": 110,
            "minturn": -110,
            "gunneraction": "rhs_mi28_gunner",
            "gunnerinaction": "rhs_mi28_gunner",
            "gunnergetinaction": "Heli_Attack_01_Pilot_enter",
            "gunnergetoutaction": "Heli_Attack_01_Pilot_exit",
            "memorypointsgetingunnerprecise": "pos gunner",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "gunnerlefthandanimname": "stick_gunner",
            "gunnerrighthandanimname": "stick_gunner",
            "castgunnershadow": 1,
            "viewgunnershadow": 1,
            "precisegetinout": 1,
            "outgunnermayfire": 1,
            "commanding": -1,
            "primarygunner": 1,
            "iscopilot": 0,
            "caneject": 1,
            "gunnercompartments": "Compartment2",
            "canhidegunner": 0,
            "usepip": 1,
            "lodturnedin": 1100,
            "lodturnedout": 1100,
            "stabilizedinaxes": 3,
            "memorypointgunneroptics": "gunnerview",
            "memorypointgunneroutoptics": "gunnerview",
            "turretinfotype": "RHS_RscWeaponMi28_FCS",
            "gunnerdoor": "door_gunner",
            "canusescanners": 0,
            "allowtablock": 0,
            # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.155,
                "maxanglex": 50,
                "maxangley": 100,
                "maxfov": 0.155,
                "minanglex": -50,
                "minangley": -100,
                "minfov": 0.057
            },
            "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
            "gunneropticseffect": ["TankCommanderOptics1"],
            # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|OpticsIn|Samshin_WFOV [Indent level: 4]
                "samshin_wfov": {
                    "opticsdisplayname": "1",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mi28_3x",
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
                    "visionmode": ["Normal","TI"],
                    "hitpoint": "Hit_Optic_OPS28"
                },
                # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|OpticsIn|Samshin_NFOV [Indent level: 4],
                "samshin_nfov": {
                    "opticsdisplayname": "2",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mi28_15x",
                    "initfov": 0.102941,
                    "maxfov": 0.102941,
                    "minfov": 0.102941,
                    "initanglex": 0,
                    "initangley": 0,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "minanglex": -30,
                    "minangley": -100,
                    "thermalmode": [0,1],
                    "visionmode": ["Normal","TI"],
                    "hitpoint": "Hit_Optic_OPS28"
                },
                # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|OpticsIn|Samshin_NFOV_Stabilised [Indent level: 4],
                "samshin_nfov_stabilised": {
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mi28_30x",
                    "opticsdisplayname": "3",
                    "initfov": 0.0318182,
                    "maxfov": 0.0318182,
                    "minfov": 0.0318182,
                    "directionstabilized": 1,
                    "initanglex": 0,
                    "initangley": 0,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "minanglex": -30,
                    "minangley": -100,
                    "thermalmode": [0,1],
                    "visionmode": ["Normal","TI"],
                    "hitpoint": "Hit_Optic_OPS28"
                }
            },
            # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 5]
                    "components": {
                        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 6],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|UAVDisplay [Indent level: 6],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 6],
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
                # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    "defaultdisplay": "SensorDisplay",
                    # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 6]
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|CrewDisplay [Indent level: 6],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 6],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|UAVDisplay [Indent level: 6],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        # Class: CfgVehicles|rhs_mi28_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 6],
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
                }
            },
            "startengine": 0,
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
            "gunnerforceoptics": 0,
            "discretedistance": [100,200,300,400,500,600,700,800,1000,1200,1500,1800,2100,2500],
            "discretedistanceinitindex": 5,
            "showhmd": 0,
            "showalltargets": 4,
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
            "gunneroutopticscolor": [0,0,0,1],
            "gunneroutopticseffect": [],
            "gunneroutforceoptics": 0,
            "gunneroutopticsshowcursor": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "gunnerusespilotview": 0,
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "viewgunnerinexternal": 0,
            "lockwhendriverout": 0,
            "lockwhenvehiclespeed": -1,
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
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
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
    # Class: CfgVehicles|rhs_mi28_base|pilotCamera [Indent level: 1],
    "pilotcamera": {
        # Class: CfgVehicles|rhs_mi28_base|pilotCamera|OpticsIn [Indent level: 2]
        "opticsin": {
            # Class: CfgVehicles|rhs_mi28_base|pilotCamera|OpticsIn|Samshin_Pilot [Indent level: 3]
            "samshin_pilot": {
                "opticsdisplayname": "1",
                "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mi28_3x",
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
                "visionmode": ["Normal","TI"],
                "hitpoint": "Hit_Optic_TOES521"
            },
            # Class: CfgVehicles|rhs_mi28_base|pilotCamera|OpticsIn|Samshin_NFOV [Indent level: 3],
            "samshin_nfov": {
                "opticsdisplayname": "2",
                "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mi28_15x",
                "initfov": 0.102941,
                "maxfov": 0.102941,
                "minfov": 0.102941,
                "initanglex": 0,
                "initangley": 0,
                "maxanglex": 30,
                "maxangley": 100,
                "minanglex": -30,
                "minangley": -100,
                "thermalmode": [0,1],
                "visionmode": ["Normal","TI"],
                "hitpoint": "Hit_Optic_TOES521"
            },
            # Class: CfgVehicles|rhs_mi28_base|pilotCamera|OpticsIn|Samshin_NFOV_Stabilised [Indent level: 3],
            "samshin_nfov_stabilised": {
                "opticsdisplayname": "3",
                "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mi28_30x",
                "initfov": 0.0233333,
                "maxfov": 0.0233333,
                "minfov": 0.0233333,
                "directionstabilized": 1,
                "initanglex": 0,
                "initangley": 0,
                "maxanglex": 30,
                "maxangley": 100,
                "minanglex": -30,
                "minangley": -100,
                "thermalmode": [0,1],
                "visionmode": ["Normal","TI"],
                "hitpoint": "Hit_Optic_TOES521"
            },
            "showminimapinoptics": 0,
            "showuavviewpinoptics": 0,
            "showslingloadmanagerinoptics": 1
        },
        "minturn": -120,
        "maxturn": 120,
        "initturn": 0,
        "minelev": -13,
        "maxelev": 80,
        "initelev": 0,
        "maxxrotspeed": 0.3,
        "maxyrotspeed": 0.3,
        "pilotopticsshowcursor": 1,
        "controllable": 1
    },
    "memorypointdriveroptics": "toes521_view",
    "driverweaponsinfotype": "RHS_RscWeaponMi28_Pilot_FCS",
    # Class: CfgVehicles|rhs_mi28_base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhs_mi28_base|UserActions|SAFEMODE [Indent level: 2]
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
        # Class: CfgVehicles|rhs_mi28_base|UserActions|openDoor [Indent level: 2],
        "opendoor": {
            "displayname": "Lights front",
            "position": "",
            "priority": 0.01,
            "radius": 3,
            "onlyforplayer": 1,
            "showwindow": 0,
            "condition": "this doorPhase 'landingLights' < 0.5 AND alive this",
            "statement": "this animateDoor ['landingLights',1]"
        },
        # Class: CfgVehicles|rhs_mi28_base|UserActions|closeDoor [Indent level: 2],
        "closedoor": {
            "displayname": "Lights side",
            "condition": "this doorPhase 'landingLights' > 0.5 AND alive this",
            "statement": "this animateDoor ['landingLights',0]",
            "position": "",
            "priority": 0.01,
            "radius": 3,
            "onlyforplayer": 1,
            "showwindow": 0
        },
        # Class: CfgVehicles|rhs_mi28_base|UserActions|WheelBrakes [Indent level: 2],
        "wheelbrakes": {
            "displayname": "Toggle Wheel Brakes",
            "shortcut": "binocular",
            "condition": "!difficultyEnabledRTD && (call rhs_fnc_findPlayer) isEqualTo (driver this)",
            "statement": "[this] call rhs_fnc_heli_wheelBrakes",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showwindow": 0,
            "hideonuse": 1
        }
    },
    # Class: CfgVehicles|rhs_mi28_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhs_mi28_base|Exhausts|Exhaust01 [Indent level: 2]
        "exhaust01": {
            "direction": "exhaust1_dir",
            "position": "exhaust1",
            "effect": "ExhaustEffectHeli"
        },
        # Class: CfgVehicles|rhs_mi28_base|Exhausts|Exhaust02 [Indent level: 2],
        "exhaust02": {
            "direction": "exhaust2_dir",
            "position": "exhaust2",
            "effect": "ExhaustEffectHeli"
        }
    },
    "armor": 60,
    "armorstructural": 25,
    "damageresistance": 0.00555,
    "hulldamagecauseexplosion": 1,
    "epeimpulsedamagecoef": 1,
    "hullexplosiondelay": [10,30],
    # Class: CfgVehicles|rhs_mi28_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitHull [Indent level: 2]
        "hithull": {
            "simulation": "RHS_Hull_Helicopter",
            "armor": -250,
            "minimalhit": -0.2,
            "radius": 0.1,
            "explosionshielding": 0.15,
            "armorcomponent": "Hit_Hull",
            "name": "hull_hit",
            "visual": "zbytek",
            "passthrough": 1,
            # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitHull|DestructionEffects [Indent level: 3],
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
            "material": 51
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 1.3,
            "radius": 0.125,
            "minimalhit": 0.05,
            "explosionshielding": 1,
            "name": "fuel_hit",
            "convexcomponent": "fuel_hit",
            "visual": "zbytek",
            "material": 51,
            "passthrough": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 1.6,
            "radius": 0.4,
            "minimalhit": 0.15,
            "explosionshielding": 1.5,
            "visual": "podsvit pristroju",
            "name": "avionics_hit",
            "convexcomponent": "avionics_hit",
            "material": 51,
            "passthrough": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitEngine1 [Indent level: 2],
        "hitengine1": {
            "armor": -50,
            "radius": 0.35,
            "explosionshielding": 1,
            "minimalhit": 0.1,
            "name": "engine_1_hit",
            "armorcomponent": "Hit_Engine_1",
            "visual": "motor",
            "passthrough": 1,
            "convexcomponent": "engine_1_hit",
            "material": 51
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "name": "engine_2_hit",
            "armorcomponent": "Hit_Engine_2",
            "armor": -50,
            "radius": 0.35,
            "explosionshielding": 1,
            "minimalhit": 0.1,
            "visual": "motor",
            "passthrough": 1,
            "convexcomponent": "engine_1_hit",
            "material": 51
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 999,
            "visual": "camo2",
            "name": "engine_hit",
            "depends": "0.5 * (HitEngine1 + HitEngine2)",
            "armorcomponent": "Hit_Engine_2",
            "radius": 0.35,
            "explosionshielding": 1,
            "minimalhit": 0.1,
            "passthrough": 1,
            "convexcomponent": "engine_1_hit",
            "material": 51
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitWings [Indent level: 2],
        "hitwings": {
            "armor": 999,
            "explosionshielding": 1,
            "material": 51,
            "radius": 0.15,
            "passthrough": 0.1,
            "name": "hitwings",
            "visual": "-",
            # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitWings|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitWings|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "wing_explo1",
                    "interval": 1,
                    "intensity": 0.5,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitWings|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1,
                    "position": "wing_explo1"
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitWings|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "lifetime": 0.04,
                    "simulation": "particles",
                    "position": "wing_explo1",
                    "interval": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitWings|DestructionEffects|RHS_ERA_Flash2 [Indent level: 4],
                "rhs_era_flash2": {
                    "position": "wing_explo2",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "interval": 1,
                    "intensity": 0.5,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitWings|DestructionEffects|RHS_ERA_Sound2 [Indent level: 4],
                "rhs_era_sound2": {
                    "position": "wing_explo2",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitWings|DestructionEffects|RHS_ERA_Smoke2 [Indent level: 4],
                "rhs_era_smoke2": {
                    "position": "wing_explo2",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "lifetime": 0.04,
                    "simulation": "particles",
                    "interval": 1
                }
            }
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitTail [Indent level: 2],
        "hittail": {
            "armor": -150,
            "explosionshielding": 0.2,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.13,
            "armorcomponent": "Hit_Tail",
            "name": "Hit_Tail",
            "visual": "vis_tail"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitVRotor [Indent level: 2],
        "hitvrotor": {
            "armor": 1.5,
            "explosionshielding": 1,
            "material": 51,
            "radius": 0.45,
            "passthrough": 0.3,
            "name": "tail_rotor_hit",
            "visual": "mala vrtule staticka",
            "depends": "HitTail"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitHRotor [Indent level: 2],
        "hithrotor": {
            "armor": 1.5,
            "explosionshielding": 1,
            "material": 51,
            "radius": 0.45,
            "passthrough": 0.1,
            "name": "main_rotor_hit",
            "visual": "velka vrtule staticka"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitRotor [Indent level: 2],
        "hitrotor": {
            "armor": 999,
            "visual": "-",
            "name": "engine_hit",
            "depends": "(HitVRotor + HitHRotor)",
            "explosionshielding": 1,
            "material": 51,
            "radius": 0.45,
            "passthrough": 0.3
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|Hit_Radar [Indent level: 2],
        "hit_radar": {
            "armor": -30,
            "explosionshielding": 0,
            "name": "",
            "visual": "-",
            "armorcomponent": "Hit_Radar",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|Hit_Optic_TOES521 [Indent level: 2],
        "hit_optic_toes521": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "-",
            "armorcomponent": "Hit_Optic_TOES521",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|Hit_Optic_OPS28 [Indent level: 2],
        "hit_optic_ops28": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "-",
            "armorcomponent": "Hit_Optic_OPS28",
            "passthrough": 0
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": -40,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "armorcomponent": "glass1",
            "name": "glass1",
            "visual": "glass1"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitGlass2 [Indent level: 2],
        "hitglass2": {
            "armor": -40,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "armorcomponent": "glass2",
            "name": "glass2",
            "visual": "glass2"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "armor": -40,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "armorcomponent": "glass3",
            "name": "glass3",
            "visual": "glass3"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitGlass4 [Indent level: 2],
        "hitglass4": {
            "armor": -40,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "armorcomponent": "glass4",
            "name": "glass4",
            "visual": "glass4"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitGlass5 [Indent level: 2],
        "hitglass5": {
            "armor": -40,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "armorcomponent": "glass5",
            "name": "glass5",
            "visual": "glass5"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitGlass6 [Indent level: 2],
        "hitglass6": {
            "armor": -40,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "armorcomponent": "glass6",
            "name": "glass6",
            "visual": "glass6"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "armor": -40,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "armorcomponent": "glass7",
            "name": "glass7",
            "visual": "glass7"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitGlass8 [Indent level: 2],
        "hitglass8": {
            "armor": -40,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.1,
            "armorcomponent": "glass8",
            "name": "glass8",
            "visual": "glass8"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitGear [Indent level: 2],
        "hitgear": {
            "armor": -50,
            "explosionshielding": 0.01,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.13,
            "armorcomponent": "Hit_Gear",
            "name": "Hit_Gear",
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitHydraulics [Indent level: 2],
        "hithydraulics": {
            "armor": -50,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.13,
            "armorcomponent": "hit_hydraulics",
            "name": "hit_hydraulics",
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitTransmission [Indent level: 2],
        "hittransmission": {
            "armor": -80,
            "explosionshielding": 0.5,
            "passthrough": 0.1,
            "minimalhit": 0.1,
            "radius": 0.13,
            "armorcomponent": "hit_transmission",
            "name": "hit_transmission",
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon1 [Indent level: 2],
        "hitpylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            "depends": "HitWings",
            # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon2 [Indent level: 2],
        "hitpylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            "depends": "HitWings",
            # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon3 [Indent level: 2],
        "hitpylon3": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_3",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            "depends": "HitWings",
            # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon3|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon4 [Indent level: 2],
        "hitpylon4": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_4",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            "depends": "HitWings",
            # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon4|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|rhs_mi28_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles|Helicopter|HitPoints|HitLight [Indent level: 2],
        "hitlight": {
            "armor": 0.1,
            "material": -1,
            "name": "light",
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
    # Class: CfgVehicles|rhs_mi28_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_mi28|data|rhs_mi28_01.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_01_dam.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_01_des.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_02.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_02_dam.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_02_des.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_03.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_03_dam.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_03_des.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_glass.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_glass_dam.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_glass_dam.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_glass_int.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_glass_dam.rvmat","rhsafrf|addons|rhs_mi28|data|rhs_mi28_glass_dam.rvmat"]
    },
    # Class: CfgVehicles|rhs_mi28_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|Door_Gunner [Indent level: 2]
        "door_gunner": {
            "source": "door",
            "animperiod": 0.8
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|Door_Pilot [Indent level: 2],
        "door_pilot": {
            "source": "door",
            "animperiod": 0.8
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|Hatch_Cargo [Indent level: 2],
        "hatch_cargo": {
            "source": "door",
            "animperiod": 0.8
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|landingLights [Indent level: 2],
        "landinglights": {
            "animperiod": 1.4,
            "source": "door"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "weapon": "rhs_weap_2a42",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|elev [Indent level: 2],
        "elev": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|elev_bank [Indent level: 2],
        "elev_bank": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|offset [Indent level: 2],
        "offset": {
            "source": "user",
            "animperiod": 0.0002
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|radome_hide [Indent level: 2],
        "radome_hide": {
            "source": "user",
            "initphase": 0,
            "animperiod": 1e-005,
            "mass": 1,
            "displayname": "hide radar",
            "onphasechanged": "[(_this # 0),['ActiveRadarSensorComponent',(_this # 1) isEqualTo 0]] remoteExecCall ['enableVehicleSensor',0] ;"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|wings_hide [Indent level: 2],
        "wings_hide": {
            "source": "user",
            "initphase": 0,
            "animperiod": 1e-005
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|eject [Indent level: 2],
        "eject": {
            "animperiod": 0.3,
            "source": "user",
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|w_launch [Indent level: 2],
        "w_launch": {
            "source": "user",
            "initphase": 0,
            "animperiod": 1e-005
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|w_radar [Indent level: 2],
        "w_radar": {
            "source": "user",
            "initphase": 0,
            "animperiod": 1e-005
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|w_laser [Indent level: 2],
        "w_laser": {
            "source": "user",
            "initphase": 0,
            "animperiod": 1e-005
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|HitEngine1 [Indent level: 2],
        "hitengine1": {
            "source": "Hit",
            "hitpoint": "HitEngine1",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|HitEngine2 [Indent level: 2],
        "hitengine2": {
            "hitpoint": "HitEngine2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|HitGear [Indent level: 2],
        "hitgear": {
            "hitpoint": "hitgear",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|HitRotor [Indent level: 2],
        "hitrotor": {
            "hitpoint": "HitRotor",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|HitAvionics [Indent level: 2],
        "hitavionics": {
            "hitpoint": "HitAvionics",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|HitGlass7 [Indent level: 2],
        "hitglass7": {
            "hitpoint": "HitGlass7",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|HitGlass8 [Indent level: 2],
        "hitglass8": {
            "hitpoint": "HitGlass8",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|Damper_1_1_source [Indent level: 2],
        "damper_1_1_source": {
            "source": "damper",
            "wheel": "Wheel_1_1"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|Damper_1_2_source [Indent level: 2],
        "damper_1_2_source": {
            "source": "damper",
            "wheel": "Wheel_1_2"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|Damper_2_1_source [Indent level: 2],
        "damper_2_1_source": {
            "source": "damper",
            "wheel": "Wheel_2_1"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|Wheel_1_1_source [Indent level: 2],
        "wheel_1_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1_1"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|Wheel_1_2_source [Indent level: 2],
        "wheel_1_2_source": {
            "source": "wheel",
            "wheel": "Wheel_1_2"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|Wheel_2_1_source [Indent level: 2],
        "wheel_2_1_source": {
            "source": "wheel",
            "wheel": "Wheel_2_1"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|Helicopter_Brakes [Indent level: 2],
        "helicopter_brakes": {
            "source": "user",
            "animperiod": 0.01,
            "initphase": 1
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|hit_pylon_1_source [Indent level: 2],
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|hit_pylon_2_source [Indent level: 2],
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|hit_pylon_3_source [Indent level: 2],
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles|rhs_mi28_base|AnimationSources|hit_pylon_4_source [Indent level: 2],
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
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
    # Class: CfgVehicles|rhs_mi28_base|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|rhs_mi28_base|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|rhs_mi28_base|compartmentsLights|Comp1|Light_Pilot [Indent level: 3]
            "light_pilot": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 5.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|rhs_mi28_base|compartmentsLights|Comp1|Light_Pilot|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.55,
                    "hardlimitend": 0.75
                },
                "point": "light_pilot"
            }
        },
        # Class: CfgVehicles|rhs_mi28_base|compartmentsLights|Comp2 [Indent level: 2],
        "comp2": {
            # Class: CfgVehicles|rhs_mi28_base|compartmentsLights|Comp2|Light_Gunner [Indent level: 3]
            "light_gunner": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|rhs_mi28_base|compartmentsLights|Comp2|Light_Gunner|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 1.45,
                    "hardlimitend": 2.45
                },
                "point": "light_gunner"
            }
        },
        # Class: CfgVehicles|rhs_mi28_base|compartmentsLights|Comp3 [Indent level: 2],
        "comp3": {
            # Class: CfgVehicles|rhs_mi28_base|compartmentsLights|Comp3|Light_Cargo [Indent level: 3]
            "light_cargo": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|rhs_mi28_base|compartmentsLights|Comp3|Light_Cargo|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 1.45,
                    "hardlimitend": 2.45
                },
                "point": "light_cargo"
            }
        }
    },
    # Class: CfgVehicles|rhs_mi28_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhs_mi28_base|Reflectors|LightL [Indent level: 2]
        "lightl": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "intensity": 250,
            "size": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            "position": "l svetlo",
            "direction": "l svetlo konec",
            "hitpoint": "l svetlo",
            "selection": "l svetlo",
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1.5,
            # Class: CfgVehicles|rhs_mi28_base|Reflectors|LightL|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 400,
                "hardlimitend": 450
            }
        },
        # Class: CfgVehicles|rhs_mi28_base|Reflectors|LightR [Indent level: 2],
        "lightr": {
            "position": "p svetlo",
            "direction": "p svetlo konec",
            "hitpoint": "p svetlo",
            "selection": "p svetlo",
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "intensity": 250,
            "size": 1,
            "innerangle": 5,
            "outerangle": 75,
            "conefadecoef": 10,
            "useflare": 0,
            "daylight": 0,
            "flaresize": 1.5,
            # Class: CfgVehicles|rhs_mi28_base|Reflectors|LightL|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 400,
                "hardlimitend": 450
            }
        },
        # Class: CfgVehicles|rhs_mi28_base|Reflectors|LightLFlare [Indent level: 2],
        "lightlflare": {
            "position": "L_Flare",
            "useflare": 1,
            "outerangle": 175,
            "color": [10,10,9],
            "ambient": [10,10,9],
            "intensity": 250,
            "size": 1,
            "innerangle": 5,
            "conefadecoef": 10,
            "direction": "l svetlo konec",
            "hitpoint": "l svetlo",
            "selection": "l svetlo",
            "daylight": 0,
            "flaresize": 1.5,
            # Class: CfgVehicles|rhs_mi28_base|Reflectors|LightL|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 400,
                "hardlimitend": 450
            }
        },
        # Class: CfgVehicles|rhs_mi28_base|Reflectors|LightRFlare [Indent level: 2],
        "lightrflare": {
            "position": "R_Flare",
            "useflare": 1,
            "outerangle": 175,
            "color": [10,10,9],
            "ambient": [10,10,9],
            "direction": "p svetlo konec",
            "hitpoint": "p svetlo",
            "selection": "p svetlo",
            "intensity": 250,
            "size": 1,
            "innerangle": 5,
            "conefadecoef": 10,
            "daylight": 0,
            "flaresize": 1.5,
            # Class: CfgVehicles|rhs_mi28_base|Reflectors|LightL|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardlimitstart": 400,
                "hardlimitend": 450
            }
        }
    },
    "aggregatereflectors": [["LightL","LightLFlare"],["LightR","LightRFlare"]],
    # Class: CfgVehicles|rhs_mi28_base|markerlights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|rhs_mi28_base|markerlights|GreenStill [Indent level: 2]
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
        # Class: CfgVehicles|rhs_mi28_base|markerlights|RedStill [Indent level: 2],
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
        # Class: CfgVehicles|rhs_mi28_base|markerlights|WhiteStill [Indent level: 2],
        "whitestill": {
            "color": [0.8,0.8,0.8],
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
        # Class: CfgVehicles|rhs_mi28_base|markerlights|WhiteBlicking [Indent level: 2],
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
        # Class: CfgVehicles|rhs_mi28_base|markerlights|RedBlinking [Indent level: 2],
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
    # Class: CfgVehicles|rhs_mi28_base|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    # Class: CfgVehicles|rhs_mi28_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        "hit": "",
        # Class: CfgVehicles|rhs_mi28_base|EventHandlers|RHS_EventHandlers [Indent level: 2],
        "rhs_eventhandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "init": "_this call rhs_fnc_mi28_init",
            "postinit": "_this call rhs_fnc_reapplyTextures",
            "incomingmissile": "_this spawn rhs_fnc_rwr_mi28",
            "getout": "_this spawn rhs_fnc_mi28_ejection",
            "engine": "_this call rhs_fnc_addParachutes;"
        },
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    "features": "Randomization: No						<br />Camo selections: 2 - main body, turret with engines and wings						<br />Script door sources: door_L, door_R, door_L_pop, door_R_pop						<br />Script animations: None 						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: No						<br />Cargo proxy indexes: 1 to 8",
    "author": "Bohemia Interactive",
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
    "accuracy": 0.5,
    "crewvulnerable": 0,
    # Class: CfgVehicles|Heli_Attack_02_base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": "A multi-purpose successor to the Mi-24, the Mi-48 Kajman (BLUFOR designation `Hornet`) is a large gunship and attack helicopter with troop transport capacity for 8 passengers. The front part of the helicopter is based on the Mi-28 attack helicopter, but the hull is modified for passenger transport. The Kajman has a coaxial rotor providing increased stability. It is armed with a 30mm three-barrel Minigun, unguided Skyfire rockets and guided Skalpel AT missiles."
    },
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "maxfordingdepth": 0.75,
    "castdrivershadow": 1,
    "supplyradius": 2.5,
    "maximumload": 2000,
    "cargocaneject": 1,
    "cost": 3e+006,
    "threat": [0.8,1,0.8],
    "maxmainrotordive": 7,
    "minmainrotordive": -7,
    "neutralmainrotordive": 0,
    "laserscanner": 1,
    "showalltargets": 4,
    "enablemanualfire": 1,
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
    "defaultusermfdvalues": [0.25,1,0.25,1],
    "faction": "CIV_F",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "washdownstrength": "1.0f",
    "washdowndiameter": "40.0f",
    "minsmokedamage": 0.3,
    "maxsmokedamage": 0.99,
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
    # Class: CfgVehicles|Helicopter|ViewPilot [Indent level: 1],
    "viewpilot": {
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
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
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
    "cyclicforwardforcecoef": 1,
    "memorypointpilot": "pilot",
    "_mainbladecenter": "rotor_center",
    "enablesweep": 1,
    "envelope": [0,0.2,0.9,2.1,2.5,3.3,3.5,3.6,3.7,3.8,3.8,3,0.9,0.7,0.5],
    "minfiretime": 20,
    "steeraheadsimul": 0.5,
    "steeraheadplan": 0.7,
    # Class: CfgVehicles|Helicopter|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initanglex": 0,
        "minanglex": -40,
        "maxanglex": 17,
        "initangley": 0,
        "minangley": -100,
        "maxangley": 100,
        "initfov": 0.5,
        "minfov": 0.3,
        "maxfov": 1.2,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "soundlandinggear": ["",1,1],
    "slingloadmemorypoint": "slingLoad0",
    "extcameraparams": [-1],
    "camouflage": 100,
    "crewcrashprotection": 0.25,
    "headgforceleaningfactor": [0.01,0.0025,0.01],
    "damageeffect": "AirDestructionEffects",
    "type": 2,
    "transportmaxbackpacks": 1,
    "dammagehalf": [],
    "dammagefull": [],
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
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetincargoprecise": ["pos cargo"],
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "selectionclan": "clan",
    "selectiondashboard": "podsvit pristroju",
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
    "memorypointsupply": "doplnovani",
    "enablewatch": 0,
    "useprecisegetinaction": 0,
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