rhs_gaz66_zu23_msv = {
    "editorPreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_gaz66_zu23_msv.paa",
    "scope": 2,
    "faction": "rhs_faction_msv",
    "crew": "rhs_msv_driver",
    "rhs_decalParameters": ["['Number', cTrucksGaz4NumberPlaces, 'Default']","['Label', cTrucksGazRightArmyPlaces, 'Platoon', 12]"],
    "author": "Red Hammer Studios",
    # Class: CfgVehicles\rhs_gaz66_zu23_msv\Turrets [Indent level: 1],
    "Turrets": {
        # Class: CfgVehicles\rhs_gaz66_zu23_msv\Turrets\MainTurret [Indent level: 2]
        "MainTurret": {
            "gunnerType": "rhs_msv_rifleman",
            "body": "mainTurret",
            "gun": "mainGun",
            "minTurn": -180,
            "maxTurn": 180,
            "initTurn": 0,
            "minElev": -10,
            "maxElev": 85,
            "initElev": 18,
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
            "gunnerGetInAction": "GetInOffroadBack",
            "gunnerGetOutAction": "GetOutHighZamak",
            "turretInfoType": "RHS_RscWeaponZeroing",
            "stabilizedInAxes": 0,
            "outGunnerMayFire": 1,
            "inGunnerMayFire": 1,
            "startEngine": 0,
            "canUseScanners": 0,
            "allowTabLock": 0,
            # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\MainTurret\ViewGunner [Indent level: 3],
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
            # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\MainTurret\ViewOptics [Indent level: 3],
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
            # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\MainTurret\OpticsIn [Indent level: 3],
            "OpticsIn": {
                # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\MainTurret\OpticsIn\Wide [Indent level: 4]
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
            # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\MainTurret\TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[85,-180],[85,180]],
                "limitsArrayBottom": [[-10,-180],[-8,-28.6867],[14.3683,-26.6867],[17,0],[14.7173,26.6372],[-8,27.6867],"",[-10,134],[-6,134.5],[-6,178],[-10,180]]
            },
            "soundAttenuationTurret": "HeliAttenuationRamp",
            # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\MainTurret\Hitpoints [Indent level: 3],
            "Hitpoints": {
                # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\MainTurret\Hitpoints\HitTurret [Indent level: 4]
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
                # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\MainTurret\Hitpoints\HitGun [Indent level: 4],
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "soundServo": ["A3|sounds_f|dummysound",0.316228,1,15],
            "primaryGunner": 1,
            "enableManualFire": 0,
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\Components [Indent level: 3],
            "Components": {
            },
            "disableSoundAttenuation": 0,
            "animationSourceBody": "mainTurret",
            "animationSourceGun": "mainGun",
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerName": "Gunner",
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
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\rhs_gaz66_zu23_msv\Turrets\CargoTurret_01 [Indent level: 2],
        "CargoTurret_01": {
            "gunnerType": "rhs_msv_sergeant",
            "gunnerAction": "vehicle_coshooter_1",
            "gunnerGetInAction": "GetInOffroadBack",
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
            # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
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
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\rhs_gaz66_zu23_msv\Turrets\CargoTurret_02 [Indent level: 2],
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
            # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\CargoTurret_02\TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[45,-65],[45,84]],
                "limitsArrayBottom": [[-37,-65],[-37,-45.6867],[-28,-35.6867],[-19,-22.6867],[-15,-12.6867],[-11,-8.6867],[-5,2.6867],[-3,14],[-4,44],[-4,64],[-7,74]]
            },
            # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\CargoTurret_02\TurnOut [Indent level: 3],
            "TurnOut": {
                "limitsArrayTop": [[45,-180],[45,180]],
                "limitsArrayBottom": [[-25,-65],[-4,-50.6867],[-4,-22.6867],[-2,6.6867],[-12,28],[-45,34],[-45,84]],
                "turnOffset": -180
            },
            "gunnerGetInAction": "GetInOffroadBack",
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
            # Class: CfgVehicles\rhs_gaz66_zu23_base\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
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
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\Truck_F\Turrets\ViewGunner [Indent level: 2],
        "ViewGunner": {
        }
    },
    "displayName": "GAZ-66 (ZU-23-2)",
    "model": "rhsafrf|addons|rhs_gaz66|rhs_gaz66_zu23.p3d",
    "icon": "rhsafrf|addons|rhs_gaz66|data|ico|icomap_GAZ66_ammo_CA.paa",
    "picture": "rhsafrf|addons|rhs_gaz66|data|ico|rhs_gaz66_zu23_pic_ca.paa",
    "transportSoldier": 1,
    # Class: CfgVehicles\rhs_gaz66_zu23_base\Damage [Indent level: 1],
    "Damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_gaz66|data|gaz66.rvmat","rhsafrf|addons|rhs_gaz66|data|gaz66_dam.rvmat","rhsafrf|addons|rhs_gaz66|data|gaz66_des.rvmat","rhsafrf|addons|rhs_gaz66|data|tent.rvmat","rhsafrf|addons|rhs_gaz66|data|tent.rvmat","rhsafrf|addons|rhs_gaz66|data|tent_des.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23_damage.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23_destruct.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23_base.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23_base_damage.rvmat","rhsafrf|addons|rhs_heavyweapons|zu23|data|zu23_base_destruct.rvmat","rhsafrf|addons|rhs_gaz66|data|glass.rvmat","rhsafrf|addons|rhs_gaz66|data|glass_damage.rvmat","rhsafrf|addons|rhs_gaz66|data|glass_damage.rvmat","rhsafrf|addons|rhs_gaz66|data|glass_in.rvmat","rhsafrf|addons|rhs_gaz66|data|glass_in_damage.rvmat","rhsafrf|addons|rhs_gaz66|data|glass_in_damage.rvmat","a3|data_f|default.rvmat","rhsafrf|addons|rhs_gaz66|data|default_destruct.rvmat","rhsafrf|addons|rhs_gaz66|data|default_destruct.rvmat"]
    },
    "unitInfoType": "RscUnitInfo",
    "threat": [0.6,0.1,0.6],
    # Class: CfgVehicles\rhs_gaz66_zu23_base\AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles\rhs_gaz66_zu23_base\AnimationSources\muzzle_source [Indent level: 2]
        "muzzle_source": {
            "source": "reload",
            "weapon": "rhs_weap_2A14"
        },
        # Class: CfgVehicles\rhs_gaz66_zu23_base\AnimationSources\fire_anim [Indent level: 2],
        "fire_anim": {
            "source": "revolving",
            "weapon": "rhs_weap_2A14"
        },
        # Class: CfgVehicles\rhs_gaz66_zu23_base\AnimationSources\muzzleHMG_ROT [Indent level: 2],
        "muzzleHMG_ROT": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2A14"
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\Door_LF [Indent level: 2],
        "Door_LF": {
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_Ural_Door",
            "soundPosition": "DoorL_axis"
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\Door_RF [Indent level: 2],
        "Door_RF": {
            "soundPosition": "DoorR_axis",
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_Ural_Door"
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\HitSpare [Indent level: 2],
        "HitSpare": {
            "source": "Hit",
            "hitpoint": "HitSpare",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\UseSpare [Indent level: 2],
        "UseSpare": {
            "hitpoint": "UseSpare",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\wiper [Indent level: 2],
        "wiper": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\wipers [Indent level: 2],
        "wipers": {
            "source": "door",
            "animPeriod": 1,
            "initPhase": 0,
            "sound": "RHS_Wipers",
            "soundPosition": "wiper_axis"
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\cover_hide [Indent level: 2],
        "cover_hide": {
            "mass": 1,
            "source": "user",
            "displayName": "hide cover",
            "animPeriod": 0.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\spare_hide [Indent level: 2],
        "spare_hide": {
            "displayName": "hide spare wheel",
            "mass": 1,
            "source": "user",
            "animPeriod": 0.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\bench_hide [Indent level: 2],
        "bench_hide": {
            "displayName": "hide cargo bench",
            "mass": 1,
            "source": "user",
            "animPeriod": 0.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\rear_numplate_hide [Indent level: 2],
        "rear_numplate_hide": {
            "displayName": "hide rear registration numbers",
            "initPhase": 1,
            "mass": 1,
            "source": "user",
            "animPeriod": 0.1
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\light_hide [Indent level: 2],
        "light_hide": {
            "displayName": "hide light covers",
            "onPhaseChanged": "(_this select 0) animateSource ['light_hide',(_this select 1),true];",
            "mass": 1,
            "source": "user",
            "animPeriod": 0.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\longlights_hide [Indent level: 2],
        "longlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\shortlights_hide [Indent level: 2],
        "shortlights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\lights_hide [Indent level: 2],
        "lights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\searchlight_hide [Indent level: 2],
        "searchlight_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\searchlight_rot [Indent level: 2],
        "searchlight_rot": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\turnout1 [Indent level: 2],
        "turnout1": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_truck\AnimationSources\turnout2 [Indent level: 2],
        "turnout2": {
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
    "mapSize": 5.66,
    "dlc": "RHS_AFRF",
    "category": "Car",
    "insideSoundCoef": 0.2,
    "vehicleClass": "rhs_vehclass_truck",
    "editorSubcategory": "rhs_EdSubcat_truck",
    "side": 0,
    "typicalCargo": ["rhs_msv_driver"],
    "nameSound": "truck",
    "accuracy": 0.25,
    "weapons": ["TruckHorn"],
    "steerAheadPlan": 0.26,
    "armor": 50,
    "damageResistance": 0.00845,
    "armorWheels": 0.12,
    "driverAction": "rhs_gaz66_driver",
    "tf_hasLRradio_api": 0,
    "getInAction": "GetInLow",
    "getOutAction": "GetOutLow",
    "cargoGetInAction": ["GetInLow","GetInMRAP_01_cargo"],
    "cargoGetOutAction": ["GetOutLow","GetOutHelicopterCargo"],
    "memoryPointSupply": "pos codriver dir",
    "normalSpeedForwardCoef": 0.75,
    "slowSpeedForwardCoef": 0.45,
    "terrainCoef": 2,
    "simulation": "carx",
    "dampersBumpCoef": 2,
    "precision": 10,
    "brakeDistance": 3,
    "acceleration": 15,
    "fireResistance": 5,
    "maxSpeed": 90,
    "fuelCapacity": 40,
    "RHS_fuelCapacity": 210,
    "wheelCircumference": 3.3,
    "brakeIdleSpeed": 1,
    "maxFordingDepth": 0,
    "waterResistance": 1,
    "waterResistanceCoef": 0.15,
    "waterSpeedFactor": 0.2,
    "waterLeakiness": 10,
    # Class: CfgVehicles\rhs_truck\complexGearbox [Indent level: 1],
    "complexGearbox": {
        "GearboxRatios": ["R1",-7.9,"N",0,"D1",6.48,"D2",3.09,"D3",1.6,"D4",0.8],
        "TransmissionRatios": ["High",6.79],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R"
    },
    "changeGearMinEffectivity": [0.95,0.15,0.95,0.95,0.95,0.95],
    "switchTime": 0.83,
    "latency": 1.5,
    "differentialType": "all_limited",
    "frontRearSplit": 0.5,
    "frontBias": 1.3,
    "rearBias": 1.3,
    "centreBias": 1,
    "clutchStrength": 40,
    "transmissionLosses": 8,
    "dampingRateFullThrottle": 0.05,
    "dampingRateZeroThrottleClutchEngaged": 1.35,
    "dampingRateZeroThrottleClutchDisengaged": 0.35,
    "torqueCurve": [[0,0],[0.3125,0.897887],[0.375,0.940141],[0.5,0.961268],[0.625,1],[0.78125,1],[0.875,0.961268],[1,0.464789]],
    "enginePower": 89,
    "engineMOI": 0.95,
    "peakTorque": 568,
    "maxOmega": 335.1,
    "minOmega": 50,
    "idleRPM": 500,
    "redRPM": 3200,
    "engineLosses": 10,
    "thrustDelay": 1.5,
    "accelAidForceYOffset": -0.15,
    "antiRollbarForceCoef": 0.2,
    "antiRollbarForceLimit": 0.5,
    "antiRollbarSpeedMin": 30,
    "antiRollbarSpeedMax": 65,
    # Class: CfgVehicles\rhs_truck\Wheels [Indent level: 1],
    "Wheels": {
        # Class: CfgVehicles\rhs_truck\Wheels\LF [Indent level: 2]
        "LF": {
            "steering": 1,
            "width": 0.32,
            "side": "left",
            "boneName": "wheel_1_1_damper",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "suspForceAppPointOffset": "wheel_1_1_axis",
            "tireForceAppPointOffset": "wheel_1_1_axis",
            "suspTravelDirection": [-0.125,-1,0],
            "mass": 80,
            "MOI": 28,
            "dampingRate": 6.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 8500,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.3,
            "maxDroop": 0.25,
            "sprungMass": -1,
            "springStrength": 41938,
            "springDamperRate": 10342,
            "longitudinalStiffnessPerUnitGravity": 2986,
            "latStiffX": 25,
            "latStiffY": 30,
            "frictionVsSlipGraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles\rhs_truck\Wheels\LR [Indent level: 2],
        "LR": {
            "boneName": "wheel_1_2_damper",
            "steering": 0,
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "suspForceAppPointOffset": "wheel_1_2_axis",
            "tireForceAppPointOffset": "wheel_1_2_axis",
            "maxHandBrakeTorque": 20000,
            "latStiffX": 5,
            "width": 0.32,
            "side": "left",
            "suspTravelDirection": [-0.125,-1,0],
            "mass": 80,
            "MOI": 28,
            "dampingRate": 6.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 8500,
            "maxCompression": 0.3,
            "maxDroop": 0.25,
            "sprungMass": -1,
            "springStrength": 41938,
            "springDamperRate": 10342,
            "longitudinalStiffnessPerUnitGravity": 2986,
            "latStiffY": 30,
            "frictionVsSlipGraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles\rhs_truck\Wheels\RF [Indent level: 2],
        "RF": {
            "boneName": "wheel_2_1_damper",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "suspForceAppPointOffset": "wheel_2_1_axis",
            "tireForceAppPointOffset": "wheel_2_1_axis",
            "steering": 1,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": 0.32,
            "mass": 80,
            "MOI": 28,
            "dampingRate": 6.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 8500,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.3,
            "maxDroop": 0.25,
            "sprungMass": -1,
            "springStrength": 41938,
            "springDamperRate": 10342,
            "longitudinalStiffnessPerUnitGravity": 2986,
            "latStiffX": 25,
            "latStiffY": 30,
            "frictionVsSlipGraph": [[0,1.2],[0.5,1.13],[1,1]]
        },
        # Class: CfgVehicles\rhs_truck\Wheels\RR [Indent level: 2],
        "RR": {
            "boneName": "wheel_2_2_damper",
            "steering": 0,
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "suspForceAppPointOffset": "wheel_2_2_axis",
            "tireForceAppPointOffset": "wheel_2_2_axis",
            "maxHandBrakeTorque": 20000,
            "latStiffX": 5,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": 0.32,
            "mass": 80,
            "MOI": 28,
            "dampingRate": 6.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 8500,
            "maxCompression": 0.3,
            "maxDroop": 0.25,
            "sprungMass": -1,
            "springStrength": 41938,
            "springDamperRate": 10342,
            "longitudinalStiffnessPerUnitGravity": 2986,
            "latStiffY": 30,
            "frictionVsSlipGraph": [[0,1.2],[0.5,1.13],[1,1]]
        }
    },
    "soundAttenuationCargo": [1,0.4],
    "soundGetIn": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_int_getout",1.77828,1,9],
    "soundGetOut": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_ext_getout",2.51189,1,25],
    "soundDammage": ["",0.562341,1],
    "soundEngineOnInt": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_int_start",1.41254,1],
    "soundEngineOnExt": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_ext_start",1.41254,1,200],
    "soundEngineOffInt": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_int_stop",1.41254,1],
    "soundEngineOffExt": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|ural4320|ural4320_engine_ext_stop",1.41254,1,200],
    "buildCrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "buildCrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "buildCrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "buildCrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "soundBuildingCrash": ["buildCrash0",0.125,"buildCrash1",0.125,"buildCrash2",0.125,"buildCrash3",0.125,"buildCrash4",0.125,"buildCrash5",0.125,"buildCrash6",0.125,"buildCrash7",0.125],
    "WoodCrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_01",1.99526,1,75],
    "WoodCrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_02",1.99526,1,75],
    "WoodCrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_03",1.99526,1,75],
    "WoodCrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_04",1.99526,1,75],
    "WoodCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_05",1.99526,1,75],
    "WoodCrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_06",1.99526,1,75],
    "soundWoodCrash": ["woodCrash0",0.125,"woodCrash1",0.125,"woodCrash2",0.125,"woodCrash3",0.125,"woodCrash4",0.125,"woodCrash5",0.125,"woodCrash6",0.125,"woodCrash7",0.125],
    "ArmorCrash0": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_01",1.99526,1,75],
    "ArmorCrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_02",1.99526,1,75],
    "ArmorCrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_03",1.99526,1,75],
    "ArmorCrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_04",1.99526,1,75],
    "soundArmorCrash": ["ArmorCrash0",0.125,"ArmorCrash1",0.125,"ArmorCrash2",0.125,"ArmorCrash3",0.125,"ArmorCrash4",0.125,"ArmorCrash5",0.125,"ArmorCrash6",0.125,"ArmorCrash7",0.125],
    # Class: CfgVehicles\rhs_truck\Sounds [Indent level: 1],
    "Sounds": {
        # Class: CfgVehicles\rhs_truck\Sounds\Idle_ext [Indent level: 2]
        "Idle_ext": {
            "sound": ["|rhsafrf|addons|rhs_gaz66|data|sounds|zil_gaz66_idle.wss",0.562341,1,200],
            "frequency": "0.95	+	((rpm/	3200) factor[(100/	3200),(800/	3200)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	3200) factor[(10/	3200),(50/	3200)])	*	((rpm/	3200) factor[(800/	3200),(600/	3200)]))*2.0"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\Engine [Indent level: 2],
        "Engine": {
            "sound": ["|rhsafrf|addons|rhs_gaz66|data|sounds|zil_gaz66_driving.wss",0.630957,1,200],
            "frequency": "0.85	+	((rpm/	3200) factor[(610/	3200),(3200/	3200)])*0.95",
            "volume": "engineOn*camPos*(((rpm/	3200) factor[(620/	3200),(820/	3200)])	*	((rpm/	3200) factor[(3200/	3200),(3200/	3200)]))*2.0"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\EngineThrust [Indent level: 2],
        "EngineThrust": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|ext_exhaust_01",0.630957,1,200],
            "frequency": "0.85	+	((rpm/	3200) factor[(610/	3200),(6400/	3200)])*0.75",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.3,1])))*(((rpm/	3200) factor[(620/	3200),(820/	3200)])	*	((rpm/	3200) factor[(3200/	3200),(3200/	3200)]))*1.5"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\Idle_int [Indent level: 2],
        "Idle_int": {
            "sound": ["|rhsafrf|addons|rhs_gaz66|data|sounds|Zil_GAz66__Int_Idle.wss",0.562341,1,200],
            "frequency": "0.8	+	((rpm/	3200) factor[(500/	3200),(800/	3200)])*0.25",
            "volume": "engineOn*(1-camPos)*(((rpm/	3200) factor[(10/	3200),(50/	3200)])	*	((rpm/	3200) factor[(800/	3200),(600/	3200)]))*2"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\Engine_int [Indent level: 2],
        "Engine_int": {
            "sound": ["|rhsafrf|addons|rhs_gaz66|data|sounds|Zil_Gaz66_Int_Driving.wss",0.562341,1,200],
            "frequency": "0.85	+	((rpm/	3200) factor[(610/	3200),(6400/	3200)])*0.95",
            "volume": "engineOn*(1-camPos)*(((rpm/    3200) factor[(400/    3200),(600/    3200)])    *    ((rpm/    3200) factor[(3200/    3200),(3200/    3200)]))*2.0"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\EngineThrust_int [Indent level: 2],
        "EngineThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|Truck_02|int_exhaust_01",0.630957,1,200],
            "frequency": "0.85	+	((rpm/	3200) factor[(610/	3200),(3200/	3200)])*0.75",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.3,1])))*(((rpm/	3200) factor[(620/	3200),(820/	3200)])	*	((rpm/	3200) factor[(3200/	3200),(3200/	3200)]))*2"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\Movement [Indent level: 2],
        "Movement": {
            "sound": "soundEnviron",
            "frequency": "1",
            "volume": "0"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresRockOut [Indent level: 2],
        "TiresRockOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_1",1,1,60],
            "frequency": "1",
            "volume": "camPos*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresSandOut [Indent level: 2],
        "TiresSandOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-sand1",1,1,60],
            "frequency": "1",
            "volume": "camPos*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresGrassOut [Indent level: 2],
        "TiresGrassOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_2",1,1,60],
            "frequency": "1",
            "volume": "camPos*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresMudOut [Indent level: 2],
        "TiresMudOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-mud2",1,1,60],
            "frequency": "1",
            "volume": "camPos*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresGravelOut [Indent level: 2],
        "TiresGravelOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_gravel_1",1,1,60],
            "frequency": "1",
            "volume": "camPos*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresAsphaltOut [Indent level: 2],
        "TiresAsphaltOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_asfalt_2",1,1,60],
            "frequency": "1",
            "volume": "camPos*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\NoiseOut [Indent level: 2],
        "NoiseOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_int_car_3",1,1,90],
            "frequency": "1",
            "volume": "camPos*(damper0 max 0.02)*(speed factor[0, 8])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresRockIn [Indent level: 2],
        "TiresRockIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_1",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresSandIn [Indent level: 2],
        "TiresSandIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-sand2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresGrassIn [Indent level: 2],
        "TiresGrassIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresMudIn [Indent level: 2],
        "TiresMudIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-mud2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresGravelIn [Indent level: 2],
        "TiresGravelIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_gravel_1",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\TiresAsphaltIn [Indent level: 2],
        "TiresAsphaltIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_asfalt_2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\NoiseIn [Indent level: 2],
        "NoiseIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_int_car_3",0.707946,1],
            "frequency": "1",
            "volume": "(damper0 max 0.1)*(speed factor[0, 8])*(1-camPos)"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\breaking_ext_road [Indent level: 2],
        "breaking_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 10])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\acceleration_ext_road [Indent level: 2],
        "acceleration_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\turn_left_ext_road [Indent level: 2],
        "turn_left_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\turn_right_ext_road [Indent level: 2],
        "turn_right_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\breaking_ext_dirt [Indent level: 2],
        "breaking_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_14_dirt_breaking",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 10])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\acceleration_ext_dirt [Indent level: 2],
        "acceleration_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|acceleration_dirt_ext_1",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\turn_left_ext_dirt [Indent level: 2],
        "turn_left_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\turn_right_ext_dirt [Indent level: 2],
        "turn_right_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\breaking_int_road [Indent level: 2],
        "breaking_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 6])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\acceleration_int_road [Indent level: 2],
        "acceleration_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\turn_left_int_road [Indent level: 2],
        "turn_left_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\turn_right_int_road [Indent level: 2],
        "turn_right_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\breaking_int_dirt [Indent level: 2],
        "breaking_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_14_dirt_breaking_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 6])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\acceleration_int_dirt [Indent level: 2],
        "acceleration_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|acceleration_dirt_int_1",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\turn_left_int_dirt [Indent level: 2],
        "turn_left_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\turn_right_int_dirt [Indent level: 2],
        "turn_right_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\RainIn [Indent level: 2],
        "RainIn": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|rain.wss",1.41254,1],
            "frequency": 1,
            "volume": "rain*(1-camPos)"
        },
        # Class: CfgVehicles\rhs_truck\Sounds\RainExt [Indent level: 2],
        "RainExt": {
            "sound": ["rhsafrf|addons|rhs_a2port_car|sounds|rain.wss",1.41254,1],
            "frequency": 1,
            "volume": "rain*camPos"
        },
        "soundSetsInt": ["RHS_gaz66_Engine_RPM0_INT_SoundSet","RHS_gaz66_Engine_RPM1_INT_SoundSet","RHS_gaz66_Engine_RPM2_INT_SoundSet","RHS_gaz66_Engine_RPM3_INT_SoundSet","gaz66_Rattling_INT_SoundSet","gaz66_Stress_INT_SoundSet","gaz66_Rain_INT_SoundSet","RHS_gaz66_Tires_Rock_Fast_INT_SoundSet","RHS_gaz66_Tires_Grass_Fast_INT_SoundSet","RHS_gaz66_Tires_Sand_Fast_INT_SoundSet","RHS_gaz66_Tires_Gravel_Fast_INT_SoundSet","RHS_gaz66_Tires_Mud_Fast_INT_SoundSet","RHS_gaz66_Tires_Asphalt_Fast_INT_SoundSet","RHS_gaz66_Tires_Water_Fast_INT_SoundSet","RHS_gaz66_Tires_Rock_Slow_INT_SoundSet","RHS_gaz66_Tires_Grass_Slow_INT_SoundSet","RHS_gaz66_Tires_Sand_Slow_INT_SoundSet","RHS_gaz66_Tires_Gravel_Slow_INT_SoundSet","RHS_gaz66_Tires_Mud_Slow_INT_SoundSet","RHS_gaz66_Tires_Asphalt_Slow_INT_SoundSet","RHS_gaz66_Tires_Water_Slow_INT_SoundSet","RHS_gaz66_Tires_Turn_Hard_INT_SoundSet","RHS_gaz66_Tires_Turn_Soft_INT_SoundSet","RHS_gaz66_Tires_Brake_Hard_INT_SoundSet","RHS_gaz66_Tires_Brake_Soft_INT_SoundSet"],
        "soundSetsExt": ["RHS_gaz66_Engine_RPM0_EXT_SoundSet","RHS_gaz66_Engine_RPM1_EXT_SoundSet","RHS_gaz66_Engine_RPM2_EXT_SoundSet","RHS_gaz66_Engine_RPM3_EXT_SoundSet","gaz66_Rattling_EXT_SoundSet","gaz66_Stress_EXT_SoundSet","gaz66_Rain_EXT_SoundSet","RHS_gaz66_Tires_Rock_Fast_EXT_SoundSet","RHS_gaz66_Tires_Grass_Fast_EXT_SoundSet","RHS_gaz66_Tires_Sand_Fast_EXT_SoundSet","RHS_gaz66_Tires_Gravel_Fast_EXT_SoundSet","RHS_gaz66_Tires_Mud_Fast_EXT_SoundSet","RHS_gaz66_Tires_Asphalt_Fast_EXT_SoundSet","RHS_gaz66_Tires_Water_Fast_EXT_SoundSet","RHS_gaz66_Tires_Rock_Slow_EXT_SoundSet","RHS_gaz66_Tires_Grass_Slow_EXT_SoundSet","RHS_gaz66_Tires_Sand_Slow_EXT_SoundSet","RHS_gaz66_Tires_Gravel_Slow_EXT_SoundSet","RHS_gaz66_Tires_Mud_Slow_EXT_SoundSet","RHS_gaz66_Tires_Asphalt_Slow_EXT_SoundSet","RHS_gaz66_Tires_Water_Slow_EXT_SoundSet","RHS_gaz66_Tires_Turn_Hard_EXT_SoundSet","RHS_gaz66_Tires_Turn_Soft_EXT_SoundSet","RHS_gaz66_Tires_Brake_Hard_EXT_SoundSet","RHS_gaz66_Tires_Brake_Soft_EXT_SoundSet"]
    },
    "cargoAction": ["rhs_passenger_apc_narrow_generic01","rhs_passenger_apc_narrow_generic03still","rhs_passenger_apc_narrow_generic03","passenger_generic01_leanright","rhs_passenger_apc_generic01","rhs_passenger_apc_generic01","rhs_passenger_apc_generic03","rhs_passenger_apc_narrow_generic01","passenger_generic01_leanleft","rhs_passenger_apc_generic03","rhs_passenger_apc_narrow_generic02","rhs_passenger_apc_generic02","rhs_passenger_apc_generic01","passenger_generic01_foldhands","rhs_passenger_apc_generic04","passenger_generic01_leanleft"],
    "cargoIsCoDriver": [1,1,0],
    "initCargoAngleY": 180,
    "driverCompartments": 1,
    "cargoCompartments": [1,2],
    "viewCargoShadow": 1,
    "viewCargoShadowDiff": 0.05,
    "wheelDamageRadiusCoef": 0.9,
    "wheelDestroyRadiusCoef": 0.4,
    "crewCrashProtection": 0.25,
    "driverLeftHandAnimName": "drivewheel",
    "driverRightHandAnimName": "drivewheel",
    "memoryPointsGetInDriver": "pos driver",
    "memoryPointsGetInDriverDir": "pos driver dir",
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInCargo": ["pos codriver","pos cargo"],
    "memoryPointsGetInCargoDir": ["pos codriver dir","pos cargo dir"],
    "driverDoor": "Door_LF",
    "cargoDoors": ["Door_RF",""],
    "slingLoadCargoMemoryPoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "slingLoadCargoMemoryPointsDir": ["SlingLoadCargo1_dir","SlingLoadCargo2_dir","SlingLoadCargo3_dir","SlingLoadCargo4_dir"],
    "hiddenSelections": ["camo1","camo2","camo3","camo4","camo5","n1","n2","n3","n4","i1","i2","i3","i4"],
    "hiddenSelectionsTextures": ["|rhsafrf|addons|rhs_gaz66|data|gaz66_co.paa","|rhsafrf|addons|rhs_gaz66|data|tent_co.paa","|rhsafrf|addons|rhs_gaz66|data|rhs_gaz66_kung_co.paa","|rhsafrf|addons|rhs_gaz66|data|rhs_gaz66_ap2kung_co.paa","|rhsafrf|addons|rhs_gaz66|data|rhs_gaz66_repkung_co.paa","rhsafrf|addons|RHS_Decals|Data|Labels|Misc|no_ca.paa"],
    # Class: CfgVehicles\rhs_truck\textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles\rhs_truck\textureSources\standard [Indent level: 2]
        "standard": {
            "displayName": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_gaz66|data|gaz66_co.paa","|rhsafrf|addons|rhs_gaz66|data|tent_co.paa","|rhsafrf|addons|rhs_gaz66|data|rhs_gaz66_kung_co.paa","|rhsafrf|addons|rhs_gaz66|data|rhs_gaz66_ap2kung_co.paa","|rhsafrf|addons|rhs_gaz66|data|rhs_gaz66_repkung_co.paa"]
        },
        # Class: CfgVehicles\rhs_truck\textureSources\camo [Indent level: 2],
        "camo": {
            "displayName": "3-Color Camo",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_gaz66|data|gaz66ru_co.paa","|rhsafrf|addons|rhs_gaz66|data|tentru_co.paa"]
        },
        # Class: CfgVehicles\rhs_truck\textureSources\cdf [Indent level: 2],
        "cdf": {
            "displayName": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_gaz66|data|gaz66_cdf_co.paa","|rhsafrf|addons|rhs_gaz66|data|tent_cdf_co.paa"]
        },
        # Class: CfgVehicles\rhs_truck\textureSources\chdkz [Indent level: 2],
        "chdkz": {
            "displayName": "ChDKZ",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_gaz66|data|gaz66_chdk_co.paa","|rhsafrf|addons|rhs_gaz66|data|tent_chdk_co.paa"]
        },
        # Class: CfgVehicles\rhs_truck\textureSources\rhs_sand [Indent level: 2],
        "rhs_sand": {
            "displayName": "Sand",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_gaz66_camo|data|gaz66_sand_co.paa","|rhsafrf|addons|rhs_gaz66|data|tent_co.paa","|rhsafrf|addons|rhs_gaz66_camo|data|rhs_gaz66_kung_sand_co.paa","|rhsafrf|addons|rhs_gaz66_camo|data|rhs_gaz66_ap2kung_sand_co.paa","|rhsafrf|addons|rhs_gaz66_camo|data|rhs_gaz66_repkung_sand_co.paa"]
        }
    },
    "textureList": [],
    # Class: CfgVehicles\rhs_truck\HitPoints [Indent level: 1],
    "HitPoints": {
        # Class: CfgVehicles\rhs_truck\HitPoints\HitBody [Indent level: 2]
        "HitBody": {
            "name": "karoserie",
            "armor": 1,
            "material": -1,
            "visual": "zbytek",
            "passThrough": 1,
            "explosionShielding": 1.5
        },
        # Class: CfgVehicles\rhs_truck\HitPoints\HitFuel [Indent level: 2],
        "HitFuel": {
            "name": "palivo",
            "armor": 0.3,
            "material": -1,
            "visual": "-",
            "passThrough": 0.1,
            "explosionShielding": 1.5
        },
        # Class: CfgVehicles\rhs_truck\HitPoints\HitLFWheel [Indent level: 2],
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
        # Class: CfgVehicles\rhs_truck\HitPoints\HitLF2Wheel [Indent level: 2],
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
        # Class: CfgVehicles\rhs_truck\HitPoints\HitRFWheel [Indent level: 2],
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
        # Class: CfgVehicles\rhs_truck\HitPoints\HitRF2Wheel [Indent level: 2],
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
        # Class: CfgVehicles\rhs_truck\HitPoints\HitSpare [Indent level: 2],
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
        # Class: CfgVehicles\rhs_truck\HitPoints\UseSpare [Indent level: 2],
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
        # Class: CfgVehicles\rhs_truck\HitPoints\HitEngine [Indent level: 2],
        "HitEngine": {
            "name": "motor",
            "armor": 0.4,
            "passThrough": 0.2,
            # Class: CfgVehicles\rhs_truck\HitPoints\HitEngine\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_truck\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke [Indent level: 4],
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_truck\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1 [Indent level: 4],
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_truck\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2 [Indent level: 4],
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_truck\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds [Indent level: 4],
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "SmokeWreck1",
                    "position": "engine_smoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                }
            },
            "material": -1,
            "visual": "",
            "explosionShielding": 0.5
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
        # Class: CfgVehicles\Car_F\HitPoints\HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "armor": 0.1,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "armor": 0.1,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitGlass3 [Indent level: 2],
        "HitGlass3": {
            "armor": 0.1,
            "material": -1,
            "name": "glass3",
            "visual": "glass3",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitGlass4 [Indent level: 2],
        "HitGlass4": {
            "armor": 0.1,
            "material": -1,
            "name": "glass4",
            "visual": "glass4",
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
        # Class: CfgVehicles\Car_F\HitPoints\HitLBWheel [Indent level: 2],
        "HitLBWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_4_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitLMWheel [Indent level: 2],
        "HitLMWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_3_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitRBWheel [Indent level: 2],
        "HitRBWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_4_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitRMWheel [Indent level: 2],
        "HitRMWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_3_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
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
        },
        # Class: CfgVehicles\Car_F\HitPoints\AnimationSources [Indent level: 2],
        "AnimationSources": {
        }
    },
    # Class: CfgVehicles\rhs_truck\ViewPilot [Indent level: 1],
    "ViewPilot": {
        "initFov": 0.7,
        "minFov": 0.25,
        "maxFov": 1.4,
        "initAngleX": -15,
        "minAngleX": -65,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -150,
        "maxAngleY": 150,
        "minMoveX": -0.5,
        "maxMoveX": 0.5,
        "minMoveY": -0.025,
        "maxMoveY": 0.1,
        "minMoveZ": -0.3,
        "maxMoveZ": 0.5,
        "speedZoomMaxSpeed": 0,
        "speedZoomMaxFOV": 0.7
    },
    # Class: CfgVehicles\rhs_truck\Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles\rhs_truck\Reflectors\LSvetla [Indent level: 2]
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
            # Class: CfgVehicles\rhs_truck\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_truck\Reflectors\RSvetla [Indent level: 2],
        "RSvetla": {
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "innerAngle": 30,
            "outerAngle": 100,
            "coneFadeCoef": 10,
            "intensity": 1.5,
            "useFlare": 1,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhs_truck\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_truck\Reflectors\Right2 [Indent level: 2],
        "Right2": {
            "position": "Light_R_Flare",
            "direction": "Light_R_Flare_end",
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhs_truck\Reflectors\Right2\Attenuation [Indent level: 3],
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
        # Class: CfgVehicles\rhs_truck\Reflectors\Left2 [Indent level: 2],
        "Left2": {
            "position": "Light_L_Flare",
            "direction": "Light_L_Flare_end",
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhs_truck\Reflectors\Left2\Attenuation [Indent level: 3],
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
        # Class: CfgVehicles\rhs_truck\Reflectors\Searchlight [Indent level: 2],
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
            # Class: CfgVehicles\rhs_truck\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_truck\Reflectors\Long_Left [Indent level: 2],
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
            # Class: CfgVehicles\rhs_truck\Reflectors\Long_Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\rhs_truck\Reflectors\Long_Right [Indent level: 2],
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
            # Class: CfgVehicles\rhs_truck\Reflectors\Long_Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\rhs_truck\Reflectors\Long_Right2 [Indent level: 2],
        "Long_Right2": {
            "useFlare": 1,
            "position": "light_R_Long_flare",
            "innerAngle": 50,
            "outerAngle": 139,
            "coneFadeCoef": 51,
            "flareSize": 1,
            "intensity": 1,
            # Class: CfgVehicles\rhs_truck\Reflectors\Long_Right2\Attenuation [Indent level: 3],
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
        # Class: CfgVehicles\rhs_truck\Reflectors\Long_Left2 [Indent level: 2],
        "Long_Left2": {
            "useFlare": 1,
            "position": "light_L_Long_flare",
            "innerAngle": 50,
            "outerAngle": 139,
            "coneFadeCoef": 51,
            "flareSize": 1,
            "intensity": 1,
            # Class: CfgVehicles\rhs_truck\Reflectors\Long_Left2\Attenuation [Indent level: 3],
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
        # Class: CfgVehicles\rhs_truck\Reflectors\cabin [Indent level: 2],
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
            # Class: CfgVehicles\rhs_truck\Reflectors\cabin\Attenuation [Indent level: 3],
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
    "aggregateReflectors": [[]],
    # Class: CfgVehicles\rhs_truck\RenderTargets [Indent level: 1],
    "RenderTargets": {
        # Class: CfgVehicles\rhs_truck\RenderTargets\LeftMirror [Indent level: 2]
        "LeftMirror": {
            "renderTarget": "rendertarget0",
            # Class: CfgVehicles\rhs_truck\RenderTargets\LeftMirror\CameraView1 [Indent level: 3],
            "CameraView1": {
                "pointPosition": "m1p",
                "pointDirection": "m1d",
                "renderQuality": 2,
                "renderVisionMode": 4,
                "fov": 0.7
            },
            "BBoxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles\rhs_truck\RenderTargets\RightMirror [Indent level: 2],
        "RightMirror": {
            "renderTarget": "rendertarget1",
            # Class: CfgVehicles\rhs_truck\RenderTargets\RightMirror\CameraView1 [Indent level: 3],
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
    # Class: CfgVehicles\rhs_truck\Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles\rhs_truck\Exhausts\Exhaust1 [Indent level: 2]
        "Exhaust1": {
            "position": "vyfuk start",
            "direction": "vyfuk konec",
            "effect": "ExhaustEffectHTruck"
        }
    },
    # Class: CfgVehicles\rhs_truck\UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles\rhs_truck\UserActions\wiperson [Indent level: 2]
        "wiperson": {
            "displayName": "Wipers on",
            "position": "",
            "radius": 12,
            "showWindow": 0,
            "onlyForplayer": 1,
            "condition": "Alive(this) AND (player == driver this) AND isengineon (this) AND this animationPhase 'wipers' < 0.5",
            "statement": "[this,0] spawn rhs_fnc_wipers"
        },
        # Class: CfgVehicles\rhs_truck\UserActions\wipersoff [Indent level: 2],
        "wipersoff": {
            "displayName": "Wipers off",
            "condition": "Alive(this) AND (player == driver this) AND this animationPhase 'wipers' > 0.5",
            "statement": "[this,1] spawn rhs_fnc_wipers",
            "position": "",
            "radius": 12,
            "showWindow": 0,
            "onlyForplayer": 1
        },
        # Class: CfgVehicles\rhs_truck\UserActions\lights_toggle [Indent level: 2],
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
        # Class: CfgVehicles\rhs_truck\UserActions\cabinlights_toggle [Indent level: 2],
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
        # Class: CfgVehicles\rhs_truck\UserActions\searchlight_toggle [Indent level: 2],
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
        # Class: CfgVehicles\rhs_truck\UserActions\searchlight_adjust [Indent level: 2],
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
    # Class: CfgVehicles\rhs_truck\Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles\rhs_truck\Attributes\ObjectTexture [Indent level: 2]
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber_type [Indent level: 2],
        "rhs_decalNumber_type": {
            "displayName": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cTrucksGaz4NumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber_type\values\Default [Indent level: 4]
                "Default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultValue": "Default"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber_type\values\DefaultRed [Indent level: 4],
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber_type\values\BoldRed [Indent level: 4],
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber_type\values\CDF [Indent level: 4],
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber_type\values\Handpaint [Indent level: 4],
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber_type\values\HandpaintBlack [Indent level: 4],
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber_type\values\Iraqi [Indent level: 4],
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber_type\values\LicensePlate [Indent level: 4],
                "LicensePlate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalNumber [Indent level: 2],
        "rhs_decalNumber": {
            "collapsed": 1,
            "displayName": "Set plate number",
            "tooltip": "Set plate number. 4 numbers are required. If 0, random number will be generated",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typeName": "Number",
            "defaultValue": "-1",
            "expression": "if( _value >= 0)then{[_this,[['Number', cTrucksGaz4NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value]]] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type [Indent level: 2],
        "rhs_decalArmy_type": {
            "displayName": "Define large door roundel type",
            "tooltip": "Decal type",
            "property": "rhs_decalArmy_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\Army [Indent level: 4]
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "Army"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\Honor [Indent level: 4],
                "Honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\HonorGDR [Indent level: 4],
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\Platoon [Indent level: 4],
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\PlatoonGDR [Indent level: 4],
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\PlatoonVDV [Indent level: 4],
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        },
        # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy [Indent level: 2],
        "rhs_decalArmy": {
            "displayName": "Set large door roundel symbol",
            "tooltip": "Set large door roundel located on both sides. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalArmy",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cTrucksGazRightArmyPlaces,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalPlatoon_type [Indent level: 2],
        "rhs_decalPlatoon_type": {
            "displayName": "Define small door roundel type",
            "property": "rhs_decalPlatoon_type",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "tooltip": "Decal type",
            "control": "Combo",
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\Army [Indent level: 4]
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "Army"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\Honor [Indent level: 4],
                "Honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\HonorGDR [Indent level: 4],
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\Platoon [Indent level: 4],
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\PlatoonGDR [Indent level: 4],
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalArmy_type\values\PlatoonVDV [Indent level: 4],
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        },
        # Class: CfgVehicles\rhs_truck\Attributes\rhs_decalPlatoon [Indent level: 2],
        "rhs_decalPlatoon": {
            "displayName": "Set small door roundel symbol",
            "tooltip": "Define small door roundel located on both sides. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cTrucksGazRightPlatoonPlaces,  _this getVariable ['rhs_decalPlatoon_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\rhs_truck\Attributes\rhs_hideLightCover [Indent level: 2],
        "rhs_hideLightCover": {
            "displayName": "Hide light covers",
            "property": "rhs_hideLightCover",
            "control": "CheckboxNumber",
            "expression": "_this animate ['light_hide',_value,true]",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhs_truck\Attributes\rhs_hidespare [Indent level: 2],
        "rhs_hidespare": {
            "displayName": "Remove spare wheel",
            "property": "rhs_hidespare",
            "expression": "_this animate ['spare_hide',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        }
    },
    "cargoProxyIndexes": [1,2,3,4,5,6,7,8,10,11],
    "getInProxyOrder": [1,2,3,4,5,6,7,8,9,10,11,12,13],
    # Class: CfgVehicles\rhs_truck\EventHandlers [Indent level: 1],
    "EventHandlers": {
        # Class: CfgVehicles\rhs_truck\EventHandlers\RHS_EventHandlers [Indent level: 2]
        "RHS_EventHandlers": {
            "init": "_this call rhs_fnc_gaz66_init",
            "dammaged": "_this call rhs_fnc_wheelDamaged"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
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
    "attenuationEffectType": "TruckAttenuation",
    "buildCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "buildCrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "buildCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "buildCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "WoodCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_07",1.99526,1,75],
    "WoodCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_08",1.99526,1,75],
    "armorCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "armorCrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "armorCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "armorCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
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
    "ace_refuel_fuelCapacity": 210,
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
    "_generalMacro": "Truck_F",
    "fuelExplosionPower": 5,
    "supplyRadius": 2.5,
    "audible": 9,
    "turnCoef": 5,
    "epeImpulseDamageCoef": 15,
    "crewExplosionProtection": 0.8,
    "maximumLoad": 3000,
    "transportMaxBackpacks": 64,
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
    "ace_refuel_flowRate": 2,
    "ace_cargo_space": 8,
    "ace_cargo_hasCargo": 1,
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
    "secondaryExplosion": -10,
    "dammageHalf": [],
    "dammageFull": [],
    "armorStructural": 4,
    "explosionShielding": 1,
    "minTotalDamageThreshold": 0.01,
    "gunnerHasFlares": 0,
    "steerAheadSimul": 0.5,
    "predictTurnPlan": 2,
    "predictTurnSimul": 1.5,
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
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
        "showCrewAim": 0,
        "ace_fcs_Enabled": 0,
        "ace_fcs_MinDistance": 200,
        "ace_fcs_MaxDistance": 5500,
        "ace_fcs_DistanceInterval": 5
    },
    "driverLeftLegAnimName": "",
    "driverRightLegAnimName": "pedal_thrust",
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
    "viewCargoShadowAmb": 1,
    "magazines": [],
    "soundEnviron": ["",0.000562341,1],
    "soundCrash": ["A3|sounds_f|dummysound",1,1],
    "extCameraPosition": [0.5,2,-10],
    "soundGear": ["",1e-005,1],
    "collisionEffect": "collisionEffect",
    "hideUnitInfo": 0,
    "htMin": 60,
    "htMax": 1800,
    "afMax": 100,
    "mfMax": 80,
    "mFact": 1,
    "tBody": 150,
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
    # Class: CfgVehicles\Car_F\ViewCargo [Indent level: 1],
    "ViewCargo": {
        "initFov": 0.7,
        "minFov": 0.25,
        "maxFov": 1.4,
        "initAngleX": 0,
        "minAngleX": -75,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -170,
        "maxAngleY": 170,
        "minMoveX": -0.5,
        "maxMoveX": 0.5,
        "minMoveY": -0.025,
        "maxMoveY": 0.1,
        "minMoveZ": -0.3,
        "maxMoveZ": 0.5,
        "speedZoomMaxSpeed": 0,
        "speedZoomMaxFOV": 0.7
    },
    # Class: CfgVehicles\Car_F\ViewOptics [Indent level: 1],
    "ViewOptics": {
        "initFov": 0.7,
        "minFov": 0.25,
        "maxFov": 1.4,
        "initAngleX": 0,
        "minAngleX": -75,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -170,
        "maxAngleY": 170,
        "minMoveX": -0.5,
        "maxMoveX": 0.5,
        "minMoveY": -0.025,
        "maxMoveY": 0.1,
        "minMoveZ": -0.3,
        "maxMoveZ": 0.5,
        "speedZoomMaxSpeed": 0,
        "speedZoomMaxFOV": 0.7
    },
    "cost": 40000,
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
    "memoryPointTrackFLL": "Stopa PLL",
    "memoryPointTrackFLR": "Stopa PLP",
    "memoryPointTrackBLL": "Stopa ZLL",
    "memoryPointTrackBLR": "Stopa ZLP",
    "memoryPointTrackFRL": "Stopa PPL",
    "memoryPointTrackFRR": "Stopa PPP",
    "memoryPointTrackBRL": "Stopa ZPL",
    "memoryPointTrackBRR": "Stopa ZPP",
    "memoryPointCirculumReference": "circulumReference",
    "gearBox": [-8,0,10,6.15,4.44,3.33],
    "Scudeffect": "ScudEffect",
    "armorLights": 0.4,
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
    "rightDustEffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffects"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffects"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"],["CRGrass1","RDustEffects"],["CRGrass1","RGrassEffects"],["CRGrass1","RDirtEffects"],["CRGrass2","RDustEffects"],["CRGrass2","RGrassEffects"],["CRGrass2","RDirtEffects"],["CRGrassW1","RDustEffects"],["CRGrassW1","RGrassEffects"],["CRGrassW1","RDirtEffects"],["CRGrassW2","RDustEffects"],["CRGrassW2","RGrassEffects"],["CRGrassW2","RDirtEffects"],["CRField1","RDustEffects"],["CRField1","RGrassEffects"],["CRField1","RDirtEffects"],["CRField2","RDustEffects"],["CRField2","RGrassEffects"],["CRField2","RDirtEffects"],["CRForest1","RDustEffects"],["CRForest1","RGrassEffects"],["CRForest1","RDirtEffects"],["CRForest2","RDustEffects"],["CRForest2","RGrassEffects"],["CRForest2","RDirtEffects"],["CRGrit1","RDustEffects"],["CRGrit1","RDirtEffects"],["CRHeather","RDustEffects"],["CRHeather","RGrassEffects"],["CRHeather","RDirtEffects"],["CRConcrete","RDirtEffects"],["TKAsfalt","RDirtEffects"],["TKBeton","RDustEffects"],["TKPlevel","RDustEffects"],["TKPlevel","RGrassEffects"],["TKPlevel","RDirtEffects"],["TKPole","RDustEffects"],["TKPole","RGrassDryEffects"],["TKPole","RDirtEffects"],["TKPolopoust","RDustEffects"],["TKPolopoust","RSandEffects"],["TKPolopoust","RDirtEffects"],["TKSkala","RDustEffects"],["TKSkala","RStonesEffects"],["TKSkalniSterk","RDustEffects"],["TKSkalniSterk","RStonesEffects"],["TKSterkNaDno","RDustEffects"],["TKSterkNaDno","RStonesEffects"],["TKMoutain","RDustEffects"],["TKMoutain","RStonesEffects"],["TKValouny","RDustEffects"],["TKValouny","RStonesEffects"],["TKTrava","RDustEffects"],["TKTrava","RGrassDryEffects"],["TKTrava","RDirtEffects"],["TKForest","RDustEffects"],["TKForest","RGrassDryEffects"],["TKForest","RDirtEffects"],["ZRAsfalt","RDirtEffects"],["ZRBeton","RDustEffects"],["RoadDirt_EP1","RDustEffects"],["RoadTarmac_EP1","RDirtEffects"],["ZRPlevel","RDustEffects"],["ZRPlevel","RGrassEffects"],["ZRPlevel","RDirtEffects"],["ZRPole","RDustEffects"],["ZRPole","RGrassDryEffects"],["ZRPole","RDirtEffects"],["ZRPolopoust","RDustEffects"],["ZRPolopoust","RSandEffects"],["ZRPolopoust","RDirtEffects"],["ZRSkala","RDustEffects"],["ZRSkala","RStonesEffects"],["ZRSkalniSterk","RDustEffects"],["ZRSkalniSterk","RStonesEffects"],["ZRSterkNaDno","RDustEffects"],["ZRSterkNaDno","RStonesEffects"],["ZRValouny","RDustEffects"],["ZRValouny","RStonesEffects"],["ZRTrava","RDustEffects"],["ZRTrava","RGrassDryEffects"],["ZRTrava","RDirtEffects"],["DEPolopoust","RDustEffects"],["DEPolopoust","RSandEffects"],["DEPolopoust","RDirtEffects"],["DESkalniSterk","RDustEffects"],["DESkalniSterk","RStonesEffects"],["DETrava","RDustEffects"],["DETrava","RGrassDryEffects"],["DETrava","RDirtEffects"],["WLGrass1","RDustEffects"],["WLGrass1","RGrassEffects"],["WLGrass1","RDirtEffects"],["WLGrass2","RDustEffects"],["WLGrass2","RGrassEffects"],["WLGrass2","RDirtEffects"],["WLGrassW1","RDustEffects"],["WLGrassW1","RGrassEffects"],["WLGrassW1","RDirtEffects"],["WLGrassW2","RDustEffects"],["WLGrassW2","RGrassEffects"],["WLGrassW2","RDirtEffects"],["WLField1","RDustEffects"],["WLField1","RGrassEffects"],["WLField1","RDirtEffects"],["WLField2","RDustEffects"],["WLField2","RGrassEffects"],["WLField2","RDirtEffects"],["WLForest1","RDustEffects"],["WLForest1","RGrassEffects"],["WLForest1","RDirtEffects"],["WLForest2","RDustEffects"],["WLForest2","RGrassEffects"],["WLForest2","RDirtEffects"],["WLMudGround","RDustEffects"],["WLMudGround","RGrassEffects"],["WLMudGround","RDirtEffects"],["WLGrit1","RDustEffects"],["WLGrit1","RDirtEffects"],["WLHeather","RDustEffects"],["WLHeather","RGrassEffects"],["WLHeather","RDirtEffects"],["WLConcrete","RDirtEffects"],["GZTrava","RDustEffects"],["GZTrava","RGrassDryEffects"],["GZTrava","RDirtEffects"],["GZforest","RDustEffects"],["GZforest","RGrassDryEffects"],["GZforest","RDirtEffects"],["GZkameny","RDustEffects"],["GZkameny","RStonesEffects"],["GZHlina","RDustEffects"],["GZHlina","RGrassEffects"],["GZHlina","RDirtEffects"],["BetonNew","RDirtEffects"],["Asf1","RDirtEffects"],["Asf2","RDirtEffects"],["Asf3","RDirtEffects"],["road","RDustEffects"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffects"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffects"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","LDustEffects"],["CRGrass1","LDustEffects"],["CRGrass1","LGrassEffects"],["CRGrass1","LDirtEffects"],["CRGrass2","LDustEffects"],["CRGrass2","LGrassEffects"],["CRGrass2","LDirtEffects"],["CRGrassW1","LDustEffects"],["CRGrassW1","LGrassEffects"],["CRGrassW1","LDirtEffects"],["CRGrassW2","LDustEffects"],["CRGrassW2","LGrassEffects"],["CRGrassW2","LDirtEffects"],["CRField1","LDustEffects"],["CRField1","LGrassEffects"],["CRField1","LDirtEffects"],["CRField2","LDustEffects"],["CRField2","LGrassEffects"],["CRField2","LDirtEffects"],["CRForest1","LDustEffects"],["CRForest1","LGrassEffects"],["CRForest1","LDirtEffects"],["CRForest2","LDustEffects"],["CRForest2","LGrassEffects"],["CRForest2","LDirtEffects"],["CRGrit1","LDustEffects"],["CRGrit1","LDirtEffects"],["CRHeather","LDustEffects"],["CRHeather","LGrassEffects"],["CRHeather","LDirtEffects"],["CRConcrete","LDirtEffects"],["TKAsfalt","LDirtEffects"],["TKBeton","LDustEffects"],["RoadDirt_EP1","LDustEffects"],["RoadTarmac_EP11","LDirtEffects"],["TKPlevel","LDustEffects"],["TKPlevel","LGrassEffects"],["TKPlevel","LDirtEffects"],["TKPole","LDustEffects"],["TKPole","LGrassDryEffects"],["TKPole","LDirtEffects"],["TKPolopoust","LDustEffects"],["TKPolopoust","LSandEffects"],["TKPolopoust","LDirtEffects"],["TKSkala","LDustEffects"],["TKSkala","LStonesEffects"],["TKSkalniSterk","LDustEffects"],["TKSkalniSterk","LStonesEffects"],["TKSterkNaDno","LDustEffects"],["TKSterkNaDno","LStonesEffects"],["TKMoutain","LDustEffects"],["TKMoutain","LStonesEffects"],["TKValouny","LDustEffects"],["TKValouny","LStonesEffects"],["TKTrava","LDustEffects"],["TKTrava","LGrassDryEffects"],["TKTrava","LDirtEffects"],["TKForest","LDustEffects"],["TKForest","LGrassDryEffects"],["TKForest","LDirtEffects"],["ZRAsfalt","LDirtEffects"],["ZRBeton","LDustEffects"],["ZRPlevel","LDustEffects"],["ZRPlevel","LGrassEffects"],["ZRPlevel","LDirtEffects"],["ZRPole","LDustEffects"],["ZRPole","LGrassDryEffects"],["ZRPole","LDirtEffects"],["ZRPolopoust","LDustEffects"],["ZRPolopoust","LSandEffects"],["ZRPolopoust","LDirtEffects"],["ZRSkala","LDustEffects"],["ZRSkala","LStonesEffects"],["ZRSkalniSterk","LDustEffects"],["ZRSkalniSterk","LStonesEffects"],["ZRSterkNaDno","LDustEffects"],["ZRSterkNaDno","LStonesEffects"],["ZRValouny","LDustEffects"],["ZRValouny","LStonesEffects"],["ZRTrava","LDustEffects"],["ZRTrava","LGrassDryEffects"],["ZRTrava","LDirtEffects"],["DEPolopoust","LDustEffects"],["DEPolopoust","LSandEffects"],["DEPolopoust","LDirtEffects"],["DESkalniSterk","LDustEffects"],["DESkalniSterk","LStonesEffects"],["DETrava","LDustEffects"],["DETrava","LGrassDryEffects"],["DETrava","LDirtEffects"],["WLGrass1","LDustEffects"],["WLGrass1","LGrassEffects"],["WLGrass1","LDirtEffects"],["WLGrass2","LDustEffects"],["WLGrass2","LGrassEffects"],["WLGrass2","LDirtEffects"],["WLGrassW1","LDustEffects"],["WLGrassW1","LGrassEffects"],["WLGrassW1","LDirtEffects"],["WLGrassW2","LDustEffects"],["WLGrassW2","LGrassEffects"],["WLGrassW2","LDirtEffects"],["WLField1","LDustEffects"],["WLField1","LGrassEffects"],["WLField1","LDirtEffects"],["WLField2","LDustEffects"],["WLField2","LGrassEffects"],["WLField2","LDirtEffects"],["WLForest1","LDustEffects"],["WLForest1","LGrassEffects"],["WLForest1","LDirtEffects"],["WLForest2","LDustEffects"],["WLForest2","LGrassEffects"],["WLForest2","LDirtEffects"],["WLMudGround","LDustEffects"],["WLMudGround","LGrassEffects"],["WLMudGround","LDirtEffects"],["WLGrit1","LDustEffects"],["WLGrit1","LDirtEffects"],["WLHeather","LDustEffects"],["WLHeather","LGrassEffects"],["WLHeather","LDirtEffects"],["WLConcrete","LDirtEffects"],["GZTrava","LDustEffects"],["GZTrava","LGrassDryEffects"],["GZTrava","LDirtEffects"],["GZforest","LDustEffects"],["GZForest","LGrassDryEffects"],["GZForest","LDirtEffects"],["GZkameny","LDustEffects"],["GZkameny","LStonesEffects"],["GZHlina","LDustEffects"],["GZHlina","LGrassEffects"],["GZHlina","LDirtEffects"],["BetonNew","LDirtEffects"],["Asf1","LDirtEffects"],["Asf2","LDirtEffects"],["Asf3","LDirtEffects"],["road","LDustEffects"],["Cesta","LDustEffects"]],
    # Class: CfgVehicles\Car\DestructionEffects [Indent level: 1],
    "DestructionEffects": {
        # Class: CfgVehicles\Car\DestructionEffects\Light1 [Indent level: 2]
        "Light1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 1,
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
            "intensity": 1,
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
        },
        # Class: CfgVehicles\Car\DestructionEffects\LightFlames2 [Indent level: 2],
        "LightFlames2": {
            "simulation": "particles",
            "type": "FlameLightBC2",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 1.5,
            "enabled": "distToWater"
        }
    },
    "sensitivityEar": 0.125,
    "sensitivity": 1.75,
    "tf_isolatedAmount": 0.1,
    # Class: CfgVehicles\Car\ACE_Actions [Indent level: 1],
    "ACE_Actions": {
        # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions [Indent level: 2]
        "ACE_MainActions": {
            "displayName": "Interactions",
            "position": "call ace_interaction_fnc_getVehiclePos",
            "selection": "",
            "distance": 4,
            "condition": "true",
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\ACE_Passengers [Indent level: 3],
            "ACE_Passengers": {
                "displayName": "Passengers",
                "condition": "alive _target",
                "statement": "",
                "exceptions": ["isNotSwimming"],
                "insertChildren": "_this call ace_interaction_fnc_addPassengersActions"
            },
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\ace_quickmount_GetIn [Indent level: 3],
            "ace_quickmount_GetIn": {
                "displayName": "Get In",
                "condition": "call ace_quickmount_fnc_canShowFreeSeats",
                "statement": "call ace_quickmount_fnc_getInNearest",
                "exceptions": ["isNotSwimming"],
                "insertChildren": "(_this select 2) param [0,[]]"
            },
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\ace_rearm_Rearm [Indent level: 3],
            "ace_rearm_Rearm": {
                "displayName": "Rearm",
                "distance": 9,
                "condition": "_this call ace_rearm_fnc_canRearm",
                "statement": "_this call ace_rearm_fnc_rearm",
                "exceptions": ["isNotInside"],
                "icon": "z|ace|addons|rearm|ui|icon_rearm_interact.paa"
            },
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\ace_repair_Repair [Indent level: 3],
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
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\ACE_unlockVehicle [Indent level: 3],
            "ACE_unlockVehicle": {
                "displayName": "Unlock Vehicle",
                "distance": 4,
                "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [2, 3]}",
                "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,false],[_target]] call CBA_fnc_targetEvent",
                "exceptions": ["isNotSwimming"],
                "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
            },
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\ACE_lockVehicle [Indent level: 3],
            "ACE_lockVehicle": {
                "displayName": "Lock Vehicle",
                "distance": 4,
                "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [0, 1]}",
                "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,true],[_target]] call CBA_fnc_targetEvent",
                "exceptions": ["isNotSwimming"],
                "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
            },
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\ACE_lockpickVehicle [Indent level: 3],
            "ACE_lockpickVehicle": {
                "displayName": "Lockpick Vehicle",
                "distance": 4,
                "condition": "[_player,_target,'canLockpick'] call ace_vehiclelock_fnc_lockpick",
                "statement": "[_player,_target,'startLockpick'] call ace_vehiclelock_fnc_lockpick",
                "exceptions": ["isNotSwimming"]
            },
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\AIME_vehicle_seats_getInAction [Indent level: 3],
            "AIME_vehicle_seats_getInAction": {
                "displayName": "Get In",
                "condition": "call AIME_vehicle_seats_fnc_getin_condition",
                "statement": "call AIME_vehicle_seats_fnc_getin_run",
                "icon": "a3|ui_f|data|igui|cfg|actions|obsolete|ui_action_getin_ca.paa",
                "insertChildren": "call AIME_vehicle_seats_fnc_change_submenus"
            },
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\ace_attach_AttachVehicle [Indent level: 3],
            "ace_attach_AttachVehicle": {
                "displayName": "Attach item",
                "condition": "_this call ace_attach_fnc_canAttach",
                "insertChildren": "_this call ace_attach_fnc_getChildrenActions",
                "exceptions": ["isNotSwimming"],
                "showDisabled": 0,
                "icon": "z|ace|addons|attach|UI|attach_ca.paa"
            },
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\ace_attach_DetachVehicle [Indent level: 3],
            "ace_attach_DetachVehicle": {
                "displayName": "Detach item",
                "condition": "_this call ace_attach_fnc_canDetach",
                "statement": "_this call ace_attach_fnc_detach",
                "exceptions": ["isNotSwimming"],
                "showDisabled": 0,
                "icon": "z|ace|addons|attach|UI|detach_ca.paa"
            },
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\ace_captives_LoadCaptive [Indent level: 3],
            "ace_captives_LoadCaptive": {
                "displayName": "Load Captive",
                "distance": 4,
                "condition": "[_player,objNull,_target] call ace_captives_fnc_canLoadCaptive",
                "statement": "[_player,objNull,_target] call ace_captives_fnc_doLoadCaptive",
                "exceptions": ["isNotEscorting","isNotSwimming"]
            },
            # Class: CfgVehicles\Car\ACE_Actions\ACE_MainActions\AIME_inventory_openAction [Indent level: 3],
            "AIME_inventory_openAction": {
                "displayName": "Inventory",
                "condition": "AIME_inventory_settingOpenAction				 && { alive _target }				 && { _target call AIME_inventory_fnc_has_inventory }",
                "statement": "_player action [`Gear`, _target]",
                "icon": "A3|ui_f|data|igui|cfg|actions|gear_ca.paa",
                "exceptions": ["isNotSwimming"]
            }
        }
    },
    # Class: CfgVehicles\Car\ACE_SelfActions [Indent level: 1],
    "ACE_SelfActions": {
        # Class: CfgVehicles\Car\ACE_SelfActions\ACE_Passengers [Indent level: 2]
        "ACE_Passengers": {
            "displayName": "Passengers",
            "condition": "alive _target",
            "statement": "",
            "insertChildren": "_this call ace_interaction_fnc_addPassengersActions"
        },
        # Class: CfgVehicles\Car\ACE_SelfActions\ace_interaction_smashWindshield [Indent level: 2],
        "ace_interaction_smashWindshield": {
            "displayName": "Smash windshield",
            "condition": "_player == driver _target && {private _damage = _target getHitPointDamage 'HitGlass1'; _damage > 0.5 && {_damage < 1}}",
            "statement": "playSound3D ['A3|Sounds_F|weapons|hits|glass_2.wss',_target]; _target setHitPointDamage ['HitGlass1',1];"
        },
        # Class: CfgVehicles\Car\ACE_SelfActions\ace_quickmount_ChangeSeat [Indent level: 2],
        "ace_quickmount_ChangeSeat": {
            "displayName": "Change seat",
            "condition": "call ace_quickmount_fnc_canShowFreeSeats",
            "statement": "",
            "insertChildren": "(_this select 2) param [0,[]]"
        },
        # Class: CfgVehicles\Car\ACE_SelfActions\ACE_unlockVehicle [Indent level: 2],
        "ACE_unlockVehicle": {
            "displayName": "Unlock Vehicle",
            "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [2, 3]}",
            "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,false],[_target]] call CBA_fnc_targetEvent",
            "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
        },
        # Class: CfgVehicles\Car\ACE_SelfActions\ACE_lockVehicle [Indent level: 2],
        "ACE_lockVehicle": {
            "displayName": "Lock Vehicle",
            "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [0, 1]}",
            "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,true],[_target]] call CBA_fnc_targetEvent",
            "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
        },
        # Class: CfgVehicles\Car\ACE_SelfActions\ACE_lockpickVehicle [Indent level: 2],
        "ACE_lockpickVehicle": {
            "displayName": "Lockpick Vehicle",
            "condition": "[_player,_target,'canLockpick'] call ace_vehiclelock_fnc_lockpick",
            "statement": "[_player,_target,'startLockpick'] call ace_vehiclelock_fnc_lockpick"
        },
        # Class: CfgVehicles\Car\ACE_SelfActions\ResetFCS [Indent level: 2],
        "ResetFCS": {
            "displayName": "Reset FCS",
            "condition": "_player call ace_fcs_fnc_canResetFCS",
            "statement": "[vehicle _player,[_player] call ace_common_fnc_getTurretIndex] call ace_fcs_fnc_reset;",
            "showDisabled": 0,
            "icon": ""
        }
    },
    "ace_refuel_canReceive": 1,
    # Class: CfgVehicles\Car\ACE_Cargo [Indent level: 1],
    "ACE_Cargo": {
    },
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
        "showCrewAim": 0,
        "ace_fcs_Enabled": 0,
        "ace_fcs_MinDistance": 200,
        "ace_fcs_MaxDistance": 5500,
        "ace_fcs_DistanceInterval": 5
    },
    "tf_range": 30000,
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
    "memoryPointsGetInDriverPrecise": "pos driver",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "memoryPointTaskMarker": "",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
    "selectionShowDamage": "poskozeni",
    "selectionBackLights": "zadni svetlo",
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
        "showCrewAim": 0,
        "ace_fcs_Enabled": 0,
        "ace_fcs_MinDistance": 200,
        "ace_fcs_MaxDistance": 5500,
        "ace_fcs_DistanceInterval": 5
    },
    "curatorInfoType": "RscDisplayAttributesVehicle",
    "curatorInfoTypeEmpty": "RscDisplayAttributesVehicleEmpty",
    "tf_hasLRradio": 0,
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
    "driverInAction": "",
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
    "coefSpeedInside": 1,
    "windSockExist": 0,
    "SLX_XEH_DISABLED": 0,
}