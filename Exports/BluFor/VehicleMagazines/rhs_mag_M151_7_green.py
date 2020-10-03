rhs_mag_M151_7_green = {
    "model": "rhsusf|addons|rhsusf_airweapons|proxypylon|rhsusf_pylon_r_FFAR_7x_green",
    "displayname": "M151 Hydra (LAU-68)",
    "hardpoints": ["RHS_HP_FFAR_USMC"],
    "scope": 2,
    "count": 7,
    "initSpeed": 44,
    "maxLeadSpeed": 200,
    "nameSound": "rockets",
    "weight": 48,
    # Ammo: rhs_ammo_Hydra_M151,
    "ammo": {
        "ammo": "rhs_ammo_Hydra_M151",
        "maverickweapon": 1,
        "maverickWeaponIndexOffset": 0,
        "model": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_r_M151_fly",
        "proxyShape": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_r_M151",
        "hit": 190,
        "indirectHit": 50,
        "indirectHitRange": 10,
        "cost": 75,
        "maxSpeed": 740,
        "thrustTime": 1.1,
        "thrust": 800,
        "sideAirFriction": 0.004,
        "timeToLive": 60,
        "fuseDistance": 40,
        "whistleDist": 24,
        "warheadName": "HE",
        "manualControl": 0,
        "maxControlRange": 0,
        "airLock": 0,
        "irLock": 0,
        "laserLock": 0,
        "nvLock": 0,
        "weaponLockSystem": 0,
        "aiAmmoUsageFlags": "64 + 128",
        "missileLockMinDistance": 500,
        "missileLockMaxDistance": 3000,
        "initTime": 0.002,
        "airFriction": 0.09,
        "maneuvrability": 0,
        "effectsMissileInit": "PylonBackEffectsFFAR",
        "muzzleEffect": "",
        "soundFly": ["A3|Sounds_F|weapons|Rockets|rocket_fly_1",0.630957,1.2,1700],
        # Class: CfgAmmo\Rocket_04_HE_F\CamShakeExplode,
        "CamShakeExplode": {
            "power": 16,
            "duration": 1.8,
            "frequency": 20,
            "distance": 191.554
        },
        # Class: CfgAmmo\Rocket_04_HE_F\CamShakeHit,
        "CamShakeHit": {
            "power": 80,
            "duration": 0.6,
            "frequency": 20,
            "distance": 1
        },
        # Class: CfgAmmo\Rocket_04_HE_F\CamShakeFire,
        "CamShakeFire": {
            "power": 2.9907,
            "duration": 1.8,
            "frequency": 20,
            "distance": 71.5542
        },
        # Class: CfgAmmo\Rocket_04_HE_F\CamShakePlayerFire,
        "CamShakePlayerFire": {
            "power": 2,
            "duration": 0.1,
            "frequency": 20,
            "distance": 1
        },
        "SoundSetExplosion": ["RocketsLight_Exp_SoundSet","RocketsLight_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "simulationStep": 0.01,
        "soundHit1": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_01",2.51189,1,2000],
        "soundHit2": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_02",2.51189,1,2000],
        "soundHit3": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_03",2.51189,1,2000],
        "multiSoundHit": ["soundHit1",0.34,"soundHit2",0.33,"soundHit3",0.33],
        "explosionSoundEffect": "DefaultExplosion",
        "soundEngine": ["",1,1,50],
        "supersonicCrackNear": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_close",0.398107,1,20],
        "supersonicCrackFar": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_50meters",0.316228,1,50],
        "CraterEffects": "ATMissileCrater",
        "explosionEffects": "ATMissileExplosion",
        "effectsMissile": "missile4",
        "deflecting": 0,
        "cmImmunity": 0.9,
        "dangerRadiusHit": -1,
        "suppressionRadiusHit": 30,
        # Class: CfgAmmo\MissileBase\HitEffects,
        "HitEffects": {
            "hitWater": "ImpactEffectsWaterRocket"
        },
        # Class: CfgAmmo\MissileBase\Components,
        "Components": {
        },
        "htMin": 60,
        "htMax": 1800,
        "afMax": 200,
        "mfMax": 100,
        "mFact": 0,
        "tBody": 0,
        # Class: CfgAmmo\MissileBase\EventHandlers,
        "EventHandlers": {
            # Class: CfgAmmo\MissileBase\EventHandlers\RHS_APS_FiredEH
            "RHS_APS_FiredEH": {
                "fired": "_this spawn rhs_fnc_aps_missileFired"
            }
        },
        "simulation": "shotMissile",
        "missileLockCone": 50,
        "visibleFire": 32,
        "audibleFire": 32,
        "visibleFireTime": 20,
        "soundHit": ["",100,1],
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
        "tracerColor": [0.7,0.7,0.5,0.04],
        "tracerColorR": [0.7,0.7,0.5,0.04],
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
        "deflectionSlowDown": 0.8,
        "explosive": 1,
        "craterWaterEffects": "ImpactEffectsWater",
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
        "artilleryLock": 0,
        "hitOnWater": 0,
        "lockSeekRadius": 100,
        "trackLead": 1,
        "trackOversteer": 1,
        "lockType": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "autoSeekTarget": 0,
        "shootDistraction": -1,
        "explosionTime": 0,
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
        "suppressionRadiusBulletClose": -1,
        "dangerRadiusBulletClose": -1,
        "caliber": 1,
        "whistleOnFire": 0,
        # Class: CfgAmmo\Default\NVGMarkers,
        "NVGMarkers": {
        },
        "minDamageForCamShakeHit": 0.55,
    },
    "displayNameShort": "HE",
    "descriptionShort": "×7 10lb HE Hydra",
    "pylonWeapon": "rhs_weap_FFARLauncher",
    "displayNameMFDFormat": "RKT|%2|%1",
    # Class: CfgMagazines\rhs_mag_M151_7\mfdElements,
    "mfdElements": {
        # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_ammoname
        "rhs_a10a_ammoname": {
            # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_ammoname\Bones
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_ammoname\Draw,
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_ammoname\Draw\PylonText1,
                "PylonText1": {
                    # Ammo: text
                    "type": {
                        "type": "text"
                    },
                    # Ammo: static,
                    "source": {
                        "source": "static",
                    },
                    # Ammo: RKT,
                    "text": {
                        "text": "RKT",
                    },
                    "scale": 1,
                    "sourceScale": 1,
                    # Ammo: center,
                    "align": {
                        "align": "center",
                    },
                    "pos": [[0.005,0.02],1],
                    "right": [[0.05,0.02],1],
                    "down": [[0.005,0.105],1]
                }
            }
        },
        # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_box,
        "rhs_a10a_box": {
            # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_box\Bones
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_box\Draw,
            "Draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_box\Draw\Default,
                "Default": {
                    "condition": "PylonAmmoRelative>=0.001",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_box\Draw\Default\Shape,
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,-0.04],1],[[0.015,-0.04],1],[[0.015,0.04],1],[[-0.015,0.04],1]]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_box\Draw\Selected,
                "Selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_box\Draw\Selected\Shape,
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,0.05],1],[[0.015,0.05],1],[[0.015,0.13],1],[[-0.015,0.13],1]]]
                    }
                },
                # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_box\Draw\Empty,
                "Empty": {
                    "condition": "PylonAmmoRelative<=0",
                    "color": [0.87,0,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_a10a_box\Draw\Empty\Shape,
                    "Shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.02,0.05],1],[[0.05,0.05],1],[[0.05,0.13],1],[[0.02,0.13],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_ah64_ammoname,
        "rhs_ah64_ammoname": {
            # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_ah64_ammoname\Bones
            "Bones": {
            },
            # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_ah64_ammoname\Draw,
            "Draw": {
                # Ammo: pylonSelected
                "condition": {
                    "condition": "pylonSelected"
                },
                # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_ah64_ammoname\Draw\PylonText1,
                "PylonText1": {
                    # Ammo: text
                    "type": {
                        "type": "text"
                    },
                    # Ammo: static,
                    "source": {
                        "source": "static",
                    },
                    # Ammo: 6PD,
                    "text": {
                        "text": "6PD",
                    },
                    "scale": 1,
                    "sourceScale": 1,
                    # Ammo: center,
                    "align": {
                        "align": "center",
                    },
                    "pos": [[0.005,0.02],1],
                    "right": [[0.05,0.02],1],
                    "down": [[0.005,0.105],1]
                },
                # Class: CfgMagazines\rhs_mag_M151_7\mfdElements\rhs_ah64_ammoname\Draw\PylonAmmo,
                "PylonAmmo": {
                    # Ammo: text
                    "type": {
                        "type": "text"
                    },
                    # Ammo: ammo,
                    "source": {
                        "source": "ammo",
                    },
                    "scale": 1,
                    "sourceScale": 1,
                    # Ammo: center,
                    "align": {
                        "align": "center",
                    },
                    "pos": [[0.015,0.02],1],
                    "right": [[0.06,0.02],1],
                    "down": [[0.015,0.105],1]
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
    "mass": 8,
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