rhs_mag_b8m1_s8kom = {
    # Ammo: rhs_ammo_s8    "ammo": {        "ammo": "rhs_ammo_s8"        "AIAmmoUsageFlags": "64+128+512"        "cost": 100        "initTime": 0.02        "sideAirFriction": 0.003        "proxyShape": "A3|Weapons_F_EPC|Ammo|Rocket_03_HE_F.p3d"        "model": "A3|Weapons_F_EPC|Ammo|Rocket_03_HE_fly_F.p3d"        "effectsMissile": "RHS_Rocket_Fired"        "effectsMissileInit": "RHS_Rocket_Init"        "soundFly": ["A3|Sounds_F|weapons|Rockets|rocket_fly_2",1,1.5,700]        "submunitionAmmo": "rhs_ammo_s8_penetrator"        "submunitionDirectionType": "SubmunitionModelDirection"        "submunitionInitialOffset": [0,0,-0.2]        "submunitionParentSpeedCoef": 0        "submunitionInitSpeed": 1000        "triggerOnImpact": 1        "deleteParentWhenTriggered": 0        "missileLockMaxDistance": 4000        "missileLockMinDistance": 700        "hit": 400        "indirectHit": 60        "indirectHitRange": 15        "warheadName": "HE"        "maxSpeed": 590        "thrustTime": 0.69        "thrust": 1060        "airFriction": 0.09        "fuseDistance": 50        "whistleDist": 30        "timeToLive": 15        "muzzleEffect": ""        "simulation": "shotMissile"        # Class: CfgAmmo\R_80mm_HE\CamShakeExplode        "CamShakeExplode": {            "power": 16,            "duration": 1.8,            "frequency": 20,            "distance": 191.554
        }        # Class: CfgAmmo\R_80mm_HE\CamShakeHit        "CamShakeHit": {            "power": 80,            "duration": 0.6,            "frequency": 20,            "distance": 1
        }        # Class: CfgAmmo\R_80mm_HE\CamShakeFire        "CamShakeFire": {            "power": 2.9907,            "duration": 1.8,            "frequency": 20,            "distance": 71.5542
        }        # Class: CfgAmmo\R_80mm_HE\CamShakePlayerFire        "CamShakePlayerFire": {            "power": 2,            "duration": 0.1,            "frequency": 20,            "distance": 1
        }        "SoundSetExplosion": ["RocketsMedium_Exp_SoundSet","RocketsMedium_Tail_SoundSet","Explosion_Debris_SoundSet"]        "dangerRadiusHit": -1        "suppressionRadiusHit": 30        "soundHit": ["A3|Sounds_F|weapons|Rockets|explosion_missile_02",2.51189,1,2500]        "explosionSoundEffect": "DefaultExplosion"        "soundEngine": ["",1,1,20]        "supersonicCrackNear": ["",1,1,50]        "supersonicCrackFar": ["",1,1,150]        "CraterEffects": "HERocketCrater"        "explosionEffects": "HERocketExplosion"        # Class: CfgAmmo\RocketBase\HitEffects        "HitEffects": {            "hitWater": "ImpactEffectsWaterRocket"
        }        # Class: CfgAmmo\RocketBase\EventHandlers        "EventHandlers": {            # Class: CfgAmmo\RocketBase\EventHandlers\RHS_APS_FiredEH            "RHS_APS_FiredEH": {                "fired": "_this spawn rhs_fnc_aps_missileFired"
            }
        }        "simulationStep": 0.05        "maneuvrability": 0        "maxControlRange": 0        "visibleFire": 32        "audibleFire": 32        "visibleFireTime": 20        "deflecting": 5        "access": 3        "underwaterHitRangeCoef": 1        "typicalSpeed": 900        "explosionForceCoef": 1        "isCraterOriented": 0        "craterShape": ""        "weaponType": "Default"        "animated": 0        "shadow": 0        "cartridge": ""        "tracerColor": [0.7,0.7,0.5,0.04]        "tracerColorR": [0.7,0.7,0.5,0.04]        "soundFall": ["",1,1]        "soundFakeFall": ["soundFall",1]        "hitGroundSoft": ["soundHit",1]        "hitGroundHard": ["soundHit",1]        "hitMan": ["soundHit",1]        "hitArmor": ["soundHit",1]        "hitIron": ["soundHit",1]        "hitBuilding": ["soundHit",1]        "hitFoliage": ["soundHit",1]        "hitWood": ["soundHit",1]        "hitGlass": ["soundHit",1]        "hitGlassArmored": ["soundHit",1]        "hitConcrete": ["soundHit",1]        "hitRubber": ["soundHit",1]        "hitPlastic": ["soundHit",1]        "hitDefault": ["soundHit",1]        "hitMetal": ["soundHit",1]        "hitMetalplate": ["soundHit",1]        "hitTyre": ["soundHit",1]        "hitWater": ["soundHit",1]        "soundImpact": ["",1,1]        "impactGroundSoft": ["soundImpact",1]        "impactGroundHard": ["soundImpact",1]        "impactMan": ["soundImpact",1]        "impactIron": ["soundImpact",1]        "impactArmor": ["soundImpact",1]        "impactBuilding": ["soundImpact",1]        "impactFoliage": ["soundImpact",1]        "impactWood": ["soundImpact",1]        "impactGlass": ["soundImpact",1]        "impactGlassArmored": ["soundImpact",1]        "impactConcrete": ["soundImpact",1]        "impactRubber": ["soundImpact",1]        "impactPlastic": ["soundImpact",1]        "impactDefault": ["soundImpact",1]        "impactMetal": ["soundImpact",1]        "impactMetalplate": ["soundImpact",1]        "impactTyre": ["soundImpact",1]        "impactWater": ["soundImpact",1]        "grenadeFireSound": []        "grenadeBurningSound": []        "deflectionSlowDown": 0.8        "explosive": 1        "craterWaterEffects": "ImpactEffectsWater"        "effectsSmoke": "SmokeShellWhite"        "effectsFire": "CannonFire"        "effectFlare": "FlareShell"        "effectFly": ""        "mineJumpEffects": ""        "waterEffectOffset": 0.45        "directionalExplosion": 0        "explosionAngle": 60        "explosionDir": "explosionDir"        "explosionPos": "explosionPos"        "explosionEffectsDir": "explosionDir"        "minimumSafeZone": 0.1        "soundTrigger": []        "soundActivation": []        "soundDeactivation": []        "minTimeToLive": 0        "irLock": 0        "airLock": 0        "laserLock": 0        "nvLock": 0        "artilleryLock": 0        "hitOnWater": 0        "lockSeekRadius": 100        "manualControl": 0        "trackLead": 1        "trackOversteer": 1        "missileLockCone": 0        "weaponLockSystem": 0        "cmImmunity": 1        "lockType": 0        "maverickweaponIndexOffset": 0        "artilleryDispersion": 1        "artilleryCharge": 1        "autoSeekTarget": 0        "shootDistraction": -1        "explosionTime": 0        "icon": ""        "explosionType": "explosive"        "mineTrigger": "RangeTrigger"        "mineBoundingTime": 3        "mineBoundingDist": 3        "mineInconspicuousness": 10        "mineFloating": -1        "mineDiveSpeed": 1        "minePlaceDist": 0.5        "suppressionRadiusBulletClose": -1        "dangerRadiusBulletClose": -1        "caliber": 1        "whistleOnFire": 0        # Class: CfgAmmo\Default\NVGMarkers        "NVGMarkers": {
        }        "minDamageForCamShakeHit": 0.55    },
    "model": "rhsafrf|addons|rhs_airweapons|rhs_pylon_r_b8m1.p3d",
    "count": 20,
    "mass": 376,
    "weight": 376,
    "pylonWeapon": "rhs_weap_s8",
    "hardpoints": ["RHS_HP_B8M1"],
    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements,
    "mfdElements": {
        # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_ammoname
        "rhs_rus_ammoname": {
            # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_ammoname\Bones
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_ammoname\Draw,
            "Draw": {
                # Ammo: PylonSelected
                "condition": {
                    "condition": "PylonSelected"
                },
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_ammoname\Draw\PylonText1,
                "PylonText1": {
                    # Ammo: text
                    "type": {
                        "type": "text"
                    },
                    # Ammo: static,
                    "source": {
                        "source": "static",
                    },
                    # Ammo: С8КОМ,
                    "text": {
                        "text": "С8КОМ",
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
        # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_ammoname_right,
        "rhs_rus_ammoname_right": {
            # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_ammoname_right\Bones
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_ammoname_right\Draw,
            "Draw": {
                # Ammo: PylonSelected
                "condition": {
                    "condition": "PylonSelected"
                },
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_ammoname_right\Draw\PylonText1,
                "PylonText1": {
                    # Ammo: text
                    "type": {
                        "type": "text"
                    },
                    # Ammo: static,
                    "source": {
                        "source": "static",
                    },
                    # Ammo: С8КОМ,
                    "text": {
                        "text": "С8КОМ",
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
        # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_su25_box,
        "rhs_su25_box": {
            # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_su25_box\Bones
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_su25_box\Draw,
            "Draw": {
                "condition": "1-pylonMagazineEmpty",
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_su25_box\Draw\Shape,
                "Shape": {
                    "type": "polygon",
                    "width": 4,
                    "points": [[[[-0.022,-0.04],1],[[0.022,-0.04],1],[[0.022,0.04],1],[[-0.022,0.04],1]]]
                },
                # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_su25_box\Draw\Selected,
                "Selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.58,0.23,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_su25_box\Draw\Selected\Shape,
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.022,0.18],1],[[0.022,0.18],1],[[0.022,0.26],1],[[-0.022,0.26],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle,
        "rhs_rus_circle": {
            # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Bones
            "Bones": {
                # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Bones\Center
                "Center": {
                    "type": "fixed",
                    "pos": [0,0]
                }
            },
            # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw,
            "Draw": {
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Default,
                "Default": {
                    "condition": "1-PylonSelected-pylonMagazineEmpty",
                    "color": [1,1,1],
                    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Default\PylonValue1,
                    "PylonValue1": {
                        "type": "text",
                        "source": "pylonAmmo",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Default\PylonText1,
                    "PylonText1": {
                        "type": "text",
                        "source": "static",
                        "text": "С8КОМ",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.12],1],
                        "right": [[0.035,0.12],1],
                        "down": [[-0.005,0.16],1]
                    },
                    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Default\Shape,
                    "Shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0339416],1],["Center",[0.015,-0.0293934],1],["Center",[0.02598,-0.0169708],1],["Center",[0.03,0],1],["Center",[0.02598,0.0169708],1],["Center",[0.015,0.0293934],1],["Center",[0,0.0339416],1],["Center",[-0.015,0.0293934],1],["Center",[-0.02598,0.0169708],1],["Center",[-0.03,0],1],["Center",[-0.02598,-0.0169708],1],["Center",[-0.015,-0.0293934],1],["Center",[0,-0.0339416],1],[],["Center",[0.0137886,-0.0156002],1],["Center",[0.0116673,-0.0132002],1],[],["Center",[0.0195,9.64363e-010],1],["Center",[0.0165,8.15999e-010],1],[],["Center",[0.0137886,0.0156002],1],["Center",[0.0116673,0.0132002],1],[],["Center",[-1.70474e-009,0.022062],1],["Center",[-1.44248e-009,0.0186679],1],[],["Center",[-0.0137886,0.0156002],1],["Center",[-0.0116673,0.0132002],1],[],["Center",[-0.0195,-2.63087e-010],1],["Center",[-0.0165,-2.22612e-010],1],[],["Center",[-0.0137886,-0.0156002],1],["Center",[-0.0116673,-0.0132002],1],[],["Center",[3.40949e-009,-0.022062],1],["Center",[2.88495e-009,-0.0186679],1],[],["Center",[0.00742462,-0.00840012],1],["Center",[0.0053033,-0.00600008],1],[],["Center",[0.00742462,0.00840012],1],["Center",[0.0053033,0.00600008],1],[],["Center",[-0.00742462,0.00840012],1],["Center",[-0.0053033,0.00600009],1],[],["Center",[-0.00742462,-0.00840012],1],["Center",[-0.0053033,-0.00600008],1],[]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Selected,
                "Selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Selected\PylonText1,
                    "PylonText1": {
                        "type": "text",
                        "source": "static",
                        "text": "С8КОМ",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.12],1],
                        "right": [[0.035,0.12],1],
                        "down": [[-0.005,0.16],1]
                    },
                    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Selected\PylonValue1,
                    "PylonValue1": {
                        "type": "text",
                        "source": "pylonAmmo",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Selected\Shape,
                    "Shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0339416],1],["Center",[0.015,-0.0293934],1],["Center",[0.02598,-0.0169708],1],["Center",[0.03,0],1],["Center",[0.02598,0.0169708],1],["Center",[0.015,0.0293934],1],["Center",[0,0.0339416],1],["Center",[-0.015,0.0293934],1],["Center",[-0.02598,0.0169708],1],["Center",[-0.03,0],1],["Center",[-0.02598,-0.0169708],1],["Center",[-0.015,-0.0293934],1],["Center",[0,-0.0339416],1],[],["Center",[0.0137886,-0.0156002],1],["Center",[0.0116673,-0.0132002],1],[],["Center",[0.0195,9.64363e-010],1],["Center",[0.0165,8.15999e-010],1],[],["Center",[0.0137886,0.0156002],1],["Center",[0.0116673,0.0132002],1],[],["Center",[-1.70474e-009,0.022062],1],["Center",[-1.44248e-009,0.0186679],1],[],["Center",[-0.0137886,0.0156002],1],["Center",[-0.0116673,0.0132002],1],[],["Center",[-0.0195,-2.63087e-010],1],["Center",[-0.0165,-2.22612e-010],1],[],["Center",[-0.0137886,-0.0156002],1],["Center",[-0.0116673,-0.0132002],1],[],["Center",[3.40949e-009,-0.022062],1],["Center",[2.88495e-009,-0.0186679],1],[],["Center",[0.00742462,-0.00840012],1],["Center",[0.0053033,-0.00600008],1],[],["Center",[0.00742462,0.00840012],1],["Center",[0.0053033,0.00600008],1],[],["Center",[-0.00742462,0.00840012],1],["Center",[-0.0053033,0.00600009],1],[],["Center",[-0.00742462,-0.00840012],1],["Center",[-0.0053033,-0.00600008],1],[]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Empty,
                "Empty": {
                    "condition": "pylonMagazineEmpty",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Empty\PylonText1,
                    "PylonText1": {
                        "type": "text",
                        "source": "static",
                        "text": "С8КОМ",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.12],1],
                        "right": [[0.035,0.12],1],
                        "down": [[-0.005,0.16],1]
                    },
                    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Empty\PylonValue1,
                    "PylonValue1": {
                        "type": "text",
                        "source": "pylonAmmo",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines\rhs_mag_b8m1_s8kom\mfdElements\rhs_rus_circle\Draw\Empty\Shape,
                    "Shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0339416],1],["Center",[0.015,-0.0293934],1],["Center",[0.02598,-0.0169708],1],["Center",[0.03,0],1],["Center",[0.02598,0.0169708],1],["Center",[0.015,0.0293934],1],["Center",[0,0.0339416],1],["Center",[-0.015,0.0293934],1],["Center",[-0.02598,0.0169708],1],["Center",[-0.03,0],1],["Center",[-0.02598,-0.0169708],1],["Center",[-0.015,-0.0293934],1],["Center",[0,-0.0339416],1],[],["Center",[0.0137886,-0.0156002],1],["Center",[0.0116673,-0.0132002],1],[],["Center",[0.0195,9.64363e-010],1],["Center",[0.0165,8.15999e-010],1],[],["Center",[0.0137886,0.0156002],1],["Center",[0.0116673,0.0132002],1],[],["Center",[-1.70474e-009,0.022062],1],["Center",[-1.44248e-009,0.0186679],1],[],["Center",[-0.0137886,0.0156002],1],["Center",[-0.0116673,0.0132002],1],[],["Center",[-0.0195,-2.63087e-010],1],["Center",[-0.0165,-2.22612e-010],1],[],["Center",[-0.0137886,-0.0156002],1],["Center",[-0.0116673,-0.0132002],1],[],["Center",[3.40949e-009,-0.022062],1],["Center",[2.88495e-009,-0.0186679],1],[],["Center",[0.00742462,-0.00840012],1],["Center",[0.0053033,-0.00600008],1],[],["Center",[0.00742462,0.00840012],1],["Center",[0.0053033,0.00600008],1],[],["Center",[-0.00742462,0.00840012],1],["Center",[-0.0053033,0.00600009],1],[],["Center",[-0.00742462,-0.00840012],1],["Center",[-0.0053033,-0.00600008],1],[]]
                    },
                    "alpha": 0.22
                }
            }
        }
    },
    "scope": 2,
    "displayName": "S-8 KOM HEAT",
    "displayNameShort": "S-8 KOM",
    "descriptionShort": "HEAT (Penetration: 350mm RHA)",
    "initSpeed": 44,
    "nameSound": "rockets",
    "maxleadspeed": 30,
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
    "maxThrowHoldTime": 2,
    "minThrowIntensityCoef": 0.3,
    "maxThrowIntensityCoef": 1.4,
    "quickReload": 0,
}