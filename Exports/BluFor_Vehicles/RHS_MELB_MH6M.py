RHS_MELB_MH6M = {
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhs_MELB_MH6M.paa",
    "scope": 2,
    "forceInGarage": 1,
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf|addons|rhsusf_melb|Data|ui|melb_mh_6m_ca.paa",
    "icon": "rhsusf|addons|rhsusf_melb|Data|ui|map_melb_mh_6m_ca.paa",
    "displayName": "MH-6M Little Bird",
    "fuelCapacity": 436,
    "fuelConsumptionRate": 0.08,
    "ejectDeadCargo": 0,
    "transportsoldier": 1,
    "cargoProxyIndexes": [9],
    "threat": [0.6,0.4,0.1],
    "cost": 7e+006,
    "availableForSupportTypes": ["Drop","Transport"],
    # Class: CfgVehicles\RHS_MELB_MH6M\Turrets,
    "Turrets": {
        # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CopilotTurret
        "CopilotTurret": {
            "gunnerCompartments": "Compartment1",
            "body": "obsTurret",
            "gun": "obsGun",
            "animationSourceBody": "obsTurret",
            "animationSourceGun": "obsGun",
            "turretInfoType": "Rsc_MELB_Turret_UnitInfo",
            "stabilizedInAxes": 3,
            "memoryPointGunnerOptics": "commanderview",
            "minElev": -180,
            "maxElev": 180,
            "initElev": 0,
            "minTurn": -180,
            "maxTurn": 180,
            "initTurn": 0,
            "minFov": 0.25,
            "maxFov": 0.9,
            "initFov": 0.75,
            "lodTurnedOut": 1100,
            "lodTurned": 1100,
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "memoryPointsGetInGunnerPrecise": "pos gunner",
            "gunBeg": "commanderview",
            "gunEnd": "laserstart",
            "memoryPointGun": "commanderview",
            "discretedistance": [100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600,2700,2800,2900,3000],
            "discretedistanceinitindex": 3,
            "weapons": ["rhs_weap_laserDesignator_AI","rhs_weap_fcs_ah64","rhsusf_weap_LWIRCM"],
            "magazines": ["rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhs_laserfcsmag","rhs_LaserMag_ai"],
            "soundServo": ["",0.01,1,30],
            "inGunnerMayFire": 1,
            "outGunnerMayFire": 1,
            "primaryGunner": 1,
            "gunnerAction": "MELB_Copilot",
            "gunnerInAction": "MELB_Copilot",
            "usePreciseGetInAction": 1,
            "precisegetinout": 0,
            "gunnerGetInAction": "Chopperlight_R_In_H",
            "gunnergetOutAction": "GetOutLow",
            "gunnerOpticsModel": "",
            "TurretCanSee": "1+2+4+8",
            "showAllTargets": 1,
            "gunnerHasFlares": 1,
            "usepip": 1,
            "canUseScanners": 1,
            "allowTabLock": 0,
            # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\ViewGunner,
            "ViewGunner": {
                "minAngleX": -65,
                "maxAngleX": 85,
                "initAngleX": 0,
                "minAngleY": -150,
                "maxAngleY": 150,
                "initAngleY": 0,
                "minFov": 0.25,
                "maxFov": 0.9,
                "initFov": 0.75
            },
            # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\OpticsIn\Wide
                "Wide": {
                    "opticsDisplayName": "TRK COR",
                    "initAngleX": 0,
                    "minAngleX": -360,
                    "maxAngleX": 360,
                    "initAngleY": 0,
                    "minAngleY": -15,
                    "maxAngleY": 85,
                    "initFov": 0.3,
                    "minFov": 0.3,
                    "maxFov": 0.3,
                    "visionMode": ["Normal","NVG","Ti"],
                    "thermalMode": [0],
                    "directionStabilized": 1,
                    "horizontallyStabilized": 1,
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_melb|data|optics|melb_flir_wf.p3d",
                    "opticsPPEffects": ["OpticsCHAbera3","OpticsBlur3"],
                    "gunnerOpticsEffect": ["TankCommanderOptics2"]
                },
                # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\OpticsIn\WideT,
                "WideT": {
                    "initFov": 0.2,
                    "minFov": 0.2,
                    "maxFov": 0.2,
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_melb|data|optics|melb_flir_w2.p3d",
                    "opticsDisplayName": "TRK COR",
                    "initAngleX": 0,
                    "minAngleX": -360,
                    "maxAngleX": 360,
                    "initAngleY": 0,
                    "minAngleY": -15,
                    "maxAngleY": 85,
                    "visionMode": ["Normal","NVG","Ti"],
                    "thermalMode": [0],
                    "directionStabilized": 1,
                    "horizontallyStabilized": 1,
                    "opticsPPEffects": ["OpticsCHAbera3","OpticsBlur3"],
                    "gunnerOpticsEffect": ["TankCommanderOptics2"]
                },
                # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\OpticsIn\MediumT,
                "MediumT": {
                    "initFov": 0.1,
                    "minFov": 0.1,
                    "maxFov": 0.1,
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_melb|data|optics|melb_flir_m.p3d",
                    "opticsDisplayName": "TRK COR",
                    "initAngleX": 0,
                    "minAngleX": -360,
                    "maxAngleX": 360,
                    "initAngleY": 0,
                    "minAngleY": -15,
                    "maxAngleY": 85,
                    "visionMode": ["Normal","NVG","Ti"],
                    "thermalMode": [0],
                    "directionStabilized": 1,
                    "horizontallyStabilized": 1,
                    "opticsPPEffects": ["OpticsCHAbera3","OpticsBlur3"],
                    "gunnerOpticsEffect": ["TankCommanderOptics2"]
                },
                # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\OpticsIn\NarrowT,
                "NarrowT": {
                    "initFov": 0.022,
                    "minFov": 0.022,
                    "maxFov": 0.022,
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_melb|data|optics|melb_flir_n.p3d",
                    "opticsDisplayName": "TRK COR",
                    "initAngleX": 0,
                    "minAngleX": -360,
                    "maxAngleX": 360,
                    "initAngleY": 0,
                    "minAngleY": -15,
                    "maxAngleY": 85,
                    "visionMode": ["Normal","NVG","Ti"],
                    "thermalMode": [0],
                    "directionStabilized": 1,
                    "horizontallyStabilized": 1,
                    "opticsPPEffects": ["OpticsCHAbera3","OpticsBlur3"],
                    "gunnerOpticsEffect": ["TankCommanderOptics2"]
                },
                # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\OpticsIn\NarrowT2,
                "NarrowT2": {
                    "initFov": 0.0092,
                    "minFov": 0.0092,
                    "maxFov": 0.0092,
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_melb|data|optics|melb_flir_n2.p3d",
                    "opticsDisplayName": "TRK COR",
                    "initAngleX": 0,
                    "minAngleX": -360,
                    "maxAngleX": 360,
                    "initAngleY": 0,
                    "minAngleY": -15,
                    "maxAngleY": 85,
                    "visionMode": ["Normal","NVG","Ti"],
                    "thermalMode": [0],
                    "directionStabilized": 1,
                    "horizontallyStabilized": 1,
                    "opticsPPEffects": ["OpticsCHAbera3","OpticsBlur3"],
                    "gunnerOpticsEffect": ["TankCommanderOptics2"]
                }
            },
            # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\Components,
            "Components": {
                # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: VehicleSystemsTemplateLeftPilot\Components
                    "Components": {
                        # Class: VehicleSystemsTemplateLeftPilot\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\MinimapDisplay,
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\CrewDisplay,
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\SlingLoadDisplay,
                        "SlingLoadDisplay": {
                            "componentType": "SlingLoadDisplayComponent",
                            "resource": "RscCustomInfoSlingLoad"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\UAVDisplay,
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\VehicleDriverDisplay,
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateLeftPilot\Components\SensorDisplay,
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
                # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    "defaultDisplay": "SensorDisplay",
                    # Class: VehicleSystemsTemplateRightPilot\Components,
                    "Components": {
                        # Class: VehicleSystemsTemplateRightPilot\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\MinimapDisplay,
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoAirborneMiniMap"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\CrewDisplay,
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\SlingLoadDisplay,
                        "SlingLoadDisplay": {
                            "componentType": "SlingLoadDisplayComponent",
                            "resource": "RscCustomInfoSlingLoad"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\UAVDisplay,
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\VehicleDriverDisplay,
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateRightPilot\Components\SensorDisplay,
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
            # Class: CfgVehicles\RHS_MELB_base\Turrets\CopilotTurret\Hitpoints,
            "Hitpoints": {
            },
            "isCopilot": 1,
            "canEject": 0,
            "gunnerName": "Copilot",
            "gunnerNotSpawned": 1,
            "maxHorizontalRotSpeed": 3,
            "maxVerticalRotSpeed": 3,
            "commanding": -1,
            "gunnerLeftHandAnimName": "lever_copilot",
            "gunnerRightHandAnimName": "stick_copilot",
            "gunnerLeftLegAnimName": "pedalL",
            "gunnerRightLegAnimName": "pedalR",
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\TurretSpec,
            "TurretSpec": {
                "showHeadPhones": 1
            },
            "startEngine": 0,
            "selectionFireAnim": "zasleh",
            "castGunnerShadow": 1,
            "viewGunnerShadow": 1,
            "gunnerForceOptics": 0,
            "enableManualFire": 0,
            "animationSourceHatch": "hatchGunner",
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
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "primary": 1,
            "hasGunner": 1,
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOpticsShowCursor": 0,
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
            "showHMD": 0,
            "viewGunnerInExternal": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "LODTurnedIn": -1,
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
            "gunnerDoor": "",
            "turretFollowFreeLook": 0,
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
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_03,
        "CargoTurret_03": {
            "gunnerAction": "passenger_bench_1",
            "gunnerCompartments": "Compartment2",
            "memoryPointsGetInGunner": "pos L1",
            "memoryPointsGetInGunnerDir": "pos L1 dir",
            "gunnerName": "Passenger (Left Bench 1)",
            "proxyIndex": 3,
            "maxElev": 45,
            "minElev": -60,
            "maxTurn": 95,
            "minTurn": -15,
            "isPersonTurret": 1,
            "ejectDeadGunner": 0,
            "playerPosition": 4,
            "soundAttenuationTurret": "",
            "disableSoundAttenuation": 1,
            "gunnerGetInAction": "GetInHeli_Light_01bench",
            # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_03\Hitpoints,
            "Hitpoints": {
            },
            # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner,
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
            "gunnerGetOutAction": "GetOutLow",
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_04,
        "CargoTurret_04": {
            "gunnerCompartments": "compartment3",
            "memoryPointsGetInGunner": "pos R1",
            "memoryPointsGetInGunnerDir": "pos R1 dir",
            "gunnerName": "Passenger (Right Bench 1)",
            "proxyIndex": 4,
            "maxTurn": 15,
            "minTurn": -95,
            "gunnerAction": "passenger_bench_1",
            "maxElev": 45,
            "minElev": -60,
            "isPersonTurret": 1,
            "ejectDeadGunner": 0,
            "playerPosition": 4,
            "soundAttenuationTurret": "",
            "disableSoundAttenuation": 1,
            "gunnerGetInAction": "GetInHeli_Light_01bench",
            # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_03\Hitpoints,
            "Hitpoints": {
            },
            # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner,
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
            "gunnerGetOutAction": "GetOutLow",
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_05,
        "CargoTurret_05": {
            "gunnerCompartments": "Compartment2",
            "memoryPointsGetInGunner": "pos L2",
            "memoryPointsGetInGunnerDir": "pos L2 dir",
            "gunnerName": "Passenger (Left Bench 2)",
            "proxyIndex": 5,
            "maxElev": 45,
            "minElev": -45,
            "maxTurn": 95,
            "minTurn": -95,
            # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_05\dynamicViewLimits,
            "dynamicViewLimits": {
                "CargoTurret_03": [-30,95],
                "CargoTurret_07": [-95,50]
            },
            "gunnerAction": "passenger_bench_1",
            "isPersonTurret": 1,
            "ejectDeadGunner": 0,
            "playerPosition": 4,
            "soundAttenuationTurret": "",
            "disableSoundAttenuation": 1,
            "gunnerGetInAction": "GetInHeli_Light_01bench",
            # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_03\Hitpoints,
            "Hitpoints": {
            },
            # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner,
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
            "gunnerGetOutAction": "GetOutLow",
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_06,
        "CargoTurret_06": {
            "gunnerCompartments": "compartment3",
            "memoryPointsGetInGunner": "pos R2",
            "memoryPointsGetInGunnerDir": "pos R2 dir",
            "gunnerName": "Passenger (Right Bench 2)",
            "proxyIndex": 6,
            # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_06\dynamicViewLimits,
            "dynamicViewLimits": {
                "CargoTurret_04": [-95,30],
                "CargoTurret_08": [-50,95]
            },
            "maxElev": 45,
            "minElev": -45,
            "maxTurn": 95,
            "minTurn": -95,
            "gunnerAction": "passenger_bench_1",
            "isPersonTurret": 1,
            "ejectDeadGunner": 0,
            "playerPosition": 4,
            "soundAttenuationTurret": "",
            "disableSoundAttenuation": 1,
            "gunnerGetInAction": "GetInHeli_Light_01bench",
            # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_03\Hitpoints,
            "Hitpoints": {
            },
            # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner,
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
            "gunnerGetOutAction": "GetOutLow",
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_07,
        "CargoTurret_07": {
            "gunnerCompartments": "Compartment2",
            "memoryPointsGetInGunner": "pos L3",
            "memoryPointsGetInGunnerDir": "pos L3 dir",
            "gunnerName": "Passenger (Left Bench 3)",
            "proxyIndex": 7,
            # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_07\dynamicViewLimits,
            "dynamicViewLimits": {
                "CargoTurret_05": [-50,95]
            },
            "maxElev": 45,
            "minElev": -45,
            "maxTurn": 95,
            "minTurn": -95,
            "gunnerAction": "passenger_bench_1",
            "isPersonTurret": 1,
            "ejectDeadGunner": 0,
            "playerPosition": 4,
            "soundAttenuationTurret": "",
            "disableSoundAttenuation": 1,
            "gunnerGetInAction": "GetInHeli_Light_01bench",
            # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_03\Hitpoints,
            "Hitpoints": {
            },
            # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner,
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
            "gunnerGetOutAction": "GetOutLow",
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_08,
        "CargoTurret_08": {
            "gunnerCompartments": "compartment3",
            "memoryPointsGetInGunner": "pos R3",
            "memoryPointsGetInGunnerDir": "pos R3 dir",
            "gunnerName": "Passenger (Right Bench 3)",
            "proxyIndex": 8,
            # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_08\dynamicViewLimits,
            "dynamicViewLimits": {
                "CargoTurret_06": [-95,50]
            },
            "maxElev": 45,
            "minElev": -45,
            "maxTurn": 95,
            "minTurn": -95,
            "gunnerAction": "passenger_bench_1",
            "isPersonTurret": 1,
            "ejectDeadGunner": 0,
            "playerPosition": 4,
            "soundAttenuationTurret": "",
            "disableSoundAttenuation": 1,
            "gunnerGetInAction": "GetInHeli_Light_01bench",
            # Class: CfgVehicles\RHS_MELB_MH6M\Turrets\CargoTurret_03\Hitpoints,
            "Hitpoints": {
            },
            # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner,
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
            "gunnerGetOutAction": "GetOutLow",
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\Helicopter_Base_H\Turrets\MainTurret,
        "MainTurret": {
            "gunnerOpticsModel": "",
            "turretCanSee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\TurretSpec,
            "TurretSpec": {
                "showHeadPhones": 1
            },
            "startEngine": 0,
            "outGunnerMayFire": 1,
            "commanding": -1,
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "memoryPointGun": "machinegun",
            "memoryPointGunnerOptics": "gunnerview",
            "selectionFireAnim": "zasleh",
            "castGunnerShadow": 1,
            "viewGunnerShadow": 1,
            "gunnerForceOptics": 0,
            "enableManualFire": 0,
            "canEject": 0,
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\HitPoints,
            "HitPoints": {
                # Class: CfgVehicles\Helicopter\Turrets\MainTurret\HitPoints\HitTurret
                "HitTurret": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "vez",
                    "visual": "vez",
                    "passThrough": 0.3
                },
                # Class: CfgVehicles\Helicopter\Turrets\MainTurret\HitPoints\HitGun,
                "HitGun": {
                    "armor": 0.2,
                    "material": 51,
                    "name": "zbran",
                    "visual": "zbran",
                    "passThrough": 0.1
                }
            },
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
            "showHMD": 0,
            "viewGunnerInExternal": 0,
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
            "isCopilot": 0,
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
            "showCrewAim": 0
        }
    },
    # Class: CfgVehicles\RHS_MELB_MH6M\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\RHS_MELB_MH6M\AnimationSources\AddBenches
        "AddBenches": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\Addgunrack,
        "Addgunrack": {
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\Addcrosshair,
        "Addcrosshair": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\Addfueltank,
        "Addfueltank": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\AddBobhead,
        "AddBobhead": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0,
            "displayName": "Bobblehead"
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\hide_NoFear,
        "hide_NoFear": {
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0,
            "displayName": "No Fear Decal"
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\hide_SGDM,
        "hide_SGDM": {
            "displayName": "Six Guns Decal",
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\hide_SN_nose,
        "hide_SN_nose": {
            "displayName": "Tail Number on nose",
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\hide_clan,
        "hide_clan": {
            "displayName": "Squad XML",
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\HitGlass1,
        "HitGlass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\HitGlass2,
        "HitGlass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\HitGlass3,
        "HitGlass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\HitGlass4,
        "HitGlass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\HitGlass5,
        "HitGlass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\HitGlass6,
        "HitGlass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\MFD_Pilot,
        "MFD_Pilot": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\MFD_CoPilot,
        "MFD_CoPilot": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\pilotpip,
        "pilotpip": {
            "source": "user",
            "animperiod": 0.001,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\copilotpip,
        "copilotpip": {
            "source": "user",
            "animperiod": 0.001,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\hit_pylon_1_source,
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\hit_pylon_2_source,
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\hit_pylon_3_source,
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles\RHS_MELB_base\AnimationSources\hit_pylon_4_source,
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\AddCargoHook,
        "AddCargoHook": {
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 0,
            "isComponent": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\AddCargoHook_COver,
        "AddCargoHook_COver": {
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 1,
            "isComponent": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitHRotor,
        "HitHRotor": {
            "source": "hit",
            "hitpoint": "HitHRotor",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitVRotor,
        "HitVRotor": {
            "source": "hit",
            "hitpoint": "HitVRotor",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitEngine,
        "HitEngine": {
            "source": "hit",
            "hitpoint": "HitEngine",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitEngine2,
        "HitEngine2": {
            "source": "hit",
            "hitpoint": "HitEngine2",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitBatteries,
        "HitBatteries": {
            "source": "hit",
            "hitpoint": "HitBatteries",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitTransmission,
        "HitTransmission": {
            "source": "hit",
            "hitpoint": "HitTransmission",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitHydraulics,
        "HitHydraulics": {
            "source": "hit",
            "hitpoint": "HitHydraulics",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\AnimationSources\HitFuel,
        "HitFuel": {
            "source": "hit",
            "hitpoint": "HitFuel",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter\AnimationSources\HitEngine1,
        "HitEngine1": {
            "source": "hit",
            "hitpoint": "HitEngine1",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter\AnimationSources\HitWinch_Source,
        "HitWinch_Source": {
            "source": "hit",
            "hitpoint": "HitWinch",
            "raw": 1
        },
        # Class: CfgVehicles\Air\AnimationSources\CollisionLightRed_source,
        "CollisionLightRed_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionRed"
        },
        # Class: CfgVehicles\Air\AnimationSources\CollisionLightWhite_source,
        "CollisionLightWhite_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionWhite"
        }
    },
    # Class: CfgVehicles\RHS_MELB_MH6M\Attributes,
    "Attributes": {
        # Class: CfgVehicles\RHS_MELB_MH6M\Attributes\rhs_MELB_TailNumber
        "rhs_MELB_TailNumber": {
            "displayName": "Define Tail Number",
            "tooltip": "Select tail number specific to this helicopter.",
            "property": "rhs_MELB_TailNumber",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ [_this,'d_SN',_value] call RHS_MELB_fnc_tailNumber}",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values,
            "values": {
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\NoChange
                "NoChange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\blank_ca,
                "blank_ca": {
                    "name": "Empty",
                    "value": "blank_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25385_ca,
                "MELB_SN_25385_ca": {
                    "name": "25385",
                    "value": "MELB_SN_25385_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25381_ca,
                "MELB_SN_25381_ca": {
                    "name": "25381",
                    "value": "MELB_SN_25381_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25378_ca,
                "MELB_SN_25378_ca": {
                    "name": "25378",
                    "value": "MELB_SN_25378_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25376_ca,
                "MELB_SN_25376_ca": {
                    "name": "25376",
                    "value": "MELB_SN_25376_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25374_ca,
                "MELB_SN_25374_ca": {
                    "name": "25374",
                    "value": "MELB_SN_25374_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25372_ca,
                "MELB_SN_25372_ca": {
                    "name": "25372",
                    "value": "MELB_SN_25372_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25366_ca,
                "MELB_SN_25366_ca": {
                    "name": "25366",
                    "value": "MELB_SN_25366_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25363_ca,
                "MELB_SN_25363_ca": {
                    "name": "25363",
                    "value": "MELB_SN_25363_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25361_ca,
                "MELB_SN_25361_ca": {
                    "name": "25361",
                    "value": "MELB_SN_25361_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25358_ca,
                "MELB_SN_25358_ca": {
                    "name": "25358",
                    "value": "MELB_SN_25358_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25355_ca,
                "MELB_SN_25355_ca": {
                    "name": "25355",
                    "value": "MELB_SN_25355_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25350_ca,
                "MELB_SN_25350_ca": {
                    "name": "25350",
                    "value": "MELB_SN_25350_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25349_ca,
                "MELB_SN_25349_ca": {
                    "name": "25349",
                    "value": "MELB_SN_25349_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25348_ca,
                "MELB_SN_25348_ca": {
                    "name": "25348",
                    "value": "MELB_SN_25348_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_25346_ca,
                "MELB_SN_25346_ca": {
                    "name": "25346",
                    "value": "MELB_SN_25346_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_24683_ca,
                "MELB_SN_24683_ca": {
                    "name": "24683",
                    "value": "MELB_SN_24683_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_23654_ca,
                "MELB_SN_23654_ca": {
                    "name": "23654",
                    "value": "MELB_SN_23654_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_23653_ca,
                "MELB_SN_23653_ca": {
                    "name": "23653",
                    "value": "MELB_SN_23653_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_23652_ca,
                "MELB_SN_23652_ca": {
                    "name": "23652",
                    "value": "MELB_SN_23652_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_23649_ca,
                "MELB_SN_23649_ca": {
                    "name": "23649",
                    "value": "MELB_SN_23649_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_23636_ca,
                "MELB_SN_23636_ca": {
                    "name": "23636",
                    "value": "MELB_SN_23636_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_23635_ca,
                "MELB_SN_23635_ca": {
                    "name": "23635",
                    "value": "MELB_SN_23635_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_23632_ca,
                "MELB_SN_23632_ca": {
                    "name": "23632",
                    "value": "MELB_SN_23632_ca"
                },
                # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_TailNumber\values\MELB_SN_23631_ca,
                "MELB_SN_23631_ca": {
                    "name": "23631",
                    "value": "MELB_SN_23631_ca"
                }
            }
        },
        # Class: CfgVehicles\RHS_MELB_MH6M\Attributes\rhs_MELB_NoFear,
        "rhs_MELB_NoFear": {
            "displayName": "No Fear",
            "property": "MELB_NoFear",
            "control": "CheckboxNumber",
            "expression": "_this animate ['hide_NoFear',_value,true]",
            "defaultValue": 0
        },
        # Class: CfgVehicles\RHS_MELB_MH6M\Attributes\rhs_MELB_SN_Nose,
        "rhs_MELB_SN_Nose": {
            "displayName": "Tail Number",
            "property": "MELB_SN_Nose",
            "expression": "_this animate ['hide_SN_nose',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": 0
        },
        # Class: CfgVehicles\RHS_MELB_MH6M\Attributes\rhs_MELB_clan,
        "rhs_MELB_clan": {
            "displayName": "Squad XML",
            "property": "MELB_clan",
            "expression": "_this animate ['hide_clan',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": 0
        },
        # Class: CfgVehicles\RHS_MELB_MH6M\Attributes\MELB_ToggleBoy,
        "MELB_ToggleBoy": {
            "displayName": "Bobblehead",
            "property": "MELB_ToggleBoy",
            "expression": "_this animate ['AddBobhead',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\Attributes\rhs_MELB_SGDM,
        "rhs_MELB_SGDM": {
            "displayName": "Six Guns",
            "property": "MELB_SGDM",
            "expression": "_this animate ['hide_SGDM',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": 0
        }
    },
    "side": 1,
    "faction": "rhs_faction_socom",
    "crew": "rhsusf_army_ucp_helipilot",
    "model": "rhsusf|addons|rhsusf_melb|MELB.p3d",
    "mapSize": 11,
    "destrType": "DestructWreck",
    "accuracy": 0.5,
    "unitInfoType": "RscUnitInfoAir_NoRadar_MELB",
    "unitInfoTypeRTD": "RHSUSF_RscUnitInfoAirRTDFullDigital_MELB",
    "nameSound": "veh_helicopter",
    "driverAction": "MELB_Pilot",
    "driverInAction": "MELB_Pilot",
    "getInAction": "ChopperLight_L_In_H",
    "getOutAction": "GetOutLow",
    "memoryPointsGetInDriver": "pos pilot",
    "memoryPointsGetInDriverDir": "pos pilot dir",
    "memoryPointsGetInDriverPrecise": "pos pilot",
    "memoryPointsGetInCargo": ["pos cargo"],
    "memoryPointsGetInCargoDir": ["pos cargo dir"],
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "usePreciseGetInAction": 1,
    "getInRadius": 1.5,
    "cargoCompartments": ["compartment3"],
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "cargoAction": ["passenger_flatground_generic04"],
    "preciseGetInOut": 0,
    "castCargoShadow": 1,
    "getInProxyOrder": [9,1,2,3,4,5,6,7,8,10],
    "extCameraPosition": [0,0.75,-10],
    "driverCanSee": 31,
    "hideWeaponsDriver": 1,
    "hideWeaponsGunner": 1,
    "hideWeaponsCargo": 1,
    "radarType": 0,
    "irTarget": 1,
    "irTargetSize": 0.7,
    "visualTarget": 1,
    "visualTargetSize": 0.8,
    "radarTarget": 1,
    "radarTargetSize": 0.8,
    "receiveRemoteTargets": 1,
    "reportRemoteTargets": 1,
    "reportOwnPosition": 1,
    "LockDetectionSystem": "4 + 8",
    "incomingMissileDetectionSystem": 16,
    "weapons": ["rhsusf_weap_LWIRCM"],
    "magazines": ["rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM","rhsusf_mag_LWIRCM"],
    "hiddenSelections": ["camo1","d_SN"],
    "hiddenSelectionsTextures": ["rhsusf|addons|rhsusf_melb|data|melb_ext_co.paa","rhsusf|addons|rhsusf_melb|data|decals|SN|blank_ca.paa"],
    # Class: CfgVehicles\RHS_MELB_base\MFD,
    "MFD": {
    },
    # Class: CfgVehicles\RHS_MELB_base\ViewOptics,
    "ViewOptics": {
        "initAngleX": 0,
        "minAngleX": -30,
        "maxAngleX": 30,
        "initAngleY": 0,
        "minAngleY": -86,
        "maxAngleY": 86,
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
    "memorypointcm": ["flare_launcher1"],
    "memorypointcmdir": ["flare_launcher1_dir"],
    "driveOnComponent": ["Skids"],
    "maxFordingDepth": 0.65,
    "mainBladeRadius": 4.32,
    "tailBladeRadius": 0.77,
    # Class: CfgVehicles\RHS_MELB_base\RotorLibHelicopterProperties,
    "RotorLibHelicopterProperties": {
        "RTDconfig": "rhsusf|addons|rhsusf_c_melb|RTD_MELB.xml",
        "autoHoverCorrection": [0.28,2.88,0],
        "defaultCollective": 0.5,
        "throttleOffToIdle": 8,
        "throttleIdleToOff": 6,
        "throttleIdleToFull": 12,
        "throttleFullToIdle": 6,
        "maxTorque": 1200,
        "stressDamagePerSec": 0.00333333,
        "maxHorizontalStabilizerLeftStress": 10000,
        "maxHorizontalStabilizerRightStress": 10000,
        "maxVerticalStabilizerStress": 10000,
        "horizontalWingsAngleCollMin": 0,
        "horizontalWingsAngleCollMax": 0,
        "maxMainRotorStress": 45000,
        "maxTailRotorStress": 20200,
        "retreatBladeStallWarningSpeed": 77.222,
        "rtd_center": "rtd_center",
        "hasAPU": 0,
        "vrsShakepowerCoef": 1
    },
    "startDuration": 10,
    "washDownStrength": "0.7f",
    "maxSpeed": 200,
    "slingLoadMemoryPoint": "slingLoad0",
    "slingLoadMaxCargoMass": 900,
    "liftForceCoef": 1,
    "cyclicAsideForceCoef": 1.65,
    "cyclicForwardForceCoef": 0.4,
    "backrotorforcecoef": 0.9,
    "bodyFrictionCoef": 0.3,
    "sensitivity": 2.5,
    "maximumLoad": 1000,
    "memoryPointSupply": "memsupply",
    "supplyradius": 4,
    "occludeSoundsWhenIn": 0.762341,
    "obstructSoundsWhenIn": 0.616228,
    "attenuationEffectType": "OpenHeliAttenuation",
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
    "soundGetIn": ["A3|Sounds_F|vehicles|air|noises|heli_get_in2",0.562341,1],
    "soundGetOut": ["A3|Sounds_F|vehicles|air|noises|heli_get_out2",0.794328,1,20],
    "soundDammage": ["A3|Sounds_F|vehicles|crashes|helis|Heli_crash_default_ext_1",3.16228,1],
    "soundEngineOnInt": ["rhsusf|addons|rhsusf_melb|Sound|Int_Start",0.4,1],
    "soundEngineOnExt": ["rhsusf|addons|rhsusf_melb|Sound|Ext_Start",0.794328,1,600],
    "soundEngineOffInt": ["rhsusf|addons|rhsusf_melb|Sound|Int_Off",0.4,1],
    "soundEngineOffExt": ["rhsusf|addons|rhsusf_melb|Sound|Ext_Off",0.794328,1,600],
    "soundLocked": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_1",1,1],
    "soundIncommingMissile": ["|A3|Sounds_F|weapons|Rockets|opfor_lock_2",0.7,1],
    "rotorDamageInt": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_int_open_1",1,1],
    "rotorDamageOut": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_ext_1",2.51189,1,150],
    "rotorDamage": ["rotorDamageInt","rotorDamageOut"],
    "tailDamageInt": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1],
    "tailDamageOut": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1,300],
    "tailDamage": ["tailDamageInt","tailDamageOut"],
    "landingSoundInt0": ["A3|Sounds_F|vehicles|air|noises|landing_skids_int1_open",1,1,100],
    "landingSoundInt1": ["A3|Sounds_F|vehicles|air|noises|landing_skids_int1_open",1,1,100],
    "landingSoundInt": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingSoundOut0": ["A3|Sounds_F|vehicles|air|noises|landing_skids_ext1",1.77828,1,100],
    "landingSoundOut1": ["A3|Sounds_F|vehicles|air|noises|landing_skids_ext1",1.77828,1,100],
    "landingSoundOut": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    "slingCargoAttach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEndINT",1,1],
    "slingCargoAttach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookLock",1,1,80],
    "slingCargoAttach": ["slingCargoAttach0","slingCargoAttach1"],
    "slingCargoDetach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEndINT",1,1],
    "slingCargoDetach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookUnlock",1,1,80],
    "slingCargoDetach": ["slingCargoDetach0","slingCargoDetach1"],
    "slingCargoDetachAir0": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_int",1,1],
    "slingCargoDetachAir1": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_ext",1,1,80],
    "slingCargoDetachAir": ["slingCargoDetach0","slingCargoDetach1"],
    "slingCargoRopeBreak0": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_int",1,1],
    "slingCargoRopeBreak1": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_ext",1,1,80],
    "slingCargoRopeBreak": ["slingCargoDetach0","slingCargoDetach1"],
    # Class: CfgVehicles\RHS_MELB_base\Sounds,
    "Sounds": {
        # Class: CfgVehicles\RHS_MELB_base\Sounds\EngineExt
        "EngineExt": {
            "sound": ["rhsusf|addons|rhsusf_melb|Sound|Ext_Idle",1.28893,1,400],
            "frequency": "rotorSpeed*(1+rotorThrust/6)*0.9",
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\RotorExt,
        "RotorExt": {
            "sound": ["rhsusf|addons|rhsusf_melb|Sound|Ext_Low",1.25893,1,500],
            "frequency": "1.3*(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/6)",
            "volume": "camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\RotorSwist,
        "RotorSwist": {
            "sound": ["rhsusf|addons|rhsusf_melb|Sound|Close",1.2,1,600],
            "frequency": "rotorSpeed*(1+rotorThrust/6)*0.9",
            "volume": "camPos * (gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]) * (rotorThrust factor [0.7, 0.9])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\EngineInt,
        "EngineInt": {
            "sound": ["rhsusf|addons|rhsusf_melb|Sound|Int_Idle",1,1],
            "frequency": "rotorSpeed*(1+rotorThrust/6)*0.9",
            "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\RotorInt,
        "RotorInt": {
            "sound": ["rhsusf|addons|rhsusf_melb|Sound|Int_Low",0.501187,1],
            "frequency": "1*(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/6)",
            "volume": "(1-camPos)*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)*0.9"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\RotorBench,
        "RotorBench": {
            "sound": ["rhsusf|addons|rhsusf_melb|Sound|Ext_Low",1.25893,1,500],
            "frequency": "1.3*(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/6)",
            "volume": "(playerPos factor [3.9, 4]) * (1 - camPos) * (rotorSpeed factor [0.3, 1]) * (1 + rotorThrust) * 0.4",
            "cone": [1.6,3.14,1.6,0.95]
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\EngineBench,
        "EngineBench": {
            "sound": ["rhsusf|addons|rhsusf_melb|Sound|Ext_Idle",1.28184,1],
            "frequency": "rotorSpeed*(1+rotorThrust/6)*0.9",
            "volume": "(playerPos factor [3.9, 4]) * (1 - camPos) * (0 max (rotorSpeed-0.4))"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\WindBench,
        "WindBench": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wind_open_out",0.562341,1,50],
            "frequency": 1,
            "volume": "4 * (playerPos factor [3.9, 4]) * (1 - camPos) * ((speed factor[0, 30]) + (speed factor[0, -30]))"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\TransmissionDamageExt_phase1,
        "TransmissionDamageExt_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\TransmissionDamageExt_phase2,
        "TransmissionDamageExt_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\TransmissionDamageInt_phase1,
        "TransmissionDamageInt_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\TransmissionDamageInt_phase2,
        "TransmissionDamageInt_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\RotorNoiseExt,
        "RotorNoiseExt": {
            "sound": ["rhsusf|addons|rhsusf_melb|Sound|Rotor_Fast",1.28184,1,200],
            "frequency": 1.5,
            "volume": "(camPos*(rotorSpeed factor [0.6, 0.85]))",
            "cone": [1.6,3.14,2,0.95]
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\FarDistance,
        "FarDistance": {
            "sound": ["rhsusf|addons|rhsusf_melb|Sound|Distance",2.09184,1.1,1100],
            "frequency": "rotorSpeed",
            "volume": "2 * camPos * (0 max (rotorSpeed-0.4))"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\FarDistanceRotor,
        "FarDistanceRotor": {
            "sound": ["rhsusf|addons|rhsusf_melb|Sound|tail_rotor",2.09184,1,1000],
            "frequency": "rotorSpeed",
            "volume": "2 * camPos * (0 max (rotorSpeed-0.4))"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\damageAlarmInt,
        "damageAlarmInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_bluefor",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\damageAlarmExt,
        "damageAlarmExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_bluefor",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\rotorLowAlarmInt,
        "rotorLowAlarmInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\rotorLowAlarmExt,
        "rotorLowAlarmExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\scrubLandInt,
        "scrubLandInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandInt_open",1,1,100],
            "frequency": 1,
            "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\scrubLandExt,
        "scrubLandExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubLand factor[0.02, 0.05])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\scrubBuildingInt,
        "scrubBuildingInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingInt",1,1,100],
            "frequency": 1,
            "volume": "2 * (1 - camPos) * (scrubBuilding factor[0.02, 0.05])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\scrubBuildingExt,
        "scrubBuildingExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\scrubTreeInt,
        "scrubTreeInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
            "frequency": 1,
            "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\scrubTreeExt,
        "scrubTreeExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\RainExt,
        "RainExt": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
            "frequency": 1,
            "volume": "camPos * (rain - rotorSpeed/2) * 2"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\RainInt,
        "RainInt": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int_open",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\SlingLoadDownExt,
        "SlingLoadDownExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\SlingLoadUpExt,
        "SlingLoadUpExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\SlingLoadDownInt,
        "SlingLoadDownInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\SlingLoadUpInt,
        "SlingLoadUpInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\WindInt,
        "WindInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wind_open_int",1,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\WindLateralMovementInt,
        "WindLateralMovementInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wind_lateral_open_int",1,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*lateralMovement*((speed factor [5,40]) + (speed factor [-5,-40]))"
        },
        # Class: CfgVehicles\RHS_MELB_base\Sounds\GStress,
        "GStress": {
            "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2b",0.116228,1,50],
            "frequency": 1,
            "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
        }
    },
    # Class: CfgVehicles\RHS_MELB_base\SoundsExt,
    "SoundsExt": {
        # Class: CfgVehicles\RHS_MELB_base\SoundsExt\SoundEvents
        "SoundEvents": {
        },
        # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds,
        "Sounds": {
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\EngineExt
            "EngineExt": {
                "sound": ["rhsusf|addons|rhsusf_melb|Sound|Ext_Idle",1.28893,1,400],
                "frequency": "1.3*rotorSpeed",
                "volume": "2 * camPos * (0 max (rotorSpeed-0.4))"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\RotorExt,
            "RotorExt": {
                "sound": ["rhsusf|addons|rhsusf_melb|Sound|Ext_Low",1.25893,1,500],
                "frequency": "1.3*(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/6)",
                "volume": "camPos * (rotorSpeed factor [0.3, 1]) * (1 + rotorThrust)"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\RotorSwist,
            "RotorSwist": {
                "sound": ["rhsusf|addons|rhsusf_melb|Sound|Close",1.2,1,600],
                "frequency": "1.3*rotorspeed",
                "volume": "camPos * (gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]) * (rotorThrust factor [0.7, 0.9])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\EngineInt,
            "EngineInt": {
                "sound": ["rhsusf|addons|rhsusf_melb|Sound|Int_Idle",1,1],
                "frequency": "rotorSpeed",
                "volume": "(1-camPos)*2*(0 max (rotorSpeed-0.4))"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\RotorInt,
            "RotorInt": {
                "sound": ["rhsusf|addons|rhsusf_melb|Sound|Int_Low",1.28184,1],
                "frequency": "(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/6)",
                "volume": "(1 - camPos) * (rotorSpeed factor [0.3, 0.7]) * (1 + rotorThrust) * 0.7"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\RotorBench,
            "RotorBench": {
                "sound": ["rhsusf|addons|rhsusf_melb|Sound|Ext_Low",1.25893,1,500],
                "frequency": "1.3*(rotorSpeed factor [0.3, 0.7]) * (rotorSpeed factor [0.3, 1]) * (1 - rotorThrust/6)",
                "volume": "(playerPos factor [3.9, 4]) * (1 - camPos) * (rotorSpeed factor [0.3, 1]) * (1 + rotorThrust) * 0.4",
                "cone": [1.6,3.14,1.6,0.95]
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\EngineBench,
            "EngineBench": {
                "sound": ["rhsusf|addons|rhsusf_melb|Sound|Ext_Idle",1.28184,1],
                "frequency": "1.3*rotorSpeed",
                "volume": "(playerPos factor [3.9, 4]) * (1 - camPos) * (0 max (rotorSpeed-0.4))"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\WindBench,
            "WindBench": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wind_open_out",0.562341,1,50],
                "frequency": 1,
                "volume": "4 * (playerPos factor [3.9, 4]) * (1 - camPos) * ((speed factor[0, 30]) + (speed factor[0, -30]))"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\TransmissionDamageExt_phase1,
            "TransmissionDamageExt_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\TransmissionDamageExt_phase2,
            "TransmissionDamageExt_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\TransmissionDamageInt_phase1,
            "TransmissionDamageInt_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\TransmissionDamageInt_phase2,
            "TransmissionDamageInt_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\RotorNoiseExt,
            "RotorNoiseExt": {
                "sound": ["rhsusf|addons|rhsusf_melb|Sound|Rotor_Fast",1.28184,1,200],
                "frequency": 1,
                "volume": "(camPos*(rotorSpeed factor [0.6, 0.85]))",
                "cone": [1.6,3.14,2,0.95]
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\FarDistance,
            "FarDistance": {
                "sound": ["rhsusf|addons|rhsusf_melb|Sound|Distance",2.09184,1.1,1100],
                "frequency": "rotorSpeed",
                "volume": "2 * camPos * (0 max (rotorSpeed-0.4))"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\FarDistanceRotor,
            "FarDistanceRotor": {
                "sound": ["rhsusf|addons|rhsusf_melb|Sound|tail_rotor",2.09184,1,1000],
                "frequency": "rotorSpeed",
                "volume": "2 * camPos * (0 max (rotorSpeed-0.4))"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\damageAlarmInt,
            "damageAlarmInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_bluefor",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\damageAlarmExt,
            "damageAlarmExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_bluefor",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\rotorLowAlarmInt,
            "rotorLowAlarmInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\rotorLowAlarmExt,
            "rotorLowAlarmExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\scrubLandInt,
            "scrubLandInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandInt_open",1,1,100],
                "frequency": 1,
                "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\scrubLandExt,
            "scrubLandExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubLand factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\scrubBuildingInt,
            "scrubBuildingInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingInt",1,1,100],
                "frequency": 1,
                "volume": "2 * (1 - camPos) * (scrubBuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\scrubBuildingExt,
            "scrubBuildingExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\scrubTreeInt,
            "scrubTreeInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
                "frequency": 1,
                "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\scrubTreeExt,
            "scrubTreeExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\RainExt,
            "RainExt": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
                "frequency": 1,
                "volume": "camPos * (rain - rotorSpeed/2) * 2"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\RainInt,
            "RainInt": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_int_open",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\SlingLoadDownExt,
            "SlingLoadDownExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\SlingLoadUpExt,
            "SlingLoadUpExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\SlingLoadDownInt,
            "SlingLoadDownInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\SlingLoadUpInt,
            "SlingLoadUpInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\WindInt,
            "WindInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wind_open_int",1.12202,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\WindLateralMovementInt,
            "WindLateralMovementInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wind_lateral_open_int",1.99526,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*lateralMovement*((speed factor [5,40]) + (speed factor [-5,-40]))"
            },
            # Class: CfgVehicles\RHS_MELB_base\SoundsExt\Sounds\GStress,
            "GStress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2b",0.116228,1,50],
                "frequency": 1,
                "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
            }
        }
    },
    # Class: CfgVehicles\RHS_MELB_base\pilotCamera,
    "pilotCamera": {
    },
    # Class: CfgVehicles\RHS_MELB_base\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\RHS_MELB_base\Exhausts\Exhaust01
        "Exhaust01": {
            "position": "exhaust1",
            "direction": "exhaust1_dir",
            "effect": "ExhaustEffectHeli"
        }
    },
    # Class: CfgVehicles\RHS_MELB_base\Library,
    "Library": {
        "libTextDesc": "Syko's Little Birds"
    },
    "armor": 35,
    "armorStructural": 5,
    "epeImpulseDamageCoef": 20,
    "damageResistance": 0.01039,
    "crewCrashProtection": 0.2,
    # Class: CfgVehicles\RHS_MELB_base\HitPoints,
    "HitPoints": {
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitFuel
        "HitFuel": {
            "armor": 2,
            "name": "fuel_hit",
            "visual": "-",
            "radius": 0.125,
            "minimalhit": 0.2,
            "explosionShielding": 0.5,
            "passThrough": 0,
            "convexComponent": "fuel_hit",
            "material": 51
        },
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitHull,
        "HitHull": {
            "name": "hull_hit",
            "armor": 6,
            "visual": "zbytek",
            "radius": 0.05,
            "convexComponent": "hull_hit",
            "explosionShielding": 1,
            "material": 51,
            "passThrough": 1
        },
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitEngine,
        "HitEngine": {
            "name": "engine_hit",
            "armor": 1.5,
            "visual": "-",
            "radius": 0.15,
            "explosionShielding": 0.85,
            "minimalhit": 0.05,
            "passThrough": 0.3,
            "convexComponent": "engine_hit",
            "material": 51
        },
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitAvionics,
        "HitAvionics": {
            "name": "avionics_hit",
            "armor": 2,
            "visual": "-",
            "radius": 0.05,
            "explosionShielding": 0.5,
            "convexComponent": "avionics_hit",
            "material": 51,
            "passThrough": 1
        },
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitVRotor,
        "HitVRotor": {
            "visual": "tail rotor static",
            "armor": 1,
            "radius": 0.05,
            "explosionShielding": 0.8,
            "name": "tail_rotor_hit",
            "convexComponent": "tail_rotor_hit",
            "material": 51,
            "passThrough": 0.3
        },
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitHRotor,
        "HitHRotor": {
            "visual": "main rotor static",
            "armor": 3,
            "radius": 0.2,
            "explosionShielding": 0.5,
            "name": "main_rotor_hit",
            "convexComponent": "main_rotor_hit",
            "material": 51,
            "passThrough": 0.1
        },
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitGlass1,
        "HitGlass1": {
            "armor": 2,
            "radius": 0.15,
            "explosionShielding": 2,
            "material": -1,
            "name": "glass1",
            "convexComponent": "glass1",
            "visual": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitGlass2,
        "HitGlass2": {
            "armor": 2,
            "radius": 0.15,
            "explosionShielding": 2,
            "name": "glass2",
            "convexComponent": "glass2",
            "visual": "glass2",
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitGlass3,
        "HitGlass3": {
            "armor": 2,
            "radius": 0.15,
            "explosionShielding": 2,
            "name": "glass3",
            "convexComponent": "glass3",
            "visual": "glass3",
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitGlass4,
        "HitGlass4": {
            "armor": 2,
            "radius": 0.15,
            "explosionShielding": 2,
            "name": "glass4",
            "convexComponent": "glass4",
            "visual": "glass4",
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon1,
        "HitPylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon1\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon2,
        "HitPylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon2\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon3,
        "HitPylon3": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_3",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon3\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon4,
        "HitPylon4": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_4",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon4\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_MELB_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\Helicopter_Base_F\HitPoints\HitEngine1,
        "HitEngine1": {
            "name": "engine_1_hit",
            "convexComponent": "engine_1_hit",
            "explosionShielding": 1,
            "armor": 0.25,
            "material": 51,
            "visual": "motor",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter_Base_F\HitPoints\HitEngine2,
        "HitEngine2": {
            "name": "engine_2_hit",
            "convexComponent": "engine_2_hit",
            "explosionShielding": 1,
            "armor": 0.25,
            "material": 51,
            "visual": "motor",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter_Base_F\HitPoints\HitMissiles,
        "HitMissiles": {
            "name": "ammo_hit",
            "convexComponent": "ammo_hit",
            "explosionShielding": 1,
            "armor": 0.1,
            "material": 51,
            "visual": "munice",
            "passThrough": 0.5
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitRGlass,
        "HitRGlass": {
            "convexComponent": "sklo predni P",
            "explosionShielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni P",
            "visual": "sklo predni P",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitLGlass,
        "HitLGlass": {
            "convexComponent": "sklo predni L",
            "explosionShielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni L",
            "visual": "sklo predni L",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitEngine3,
        "HitEngine3": {
            "name": "engine_3_hit",
            "convexComponent": "engine_3_hit",
            "explosionShielding": 1,
            "armor": 0.25,
            "material": 51,
            "visual": "motor",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitWinch,
        "HitWinch": {
            "armor": -40,
            "material": 51,
            "name": "slingLoad0",
            "visual": "",
            "passThrough": 0,
            "radius": 0.1,
            # Class: CfgVehicles\Helicopter\HitPoints\HitWinch\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Helicopter\HitPoints\HitWinch\DestructionEffects\Explo,
                "Explo": {
                    "simulation": "particles",
                    "type": "WinchDestructionExplo",
                    "position": "slingLoad0",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.06
                },
                # Class: CfgVehicles\Helicopter\HitPoints\HitWinch\DestructionEffects\Sparks,
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
        # Class: CfgVehicles\Helicopter\HitPoints\HitTransmission,
        "HitTransmission": {
            "armor": 0.8,
            "material": -1,
            "name": "transmission",
            "passThrough": 0.8
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitGlass5,
        "HitGlass5": {
            "name": "glass5",
            "convexComponent": "glass5",
            "visual": "glass5",
            "armor": 2,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitGlass6,
        "HitGlass6": {
            "name": "glass6",
            "convexComponent": "glass6",
            "visual": "glass6",
            "armor": 2,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitLight,
        "HitLight": {
            "armor": 0.1,
            "material": -1,
            "name": "light",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitHydraulics,
        "HitHydraulics": {
            "armor": 0.8,
            "material": -1,
            "name": "hydraulics",
            "passThrough": 0.8
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitGear,
        "HitGear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitHStabilizerL1,
        "HitHStabilizerL1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerL1",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitHStabilizerR1,
        "HitHStabilizerR1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerR1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitVStabilizer1,
        "HitVStabilizer1": {
            "armor": 0.8,
            "material": -1,
            "name": "VStabilizer1",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitTail,
        "HitTail": {
            "armor": 0.8,
            "material": -1,
            "name": "tail boom",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitPitotTube,
        "HitPitotTube": {
            "armor": 0.5,
            "material": -1,
            "name": "pitot tube",
            "passThrough": 0.2
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStaticPort,
        "HitStaticPort": {
            "armor": 0.1,
            "material": -1,
            "name": "static port",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStarter1,
        "HitStarter1": {
            "armor": 0.1,
            "material": -1,
            "name": "starter1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStarter2,
        "HitStarter2": {
            "armor": 0.1,
            "material": -1,
            "name": "starter2",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStarter3,
        "HitStarter3": {
            "armor": 0.1,
            "material": -1,
            "name": "starter3",
            "passThrough": 0
        }
    },
    # Class: CfgVehicles\RHS_MELB_base\Damage,
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_melb|data|melb_ext.rvmat","rhsusf|addons|rhsusf_melb|data|melb_ext_damage.rvmat","rhsusf|addons|rhsusf_melb|data|melb_ext_destruct.rvmat","rhsusf|addons|rhsusf_melb|data|melb_glass.rvmat","rhsusf|addons|rhsusf_melb|data|melb_glass_damage.rvmat","rhsusf|addons|rhsusf_melb|data|melb_glass_destruct.rvmat","rhsusf|addons|rhsusf_melb|data|melb_glass_in.rvmat","rhsusf|addons|rhsusf_melb|data|melb_glass_damage.rvmat","rhsusf|addons|rhsusf_melb|data|melb_glass_destruct.rvmat"]
    },
    # Class: CfgVehicles\RHS_MELB_base\UserActions,
    "UserActions": {
        # Class: CfgVehicles\RHS_MELB_base\UserActions\MFD_Toggle
        "MFD_Toggle": {
            "displayName": "Toggle Monitor",
            "onlyforplayer": 1,
            "position": "doplnovani",
            "radius": 2,
            "shortcut": "LandGearUp",
            "condition": "((call rhsusf_fnc_findPlayer)==driver this) or ((call rhsusf_fnc_findPlayer)==gunner this) ",
            "statement": "call RHS_MELB_fnc_MFD_toggle",
            "showWindow": 0
        },
        # Class: CfgVehicles\RHS_MELB_base\UserActions\SAFEMODE,
        "SAFEMODE": {
            "displayName": "<t color='#00FF7F'>MASTERSAFE</t>",
            "condition": "(call rhsusf_fnc_findPlayer) in this",
            "statement": "(call rhsusf_fnc_findPlayer) action ['SwitchWeapon', this, (call rhsusf_fnc_findPlayer), 0];",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showWindow": 0,
            "shortcut": "user13",
            "hideOnUse": 1
        }
    },
    # Class: CfgVehicles\RHS_MELB_base\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\RHS_MELB_base\Reflectors\Light
        "Light": {
            "color": [7000,7500,10000,1],
            "ambient": [95,95,100,0],
            "intensity": 50,
            "size": 1,
            "innerAngle": 10,
            "outerAngle": 60,
            "coneFadeCoef": 7,
            "position": "Light_pos",
            "direction": "Light_dir",
            "hitpoint": "Light_hitpoint",
            "selection": "Light",
            "useFlare": 1,
            "flareSize": 6,
            "flareMaxDistance": 250,
            "dayLight": 0,
            # Class: CfgVehicles\RHS_MELB_base\Reflectors\Light\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 4
            }
        }
    },
    # Class: CfgVehicles\RHS_MELB_base\NVGMarkers,
    "NVGMarkers": {
        # Class: CfgVehicles\RHS_MELB_base\NVGMarkers\IR_Position
        "IR_Position": {
            "color": [0.1,0.1,0.1],
            "ambient": [0.01,0.01,0.01],
            "brightness": 0.15,
            "name": "IR_Position",
            "drawLight": 1,
            "drawLightSize": 0.01,
            "drawLightCenterSize": 0.005,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "onlyInNvg": 1,
            "useFlare": 0
        }
    },
    # Class: CfgVehicles\RHS_MELB_base\EventHandlers,
    "EventHandlers": {
        # Class: CfgVehicles\RHS_MELB_base\EventHandlers\RHS_MELB_EH
        "RHS_MELB_EH": {
            "handleDamage": "_this call RHS_MELB_fnc_fallDamage"
        },
        "fired": "",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    # Class: CfgVehicles\RHS_MELB_base\Components,
    "Components": {
        # Class: CfgVehicles\RHS_MELB_base\Components\SensorsManagerComponent
        "SensorsManagerComponent": {
            # Class: CfgVehicles\RHS_MELB_base\Components\SensorsManagerComponent\Components
            "Components": {
                # Class: CfgVehicles\RHS_MELB_base\Components\SensorsManagerComponent\Components\DataLinkSensorComponent
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
                },
                # Class: CfgVehicles\RHS_MELB_base\Components\SensorsManagerComponent\Components\PassiveRadarSensorComponent,
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
                # Class: CfgVehicles\RHS_MELB_base\Components\SensorsManagerComponent\Components\LaserSensorComponent,
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
                }
            }
        },
        # Class: CfgVehicles\RHS_MELB_base\Components\VehicleSystemsDisplayManagerComponentLeft,
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: VehicleSystemsTemplateLeftPilot\Components
            "Components": {
                # Class: VehicleSystemsTemplateLeftPilot\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: VehicleSystemsTemplateLeftPilot\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                # Class: VehicleSystemsTemplateLeftPilot\Components\CrewDisplay,
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: VehicleSystemsTemplateLeftPilot\Components\SlingLoadDisplay,
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                # Class: VehicleSystemsTemplateLeftPilot\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: VehicleSystemsTemplateLeftPilot\Components\VehicleDriverDisplay,
                "VehicleDriverDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Driver"
                },
                # Class: VehicleSystemsTemplateLeftPilot\Components\SensorDisplay,
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
        # Class: CfgVehicles\RHS_MELB_base\Components\VehicleSystemsDisplayManagerComponentRight,
        "VehicleSystemsDisplayManagerComponentRight": {
            "defaultDisplay": "SensorDisplay",
            # Class: VehicleSystemsTemplateRightPilot\Components,
            "Components": {
                # Class: VehicleSystemsTemplateRightPilot\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: VehicleSystemsTemplateRightPilot\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                # Class: VehicleSystemsTemplateRightPilot\Components\CrewDisplay,
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: VehicleSystemsTemplateRightPilot\Components\SlingLoadDisplay,
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                # Class: VehicleSystemsTemplateRightPilot\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: VehicleSystemsTemplateRightPilot\Components\VehicleDriverDisplay,
                "VehicleDriverDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Driver"
                },
                # Class: VehicleSystemsTemplateRightPilot\Components\SensorDisplay,
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
        },
        # Class: CfgVehicles\Air\Components\TransportCountermeasuresComponent,
        "TransportCountermeasuresComponent": {
        }
    },
    "_generalMacro": "Helicopter_Base_H",
    "irScanRangeMin": 0,
    "irScanRangeMax": 0,
    "irScanToEyeFactor": 1,
    # Class: CfgVehicles\Helicopter_Base_H\PilotSpec,
    "PilotSpec": {
        "showHeadPhones": 1
    },
    # Class: CfgVehicles\Helicopter_Base_H\CargoSpec,
    "CargoSpec": {
        # Class: CfgVehicles\Helicopter_Base_H\CargoSpec\Cargo1
        "Cargo1": {
            "showHeadPhones": 1
        }
    },
    "transportMaxWeapons": 12,
    "transportMaxMagazines": 48,
    "transportMaxBackpacks": 24,
    # Class: CfgVehicles\Helicopter_Base_H\TransportBackpacks,
    "TransportBackpacks": {
    },
    # Class: CfgVehicles\Helicopter_Base_H\TransportMagazines,
    "TransportMagazines": {
    },
    # Class: CfgVehicles\Helicopter_Base_H\TransportWeapons,
    "TransportWeapons": {
    },
    # Class: CfgVehicles\Helicopter_Base_H\TransportItems,
    "TransportItems": {
        # Class: CfgVehicles\Helicopter_Base_H\TransportItems\_xx_FirstAidKit
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 4
        },
        # Class: CfgVehicles\Helicopter_Base_H\TransportItems\_xx_Toolkit,
        "_xx_Toolkit": {
            "name": "Toolkit",
            "count": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\TransportItems\_xx_ItemGPS,
        "_xx_ItemGPS": {
            "name": "ItemGPS",
            "count": 1
        },
        # Class: CfgVehicles\Helicopter_Base_H\TransportItems\_xx_ItemRadio,
        "_xx_ItemRadio": {
            "name": "ItemRadio",
            "count": 1
        }
    },
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "washDownDiameter": "40.0f",
    "minSmokeDamage": 0.3,
    "maxSmokeDamage": 0.99,
    "selectionHRotorStill": "main rotor static",
    "selectionHRotorMove": "main rotor blur",
    "selectionVRotorStill": "tail rotor static",
    "selectionVRotorMove": "tail rotor blur",
    "driverLeftHandAnimName": "lever_pilot",
    "driverRightHandAnimName": "stick_pilot",
    "driverLeftLegAnimName": "pedalL",
    "driverRightLegAnimName": "pedalR",
    # Class: CfgVehicles\Helicopter_Base_F\CamShake,
    "CamShake": {
        "power": 30,
        "frequency": 20,
        "distance": 50,
        "minSpeed": 50
    },
    "camShakeCoef": 0,
    "simulation": "helicopterrtd",
    "unitInfoTypeLite": "RscUnitInfoAirRTDBasic",
    "vehicleClass": "Air",
    "gearRetracting": 0,
    "dustEffect": "HeliDust",
    "waterEffect": "HeliWater",
    "gearUpTime": 3.33,
    "gearDownTime": 2,
    "gearMinAlt": 0.5,
    # Class: CfgVehicles\Helicopter\ViewPilot,
    "ViewPilot": {
        "initFov": 0.9,
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
    "mainRotorSpeed": 1,
    "backRotorSpeed": 1.5,
    "maxMainRotorDive": 0,
    "maxBackRotorDive": 0,
    "minMainRotorDive": 0,
    "minBackRotorDive": 0,
    "neutralBackRotorDive": 0,
    "neutralMainRotorDive": 0,
    "memoryPointLMissile": "L strela",
    "memoryPointRMissile": "P strela",
    "memoryPointLRocket": "L raketa",
    "memoryPointRRocket": "P raketa",
    "memoryPointGun": "",
    "memoryPointPilot": "pilot",
    "_mainBladeCenter": "rotor_center",
    "selectionFireAnim": "zasleh",
    "enableSweep": 1,
    "envelope": [0,0.2,0.9,2.1,2.5,3.3,3.5,3.6,3.7,3.8,3.8,3,0.9,0.7,0.5],
    "minFireTime": 20,
    "steerAheadSimul": 0.5,
    "steerAheadPlan": 0.7,
    "soundLandingGear": ["",1,1],
    # Class: CfgVehicles\Helicopter\SpeechVariants,
    "SpeechVariants": {
        # Class: CfgVehicles\Helicopter\SpeechVariants\Default
        "Default": {
            "speechSingular": ["veh_air_helicopter_s"],
            "speechPlural": ["veh_air_helicopter_p"]
        }
    },
    "editorSubcategory": "EdSubcat_Helicopters",
    "extCameraParams": [-1],
    "textSingular": "helicopter",
    "textPlural": "helicopters",
    "camouflage": 100,
    "audible": 50,
    "headGforceLeaningFactor": [0.01,0.0025,0.01],
    "driverCanEject": 0,
    "damageEffect": "AirDestructionEffects",
    "type": 2,
    "dammageHalf": [],
    "dammageFull": [],
    "crewVulnerable": 1,
    "explosionShielding": 4,
    "minTotalDamageThreshold": 0.005,
    # Class: CfgVehicles\Helicopter\DestructionEffects,
    "DestructionEffects": {
    },
    "mainBladeCenter": "rotor_center",
    "tailBladeCenter": "rotor_02_center",
    "tailBladeVertical": 1,
    "slingLoadMinCargoMass": 0,
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
    "typicalCargo": ["Soldier"],
    "enableGPS": 1,
    # Class: CfgVehicles\Air\MarkerLights,
    "MarkerLights": {
        # Class: CfgVehicles\Air\MarkerLights\RedStill
        "RedStill": {
            "name": "cerveny pozicni",
            "color": [0.3,0.03,0.03,1],
            "ambient": [0.03,0.003,0.003,1],
            "brightness": 0.01,
            "blinking": 0
        },
        # Class: CfgVehicles\Air\MarkerLights\GreenStill,
        "GreenStill": {
            "name": "zeleny pozicni",
            "color": [0.03,0.3,0.03,1],
            "ambient": [0.003,0.03,0.003,1],
            "brightness": 0.01,
            "blinking": 0
        },
        # Class: CfgVehicles\Air\MarkerLights\WhiteStill,
        "WhiteStill": {
            "name": "bily pozicni",
            "color": [0.3,0.3,0.3,1],
            "ambient": [0.03,0.03,0.03,1],
            "brightness": 0.01,
            "blinking": 0
        },
        # Class: CfgVehicles\Air\MarkerLights\WhiteBlinking,
        "WhiteBlinking": {
            "name": "bily pozicni blik",
            "color": [1,1,1,1],
            "ambient": [0.1,0.1,0.1,1],
            "brightness": 0.01,
            "blinking": 1
        },
        # Class: CfgVehicles\Air\MarkerLights\RedBlinking,
        "RedBlinking": {
            "name": "cerveny pozicni blik",
            "color": [0.5,0.05,0.05,1],
            "ambient": [0.05,0.005,0.005,1],
            "brightness": 0.01,
            "blinking": 1
        },
        # Class: CfgVehicles\Air\MarkerLights\PositionRed,
        "PositionRed": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "intensity": 75,
            "name": "PositionLight_red_1_pos",
            "drawLight": 1,
            "drawLightSize": 0.15,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\Air\MarkerLights\PositionRed\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\Air\MarkerLights\PositionGreen,
        "PositionGreen": {
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "name": "PositionLight_green_1_pos",
            "intensity": 75,
            "drawLight": 1,
            "drawLightSize": 0.15,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\Air\MarkerLights\PositionRed\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\Air\MarkerLights\PositionWhite,
        "PositionWhite": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "PositionLight_white_1_pos",
            "drawLightSize": 0.2,
            "intensity": 75,
            "drawLight": 1,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\Air\MarkerLights\PositionRed\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\Air\MarkerLights\CollisionRed,
        "CollisionRed": {
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "name": "CollisionLight_red_1_pos",
            "blinking": 1,
            "blinkingPattern": [0.2,1.3],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.08,
            "intensity": 75,
            "drawLight": 1,
            "activeLight": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\Air\MarkerLights\PositionRed\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\Air\MarkerLights\CollisionWhite,
        "CollisionWhite": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "CollisionLight_white_1_pos",
            "blinking": 1,
            "blinkingPattern": [0.1,0.9],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.2,
            "drawLightCenterSize": 0.04,
            "intensity": 75,
            "drawLight": 1,
            "activeLight": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\Air\MarkerLights\PositionRed\Attenuation,
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
    "weaponsGroup1": "1 + 		2",
    "weaponsGroup2": 4,
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    "waterLeakiness": 100,
    "waterResistance": 1,
    "impactEffectsSea": "ImpactEffectsAir",
    "flareVelocity": 100,
    "enableRadio": 1,
    "countermeasureActivationRadius": 10000,
    # Class: CfgVehicles\Air\camShakeGForce,
    "camShakeGForce": {
        "power": 0.2,
        "frequency": 3,
        "distance": 0,
        "minSpeed": 1
    },
    # Class: CfgVehicles\Air\camShakeDamage,
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
    # Class: CfgVehicles\AllVehicles\SquadTitles,
    "SquadTitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memoryPointDriverOptics": ["driverview","pilot"],
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "memoryPointTaskMarker": "",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
    "selectionShowDamage": "poskozeni",
    "selectionBackLights": "zadni svetlo",
    # Class: CfgVehicles\AllVehicles\NewTurret,
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
    # Class: CfgVehicles\AllVehicles\SoundEvents,
    "SoundEvents": {
    },
    "tracksSpeed": 0,
    "selectionLeftOffset": "",
    "selectionRightOffset": "",
    # Class: CfgVehicles\AllVehicles\RenderTargets,
    "RenderTargets": {
    },
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
    "enableWatch": 0,
    "allowTabLock": 1,
    "showAllTargets": 0,
    "dustFrontLeftPos": "dustFrontLeft",
    "dustFrontRightPos": "dustFrontRight",
    "dustBackLeftPos": "dustBackLeft",
    "dustBackRightPos": "dustBackRight",
    "wheelCircumference": 1,
    "waterResistanceCoef": 0.5,
    "waterLinearDampingCoefX": 0,
    "waterLinearDampingCoefY": 0,
    "waterAngularDampingCoef": 0,
    "showNVGDriver": 0,
    "showNVGCommander": 0,
    "showNVGGunner": 0,
    "showNVGCargo": [0],
    "soundAttenuationCargo": [1],
    "countsForScoreboard": 1,
    "hullDamageCauseExplosion": 0,
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
    "soundGearUp": ["",1,1],
    "soundGearDown": ["",1,1],
    "soundFlapsUp": ["",1,1],
    "soundFlapsDown": ["",1,1],
    "cabinOpenSound": ["",1,1],
    "cabinCloseSound": ["",1,1],
    "cabinOpenSoundInternal": ["",1,1],
    "cabinCloseSoundInternal": ["",1,1],
    "emptySound": ["",0,1],
    "aggregateReflectors": [],
    "cargoIsCoDriver": [0],
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
    # Class: CfgVehicles\All\FxExplo,
    "FxExplo": {
        "access": 1
    },
    # Class: CfgVehicles\All\GunFire,
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
    # Class: CfgVehicles\All\GunClouds,
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
    # Class: CfgVehicles\All\MGunClouds,
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
    "slingLoadCargoMemoryPoints": [],
    "slingLoadCargoMemoryPointsDir": [],
    "numberPhysicalWheels": 0,
    "damageHalf": [],
    "damageFull": [],
    "soundTurnIn": ["",0.000316228,1],
    "soundTurnOut": ["",0.000316228,1],
    "soundTurnInInternal": ["",0.000316228,1],
    "soundTurnOutInternal": ["",0.000316228,1],
    "features": "",
    "insideDetectCoef": 0.05,
}