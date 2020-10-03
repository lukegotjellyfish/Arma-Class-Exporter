rhsgref_cdf_b_ural_Zu23 = {
    "author": "Red Hammer Studios",
    "faction": "rhsgref_faction_cdf_ground_b",
    "side": 1,
    "scope": 2,
    "scopeCurator": 2,
    "crew": "rhsgref_cdf_b_reg_rifleman",
    # Class: CfgVehicles\rhsgref_cdf_b_ural_Zu23\Turrets [Indent level: 1],
    "Turrets": {
        # Class: CfgVehicles\rhsgref_cdf_b_ural_Zu23\Turrets\MainTurret [Indent level: 2]
        "MainTurret": {
            "gunnerType": "rhsgref_cdf_b_reg_rifleman",
            "body": "mainTurret",
            "gun": "mainGun",
            "minTurn": -180,
            "maxTurn": 180,
            "initTurn": 0,
            "minElev": -10,
            "maxElev": 85,
            "initElev": 10,
            "weapons": ["rhs_weap_2A14"],
            "magazines": ["RHS_mag_AZP23_100","RHS_mag_AZP23_100","RHS_mag_AZP23_100","RHS_mag_AZP23_100","RHS_mag_AZP23_100","RHS_mag_AZP23_100","RHS_mag_AZP23_100","RHS_mag_AZP23_100","RHS_mag_AZP23_100"],
            "gunnerAction": "RHS_Zu23_Cargo",
            "selectionFireAnim": "zasleh",
            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_pzu5",
            "gunnerOutOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_pzu5",
            "gunnerOpticsEffect": ["OpticsCHAbera1","OpticsBlur2"],
            "gunnerForceOptics": 0,
            "memoryPointGun": ["muzzle_1","muzzle_2"],
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "memorypointgunneroptics": "gunnerview",
            "memoryPointGunnerOutOptics": "gunnerview",
            "gunnerCompartments": "Compartment2",
            "gunnerGetInAction": "GetInHemttBack",
            "gunnerGetOutAction": "GetOutHighZamak",
            "turretInfoType": "RHS_RscWeaponZeroing",
            "stabilizedInAxes": 0,
            "outGunnerMayFire": 1,
            "inGunnerMayFire": 1,
            "startEngine": 0,
            "canUseScanners": 0,
            "allowTabLock": 0,
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\MainTurret\ViewGunner [Indent level: 3],
            "ViewGunner": {
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
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\MainTurret\ViewOptics [Indent level: 3],
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.093,
                "minFov": 0.093,
                "maxFov": 0.093
            },
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\MainTurret\OpticsIn [Indent level: 3],
            "OpticsIn": {
                # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\MainTurret\OpticsIn\Wide [Indent level: 4]
                "Wide": {
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_pzu5",
                    "gunnerOpticsEffect": ["TankGunnerOptics2","OpticsBlur1","OpticsCHAbera3"],
                    "gunnerOutOpticsEffect": ["TankGunnerOptics2","OpticsBlur1","OpticsCHAbera3"],
                    "visionMode": ["Normal"],
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "initFov": 0.093,
                    "minFov": 0.093,
                    "maxFov": 0.093
                }
            },
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\MainTurret\TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[85,-180],[85,180]],
                "limitsArrayBottom": [[-10,-180],[-8,-35.6867],[9.3683,-32.6867],[10,0],[9.7173,32.6372],[-8,36.6867],"",[-10,134],[-6,134.5],[-6,178],[-10,180]]
            },
            "soundAttenuationTurret": "HeliAttenuationRamp",
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\MainTurret\Hitpoints [Indent level: 3],
            "Hitpoints": {
                # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\MainTurret\Hitpoints\HitTurret [Indent level: 4]
                "HitTurret": {
                    "armor": -40,
                    "material": -1,
                    "name": "Hit_Turret",
                    "armorComponent": "Hit_Turret",
                    "visual": "vez",
                    "passThrough": 0,
                    "minimalHit": 0.01,
                    "explosionShielding": 0.009,
                    "radius": 0.15
                },
                # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\MainTurret\Hitpoints\HitGun [Indent level: 4],
                "HitGun": {
                    "armor": -30,
                    "material": -1,
                    "name": "Hit_Gun",
                    "armorComponent": "Hit_Gun",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": 0.01,
                    "explosionShielding": 0.001,
                    "radius": 0.12
                }
            },
            "disableSoundAttenuation": 0,
            "animationSourceBody": "mainTurret",
            "animationSourceGun": "mainGun",
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerName": "Gunner",
            "primaryGunner": 1,
            "primaryObserver": 0,
            "soundServo": ["",0.00316228,1],
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
            "commanding": 1,
            "turretCanSee": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOpticsShowCursor": 0,
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOutOpticsEffect": [],
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
            "isCopilot": 0,
            "canEject": 1,
            "gunnerLeftHandAnimName": "",
            "gunnerRightHandAnimName": "",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "gunnerDoor": "",
            "preciseGetInOut": 0,
            "turretFollowFreeLook": 0,
            "showAllTargets": 0,
            "dontCreateAI": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
            "TurnOut": {
                "turnOffset": 0
            },
            "gunnerInAction": "ManActTestDriver",
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\rhsgref_cdf_b_ural_Zu23\Turrets\CargoTurret_01 [Indent level: 2],
        "CargoTurret_01": {
            "gunnerType": "rhsgref_cdf_b_reg_officer",
            "gunnerAction": "vehicle_coshooter_1",
            "gunnerGetInAction": "GetInHemttBack",
            "gunnerGetOutAction": "GetOutHighZamak",
            "memoryPointsGetInGunner": "pos cargo",
            "memoryPointsGetInGunnerDir": "pos cargo dir",
            "gunnerName": "Commander",
            "primaryObserver": 1,
            "dontCreateAI": 0,
            "commanding": 4,
            "gunnerCompartments": "Compartment2",
            "proxyIndex": 3,
            "maxElev": 45,
            "minElev": -15,
            "maxTurn": 84,
            "minTurn": -65,
            "gunnerUsesPilotView": 1,
            "memorypointgunneroptics": "",
            "selectionFireAnim": "",
            "isPersonTurret": 1,
            "playerPosition": 2,
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
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
            "gunnerDoor": "",
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
            "showCrewAim": 0
        },
        # Class: CfgVehicles\rhsgref_cdf_b_ural_Zu23\Turrets\CargoTurret_02 [Indent level: 2],
        "CargoTurret_02": {
            "playerPosition": 1,
            "commanding": 2,
            "primaryObserver": 0,
            "gunnerName": "Passenger (front)",
            "proxyIndex": 4,
            "isPersonTurret": 2,
            "gunnerAction": "passenger_flatground_4_vehicle_passenger_stand_1",
            "gunnerInAction": "vehicle_passenger_stand_1_passenger_flatground_4",
            "animationSourceHatch": "gunner_rf_turn",
            "allowLauncherOut": 1,
            "canHideGunner": 1,
            "dontCreateAI": 1,
            "memoryPointsGetInGunner": "pos cargo LR",
            "memoryPointsGetInGunnerDir": "pos cargo LR dir",
            "minElev": -45,
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\CargoTurret_02\TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[45,-65],[45,84]],
                "limitsArrayBottom": [[-7,-65],[-7,-45.6867],[-2,-35.6867],[5,-22.6867],[5,-12.6867],[-3,-8.6867],[-3,2.6867],[-7,14],[4,44],[4,64],[-7,74]]
            },
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\CargoTurret_02\TurnOut [Indent level: 3],
            "TurnOut": {
                "limitsArrayTop": [[45,-180],[45,180]],
                "limitsArrayBottom": [[-45,-65],[-42,-45.6867],[-34,-22.6867],[-12,12.6867],[-8,44],[-11,74],[-25,84]],
                "turnOffset": -180
            },
            "gunnerGetInAction": "GetInHemttBack",
            "gunnerGetOutAction": "GetOutHighZamak",
            "gunnerCompartments": "Compartment2",
            "maxElev": 45,
            "maxTurn": 84,
            "minTurn": -65,
            "gunnerUsesPilotView": 1,
            "memorypointgunneroptics": "",
            "selectionFireAnim": "",
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
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
            "animationSourceCamElev": "camElev",
            "gunnerType": "",
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
            "castGunnerShadow": 0,
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
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
            "gunnerDoor": "",
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "allowLauncherIn": 0,
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\rhsgref_cdf_b_ural_Zu23\Turrets\CargoTurret_03 [Indent level: 2],
        "CargoTurret_03": {
            "isPersonTurret": 1,
            "canHideGunner": 0,
            "gunnerName": "Passenger (rear)",
            "allowLauncherOut": 0,
            "proxyIndex": 5,
            "gunnerAction": "passenger_flatground_2",
            "animationSourceHatch": "",
            "memoryPointsGetInGunner": "pos cargo RR",
            "memoryPointsGetInGunnerDir": "pos cargo RR dir",
            "minTurn": -65,
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\CargoTurret_03\TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[45,-65],[45,84]],
                "limitsArrayBottom": [[-4,-65],[-8,-45.6867],[-15,-22.6867],[-11,24],[-12,84]]
            },
            "playerPosition": 1,
            "commanding": 2,
            "primaryObserver": 0,
            "gunnerInAction": "vehicle_passenger_stand_1_passenger_flatground_4",
            "dontCreateAI": 1,
            "minElev": -45,
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\CargoTurret_02\TurnOut [Indent level: 3],
            "TurnOut": {
                "limitsArrayTop": [[45,-180],[45,180]],
                "limitsArrayBottom": [[-45,-65],[-42,-45.6867],[-34,-22.6867],[-12,12.6867],[-8,44],[-11,74],[-25,84]],
                "turnOffset": -180
            },
            "gunnerGetInAction": "GetInHemttBack",
            "gunnerGetOutAction": "GetOutHighZamak",
            "gunnerCompartments": "Compartment2",
            "maxElev": 45,
            "maxTurn": 84,
            "gunnerUsesPilotView": 1,
            "memorypointgunneroptics": "",
            "selectionFireAnim": "",
            "soundAttenuationTurret": "HeliAttenuationRamp",
            "disableSoundAttenuation": 0,
            # Class: CfgVehicles\RHS_Ural_Zu23_Base\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
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
            "animationSourceCamElev": "camElev",
            "gunnerType": "",
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
            "castGunnerShadow": 0,
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
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
            "gunnerDoor": "",
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "allowLauncherIn": 0,
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        }
    },
    "editorPreview": "rhsgref|addons|rhsgref_editorPreviews|data|rhsgref_cdf_ural_Zu23.paa",
    "dlc": "RHS_GREF",
    "rhs_decalParameters": ["['Number', cDecals4CarsNumberPlaces, 'CDF']"],
    "accuracy": 0.5,
    "typicalCargo": ["rhsgref_cdf_reg_rifleman_lite"],
    "hiddenSelectionsTextures": ["rhsafrf|addons|rhs_a2port_car|ural|data|ural_kabina_camo_co.paa","rhsafrf|addons|rhs_a2port_car|ural|data|ural_open_cdf_co.paa"],
    "displayName": "Ural-4320 (ZU-23-2)",
    "transportSoldier": 2,
    "model": "rhsafrf|addons|rhs_a2port_car|Ural|ural_zu23.p3d",
    "icon": "rhsafrf|addons|rhs_a2port_car|data|mapico|icomap_URAL_zu23_CA.paa",
    "picture": "rhsafrf|addons|rhs_a2port_car|data|ico|rhs_ural4320_zu23_pic_ca.paa",
    "mapsize": 8,
    "unitInfoType": "RscUnitInfo",
    "threat": [0.6,0.1,0.6],
    # Class: CfgVehicles\RHS_Ural_Zu23_Base\AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles\RHS_Ural_Zu23_Base\AnimationSources\muzzle_source [Indent level: 2]
        "muzzle_source": {
            "source": "reload",
            "weapon": "rhs_weap_2A14"
        },
        # Class: CfgVehicles\RHS_Ural_Zu23_Base\AnimationSources\fire_anim [Indent level: 2],
        "fire_anim": {
            "source": "revolving",
            "weapon": "rhs_weap_2A14"
        },
        # Class: CfgVehicles\RHS_Ural_Zu23_Base\AnimationSources\muzzleHMG_ROT [Indent level: 2],
        "muzzleHMG_ROT": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2A14"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\Door_LF [Indent level: 2],
        "Door_LF": {
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_Ural_Door",
            "soundPosition": "osa_dvere_lp"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\Door_RF [Indent level: 2],
        "Door_RF": {
            "soundPosition": "osa_dvere_pp",
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_Ural_Door"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\gearbox [Indent level: 2],
        "gearbox": {
            "sound": "RHS_gearbox",
            "soundPosition": "gear_axis",
            "source": "door",
            "animPeriod": 0.8
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\HitSpare [Indent level: 2],
        "HitSpare": {
            "source": "Hit",
            "hitpoint": "HitSpare",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\UseSpare [Indent level: 2],
        "UseSpare": {
            "hitpoint": "UseSpare",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\spare_hide [Indent level: 2],
        "spare_hide": {
            "mass": 1,
            "source": "user",
            "useSource": 1,
            "displayName": "hide spare wheel",
            "animPeriod": 0.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\bench_hide [Indent level: 2],
        "bench_hide": {
            "displayName": "hide cargo bench",
            "lockCargo": [3,4,5,6,7,8,9,10,11,12,23,24],
            "lockCargoAnimationPhase": 1,
            "mass": 1,
            "source": "user",
            "useSource": 1,
            "animPeriod": 0.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\people_tag_hide [Indent level: 2],
        "people_tag_hide": {
            "displayName": "hide cargo label",
            "mass": 1,
            "source": "user",
            "useSource": 1,
            "animPeriod": 0.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\rear_numplate_hide [Indent level: 2],
        "rear_numplate_hide": {
            "displayName": "hide rear registration numbers",
            "initPhase": 1,
            "mass": 1,
            "source": "user",
            "useSource": 1,
            "animPeriod": 0.1
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\light_hide [Indent level: 2],
        "light_hide": {
            "displayName": "hide light covers",
            "mass": 1,
            "source": "user",
            "useSource": 1,
            "animPeriod": 0.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\longlights_hide [Indent level: 2],
        "longlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\shortlights_hide [Indent level: 2],
        "shortlights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\lights_hide [Indent level: 2],
        "lights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\searchlight_hide [Indent level: 2],
        "searchlight_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\AnimationSources\searchlight_rot [Indent level: 2],
        "searchlight_rot": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitLFWheel [Indent level: 2],
        "HitLFWheel": {
            "source": "Hit",
            "hitpoint": "HitLFWheel",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitRFWheel [Indent level: 2],
        "HitRFWheel": {
            "hitpoint": "HitRFWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitLBWheel [Indent level: 2],
        "HitLBWheel": {
            "hitpoint": "HitLF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitRBWheel [Indent level: 2],
        "HitRBWheel": {
            "hitpoint": "HitRF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitLF2Wheel [Indent level: 2],
        "HitLF2Wheel": {
            "hitpoint": "HitLBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitRF2Wheel [Indent level: 2],
        "HitRF2Wheel": {
            "hitpoint": "HitRBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitLMWheel [Indent level: 2],
        "HitLMWheel": {
            "hitpoint": "HitLMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitRMWheel [Indent level: 2],
        "HitRMWheel": {
            "hitpoint": "HitRMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass3 [Indent level: 2],
        "HitGlass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass4 [Indent level: 2],
        "HitGlass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass5 [Indent level: 2],
        "HitGlass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass6 [Indent level: 2],
        "HitGlass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit",
            "raw": 1
        }
    },
    # Class: CfgVehicles\RHS_Ural_Zu23_Base\Damage [Indent level: 1],
    "Damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_tigr|data|glass.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_int.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23_damage.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23_destruct.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23_base.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23_base_damage.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23_base_destruct.rvmat","rhsafrf|addons|rhs_a2port_car|Ural|Data|ural_kabina.rvmat","rhsafrf|addons|rhs_a2port_car|Ural|Data|ural_kabina_damage.rvmat","rhsafrf|addons|rhs_a2port_car|Ural|Data|ural_kabina_destruct.rvmat","rhsafrf|addons|rhs_a2port_car|Ural|Data|ural_open.rvmat","rhsafrf|addons|rhs_a2port_car|Ural|Data|ural_open_damage.rvmat","rhsafrf|addons|rhs_a2port_car|Ural|Data|ural_open_destruct.rvmat","rhsafrf|addons|rhs_a2port_car|Ural|Data|ural_interier.rvmat","rhsafrf|addons|rhs_a2port_car|Ural|Data|ural_interier_damage.rvmat","rhsafrf|addons|rhs_a2port_car|Ural|Data|ural_interier_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles\RHS_Ural_Zu23_Base\textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles\RHS_Ural_Zu23_Base\textureSources\standard [Indent level: 2]
        "standard": {
            "displayName": "Khaki",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_a2port_car|ural|data|ural_kabina_khk_co.paa","rhsafrf|addons|rhs_a2port_car|ural|data|ural_open_co.paa"],
            "factions": ["rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles\RHS_Ural_Zu23_Base\textureSources\Camo [Indent level: 2],
        "Camo": {
            "displayName": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_a2port_car|ural|data|ural_kabina_camo_co.paa","rhsafrf|addons|rhs_a2port_car|ural|data|ural_open_cdf_co.paa"],
            "factions": ["rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles\RHS_Ural_Zu23_Base\textureSources\Camo1 [Indent level: 2],
        "Camo1": {
            "displayName": "Takistan",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_a2port_car|ural|data|ural_kabina_tka_co.paa","rhsafrf|addons|rhs_a2port_car|ural|data|ural_open_tka_co.paa"],
            "factions": ["rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles\RHS_Ural_Zu23_Base\textureSources\Camo2 [Indent level: 2],
        "Camo2": {
            "displayName": "Chedaki",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_a2port_car|ural|data|ural_kabina_co.paa","rhsafrf|addons|rhs_a2port_car|ural|data|ural_open_chdkz_co.paa"],
            "factions": ["rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        }
    },
    "textureList": [],
    "category": "Car",
    "insideSoundCoef": 0.2,
    "tf_hasLRradio_api": 0,
    "viewDriverInExternal": 1,
    "hiddenSelections": ["camo1","camo2","n1","n2","n3","n4","i1","i2","i3","i4"],
    # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\ObjectTexture [Indent level: 2]
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber_type [Indent level: 2],
        "rhs_decalNumber_type": {
            "displayName": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cDecals4CarsNumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber_type\values\Default [Indent level: 4]
                "Default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultValue": "Default"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber_type\values\DefaultRed [Indent level: 4],
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber_type\values\BoldRed [Indent level: 4],
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber_type\values\CDF [Indent level: 4],
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber_type\values\Handpaint [Indent level: 4],
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber_type\values\HandpaintBlack [Indent level: 4],
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber_type\values\Iraqi [Indent level: 4],
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber_type\values\LicensePlate [Indent level: 4],
                "LicensePlate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalNumber [Indent level: 2],
        "rhs_decalNumber": {
            "collapsed": 1,
            "displayName": "Set plate number",
            "tooltip": "Set plate number. 4 numbers are required. If 0, random number will be generated",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typeName": "Number",
            "defaultValue": "-1",
            "expression": "if( _value >= 0)then{[_this,[['Number', cDecals4CarsNumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value]]] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type [Indent level: 2],
        "rhs_decalArmy_type": {
            "displayName": "Define large door roundel type",
            "tooltip": "Decal type",
            "property": "rhs_decalArmy_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "typeName": "STRING",
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\Army [Indent level: 4]
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "Army"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\Honor [Indent level: 4],
                "Honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\HonorGDR [Indent level: 4],
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\Platoon [Indent level: 4],
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\PlatoonGDR [Indent level: 4],
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\PlatoonVDV [Indent level: 4],
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy [Indent level: 2],
        "rhs_decalArmy": {
            "displayName": "Set large door roundel symbol",
            "tooltip": "Set large door roundel located on both sides. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalArmy",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cDecalsCarsRightArmyPlaces,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalPlatoon_type [Indent level: 2],
        "rhs_decalPlatoon_type": {
            "displayName": "Define small door roundel type",
            "property": "rhs_decalPlatoon_type",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "tooltip": "Decal type",
            "control": "Combo",
            "typeName": "STRING",
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\Army [Indent level: 4]
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "Army"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\Honor [Indent level: 4],
                "Honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\HonorGDR [Indent level: 4],
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\Platoon [Indent level: 4],
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\PlatoonGDR [Indent level: 4],
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalArmy_type\values\PlatoonVDV [Indent level: 4],
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_decalPlatoon [Indent level: 2],
        "rhs_decalPlatoon": {
            "displayName": "Set small door roundel symbol",
            "tooltip": "Define small door roundel located on both sides. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cDecalsCarsRightPlatoonPlaces,  _this getVariable ['rhs_decalPlatoon_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_hideLightCover [Indent level: 2],
        "rhs_hideLightCover": {
            "displayName": "Hide light covers",
            "property": "rhs_hideLightCover",
            "control": "CheckboxNumber",
            "expression": "_this animate ['light_hide',_value,true]",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\rhs_hidespare [Indent level: 2],
        "rhs_hidespare": {
            "displayName": "Remove spare wheel",
            "property": "rhs_hidespare",
            "expression": "_this animate ['spare_hide',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\Door_LF [Indent level: 2],
        "Door_LF": {
            "displayName": "Open front left door",
            "property": "Door_LF",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Attributes\Door_RF [Indent level: 2],
        "Door_RF": {
            "displayName": "Open front right door",
            "property": "Door_RF",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        }
    },
    "driverAction": "RHS_URAL_driver",
    "driverInAction": "RHS_URAL_driver",
    "soundAttenuationCargo": [1,1,0.3],
    "cost": 50000,
    "transportMaxBackpacks": 6,
    "vehicleClass": "rhs_vehclass_truck",
    "editorSubcategory": "rhs_EdSubcat_truck",
    "driverLeftHandAnimName": "drivewheel",
    "driverRightHandAnimName": "shift",
    "driverRightLegAnimName": "pedalR",
    "driverLeftLegAnimName": "pedalL",
    "weapons": ["TruckHorn3"],
    "supplyRadius": 5.5,
    "soundGear": ["rhsafrf|addons|rhs_a2port_car|sounds|Gear_Change",2,1],
    "soundGetIn": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_int_getout",1.77828,1,9],
    "soundGetOut": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_ext_getout",2.51189,1,25],
    "soundEngineOnInt": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_int_start",1.41254,1],
    "soundEngineOnExt": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_ext_start",1.41254,1,200],
    "soundEngineOffInt": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_int_stop",1.41254,1],
    "soundEngineOffExt": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_ext_stop",1.41254,1,200],
    # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds [Indent level: 1],
    "Sounds": {
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Idle_ext [Indent level: 2]
        "Idle_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|ext-ural-idle",1.58489,1,150],
            "frequency": "0.9	+	((rpm/	4000) factor[(200/	4000),(950/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(100/	4000),(300/	4000)])	*	((rpm/	4000) factor[(800/	4000),(500/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine [Indent level: 2],
        "Engine": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|ext-ural-acceleration",1.41254,1,200],
            "frequency": "0.8	+	((rpm/	4000) factor[(800/	4000),(1300/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(650/	4000),(750/	4000)])	*	((rpm/	4000) factor[(900/	4000),(800/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine1_ext [Indent level: 2],
        "Engine1_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|ext-ural-low",1.25893,1,240],
            "frequency": "0.8	+	((rpm/	4000) factor[(1200/	4000),(1600/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(850/	4000),(950/	4000)])	*	((rpm/	4000) factor[(1400/	4000),(1200/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine2_ext [Indent level: 2],
        "Engine2_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|ext-ural-high",1.25893,1,280],
            "frequency": "0.8	+	((rpm/	4000) factor[(1400/	4000),(2100/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(1200/	4000),(1350/	4000)])	*	((rpm/	4000) factor[(1800/	4000),(1400/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine3_ext [Indent level: 2],
        "Engine3_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|ext-ural-high",1.12202,1,320],
            "frequency": "0.8	+	((rpm/	4000) factor[(1300/	4000),(2900/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(1450/	4000),(1650/	4000)])	*	((rpm/	4000) factor[(2670/	4000),(2200/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine4_ext [Indent level: 2],
        "Engine4_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|ext-ural-high",1.12202,1,360],
            "frequency": "0.8	+	((rpm/	4000) factor[(2200/	4000),(4200/	4000)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	4000) factor[(2350/	4000),(2800/	4000)])	*	((rpm/	4000) factor[(3150/	4000),(3050/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine5_ext [Indent level: 2],
        "Engine5_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|ext-ural-high",1.12202,1,420],
            "frequency": "0.95	+	((rpm/	4000) factor[(3100/	4000),(4900/	4000)])*0.15",
            "volume": "engineOn*camPos*((rpm/	4000) factor[(3100/	4000),(4100/	4000)])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\IdleThrust [Indent level: 2],
        "IdleThrust": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_idle_exhaust",1.12202,1,200],
            "frequency": "0.9	+	((rpm/	4000) factor[(200/	4000),(950/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(100/	4000),(300/	4000)])	*	((rpm/	4000) factor[(800/	4000),(500/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\EngineThrust [Indent level: 2],
        "EngineThrust": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_low1_exhaust",1.12202,1,250],
            "frequency": "0.8	+	((rpm/	4000) factor[(800/	4000),(1300/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(650/	4000),(750/	4000)])	*	((rpm/	4000) factor[(900/	4000),(800/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine1_Thrust_ext [Indent level: 2],
        "Engine1_Thrust_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_low1_exhaust",1.12202,1,280],
            "frequency": "0.8	+	((rpm/	4000) factor[(1200/	4000),(1600/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(850/	4000),(950/	4000)])	*	((rpm/	4000) factor[(1400/	4000),(1200/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine2_Thrust_ext [Indent level: 2],
        "Engine2_Thrust_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1_exhaust",1,1,320],
            "frequency": "0.8	+	((rpm/	4000) factor[(1400/	4000),(2100/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(1200/	4000),(1350/	4000)])	*	((rpm/	4000) factor[(1800/	4000),(1400/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine3_Thrust_ext [Indent level: 2],
        "Engine3_Thrust_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1_exhaust",1,1,360],
            "frequency": "0.8	+	((rpm/	4000) factor[(1300/	4000),(2900/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(1450/	4000),(1650/	4000)])	*	((rpm/	4000) factor[(2670/	4000),(2200/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine4_Thrust_ext [Indent level: 2],
        "Engine4_Thrust_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1_exhaust",1,1,400],
            "frequency": "0.8	+	((rpm/	4000) factor[(2200/	4000),(4200/	4000)])*0.3",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(2350/	4000),(2800/	4000)])	*	((rpm/	4000) factor[(3150/	4000),(3050/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine5_Thrust_ext [Indent level: 2],
        "Engine5_Thrust_ext": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_ext_high1_exhaust",1.25893,1,450],
            "frequency": "0.9	+	((rpm/	4000) factor[(3100/	4000),(4900/	4000)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	4000) factor[(3100/	4000),(4100/	4000)])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Idle_int [Indent level: 2],
        "Idle_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|int-ural-idle",1.41254,1],
            "frequency": "0.9	+	((rpm/	4000) factor[(200/	4000),(950/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(100/	4000),(300/	4000)])	*	((rpm/	4000) factor[(800/	4000),(500/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine_int [Indent level: 2],
        "Engine_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|int-ural-acceleration",1.41254,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(800/	4000),(1300/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(650/	4000),(750/	4000)])	*	((rpm/	4000) factor[(900/	4000),(800/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine1_int [Indent level: 2],
        "Engine1_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|int-ural-low",1.25893,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(1200/	4000),(1600/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(850/	4000),(950/	4000)])	*	((rpm/	4000) factor[(1400/	4000),(1200/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine2_int [Indent level: 2],
        "Engine2_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|int-ural-high",1.25893,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(1400/	4000),(2100/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(1200/	4000),(1350/	4000)])	*	((rpm/	4000) factor[(1800/	4000),(1400/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine3_int [Indent level: 2],
        "Engine3_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|int-ural-high",1.25893,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(1300/	4000),(2900/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(1450/	4000),(1650/	4000)])	*	((rpm/	4000) factor[(2670/	4000),(2200/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine4_int [Indent level: 2],
        "Engine4_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|int-ural-high",1.25893,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(2200/	4000),(4200/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	4000) factor[(2350/	4000),(2800/	4000)])	*	((rpm/	4000) factor[(3150/	4000),(3050/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine5_int [Indent level: 2],
        "Engine5_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|URAL|int-ural-high",1.25893,1],
            "frequency": "0.95	+	((rpm/	4000) factor[(3100/	4000),(4900/	4000)])*0.15",
            "volume": "engineOn*(1-camPos)*((rpm/	4000) factor[(3100/	4000),(4100/	4000)])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\IdleThrust_int [Indent level: 2],
        "IdleThrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_idle_exhaust",1.41254,1],
            "frequency": "0.9	+	((rpm/	4000) factor[(200/	4000),(950/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(100/	4000),(300/	4000)])	*	((rpm/	4000) factor[(800/	4000),(500/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\EngineThrust_int [Indent level: 2],
        "EngineThrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_low1_exhaust",1.25893,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(800/	4000),(1300/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(650/	4000),(750/	4000)])	*	((rpm/	4000) factor[(900/	4000),(800/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine1_Thrust_int [Indent level: 2],
        "Engine1_Thrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_low1_exhaust",1.25893,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(1200/	4000),(1600/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(850/	4000),(950/	4000)])	*	((rpm/	4000) factor[(1400/	4000),(1200/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine2_Thrust_int [Indent level: 2],
        "Engine2_Thrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1_exhaust",1.12202,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(1400/	4000),(2100/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(1200/	4000),(1350/	4000)])	*	((rpm/	4000) factor[(1800/	4000),(1400/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine3_Thrust_int [Indent level: 2],
        "Engine3_Thrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1_exhaust",1.12202,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(1300/	4000),(2900/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(1450/	4000),(1650/	4000)])	*	((rpm/	4000) factor[(2670/	4000),(2200/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine4_Thrust_int [Indent level: 2],
        "Engine4_Thrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1_exhaust",1.12202,1],
            "frequency": "0.8	+	((rpm/	4000) factor[(2200/	4000),(4200/	4000)])*0.3",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	4000) factor[(2350/	4000),(2800/	4000)])	*	((rpm/	4000) factor[(3150/	4000),(3050/	4000)]))"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Engine5_Thrust_int [Indent level: 2],
        "Engine5_Thrust_int": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|UAZ|uaz_int_high1_exhaust",1.12202,1],
            "frequency": "0.9	+	((rpm/	4000) factor[(3100/	4000),(4900/	4000)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	4000) factor[(3100/	4000),(4100/	4000)])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\Movement [Indent level: 2],
        "Movement": {
            "sound": "soundEnviron",
            "frequency": "1",
            "volume": "0"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\RainIn [Indent level: 2],
        "RainIn": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|rain.wss",1.41254,1],
            "frequency": 1,
            "volume": "rain*(1-camPos)"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\RainExt [Indent level: 2],
        "RainExt": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|rain.wss",1.41254,1],
            "frequency": 1,
            "volume": "rain*camPos"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresRockOut [Indent level: 2],
        "TiresRockOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_1",1.12202,1,60],
            "frequency": "1",
            "volume": "camPos*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresSandOut [Indent level: 2],
        "TiresSandOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-sand1",1.12202,1,60],
            "frequency": "1",
            "volume": "camPos*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresGrassOut [Indent level: 2],
        "TiresGrassOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_2",1.12202,1,60],
            "frequency": "1",
            "volume": "camPos*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresMudOut [Indent level: 2],
        "TiresMudOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-mud2",1.12202,1,60],
            "frequency": "1",
            "volume": "camPos*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresGravelOut [Indent level: 2],
        "TiresGravelOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_gravel_1",1.12202,1,60],
            "frequency": "1",
            "volume": "camPos*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresAsphaltOut [Indent level: 2],
        "TiresAsphaltOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_asfalt_2",1.12202,1,60],
            "frequency": "1",
            "volume": "camPos*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\NoiseOut [Indent level: 2],
        "NoiseOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_ext_car_3",1,1,90],
            "frequency": "1",
            "volume": "camPos*(damper0 max 0.02)*(speed factor[0, 8])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresRockIn [Indent level: 2],
        "TiresRockIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_1",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresSandIn [Indent level: 2],
        "TiresSandIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-sand2",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresGrassIn [Indent level: 2],
        "TiresGrassIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_2",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresMudIn [Indent level: 2],
        "TiresMudIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-mud2",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresGravelIn [Indent level: 2],
        "TiresGravelIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_gravel_1",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\TiresAsphaltIn [Indent level: 2],
        "TiresAsphaltIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_asfalt_2",1.12202,1],
            "frequency": "1",
            "volume": "(1-camPos)*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\NoiseIn [Indent level: 2],
        "NoiseIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_int_car_3",1,1],
            "frequency": "1",
            "volume": "(damper0 max 0.1)*(speed factor[0, 8])*(1-camPos)"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\breaking_ext_road [Indent level: 2],
        "breaking_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04",1.41254,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\acceleration_ext_road [Indent level: 2],
        "acceleration_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1.41254,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 2])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\turn_left_ext_road [Indent level: 2],
        "turn_left_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1.41254,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\turn_right_ext_road [Indent level: 2],
        "turn_right_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",1.41254,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\breaking_ext_dirt [Indent level: 2],
        "breaking_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_14_dirt_breaking",1.41254,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[1, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\acceleration_ext_dirt [Indent level: 2],
        "acceleration_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_16_dirt_acceleration",1.41254,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 1])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\turn_left_ext_dirt [Indent level: 2],
        "turn_left_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt",1.41254,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[1, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\turn_right_ext_dirt [Indent level: 2],
        "turn_right_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt",1.41254,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[1, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\breaking_int_road [Indent level: 2],
        "breaking_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\acceleration_int_road [Indent level: 2],
        "acceleration_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 2])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\turn_left_int_road [Indent level: 2],
        "turn_left_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\turn_right_int_road [Indent level: 2],
        "turn_right_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\breaking_int_dirt [Indent level: 2],
        "breaking_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_14_dirt_breaking_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\acceleration_int_dirt [Indent level: 2],
        "acceleration_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_16_dirt_acceleration_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[0.1, 0.4])*(Speed Factor[15, 2])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\turn_left_int_dirt [Indent level: 2],
        "turn_left_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[0.1, 0.4])*(Speed Factor[2, 15])"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Sounds\turn_right_int_dirt [Indent level: 2],
        "turn_right_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt_int",3.16228,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[-0.1, -0.4])*(Speed Factor[2, 15])"
        },
        "soundSetsInt": ["RHS_ural4320_Engine_RPM0_INT_SoundSet","RHS_ural4320_Engine_RPM1_INT_SoundSet","RHS_ural4320_Engine_RPM2_INT_SoundSet","RHS_ural4320_Engine_INT_Burst_SoundSet","ural4320_Rattling_INT_SoundSet","ural4320_Stress_INT_SoundSet","ural4320_Rain_INT_SoundSet","RHS_ural4320_Tires_Rock_Fast_INT_SoundSet","RHS_ural4320_Tires_Grass_Fast_INT_SoundSet","RHS_ural4320_Tires_Sand_Fast_INT_SoundSet","RHS_ural4320_Tires_Gravel_Fast_INT_SoundSet","RHS_ural4320_Tires_Mud_Fast_INT_SoundSet","RHS_ural4320_Tires_Asphalt_Fast_INT_SoundSet","RHS_ural4320_Tires_Water_Fast_INT_SoundSet","RHS_ural4320_Tires_Rock_Slow_INT_SoundSet","RHS_ural4320_Tires_Grass_Slow_INT_SoundSet","RHS_ural4320_Tires_Sand_Slow_INT_SoundSet","RHS_ural4320_Tires_Gravel_Slow_INT_SoundSet","RHS_ural4320_Tires_Mud_Slow_INT_SoundSet","RHS_ural4320_Tires_Asphalt_Slow_INT_SoundSet","RHS_ural4320_Tires_Water_Slow_INT_SoundSet","RHS_ural4320_Tires_Turn_Hard_INT_SoundSet","RHS_ural4320_Tires_Turn_Soft_INT_SoundSet","RHS_ural4320_Tires_Brake_Hard_INT_SoundSet","RHS_ural4320_Tires_Brake_Soft_INT_SoundSet"],
        "soundSetsExt": ["RHS_ural4320_Engine_RPM0_EXT_SoundSet","RHS_ural4320_Engine_RPM1_EXT_SoundSet","RHS_ural4320_Engine_RPM2_EXT_SoundSet","RHS_ural4320_Engine_EXT_Burst_SoundSet","ural4320_Rattling_EXT_SoundSet","ural4320_Stress_EXT_SoundSet","ural4320_Rain_EXT_SoundSet","RHS_ural4320_Tires_Rock_Fast_EXT_SoundSet","RHS_ural4320_Tires_Grass_Fast_EXT_SoundSet","RHS_ural4320_Tires_Sand_Fast_EXT_SoundSet","RHS_ural4320_Tires_Gravel_Fast_EXT_SoundSet","RHS_ural4320_Tires_Mud_Fast_EXT_SoundSet","RHS_ural4320_Tires_Asphalt_Fast_EXT_SoundSet","RHS_ural4320_Tires_Water_Fast_EXT_SoundSet","RHS_ural4320_Tires_Rock_Slow_EXT_SoundSet","RHS_ural4320_Tires_Grass_Slow_EXT_SoundSet","RHS_ural4320_Tires_Sand_Slow_EXT_SoundSet","RHS_ural4320_Tires_Gravel_Slow_EXT_SoundSet","RHS_ural4320_Tires_Mud_Slow_EXT_SoundSet","RHS_ural4320_Tires_Asphalt_Slow_EXT_SoundSet","RHS_ural4320_Tires_Water_Slow_EXT_SoundSet","RHS_ural4320_Tires_Turn_Hard_EXT_SoundSet","RHS_ural4320_Tires_Turn_Soft_EXT_SoundSet","RHS_ural4320_Tires_Brake_Hard_EXT_SoundSet","RHS_ural4320_Tires_Brake_Soft_EXT_SoundSet"]
    },
    "memoryPointsGetInCargo": ["pos codriver","pos codriver","pos cargo"],
    "memoryPointsGetInCargoDir": ["pos codriver dir","pos codriver dir","pos cargo dir"],
    "driverDoor": "Door_LF",
    "cargoDoors": ["Door_RF","Door_RF",""],
    "driverCompartments": "Compartment1",
    "cargoCompartments": ["Compartment1","Compartment1","Compartment2","Compartment2","Compartment2","Compartment2"],
    "armor": 52,
    "minTotalDamageThreshold": 0.13,
    "wheelDamageRadiusCoef": 0.9,
    "wheelDestroyRadiusCoef": 0.4,
    "crewCrashProtection": 0.25,
    "fuelExplosionPower": 0.1,
    # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints [Indent level: 1],
    "HitPoints": {
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitLFWheel [Indent level: 2]
        "HitLFWheel": {
            "radius": 0.25,
            "visual": "wheel_1_1_damage",
            "armorComponent": "wheel_1_1_hide",
            "armor": -200,
            "minimalHit": -0.01,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_1_1_steering"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitLF2Wheel [Indent level: 2],
        "HitLF2Wheel": {
            "radius": 0.25,
            "visual": "wheel_1_2_damage",
            "armorComponent": "wheel_1_2_hide",
            "armor": -200,
            "minimalHit": -0.01,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_1_2_steering"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitLMWheel [Indent level: 2],
        "HitLMWheel": {
            "radius": 0.25,
            "visual": "wheel_1_3_damage",
            "armorComponent": "wheel_1_3_hide",
            "armor": -200,
            "minimalHit": -0.01,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_1_3_steering"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitLBWheel [Indent level: 2],
        "HitLBWheel": {
            "radius": 0.25,
            "visual": "wheel_1_4_damage",
            "armorComponent": "wheel_1_4_hide",
            "armor": -200,
            "minimalHit": -0.01,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_1_4_steering"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitRFWheel [Indent level: 2],
        "HitRFWheel": {
            "radius": 0.25,
            "visual": "wheel_2_1_damage",
            "armorComponent": "wheel_2_1_hide",
            "armor": -200,
            "minimalHit": -0.01,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_2_1_steering"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitRF2Wheel [Indent level: 2],
        "HitRF2Wheel": {
            "radius": 0.25,
            "visual": "wheel_2_2_damage",
            "armorComponent": "wheel_2_2_hide",
            "armor": -200,
            "minimalHit": -0.01,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_2_2_steering"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitRMWheel [Indent level: 2],
        "HitRMWheel": {
            "radius": 0.25,
            "visual": "wheel_2_3_damage",
            "armorComponent": "wheel_2_3_hide",
            "armor": -200,
            "minimalHit": -0.01,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_2_3_steering"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitRBWheel [Indent level: 2],
        "HitRBWheel": {
            "radius": 0.25,
            "visual": "wheel_2_4_damage",
            "armorComponent": "wheel_2_4_hide",
            "armor": -200,
            "minimalHit": -0.01,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_2_4_steering"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitSpare [Indent level: 2],
        "HitSpare": {
            "name": "spare1",
            "radius": 0.25,
            "visual": "wheel_2_2_damage",
            "armorComponent": "wheel_2_2_hide",
            "armor": -200,
            "minimalHit": -0.01,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\UseSpare [Indent level: 2],
        "UseSpare": {
            "name": "",
            "visual": "-",
            "armor": 1,
            "radius": 0.25,
            "armorComponent": "wheel_2_2_hide",
            "minimalHit": -0.01,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitFuel [Indent level: 2],
        "HitFuel": {
            "armor": 0.5,
            "radius": 0.2,
            "name": "Hit_Fuel",
            "armorComponent": "Hit_Fuel",
            "visual": "-",
            "passThrough": 0.2
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitEngine [Indent level: 2],
        "HitEngine": {
            "armor": 0.5,
            "radius": 0.2,
            "name": "Hit_Engine",
            "armorComponent": "Hit_Engine",
            "visual": "zbytek",
            "passThrough": 0.2,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitEngine\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke [Indent level: 4],
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1 [Indent level: 4],
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2 [Indent level: 4],
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds [Indent level: 4],
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "SmokeWreck1",
                    "position": "engine_smoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                }
            }
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitBody [Indent level: 2],
        "HitBody": {
            "name": "karoserie",
            "visual": "zbytek",
            "passThrough": 1,
            "radius": 0.2,
            "armor": 1,
            "material": -1,
            "explosionShielding": 1.5
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "armor": 0.1,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "armor": 0.05,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitGlass3 [Indent level: 2],
        "HitGlass3": {
            "armor": 0.05,
            "material": -1,
            "name": "glass3",
            "visual": "glass3",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\HitPoints\HitGlass4 [Indent level: 2],
        "HitGlass4": {
            "visual": "glass4",
            "armor": 0.05,
            "material": -1,
            "name": "glass4",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitRGlass [Indent level: 2],
        "HitRGlass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni P",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitLGlass [Indent level: 2],
        "HitLGlass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni L",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitGlass5 [Indent level: 2],
        "HitGlass5": {
            "armor": 0.1,
            "material": -1,
            "name": "glass5",
            "visual": "glass5",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitGlass6 [Indent level: 2],
        "HitGlass6": {
            "armor": 0.1,
            "material": -1,
            "name": "glass6",
            "visual": "glass6",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitHull [Indent level: 2],
        "HitHull": {
            "armor": 1.5,
            "material": -1,
            "name": "palivo",
            "visual": "",
            "passThrough": 0.5,
            "explosionShielding": 8,
            "minimalHit": 0.1
        }
    },
    "cargoAction": ["rhs_passenger_apc_narrow_generic01","rhs_passenger_apc_narrow_generic03still","rhs_passenger_apc_narrow_generic03","passenger_generic01_leanright","rhs_passenger_apc_generic01","rhs_passenger_apc_generic01","rhs_passenger_apc_generic03","rhs_passenger_apc_narrow_generic01","passenger_generic01_leanleft","rhs_passenger_apc_generic03","rhs_passenger_apc_narrow_generic02","rhs_passenger_apc_generic02","rhs_passenger_apc_generic01","passenger_generic01_foldhands","rhs_passenger_apc_generic04","passenger_generic01_leanleft"],
    "getInAction": "GetInMantis",
    "getOutAction": "GetOutMedium",
    "cargoGetInAction": ["GetInMantis","GetInMantis","GetInHemttBack"],
    "cargoGetOutAction": ["GetOutMedium","GetOutMedium","GetOutHighZamak"],
    "memorypointtrackbll": "Stopa ZLL",
    "memorypointtrackblr": "Stopa ZLP",
    "memorypointtrackbrl": "Stopa ZPL",
    "memorypointtrackbrr": "Stopa ZPP",
    "memorypointtrackfll": "Stopa PLL",
    "memorypointtrackflr": "Stopa PLP",
    "memorypointtrackfrl": "Stopa PPL",
    "memorypointtrackfrr": "Stopa PPP",
    # Class: CfgVehicles\RHS_Ural_BaseTurret\Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Exhausts\Exhaust1 [Indent level: 2]
        "Exhaust1": {
            "position": "vyfuk start",
            "direction": "vyfuk konec",
            "effect": "ExhaustEffectHTruck"
        }
    },
    # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\LSvetla [Indent level: 2]
        "LSvetla": {
            "color": [800,900,650],
            "ambient": [2,2,2],
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerAngle": 30,
            "outerAngle": 100,
            "coneFadeCoef": 10,
            "intensity": 1.5,
            "useFlare": 1,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\RSvetla [Indent level: 2],
        "RSvetla": {
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "innerAngle": 40,
            "outerAngle": 120,
            "intensity": 2.5,
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "coneFadeCoef": 10,
            "useFlare": 1,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Right2 [Indent level: 2],
        "Right2": {
            "position": "Light_R_Flare",
            "direction": "Light_R_Flare_end",
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Right2\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "dayLight": 0,
            "flareSize": 0.85
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Left2 [Indent level: 2],
        "Left2": {
            "position": "Light_L_Flare",
            "direction": "Light_L_Flare_end",
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Left2\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "color": [800,900,650],
            "ambient": [2,2,2],
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "dayLight": 0,
            "flareSize": 0.85
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Searchlight [Indent level: 2],
        "Searchlight": {
            "position": "Searchlight_pos",
            "direction": "Searchlight_dir",
            "hitpoint": "Searchlight",
            "selection": "Searchlight",
            "useFlare": 1,
            "innerAngle": 35,
            "outerAngle": 179,
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "coneFadeCoef": 10,
            "intensity": 1.5,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Long_Left [Indent level: 2],
        "Long_Left": {
            "color": [800,900,650],
            "ambient": [5,5,5],
            "position": "Light_L_Long",
            "direction": "Light_L_Long_end",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerAngle": 22,
            "outerAngle": 29,
            "coneFadeCoef": 1,
            "intensity": 100,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Long_Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Long_Right [Indent level: 2],
        "Long_Right": {
            "position": "Light_R_Long",
            "direction": "Light_R_Long_end",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [800,900,650],
            "ambient": [5,5,5],
            "size": 1,
            "innerAngle": 22,
            "outerAngle": 29,
            "coneFadeCoef": 1,
            "intensity": 100,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Long_Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Long_Right2 [Indent level: 2],
        "Long_Right2": {
            "useFlare": 1,
            "position": "light_R_Long_flare",
            "innerAngle": 50,
            "outerAngle": 139,
            "coneFadeCoef": 51,
            "flareSize": 1,
            "intensity": 1,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Long_Right2\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "direction": "Light_R_Long_end",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [800,900,650],
            "ambient": [5,5,5],
            "size": 1,
            "dayLight": 0,
            "flareMaxDistance": 750
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Long_Left2 [Indent level: 2],
        "Long_Left2": {
            "useFlare": 1,
            "position": "light_L_Long_flare",
            "innerAngle": 50,
            "outerAngle": 139,
            "coneFadeCoef": 51,
            "flareSize": 1,
            "intensity": 1,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\Long_Left2\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "color": [800,900,650],
            "ambient": [5,5,5],
            "direction": "Light_L_Long_end",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "dayLight": 0,
            "flareMaxDistance": 750
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\cabin [Indent level: 2],
        "cabin": {
            "color": [800,900,650],
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
            "dayLight": 0,
            "blinking": 0,
            # Class: CfgVehicles\RHS_Ural_BaseTurret\Reflectors\cabin\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 1.5,
                "hardLimitEnd": 2
            }
        }
    },
    "aggregateReflectors": [["LSvetla"],["Left2"],["RSvetla"],["Right2"],["Long_Left2","Long_Right2"]],
    "armorLights": 0.05,
    # Class: CfgVehicles\RHS_Ural_BaseTurret\RenderTargets [Indent level: 1],
    "RenderTargets": {
        # Class: CfgVehicles\RHS_Ural_BaseTurret\RenderTargets\LeftMirror [Indent level: 2]
        "LeftMirror": {
            "renderTarget": "rendertarget0",
            # Class: CfgVehicles\RHS_Ural_BaseTurret\RenderTargets\LeftMirror\CameraView1 [Indent level: 3],
            "CameraView1": {
                "pointPosition": "m1p",
                "pointDirection": "m1d",
                "renderQuality": 2,
                "renderVisionMode": 4,
                "fov": 0.7
            },
            "BBoxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\RenderTargets\RightMirror [Indent level: 2],
        "RightMirror": {
            "renderTarget": "rendertarget1",
            # Class: CfgVehicles\RHS_Ural_BaseTurret\RenderTargets\RightMirror\CameraView1 [Indent level: 3],
            "CameraView1": {
                "pointPosition": "m2p",
                "pointDirection": "m2d",
                "renderQuality": 2,
                "renderVisionMode": 4,
                "fov": 0.7
            },
            "BBoxes": ["PIP_2_TL","PIP_2_TR","PIP_2_BL","PIP_2_BR"]
        }
    },
    # Class: CfgVehicles\RHS_Ural_BaseTurret\UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles\RHS_Ural_BaseTurret\UserActions\lights_toggle [Indent level: 2]
        "lights_toggle": {
            "displayName": "Toggle short/long lights",
            "position": "",
            "shortcut": "vehLockTargets",
            "radius": 12,
            "priority": 1.5,
            "showWindow": 0,
            "onlyForplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)",
            "statement": "[this,0] call rhs_fnc_carLightToggle"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\UserActions\cabinlights_toggle [Indent level: 2],
        "cabinlights_toggle": {
            "shortcut": "lockTarget",
            "displayName": "Toggle cabin lights",
            "statement": "[this,1] call rhs_fnc_carLightToggle",
            "position": "",
            "radius": 12,
            "priority": 1.5,
            "showWindow": 0,
            "onlyForplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\UserActions\searchlight_toggle [Indent level: 2],
        "searchlight_toggle": {
            "shortcut": "",
            "displayName": "Toggle searchlight",
            "statement": "[this,3] call rhs_fnc_carLightToggle",
            "position": "",
            "radius": 12,
            "priority": 1.5,
            "showWindow": 0,
            "onlyForplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)"
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\UserActions\searchlight_adjust [Indent level: 2],
        "searchlight_adjust": {
            "shortcut": "",
            "displayName": "Adjust searchlight",
            "condition": "((call rhs_fnc_findPlayer) == driver this) AND (isLightOn this) AND (this animationPhase 'searchlight_hide' == 0)",
            "statement": "[this] spawn rhs_fnc_adjustSearchlight",
            "position": "",
            "radius": 12,
            "priority": 1.5,
            "showWindow": 0,
            "onlyForplayer": 1
        }
    },
    "normalSpeedForwardCoef": 0.6,
    "slowSpeedForwardCoef": 0.45,
    "turnCoef": 4,
    "terrainCoef": 0.7,
    "waterSpeedFactor": 0.4,
    "simulation": "carx",
    "dampersBumpCoef": 6,
    "precision": 10,
    "brakeDistance": 3,
    "acceleration": 15,
    "fireResistance": 5,
    "maxSpeed": 76,
    "fuelCapacity": 40,
    "RHS_fuelCapacity": 300,
    "wheelCircumference": 3.87,
    "brakeIdleSpeed": 1.25,
    "maxFordingDepth": 0,
    "waterResistance": 1,
    "waterResistanceCoef": 0.2,
    "waterLeakiness": 10,
    # Class: CfgVehicles\RHS_Ural_BaseTurret\complexGearbox [Indent level: 1],
    "complexGearbox": {
        "GearboxRatios": ["R1",-5.3,"N",0,"D1",5.62,"D2",2.89,"D3",1.64,"D4",1,"D5",0.724],
        "TransmissionRatios": ["High",5.82],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R"
    },
    "changeGearMinEffectivity": [0.95,0,0.8,0.85,0.85,0.95,0.85],
    "switchTime": 0.31,
    "latency": 1.5,
    "differentialType": "all_limited",
    "frontRearSplit": 0.5,
    "frontBias": 1.3,
    "rearBias": 0.6,
    "centreBias": 1.3,
    "clutchStrength": 75,
    "transmissionLosses": 12,
    "dampingRateFullThrottle": 0.08,
    "dampingRateZeroThrottleClutchEngaged": 1.35,
    "dampingRateZeroThrottleClutchDisengaged": 0.35,
    "torqueCurve": [[0,0],[0.428571,0.917327],[0.52381,0.934315],[0.595238,1],[0.690476,1],[0.761905,0.956965],[0.857143,0.928652],[1,0.509626]],
    "enginePower": 179,
    "engineMOI": 2,
    "peakTorque": 1059.6,
    "maxOmega": 219.91,
    "minOmega": 65,
    "idleRPM": 650,
    "redRPM": 2100,
    "engineLosses": 14,
    "thrustDelay": 2.4,
    "engineBrakeCoef": 0.3,
    "antiRollbarForceCoef": 25,
    "antiRollbarForceLimit": 45.5,
    "antiRollbarSpeedMin": 30,
    "antiRollbarSpeedMax": 60,
    # Class: CfgVehicles\RHS_Ural_BaseTurret\Wheels [Indent level: 1],
    "Wheels": {
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Wheels\LF [Indent level: 2]
        "LF": {
            "width": "0.37",
            "steering": 1,
            "side": "left",
            "boneName": "wheel_1_1_damper",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "mass": 90,
            "MOI": 18,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 12500,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "suspForceAppPointOffset": "wheel_1_1_axis",
            "tireForceAppPointOffset": "wheel_1_1_axis",
            "maxCompression": 0.27,
            "maxDroop": 0.2,
            "sprungMass": -1,
            "springStrength": 171813,
            "springDamperRate": 15872,
            "longitudinalStiffnessPerUnitGravity": 14582,
            "latStiffX": 3.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Wheels\LR [Indent level: 2],
        "LR": {
            "boneName": "wheel_1_2_damper",
            "steering": 0,
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "suspForceAppPointOffset": "wheel_1_2_axis",
            "tireForceAppPointOffset": "wheel_1_2_axis",
            "maxHandBrakeTorque": 20000,
            "width": "0.37",
            "side": "left",
            "mass": 90,
            "MOI": 18,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 12500,
            "suspTravelDirection": [-0.125,-1,0],
            "maxCompression": 0.27,
            "maxDroop": 0.2,
            "sprungMass": -1,
            "springStrength": 171813,
            "springDamperRate": 15872,
            "longitudinalStiffnessPerUnitGravity": 14582,
            "latStiffX": 3.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Wheels\LR2 [Indent level: 2],
        "LR2": {
            "boneName": "wheel_1_3_damper",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "suspForceAppPointOffset": "wheel_1_3_axis",
            "tireForceAppPointOffset": "wheel_1_3_axis",
            "steering": 0,
            "maxHandBrakeTorque": 20000,
            "width": "0.37",
            "side": "left",
            "mass": 90,
            "MOI": 18,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 12500,
            "suspTravelDirection": [-0.125,-1,0],
            "maxCompression": 0.27,
            "maxDroop": 0.2,
            "sprungMass": -1,
            "springStrength": 171813,
            "springDamperRate": 15872,
            "longitudinalStiffnessPerUnitGravity": 14582,
            "latStiffX": 3.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Wheels\RF [Indent level: 2],
        "RF": {
            "boneName": "wheel_2_1_damper",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "suspForceAppPointOffset": "wheel_2_1_axis",
            "tireForceAppPointOffset": "wheel_2_1_axis",
            "steering": 1,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": "0.37",
            "mass": 90,
            "MOI": 18,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 12500,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.27,
            "maxDroop": 0.2,
            "sprungMass": -1,
            "springStrength": 171813,
            "springDamperRate": 15872,
            "longitudinalStiffnessPerUnitGravity": 14582,
            "latStiffX": 3.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Wheels\RR [Indent level: 2],
        "RR": {
            "boneName": "wheel_2_2_damper",
            "steering": 0,
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "suspForceAppPointOffset": "wheel_2_2_axis",
            "tireForceAppPointOffset": "wheel_2_2_axis",
            "maxHandBrakeTorque": 20000,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": "0.37",
            "mass": 90,
            "MOI": 18,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 12500,
            "maxCompression": 0.27,
            "maxDroop": 0.2,
            "sprungMass": -1,
            "springStrength": 171813,
            "springDamperRate": 15872,
            "longitudinalStiffnessPerUnitGravity": 14582,
            "latStiffX": 3.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles\RHS_Ural_BaseTurret\Wheels\RR2 [Indent level: 2],
        "RR2": {
            "boneName": "wheel_2_3_damper",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "suspForceAppPointOffset": "wheel_2_3_axis",
            "tireForceAppPointOffset": "wheel_2_3_axis",
            "steering": 0,
            "maxHandBrakeTorque": 20000,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": "0.37",
            "mass": 90,
            "MOI": 18,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 12500,
            "maxCompression": 0.27,
            "maxDroop": 0.2,
            "sprungMass": -1,
            "springStrength": 171813,
            "springDamperRate": 15872,
            "longitudinalStiffnessPerUnitGravity": 14582,
            "latStiffX": 3.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0,1.2],[0.5,1.13],[1,1]]
        }
    },
    # Class: CfgVehicles\RHS_Ural_BaseTurret\EventHandlers [Indent level: 1],
    "EventHandlers": {
        # Class: CfgVehicles\RHS_Ural_BaseTurret\EventHandlers\RHS_EventHandlers [Indent level: 2]
        "RHS_EventHandlers": {
            "init": "_this call rhs_fnc_a2port_car_init",
            "engine": "if(_this select 1)then{_this call RHS_fnc_gearSound};",
            "dammaged": " _this call rhs_fnc_wheelDamaged"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers [Indent level: 0],
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "attenuationEffectType": "TruckAttenuation",
    "soundDammage": ["",0.562341,1],
    "buildCrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "buildCrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "buildCrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "buildCrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "buildCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "buildCrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "buildCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "buildCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundBuildingCrash": ["buildCrash0",0.125,"buildCrash1",0.125,"buildCrash2",0.125,"buildCrash3",0.125,"buildCrash4",0.125,"buildCrash5",0.125,"buildCrash6",0.125,"buildCrash7",0.125],
    "WoodCrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_01",1.99526,1,75],
    "WoodCrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_02",1.99526,1,75],
    "WoodCrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_03",1.99526,1,75],
    "WoodCrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_04",1.99526,1,75],
    "WoodCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_05",1.99526,1,75],
    "WoodCrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_06",1.99526,1,75],
    "WoodCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_07",1.99526,1,75],
    "WoodCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_08",1.99526,1,75],
    "soundWoodCrash": ["woodCrash0",0.125,"woodCrash1",0.125,"woodCrash2",0.125,"woodCrash3",0.125,"woodCrash4",0.125,"woodCrash5",0.125,"woodCrash6",0.125,"woodCrash7",0.125],
    "armorCrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "armorCrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "armorCrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "armorCrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "armorCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "armorCrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "armorCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "armorCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundArmorCrash": ["ArmorCrash0",0.125,"ArmorCrash1",0.125,"ArmorCrash2",0.125,"ArmorCrash3",0.125,"ArmorCrash4",0.125,"ArmorCrash5",0.125,"ArmorCrash6",0.125,"ArmorCrash7",0.125],
    "Crash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "Crash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "Crash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "Crash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "Crash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "Crash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "Crash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "Crash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundCrashes": ["Crash0",0.125,"Crash1",0.125,"Crash2",0.125,"Crash3",0.125,"Crash4",0.125,"Crash5",0.125,"Crash6",0.125,"Crash7",0.125],
    "BushCrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_01",0.630957,1,50],
    "BushCrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_02",0.630957,1,50],
    "BushCrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_03",0.630957,1,50],
    "BushCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_03",0.630957,0.8,50],
    "soundBushCrash": ["BushCrash1",0.25,"BushCrash2",0.25,"BushCrash3",0.25,"BushCrash4",0.25],
    # Class: CfgVehicles\Truck_F\SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles\Truck_F\SpeechVariants\Default [Indent level: 2]
        "Default": {
            "speechSingular": ["veh_vehicle_truck_s"],
            "speechPlural": ["veh_vehicle_truck_p"]
        }
    },
    "textSingular": "truck",
    "textPlural": "trucks",
    "nameSound": "veh_vehicle_truck_s",
    "_generalMacro": "Truck_F",
    "audible": 9,
    "epeImpulseDamageCoef": 15,
    "crewExplosionProtection": 0.8,
    "maximumLoad": 3000,
    "transportMaxMagazines": 256,
    "transportMaxWeapons": 64,
    # Class: CfgVehicles\Truck_F\PlayerSteeringCoefficients [Indent level: 1],
    "PlayerSteeringCoefficients": {
        "turnIncreaseConst": 0.5,
        "turnIncreaseLinear": 1,
        "turnIncreaseTime": 0,
        "turnDecreaseConst": 5,
        "turnDecreaseLinear": 0,
        "turnDecreaseTime": 0,
        "maxTurnHundred": 1
    },
    # Class: CfgVehicles\Truck_F\TransportBackpacks [Indent level: 1],
    "TransportBackpacks": {
    },
    # Class: CfgVehicles\Truck_F\TransportMagazines [Indent level: 1],
    "TransportMagazines": {
    },
    # Class: CfgVehicles\Truck_F\TransportWeapons [Indent level: 1],
    "TransportWeapons": {
    },
    # Class: CfgVehicles\Truck_F\TransportItems [Indent level: 1],
    "TransportItems": {
        # Class: CfgVehicles\Truck_F\TransportItems\_xx_FirstAidKit [Indent level: 2]
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 10
        }
    },
    "numberPhysicalWheels": 6,
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
    "secondaryExplosion": -10,
    "dammageHalf": [],
    "dammageFull": [],
    "armorStructural": 4,
    "explosionShielding": 1,
    "gunnerHasFlares": 0,
    "steerAheadSimul": 0.5,
    "steerAheadPlan": 0.35,
    "predictTurnPlan": 2,
    "predictTurnSimul": 1.5,
    "accelAidForceYOffset": -1,
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    # Class: CfgVehicles\Car_F\ViewPilot [Indent level: 1],
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
    "headGforceLeaningFactor": [0.01,0.01,0.015],
    # Class: CfgVehicles\Car_F\NewTurret [Indent level: 1],
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
        "showCrewAim": 0
    },
    "holdOffroadFormation": 1,
    # Class: CfgVehicles\Car_F\NVGMarkers [Indent level: 1],
    "NVGMarkers": {
        # Class: CfgVehicles\Car_F\NVGMarkers\NVGMarker01 [Indent level: 2]
        "NVGMarker01": {
            "name": "nvg_marker",
            "color": [0.03,0.003,0.003,1],
            "ambient": [0.003,0.0003,0.0003,1],
            "brightness": 0.001,
            "blinking": 1
        }
    },
    "viewCargoShadowDiff": 1,
    "viewCargoShadowAmb": 1,
    "magazines": [],
    "soundEnviron": ["",0.000562341,1],
    "soundCrash": ["A3|sounds_f|dummysound",1,1],
    "extCameraPosition": [0.5,2,-10],
    "collisionEffect": "collisionEffect",
    "hideUnitInfo": 0,
    "htMin": 60,
    "htMax": 1800,
    "afMax": 100,
    "mfMax": 80,
    "mFact": 1,
    "tBody": 150,
    "memoryPointSupply": "doplnovani",
    "brakeTorque": 6000,
    "longStiff": 15000,
    "latStiffX": 2000,
    "latStiffY": 18000,
    "wheelMask": "wheel_X_X",
    "camShakeCoef": 0.2,
    "maxGForce": 3,
    # Class: CfgVehicles\Car_F\camShakeGForce [Indent level: 1],
    "camShakeGForce": {
        "power": 2,
        "frequency": 60,
        "distance": 0,
        "minSpeed": 60
    },
    # Class: CfgVehicles\Car_F\Components [Indent level: 1],
    "Components": {
        # Class: CfgVehicles\Car\Components\AICarSteeringComponent [Indent level: 2]
        "AICarSteeringComponent": {
            "steeringPIDWeights": [2.9,0.1,0.2],
            "speedPIDWeights": [0.7,0.2,0],
            "convoyPIDWeights": [1,0.01,0.01],
            "doRemapSpeed": 1,
            "remapSpeedRange": [30,70],
            "remapSpeedScalar": [1,0.35],
            "doPredictForward": 1,
            "predictForwardRange": [1,20],
            "steerAheadSaturation": [0.01,0.4],
            "speedPredictionMethod": 2,
            "wheelAngleCoef": 0.7,
            "forwardAngleCoef": 0.7,
            "steeringAngleCoef": 1,
            "differenceAngleCoef": 0.4,
            "stuckMaxTime": 3,
            "allowOvertaking": 1,
            "allowDrifting": 0,
            "allowCollisionAvoidance": 1,
            "maxWheelAngleDiff": 0.2616,
            "minSpeedToKeep": 0.1,
            "commandTurnFactor": 1
        },
        # Class: CfgVehicles\LandVehicle\Components\TransportCountermeasuresComponent [Indent level: 2],
        "TransportCountermeasuresComponent": {
        }
    },
    "unloadInCombat": 1,
    "canFloat": 0,
    "limitedSpeedCoef": 0.5,
    "hullDamageCauseExplosion": 1,
    # Class: CfgVehicles\Car\PlateInfos [Indent level: 1],
    "PlateInfos": {
        "name": "spz",
        "color": [0,0,0,0.75]
    },
    "selectionFireAnim": "zasleh",
    "alphaTracks": 0.2,
    "memoryPointCirculumReference": "circulumReference",
    "gearBox": [-8,0,10,6.15,4.44,3.33],
    "Scudeffect": "ScudEffect",
    "preferRoads": 1,
    "formationX": 20,
    "formationZ": 20,
    "type": 0,
    "scudModel": "",
    "damperSize": 0.1,
    "damperForce": 1,
    "damperDamping": 1,
    "inputTurnCurve": [[0,[0,0,1,1]],[30,[0,0,0.2,0.008,0.4,0.032,0.6,0.216,0.8,0.512,1,1]]],
    "enableGPS": 0,
    "soundEngine": ["",1.77828,0.9],
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffects"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffects"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffects"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffects"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","LDustEffects"]],
    # Class: CfgVehicles\Car\DestructionEffects [Indent level: 1],
    "DestructionEffects": {
        # Class: CfgVehicles\Car\DestructionEffects\Light1 [Indent level: 2]
        "Light1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 0.001,
            "interval": 1,
            "lifeTime": 3,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles\Car\DestructionEffects\Sound [Indent level: 2],
        "Sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles\Car\DestructionEffects\Fire1 [Indent level: 2],
        "Fire1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1Small",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Car\DestructionEffects\Refract1 [Indent level: 2],
        "Refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefractSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Car\DestructionEffects\Smoke1 [Indent level: 2],
        "Smoke1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmokeSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Car\DestructionEffects\Sparks1 [Indent level: 2],
        "Sparks1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifeTime": 0
        },
        # Class: CfgVehicles\Car\DestructionEffects\FireSparks1 [Indent level: 2],
        "FireSparks1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2.8
        },
        # Class: CfgVehicles\Car\DestructionEffects\Fire2 [Indent level: 2],
        "Fire2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Car\DestructionEffects\Smoke1_2 [Indent level: 2],
        "Smoke1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Car\DestructionEffects\Smoke2 [Indent level: 2],
        "Smoke2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 3.2
        }
    },
    "sensitivityEar": 0.125,
    "sensitivity": 1.75,
    "selectionBrakeLights": "brzdove svetlo",
    "memoryPointMissile": ["spice rakety","usti hlavne"],
    "memoryPointMissileDir": ["konec rakety","konec hlavne"],
    "engineStartSpeed": 1.5,
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "leftWaterEffect": "LWaterEffects",
    "rightWaterEffect": "RWaterEffects",
    "leftFastWaterEffect": "LWaterEffects",
    "rightFastWaterEffect": "RWaterEffects",
    "tracksSpeed": 0,
    "selectionLeftOffset": "PasOffsetL",
    "selectionRightOffset": "PasOffsetP",
    "explosionEffect": "FuelExplosion",
    # Class: CfgVehicles\LandVehicle\CommanderOptics [Indent level: 1],
    "CommanderOptics": {
        "proxyType": "CPCommander",
        "proxyIndex": 1,
        "gunnerName": "Commander",
        "primaryGunner": 0,
        "primaryObserver": 1,
        "stabilizedInAxes": 0,
        "body": "obsTurret",
        "gun": "obsGun",
        "animationSourceBody": "obsTurret",
        "animationSourceGun": "obsGun",
        "animationSourceHatch": "hatchCommander",
        "animationSourceCamElev": "camElev",
        "soundServo": ["A3|sounds_f|dummysound",0.01,1,10],
        "gunBeg": "",
        "gunEnd": "",
        "minElev": -4,
        "maxElev": 20,
        "initElev": 0,
        "minTurn": -360,
        "maxTurn": 360,
        "initTurn": 0,
        "commanding": 2,
        "outGunnerMayFire": 1,
        "inGunnerMayFire": 1,
        "viewGunnerInExternal": 0,
        "gunnerOpticsModel": "A3|weapons_f|reticle|Optics_Commander_02_F",
        "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
        "gunnerOutOpticsColor": [0,0,0,1],
        "gunnerOutForceOptics": 0,
        "gunnerOutOpticsShowCursor": 0,
        "gunnerOpticsEffect": [],
        "gunnerOutOpticsEffect": [],
        "memoryPointGunnerOutOptics": "commander_weapon_view",
        "memoryPointGunnerOptics": "commanderview",
        "memoryPointsGetInGunner": "pos commander",
        "memoryPointsGetInGunnerDir": "pos commander dir",
        "gunnerGetInAction": "GetInHigh",
        "gunnerGetOutAction": "GetOutHigh",
        "memoryPointGun": "gun_muzzle",
        "selectionFireAnim": "zasleh_1",
        # Class: CfgVehicles\LandVehicle\CommanderOptics\ViewOptics [Indent level: 2],
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
        # Class: CfgVehicles\LandVehicle\CommanderOptics\ViewGunner [Indent level: 2],
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
        "gunnerType": "",
        "weapons": [],
        "magazines": [],
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
        "turretCanSee": 0,
        "canUseScanners": 1,
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
        "TurretSpec": {
            "showHeadPhones": 0
        },
        "gunnerOpticsColor": [0,0,0,1],
        "gunnerForceOptics": 1,
        "gunnerOpticsShowCursor": 0,
        "turretInfoType": "",
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
        "showHMD": 0,
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
        "showCrewAim": 0
    },
    "wheelDamageThreshold": 0.2,
    "wheelDestroyThreshold": 0.99,
    "weaponsGroup1": 1,
    "weaponsGroup2": "2 + 		4",
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    # Class: CfgVehicles\AllVehicles\SquadTitles [Indent level: 1],
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
    "selectionShowDamage": "poskozeni",
    "selectionBackLights": "zadni svetlo",
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
    # Class: CfgVehicles\AllVehicles\ViewOptics [Indent level: 1],
    "ViewOptics": {
        "initAngleX": 0,
        "minAngleX": -30,
        "maxAngleX": 30,
        "initAngleY": 0,
        "minAngleY": -100,
        "maxAngleY": 100,
        "initFov": 0.7,
        "minFov": 0.42,
        "maxFov": 0.85,
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": 0,
        "maxMoveY": 0,
        "minMoveZ": 0,
        "maxMoveZ": 0,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    # Class: CfgVehicles\AllVehicles\PilotSpec [Indent level: 1],
    "PilotSpec": {
        "showHeadPhones": 0
    },
    # Class: CfgVehicles\AllVehicles\CargoSpec [Indent level: 1],
    "CargoSpec": {
        # Class: CfgVehicles\AllVehicles\CargoSpec\Cargo1 [Indent level: 2]
        "Cargo1": {
            "showHeadPhones": 0
        }
    },
    # Class: CfgVehicles\AllVehicles\MFD [Indent level: 1],
    "MFD": {
    },
    # Class: CfgVehicles\AllVehicles\SoundEvents [Indent level: 1],
    "SoundEvents": {
    },
    "cargoProxyIndexes": [],
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "preciseGetInOut": 0,
    "cargoPreciseGetInOut": [0],
    "availableForSupportTypes": [],
    "waterPPInVehicle": 1,
    "impactEffectsSea": "ImpactEffectsSea",
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
    "camouflage": 2,
    "spotableDarkNightLightsOff": 0.001,
    "spotableNightLightsOff": 0.02,
    "spotableNightLightsOn": 4,
    "accuracyDarkNightLightsOff": 0.001,
    "accuracyNightLightsOff": 0.006,
    "accuracyNightLightsOn": 0.1,
    "outsideSoundFilter": 0,
    "obstructSoundLFRatio": 0,
    "occludeSoundLFRatio": 0.25,
    "enableManualFire": 1,
    "portrait": "",
    "ghostPreview": "",
    "destrType": "DestructDefault",
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
    "minFireTime": 20,
    "indirectHitEnemyCoefAI": 10,
    "indirectHitFriendlyCoefAI": -20,
    "indirectHitCivilianCoefAI": -20,
    "indirectHitUnknownCoefAI": -0.5,
    "formationTime": 5,
    "alwaysTarget": 0,
    "irTarget": 1,
    "irScanRangeMin": 0,
    "irScanRangeMax": 0,
    "irScanToEyeFactor": 1,
    "irScanGround": 1,
    "laserTarget": 0,
    "laserScanner": 0,
    "nvTarget": 0,
    "nvScanner": 0,
    "artilleryTarget": 0,
    "artilleryScanner": 0,
    "canUseScanners": 1,
    "unitInfoTypeLite": 0,
    "nightVision": 0,
    "radarType": 0,
    "hasDriver": 1,
    "driverForceOptics": 0,
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 0,
    "getInRadius": 2.5,
    "enableWatch": 0,
    "enableRadio": 0,
    "lockDetectionSystem": 0,
    "incomingMissileDetectionSystem": 0,
    "usePreciseGetInAction": 0,
    "allowTabLock": 1,
    "showAllTargets": 0,
    "dustFrontLeftPos": "dustFrontLeft",
    "dustFrontRightPos": "dustFrontRight",
    "dustBackLeftPos": "dustBackLeft",
    "dustBackRightPos": "dustBackRight",
    "waterLinearDampingCoefX": 0,
    "waterLinearDampingCoefY": 0,
    "waterAngularDampingCoef": 0,
    "showNVGDriver": 0,
    "showNVGCommander": 0,
    "showNVGGunner": 0,
    "showNVGCargo": [0],
    "countsForScoreboard": 1,
    # Class: CfgVehicles\All\MarkerLights [Indent level: 1],
    "MarkerLights": {
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
    # Class: CfgVehicles\All\SoundEnvironExt [Indent level: 1],
    "SoundEnvironExt": {
    },
    # Class: CfgVehicles\All\SoundEquipment [Indent level: 1],
    "SoundEquipment": {
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
    "soundLandCrashes": ["soundLandCrash",1],
    "soundWaterCrashes": ["soundWaterCrash",1],
    "emptySound": ["",0,1],
    "soundLocked": ["",1,1],
    "soundIncommingMissile": ["",1,1],
    "cargoIsCoDriver": [0],
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
    "ejectDeadDriver": 0,
    "ejectDeadCargo": 0,
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
    "selectionDamage": "zbytek",
    "HeadAimDown": 0,
    "cargoCanEject": 1,
    "driverCanEject": 1,
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
    "minGForce": 0.2,
    "gForceShakeAttenuation": 0.5,
    # Class: CfgVehicles\All\camShakeDamage [Indent level: 1],
    "camShakeDamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minSpeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "soundTurnIn": ["",0.000316228,1],
    "soundTurnOut": ["",0.000316228,1],
    "soundTurnInInternal": ["",0.000316228,1],
    "soundTurnOutInternal": ["",0.000316228,1],
    "features": "",
    "insideDetectCoef": 0.05,
}