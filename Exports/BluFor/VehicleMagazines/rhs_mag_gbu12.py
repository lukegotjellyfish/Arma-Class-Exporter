rhs_mag_gbu12 = {
    "count": 1,
    "displayName": "GBU-12",
    "descriptionShort": "500lb Paveway II",
    # Ammo: rhs_ammo_gbu12,
    "ammo": {
        "ammo": "rhs_ammo_gbu12",
        "model": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_b_gbu12_fly",
        "proxyShape": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_b_gbu12",
        "initTime": 0.2,
        "maverickWeaponIndexOffset": 8,
        "SoundSetExplosion": ["BombsHeavy_Exp_SoundSet","BombsHeavy_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "hit": 5000,
        "indirectHit": 1100,
        "indirectHitRange": 12,
        "maneuvrability": 10,
        "fuseDistance": 50,
        "trackLead": 0.95,
        "trackOversteer": 1,
        "airFriction": 0.06,
        "sideAirFriction": 0.12,
        "aiAmmoUsageFlags": "128 + 512",
        "dangerRadiusHit": 1000,
        "suppressionRadiusHit": 120,
        "craterEffects": "BombCrater",
        "explosionEffects": "BombExplosion",
        "explosionSoundEffect": "DefaultExplosion",
        "explosionTime": 2,
        "multiSoundHit": ["soundHit1",0.2,"soundHit2",0.2,"soundHit3",0.2,"soundHit4",0.2,"soundHit5",0.2],
        "soundHit1": ["|A3|Sounds_F|weapons|Explosion|expl_big_1",2.51189,1,2400],
        "soundHit2": ["|A3|Sounds_F|weapons|Explosion|expl_big_2",2.51189,1,2400],
        "soundHit3": ["|A3|Sounds_F|weapons|Explosion|expl_big_3",2.51189,1,2400],
        "soundHit4": ["|A3|Sounds_F|weapons|Explosion|expl_shell_1",2.51189,1,2400],
        "soundHit5": ["|A3|Sounds_F|weapons|Explosion|expl_shell_2",2.51189,1,2400],
        "whistleDist": 24,
        "missileLockCone": 120,
        "missileKeepLockedCone": 120,
        "missileLockMaxDistance": 5000,
        "missileLockMinDistance": 100,
        "missileLockMaxSpeed": 30,
        "autoSeekTarget": 1,
        "lockSeekRadius": 500,
        "weaponLockSystem": 4,
        "cmImmunity": 0.3,
        "flightProfiles": ["LoalAltitude"],
        # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\LoalAltitude [Indent level: 1],
        "LoalAltitude": {
            "lockSeekAltitude": 500
        },
        # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\Components [Indent level: 1],
        "Components": {
            # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\Components\SensorsManagerComponent [Indent level: 2]
            "SensorsManagerComponent": {
                # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\Components\SensorsManagerComponent\Components [Indent level: 3]
                "Components": {
                    # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\Components\SensorsManagerComponent\Components\NVSensorComponent [Indent level: 4]
                    "NVSensorComponent": {
                        # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\Components\SensorsManagerComponent\Components\NVSensorComponent\AirTarget [Indent level: 5]
                        "AirTarget": {
                            "minRange": 500,
                            "maxRange": 5000,
                            "objectDistanceLimitCoef": -1,
                            "viewDistanceLimitCoef": 1
                        },
                        # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\Components\SensorsManagerComponent\Components\NVSensorComponent\GroundTarget [Indent level: 5],
                        "GroundTarget": {
                            "minRange": 500,
                            "maxRange": 5000,
                            "objectDistanceLimitCoef": 1,
                            "viewDistanceLimitCoef": 1
                        },
                        "maxTrackableSpeed": 30,
                        "angleRangeHorizontal": 120,
                        "angleRangeVertical": 120,
                        "componentType": "NVSensorComponent",
                        "color": [1,1,1,0],
                        "typeRecognitionDistance": 0,
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
                    # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\Components\SensorsManagerComponent\Components\LaserSensorComponent [Indent level: 4],
                    "LaserSensorComponent": {
                        # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\Components\SensorsManagerComponent\Components\LaserSensorComponent\AirTarget [Indent level: 5]
                        "AirTarget": {
                            "minRange": 5000,
                            "maxRange": 5000,
                            "objectDistanceLimitCoef": -1,
                            "viewDistanceLimitCoef": -1
                        },
                        # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\Components\SensorsManagerComponent\Components\LaserSensorComponent\GroundTarget [Indent level: 5],
                        "GroundTarget": {
                            "minRange": 5000,
                            "maxRange": 5000,
                            "objectDistanceLimitCoef": -1,
                            "viewDistanceLimitCoef": -1
                        },
                        "maxTrackableSpeed": 30,
                        "angleRangeHorizontal": 120,
                        "angleRangeVertical": 120,
                        "componentType": "LaserSensorComponent",
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
                        "minTrackableATL": -1e+010,
                        "maxTrackableATL": 1e+010
                    }
                }
            }
        },
        "cost": 20000,
        "irLock": 0,
        "laserLock": 1,
        "maxControlRange": 100000,
        "simulation": "shotMissile",
        "maxSpeed": 100,
        "timeToLive": 120,
        "thrustTime": 0,
        "thrust": 0,
        "access": 3,
        "underwaterHitRangeCoef": 1,
        "typicalSpeed": 900,
        "explosionForceCoef": 1,
        "isCraterOriented": 0,
        "craterShape": "",
        "weaponType": "Default",
        "animated": 0,
        "shadow": 0,
        "cartridge": "",
        "simulationStep": 0.05,
        "tracerColor": [0.7,0.7,0.5,0.04],
        "tracerColorR": [0.7,0.7,0.5,0.04],
        "soundFly": ["",1,1],
        "soundEngine": ["",1,1],
        "soundHit": ["",1,1],
        "supersonicCrackNear": ["",1,1],
        "supersonicCrackFar": ["",1,1],
        "soundFall": ["",1,1],
        "soundFakeFall": ["soundFall",1],
        "hitGroundSoft": ["soundHit",1],
        "hitGroundHard": ["soundHit",1],
        "hitMan": ["soundHit",1],
        "hitArmor": ["soundHit",1],
        "hitIron": ["soundHit",1],
        "hitBuilding": ["soundHit",1],
        "hitFoliage": ["soundHit",1],
        "hitWood": ["soundHit",1],
        "hitGlass": ["soundHit",1],
        "hitGlassArmored": ["soundHit",1],
        "hitConcrete": ["soundHit",1],
        "hitRubber": ["soundHit",1],
        "hitPlastic": ["soundHit",1],
        "hitDefault": ["soundHit",1],
        "hitMetal": ["soundHit",1],
        "hitMetalplate": ["soundHit",1],
        "hitTyre": ["soundHit",1],
        "hitWater": ["soundHit",1],
        "soundImpact": ["",1,1],
        "impactGroundSoft": ["soundImpact",1],
        "impactGroundHard": ["soundImpact",1],
        "impactMan": ["soundImpact",1],
        "impactIron": ["soundImpact",1],
        "impactArmor": ["soundImpact",1],
        "impactBuilding": ["soundImpact",1],
        "impactFoliage": ["soundImpact",1],
        "impactWood": ["soundImpact",1],
        "impactGlass": ["soundImpact",1],
        "impactGlassArmored": ["soundImpact",1],
        "impactConcrete": ["soundImpact",1],
        "impactRubber": ["soundImpact",1],
        "impactPlastic": ["soundImpact",1],
        "impactDefault": ["soundImpact",1],
        "impactMetal": ["soundImpact",1],
        "impactMetalplate": ["soundImpact",1],
        "impactTyre": ["soundImpact",1],
        "impactWater": ["soundImpact",1],
        "grenadeFireSound": [],
        "grenadeBurningSound": [],
        "deflecting": 0,
        "deflectionSlowDown": 0.8,
        "explosive": 1,
        "craterWaterEffects": "ImpactEffectsWater",
        "effectsMissile": "ExplosionEffects",
        "effectsMissileInit": "",
        "effectsSmoke": "SmokeShellWhite",
        "effectsFire": "CannonFire",
        "effectFlare": "FlareShell",
        "effectFly": "",
        "mineJumpEffects": "",
        "waterEffectOffset": 0.45,
        "directionalExplosion": 0,
        "explosionAngle": 60,
        "explosionDir": "explosionDir",
        "explosionPos": "explosionPos",
        "explosionEffectsDir": "explosionDir",
        "minimumSafeZone": 0.1,
        "soundTrigger": [],
        "soundActivation": [],
        "soundDeactivation": [],
        "minTimeToLive": 0,
        "airLock": 0,
        "nvLock": 0,
        "artilleryLock": 0,
        "hitOnWater": 0,
        "manualControl": 0,
        "lockType": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "visibleFire": 0,
        "audibleFire": 0,
        "shootDistraction": -1,
        "visibleFireTime": 0,
        "icon": "",
        "submunitionAmmo": "",
        "explosionType": "explosive",
        "mineTrigger": "RangeTrigger",
        "mineBoundingTime": 3,
        "mineBoundingDist": 3,
        "mineInconspicuousness": 10,
        "mineFloating": -1,
        "mineDiveSpeed": 1,
        "minePlaceDist": 0.5,
        # Class: CfgAmmo\Default\HitEffects [Indent level: 1],
        "HitEffects": {
            "vehicle": "ImpactMetal",
            "object": "ImpactConcrete"
        },
        "suppressionRadiusBulletClose": -1,
        "dangerRadiusBulletClose": -1,
        "caliber": 1,
        "whistleOnFire": 0,
        # Class: CfgAmmo\Default\NVGMarkers [Indent level: 1],
        "NVGMarkers": {
        },
        "minDamageForCamShakeHit": 0.55,
        # Class: CfgAmmo\Default\EventHandlers [Indent level: 1],
        "EventHandlers": {
        },
    },
        "EventHandlers": "rhs_ammo_gbu12",
    "model": "A3|Weapons_F|DynamicLoadout|PylonMissile_1x_Bomb_02_F.p3d",
    "hardpoints": ["RHS_HP_LGB_500"],
    "pylonWeapon": "rhs_weap_gbu12",
    "displayNameMFDFormat": "GBU12|%1",
    # Class: CfgMagazines\rhs_mag_gbu12\mfdElements [Indent level: 1],
    "mfdElements": {
        # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_ammoname [Indent level: 2]
        "rhs_a10a_ammoname": {
            # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_ammoname\Bones [Indent level: 3]
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_ammoname\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_ammoname\Draw\PylonText1 [Indent level: 4],
                "PylonText1": {
                    # Ammo: text
                    "type": {
                        "type": "text"
                    }
                        "type": "text",
                    # Ammo: static,
                    "source": {
                        "source": "static",
                    },
                        "source": "static",
                    # Ammo: GBU,
                    "text": {
                        "text": "GBU",
                    },
                        "text": "GBU",
                    "scale": 1,
                    "sourceScale": 1,
                    # Ammo: center,
                    "align": {
                        "align": "center",
                    },
                        "align": "center",
                    "pos": [[0.005,0.02],1],
                    "right": [[0.05,0.02],1],
                    "down": [[0.005,0.105],1]
                }
            }
        },
        # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_box [Indent level: 2],
        "rhs_a10a_box": {
            # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_box\Bones [Indent level: 3]
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_box\Draw [Indent level: 3],
            "Draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_box\Draw\Default [Indent level: 4],
                "Default": {
                    "condition": "PylonAmmoRelative>=0.001",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_box\Draw\Default\Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,-0.04],1],[[0.015,-0.04],1],[[0.015,0.04],1],[[-0.015,0.04],1]]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_box\Draw\Selected [Indent level: 4],
                "Selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_box\Draw\Selected\Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,0.05],1],[[0.015,0.05],1],[[0.015,0.13],1],[[-0.015,0.13],1]]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_box\Draw\Empty [Indent level: 4],
                "Empty": {
                    "condition": "PylonAmmoRelative<=0",
                    "color": [0.87,0,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\rhs_a10a_box\Draw\Empty\Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.02,0.05],1],[[0.05,0.05],1],[[0.05,0.13],1],[[0.02,0.13],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD [Indent level: 2],
        "RHS_A29_Weap_MFD": {
            # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD\Bones [Indent level: 3]
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD\Draw [Indent level: 3],
            "Draw": {
                # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD\Draw\BackgroundGroup [Indent level: 4]
                "BackgroundGroup": {
                    "color": [0,0,0],
                    # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD\Draw\BackgroundGroup\Background [Indent level: 5],
                    "Background": {
                        "type": "polygon",
                        "points": [[[[-0.02,-0.08],1],[[0.03,-0.08],1],[[0.03,0.06],1],[[-0.02,0.06],1]]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD\Draw\Default [Indent level: 4],
                "Default": {
                    "condition": "PylonAmmoRelative>0",
                    "color": [0,0.12,0],
                    # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD\Draw\Default\Shape [Indent level: 5],
                    "Shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.00825,0.0265625],1],[[0.0123125,0.0265625],1],[],[[-0.0051875,0.0265625],1],[[-0.001125,0.0265625],1],[],[[-0.0105,-0.0575],1],[[0.017625,-0.0575],1],[],[[-0.0105,0.00749999],1],[[0.017625,0.00749999],1],[],[[-0.000812501,0.050625],1],[[-0.000812501,0.0178125],1],[[0.0016875,0.01625],1],[[0.0035625,0.015625],1],[[0.00825,0.02],1],[[0.007625,0.0503125],1],[],[[0.0035625,0.0578125],1],[[0.0066875,0.0565625],1],[[0.007625,0.0534375],1],[[0.007625,0.0503125],1],[[0.0210625,0.055],1],[[0.0210625,0.0303125],1],[[0.0123125,0.0265625],1],[[0.017625,0.0078125],1],[[0.017625,-0.056875],1],[[0.017625,-0.0646875],1],[[0.0160625,-0.070625],1],[[0.0141875,-0.0740625],1],[[0.0110625,-0.076875],1],[[0.0079375,-0.0784375],1],[[0.0035625,-0.0790625],1],[[-0.000812501,-0.0784375],1],[[-0.00393751,-0.0765625],1],[[-0.0070625,-0.07375],1],[[-0.0089375,-0.0703125],1],[[-0.0105,-0.0646875],1],[[-0.0105,-0.056875],1],[[-0.0105,0.0078125],1],[[-0.0051875,0.0265625],1],[[-0.013625,0.030625],1],[[-0.013625,0.054375],1],[[-0.000812501,0.050625],1],[[0.0035625,0.0578125],1]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD\Draw\Selected [Indent level: 4],
                "Selected": {
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "color": [0.99,0.94,0.59],
                    # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD\Draw\Selected\Shape [Indent level: 5],
                    "Shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.00825,0.0265625],1],[[0.0123125,0.0265625],1],[],[[-0.0051875,0.0265625],1],[[-0.001125,0.0265625],1],[],[[-0.0105,-0.0575],1],[[0.017625,-0.0575],1],[],[[-0.0105,0.00749999],1],[[0.017625,0.00749999],1],[],[[-0.000812501,0.050625],1],[[-0.000812501,0.0178125],1],[[0.0016875,0.01625],1],[[0.0035625,0.015625],1],[[0.00825,0.02],1],[[0.007625,0.0503125],1],[],[[0.0035625,0.0578125],1],[[0.0066875,0.0565625],1],[[0.007625,0.0534375],1],[[0.007625,0.0503125],1],[[0.0210625,0.055],1],[[0.0210625,0.0303125],1],[[0.0123125,0.0265625],1],[[0.017625,0.0078125],1],[[0.017625,-0.056875],1],[[0.017625,-0.0646875],1],[[0.0160625,-0.070625],1],[[0.0141875,-0.0740625],1],[[0.0110625,-0.076875],1],[[0.0079375,-0.0784375],1],[[0.0035625,-0.0790625],1],[[-0.000812501,-0.0784375],1],[[-0.00393751,-0.0765625],1],[[-0.0070625,-0.07375],1],[[-0.0089375,-0.0703125],1],[[-0.0105,-0.0646875],1],[[-0.0105,-0.056875],1],[[-0.0105,0.0078125],1],[[-0.0051875,0.0265625],1],[[-0.013625,0.030625],1],[[-0.013625,0.054375],1],[[-0.000812501,0.050625],1],[[0.0035625,0.0578125],1]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD\Draw\Empty [Indent level: 4],
                "Empty": {
                    "condition": "PylonAmmoRelative <= 0",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD\Draw\Empty\Shape [Indent level: 5],
                    "Shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.00825,0.0265625],1],[[0.0123125,0.0265625],1],[],[[-0.0051875,0.0265625],1],[[-0.001125,0.0265625],1],[],[[-0.0105,-0.0575],1],[[0.017625,-0.0575],1],[],[[-0.0105,0.00749999],1],[[0.017625,0.00749999],1],[],[[-0.000812501,0.050625],1],[[-0.000812501,0.0178125],1],[[0.0016875,0.01625],1],[[0.0035625,0.015625],1],[[0.00825,0.02],1],[[0.007625,0.0503125],1],[],[[0.0035625,0.0578125],1],[[0.0066875,0.0565625],1],[[0.007625,0.0534375],1],[[0.007625,0.0503125],1],[[0.0210625,0.055],1],[[0.0210625,0.0303125],1],[[0.0123125,0.0265625],1],[[0.017625,0.0078125],1],[[0.017625,-0.056875],1],[[0.017625,-0.0646875],1],[[0.0160625,-0.070625],1],[[0.0141875,-0.0740625],1],[[0.0110625,-0.076875],1],[[0.0079375,-0.0784375],1],[[0.0035625,-0.0790625],1],[[-0.000812501,-0.0784375],1],[[-0.00393751,-0.0765625],1],[[-0.0070625,-0.07375],1],[[-0.0089375,-0.0703125],1],[[-0.0105,-0.0646875],1],[[-0.0105,-0.056875],1],[[-0.0105,0.0078125],1],[[-0.0051875,0.0265625],1],[[-0.013625,0.030625],1],[[-0.013625,0.054375],1],[[-0.000812501,0.050625],1],[[0.0035625,0.0578125],1]]
                    }
                }
            }
        },
        # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD_Inventory [Indent level: 2],
        "RHS_A29_Weap_MFD_Inventory": {
            # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD_Inventory\Bones [Indent level: 3]
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD_Inventory\Draw [Indent level: 3],
            "Draw": {
                # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD_Inventory\Draw\PylonText1 [Indent level: 4]
                "PylonText1": {
                    "type": "text",
                    "source": "static",
                    "text": "GBU-12",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0,0.02],1],
                    "right": [[0.025,0.02],1],
                    "down": [[0,0.04],1]
                },
                # Class: CfgMagazines\rhs_mag_gbu12\mfdElements\RHS_A29_Weap_MFD_Inventory\Draw\PylonText2 [Indent level: 4],
                "PylonText2": {
                    "type": "text",
                    "source": "static",
                    "text": "LOAL",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0,0.054],1],
                    "right": [[0.025,0.054],1],
                    "down": [[0,0.074],1]
                }
            }
        }
    },
    "author": "Bohemia Interactive",
    "scope": 2,
    "displayNameShort": "Bomb",
    "initSpeed": 0,
    "maxLeadSpeed": 25,
    "nameSound": "cannon",
    "type": 0,
    "reloadAction": "",
    "weaponPoolAvailable": 0,
    "value": 1,
    "picture": "",
    "modelSpecial": "",
    "useAction": 0,
    "useActionTitle": "",
    "selectionFireAnim": "zasleh",
    "mass": 8,
    "simulation": "ProxyMagazines",
    "weight": 0,
    # Class: CfgMagazines\Default\InventoryPlacements [Indent level: 1],
    "InventoryPlacements": {
    },
    # Class: CfgMagazines\Default\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "maxThrowHoldTime": 2,
    "minThrowIntensityCoef": 0.3,
    "maxThrowIntensityCoef": 1.4,
    "quickReload": 0,
}