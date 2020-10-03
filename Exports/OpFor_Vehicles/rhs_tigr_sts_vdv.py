rhs_tigr_sts_vdv = {
    "editorPreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_tigr_sts_vdv.paa",
    "scope": 2,
    "scopeCurator": 2,
    "model": "rhsafrf|addons|rhs_tigr|RHS_Tigr_sts",
    "dlc": "RHS_AFRF",
    "author": "Red Hammer Studios",
    "displayName": "GAZ-233014",
    "tf_hasLRradio_api": 1,
    "crewVulnerable": 1,
    "hideProxyInCombat": 0,
    "transportSoldier": 5,
    "cargoProxyIndexes": [1,2,3,4,5],
    "getInProxyOrder": [1,2,3,4,5],
    "magazines": ["rhs_proxy_ags30_12_mag","rhs_proxy_pkm_18_mag"],
    # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets,
    "Turrets": {
        # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret
        "MainTurret": {
            "gunnerType": "rhs_vdv_grenadier",
            "memoryPointGun": "weapon_pkm_end",
            "gunBeg": "weapon_pkm_end",
            "gunEnd": "weapon_pkm_start",
            "body": "mainTurret",
            "gun": "weapon_pkm",
            "animationSourceGun": "weapon_pkm",
            "gunnerLeftHandAnimName": "weapon_pkm",
            "gunnerRightHandAnimName": "weapon_pkm",
            "gunnerLeftLegAnimName": "weapon_pkm_leg_left",
            "gunnerRightLegAnimName": "weapon_pkm_leg_right",
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "gunnerDoor": "Door_Rear",
            "outGunnerMayFire": 1,
            "forceHideGunner": 0,
            "castGunnerShadow": 1,
            "viewGunnerInExternal": 1,
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "gunnerForceOptics": 0,
            "turretInfoType": "rhs_tigr_sts_turret",
            "discreteDistance": [420,100,200,300,400,500,600,700,800,900,1000,1100,1200,1300,1400,1500],
            "discreteDistanceInitIndex": 0,
            "weapons": ["rhs_weap_pkm_tigr"],
            "magazines": ["rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","rhs_mag_762x54mm_100","RHS_mag_VOG30_30"],
            "gunnerAction": "rhs_tigr_gunner_pkm",
            "gunnerInAction": "rhs_tigr_gunner_pkm",
            "memoryPointGunnerOptics": "gunnerview_pkm",
            "selectionFireAnim": "muzzleFlash1",
            "ejectDeadGunner": 1,
            "soundAttenuationTurret": "HeliAttenuationGunner",
            "disableSoundAttenuation": 1,
            "minElev": -25,
            "maxElev": 60,
            "stabilizedInAxes": 0,
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\ViewGunner,
            "ViewGunner": {
                "initAngleX": 5,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.7,
                "minFov": 0.25,
                "maxFov": 1
            },
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\OpticsIn\Sight
                "Sight": {
                    "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
                    "initFov": 0.7,
                    "minFov": 0.35,
                    "maxFov": 0.7,
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                }
            },
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\Hitpoints,
            "Hitpoints": {
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\Hitpoints\Hit_PKM_Turret
                "Hit_PKM_Turret": {
                    "armor": -100,
                    "minimalHit": -0.13,
                    "explosionShielding": 0.5,
                    "radius": 0.1,
                    "name": "Hit_PKM_Turret",
                    "visual": "-",
                    "armorComponent": "Hit_PKM_Turret",
                    "passThrough": 0,
                    "isTurret": 1
                },
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\Hitpoints\Hit_PKM_Gun,
                "Hit_PKM_Gun": {
                    "armor": -100,
                    "minimalHit": -0.13,
                    "explosionShielding": 0.5,
                    "radius": 0.1,
                    "name": "Hit_PKM_Gun",
                    "visual": "-",
                    "armorComponent": "Hit_PKM_Gun",
                    "passThrough": 0,
                    "isGun": 1
                }
            },
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "soundServo": ["A3|sounds_f|dummysound",0.316228,1,15],
            "minTurn": -360,
            "maxTurn": 360,
            "primaryGunner": 1,
            "enableManualFire": 0,
            "startEngine": 0,
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\ViewOptics,
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
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\Components,
            "Components": {
            },
            "animationSourceBody": "mainTurret",
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerName": "Gunner",
            "primaryObserver": 0,
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
            "primary": 1,
            "hasGunner": 1,
            "commanding": 1,
            "turretCanSee": 0,
            "canUseScanners": 1,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
            "TurretSpec": {
                "showHeadPhones": 0
            },
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
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
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
            "forceNVG": 0,
            "isCopilot": 0,
            "canEject": 1,
            "preciseGetInOut": 0,
            "turretFollowFreeLook": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "dontCreateAI": 0,
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
        # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret,
        "AGS_Turret": {
            "memoryPointGun": "weapon_ags_end",
            "gunBeg": "weapon_ags_end",
            "gunEnd": "weapon_ags_start",
            "body": "turret_ags",
            "gun": "weapon_ags",
            "animationSourceBody": "turret_ags",
            "animationSourceGun": "weapon_ags",
            "selectionFireAnim": "muzzleFlash2",
            "dontCreateAi": 1,
            "cantCreateAI": 1,
            "proxyIndex": 2,
            "LODTurnedIn": 1000,
            "LODTurnedOut": 1000,
            "gunnerLeftHandAnimName": "weapon_ags",
            "gunnerRightHandAnimName": "weapon_ags",
            "gunnerLeftLegAnimName": "weapon_ags_leg_left",
            "gunnerRightLegAnimName": "weapon_ags_leg_right",
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "initTurn": -30,
            "weapons": ["RHS_weap_AGS30_tigr"],
            "magazines": ["RHS_mag_VOG30_30","RHS_mag_VOG30_30","RHS_mag_VOG30_30","RHS_mag_VOG30_30","RHS_mag_VOG30_30","RHS_mag_VOG30_30","RHS_mag_VOG30_30","RHS_mag_VOG30_30","RHS_mag_VOG30_30","RHS_mag_VOG30_30","RHS_mag_VOG30_30","RHS_mag_VOG30_30","rhs_mag_762x54mm_100"],
            "gunnerAction": "rhs_tigr_gunner_ags",
            "gunnerInAction": "rhs_tigr_gunner_ags",
            "memoryPointGunnerOptics": "gunnerview_ags",
            "discreteDistance": [],
            "discreteDistanceInitIndex": 0,
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\OpticsIn\Sight
                "Sight": {
                    "hitpoint": "Hit_AGS_Optic",
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_heavyweapons|data|optika_AGS30",
                    "initFov": 0.25,
                    "minFov": 0.25,
                    "maxFov": 0.25,
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                }
            },
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\Hitpoints,
            "Hitpoints": {
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\Hitpoints\Hit_AGS_Turret
                "Hit_AGS_Turret": {
                    "armor": -100,
                    "minimalHit": -0.13,
                    "explosionShielding": 0.5,
                    "radius": 0.1,
                    "name": "Hit_AGS_Turret",
                    "visual": "-",
                    "armorComponent": "Hit_AGS_Turret",
                    "passThrough": 0,
                    "isTurret": 1
                },
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\Hitpoints\Hit_AGS_Gun,
                "Hit_AGS_Gun": {
                    "armor": -100,
                    "minimalHit": -0.13,
                    "explosionShielding": 0.5,
                    "radius": 0.1,
                    "name": "Hit_AGS_Gun",
                    "visual": "-",
                    "armorComponent": "Hit_AGS_Gun",
                    "passThrough": 0,
                    "isGun": 1
                },
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\Hitpoints\Hit_AGS_Optic,
                "Hit_AGS_Optic": {
                    "armor": -30,
                    "minimalHit": -0.13,
                    "explosionShielding": 0.5,
                    "radius": 0.1,
                    "name": "Hit_AGS_Optic",
                    "visual": "-",
                    "armorComponent": "Hit_AGS_Optic",
                    "passThrough": 0
                }
            },
            "gunnerType": "rhs_vdv_grenadier",
            "gunnerDoor": "Door_Rear",
            "outGunnerMayFire": 1,
            "forceHideGunner": 0,
            "castGunnerShadow": 1,
            "viewGunnerInExternal": 1,
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "gunnerForceOptics": 0,
            "turretInfoType": "rhs_tigr_sts_turret",
            "ejectDeadGunner": 1,
            "soundAttenuationTurret": "HeliAttenuationGunner",
            "disableSoundAttenuation": 1,
            "minElev": -25,
            "maxElev": 60,
            "stabilizedInAxes": 0,
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\ViewGunner,
            "ViewGunner": {
                "initAngleX": 5,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.7,
                "minFov": 0.25,
                "maxFov": 1
            },
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "soundServo": ["A3|sounds_f|dummysound",0.316228,1,15],
            "minTurn": -360,
            "maxTurn": 360,
            "primaryGunner": 1,
            "enableManualFire": 0,
            "startEngine": 0,
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\ViewOptics,
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
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\Components,
            "Components": {
            },
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "gunnerName": "Gunner",
            "primaryObserver": 0,
            "soundElevation": ["",0.00316228,1],
            "initElev": 0,
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
            "canUseScanners": 1,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
            "TurretSpec": {
                "showHeadPhones": 0
            },
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
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "inGunnerMayFire": 1,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "gunnerCompartments": "Compartment1",
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
            "forceNVG": 0,
            "isCopilot": 0,
            "canEject": 1,
            "preciseGetInOut": 0,
            "turretFollowFreeLook": 0,
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
            "showCrewAim": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\Turrets\CargoTurret_01,
        "CargoTurret_01": {
            "gunnerAction": "vehicle_turnout_1",
            "gunnerInAction": "RHS_Tigr_CargoIn01",
            "animationSourceHatch": "Hatch_Front",
            "isPersonTurret": 2,
            "enabledByAnimationSource": "hatch_front_door",
            "gunnerGetInAction": "GetInMantis",
            "gunnerGetOutAction": "GetOutMantis",
            "commanding": -2,
            "rhs_hatch_control": 1,
            "memoryPointsGetInGunner": "pos cargo",
            "memoryPointsGetInGunnerDir": "pos cargo dir",
            "gunnerName": "Passenger (Front Hatch)",
            "gunnerCompartments": "Compartment1",
            "gunnerDoor": "Door_Rear",
            "memoryPointGunnerOptics": "",
            "gunnerForceOptics": 0,
            "canHideGunner": 1,
            "LODTurnedIn": 1000,
            "LODTurnedOut": 0,
            "proxyIndex": 9,
            "maxElev": 45,
            "minElev": -35,
            "maxTurn": 61,
            "minTurn": -65,
            "inGunnerMayFire": 0,
            # Class: CfgVehicles\rhs_tigr_base\Turrets\CargoTurret_01\TurnIn,
            "TurnIn": {
                "limitsArrayTop": [[0,0],[0,0]],
                "limitsArrayBottom": [[0,0],[0,0]]
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
            # Class: CfgVehicles\AllVehicles\CargoTurret\Hitpoints,
            "Hitpoints": {
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
            "disableSoundAttenuation": 1,
            "outGunnerMayFire": 1,
            "showAsCargo": 1,
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
            "forceHideGunner": 0,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
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
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
            "TurnOut": {
                "turnOffset": 0
            },
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\Turrets\CargoTurret_02,
        "CargoTurret_02": {
            "proxyIndex": 7,
            "isPersonTurret": 2,
            "animationSourceHatch": "Hatch_Back",
            "enabledByAnimationSource": "hatch_back_door",
            "gunnerName": "Passenger (Rear Hatch)",
            "memoryPointsGetInGunner": "pos hatch rear",
            "memoryPointsGetInGunnerDir": "pos hatch rear dir",
            "gunnerAction": "vehicle_turnout_1",
            "gunnerInAction": "RHS_Tigr_CargoIn01",
            "gunnerGetInAction": "GetInMantis",
            "gunnerGetOutAction": "GetOutMantis",
            "commanding": -2,
            "rhs_hatch_control": 1,
            "gunnerCompartments": "Compartment1",
            "gunnerDoor": "Door_Rear",
            "memoryPointGunnerOptics": "",
            "gunnerForceOptics": 0,
            "canHideGunner": 1,
            "LODTurnedIn": 1000,
            "LODTurnedOut": 0,
            "maxElev": 45,
            "minElev": -35,
            "maxTurn": 61,
            "minTurn": -65,
            "inGunnerMayFire": 0,
            # Class: CfgVehicles\rhs_tigr_base\Turrets\CargoTurret_01\TurnIn,
            "TurnIn": {
                "limitsArrayTop": [[0,0],[0,0]],
                "limitsArrayBottom": [[0,0],[0,0]]
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
            # Class: CfgVehicles\AllVehicles\CargoTurret\Hitpoints,
            "Hitpoints": {
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
            "disableSoundAttenuation": 1,
            "outGunnerMayFire": 1,
            "showAsCargo": 1,
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
            "forceHideGunner": 0,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
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
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
            "TurnOut": {
                "turnOffset": 0
            },
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        }
    },
    # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_pkm_reload
        "weapon_pkm_reload": {
            "source": "reload",
            "weapon": "rhs_weap_pkm_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_pkm_ReloadMagazine,
        "weapon_pkm_ReloadMagazine": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_pkm_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_pkm_ammoRandom,
        "weapon_pkm_ammoRandom": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkm_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\Revolving,
        "Revolving": {
            "source": "revolving",
            "weapon": "rhs_weap_pkm_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_ags_reload,
        "weapon_ags_reload": {
            "source": "reload",
            "weapon": "RHS_weap_AGS30_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_ags_ReloadMagazine,
        "weapon_ags_ReloadMagazine": {
            "source": "reloadmagazine",
            "weapon": "RHS_weap_AGS30_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_ags_ammoRandom,
        "weapon_ags_ammoRandom": {
            "source": "ammorandom",
            "weapon": "RHS_weap_AGS30_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\rpg26_hide_1,
        "rpg26_hide_1": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\rpg26_hide_2,
        "rpg26_hide_2": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\rpg26_hide_3,
        "rpg26_hide_3": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\rpg26_hide_4,
        "rpg26_hide_4": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\turret_correct,
        "turret_correct": {
            "animPeriod": 1.8,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\hatch_gunner,
        "hatch_gunner": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\HitSpare,
        "HitSpare": {
            "source": "Hit",
            "hitpoint": "HitSpare",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\UseSpare,
        "UseSpare": {
            "hitpoint": "UseSpare",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\hatch_front_door,
        "hatch_front_door": {
            "mass": 1,
            "source": "door",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\hatch_back_door,
        "hatch_back_door": {
            "mass": 1,
            "source": "door",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\spare_hide,
        "spare_hide": {
            "animPeriod": 1e-008,
            "source": "user",
            "displayName": "hide spare wheel",
            "mass": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\Door_LF,
        "Door_LF": {
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_UAZ_Door",
            "soundPosition": "door_1_1_axis"
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\Door_RF,
        "Door_RF": {
            "soundPosition": "door_1_2_axis",
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_UAZ_Door"
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\Door_Rear,
        "Door_Rear": {
            "soundPosition": "door_2_1_axis",
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_UAZ_Door"
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\HitGlass7,
        "HitGlass7": {
            "hitpoint": "HitGlass7",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\HitGlass8,
        "HitGlass8": {
            "hitpoint": "HitGlass8",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\HitGlass9,
        "HitGlass9": {
            "hitpoint": "HitGlass9",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\HitGlass10,
        "HitGlass10": {
            "hitpoint": "HitGlass10",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\longlights_hide,
        "longlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\shortlights_hide,
        "shortlights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\lights_hide,
        "lights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\searchlight_hide,
        "searchlight_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\cabinlights_hide,
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\MRAP_02_base_F\AnimationSources\HitReserveWheel,
        "HitReserveWheel": {
            "source": "Hit",
            "hitpoint": "HitReserveWheel",
            "raw": 1
        },
        # Class: CfgVehicles\MRAP_02_base_F\AnimationSources\Door_LM,
        "Door_LM": {
            "source": "door",
            "animPeriod": 0.8,
            "initPhase": 0
        },
        # Class: CfgVehicles\MRAP_02_base_F\AnimationSources\Door_RM,
        "Door_RM": {
            "source": "door",
            "animPeriod": 0.8,
            "initPhase": 0
        },
        # Class: CfgVehicles\MRAP_02_base_F\AnimationSources\HitGlass6,
        "HitGlass6": {
            "source": "Hit",
            "hitpoint": "HitGlass6",
            "raw": 1
        },
        # Class: CfgVehicles\MRAP_02_base_F\AnimationSources\HitGlass11,
        "HitGlass11": {
            "hitpoint": "HitGlass11",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitLFWheel,
        "HitLFWheel": {
            "source": "Hit",
            "hitpoint": "HitLFWheel",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitRFWheel,
        "HitRFWheel": {
            "hitpoint": "HitRFWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitLBWheel,
        "HitLBWheel": {
            "hitpoint": "HitLF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitRBWheel,
        "HitRBWheel": {
            "hitpoint": "HitRF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitLF2Wheel,
        "HitLF2Wheel": {
            "hitpoint": "HitLBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitRF2Wheel,
        "HitRF2Wheel": {
            "hitpoint": "HitRBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitLMWheel,
        "HitLMWheel": {
            "hitpoint": "HitLMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitRMWheel,
        "HitRMWheel": {
            "hitpoint": "HitRMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass1,
        "HitGlass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass2,
        "HitGlass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass3,
        "HitGlass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass4,
        "HitGlass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Car_F\AnimationSources\HitGlass5,
        "HitGlass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        }
    },
    # Class: CfgVehicles\rhs_tigr_sts_vdv\EventHandlers,
    "EventHandlers": {
        # Class: CfgVehicles\rhs_tigr_sts_vdv\EventHandlers\RHS_EventHandlers
        "RHS_EventHandlers": {
            "init": "_this call rhs_fnc_tigr_init; (_this select 0) lockTurret [[1],true]; _this call rhs_fnc_tigr_sts_inventory_eh;",
            "getIn": "_this call rhs_fnc_tigr_sts_turret_getin_eh",
            "getOut": "_this spawn rhs_fnc_tigr_sts_turret_getout_eh",
            "seatSwitched": "_this call rhs_fnc_tigr_sts_turret_seat_eh",
            "containerClosed": "_this call rhs_fnc_tigr_sts_inventory_eh;",
            "reloaded": "_this call rhs_fnc_tigr_sts_reloaded_eh",
            "turnIn": "([0] + _this)  call rhs_fnc_turretAction;",
            "turnOut": "([1] + _this) call rhs_fnc_turretAction;",
            "dammaged": "_this call rhs_fnc_wheelDamaged"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\EventHandlers\RHS_TigrHandler,
        "RHS_TigrHandler": {
        },
        "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "category": "Car",
    "insideSoundCoef": 0.4,
    "slingLoadCargoMemoryPoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "canfloat": 0,
    "cargoaction": ["RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo02"],
    "cargoIsCoDriver": [0,0],
    "castDriverShadow": 1,
    # Class: CfgVehicles\rhs_tigr_base\Library,
    "Library": {
        "libTextDesc": "You can write something in here."
    },
    "faction": "rhs_faction_vdv",
    "crew": "rhs_vdv_driver_armored",
    "rhs_decalParameters": ["['Number', cDecalsTigr4NumberPlaces, 'LicensePlate']","['Label', cDecalsTigrRightArmyPlaces, 'Army', 2]","['Label', cDecalsTigrRightPlatoonPlaces, 'Platoon',11]"],
    "driverRightLegAnimName": "pedalR",
    "driverLeftLegAnimName": "pedalL",
    "normalSpeedForwardCoef": 0.6,
    "slowSpeedForwardCoef": 0.45,
    "turnCoef": 3,
    "terrainCoef": 1.5,
    "waterSpeedFactor": 0.4,
    "simulation": "carx",
    "dampersBumpCoef": 4,
    "precision": 9,
    "brakeDistance": 3,
    "acceleration": 15,
    "fireResistance": 5,
    "maxSpeed": 140,
    "fuelCapacity": 17.5,
    "RHS_fuelCapacity": 140,
    "wheelCircumference": 2.45,
    "brakeIdleSpeed": 2,
    "maxFordingDepth": 0,
    "waterResistance": 1,
    "waterLeakiness": 10,
    # Class: CfgVehicles\rhs_tigr_base\complexGearbox,
    "complexGearbox": {
        "GearboxRatios": ["R1",-4.476,"N",0,"D1",3.1,"D2",1.81,"D3",1.41,"D4",1,"D5",0.71],
        "TransmissionRatios": ["High",5],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R"
    },
    "changeGearMinEffectivity": [0.95,0,0.9,0.9,0.9,0.9,0.9],
    "switchTime": 0.28,
    "latency": 1,
    "differentialType": "all_limited",
    "frontRearSplit": 0.5,
    "frontBias": 1.5,
    "rearBias": 1.5,
    "centreBias": 1.3,
    "clutchStrength": 35,
    "transmissionLosses": 9,
    "dampingRateFullThrottle": 0.08,
    "dampingRateZeroThrottleClutchEngaged": 1.35,
    "dampingRateZeroThrottleClutchDisengaged": 0.35,
    "torqueCurve": [[0.3,0.34918],[0.4,0.695082],[0.48,0.97377],[0.6,1],[0.72,1],[0.8,0.965574],[0.88,0.911475],[1.1244,0]],
    "enginePower": 134,
    "peakTorque": 915,
    "maxOmega": 261.8,
    "minOmega": 55,
    "idleRPM": 750,
    "redRPM": 2500,
    "engineLosses": 11,
    "thrustDelay": 0.8,
    "engineBrakeCoef": 0.3,
    "antiRollbarForceCoef": 3.5,
    "antiRollbarForceLimit": 4.5,
    "antiRollbarSpeedMin": 40,
    "antiRollbarSpeedMax": 120,
    # Class: CfgVehicles\rhs_tigr_base\Wheels,
    "Wheels": {
        # Class: CfgVehicles\rhs_tigr_base\Wheels\LF
        "LF": {
            "boneName": "wheel_1_1_damper",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "suspForceAppPointOffset": "wheel_1_1_axis",
            "tireForceAppPointOffset": "wheel_1_1_axis",
            "side": "left",
            "suspTravelDirection": [-0.125,-1,0],
            "width": 0.32,
            "steering": 1,
            "mass": 60,
            "MOI": 10,
            "dampingRate": 3.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 12000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.13,
            "maxDroop": 0.11,
            "sprungMass": -1,
            "springStrength": 135000,
            "springDamperRate": 12471,
            "longitudinalStiffnessPerUnitGravity": 4800,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0.17,0.95],[0.4,0.85],[1,0.75]]
        },
        # Class: CfgVehicles\rhs_tigr_base\Wheels\LR,
        "LR": {
            "boneName": "wheel_1_2_damper",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "suspForceAppPointOffset": "wheel_1_2_axis",
            "tireForceAppPointOffset": "wheel_1_2_axis",
            "steering": 0,
            "maxHandBrakeTorque": 20000,
            "side": "left",
            "suspTravelDirection": [-0.125,-1,0],
            "width": 0.32,
            "mass": 60,
            "MOI": 10,
            "dampingRate": 3.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 12000,
            "maxCompression": 0.13,
            "maxDroop": 0.11,
            "sprungMass": -1,
            "springStrength": 135000,
            "springDamperRate": 12471,
            "longitudinalStiffnessPerUnitGravity": 4800,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0.17,0.95],[0.4,0.85],[1,0.75]]
        },
        # Class: CfgVehicles\rhs_tigr_base\Wheels\RF,
        "RF": {
            "boneName": "wheel_2_1_damper",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "suspForceAppPointOffset": "wheel_2_1_axis",
            "tireForceAppPointOffset": "wheel_2_1_axis",
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "steering": 1,
            "width": 0.32,
            "mass": 60,
            "MOI": 10,
            "dampingRate": 3.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 12000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.13,
            "maxDroop": 0.11,
            "sprungMass": -1,
            "springStrength": 135000,
            "springDamperRate": 12471,
            "longitudinalStiffnessPerUnitGravity": 4800,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0.17,0.95],[0.4,0.85],[1,0.75]]
        },
        # Class: CfgVehicles\rhs_tigr_base\Wheels\RR,
        "RR": {
            "boneName": "wheel_2_2_damper",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "suspForceAppPointOffset": "wheel_2_2_axis",
            "tireForceAppPointOffset": "wheel_2_2_axis",
            "steering": 0,
            "maxHandBrakeTorque": 20000,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": 0.32,
            "mass": 60,
            "MOI": 10,
            "dampingRate": 3.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 12000,
            "maxCompression": 0.13,
            "maxDroop": 0.11,
            "sprungMass": -1,
            "springStrength": 135000,
            "springDamperRate": 12471,
            "longitudinalStiffnessPerUnitGravity": 4800,
            "latStiffX": 2.5,
            "latStiffY": 18,
            "frictionVsSlipGraph": [[0.17,0.95],[0.4,0.85],[1,0.75]]
        }
    },
    # Class: CfgVehicles\rhs_tigr_base\Sounds,
    "Sounds": {
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Idle_ext
        "Idle_ext": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_tigr_idle_ext",0.698107,1,250],
            "frequency": "0.75	+	((rpm/	2700) factor[(610/	2700),(2700/	2700)])*0.95",
            "volume": "engineOn*camPos*(((rpm/	2700) factor[(10/	2700),(50/	2700)])	*	((rpm/	2700) factor[(800/	2700),(600/	2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Engine,
        "Engine": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_tigr_idle_ext",0.446684,1,350],
            "frequency": "0.75	+	((rpm/	2700) factor[(610/	2700),(2700/	2700)])*0.95",
            "volume": "engineOn*camPos*(((rpm/	2700) factor[(620/	2700),(820/	2700)])	*	((rpm/	2700) factor[(2700/	2700),(2700/	2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\EngineThrust,
        "EngineThrust": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_exhaust_low1",0.5,1,250],
            "frequency": "0.65	+	((rpm/	2700) factor[(610/	2700),(6400/	2700)])*0.75",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.4,1])))*(((rpm/	2700) factor[(620/	2700),(820/	2700)])	*	((rpm/	2700) factor[(2700/	2700),(2700/	2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\GearboxWhine_Ext,
        "GearboxWhine_Ext": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_axle_whine_ext",0.35,1,250],
            "frequency": "0.85	+	((rpm/	2700) factor[(610/	2700),(2700/	2700)])*0.95",
            "volume": "engineOn*camPos*(((rpm/	2700) factor[(700/	2700),(850/	2700)])	*	((rpm/	2700) factor[(2700/	2700),(2700/	2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Turbo_Ext,
        "Turbo_Ext": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|turbo_ext",0.2,1,50],
            "frequency": "0.85	+	((rpm/	2700) factor[(610/	2700),(2700/	2700)])*0.95",
            "volume": "engineOn*camPos*(((rpm/ 2700) factor[(620/  2700),(820/ 2700)]) * ((rpm/  2700) factor[(2700/ 2700),(2700/  2700)]))*2.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Idle_int,
        "Idle_int": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_tigr_idle_int",0.6,1],
            "frequency": "0.75 + ((rpm/  2700) factor[(610/  2700),(2700/  2700)])*0.95",
            "volume": "engineOn*(1-camPos)*(((rpm/ 2700) factor[(10/ 2700),(50/  2700)]) * ((rpm/  2700) factor[(800/  2700),(600/ 2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Engine_int,
        "Engine_int": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_tigr_idle_int",0.6,1],
            "frequency": "0.75 + ((rpm/  2700) factor[(610/  2700),(2700/  2700)])*0.95",
            "volume": "engineOn*(1-camPos)*(((rpm/ 2700) factor[(620/  2700),(820/ 2700)]) * ((rpm/  2700) factor[(2700/ 2700),(2700/  2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\EngineThrust_int,
        "EngineThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_exhaust_low1",0.4,1],
            "frequency": "0.85	+	((rpm/	2700) factor[(610/	2700),(2700/	2700)])*0.75",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.4,1])))*(((rpm/  2700) factor[(620/  2700),(820/ 2700)]) * ((rpm/  2700) factor[(2700/ 2700),(2700/  2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\GearboxWhine_Int,
        "GearboxWhine_Int": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_axle_whine_int",0.2,1],
            "frequency": "0.85 + ((rpm/  2700) factor[(610/  2700),(2700/  2700)])*0.95",
            "volume": "engineOn*(1-camPos)*(((rpm/ 2700) factor[(700/  2700),(850/ 2700)]) * ((rpm/  2700) factor[(2700/ 2700),(2700/  2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Turbo_Int,
        "Turbo_Int": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|turbo_ext",0.15,1],
            "frequency": "0.85 + ((rpm/  2700) factor[(610/  2700),(2700/  2700)])*0.75",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/  2700) factor[(620/  2700),(820/ 2700)]) * ((rpm/  2700) factor[(2700/ 2700),(2700/  2700)]))*1.0"
        }
    },
    "armor": 60,
    "armorGlass": 0.9,
    "armorWheels": 4.9,
    "minTotalDamageThreshold": 0.2,
    "damageResistance": 0.00562,
    "secondaryExplosion": -1,
    "fuelExplosionPower": 0.1,
    # Class: CfgVehicles\rhs_tigr_base\TransportMagazines,
    "TransportMagazines": {
        # Class: CfgVehicles\rhs_tigr_base\TransportMagazines\_xx_rhs_30Rnd_545x39_7N10_AK
        "_xx_rhs_30Rnd_545x39_7N10_AK": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": 4
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportMagazines\_xx_rhs_100Rnd_762x54mmR,
        "_xx_rhs_100Rnd_762x54mmR": {
            "magazine": "rhs_100Rnd_762x54mmR",
            "count": 8
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportMagazines\_xx_rhs_mag_rdg2_white,
        "_xx_rhs_mag_rdg2_white": {
            "magazine": "rhs_mag_rdg2_white",
            "count": 2
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportMagazines\_xx_rhs_mag_rgd5,
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 6
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportMagazines\_xx_rhs_rpg26_mag,
        "_xx_rhs_rpg26_mag": {
            "magazine": "rhs_rpg26_mag",
            "count": 4
        }
    },
    # Class: CfgVehicles\rhs_tigr_base\TransportWeapons,
    "TransportWeapons": {
        # Class: CfgVehicles\rhs_tigr_base\TransportWeapons\_xx_rhs_weap_rpg26
        "_xx_rhs_weap_rpg26": {
            "weapon": "rhs_weap_rpg26",
            "count": 4
        }
    },
    # Class: CfgVehicles\rhs_tigr_base\TransportItems,
    "TransportItems": {
        # Class: CfgVehicles\rhs_tigr_base\TransportItems\_xx_FirstAidKit
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportItems\_xx_Medikit,
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportItems\_xx_Toolkit,
        "_xx_Toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    "hiddenSelections": ["camo1","camo2","camo3","camo4","camo5","n1","n2","n3","n4","i1","i2","i3","i4"],
    "hiddenSelectionsTextures": ["rhsafrf|addons|rhs_tigr|data|rhs_tigr_co.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_01_co.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_02_co.paa","rhsafrf|addons|rhs_tigr|sts_proxies|data|tigr_ext_ads_co.paa","rhsafrf|addons|rhs_tigr|m_proxies|data|tigr_m_adds_co.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa"],
    # Class: CfgVehicles\rhs_tigr_base\textureSources,
    "textureSources": {
        # Class: CfgVehicles\rhs_tigr_base\textureSources\standard
        "standard": {
            "displayName": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_tigr|data|rhs_tigr_co.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_01_co.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_02_co.paa","rhsafrf|addons|rhs_tigr|sts_proxies|data|tigr_ext_ads_co.paa","rhsafrf|addons|rhs_tigr|m_proxies|data|tigr_m_adds_co.paa"],
            "factions": ["rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles\rhs_tigr_base\textureSources\Camo,
        "Camo": {
            "displayName": "Camo",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_tigr|data|rhs_tigr_co_camo.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_01_co.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_02_co.paa","rhsafrf|addons|rhs_tigr|sts_proxies|data|tigr_ext_ads_co.paa","rhsafrf|addons|rhs_tigr|m_proxies|data|tigr_m_adds_co.paa"],
            "factions": ["rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        }
    },
    "textureList": [],
    # Class: CfgVehicles\rhs_tigr_base\Attributes,
    "Attributes": {
        # Class: CfgVehicles\rhs_tigr_base\Attributes\ObjectTexture
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type,
        "rhs_decalNumber_type": {
            "displayName": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cDecalsTigr4NumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values,
            "values": {
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\Default
                "Default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultValue": "Default"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\DefaultRed,
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\BoldRed,
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\CDF,
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\Handpaint,
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\HandpaintBlack,
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\Iraqi,
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\LicensePlate,
                "LicensePlate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber,
        "rhs_decalNumber": {
            "collapsed": 1,
            "displayName": "Set plate number",
            "tooltip": "Set plate number. 4 numbers are required. If 0, random number will be generated",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typeName": "Number",
            "defaultValue": "-1",
            "expression": "if( _value >= 0)then{[_this,[['Number', cDecalsTigr4NumberPlaces, _this getVariable ['rhs_decalNumber_type','LicensePlate'], _value]]] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type,
        "rhs_decalArmy_type": {
            "displayName": "Define large door roundel type",
            "tooltip": "Decal type",
            "property": "rhs_decalArmy_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values,
            "values": {
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Army
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "Army"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Honor,
                "Honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\HonorGDR,
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Platoon,
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\PlatoonGDR,
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\PlatoonVDV,
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy,
        "rhs_decalArmy": {
            "displayName": "Set large door roundel symbol",
            "tooltip": "Set large door roundel located on both sides. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalArmy",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cDecalsTigrRightArmyPlaces,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalPlatoon_type,
        "rhs_decalPlatoon_type": {
            "displayName": "Define small door roundel type",
            "property": "rhs_decalPlatoon_type",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "tooltip": "Decal type",
            "control": "Combo",
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values,
            "values": {
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Army
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "Army"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Honor,
                "Honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\HonorGDR,
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Platoon,
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\PlatoonGDR,
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\PlatoonVDV,
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalPlatoon,
        "rhs_decalPlatoon": {
            "displayName": "Set small door roundel symbol",
            "tooltip": "Define small door roundel located on both sides. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cDecalsTigrRightPlatoonPlaces,  _this getVariable ['rhs_decalPlatoon_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_hidespare,
        "rhs_hidespare": {
            "displayName": "Remove spare wheel",
            "property": "rhs_hidespare",
            "control": "CheckboxNumber",
            "expression": "_this animate ['spare_hide',_value,true]",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\Door_LF,
        "Door_LF": {
            "displayName": "Open front left door",
            "property": "Door_LF",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\Door_RF,
        "Door_RF": {
            "displayName": "Open front right door",
            "property": "Door_RF",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\Door_Rear,
        "Door_Rear": {
            "displayName": "Open rear doors",
            "property": "Door_Rear",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        }
    },
    "destrType": "DestructDefault",
    "driverAction": "rhs_tigr_driver",
    "driverInAction": "rhs_tigr_driver",
    "viewDriverInExternal": 1,
    "driverIsCommander": 1,
    "enableGPS": 0,
    "getInAction": "GetInLow",
    "getOutAction": "GetOutLow",
    "Icon": "rhsafrf|addons|rhs_tigr|data|map_ico|RHS_icomap_Tigr_ca.paa",
    "mapSize": 6,
    "picture": "rhsafrf|addons|rhs_tigr|data|ico|rhs_tigr_pic_ca.paa",
    "selectionBackLights": "zadni svetlo",
    "selectionBrakeLights": "brzdove svetlo",
    "selectionDashboard": "light",
    "side": 0,
    "attenuationEffectType": "RHS_CarAttenuation",
    "TextPlural": "Tigrs",
    "TextSingular": "Tigr",
    "vehicleClass": "rhs_vehclass_car",
    "editorSubcategory": "rhs_EdSubcat_car",
    "weapons": ["TruckHorn"],
    "memoryPointsGetInDriver": "pos driver",
    "memoryPointsGetInDriverDir": "pos driver dir",
    "memoryPointsGetInCargo": ["pos codriver","pos cargo"],
    "memoryPointsGetInCargoDir": ["pos codriver dir","pos cargo dir"],
    "driverDoor": "Door_LF",
    "cargoDoors": ["Door_RF","Door_Rear"],
    "soundGear": ["",5.62341e-005,1],
    # Class: CfgVehicles\rhs_tigr_base\RenderTargets,
    "RenderTargets": {
        # Class: CfgVehicles\rhs_tigr_base\RenderTargets\LeftMirror
        "LeftMirror": {
            "renderTarget": "rendertarget0",
            # Class: CfgVehicles\rhs_tigr_base\RenderTargets\LeftMirror\CameraView1,
            "CameraView1": {
                "pointPosition": "pp1",
                "pointDirection": "pd1",
                "renderQuality": 2,
                "renderVisionMode": 4,
                "fov": 0.7
            },
            "BBoxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles\rhs_tigr_base\RenderTargets\RightMirror,
        "RightMirror": {
            "renderTarget": "rendertarget1",
            # Class: CfgVehicles\rhs_tigr_base\RenderTargets\RightMirror\CameraView1,
            "CameraView1": {
                "pointPosition": "pp2",
                "pointDirection": "pd2",
                "renderQuality": 2,
                "renderVisionMode": 4,
                "fov": 0.7
            },
            "BBoxes": ["PIP_2_TL","PIP_2_TR","PIP_2_BL","PIP_2_BR"]
        }
    },
    # Class: CfgVehicles\rhs_tigr_base\Damage,
    "Damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_tigr|data|glass.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","rhsafrf|addons|rhs_btr70|data|kamaz_glass_in.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_tigr.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_dam_tigr.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_destr_tigr.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int01.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_dam_tigr_int01.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_destr_tigr.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int02.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_dam_tigr_int02.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_destr_tigr.rvmat","rhsafrf|addons|rhs_tigr|sts_proxies|data|rhs_tigr_ext_ads.rvmat","rhsafrf|addons|rhs_tigr|sts_proxies|data|rhs_dam_tigr_ext_ads.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_destr_tigr.rvmat","rhsafrf|addons|rhs_tigr|m_proxies|data|rhs_tigrM_ext_ads.rvmat","rhsafrf|addons|rhs_tigr|m_proxies|data|rhs_dam_tigrM_ext_ads.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_destr_tigr.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles\rhs_tigr_base\HitPoints,
    "HitPoints": {
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitLFWheel
        "HitLFWheel": {
            "armor": 3.1,
            "radius": 0.33,
            "visual": "wheel_1_1_damage",
            "armorComponent": "wheel_1_1_hide",
            "minimalHit": -0.016,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_1_1_steering"
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitLF2Wheel,
        "HitLF2Wheel": {
            "armor": 3.1,
            "radius": 0.33,
            "visual": "wheel_1_2_damage",
            "armorComponent": "wheel_1_2_hide",
            "minimalHit": -0.016,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_1_2_steering"
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitRFWheel,
        "HitRFWheel": {
            "armor": 3.1,
            "radius": 0.33,
            "visual": "wheel_2_1_damage",
            "armorComponent": "wheel_2_1_hide",
            "minimalHit": -0.016,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_2_1_steering"
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitRF2Wheel,
        "HitRF2Wheel": {
            "armor": 3.1,
            "radius": 0.33,
            "visual": "wheel_2_2_damage",
            "armorComponent": "wheel_2_2_hide",
            "minimalHit": -0.016,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_2_2_steering"
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitSpare,
        "HitSpare": {
            "name": "spare1",
            "armor": 3.1,
            "radius": 0.33,
            "visual": "wheel_2_2_damage",
            "armorComponent": "wheel_2_2_hide",
            "minimalHit": -0.016,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\UseSpare,
        "UseSpare": {
            "name": "",
            "visual": "-",
            "armor": 1,
            "radius": 0.33,
            "armorComponent": "wheel_2_2_hide",
            "minimalHit": -0.016,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitHull,
        "HitHull": {
            "armor": -200,
            "name": "karoserie",
            "visual": "zbytek",
            "passThrough": 0.2,
            "minimalHit": -0.2,
            "explosionShielding": 0.2,
            "radius": 0.25
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitBody,
        "HitBody": {
            "minimalHit": 0.1,
            "armor": 4,
            "material": -1,
            "name": "karoserie",
            "visual": "zbytek",
            "passThrough": 1,
            "explosionShielding": 1,
            "radius": 0.45
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitFuel,
        "HitFuel": {
            "armor": 0.5,
            "name": "palivo",
            "visual": "-",
            "material": -1,
            "passThrough": 0.2,
            "minimalHit": 0.2,
            "explosionShielding": 0.1,
            "radius": 0.25
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine,
        "HitEngine": {
            "minimalHit": 0.02,
            "armor": 3.9,
            "name": "motor",
            "visual": "zbytek",
            # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke,
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1,
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2,
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds,
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
            "passThrough": 0.4,
            "explosionShielding": 0.4,
            "radius": 0.45
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass1,
        "HitGlass1": {
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass2,
        "HitGlass2": {
            "name": "glass2",
            "visual": "glass2",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass3,
        "HitGlass3": {
            "name": "glass3",
            "visual": "glass3",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass4,
        "HitGlass4": {
            "name": "glass4",
            "visual": "glass4",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass5,
        "HitGlass5": {
            "name": "glass5",
            "visual": "glass5",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass6,
        "HitGlass6": {
            "name": "glass6",
            "visual": "glass6",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass7,
        "HitGlass7": {
            "name": "glass7",
            "visual": "glass7",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass8,
        "HitGlass8": {
            "name": "glass8",
            "visual": "glass8",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass9,
        "HitGlass9": {
            "name": "glass9",
            "visual": "glass9",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass10,
        "HitGlass10": {
            "name": "glass10",
            "visual": "glass10",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\MRAP_02_base_F\HitPoints\HitReserveWheel,
        "HitReserveWheel": {
            "armor": 0.5,
            "material": -1,
            "name": "wheel_reserve_hit",
            "visual": "",
            "passThrough": 0.3,
            "explosionShielding": 0.8
        },
        # Class: CfgVehicles\MRAP_02_base_F\HitPoints\HitGlass11,
        "HitGlass11": {
            "name": "glass11",
            "visual": "glass11",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitRGlass,
        "HitRGlass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni P",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitLGlass,
        "HitLGlass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni L",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitLBWheel,
        "HitLBWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_4_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitLMWheel,
        "HitLMWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_3_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitRBWheel,
        "HitRBWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_4_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles\Car_F\HitPoints\HitRMWheel,
        "HitRMWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_3_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        }
    },
    "canHideDriver": 0,
    "driverCompartments": "Compartment1",
    "cargoCompartments": ["Compartment1"],
    # Class: CfgVehicles\rhs_tigr_base\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla
        "LSvetla": {
            "color": [800,900,650],
            "ambient": [2,2,2],
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "innerAngle": 50,
            "outerAngle": 140,
            "coneFadeCoef": 10,
            "intensity": 2.5,
            "useFlare": 1,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\RSvetla,
        "RSvetla": {
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "innerAngle": 50,
            "outerAngle": 140,
            "coneFadeCoef": 10,
            "intensity": 2.5,
            "useFlare": 1,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\CSvetla,
        "CSvetla": {
            "position": "C svetlo",
            "direction": "konec C svetla",
            "hitpoint": "C svetlo",
            "selection": "C svetlo",
            "innerAngle": 35,
            "outerAngle": 179,
            "intensity": 0.85,
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "coneFadeCoef": 10,
            "useFlare": 1,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Searchlight,
        "Searchlight": {
            "position": "Searchlight_pos",
            "direction": "Searchlight_dir",
            "hitpoint": "Searchlight",
            "selection": "Searchlight",
            "innerAngle": 35,
            "outerAngle": 179,
            "intensity": 0.85,
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "coneFadeCoef": 10,
            "useFlare": 1,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Right2,
        "Right2": {
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Right2\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "dayLight": 0,
            "flareSize": 0.85
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Left2,
        "Left2": {
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Left2\Attenuation,
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
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "size": 1,
            "dayLight": 0,
            "flareSize": 0.85
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Left,
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Right,
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Left\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Right2,
        "Long_Right2": {
            "useFlare": 1,
            "position": "light_R_Long_flare",
            "innerAngle": 50,
            "outerAngle": 139,
            "coneFadeCoef": 51,
            "flareSize": 1,
            "intensity": 1,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Right2\Attenuation,
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
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Left2,
        "Long_Left2": {
            "useFlare": 1,
            "position": "light_L_Long_flare",
            "innerAngle": 50,
            "outerAngle": 139,
            "coneFadeCoef": 51,
            "flareSize": 1,
            "intensity": 1,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Left2\Attenuation,
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
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\cabin,
        "cabin": {
            "color": [40,350,960],
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
            "useFlare": 0,
            "flareSize": 1,
            "flareMaxDistance": 5,
            "dayLight": 1,
            "blinking": 0,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\cabin\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 1,
                "hardLimitEnd": 1.5
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\cargo_light_1,
        "cargo_light_1": {
            "color": [40,350,960],
            "position": "cargo_light_1",
            "direction": "cargo_light_1_dir",
            "hitpoint": "cargo_light_1",
            "selection": "cargo_light_1",
            "intensity": 3,
            "useFlare": 0,
            "coneFadeCoef": 0.1,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\cargo_light_1\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 70,
                "hardLimitStart": 0.5,
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
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\reverse_light_1,
        "reverse_light_1": {
            "intensity": 0.1,
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "position": "reverse_light_1_pos",
            "direction": "reverse_light_1_dir",
            "hitpoint": "reverse_light_hit",
            "selection": "reverse_light",
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "coneFadeCoef": 10,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\reverse_light_2,
        "reverse_light_2": {
            "position": "reverse_light_2_pos",
            "direction": "reverse_light_2_dir",
            "intensity": 0.1,
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "hitpoint": "reverse_light_hit",
            "selection": "reverse_light",
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "coneFadeCoef": 10,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        }
    },
    "aggregateReflectors": [["LSvetla","RSvetla"],["Left2","Right2"],["CSvetla"],["Long_Left2","Long_Right2"],["reverse_light_1","reverse_light_2"]],
    "armorLights": 0.1,
    # Class: CfgVehicles\rhs_tigr_base\UserActions,
    "UserActions": {
        # Class: CfgVehicles\rhs_tigr_base\UserActions\lights_toggle
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
        # Class: CfgVehicles\rhs_tigr_base\UserActions\cabinlights_toggle,
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
        # Class: CfgVehicles\rhs_tigr_base\UserActions\searchlight_toggle,
        "searchlight_toggle": {
            "shortcut": "",
            "displayName": "Toggle rear searchlight",
            "statement": "[this,3] call rhs_fnc_carLightToggle",
            "position": "",
            "radius": 12,
            "priority": 1.5,
            "showWindow": 0,
            "onlyForplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)"
        }
    },
    "soundGetIn": ["A3|Sounds_F|vehicles2|soft|Mrap_02|Mrap_02_Enter",0.446684,1],
    "soundGetOut": ["A3|Sounds_F|vehicles2|soft|Mrap_02|Mrap_02_Exit",0.446684,1,40],
    "soundDammage": ["",0.562341,1],
    "soundEngineOnInt": ["A3|Sounds_F|vehicles2|soft|Mrap_02|Mrap_02_Engine_Ext_Start",0.501187,1],
    "soundEngineOffInt": ["A3|Sounds_F|vehicles2|soft|Mrap_02|Mrap_02_Engine_Ext_stop",0.398107,1],
    "soundEngineOnExt": ["A3|Sounds_F|vehicles2|soft|Mrap_02|Mrap_02_Engine_Ext_Start",1.99526,1,50],
    "soundEngineOffExt": ["A3|Sounds_F|vehicles2|soft|Mrap_02|Mrap_02_Engine_Ext_stop",1.99526,1,50],
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
    "features": "Randomization: No						<br />Camo selections: 2 - the body, wheels and accessories						<br />Script door sources: Door_LF, Door_RF, Door_LB, Door_RB, Door_rear						<br />Script animations: None						<br />Executed scripts: None						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: 1 to 4",
    # Class: CfgVehicles\MRAP_02_base_F\SpeechVariants,
    "SpeechVariants": {
        # Class: CfgVehicles\MRAP_02_base_F\SpeechVariants\Default
        "Default": {
            "speechSingular": ["veh_vehicle_MRAP_s"],
            "speechPlural": ["veh_vehicle_MRAP_p"]
        }
    },
    "nameSound": "veh_vehicle_MRAP_s",
    "_generalMacro": "MRAP_02_base_F",
    "transportMaxBackpacks": 5,
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 1,
    "crewCrashProtection": 1.35,
    "crewExplosionProtection": 0.9999,
    "enableRadio": 1,
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "armorStructural": 5,
    "cost": 500000,
    "threat": [0.8,0.6,0.6],
    # Class: CfgVehicles\MRAP_02_base_F\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\MRAP_02_base_F\Exhausts\Exhaust1
        "Exhaust1": {
            "position": "exhaust_pos",
            "direction": "exhaust_dir",
            "effect": "ExhaustEffectHTruck"
        }
    },
    "wheelDamageThreshold": 0.18,
    "wheelDamageRadiusCoef": 0.75,
    "wheelDestroyRadiusCoef": 0.48,
    "cargoGetInAction": ["GetInMantis"],
    "cargoGetOutAction": ["GetOutMantis"],
    "smokeLauncherGrenadeCount": 8,
    "smokeLauncherVelocity": 14,
    "smokeLauncherOnTurret": 0,
    "smokeLauncherAngle": 150,
    "extCameraPosition": [0,2,-9],
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
    "dammageHalf": [],
    "dammageFull": [],
    "explosionShielding": 1,
    "gunnerHasFlares": 0,
    "steerAheadSimul": 0.5,
    "steerAheadPlan": 0.35,
    "predictTurnPlan": 2,
    "predictTurnSimul": 1.5,
    "epeImpulseDamageCoef": 15,
    "accelAidForceYOffset": -1,
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    # Class: CfgVehicles\Car_F\PlayerSteeringCoefficients,
    "PlayerSteeringCoefficients": {
        "turnIncreaseConst": 1,
        "turnIncreaseLinear": 1,
        "turnIncreaseTime": 0,
        "turnDecreaseConst": 5,
        "turnDecreaseLinear": 0,
        "turnDecreaseTime": 0,
        "maxTurnHundred": 1
    },
    # Class: CfgVehicles\Car_F\ViewPilot,
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
    # Class: CfgVehicles\Car_F\NewTurret,
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
    "driverLeftHandAnimName": "drivewheel",
    "driverRightHandAnimName": "drivewheel",
    "holdOffroadFormation": 1,
    # Class: CfgVehicles\Car_F\NVGMarkers,
    "NVGMarkers": {
        # Class: CfgVehicles\Car_F\NVGMarkers\NVGMarker01
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
    "accuracy": 0.25,
    "audible": 5,
    "soundEnviron": ["",0.000562341,1],
    "soundCrash": ["A3|sounds_f|dummysound",1,1],
    "collisionEffect": "collisionEffect",
    "hideUnitInfo": 0,
    "htMin": 60,
    "htMax": 1800,
    "afMax": 100,
    "mfMax": 80,
    "mFact": 1,
    "tBody": 150,
    "transportMaxWeapons": 12,
    "transportMaxMagazines": 64,
    "maximumLoad": 2000,
    "supplyRadius": -1,
    "memoryPointSupply": "doplnovani",
    # Class: CfgVehicles\Car_F\TransportBackpacks,
    "TransportBackpacks": {
    },
    "brakeTorque": 6000,
    "longStiff": 15000,
    "latStiffX": 2000,
    "latStiffY": 18000,
    "wheelMask": "wheel_X_X",
    "numberPhysicalWheels": 4,
    "camShakeCoef": 0.2,
    "maxGForce": 3,
    # Class: CfgVehicles\Car_F\camShakeGForce,
    "camShakeGForce": {
        "power": 2,
        "frequency": 60,
        "distance": 0,
        "minSpeed": 60
    },
    # Class: CfgVehicles\Car_F\Components,
    "Components": {
        # Class: CfgVehicles\Car\Components\AICarSteeringComponent
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
        # Class: CfgVehicles\LandVehicle\Components\TransportCountermeasuresComponent,
        "TransportCountermeasuresComponent": {
        }
    },
    "unloadInCombat": 1,
    "limitedSpeedCoef": 0.5,
    "hullDamageCauseExplosion": 1,
    # Class: CfgVehicles\Car\PlateInfos,
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
    "preferRoads": 1,
    "unitInfoType": "RscUnitInfo",
    "formationX": 20,
    "formationZ": 20,
    "type": 0,
    "typicalCargo": ["Soldier"],
    "scudModel": "",
    "damperSize": 0.1,
    "damperForce": 1,
    "damperDamping": 1,
    "inputTurnCurve": [[0,[0,0,1,1]],[30,[0,0,0.2,0.008,0.4,0.032,0.6,0.216,0.8,0.512,1,1]]],
    "soundEngine": ["",1.77828,0.9],
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffects"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffects"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffects"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffects"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","LDustEffects"]],
    # Class: CfgVehicles\Car\DestructionEffects,
    "DestructionEffects": {
        # Class: CfgVehicles\Car\DestructionEffects\Light1
        "Light1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 0.001,
            "interval": 1,
            "lifeTime": 3,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles\Car\DestructionEffects\Sound,
        "Sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles\Car\DestructionEffects\Fire1,
        "Fire1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1Small",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Car\DestructionEffects\Refract1,
        "Refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefractSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Car\DestructionEffects\Smoke1,
        "Smoke1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmokeSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Car\DestructionEffects\Sparks1,
        "Sparks1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifeTime": 0
        },
        # Class: CfgVehicles\Car\DestructionEffects\FireSparks1,
        "FireSparks1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2.8
        },
        # Class: CfgVehicles\Car\DestructionEffects\Fire2,
        "Fire2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Car\DestructionEffects\Smoke1_2,
        "Smoke1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Car\DestructionEffects\Smoke2,
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
    # Class: CfgVehicles\LandVehicle\CommanderOptics,
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
        # Class: CfgVehicles\LandVehicle\CommanderOptics\ViewOptics,
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
        # Class: CfgVehicles\LandVehicle\CommanderOptics\ViewGunner,
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
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
        "showCrewAim": 0
    },
    "wheelDestroyThreshold": 0.99,
    "weaponsGroup1": 1,
    "weaponsGroup2": "2 + 		4",
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    # Class: CfgVehicles\AllVehicles\SquadTitles,
    "SquadTitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memoryPointDriverOptics": ["driverview","pilot"],
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInDriverPrecise": "pos driver",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionShowDamage": "poskozeni",
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
    # Class: CfgVehicles\AllVehicles\ViewOptics,
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
    # Class: CfgVehicles\AllVehicles\MFD,
    "MFD": {
    },
    # Class: CfgVehicles\AllVehicles\SoundEvents,
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
    "getInRadius": 2.5,
    "enableWatch": 0,
    "lockDetectionSystem": 0,
    "incomingMissileDetectionSystem": 0,
    "usePreciseGetInAction": 0,
    "allowTabLock": 1,
    "showAllTargets": 0,
    "dustFrontLeftPos": "dustFrontLeft",
    "dustFrontRightPos": "dustFrontRight",
    "dustBackLeftPos": "dustBackLeft",
    "dustBackRightPos": "dustBackRight",
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
    # Class: CfgVehicles\All\MarkerLights,
    "MarkerLights": {
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
    "driverOpticsModel": "",
    "driverOpticsEffect": [],
    "driverOpticsColor": [1,1,1,1],
    "forceHideDriver": 0,
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
    "driverCanEject": 1,
    "airCapacity": 10,
    "waterDamageEngine": 0.2,
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "coefSpeedInside": 2,
    "windSockExist": 0,
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    "minGForce": 0.2,
    "gForceShakeAttenuation": 0.5,
    # Class: CfgVehicles\All\camShakeDamage,
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
    "insideDetectCoef": 0.05,
}