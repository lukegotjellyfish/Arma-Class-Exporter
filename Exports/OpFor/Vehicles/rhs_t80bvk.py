rhs_t80bvk = {
    "editorPreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_t80bvk.paa",
    "author": "Red Hammer Studios",
    "displayName": "T-80BVK",
    "hiddenSelectionsTextures": ["rhsafrf|addons|rhs_t80|data|hull.pac","rhsafrf|addons|rhs_t80|data|turetbk.paa","","rhsafrf|addons|rhs_t80|data|searchlightopen_co.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa"],
    "hiddenSelectionsMaterials": ["rhsafrf|addons|rhs_t80|data|materials|hull_g.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_bk.rvmat","","rhsafrf|addons|rhs_t80|data|materials|searchlight.rvmat"],
    # Class: CfgVehicles\rhs_t80bvk\Turrets [Indent level: 1],
    "Turrets": {
        # Class: CfgVehicles\rhs_t80bvk\Turrets\MainTurret [Indent level: 2]
        "MainTurret": {
            "magazines": ["rhs_mag_3bm22_14","rhs_mag_3bk18m_8","rhs_mag_3of26_6","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_3d17","rhs_laserfcsmag","rhs_laserfcsmag"],
            # Class: CfgVehicles\rhs_t80bvk\Turrets\MainTurret\Turrets [Indent level: 3],
            "Turrets": {
                # Class: CfgVehicles\rhs_t80bvk\Turrets\MainTurret\Turrets\CommanderOptics [Indent level: 4]
                "CommanderOptics": {
                    "LodTurnedOut": 1200,
                    "weapons": [],
                    "magazines": [],
                    "outGunnerMayFire": 1,
                    "inGunnerMayFire": 1,
                    "gunBeg": "Mgun_end",
                    "gunEnd": "Mgun_start",
                    "body": "RHS_T80B_com_coppula",
                    "gun": "RHS_T80B_com_Gun",
                    "gunnerAction": "rhs_t80_commander_out",
                    "gunnerInAction": "rhs_T80_Commander_in",
                    "gunnerType": "rhs_msv_crew_commander",
                    "viewGunnerInExternal": 1,
                    "gunnerGetInAction": "GetInMedium",
                    "gunnerGetOutAction": "GetOutMedium",
                    "gunnerDoor": "hatchC",
                    "ejectDeadGunner": 0,
                    "minElev": -15,
                    "maxElev": 80,
                    "initElev": 0,
                    "minTurn": -360,
                    "maxTurn": 360,
                    "initTurn": 0,
                    "lockWhenDriverOut": 0,
                    "gunnerOutForceOptics": 0,
                    "animationSourceHatch": "HatchCommander",
                    "animationSourceBody": "obsTurret",
                    "animationSourceGun": "obsGun",
                    "memoryPointGunnerOptics": "commanderview",
                    "memoryPointGunnerOutOptics": "commander_out_view",
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                    "gunnerOutOpticsModel": "",
                    "nightVision": 1,
                    "stabilizedInAxes": 3,
                    "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
                    "gunnerHasFlares": 1,
                    # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderOptics\ViewGunner [Indent level: 5],
                    "ViewGunner": {
                        "initAngleX": 5,
                        "minAngleX": -65,
                        "maxAngleX": 85,
                        "initAngleY": 0,
                        "minAngleY": -150,
                        "maxAngleY": 150,
                        "initFov": 0.7,
                        "minFov": 0.25,
                        "maxFov": 1.1
                    },
                    # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderOptics\ViewOptics [Indent level: 5],
                    "ViewOptics": {
                        "initAngleX": 0,
                        "minAngleX": -30,
                        "maxAngleX": 30,
                        "initAngleY": 0,
                        "minAngleY": -100,
                        "maxAngleY": 100,
                        "initFov": 0.101,
                        "minFov": 0.102,
                        "maxFov": 0.102,
                        "visionMode": ["Normal"],
                        "minMoveX": 0,
                        "maxMoveX": 0,
                        "minMoveY": 0,
                        "maxMoveY": 0,
                        "minMoveZ": 0,
                        "maxMoveZ": 0,
                        "speedZoomMaxSpeed": 1e+010,
                        "speedZoomMaxFOV": 0
                    },
                    # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn [Indent level: 5],
                    "OpticsIn": {
                        # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Wide [Indent level: 6]
                        "Wide": {
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                            "initFov": 0.14,
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "minFov": 0.102,
                            "maxFov": 0.102,
                            "visionMode": ["Normal"],
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        },
                        # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Night [Indent level: 6],
                        "Night": {
                            "initFov": 0.166667,
                            "visionMode": ["NVG"],
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3_night.p3d",
                            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "minFov": 0.102,
                            "maxFov": 0.102,
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        },
                        # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Periscope [Indent level: 6],
                        "Periscope": {
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "initFov": 0.26,
                            "minFov": 0.26,
                            "maxFov": 0.26,
                            "visionMode": ["Normal"],
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
                            "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
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
                    "startEngine": 0,
                    "selectionFireAnim": "",
                    "memoryPointsGetInGunner": "pos commander",
                    "memoryPointsGetInGunnerDir": "pos commander dir",
                    "LodOpticsOut": 1200,
                    "canUseScanners": 0,
                    "allowTabLock": 0,
                    "turretInfoType": "RHS_RscWeaponTKN3_FCS",
                    # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components [Indent level: 5],
                    "Components": {
                        # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "VehicleSystemsDisplayManagerComponentLeft": {
                            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\EmptyDisplay [Indent level: 7]
                            "EmptyDisplay": {
                                "componentType": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\CrewDisplay [Indent level: 7],
                            "CrewDisplay": {
                                "componentType": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        },
                        # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "VehicleSystemsDisplayManagerComponentRight": {
                            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\EmptyDisplay [Indent level: 7]
                            "EmptyDisplay": {
                                "componentType": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\CrewDisplay [Indent level: 7],
                            "CrewDisplay": {
                                "componentType": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        }
                    },
                    # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints [Indent level: 5],
                    "HitPoints": {
                        # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitTurretCom [Indent level: 6]
                        "HitTurretCom": {
                            "isTurret": 1,
                            "armor": 0.3,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.03,
                            "explosionShielding": 0.6,
                            "radius": 0.25
                        },
                        # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitGunCom [Indent level: 6],
                        "HitGunCom": {
                            "isGun": 1,
                            "armor": 0.3,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.03,
                            "explosionShielding": 0.6,
                            "radius": 0.25
                        }
                    },
                    "proxyType": "CPCommander",
                    "proxyIndex": 1,
                    "gunnerName": "Commander",
                    "primaryGunner": 0,
                    "primaryObserver": 1,
                    "animationSourceCamElev": "camElev",
                    "soundServo": ["A3|sounds_f|dummysound",0.01,1,10],
                    "commanding": 2,
                    "gunnerOutOpticsColor": [0,0,0,1],
                    "gunnerOutOpticsShowCursor": 0,
                    "gunnerOutOpticsEffect": [],
                    "memoryPointGun": "gun_muzzle",
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
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
                    "TurretSpec": {
                        "showHeadPhones": 0
                    },
                    "gunnerOpticsColor": [0,0,0,1],
                    "gunnerForceOptics": 1,
                    "gunnerOpticsShowCursor": 0,
                    "gunnerFireAlsoInInternalCamera": 1,
                    "gunnerOutFireAlsoInInternalCamera": 1,
                    "gunnerUsesPilotView": 0,
                    "castGunnerShadow": 0,
                    "viewGunnerShadow": 1,
                    "viewGunnerShadowDiff": 1,
                    "viewGunnerShadowAmb": 1,
                    "hideWeaponsGunner": 1,
                    "canHideGunner": -1,
                    "forceHideGunner": 0,
                    "showHMD": 0,
                    "lockWhenVehicleSpeed": -1,
                    "gunnerCompartments": "Compartment1",
                    "LODTurnedIn": -1,
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
                    "preciseGetInOut": 0,
                    "turretFollowFreeLook": 0,
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
                    "showCrewAim": 0,
                    "ace_fcs_Enabled": 0,
                    "ace_fcs_MinDistance": 200,
                    "ace_fcs_MaxDistance": 5500,
                    "ace_fcs_DistanceInterval": 5
                },
                # Class: CfgVehicles\rhs_t80bvk\Turrets\MainTurret\Turrets\CommanderMG [Indent level: 4],
                "CommanderMG": {
                    "LodTurnedOut": 1200,
                    "maxElev": 25,
                    "gunnername": "Commander HMG",
                    "proxyindex": 2,
                    "dontCreateAi": 1,
                    "cantCreateAI": 1,
                    "body": "mg_turret",
                    "gun": "mg_gun",
                    "animationSourceBody": "mg_turret",
                    "animationSourceGun": "mg_gun",
                    "gunnerDoor": "",
                    "turretInfoType": "RHS_RscWeaponZeroing",
                    "discreteDistance": [100,200,300,400,500,600,800,900,1000,1100,1200,1400,1500,1800,1900,2000],
                    "discreteDistanceInitIndex": 2,
                    "stabilizedInAxes": 0,
                    "canHideGunner": 0,
                    "viewGunnerShadow": 0,
                    "memoryPointGunnerOutOptics": "commander_out_view",
                    "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                    "disableSoundAttenuation": 1,
                    "gunnerLeftHandAnimName": "",
                    "gunnerRightHandAnimName": "mg_handle2",
                    "maxVerticalRotSpeed": 0.35,
                    "minElev": -5,
                    "initElev": 0,
                    "initTurn": 0,
                    "weapons": ["rhs_weap_nsvt_t80"],
                    "magazines": ["rhs_mag_127x108mm_50","rhs_mag_127x108mm_50","rhs_mag_127x108mm_50"],
                    "selectionFireAnim": "zasleh3",
                    # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderMG\OpticsIn [Indent level: 5],
                    "OpticsIn": {
                        # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderMG\OpticsIn\Wide [Indent level: 6]
                        "Wide": {
                            "visionMode": ["Normal"],
                            "initFov": 0.583333,
                            "minFov": 0.583333,
                            "maxFov": 0.583333,
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
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
                        },
                        # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Night [Indent level: 6],
                        "Night": {
                            "initFov": 0.166667,
                            "visionMode": ["NVG"],
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3_night.p3d",
                            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "minFov": 0.102,
                            "maxFov": 0.102,
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        },
                        # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Periscope [Indent level: 6],
                        "Periscope": {
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "initFov": 0.26,
                            "minFov": 0.26,
                            "maxFov": 0.26,
                            "visionMode": ["Normal"],
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
                            "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
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
                    "gunnercompartments": "Compartment5",
                    "outGunnerMayFire": 1,
                    "inGunnerMayFire": 1,
                    "gunBeg": "Mgun_end",
                    "gunEnd": "Mgun_start",
                    "gunnerAction": "rhs_t80_commander_out",
                    "gunnerInAction": "rhs_T80_Commander_in",
                    "gunnerType": "rhs_msv_crew_commander",
                    "viewGunnerInExternal": 1,
                    "gunnerGetInAction": "GetInMedium",
                    "gunnerGetOutAction": "GetOutMedium",
                    "ejectDeadGunner": 0,
                    "minTurn": -360,
                    "maxTurn": 360,
                    "lockWhenDriverOut": 0,
                    "gunnerOutForceOptics": 0,
                    "animationSourceHatch": "HatchCommander",
                    "memoryPointGunnerOptics": "commanderview",
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                    "nightVision": 1,
                    "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
                    "gunnerHasFlares": 1,
                    # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderOptics\ViewGunner [Indent level: 5],
                    "ViewGunner": {
                        "initAngleX": 5,
                        "minAngleX": -65,
                        "maxAngleX": 85,
                        "initAngleY": 0,
                        "minAngleY": -150,
                        "maxAngleY": 150,
                        "initFov": 0.7,
                        "minFov": 0.25,
                        "maxFov": 1.1
                    },
                    # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Turrets\CommanderOptics\ViewOptics [Indent level: 5],
                    "ViewOptics": {
                        "initAngleX": 0,
                        "minAngleX": -30,
                        "maxAngleX": 30,
                        "initAngleY": 0,
                        "minAngleY": -100,
                        "maxAngleY": 100,
                        "initFov": 0.101,
                        "minFov": 0.102,
                        "maxFov": 0.102,
                        "visionMode": ["Normal"],
                        "minMoveX": 0,
                        "maxMoveX": 0,
                        "minMoveY": 0,
                        "maxMoveY": 0,
                        "minMoveZ": 0,
                        "maxMoveZ": 0,
                        "speedZoomMaxSpeed": 1e+010,
                        "speedZoomMaxFOV": 0
                    },
                    "startEngine": 0,
                    "memoryPointsGetInGunner": "pos commander",
                    "memoryPointsGetInGunnerDir": "pos commander dir",
                    "LodOpticsOut": 1200,
                    "canUseScanners": 0,
                    "allowTabLock": 0,
                    # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components [Indent level: 5],
                    "Components": {
                        # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "VehicleSystemsDisplayManagerComponentLeft": {
                            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\EmptyDisplay [Indent level: 7]
                            "EmptyDisplay": {
                                "componentType": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\CrewDisplay [Indent level: 7],
                            "CrewDisplay": {
                                "componentType": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        },
                        # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "VehicleSystemsDisplayManagerComponentRight": {
                            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\EmptyDisplay [Indent level: 7]
                            "EmptyDisplay": {
                                "componentType": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\CrewDisplay [Indent level: 7],
                            "CrewDisplay": {
                                "componentType": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            }
                        }
                    },
                    # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints [Indent level: 5],
                    "HitPoints": {
                        # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitTurretCom [Indent level: 6]
                        "HitTurretCom": {
                            "isTurret": 1,
                            "armor": 0.3,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.03,
                            "explosionShielding": 0.6,
                            "radius": 0.25
                        },
                        # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitGunCom [Indent level: 6],
                        "HitGunCom": {
                            "isGun": 1,
                            "armor": 0.3,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.03,
                            "explosionShielding": 0.6,
                            "radius": 0.25
                        }
                    },
                    "proxyType": "CPCommander",
                    "primaryGunner": 0,
                    "primaryObserver": 1,
                    "animationSourceCamElev": "camElev",
                    "soundServo": ["A3|sounds_f|dummysound",0.01,1,10],
                    "commanding": 2,
                    "gunnerOutOpticsColor": [0,0,0,1],
                    "gunnerOutOpticsShowCursor": 0,
                    "gunnerOutOpticsEffect": [],
                    "memoryPointGun": "gun_muzzle",
                    "soundElevation": ["",0.00316228,1],
                    "minOutElev": -4,
                    "maxOutElev": 20,
                    "initOutElev": 0,
                    "minOutTurn": -60,
                    "maxOutTurn": 60,
                    "initOutTurn": 0,
                    "maxHorizontalRotSpeed": 1.2,
                    "minCamElev": -90,
                    "maxCamElev": 90,
                    "initCamElev": 0,
                    "primary": 1,
                    "hasGunner": 1,
                    "turretCanSee": 0,
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
                    "TurretSpec": {
                        "showHeadPhones": 0
                    },
                    "gunnerOpticsColor": [0,0,0,1],
                    "gunnerForceOptics": 1,
                    "gunnerOpticsShowCursor": 0,
                    "gunnerFireAlsoInInternalCamera": 1,
                    "gunnerOutFireAlsoInInternalCamera": 1,
                    "gunnerUsesPilotView": 0,
                    "castGunnerShadow": 0,
                    "viewGunnerShadowDiff": 1,
                    "viewGunnerShadowAmb": 1,
                    "hideWeaponsGunner": 1,
                    "forceHideGunner": 0,
                    "showHMD": 0,
                    "lockWhenVehicleSpeed": -1,
                    "LODTurnedIn": -1,
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
                    "gunnerLeftLegAnimName": "",
                    "gunnerRightLegAnimName": "",
                    "preciseGetInOut": 0,
                    "turretFollowFreeLook": 0,
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
                }
            },
            # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Reflectors [Indent level: 3],
            "Reflectors": {
                # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Reflectors\Searchlight_FG125 [Indent level: 4]
                "Searchlight_FG125": {
                    "color": [1900,1300,950],
                    "ambient": [5,5,5],
                    "position": "Light_FG125",
                    "direction": "Light_FG125_end",
                    "hitpoint": "Light_FG125",
                    "selection": "Light_FG125",
                    "size": 1,
                    "innerAngle": 8,
                    "outerAngle": 15,
                    "coneFadeCoef": 1,
                    "intensity": 45,
                    "useFlare": 1,
                    "dayLight": 1,
                    "flareSize": 0.85,
                    # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Reflectors\Searchlight_FG125\Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 1,
                        "constant": 0,
                        "linear": 0,
                        "quadratic": 0.02,
                        "hardLimitStart": 630,
                        "hardLimitEnd": 660
                    }
                },
                # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Reflectors\Searchlight_FG125_Flare [Indent level: 4],
                "Searchlight_FG125_Flare": {
                    "color": [7,6,6.5],
                    "ambient": [22,22,22],
                    "position": "Light_FG125",
                    "direction": "Light_FG125_end",
                    "hitpoint": "Light_FG125",
                    "selection": "Light_FG125",
                    "size": 1,
                    "innerAngle": 30,
                    "outerAngle": 175,
                    "coneFadeCoef": 10,
                    "intensity": 100,
                    "useFlare": 1,
                    "dayLight": 0,
                    "flareSize": 1.85,
                    # Class: CfgVehicles\rhs_t80bv\Turrets\MainTurret\Reflectors\Searchlight_FG125_Flare\Attenuation [Indent level: 5],
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 0,
                        "quadratic": 10,
                        "hardLimitStart": 0,
                        "hardLimitEnd": 0.9
                    }
                }
            },
            "armorLights": 0.1,
            "initTurn": -13,
            "gunnerAction": "rhs_t80_gunner_out",
            "gunnerInAction": "rhs_t80_gunner_in",
            "viewGunnerInExternal": 1,
            "gunnerGetInAction": "GetInMedium",
            "gunnerGetOutAction": "GetOutMedium",
            "gunnerDoor": "hatchG",
            "ejectDeadGunner": 0,
            "startEngine": 0,
            "soundServo": ["rhsafrf|addons|rhs_t80|Sound|servo.ogg",6,1,20],
            "armorStructural": 60,
            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\HitPoints [Indent level: 3],
            "HitPoints": {
                # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\HitPoints\HitTurret [Indent level: 4]
                "HitTurret": {
                    "armor": -100,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passThrough": 0,
                    "minimalHit": 0.01,
                    "explosionShielding": 0.009,
                    "radius": 0.15
                },
                # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\HitPoints\HitGun [Indent level: 4],
                "HitGun": {
                    "armor": -150,
                    "material": -1,
                    "name": "zbran",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": -0.2,
                    "explosionShielding": 0.001,
                    "radius": 0.12
                }
            },
            "weapons": ["rhs_weap_2a46_2","rhs_weap_pkt","rhs_weap_902a","rhs_weap_fcs"],
            "memoryPointGun": "Mgun",
            "selectionFireAnim": "zasleh1",
            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_1g42.p3d",
            "gunnerOutOpticsModel": "",
            "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
            "nightVision": 1,
            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\OpticsIn [Indent level: 3],
            "OpticsIn": {
                # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\OpticsIn\day1 [Indent level: 4]
                "day1": {
                    "opticsDisplayName": "DAY",
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "initFov": 0.179487,
                    "minFov": 0.179487,
                    "maxFov": 0.179487,
                    "visionMode": ["Normal"],
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_1g42.p3d",
                    "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\OpticsIn\day2 [Indent level: 4],
                "day2": {
                    "opticsDisplayName": "DAYZOOM",
                    "initFov": 0.0777778,
                    "minFov": 0.0777778,
                    "maxFov": 0.0777778,
                    "visionMode": ["Normal"],
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_1g42.p3d",
                    "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
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
                },
                # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\OpticsIn\Periscope [Indent level: 4],
                "Periscope": {
                    "opticsDisplayName": "PERISCOPE",
                    "initFov": 0.466667,
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
                    "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "minFov": 0.179487,
                    "maxFov": 0.179487,
                    "visionMode": ["Normal"],
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\OpticsIn
ight3 [Indent level: 4],
                "night3": {
                    "opticsDisplayName": "NIGHT",
                    "initFov": 0.1,
                    "minFov": 0.1,
                    "maxFov": 0.1,
                    "visionMode": ["NVG"],
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_empty",
                    "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera3"],
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
            "minElev": -4,
            "maxElev": 18,
            "minTurn": -360,
            "maxTurn": 360,
            "initElev": 5,
            "lockWhenDriverOut": 1,
            "maxHorizontalRotSpeed": 0.4,
            "maxVerticalRotSpeed": 0.07,
            "radarType": 0,
            "turretInfoType": "rhs_gui_optic_t80_rangefinder",
            "discreteDistance": [100],
            "discreteDistanceInitIndex": 0,
            "canUseScanners": 0,
            "allowTabLock": 0,
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "body": "RHS_T80B_MainTurret",
            "gun": "RHS_T80B_MainGun",
            "stabilizedInAxes": 3,
            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\ViewGunner [Indent level: 3],
            "ViewGunner": {
                "initAngleX": 5,
                "minAngleX": -65,
                "maxAngleX": 85,
                "initAngleY": 0,
                "minAngleY": -150,
                "maxAngleY": 150,
                "initFov": 0.7,
                "minFov": 0.25,
                "maxFov": 1.1
            },
            # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Components [Indent level: 3],
            "Components": {
                # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\EmptyDisplay [Indent level: 5]
                    "EmptyDisplay": {
                        "componentType": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\CrewDisplay [Indent level: 5],
                    "CrewDisplay": {
                        "componentType": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                },
                # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "VehicleSystemsDisplayManagerComponentRight": {
                    # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\EmptyDisplay [Indent level: 5]
                    "EmptyDisplay": {
                        "componentType": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles\rhs_tank_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\CrewDisplay [Indent level: 5],
                    "CrewDisplay": {
                        "componentType": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                }
            },
            "commanding": 1,
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "primaryGunner": 1,
            "gunnerOutOpticsEffect": [],
            "animationSourceBody": "mainTurret",
            "animationSourceGun": "mainGun",
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerName": "Gunner",
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
            "turretCanSee": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerForceOptics": 1,
            "gunnerOpticsShowCursor": 0,
            "gunnerOutOpticsColor": [0,0,0,1],
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
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "forceHideGunner": 0,
            "outGunnerMayFire": 0,
            "inGunnerMayFire": 1,
            "showHMD": 0,
            "lockWhenVehicleSpeed": -1,
            "gunnerCompartments": "Compartment1",
            "LODTurnedIn": -1,
            "LODTurnedOut": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
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
            "preciseGetInOut": 0,
            "turretFollowFreeLook": 0,
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
            "memoryPointGunnerOptics": "gunnerview",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        }
    },
    "smokeLauncherGrenadeCount": 6,
    "smokeLauncherVelocity": 14,
    "smokeLauncherOnTurret": 1,
    "smokeLauncherAngle": 60,
    # Class: CfgVehicles\rhs_t80bvk\AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles\rhs_t80bvk\AnimationSources\kshield_unhide [Indent level: 2]
        "kshield_unhide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-010,
            "mass": -20,
            "displayName": "hide commander shield",
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles\rhs_t80bvk\AnimationSources\kdeck_unhide [Indent level: 2],
        "kdeck_unhide": {
            "initPhase": 0,
            "displayName": "hide commander deck",
            "author": "Red Hammer Studios",
            "source": "user",
            "animPeriod": 1e-010,
            "mass": -20
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\smokecap_revolving_source [Indent level: 2],
        "smokecap_revolving_source": {
            "source": "revolving",
            "weapon": "rhs_weap_902a"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_1_source [Indent level: 2],
        "era_1_source": {
            "source": "Hit",
            "hitpoint": "era_1_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_2_source [Indent level: 2],
        "era_2_source": {
            "source": "Hit",
            "hitpoint": "era_2_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_3_source [Indent level: 2],
        "era_3_source": {
            "source": "Hit",
            "hitpoint": "era_3_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_4_source [Indent level: 2],
        "era_4_source": {
            "source": "Hit",
            "hitpoint": "era_4_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_5_source [Indent level: 2],
        "era_5_source": {
            "source": "Hit",
            "hitpoint": "era_5_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_6_source [Indent level: 2],
        "era_6_source": {
            "source": "Hit",
            "hitpoint": "era_6_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_7_source [Indent level: 2],
        "era_7_source": {
            "source": "Hit",
            "hitpoint": "era_7_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_8_source [Indent level: 2],
        "era_8_source": {
            "source": "Hit",
            "hitpoint": "era_8_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_9_source [Indent level: 2],
        "era_9_source": {
            "source": "Hit",
            "hitpoint": "era_9_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_10_source [Indent level: 2],
        "era_10_source": {
            "source": "Hit",
            "hitpoint": "era_10_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_11_source [Indent level: 2],
        "era_11_source": {
            "source": "Hit",
            "hitpoint": "era_11_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_12_source [Indent level: 2],
        "era_12_source": {
            "source": "Hit",
            "hitpoint": "era_12_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_13_source [Indent level: 2],
        "era_13_source": {
            "source": "Hit",
            "hitpoint": "era_13_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_14_source [Indent level: 2],
        "era_14_source": {
            "source": "Hit",
            "hitpoint": "era_14_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_15_source [Indent level: 2],
        "era_15_source": {
            "source": "Hit",
            "hitpoint": "era_15_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_16_source [Indent level: 2],
        "era_16_source": {
            "source": "Hit",
            "hitpoint": "era_16_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_17_source [Indent level: 2],
        "era_17_source": {
            "source": "Hit",
            "hitpoint": "era_17_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_18_source [Indent level: 2],
        "era_18_source": {
            "source": "Hit",
            "hitpoint": "era_18_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_19_source [Indent level: 2],
        "era_19_source": {
            "source": "Hit",
            "hitpoint": "era_19_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_20_source [Indent level: 2],
        "era_20_source": {
            "source": "Hit",
            "hitpoint": "era_20_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_21_source [Indent level: 2],
        "era_21_source": {
            "source": "Hit",
            "hitpoint": "era_21_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_22_source [Indent level: 2],
        "era_22_source": {
            "source": "Hit",
            "hitpoint": "era_22_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_23_source [Indent level: 2],
        "era_23_source": {
            "source": "Hit",
            "hitpoint": "era_23_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_24_source [Indent level: 2],
        "era_24_source": {
            "source": "Hit",
            "hitpoint": "era_24_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_25_source [Indent level: 2],
        "era_25_source": {
            "source": "Hit",
            "hitpoint": "era_25_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_26_source [Indent level: 2],
        "era_26_source": {
            "source": "Hit",
            "hitpoint": "era_26_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_27_source [Indent level: 2],
        "era_27_source": {
            "source": "Hit",
            "hitpoint": "era_27_hitpoint"
        },
        # Class: CfgVehicles\rhs_t80bv\AnimationSources\era_28_source [Indent level: 2],
        "era_28_source": {
            "source": "Hit",
            "hitpoint": "era_28_hitpoint"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\sideskirt_unhide [Indent level: 2],
        "sideskirt_unhide": {
            "displayName": "hide side skirt",
            "mass": -220,
            "source": "user",
            "animPeriod": 1e-010,
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\fbskirt_unhide [Indent level: 2],
        "fbskirt_unhide": {
            "displayName": "hide front bottom rubber skirt",
            "mass": -100,
            "source": "user",
            "animPeriod": 1e-010,
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\ftskirt_unhide [Indent level: 2],
        "ftskirt_unhide": {
            "displayName": "hide front top rubber skirt",
            "mass": -50,
            "source": "user",
            "animPeriod": 1e-010,
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\log_unhide [Indent level: 2],
        "log_unhide": {
            "displayName": "hide back log",
            "mass": -100,
            "source": "user",
            "animPeriod": 1e-010,
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\snorkel_unhide [Indent level: 2],
        "snorkel_unhide": {
            "displayName": "mount snorkel",
            "mass": 1,
            "onPhaseChanged": "if(_this select 1 == 0)then{_this select 0 animate ['snorkel_unhide2',0];_this select 0 animate ['snorkel_unhide2',0];_this select 0 animate ['snorkel_hide',1];}else{_this select 0 animate ['snorkel_unhide2',1];_this select 0 animate ['snorkel_unhide2',1];_this select 0 animate ['snorkel_hide',0];}",
            "source": "user",
            "animPeriod": 1e-010,
            "author": "Red Hammer Studios"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\snorkel_unhide2 [Indent level: 2],
        "snorkel_unhide2": {
            "source": "user",
            "initPhase": 0,
            "animPeriod": 1e-010
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\snorkel_hide [Indent level: 2],
        "snorkel_hide": {
            "initPhase": 1,
            "source": "user",
            "animPeriod": 1e-010
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\TCOverrideTurret [Indent level: 2],
        "TCOverrideTurret": {
            "source": "user",
            "animPeriod": 4,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\recoil_source [Indent level: 2],
        "recoil_source": {
            "source": "door",
            "animPeriod": 6,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\reload_source [Indent level: 2],
        "reload_source": {
            "weapon": "rhs_weap_2a46_2",
            "source": "reload"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\reload_magazine_source [Indent level: 2],
        "reload_magazine_source": {
            "source": "reloadMagazine",
            "weapon": "rhs_weap_2a46_2"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\muzzle_rot_cannon [Indent level: 2],
        "muzzle_rot_cannon": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a46_2"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "weapon": "rhs_weap_nsvt_t80",
            "source": "ammorandom"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\muzzle_rot_coax [Indent level: 2],
        "muzzle_rot_coax": {
            "weapon": "rhs_weap_pkt",
            "source": "ammorandom"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\ReloadAnim [Indent level: 2],
        "ReloadAnim": {
            "source": "reload",
            "weapon": "rhs_weap_nsvt_t80"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\ReloadMagazine [Indent level: 2],
        "ReloadMagazine": {
            "source": "reloadmagazine",
            "weapon": "rhs_weap_nsvt_t80"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\Revolving [Indent level: 2],
        "Revolving": {
            "source": "revolving",
            "weapon": "rhs_weap_nsvt_t80"
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\autoloader [Indent level: 2],
        "autoloader": {
            "source": "user",
            "animPeriod": 3.25,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\elev [Indent level: 2],
        "elev": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\elev_bank [Indent level: 2],
        "elev_bank": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\lead [Indent level: 2],
        "lead": {
            "source": "user",
            "animperiod": 0.001
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\offset [Indent level: 2],
        "offset": {
            "source": "user",
            "animperiod": 0.0002
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\HatchC [Indent level: 2],
        "HatchC": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\HatchG [Indent level: 2],
        "HatchG": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\HatchD [Indent level: 2],
        "HatchD": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_tank_base\AnimationSources\turretHide [Indent level: 2],
        "turretHide": {
            "animPeriod": 1e-010,
            "source": "user",
            "initPhase": 0
        }
    },
    # Class: CfgVehicles\rhs_t80bvk\Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles\rhs_t80bvk\Attributes\ObjectTexture [Indent level: 2]
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_decalNumber_type [Indent level: 2],
        "rhs_decalNumber_type": {
            "displayName": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cRHST80NumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalNumber_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalNumber_type\values\Default [Indent level: 4]
                "Default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultValue": "Default"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalNumber_type\values\DefaultRed [Indent level: 4],
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalNumber_type\values\BoldRed [Indent level: 4],
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalNumber_type\values\CDF [Indent level: 4],
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalNumber_type\values\Handpaint [Indent level: 4],
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalNumber_type\values\HandpaintBlack [Indent level: 4],
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalNumber_type\values\Iraqi [Indent level: 4],
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalNumber_type\values\LicensePlate [Indent level: 4],
                "LicensePlate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_decalNumber [Indent level: 2],
        "rhs_decalNumber": {
            "collapsed": 1,
            "displayName": "Set side number",
            "tooltip": "Set side number. 3 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typeName": "Number",
            "defaultValue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHST80NumberPlaces}else{[_this, [['Number', cRHST80NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_decalArmy_type [Indent level: 2],
        "rhs_decalArmy_type": {
            "displayName": "Define army symbol type",
            "property": "rhs_decalArmy_type",
            # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalArmy_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalArmy_type\values\Army [Indent level: 4]
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "1"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalArmy_type\values\Platoon [Indent level: 4],
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalArmy_type\values\PlatoonGDR [Indent level: 4],
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalArmy_type\values\PlatoonVDV [Indent level: 4],
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalArmy_type\values\Honor [Indent level: 4],
                "Honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultValue": "0"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalArmy_type\values\HonorGDR [Indent level: 4],
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "typeName": "STRING"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_decalArmy [Indent level: 2],
        "rhs_decalArmy": {
            "displayName": "Set army symbol",
            "tooltip": "Define symbol located on gunner hatch. Usually used for army symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalArmy",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHST80ArmSymPlaces,  _this getVariable ['rhs_decalArmy_type','Army'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_decalHonor_type [Indent level: 2],
        "rhs_decalHonor_type": {
            "displayName": "Define honor symbol type",
            "property": "rhs_decalHonor_type",
            # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalHonor_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalHonor_type\values\Honor [Indent level: 4]
                "Honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultValue": "0"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalHonor_type\values\HonorGDR [Indent level: 4],
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalHonor_type\values\Platoon [Indent level: 4],
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalHonor_type\values\PlatoonGDR [Indent level: 4],
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalHonor_type\values\PlatoonVDV [Indent level: 4],
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalHonor_type\values\Army [Indent level: 4],
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "1"
                }
            },
            "tooltip": "Decal type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "typeName": "STRING"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_decalHonor [Indent level: 2],
        "rhs_decalHonor": {
            "displayName": "Set honor symbol",
            "tooltip": "Define symbol located on IR Lamp. Usually used for honor symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalHonor",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHST80HnrSymPlaces,  _this getVariable ['rhs_decalHonor_type','Honor'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_ammoslot_1_type [Indent level: 2],
        "rhs_ammoslot_1_type": {
            "displayName": "Ammo slot #1 type",
            "tooltip": "Define type of shell for #1 slot [AP rounds]",
            "property": "rhs_ammoslot_1_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm42_10 [Indent level: 4]
                "rhs_mag_3bm42_10": {
                    "name": "APFSDS-T 3BM42",
                    "value": "rhs_mag_3bm42",
                    "defaultValue": "rhs_mag_3bm42"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm9_10 [Indent level: 4],
                "rhs_mag_3bm9_10": {
                    "name": "APFSDS-T 3BM9",
                    "value": "rhs_mag_3bm9",
                    "defaultValue": "rhs_mag_3bm9"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm12_10 [Indent level: 4],
                "rhs_mag_3bm12_10": {
                    "name": "APFSDS-T 3BM12",
                    "value": "rhs_mag_3bm12",
                    "defaultValue": "rhs_mag_3bm12"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm15_10 [Indent level: 4],
                "rhs_mag_3bm15_10": {
                    "name": "APFSDS-T 3BM15",
                    "value": "rhs_mag_3bm15",
                    "defaultValue": "rhs_mag_3bm15"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm17_10 [Indent level: 4],
                "rhs_mag_3bm17_10": {
                    "name": "APFSDS-T 3BM17",
                    "value": "rhs_mag_3bm17",
                    "defaultValue": "rhs_mag_3bm17"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm22_10 [Indent level: 4],
                "rhs_mag_3bm22_10": {
                    "name": "APFSDS-T 3BM22",
                    "value": "rhs_mag_3bm22",
                    "defaultValue": "rhs_mag_3bm22"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm29_10 [Indent level: 4],
                "rhs_mag_3bm29_10": {
                    "name": "APFSDS-T 3BM29",
                    "value": "rhs_mag_3bm29",
                    "defaultValue": "rhs_mag_3bm29"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm26_10 [Indent level: 4],
                "rhs_mag_3bm26_10": {
                    "name": "APFSDS-T 3BM26",
                    "value": "rhs_mag_3bm26",
                    "defaultValue": "rhs_mag_3bm26"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm32_10 [Indent level: 4],
                "rhs_mag_3bm32_10": {
                    "name": "APFSDS-T 3BM32",
                    "value": "rhs_mag_3bm32",
                    "defaultValue": "rhs_mag_3bm32"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm42m_10 [Indent level: 4],
                "rhs_mag_3bm42m_10": {
                    "name": "APFSDS-T 3BM42M",
                    "value": "rhs_mag_3bm42m",
                    "defaultValue": "rhs_mag_3bm42m"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_1_type\values\rhs_mag_3bm46_10 [Indent level: 4],
                "rhs_mag_3bm46_10": {
                    "name": "APFSDS-T 3BM48",
                    "value": "rhs_mag_3bm46",
                    "defaultValue": "rhs_mag_3bm46"
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_ammoslot_1 [Indent level: 2],
        "rhs_ammoslot_1": {
            "displayName": "Ammo slot #1 count",
            "tooltip": "Define number of rounds stored inside of type #1. Max 28. Leave -1 for default loadout",
            "property": "rhs_ammoslot_1",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',28] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultValue": "-1",
            "validate": "NUMBER",
            "typeName": "NUMBER"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_ammoslot_2_type [Indent level: 2],
        "rhs_ammoslot_2_type": {
            "displayName": "Ammo slot #2 type",
            "tooltip": "Define type of shell for #2 slot [HEAT rounds]",
            "property": "rhs_ammoslot_2_type",
            # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_2_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_2_type\values\rhs_mag_3bk21_8 [Indent level: 4]
                "rhs_mag_3bk21_8": {
                    "name": "HEAT-FS 3BK21",
                    "value": "rhs_mag_3bk21",
                    "defaultValue": "rhs_mag_3bk21"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_2_type\values\rhs_mag_3bk12_8 [Indent level: 4],
                "rhs_mag_3bk12_8": {
                    "name": "HEAT-FS 3BK12",
                    "value": "rhs_mag_3bk12",
                    "defaultValue": "rhs_mag_3bk12"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_2_type\values\rhs_mag_3bk14_8 [Indent level: 4],
                "rhs_mag_3bk14_8": {
                    "name": "HEAT-FS 3BK14",
                    "value": "rhs_mag_3bk14",
                    "defaultValue": "rhs_mag_3bk14"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_2_type\values\rhs_mag_3bk18_8 [Indent level: 4],
                "rhs_mag_3bk18_8": {
                    "name": "HEAT-FS 3BK18",
                    "value": "rhs_mag_3bk18",
                    "defaultValue": "rhs_mag_3bk18"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_2_type\values\rhs_mag_3bk18m_8 [Indent level: 4],
                "rhs_mag_3bk18m_8": {
                    "name": "HEAT-FS 3BK18M",
                    "value": "rhs_mag_3bk18m",
                    "defaultValue": "rhs_mag_3bk18m"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_2_type\values\rhs_mag_3bk29_8 [Indent level: 4],
                "rhs_mag_3bk29_8": {
                    "name": "HEAT-FS 3BK29",
                    "value": "rhs_mag_3bk29",
                    "defaultValue": "rhs_mag_3bk29"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_2_type\values\rhs_mag_3bk31_8 [Indent level: 4],
                "rhs_mag_3bk31_8": {
                    "name": "HEAT-FS 3BK31",
                    "value": "rhs_mag_3bk31",
                    "defaultValue": "rhs_mag_3bk31"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": 0,
            "typeName": "STRING"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_ammoslot_2 [Indent level: 2],
        "rhs_ammoslot_2": {
            "displayName": "Ammo slot #2 count",
            "tooltip": "Define number of rounds stored inside of type #2. Max 28. Leave -1 for default loadout",
            "property": "rhs_ammoslot_2",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',28] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultValue": "-1",
            "validate": "NUMBER",
            "typeName": "NUMBER"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_ammoslot_3_type [Indent level: 2],
        "rhs_ammoslot_3_type": {
            "displayName": "Ammo slot #3 type",
            "tooltip": "Define type of shell for #3 slot [HE rounds]",
            "property": "rhs_ammoslot_3_type",
            # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_3_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_3_type\values\rhs_mag_3of26_6 [Indent level: 4]
                "rhs_mag_3of26_6": {
                    "name": "HE-FRAG-FS 3OF26",
                    "value": "rhs_mag_3of26",
                    "defaultValue": "rhs_mag_3of26"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_3_type\values\rhs_mag_3of11_6 [Indent level: 4],
                "rhs_mag_3of11_6": {
                    "name": "HE-FRAG-FS 3OF11",
                    "value": "rhs_mag_3of11",
                    "defaultValue": "rhs_mag_3of11"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": 0,
            "typeName": "STRING"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_ammoslot_3 [Indent level: 2],
        "rhs_ammoslot_3": {
            "displayName": "Ammo slot #3 count",
            "tooltip": "Define number of rounds stored inside of type #3. Max 28. Leave -1 for default loadout",
            "property": "rhs_ammoslot_3",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',28] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultValue": "-1",
            "validate": "NUMBER",
            "typeName": "NUMBER"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\sideskirt_unhide [Indent level: 2],
        "sideskirt_unhide": {
            "displayName": "Hide side skirt",
            "property": "sideskirt_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\fbskirt_unhide [Indent level: 2],
        "fbskirt_unhide": {
            "displayName": "Hide front bottom rubber skirt",
            "property": "fbskirt_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\ftskirt_unhide [Indent level: 2],
        "ftskirt_unhide": {
            "displayName": "Hide front top rubber skirt",
            "property": "ftskirt_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\log_unhide [Indent level: 2],
        "log_unhide": {
            "displayName": "Hide back log",
            "property": "log_unhide",
            "control": "CheckboxNumber",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\kshield_unhide [Indent level: 2],
        "kshield_unhide": {
            "displayName": "Hide commander shield",
            "expression": "[_this,_value,'%s'] call rhs_fnc_setHabarEden",
            "property": "kshield_unhide",
            "control": "CheckboxNumber",
            "defaultValue": "-1"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_disableHabar [Indent level: 2],
        "rhs_disableHabar": {
            "displayName": "Disable randomized habar",
            "property": "rhs_disableHabar",
            "expression": "[_this,_value,'%s',_value] call rhs_fnc_setHabarEden",
            "defaultValue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_snorkel [Indent level: 2],
        "rhs_snorkel": {
            "displayName": "Mount snorkel",
            "property": "rhs_snorkel",
            "expression": "_this  animate ['snorkel_unhide',_value];_this  animate ['snorkel_unhide2',_value];_this animate ['snorkel_hide',1-_value];",
            "defaultValue": "0",
            "control": "CheckboxNumber"
        },
        # Class: CfgVehicles\rhs_t80bvk\Attributes\rhs_searchlight [Indent level: 2],
        "rhs_searchlight": {
            "displayName": "Close gunner searchlight",
            "property": "rhs_searchlight",
            "control": "Checkbox",
            "expression": "[_this,_value] call rhs_fnc_t80_searchlightTexture ",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhs_t80bv\Attributes\rhs_ammoslot_4_type [Indent level: 2],
        "rhs_ammoslot_4_type": {
            "displayName": "Ammo slot #4 type",
            "tooltip": "Define type of shell for #4 slot [ATGM rounds]",
            "property": "rhs_ammoslot4_type",
            # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_4_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_4_type\values\rhs_mag_9m112m_6 [Indent level: 4]
                "rhs_mag_9m112m_6": {
                    "name": "ATGM 9M112M",
                    "value": "rhs_mag_9m112m",
                    "defaultValue": "rhs_mag_9m112m"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_4_type\values\rhs_mag_9m112_6 [Indent level: 4],
                "rhs_mag_9m112_6": {
                    "name": "ATGM 9M112",
                    "value": "rhs_mag_9m112",
                    "defaultValue": "rhs_mag_9m112"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_4_type\values\rhs_mag_9m112m2_6 [Indent level: 4],
                "rhs_mag_9m112m2_6": {
                    "name": "ATGM 9M112M2",
                    "value": "rhs_mag_9m112m2",
                    "defaultValue": "rhs_mag_9m112m2"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_4_type\values\rhs_mag_9m124_6 [Indent level: 4],
                "rhs_mag_9m124_6": {
                    "name": "ATGM 9M124",
                    "value": "rhs_mag_9m124",
                    "defaultValue": "rhs_mag_9m124"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_ammoslot_4_type\values\rhs_mag_9m128_6 [Indent level: 4],
                "rhs_mag_9m128_6": {
                    "name": "ATGM 9M128",
                    "value": "rhs_mag_9m128",
                    "defaultValue": "rhs_mag_9m128"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": 0,
            "typeName": "STRING"
        },
        # Class: CfgVehicles\rhs_t80bv\Attributes\rhs_ammoslot_4 [Indent level: 2],
        "rhs_ammoslot_4": {
            "displayName": "Ammo slot #4 count",
            "tooltip": "Define number of rounds stored inside of type #4. Max 28. Leave -1 for default loadout",
            "property": "rhs_ammoslot_4",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',28] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultValue": "-1",
            "validate": "NUMBER",
            "typeName": "NUMBER"
        },
        # Class: CfgVehicles\rhs_t80b\Attributes\rhs_decalPlatoon_type [Indent level: 2],
        "rhs_decalPlatoon_type": {
            "displayName": "Define platoon symbol type",
            "tooltip": "Decal type",
            "property": "rhs_decalPlatoon_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalPlatoon_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalPlatoon_type\values\Platoon [Indent level: 4]
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalPlatoon_type\values\PlatoonGDR [Indent level: 4],
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalPlatoon_type\values\PlatoonVDV [Indent level: 4],
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalPlatoon_type\values\Army [Indent level: 4],
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "1"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalPlatoon_type\values\Honor [Indent level: 4],
                "Honor": {
                    "name": "Honor",
                    "value": "Honor",
                    "defaultValue": "0"
                },
                # Class: CfgVehicles\rhs_tank_base\Attributes\rhs_decalPlatoon_type\values\HonorGDR [Indent level: 4],
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            }
        },
        # Class: CfgVehicles\rhs_t80b\Attributes\rhs_decalPlatoon [Indent level: 2],
        "rhs_decalPlatoon": {
            "displayName": "Set platoon symbol",
            "tooltip": "Set platoon symbol located on turret front. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHST80PlnSymPlaces,  _this getVariable ['rhs_decalPlatoon_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        }
    },
    # Class: CfgVehicles\rhs_t80bvk\Library [Indent level: 1],
    "Library": {
        "libTextDesc": "T-80BVK. Commander variant of the T-80BV, similar to T-80BK, but with hanging dynamic armor."
    },
    "model": "rhsafrf|addons|rhs_t80|T80BV.p3d",
    "armor": 550,
    # Class: CfgVehicles\rhs_t80bv\HitPoints [Indent level: 1],
    "HitPoints": {
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_1_hitpoint [Indent level: 2]
        "era_1_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e1",
            "armorComponent": "e1",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_1_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_1_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_1_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_1_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_1_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_2_hitpoint [Indent level: 2],
        "era_2_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e2",
            "armorComponent": "e2",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_2_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_2_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_2_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_2_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_2_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_3_hitpoint [Indent level: 2],
        "era_3_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e3",
            "armorComponent": "e3",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_3_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_3_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_3_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_3_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_3_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_4_hitpoint [Indent level: 2],
        "era_4_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e4",
            "armorComponent": "e4",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_4_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_4_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_4_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_4_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_4_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_5_hitpoint [Indent level: 2],
        "era_5_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e5",
            "armorComponent": "e5",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_5_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_5_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_5_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e5",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_5_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_5_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e5",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_6_hitpoint [Indent level: 2],
        "era_6_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e6",
            "armorComponent": "e6",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_6_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_6_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_6_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e6",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_6_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_6_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e6",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_7_hitpoint [Indent level: 2],
        "era_7_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e7",
            "armorComponent": "e7",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_7_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_7_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_7_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_7_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_7_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_8_hitpoint [Indent level: 2],
        "era_8_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e8",
            "armorComponent": "e8",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_8_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_8_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e8",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_8_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e8",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_8_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e8",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_8_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e8",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_9_hitpoint [Indent level: 2],
        "era_9_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e9",
            "armorComponent": "e9",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_9_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_9_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e9",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_9_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e9",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_9_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e9",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_9_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e9",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_10_hitpoint [Indent level: 2],
        "era_10_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e10",
            "armorComponent": "e10",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_10_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_10_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e10",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_10_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e10",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_10_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e10",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_10_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e10",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_11_hitpoint [Indent level: 2],
        "era_11_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e11",
            "armorComponent": "e11",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_11_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_11_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e11",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_11_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e11",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_11_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e11",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_11_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e11",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_12_hitpoint [Indent level: 2],
        "era_12_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e12",
            "armorComponent": "e12",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_12_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_12_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e12",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_12_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e12",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_12_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e12",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_12_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e12",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_13_hitpoint [Indent level: 2],
        "era_13_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e13",
            "armorComponent": "e13",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_13_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_13_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e13",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_13_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e13",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_13_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e13",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_13_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e13",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_14_hitpoint [Indent level: 2],
        "era_14_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e14",
            "armorComponent": "e14",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_14_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_14_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e14",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_14_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e14",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_14_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e14",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_14_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e14",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_15_hitpoint [Indent level: 2],
        "era_15_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e15",
            "armorComponent": "e15",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_15_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_15_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e15",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_15_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e15",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_15_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e15",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_15_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e15",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_16_hitpoint [Indent level: 2],
        "era_16_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e16",
            "armorComponent": "e16",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_16_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_16_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e16",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_16_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e16",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_16_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e16",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_16_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e16",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_17_hitpoint [Indent level: 2],
        "era_17_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e17",
            "armorComponent": "e17",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_17_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_17_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e17",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_17_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e17",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_17_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e17",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_17_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e17",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_18_hitpoint [Indent level: 2],
        "era_18_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e18",
            "armorComponent": "e18",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_18_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_18_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e18",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_18_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e18",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_18_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e18",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_18_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e18",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_19_hitpoint [Indent level: 2],
        "era_19_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e19",
            "armorComponent": "e19",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_19_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_19_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e19",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_19_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e19",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_19_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e19",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_19_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e19",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_20_hitpoint [Indent level: 2],
        "era_20_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e20",
            "armorComponent": "e20",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_20_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_20_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e20",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_20_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e20",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_20_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e20",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_20_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e20",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_21_hitpoint [Indent level: 2],
        "era_21_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e21",
            "armorComponent": "e21",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_21_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_21_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e21",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_21_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e21",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_21_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e21",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_21_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e21",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_22_hitpoint [Indent level: 2],
        "era_22_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e22",
            "armorComponent": "e22",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_22_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_22_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e22",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_22_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e22",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_22_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e22",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_22_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e22",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_23_hitpoint [Indent level: 2],
        "era_23_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e23",
            "armorComponent": "e23",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_23_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_23_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e23",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_23_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e23",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_23_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e23",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_23_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e23",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_24_hitpoint [Indent level: 2],
        "era_24_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e24",
            "armorComponent": "e24",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_24_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_24_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e24",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_24_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e24",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_24_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e24",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_24_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e24",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_25_hitpoint [Indent level: 2],
        "era_25_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e25",
            "armorComponent": "e25",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_25_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_25_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e25",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_25_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e25",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_25_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e25",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_25_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e25",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_26_hitpoint [Indent level: 2],
        "era_26_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e26",
            "armorComponent": "e26",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_26_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_26_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e26",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_26_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e26",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_26_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e26",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_26_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e26",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_27_hitpoint [Indent level: 2],
        "era_27_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e27",
            "armorComponent": "e27",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_27_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_27_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e27",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_27_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e27",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_27_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e27",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_27_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e27",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_t80bv\HitPoints\era_28_hitpoint [Indent level: 2],
        "era_28_hitpoint": {
            "simulation": "RHS_ERA_K1",
            "armor": -80,
            "material": -1,
            "name": "e28",
            "armorComponent": "e28",
            "passThrough": 0,
            "minimalHit": -0.5,
            "explosionShielding": 0.01,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\rhs_t80bv\HitPoints\era_28_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_28_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e28",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_28_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e28",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_28_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e28",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\rhs_t80bv\HitPoints\era_28_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e28",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\rhs_tank_base\HitPoints\Armor_Composite_65 [Indent level: 2],
        "Armor_Composite_65": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_65_Hit",
            "armorComponent": "Armor_CE_65",
            "simulation": "RHS_Composite_65",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhs_tank_base\HitPoints\Armor_Composite_70 [Indent level: 2],
        "Armor_Composite_70": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_70_Hit",
            "armorComponent": "Armor_CE_70",
            "simulation": "RHS_Composite_70",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhs_tank_base\HitPoints\Armor_Composite_75 [Indent level: 2],
        "Armor_Composite_75": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_75_Hit",
            "armorComponent": "Armor_CE_75",
            "simulation": "RHS_Composite_75",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhs_tank_base\HitPoints\Armor_Composite_80 [Indent level: 2],
        "Armor_Composite_80": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_80_Hit",
            "armorComponent": "Armor_CE_80",
            "simulation": "RHS_Composite_80",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhs_tank_base\HitPoints\Armor_Composite_85 [Indent level: 2],
        "Armor_Composite_85": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_85_Hit",
            "armorComponent": "Armor_CE_85",
            "simulation": "RHS_Composite_85",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhs_tank_base\HitPoints\Armor_Composite_95 [Indent level: 2],
        "Armor_Composite_95": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_95_Hit",
            "armorComponent": "Armor_CE_95",
            "simulation": "RHS_Composite_95",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhs_tank_base\HitPoints\HitHull [Indent level: 2],
        "HitHull": {
            "armor": -100,
            "material": -1,
            "name": "telo",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.1,
            "explosionShielding": 0.01,
            "radius": 0.13
        },
        # Class: CfgVehicles\rhs_tank_base\HitPoints\HitEngine [Indent level: 2],
        "HitEngine": {
            "armor": -150,
            "material": -1,
            "name": "motor",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.14,
            "explosionShielding": 0.01,
            "radius": 0.23,
            # Class: CfgVehicles\rhs_tank_base\HitPoints\HitEngine\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke [Indent level: 4],
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Fire [Indent level: 4],
                "RHS_Engine_Fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sparks [Indent level: 4],
                "RHS_Engine_Sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds [Indent level: 4],
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1 [Indent level: 4],
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2 [Indent level: 4],
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                }
            }
        },
        # Class: CfgVehicles\rhs_tank_base\HitPoints\HitLTrack [Indent level: 2],
        "HitLTrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_L",
            "passThrough": 0,
            "minimalHit": -0.25,
            "explosionShielding": 0.5,
            "radius": 0.3,
            "visual": "pas_L"
        },
        # Class: CfgVehicles\rhs_tank_base\HitPoints\HitRTrack [Indent level: 2],
        "HitRTrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_P",
            "passThrough": 0,
            "minimalHit": -0.25,
            "explosionShielding": 0.5,
            "radius": 0.3,
            "visual": "pas_P"
        },
        # Class: CfgVehicles\Tank_F\HitPoints\HitFuel [Indent level: 2],
        "HitFuel": {
            "armor": 0.6,
            "material": -1,
            "name": "NEtelo",
            "visual": "motor",
            "passThrough": 0,
            "minimalHit": 0.1,
            "explosionShielding": 0.3
        }
    },
    # Class: CfgVehicles\rhs_t80bv\textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles\rhs_t80bv\textureSources\RHS_CDF [Indent level: 2]
        "RHS_CDF": {
            "displayName": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_t80_hull_cdf_co.paa","rhsgref|addons|rhsgref_vehicles_ret|data|cdf|rhs_t80_turret_cdf_co.paa"]
        }
    },
    "scope": 2,
    "faction": "rhs_faction_tv",
    "crew": "rhs_msv_crew",
    "typicalCargo": ["rhs_msv_crew","rhs_msv_crew","rhs_msv_crew"],
    "ace_refuel_fuelCapacity": 1100,
    "dlc": "RHS_AFRF",
    "rhs_hasSnorkel": 1,
    "rhs_habarType": 2,
    "rhs_decalParameters": ["['Number',cRHST80NumberPlaces,'Default']","['Label',cRHST80PlnSymPlaces, 'Platoon',8]"],
    "allowTabLock": 0,
    "destrType": "DestructDefault",
    "htMin": 60,
    "htMax": 1800,
    "afMax": 200,
    "mfMax": 100,
    "side": 0,
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "simulation": "tankX",
    "normalSpeedForwardCoef": 0.75,
    "slowSpeedForwardCoef": 0.25,
    "fuelCapacity": 19.5,
    "RHS_fuelCapacity": 1540,
    "brakeIdleSpeed": 1.78,
    "maxSpeed": 65,
    "engineMOI": 20,
    "enginePower": 809,
    "peakTorque": 4393,
    "minOmega": 114.72,
    "maxOmega": 350.86,
    "idleRPM": 1200,
    "redRPM": 3255,
    "torqueCurve": [[0.30722,0],[0.447619,0.948555],[0.526574,0.897109],[0.60553,0.845664],[0.684485,0.794218],[0.763441,0.742773],[0.842396,0.691327],[1.90292,0]],
    "thrustDelay": 0.3,
    "dampingRateFullThrottle": 0.3,
    "dampingRateZeroThrottleClutchEngaged": 3,
    "dampingRateZeroThrottleClutchDisengaged": 0.25,
    "antiRollbarForceCoef": 24,
    "antiRollbarForceLimit": 42,
    "antiRollbarSpeedMin": 30,
    "antiRollbarSpeedMax": 75,
    "engineBrakeCoef": 0,
    "tracksSpeed": 1.4,
    "tankTurnForce": 850000,
    "tankTurnForceAngMinSpd": 0.7,
    "tankTurnForceAngSpd": 0.72,
    "accelAidForceCoef": 3.3,
    "accelAidForceYOffset": -4,
    "accelAidForceSpd": 2.53,
    "maxFordingDepth": 0,
    "waterResistance": 0,
    "waterDamageEngine": 0.2,
    "waterLeakiness": 10,
    "engineLosses": 25,
    "transmissionLosses": 15,
    "clutchStrength": 30,
    "latency": 1.3,
    "switchTime": 0,
    "changeGearType": "rpmratio",
    "changeGearOmegaRatios": [1,0.333333,0.333333,0,0.96,0.333333,0.983333,0.7,0.983333,0.733333,0.983333,0.733333],
    # Class: CfgVehicles\rhs_tank_base\complexGearbox [Indent level: 1],
    "complexGearbox": {
        "GearboxRatios": ["R1",-9.36,"N",0,"D1",4.38,"D2",2.16,"D3",1.46,"D4",1],
        "TransmissionRatios": ["High",12.85],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R",
        "transmissionDelay": 0.9
    },
    # Class: CfgVehicles\rhs_tank_base\Wheels [Indent level: 1],
    "Wheels": {
        # Class: CfgVehicles\rhs_tank_base\Wheels\L2 [Indent level: 2]
        "L2": {
            "suspTravelDirection": [-0.125,-1,0],
            "boneName": "RHS_T80B_SUSL_1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\L3 [Indent level: 2],
        "L3": {
            "boneName": "RHS_T80B_SUSL_3",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\L4 [Indent level: 2],
        "L4": {
            "boneName": "RHS_T80B_SUSL_5",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\L5 [Indent level: 2],
        "L5": {
            "boneName": "RHS_T80B_SUSL_7",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\L6 [Indent level: 2],
        "L6": {
            "boneName": "RHS_T80B_SUSL_9",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\L7 [Indent level: 2],
        "L7": {
            "boneName": "RHS_T80B_SUSL_11",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\L9 [Indent level: 2],
        "L9": {
            "boneName": "",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\L1 [Indent level: 2],
        "L1": {
            "boneName": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\R2 [Indent level: 2],
        "R2": {
            "suspTravelDirection": [0.125,-1,0],
            "boneName": "RHS_T80B_SUSR_1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\R3 [Indent level: 2],
        "R3": {
            "boneName": "RHS_T80B_SUSR_3",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\R4 [Indent level: 2],
        "R4": {
            "boneName": "RHS_T80B_SUSR_5",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\R5 [Indent level: 2],
        "R5": {
            "boneName": "RHS_T80B_SUSR_7",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\R6 [Indent level: 2],
        "R6": {
            "boneName": "RHS_T80B_SUSR_9",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\R7 [Indent level: 2],
        "R7": {
            "boneName": "RHS_T80B_SUSR_11",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "maxDroop": 0.14,
            "maxCompression": 0.14,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\R9 [Indent level: 2],
        "R9": {
            "boneName": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        },
        # Class: CfgVehicles\rhs_tank_base\Wheels\R1 [Indent level: 2],
        "R1": {
            "boneName": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.36,
            "mass": 188,
            "MOI": 14.0783,
            "maxBrakeTorque": 10000,
            "sprungMass": 3416.67,
            "springStrength": 354000,
            "springDamperRate": 11000,
            "dampingRate": 1382,
            "dampingRateInAir": 1382,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 72000,
            "frictionVsSlipGraph": [[0,0.4],[0.18,1],[0.7,0.75]]
        }
    },
    "soundEngineOnExt": ["rhsafrf|addons|rhs_vehiclesounds|sounds|armor|t80|t80_engine_ext_start",1.77828,1,100],
    "soundEngineOnInt": ["rhsafrf|addons|rhs_vehiclesounds|sounds|armor|t80|t80_engine_ext_start",1.77828,1],
    # Class: CfgVehicles\rhs_tank_base\Sounds [Indent level: 1],
    "Sounds": {
        # Class: CfgVehicles\rhs_tank_base\Sounds\Idle_ext [Indent level: 2]
        "Idle_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",0.794328,1,200],
            "frequency": "0.95	+	((rpm/	2640) factor[(400*1.57/	2640),(900*1.57/	2640)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(100*1.57/	2640),(200*1.57/	2640)])	*	((rpm/	2640) factor[(900*1.57/	2640),(700*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine [Indent level: 2],
        "Engine": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",0.891251,1,240],
            "frequency": "0.8	+	((rpm/	2640) factor[(700*1.57/	2640),(1100*1.57/	2640)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(705*1.57/	2640),(850*1.57/	2640)])	*	((rpm/	2640) factor[(1100 *1.57/	2640),(950*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine1_ext [Indent level: 2],
        "Engine1_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",1.12202,1,280],
            "frequency": "0.8	+	((rpm/	2640) factor[(950*1.57/	2640),(1400*1.57/	2640)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(900*1.57/	2640),(1050*1.57/	2640)])	*	((rpm/	2640) factor[(1400*1.57/	2640),(1200*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine2_ext [Indent level: 2],
        "Engine2_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",1.25893,1,320],
            "frequency": "0.8	+	((rpm/	2640) factor[(1200*1.57/	2640),(1700*1.57/	2640)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(1170*1.57/	2640),(1380*1.57/	2640)])	*	((rpm/	2640) factor[(1700*1.57/	2640),(1500*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine3_ext [Indent level: 2],
        "Engine3_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",1.41254,1,360],
            "frequency": "0.8	+	((rpm/	2640) factor[(1500*1.57/	2640),(2100*1.57/	2640)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(1500*1.57/	2640),(1670*1.57/	2640)])	*	((rpm/	2640) factor[(2100*1.57/	2640),(1800*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine4_ext [Indent level: 2],
        "Engine4_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",1.58489,1,400],
            "frequency": "0.8	+	((rpm/	2640) factor[(1800*1.57/	2640),(2300*1.57/	2640)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2640) factor[(1780*1.57/	2640),(2060*1.57/	2640)])	*	((rpm/	2640) factor[(2450*1.57/	2640),(2200*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine5_ext [Indent level: 2],
        "Engine5_ext": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|t80turbine",1.77828,1,440],
            "frequency": "0.8	+	((rpm/	2640) factor[(2100*1.57/	2640),(2640*1.57/	2640)])*0.1",
            "volume": "engineOn*camPos*((rpm/	2640) factor[(2150*1.57/	2640),(2500*1.57/	2640)])"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Idle_int [Indent level: 2],
        "Idle_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm1",0.501187,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(400*1.57/	2640),(900*1.57/	2640)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(100*1.57/	2640),(200*1.57/	2640)])	*	((rpm/	2640) factor[(900*1.57/	2640),(700*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine_int [Indent level: 2],
        "Engine_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm2",0.354813,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(700*1.57/	2640),(1100*1.57/	2640)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(705*1.57/	2640),(850*1.57/	2640)])	*	((rpm/	2640) factor[(1100 *1.57/	2640),(950*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine1_int [Indent level: 2],
        "Engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm3",0.398107,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(950*1.57/	2640),(1400*1.57/	2640)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(900*1.57/	2640),(1050*1.57/	2640)])	*	((rpm/	2640) factor[(1400*1.57/	2640),(1200*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine2_int [Indent level: 2],
        "Engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm4",0.446684,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(1200*1.57/	2640),(1700*1.57/	2640)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(1170*1.57/	2640),(1380*1.57/	2640)])	*	((rpm/	2640) factor[(1700*1.57/	2640),(1500*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine3_int [Indent level: 2],
        "Engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm5",0.501187,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(1500*1.57/	2640),(2100*1.57/	2640)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(1500*1.57/	2640),(1670*1.57/	2640)])	*	((rpm/	2640) factor[(2100*1.57/	2640),(1800*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine4_int [Indent level: 2],
        "Engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm6",0.562341,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(1800*1.57/	2640),(2300*1.57/	2640)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	2640) factor[(1780*1.57/	2640),(2060*1.57/	2640)])	*	((rpm/	2640) factor[(2450*1.57/	2640),(2200*1.57/	2640)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\Engine5_int [Indent level: 2],
        "Engine5_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_01|MBT1_engine_int_rpm7",0.630957,1],
            "frequency": "0.8	+	((rpm/	2640) factor[(2100*1.57/	2640),(2640*1.57/	2640)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	2640) factor[(2150*1.57/	2640),(2500*1.57/	2640)])"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\NoiseInt [Indent level: 2],
        "NoiseInt": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_int_1",0.501187,1],
            "frequency": "1",
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\NoiseExt [Indent level: 2],
        "NoiseExt": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_ext_1",0.891251,1,50],
            "frequency": "1",
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsOutH0 [Indent level: 2],
        "ThreadsOutH0": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|T80-Treads",0.398107,1,140],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsOutH1 [Indent level: 2],
        "ThreadsOutH1": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|T80-Treads",0.446684,1,160],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsOutH2 [Indent level: 2],
        "ThreadsOutH2": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|T80-Treads",0.501187,1,180],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsOutH3 [Indent level: 2],
        "ThreadsOutH3": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|T80-Treads",0.562341,1,200],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsOutH4 [Indent level: 2],
        "ThreadsOutH4": {
            "sound": ["rhsafrf|addons|rhs_t80|Sound|T80-Treads",0.562341,1,220],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsOutS0 [Indent level: 2],
        "ThreadsOutS0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_ext_treads_soft_01",0.316228,1,120],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsOutS1 [Indent level: 2],
        "ThreadsOutS1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_ext_treads_soft_02",0.354813,1,140],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsOutS2 [Indent level: 2],
        "ThreadsOutS2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_ext_treads_soft_03",0.398107,1,160],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsOutS3 [Indent level: 2],
        "ThreadsOutS3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_ext_treads_soft_04",0.446684,1,180],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsOutS4 [Indent level: 2],
        "ThreadsOutS4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_ext_treads_soft_05",0.501187,1,200],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsInH0 [Indent level: 2],
        "ThreadsInH0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_hard_01",0.251189,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsInH1 [Indent level: 2],
        "ThreadsInH1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_hard_02",0.281838,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsInH2 [Indent level: 2],
        "ThreadsInH2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_hard_03",0.316228,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsInH3 [Indent level: 2],
        "ThreadsInH3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_hard_04",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsInH4 [Indent level: 2],
        "ThreadsInH4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_hard_05",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsInS0 [Indent level: 2],
        "ThreadsInS0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_soft_01",0.316228,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-0) max 0)*1.57/	60),(((-5) max 5)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-15) max 15)*1.57/	60),(((-10) max 10)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsInS1 [Indent level: 2],
        "ThreadsInS1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_soft_02",0.316228,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-10) max 10)*1.57/	60),(((-15) max 15)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-30) max 30)*1.57/	60),(((-25) max 25)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsInS2 [Indent level: 2],
        "ThreadsInS2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_soft_03",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-25) max 25)*1.57/	60),(((-30) max 30)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-45) max 45)*1.57/	60),(((-40) max 40)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsInS3 [Indent level: 2],
        "ThreadsInS3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_soft_04",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-40) max 40)*1.57/	60),(((-45) max 45)*1.57/	60)])	*	((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-55) max 55)*1.57/	60),(((-50) max 50)*1.57/	60)]))"
        },
        # Class: CfgVehicles\rhs_tank_base\Sounds\ThreadsInS4 [Indent level: 2],
        "ThreadsInS4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|v2_int_treads_soft_05",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)*1.57/	60) factor[(((-49) max 49)*1.57/	60),(((-53) max 53)*1.57/	60)])"
        },
        "soundSetsInt": ["RHS_T80_Engine_RPM0_INT_SoundSet","RHS_T80_Engine_RPM1_INT_SoundSet","RHS_T80_Engine_RPM2_INT_SoundSet","RHS_T80_Engine_INT_Burst_SoundSet","RHS_T80_Tracks_01_INT_SoundSet","RHS_T80_Tracks_02_INT_SoundSet","RHS_T80_Tracks_03_INT_SoundSet","RHS_T80_Tracks_04_INT_SoundSet","RHS_T80_Tracks_05_INT_SoundSet","RHS_T80_Tracks_06_INT_SoundSet","T80_Interior_Tone_Engine_Off_SoundSet","T80_Interior_Tone_Engine_On_SoundSet","T80_Rattling_INT_SoundSet","T80_Rain_INT_SoundSet","RHS_T80_Tracks_Brake_Hard_INT_SoundSet","RHS_T80_Tracks_Brake_Soft_INT_SoundSet","RHS_T80_Tracks_Turn_Hard_INT_SoundSet","RHS_T80_Tracks_Turn_Soft_INT_SoundSet","RHS_T80_Drive_Water_INT_SoundSet","RHS_T80_Drive_Dirt_INT_SoundSet","","MBT_02_Turbine01_Int_Tonal_SoundSet","MBT_02_Turbine01_Int_Noisy_SoundSet","MBT_02_Servo01_Int_SoundSet","Tracks_Movement_Dirt_Int_01_SoundSet","Tracks_Surface_Soft_Int_SoundSet","Tracks_Surface_Sand_Int_SoundSet","Tracks_Surface_Squeaks_Soft_Int_SoundSet","Tracks_Surface_Squeaks_Hard_Int_SoundSet","Tanks_Material_Strain_Int_SoundSet","Tank_General_Collision_Int_SoundSet","rhs_tank_t72_int_autoloader_SoundSet"],
        "soundSetsExt": ["RHS_T80_Engine_RPM0_EXT_SoundSet","RHS_T80_Engine_RPM1_EXT_SoundSet","RHS_T80_Engine_RPM2_EXT_SoundSet","RHS_T80_Engine_EXT_Burst_SoundSet","RHS_T80_Tracks_01_EXT_SoundSet","RHS_T80_Tracks_02_EXT_SoundSet","RHS_T80_Tracks_03_EXT_SoundSet","RHS_T80_Tracks_04_EXT_SoundSet","RHS_T80_Tracks_05_EXT_SoundSet","RHS_T80_Tracks_06_EXT_SoundSet","T80_Rain_EXT_SoundSet","RHS_T80_Tracks_Brake_Hard_EXT_SoundSet","RHS_T80_Tracks_Brake_Soft_EXT_SoundSet","RHS_T80_Tracks_Turn_Hard_EXT_SoundSet","RHS_T80_Tracks_Turn_Soft_EXT_SoundSet","RHS_T80_Drive_Water_EXT_SoundSet","RHS_T80_Drive_Dirt_EXT_SoundSet","","MBT_02_Turbine01_Ext_Front_Tonal_SoundSet","MBT_02_Turbine01_Ext_Rear_Tonal_SoundSet","MBT_02_Turbine01_Ext_Front_Noisy_SoundSet","MBT_02_Turbine01_Ext_Rear_Noisy_SoundSet","MBT_02_Servo01_Ext_SoundSet","MBT_02_Servo02_Ext_SoundSet","Tracks_Movement_Dirt_Ext_01_SoundSet","Tracks_Surface_Soft_Ext_SoundSet","Tracks_Surface_Sand_Ext_SoundSet","Tracks_Surface_Squeaks_Soft_Ext_SoundSet","Tracks_Surface_Squeaks_Hard_Ext_SoundSet","Tank_General_Collision_SoundShader","rhs_tank_t72_ext_autoloader_SoundSet"]
    },
    "picture": "rhsafrf|addons|rhs_t80|data|icon|rhs_t80_pic_ca.paa",
    "Icon": "rhsafrf|addons|rhs_t72|data|icomap_t72_CA.paa",
    "mapSize": 9.5,
    "vehicleClass": "rhs_vehclass_tank",
    "editorSubcategory": "rhs_EdSubcat_tank",
    "accuracy": 0.2,
    "cost": 1.5e+006,
    "unitInfoType": "RHS_RscInfoT80",
    "tf_range_api": 45000,
    "enableGPS": 0,
    "incomingMissileDetectionSystem": 0,
    "driverCanSee": "2+4+8",
    "gunnerCanSee": "2+4+8",
    "commanderCanSee": "2+4+8",
    "viewCargoShadow": 1,
    "viewCargoShadowDiff": 1,
    "viewCargoShadowAmb": 1,
    "viewDriverShadow": 1,
    "viewDriverInExternal": 1,
    "forceHideDriver": 0,
    "driverForceOptics": 1,
    "driverOutForceOptics": 1,
    "getInAction": "GetInLow",
    "getOutAction": "GetOutLow",
    "driverAction": "driver_apcwheeled2_out",
    "driverInAction": "rhs_t72_driver",
    "driverDoor": "hatchD",
    "memoryPointDriverOutOptics": "Driver_out_view",
    "driverOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
    "LODDriverTurnedIn": 0,
    "LODDriverTurnedOut": 0,
    "LODDriverOpticsIn": 0,
    "extCameraPosition": [0,2.25,-10],
    # Class: CfgVehicles\rhs_tank_base\DriverOpticsIn [Indent level: 1],
    "DriverOpticsIn": {
        # Class: CfgVehicles\rhs_tank_base\DriverOpticsIn\OpticView [Indent level: 2]
        "OpticView": {
            "OpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5",
            "hitpoint": "Hit_Optic_Driver",
            "initFov": 0.7,
            "minFov": 0.7,
            "maxFov": 0.7,
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
        }
    },
    "hiddenSelections": ["camo1","camo2","","Search_random","n1","n2","n3","i1","i2","i3"],
    "textureList": [],
    "rhs_randomizedHabar": ["log_unhide","sideskirt_unhide","fbskirt_unhide","ftskirt_unhide"],
    "wheelCircumference": 2.312,
    "damageResistance": 0.02,
    "type": 1,
    "threat": [0.9,0.8,0.2],
    "driveOnComponent": ["Slide"],
    "armorStructural": 220,
    "explosionShielding": 100,
    "crewExplosionProtection": 1,
    "minTotalDamageThreshold": 0.5,
    "fireResistance": -1,
    "crewVulnerable": 0,
    # Class: CfgVehicles\rhs_tank_base\ViewOptics [Indent level: 1],
    "ViewOptics": {
        "initFov": 0.7,
        "minFov": 0.7,
        "maxFov": 0.7,
        "visionMode": ["Normal","NVG"],
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
    # Class: CfgVehicles\rhs_tank_base\TransportMagazines [Indent level: 1],
    "TransportMagazines": {
        # Class: CfgVehicles\rhs_tank_base\TransportMagazines\_xx_rhs_30Rnd_545x39_7N10_AK [Indent level: 2]
        "_xx_rhs_30Rnd_545x39_7N10_AK": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": 10
        },
        # Class: CfgVehicles\rhs_tank_base\TransportMagazines\_xx_rhs_mag_rgd5 [Indent level: 2],
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 10
        },
        # Class: CfgVehicles\rhs_tank_base\TransportMagazines\_xx_rhs_mag_nspn_red [Indent level: 2],
        "_xx_rhs_mag_nspn_red": {
            "magazine": "rhs_mag_nspn_red",
            "count": 10
        }
    },
    # Class: CfgVehicles\rhs_tank_base\TransportItems [Indent level: 1],
    "TransportItems": {
        # Class: CfgVehicles\rhs_tank_base\TransportItems\_xx_FirstAidKit [Indent level: 2]
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles\rhs_tank_base\TransportItems\_xx_Medikit [Indent level: 2],
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles\rhs_tank_base\TransportItems\_xx_Toolkit [Indent level: 2],
        "_xx_Toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    "insideSoundCoef": 0.9,
    # Class: CfgVehicles\rhs_tank_base\Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles\rhs_tank_base\Reflectors\Driver_FG125_Cover [Indent level: 2]
        "Driver_FG125_Cover": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerAngle": 35,
            "outerAngle": 75,
            "coneFadeCoef": 5,
            "intensity": 15,
            "useFlare": 0,
            "dayLight": 1,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhs_tank_base\Reflectors\Driver_FG125_Cover\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.2,
                "hardLimitStart": 130,
                "hardLimitEnd": 160
            }
        },
        # Class: CfgVehicles\rhs_tank_base\Reflectors\Driver_FG125_Cover_Flare [Indent level: 2],
        "Driver_FG125_Cover_Flare": {
            "intensity": 5,
            "innerAngle": 55,
            "outerAngle": 155,
            "flareSize": 0.3,
            "useFlare": 1,
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "coneFadeCoef": 5,
            "dayLight": 1,
            # Class: CfgVehicles\rhs_tank_base\Reflectors\Driver_FG125_Cover\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.2,
                "hardLimitStart": 130,
                "hardLimitEnd": 160
            }
        }
    },
    "aggregateReflectors": [["Driver_FG125_Cover","Driver_FG125_Cover_Flare"]],
    "armorLights": 0.1,
    # Class: CfgVehicles\rhs_tank_base\Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles\rhs_tank_base\Exhausts\Exhaust1 [Indent level: 2]
        "Exhaust1": {
            "position": "vyfuk start",
            "direction": "vyfuk konec",
            "effect": "RHS_ExhaustEffectTankGasBack"
        },
        # Class: CfgVehicles\rhs_tank_base\Exhausts\Exhaust2 [Indent level: 2],
        "Exhaust2": {
            "position": "vyfuk start 2",
            "direction": "vyfuk konec 2",
            "effect": "RHS_ExhaustEffectTankGasBack"
        }
    },
    "selectionLeftOffset": "pasanimL",
    "selectionRightOffset": "pasanimP",
    # Class: CfgVehicles\rhs_tank_base\EventHandlers [Indent level: 1],
    "EventHandlers": {
        # Class: CfgVehicles\rhs_tank_base\EventHandlers\RHS_EventHandlers [Indent level: 2]
        "RHS_EventHandlers": {
            "init": "_this call RHS_fnc_t80_init;",
            "fired": "_this call RHS_fnc_t80_autoloader;",
            "killed": "[_this select 0,'rhs_Wreck_T80_turret_F'] call rhs_fnc_turretBlow",
            "engine": "[_this select 0,_this select 1,20] call rhs_fnc_engineStartupDelay",
            "getOut": "_this call rhs_fnc_t72_hatch;_this call rhs_fnc_hatchAbandon"
        },
        # Class: CfgVehicles\rhs_tank_base\EventHandlers\RHS_HitSpall [Indent level: 2],
        "RHS_HitSpall": {
            "hitpart": "_this call rhs_fnc_hitSpall"
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
    # Class: CfgVehicles\rhs_tank_base\UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles\rhs_tank_base\UserActions\trunk_open [Indent level: 2]
        "trunk_open": {
            "displayName": "Use NSVT",
            "position": "trunk_action",
            "radius": 2,
            "onlyForplayer": 0,
            "condition": "this animationPhase 'RHS_T80B_Hatch_commander'>0.5 and ((call rhs_fnc_findPlayer) == commander this)",
            "statement": "(call rhs_fnc_findPlayer) action ['moveToTurret', this, [0,1]];[this,[[0,0],true]] remoteExecCall ['lockTurret']"
        },
        # Class: CfgVehicles\rhs_tank_base\UserActions\trunk_close [Indent level: 2],
        "trunk_close": {
            "displayName": "Leave NSVT",
            "condition": "vehicle (call rhs_fnc_findPlayer) turretUnit [0,1] == (call rhs_fnc_findPlayer)",
            "statement": "(call rhs_fnc_findPlayer) action ['moveToTurret', this, [0,0]];[this,[[0,0],false]] remoteExecCall ['lockTurret']",
            "position": "trunk_action",
            "radius": 2,
            "onlyForplayer": 0
        }
    },
    # Class: CfgVehicles\rhs_tank_base\Damage [Indent level: 1],
    "Damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_t80|data|materials|hull_g.rvmat","rhsafrf|addons|rhs_t80|data|materials|hull_g_dam.rvmat","rhsafrf|addons|rhs_t80|data|materials|hull_destroy.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_bk.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_G_dam.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_destroy.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_G.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_G_dam.rvmat","rhsafrf|addons|rhs_t80|data|materials|turret_destroy.rvmat","rhsafrf|addons|rhs_t80|data|materials|track.rvmat","rhsafrf|addons|rhs_t80|data|materials|track.rvmat","rhsafrf|addons|rhs_t80|data|materials|track_destroy.rvmat","rhsafrf|addons|rhs_t80|data|materials|searchlight.rvmat","rhsafrf|addons|rhs_t80|data|materials|searchlight.rvmat","rhsafrf|addons|rhs_t80|data|materials|searchlight_destroy.rvmat"]
    },
    # Class: CfgVehicles\rhs_tank_base\Components [Indent level: 1],
    "Components": {
        # Class: CfgVehicles\rhs_tank_base\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: CfgVehicles\rhs_tank_base\Components\VehicleSystemsDisplayManagerComponentLeft\EmptyDisplay [Indent level: 3]
            "EmptyDisplay": {
                "componentType": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles\rhs_tank_base\Components\VehicleSystemsDisplayManagerComponentLeft\CrewDisplay [Indent level: 3],
            "CrewDisplay": {
                "componentType": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles\rhs_tank_base\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "VehicleSystemsDisplayManagerComponentRight": {
            # Class: CfgVehicles\rhs_tank_base\Components\VehicleSystemsDisplayManagerComponentRight\EmptyDisplay [Indent level: 3]
            "EmptyDisplay": {
                "componentType": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles\rhs_tank_base\Components\VehicleSystemsDisplayManagerComponentRight\CrewDisplay [Indent level: 3],
            "CrewDisplay": {
                "componentType": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles\Tank_F\Components\AITankSteeringComponent [Indent level: 2],
        "AITankSteeringComponent": {
            "steeringPIDWeights": [2.9,0.1,0.2],
            "speedPIDWeights": [0.7,0.2,0],
            "doRemapSpeed": 0,
            "remapSpeedRange": [30,70],
            "remapSpeedScalar": [1,0.35],
            "doPredictForward": 1,
            "predictForwardRange": [1,20],
            "steerAheadSaturation": [0.01,0.4],
            "speedPredictionMethod": 3,
            "wheelAngleCoef": 0.7,
            "forwardAngleCoef": 0.7,
            "steeringAngleCoef": 1,
            "differenceAngleCoef": 1,
            "stuckMaxTime": 3,
            "allowOvertaking": 1,
            "allowCollisionAvoidance": 1,
            "allowDrifting": 0,
            "maxWheelAngleDiff": 0.2616,
            "minSpeedToKeep": 0.01,
            "commandTurnFactor": 2,
            "allowTurnAroundInPoint": 1,
            "convoyPIDWeights": [1,0,0],
            "predictForwardMaxSpeed": 15
        },
        # Class: CfgVehicles\LandVehicle\Components\TransportCountermeasuresComponent [Indent level: 2],
        "TransportCountermeasuresComponent": {
        }
    },
    "attenuationEffectType": "TankAttenuation",
    "soundGetIn": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1],
    "soundGetOut": ["A3|Sounds_F_EPB|Tracked|noises|get_in_out",0.562341,1,20],
    "soundTurnIn": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnOut": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnInInternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnOutInternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundDammage": ["",0.562341,1],
    "soundEngineOffInt": ["A3|Sounds_F|vehicles2|armor|MBT_02|MBT_02_Engine_Int_Stop",1,1],
    "soundEngineOffExt": ["A3|Sounds_F|vehicles2|armor|MBT_02|MBT_02_Engine_Ext_Stop",3.16228,1,100],
    "BushCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_01",0.630957,1,100],
    "BushCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_02",0.630957,1,100],
    "BushCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_03",0.630957,1,100],
    "soundBushCrash": ["BushCrash1",0.33,"BushCrash2",0.33,"BushCrash3",0.33],
    "buildCrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "buildCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "buildCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "buildCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "buildCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "buildCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundBuildingCrash": ["buildCrash0",0.166,"buildCrash1",0.166,"buildCrash2",0.166,"buildCrash3",0.166,"buildCrash4",0.166,"buildCrash5",0.166],
    "woodCrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "woodCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "woodCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "woodCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "woodCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "woodCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundWoodCrash": ["woodCrash0",0.166,"woodCrash1",0.166,"woodCrash2",0.166,"woodCrash3",0.166,"woodCrash4",0.166,"woodCrash5",0.166],
    "ArmorCrash0": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_01",3.16228,1,200],
    "ArmorCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_02",3.16228,1,200],
    "ArmorCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_03",3.16228,1,200],
    "ArmorCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_04",3.16228,1,200],
    "ArmorCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "ArmorCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "soundArmorCrash": ["ArmorCrash0",0.166,"ArmorCrash1",0.166,"ArmorCrash2",0.166,"ArmorCrash3",0.166,"ArmorCrash4",0.166,"ArmorCrash5",0.166],
    "_generalMacro": "Tank_F",
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "sensorPosition": "gunnerView",
    "audible": 18,
    "sensitivityEar": "0.0075 /3",
    "turnCoef": 5,
    "steerAheadSimul": 0.3,
    "steerAheadPlan": 0.4,
    "brakeDistance": 5,
    "precision": 10,
    "hideProxyInCombat": 1,
    "radarTarget": 1,
    "radarTargetSize": 1.2,
    "visualTarget": 1,
    "visualTargetSize": 1,
    "irTargetSize": 1.2,
    "irScanGround": 2,
    "irScanRangeMax": 0,
    "irScanRangeMin": 0,
    "irScanToEyeFactor": 1,
    "enableRadio": 1,
    "LockDetectionSystem": 0,
    "countermeasureActivationRadius": 2000,
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_3",0.316228,1],
    "memoryPointCargoLight": "cargo light",
    "dampersBumpCoef": 4.5,
    "crewCrashProtection": 0.25,
    "secondaryExplosion": -1,
    "fuelExplosionPower": 1,
    "transportMaxWeapons": 12,
    "transportMaxMagazines": 128,
    "transportMaxBackpacks": 12,
    "maximumLoad": 3000,
    "supplyRadius": -1,
    "memoryPointSupply": "doplnovani",
    # Class: CfgVehicles\Tank_F\TransportBackpacks [Indent level: 1],
    "TransportBackpacks": {
    },
    # Class: CfgVehicles\Tank_F\TransportWeapons [Indent level: 1],
    "TransportWeapons": {
    },
    # Class: CfgVehicles\Tank_F\CamShake [Indent level: 1],
    "CamShake": {
        "power": 5,
        "frequency": 20,
        "distance": 20,
        "minSpeed": 5
    },
    "camShakeCoef": 0,
    # Class: CfgVehicles\Tank_F\NVGMarkers [Indent level: 1],
    "NVGMarkers": {
        # Class: CfgVehicles\Tank_F\NVGMarkers\NVGMarker01 [Indent level: 2]
        "NVGMarker01": {
            "name": "nvg_marker",
            "color": [0.03,0.003,0.003,1],
            "ambient": [0.003,0.0003,0.0003,1],
            "brightness": 0.001,
            "blinking": 1
        }
    },
    "memoryPointDriverOptics": "driverview",
    "engineStartSpeed": 5,
    "explosionEffect": "FuelExplosionBig",
    "mFact": 1,
    "tBody": 250,
    "numberPhysicalWheels": 16,
    "ace_cookoff_ammoLocation": "HitHull",
    "ace_cookoff_cookoffSelections": ["poklop_gunner","poklop_commander"],
    "ace_cookoff_probability": 0.5,
    # Class: CfgVehicles\Tank_F\ACE_Actions [Indent level: 1],
    "ACE_Actions": {
        # Class: CfgVehicles\Tank_F\ACE_Actions\ACE_MainActions [Indent level: 2]
        "ACE_MainActions": {
            "displayName": "Interactions",
            "position": "call ace_interaction_fnc_getVehiclePos",
            "selection": "",
            "distance": 4,
            "condition": "true",
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ACE_Passengers [Indent level: 3],
            "ACE_Passengers": {
                "displayName": "Passengers",
                "condition": "alive _target",
                "statement": "",
                "exceptions": ["isNotSwimming"],
                "insertChildren": "_this call ace_interaction_fnc_addPassengersActions"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_quickmount_GetIn [Indent level: 3],
            "ace_quickmount_GetIn": {
                "displayName": "Get In",
                "condition": "call ace_quickmount_fnc_canShowFreeSeats",
                "statement": "call ace_quickmount_fnc_getInNearest",
                "exceptions": ["isNotSwimming"],
                "insertChildren": "(_this select 2) param [0,[]]"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_rearm_Rearm [Indent level: 3],
            "ace_rearm_Rearm": {
                "displayName": "Rearm",
                "distance": 9,
                "condition": "_this call ace_rearm_fnc_canRearm",
                "statement": "_this call ace_rearm_fnc_rearm",
                "exceptions": ["isNotInside"],
                "icon": "z|ace|addons|rearm|ui|icon_rearm_interact.paa"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_repair_Repair [Indent level: 3],
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
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ACE_unlockVehicle [Indent level: 3],
            "ACE_unlockVehicle": {
                "displayName": "Unlock Vehicle",
                "distance": 4,
                "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [2, 3]}",
                "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,false],[_target]] call CBA_fnc_targetEvent",
                "exceptions": ["isNotSwimming"],
                "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ACE_lockVehicle [Indent level: 3],
            "ACE_lockVehicle": {
                "displayName": "Lock Vehicle",
                "distance": 4,
                "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [0, 1]}",
                "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,true],[_target]] call CBA_fnc_targetEvent",
                "exceptions": ["isNotSwimming"],
                "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ACE_lockpickVehicle [Indent level: 3],
            "ACE_lockpickVehicle": {
                "displayName": "Lockpick Vehicle",
                "distance": 4,
                "condition": "[_player,_target,'canLockpick'] call ace_vehiclelock_fnc_lockpick",
                "statement": "[_player,_target,'startLockpick'] call ace_vehiclelock_fnc_lockpick",
                "exceptions": ["isNotSwimming"]
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\AIME_vehicle_seats_getInAction [Indent level: 3],
            "AIME_vehicle_seats_getInAction": {
                "displayName": "Get In",
                "condition": "call AIME_vehicle_seats_fnc_getin_condition",
                "statement": "call AIME_vehicle_seats_fnc_getin_run",
                "icon": "a3|ui_f|data|igui|cfg|actions|obsolete|ui_action_getin_ca.paa",
                "insertChildren": "call AIME_vehicle_seats_fnc_change_submenus"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_attach_AttachVehicle [Indent level: 3],
            "ace_attach_AttachVehicle": {
                "displayName": "Attach item",
                "condition": "_this call ace_attach_fnc_canAttach",
                "insertChildren": "_this call ace_attach_fnc_getChildrenActions",
                "exceptions": ["isNotSwimming"],
                "showDisabled": 0,
                "icon": "z|ace|addons|attach|UI|attach_ca.paa"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_attach_DetachVehicle [Indent level: 3],
            "ace_attach_DetachVehicle": {
                "displayName": "Detach item",
                "condition": "_this call ace_attach_fnc_canDetach",
                "statement": "_this call ace_attach_fnc_detach",
                "exceptions": ["isNotSwimming"],
                "showDisabled": 0,
                "icon": "z|ace|addons|attach|UI|detach_ca.paa"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_captives_LoadCaptive [Indent level: 3],
            "ace_captives_LoadCaptive": {
                "displayName": "Load Captive",
                "distance": 4,
                "condition": "[_player,objNull,_target] call ace_captives_fnc_canLoadCaptive",
                "statement": "[_player,objNull,_target] call ace_captives_fnc_doLoadCaptive",
                "exceptions": ["isNotEscorting","isNotSwimming"]
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\AIME_inventory_openAction [Indent level: 3],
            "AIME_inventory_openAction": {
                "displayName": "Inventory",
                "condition": "AIME_inventory_settingOpenAction				 && { alive _target }				 && { _target call AIME_inventory_fnc_has_inventory }",
                "statement": "_player action [`Gear`, _target]",
                "icon": "A3|ui_f|data|igui|cfg|actions|gear_ca.paa",
                "exceptions": ["isNotSwimming"]
            }
        }
    },
    # Class: CfgVehicles\Tank_F\Periscope [Indent level: 1],
    "Periscope": {
    },
    "getInRadius": 3.5,
    "hullDamageCauseExplosion": 1,
    "selectionFireAnim": "zasleh",
    "bounding": "usti hlavne",
    "fireDustEffect": "FDustEffects",
    "gearBox": [-7,0,11,8,5.7,4.2],
    "alphaTracks": 0.7,
    "textureTrackWheel": 0,
    "memoryPointTrack1L": "Stopa LL",
    "memoryPointTrack1R": "Stopa LR",
    "memoryPointTrack2L": "Stopa RL",
    "memoryPointTrack2R": "Stopa RR",
    # Class: CfgVehicles\Tank\ViewPilot [Indent level: 1],
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
    "predictTurnSimul": 1.2,
    "predictTurnPlan": 1,
    "soundGear": ["",0.000316228,1],
    "outsideSoundFilter": 1,
    "nightVision": 0,
    "formationX": 20,
    "formationZ": 30,
    "canFloat": 0,
    "camouflage": 8,
    "driverOpticsColor": [1,1,1,1],
    # Class: CfgVehicles\Tank\CargoLight [Indent level: 1],
    "CargoLight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
    # Class: CfgVehicles\Tank\SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles\Tank\SpeechVariants\Default [Indent level: 2]
        "Default": {
            "speechSingular": ["veh_vehicle_tank_s"],
            "speechPlural": ["veh_vehicle_tank_p"]
        }
    },
    "textSingular": "tank",
    "textPlural": "tanks",
    "nameSound": "veh_vehicle_tank_s",
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffectsBig"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffectsBig"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffectsBig"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffectsBig"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffectsBig"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffectsBig"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassEffectsDryBig"],["GdtStratisDryGrass","RDirtEffectsBig"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffectsBig"],["GdtStratisGreenGrass","RDirtEffectsBig"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffectsBig"],["GdtStratisRocky","RDirtEffectsBig"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffectsBig"],["GdtStratisThistles","RDirtEffectsBig"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffectsBig"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffectsBig"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffectsBig"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffectsBig"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffectsBig"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffectsBig"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffectsBig"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RDirtEffectsBig"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RDirtEffectsBig"],["GdtDesert1","RStonesEffectsBig"],["GdtDesert2","RDustEffects"],["GdtDesert2","RGrassEffectsBig"],["GdtDesert2","RDirtEffectsBig"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffectsBig"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffectsBig"],["GdtGrassGreen","RDirtEffectsBig"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassEffectsDryBig"],["GdtGrassDry","RDirtEffectsBig"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffectsBig"],["GdtGrassWild","RDirtEffectsBig"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffectsBig"],["GdtWildField","RDirtEffectsBig"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffectsBig"],["GdtWeed1","RDirtEffectsBig"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffectsBig"],["GdtWeed2","RDirtEffectsBig"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffectsBig"],["GdtThorn","RDirtEffectsBig"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffectsBig"],["GdtStony","RDirtEffectsBig"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffectsBig"],["GdtStonyGreen","RDirtEffectsBig"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffectsBig"],["GdtStonyThistle","RDirtEffectsBig"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"],["CRGrass1","RDustEffects"],["CRGrass1","RGrassEffectsBig"],["CRGrass1","RDirtEffectsBig"],["CRGrass2","RDustEffects"],["CRGrass2","RGrassEffectsBig"],["CRGrass2","RDirtEffectsBig"],["CRGrassW1","RDustEffects"],["CRGrassW1","RGrassEffectsBig"],["CRGrassW1","RDirtEffectsBig"],["CRGrassW2","RDustEffects"],["CRGrassW2","RGrassEffectsBig"],["CRGrassW2","RDirtEffectsBig"],["CRField1","RDustEffects"],["CRField1","RGrassEffectsBig"],["CRField1","RDirtEffectsBig"],["CRField2","RDustEffects"],["CRField2","RGrassEffectsBig"],["CRField2","RDirtEffectsBig"],["CRForest1","RDustEffects"],["CRForest1","RGrassEffectsBig"],["CRForest1","RDirtEffectsBig"],["CRForest2","RDustEffects"],["CRForest2","RGrassEffectsBig"],["CRForest2","RDirtEffectsBig"],["CRGrit1","RDustEffects"],["CRGrit1","RDirtEffectsBig"],["CRHeather","RDustEffects"],["CRHeather","RGrassEffectsBig"],["CRHeather","RDirtEffectsBig"],["CRConcrete","RDirtEffectsBig"],["TKAsfalt","RDirtEffectsBig"],["TKBeton","RDustEffects"],["TKPlevel","RDustEffects"],["TKPlevel","RGrassEffectsBig"],["TKPlevel","RDirtEffectsBig"],["TKPole","RDustEffects"],["TKPole","RGrassEffectsDryBig"],["TKPole","RDirtEffectsBig"],["TKPolopoust","RDustEffects"],["TKPolopoust","RSandEffects"],["TKPolopoust","RDirtEffectsBig"],["TKSkala","RDustEffects"],["TKSkala","RStonesEffects"],["TKSkalniSterk","RDustEffects"],["TKSkalniSterk","RStonesEffects"],["TKSterkNaDno","RDustEffects"],["TKSterkNaDno","RStonesEffects"],["TKMoutain","RDustEffects"],["TKMoutain","RStonesEffects"],["TKValouny","RDustEffects"],["TKValouny","RStonesEffects"],["TKTrava","RDustEffects"],["TKTrava","RGrassEffectsDryBig"],["TKTrava","RDirtEffectsBig"],["TKForest","RDustEffects"],["TKForest","RGrassEffectsDryBig"],["TKForest","RDirtEffectsBig"],["ZRAsfalt","RDirtEffectsBig"],["ZRBeton","RDustEffects"],["RoadDirt_EP1","RDustEffects"],["RoadTarmac_EP1","RDirtEffectsBig"],["ZRPlevel","RDustEffects"],["ZRPlevel","RGrassEffectsBig"],["ZRPlevel","RDirtEffectsBig"],["ZRPole","RDustEffects"],["ZRPole","RGrassEffectsDryBig"],["ZRPole","RDirtEffectsBig"],["ZRPolopoust","RDustEffects"],["ZRPolopoust","RSandEffects"],["ZRPolopoust","RDirtEffectsBig"],["ZRSkala","RDustEffects"],["ZRSkala","RStonesEffects"],["ZRSkalniSterk","RDustEffects"],["ZRSkalniSterk","RStonesEffects"],["ZRSterkNaDno","RDustEffects"],["ZRSterkNaDno","RStonesEffects"],["ZRValouny","RDustEffects"],["ZRValouny","RStonesEffects"],["ZRTrava","RDustEffects"],["ZRTrava","RGrassEffectsDryBig"],["ZRTrava","RDirtEffectsBig"],["DEPolopoust","RDustEffects"],["DEPolopoust","RSandEffects"],["DEPolopoust","RDirtEffectsBig"],["DESkalniSterk","RDustEffects"],["DESkalniSterk","RStonesEffects"],["DETrava","RDustEffects"],["DETrava","RGrassEffectsDryBig"],["DETrava","RDirtEffectsBig"],["WLGrass1","RDustEffects"],["WLGrass1","RGrassEffectsBig"],["WLGrass1","RDirtEffectsBig"],["WLGrass2","RDustEffects"],["WLGrass2","RGrassEffectsBig"],["WLGrass2","RDirtEffectsBig"],["WLGrassW1","RDustEffects"],["WLGrassW1","RGrassEffectsBig"],["WLGrassW1","RDirtEffectsBig"],["WLGrassW2","RDustEffects"],["WLGrassW2","RGrassEffectsBig"],["WLGrassW2","RDirtEffectsBig"],["WLField1","RDustEffects"],["WLField1","RGrassEffectsBig"],["WLField1","RDirtEffectsBig"],["WLField2","RDustEffects"],["WLField2","RGrassEffectsBig"],["WLField2","RDirtEffectsBig"],["WLForest1","RDustEffects"],["WLForest1","RGrassEffectsBig"],["WLForest1","RDirtEffectsBig"],["WLForest2","RDustEffects"],["WLForest2","RGrassEffectsBig"],["WLForest2","RDirtEffectsBig"],["WLMudGround","RDustEffects"],["WLMudGround","RGrassEffectsBig"],["WLMudGround","RDirtEffectsBig"],["WLGrit1","RDustEffects"],["WLGrit1","RDirtEffectsBig"],["WLHeather","RDustEffects"],["WLHeather","RGrassEffectsBig"],["WLHeather","RDirtEffectsBig"],["WLConcrete","RDirtEffectsBig"],["GZTrava","RDustEffects"],["GZTrava","RGrassEffectsDryBig"],["GZTrava","RDirtEffectsBig"],["GZforest","RDustEffects"],["GZforest","RGrassEffectsDryBig"],["GZforest","RDirtEffectsBig"],["GZkameny","RDustEffects"],["GZkameny","RStonesEffects"],["GZHlina","RDustEffects"],["GZHlina","RGrassEffectsBig"],["GZHlina","RDi,
    "leftDustEffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffectsBig"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffectsBig"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffectsBig"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffectsBig"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffectsBig"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffectsBig"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassEffectsDryBig"],["GdtStratisDryGrass","LDirtEffectsBig"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffectsBig"],["GdtStratisGreenGrass","LDirtEffectsBig"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffectsBig"],["GdtStratisRocky","LDirtEffectsBig"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffectsBig"],["GdtStratisThistles","LDirtEffectsBig"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffectsBig"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffectsBig"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffectsBig"],["GdtRubble","LDirtEffectsBig"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffectsBig"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffectsBig"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffectsBig"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffectsBig"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LDirtEffectsBig"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LDirtEffectsBig"],["GdtDesert1","LStonesEffectsBig"],["GdtDesert2","LDustEffects"],["GdtDesert2","LGrassEffectsBig"],["GdtDesert2","LDirtEffectsBig"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffectsBig"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffectsBig"],["GdtGrassGreen","LDirtEffectsBig"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassEffectsDryBig"],["GdtGrassDry","LDirtEffectsBig"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffectsBig"],["GdtGrassWild","LDirtEffectsBig"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffectsBig"],["GdtWildField","LDirtEffectsBig"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffectsBig"],["GdtWeed1","LDirtEffectsBig"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffectsBig"],["GdtWeed2","LDirtEffectsBig"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffectsBig"],["GdtThorn","LDirtEffectsBig"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffectsBig"],["GdtStony","LDirtEffectsBig"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffectsBig"],["GdtStonyGreen","LDirtEffectsBig"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffectsBig"],["GdtStonyThistle","LDirtEffectsBig"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","LDustEffects"],["CRGrass1","LDustEffects"],["CRGrass1","LGrassEffectsBig"],["CRGrass1","LDirtEffectsBig"],["CRGrass2","LDustEffects"],["CRGrass2","LGrassEffectsBig"],["CRGrass2","LDirtEffectsBig"],["CRGrassW1","LDustEffects"],["CRGrassW1","LGrassEffectsBig"],["CRGrassW1","LDirtEffectsBig"],["CRGrassW2","LDustEffects"],["CRGrassW2","LGrassEffectsBig"],["CRGrassW2","LDirtEffectsBig"],["CRField1","LDustEffects"],["CRField1","LGrassEffectsBig"],["CRField1","LDirtEffectsBig"],["CRField2","LDustEffects"],["CRField2","LGrassEffectsBig"],["CRField2","LDirtEffectsBig"],["CRForest1","LDustEffects"],["CRForest1","LGrassEffectsBig"],["CRForest1","LDirtEffectsBig"],["CRForest2","LDustEffects"],["CRForest2","LGrassEffectsBig"],["CRForest2","LDirtEffectsBig"],["CRGrit1","LDustEffects"],["CRGrit1","LDirtEffectsBig"],["CRHeather","LDustEffects"],["CRHeather","LGrassEffectsBig"],["CRHeather","LDirtEffectsBig"],["CRConcrete","LDirtEffectsBig"],["TKAsfalt","LDirtEffectsBig"],["TKBeton","LDustEffects"],["RoadDirt_EP1","LDustEffects"],["RoadTarmac_EP11","LDirtEffectsBig"],["TKPlevel","LDustEffects"],["TKPlevel","LGrassEffectsBig"],["TKPlevel","LDirtEffectsBig"],["TKPole","LDustEffects"],["TKPole","LGrassEffectsDryBig"],["TKPole","LDirtEffectsBig"],["TKPolopoust","LDustEffects"],["TKPolopoust","LSandEffects"],["TKPolopoust","LDirtEffectsBig"],["TKSkala","LDustEffects"],["TKSkala","LStonesEffectsBig"],["TKSkalniSterk","LDustEffects"],["TKSkalniSterk","LStonesEffectsBig"],["TKSterkNaDno","LDustEffects"],["TKSterkNaDno","LStonesEffectsBig"],["TKMoutain","LDustEffects"],["TKMoutain","LStonesEffectsBig"],["TKValouny","LDustEffects"],["TKValouny","LStonesEffectsBig"],["TKTrava","LDustEffects"],["TKTrava","LGrassEffectsDryBig"],["TKTrava","LDirtEffectsBig"],["TKForest","LDustEffects"],["TKForest","LGrassEffectsDryBig"],["TKForest","LDirtEffectsBig"],["ZRAsfalt","LDirtEffectsBig"],["ZRBeton","LDustEffects"],["ZRPlevel","LDustEffects"],["ZRPlevel","LGrassEffectsBig"],["ZRPlevel","LDirtEffectsBig"],["ZRPole","LDustEffects"],["ZRPole","LGrassEffectsDryBig"],["ZRPole","LDirtEffectsBig"],["ZRPolopoust","LDustEffects"],["ZRPolopoust","LSandEffects"],["ZRPolopoust","LDirtEffectsBig"],["ZRSkala","LDustEffects"],["ZRSkala","LStonesEffectsBig"],["ZRSkalniSterk","LDustEffects"],["ZRSkalniSterk","LStonesEffectsBig"],["ZRSterkNaDno","LDustEffects"],["ZRSterkNaDno","LStonesEffectsBig"],["ZRValouny","LDustEffects"],["ZRValouny","LStonesEffectsBig"],["ZRTrava","LDustEffects"],["ZRTrava","LGrassEffectsDryBig"],["ZRTrava","LDirtEffectsBig"],["DEPolopoust","LDustEffects"],["DEPolopoust","LSandEffects"],["DEPolopoust","LDirtEffectsBig"],["DESkalniSterk","LDustEffects"],["DESkalniSterk","LStonesEffectsBig"],["DETrava","LDustEffects"],["DETrava","LGrassEffectsDryBig"],["DETrava","LDirtEffectsBig"],["WLGrass1","LDustEffects"],["WLGrass1","LGrassEffectsBig"],["WLGrass1","LDirtEffectsBig"],["WLGrass2","LDustEffects"],["WLGrass2","LGrassEffectsBig"],["WLGrass2","LDirtEffectsBig"],["WLGrassW1","LDustEffects"],["WLGrassW1","LGrassEffectsBig"],["WLGrassW1","LDirtEffectsBig"],["WLGrassW2","LDustEffects"],["WLGrassW2","LGrassEffectsBig"],["WLGrassW2","LDirtEffectsBig"],["WLField1","LDustEffects"],["WLField1","LGrassEffectsBig"],["WLField1","LDirtEffectsBig"],["WLField2","LDustEffects"],["WLField2","LGrassEffectsBig"],["WLField2","LDirtEffectsBig"],["WLForest1","LDustEffects"],["WLForest1","LGrassEffectsBig"],["WLForest1","LDirtEffectsBig"],["WLForest2","LDustEffects"],["WLForest2","LGrassEffectsBig"],["WLForest2","LDirtEffectsBig"],["WLMudGround","LDustEffects"],["WLMudGround","LGrassEffectsBig"],["WLMudGround","LDirtEffectsBig"],["WLGrit1","LDustEffects"],["WLGrit1","LDirtEffectsBig"],["WLHeather","LDustEffects"],["WLHeather","LGrassEffectsBig"],["WLHeather","LDirtEffectsBig"],["WLConcrete","LDirtEffectsBig"],["GZTrava","LDustEffects"],["GZTrava","LGrassEffectsDryBig"],["GZTrava","LDirtEffectsBig"],["GZforest","LDustEffects"],["GZForest","LGrassEffectsDryBig"],["GZForest","LDirtEffectsBig"],["GZkameny","LDustEffects"],["GZkameny","LStonesEffectsBig"],["GZHli,
    # Class: CfgVehicles\Tank\DestructionEffects [Indent level: 1],
    "DestructionEffects": {
        # Class: CfgVehicles\Tank\DestructionEffects\LightBig1 [Indent level: 2]
        "LightBig1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles\Tank\DestructionEffects\Sound [Indent level: 2],
        "Sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireBig1 [Indent level: 2],
        "FireBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\Refract1 [Indent level: 2],
        "Refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefract",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig1 [Indent level: 2],
        "SmokeBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SparksBig1 [Indent level: 2],
        "SparksBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 0
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireSparksBig1 [Indent level: 2],
        "FireSparksBig1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2.8
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireBig2 [Indent level: 2],
        "FireBig2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig1_2 [Indent level: 2],
        "SmokeBig1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig2 [Indent level: 2],
        "SmokeBig2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 3.2
        },
        # Class: CfgVehicles\Tank\DestructionEffects\LightFlames1 [Indent level: 2],
        "LightFlames1": {
            "simulation": "particles",
            "type": "FlameLightBC",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 0.5,
            "enabled": "distToWater"
        }
    },
    "headGforceLeaningFactor": [0.0075,0.005,0.0075],
    "tf_hasLRradio": 1,
    "tf_isolatedAmount": 1,
    # Class: CfgVehicles\Tank\ViewCargo [Indent level: 1],
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
    # Class: CfgVehicles\Tank\ACE_SelfActions [Indent level: 1],
    "ACE_SelfActions": {
        # Class: CfgVehicles\Tank\ACE_SelfActions\ACE_Passengers [Indent level: 2]
        "ACE_Passengers": {
            "displayName": "Passengers",
            "condition": "alive _target",
            "statement": "",
            "insertChildren": "_this call ace_interaction_fnc_addPassengersActions"
        },
        # Class: CfgVehicles\Tank\ACE_SelfActions\ace_quickmount_ChangeSeat [Indent level: 2],
        "ace_quickmount_ChangeSeat": {
            "displayName": "Change seat",
            "condition": "call ace_quickmount_fnc_canShowFreeSeats",
            "statement": "",
            "insertChildren": "(_this select 2) param [0,[]]"
        },
        # Class: CfgVehicles\Tank\ACE_SelfActions\ACE_unlockVehicle [Indent level: 2],
        "ACE_unlockVehicle": {
            "displayName": "Unlock Vehicle",
            "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [2, 3]}",
            "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,false],[_target]] call CBA_fnc_targetEvent",
            "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
        },
        # Class: CfgVehicles\Tank\ACE_SelfActions\ACE_lockVehicle [Indent level: 2],
        "ACE_lockVehicle": {
            "displayName": "Lock Vehicle",
            "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [0, 1]}",
            "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,true],[_target]] call CBA_fnc_targetEvent",
            "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
        },
        # Class: CfgVehicles\Tank\ACE_SelfActions\ACE_lockpickVehicle [Indent level: 2],
        "ACE_lockpickVehicle": {
            "displayName": "Lockpick Vehicle",
            "condition": "[_player,_target,'canLockpick'] call ace_vehiclelock_fnc_lockpick",
            "statement": "[_player,_target,'startLockpick'] call ace_vehiclelock_fnc_lockpick"
        },
        # Class: CfgVehicles\Tank\ACE_SelfActions\ResetFCS [Indent level: 2],
        "ResetFCS": {
            "displayName": "Reset FCS",
            "condition": "_player call ace_fcs_fnc_canResetFCS",
            "statement": "[vehicle _player,[_player] call ace_common_fnc_getTurretIndex] call ace_fcs_fnc_reset;",
            "showDisabled": 0,
            "icon": ""
        }
    },
    "ace_refuel_canReceive": 1,
    "ace_refuel_flowRate": 4,
    "ace_cargo_space": 4,
    "ace_cargo_hasCargo": 1,
    "selectionBrakeLights": "brzdove svetlo",
    "memoryPointMissile": ["spice rakety","usti hlavne"],
    "memoryPointMissileDir": ["konec rakety","konec hlavne"],
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "leftWaterEffect": "LWaterEffects",
    "rightWaterEffect": "RWaterEffects",
    "leftFastWaterEffect": "LWaterEffects",
    "rightFastWaterEffect": "RWaterEffects",
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
    "wheelDamageRadiusCoef": 0.9,
    "wheelDestroyRadiusCoef": 0.4,
    "weaponsGroup1": 1,
    "weaponsGroup2": "2 + 		4",
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    # Class: CfgVehicles\AllVehicles\SquadTitles [Indent level: 1],
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
    # Class: CfgVehicles\AllVehicles\NewTurret [Indent level: 1],
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
    # Class: CfgVehicles\AllVehicles\RenderTargets [Indent level: 1],
    "RenderTargets": {
    },
    "cargoProxyIndexes": [],
    "driverLeftHandAnimName": "",
    "driverRightHandAnimName": "",
    "driverLeftLegAnimName": "",
    "driverRightLegAnimName": "",
    "cargoDoors": [],
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
    "epeImpulseDamageCoef": 30,
    "gunnerHasFlares": 1,
    "enableManualFire": 1,
    "sensitivity": 2.5,
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
    "radarType": 0,
    "limitedSpeedCoef": 0.22,
    "hasDriver": 1,
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 0,
    "enableWatch": 0,
    "usePreciseGetInAction": 0,
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
    "soundCrashes": ["soundCrash",1],
    "soundLandCrashes": ["soundLandCrash",1],
    "soundWaterCrashes": ["soundWaterCrash",1],
    "emptySound": ["",0,1],
    "soundLocked": ["",1,1],
    "cargoAction": [],
    "cargoIsCoDriver": [0],
    "driverCompartments": "Compartment1",
    "cargoCompartments": ["Compartment1"],
    "driverOpticsEffect": [],
    "canHideDriver": -1,
    "castDriverShadow": 0,
    "castCargoShadow": 0,
    "viewDriverShadowDiff": 1,
    "viewDriverShadowAmb": 1,
    "ejectDeadDriver": 0,
    "ejectDeadCargo": 0,
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
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "slingLoadCargoMemoryPoints": [],
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    # Class: CfgVehicles\All\camShakeGForce [Indent level: 1],
    "camShakeGForce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minSpeed": 1,
        "duration": 3
    },
    "minGForce": 0.2,
    "maxGForce": 2,
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
    "features": "",
    "insideDetectCoef": 0.05,
    "coefSpeedInside": 1,
    "windSockExist": 0,
    "SLX_XEH_DISABLED": 0,
}