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
    # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets [Indent level: 1],
    "Turrets": {
        # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret [Indent level: 2]
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
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\ViewGunner [Indent level: 3],
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
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\OpticsIn [Indent level: 3],
            "OpticsIn": {
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\OpticsIn\Sight [Indent level: 4]
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
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\Hitpoints [Indent level: 3],
            "Hitpoints": {
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\Hitpoints\Hit_PKM_Turret [Indent level: 4]
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
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\Hitpoints\Hit_PKM_Gun [Indent level: 4],
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
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\ViewOptics [Indent level: 3],
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
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\Components [Indent level: 3],
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
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
            "preciseGetInOut": 0,
            "turretFollowFreeLook": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "dontCreateAI": 0,
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
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\OpticsIn [Indent level: 3],
            "OpticsIn": {
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\OpticsIn\Sight [Indent level: 4]
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
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\Hitpoints [Indent level: 3],
            "Hitpoints": {
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\Hitpoints\Hit_AGS_Turret [Indent level: 4]
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
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\Hitpoints\Hit_AGS_Gun [Indent level: 4],
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
                # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\AGS_Turret\Hitpoints\Hit_AGS_Optic [Indent level: 4],
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
            # Class: CfgVehicles\rhs_tigr_sts_vdv\Turrets\MainTurret\ViewGunner [Indent level: 3],
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
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\ViewOptics [Indent level: 3],
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
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\Components [Indent level: 3],
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
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
            "preciseGetInOut": 0,
            "turretFollowFreeLook": 0,
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
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\rhs_tigr_base\Turrets\CargoTurret_01 [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_base\Turrets\CargoTurret_01\TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[0,0],[0,0]],
                "limitsArrayBottom": [[0,0],[0,0]]
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
            # Class: CfgVehicles\AllVehicles\CargoTurret\Hitpoints [Indent level: 2],
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
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
            "TurnOut": {
                "turnOffset": 0
            },
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\rhs_tigr_base\Turrets\CargoTurret_02 [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_base\Turrets\CargoTurret_01\TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[0,0],[0,0]],
                "limitsArrayBottom": [[0,0],[0,0]]
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
            # Class: CfgVehicles\AllVehicles\CargoTurret\Hitpoints [Indent level: 2],
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
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
            "TurnOut": {
                "turnOffset": 0
            },
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        }
    },
    # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_pkm_reload [Indent level: 2]
        "weapon_pkm_reload": {
            "source": "reload",
            "weapon": "rhs_weap_pkm_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_pkm_ReloadMagazine [Indent level: 2],
        "weapon_pkm_ReloadMagazine": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_pkm_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_pkm_ammoRandom [Indent level: 2],
        "weapon_pkm_ammoRandom": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkm_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\Revolving [Indent level: 2],
        "Revolving": {
            "source": "revolving",
            "weapon": "rhs_weap_pkm_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_ags_reload [Indent level: 2],
        "weapon_ags_reload": {
            "source": "reload",
            "weapon": "RHS_weap_AGS30_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_ags_ReloadMagazine [Indent level: 2],
        "weapon_ags_ReloadMagazine": {
            "source": "reloadmagazine",
            "weapon": "RHS_weap_AGS30_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\weapon_ags_ammoRandom [Indent level: 2],
        "weapon_ags_ammoRandom": {
            "source": "ammorandom",
            "weapon": "RHS_weap_AGS30_tigr"
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\rpg26_hide_1 [Indent level: 2],
        "rpg26_hide_1": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\rpg26_hide_2 [Indent level: 2],
        "rpg26_hide_2": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\rpg26_hide_3 [Indent level: 2],
        "rpg26_hide_3": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\rpg26_hide_4 [Indent level: 2],
        "rpg26_hide_4": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\turret_correct [Indent level: 2],
        "turret_correct": {
            "animPeriod": 1.8,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_sts_vdv\AnimationSources\hatch_gunner [Indent level: 2],
        "hatch_gunner": {
            "source": "user",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\HitSpare [Indent level: 2],
        "HitSpare": {
            "source": "Hit",
            "hitpoint": "HitSpare",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\UseSpare [Indent level: 2],
        "UseSpare": {
            "hitpoint": "UseSpare",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\hatch_front_door [Indent level: 2],
        "hatch_front_door": {
            "mass": 1,
            "source": "door",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\hatch_back_door [Indent level: 2],
        "hatch_back_door": {
            "mass": 1,
            "source": "door",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\spare_hide [Indent level: 2],
        "spare_hide": {
            "animPeriod": 1e-008,
            "source": "user",
            "displayName": "hide spare wheel",
            "mass": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\Door_LF [Indent level: 2],
        "Door_LF": {
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_UAZ_Door",
            "soundPosition": "door_1_1_axis"
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\Door_RF [Indent level: 2],
        "Door_RF": {
            "soundPosition": "door_1_2_axis",
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_UAZ_Door"
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\Door_Rear [Indent level: 2],
        "Door_Rear": {
            "soundPosition": "door_2_1_axis",
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_UAZ_Door"
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\HitGlass7 [Indent level: 2],
        "HitGlass7": {
            "hitpoint": "HitGlass7",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\HitGlass8 [Indent level: 2],
        "HitGlass8": {
            "hitpoint": "HitGlass8",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\HitGlass9 [Indent level: 2],
        "HitGlass9": {
            "hitpoint": "HitGlass9",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\HitGlass10 [Indent level: 2],
        "HitGlass10": {
            "hitpoint": "HitGlass10",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\longlights_hide [Indent level: 2],
        "longlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\shortlights_hide [Indent level: 2],
        "shortlights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\lights_hide [Indent level: 2],
        "lights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\searchlight_hide [Indent level: 2],
        "searchlight_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\AnimationSources\cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\MRAP_02_base_F\AnimationSources\HitReserveWheel [Indent level: 2],
        "HitReserveWheel": {
            "source": "Hit",
            "hitpoint": "HitReserveWheel",
            "raw": 1
        },
        # Class: CfgVehicles\MRAP_02_base_F\AnimationSources\Door_LM [Indent level: 2],
        "Door_LM": {
            "source": "door",
            "animPeriod": 0.8,
            "initPhase": 0
        },
        # Class: CfgVehicles\MRAP_02_base_F\AnimationSources\Door_RM [Indent level: 2],
        "Door_RM": {
            "source": "door",
            "animPeriod": 0.8,
            "initPhase": 0
        },
        # Class: CfgVehicles\MRAP_02_base_F\AnimationSources\HitGlass6 [Indent level: 2],
        "HitGlass6": {
            "source": "Hit",
            "hitpoint": "HitGlass6",
            "raw": 1
        },
        # Class: CfgVehicles\MRAP_02_base_F\AnimationSources\HitGlass11 [Indent level: 2],
        "HitGlass11": {
            "hitpoint": "HitGlass11",
            "source": "Hit",
            "raw": 1
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
        }
    },
    # Class: CfgVehicles\rhs_tigr_sts_vdv\EventHandlers [Indent level: 1],
    "EventHandlers": {
        # Class: CfgVehicles\rhs_tigr_sts_vdv\EventHandlers\RHS_EventHandlers [Indent level: 2]
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
        # Class: CfgVehicles\rhs_tigr_sts_vdv\EventHandlers\RHS_TigrHandler [Indent level: 2],
        "RHS_TigrHandler": {
        },
        "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};",
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
    "category": "Car",
    "insideSoundCoef": 0.4,
    "slingLoadCargoMemoryPoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "canfloat": 0,
    "cargoaction": ["RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo01","RHS_UAZ_Cargo02"],
    "cargoIsCoDriver": [0,0],
    "castDriverShadow": 1,
    # Class: CfgVehicles\rhs_tigr_base\Library [Indent level: 1],
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
    # Class: CfgVehicles\rhs_tigr_base\complexGearbox [Indent level: 1],
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
    # Class: CfgVehicles\rhs_tigr_base\Wheels [Indent level: 1],
    "Wheels": {
        # Class: CfgVehicles\rhs_tigr_base\Wheels\LF [Indent level: 2]
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
        # Class: CfgVehicles\rhs_tigr_base\Wheels\LR [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\Wheels\RF [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\Wheels\RR [Indent level: 2],
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
    # Class: CfgVehicles\rhs_tigr_base\Sounds [Indent level: 1],
    "Sounds": {
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Idle_ext [Indent level: 2]
        "Idle_ext": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_tigr_idle_ext",0.698107,1,250],
            "frequency": "0.75	+	((rpm/	2700) factor[(610/	2700),(2700/	2700)])*0.95",
            "volume": "engineOn*camPos*(((rpm/	2700) factor[(10/	2700),(50/	2700)])	*	((rpm/	2700) factor[(800/	2700),(600/	2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Engine [Indent level: 2],
        "Engine": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_tigr_idle_ext",0.446684,1,350],
            "frequency": "0.75	+	((rpm/	2700) factor[(610/	2700),(2700/	2700)])*0.95",
            "volume": "engineOn*camPos*(((rpm/	2700) factor[(620/	2700),(820/	2700)])	*	((rpm/	2700) factor[(2700/	2700),(2700/	2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\EngineThrust [Indent level: 2],
        "EngineThrust": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_exhaust_low1",0.5,1,250],
            "frequency": "0.65	+	((rpm/	2700) factor[(610/	2700),(6400/	2700)])*0.75",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.4,1])))*(((rpm/	2700) factor[(620/	2700),(820/	2700)])	*	((rpm/	2700) factor[(2700/	2700),(2700/	2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\GearboxWhine_Ext [Indent level: 2],
        "GearboxWhine_Ext": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_axle_whine_ext",0.35,1,250],
            "frequency": "0.85	+	((rpm/	2700) factor[(610/	2700),(2700/	2700)])*0.95",
            "volume": "engineOn*camPos*(((rpm/	2700) factor[(700/	2700),(850/	2700)])	*	((rpm/	2700) factor[(2700/	2700),(2700/	2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Turbo_Ext [Indent level: 2],
        "Turbo_Ext": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|turbo_ext",0.2,1,50],
            "frequency": "0.85	+	((rpm/	2700) factor[(610/	2700),(2700/	2700)])*0.95",
            "volume": "engineOn*camPos*(((rpm/ 2700) factor[(620/  2700),(820/ 2700)]) * ((rpm/  2700) factor[(2700/ 2700),(2700/  2700)]))*2.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Idle_int [Indent level: 2],
        "Idle_int": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_tigr_idle_int",0.6,1],
            "frequency": "0.75 + ((rpm/  2700) factor[(610/  2700),(2700/  2700)])*0.95",
            "volume": "engineOn*(1-camPos)*(((rpm/ 2700) factor[(10/ 2700),(50/  2700)]) * ((rpm/  2700) factor[(800/  2700),(600/ 2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Engine_int [Indent level: 2],
        "Engine_int": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_tigr_idle_int",0.6,1],
            "frequency": "0.75 + ((rpm/  2700) factor[(610/  2700),(2700/  2700)])*0.95",
            "volume": "engineOn*(1-camPos)*(((rpm/ 2700) factor[(620/  2700),(820/ 2700)]) * ((rpm/  2700) factor[(2700/ 2700),(2700/  2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\EngineThrust_int [Indent level: 2],
        "EngineThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_exhaust_low1",0.4,1],
            "frequency": "0.85	+	((rpm/	2700) factor[(610/	2700),(2700/	2700)])*0.75",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.4,1])))*(((rpm/  2700) factor[(620/  2700),(820/ 2700)]) * ((rpm/  2700) factor[(2700/ 2700),(2700/  2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\GearboxWhine_Int [Indent level: 2],
        "GearboxWhine_Int": {
            "sound": ["rhsafrf|addons|rhs_vehiclesounds|sounds|soft|Tigr|rhs_axle_whine_int",0.2,1],
            "frequency": "0.85 + ((rpm/  2700) factor[(610/  2700),(2700/  2700)])*0.95",
            "volume": "engineOn*(1-camPos)*(((rpm/ 2700) factor[(700/  2700),(850/ 2700)]) * ((rpm/  2700) factor[(2700/ 2700),(2700/  2700)]))*1.0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Sounds\Turbo_Int [Indent level: 2],
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
    # Class: CfgVehicles\rhs_tigr_base\TransportMagazines [Indent level: 1],
    "TransportMagazines": {
        # Class: CfgVehicles\rhs_tigr_base\TransportMagazines\_xx_rhs_30Rnd_545x39_7N10_AK [Indent level: 2]
        "_xx_rhs_30Rnd_545x39_7N10_AK": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": 4
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportMagazines\_xx_rhs_100Rnd_762x54mmR [Indent level: 2],
        "_xx_rhs_100Rnd_762x54mmR": {
            "magazine": "rhs_100Rnd_762x54mmR",
            "count": 8
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportMagazines\_xx_rhs_mag_rdg2_white [Indent level: 2],
        "_xx_rhs_mag_rdg2_white": {
            "magazine": "rhs_mag_rdg2_white",
            "count": 2
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportMagazines\_xx_rhs_mag_rgd5 [Indent level: 2],
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 6
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportMagazines\_xx_rhs_rpg26_mag [Indent level: 2],
        "_xx_rhs_rpg26_mag": {
            "magazine": "rhs_rpg26_mag",
            "count": 4
        }
    },
    # Class: CfgVehicles\rhs_tigr_base\TransportWeapons [Indent level: 1],
    "TransportWeapons": {
        # Class: CfgVehicles\rhs_tigr_base\TransportWeapons\_xx_rhs_weap_rpg26 [Indent level: 2]
        "_xx_rhs_weap_rpg26": {
            "weapon": "rhs_weap_rpg26",
            "count": 4
        }
    },
    # Class: CfgVehicles\rhs_tigr_base\TransportItems [Indent level: 1],
    "TransportItems": {
        # Class: CfgVehicles\rhs_tigr_base\TransportItems\_xx_FirstAidKit [Indent level: 2]
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportItems\_xx_Medikit [Indent level: 2],
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles\rhs_tigr_base\TransportItems\_xx_Toolkit [Indent level: 2],
        "_xx_Toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    "hiddenSelections": ["camo1","camo2","camo3","camo4","camo5","n1","n2","n3","n4","i1","i2","i3","i4"],
    "hiddenSelectionsTextures": ["rhsafrf|addons|rhs_tigr|data|rhs_tigr_co.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_01_co.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_02_co.paa","rhsafrf|addons|rhs_tigr|sts_proxies|data|tigr_ext_ads_co.paa","rhsafrf|addons|rhs_tigr|m_proxies|data|tigr_m_adds_co.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa"],
    # Class: CfgVehicles\rhs_tigr_base\textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles\rhs_tigr_base\textureSources\standard [Indent level: 2]
        "standard": {
            "displayName": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_tigr|data|rhs_tigr_co.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_01_co.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_02_co.paa","rhsafrf|addons|rhs_tigr|sts_proxies|data|tigr_ext_ads_co.paa","rhsafrf|addons|rhs_tigr|m_proxies|data|tigr_m_adds_co.paa"],
            "factions": ["rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        },
        # Class: CfgVehicles\rhs_tigr_base\textureSources\Camo [Indent level: 2],
        "Camo": {
            "displayName": "Camo",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_tigr|data|rhs_tigr_co_camo.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_01_co.paa","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int_02_co.paa","rhsafrf|addons|rhs_tigr|sts_proxies|data|tigr_ext_ads_co.paa","rhsafrf|addons|rhs_tigr|m_proxies|data|tigr_m_adds_co.paa"],
            "factions": ["rhs_faction_vmf","rhs_faction_vdv","rhs_faction_vdv","rhs_faction_vv"]
        }
    },
    "textureList": [],
    # Class: CfgVehicles\rhs_tigr_base\Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles\rhs_tigr_base\Attributes\ObjectTexture [Indent level: 2]
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type [Indent level: 2],
        "rhs_decalNumber_type": {
            "displayName": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cDecalsTigr4NumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\Default [Indent level: 4]
                "Default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultValue": "Default"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\DefaultRed [Indent level: 4],
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\BoldRed [Indent level: 4],
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\CDF [Indent level: 4],
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\Handpaint [Indent level: 4],
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\HandpaintBlack [Indent level: 4],
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\Iraqi [Indent level: 4],
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber_type\values\LicensePlate [Indent level: 4],
                "LicensePlate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalNumber [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type [Indent level: 2],
        "rhs_decalArmy_type": {
            "displayName": "Define large door roundel type",
            "tooltip": "Decal type",
            "property": "rhs_decalArmy_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Army [Indent level: 4]
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "Army"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Honor [Indent level: 4],
                "Honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\HonorGDR [Indent level: 4],
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Platoon [Indent level: 4],
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\PlatoonGDR [Indent level: 4],
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\PlatoonVDV [Indent level: 4],
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy [Indent level: 2],
        "rhs_decalArmy": {
            "displayName": "Set large door roundel symbol",
            "tooltip": "Set large door roundel located on both sides. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalArmy",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cDecalsTigrRightArmyPlaces,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalPlatoon_type [Indent level: 2],
        "rhs_decalPlatoon_type": {
            "displayName": "Define small door roundel type",
            "property": "rhs_decalPlatoon_type",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "tooltip": "Decal type",
            "control": "Combo",
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Army [Indent level: 4]
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "Army"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Honor [Indent level: 4],
                "Honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\HonorGDR [Indent level: 4],
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\Platoon [Indent level: 4],
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\PlatoonGDR [Indent level: 4],
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalArmy_type\values\PlatoonVDV [Indent level: 4],
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                }
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_decalPlatoon [Indent level: 2],
        "rhs_decalPlatoon": {
            "displayName": "Set small door roundel symbol",
            "tooltip": "Define small door roundel located on both sides. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cDecalsTigrRightPlatoonPlaces,  _this getVariable ['rhs_decalPlatoon_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\rhs_hidespare [Indent level: 2],
        "rhs_hidespare": {
            "displayName": "Remove spare wheel",
            "property": "rhs_hidespare",
            "control": "CheckboxNumber",
            "expression": "_this animate ['spare_hide',_value,true]",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\Door_LF [Indent level: 2],
        "Door_LF": {
            "displayName": "Open front left door",
            "property": "Door_LF",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\Door_RF [Indent level: 2],
        "Door_RF": {
            "displayName": "Open front right door",
            "property": "Door_RF",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhs_tigr_base\Attributes\Door_Rear [Indent level: 2],
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
    # Class: CfgVehicles\rhs_tigr_base\RenderTargets [Indent level: 1],
    "RenderTargets": {
        # Class: CfgVehicles\rhs_tigr_base\RenderTargets\LeftMirror [Indent level: 2]
        "LeftMirror": {
            "renderTarget": "rendertarget0",
            # Class: CfgVehicles\rhs_tigr_base\RenderTargets\LeftMirror\CameraView1 [Indent level: 3],
            "CameraView1": {
                "pointPosition": "pp1",
                "pointDirection": "pd1",
                "renderQuality": 2,
                "renderVisionMode": 4,
                "fov": 0.7
            },
            "BBoxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles\rhs_tigr_base\RenderTargets\RightMirror [Indent level: 2],
        "RightMirror": {
            "renderTarget": "rendertarget1",
            # Class: CfgVehicles\rhs_tigr_base\RenderTargets\RightMirror\CameraView1 [Indent level: 3],
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
    # Class: CfgVehicles\rhs_tigr_base\Damage [Indent level: 1],
    "Damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_tigr|data|glass.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","rhsafrf|addons|rhs_btr70|data|kamaz_glass_in.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_tigr.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_dam_tigr.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_destr_tigr.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int01.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_dam_tigr_int01.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_destr_tigr.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_tigr_int02.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_dam_tigr_int02.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_destr_tigr.rvmat","rhsafrf|addons|rhs_tigr|sts_proxies|data|rhs_tigr_ext_ads.rvmat","rhsafrf|addons|rhs_tigr|sts_proxies|data|rhs_dam_tigr_ext_ads.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_destr_tigr.rvmat","rhsafrf|addons|rhs_tigr|m_proxies|data|rhs_tigrM_ext_ads.rvmat","rhsafrf|addons|rhs_tigr|m_proxies|data|rhs_dam_tigrM_ext_ads.rvmat","rhsafrf|addons|rhs_tigr|data|rhs_destr_tigr.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles\rhs_tigr_base\HitPoints [Indent level: 1],
    "HitPoints": {
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitLFWheel [Indent level: 2]
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
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitLF2Wheel [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitRFWheel [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitRF2Wheel [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitSpare [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\UseSpare [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitHull [Indent level: 2],
        "HitHull": {
            "armor": -200,
            "name": "karoserie",
            "visual": "zbytek",
            "passThrough": 0.2,
            "minimalHit": -0.2,
            "explosionShielding": 0.2,
            "radius": 0.25
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitBody [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitFuel [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine [Indent level: 2],
        "HitEngine": {
            "minimalHit": 0.02,
            "armor": 3.9,
            "name": "motor",
            "visual": "zbytek",
            # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke [Indent level: 4],
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1 [Indent level: 4],
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2 [Indent level: 4],
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds [Indent level: 4],
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
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "name": "glass2",
            "visual": "glass2",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass3 [Indent level: 2],
        "HitGlass3": {
            "name": "glass3",
            "visual": "glass3",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass4 [Indent level: 2],
        "HitGlass4": {
            "name": "glass4",
            "visual": "glass4",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass5 [Indent level: 2],
        "HitGlass5": {
            "name": "glass5",
            "visual": "glass5",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass6 [Indent level: 2],
        "HitGlass6": {
            "name": "glass6",
            "visual": "glass6",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass7 [Indent level: 2],
        "HitGlass7": {
            "name": "glass7",
            "visual": "glass7",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass8 [Indent level: 2],
        "HitGlass8": {
            "name": "glass8",
            "visual": "glass8",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass9 [Indent level: 2],
        "HitGlass9": {
            "name": "glass9",
            "visual": "glass9",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhs_tigr_base\HitPoints\HitGlass10 [Indent level: 2],
        "HitGlass10": {
            "name": "glass10",
            "visual": "glass10",
            "armor": 8.1,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\MRAP_02_base_F\HitPoints\HitReserveWheel [Indent level: 2],
        "HitReserveWheel": {
            "armor": 0.5,
            "material": -1,
            "name": "wheel_reserve_hit",
            "visual": "",
            "passThrough": 0.3,
            "explosionShielding": 0.8
        },
        # Class: CfgVehicles\MRAP_02_base_F\HitPoints\HitGlass11 [Indent level: 2],
        "HitGlass11": {
            "name": "glass11",
            "visual": "glass11",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
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
        # Class: CfgVehicles\Car_F\HitPoints\AnimationSources [Indent level: 2],
        "AnimationSources": {
        }
    },
    "canHideDriver": 0,
    "driverCompartments": "Compartment1",
    "cargoCompartments": ["Compartment1"],
    # Class: CfgVehicles\rhs_tigr_base\Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla [Indent level: 2]
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\RSvetla [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\CSvetla [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Searchlight [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Right2 [Indent level: 2],
        "Right2": {
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Right2\Attenuation [Indent level: 3],
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
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Left2 [Indent level: 2],
        "Left2": {
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Left2\Attenuation [Indent level: 3],
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
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Left [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Right [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Right2 [Indent level: 2],
        "Long_Right2": {
            "useFlare": 1,
            "position": "light_R_Long_flare",
            "innerAngle": 50,
            "outerAngle": 139,
            "coneFadeCoef": 51,
            "flareSize": 1,
            "intensity": 1,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Right2\Attenuation [Indent level: 3],
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
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Left2 [Indent level: 2],
        "Long_Left2": {
            "useFlare": 1,
            "position": "light_L_Long_flare",
            "innerAngle": 50,
            "outerAngle": 139,
            "coneFadeCoef": 51,
            "flareSize": 1,
            "intensity": 1,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\Long_Left2\Attenuation [Indent level: 3],
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
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\cabin [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\cabin\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 1,
                "hardLimitEnd": 1.5
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\cargo_light_1 [Indent level: 2],
        "cargo_light_1": {
            "color": [40,350,960],
            "position": "cargo_light_1",
            "direction": "cargo_light_1_dir",
            "hitpoint": "cargo_light_1",
            "selection": "cargo_light_1",
            "intensity": 3,
            "useFlare": 0,
            "coneFadeCoef": 0.1,
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\cargo_light_1\Attenuation [Indent level: 3],
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
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\reverse_light_1 [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhs_tigr_base\Reflectors\reverse_light_2 [Indent level: 2],
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
            # Class: CfgVehicles\rhs_tigr_base\Reflectors\LSvetla\Attenuation [Indent level: 3],
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
    # Class: CfgVehicles\rhs_tigr_base\UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles\rhs_tigr_base\UserActions\lights_toggle [Indent level: 2]
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
        # Class: CfgVehicles\rhs_tigr_base\UserActions\cabinlights_toggle [Indent level: 2],
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
        # Class: CfgVehicles\rhs_tigr_base\UserActions\searchlight_toggle [Indent level: 2],
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
    "ace_refuel_fuelCapacity": 138,
    "soundGetIn": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|handling|getin|mrap_2.ogg",0.5,1],
    "soundGetOut": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|handling|getout|mrap_2.ogg",0.5,1,40],
    "soundDammage": [".ogg",0.5,1],
    "soundEngineOnInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_02|mrap_02_start_int.ogg",1,1],
    "soundEngineOffInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_02|mrap_02_shut_int.ogg",1,1],
    "soundEngineOnExt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_02|mrap_02_start_ext.ogg",1,1,125],
    "soundEngineOffExt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_02|mrap_02_shut_ext.ogg",1,1,100],
    "buildCrash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_01.ogg",1.5,1,300],
    "buildCrash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_02.ogg",1.5,1,300],
    "buildCrash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_03.ogg",1.5,1,300],
    "buildCrash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_04.ogg",1.5,1,300],
    "buildCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "buildCrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "buildCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "buildCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundBuildingCrash": ["buildcrash0",0.25,"buildcrash1",0.25,"buildcrash2",0.25,"buildcrash3",0.25],
    "WoodCrash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_01.ogg",1.5,1,300],
    "WoodCrash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_02.ogg",1.5,1,300],
    "WoodCrash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_03.ogg",1.5,1,300],
    "WoodCrash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_04.ogg",1.5,1,300],
    "WoodCrash4": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_05.ogg",1.5,1,300],
    "WoodCrash5": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_06.ogg",1.5,1,300],
    "WoodCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_07",1.99526,1,75],
    "WoodCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_08",1.99526,1,75],
    "soundWoodCrash": ["woodcrash0",0.166,"woodcrash1",0.166,"woodcrash2",0.166,"woodcrash3",0.166,"woodcrash4",0.166,"woodcrash5",0.166],
    "armorCrash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_01.ogg",1.5,1,300],
    "armorCrash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_02.ogg",1.5,1,300],
    "armorCrash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_03.ogg",1.5,1,300],
    "armorCrash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_04.ogg",1.5,1,300],
    "armorCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "armorCrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "armorCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "armorCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundArmorCrash": ["armorcrash0",0.25,"armorcrash1",0.25,"armorcrash2",0.25,"armorcrash3",0.25],
    "Crash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_01.ogg",1.5,1,300],
    "Crash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_02.ogg",1.5,1,300],
    "Crash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_03.ogg",1.5,1,300],
    "Crash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_04.ogg",1.5,1,300],
    "Crash4": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_05.ogg",1.5,1,300],
    "Crash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "Crash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "Crash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundCrashes": ["crash0",0.2,"crash1",0.2,"crash2",0.2,"crash3",0.2,"crash4",0.2],
    "BushCrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_01",0.630957,1,50],
    "BushCrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_02",0.630957,1,50],
    "BushCrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_03",0.630957,1,50],
    "BushCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_03",0.630957,0.8,50],
    "soundBushCrash": ["BushCrash1",0.25,"BushCrash2",0.25,"BushCrash3",0.25,"BushCrash4",0.25],
    "features": "Randomization: No						<br />Camo selections: 2 - the body, wheels and accessories						<br />Script door sources: Door_LF, Door_RF, Door_LB, Door_RB, Door_rear						<br />Script animations: None						<br />Executed scripts: None						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: 1 to 4",
    # Class: CfgVehicles\MRAP_02_base_F\SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles\MRAP_02_base_F\SpeechVariants\Default [Indent level: 2]
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
    # Class: CfgVehicles\MRAP_02_base_F\Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles\MRAP_02_base_F\Exhausts\Exhaust1 [Indent level: 2]
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
    "tf_hasLRradio": 1,
    "tf_isolatedAmount": 0.7,
    "ace_cookoff_engineSmokeOffset": [0,-2,0],
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
    # Class: CfgVehicles\Car_F\PlayerSteeringCoefficients [Indent level: 1],
    "PlayerSteeringCoefficients": {
        "turnIncreaseConst": 1,
        "turnIncreaseLinear": 1,
        "turnIncreaseTime": 0,
        "turnDecreaseConst": 5,
        "turnDecreaseLinear": 0,
        "turnDecreaseTime": 0,
        "maxTurnHundred": 1
    },
    # Class: CfgVehicles\Car_F\ViewPilot [Indent level: 1],
    "ViewPilot": {
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
    "driverLeftHandAnimName": "drivewheel",
    "driverRightHandAnimName": "drivewheel",
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
    # Class: CfgVehicles\Car_F\TransportBackpacks [Indent level: 1],
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
    "unloadInCombat": 1,
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
    "ace_cargo_space": 4,
    "ace_cargo_hasCargo": 1,
    # Class: CfgVehicles\Car\ACE_Cargo [Indent level: 1],
    "ACE_Cargo": {
    },
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
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInDriverPrecise": "pos driver",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionShowDamage": "poskozeni",
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
    "ace_refuel_flowRate": 1,
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
    "insideDetectCoef": 0.05,
    "coefSpeedInside": 1,
    "windSockExist": 0,
    "SLX_XEH_DISABLED": 0,
}