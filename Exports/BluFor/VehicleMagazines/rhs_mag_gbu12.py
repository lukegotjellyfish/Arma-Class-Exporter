rhs_mag_gbu12 = {
    "count": 1,
    "displayname": "GBU-12",
    "descriptionshort": "500lb Paveway II",
    # Ammo: CfgMagazines|rhs_mag_gbu12|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "rhs_ammo_gbu12",
        "model": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_b_gbu12_fly",
        "proxyshape": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_b_gbu12",
        "inittime": 0.2,
        "maverickweaponindexoffset": 8,
        "soundsetexplosion": ["BombsHeavy_Exp_SoundSet","BombsHeavy_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "hit": 5000,
        "indirecthit": 1100,
        "indirecthitrange": 12,
        "maneuvrability": 10,
        "fusedistance": 50,
        "tracklead": 0.95,
        "trackoversteer": 1,
        "airfriction": 0.06,
        "sideairfriction": 0.12,
        "aiammousageflags": "128 + 512",
        "dangerradiushit": 1000,
        "suppressionradiushit": 120,
        "cratereffects": "BombCrater",
        "explosioneffects": "BombExplosion",
        "explosionsoundeffect": "DefaultExplosion",
        "explosiontime": 2,
        "multisoundhit": ["soundHit1",0.2,"soundHit2",0.2,"soundHit3",0.2,"soundHit4",0.2,"soundHit5",0.2],
        "soundhit1": ["|A3|Sounds_F|weapons|Explosion|expl_big_1",2.51189,1,2400],
        "soundhit2": ["|A3|Sounds_F|weapons|Explosion|expl_big_2",2.51189,1,2400],
        "soundhit3": ["|A3|Sounds_F|weapons|Explosion|expl_big_3",2.51189,1,2400],
        "soundhit4": ["|A3|Sounds_F|weapons|Explosion|expl_shell_1",2.51189,1,2400],
        "soundhit5": ["|A3|Sounds_F|weapons|Explosion|expl_shell_2",2.51189,1,2400],
        "whistledist": 24,
        "missilelockcone": 120,
        "missilekeeplockedcone": 120,
        "missilelockmaxdistance": 5000,
        "missilelockmindistance": 100,
        "missilelockmaxspeed": 30,
        "autoseektarget": 1,
        "lockseekradius": 500,
        "weaponlocksystem": 4,
        "cmimmunity": 0.3,
        "flightprofiles": ["LoalAltitude"],
        # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|LoalAltitude [Indent level: 1],
        "loalaltitude": {
            "lockseekaltitude": 500
        },
        # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|Components [Indent level: 1],
        "components": {
            # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|Components|SensorsManagerComponent [Indent level: 2]
            "sensorsmanagercomponent": {
                # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|Components|SensorsManagerComponent|Components [Indent level: 3]
                "components": {
                    # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|Components|SensorsManagerComponent|Components|NVSensorComponent [Indent level: 4]
                    "nvsensorcomponent": {
                        # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|Components|SensorsManagerComponent|Components|NVSensorComponent|AirTarget [Indent level: 5]
                        "airtarget": {
                            "minrange": 500,
                            "maxrange": 5000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": 1
                        },
                        # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|Components|SensorsManagerComponent|Components|NVSensorComponent|GroundTarget [Indent level: 5],
                        "groundtarget": {
                            "minrange": 500,
                            "maxrange": 5000,
                            "objectdistancelimitcoef": 1,
                            "viewdistancelimitcoef": 1
                        },
                        "maxtrackablespeed": 30,
                        "anglerangehorizontal": 120,
                        "anglerangevertical": 120,
                        "componenttype": "NVSensorComponent",
                        "color": [1,1,1,0],
                        "typerecognitiondistance": 0,
                        "allowsmarking": 1,
                        "groundnoisedistancecoef": -1,
                        "maxgroundnoisedistance": -1,
                        "minspeedthreshold": 0,
                        "maxspeedthreshold": 0,
                        "animdirection": "",
                        "aimdown": 0,
                        "mintrackablespeed": -1e+010,
                        "mintrackableatl": -1e+010,
                        "maxtrackableatl": 1e+010
                    },
                    # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4],
                    "lasersensorcomponent": {
                        # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|Components|SensorsManagerComponent|Components|LaserSensorComponent|AirTarget [Indent level: 5]
                        "airtarget": {
                            "minrange": 5000,
                            "maxrange": 5000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|Components|SensorsManagerComponent|Components|LaserSensorComponent|GroundTarget [Indent level: 5],
                        "groundtarget": {
                            "minrange": 5000,
                            "maxrange": 5000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        "maxtrackablespeed": 30,
                        "anglerangehorizontal": 120,
                        "anglerangevertical": 120,
                        "componenttype": "LaserSensorComponent",
                        "typerecognitiondistance": 0,
                        "color": [1,1,1,0],
                        "allowsmarking": 1,
                        "groundnoisedistancecoef": -1,
                        "maxgroundnoisedistance": -1,
                        "minspeedthreshold": 0,
                        "maxspeedthreshold": 0,
                        "animdirection": "",
                        "aimdown": 0,
                        "mintrackablespeed": -1e+010,
                        "mintrackableatl": -1e+010,
                        "maxtrackableatl": 1e+010
                    }
                }
            }
        },
        "cost": 20000,
        "irlock": 0,
        "laserlock": 1,
        "maxcontrolrange": 100000,
        "simulation": "shotMissile",
        "maxspeed": 100,
        "timetolive": 120,
        "thrusttime": 0,
        "thrust": 0,
        "access": 3,
        "underwaterhitrangecoef": 1,
        "typicalspeed": 900,
        "explosionforcecoef": 1,
        "iscrateroriented": 0,
        "cratershape": "",
        "weapontype": "Default",
        "animated": 0,
        "shadow": 0,
        "cartridge": "",
        "simulationstep": 0.05,
        "tracercolor": [0.7,0.7,0.5,0.04],
        "tracercolorr": [0.7,0.7,0.5,0.04],
        "soundfly": ["",1,1],
        "soundengine": ["",1,1],
        "soundhit": ["",1,1],
        "supersoniccracknear": ["",1,1],
        "supersoniccrackfar": ["",1,1],
        "soundfall": ["",1,1],
        "soundfakefall": ["soundFall",1],
        "hitgroundsoft": ["soundHit",1],
        "hitgroundhard": ["soundHit",1],
        "hitman": ["soundHit",1],
        "hitarmor": ["soundHit",1],
        "hitiron": ["soundHit",1],
        "hitbuilding": ["soundHit",1],
        "hitfoliage": ["soundHit",1],
        "hitwood": ["soundHit",1],
        "hitglass": ["soundHit",1],
        "hitglassarmored": ["soundHit",1],
        "hitconcrete": ["soundHit",1],
        "hitrubber": ["soundHit",1],
        "hitplastic": ["soundHit",1],
        "hitdefault": ["soundHit",1],
        "hitmetal": ["soundHit",1],
        "hitmetalplate": ["soundHit",1],
        "hittyre": ["soundHit",1],
        "hitwater": ["soundHit",1],
        "soundimpact": ["",1,1],
        "impactgroundsoft": ["soundImpact",1],
        "impactgroundhard": ["soundImpact",1],
        "impactman": ["soundImpact",1],
        "impactiron": ["soundImpact",1],
        "impactarmor": ["soundImpact",1],
        "impactbuilding": ["soundImpact",1],
        "impactfoliage": ["soundImpact",1],
        "impactwood": ["soundImpact",1],
        "impactglass": ["soundImpact",1],
        "impactglassarmored": ["soundImpact",1],
        "impactconcrete": ["soundImpact",1],
        "impactrubber": ["soundImpact",1],
        "impactplastic": ["soundImpact",1],
        "impactdefault": ["soundImpact",1],
        "impactmetal": ["soundImpact",1],
        "impactmetalplate": ["soundImpact",1],
        "impacttyre": ["soundImpact",1],
        "impactwater": ["soundImpact",1],
        "grenadefiresound": [],
        "grenadeburningsound": [],
        "deflecting": 0,
        "deflectionslowdown": 0.8,
        "explosive": 1,
        "craterwatereffects": "ImpactEffectsWater",
        "effectsmissile": "ExplosionEffects",
        "effectsmissileinit": "",
        "effectssmoke": "SmokeShellWhite",
        "effectsfire": "CannonFire",
        "effectflare": "FlareShell",
        "effectfly": "",
        "minejumpeffects": "",
        "watereffectoffset": 0.45,
        "directionalexplosion": 0,
        "explosionangle": 60,
        "explosiondir": "explosionDir",
        "explosionpos": "explosionPos",
        "explosioneffectsdir": "explosionDir",
        "minimumsafezone": 0.1,
        "soundtrigger": [],
        "soundactivation": [],
        "sounddeactivation": [],
        "mintimetolive": 0,
        "airlock": 0,
        "nvlock": 0,
        "artillerylock": 0,
        "hitonwater": 0,
        "manualcontrol": 0,
        "locktype": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "visiblefire": 0,
        "audiblefire": 0,
        "shootdistraction": -1,
        "visiblefiretime": 0,
        "icon": "",
        "submunitionammo": "",
        "explosiontype": "explosive",
        "minetrigger": "RangeTrigger",
        "mineboundingtime": 3,
        "mineboundingdist": 3,
        "mineinconspicuousness": 10,
        "minefloating": -1,
        "minedivespeed": 1,
        "mineplacedist": 0.5,
        # Class: CfgAmmo|Default|HitEffects [Indent level: 1],
        "hiteffects": {
            "vehicle": "ImpactMetal",
            "object": "ImpactConcrete"
        },
        "suppressionradiusbulletclose": -1,
        "dangerradiusbulletclose": -1,
        "caliber": 1,
        "whistleonfire": 0,
        # Class: CfgAmmo|Default|NVGMarkers [Indent level: 1],
        "nvgmarkers": {
        },
        "mindamageforcamshakehit": 0.55,
        # Class: CfgAmmo|Default|EventHandlers [Indent level: 1],
        "eventhandlers": {
        },
    },
    "eventhandlers": "rhs_ammo_gbu12",
    "model": "A3|Weapons_F|DynamicLoadout|PylonMissile_1x_Bomb_02_F.p3d",
    "hardpoints": ["RHS_HP_LGB_500"],
    "pylonweapon": "rhs_weap_gbu12",
    "displaynamemfdformat": "GBU12|%1",
    # Class: CfgMagazines|rhs_mag_gbu12|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_ammoname [Indent level: 2]
        "rhs_a10a_ammoname": {
            # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_ammoname|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_ammoname|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_ammoname|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "GBU",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.005,0.02],1],
                    "right": [[0.05,0.02],1],
                    "down": [[0.005,0.105],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_box [Indent level: 2],
        "rhs_a10a_box": {
            # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_box|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_box|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_box|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "PylonAmmoRelative>=0.001",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_box|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,-0.04],1],[[0.015,-0.04],1],[[0.015,0.04],1],[[-0.015,0.04],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_box|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_box|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,0.05],1],[[0.015,0.05],1],[[0.015,0.13],1],[[-0.015,0.13],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_box|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative<=0",
                    "color": [0.87,0,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|rhs_a10a_box|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.02,0.05],1],[[0.05,0.05],1],[[0.05,0.13],1],[[0.02,0.13],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD [Indent level: 2],
        "rhs_a29_weap_mfd": {
            # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD|Draw|BackgroundGroup [Indent level: 4]
                "backgroundgroup": {
                    "color": [0,0,0],
                    # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD|Draw|BackgroundGroup|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[-0.02,-0.08],1],[[0.03,-0.08],1],[[0.03,0.06],1],[[-0.02,0.06],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "PylonAmmoRelative>0",
                    "color": [0,0.12,0],
                    # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.00825,0.0265625],1],[[0.0123125,0.0265625],1],[],[[-0.0051875,0.0265625],1],[[-0.001125,0.0265625],1],[],[[-0.0105,-0.0575],1],[[0.017625,-0.0575],1],[],[[-0.0105,0.00749999],1],[[0.017625,0.00749999],1],[],[[-0.000812501,0.050625],1],[[-0.000812501,0.0178125],1],[[0.0016875,0.01625],1],[[0.0035625,0.015625],1],[[0.00825,0.02],1],[[0.007625,0.0503125],1],[],[[0.0035625,0.0578125],1],[[0.0066875,0.0565625],1],[[0.007625,0.0534375],1],[[0.007625,0.0503125],1],[[0.0210625,0.055],1],[[0.0210625,0.0303125],1],[[0.0123125,0.0265625],1],[[0.017625,0.0078125],1],[[0.017625,-0.056875],1],[[0.017625,-0.0646875],1],[[0.0160625,-0.070625],1],[[0.0141875,-0.0740625],1],[[0.0110625,-0.076875],1],[[0.0079375,-0.0784375],1],[[0.0035625,-0.0790625],1],[[-0.000812501,-0.0784375],1],[[-0.00393751,-0.0765625],1],[[-0.0070625,-0.07375],1],[[-0.0089375,-0.0703125],1],[[-0.0105,-0.0646875],1],[[-0.0105,-0.056875],1],[[-0.0105,0.0078125],1],[[-0.0051875,0.0265625],1],[[-0.013625,0.030625],1],[[-0.013625,0.054375],1],[[-0.000812501,0.050625],1],[[0.0035625,0.0578125],1]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "color": [0.99,0.94,0.59],
                    # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.00825,0.0265625],1],[[0.0123125,0.0265625],1],[],[[-0.0051875,0.0265625],1],[[-0.001125,0.0265625],1],[],[[-0.0105,-0.0575],1],[[0.017625,-0.0575],1],[],[[-0.0105,0.00749999],1],[[0.017625,0.00749999],1],[],[[-0.000812501,0.050625],1],[[-0.000812501,0.0178125],1],[[0.0016875,0.01625],1],[[0.0035625,0.015625],1],[[0.00825,0.02],1],[[0.007625,0.0503125],1],[],[[0.0035625,0.0578125],1],[[0.0066875,0.0565625],1],[[0.007625,0.0534375],1],[[0.007625,0.0503125],1],[[0.0210625,0.055],1],[[0.0210625,0.0303125],1],[[0.0123125,0.0265625],1],[[0.017625,0.0078125],1],[[0.017625,-0.056875],1],[[0.017625,-0.0646875],1],[[0.0160625,-0.070625],1],[[0.0141875,-0.0740625],1],[[0.0110625,-0.076875],1],[[0.0079375,-0.0784375],1],[[0.0035625,-0.0790625],1],[[-0.000812501,-0.0784375],1],[[-0.00393751,-0.0765625],1],[[-0.0070625,-0.07375],1],[[-0.0089375,-0.0703125],1],[[-0.0105,-0.0646875],1],[[-0.0105,-0.056875],1],[[-0.0105,0.0078125],1],[[-0.0051875,0.0265625],1],[[-0.013625,0.030625],1],[[-0.013625,0.054375],1],[[-0.000812501,0.050625],1],[[0.0035625,0.0578125],1]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative <= 0",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.00825,0.0265625],1],[[0.0123125,0.0265625],1],[],[[-0.0051875,0.0265625],1],[[-0.001125,0.0265625],1],[],[[-0.0105,-0.0575],1],[[0.017625,-0.0575],1],[],[[-0.0105,0.00749999],1],[[0.017625,0.00749999],1],[],[[-0.000812501,0.050625],1],[[-0.000812501,0.0178125],1],[[0.0016875,0.01625],1],[[0.0035625,0.015625],1],[[0.00825,0.02],1],[[0.007625,0.0503125],1],[],[[0.0035625,0.0578125],1],[[0.0066875,0.0565625],1],[[0.007625,0.0534375],1],[[0.007625,0.0503125],1],[[0.0210625,0.055],1],[[0.0210625,0.0303125],1],[[0.0123125,0.0265625],1],[[0.017625,0.0078125],1],[[0.017625,-0.056875],1],[[0.017625,-0.0646875],1],[[0.0160625,-0.070625],1],[[0.0141875,-0.0740625],1],[[0.0110625,-0.076875],1],[[0.0079375,-0.0784375],1],[[0.0035625,-0.0790625],1],[[-0.000812501,-0.0784375],1],[[-0.00393751,-0.0765625],1],[[-0.0070625,-0.07375],1],[[-0.0089375,-0.0703125],1],[[-0.0105,-0.0646875],1],[[-0.0105,-0.056875],1],[[-0.0105,0.0078125],1],[[-0.0051875,0.0265625],1],[[-0.013625,0.030625],1],[[-0.013625,0.054375],1],[[-0.000812501,0.050625],1],[[0.0035625,0.0578125],1]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD_Inventory [Indent level: 2],
        "rhs_a29_weap_mfd_inventory": {
            # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD_Inventory|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonText1 [Indent level: 4]
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "GBU-12",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0,0.02],1],
                    "right": [[0.025,0.02],1],
                    "down": [[0,0.04],1]
                },
                # Class: CfgMagazines|rhs_mag_gbu12|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonText2 [Indent level: 4],
                "pylontext2": {
                    "type": "text",
                    "source": "static",
                    "text": "LOAL",
                    "scale": 1,
                    "sourcescale": 1,
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
    "displaynameshort": "Bomb",
    "initspeed": 0,
    "maxleadspeed": 25,
    "namesound": "cannon",
    "type": 0,
    "reloadaction": "",
    "weaponpoolavailable": 0,
    "value": 1,
    "picture": "",
    "modelspecial": "",
    "useaction": 0,
    "useactiontitle": "",
    "selectionfireanim": "zasleh",
    "mass": 8,
    "simulation": "ProxyMagazines",
    "weight": 0,
    # Class: CfgMagazines|Default|InventoryPlacements [Indent level: 1],
    "inventoryplacements": {
    },
    # Class: CfgMagazines|Default|Library [Indent level: 1],
    "library": {
        "libtextdesc": ""
    },
    "maxthrowholdtime": 2,
    "minthrowintensitycoef": 0.3,
    "maxthrowintensitycoef": 1.4,
    "quickreload": 0,
}