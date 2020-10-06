rhsusf_m1025_w_Mk19 = {
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_m1025_w_mk19.paa",
    "faction": "rhs_faction_usarmy_wd",
    "vehicleClass": "rhs_vehclass_car",
    "crew": "rhsusf_army_ucp_rifleman",
    "author": "Red Hammer Studios",
    "model": "rhsusf|addons|rhsusf_hmmwv|rhsusf_m1025_mk19",
    "Icon": "rhsusf|addons|rhsusf_hmmwv|icons|ico_m1025_mk19.paa",
    "Picture": "rhsusf|addons|rhsusf_hmmwv|pictures|rhsusf_m1025_mk19_ca.paa",
    "displayname": "M1025A2 (Mk19)",
    # Class: CfgVehicles\rhsusf_m1025_w_mk19\Turrets [Indent level: 1],
    "Turrets": {
        # Class: CfgVehicles\rhsusf_m1025_w_mk19\Turrets\M2_Turret [Indent level: 2]
        "M2_Turret": {
            "discreteDistance": [100,200,300,400,500,600,800,1000,1100,1200,1300,1400,1500],
            "discreteDistanceInitIndex": 2,
            "gunnerLeftHandAnimName": "OtocHlaven",
            "gunnerRightHandAnimName": "OtocHlaven",
            "weapons": ["RHS_MK19"],
            "magazines": ["RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M1001"],
            "gunnerLeftLegAnimName": "leg_left",
            "gunnerRightLegAnimName": "leg_right",
            "body": "mainTurret",
            "gun": "mainGun",
            "animationSourceBody": "mainTurret",
            "animationSourceGun": "mainGun",
            "turretInfoType": "RscOptics_Offroad_01",
            "gunnerForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "minElev": -10,
            "maxElev": 40,
            "soundServo": ["A3|sounds_f|dummysound",1e-006,1],
            "soundAttenuationTurret": "HeliAttenuationGunner",
            "disableSoundAttenuation": 1,
            "gunnerAction": "RHS_HMMWV_Gunner03",
            "gunnerInAction": "RHS_HMMWV_Gunner03a_in",
            "lodTurnedIn": 0,
            "lodTurnedOut": 1000,
            "lodOpticsOut": 1000,
            "canhideGunner": 1,
            "inGunnerMayFire": 0,
            "outGunnerMayFire": 1,
            "viewGunnerInExternal": 1,
            "gunnerDoor": "Door_RB",
            "gunnerCompartments": "Compartment1",
            "ejectDeadGunner": 0,
            "castGunnerShadow": 1,
            "stabilizedInAxes": 0,
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGunnerOptics": "",
            "memoryPointGunnerOutOptics": "gunnerview",
            "gunnerOpticsModel": "",
            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "optics": 0,
            "memoryPointsGetInGunner": "pos_cargo_RB",
            "memoryPointsGetInGunnerDir": "pos_cargo_RB_dir",
            # Class: CfgVehicles\rhsusf_m1025_w_m2\Turrets\M2_Turret\ViewOptics [Indent level: 3],
            "ViewOptics": {
                "initFov": 0.7,
                "minFov": 0.25,
                "maxFov": 1.1,
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
            # Class: CfgVehicles\rhsusf_m1025_w_m2\Turrets\M2_Turret\ViewGunner [Indent level: 3],
            "ViewGunner": {
                "initFov": 0.7,
                "minFov": 0.25,
                "maxFov": 1.1,
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
            "memoryPointGun": "machinegun",
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "minTurn": -360,
            "maxTurn": 360,
            "primaryGunner": 1,
            "enableManualFire": 0,
            "startEngine": 0,
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\HitPoints [Indent level: 3],
            "HitPoints": {
                # Class: CfgVehicles\Car_F\Turrets\MainTurret\HitPoints\HitTurret [Indent level: 4]
                "HitTurret": {
                    "armor": 0.8,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passThrough": 0.5,
                    "explosionShielding": 0.4
                },
                # Class: CfgVehicles\Car_F\Turrets\MainTurret\HitPoints\HitGun [Indent level: 4],
                "HitGun": {
                    "armor": 0.4,
                    "material": -1,
                    "name": "zbran",
                    "visual": "zbran",
                    "passThrough": 0,
                    "explosionShielding": 0.2
                }
            },
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\Components [Indent level: 3],
            "Components": {
            },
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerName": "Gunner",
            "gunnerType": "",
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
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOpticsEffect": [],
            "gunnerOutOpticsEffect": [],
            "gunnerOutForceOptics": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "hideWeaponsGunner": 1,
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
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\rhsusf_m1025_w_mk19\Turrets\CargoTurret_01 [Indent level: 2],
        "CargoTurret_01": {
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "passenger_inside_1",
            "gunnerName": "Passenger (Right Front)",
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "memoryPointsGetInGunner": "pos_cargo_RF",
            "memoryPointsGetInGunnerDir": "pos_cargo_RF_dir",
            "memoryPointGunnerOptics": "",
            "gunnerDoor": "Door_RF",
            "proxyIndex": 1,
            "maxTurn": -34,
            "minTurn": -75,
            "maxElev": 15,
            "minElev": -7,
            # Class: CfgVehicles\rhsusf_m1025_w\Turrets\CargoTurret_01\dynamicViewLimits [Indent level: 3],
            "dynamicViewLimits": {
            },
            "enabledByAnimationSource": "ani_window_2",
            "selectionFireAnim": "",
            # Class: CfgVehicles\rhsusf_m1025_w\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
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
            "commanding": 0,
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
            "isPersonTurret": 1,
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\rhsusf_m1025_w_mk19\Turrets\CargoTurret_02 [Indent level: 2],
        "CargoTurret_02": {
            "gunnerAction": "passenger_inside_2",
            "gunnerName": "Passenger (Right Back)",
            "memoryPointsGetInGunner": "pos_cargo_RB",
            "memoryPointsGetInGunnerDir": "pos_cargo_RB_dir",
            "proxyIndex": 2,
            "enabledByAnimationSource": "ani_window_4",
            "gunnerDoor": "Door_RB",
            "maxTurn": -37,
            "minTurn": -65,
            "maxElev": 9,
            "minElev": -15,
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "memoryPointGunnerOptics": "",
            # Class: CfgVehicles\rhsusf_m1025_w\Turrets\CargoTurret_01\dynamicViewLimits [Indent level: 3],
            "dynamicViewLimits": {
            },
            "selectionFireAnim": "",
            # Class: CfgVehicles\rhsusf_m1025_w\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
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
            "commanding": 0,
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
            "isPersonTurret": 1,
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\rhsusf_m1025_w_mk19\Turrets\CargoTurret_03 [Indent level: 2],
        "CargoTurret_03": {
            "gunnerAction": "passenger_inside_2",
            "gunnerName": "Passenger (Left Back)",
            "memoryPointsGetInGunner": "pos_cargo_LB",
            "memoryPointsGetInGunnerDir": "pos_cargo_LB_dir",
            "proxyIndex": 3,
            "maxTurn": 90,
            "minTurn": 54,
            "maxElev": 9,
            "minElev": -15,
            "enabledByAnimationSource": "ani_window_3",
            "gunnerDoor": "Door_LB",
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "memoryPointGunnerOptics": "",
            # Class: CfgVehicles\rhsusf_m1025_w\Turrets\CargoTurret_01\dynamicViewLimits [Indent level: 3],
            "dynamicViewLimits": {
            },
            "selectionFireAnim": "",
            # Class: CfgVehicles\rhsusf_m1025_w\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
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
            "commanding": 0,
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
            "isPersonTurret": 1,
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
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        },
        # Class: CfgVehicles\rhsusf_m998_w_4dr\Turrets\CargoTurret_04 [Indent level: 2],
        "CargoTurret_04": {
            "gunnerName": "Passenger (Right Middle)",
            "memoryPointsGetInGunner": "pos_cargo_RB",
            "memoryPointsGetInGunnerDir": "pos_cargo_RB_dir",
            "proxyIndex": 2,
            "maxTurn": -20,
            "minTurn": -95,
            "gunnerAction": "passenger_inside_2",
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            # Class: CfgVehicles\rhsusf_m998_w_4dr\Turrets\CargoTurret_03\dynamicViewLimits [Indent level: 3],
            "dynamicViewLimits": {
            },
            "gunnerCompartments": "Compartment2",
            "maxElev": 55,
            "minElev": -45,
            "isPersonTurret": 1,
            # Class: CfgVehicles\rhsusf_m998_w_4dr\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
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
            "commanding": 0,
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
        # Class: CfgVehicles\rhsusf_m998_w_4dr\Turrets\CargoTurret_05 [Indent level: 2],
        "CargoTurret_05": {
            "gunnerName": "Passenger (Left Middle)",
            "memoryPointsGetInGunner": "pos_cargo_LB",
            "memoryPointsGetInGunnerDir": "pos_cargo_LB_dir",
            "proxyIndex": 3,
            "maxTurn": 95,
            "minTurn": 38,
            "gunnerAction": "passenger_inside_2",
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            # Class: CfgVehicles\rhsusf_m998_w_4dr\Turrets\CargoTurret_03\dynamicViewLimits [Indent level: 3],
            "dynamicViewLimits": {
            },
            "gunnerCompartments": "Compartment2",
            "maxElev": 55,
            "minElev": -45,
            "isPersonTurret": 1,
            # Class: CfgVehicles\rhsusf_m998_w_4dr\Turrets\CargoTurret_01\Hitpoints [Indent level: 3],
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
            "commanding": 0,
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
        # Class: CfgVehicles\Car_F\Turrets\MainTurret [Indent level: 2],
        "MainTurret": {
            "stabilizedInAxes": 4,
            "outGunnerMayFire": 1,
            "memoryPointGun": "machinegun",
            "body": "",
            "gun": "",
            "gunnerAction": "ManActTestDriverOut",
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "soundServo": ["A3|sounds_f|dummysound",0.316228,1,15],
            "minElev": -5,
            "maxElev": 40,
            "minTurn": -360,
            "maxTurn": 360,
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "primaryGunner": 1,
            "enableManualFire": 0,
            "gunnerForceOptics": 0,
            "startEngine": 0,
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\HitPoints [Indent level: 3],
            "HitPoints": {
                # Class: CfgVehicles\Car_F\Turrets\MainTurret\HitPoints\HitTurret [Indent level: 4]
                "HitTurret": {
                    "armor": 0.8,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passThrough": 0.5,
                    "explosionShielding": 0.4
                },
                # Class: CfgVehicles\Car_F\Turrets\MainTurret\HitPoints\HitGun [Indent level: 4],
                "HitGun": {
                    "armor": 0.4,
                    "material": -1,
                    "name": "zbran",
                    "visual": "zbran",
                    "passThrough": 0,
                    "explosionShielding": 0.2
                }
            },
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
            # Class: CfgVehicles\Car_F\Turrets\MainTurret\ViewGunner [Indent level: 3],
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
            "gunnerType": "",
            "primaryObserver": 0,
            "weapons": [],
            "magazines": [],
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
            "gunnerInAction": "ManActTestDriver",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0,
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        }
    },
    # Class: CfgVehicles\rhsusf_m1025_w_mk19\AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles\rhsusf_m1025_w_mk19\AnimationSources\belt_rotation [Indent level: 2]
        "belt_rotation": {
            "source": "reload",
            "weapon": "RHS_MK19"
        },
        # Class: CfgVehicles\rhsusf_m1025_w_mk19\AnimationSources\ReloadMagazine [Indent level: 2],
        "ReloadMagazine": {
            "source": "reloadmagazine",
            "weapon": "RHS_MK19"
        },
        # Class: CfgVehicles\rhsusf_m1025_w_mk19\AnimationSources\Revolving [Indent level: 2],
        "Revolving": {
            "source": "revolving",
            "weapon": "RHS_MK19"
        },
        # Class: CfgVehicles\rhsusf_m1025_w_m2\AnimationSources\ReloadAnim [Indent level: 2],
        "ReloadAnim": {
            "source": "reload",
            "weapon": "RHS_M2"
        },
        # Class: CfgVehicles\rhsusf_m1025_w_m2\AnimationSources\muzzle_rot_MG [Indent level: 2],
        "muzzle_rot_MG": {
            "source": "ammorandom",
            "weapon": "RHS_M2"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\AnimationSources\trunk [Indent level: 2],
        "trunk": {
            "source": "user",
            "animPeriod": 1.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m1025_w\AnimationSources\ani_window_1 [Indent level: 2],
        "ani_window_1": {
            "source": "door",
            "animPeriod": 1.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m1025_w\AnimationSources\ani_window_2 [Indent level: 2],
        "ani_window_2": {
            "source": "door",
            "animPeriod": 1.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m1025_w\AnimationSources\ani_window_3 [Indent level: 2],
        "ani_window_3": {
            "source": "door",
            "animPeriod": 1.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m1025_w\AnimationSources\ani_window_4 [Indent level: 2],
        "ani_window_4": {
            "source": "door",
            "animPeriod": 1.1,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_4dr_fulltop\AnimationSources\hide_backTop [Indent level: 2],
        "hide_backTop": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-005
        },
        # Class: CfgVehicles\rhsusf_m998_w_4dr_fulltop\AnimationSources\hide_middleTop [Indent level: 2],
        "hide_middleTop": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-005
        },
        # Class: CfgVehicles\rhsusf_m998_w_4dr_halftop\AnimationSources\hide_frontTop [Indent level: 2],
        "hide_frontTop": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-005
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\longlights_hide [Indent level: 2],
        "longlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\shortlights_hide [Indent level: 2],
        "shortlights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\lights_hide [Indent level: 2],
        "lights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\light_bo [Indent level: 2],
        "light_bo": {
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\light_stop [Indent level: 2],
        "light_stop": {
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\hide_snorkel [Indent level: 2],
        "hide_snorkel": {
            "initPhase": 1,
            "displayName": "hide snorkel",
            "author": "Red Hammer Studios",
            "mass": -80,
            "source": "user",
            "animPeriod": 1e-005
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\hide_CIP [Indent level: 2],
        "hide_CIP": {
            "displayName": "hide CIP",
            "author": "Red Hammer Studios",
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\hide_BFT [Indent level: 2],
        "hide_BFT": {
            "displayName": "hide BFT",
            "author": "Red Hammer Studios",
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\hide_Antenna [Indent level: 2],
        "hide_Antenna": {
            "displayName": "hide Antennas",
            "author": "Red Hammer Studios",
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\hide_A2_Parts [Indent level: 2],
        "hide_A2_Parts": {
            "displayName": "hide A2 Parts",
            "author": "Red Hammer Studios",
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\A1_bumper [Indent level: 2],
        "A1_bumper": {
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\Hide_A2Bumper [Indent level: 2],
        "Hide_A2Bumper": {
            "displayName": "switch to old bumper",
            "author": "Red Hammer Studios",
            "forceAnimatePhase": 1,
            "forceAnimate": ["A1_bumper",1],
            "forceAnimate2": ["A1_bumper",0],
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\Hide_Brushguard [Indent level: 2],
        "Hide_Brushguard": {
            "initPhase": 1,
            "displayName": "hide brushguard",
            "author": "Red Hammer Studios",
            "source": "user",
            "animPeriod": 1e-005
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\Door_LF [Indent level: 2],
        "Door_LF": {
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_HMMWV_Door",
            "soundPosition": "door_1_axis"
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\Door_RF [Indent level: 2],
        "Door_RF": {
            "soundPosition": "door_2_axis",
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_HMMWV_Door"
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\Door_LB [Indent level: 2],
        "Door_LB": {
            "soundPosition": "door_3_axis",
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_HMMWV_Door"
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\AnimationSources\Door_RB [Indent level: 2],
        "Door_RB": {
            "soundPosition": "door_4_axis",
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHS_HMMWV_Door"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\HitLFWheel [Indent level: 2],
        "HitLFWheel": {
            "source": "Hit",
            "hitpoint": "HitLFWheel",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\HitRFWheel [Indent level: 2],
        "HitRFWheel": {
            "hitpoint": "HitRFWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\HitLBWheel [Indent level: 2],
        "HitLBWheel": {
            "hitpoint": "HitLF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\HitRBWheel [Indent level: 2],
        "HitRBWheel": {
            "hitpoint": "HitRF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\HitGlass3 [Indent level: 2],
        "HitGlass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\HitGlass4 [Indent level: 2],
        "HitGlass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\HitGlass5 [Indent level: 2],
        "HitGlass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\HitGlass6 [Indent level: 2],
        "HitGlass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\Hitwindshield_1 [Indent level: 2],
        "Hitwindshield_1": {
            "hitpoint": "Hitwindshield_1",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\AnimationSources\Hitwindshield_2 [Indent level: 2],
        "Hitwindshield_2": {
            "hitpoint": "Hitwindshield_2",
            "source": "Hit",
            "raw": 1
        }
    },
    "attenuationEffectType": "RHS_CarAttenuation",
    # Class: CfgVehicles\rhsusf_m1025_w_m2\SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles\rhsusf_m1025_w_m2\SpeechVariants\Default [Indent level: 2]
        "Default": {
            "speechSingular": ["veh_vehicle_armedcar_s"],
            "speechPlural": ["veh_vehicle_armedcar_p"]
        }
    },
    "textSingular": "alpha victor (MRAP)",
    "textPlural": "alpha victors",
    "nameSound": "veh_vehicle_armedcar_s",
    # Class: CfgVehicles\rhsusf_m1025_w_m2\HitPoints [Indent level: 1],
    "HitPoints": {
        # Class: CfgVehicles\rhsusf_m1025_w\HitPoints\hitwindshield_1 [Indent level: 2]
        "hitwindshield_1": {
            "armor": 2.29,
            "material": -1,
            "name": "windshield_1",
            "armorComponent": "windshield_1",
            "visual": "windshield_1",
            "passThrough": 0,
            "radius": 0.4
        },
        # Class: CfgVehicles\rhsusf_m1025_w\HitPoints\hitwindshield_2 [Indent level: 2],
        "hitwindshield_2": {
            "armor": 2.29,
            "material": -1,
            "name": "windshield_2",
            "armorComponent": "windshield_2",
            "visual": "windshield_2",
            "passThrough": 0,
            "radius": 0.4
        },
        # Class: CfgVehicles\rhsusf_m1025_w\HitPoints\HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "armor": 2.09,
            "material": -1,
            "name": "glass1",
            "armorComponent": "glass1",
            "visual": "glass1",
            "passThrough": 0,
            "radius": 0.4
        },
        # Class: CfgVehicles\rhsusf_m1025_w\HitPoints\HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "armor": 2.09,
            "name": "glass2",
            "armorComponent": "glass2",
            "visual": "glass2",
            "radius": 0.4,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_m1025_w\HitPoints\HitGlass3 [Indent level: 2],
        "HitGlass3": {
            "armor": 2.09,
            "name": "glass3",
            "armorComponent": "glass3",
            "visual": "glass3",
            "radius": 0.4,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_m1025_w\HitPoints\HitGlass4 [Indent level: 2],
        "HitGlass4": {
            "armor": 2.09,
            "name": "glass4",
            "armorComponent": "glass4",
            "visual": "glass4",
            "radius": 0.4,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitGlass5 [Indent level: 2],
        "HitGlass5": {
            "name": "glass5",
            "armorComponent": "glass5",
            "visual": "glass5",
            "radius": 0.4,
            "armor": 0.09,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitGlass6 [Indent level: 2],
        "HitGlass6": {
            "name": "glass6",
            "armorComponent": "glass6",
            "visual": "glass6",
            "radius": 0.4,
            "armor": 0.09,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitBody [Indent level: 2],
        "HitBody": {
            "armor": 4.6,
            "material": -1,
            "passThrough": 1,
            "radius": 0.2,
            "name": "vehicle",
            "visual": "damage"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\hitfuel [Indent level: 2],
        "hitfuel": {
            "armor": -150,
            "passThrough": 0.5,
            "explosionShielding": 0.5,
            "radius": 0.2,
            "name": "fuel",
            "visual": "-"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitLFWheel [Indent level: 2],
        "HitLFWheel": {
            "radius": 0.2,
            "visual": "wheel_1_tire",
            "name": "wheel_1",
            "armorComponent": "wheel_1_tire",
            "armor": -150,
            "minimalHit": -0.045,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitRFWheel [Indent level: 2],
        "HitRFWheel": {
            "radius": 0.2,
            "visual": "wheel_2_tire",
            "name": "wheel_2",
            "armorComponent": "wheel_2_tire",
            "armor": -150,
            "minimalHit": -0.045,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitLF2Wheel [Indent level: 2],
        "HitLF2Wheel": {
            "radius": 0.2,
            "visual": "wheel_3_tire",
            "name": "wheel_3",
            "armorComponent": "wheel_3_tire",
            "armor": -150,
            "minimalHit": -0.045,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitRF2Wheel [Indent level: 2],
        "HitRF2Wheel": {
            "radius": 0.2,
            "visual": "wheel_4_tire",
            "name": "wheel_4",
            "armorComponent": "wheel_4_tire",
            "armor": -150,
            "minimalHit": -0.045,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitEngine [Indent level: 2],
        "HitEngine": {
            "armor": -100,
            "minimalhit": -0.1,
            "passThrough": 0.2,
            "radius": 0.15,
            "name": "engine",
            "visual": "damage",
            # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitEngine\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke [Indent level: 4],
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Fire [Indent level: 4],
                "RHS_Engine_Fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sparks [Indent level: 4],
                "RHS_Engine_Sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds [Indent level: 4],
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1 [Indent level: 4],
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2 [Indent level: 4],
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
        # Class: CfgVehicles\MRAP_01_base_F\HitPoints\HitHull [Indent level: 2],
        "HitHull": {
            "armor": 1,
            "material": -1,
            "armorComponent": "hit_hull",
            "name": "hit_hull_point",
            "visual": "-",
            "passThrough": 0.5,
            "minimalHit": 0.2,
            "explosionShielding": 0.6,
            "radius": 0.25
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
    "threat": [0.9,0.3,0.1],
    "showNVGGunner": 1,
    "hiddenSelections": ["exterior","interior","A2","wheels","mainbody","hood gratting","camo1","camo2","camo3","unitdecals_1","unitdecals_2","ind_wait","ind_brake","ind_highbeam"],
    "HiddenSelectionsTextures": ["rhsusf|addons|rhsusf_hmmwv|textures|m998_exterior_w_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m998_interior_w_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|A2_parts_WD_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|wheel_wranglermt_b_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m998_mainbody_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|gratting_w_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|tile_exmetal_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m1025_w_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|mk64mount_w_co.paa","rhsusf|addons|rhsusf_hmmwv|unitdecals|101stab_502reg_2ndbn_a12_w_co.paa",""],
    # Class: CfgVehicles\rhsusf_m1025_w_m2\textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles\rhsusf_m1025_w_m2\textureSources\standard [Indent level: 2]
        "standard": {
            "displayName": "Woodland",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_hmmwv|textures|m998_exterior_w_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m998_interior_w_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|A2_parts_WD_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|wheel_wranglermt_b_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m998_mainbody_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|gratting_w_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|tile_exmetal_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m1025_w_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|mk64mount_w_co.paa"],
            "factions": ["rhs_faction_usarmy_wd"]
        },
        # Class: CfgVehicles\rhsusf_m1025_w_m2\textureSources\Desert [Indent level: 2],
        "Desert": {
            "displayName": "Desert",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_hmmwv|textures|m998_exterior_d_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m998_interior_d_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|A2_parts_D_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|wheel_wranglermt_d_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m998_mainbody_d_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|gratting_d_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|tile_exmetal_d_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m1025_d_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|mk64mount_d_co.paa"],
            "factions": ["rhs_faction_usarmy_wd"]
        },
        # Class: CfgVehicles\rhsusf_m1025_w_m2\textureSources\Olive [Indent level: 2],
        "Olive": {
            "displayName": "Olive",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_hmmwv|textures|m998_exterior_g_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m998_interior_w_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|A2_parts_g_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|wheel_wranglermt_b_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m998_mainbody_g_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|gratting_w_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|tile_exmetal_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|m1025_g_co.paa","rhsusf|addons|rhsusf_hmmwv|textures|mk64mount_w_co.paa"],
            "factions": ["rhs_faction_usarmy_wd"]
        }
    },
    "textureList": [],
    "normalSpeedForwardCoef": 0.7,
    "slownSpeedForwardCoef": 0.55,
    "turnCoef": 3,
    "terrainCoef": 0.5,
    "simulation": "carx",
    "dampersBumpCoef": 0,
    "precision": 9,
    "brakeDistance": 3,
    "acceleration": 15,
    "fireResistance": 5,
    "maxSpeed": 109,
    "fuelCapacity": 22.5,
    "wheelCircumference": 2.95,
    "brakeIdleSpeed": 1.8,
    "canFloat": 0,
    "maxFordingDepth": 0,
    "waterSpeedFactor": 0.3,
    "waterResistance": 1,
    "waterResistanceCoef": 0.2,
    "waterLeakiness": 20,
    "switchTime": 0.5,
    "latency": 1,
    "changeGearType": "effective",
    "changeGearOmegaRatios": [1,0.294118,0.205882,0.147059,0.926471,0.470588,0.764706,0.352941,0.852941,0.5,1,0.647059],
    # Class: CfgVehicles\rhsusf_m1025_w\complexGearbox [Indent level: 1],
    "complexGearbox": {
        "GearboxRatios": ["R1",-3.07,"N",0,"D1",2.78,"D2",1.48,"D3",1,"D4",0.75],
        "TransmissionRatios": ["High",6],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R"
    },
    "differentialType": "all_limited",
    "frontRearSplit": 0.5,
    "frontBias": 2.7,
    "rearBias": 1.9,
    "centreBias": 1.5,
    "clutchStrength": 85,
    "transmissionLosses": 20,
    "dampingRateFullThrottle": 0.15,
    "dampingRateZeroThrottleClutchEngaged": 2.8,
    "dampingRateZeroThrottleClutchDisengaged": 0.35,
    "torqueCurve": [[0.191176,0.703518],[0.294118,0.778894],[0.411765,0.911223],[0.529412,1],[0.705882,0.976549],[0.764706,0.835846],[0.941176,0.79062],[1.05971,0]],
    "engineMOI": 7,
    "enginePower": 160,
    "peakTorque": 597,
    "minOmega": 41,
    "maxOmega": 356.05,
    "idleRPM": 650,
    "redRPM": 3400,
    "engineLosses": 12,
    "thrustDelay": 0.8,
    "engineBrakeCoef": 0.8,
    "antiRollbarForceCoef": 20,
    "antiRollbarForceLimit": 5.5,
    "antiRollbarSpeedMin": 10,
    "antiRollbarSpeedMax": 80,
    "accelAidForceYOffset": -1.25,
    # Class: CfgVehicles\rhsusf_m1025_w\Wheels [Indent level: 1],
    "Wheels": {
        # Class: CfgVehicles\rhsusf_m1025_w\Wheels\LF [Indent level: 2]
        "LF": {
            "side": "left",
            "boneName": "wheel_1_1_damper",
            "center": "axis_wheel_1_1",
            "boundary": "bound_wheel_1_1",
            "suspForceAppPointOffset": "axis_wheel_1_1",
            "tireForceAppPointOffset": "axis_wheel_1_1",
            "suspTravelDirection": [-0.125,-1,0],
            "steering": 1,
            "width": 0.25,
            "mass": 40,
            "MOI": 10,
            "dampingRate": 0.1,
            "maxBrakeTorque": 9000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.1,
            "maxDroop": 0.1,
            "sprungMass": -1,
            "springStrength": 58550,
            "springDamperRate": 7500,
            "longitudinalStiffnessPerUnitGravity": 7500,
            "latStiffX": 40,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Wheels\LR [Indent level: 2],
        "LR": {
            "boneName": "wheel_1_2_damper",
            "steering": 0,
            "center": "axis_wheel_3_1",
            "boundary": "bound_wheel_3_1",
            "suspForceAppPointOffset": "axis_wheel_3_1",
            "tireForceAppPointOffset": "axis_wheel_3_1",
            "maxHandBrakeTorque": 30000,
            "side": "left",
            "suspTravelDirection": [-0.125,-1,0],
            "width": 0.25,
            "mass": 40,
            "MOI": 10,
            "dampingRate": 0.1,
            "maxBrakeTorque": 9000,
            "maxCompression": 0.1,
            "maxDroop": 0.1,
            "sprungMass": -1,
            "springStrength": 58550,
            "springDamperRate": 7500,
            "longitudinalStiffnessPerUnitGravity": 7500,
            "latStiffX": 40,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Wheels\RF [Indent level: 2],
        "RF": {
            "boneName": "wheel_2_1_damper",
            "center": "axis_wheel_2_1",
            "boundary": "bound_wheel_2_1",
            "suspForceAppPointOffset": "axis_wheel_2_1",
            "tireForceAppPointOffset": "axis_wheel_2_1",
            "steering": 1,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": 0.25,
            "mass": 40,
            "MOI": 10,
            "dampingRate": 0.1,
            "maxBrakeTorque": 9000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.1,
            "maxDroop": 0.1,
            "sprungMass": -1,
            "springStrength": 58550,
            "springDamperRate": 7500,
            "longitudinalStiffnessPerUnitGravity": 7500,
            "latStiffX": 40,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Wheels\RR [Indent level: 2],
        "RR": {
            "boneName": "wheel_2_2_damper",
            "steering": 0,
            "center": "axis_wheel_4_1",
            "boundary": "bound_wheel_4_1",
            "suspForceAppPointOffset": "axis_wheel_4_1",
            "tireForceAppPointOffset": "axis_wheel_4_1",
            "maxHandBrakeTorque": 30000,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": 0.25,
            "mass": 40,
            "MOI": 10,
            "dampingRate": 0.1,
            "maxBrakeTorque": 9000,
            "maxCompression": 0.1,
            "maxDroop": 0.1,
            "sprungMass": -1,
            "springStrength": 58550,
            "springDamperRate": 7500,
            "longitudinalStiffnessPerUnitGravity": 7500,
            "latStiffX": 40,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,2.5],[0.5,2.3],[1,2]]
        }
    },
    "forceHideDriver": 1,
    "crewExplosionProtection": 0.95,
    # Class: CfgVehicles\rhsusf_m1025_w\UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles\rhsusf_m1025_w\UserActions\trunk_open [Indent level: 2]
        "trunk_open": {
            "displayName": "Open Trunk",
            "position": "trunk_action",
            "radius": 2,
            "onlyForplayer": 0,
            "condition": "this animationPhase 'ani_trunk_1'<0.5",
            "statement": "this animate ['ani_trunk_1', 1];"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\UserActions\trunk_close [Indent level: 2],
        "trunk_close": {
            "displayName": "Close Trunk",
            "condition": "this animationPhase 'ani_trunk_1'==1",
            "statement": "this animate ['ani_trunk_1', 0]",
            "position": "trunk_action",
            "radius": 2,
            "onlyForplayer": 0
        },
        # Class: CfgVehicles\rhsusf_m1025_w\UserActions\window_action [Indent level: 2],
        "window_action": {
            "userActionID": 101,
            "displayName": "Raise/Lower window",
            "position": "pos_driverpos",
            "radius": 14,
            "onlyForplayer": 0,
            "condition": "((call rhsusf_fnc_findPlayer) in this) AND ((gunner this) != (call rhsusf_fnc_findPlayer) )",
            "statement": "this call rhs_fnc_m1025_windowHandler"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\UserActions\door_action [Indent level: 2],
        "door_action": {
            "userActionID": 102,
            "displayName": "Door toggle",
            "condition": "((call rhsusf_fnc_findPlayer) in this)",
            "statement": "call rhs_fnc_m1025_doorToggle",
            "position": "pos_driverpos",
            "radius": 14,
            "onlyForplayer": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\UserActions\light_bo_off [Indent level: 2],
        "light_bo_off": {
            "displayName": "B.O. Light off",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyForplayer": 0,
            "condition": "(player == driver this) && this animationPhase 'light_bo'<0.5;",
            "statement": "this animate ['light_bo', 1];this animate ['light_brake_bo', 1]"
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\UserActions\light_bo_on [Indent level: 2],
        "light_bo_on": {
            "displayName": "B.O. Light on",
            "condition": "(player == driver this) && this animationPhase 'light_bo'==1;",
            "statement": "this animate ['light_bo', 0];this animate ['light_brake_bo', 0]",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyForplayer": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\UserActions\light_stop_off [Indent level: 2],
        "light_stop_off": {
            "displayName": "Stop Light off",
            "condition": "(player == driver this) && this animationPhase 'light_stop'<0.5",
            "statement": "this animate ['light_stop', 1]",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyForplayer": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\UserActions\light_stop_on [Indent level: 2],
        "light_stop_on": {
            "displayName": "Stop Light on",
            "condition": "(player == driver this) && this animationPhase 'light_stop'==1",
            "statement": "this animate ['light_stop', 0]",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyForplayer": 0
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\UserActions\lights_toggle [Indent level: 2],
        "lights_toggle": {
            "displayName": "Toggle short/long lights",
            "position": "",
            "shortcut": "vehLockTargets",
            "radius": 12,
            "priority": 1.5,
            "showWindow": 0,
            "onlyForplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)",
            "statement": "[this,2] call rhsusf_fnc_carLightToggle"
        }
    },
    # Class: CfgVehicles\rhsusf_m1025_w\TransportBackpacks [Indent level: 1],
    "TransportBackpacks": {
        # Class: CfgVehicles\rhsusf_m1025_w\TransportBackpacks\_xx_rhsusf_falconii [Indent level: 2]
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 2
        }
    },
    # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines [Indent level: 1],
    "TransportMagazines": {
        # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines\_xx_rhs_m136_hedp_mag [Indent level: 2]
        "_xx_rhs_m136_hedp_mag": {
            "magazine": "rhs_m136_hedp_mag",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines\_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2],
        "_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 20
        },
        # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines\_xx_rhsusf_100Rnd_556x45_soft_pouch [Indent level: 2],
        "_xx_rhsusf_100Rnd_556x45_soft_pouch": {
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch",
            "count": 8
        },
        # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines\_xx_rhs_mag_M441_HE [Indent level: 2],
        "_xx_rhs_mag_M441_HE": {
            "magazine": "rhs_mag_M441_HE",
            "count": 16
        },
        # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines\_xx_rhs_mag_M714_white [Indent level: 2],
        "_xx_rhs_mag_M714_white": {
            "magazine": "rhs_mag_M714_white",
            "count": 4
        },
        # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines\_xx_rhs_mag_M662_red [Indent level: 2],
        "_xx_rhs_mag_M662_red": {
            "magazine": "rhs_mag_M662_red",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines\_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 4
        },
        # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines\_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines\_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1025_w\TransportMagazines\_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 4
        }
    },
    # Class: CfgVehicles\rhsusf_m1025_w\TransportItems [Indent level: 1],
    "TransportItems": {
        # Class: CfgVehicles\rhsusf_m1025_w\TransportItems\_xx_FirstAidKit [Indent level: 2]
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 4
        }
    },
    # Class: CfgVehicles\rhsusf_m1025_w\TransportWeapons [Indent level: 1],
    "TransportWeapons": {
        # Class: CfgVehicles\rhsusf_m1025_w\TransportWeapons\_xx_rhs_weap_m4_carryhandle [Indent level: 2]
        "_xx_rhs_weap_m4_carryhandle": {
            "weapon": "rhs_weap_m4_carryhandle",
            "count": 2
        },
        # Class: CfgVehicles\rhsusf_m1025_w\TransportWeapons\_xx_rhs_weap_M136_hedp [Indent level: 2],
        "_xx_rhs_weap_M136_hedp": {
            "weapon": "rhs_weap_M136_hedp",
            "count": 2
        }
    },
    "transportSoldier": 0,
    "cargoAction": ["RHS_HMMWV_Cargo","RHS_HMMWV_Cargo","RHS_HMMWV_Cargo"],
    "memoryPointsGetInCargo": ["pos_cargo_RF","pos_cargo_RB","pos_cargo_LB"],
    "memoryPointsGetInCargoDir": ["pos_cargo_RF_dir","pos_cargo_RB_dir","pos_cargo_LB_dir"],
    "cargoProxyIndexes": [],
    "getInProxyOrder": [1,2,3],
    # Class: CfgVehicles\rhsusf_m1025_w\Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\ObjectTexture [Indent level: 2]
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\rhs_decalMask [Indent level: 2],
        "rhs_decalMask": {
            "displayName": "Define 1st decal",
            "tooltip": "Define decal located on mask & rear of vehicle",
            "property": "rhs_decalMask",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ [_this,'unitdecals_1',_value] call rhs_fnc_hmmwv_setDecal}",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values\NoChange [Indent level: 4]
                "NoChange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values\blankdecal_ca [Indent level: 4],
                "blankdecal_ca": {
                    "name": "Empty",
                    "value": "82ndab_505reg_1stbn_e25_w_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values\82ndab_505reg_1stbn_e25_w_ca [Indent level: 4],
                "82ndab_505reg_1stbn_e25_w_ca": {
                    "name": "82nd AB 505 regiment, 1st BN, E25 - Woodland",
                    "value": "82ndab_505reg_1stbn_e25_w_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values\82ndab_505reg_1stbn_e25_d_ca [Indent level: 4],
                "82ndab_505reg_1stbn_e25_d_ca": {
                    "name": "82nd AB 505 regiment, 1st BN, E25 - Desert",
                    "value": "82ndab_505reg_1stbn_e25_d_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values\test_1stbn_e25_w_ca [Indent level: 4],
                "test_1stbn_e25_w_ca": {
                    "name": "82nd AB 505 regiment, 1st BN, E25",
                    "value": "test_1stbn_e25_w_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values\101stab_502reg_2ndbn_a12_w_co [Indent level: 4],
                "101stab_502reg_2ndbn_a12_w_co": {
                    "name": "101st AB 502 regiment, 2nd BN, A12 - Woodland",
                    "value": "82ndab_505reg_1stbn_e25_w_ca",
                    "defaultValue": "101stab_502reg_2ndbn_a12_w_co"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values\101stab_502reg_2ndbn_a12_d_co [Indent level: 4],
                "101stab_502reg_2ndbn_a12_d_co": {
                    "name": "101st AB 502 regiment, 2nd BN, A12 - Desert",
                    "value": "101stab_502reg_2ndbn_a12_d_co"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values\1stcav_1stbn_12th_e25_w_ca [Indent level: 4],
                "1stcav_1stbn_12th_e25_w_ca": {
                    "name": "1st Cavalry Div, 2nd Battalion, 12th Cavalry 'Thunder Horse' - Woodland",
                    "value": "1stcav_1stbn_12th_e25_w_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values\1stcav_1stbn_12th_e25_d_ca [Indent level: 4],
                "1stcav_1stbn_12th_e25_d_ca": {
                    "name": "1st Cavalry Div, 2nd Battalion, 12th Cavalry 'Thunder Horse' - Desert",
                    "value": "1stcav_1stbn_12th_e25_d_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalMask\values\usmc_210321_ca [Indent level: 4],
                "usmc_210321_ca": {
                    "name": "USMC 210321",
                    "value": "usmc_210321_ca"
                }
            }
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\rhs_decalDoors [Indent level: 2],
        "rhs_decalDoors": {
            "displayName": "Define 2nd decal",
            "tooltip": "Define decals located on doors & vehicle rear",
            "property": "rhs_decalDoors",
            "expression": "if(_value != 'NoChange')then{ [_this,'unitdecals_2',_value] call rhs_fnc_hmmwv_setDecal}",
            # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\NoChange [Indent level: 4]
                "NoChange": {
                    "name": "Default defined",
                    "value": "NoChange"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\blankdecal_ca [Indent level: 4],
                "blankdecal_ca": {
                    "name": "Empty",
                    "value": "blankdecal_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\militarypolice_b_ca [Indent level: 4],
                "militarypolice_b_ca": {
                    "name": "Military Police",
                    "value": "militarypolice_b_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\e25_ca [Indent level: 4],
                "e25_ca": {
                    "name": "E25^",
                    "value": "e25arr_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\e23_ca [Indent level: 4],
                "e23_ca": {
                    "name": "E23^",
                    "value": "e23arr_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\a12_co [Indent level: 4],
                "a12_co": {
                    "name": "A12^",
                    "value": "a12arr_co"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\55_co [Indent level: 4],
                "55_co": {
                    "name": "55^",
                    "value": "55arr_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\05_co [Indent level: 4],
                "05_co": {
                    "name": "05^",
                    "value": "05arr_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\arr_co [Indent level: 4],
                "arr_co": {
                    "name": "^",
                    "value": "arr_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\down_ca [Indent level: 4],
                "down_ca": {
                    "name": "Arrow down",
                    "value": "downarr_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\pol_isaf_v1_ca [Indent level: 4],
                "pol_isaf_v1_ca": {
                    "name": "Polish - ISAF v1",
                    "value": "pol_isaf_v1_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\pol_isaf_v2_ca [Indent level: 4],
                "pol_isaf_v2_ca": {
                    "name": "Polish - ISAF v2",
                    "value": "pol_isaf_v2_ca"
                },
                # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_decalDoors\values\pol_isaf_v3_ca [Indent level: 4],
                "pol_isaf_v3_ca": {
                    "name": "Polish - ISAF v3",
                    "value": "pol_isaf_v3_ca"
                }
            },
            "control": "Combo",
            "defaultValue": 0,
            "typeName": "STRING"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\rhs_hideCIP [Indent level: 2],
        "rhs_hideCIP": {
            "displayName": "Hide CIP",
            "property": "rhs_hideCIP",
            "control": "CheckboxNumber",
            "expression": "_this animate ['hide_CIP',_value,true]",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\rhs_hideBFT [Indent level: 2],
        "rhs_hideBFT": {
            "displayName": "Hide BFT",
            "property": "rhs_hideBFT",
            "expression": "_this animate ['hide_BFT',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\rhs_hideAntennas [Indent level: 2],
        "rhs_hideAntennas": {
            "displayName": "Hide antennas",
            "property": "rhs_hideBFT",
            "expression": "_this animate ['hide_Antenna',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\rhs_hideA2Parts [Indent level: 2],
        "rhs_hideA2Parts": {
            "displayName": "Hide A2 parts",
            "property": "rhs_hideA2Parts",
            "expression": "_this animate ['hide_A2_Parts',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\Door_LF [Indent level: 2],
        "Door_LF": {
            "displayName": "Open front left door",
            "property": "Door_LF",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\ani_window_1 [Indent level: 2],
        "ani_window_1": {
            "displayName": "Open front left window",
            "property": "ani_window_1",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\Door_RF [Indent level: 2],
        "Door_RF": {
            "displayName": "Open front right door",
            "property": "Door_RF",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\ani_window_2 [Indent level: 2],
        "ani_window_2": {
            "displayName": "Open front right window",
            "property": "ani_window_2",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\Door_LB [Indent level: 2],
        "Door_LB": {
            "displayName": "Open back left door",
            "property": "Door_LB",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\ani_window_3 [Indent level: 2],
        "ani_window_3": {
            "displayName": "Open back left window",
            "property": "ani_window_3",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\Door_RB [Indent level: 2],
        "Door_RB": {
            "displayName": "Open back right door",
            "property": "Door_RB",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\ani_window_4 [Indent level: 2],
        "ani_window_4": {
            "displayName": "Open back right window",
            "property": "ani_window_4",
            "expression": "_this animateDoor ['%s',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_m1025_w\Attributes\ani_trunk_1 [Indent level: 2],
        "ani_trunk_1": {
            "displayName": "Open trunk",
            "property": "ani_trunk_1",
            "expression": "_this animate ['%s',_value,true]",
            "control": "Slider",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Attributes\rhs_HideA2Bumper [Indent level: 2],
        "rhs_HideA2Bumper": {
            "displayName": "switch to old bumper",
            "property": "rhs_HideA2Bumper",
            "expression": "_this animateSource ['Hide_A2Bumper',_value,true]",
            "control": "CheckboxNumber",
            "defaultValue": "0"
        }
    },
    # Class: CfgVehicles\rhsusf_m1025_w\EventHandlers [Indent level: 1],
    "EventHandlers": {
        # Class: CfgVehicles\rhsusf_m1025_w\EventHandlers\rhs_m1025_eh [Indent level: 2]
        "rhs_m1025_eh": {
            "getOut": "_this call rhs_fnc_m1025_doorHandler"
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
    "soundAttenuationCargo": [1],
    # Class: CfgVehicles\rhsusf_m998_w_4dr_fulltop\Sounds [Indent level: 1],
    "Sounds": {
        # Class: CfgVehicles\rhsusf_m998_w_4dr_fulltop\Sounds\RainIn [Indent level: 2]
        "RainIn": {
            "sound": ["rhsusf|addons|rhsusf_sounds|misc|rain.wss",1.41254,1],
            "frequency": 1,
            "volume": "rain*(1-camPos)"
        },
        # Class: CfgVehicles\rhsusf_m998_w_4dr_fulltop\Sounds\RainExt [Indent level: 2],
        "RainExt": {
            "sound": ["rhsusf|addons|rhsusf_sounds|misc|rain.wss",1.41254,1],
            "frequency": 1,
            "volume": "rain*camPos"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Idle_ext [Indent level: 2],
        "Idle_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_idle",0.398107,1,150],
            "frequency": "0.95	+	((rpm/	3400) factor[(604/	3400),(1058/	3400)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	3400) factor[(453/	3400),(831/	3400)])	*	((rpm/	3400) factor[(1360/	3400),(982/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine [Indent level: 2],
        "Engine": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_low1",0.446684,1,250],
            "frequency": "0.9	+	((rpm/	3400) factor[(1058/	3400),(1587/	3400)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3400) factor[(1058/	3400),(1360/	3400)])	*	((rpm/	3400) factor[(1738/	3400),(1511/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine1_ext [Indent level: 2],
        "Engine1_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_low2",0.562341,1,300],
            "frequency": "0.9	+		((rpm/	3400) factor[(1587/	3400),(2116/	3400)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3400) factor[(1436/	3400),(1738/	3400)])	*	((rpm/	3400) factor[(2267/	3400),(1889/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine2_ext [Indent level: 2],
        "Engine2_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_mid",0.707946,1,350],
            "frequency": "0.9	+	((rpm/	3400) factor[(2116/	3400),(2720/	3400)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	3400) factor[(1889/	3400),(2342/	3400)])	*	((rpm/	3400) factor[(2569/	3400),(2796/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine3_ext [Indent level: 2],
        "Engine3_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_high",1,1,400],
            "frequency": "0.95	+	((rpm/	3400) factor[(2720/	3400),(3400/	3400)])*0.1",
            "volume": "engineOn*camPos*((rpm/	3400) factor[(2871/	3400),(3400/	3400)])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\IdleThrust [Indent level: 2],
        "IdleThrust": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_exhaust_idle",0.562341,1,200],
            "frequency": "0.95	+	((rpm/	3400) factor[(604/	3400),(1058/	3400)])*0.15",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3400) factor[(453/	3400),(831/	3400)])	*	((rpm/	3400) factor[(1360/	3400),(982/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\EngineThrust [Indent level: 2],
        "EngineThrust": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_exhaust_low1",0.707946,1,350],
            "frequency": "0.9	+	((rpm/	3400) factor[(1058/	3400),(1587/	3400)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3400) factor[(1058/	3400),(1360/	3400)])	*	((rpm/	3400) factor[(1738/	3400),(1511/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine1_Thrust_ext [Indent level: 2],
        "Engine1_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_exhaust_low2",0.891251,1,400],
            "frequency": "0.9	+		((rpm/	3400) factor[(1587/	3400),(2116/	3400)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3400) factor[(1436/	3400),(1738/	3400)])	*	((rpm/	3400) factor[(2267/	3400),(1889/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine2_Thrust_ext [Indent level: 2],
        "Engine2_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_exhaust_mid",1.12202,1,425],
            "frequency": "0.9	+	((rpm/	3400) factor[(2116/	3400),(2720/	3400)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3400) factor[(1889/	3400),(2342/	3400)])	*	((rpm/	3400) factor[(3400/	3400),(2796/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine3_Thrust_ext [Indent level: 2],
        "Engine3_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_ext_exhaust_high",1.25893,1,450],
            "frequency": "0.95	+	((rpm/	3400) factor[(2720/	3400),(3400/	3400)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	3400) factor[(2871/	3400),(3400/	3400)])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Idle_int [Indent level: 2],
        "Idle_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_idle",0.251189,1],
            "frequency": "0.95	+	((rpm/	3400) factor[(604/	3400),(1058/	3400)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	3400) factor[(453/	3400),(831/	3400)])	*	((rpm/	3400) factor[(1360/	3400),(982/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine_int [Indent level: 2],
        "Engine_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_low1",0.316228,1],
            "frequency": "0.9	+	((rpm/	3400) factor[(1058/	3400),(1587/	3400)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3400) factor[(1058/	3400),(1360/	3400)])	*	((rpm/	3400) factor[(1738/	3400),(1511/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine1_int [Indent level: 2],
        "Engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_low2",0.398107,1],
            "frequency": "0.9	+		((rpm/	3400) factor[(1587/	3400),(2116/	3400)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3400) factor[(1436/	3400),(1738/	3400)])	*	((rpm/	3400) factor[(2267/	3400),(1889/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine2_int [Indent level: 2],
        "Engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_mid",0.501187,1],
            "frequency": "0.9	+	((rpm/	3400) factor[(2116/	3400),(2720/	3400)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	3400) factor[(1889/	3400),(2342/	3400)])	*	((rpm/	3400) factor[(3400/	3400),(2796/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine3_int [Indent level: 2],
        "Engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_high",0.630957,1],
            "frequency": "0.95	+	((rpm/	3400) factor[(2720/	3400),(3400/	3400)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	3400) factor[(2871/	3400),(3400/	3400)])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\IdleThrust_int [Indent level: 2],
        "IdleThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_exhaust_idle",0.354813,1],
            "frequency": "0.95	+	((rpm/	3400) factor[(604/	3400),(1058/	3400)])*0.15",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3400) factor[(453/	3400),(831/	3400)])	*	((rpm/	3400) factor[(1360/	3400),(982/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\EngineThrust_int [Indent level: 2],
        "EngineThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_exhaust_low1",0.446684,1],
            "frequency": "0.9	+	((rpm/	3400) factor[(1058/	3400),(1587/	3400)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3400) factor[(1058/	3400),(1360/	3400)])	*	((rpm/	3400) factor[(1738/	3400),(1511/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine1_Thrust_int [Indent level: 2],
        "Engine1_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_exhaust_low2",0.562341,1],
            "frequency": "0.9	+		((rpm/	3400) factor[(1587/	3400),(2116/	3400)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3400) factor[(1436/	3400),(1738/	3400)])	*	((rpm/	3400) factor[(2267/	3400),(1889/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine2_Thrust_int [Indent level: 2],
        "Engine2_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_exhaust_mid",0.707946,1],
            "frequency": "0.9	+	((rpm/	3400) factor[(2116/	3400),(2720/	3400)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	3400) factor[(1889/	3400),(2342/	3400)])	*	((rpm/	3400) factor[(3400/	3400),(2796/	3400)]))"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\Engine3_Thrust_int [Indent level: 2],
        "Engine3_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|soft|MRAP_01|MRAP_01_int_exhaust_high",0.794328,1],
            "frequency": "0.95	+	((rpm/	3400) factor[(2720/	3400),(3400/	3400)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	3400) factor[(2116/	3400),(3400/	3400)])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresRockOut [Indent level: 2],
        "TiresRockOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_1",1.41254,1,60],
            "frequency": "1",
            "volume": "camPos*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresSandOut [Indent level: 2],
        "TiresSandOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-sand1",1.41254,1,60],
            "frequency": "1",
            "volume": "camPos*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresGrassOut [Indent level: 2],
        "TiresGrassOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_dirt_soft_2",1.25893,1,60],
            "frequency": "1",
            "volume": "camPos*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresMudOut [Indent level: 2],
        "TiresMudOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext-tires-mud2",1.12202,1,60],
            "frequency": "1",
            "volume": "camPos*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresGravelOut [Indent level: 2],
        "TiresGravelOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_gravel_1",1.25893,1,60],
            "frequency": "1",
            "volume": "camPos*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresAsphaltOut [Indent level: 2],
        "TiresAsphaltOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|ext_tires_asfalt_2",1.12202,1,60],
            "frequency": "1",
            "volume": "camPos*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\NoiseOut [Indent level: 2],
        "NoiseOut": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_ext_car_3",1.12202,1,90],
            "frequency": "1",
            "volume": "camPos*(damper0 max 0.02)*(speed factor[0, 8])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresRockIn [Indent level: 2],
        "TiresRockIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_1",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*rock*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresSandIn [Indent level: 2],
        "TiresSandIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-sand2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*sand*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresGrassIn [Indent level: 2],
        "TiresGrassIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_dirt_soft_2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*grass*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresMudIn [Indent level: 2],
        "TiresMudIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int-tires-mud2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*mud*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresGravelIn [Indent level: 2],
        "TiresGravelIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_gravel_1",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*gravel*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\TiresAsphaltIn [Indent level: 2],
        "TiresAsphaltIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|tires|int_tires_asfalt_2",0.707946,1],
            "frequency": "1",
            "volume": "(1-camPos)*asphalt*(speed factor[2, 20])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\NoiseIn [Indent level: 2],
        "NoiseIn": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|noise_int_car_3",0.562341,1],
            "frequency": "1",
            "volume": "(damper0 max 0.1)*(speed factor[0, 8])*(1-camPos)"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\breaking_ext_road [Indent level: 2],
        "breaking_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 10])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\acceleration_ext_road [Indent level: 2],
        "acceleration_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\turn_left_ext_road [Indent level: 2],
        "turn_left_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\turn_right_ext_road [Indent level: 2],
        "turn_right_ext_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02",0.707946,1,80],
            "frequency": 1,
            "volume": "engineOn*camPos*asphalt*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\breaking_ext_dirt [Indent level: 2],
        "breaking_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_14_dirt_breaking",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 10])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\acceleration_ext_dirt [Indent level: 2],
        "acceleration_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|acceleration_dirt_ext_1",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\turn_left_ext_dirt [Indent level: 2],
        "turn_left_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\turn_right_ext_dirt [Indent level: 2],
        "turn_right_ext_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt",0.707946,1,60],
            "frequency": 1,
            "volume": "engineOn*camPos*(1-asphalt)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\breaking_int_road [Indent level: 2],
        "breaking_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_04_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 6])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\acceleration_int_road [Indent level: 2],
        "acceleration_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\turn_left_int_road [Indent level: 2],
        "turn_left_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\turn_right_int_road [Indent level: 2],
        "turn_right_int_road": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_loop_02_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*asphalt*(1-camPos)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\breaking_int_dirt [Indent level: 2],
        "breaking_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_14_dirt_breaking_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[-0.15, -0.3])*(Speed Factor[2, 6])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\acceleration_int_dirt [Indent level: 2],
        "acceleration_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|acceleration_dirt_int_1",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(LongSlipDrive Factor[0.15, 0.3])*(Speed Factor[10, 0])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\turn_left_int_dirt [Indent level: 2],
        "turn_left_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[0.15, 0.3])*(Speed Factor[0, 10])"
        },
        # Class: CfgVehicles\rhsusf_hmmwe_base\Sounds\turn_right_int_dirt [Indent level: 2],
        "turn_right_int_dirt": {
            "sound": ["A3|Sounds_F|vehicles|soft|noises|slipping_tires_18_dirt_int",0.630957,1],
            "frequency": 1,
            "volume": "engineOn*(1-asphalt)*(1-camPos)*(latSlipDrive Factor[-0.15, -0.3])*(Speed Factor[0, 10])"
        }
    },
    "driverDoor": "Door_LF",
    "cargoDoors": ["Door_RF","Door_RB","Door_LB"],
    "side": 1,
    "scope": 2,
    "typicalCargo": ["rhsusf_army_ocp_driver"],
    # Class: CfgVehicles\rhsusf_m998_w_2dr\Library [Indent level: 1],
    "Library": {
        "libTextDesc": "M998, 1-1/4 ton, cargo carrier, wood (open)"
    },
    "damperSize": 0.15,
    "damperForce": 1,
    "damperDamping": 1,
    "selectionBrakeLights": "light_brake",
    "selectionBackLights": "light_drive",
    "driverAction": "RHS_HMMWV_Driver",
    "driverInAction": "RHS_HMMWV_Driver",
    "memoryPointsGetInCoDriver": "pos_codriver",
    "memoryPointsGetInCoDriverDir": "pos_codriver_dir",
    "memoryPointsGetInDriver": "pos_driver",
    "memoryPointsGetInDriverDir": "pos_driver_dir",
    "cargoCompartments": [1,2],
    "transportMaxBackpacks": 7,
    "castDriverShadow": 1,
    "castCargoShadow": 1,
    # Class: CfgVehicles\rhsusf_m998_w_2dr\Damage [Indent level: 1],
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_hmmwv|textures|A2_parts.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|A2_parts_half_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|rhs_destr_hmmwv.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_4drcargo.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_exterior_half_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|rhs_destr_hmmwv.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_exterior.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_exterior_half_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|rhs_destr_hmmwv.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m1025.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m1025_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|rhs_destr_hmmwv.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_mainbody.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_mainbody.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|rhs_destr_hmmwv.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_interior.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_interior_half_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|rhs_destr_hmmwv.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|wheel_wranglermt.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|wheel_wranglermt_half_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|wheel_wranglermt_full_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|wheel_wranglermt_tire.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|wheel_wranglermt_tire_half_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|wheel_wranglermt_tire_full_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_windows.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_windows_half_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_windows_half_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_tarpwindows.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_tarpwindows_half_d.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|m998_tarpwindows_half_d.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","rhsusf|addons|rhsusf_hmmwv|textures|rhs_destr_hmmwv.rvmat"]
    },
    # Class: CfgVehicles\rhsusf_m998_w_2dr\RenderTargets [Indent level: 1],
    "RenderTargets": {
        # Class: CfgVehicles\rhsusf_m998_w_2dr\RenderTargets\LeftMirror [Indent level: 2]
        "LeftMirror": {
            "renderTarget": "rendertarget0",
            # Class: CfgVehicles\rhsusf_m998_w_2dr\RenderTargets\LeftMirror\CameraView1 [Indent level: 3],
            "CameraView1": {
                "pointPosition": "m1p",
                "pointDirection": "m1d",
                "renderQuality": 2,
                "renderVisionMode": 4,
                "fov": 0.7
            },
            "BBoxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\RenderTargets\RightMirror [Indent level: 2],
        "RightMirror": {
            "renderTarget": "rendertarget1",
            # Class: CfgVehicles\rhsusf_m998_w_2dr\RenderTargets\RightMirror\CameraView1 [Indent level: 3],
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
    # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Left [Indent level: 2]
        "Left": {
            "color": [800,900,650],
            "ambient": [2,2,2],
            "position": "light_hd_1",
            "direction": "light_hd_1_dir",
            "hitpoint": "light_hd_1",
            "selection": "light_hd_1",
            "size": 1,
            "innerAngle": 30,
            "outerAngle": 100,
            "coneFadeCoef": 5,
            "intensity": 2.5,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Left_Flare [Indent level: 2],
        "Left_Flare": {
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Left_Flare\Attenuation [Indent level: 3],
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
            "position": "light_hd_1",
            "direction": "light_hd_1_dir",
            "hitpoint": "light_hd_1",
            "selection": "light_hd_1",
            "size": 1,
            "dayLight": 0,
            "flareSize": 0.85
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Right [Indent level: 2],
        "Right": {
            "position": "light_hd_2",
            "direction": "light_hd_2_dir",
            "hitpoint": "light_hd_2",
            "selection": "light_hd_2",
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "innerAngle": 30,
            "outerAngle": 100,
            "coneFadeCoef": 5,
            "intensity": 2.5,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Right_Flare [Indent level: 2],
        "Right_Flare": {
            "useFlare": 1,
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Right_Flare\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "position": "light_hd_2",
            "direction": "light_hd_2_dir",
            "hitpoint": "light_hd_2",
            "selection": "light_hd_2",
            "color": [800,900,650],
            "ambient": [2,2,2],
            "size": 1,
            "dayLight": 0,
            "flareSize": 0.85
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Long_Left [Indent level: 2],
        "Long_Left": {
            "color": [800,900,650],
            "ambient": [5,5,5],
            "position": "Light_L_Long",
            "direction": "Light_L_Long_end",
            "hitpoint": "light_hd_1",
            "selection": "light_hd_1",
            "size": 1,
            "innerAngle": 22,
            "outerAngle": 29,
            "coneFadeCoef": 1,
            "intensity": 100,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750,
            # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Long_Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Long_Right [Indent level: 2],
        "Long_Right": {
            "position": "Light_R_Long",
            "direction": "Light_R_Long_end",
            "hitpoint": "light_hd_2",
            "selection": "light_hd_2",
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
            # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Long_Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Long_Right2 [Indent level: 2],
        "Long_Right2": {
            "useFlare": 1,
            "position": "light_R_Long_flare",
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Long_Right2\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "direction": "Light_R_Long_end",
            "hitpoint": "light_hd_2",
            "selection": "light_hd_2",
            "color": [800,900,650],
            "ambient": [5,5,5],
            "size": 1,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750
        },
        # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Long_Left2 [Indent level: 2],
        "Long_Left2": {
            "useFlare": 1,
            "position": "light_L_Long_flare",
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles\rhsusf_m998_w_2dr\Reflectors\Long_Left2\Attenuation [Indent level: 3],
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
            "hitpoint": "light_hd_1",
            "selection": "light_hd_1",
            "size": 1,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750
        }
    },
    "aggregateReflectors": [["Left","Right"]],
    # Class: CfgVehicles\rhsusf_m998_w_2dr\NVGMarkers [Indent level: 1],
    "NVGMarkers": {
        # Class: CfgVehicles\rhsusf_m998_w_2dr\NVGMarkers\NVGMarker01 [Indent level: 2]
        "NVGMarker01": {
            "name": "nvg_marker",
            "color": [0.03,0.003,0.003,1],
            "ambient": [0.003,0.0003,0.0003,1],
            "brightness": 0.001,
            "blinking": 1
        }
    },
    "dlc": "RHS_USAF",
    "category": "Car",
    "insideSoundCoef": 0.4,
    "tf_hasLRradio_api": 1,
    "crewVulnerable": 1,
    "armor": 80,
    "minTotalDamageThreshold": 0.21,
    "fuelExplosionPower": 0.1,
    "secondaryExplosion": 0,
    "camShakeCoef": 0.4,
    "selectionDamage": "damage",
    "getInAction": "GetInLow",
    "getOutAction": "GetOutLow",
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "slingLoadCargoMemoryPoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "driverLeftHandAnimName": "steeringwheel",
    "driverRightHandAnimName": "steeringwheel",
    "driverRightLegAnimName": "pedalR",
    "driverLeftLegAnimName": "pedalL",
    "showNVGDriver": 1,
    "showNVGCargo": [1],
    "viewDriverInExternal": 1,
    "gunnerHasFlares": 0,
    "mapSize": 5.5,
    "extCameraPosition": [0.5,2,-10],
    "supplyRadius": 2,
    "hideUnitInfo": 0,
    # Class: CfgVehicles\rhsusf_hmmwe_base\Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles\rhsusf_hmmwe_base\Exhausts\exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaust1_1",
            "direction": "exhaust1_2",
            "effect": "ExhaustsEffect"
        }
    },
    # Class: CfgVehicles\rhsusf_hmmwe_base\Components [Indent level: 1],
    "Components": {
        # Class: CfgVehicles\rhsusf_hmmwe_base\Components\AICarSteeringComponent [Indent level: 2]
        "AICarSteeringComponent": {
            "steeringPIDWeights": [3.1,0.1,0.4],
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
            "steeringAngleCoef": 1.2,
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
    "ace_refuel_fuelCapacity": 95,
    "soundGetIn": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|handling|getin|mrap_1.ogg",0.5,1],
    "soundGetOut": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|handling|getout|mrap_1.ogg",0.5,1,40],
    "soundDammage": [".ogg",0.5,1],
    "soundEngineOnInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_01|mrap_01_start_int.ogg",1,1],
    "soundEngineOffInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_01|mrap_01_shut_int.ogg",1,1],
    "soundEngineOnExt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_01|mrap_01_start_ext.ogg",1,1,125],
    "soundEngineOffExt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_01|mrap_01_shut_ext.ogg",1,1,100],
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
    "features": "Randomization: No						<br />Camo selections: 2 - the body, wheels and cover						<br />Script door sources: Door_LF, Door_RF, Door_LB, Door_RB						<br />Script animations: None						<br />Executed scripts: None						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: 1 to 3",
    "_generalMacro": "MRAP_01_base_F",
    "editorSubcategory": "EdSubcat_Cars",
    "crewCrashProtection": 1.35,
    "enableRadio": 1,
    "enableGPS": 1,
    "armorStructural": 5,
    "cost": 500000,
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "wheelDamageThreshold": 0.18,
    "wheelDamageRadiusCoef": 0.75,
    "wheelDestroyRadiusCoef": 0.48,
    "sensorPosition": "sensorPos",
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 1,
    "smokeLauncherGrenadeCount": 8,
    "smokeLauncherVelocity": 14,
    "smokeLauncherOnTurret": 0,
    "smokeLauncherAngle": 360,
    "weapons": ["TruckHorn2"],
    "magazines": [],
    "changeGearMinEffectivity": [0.95,0.15,0.95,0.95,0.95,0.95,0.95],
    "tf_hasLRradio": 1,
    "tf_isolatedAmount": 0.7,
    "ace_cookoff_engineSmokeOffset": [0,-2,0],
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
    "dammageHalf": [],
    "dammageFull": [],
    "explosionShielding": 1,
    "steerAheadSimul": 0.5,
    "steerAheadPlan": 0.35,
    "predictTurnPlan": 2,
    "predictTurnSimul": 1.5,
    "epeImpulseDamageCoef": 15,
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
    "holdOffroadFormation": 1,
    "viewCargoShadowDiff": 1,
    "viewCargoShadowAmb": 1,
    "accuracy": 0.25,
    "audible": 5,
    "soundEnviron": ["",0.000562341,1],
    "soundCrash": ["A3|sounds_f|dummysound",1,1],
    "soundGear": ["",1e-005,1],
    "collisionEffect": "collisionEffect",
    "htMin": 60,
    "htMax": 1800,
    "afMax": 100,
    "mfMax": 80,
    "mFact": 1,
    "tBody": 150,
    "transportMaxWeapons": 12,
    "transportMaxMagazines": 64,
    "maximumLoad": 2000,
    "memoryPointSupply": "doplnovani",
    "brakeTorque": 6000,
    "longStiff": 15000,
    "latStiffX": 2000,
    "latStiffY": 18000,
    "wheelMask": "wheel_X_X",
    "numberPhysicalWheels": 4,
    "maxGForce": 3,
    # Class: CfgVehicles\Car_F\camShakeGForce [Indent level: 1],
    "camShakeGForce": {
        "power": 2,
        "frequency": 60,
        "distance": 0,
        "minSpeed": 60
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
    "armorLights": 0.4,
    "preferRoads": 1,
    "unitInfoType": "RscUnitInfo",
    "formationX": 20,
    "formationZ": 20,
    "type": 0,
    "scudModel": "",
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
    "memoryPointsGetInDriverPrecise": "pos driver",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
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
    "slowSpeedForwardCoef": 0.3,
    "enableManualFire": 1,
    "portrait": "",
    "ghostPreview": "",
    "destrType": "DestructDefault",
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
    "waterLinearDampingCoefX": 0,
    "waterLinearDampingCoefY": 0,
    "waterAngularDampingCoef": 0,
    "showNVGCommander": 0,
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
    "driverCompartments": "Compartment1",
    "driverOpticsModel": "",
    "driverOpticsEffect": [],
    "driverOpticsColor": [1,1,1,1],
    "hideProxyInCombat": 0,
    "canHideDriver": -1,
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