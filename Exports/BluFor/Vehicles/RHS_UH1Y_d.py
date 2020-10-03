RHS_UH1Y_d = {
    "faction": "rhs_faction_usmc_d",
    "vehicleClass": "rhs_vehclass_helicopter",
    "crew": "rhsusf_usmc_marpat_d_helipilot",
    "typicalCargo": ["rhsusf_usmc_marpat_d_helicrew"],
    "author": "Red Hammer Studios",
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|RHS_UH1Y_d.paa",
    "scope": 2,
    "accuracy": 1.5,
    "selectionFireAnim": "",
    # Class: CfgVehicles\RHS_UH1Y\Turrets,
    "Turrets": {
        # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret
        "CopilotTurret": {
            "primaryObserver": 0,
            "primaryGunner": 1,
            "primary": 1,
            "playerPosition": 0,
            "isCopilot": 1,
            "usePiP": 1,
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\MFD,
            "MFD": {
            },
            "gunnerName": "Observer",
            "weapons": ["rhs_weap_laserDesignator_AI"],
            "magazines": ["rhs_LaserMag_ai"],
            "gunnerAction": "RHS_UH1Y_Copilot",
            "gunnerInAction": "RHS_UH1Y_Copilot",
            "body": "ObsTurret",
            "gun": "ObsGun",
            "animationSourceBody": "ObsTurret",
            "animationSourceGun": "ObsGun",
            "gunBeg": "gun_end",
            "gunEnd": "gun_begin",
            "memoryPointGun": "gun_end",
            "memoryPointGunnerOptics": "commanderview",
            "turretInfoType": "RHS_RscUH1Y_Observer",
            "initElev": 0,
            "minElev": -80,
            "maxElev": 30,
            "minTurn": -180,
            "maxTurn": 180,
            "CanEject": 0,
            "memoryPointsGetInGunner": "pos codriver",
            "memoryPointsGetInGunnerDir": "pos codriver dir",
            "gunnerGetInAction": "copilot_Heli_Light_02_Enter",
            "gunnerGetOutAction": "copilot_Heli_Light_02_Exit",
            "selectionFireAnim": "",
            "preciseGetInOut": 1,
            "GunnerDoor": "DoorL",
            "gunnerLeftHandAnimName": "lever_copilot",
            "gunnerRightHandAnimName": "stick_copilot",
            "proxyIndex": 1,
            "commanding": -1,
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\OpticsIn\Wide
                "Wide": {
                    "opticsDisplayName": "W",
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "initFov": 0.466,
                    "minFov": 0.0218,
                    "maxFov": 0.466,
                    "visionMode": ["Normal","Ti"],
                    "directionStabilized": 1,
                    "thermalMode": [0,1],
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhs_uh1_flir"
                }
            },
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\OpticsOut,
            "OpticsOut": {
                # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\OpticsOut\Monocular
                "Monocular": {
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "initFov": 1.1,
                    "minFov": 0.33,
                    "maxFov": 1.1,
                    "visionMode": ["Normal","NVG"],
                    "gunnerOpticsModel": "",
                    "gunnerOpticsEffect": []
                }
            },
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Reflectors,
            "Reflectors": {
                # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Reflectors\cabin
                "cabin": {
                    "color": [830,100,100],
                    "ambient": [5,0,0],
                    "intensity": 4,
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
                    # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Reflectors\cabin\Attenuation,
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 50,
                        "hardLimitStart": 1,
                        "hardLimitEnd": 1.5
                    }
                },
                # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Reflectors\cargo_light_1,
                "cargo_light_1": {
                    "color": [830,100,100],
                    "position": "cargo_light_1",
                    "direction": "cargo_light_1_dir",
                    "hitpoint": "cargo_light_1",
                    "selection": "cargo_light_1",
                    "intensity": 7,
                    "useFlare": 0,
                    "coneFadeCoef": 0.1,
                    # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Reflectors\cargo_light_1\Attenuation,
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardLimitStart": 1,
                        "hardLimitEnd": 1.5
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
                # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Reflectors\cargo_light_2,
                "cargo_light_2": {
                    "position": "cargo_light_2",
                    "direction": "cargo_light_2_dir",
                    "hitpoint": "cargo_light_2",
                    "selection": "cargo_light_2",
                    "color": [830,100,100],
                    "intensity": 7,
                    "useFlare": 0,
                    "coneFadeCoef": 0.1,
                    # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Reflectors\cargo_light_1\Attenuation,
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 1,
                        "quadratic": 70,
                        "hardLimitStart": 1,
                        "hardLimitEnd": 1.5
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
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components,
            "Components": {
                # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components
                    "Components": {
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\MinimapDisplay,
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay,
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SensorDisplay,
                        "SensorDisplay": {
                            "componentType": "SensorsDisplayComponent",
                            "range": [8000,16000,20000,50000],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultDisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    "defaultDisplay": "SensorDisplay",
                    # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components,
                    "Components": {
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\MinimapDisplay,
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay,
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\CopilotTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\SensorDisplay,
                        "SensorDisplay": {
                            "componentType": "SensorsDisplayComponent",
                            "range": [8000,16000,20000,50000],
                            "resource": "RscCustomInfoSensors"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "stabilizedInAxes": 3,
            "initTurn": 0,
            "soundServo": ["",0.01,1,30],
            "inGunnerMayFire": 1,
            "gunnerOpticsEffect": [],
            "gunnerOpticsModel": "",
            "gunnerLeftLegAnimName": "pedalL",
            "gunnerRightLegAnimName": "pedalR",
            # Class: CfgVehicles\Heli_light_03_base_F\Turrets\MainTurret\ViewGunner,
            "ViewGunner": {
                "initAngleX": -15,
                "initFov": 0.9,
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
            "startEngine": 0,
            "gunnerHasFlares": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\Turrets\MainTurret\HitPoints,
            "HitPoints": {
                # Class: CfgVehicles\Heli_light_03_base_F\Turrets\MainTurret\HitPoints\HitTurret
                "HitTurret": {
                    "armor": 1,
                    "material": -1,
                    "name": "main_turret_hit",
                    "visual": "gun",
                    "passThrough": 0.2,
                    "radius": 0.25
                },
                # Class: CfgVehicles\Heli_light_03_base_F\Turrets\MainTurret\HitPoints\HitGun,
                "HitGun": {
                    "armor": 1,
                    "material": -1,
                    "name": "main_gun_hit",
                    "visual": "gun",
                    "passThrough": 0.2,
                    "radius": 0.25
                }
            },
            "turretCanSee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\TurretSpec,
            "TurretSpec": {
                "showHeadPhones": 1
            },
            "outGunnerMayFire": 1,
            "castGunnerShadow": 1,
            "viewGunnerShadow": 1,
            "gunnerForceOptics": 0,
            "enableManualFire": 0,
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "gunnerType": "",
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
            "hasGunner": 1,
            "canUseScanners": 1,
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOpticsShowCursor": 0,
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
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
            "gunnerCompartments": "Compartment1",
            "LODTurnedIn": -1,
            "LODTurnedOut": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
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
            "turretFollowFreeLook": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "dontCreateAI": 0,
            "disableSoundAttenuation": 0,
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
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret,
        "MainTurret": {
            "usePiP": 0,
            "isCopilot": 0,
            "showAsCargo": 1,
            "proxyIndex": 2,
            "animationSourceBody": "mainTurret",
            "animationSourceGun": "mainGun",
            "body": "mainTurret",
            "gun": "mainGun",
            "minElev": -55,
            "maxElev": 20,
            "initElev": 0,
            "minTurn": 30,
            "maxTurn": 125,
            "initTurn": 90,
            "soundServo": ["",0.01,1],
            "gunnerLeftHandAnimName": "OtocHlaven_1",
            "gunnerRightHandAnimName": "OtocHlaven_1",
            "gunnerLeftLegAnimName": "gunner_1_leg_left",
            "gunnerRightLegAnimName": "gunner_1_legs",
            "gunnerAction": "RHS_UH1Y_Gunner_L",
            "gunnerInAction": "RHS_UH1Y_Gunner_L",
            "animationSourceHatch": "",
            "stabilizedInAxes": "StabilizedInAxesNone",
            "gunBeg": "muzzle_1",
            "gunEnd": "chamber_1",
            "selectionFireAnim": "zasleh",
            "weapons": ["rhs_weap_m134_minigun_1"],
            "magazines": ["rhs_mag_762x51_m80a1_4000"],
            "gunnerName": "Left door gunner",
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "gunnerOutOpticsShowCursor": 1,
            "gunnerOpticsShowCursor": 1,
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "RHS_HIND_Cargo_Exit",
            "preciseGetInOut": 0,
            "turretInfoType": "RscWeaponZeroing",
            "commanding": -2,
            "playerPosition": 1,
            "primaryGunner": 0,
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\ViewOptics,
            "ViewOptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 75,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -75,
                "minangley": -100,
                "minfov": 0.25
            },
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\ViewGunner,
            "ViewGunner": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 75,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -75,
                "minangley": -100,
                "minfov": 0.25,
                "visionMode": []
            },
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\OpticsIn\ViewOptics
                "ViewOptics": {
                    "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
                    "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.7,
                    "maxanglex": 75,
                    "maxangley": 100,
                    "maxfov": 1.1,
                    "minanglex": -75,
                    "minangley": -100,
                    "minfov": 0.25,
                    "visionMode": []
                }
            },
            "gunnerCompartments": "Compartment2",
            "memoryPointGun": "machinegun",
            "memoryPointGunnerOptics": "gunnerview_1",
            "soundAttenuationTurret": "HeliAttenuationGunner",
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Reflectors,
            "Reflectors": {
            },
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components,
            "Components": {
                # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components
                    "Components": {
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay,
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
                # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    "defaultDisplay": "SensorDisplay",
                    # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components,
                    "Components": {
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay,
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
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Hitpoints,
            "Hitpoints": {
            },
            "inGunnerMayFire": 1,
            "gunnerOpticsEffect": [],
            # Class: CfgVehicles\Heli_light_03_base_F\Turrets\MainTurret\OpticsOut,
            "OpticsOut": {
                # Class: CfgVehicles\Heli_light_03_base_F\Turrets\MainTurret\OpticsOut\Monocular
                "Monocular": {
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "minFov": 0.25,
                    "maxFov": 1.25,
                    "initFov": 0.75,
                    "visionMode": ["Normal","NVG"],
                    "gunnerOpticsModel": "",
                    "gunnerOpticsEffect": []
                }
            },
            "startEngine": 0,
            "gunnerHasFlares": 0,
            "turretCanSee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\TurretSpec,
            "TurretSpec": {
                "showHeadPhones": 1
            },
            "outGunnerMayFire": 1,
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "castGunnerShadow": 1,
            "viewGunnerShadow": 1,
            "gunnerForceOptics": 0,
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
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
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
            "forceNVG": 0,
            "gunnerDoor": "",
            "turretFollowFreeLook": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "dontCreateAI": 0,
            "disableSoundAttenuation": 0,
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
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_UH1Y\Turrets\RightDoorGun,
        "RightDoorGun": {
            "body": "Turret_2",
            "gun": "Gun_2",
            "animationSourceBody": "Turret_2",
            "animationSourceGun": "Gun_2",
            "weapons": ["rhs_weap_m134_minigun_2"],
            "stabilizedInAxes": "StabilizedInAxesNone",
            "selectionFireAnim": "zasleh_1",
            "proxyIndex": 3,
            "playerPosition": 1,
            "gunnerName": "Right door gunner",
            "commanding": -3,
            "minElev": -55,
            "maxElev": 20,
            "initElev": 0,
            "minTurn": -135,
            "maxTurn": -25,
            "initTurn": -90,
            "gunBeg": "muzzle_2",
            "gunEnd": "chamber_2",
            "primaryGunner": 0,
            "memoryPointGun": "machinegun_1",
            "memoryPointGunnerOptics": "gunnerview_2",
            "gunnerLeftHandAnimName": "OtocHlaven_2",
            "gunnerRightHandAnimName": "OtocHlaven_2",
            "gunnerLeftLegAnimName": "gunner_2_leg_left",
            "gunnerRightLegAnimName": "gunner_2_legs",
            "gunnerAction": "RHS_UH1Y_Gunner_R",
            "gunnerInAction": "RHS_UH1Y_Gunner_R",
            "usePiP": 0,
            "isCopilot": 0,
            "showAsCargo": 1,
            "soundServo": ["",0.01,1],
            "animationSourceHatch": "",
            "magazines": ["rhs_mag_762x51_m80a1_4000"],
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "gunnerOutOpticsShowCursor": 1,
            "gunnerOpticsShowCursor": 1,
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "RHS_HIND_Cargo_Exit",
            "preciseGetInOut": 0,
            "turretInfoType": "RscWeaponZeroing",
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\ViewOptics,
            "ViewOptics": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 75,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -75,
                "minangley": -100,
                "minfov": 0.25
            },
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\ViewGunner,
            "ViewGunner": {
                "initanglex": 0,
                "initangley": 0,
                "initfov": 0.7,
                "maxanglex": 75,
                "maxangley": 100,
                "maxfov": 1.1,
                "minanglex": -75,
                "minangley": -100,
                "minfov": 0.25,
                "visionMode": []
            },
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\OpticsIn\ViewOptics
                "ViewOptics": {
                    "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
                    "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                    "initanglex": 0,
                    "initangley": 0,
                    "initfov": 0.7,
                    "maxanglex": 75,
                    "maxangley": 100,
                    "maxfov": 1.1,
                    "minanglex": -75,
                    "minangley": -100,
                    "minfov": 0.25,
                    "visionMode": []
                }
            },
            "gunnerCompartments": "Compartment2",
            "soundAttenuationTurret": "HeliAttenuationGunner",
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Reflectors,
            "Reflectors": {
            },
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components,
            "Components": {
                # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components
                    "Components": {
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay,
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
                # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    "defaultDisplay": "SensorDisplay",
                    # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components,
                    "Components": {
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay,
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
            # Class: CfgVehicles\RHS_UH1Y\Turrets\MainTurret\Hitpoints,
            "Hitpoints": {
            },
            "inGunnerMayFire": 1,
            "gunnerOpticsEffect": [],
            # Class: CfgVehicles\Heli_light_03_base_F\Turrets\MainTurret\OpticsOut,
            "OpticsOut": {
                # Class: CfgVehicles\Heli_light_03_base_F\Turrets\MainTurret\OpticsOut\Monocular
                "Monocular": {
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "minFov": 0.25,
                    "maxFov": 1.25,
                    "initFov": 0.75,
                    "visionMode": ["Normal","NVG"],
                    "gunnerOpticsModel": "",
                    "gunnerOpticsEffect": []
                }
            },
            "startEngine": 0,
            "gunnerHasFlares": 0,
            "turretCanSee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\TurretSpec,
            "TurretSpec": {
                "showHeadPhones": 1
            },
            "outGunnerMayFire": 1,
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "castGunnerShadow": 1,
            "viewGunnerShadow": 1,
            "gunnerForceOptics": 0,
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
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
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
            "forceNVG": 0,
            "gunnerDoor": "",
            "turretFollowFreeLook": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "dontCreateAI": 0,
            "disableSoundAttenuation": 0,
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
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_01,
        "CargoTurret_01": {
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "passenger_inside_2",
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "RHS_HIND_Cargo_Exit",
            "memoryPointsGetInGunner": "pos cargo R",
            "memoryPointsGetInGunnerDir": "pos cargo R dir",
            "gunnerName": "Passenger (Right Bench 1)",
            "gunnerCompartments": "Compartment2",
            "memoryPointGunnerOptics": "",
            "proxyIndex": 1,
            "maxElev": 15,
            "minElev": -45,
            "maxTurn": -48,
            "minTurn": -104,
            "isPersonTurret": 1,
            "gunnerUsesPilotView": 1,
            "selectionFireAnim": "",
            "gunnerCanEject": 1,
            "cantCreateAI": 1,
            "commanding": -1,
            "playerPosition": 1,
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_01\Hitpoints,
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
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_02,
        "CargoTurret_02": {
            "gunnerName": "Passenger (Right Bench 2)",
            "memoryPointsGetInGunner": "pos cargo R4",
            "memoryPointsGetInGunnerDir": "pos cargo R4 dir",
            "proxyIndex": 3,
            "maxTurn": 47,
            "minTurn": 22,
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "passenger_inside_2",
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "RHS_HIND_Cargo_Exit",
            "gunnerCompartments": "Compartment2",
            "memoryPointGunnerOptics": "",
            "maxElev": 15,
            "minElev": -45,
            "isPersonTurret": 1,
            "gunnerUsesPilotView": 1,
            "selectionFireAnim": "",
            "gunnerCanEject": 1,
            "cantCreateAI": 1,
            "commanding": -1,
            "playerPosition": 1,
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_01\Hitpoints,
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
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_03,
        "CargoTurret_03": {
            "gunnerName": "Passenger (Right Bench 3)",
            "memoryPointsGetInGunner": "pos cargo R2",
            "memoryPointsGetInGunnerDir": "pos cargo R2 dir",
            "proxyIndex": 6,
            "maxTurn": 70,
            "minTurn": 22,
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "passenger_inside_2",
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "RHS_HIND_Cargo_Exit",
            "gunnerCompartments": "Compartment2",
            "memoryPointGunnerOptics": "",
            "maxElev": 15,
            "minElev": -45,
            "isPersonTurret": 1,
            "gunnerUsesPilotView": 1,
            "selectionFireAnim": "",
            "gunnerCanEject": 1,
            "cantCreateAI": 1,
            "commanding": -1,
            "playerPosition": 1,
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_01\Hitpoints,
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
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_04,
        "CargoTurret_04": {
            "memoryPointsGetInGunner": "pos cargo L",
            "memoryPointsGetInGunnerDir": "pos cargo L dir",
            "gunnerName": "Passenger (Left Bench 1)",
            "proxyIndex": 2,
            "maxTurn": 104,
            "minTurn": 58,
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "passenger_inside_2",
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "RHS_HIND_Cargo_Exit",
            "gunnerCompartments": "Compartment2",
            "memoryPointGunnerOptics": "",
            "maxElev": 15,
            "minElev": -45,
            "isPersonTurret": 1,
            "gunnerUsesPilotView": 1,
            "selectionFireAnim": "",
            "gunnerCanEject": 1,
            "cantCreateAI": 1,
            "commanding": -1,
            "playerPosition": 1,
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_01\Hitpoints,
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
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_05,
        "CargoTurret_05": {
            "gunnerName": "Passenger (Left Bench 2)",
            "memoryPointsGetInGunner": "pos cargo L4",
            "memoryPointsGetInGunnerDir": "pos cargo L4 dir",
            "proxyIndex": 4,
            "maxTurn": -16,
            "minTurn": -40,
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "passenger_inside_2",
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "RHS_HIND_Cargo_Exit",
            "gunnerCompartments": "Compartment2",
            "memoryPointGunnerOptics": "",
            "maxElev": 15,
            "minElev": -45,
            "isPersonTurret": 1,
            "gunnerUsesPilotView": 1,
            "selectionFireAnim": "",
            "gunnerCanEject": 1,
            "cantCreateAI": 1,
            "commanding": -1,
            "playerPosition": 1,
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_01\Hitpoints,
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
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_06,
        "CargoTurret_06": {
            "gunnerName": "Passenger (Left Bench 3)",
            "memoryPointsGetInGunner": "pos cargo L2",
            "memoryPointsGetInGunnerDir": "pos cargo L2 dir",
            "proxyIndex": 7,
            "maxTurn": 3,
            "minTurn": -55,
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "passenger_inside_2",
            "gunnerGetInAction": "GetInHeli_Transport_01Cargo",
            "gunnerGetOutAction": "RHS_HIND_Cargo_Exit",
            "gunnerCompartments": "Compartment2",
            "memoryPointGunnerOptics": "",
            "maxElev": 15,
            "minElev": -45,
            "isPersonTurret": 1,
            "gunnerUsesPilotView": 1,
            "selectionFireAnim": "",
            "gunnerCanEject": 1,
            "cantCreateAI": 1,
            "commanding": -1,
            "playerPosition": 1,
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            # Class: CfgVehicles\RHS_UH1Y\Turrets\CargoTurret_01\Hitpoints,
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
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        }
    },
    # Class: CfgVehicles\RHS_UH1Y\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\RHS_UH1Y\AnimationSources\Gatling_1
        "Gatling_1": {
            "source": "revolving",
            "weapon": "rhs_weap_m134_minigun_1"
        },
        # Class: CfgVehicles\RHS_UH1Y\AnimationSources\Gatling_2,
        "Gatling_2": {
            "source": "revolving",
            "weapon": "rhs_weap_m134_minigun_2"
        },
        # Class: CfgVehicles\RHS_UH1Y\AnimationSources\muzzle_rot_hmg,
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m134_minigun_1"
        },
        # Class: CfgVehicles\RHS_UH1Y\AnimationSources\muzzle_rot_hmg2,
        "muzzle_rot_hmg2": {
            "source": "ammorandom",
            "weapon": "rhs_weap_m134_minigun_2"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\cargolights_hide,
        "cargolights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\cabinlights_hide,
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\HitAvionics,
        "HitAvionics": {
            "source": "hit",
            "hitpoint": "HitAvionics",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\HitFuel,
        "HitFuel": {
            "source": "hit",
            "hitpoint": "HitFuel",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\DoorL,
        "DoorL": {
            "source": "door",
            "animPeriod": 0.8,
            "initPhase": 0,
            "sound": "MetalDoorsSound",
            "soundPosition": "doorL_axis"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\DoorR,
        "DoorR": {
            "soundPosition": "doorR_axis",
            "source": "door",
            "animPeriod": 0.8,
            "initPhase": 0,
            "sound": "MetalDoorsSound"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\DoorRB,
        "DoorRB": {
            "source": "user",
            "animPeriod": 1.5,
            "initPhase": 1,
            "sound": "MetalOldBigDoorsSound",
            "soundPosition": "doorRB_axis"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\DoorLB,
        "DoorLB": {
            "soundPosition": "doorLB_axis",
            "source": "user",
            "animPeriod": 1.5,
            "initPhase": 1,
            "sound": "MetalOldBigDoorsSound"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\doorHandler_L,
        "doorHandler_L": {
            "source": "user",
            "animPeriod": 0.0001,
            "initPhase": 0,
            "sound": "MetalDoorsSound",
            "soundPosition": "doorL_axis"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\doorHandler_R,
        "doorHandler_R": {
            "source": "user",
            "animPeriod": 0.0001,
            "initPhase": 0,
            "sound": "MetalDoorsSound",
            "soundPosition": "doorL_axis"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\pip1_on,
        "pip1_on": {
            "source": "user",
            "animPeriod": 0.0001,
            "initPhase": 0,
            "sound": "MetalDoorsSound",
            "soundPosition": "doorL_axis"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\pip2_on,
        "pip2_on": {
            "source": "user",
            "animPeriod": 0.0001,
            "initPhase": 0,
            "sound": "MetalDoorsSound",
            "soundPosition": "doorL_axis"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\hide_rockets,
        "hide_rockets": {
            "mass": -50,
            "source": "user",
            "animPeriod": 0.0001,
            "initPhase": 0,
            "sound": "MetalDoorsSound",
            "soundPosition": "doorL_axis"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\hide_mg,
        "hide_mg": {
            "displayName": "hide MG",
            "mass": -120,
            "source": "user",
            "animPeriod": 0.0001,
            "initPhase": 0,
            "sound": "MetalDoorsSound",
            "soundPosition": "doorL_axis"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\hide_FrontDoors,
        "hide_FrontDoors": {
            "displayName": "hide front doors",
            "initPhase": 0,
            "mass": -100,
            "source": "user",
            "animPeriod": 0.0001,
            "sound": "MetalDoorsSound",
            "soundPosition": "doorL_axis"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\hide_CargoDoors,
        "hide_CargoDoors": {
            "displayName": "hide cargo doors",
            "mass": -200,
            "initPhase": 0,
            "source": "user",
            "animPeriod": 0.0001,
            "sound": "MetalDoorsSound",
            "soundPosition": "doorL_axis"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\HUDAction,
        "HUDAction": {
            "source": "user",
            "animPeriod": 2,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\HUDAction_1,
        "HUDAction_1": {
            "animPeriod": 0.1,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\mainRotor_folded,
        "mainRotor_folded": {
            "source": "user",
            "animPeriod": 0.001,
            "initPhase": 0,
            "mass": 1,
            "displayName": "fold main rotor",
            "onPhaseChanged": "_this call rhs_fnc_foldHeli"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\HitGlass7,
        "HitGlass7": {
            "hitpoint": "HitGlass7",
            "raw": 1,
            "source": "hit"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\hit_pylon_1_source,
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\AnimationSources\hit_pylon_2_source,
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\GunL_Revolving,
        "GunL_Revolving": {
            "source": "revolving",
            "weapon": "M134_minigun"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\GunR_Revolving,
        "GunR_Revolving": {
            "source": "revolving",
            "weapon": "M134_minigun"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\muzzle_hide,
        "muzzle_hide": {
            "source": "reload",
            "weapon": "M134_minigun"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\Muzzle_Flash,
        "Muzzle_Flash": {
            "source": "ammorandom",
            "weapon": "M134_minigun",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\Missiles_revolving,
        "Missiles_revolving": {
            "source": "revolving",
            "weapon": "missiles_DAR"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\RocketPods_Hide,
        "RocketPods_Hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HideWeapons,
        "HideWeapons": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass1,
        "HitGlass1": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass1"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass2,
        "HitGlass2": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass2"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass3,
        "HitGlass3": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass3"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass4,
        "HitGlass4": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass4"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass5,
        "HitGlass5": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass5"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass6,
        "HitGlass6": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass6"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass8,
        "HitGlass8": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass8"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass9,
        "HitGlass9": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass9"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass10,
        "HitGlass10": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass10"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass11,
        "HitGlass11": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass11"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass12,
        "HitGlass12": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass12"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass13,
        "HitGlass13": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass13"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\AnimationSources\HitGlass14,
        "HitGlass14": {
            "raw": 1,
            "source": "hit",
            "hitpoint": "HitGlass14"
        },
        # Class: CfgVehicles\Helicopter\AnimationSources\HitEngine1,
        "HitEngine1": {
            "source": "hit",
            "hitpoint": "HitEngine1",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter\AnimationSources\HitEngine2,
        "HitEngine2": {
            "source": "hit",
            "hitpoint": "HitEngine2",
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
    # Class: CfgVehicles\RHS_UH1Y\UserActions,
    "UserActions": {
        # Class: CfgVehicles\RHS_UH1Y\UserActions\HUDoff
        "HUDoff": {
            "displayName": "HUD on",
            "displayNameDefault": "HUD on",
            "position": "zamerny",
            "radius": 1,
            "onlyForPlayer": 1,
            "condition": "(player==driver this)and(this animationphase 'HUDAction' !=1)",
            "statement": "this animate ['HUDAction',1];this animate ['HUDAction_1',1]"
        },
        # Class: CfgVehicles\RHS_UH1Y\UserActions\HUDon,
        "HUDon": {
            "displayName": "HUD off",
            "displayNameDefault": "HUD off",
            "condition": "(player==driver this)and(this animationphase 'HUDAction' !=0)",
            "statement": "this animate ['HUDAction',0];this animate ['HUDAction_1',0]",
            "position": "zamerny",
            "radius": 1,
            "onlyForPlayer": 1
        },
        # Class: CfgVehicles\RHS_UH1Y\UserActions\TogglePIP,
        "TogglePIP": {
            "displayName": "Toggle monitor",
            "displayNameDefault": "Toggle monitor",
            "condition": "( (call rhsusf_fnc_findPlayer)==driver this) or ((call rhsusf_fnc_findPlayer)==this turretUnit [0]) ",
            "statement": "call rhs_fnc_uh1_toggleCam",
            "position": "zamerny",
            "radius": 1,
            "onlyForPlayer": 1
        },
        # Class: CfgVehicles\RHS_UH1Y\UserActions\ToggleLight,
        "ToggleLight": {
            "displayName": "Toggle interior light",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "player in this;",
            "statement": "[this,'cargolights_hide'] call rhs_fnc_toggleIntLight",
            "onlyforplayer": 1
        }
    },
    # Class: CfgVehicles\RHS_UH1Y\EventHandlers,
    "EventHandlers": {
        # Class: CfgVehicles\RHS_UH1Y\EventHandlers\RHSUSF_EventHandlers
        "RHSUSF_EventHandlers": {
        },
        "fired": "",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "side": 1,
    # Class: CfgVehicles\RHS_UH1Y_US_base\Components,
    "Components": {
        # Class: CfgVehicles\RHS_UH1Y_US_base\Components\TransportPylonsComponent
        "TransportPylonsComponent": {
            "UIPicture": "rhsusf|addons|rhsusf_a2port_air2|data|loadouts|RHS_UH1_EDEN_CA.paa",
            # Class: CfgVehicles\RHS_UH1Y_US_base\Components\TransportPylonsComponent\pylons,
            "pylons": {
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\TransportPylonsComponent\pylons\pylon1
                "pylon1": {
                    "hardpoints": ["RHS_HP_FFAR_USMC"],
                    "UIposition": [0.573,0.44],
                    "maxweight": 1200,
                    "priority": 1,
                    "attachment": "rhs_mag_M151_7_green",
                    "bay": -1,
                    "hitpoint": "HitPylon1"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\TransportPylonsComponent\pylons\pylon2,
                "pylon2": {
                    "UIposition": [0.1,0.44],
                    "mirroredMissilePos": 1,
                    "hitpoint": "HitPylon2",
                    "hardpoints": ["RHS_HP_FFAR_USMC"],
                    "maxweight": 1200,
                    "priority": 1,
                    "attachment": "rhs_mag_M151_7_green",
                    "bay": -1
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\TransportPylonsComponent\pylons\cmDispenser,
                "cmDispenser": {
                    "hardpoints": ["RHSUSF_cm_ANALE39","RHSUSF_cm_ANALE39_x2","RHSUSF_cm_ANALE39_x4"],
                    "priority": 1,
                    "attachment": "rhsusf_ANALE39_CMFlare_Chaff_Magazine_x4",
                    "maxweight": 800,
                    "UIposition": [0.33,0]
                }
            },
            # Class: CfgVehicles\RHS_UH1Y_US_base\Components\TransportPylonsComponent\Presets,
            "Presets": {
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\TransportPylonsComponent\Presets\Empty
                "Empty": {
                    "attachment": ["",""],
                    "displayname": "<empty>"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\TransportPylonsComponent\Presets\FFAR,
                "FFAR": {
                    "attachment": ["rhs_mag_M151_7_green","rhs_mag_M151_7_green","rhsusf_ANALE39_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "FFAR"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\TransportPylonsComponent\Presets\GS,
                "GS": {
                    "attachment": ["rhs_mag_M151_19_green","rhs_mag_M151_19_green","rhsusf_ANALE39_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Ground Suppression"
                }
            }
        },
        # Class: CfgVehicles\RHS_UH1Y_US_base\Components\SensorsManagerComponent,
        "SensorsManagerComponent": {
            # Class: CfgVehicles\RHS_UH1Y_US_base\Components\SensorsManagerComponent\Components
            "Components": {
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\SensorsManagerComponent\Components\IRSensorComponent
                "IRSensorComponent": {
                    # Class: CfgVehicles\RHS_UH1Y_US_base\Components\SensorsManagerComponent\Components\IRSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 2000,
                        "maxRange": 4000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": 1
                    },
                    # Class: CfgVehicles\RHS_UH1Y_US_base\Components\SensorsManagerComponent\Components\IRSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 4000,
                        "maxRange": 4000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": 1
                    },
                    "animDirection": "ObsGun",
                    "angleRangeHorizontal": 40,
                    "angleRangeVertical": 30,
                    "typeRecognitionDistance": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "maxFogSeeThrough": 0.95,
                    "minTrackableSpeed": 0,
                    "maxTrackableSpeed": 695,
                    "componentType": "IRSensorComponent",
                    "color": [1,0,0,1],
                    "allowsMarking": 1,
                    "groundNoiseDistanceCoef": -1,
                    "maxGroundNoiseDistance": -1,
                    "aimDown": 0,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\SensorsManagerComponent\Components\VisualSensorComponent,
                "VisualSensorComponent": {
                    # Class: CfgVehicles\RHS_UH1Y_US_base\Components\SensorsManagerComponent\Components\VisualSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 500,
                        "maxRange": 2000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": 1
                    },
                    # Class: CfgVehicles\RHS_UH1Y_US_base\Components\SensorsManagerComponent\Components\VisualSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 500,
                        "maxRange": 2000,
                        "objectDistanceLimitCoef": 1,
                        "viewDistanceLimitCoef": 1
                    },
                    "maxTrackableSpeed": 70,
                    "animDirection": "ObsGun",
                    "angleRangeHorizontal": 40,
                    "angleRangeVertical": 30,
                    "componentType": "VisualSensorComponent",
                    "nightRangeCoef": 0,
                    "maxFogSeeThrough": 0.94,
                    "color": [1,1,0.5,0.8],
                    "typeRecognitionDistance": 2000,
                    "allowsMarking": 1,
                    "groundNoiseDistanceCoef": -1,
                    "maxGroundNoiseDistance": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "aimDown": 0,
                    "minTrackableSpeed": -1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\SensorsManagerComponent\Components\LaserSensorComponent,
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
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\SensorsManagerComponent\Components\PassiveRadarSensorComponent,
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
                }
            }
        },
        # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentLeft,
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components
            "Components": {
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay,
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SlingLoadDisplay,
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SensorDisplay,
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
        # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentRight,
        "VehicleSystemsDisplayManagerComponentRight": {
            "defaultDisplay": "SensorDisplay",
            # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentRight\Components,
            "Components": {
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay,
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\SlingLoadDisplay,
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent",
                    "resource": "RscCustomInfoSlingLoad"
                },
                # Class: CfgVehicles\RHS_UH1Y_US_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\SensorDisplay,
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
        # Class: CfgVehicles\RHS_UH1Y_US_base\Components\TransportCountermeasuresComponent,
        "TransportCountermeasuresComponent": {
        }
    },
    "model": "rhsusf|addons|rhsusf_a2port_air2|UH1Y|UH1Y.p3d",
    "displayName": "UH-1Y (MG)",
    "helmetMountedDisplay": 0,
    "picture": "rhsusf|addons|rhsusf_a2port_air|data|ico|rhs_uh1y_pic_ca.paa",
    "icon": "rhsusf|addons|rhsusf_a2port_air2|data|mapico|Icon_UH1Y_CA.paa",
    "mapSize": 15,
    # Class: CfgVehicles\RHS_UH1Y_base\MFD,
    "MFD": {
    },
    # Class: CfgVehicles\RHS_UH1Y_base\Library,
    "Library": {
        "libTextDesc": "The UH-1Y Venom is an American medium-size multipurpose utility army helicopter. It is equipped with two external Mk66 70 mm rocket stations and two M240D 7.62 mm machine guns.<br />The UH-1Y is able to carry up to 3 tons of cargo or up to 10 passengers. It can provide close air support missions as well as transportation or reconnaissance."
    },
    "fuelCapacity": 600,
    "maxSpeed": 295,
    "cyclicAsideForceCoef": 1,
    "cyclicForwardForceCoef": 0.9,
    "mainRotorSpeed": 1.2,
    "backRotorSpeed": 6.1,
    "driverDoor": "doorR",
    "memoryPointsGetInDriver": "pos Driver",
    "memoryPointsGetInDriverDir": "pos gunner dir",
    "memoryPointsGetInDriverPrecise": "pos driver",
    "memoryPointsGetInGunner": "pos gunner",
    "memoryPointsGetInGunnerDir": "pos gunner dir",
    "transportSoldier": 1,
    "cargoProxyIndexes": [5],
    "getInProxyOrder": [1,2,3,4,5,6,7],
    "memoryPointsGetInCargo": ["pos cargo L"],
    "memoryPointsGetInCargoDir": ["pos cargo L dir"],
    "cargoDoors": ["DoorLB"],
    "cargoIsCoDriver": [0],
    "threat": [0.8,0.1,0.3],
    "gunnerCanSee": "2+4+8+16",
    "driverCanSee": "2+4+8+16",
    # Class: CfgVehicles\RHS_UH1Y_base\TransportMagazines,
    "TransportMagazines": {
        # Class: CfgVehicles\RHS_UH1Y_base\TransportMagazines\_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag
        "_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 12
        },
        # Class: CfgVehicles\RHS_UH1Y_base\TransportMagazines\_xx_rhs_mag_m67,
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 4
        },
        # Class: CfgVehicles\RHS_UH1Y_base\TransportMagazines\_xx_rhs_mag_m18_green,
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 2
        },
        # Class: CfgVehicles\RHS_UH1Y_base\TransportMagazines\_xx_rhs_mag_m18_red,
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 2
        },
        # Class: CfgVehicles\RHS_UH1Y_base\TransportMagazines\_xx_rhs_mag_an_m8hc,
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 4
        }
    },
    # Class: CfgVehicles\RHS_UH1Y_base\TransportItems,
    "TransportItems": {
        # Class: CfgVehicles\RHS_UH1Y_base\TransportItems\_xx_FirstAidKit
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles\RHS_UH1Y_base\TransportItems\_xx_Medikit,
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 2
        }
    },
    # Class: CfgVehicles\RHS_UH1Y_base\TransportWeapons,
    "TransportWeapons": {
        # Class: CfgVehicles\RHS_UH1Y_base\TransportWeapons\_xx_rhs_weap_m4_carryhandle
        "_xx_rhs_weap_m4_carryhandle": {
            "weapon": "rhs_weap_m4_carryhandle",
            "count": 2
        }
    },
    # Class: CfgVehicles\RHS_UH1Y_base\TransportBackpacks,
    "TransportBackpacks": {
        # Class: CfgVehicles\RHS_UH1Y_base\TransportBackpacks\_xx_B_Parachute
        "_xx_B_Parachute": {
            "backpack": "B_Parachute",
            "count": 4
        }
    },
    "radarType": 0,
    "attenuationEffectType": "HeliAttenuation",
    "occludeSoundsWhenIn": 0.562341,
    "obstructSoundsWhenIn": 0.316228,
    "driverInAction": "RHS_UH1Y_Pilot",
    "driverAction": "RHS_UH1Y_Pilot",
    "cargoAction": ["RHS_UH1Y_Cargo02","RHS_UH1Y_Cargo03","RHS_UH1Y_Cargo03","RHS_UH1Y_Cargo02","RHS_UH1Y_Cargo01"],
    # Class: CfgVehicles\RHS_UH1Y_base\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\RHS_UH1Y_base\Exhausts\Exhaust1
        "Exhaust1": {
            "position": "exhaust1",
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectHeliCom"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\Exhausts\Exhaust2,
        "Exhaust2": {
            "position": "exhaust2",
            "direction": "exhaust2_dir",
            "effect": "ExhaustsEffectHeliCom"
        }
    },
    # Class: CfgVehicles\RHS_UH1Y_base\MarkerLights,
    "MarkerLights": {
        # Class: CfgVehicles\RHS_UH1Y_base\MarkerLights\WhiteStill
        "WhiteStill": {
            "name": "bily pozicni",
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "blinking": 1,
            "intensity": 75,
            "blinkingPattern": [0.1,0.9],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.2,
            "drawLightCenterSize": 0.04
        },
        # Class: CfgVehicles\RHS_UH1Y_base\MarkerLights\RedStill,
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
        # Class: CfgVehicles\RHS_UH1Y_base\MarkerLights\GreenStill,
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
        # Class: CfgVehicles\RHS_UH1Y_base\MarkerLights\RedBlinking,
        "RedBlinking": {
            "name": "bily pozicni blik",
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 75,
            "blinking": 1,
            "blinkingPattern": [0.1,0.9],
            "blinkingPatternGuarantee": 0,
            "drawLightSize": 0.2,
            "drawLightCenterSize": 0.04
        },
        # Class: CfgVehicles\RHS_UH1Y_base\MarkerLights\WhiteBlinking,
        "WhiteBlinking": {
            "name": "cerveny pozicni blik",
            "blinkingPattern": [0.2,1.3],
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.08,
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "intensity": 75,
            "blinking": 1,
            "blinkingPatternGuarantee": 0
        }
    },
    # Class: CfgVehicles\RHS_UH1Y_base\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\RHS_UH1Y_base\Reflectors\Middle
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
            # Class: CfgVehicles\RHS_UH1Y_base\Reflectors\Middle\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 4
            }
        }
    },
    # Class: CfgVehicles\RHS_UH1Y_base\HitPoints,
    "HitPoints": {
        # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitAvionics
        "HitAvionics": {
            "visual": "-",
            "armor": 1.3,
            "radius": 0.25,
            "minimalHit": 0.05,
            "explosionShielding": 1.5,
            "name": "avionics_hit",
            "convexComponent": "avionics_hit",
            "material": 51,
            "passThrough": 1
        },
        # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitEngine1,
        "HitEngine1": {
            "armor": 2.5,
            "radius": 0.12,
            "minimalHit": 0.05,
            "name": "engine_1_hit",
            "explosionShielding": 3,
            "visual": "motor",
            "passThrough": 1,
            "convexComponent": "engine_1_hit",
            "material": 51
        },
        # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitEngine2,
        "HitEngine2": {
            "armor": 2.5,
            "radius": 0.12,
            "minimalHit": 0.05,
            "name": "engine_2_hit",
            "convexComponent": "engine_2_hit",
            "explosionShielding": 3,
            "visual": "motor",
            "passThrough": 1,
            "material": 51
        },
        # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitVRotor,
        "HitVRotor": {
            "armor": 1,
            "material": 51,
            "name": "mala vrtule",
            "visual": "mala vrtule staticka",
            "passThrough": 0.5
        },
        # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitHRotor,
        "HitHRotor": {
            "armor": 1,
            "material": 51,
            "name": "velka vrtule",
            "visual": "velka vrtule staticka",
            "passThrough": 0.5
        },
        # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitFuel,
        "HitFuel": {
            "armor": 3,
            "explosionShielding": 4,
            "name": "fuel_hit",
            "passThrough": 0.5,
            "visual": "fuel_hit",
            "radius": 0.2,
            "minimalHit": 0.05,
            "depends": "Total",
            "convexComponent": "hull_hit",
            "material": 51
        },
        # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitGlass7,
        "HitGlass7": {
            "name": "glass7",
            "visual": "glass7",
            "radius": 0.37,
            "armor": 1,
            "explosionShielding": 2,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass5S,
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
        # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon1,
        "HitPylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon1\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon2,
        "HitPylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon2\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_UH1Y_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitHull,
        "HitHull": {
            "armor": 999,
            "minimalHit": 0.05,
            "depends": "Total",
            "radius": 0.01,
            "name": "hull_hit",
            "convexComponent": "hull_hit",
            "explosionShielding": 1,
            "material": 51,
            "visual": "trup",
            "passThrough": 1
        },
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitEngine,
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
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1,
        "HitGlass1": {
            "name": "glass1",
            "visual": "glass1",
            "radius": 0.37,
            "armor": 1,
            "explosionShielding": 2,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects1",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass1\DestructionEffects\BrokenGlass5S,
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
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2,
        "HitGlass2": {
            "name": "glass2",
            "visual": "glass2",
            "radius": 0.37,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects2",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass2\DestructionEffects\BrokenGlass5S,
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
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3,
        "HitGlass3": {
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.25,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects3",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass3\DestructionEffects\BrokenGlass5S,
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
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4,
        "HitGlass4": {
            "name": "glass4",
            "visual": "glass4",
            "radius": 0.25,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects4",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass4\DestructionEffects\BrokenGlass5S,
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
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5,
        "HitGlass5": {
            "name": "glass5",
            "visual": "glass5",
            "radius": 0.34,
            "armor": 1,
            "explosionShielding": 2,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects5",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass5\DestructionEffects\BrokenGlass5S,
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
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6,
        "HitGlass6": {
            "name": "glass6",
            "visual": "glass6",
            "radius": 0.34,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects6",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass6\DestructionEffects\BrokenGlass5S,
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
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8,
        "HitGlass8": {
            "name": "glass8",
            "visual": "glass8",
            "radius": 0.34,
            "armor": 1,
            "explosionShielding": 1.5,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects8",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass8\DestructionEffects\BrokenGlass5S,
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
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9,
        "HitGlass9": {
            "name": "glass9",
            "visual": "glass9",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects9",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass9\DestructionEffects\BrokenGlass5S,
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
        # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10,
        "HitGlass10": {
            "name": "glass10",
            "visual": "glass10",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.025,
            "passThrough": 0,
            # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5NS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4SS",
                    "position": "GlassEffects10",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\Heli_light_03_base_F\HitPoints\HitGlass10\DestructionEffects\BrokenGlass5S,
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
    # Class: CfgVehicles\RHS_UH1Y_base\Damage,
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_sklo.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_sklo_damage.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_sklo_damage.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_sklo_in.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_sklo_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_sklo_in_damage.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_ext.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_ext_damage.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_ext_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_int.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_int_damage.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_int_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|launcher.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|launcher.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|launcher_destruct.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_cockpit.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_cockpit_damage.rvmat","rhsusf|addons|rhsusf_a2port_air2|UH1Y|data|uh1y_cockpit_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    "LockDetectionSystem": "8 + 4",
    "incomingMissileDetectionSystem": 16,
    "hiddenSelections": ["camo1","camo2","rn1","rn2","rn3","rn4","tn1","tn2","tn3","tn4","tn5","tn6","dn1","dn2","dn3","dn4","dn5","dn6","dn7","dn8","dn9","dn10","dn11","dn12","zn1","zn2","zn3"],
    "hiddenSelectionsTextures": ["rhsusf|addons|rhsusf_a2port_air2|uh1y|data|uh1y_ext_co.paa","rhsusf|addons|rhsusf_a2port_air2|uh1y|data|uh1y_int_co.paa"],
    # Class: CfgVehicles\RHS_UH1Y_base\textureSources,
    "textureSources": {
        # Class: CfgVehicles\RHS_UH1Y_base\textureSources\standard
        "standard": {
            "displayName": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_a2port_air2|uh1y|data|uh1y_ext_co.paa","rhsusf|addons|rhsusf_a2port_air2|uh1y|data|uh1y_int_co.paa"],
            "factions": ["rhs_faction_usmc_wd","rhs_faction_usmc_d"]
        }
    },
    "textureList": ["standard",1],
    # Class: CfgVehicles\RHS_UH1Y_base\Attributes,
    "Attributes": {
        # Class: CfgVehicles\RHS_UH1Y_base\Attributes\ObjectTexture
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\RHS_UH1Y_base\Attributes\DoorL,
        "DoorL": {
            "displayName": "Open left door",
            "property": "DoorL",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\Attributes\DoorR,
        "DoorR": {
            "displayName": "Open right door",
            "property": "DoorR",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles\RHS_UH1Y_base\Attributes\FoldHeli,
        "FoldHeli": {
            "displayName": "Fold helicopter rotors",
            "property": "FoldHeli",
            "expression": "[_this,_value] call rhs_fnc_foldHeli",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        }
    },
    # Class: CfgVehicles\RHS_UH1Y_base\RotorLibHelicopterProperties,
    "RotorLibHelicopterProperties": {
        "RTDconfig": "rhsusf|addons|rhsusf_c_a2port_air|UH1Y|RTD_UH1Y.xml",
        "defaultCollective": 0.75,
        "autoHoverCorrection": [5,2.4,0],
        "maxTorque": 1280,
        "maxMainRotorStress": 130000,
        "maxTailRotorStress": 50000,
        "retreatBladeStallWarningSpeed": 87.4556,
        "horizontalWingsAngleCollMin": 0,
        "horizontalWingsAngleCollMax": 0,
        "maxHorizontalStabilizerLeftStress": 10000,
        "maxHorizontalStabilizerRightStress": 10000,
        "maxVerticalStabilizerStress": 10000,
        "stressDamagePerSec": 0.00333333
    },
    "numberPhysicalWheels": 0,
    "dlc": "RHS_USAF",
    "rhs_hasNoRadar": 1,
    "armorStructural": 2,
    "category": "Air",
    "memoryPointCM": ["flare_launcher1","flare_launcher2"],
    "memoryPointCMDir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "irTarget": 1,
    "irTargetSize": 0.9,
    "visualTarget": 1,
    "visualTargetSize": 1,
    "radarTarget": 1,
    "radarTargetSize": 1,
    "gearRetracting": 0,
    "availableForSupportTypes": ["Drop","Transport"],
    "cargoCanEject": 1,
    "driverCanEject": 0,
    # Class: CfgVehicles\RHS_UH1_Base\pilotCamera,
    "pilotCamera": {
    },
    "unitInfoType": "RHSUSF_RscUnitInfoAir_UH1Y",
    "unitInfoTypeRTD": "RHSUSF_RscUnitInfoAirRTDFullDigital_UH1Y",
    "weapons": [],
    "magazines": [],
    "selectionHRotorStill": "velka vrtule staticka",
    "selectionHRotorMove": "velka vrtule blur",
    "selectionVRotorStill": "mala vrtule staticka",
    "selectionVRotorMove": "mala vrtule blur",
    "selectionDamage": "trup",
    "selectionShowDamage": "poskozeni",
    "slingLoadMaxCargoMass": 4084,
    "memoryPointLRocket": "l raketa",
    "memoryPointRRocket": "p raketa",
    "memoryPointLMissile": "l strela",
    "memoryPointRMissile": "p strela",
    "GetInAction": "pilot_Heli_Light_02_Enter",
    "GetOutAction": "pilot_Heli_Light_02_Exit",
    "preciseGetInOut": 1,
    "getInRadius": 1.5,
    # Class: CfgVehicles\RHS_UH1_Base\RenderTargets,
    "RenderTargets": {
    },
    # Class: CfgVehicles\RHS_UH1_Base\ViewPilot,
    "ViewPilot": {
        "initFov": 0.75,
        "minFov": 0.3,
        "maxFov": 1.2,
        "initAngleX": -2.5,
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
    "features": "Randomization: No 						<br />Camo selections: 1 - the whole exterior 						<br />Script door sources: None 						<br />Script animations:  None 						<br />Executed scripts: None 						<br />Firing from vehicles: Positions 1, 2 (doors) 						<br />Slingload: Slingloads up to 2000 kg 						<br />Cargo proxy indexes: 1 to 6",
    "_generalMacro": "Heli_light_03_base_F",
    "editorSubcategory": "EdSubcat_Helicopters",
    "hideWeaponsDriver": 1,
    "hideWeaponsGunner": 1,
    "hideWeaponsCargo": 1,
    "cargoCompartments": ["Compartment2"],
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "driveOnComponent": ["Skids"],
    "maximumLoad": 2000,
    "fuelConsumptionRate": 0.103,
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
    "soundDammage": ["A3|Sounds_F|vehicles|crashes|helis|Heli_crash_default_int_1",10,1],
    "soundGetIn": ["A3|Sounds_F|vehicles|air|Heli_Light_03|open",1,1],
    "soundGetOut": ["A3|Sounds_F|vehicles|air|Heli_Light_03|close",1,1,50],
    "soundEngineOnInt": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_start_int",0.398107,1],
    "soundEngineOnExt": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_start_ext",2.51189,1,600],
    "soundEngineOffInt": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_stop_int",0.398107,1],
    "soundEngineOffExt": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_stop_ext",2.51189,1,600],
    "soundLocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",1,1],
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_2",0.316228,1],
    "rotorDamageInt": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_int_open_1",1,1],
    "rotorDamageOut": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_ext_1",2.51189,1,150],
    "rotorDamage": ["rotorDamageInt","rotorDamageOut"],
    "tailDamageInt": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1],
    "tailDamageOut": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1,300],
    "tailDamage": ["tailDamageInt","tailDamageOut"],
    "landingSoundInt0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_small_int1",1,1,100],
    "landingSoundInt1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_small_int2",1,1,100],
    "landingSoundInt": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingSoundOut0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext1",1.77828,1,100],
    "landingSoundOut1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext2",1.77828,1,100],
    "landingSoundOut": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    "slingCargoAttach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEndINT",1,1],
    "slingCargoAttach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookLock",1.77828,1,200],
    "slingCargoAttach": ["slingCargoAttach0","slingCargoAttach1"],
    "slingCargoDetach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEndINT",1,1],
    "slingCargoDetach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookUnlock",1.77828,1,200],
    "slingCargoDetach": ["slingCargoDetach0","slingCargoDetach1"],
    "slingCargoDetachAir0": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_int",1,1],
    "slingCargoDetachAir1": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_ext",1,1,300],
    "slingCargoDetachAir": ["slingCargoDetach0","slingCargoDetach1"],
    "slingCargoRopeBreak0": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_int",1,1],
    "slingCargoRopeBreak1": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_ext",1,1,200],
    "slingCargoRopeBreak": ["slingCargoDetach0","slingCargoDetach1"],
    "gearUpExt": ["A3|Sounds_F|vehicles|air|Heli_Transport_01|gear_up_OUT",1,1,1000],
    "gearUpInt": ["A3|Sounds_F|vehicles|air|Heli_Transport_01|gear_up_IN",1,1,100],
    "gearUp": ["gearUpInt","gearUpExt"],
    "gearDownInt": ["A3|Sounds_F|vehicles|air|Heli_Transport_01|gear_down_IN",1,1,100],
    "gearDownExt": ["A3|Sounds_F|vehicles|air|Heli_Transport_01|gear_down_OUT",1,1,1000],
    "gearDown": ["gearDownInt","gearDownExt"],
    # Class: CfgVehicles\Heli_light_03_base_F\Sounds,
    "Sounds": {
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\EngineExt
        "EngineExt": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_engine_ext",1.77828,1,700],
            "frequency": "rotorSpeed",
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\RotorExt,
        "RotorExt": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_rotor_ext",1.41254,1,1100],
            "frequency": "rotorSpeed * (1-rotorThrust/5)",
            "volume": "camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\RotorNoiseExt,
        "RotorNoiseExt": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Light_03|rotor_swist",1,1,300],
            "frequency": 1,
            "volume": "camPos * (rotorThrust factor [0.7, 0.9])",
            "cone": [0.7,1.3,1,0]
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\EngineInt,
        "EngineInt": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_engine_int",1,1],
            "frequency": "rotorSpeed",
            "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\RotorInt,
        "RotorInt": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_rotor_int",1.77828,1],
            "frequency": "rotorSpeed * (1-rotorThrust/5)",
            "volume": "(1-camPos)*(0 max (rotorSpeed*rotorSpeed-0.1))*(1 + rotorThrust)"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\TransmissionDamageExt_phase1,
        "TransmissionDamageExt_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\TransmissionDamageExt_phase2,
        "TransmissionDamageExt_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\TransmissionDamageInt_phase1,
        "TransmissionDamageInt_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\TransmissionDamageInt_phase2,
        "TransmissionDamageInt_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\damageAlarmInt,
        "damageAlarmInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\damageAlarmExt,
        "damageAlarmExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\rotorLowAlarmInt,
        "rotorLowAlarmInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\rotorLowAlarmExt,
        "rotorLowAlarmExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\scrubLandInt,
        "scrubLandInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandInt_open",1,1,100],
            "frequency": 1,
            "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\scrubLandExt,
        "scrubLandExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubLand factor[0.02, 0.05])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\scrubBuildingInt,
        "scrubBuildingInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingInt",1,1,100],
            "frequency": 1,
            "volume": "2 * (1 - camPos) * (scrubBuilding factor[0.02, 0.05])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\scrubBuildingExt,
        "scrubBuildingExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\scrubTreeInt,
        "scrubTreeInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
            "frequency": 1,
            "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\scrubTreeExt,
        "scrubTreeExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\RainExt,
        "RainExt": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
            "frequency": 1,
            "volume": "camPos * (rain - rotorSpeed/2) * 2"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\RainInt,
        "RainInt": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\SlingLoadDownExt,
        "SlingLoadDownExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1.25893,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\SlingLoadUpExt,
        "SlingLoadUpExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1.25893,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\SlingLoadDownInt,
        "SlingLoadDownInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\SlingLoadUpInt,
        "SlingLoadUpInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\WindInt,
        "WindInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wind_open_int",0.562341,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
        },
        # Class: CfgVehicles\Heli_light_03_base_F\Sounds\GStress,
        "GStress": {
            "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2b",0.354813,1,50],
            "frequency": 1,
            "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
        }
    },
    # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt,
    "SoundsExt": {
        # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\SoundEvents
        "SoundEvents": {
        },
        # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds,
        "Sounds": {
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\EngineExt
            "EngineExt": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_engine_ext",1.77828,1,700],
                "frequency": "rotorSpeed",
                "volume": "camPos*((rotorSpeed-0.72)*4)"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\RotorExt,
            "RotorExt": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_rotor_ext",1.41254,1,1100],
                "frequency": "rotorSpeed * (1-rotorThrust/5)",
                "volume": "camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\RotorNoiseExt,
            "RotorNoiseExt": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Light_03|rotor_swist",1,1,300],
                "frequency": 1,
                "volume": "camPos * (rotorThrust factor [0.7, 0.9])",
                "cone": [0.7,1.3,1,0]
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\EngineInt,
            "EngineInt": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_engine_int",1,1],
                "frequency": "rotorSpeed",
                "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\RotorInt,
            "RotorInt": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Light_03|heli_rotor_int",1.77828,1],
                "frequency": "rotorSpeed * (1-rotorThrust/5)",
                "volume": "(1-camPos)*(0 max (rotorSpeed*rotorSpeed-0.1))*(1 + rotorThrust)"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\TransmissionDamageExt_phase1,
            "TransmissionDamageExt_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\TransmissionDamageExt_phase2,
            "TransmissionDamageExt_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\TransmissionDamageInt_phase1,
            "TransmissionDamageInt_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\TransmissionDamageInt_phase2,
            "TransmissionDamageInt_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\damageAlarmInt,
            "damageAlarmInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\damageAlarmExt,
            "damageAlarmExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\rotorLowAlarmInt,
            "rotorLowAlarmInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\rotorLowAlarmExt,
            "rotorLowAlarmExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\scrubLandInt,
            "scrubLandInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandInt_open",1,1,100],
                "frequency": 1,
                "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\scrubLandExt,
            "scrubLandExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubLandExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubLand factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\scrubBuildingInt,
            "scrubBuildingInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingInt",1,1,100],
                "frequency": 1,
                "volume": "2 * (1 - camPos) * (scrubBuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\scrubBuildingExt,
            "scrubBuildingExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubBuildingExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\scrubTreeInt,
            "scrubTreeInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
                "frequency": 1,
                "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\scrubTreeExt,
            "scrubTreeExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\RainExt,
            "RainExt": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
                "frequency": 1,
                "volume": "camPos * (rain - rotorSpeed/2) * 2"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\RainInt,
            "RainInt": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\SlingLoadDownExt,
            "SlingLoadDownExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\SlingLoadUpExt,
            "SlingLoadUpExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\SlingLoadDownInt,
            "SlingLoadDownInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\SlingLoadUpInt,
            "SlingLoadUpInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\WindInt,
            "WindInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wind_open_int",0.562341,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
            },
            # Class: CfgVehicles\Heli_light_03_base_F\SoundsExt\Sounds\GStress,
            "GStress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2b",0.354813,1,50],
                "frequency": 1,
                "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
            }
        }
    },
    # Class: CfgVehicles\Heli_light_03_base_F\Armory,
    "Armory": {
        "description": "The WY-55 Hellcat is a multi-purpose military helicopter, most suited for a role of anti-surface battlefield utility, which also has a limited transport capacity. It replaces its predecessor the Super Lynx, improving the maneuverability, durability and protection. The armed version is fitted with twin miniguns and unguided rockets."
    },
    "enableManualFire": 0,
    "cost": 700000,
    "armor": 40,
    "damageResistance": 0.00555,
    "irScanRangeMin": 0,
    "irScanRangeMax": 0,
    "irScanToEyeFactor": 1,
    "mainBladeRadius": 6.2,
    "tailBladeRadius": 1.2,
    "maxFordingDepth": 0.7,
    "defaultUserMFDvalues": [0,1,0.3,1],
    "memoryPointGun": ["z_gunL_muzzle","z_gunR_muzzle"],
    "gunBeg": ["z_gunL_muzzle","z_gunR_muzzle"],
    "gunEnd": ["z_gunL_chamber","z_gunR_chamber"],
    "aggregateReflectors": [["Light_1","Light_2"],["Light_3","Light_4"]],
    "memoryPointDriverOptics": "slingCamera",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "washDownStrength": "1.0f",
    "washDownDiameter": "40.0f",
    "minSmokeDamage": 0.3,
    "maxSmokeDamage": 0.99,
    "driverLeftHandAnimName": "lever_pilot",
    "driverRightHandAnimName": "stick_pilot",
    "driverLeftLegAnimName": "pedalL",
    "driverRightLegAnimName": "pedalR",
    "destrType": "DestructWreck",
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
    "dustEffect": "HeliDust",
    "waterEffect": "HeliWater",
    "gearUpTime": 3.33,
    "gearDownTime": 2,
    "gearMinAlt": 0.5,
    # Class: CfgVehicles\Helicopter\CargoSpec,
    "CargoSpec": {
        # Class: CfgVehicles\Helicopter\CargoSpec\Cargo1
        "Cargo1": {
            "showHeadPhones": 1
        },
        # Class: CfgVehicles\Helicopter\CargoSpec\Cargo2,
        "Cargo2": {
            "showHeadPhones": 0
        }
    },
    "startDuration": 20,
    "maxMainRotorDive": 0,
    "maxBackRotorDive": 0,
    "minMainRotorDive": 0,
    "minBackRotorDive": 0,
    "neutralBackRotorDive": 0,
    "neutralMainRotorDive": 0,
    "liftForceCoef": 1,
    "backRotorForceCoef": 1,
    "bodyFrictionCoef": 1,
    "memoryPointPilot": "pilot",
    "_mainBladeCenter": "rotor_center",
    "enableSweep": 1,
    "envelope": [0,0.2,0.9,2.1,2.5,3.3,3.5,3.6,3.7,3.8,3.8,3,0.9,0.7,0.5],
    "minFireTime": 20,
    "steerAheadSimul": 0.5,
    "steerAheadPlan": 0.7,
    # Class: CfgVehicles\Helicopter\ViewOptics,
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
    # Class: CfgVehicles\Helicopter\SpeechVariants,
    "SpeechVariants": {
        # Class: CfgVehicles\Helicopter\SpeechVariants\Default
        "Default": {
            "speechSingular": ["veh_air_helicopter_s"],
            "speechPlural": ["veh_air_helicopter_p"]
        }
    },
    "extCameraParams": [-1],
    "textSingular": "helicopter",
    "textPlural": "helicopters",
    "nameSound": "veh_air_helicopter_s",
    "camouflage": 100,
    "audible": 50,
    "epeImpulseDamageCoef": 50,
    "crewCrashProtection": 0.25,
    "headGforceLeaningFactor": [0.01,0.0025,0.01],
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "damageEffect": "AirDestructionEffects",
    "type": 2,
    "transportMaxBackpacks": 1,
    "supplyRadius": 1.2,
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
    "transportMaxMagazines": 20,
    "transportMaxWeapons": 3,
    "enableGPS": 1,
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
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
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
    # Class: CfgVehicles\AllVehicles\PilotSpec,
    "PilotSpec": {
        "showHeadPhones": 0
    },
    # Class: CfgVehicles\AllVehicles\SoundEvents,
    "SoundEvents": {
    },
    "tracksSpeed": 0,
    "selectionLeftOffset": "",
    "selectionRightOffset": "",
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
    "sensitivity": 2.5,
    "sensitivityEar": 0.0075,
    "portrait": "",
    "ghostPreview": "",
    "armorLights": 0.4,
    "replaceDamaged": "",
    "replaceDamagedLimit": 0.9,
    "replaceDamagedHitpoints": [],
    "keepInEPESceneAfterDeath": 0,
    "extCameraPosition": [0,2,-20],
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
    "memoryPointSupply": "doplnovani",
    "enableWatch": 0,
    "usePreciseGetInAction": 0,
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
    "HeadAimDown": 0,
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