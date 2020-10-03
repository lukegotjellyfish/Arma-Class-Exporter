rhs_mag_fab250 = {
    "model": "rhsafrf|addons|rhs_a2port_air|data|rhs_pylon_m_fab250",
    "scope": 2,
    # Ammo: rhs_ammo_fab250,
    "ammo": {
        "ammo": "rhs_ammo_fab250",
        "hit": 5000,
        "indirectHit": 1140,
        "indirectHitRange": 15,
        "dangerRadiusHit": 1250,
        "suppressionRadiusHit": 100,
        "model": "rhsafrf|addons|rhs_a2port_air|data|rhs_m_fab250",
        "proxyShape": "rhsafrf|addons|rhs_a2port_air|data|rhs_m_fab250",
        "cost": 50,
        "flightProfiles": ["Direct"],
        # Class: CfgAmmo\rhs_ammo_fab100\Direct,
        "Direct": {
        },
        "explosionForceCoef": 10,
        "irLock": 0,
        "laserLock": 0,
        "allowAgainstInfantry": 1,
        "autoSeekTarget": 0,
        "aiAmmoUsageFlags": "64 + 128 + 512",
        "weaponLockSystem": 1,
        "soundFakeFall0": ["a3|Sounds_F|weapons|falling_bomb|fall_01",3.16228,1,1000],
        "soundFakeFall1": ["a3|Sounds_F|weapons|falling_bomb|fall_02",3.16228,1,1000],
        "soundFakeFall2": ["a3|Sounds_F|weapons|falling_bomb|fall_03",3.16228,1,1000],
        "soundFakeFall3": ["a3|Sounds_F|weapons|falling_bomb|fall_04",3.16228,1,1000],
        "soundFakeFall": ["soundFakeFall0",0.25,"soundFakeFall1",0.25,"soundFakeFall2",0.25,"soundFakeFall3",0.25],
        # Class: CfgAmmo\rhs_ammo_fab100\Components,
        "Components": {
            # Class: CfgAmmo\rhs_ammo_fab100\Components\SensorsManagerComponent
            "SensorsManagerComponent": {
                # Class: CfgAmmo\rhs_ammo_fab100\Components\SensorsManagerComponent\Components
                "Components": {
                }
            }
        },
        "maverickWeaponIndexOffset": 8,
        "SoundSetExplosion": ["BombsHeavy_Exp_SoundSet","BombsHeavy_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "maneuvrability": 10,
        "fuseDistance": 50,
        "trackLead": 0.95,
        "trackOversteer": 1,
        "airFriction": 0.06,
        "sideAirFriction": 0.12,
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
        "lockSeekRadius": 500,
        "cmImmunity": 0.3,
        # Class: CfgAmmo\ammo_Bomb_LaserGuidedBase\LoalAltitude,
        "LoalAltitude": {
            "lockSeekAltitude": 500
        },
        "maxControlRange": 100000,
        "simulation": "shotMissile",
        "maxSpeed": 100,
        "timeToLive": 120,
        "initTime": 0,
        "thrustTime": 0,
        "thrust": 0,
        "access": 3,
        "underwaterHitRangeCoef": 1,
        "typicalSpeed": 900,
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
        # Class: CfgAmmo\Default\HitEffects,
        "HitEffects": {
            "vehicle": "ImpactMetal",
            "object": "ImpactConcrete"
        },
        "suppressionRadiusBulletClose": -1,
        "dangerRadiusBulletClose": -1,
        "caliber": 1,
        "whistleOnFire": 0,
        # Class: CfgAmmo\Default\NVGMarkers,
        "NVGMarkers": {
        },
        "minDamageForCamShakeHit": 0.55,
        # Class: CfgAmmo\Default\EventHandlers,
        "EventHandlers": {
        },
    },
    "count": 1,
    "displayname": "FAB-250",
    "displayNameShort": "HE",
    "initspeed": 0,
    "maxleadspeed": 5,
    "namesound": "",
    "hardpoints": ["RHS_HP_FAB250"],
    "pylonWeapon": "rhs_weap_fab250",
    "weight": 266,
    "mass": 266,
    # Class: CfgMagazines\rhs_mag_fab250\mfdElements,
    "mfdElements": {
        # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_ammoname
        "rhs_rus_ammoname": {
            # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_ammoname\Bones
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_ammoname\Draw,
            "Draw": {
                # Ammo: PylonSelected
                "condition": {
                    "condition": "PylonSelected"
                },
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_ammoname\Draw\PylonText1,
                "PylonText1": {
                    # Ammo: text
                    "type": {
                        "type": "text"
                    },
                    # Ammo: static,
                    "source": {
                        "source": "static",
                    },
                    # Ammo: АБ250,
                    "text": {
                        "text": "АБ250",
                    },
                    "scale": 1,
                    "sourceScale": 1,
                    # Ammo: center,
                    "align": {
                        "align": "center",
                    },
                    "pos": [[-0.005,0.02],1],
                    "right": [[0.045,0.02],1],
                    "down": [[-0.005,0.065],1]
                }
            }
        },
        # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_ammoname_right,
        "rhs_rus_ammoname_right": {
            # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_ammoname_right\Bones
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_ammoname_right\Draw,
            "Draw": {
                # Ammo: PylonSelected
                "condition": {
                    "condition": "PylonSelected"
                },
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_ammoname_right\Draw\PylonText1,
                "PylonText1": {
                    # Ammo: text
                    "type": {
                        "type": "text"
                    },
                    # Ammo: static,
                    "source": {
                        "source": "static",
                    },
                    # Ammo: АБ250,
                    "text": {
                        "text": "АБ250",
                    },
                    "scale": 1,
                    "sourceScale": 1,
                    # Ammo: right,
                    "align": {
                        "align": "right",
                    },
                    "pos": [[-0.005,0.02],1],
                    "right": [[0.045,0.02],1],
                    "down": [[-0.005,0.065],1]
                }
            }
        },
        # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_su25_box,
        "rhs_su25_box": {
            # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_su25_box\Bones
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_su25_box\Draw,
            "Draw": {
                "condition": "1-pylonMagazineEmpty",
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_su25_box\Draw\Shape,
                "Shape": {
                    "type": "polygon",
                    "width": 4,
                    "points": [[[[-0.022,-0.04],1],[[0.022,-0.04],1],[[0.022,0.04],1],[[-0.022,0.04],1]]]
                },
                # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_su25_box\Draw\Selected,
                "Selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.58,0.23,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_su25_box\Draw\Selected\Shape,
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.022,0.18],1],[[0.022,0.18],1],[[0.022,0.26],1],[[-0.022,0.26],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle,
        "rhs_rus_circle": {
            # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Bones
            "Bones": {
                # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Bones\Center
                "Center": {
                    "type": "fixed",
                    "pos": [0,0]
                }
            },
            # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw,
            "Draw": {
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Default,
                "Default": {
                    "condition": "1-PylonSelected-pylonMagazineEmpty",
                    "color": [1,1,1],
                    # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Default\PylonText1,
                    "PylonText1": {
                        "type": "text",
                        "source": "static",
                        "text": "АБ250",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Default\Shape,
                    "Shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0169708],1],["Center",[0.0075,-0.0146967],1],["Center",[0.01299,-0.0084854],1],["Center",[0.015,0],1],["Center",[0.01299,0.0084854],1],["Center",[0.0075,0.0146967],1],["Center",[0,0.0169708],1],["Center",[-0.0075,0.0146967],1],["Center",[-0.01299,0.0084854],1],["Center",[-0.015,0],1],["Center",[-0.01299,-0.0084854],1],["Center",[-0.0075,-0.0146967],1],["Center",[0,-0.0169708],1],[],["Center",[0.0106066,-0.0120002],1],["Center",[0.0176777,-0.0200003],1],[],["Center",[0.0106066,0.0120002],1],["Center",[0.0176777,0.0200003],1],[],["Center",[-0.0106066,0.0120002],1],["Center",[-0.0176777,0.0200003],1],[],["Center",[-0.0106066,-0.0120002],1],["Center",[-0.0176777,-0.0200003],1],[]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Selected,
                "Selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Selected\PylonText1,
                    "PylonText1": {
                        "type": "text",
                        "source": "static",
                        "text": "АБ250",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Selected\Shape,
                    "Shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0169708],1],["Center",[0.0075,-0.0146967],1],["Center",[0.01299,-0.0084854],1],["Center",[0.015,0],1],["Center",[0.01299,0.0084854],1],["Center",[0.0075,0.0146967],1],["Center",[0,0.0169708],1],["Center",[-0.0075,0.0146967],1],["Center",[-0.01299,0.0084854],1],["Center",[-0.015,0],1],["Center",[-0.01299,-0.0084854],1],["Center",[-0.0075,-0.0146967],1],["Center",[0,-0.0169708],1],[],["Center",[0.0106066,-0.0120002],1],["Center",[0.0176777,-0.0200003],1],[],["Center",[0.0106066,0.0120002],1],["Center",[0.0176777,0.0200003],1],[],["Center",[-0.0106066,0.0120002],1],["Center",[-0.0176777,0.0200003],1],[],["Center",[-0.0106066,-0.0120002],1],["Center",[-0.0176777,-0.0200003],1],[]]
                    },
                    # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Selected\Polygon,
                    "Polygon": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[["Center",1,[0,0],1],["Center",[0.0106066,-0.0120002],1],["Center",[0.015,7.41817e-010],1],["Center",[0.0106066,0.0120002],1]],[["Center",1,[0,0],1],["Center",[0.0106066,0.0120002],1],["Center",[-1.31134e-009,0.0169708],1],["Center",[-0.0106066,0.0120002],1]],[["Center",1,[0,0],1],["Center",[-0.0106066,0.0120002],1],["Center",[-0.015,-2.02375e-010],1],["Center",[-0.0106066,-0.0120002],1]],[["Center",1,[0,0],1],["Center",[-0.0106066,-0.0120002],1],["Center",[2.62268e-009,-0.0169708],1],["Center",[0.0106066,-0.0120002],1]]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Empty,
                "Empty": {
                    "condition": "pylonMagazineEmpty",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Empty\PylonText1,
                    "PylonText1": {
                        "type": "text",
                        "source": "static",
                        "text": "АБ250",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Empty\Shape,
                    "Shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0169708],1],["Center",[0.0075,-0.0146967],1],["Center",[0.01299,-0.0084854],1],["Center",[0.015,0],1],["Center",[0.01299,0.0084854],1],["Center",[0.0075,0.0146967],1],["Center",[0,0.0169708],1],["Center",[-0.0075,0.0146967],1],["Center",[-0.01299,0.0084854],1],["Center",[-0.015,0],1],["Center",[-0.01299,-0.0084854],1],["Center",[-0.0075,-0.0146967],1],["Center",[0,-0.0169708],1],[],["Center",[0.0106066,-0.0120002],1],["Center",[0.0176777,-0.0200003],1],[],["Center",[0.0106066,0.0120002],1],["Center",[0.0176777,0.0200003],1],[],["Center",[-0.0106066,0.0120002],1],["Center",[-0.0176777,0.0200003],1],[],["Center",[-0.0106066,-0.0120002],1],["Center",[-0.0176777,-0.0200003],1],[]]
                    },
                    # Class: CfgMagazines\rhs_mag_fab250\mfdElements\rhs_rus_circle\Draw\Empty\Polygon,
                    "Polygon": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[["Center",1,[0,0],1],["Center",[0.0106066,-0.0120002],1],["Center",[0.015,7.41817e-010],1],["Center",[0.0106066,0.0120002],1]],[["Center",1,[0,0],1],["Center",[0.0106066,0.0120002],1],["Center",[-1.31134e-009,0.0169708],1],["Center",[-0.0106066,0.0120002],1]],[["Center",1,[0,0],1],["Center",[-0.0106066,0.0120002],1],["Center",[-0.015,-2.02375e-010],1],["Center",[-0.0106066,-0.0120002],1]],[["Center",1,[0,0],1],["Center",[-0.0106066,-0.0120002],1],["Center",[2.62268e-009,-0.0169708],1],["Center",[0.0106066,-0.0120002],1]]]
                    },
                    "alpha": 0.22
                }
            }
        }
    },
    "author": "Bohemia Interactive",
    "type": 0,
    "reloadAction": "",
    "weaponPoolAvailable": 0,
    "value": 1,
    "picture": "",
    "modelSpecial": "",
    "useAction": 0,
    "useActionTitle": "",
    "selectionFireAnim": "zasleh",
    "simulation": "ProxyMagazines",
    # Class: CfgMagazines\Default\InventoryPlacements,
    "InventoryPlacements": {
    },
    # Class: CfgMagazines\Default\Library,
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
    "maxThrowHoldTime": 2,
    "minThrowIntensityCoef": 0.3,
    "maxThrowIntensityCoef": 1.4,
    "quickReload": 0,
}