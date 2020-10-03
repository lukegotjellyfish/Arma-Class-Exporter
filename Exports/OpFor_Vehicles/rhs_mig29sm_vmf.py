rhs_mig29sm_vmf = {
    "author": "Red Hammer Studios",
    "editorPreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_mig29s_vmf.paa",
    "scope": 2,
    "faction": "rhs_faction_vmf",
    "textureList": ["Standard",1],
    "rhs_decalParameters": ["['Number',cRHSAIRMIG29NumberPlaces,'AviaBlue']","['Label', cRHSAIRMIG29StarPlaces, 'Aviation', 2]","['Label', cRHSAIRMIG29TailPlaces, 'Mig29TailSign', 1]","['Label', cRHSAIRMIG29NosePlaces, 'Mig29NoseArt', 2]"],
    "side": 0,
    "crew": "rhs_pilot",
    "typicalCargo": ["rhs_pilot"],
    "hiddenselectionstextures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_lgray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_lgray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_lgray_co.paa"],
    "displayName": "MiG-29SM",
    "model": "rhsafrf|addons|rhs_mig29|mig29sm.p3d",
    # Class: CfgVehicles\rhs_mig29sm_base\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\rhs_mig29sm_base\AnimationSources\Hide_TV
        "Hide_TV": {
            "source": "user",
            "initPhase": 0,
            "animPeriod": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\CollisionLightRed_source,
        "CollisionLightRed_source": {
            "source": "MarkerLight",
            "markerLight": "PositionRed"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\CollisionLightGreen_source,
        "CollisionLightGreen_source": {
            "source": "MarkerLight",
            "markerLight": "PositionGreen"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\CollisionLightWhite_source,
        "CollisionLightWhite_source": {
            "source": "MarkerLight",
            "markerLight": "PositionWhite"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\UserSunfilter,
        "UserSunfilter": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\fold_mirrors,
        "fold_mirrors": {
            "source": "user",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\switch_gear,
        "switch_gear": {
            "animPeriod": 0.8,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\switch_hud,
        "switch_hud": {
            "animPeriod": 0.8,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\switch_mastersafe,
        "switch_mastersafe": {
            "animPeriod": 0.8,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\afterburner_source,
        "afterburner_source": {
            "source": "user",
            "initPhase": 0,
            "animPeriod": 1.5
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\eject,
        "eject": {
            "source": "door",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\eject_hide,
        "eject_hide": {
            "source": "user",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\rwr_lights_lock,
        "rwr_lights_lock": {
            "source": "user",
            "initPhase": 0,
            "animPeriod": 8
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\rwr_lock_dir_primary,
        "rwr_lock_dir_primary": {
            "animPeriod": 0.1,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\rwr_lock_primary,
        "rwr_lock_primary": {
            "animPeriod": 1e-007,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\rwr_signal_strenght,
        "rwr_signal_strenght": {
            "animPeriod": 1e-007,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\HitEngine_1,
        "HitEngine_1": {
            "source": "hit",
            "hitpoint": "HitEngine"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\HitEngine_2,
        "HitEngine_2": {
            "source": "hit",
            "hitpoint": "HitEngine2"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\GSh_ammorandom,
        "GSh_ammorandom": {
            "source": "ammorandom",
            "weapon": "rhs_weap_GSh301"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\GSh_reload,
        "GSh_reload": {
            "source": "reload",
            "weapon": "rhs_weap_GSh301"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\rwr_lights,
        "rwr_lights": {
            "animPeriod": 1e-007,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\Damper_1_source,
        "Damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\Damper_2_source,
        "Damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\Damper_3_source,
        "Damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\Wheel_1_source,
        "Wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\Wheel_2_source,
        "Wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\Wheel_3_source,
        "Wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\hit_pylon_1_source,
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\hit_pylon_2_source,
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\hit_pylon_3_source,
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\hit_pylon_4_source,
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\hit_pylon_5_source,
        "hit_pylon_5_source": {
            "source": "Hit",
            "hitpoint": "HitPylon5"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\hit_pylon_6_source,
        "hit_pylon_6_source": {
            "source": "Hit",
            "hitpoint": "HitPylon6"
        },
        # Class: CfgVehicles\rhs_mig29s_base\AnimationSources\hit_pylon_7_source,
        "hit_pylon_7_source": {
            "source": "Hit",
            "hitpoint": "HitPylon7"
        }
    },
    "unitInfoType": "RHS_RscUnitInfoAir_MiG29SM",
    # Class: CfgVehicles\rhs_mig29sm_base\pilotCamera,
    "pilotCamera": {
        # Class: CfgVehicles\rhs_mig29sm_base\pilotCamera\OpticsIn
        "OpticsIn": {
            # Class: CfgVehicles\rhs_mig29sm_base\pilotCamera\OpticsIn\Wide
            "Wide": {
                "opticsDisplayName": "DEFAULT",
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.35,
                "minFov": 0.35,
                "maxFov": 0.35,
                "directionStabilized": 0,
                "visionMode": ["Normal","TI"],
                "thermalMode": [0,1],
                "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mig29sm_tv_1x.p3d"
            },
            # Class: CfgVehicles\rhs_mig29sm_base\pilotCamera\OpticsIn\Narrow,
            "Narrow": {
                "opticsDisplayName": "ZOOM",
                "initFov": 0.04375,
                "minFov": 0.04375,
                "maxFov": 0.04375,
                "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mig29sm_tv_1x.p3d",
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "directionStabilized": 0,
                "visionMode": ["Normal","TI"],
                "thermalMode": [0,1]
            },
            # Class: CfgVehicles\rhs_mig29sm_base\pilotCamera\OpticsIn\VeryNarrow,
            "VeryNarrow": {
                "opticsDisplayName": "ZOOM",
                "initFov": 0.0152174,
                "minFov": 0.0152174,
                "maxFov": 0.0152174,
                "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_mig29sm_tv_1x.p3d",
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "directionStabilized": 0,
                "visionMode": ["Normal","TI"],
                "thermalMode": [0,1]
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
    "memoryPointDriverOptics": "pilotCamera",
    # Class: CfgVehicles\rhs_mig29sm_base\Components,
    "Components": {
        # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent
        "TransportPylonsComponent": {
            "UIPicture": "rhsafrf|addons|rhs_mig29|data|loadouts|RHS_MiG29_EDEN_CA.paa",
            # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\pylons,
            "pylons": {
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\pylons\pylon1
                "pylon1": {
                    "hardpoints": ["RHS_HP_KH25_APU68_MIG29","RHS_HP_KH29_AKU58_MIG29","RHS_HP_FAB100_BD3_UMK2A","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB250_BD3_UMK2A","RHS_HP_FAB500_BD3_UMK2A","RHS_HP_KAB500_BD3_UMK2A","RHS_HP_KMGU2_BD3_UMK2A","RHS_HP_BD3_USK_A_O25L","RHS_HP_APU68_BD3_UMK2A","RHS_HP_B13L_BD3_UMK2A","RHS_HP_B8M1_BD3_UMK2A","RHS_HP_UB16_BD3_UMK2A","RHS_HP_UB32_BD3_UMK2A","RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R27_APU470","RHS_HP_R60_APU60","RHS_HP_R73_APU73","RHS_HP_PTB1150"],
                    "priority": 9,
                    "attachment": "rhs_mag_R27ER_APU470",
                    "maxweight": 1200,
                    "UIposition": [0.32,0.2],
                    "hitpoint": "HitPylon1"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\pylons\pylon2,
                "pylon2": {
                    "UIposition": [0.32,0.35],
                    "mirroredMissilePos": 1,
                    "hitpoint": "HitPylon2",
                    "hardpoints": ["RHS_HP_KH25_APU68_MIG29","RHS_HP_KH29_AKU58_MIG29","RHS_HP_FAB100_BD3_UMK2A","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB250_BD3_UMK2A","RHS_HP_FAB500_BD3_UMK2A","RHS_HP_KAB500_BD3_UMK2A","RHS_HP_KMGU2_BD3_UMK2A","RHS_HP_BD3_USK_A_O25L","RHS_HP_APU68_BD3_UMK2A","RHS_HP_B13L_BD3_UMK2A","RHS_HP_B8M1_BD3_UMK2A","RHS_HP_UB16_BD3_UMK2A","RHS_HP_UB32_BD3_UMK2A","RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R27_APU470","RHS_HP_R60_APU60","RHS_HP_R73_APU73","RHS_HP_PTB1150"],
                    "priority": 9,
                    "attachment": "rhs_mag_R27ER_APU470",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\pylons\pylon3,
                "pylon3": {
                    "hardpoints": ["RHS_HP_KH25_APU68_MIG29","RHS_HP_FAB100_BD3_UMK2A","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB250_BD3_UMK2A","RHS_HP_FAB500_BD3_UMK2A","RHS_HP_KAB500_BD3_UMK2A","RHS_HP_KMGU2_BD3_UMK2A","RHS_HP_BD3_USK_A_O25L","RHS_HP_APU68_BD3_UMK2A","RHS_HP_B13L_BD3_UMK2A","RHS_HP_B8M1_BD3_UMK2A","RHS_HP_UB16_BD3_UMK2A","RHS_HP_UB32_BD3_UMK2A","RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R60_APU60","RHS_HP_R73_APU73"],
                    "priority": 7,
                    "UIposition": [0.33,0.15],
                    "attachment": "rhs_mag_R73M_APU73",
                    "hitpoint": "HitPylon3",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\pylons\pylon4,
                "pylon4": {
                    "UIposition": [0.33,0.4],
                    "mirroredMissilePos": 3,
                    "hitpoint": "HitPylon4",
                    "hardpoints": ["RHS_HP_KH25_APU68_MIG29","RHS_HP_FAB100_BD3_UMK2A","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB250_BD3_UMK2A","RHS_HP_FAB500_BD3_UMK2A","RHS_HP_KAB500_BD3_UMK2A","RHS_HP_KMGU2_BD3_UMK2A","RHS_HP_BD3_USK_A_O25L","RHS_HP_APU68_BD3_UMK2A","RHS_HP_B13L_BD3_UMK2A","RHS_HP_B8M1_BD3_UMK2A","RHS_HP_UB16_BD3_UMK2A","RHS_HP_UB32_BD3_UMK2A","RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R60_APU60","RHS_HP_R73_APU73"],
                    "priority": 7,
                    "attachment": "rhs_mag_R73M_APU73",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\pylons\pylon5,
                "pylon5": {
                    "hardpoints": ["RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R60_APU60","RHS_HP_R73_APU73"],
                    "priority": 10,
                    "attachment": "rhs_mag_R73M_APU73",
                    "maxweight": 1200,
                    "UIposition": [0.34,0.1],
                    "hitpoint": "HitPylon5"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\pylons\pylon6,
                "pylon6": {
                    "UIposition": [0.34,0.45],
                    "mirroredMissilePos": 5,
                    "hitpoint": "HitPylon6",
                    "hardpoints": ["RHS_HP_R77M_AKU170_MIG29","RHS_HP_R77_AKU170_MIG29","RHS_HP_R60_APU60","RHS_HP_R73_APU73"],
                    "priority": 10,
                    "attachment": "rhs_mag_R73M_APU73",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\pylons\pylon7,
                "pylon7": {
                    "hardpoints": ["RHS_HP_PTB1500"],
                    "priority": 1,
                    "UIposition": [0.33,0.275],
                    "attachment": "",
                    "hitpoint": "HitPylon7",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\pylons\cmDispenser,
                "cmDispenser": {
                    "hardpoints": ["RHS_cm_BVP3026","RHS_cm_BVP3026_x2"],
                    "priority": 1,
                    "attachment": "rhs_BVP3026_CMFlare_Chaff_Magazine_x2",
                    "maxweight": 800,
                    "UIposition": [0.625,0.275]
                }
            },
            # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\Presets,
            "Presets": {
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\Presets\Bomb
                "Bomb": {
                    "attachment": ["rhs_mag_fab500_bd3_umk2a","rhs_mag_fab500_bd3_umk2a","rhs_mag_fab500_bd3_umk2a","rhs_mag_fab500_bd3_umk2a","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "Bomb"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\Presets\LaserBomb,
                "LaserBomb": {
                    "attachment": ["rhs_mag_kab500kr_bd3_umk2a","rhs_mag_kab500kr_bd3_umk2a","rhs_mag_kab500kr_bd3_umk2a","rhs_mag_kab500kr_bd3_umk2a","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "Guided bombs"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\Presets\AirToGround,
                "AirToGround": {
                    "attachment": ["rhs_mag_kh29T_aku58_mig29","rhs_mag_kh29T_aku58_mig29","rhs_mag_b8m1_bd3_umk2a_s8df","rhs_mag_b8m1_bd3_umk2a_s8df","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "Kh-29T"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\Presets\KMGU,
                "KMGU": {
                    "attachment": ["rhs_mag_kmgu2_ao25_bd3_umk2a","rhs_mag_kmgu2_ao25_bd3_umk2a","rhs_mag_kmgu2_ao25_bd3_umk2a","rhs_mag_kmgu2_ao25_bd3_umk2a","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "KMGU-2 (AO-2.5)"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\Presets\AA,
                "AA": {
                    "attachment": ["rhs_mag_R27ER_APU470","rhs_mag_R27ER_APU470","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "Anti Air"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\TransportPylonsComponent\Presets\CAS,
                "CAS": {
                    "attachment": ["rhs_mag_b8m1_bd3_umk2a_s8kom","rhs_mag_b8m1_bd3_umk2a_s8kom","rhs_mag_b8m1_bd3_umk2a_s8df","rhs_mag_b8m1_bd3_umk2a_s8df","rhs_mag_R73M_APU73","rhs_mag_R73M_APU73","rhs_BVP3026_CMFlare_Chaff_Magazine_x2"],
                    "displayname": "Close Air Support"
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent,
        "SensorsManagerComponent": {
            # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent\Components
            "Components": {
                # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent\Components\IRSensorComponent
                "IRSensorComponent": {
                    # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent\Components\IRSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 500,
                        "maxRange": 5000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": 1
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent\Components\IRSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 500,
                        "maxRange": 500,
                        "objectDistanceLimitCoef": 1,
                        "viewDistanceLimitCoef": 1
                    },
                    "angleRangeHorizontal": 360,
                    "angleRangeVertical": 120,
                    "maxTrackableSpeed": 500,
                    "componentType": "IRSensorComponent",
                    "typeRecognitionDistance": 2000,
                    "maxFogSeeThrough": 0.995,
                    "color": [1,0,0,1],
                    "allowsMarking": 1,
                    "groundNoiseDistanceCoef": -1,
                    "maxGroundNoiseDistance": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "animDirection": "",
                    "aimDown": 0,
                    "minTrackableSpeed": -1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent\Components\PassiveRadarSensorComponent,
                "PassiveRadarSensorComponent": {
                    "componentType": "PassiveRadarSensorComponent",
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
                # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent,
                "ActiveRadarSensorComponent": {
                    # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 23000,
                        "maxRange": 23000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 9000,
                        "maxRange": 9000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "typeRecognitionDistance": 6000,
                    "angleRangeHorizontal": 60,
                    "angleRangeVertical": 60,
                    "groundNoiseDistanceCoef": 0.1,
                    "componentType": "ActiveRadarSensorComponent",
                    "maxGroundNoiseDistance": 200,
                    "minSpeedThreshold": 20.8333,
                    "maxSpeedThreshold": 27.7778,
                    "color": [0,1,1,1],
                    "allowsMarking": 1,
                    "animDirection": "",
                    "aimDown": 0,
                    "minTrackableSpeed": -1e+010,
                    "maxTrackableSpeed": 1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent\Components\LaserSensorComponent,
                "LaserSensorComponent": {
                    "componentType": "LaserSensorComponent",
                    # Class: SensorTemplateLaser\AirTarget,
                    "AirTarget": {
                        "minRange": 6000,
                        "maxRange": 6000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: SensorTemplateLaser\GroundTarget,
                    "GroundTarget": {
                        "minRange": 6000,
                        "maxRange": 6000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "angleRangeHorizontal": 180,
                    "angleRangeVertical": 180,
                    "typeRecognitionDistance": 0,
                    "color": [1,1,1,0],
                    "allowsMarking": 1,
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
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\SensorsManagerComponent\Components\DataLinkSensorComponent,
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
        # Class: CfgVehicles\rhs_mig29sm_base\Components\VehicleSystemsDisplayManagerComponentLeft,
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: CfgVehicles\rhs_mig29sm_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components
            "Components": {
                # Class: CfgVehicles\rhs_mig29sm_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SensorDisplay,
                "SensorDisplay": {
                    "componentType": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [16000,35000,3000,8000],
                    "showTargetTypes": "1+2+4+8+32+128+256"
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultDisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles\rhs_mig29sm_base\Components\VehicleSystemsDisplayManagerComponentRight,
        "VehicleSystemsDisplayManagerComponentRight": {
            "defaultDisplay": "SensorDisplay",
            # Class: CfgVehicles\rhs_mig29sm_base\Components\VehicleSystemsDisplayManagerComponentRight\Components,
            "Components": {
                # Class: CfgVehicles\rhs_mig29sm_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\SensorDisplay,
                "SensorDisplay": {
                    "componentType": "SensorsDisplayComponent",
                    "resource": "RscCustomInfoSensors",
                    "range": [16000,35000,3000,8000],
                    "showTargetTypes": "1+2+4+8+32+128+256"
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
    "defaultUserMFDvalues": [1,0,0,0],
    # Class: CfgVehicles\rhs_mig29sm_base\MFD,
    "MFD": {
        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD
        "HUD": {
            "topLeft": "HUD_top_left",
            "topRight": "HUD_top_right",
            "bottomLeft": "HUD_bottom_left",
            "enableParallax": 1,
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_rus",
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\material,
            "material": {
                "ambient": [10,10,10,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones,
            "Bones": {
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\PlaneOrientation
                "PlaneOrientation": {
                    "type": "fixed",
                    "refreshRate": 0.1,
                    "pos": [0.5,0.53]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\ClimbFixed,
                "ClimbFixed": {
                    "type": "fixed",
                    "pos": [0.898,0.7]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\ClimbRotate,
                "ClimbRotate": {
                    "type": "rotational",
                    "source": "vspeed",
                    "sourceScale": 1,
                    "center": [0.88,0.7],
                    "min": -30,
                    "max": 30,
                    "minAngle": -90,
                    "maxAngle": 90,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\WeaponAim,
                "WeaponAim": {
                    "type": "vector",
                    "source": "weapon",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\Velocity,
                "Velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\HorizonBankSource,
                "HorizonBankSource": {
                    "type": "rotational",
                    "source": "HorizonBank",
                    "center": [0.5,0.53],
                    "min": -6.2831,
                    "max": 6.2831,
                    "minAngle": -360,
                    "maxAngle": 360
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\HorizonBankInverted,
                "HorizonBankInverted": {
                    "type": "rotational",
                    "source": "HorizonBank",
                    "center": [0.5,0.53],
                    "min": -6.2831,
                    "max": 6.2831,
                    "minAngle": 360,
                    "maxAngle": -360,
                    "refreshRate": 0.1
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\HorizonBankRotFull,
                "HorizonBankRotFull": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "center": [0,0],
                    "min": -3.1416,
                    "max": 3.1416,
                    "minAngle": -180,
                    "maxAngle": 180,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\Level0,
                "Level0": {
                    "source": "horizonDive",
                    "type": "linear",
                    "angle": 0,
                    "min": -3.4,
                    "max": 3.4,
                    "minPos": [0.5,4.78],
                    "maxPos": [0.5,-3.72],
                    "refreshRate": 0.1
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\TerrainBone,
                "TerrainBone": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "sourceScale": 1,
                    "min": 0,
                    "max": 200,
                    "minPos": [0,0.666],
                    "maxPos": [0,0.4]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\ImpactPoint,
                "ImpactPoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\ImpactPointRelative,
                "ImpactPointRelative": {
                    "type": "vector",
                    "source": "impactpointweaponRelative",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\Limit0109,
                "Limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\Target,
                "Target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\TargetingPodTarget,
                "TargetingPodTarget": {
                    "source": "pilotcamera",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\WPPoint,
                "WPPoint": {
                    "type": "vector",
                    "source": "WPPoint",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot1,
                "MissileFlightTimeRot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minAngle": 0,
                    "maxAngle": 18,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot2,
                "MissileFlightTimeRot2": {
                    "maxAngle": 37,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot3,
                "MissileFlightTimeRot3": {
                    "maxAngle": 55.5,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot4,
                "MissileFlightTimeRot4": {
                    "maxAngle": 74,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot5,
                "MissileFlightTimeRot5": {
                    "maxAngle": 92.5,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot6,
                "MissileFlightTimeRot6": {
                    "maxAngle": 111,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot7,
                "MissileFlightTimeRot7": {
                    "maxAngle": 129.5,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot8,
                "MissileFlightTimeRot8": {
                    "maxAngle": 148,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot9,
                "MissileFlightTimeRot9": {
                    "maxAngle": 166.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot10,
                "MissileFlightTimeRot10": {
                    "maxAngle": 185,
                    "max": 10,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot11,
                "MissileFlightTimeRot11": {
                    "maxAngle": 203.5,
                    "max": 11,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot12,
                "MissileFlightTimeRot12": {
                    "maxAngle": 222,
                    "max": 12,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot13,
                "MissileFlightTimeRot13": {
                    "maxAngle": 240.5,
                    "max": 13,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot14,
                "MissileFlightTimeRot14": {
                    "maxAngle": 259,
                    "max": 14,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot15,
                "MissileFlightTimeRot15": {
                    "maxAngle": 277.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot16,
                "MissileFlightTimeRot16": {
                    "maxAngle": 296,
                    "max": 16,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot17,
                "MissileFlightTimeRot17": {
                    "maxAngle": 314.5,
                    "max": 17,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot18,
                "MissileFlightTimeRot18": {
                    "maxAngle": 333,
                    "max": 18,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot19,
                "MissileFlightTimeRot19": {
                    "maxAngle": 351.5,
                    "max": 19,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\MissileFlightTimeRot20,
                "MissileFlightTimeRot20": {
                    "maxAngle": 370,
                    "max": 20,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\Airport1,
                "Airport1": {
                    "type": "vector",
                    "source": "airportCorner1",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\Airport2,
                "Airport2": {
                    "source": "airportCorner2",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\Airport3,
                "Airport3": {
                    "source": "airportCorner3",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\Airport4,
                "Airport4": {
                    "source": "airportCorner4",
                    "type": "vector",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\ILS_H,
                "ILS_H": {
                    "type": "ils",
                    "pos0": [0.5,0.53],
                    "pos3": [0.674,0.53]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\ILS_W,
                "ILS_W": {
                    "pos3": [0.5,0.707],
                    "type": "ils",
                    "pos0": [0.5,0.53]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\LarAmmoMax,
                "LarAmmoMax": {
                    "type": "linear",
                    "source": "LarAmmoMax",
                    "sourceScale": 1,
                    "min": 0,
                    "max": 1,
                    "minPos": [0,1],
                    "maxPos": [0,0]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\LarAmmoMin,
                "LarAmmoMin": {
                    "source": "LarAmmoMin",
                    "type": "linear",
                    "sourceScale": 1,
                    "min": 0,
                    "max": 1,
                    "minPos": [0,1],
                    "maxPos": [0,0]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\LarTargetDist,
                "LarTargetDist": {
                    "source": "LarTargetDist",
                    "sourceScale": 0.65,
                    "type": "linear",
                    "min": 0,
                    "max": 1,
                    "minPos": [0,1],
                    "maxPos": [0,0]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\LarAmmoMGunMax,
                "LarAmmoMGunMax": {
                    "type": "rotational",
                    "source": "LarAmmoMax",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 1,
                    "minAngle": -180,
                    "maxAngle": 180,
                    "aspectRatio": 1.01724
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Bones\LarAmmoMGunMin,
                "LarAmmoMGunMin": {
                    "source": "LarAmmoMin",
                    "type": "rotational",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 1,
                    "minAngle": -180,
                    "maxAngle": 180,
                    "aspectRatio": 1.01724
                }
            },
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw,
            "Draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                "condition": "on-user3",
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont,
                "Horizont": {
                    "clipTL": [0.1,0.38],
                    "clipBR": [0.9,0.78],
                    "condition": "1-(bomb+mgun+atmissile+aamissile+rocket)*activeSensorsOn",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed,
                    "Dimmed": {
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level00
                        "Level00": {
                            "type": "line",
                            "width": 5,
                            "points": [["Level0",[0.176,0],1],["Level0",[-0.176,0],1],[]]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2M00,
                        "Level2M00": {
                            "type": "line",
                            "lineType": 0,
                            "points": [["Level0",[0.224,0],1],["Level0",[0.18,0],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALM2_1_00,
                        "VALM2_1_00": {
                            "type": "text",
                            "source": "static",
                            "text": 0,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,-0.036],1],
                            "right": ["Level0",[0.24,-0.036],1],
                            "down": ["Level0",[0.2,-0.004],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2M10,
                        "Level2M10": {
                            "type": "line",
                            "lineType": 0,
                            "points": [["Level0",[0.224,-0.218519],1],["Level0",[0.18,-0.218519],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALM2_1_10,
                        "VALM2_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": 10,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,-0.254519],1],
                            "right": ["Level0",[0.24,-0.254519],1],
                            "down": ["Level0",[0.2,-0.222519],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2P10,
                        "Level2P10": {
                            "type": "line",
                            "lineType": 2,
                            "points": [["Level0",[0.224,0.218519],1],["Level0",[0.18,0.218519],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALP2_1_10,
                        "VALP2_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,0.182519],1],
                            "right": ["Level0",[0.24,0.182519],1],
                            "down": ["Level0",[0.2,0.214519],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2M20,
                        "Level2M20": {
                            "type": "line",
                            "lineType": 0,
                            "points": [["Level0",[0.224,-0.437037],1],["Level0",[0.18,-0.437037],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALM2_1_20,
                        "VALM2_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": 20,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,-0.473037],1],
                            "right": ["Level0",[0.24,-0.473037],1],
                            "down": ["Level0",[0.2,-0.441037],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2P20,
                        "Level2P20": {
                            "type": "line",
                            "lineType": 2,
                            "points": [["Level0",[0.224,0.437037],1],["Level0",[0.18,0.437037],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALP2_1_20,
                        "VALP2_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,0.401037],1],
                            "right": ["Level0",[0.24,0.401037],1],
                            "down": ["Level0",[0.2,0.433037],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2M30,
                        "Level2M30": {
                            "type": "line",
                            "lineType": 0,
                            "points": [["Level0",[0.224,-0.655556],1],["Level0",[0.18,-0.655556],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALM2_1_30,
                        "VALM2_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": 30,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,-0.691556],1],
                            "right": ["Level0",[0.24,-0.691556],1],
                            "down": ["Level0",[0.2,-0.659556],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2P30,
                        "Level2P30": {
                            "type": "line",
                            "lineType": 2,
                            "points": [["Level0",[0.224,0.655556],1],["Level0",[0.18,0.655556],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALP2_1_30,
                        "VALP2_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,0.619556],1],
                            "right": ["Level0",[0.24,0.619556],1],
                            "down": ["Level0",[0.2,0.651556],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2M40,
                        "Level2M40": {
                            "type": "line",
                            "lineType": 0,
                            "points": [["Level0",[0.224,-0.874074],1],["Level0",[0.18,-0.874074],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALM2_1_40,
                        "VALM2_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": 40,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,-0.910074],1],
                            "right": ["Level0",[0.24,-0.910074],1],
                            "down": ["Level0",[0.2,-0.878074],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2P40,
                        "Level2P40": {
                            "type": "line",
                            "lineType": 2,
                            "points": [["Level0",[0.224,0.874074],1],["Level0",[0.18,0.874074],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALP2_1_40,
                        "VALP2_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,0.838074],1],
                            "right": ["Level0",[0.24,0.838074],1],
                            "down": ["Level0",[0.2,0.870074],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2M50,
                        "Level2M50": {
                            "type": "line",
                            "lineType": 0,
                            "points": [["Level0",[0.224,-1.09259],1],["Level0",[0.18,-1.09259],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALM2_1_50,
                        "VALM2_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": 50,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,-1.12859],1],
                            "right": ["Level0",[0.24,-1.12859],1],
                            "down": ["Level0",[0.2,-1.09659],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2P50,
                        "Level2P50": {
                            "type": "line",
                            "lineType": 2,
                            "points": [["Level0",[0.224,1.09259],1],["Level0",[0.18,1.09259],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALP2_1_50,
                        "VALP2_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,1.05659],1],
                            "right": ["Level0",[0.24,1.05659],1],
                            "down": ["Level0",[0.2,1.08859],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2M60,
                        "Level2M60": {
                            "type": "line",
                            "lineType": 0,
                            "points": [["Level0",[0.224,-1.31111],1],["Level0",[0.18,-1.31111],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALM2_1_60,
                        "VALM2_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": 60,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,-1.34711],1],
                            "right": ["Level0",[0.24,-1.34711],1],
                            "down": ["Level0",[0.2,-1.31511],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2P60,
                        "Level2P60": {
                            "type": "line",
                            "lineType": 2,
                            "points": [["Level0",[0.224,1.31111],1],["Level0",[0.18,1.31111],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALP2_1_60,
                        "VALP2_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,1.27511],1],
                            "right": ["Level0",[0.24,1.27511],1],
                            "down": ["Level0",[0.2,1.30711],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2M70,
                        "Level2M70": {
                            "type": "line",
                            "lineType": 0,
                            "points": [["Level0",[0.224,-1.52963],1],["Level0",[0.18,-1.52963],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALM2_1_70,
                        "VALM2_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": 70,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,-1.56563],1],
                            "right": ["Level0",[0.24,-1.56563],1],
                            "down": ["Level0",[0.2,-1.53363],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2P70,
                        "Level2P70": {
                            "type": "line",
                            "lineType": 2,
                            "points": [["Level0",[0.224,1.52963],1],["Level0",[0.18,1.52963],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALP2_1_70,
                        "VALP2_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,1.49363],1],
                            "right": ["Level0",[0.24,1.49363],1],
                            "down": ["Level0",[0.2,1.52563],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2M80,
                        "Level2M80": {
                            "type": "line",
                            "lineType": 0,
                            "points": [["Level0",[0.224,-1.74815],1],["Level0",[0.18,-1.74815],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALM2_1_80,
                        "VALM2_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": 80,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,-1.78415],1],
                            "right": ["Level0",[0.24,-1.78415],1],
                            "down": ["Level0",[0.2,-1.75215],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\Level2P80,
                        "Level2P80": {
                            "type": "line",
                            "lineType": 2,
                            "points": [["Level0",[0.224,1.74815],1],["Level0",[0.18,1.74815],1]],
                            "width": 5
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\Dimmed\VALP2_1_80,
                        "VALP2_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "align": "center",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["Level0",[0.2,1.71215],1],
                            "right": ["Level0",[0.24,1.71215],1],
                            "down": ["Level0",[0.2,1.74415],1]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\BankDetailed,
                    "BankDetailed": {
                        "condition": "1-(bomb+mgun+atmissile+aamissile+rocket+missilelocked + missilelocking+activeSensorsOn)",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Horizont\BankDetailed\Level00,
                        "Level00": {
                            "type": "line",
                            "width": 5,
                            "points": [["PlaneOrientation",[-0.144889,0.0394922],1],["PlaneOrientation",[-0.164207,0.0447579],1],[],["PlaneOrientation",[-0.129904,0.0762931],1],["PlaneOrientation",[-0.164545,0.0966379],1],[],["PlaneOrientation",[-0.106066,0.107895],1],["PlaneOrientation",[-0.120208,0.122281],1],[],["PlaneOrientation",[-0.075,0.132144],1],["PlaneOrientation",[-0.095,0.167382],1],[],["PlaneOrientation",[0.144889,0.0394922],1],["PlaneOrientation",[0.164207,0.0447578],1],[],["PlaneOrientation",[0.129904,0.0762931],1],["PlaneOrientation",[0.164545,0.0966379],1],[],["PlaneOrientation",[0.106066,0.107895],1],["PlaneOrientation",[0.120208,0.122281],1],[],["PlaneOrientation",[0.075,0.132144],1],["PlaneOrientation",[0.095,0.167382],1],[]]
                        }
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PlaneOrientationCrosshair,
                "PlaneOrientationCrosshair": {
                    "type": "line",
                    "width": 3,
                    "points": [["HorizonBankInverted",[-0.1375,0],1],["HorizonBankInverted",[-0.0416667,0],1],[],["HorizonBankInverted",[-0.0833333,0],1],["HorizonBankInverted",[-0.0833333,-0.025],1],[],["HorizonBankInverted",[0.0416667,0],1],["HorizonBankInverted",[0.1375,0],1],[],["HorizonBankInverted",[0.0833333,0],1],["HorizonBankInverted",[0.0833333,-0.025],1],[],["HorizonBankInverted",[-0,0.0333333],1],["HorizonBankInverted",[-0,0.075],1],[],["PlaneOrientation",[-0.170833,0],1],["PlaneOrientation",[-0.145833,0],1],[],["PlaneOrientation",[0.145833,0],1],["PlaneOrientation",[0.170833,0],1],[]]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\GunCross,
                "GunCross": {
                    "condition": "1-mgun*impactDistance*(altitudeAGL>=5)",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\GunCross\Cross,
                    "Cross": {
                        "type": "line",
                        "width": 3,
                        "points": [["PlaneOrientation",[0,-0.03],1],["PlaneOrientation",[0,-0.01],1],[],["PlaneOrientation",[0,0.03],1],["PlaneOrientation",[0,0.01],1],[],["PlaneOrientation",[-0.03,0],1],["PlaneOrientation",[-0.01,0],1],[],["PlaneOrientation",[0.03,0],1],["PlaneOrientation",[0.01,0],1],[]]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MissileLocked,
                "MissileLocked": {
                    "condition": "missilelocked",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MissileLocked\LaunchReady,
                    "LaunchReady": {
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
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MissileLocking,
                "MissileLocking": {
                    "condition": "missilelocking",
                    "blinkingPattern": [0.2,0.5],
                    "blinkingStartsOn": 1,
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MissileLocking\LaunchReady,
                    "LaunchReady": {
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
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\SpeedNumber0,
                "SpeedNumber0": {
                    "type": "text",
                    "source": "static",
                    "text": 0,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.31,"0.09+0.19"],1],
                    "right": [[0.375,"0.09+0.19"],1],
                    "down": [[0.31,0.35],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\SpeedNumber,
                "SpeedNumber": {
                    "source": "speed",
                    "sourceScale": 0.36,
                    "pos": [[0.275,"0.09+0.19"],1],
                    "right": [[0.34,"0.09+0.19"],1],
                    "down": [[0.275,0.35],1],
                    "type": "text",
                    "text": 0,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AccelerationLine,
                "AccelerationLine": {
                    "type": "line",
                    "width": 4,
                    "points": [[[0.22,0.35],1],[[0.29,0.35],1]]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Acceleration0Group,
                "Acceleration0Group": {
                    "condition": "1-abs(gmeterZ)",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\Acceleration0Group\Acceleration,
                    "Acceleration": {
                        "type": "line",
                        "width": 2,
                        "points": [[[0.249,0.362],1],[[0.255,0.35],1],[[0.261,0.362],1],[[0.249,0.362],1]]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AccelerationPlusGroup,
                "AccelerationPlusGroup": {
                    "condition": "gmeterZ>=0.5",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AccelerationPlusGroup\Acceleration,
                    "Acceleration": {
                        "type": "line",
                        "width": 2,
                        "points": [[[0.279,0.362],1],[[0.285,0.35],1],[[0.291,0.362],1],[[0.279,0.362],1]]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AccelerationMinusGroup,
                "AccelerationMinusGroup": {
                    "condition": "gmeterZ<=-0.5",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AccelerationMinusGroup\Acceleration,
                    "Acceleration": {
                        "type": "line",
                        "width": 2,
                        "points": [[[0.219,0.362],1],[[0.225,0.35],1],[[0.231,0.362],1],[[0.219,0.362],1]]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AltitudeNumber0,
                "AltitudeNumber0": {
                    "type": "text",
                    "source": "static",
                    "text": 0,
                    "align": "left",
                    "scale": 1,
                    "pos": [[0.82,"0.09+0.19"],1],
                    "right": [[0.885,"0.09+0.19"],1],
                    "down": [[0.82,0.35],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AltitudeNumber,
                "AltitudeNumber": {
                    "source": "altitudeASL",
                    "sourceScale": 0.1,
                    "sourceLength": 1,
                    "pos": [[0.785,"0.09+0.19"],1],
                    "right": [[0.85,"0.09+0.19"],1],
                    "down": [[0.785,0.35],1],
                    "type": "text",
                    "text": 0,
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\RadarOnGroup,
                "RadarOnGroup": {
                    "condition": "activeSensorsOn",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\RadarOnGroup\RadarText,
                    "RadarText": {
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
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup,
                "PylonGroup": {
                    "condition": "bomb+mgun+atmissile+aamissile+rocket",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon1,
                    "Pylon1": {
                        "condition": "1-pylonSelected1",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon1\PylonLine,
                        "PylonLine": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.509,0.78],1],[[0.541,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon1Selected,
                    "Pylon1Selected": {
                        "condition": "pylonSelected1",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon1Selected\PylonLine,
                        "PylonLine": {
                            "points": [[[0.509,0.745],1],[[0.541,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon2,
                    "Pylon2": {
                        "condition": "1-pylonSelected2",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon2\PylonLine,
                        "PylonLine": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.434,0.78],1],[[0.466,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon2Selected,
                    "Pylon2Selected": {
                        "condition": "pylonSelected2",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon2Selected\PylonLine,
                        "PylonLine": {
                            "points": [[[0.434,0.745],1],[[0.466,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon3,
                    "Pylon3": {
                        "condition": "1-pylonSelected3",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon3\PylonLine,
                        "PylonLine": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.559,0.78],1],[[0.591,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon3Selected,
                    "Pylon3Selected": {
                        "condition": "pylonSelected3",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon3Selected\PylonLine,
                        "PylonLine": {
                            "points": [[[0.559,0.745],1],[[0.591,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon4,
                    "Pylon4": {
                        "condition": "1-pylonSelected4",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon4\PylonLine,
                        "PylonLine": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.384,0.78],1],[[0.416,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon4Selected,
                    "Pylon4Selected": {
                        "condition": "pylonSelected4",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon4Selected\PylonLine,
                        "PylonLine": {
                            "points": [[[0.384,0.745],1],[[0.416,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon5,
                    "Pylon5": {
                        "condition": "1-pylonSelected5",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon5\PylonLine,
                        "PylonLine": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.609,0.78],1],[[0.641,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon5Selected,
                    "Pylon5Selected": {
                        "condition": "pylonSelected5",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon5Selected\PylonLine,
                        "PylonLine": {
                            "points": [[[0.609,0.745],1],[[0.641,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon6,
                    "Pylon6": {
                        "condition": "1-pylonSelected6",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon6\PylonLine,
                        "PylonLine": {
                            "type": "line",
                            "width": 6,
                            "points": [[[0.334,0.78],1],[[0.366,0.78],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon6Selected,
                    "Pylon6Selected": {
                        "condition": "pylonSelected6",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\Pylon6Selected\PylonLine,
                        "PylonLine": {
                            "points": [[[0.334,0.745],1],[[0.366,0.745],1]],
                            "type": "line",
                            "width": 6
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\PylonName1,
                    "PylonName1": {
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "pylon": 1,
                        "name": "rhs_rus_ammoname"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\PylonName2,
                    "PylonName2": {
                        "pylon": 2,
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "name": "rhs_rus_ammoname"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\PylonName3,
                    "PylonName3": {
                        "pylon": 3,
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "name": "rhs_rus_ammoname"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\PylonName4,
                    "PylonName4": {
                        "pylon": 4,
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "name": "rhs_rus_ammoname"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\PylonName5,
                    "PylonName5": {
                        "pylon": 5,
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "name": "rhs_rus_ammoname"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\PylonGroup\PylonName6,
                    "PylonName6": {
                        "pylon": 6,
                        "type": "pylonicon",
                        "pos": [[0.74,0.73],1],
                        "name": "rhs_rus_ammoname"
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\ILS,
                "ILS": {
                    "condition": "ils",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\ILS\Glideslope,
                    "Glideslope": {
                        "clipTL": [0,0],
                        "clipBR": [1,1],
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\ILS\Glideslope\ILS,
                        "ILS": {
                            "type": "line",
                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[-0.24,-0.0244138],1],["ILS_W",[-0.24,0.0244138],1],[],["ILS_W",[-0.12,-0.0183103],1],["ILS_W",[-0.12,0.0183103],1],[],["ILS_W",[0,-0.0244138],1],["ILS_W",[0,0.0244138],1],[],["ILS_W",[0.12,-0.0183103],1],["ILS_W",[0.12,0.0183103],1],[],["ILS_W",[0.24,-0.0244138],1],["ILS_W",[0.24,0.0244138],1],[],["ILS_H",[0,-0.244138],1],["ILS_H",[0,0.244138],1],[],["ILS_H",[-0.024,-0.244138],1],["ILS_H",[0.024,-0.244138],1],[],["ILS_H",[-0.018,-0.122069],1],["ILS_H",[0.018,-0.122069],1],[],["ILS_H",[-0.024,0],1],["ILS_H",[0.024,0],1],[],["ILS_H",[-0.018,0.122069],1],["ILS_H",[0.018,0.122069],1],[],["ILS_H",[-0.024,0.244138],1],["ILS_H",[0.024,0.244138],1]]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\ILS\Glideslope\airport,
                        "airport": {
                            "type": "line",
                            "points": [["airport1",1],["airport2",1],["airport4",1],["airport3",1],["airport1",1]]
                        }
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\HeadingArrow,
                "HeadingArrow": {
                    "type": "line",
                    "width": 3,
                    "points": [[[0.48,0.365],1],[[0.5,0.345],1],[[0.52,0.365],1],[[0.48,0.365],1]]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\HeadingLine,
                "HeadingLine": {
                    "type": "line",
                    "width": 4,
                    "points": [[[0.35,0.34],1],[[0.65,0.34],1]]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\HeadingScale,
                "HeadingScale": {
                    "type": "scale",
                    "horizontal": 1,
                    "source": "heading",
                    "sourceScale": 0.1,
                    "width": 4,
                    "NeverEatSeaWeed": 0,
                    "refreshRate": 0.1,
                    "top": 0.35,
                    "center": 0.5,
                    "bottom": 0.65,
                    "lineXleft": 0.338,
                    "lineYright": 0.328,
                    "lineXleftMajor": 0.338,
                    "lineYrightMajor": 0.318,
                    "majorLineEach": 2,
                    "numberEach": 2,
                    "step": 0.5,
                    "stepSize": 0.0526316,
                    "align": "center",
                    "scale": 1,
                    "pos": [0.35,0.27],
                    "right": [0.4,0.27],
                    "down": [0.35,0.31]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MarchGroup,
                "MarchGroup": {
                    "condition": "1-(bomb+mgun+atmissile+aamissile+rocket)",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MarchGroup\MarchText,
                    "MarchText": {
                        "type": "text",
                        "source": "static",
                        "text": "МРШ",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[0.18,0.75],1],
                        "right": [[0.23,0.75],1],
                        "down": [[0.18,0.8],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MarchGroup\SpeedNumber0,
                    "SpeedNumber0": {
                        "type": "text",
                        "source": "WPDist",
                        "sourceScale": 0.001,
                        "sourcePrecision": 1,
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,0.75],1],
                        "right": [[0.55,0.75],1],
                        "down": [[0.5,0.8],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MarchGroup\WP,
                    "WP": {
                        "condition": "wpvalid",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MarchGroup\WP\shape,
                        "shape": {
                            "type": "line",
                            "width": 4,
                            "points": [["WPPoint",[0,-0.0406897],1],["WPPoint",[0.006944,-0.0400712],1],["WPPoint",[0.01368,-0.0382361],1],["WPPoint",[0.02,-0.0352372],1],["WPPoint",[0.025712,-0.0311683],1],["WPPoint",[0.03064,-0.0261553],1],["WPPoint",[0.03464,-0.0203448],1],["WPPoint",[0.037588,-0.0139159],1],["WPPoint",[0.039392,-0.00706372],1],["WPPoint",[0.04,0],1],["WPPoint",[0.039392,0.00706372],1],["WPPoint",[0.037588,0.0139159],1],["WPPoint",[0.03464,0.0203448],1],["WPPoint",[0.03064,0.0261553],1],["WPPoint",[0.025712,0.0311683],1],["WPPoint",[0.02,0.0352372],1],["WPPoint",[0.01368,0.0382361],1],["WPPoint",[0.006944,0.0400712],1],["WPPoint",[0,0.0406897],1],["WPPoint",[-0.006944,0.0400712],1],["WPPoint",[-0.01368,0.0382361],1],["WPPoint",[-0.02,0.0352372],1],["WPPoint",[-0.025712,0.0311683],1],["WPPoint",[-0.03064,0.0261553],1],["WPPoint",[-0.03464,0.0203448],1],["WPPoint",[-0.037588,0.0139159],1],["WPPoint",[-0.039392,0.00706372],1],["WPPoint",[-0.04,0],1],["WPPoint",[-0.039392,-0.00706372],1],["WPPoint",[-0.037588,-0.0139159],1],["WPPoint",[-0.03464,-0.0203448],1],["WPPoint",[-0.03064,-0.0261553],1],["WPPoint",[-0.025712,-0.0311683],1],["WPPoint",[-0.02,-0.0352372],1],["WPPoint",[-0.01368,-0.0382361],1],["WPPoint",[-0.006944,-0.0400712],1],["WPPoint",[0,-0.0406897],1],[]]
                        }
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\HelmetModeGroup,
                "HelmetModeGroup": {
                    "condition": "user2*(bomb+mgun+atmissile+aamissile+rocket)",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\HelmetModeGroup\HelmetText,
                    "HelmetText": {
                        "type": "text",
                        "source": "static",
                        "text": "ШЛМ",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[0.18,0.75],1],
                        "right": [[0.23,0.75],1],
                        "down": [[0.18,0.8],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\HelmetModeGroup\BWBText,
                    "BWBText": {
                        "type": "text",
                        "source": "static",
                        "text": "БВБ",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[0.18,0.79],1],
                        "right": [[0.23,0.79],1],
                        "down": [[0.18,0.84],1]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun,
                "MGun": {
                    "condition": "mgun",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\AmmoBox,
                    "AmmoBox": {
                        "type": "line",
                        "width": 3,
                        "points": [[[0.757,0.748],1],[[0.757,0.782],1],[[0.723,0.782],1],[[0.723,0.748],1],[[0.757,0.748],1],[]]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\Full,
                    "Full": {
                        "condition": "ammo>=113",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\Full\AmmoText,
                        "AmmoText": {
                            "type": "text",
                            "source": "static",
                            "text": "4",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0.74,0.745],1],
                            "right": [[0.785,0.745],1],
                            "down": [[0.74,0.79],1]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\AlmostFull,
                    "AlmostFull": {
                        "condition": "(ammo>=75)*(ammo<=112)",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\AlmostFull\AmmoText,
                        "AmmoText": {
                            "type": "text",
                            "source": "static",
                            "text": "3",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0.74,0.74],1],
                            "right": [[0.785,0.74],1],
                            "down": [[0.74,0.785],1]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\Half,
                    "Half": {
                        "condition": "(ammo>=38)*(ammo<=74)",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\Half\AmmoText,
                        "AmmoText": {
                            "type": "text",
                            "source": "static",
                            "text": "2",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0.74,0.74],1],
                            "right": [[0.785,0.74],1],
                            "down": [[0.74,0.785],1]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\AlmostEmpty,
                    "AlmostEmpty": {
                        "condition": "(ammo>=1)*(ammo<=37)",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\AlmostEmpty\AmmoText,
                        "AmmoText": {
                            "type": "text",
                            "source": "static",
                            "text": "1",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0.74,0.745],1],
                            "right": [[0.785,0.745],1],
                            "down": [[0.74,0.79],1]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\Empty,
                    "Empty": {
                        "condition": "ammo<=0",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\Empty\AmmoText,
                        "AmmoText": {
                            "type": "text",
                            "source": "static",
                            "text": "0",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0.74,0.745],1],
                            "right": [[0.785,0.745],1],
                            "down": [[0.74,0.79],1]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\CrossCondition,
                    "CrossCondition": {
                        "condition": "impactDistance*(altitudeAGL>=5)",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\CrossCondition\Cross,
                        "Cross": {
                            "type": "line",
                            "width": 3,
                            "points": [["ImpactPointRelative",[0,-0.025431],1],["ImpactPointRelative",[0,-0.0152586],1],[],["ImpactPointRelative",[0,0.025431],1],["ImpactPointRelative",[0,0.0152586],1],[],["ImpactPointRelative",[-0.025,0],1],["ImpactPointRelative",[-0.015,0],1],[],["ImpactPointRelative",[0.025,0],1],["ImpactPointRelative",[0.015,0],1],[],["ImpactPointRelative",[0,-0.002],1],["ImpactPointRelative",[0,0.002],1],[],["ImpactPointRelative",[-0.002,0],1],["ImpactPointRelative",[0.002,0],1],[]]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\MGun\CrossCondition\Circle,
                        "Circle": {
                            "type": "line",
                            "width": 4,
                            "points": [["ImpactPointRelative",[0,-0.0260414],1],["ImpactPointRelative",[0,-0.0325517],1],["MissileFlightTimeRot1",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot2",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot3",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot4",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot5",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot6",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot7",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot8",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot9",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot10",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot11",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot12",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot13",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot14",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot15",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot16",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot17",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot18",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot19",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot20",[0,0.032],1,"ImpactPointRelative",1],["MissileFlightTimeRot20",[0,0.0256],1,"ImpactPointRelative",1]]
                        }
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\BombCrosshairGroup,
                "BombCrosshairGroup": {
                    "type": "group",
                    "condition": "bomb+rocket*impactDistance",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\BombCrosshairGroup\BombCrosshair,
                    "BombCrosshair": {
                        "type": "line",
                        "width": 4,
                        "points": [["ImpactPoint",[0,-0.0406897],1],["ImpactPoint",[0.006944,-0.0400712],1],["ImpactPoint",[0.01368,-0.0382361],1],["ImpactPoint",[0.02,-0.0352372],1],["ImpactPoint",[0.025712,-0.0311683],1],["ImpactPoint",[0.03064,-0.0261553],1],["ImpactPoint",[0.03464,-0.0203448],1],["ImpactPoint",[0.037588,-0.0139159],1],["ImpactPoint",[0.039392,-0.00706372],1],["ImpactPoint",[0.04,0],1],["ImpactPoint",[0.039392,0.00706372],1],["ImpactPoint",[0.037588,0.0139159],1],["ImpactPoint",[0.03464,0.0203448],1],["ImpactPoint",[0.03064,0.0261553],1],["ImpactPoint",[0.025712,0.0311683],1],["ImpactPoint",[0.02,0.0352372],1],["ImpactPoint",[0.01368,0.0382361],1],["ImpactPoint",[0.006944,0.0400712],1],["ImpactPoint",[0,0.0406897],1],["ImpactPoint",[-0.006944,0.0400712],1],["ImpactPoint",[-0.01368,0.0382361],1],["ImpactPoint",[-0.02,0.0352372],1],["ImpactPoint",[-0.025712,0.0311683],1],["ImpactPoint",[-0.03064,0.0261553],1],["ImpactPoint",[-0.03464,0.0203448],1],["ImpactPoint",[-0.037588,0.0139159],1],["ImpactPoint",[-0.039392,0.00706372],1],["ImpactPoint",[-0.04,0],1],["ImpactPoint",[-0.039392,-0.00706372],1],["ImpactPoint",[-0.037588,-0.0139159],1],["ImpactPoint",[-0.03464,-0.0203448],1],["ImpactPoint",[-0.03064,-0.0261553],1],["ImpactPoint",[-0.025712,-0.0311683],1],["ImpactPoint",[-0.02,-0.0352372],1],["ImpactPoint",[-0.01368,-0.0382361],1],["ImpactPoint",[-0.006944,-0.0400712],1],["ImpactPoint",[0,-0.0406897],1],[],[],["ImpactPoint",[0,0.005],1],["ImpactPoint",[0.005,-0],1],["ImpactPoint",[0,-0.005],1],["ImpactPoint",[-0.005,-0],1],["ImpactPoint",[0,0.005],1]]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AAMissilesGroup,
                "AAMissilesGroup": {
                    "type": "group",
                    "condition": "aamissile",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AAMissilesGroup\PPSGroup,
                    "PPSGroup": {
                        "condition": "1",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AAMissilesGroup\PPSGroup\GText,
                        "GText": {
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
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AAMissilesGroup\ZPSGroup,
                    "ZPSGroup": {
                        "condition": "0",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\AAMissilesGroup\ZPSGroup\GText,
                        "GText": {
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
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\TargetDiamond,
                "TargetDiamond": {
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\TargetDiamond\shape
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0,-0.015],1],["Target",1,"Limit0109",1,[-0.0075,0],1],["Target",1,"Limit0109",1,[0,0.0125],1],["Target",1,"Limit0109",1,[0.0075,0],1],["Target",1,"Limit0109",1,[0,-0.0125],1]]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\TargetLocked,
                "TargetLocked": {
                    "condition": "TargetHeight>=1",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\TargetLocked\TargetSquare,
                    "TargetSquare": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0,-0.0508621],1],["Target",1,"Limit0109",1,[0.05,0],1],["Target",1,"Limit0109",1,[0,0.0508621],1],["Target",1,"Limit0109",1,[-0.05,0],1],["Target",1,"Limit0109",1,[0,-0.0508621],1]]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\TargetLocked\TargetSpeed0,
                    "TargetSpeed0": {
                        "type": "text",
                        "source": "static",
                        "text": 0,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.31,"0.09+0.15"],1],
                        "right": [[0.35,"0.09+0.15"],1],
                        "down": [[0.31,0.285],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\TargetLocked\TargetSpeed,
                    "TargetSpeed": {
                        "source": "LarTargetSpeed",
                        "sourceScale": 0.36,
                        "pos": [[0.29,"0.09+0.15"],1],
                        "right": [[0.33,"0.09+0.15"],1],
                        "down": [[0.29,0.285],1],
                        "type": "text",
                        "text": 0,
                        "align": "left",
                        "scale": 1
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\TargetLocked\TargetHeight0,
                    "TargetHeight0": {
                        "type": "text",
                        "source": "static",
                        "text": 0,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.82,"0.09+0.15"],1],
                        "right": [[0.86,"0.09+0.15"],1],
                        "down": [[0.82,0.285],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\TargetLocked\TargetHeight,
                    "TargetHeight": {
                        "source": "TargetHeight",
                        "sourceScale": 0.1,
                        "sourceLength": 1,
                        "pos": [[0.8,"0.09+0.15"],1],
                        "right": [[0.84,"0.09+0.15"],1],
                        "down": [[0.8,0.285],1],
                        "type": "text",
                        "text": 0,
                        "align": "left",
                        "scale": 1
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR,
                "LAR": {
                    "type": "group",
                    "condition": "bomb+mgun+atmissile+aamissile+rocket",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\Lines,
                    "Lines": {
                        "type": "line",
                        "width": 3,
                        "points": [[[0.24,0.375],1],[[0.26,0.375],1],[[0.26,0.695],1],[[0.24,0.695],1],[],[[0.24,0.631],1],[[0.26,0.631],1],[],[[0.24,0.567],1],[[0.26,0.567],1],[],[[0.24,0.503],1],[[0.26,0.503],1],[],[[0.24,0.439],1],[[0.26,0.439],1],[],["LarTargetDist",-0.32,[0.272,0.707],1],["LarTargetDist",-0.32,[0.26,0.695],1],["LarTargetDist",-0.32,[0.272,0.683],1],["LarTargetDist",-0.32,[0.272,0.692],1],["LarTargetDist",-0.32,[0.282,0.692],1],["LarTargetDist",-0.32,[0.282,0.698],1],["LarTargetDist",-0.32,[0.272,0.698],1],["LarTargetDist",-0.32,[0.272,0.707],1]]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\RadarSearch,
                    "RadarSearch": {
                        "condition": "activeSensorsOn - missilelocked - missilelocking",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\RadarSearch\Shape,
                        "Shape": {
                            "type": "line",
                            "width": 3,
                            "points": [[[0.725,0.375],1],[[0.74,0.375],1],[[0.74,0.695],1],[[0.725,0.695],1],[],[[0.74,0.535],1],[[0.725,0.535],1],[],[[0.76,0.519],1],[[0.76,0.551],1],[],[[0.755,0.5222],1],[[0.74,0.5222],1],[],[[0.74,0.5478],1],[[0.755,0.5478],1],[],[[0.47,0.715],1],[[0.53,0.715],1]]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\RadarSearch\RadarTopText,
                        "RadarTopText": {
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [["0.96-0.26",0.35625],1],
                            "right": [[0.735,0.35625],1],
                            "down": [["0.96-0.26",0.39125],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\RadarSearch\RadarElevText,
                        "RadarElevText": {
                            "type": "text",
                            "source": "static",
                            "text": "0",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [["1.035-0.26",0.519],1],
                            "right": [[0.81,0.519],1],
                            "down": [["1.035-0.26",0.554],1]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\Poly,
                    "Poly": {
                        "type": "polygon",
                        "points": [[["LarAmmoMin",-0.32,[0.261,0.695],1],["LarAmmoMin",-0.32,[0.261,0.7],1],["LarAmmoMin",-0.32,[0.272,0.7],1],["LarAmmoMin",-0.32,[0.272,0.695],1]],[["LarAmmoMin",-0.32,[0.261,0.62],1],["LarAmmoMin",-0.32,[0.261,0.63],1],["LarAmmoMin",-0.32,[0.272,0.63],1],["LarAmmoMin",-0.32,[0.272,0.62],1]],[["LarAmmoMax",-0.32,[0.261,0.785],1],["LarAmmoMax",-0.32,[0.261,0.79],1],["LarAmmoMax",-0.32,[0.272,0.79],1],["LarAmmoMax",-0.32,[0.272,0.785],1]]]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\LARText1,
                    "LARText1": {
                        "type": "text",
                        "source": "LarTop",
                        "sourceScale": "0.001*1.5",
                        "scale": 1,
                        "pos": [[0.235,0.361],1],
                        "right": [[0.27,0.361],1],
                        "down": [[0.235,0.389],1],
                        "align": "left"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\LARText2,
                    "LARText2": {
                        "source": "LarTop",
                        "sourcePrecision": -1,
                        "sourceScale": "0.0008*1.5",
                        "pos": [[0.235,0.425],1],
                        "right": [[0.27,0.425],1],
                        "down": [[0.235,0.453],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\LARText3,
                    "LARText3": {
                        "source": "LarTop",
                        "sourcePrecision": -1,
                        "sourceScale": "0.0006*1.5",
                        "pos": [[0.235,0.489],1],
                        "right": [[0.27,0.489],1],
                        "down": [[0.235,0.517],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\LARText4,
                    "LARText4": {
                        "source": "LarTop",
                        "sourcePrecision": -1,
                        "sourceScale": "0.0004*1.5",
                        "pos": [[0.235,0.553],1],
                        "right": [[0.27,0.553],1],
                        "down": [[0.235,0.581],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\LARText5,
                    "LARText5": {
                        "source": "LarTop",
                        "sourcePrecision": -1,
                        "sourceScale": "0.0002*1.5",
                        "pos": [[0.235,0.617],1],
                        "right": [[0.27,0.617],1],
                        "down": [[0.235,0.645],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\LAR\LARText6,
                    "LARText6": {
                        "source": "static",
                        "text": 0,
                        "sourcePrecision": -1,
                        "sourceScale": "0.0002*1.5",
                        "pos": [[0.235,0.681],1],
                        "right": [[0.27,0.681],1],
                        "down": [[0.235,0.709],1],
                        "type": "text",
                        "scale": 1,
                        "align": "left"
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD\Draw\RadarBoxes,
                "RadarBoxes": {
                    "type": "radar",
                    "pos0": [0.5,0.53],
                    "pos10": [1.08,1.12],
                    "width": 4,
                    "points": [[[0,-0.0406897],1],[[0.006944,-0.0400712],1],[[0.01368,-0.0382361],1],[[0.02,-0.0352372],1],[[0.025712,-0.0311683],1],[[0.03064,-0.0261553],1],[[0.03464,-0.0203448],1],[[0.037588,-0.0139159],1],[[0.039392,-0.00706372],1],[[0.04,0],1],[[0.039392,0.00706372],1],[[0.037588,0.0139159],1],[[0.03464,0.0203448],1],[[0.03064,0.0261553],1],[[0.025712,0.0311683],1],[[0.02,0.0352372],1],[[0.01368,0.0382361],1],[[0.006944,0.0400712],1],[[0,0.0406897],1],[[-0.006944,0.0400712],1],[[-0.01368,0.0382361],1],[[-0.02,0.0352372],1],[[-0.025712,0.0311683],1],[[-0.03064,0.0261553],1],[[-0.03464,0.0203448],1],[[-0.037588,0.0139159],1],[[-0.039392,0.00706372],1],[[-0.04,0],1],[[-0.039392,-0.00706372],1],[[-0.037588,-0.0139159],1],[[-0.03464,-0.0203448],1],[[-0.03064,-0.0261553],1],[[-0.025712,-0.0311683],1],[[-0.02,-0.0352372],1],[[-0.01368,-0.0382361],1],[[-0.006944,-0.0400712],1],[[0,-0.0406897],1],[]]
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD_static,
        "HUD_static": {
            "topLeft": "HUD_top_left",
            "topRight": "HUD_top_right",
            "bottomLeft": "HUD_bottom_left",
            "enableParallax": 1,
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_rus",
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD_static\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD_static\Draw,
            "Draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                "condition": "user3*on",
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HUD_static\Draw\Shape,
                "Shape": {
                    "type": "polygon",
                    "texture": "rhsafrf|addons|rhs_c_a2port_air|Su25|rhs_su25_reticle_static_ca.paa",
                    "points": [[[[0.225,0.415],1],[[0.785,0.415],1],[[0.785,0.915],1],[[0.225,0.915],1]]]
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1,
        "MFD_1": {
            "topLeft": "MFD_1_TL",
            "topRight": "MFD_1_TR",
            "bottomLeft": "MFD_1_BL",
            "enableParallax": 0,
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,0,0,0.1],
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Bones,
            "Bones": {
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Bones\Pylon1
                "Pylon1": {
                    "type": "fixed",
                    "pos": [0.682,0.633577]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Bones\Pylon2,
                "Pylon2": {
                    "pos": [0.324,0.633577],
                    "type": "fixed"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Bones\Pylon3,
                "Pylon3": {
                    "pos": [0.789,0.633577],
                    "type": "fixed"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Bones\Pylon4,
                "Pylon4": {
                    "pos": [0.217,0.633577],
                    "type": "fixed"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Bones\Pylon5,
                "Pylon5": {
                    "pos": [0.896,0.633577],
                    "type": "fixed"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Bones\Pylon6,
                "Pylon6": {
                    "pos": [0.11,0.633577],
                    "type": "fixed"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Bones\Pylon7,
                "Pylon7": {
                    "pos": [0.503,0.633577],
                    "type": "fixed"
                }
            },
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 0.22,
                "condition": "on",
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_TV,
                "Group_TV": {
                    "condition": "user45<=0"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_NAV,
                "Group_NAV": {
                    "condition": "(user45 >= 1)*(user45<=1)"
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP,
                "Group_WEAP": {
                    "condition": "(user45 >= 2)*(user45<=2)+1",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\AmmoGunText,
                    "AmmoGunText": {
                        "type": "text",
                        "source": "static",
                        "text": "ВПУ",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.04,0.15],1],
                        "right": [[0.1,0.15],1],
                        "down": [[0.04,0.21],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\AmmoValue,
                    "AmmoValue": {
                        "type": "text",
                        "source": "ammo",
                        "sourceIndex": 1,
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.04,0.22],1],
                        "right": [[0.1,0.22],1],
                        "down": [[0.04,0.28],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\CMGunText,
                    "CMGunText": {
                        "type": "text",
                        "source": "static",
                        "text": "ЛТЦ",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.95,0.15],1],
                        "right": [[1.01,0.15],1],
                        "down": [[0.95,0.21],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\CMValue,
                    "CMValue": {
                        "type": "text",
                        "source": "cmAmmo",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.95,0.22],1],
                        "right": [[1.01,0.22],1],
                        "down": [[0.95,0.28],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon1_empty,
                    "Pylon1_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty1",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon1_empty\Shape,
                        "Shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon1",[-0.02,0.0226277],1],["Pylon1",[0.02,-0.0226277],1],[],["Pylon1",[-0.02,-0.0226277],1],["Pylon1",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon2_empty,
                    "Pylon2_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty2",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon2_empty\Shape,
                        "Shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon2",[-0.02,0.0226277],1],["Pylon2",[0.02,-0.0226277],1],[],["Pylon2",[-0.02,-0.0226277],1],["Pylon2",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon3_empty,
                    "Pylon3_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty3",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon3_empty\Shape,
                        "Shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon3",[-0.02,0.0226277],1],["Pylon3",[0.02,-0.0226277],1],[],["Pylon3",[-0.02,-0.0226277],1],["Pylon3",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon4_empty,
                    "Pylon4_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty4",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon4_empty\Shape,
                        "Shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon4",[-0.02,0.0226277],1],["Pylon4",[0.02,-0.0226277],1],[],["Pylon4",[-0.02,-0.0226277],1],["Pylon4",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon5_empty,
                    "Pylon5_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty5",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon5_empty\Shape,
                        "Shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon5",[-0.02,0.0226277],1],["Pylon5",[0.02,-0.0226277],1],[],["Pylon5",[-0.02,-0.0226277],1],["Pylon5",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon6_empty,
                    "Pylon6_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty6",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon6_empty\Shape,
                        "Shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon6",[-0.02,0.0226277],1],["Pylon6",[0.02,-0.0226277],1],[],["Pylon6",[-0.02,-0.0226277],1],["Pylon6",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon7_empty,
                    "Pylon7_empty": {
                        "color": [1,0,0],
                        "condition": "pylonEmpty7",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\Pylon7_empty\Shape,
                        "Shape": {
                            "type": "line",
                            "width": 8,
                            "points": [["Pylon7",[-0.02,0.0226277],1],["Pylon7",[0.02,-0.0226277],1],[],["Pylon7",[-0.02,-0.0226277],1],["Pylon7",[0.02,0.0226277],1]]
                        }
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\PylonName1,
                    "PylonName1": {
                        "type": "pylonicon",
                        "pos": ["Pylon1",[0,0],1],
                        "pylon": 1,
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\PylonName2,
                    "PylonName2": {
                        "pos": ["Pylon2",[0,0],1],
                        "pylon": 2,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\PylonName3,
                    "PylonName3": {
                        "pos": ["Pylon3",[0,0],1],
                        "pylon": 3,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\PylonName4,
                    "PylonName4": {
                        "pos": ["Pylon4",[0,0],1],
                        "pylon": 4,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\PylonName5,
                    "PylonName5": {
                        "pos": ["Pylon5",[0,0],1],
                        "pylon": 5,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\PylonName6,
                    "PylonName6": {
                        "pos": ["Pylon6",[0,0],1],
                        "pylon": 6,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_1\Draw\Group_WEAP\PylonName7,
                    "PylonName7": {
                        "pos": ["Pylon7",[0,0],1],
                        "pylon": 7,
                        "type": "pylonicon",
                        "name": "rhs_rus_circle"
                    }
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2,
        "MFD_2": {
            "topLeft": "MFD_2_TL",
            "topRight": "MFD_2_TR",
            "bottomLeft": "MFD_2_BL",
            "enableParallax": 0,
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,0,0,0.1],
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw,
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\RadioFQ_1,
                "RadioFQ_1": {
                    "type": "text",
                    "source": "static",
                    "text": "КСБ 08.125.000.000",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.74,0.1],1],
                    "right": [[0.785,0.1],1],
                    "down": [[0.74,0.145],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\RadioFQ_2,
                "RadioFQ_2": {
                    "type": "text",
                    "source": "static",
                    "text": "КСД 08.312.522.000",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.74,0.17],1],
                    "right": [[0.785,0.17],1],
                    "down": [[0.74,0.215],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\RadioFQ_3,
                "RadioFQ_3": {
                    "type": "text",
                    "source": "static",
                    "text": "НВГ 12.541.100.000",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.74,0.28],1],
                    "right": [[0.785,0.28],1],
                    "down": [[0.74,0.325],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\RadioFQ_4,
                "RadioFQ_4": {
                    "type": "text",
                    "source": "static",
                    "text": "ИРГ 00.101.512.000",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.74,0.35],1],
                    "right": [[0.785,0.35],1],
                    "down": [[0.74,0.395],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\FuelText,
                "FuelText": {
                    "type": "text",
                    "source": "static",
                    "text": "ТОПЛИВО",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.04,0.1],1],
                    "right": [[0.085,0.1],1],
                    "down": [[0.04,0.145],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\FuelSource,
                "FuelSource": {
                    "type": "text",
                    "source": "fuel",
                    "sourceScale": 4400,
                    "sourcePrecision": 0,
                    "sourceLength": 3,
                    "align": "right",
                    "scale": 1,
                    "pos": [[0.04,"0.1+0.07"],1],
                    "right": [[0.09,"0.1+0.07"],1],
                    "down": [[0.04,0.22],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\FuelText2,
                "FuelText2": {
                    "type": "text",
                    "source": "static",
                    "text": "Л",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [["0.04+0.11",0.17],1],
                    "right": [[0.195,0.17],1],
                    "down": [["0.04+0.11",0.215],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Time,
                "Time": {
                    "type": "text",
                    "source": "time",
                    "text": "%X",
                    "sourceScale": 1,
                    "align": "right",
                    "scale": 1,
                    "pos": [["0.04+0.27",0.1],1],
                    "right": [[0.355,0.1],1],
                    "down": [["0.04+0.27",0.145],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Date,
                "Date": {
                    "text": "%x",
                    "pos": [["0.04+0.27","0.1+0.07"],1],
                    "right": [[0.355,"0.1+0.07"],1],
                    "down": [["0.04+0.27",0.215],1],
                    "type": "text",
                    "source": "time",
                    "sourceScale": 1,
                    "align": "right",
                    "scale": 1
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\NavigationText,
                "NavigationText": {
                    "type": "text",
                    "source": "static",
                    "text": "НАВИГАЦИЯ",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.04,0.62],1],
                    "right": [[0.1,0.62],1],
                    "down": [[0.04,0.68],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\PositionText,
                "PositionText": {
                    "type": "text",
                    "source": "static",
                    "text": "ПОЗИЦИЯ:",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.04,0.69],1],
                    "right": [[0.09,0.69],1],
                    "down": [[0.04,0.74],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\CordX,
                "CordX": {
                    "type": "text",
                    "source": "coordinateX",
                    "sourceScale": 0.01,
                    "sourceLength": 3,
                    "sourceOffset": -0.5,
                    "align": "right",
                    "scale": 1,
                    "pos": [["0.04+0.22","0.62+0.07"],1],
                    "right": [[0.31,"0.62+0.07"],1],
                    "down": [["0.04+0.22",0.74],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\CordY,
                "CordY": {
                    "source": "coordinateY",
                    "pos": [["0.04+0.22+0.07","0.62+0.07"],1],
                    "right": [[0.38,"0.62+0.07"],1],
                    "down": [["0.04+0.22+0.07",0.74],1],
                    "type": "text",
                    "sourceScale": 0.01,
                    "sourceLength": 3,
                    "sourceOffset": -0.5,
                    "align": "right",
                    "scale": 1
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\ATLText,
                "ATLText": {
                    "type": "text",
                    "source": "static",
                    "text": "ВЫСОТА:",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [["0.04+0.03",0.76],1],
                    "right": [[0.12,0.76],1],
                    "down": [["0.04+0.03",0.81],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\ATLValue,
                "ATLValue": {
                    "type": "text",
                    "source": "altitudeAGL",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "sourceOffset": -2.1,
                    "align": "right",
                    "scale": 1,
                    "pos": [["0.04+0.22","0.62+0.14"],1],
                    "right": [[0.31,"0.62+0.14"],1],
                    "down": [["0.04+0.22",0.81],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\ATLText2,
                "ATLText2": {
                    "type": "text",
                    "source": "static",
                    "text": "м",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [["0.04+0.32",0.77],1],
                    "right": [[0.41,0.77],1],
                    "down": [["0.04+0.32",0.805],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\DirectionText,
                "DirectionText": {
                    "type": "text",
                    "source": "static",
                    "text": "КУРС:",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [["0.04+0.075",0.83],1],
                    "right": [[0.165,0.83],1],
                    "down": [["0.04+0.075",0.88],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\DirectionValue,
                "DirectionValue": {
                    "type": "text",
                    "source": "heading",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [["0.04+0.22",0.83],1],
                    "right": [[0.31,0.83],1],
                    "down": [["0.04+0.22",0.88],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Waypoints,
                "Waypoints": {
                    "condition": "wpvalid",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Waypoints\WPIndexText,
                    "WPIndexText": {
                        "type": "text",
                        "source": "static",
                        "text": "ИНДЕКС ППМ:",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.84,0.69],1],
                        "right": [[0.89,0.69],1],
                        "down": [[0.84,0.74],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Waypoints\WPIndexValue,
                    "WPIndexValue": {
                        "type": "text",
                        "source": "wpindex",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.87,0.69],1],
                        "right": [[0.92,0.69],1],
                        "down": [[0.87,0.74],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Waypoints\WPDistText,
                    "WPDistText": {
                        "type": "text",
                        "source": "static",
                        "text": "РАССТОЯНИЕ:",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [[0.84,0.76],1],
                        "right": [[0.89,0.76],1],
                        "down": [[0.84,0.81],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Waypoints\WPDistText2,
                    "WPDistText2": {
                        "type": "text",
                        "source": "static",
                        "text": "км",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "pos": [[0.94,0.77],1],
                        "right": [[0.99,0.77],1],
                        "down": [[0.94,0.805],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Waypoints\WPDistValue,
                    "WPDistValue": {
                        "type": "text",
                        "source": "WPDist",
                        "sourceScale": 0.001,
                        "sourceLength": 1,
                        "sourcePrecision": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.87,"0.62+0.07*2"],1],
                        "right": [[0.92,"0.62+0.07*2"],1],
                        "down": [[0.87,0.81],1]
                    },
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Waypoints\Waypoints,
                    "Waypoints": {
                        "condition": "user40",
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Waypoints\Waypoints\WPHeadingText,
                        "WPHeadingText": {
                            "type": "text",
                            "source": "static",
                            "text": "КУРС ДО ППМ:",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "left",
                            "pos": [[0.84,0.83],1],
                            "right": [[0.89,0.83],1],
                            "down": [[0.84,0.88],1]
                        },
                        # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\Waypoints\Waypoints\WPHeadingValue,
                        "WPHeadingValue": {
                            "type": "text",
                            "source": "user",
                            "sourceIndex": 40,
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "right",
                            "pos": [[0.87,0.83],1],
                            "right": [[0.92,0.83],1],
                            "down": [[0.87,0.88],1]
                        }
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\NoWaypoints,
                "NoWaypoints": {
                    "condition": "1- wpvalid",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\NoWaypoints\PrevText,
                    "PrevText": {
                        "type": "text",
                        "source": "static",
                        "text": "ВЫБЕРИ МАРШРУТ",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[0.76,0.73],1],
                        "right": [[0.83,0.73],1],
                        "down": [[0.76,0.8],1]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\PrevText,
                "PrevText": {
                    "type": "text",
                    "source": "static",
                    "text": "ПОВОРОТ",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.02,0.94],1],
                    "right": [[0.07,0.94],1],
                    "down": [[0.02,0.99],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\MinusText,
                "MinusText": {
                    "type": "text",
                    "source": "static",
                    "text": "-",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.69,0.94],1],
                    "right": [[0.76,0.94],1],
                    "down": [[0.69,1.01],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\MFD_2\Draw\PlusText,
                "PlusText": {
                    "type": "text",
                    "source": "static",
                    "text": "+",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.9,0.94],1],
                    "right": [[0.97,0.94],1],
                    "down": [[0.9,1.01],1]
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD,
        "HMD": {
            "topLeft": "HUD_top_left",
            "topRight": "HUD_top_right",
            "bottomLeft": "HUD_bottom_left",
            "helmetMountedDisplay": 1,
            "helmetPosition": [-0.0325,0.0325,0.1],
            "helmetRight": [0.065,0,0],
            "helmetDown": [0,-0.065,0],
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_rus",
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Bones,
            "Bones": {
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Bones\PlaneW
                "PlaneW": {
                    "type": "fixed",
                    "pos": [0.5,0.5],
                    "pos10": [0.774,0.77]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Bones\Target,
                "Target": {
                    "source": "targettoview",
                    "type": "vector",
                    "pos0": [0.5,0.5],
                    "pos10": [0.774,0.77]
                }
            },
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Draw,
            "Draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                "condition": "user2",
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Draw\SearchMode,
                "SearchMode": {
                    "condition": "1-missileLocked - missileLocking",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Draw\SearchMode\CircleLock,
                    "CircleLock": {
                        "type": "line",
                        "width": 12,
                        "points": [["PlaneW",[0,-0.0591241],1],["PlaneW",[0.010416,-0.0582254],1],["PlaneW",[0.02052,-0.0555589],1],["PlaneW",[0.03,-0.0512015],1],["PlaneW",[0.038568,-0.0452891],1],["PlaneW",[0.04596,-0.038005],1],["PlaneW",[0.05196,-0.029562],1],["PlaneW",[0.056382,-0.0202204],1],["PlaneW",[0.059088,-0.0102639],1],["PlaneW",[0.06,0],1],["PlaneW",[0.059088,0.0102639],1],["PlaneW",[0.056382,0.0202204],1],["PlaneW",[0.05196,0.029562],1],["PlaneW",[0.04596,0.038005],1],["PlaneW",[0.038568,0.0452891],1],["PlaneW",[0.03,0.0512015],1],["PlaneW",[0.02052,0.0555589],1],["PlaneW",[0.010416,0.0582254],1],["PlaneW",[0,0.0591241],1],["PlaneW",[-0.010416,0.0582254],1],["PlaneW",[-0.02052,0.0555589],1],["PlaneW",[-0.03,0.0512015],1],["PlaneW",[-0.038568,0.0452891],1],["PlaneW",[-0.04596,0.038005],1],["PlaneW",[-0.05196,0.029562],1],["PlaneW",[-0.056382,0.0202204],1],["PlaneW",[-0.059088,0.0102639],1],["PlaneW",[-0.06,0],1],["PlaneW",[-0.059088,-0.0102639],1],["PlaneW",[-0.056382,-0.0202204],1],["PlaneW",[-0.05196,-0.029562],1],["PlaneW",[-0.04596,-0.038005],1],["PlaneW",[-0.038568,-0.0452891],1],["PlaneW",[-0.03,-0.0512015],1],["PlaneW",[-0.02052,-0.0555589],1],["PlaneW",[-0.010416,-0.0582254],1],["PlaneW",[0,-0.0591241],1],[]]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Draw\InvalidLock,
                "InvalidLock": {
                    "condition": "abs(cameraHeadingDiff) > 70 - missileLocked - missileLocking",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Draw\InvalidLock\CircleLock,
                    "CircleLock": {
                        "type": "line",
                        "width": 12,
                        "points": [["PlaneW",[-0.0707107,0.0696784],1],["PlaneW",[0.0707107,-0.0696784],1],[],["PlaneW",[-0.0707107,-0.0696784],1],["PlaneW",[0.0707107,0.0696784],1]]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Draw\Locking,
                "Locking": {
                    "blinkingPattern": [0.2,0.2],
                    "blinkingStartsOn": 1,
                    "condition": "missileLocking",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Draw\Locking\CircleLock,
                    "CircleLock": {
                        "type": "line",
                        "width": 12,
                        "points": [["Target",[0,-0.0591241],1],["Target",[0.010416,-0.0582254],1],["Target",[0.02052,-0.0555589],1],["Target",[0.03,-0.0512015],1],["Target",[0.038568,-0.0452891],1],["Target",[0.04596,-0.038005],1],["Target",[0.05196,-0.029562],1],["Target",[0.056382,-0.0202204],1],["Target",[0.059088,-0.0102639],1],["Target",[0.06,0],1],["Target",[0.059088,0.0102639],1],["Target",[0.056382,0.0202204],1],["Target",[0.05196,0.029562],1],["Target",[0.04596,0.038005],1],["Target",[0.038568,0.0452891],1],["Target",[0.03,0.0512015],1],["Target",[0.02052,0.0555589],1],["Target",[0.010416,0.0582254],1],["Target",[0,0.0591241],1],["Target",[-0.010416,0.0582254],1],["Target",[-0.02052,0.0555589],1],["Target",[-0.03,0.0512015],1],["Target",[-0.038568,0.0452891],1],["Target",[-0.04596,0.038005],1],["Target",[-0.05196,0.029562],1],["Target",[-0.056382,0.0202204],1],["Target",[-0.059088,0.0102639],1],["Target",[-0.06,0],1],["Target",[-0.059088,-0.0102639],1],["Target",[-0.056382,-0.0202204],1],["Target",[-0.05196,-0.029562],1],["Target",[-0.04596,-0.038005],1],["Target",[-0.038568,-0.0452891],1],["Target",[-0.03,-0.0512015],1],["Target",[-0.02052,-0.0555589],1],["Target",[-0.010416,-0.0582254],1],["Target",[0,-0.0591241],1],[]]
                    }
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Draw\Locked,
                "Locked": {
                    "condition": "missileLocked",
                    # Class: CfgVehicles\rhs_mig29sm_base\MFD\HMD\Draw\Locked\CircleLock,
                    "CircleLock": {
                        "type": "line",
                        "width": 12,
                        "points": [["Target",[0,-0.0591241],1],["Target",[0.010416,-0.0582254],1],["Target",[0.02052,-0.0555589],1],["Target",[0.03,-0.0512015],1],["Target",[0.038568,-0.0452891],1],["Target",[0.04596,-0.038005],1],["Target",[0.05196,-0.029562],1],["Target",[0.056382,-0.0202204],1],["Target",[0.059088,-0.0102639],1],["Target",[0.06,0],1],["Target",[0.059088,0.0102639],1],["Target",[0.056382,0.0202204],1],["Target",[0.05196,0.029562],1],["Target",[0.04596,0.038005],1],["Target",[0.038568,0.0452891],1],["Target",[0.03,0.0512015],1],["Target",[0.02052,0.0555589],1],["Target",[0.010416,0.0582254],1],["Target",[0,0.0591241],1],["Target",[-0.010416,0.0582254],1],["Target",[-0.02052,0.0555589],1],["Target",[-0.03,0.0512015],1],["Target",[-0.038568,0.0452891],1],["Target",[-0.04596,0.038005],1],["Target",[-0.05196,0.029562],1],["Target",[-0.056382,0.0202204],1],["Target",[-0.059088,0.0102639],1],["Target",[-0.06,0],1],["Target",[-0.059088,-0.0102639],1],["Target",[-0.056382,-0.0202204],1],["Target",[-0.05196,-0.029562],1],["Target",[-0.04596,-0.038005],1],["Target",[-0.038568,-0.0452891],1],["Target",[-0.03,-0.0512015],1],["Target",[-0.02052,-0.0555589],1],["Target",[-0.010416,-0.0582254],1],["Target",[0,-0.0591241],1],[]]
                    }
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29sm_base\MFD\CM_Counter,
        "CM_Counter": {
            "topLeft": "MFD_CM_TL",
            "topRight": "MFD_CM_TR",
            "bottomLeft": "MFD_CM_BL",
            "enableParallax": 0,
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,1,0,0.1],
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\CM_Counter\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\CM_Counter\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 0.06,
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\CM_Counter\Draw\CMcount,
                "CMcount": {
                    "type": "text",
                    "source": "cmammo",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.5,0.2],1],
                    "right": [[0.8,0.2],1],
                    "down": [[0.5,0.7],1]
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29sm_base\MFD\EKRAN,
        "EKRAN": {
            "topLeft": "MFD_Ekran_TL",
            "topRight": "MFD_Ekran_TR",
            "bottomLeft": "MFD_Ekran_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\EKRAN\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\rhs_mig29sm_base\MFD\EKRAN\Draw,
            "Draw": {
                "color": [0.98,0.63,0],
                "alpha": 0.66,
                "condition": "gmeter>=9",
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\EKRAN\Draw\CMcount,
                "CMcount": {
                    "type": "text",
                    "source": "static",
                    "text": "Вибрация",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.5,0.2],1],
                    "right": [[0.7,0.2],1],
                    "down": [[0.5,0.4],1]
                },
                # Class: CfgVehicles\rhs_mig29sm_base\MFD\EKRAN\Draw\WarText2,
                "WarText2": {
                    "type": "text",
                    "source": "static",
                    "text": "двиг.",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "center",
                    "pos": [[0.5,0.6],1],
                    "right": [[0.7,0.6],1],
                    "down": [[0.5,0.8],1]
                }
            }
        }
    },
    "dlc": "RHS_AFRF",
    "picture": "rhsafrf|addons|rhs_mig29|data|ui|picture_mig29s_ca.paa",
    "icon": "rhsafrf|addons|rhs_mig29|data|ui|icon_mig29s_co.paa",
    "mapSize": 20,
    "vehicleClass": "rhs_vehclass_aircraft",
    "destrType": "DestructWreck",
    "cost": 2e+007,
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "extCameraPosition": [0,0,-15],
    "fuelCapacity": 500,
    "canFloat": 0,
    "waterLeakiness": 25,
    "waterResistanceCoef": 0.004,
    # Class: CfgVehicles\rhs_mig29s_base\Library,
    "Library": {
        "libEnable": 0,
        "libTextDesc": ""
    },
    "irTarget": 1,
    "irTargetSize": 1,
    "irScanGround": 1,
    "irScanRangeMin": 100,
    "irScanRangeMax": 60000,
    "irScanToEyeFactor": 2,
    "visualTarget": 1,
    "visualTargetSize": 0.9,
    "radarTarget": 1,
    "radarTargetSize": 1,
    "receiveRemoteTargets": 1,
    "reportRemoteTargets": 1,
    "reportOwnPosition": 1,
    "LESH_canBeTowed": 1,
    "LESH_towFromFront": 1,
    "LESH_AxisOffsetTarget": [0,6.8,-2.04],
    "LESH_WheelOffset": [0,-0.7],
    "selectionFireAnim": "",
    "memoryPointGun": ["machinegun"],
    "gunBeg": ["muzzle_1"],
    "gunEnd": ["chamber_1"],
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "gunAimDown": 0,
    "weapons": ["rhs_weap_MASTERSAFE","rhs_weap_GSh301"],
    "magazines": ["rhs_mag_gsh30_mixed_150"],
    "lockDetectionSystem": 8,
    "incommingMisslieDetectionSystem": 8,
    "soundLocked": ["|rhsafrf|addons|rhs_mig29|sound|locking",0.000316228,1],
    "soundIncommingMissile": ["|rhsafrf|addons|rhs_mig29|sound|incomingmissile",0.8,1],
    "weaponsGroup1": 128,
    "weaponsGroup4": 64,
    "threat": [1,1,1],
    "type": 2,
    "minFireTime": 30,
    "camouflage": 8,
    "audible": 5,
    "accuracy": 0.2,
    "ejectDamageLimit": 1,
    "availableForSupportTypes": ["CAS_Bombing"],
    # Class: CfgVehicles\rhs_mig29s_base\Turrets,
    "Turrets": {
    },
    # Class: CfgVehicles\rhs_mig29s_base\EjectionSystem,
    "EjectionSystem": {
    },
    "armor": 60,
    "damageResistance": 0.00336,
    "armorStructural": 3,
    # Class: CfgVehicles\rhs_mig29s_base\Hitpoints,
    "Hitpoints": {
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitHull
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
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitAvionics,
        "HitAvionics": {
            "armor": 0.2,
            "explosionShielding": 0.2,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitEngine,
        "HitEngine": {
            "armor": 0.7,
            "explosionShielding": 0.65,
            "passThrough": 0.01,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_l",
            "depends": "0"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitEngine2,
        "HitEngine2": {
            "armor": 0.7,
            "explosionShielding": 0.65,
            "passThrough": 0.01,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_r",
            "depends": "0"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitFuel,
        "HitFuel": {
            "armor": 1.1,
            "explosionShielding": 0.4,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel",
            "visual": "vis_fuel",
            "depends": "0"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitLAileron_link,
        "HitLAileron_link": {
            "armor": 0.7,
            "explosionShielding": 0.7,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_l",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitRAileron_link,
        "HitRAileron_link": {
            "armor": 0.7,
            "explosionShielding": 0.7,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_r",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitLAileron,
        "HitLAileron": {
            "armor": 0.2,
            "explosionShielding": 0.3,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "visual": "vis_wing_l",
            "depends": "HitLAileron_link*0.7"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitRAileron,
        "HitRAileron": {
            "armor": 0.2,
            "explosionShielding": 0.3,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "visual": "vis_wing_r",
            "depends": "HitRAileron_link*0.7"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitControlRear,
        "HitControlRear": {
            "armor": 0.2,
            "explosionShielding": 0.3,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.04,
            "material": -1,
            "name": "hit_control_rear",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitLCElevator,
        "HitLCElevator": {
            "armor": 0.2,
            "explosionShielding": 0.3,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitRElevator,
        "HitRElevator": {
            "armor": 0.2,
            "explosionShielding": 0.3,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitLCRudder,
        "HitLCRudder": {
            "armor": 0.2,
            "explosionShielding": 0.3,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_rudder_l",
            "visual": "vis_rudder_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitRightRudder,
        "HitRightRudder": {
            "armor": 0.2,
            "explosionShielding": 0.3,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_rudder_r",
            "visual": "vis_rudder_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitGlass1,
        "HitGlass1": {
            "armor": 0.2,
            "explosionShielding": 0.6,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.3,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "depends": "0"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitGlass2,
        "HitGlass2": {
            "armor": 0.2,
            "explosionShielding": 0.6,
            "passThrough": 0.01,
            "minimalHit": 0.1,
            "radius": 0.3,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "depends": "0"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\IndicatorEng1,
        "IndicatorEng1": {
            "visual": "ind_eng_l_dam",
            "depends": "HitEngine",
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0.01,
            "minimalHit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\IndicatorEng2,
        "IndicatorEng2": {
            "visual": "ind_eng_r_dam",
            "depends": "HitEngine2",
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0.01,
            "minimalHit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\IndicatorOil1,
        "IndicatorOil1": {
            "visual": "ind_oil_l",
            "depends": "HitLAileron+HitLAileron_link+HitControlRear+HitLCElevator+HitLCRudder",
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0.01,
            "minimalHit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\IndicatorOil2,
        "IndicatorOil2": {
            "visual": "ind_oil_r",
            "depends": "HitRAileron+HitRAileron_link+HitControlRear+HitRElevator+HitRightRudder",
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0.01,
            "minimalHit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon1,
        "HitPylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon1\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon1\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon1\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon1\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon1\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon2,
        "HitPylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon2\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon2\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon2\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon2\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon2\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon3,
        "HitPylon3": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_3",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon3\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon3\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon3\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon3\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon3\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon4,
        "HitPylon4": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_4",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon4\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon4\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon4\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon4\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon4\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon5,
        "HitPylon5": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_5",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon5\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon5\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon5\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon5\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon5\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon6,
        "HitPylon6": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_6",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon6\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon6\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon6\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon6\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon6\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon7,
        "HitPylon7": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_7",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.85,
            "visual": "-",
            # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon7\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon7\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon7\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon7\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_mig29s_base\Hitpoints\HitPylon7\DestructionEffects\RHS_Pylon_Shard,
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        }
    },
    "maxSpeed": 1300,
    "landingAoa": "5*3.1415/180",
    "landingSpeed": 190,
    "stallSpeed": 170,
    "stallWarningTreshold": 0.5,
    "wheelSteeringSensitivity": 2,
    "airBrake": 1,
    "airBrakeFrictionCoef": 3.3,
    "flaps": 1,
    "flapsFrictionCoef": 0.32,
    "gearsUpFrictionCoef": 0.5,
    "airFrictionCoefs0": [0,0,0],
    "airFrictionCoefs1": [0.1,0.5,0.0082],
    "airFrictionCoefs2": [0.001,0.005,7.5e-005],
    "angleOfIndicence": "1*3.1415/180",
    "envelope": [0,0.02,0.6,1.19,1.45,2.2,2.7,3.1,4.2,4.9,5.1,5,5.6,5.75,5.82,5.9,5.95,6,6.03,6.05,6.07,6.08,6.09,4,1.5],
    "altNoForce": 14000,
    "altFullForce": 6000,
    "thrustCoef": [1.54,1.46,1.37,1.35,1.21,1.17,1.02,0.97,0.92,0.85,0.7,0.3,0,0,0,0],
    "aileronSensitivity": 1.1,
    "aileronCoef": [0,0.15,0.4,0.85,1.2,1.3,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.4,1.1,0.6],
    "elevatorSensitivity": 1.6,
    "elevatorCoef": [0,0.2,0.55,0.8,1.02,1.04,1.05,1.06,1.07,1.07,1.06,1.04,1.02,1,0.9,0.6],
    "rudderInfluence": 0.866,
    "rudderCoef": [0,0.6,1,1.5,2,2.2,2.3,2.3,2,1.6,1],
    "aileronControlsSensitivityCoef": 4,
    "elevatorControlsSensitivityCoef": 3.5,
    "rudderControlsSensitivityCoef": 4,
    "draconicForceXCoef": 9,
    "draconicForceYCoef": 1.9,
    "draconicForceZCoef": 1,
    "draconicTorqueXCoef": [4.8,5,5.5,6.2,7,7.7,8.4,10.1,11,12,13],
    "draconicTorqueYCoef": [12,10,6,2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
    "gearRetracting": 1,
    "gearUpTime": 4.5,
    "gearDownTime": 3,
    "RHS_AfterBurner_FuelDrag": 0.3,
    "category": "Air",
    "DriverAction": "rhs_Mig29_Pilot",
    "driverLeftHandAnimName": "lever_pilot",
    "driverRightHandAnimName": "stick_pilot",
    "driverLeftLegAnimName": "pedal_L",
    "driverRightLegAnimName": "pedal_R",
    "viewDriverShadow": 1,
    "castDriverShadow": 1,
    "hadDriver": 1,
    "hasGunner": 0,
    "hasCommander": 1,
    "driverIsCommander": 1,
    "driverCompartments": 1,
    "HeadAimDown": 3,
    "camShakeCoef": 0.6,
    "headGforceLeaningFactor": [0.005,0.001,0.015],
    "attenuationEffectType": "PlaneAttenuation",
    "insideSoundCoef": 1,
    "soundGetIn": ["A3|Sounds_F|vehicles|air|CAS_01|getin_wipeout",1,1,40],
    "soundGetOut": ["A3|Sounds_F|air|Plane_Fighter_03|getout",1,1,40],
    "soundEngineOnInt": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_start_int",1,1],
    "soundEngineOnExt": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_start_ext",1.75,1,300],
    "soundEngineOffInt": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_shut_int",1,1],
    "soundEngineOffExt": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|O_Plane_Fighter_02_engine_shut_ext",1.75,1,300],
    "cabinOpenSound": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_open_ext",3.16228,1,40],
    "cabinCloseSound": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_close_ext",3.16228,1,40],
    "cabinOpenSoundInternal": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_open_int",10,1,40],
    "cabinCloseSoundInternal": ["A3|Sounds_F_Jets|vehicles|air|Plane_Fighter_02|FX_Plane_Fighter_02_cabine_close_int",10,1,40],
    "soundLandCrash": ["|rhsafrf|addons|rhs_mig29|sound|touch",1,1.1],
    "soundServo": ["|rhsafrf|addons|rhs_mig29|sound|gear",10,0.5],
    "soundGear": ["|rhsafrf|addons|rhs_mig29|sound|gear",10,0.5],
    "soundDammage": ["|rhsafrf|addons|rhs_mig29|sound|warn",0.562341,1],
    "soundGearUp": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_gear_up",2.25,1,250],
    "soundGearDown": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_gear_down",2.25,1,250],
    "soundFlapsUp": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_Flaps_Up",1.5,1,150],
    "soundFlapsDown": ["A3|Sounds_F_Jets|vehicles|air|Shared|FX_Plane_Jet_Flaps_Down",1.5,1,150],
    "soundSetSonicBoom": ["Plane_Fighter_SonicBoom_SoundSet"],
    # Class: CfgVehicles\rhs_mig29s_base\Sounds,
    "Sounds": {
        "soundSets": ["Plane_Fighter_02_EngineLowExt_SoundSet","Plane_Fighter_02_EngineHighExt_SoundSet","Plane_Fighter_02_ForsageExt_SoundSet","Plane_Fighter_02_WindNoiseExt_SoundSet","Plane_Fighter_02_EngineExt_Dist_Front_SoundSet","Plane_Fighter_02_EngineExt_Middle_SoundSet","Plane_Fighter_02_EngineExt_Dist_Rear_SoundSet","Plane_Fighter_02_EngineLowInt_SoundSet","Plane_Fighter_02_EngineHighInt_SoundSet","Plane_Fighter_02_ForsageInt_SoundSet","Plane_Fighter_02_WindNoiseInt_SoundSet","Plane_Fighter_02_VelocityInt_SoundSet"],
        # Class: CfgVehicles\rhs_mig29s_base\Sounds\EngineLowOut,
        "EngineLowOut": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|ext",10,1,1600],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "engineOn*camPos*(rpm factor[0.85, 0])"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Sounds\EngineHighOut,
        "EngineHighOut": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|ext",10,1.3,1800],
            "frequency": "1",
            "volume": "engineOn*camPos*(rpm factor[0.55, 1.0])"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Sounds\ForsageOut,
        "ForsageOut": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|ext-aft",3.16228,0.8,2000],
            "frequency": "1",
            "volume": "engineOn*camPos*(thrust factor[0.5, 1.0])",
            "cone": [3.14,3.92,2,0.4]
        },
        # Class: CfgVehicles\rhs_mig29s_base\Sounds\WindNoiseOut,
        "WindNoiseOut": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|ext-wind",1,1,150],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "camPos*(speed factor[1, 150])"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Sounds\EngineLowIn,
        "EngineLowIn": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|int",3.16228,1],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.85, 0]))"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Sounds\EngineHighIn,
        "EngineHighIn": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|int",3.16228,1],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(rpm factor[0.55, 1.0]))"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Sounds\ForsageIn,
        "ForsageIn": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|int-aft",1.77828,0.8],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.5, 1.0]))"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Sounds\WindNoiseIn,
        "WindNoiseIn": {
            "sound": ["|rhsafrf|addons|rhs_mig29|sound|int-wind",1,1],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "(1-camPos)*(speed factor[1, 150])"
        }
    },
    # Class: CfgVehicles\rhs_mig29s_base\ViewPilot,
    "ViewPilot": {
        "initFov": 1,
        "minFov": 0.3,
        "maxFov": 1.2,
        "initAngleX": 0,
        "minAngleX": -65,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -125,
        "maxAngleY": 125,
        "minMoveX": -0.2,
        "maxMoveX": 0.2,
        "minMoveY": -0.1,
        "maxMoveY": 0.1,
        "minMoveZ": -0.1,
        "maxMoveZ": 0.2,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    # Class: CfgVehicles\rhs_mig29s_base\Eventhandlers,
    "Eventhandlers": {
        "hit": "",
        # Class: CfgVehicles\rhs_mig29s_base\Eventhandlers\RHS_EventHandlers,
        "RHS_EventHandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "init": "_this call rhs_fnc_air_init",
            "fired": "[_this select 0,_this select 1,'RHS_Weap_GSh301',1] call rhs_fnc_burstLimiter",
            "getout": "[_this select 0, _this select 2,'rhs_mig29s_canopy'] call rhs_fnc_K36D_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes;"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Eventhandlers\BIS_Randomisation,
        "BIS_Randomisation": {
            "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;}"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    # Class: CfgVehicles\rhs_mig29s_base\Damage,
    "Damage": {
        "tex": ["rhsafrf|addons|rhs_air|t50|data|afterburner_ca.paa","#(argb,8,8,3)color(0,0,0,0,co)","rhsafrf|addons|rhs_mig29|data|rhs_mig29_warnings_empty_ca.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_warnings_ca.paa"],
        "mat": ["rhsafrf|addons|rhs_mig29|data|mig29s_glass.rvmat","rhsafrf|addons|rhs_mig29|data|mig29s_glass_damage.rvmat","rhsafrf|addons|rhs_mig29|data|mig29s_glass_damage.rvmat","rhsafrf|addons|rhs_mig29|data|skin1.rvmat","rhsafrf|addons|rhs_mig29|data|skin1_damage.rvmat","rhsafrf|addons|rhs_mig29|data|mig29s_destruct.rvmat","rhsafrf|addons|rhs_mig29|data|skin2.rvmat","rhsafrf|addons|rhs_mig29|data|skin2_damage.rvmat","rhsafrf|addons|rhs_mig29|data|mig29s_destruct.rvmat","rhsafrf|addons|rhs_mig29|data|skin3.rvmat","rhsafrf|addons|rhs_mig29|data|skin3_damage.rvmat","rhsafrf|addons|rhs_mig29|data|mig29s_destruct.rvmat"]
    },
    "hiddenselections": ["camo1","camo2","camo3","n1","n2","i1","nt1","nt2","ntt1","ntt2","nts1","nts2","nts3","nts4","nts5","ns1","ns2","ns3","it1","in1","gps_map"],
    # Class: CfgVehicles\rhs_mig29s_base\textureSources,
    "textureSources": {
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Standard
        "Standard": {
            "author": "Red Hammer Studios",
            "displayName": "Blue",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Gray,
        "Gray": {
            "displayName": "Gray",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_gray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_gray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_gray_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\LightGray,
        "LightGray": {
            "displayName": "Light Gray",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_lgray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_lgray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_lgray_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\LightGray2,
        "LightGray2": {
            "displayName": "Light Gray 2",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_lgray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_lgray2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_lgray_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Gray_camo,
        "Gray_camo": {
            "displayName": "Gray Camo",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_gray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_gray_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_gray_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo,
        "Green_camo": {
            "displayName": "Green Camo 1",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo2,
        "Green_camo2": {
            "displayName": "Green Camo 2",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo3,
        "Green_camo3": {
            "displayName": "Green Camo 3",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green22_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo4,
        "Green_camo4": {
            "displayName": "Green Camo 4",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green23_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo5,
        "Green_camo5": {
            "displayName": "Green Camo 5",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green24_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo6,
        "Green_camo6": {
            "displayName": "Green Camo 6",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green25_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo7,
        "Green_camo7": {
            "displayName": "Green Camo 7",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green3_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green3_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green3_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo_kubinka,
        "Green_camo_kubinka": {
            "displayName": "Green Camo Kubinka",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green_kubinka.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green_kubinka.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green_kubinka.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo_lipetsk,
        "Green_camo_lipetsk": {
            "displayName": "Green Camo Lipetsk",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green_lipetsk_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green24_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green_lipetsk_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo_aggressor1,
        "Green_camo_aggressor1": {
            "displayName": "Aggressor 1",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green_aggressor1_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green_aggressor1_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green2_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\Green_camo_aggressor2,
        "Green_camo_aggressor2": {
            "displayName": "Aggressor 2",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_mig29|data|rhs_mig29_01_mimic_green_aggressor2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_02_mimic_green_aggressor2_co.paa","rhsafrf|addons|rhs_mig29|data|rhs_mig29_03_mimic_green_aggressor2_co.paa"],
            "factions": ["rhs_faction_vvs","rhs_faction_vvs_c","rhs_faction_vmf"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\RHS_SAF_Gray,
        "RHS_SAF_Gray": {
            "displayName": "SAF (Gray)",
            "author": "Red Hammer Studios",
            "textures": ["rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_01_gray_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_02_gray_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_03_gray_co.paa"],
            "factions": ["rhssaf_faction_airforce"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\RHS_SAF_Blue,
        "RHS_SAF_Blue": {
            "displayName": "SAF (Blue-Gray)",
            "author": "Red Hammer Studios",
            "textures": ["rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_01_blue_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_02_blue_co.paa","rhssaf|addons|rhssaf_t_vehicle_ret|mig29|data|rhs_mig29_03_blue_co.paa"],
            "factions": ["rhssaf_faction_airforce"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\RHS_CDF1,
        "RHS_CDF1": {
            "displayName": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_01_cdf1_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_02_cdf1_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_03_cdf1_co.paa"],
            "factions": ["rhsgref_faction_cdf_air","rhsgref_faction_cdf_air_b"],
            "materials": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_01_cdf1.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_02_cdf1.rvmat","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_03_cdf1.rvmat"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\RHS_CDF2,
        "RHS_CDF2": {
            "displayName": "CDF (Summer)",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_01_cdf2_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_02_cdf2_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_03_cdf2_co.paa"],
            "factions": ["rhsgref_faction_cdf_air","rhsgref_faction_cdf_air_b"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\RHS_CDF3,
        "RHS_CDF3": {
            "displayName": "CDF (Winter)",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_01_cdf3_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_02_cdf3_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_03_cdf3_co.paa"],
            "factions": ["rhsgref_faction_cdf_air","rhsgref_faction_cdf_air_b"]
        },
        # Class: CfgVehicles\rhs_mig29s_base\textureSources\RHS_TKA,
        "RHS_TKA": {
            "displayName": "Takistan",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_01_tka_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_02_tka_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_mig29_03_tka_co.paa"],
            "factions": [""]
        }
    },
    # Class: CfgVehicles\rhs_mig29s_base\Attributes,
    "Attributes": {
        # Class: CfgVehicles\rhs_mig29s_base\Attributes\ObjectTexture
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type,
        "rhs_decalNumber_type": {
            "displayName": "Define font type of intake number",
            "tooltip": "Define kind of font that will be drawn on vehicle intake",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', [cRHSAIRMIG29NumberPlaces,cRHSAIRMIG29TailNumberPlaces, cRHSAIRMIG29TailTopNumberPlaces], [_value,_this getVariable ['rhs_decalTailNumber_type',['AviaWhite','AviaYellow','Empty']],['AviaWhite','Empty']]]]] call rhs_fnc_decalsInit}",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values,
            "values": {
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\NoChange
                "NoChange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\Hidden,
                "Hidden": {
                    "name": "Hidden",
                    "value": "Empty"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\AviaYellow,
                "AviaYellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\AviaBlue,
                "AviaBlue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultValue": "AviaBlue"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\AviaRed,
                "AviaRed": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\AviaWhiteOut,
                "AviaWhiteOut": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\AviaWhite,
                "AviaWhite": {
                    "name": "Aviation White",
                    "value": "AviaWhite"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\AviaWhiteShadow,
                "AviaWhiteShadow": {
                    "name": "Aviation White Shadow",
                    "value": "AviaWhiteShadow"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\AviaOrange,
                "AviaOrange": {
                    "name": "Aviation Orange",
                    "value": "AviaOrange"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\AviaCDF,
                "AviaCDF": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\Default,
                "Default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\DefaultRed,
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\BoldRed,
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\CDF,
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\Handpaint,
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\HandpaintBlack,
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber_type\values\Iraqi,
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type,
        "rhs_decalTailNumber_type": {
            "displayName": "Define font type of tail number",
            "tooltip": "Define kind of font that will be drawn on vehicle tail",
            "property": "rhs_decalTailNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', [cRHSAIRMIG29NumberPlaces,cRHSAIRMIG29TailNumberPlaces, cRHSAIRMIG29TailTopNumberPlaces], [_this getVariable ['rhs_decalNumber_type',['AviaWhite','AviaRed','AviaBlue','AviaOrange','AviaWhiteShadow']],_value,['AviaWhite','Empty']]]]] call rhs_fnc_decalsInit}",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values,
            "values": {
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\NoChange
                "NoChange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\Hidden,
                "Hidden": {
                    "name": "Hidden",
                    "value": "Empty"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\AviaYellow,
                "AviaYellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\AviaBlue,
                "AviaBlue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultValue": "AviaBlue"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\AviaRed,
                "AviaRed": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\AviaWhiteOut,
                "AviaWhiteOut": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\AviaWhite,
                "AviaWhite": {
                    "name": "Aviation White",
                    "value": "AviaWhite"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\AviaWhiteShadow,
                "AviaWhiteShadow": {
                    "name": "Aviation White Shadow",
                    "value": "AviaWhiteShadow"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\AviaOrange,
                "AviaOrange": {
                    "name": "Aviation Orange",
                    "value": "AviaOrange"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\AviaCDF,
                "AviaCDF": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\Default,
                "Default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\DefaultRed,
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\BoldRed,
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\CDF,
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\Handpaint,
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\HandpaintBlack,
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTailNumber_type\values\Iraqi,
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNumber,
        "rhs_decalNumber": {
            "displayName": "Set side number",
            "tooltip": "Set side number. 2 numbers are required. Type 0 to hide numbers completly",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "defaultValue": "-1",
            "typeName": "Number",
            "expression": "if(_value >= 0)then{if(_value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRMIG29NumberPlaces;{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRMIG29TailNumberPlaces;{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRMIG29TailTopNumberPlaces}else{[_this, [['Number', [cRHSAIRMIG29NumberPlaces,cRHSAIRMIG29TailNumberPlaces, cRHSAIRMIG29TailTopNumberPlaces], [_this getVariable ['rhs_decalNumber_type',['AviaWhite','AviaRed','AviaBlue','AviaOrange','AviaWhiteShadow']],_this getVariable ['rhs_decalTailNumber_type',['AviaWhite','AviaYellow','Empty']],['AviaWhite','Empty']], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalRoundel,
        "rhs_decalRoundel": {
            "displayName": "Define Roundel",
            "tooltip": "Define Roundel texture located on the wings and tail.",
            "property": "rhs_decalRoundel",
            "control": "Combo",
            "expression": "if(_value >= 0)then{ [_this, [[ 'Label', cRHSAIRMIG29StarPlaces, 'Aviation', _value ]]] call rhs_fnc_decalsInit};",
            "defaultValue": "-1",
            "typeName": "Number",
            # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalRoundel\values,
            "values": {
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalRoundel\values\Random
                "Random": {
                    "name": "Random",
                    "value": -1,
                    "defaultValue": -1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalRoundel\values\Empty,
                "Empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalRoundel\values\RU_Star_Old,
                "RU_Star_Old": {
                    "name": "Russia",
                    "value": 2
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalRoundel\values\RU_Star_New2,
                "RU_Star_New2": {
                    "name": "Russia (New)",
                    "value": 7
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalRoundel\values\CDF,
                "CDF": {
                    "name": "Chernarus",
                    "value": 4
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalRoundel\values\CDF_New,
                "CDF_New": {
                    "name": "Chernarus (Gray)",
                    "value": 5
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalRoundel\values\Takistan,
                "Takistan": {
                    "name": "Takistan",
                    "value": 6
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt,
        "rhs_decalNoseArt": {
            "displayName": "Define Nose Art",
            "tooltip": "Define Nose Art texture located near the cabin.",
            "property": "rhs_decalNoseArt",
            "control": "Combo",
            "expression": "if(_value >= 0)then{ [_this, [[ 'Label', cRHSAIRMIG29NosePlaces, 'Mig29NoseArt', _value ]]] call rhs_fnc_decalsInit};",
            "defaultValue": "-1",
            "typeName": "Number",
            # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values,
            "values": {
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Random
                "Random": {
                    "name": "Random",
                    "value": -1,
                    "defaultValue": -1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Empty,
                "Empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\VvsRandom,
                "VvsRandom": {
                    "name": "VVS Random",
                    "value": 1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Vmf,
                "Vmf": {
                    "name": "VMF Flag",
                    "value": 2
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Excellence,
                "Excellence": {
                    "name": "Aircraft of Excellence",
                    "value": 8
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Mig787,
                "Mig787": {
                    "name": "787th IAP (MiG Logo)",
                    "value": 3
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Shark1,
                "Shark1": {
                    "name": "Shark Mouth 1",
                    "value": 4
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Shark2,
                "Shark2": {
                    "name": "Shark Mouth 2",
                    "value": 5
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Iap33,
                "Iap33": {
                    "name": "33rd IAP",
                    "value": 6
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Osad21,
                "Osad21": {
                    "name": "21st OSAD",
                    "value": 7
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Iap968,
                "Iap968": {
                    "name": "968th IAP",
                    "value": 9
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Iap960,
                "Iap960": {
                    "name": "960th IAP",
                    "value": 10
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalNoseArt\values\Gvardiya,
                "Gvardiya": {
                    "name": "Guards Regiment",
                    "value": 11
                }
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail,
        "rhs_decalTail": {
            "displayName": "Define Tail Art",
            "tooltip": "Define tail decal that will be drawn on vehicle",
            "property": "rhs_decalTail",
            "control": "Combo",
            "expression": "if(_value >= 0)then{[_this,[['Label', cRHSAIRMIG29TailPlaces, 'Mig29TailSign',_value]]] call rhs_fnc_decalsInit};",
            "defaultValue": -1,
            "typeName": "Number",
            # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values,
            "values": {
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\Default
                "Default": {
                    "name": "Default",
                    "value": -1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\Empty,
                "Empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\VMF,
                "VMF": {
                    "name": "VMF Russia",
                    "value": 1,
                    "defaultValue": 1
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\VVS,
                "VVS": {
                    "name": "VVS Russia",
                    "value": 2
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\VvsRandom,
                "VvsRandom": {
                    "name": "VVS Random",
                    "value": 3
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\Mary1st,
                "Mary1st": {
                    "name": "Mary 1st AB Bee",
                    "value": 4
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\Iap33,
                "Iap33": {
                    "name": "33rd IAP",
                    "value": 5
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\Iap120,
                "Iap120": {
                    "name": "120th IAP",
                    "value": 6
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\Iap404,
                "Iap404": {
                    "name": "404th IAP",
                    "value": 7
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\Ab1521,
                "Ab1521": {
                    "name": "1521st AB",
                    "value": 8
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\Mig,
                "Mig": {
                    "name": "787th IAP (MiG Logo)",
                    "value": 9
                },
                # Class: CfgVehicles\rhs_mig29s_base\Attributes\rhs_decalTail\values\Rusavia,
                "Rusavia": {
                    "name": "787th IAP (Rusavia)",
                    "value": 10
                }
            }
        }
    },
    # Class: CfgVehicles\rhs_mig29s_base\compartmentsLights,
    "compartmentsLights": {
        # Class: CfgVehicles\rhs_mig29s_base\compartmentsLights\Comp1
        "Comp1": {
            # Class: CfgVehicles\rhs_mig29s_base\compartmentsLights\Comp1\Light_General
            "Light_General": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.15,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\rhs_mig29s_base\compartmentsLights\Comp1\Light_General\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.65,
                    "hardLimitEnd": 0.95
                },
                "point": "light_general"
            }
        }
    },
    # Class: CfgVehicles\rhs_mig29s_base\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Left
        "Left": {
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "position": "light_l_source",
            "direction": "light_l_target",
            "hitpoint": "light_l",
            "selection": "light_l",
            "size": 1,
            "brightness": 1,
            "intensity": 5e+006,
            "innerAngle": 20,
            "outerAngle": 120,
            "coneFadeCoef": 50,
            "useFlare": 0,
            # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Left_flare,
        "Left_flare": {
            "innerAngle": 10,
            "outerAngle": 170,
            "useFlare": 1,
            "intensity": 111,
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "position": "light_l_source",
            "direction": "light_l_target",
            "hitpoint": "light_l",
            "selection": "light_l",
            "size": 1,
            "brightness": 1,
            "coneFadeCoef": 50,
            # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Right,
        "Right": {
            "position": "light_r_source",
            "direction": "light_r_target",
            "hitpoint": "light_r",
            "selection": "light_r",
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "size": 1,
            "brightness": 1,
            "intensity": 5e+006,
            "innerAngle": 20,
            "outerAngle": 120,
            "coneFadeCoef": 50,
            "useFlare": 0,
            # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Right_flare,
        "Right_flare": {
            "innerAngle": 120,
            "outerAngle": 170,
            "useFlare": 1,
            "intensity": 111,
            "position": "light_r_source",
            "direction": "light_r_target",
            "hitpoint": "light_r",
            "selection": "light_r",
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "size": 1,
            "brightness": 1,
            "coneFadeCoef": 50,
            # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Center,
        "Center": {
            "position": "light_f_source",
            "direction": "light_f_target",
            "hitpoint": "light_f",
            "selection": "light_f",
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "size": 1,
            "brightness": 1,
            "intensity": 5e+006,
            "innerAngle": 20,
            "outerAngle": 120,
            "coneFadeCoef": 50,
            "useFlare": 0,
            # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Center_flare,
        "Center_flare": {
            "innerAngle": 120,
            "outerAngle": 170,
            "useFlare": 1,
            "intensity": 111,
            "position": "light_f_source",
            "direction": "light_f_target",
            "hitpoint": "light_f",
            "selection": "light_f",
            "color": [0.8,0.8,1,1],
            "ambient": [0.07,0.07,0.07,1],
            "size": 1,
            "brightness": 1,
            "coneFadeCoef": 50,
            # Class: CfgVehicles\rhs_mig29s_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            }
        }
    },
    "aggregateReflectors": [["Left"],["Left_flare"],["Right"],["Right_flare"],["Center"],["Center_flare"]],
    # Class: CfgVehicles\rhs_mig29s_base\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\rhs_mig29s_base\Exhausts\Exhaust1
        "Exhaust1": {
            "position": "exhaust_l_axis_base",
            "direction": "exhaust_l_axis_end",
            "effect": "RHS_ExhaustsEffectPlaneHP",
            "engineIndex": 0
        },
        # Class: CfgVehicles\rhs_mig29s_base\Exhausts\Exhaust2,
        "Exhaust2": {
            "position": "exhaust_r_axis_base",
            "direction": "exhaust_r_axis_end",
            "effect": "RHS_ExhaustsEffectPlaneHP",
            "engineIndex": 1
        }
    },
    # Class: CfgVehicles\rhs_mig29s_base\WingVortices,
    "WingVortices": {
        # Class: CfgVehicles\rhs_mig29s_base\WingVortices\WingTipLeft
        "WingTipLeft": {
            "effectName": "WingVortices",
            "position": "light_nav_left"
        },
        # Class: CfgVehicles\rhs_mig29s_base\WingVortices\WingTipRight,
        "WingTipRight": {
            "effectName": "WingVortices",
            "position": "light_nav_right"
        },
        # Class: CfgVehicles\rhs_mig29s_base\WingVortices\BodyLeft,
        "BodyLeft": {
            "effectName": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles\rhs_mig29s_base\WingVortices\BodyRight,
        "BodyRight": {
            "effectName": "BodyVortices",
            "position": "body_vapour_R_S"
        }
    },
    "maxOmega": 2000,
    # Class: CfgVehicles\rhs_mig29s_base\Wheels,
    "Wheels": {
        "disableWheelsWhenDestroyed": 1,
        # Class: CfgVehicles\rhs_mig29s_base\Wheels\Wheel_1,
        "Wheel_1": {
            "boneName": "fg_damper",
            "steering": 1,
            "side": "left",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 150,
            "MOI": 40,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 21500,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "suspForceAppPointOffset": "Wheel_1_center",
            "tireForceAppPointOffset": "Wheel_1_center",
            "maxCompression": 0.18,
            "maxDroop": 0.18,
            "sprungMass": 3966,
            "springStrength": 56600,
            "springDamperRate": 215570,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\rhs_mig29s_base\Wheels\Wheel_1_fake,
        "Wheel_1_fake": {
            "boneName": "fg_damper",
            "steering": 1,
            "side": "left",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.16,
            "mass": 150,
            "MOI": 40,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 21500,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "suspForceAppPointOffset": "Wheel_1_center",
            "tireForceAppPointOffset": "Wheel_1_center",
            "maxCompression": 0.18,
            "maxDroop": 0.18,
            "sprungMass": 3966,
            "springStrength": 56600,
            "springDamperRate": 215570,
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\rhs_mig29s_base\Wheels\Wheel_2,
        "Wheel_2": {
            "boneName": "lg_damper",
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "suspForceAppPointOffset": "Wheel_2_center",
            "tireForceAppPointOffset": "Wheel_2_center",
            "steering": 0,
            "width": 0.28,
            "maxCompression": 0.13,
            "maxDroop": 0.13,
            "sprungMass": 4652,
            "springDamperRate": 220570,
            "springStrength": 151000,
            "side": "left",
            "mass": 150,
            "MOI": 40,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 21500,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\rhs_mig29s_base\Wheels\Wheel_3,
        "Wheel_3": {
            "boneName": "rg_damper",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspForceAppPointOffset": "Wheel_3_center",
            "tireForceAppPointOffset": "Wheel_3_center",
            "side": "right",
            "steering": 0,
            "width": 0.28,
            "maxCompression": 0.13,
            "maxDroop": 0.13,
            "sprungMass": 4652,
            "springDamperRate": 220570,
            "springStrength": 151000,
            "mass": 150,
            "MOI": 40,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 21500,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "longitudinalStiffnessPerUnitGravity": 5000,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    # Class: CfgVehicles\rhs_mig29s_base\MarkerLights,
    "MarkerLights": {
        # Class: CfgVehicles\rhs_mig29s_base\MarkerLights\PositionRed
        "PositionRed": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 500,
            "name": "light_nav_left",
            "drawLight": 1.5,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\rhs_mig29s_base\MarkerLights\PositionRed\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\MarkerLights\PositionGreen,
        "PositionGreen": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "light_nav_right",
            "intensity": 500,
            "drawLight": 1.5,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\rhs_mig29s_base\MarkerLights\PositionRed\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\rhs_mig29s_base\MarkerLights\PositionWhite,
        "PositionWhite": {
            "color": [1,1,1],
            "ambient": [0.08,0.08,0.08],
            "name": "light_nav_back",
            "intensity": 500,
            "drawLight": 1.5,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\rhs_mig29s_base\MarkerLights\PositionRed\Attenuation,
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
    # Class: CfgVehicles\rhs_mig29s_base\UserActions,
    "UserActions": {
        # Class: CfgVehicles\rhs_mig29s_base\UserActions\SAFEMODE
        "SAFEMODE": {
            "displayName": "<t color='#00FF7F'>MASTERSAFE</t>",
            "condition": "(call rhs_fnc_findPlayer) in this",
            "statement": "(call rhs_fnc_findPlayer) action ['SwitchWeapon', this, (call rhs_fnc_findPlayer), (weapons this) find 'rhs_weap_MASTERSAFE'];",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showWindow": 0,
            "shortcut": "user13",
            "hideOnUse": 1
        },
        # Class: CfgVehicles\rhs_mig29s_base\UserActions\FilterOn,
        "FilterOn": {
            "displayName": "Sunfilter on",
            "condition": "(call rhs_fnc_findPlayer) in this && (this animationPhase 'AnimateSunfilter' == 0)",
            "statement": "this animate ['AnimateSunfilter',1];",
            "priority": 0.5,
            "position": "",
            "radius": 10,
            "onlyforplayer": 1,
            "showWindow": 0,
            "shortcut": "user13",
            "hideOnUse": 1
        },
        # Class: CfgVehicles\rhs_mig29s_base\UserActions\FilterOff,
        "FilterOff": {
            "displayName": "Sunfilter off",
            "condition": "(this animationPhase 'AnimateSunfilter' == 1)",
            "statement": "this animate ['AnimateSunfilter',0];",
            "priority": 0.5,
            "position": "",
            "radius": 10,
            "onlyforplayer": 1,
            "showWindow": 0,
            "shortcut": "user13",
            "hideOnUse": 1
        },
        # Class: CfgVehicles\rhs_mig29s_base\UserActions\Helmet,
        "Helmet": {
            "displayName": "Toggle HMD",
            "shortcut": "user14",
            "statement": "if(this getVariable ['rhs_mfd_2',false])then{this setUserMFDvalue [2,0];this setVariable ['rhs_mfd_2',false]}else{this setUserMFDvalue [2,1];this setVariable ['rhs_mfd_2',true]}",
            "condition": "(call rhs_fnc_findPlayer) in this",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showWindow": 0,
            "hideOnUse": 1
        },
        # Class: CfgVehicles\rhs_mig29s_base\UserActions\Reticle,
        "Reticle": {
            "displayName": "<t color='#FBB829'>Toggle reticle</t>",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showWindow": 0,
            "hideOnUse": 1,
            "condition": "(call rhs_fnc_findPlayer) in this",
            "shortcut": "user10",
            "statement": "if(((getUserMFDvalue this) select 3) isEqualTo 0)then{this setUserMFDvalue [3,1];}else{this setUserMFDvalue [3,0];}"
        },
        # Class: CfgVehicles\rhs_mig29s_base\UserActions\Mirrors,
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
            "statement": "this animateSource ['fold_mirrors',abs((this animationSourcePhase 'fold_mirrors') -1)]"
        }
    },
    # Class: CfgVehicles\rhs_mig29s_base\RenderTargets,
    "RenderTargets": {
        # Class: CfgVehicles\rhs_mig29s_base\RenderTargets\Mirror
        "Mirror": {
            "renderTarget": "rendertarget0",
            # Class: CfgVehicles\rhs_mig29s_base\RenderTargets\Mirror\CameraView1,
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
    "defaultUserMFDstrings": ["rhsafrf|addons|rhs_c_a2port_air|Su25|rhs_su25_reticle_static_ca.paa"],
    "_generalMacro": "Plane_Base_F",
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "waterLinearDampingCoefY": 0,
    "waterLinearDampingCoefX": 5,
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
    # Class: CfgVehicles\Plane_Base_F\TransportItems,
    "TransportItems": {
        # Class: CfgVehicles\Plane_Base_F\TransportItems\_xx_FirstAidKit
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 4
        },
        # Class: CfgVehicles\Plane_Base_F\TransportItems\_xx_ItemGPS,
        "_xx_ItemGPS": {
            "name": "ItemGPS",
            "count": 1
        },
        # Class: CfgVehicles\Plane_Base_F\TransportItems\_xx_ItemRadio,
        "_xx_ItemRadio": {
            "name": "ItemRadio",
            "count": 1
        }
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
    "brakeDistance": 500,
    "steerAheadSimul": 1,
    "steerAheadPlan": 2,
    "cabinOpening": 1,
    "durationGetIn": 0.99,
    "durationGetOut": 0.99,
    "vtol": 0,
    "tailHook": 0,
    "lightOnGear": 1,
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
    "memoryPointLRocket": "L raketa",
    "memoryPointRRocket": "P raketa",
    "memoryPointLDust": "levy prach",
    "memoryPointRDust": "pravy prach",
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
    "fuelExplosionPower": 10,
    "epeImpulseDamageCoef": 10,
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
    "minTotalDamageThreshold": 0.005,
    # Class: CfgVehicles\Plane\DestructionEffects,
    "DestructionEffects": {
    },
    "formationTime": 10,
    "outsideSoundFilter": 1,
    "occludeSoundsWhenIn": 0.316228,
    "obstructSoundsWhenIn": 0.316228,
    "nightVision": 0,
    "cargoCompartments": [0],
    "enableGPS": 1,
    "weaponsGroup2": 4,
    "weaponsGroup3": "8 + 	16 + 	32",
    "editorSubcategory": "EdSubcat_Planes",
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    "maxFordingDepth": 0.001,
    "waterResistance": 1,
    "impactEffectsSea": "ImpactEffectsAir",
    "flareVelocity": 100,
    "enableRadio": 1,
    "radarType": 4,
    "incomingMissileDetectionSystem": "8 + 16",
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
    "memoryPointTaskMarker": "",
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
    "cargoProxyIndexes": [],
    "driverDoor": "",
    "cargoDoors": [],
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "preciseGetInOut": 0,
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
    "soundWaterCrash": ["",0.177828,1],
    "soundElevation": ["",0.00316228,0.5],
    "sounddamage": ["",1,1],
    "soundCrashes": ["soundCrash",1],
    "soundLandCrashes": ["soundLandCrash",1],
    "soundWaterCrashes": ["soundWaterCrash",1],
    "emptySound": ["",0,1],
    "soundWoodCrash": ["emptySound",0],
    "soundBushCrash": ["emptySound",0],
    "soundBuildingCrash": ["emptySound",0],
    "soundArmorCrash": ["emptySound",0],
    "driverInAction": "",
    "cargoAction": [],
    "cargoIsCoDriver": [0],
    "driverOpticsModel": "",
    "driverOpticsEffect": [],
    "driverOpticsColor": [1,1,1,1],
    "hideProxyInCombat": 0,
    "forceHideDriver": 0,
    "canHideDriver": -1,
    "castCargoShadow": 0,
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
    # Class: CfgVehicles\All\FxExplo,
    "FxExplo": {
        "access": 1
    },
    "selectionDamage": "zbytek",
    "cargoCanEject": 1,
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