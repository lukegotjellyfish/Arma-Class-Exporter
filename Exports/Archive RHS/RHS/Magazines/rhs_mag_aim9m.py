rhs_mag_aim9m = {
    "displayname": "AIM-9M",
    "displaynamemfdformat": "%1 AIM-9M",
    # Ammo: CfgMagazines|rhs_mag_aim9m|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "rhs_ammo_aim9m",
        "model": "a3|Weapons_F_EPC|Ammo|Missile_AA_04_fly_F.p3d",
        "proxyshape": "a3|Weapons_F_EPC|Ammo|Missile_AA_04_F.p3d",
        "maneuvrability": 30,
        "cmimmunity": 0.9,
        "missilelockcone": 90,
        "missilekeeplockedcone": 90,
        "hit": 150,
        "indirecthit": 90,
        "indirecthitrange": 14,
        "proximityexplosiondistance": 19,
        "simulationstep": 0.001,
        "airlock": 2,
        "irlock": 1,
        "cost": 1500,
        "maxspeed": 1029,
        "timetolive": 35,
        "sideairfriction": 0.2,
        "trackoversteer": 0.95,
        "tracklead": 0.75,
        "inittime": 0,
        "thrusttime": 3,
        "thrust": 390,
        "fusedistance": 300,
        "explosionangle": 60,
        "cratereffects": "AAMissileCrater",
        "explosioneffects": "AAMissileExplosion",
        "effectsmissile": "rhs_missile3",
        "whistledist": 20,
        "missilelockmaxdistance": 8000,
        "missilelockmindistance": 300,
        "missilelockmaxspeed": 555,
        "weaponlocksystem": "2 + 16",
        # Class: CfgAmmo|rhs_ammo_Sidewinder_AA|Components [Indent level: 1],
        "components": {
            # Class: CfgAmmo|rhs_ammo_Sidewinder_AA|Components|SensorsManagerComponent [Indent level: 2]
            "sensorsmanagercomponent": {
                # Class: CfgAmmo|rhs_ammo_Sidewinder_AA|Components|SensorsManagerComponent|Components [Indent level: 3]
                "components": {
                    # Class: CfgAmmo|rhs_ammo_Sidewinder_AA|Components|SensorsManagerComponent|Components|IRSensorComponent [Indent level: 4]
                    "irsensorcomponent": {
                        # Class: CfgAmmo|rhs_ammo_Sidewinder_AA|Components|SensorsManagerComponent|Components|IRSensorComponent|AirTarget [Indent level: 5]
                        "airtarget": {
                            "minrange": 500,
                            "maxrange": 8000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": 1
                        },
                        # Class: CfgAmmo|rhs_ammo_Sidewinder_AA|Components|SensorsManagerComponent|Components|IRSensorComponent|GroundTarget [Indent level: 5],
                        "groundtarget": {
                            "minrange": 500,
                            "maxrange": 8000,
                            "objectdistancelimitcoef": 1,
                            "viewdistancelimitcoef": 1
                        },
                        "typerecognitiondistance": -1,
                        "anglerangehorizontal": 120,
                        "anglerangevertical": 120,
                        "groundnoisedistancecoef": 0.03,
                        "maxgroundnoisedistance": -1,
                        "minspeedthreshold": 0,
                        "maxspeedthreshold": 0,
                        "maxfogseethrough": 0.8,
                        "mintrackablespeed": -1e+010,
                        "maxtrackablespeed": 555,
                        "mintrackableatl": 20,
                        "maxtrackableatl": 1e+010,
                        "componenttype": "IRSensorComponent",
                        "color": [1,0,0,1],
                        "allowsmarking": 1,
                        "animdirection": "",
                        "aimdown": 0
                    }
                }
            }
        },
        "maverickweaponindexoffset": 0,
        "warheadname": "HE",
        "laserlock": 0,
        "nvlock": 0,
        "manualcontrol": 0,
        "maxcontrolrange": 4500,
        "aiammousageflags": 256,
        "airfriction": 0.14,
        "effectsmissileinit": "PylonBackEffects",
        "muzzleeffect": "",
        "soundhit1": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_01",2.51189,1,2000],
        "soundhit2": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_02",2.51189,1,2000],
        "soundhit3": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_03",2.51189,1,2000],
        "multisoundhit": ["soundHit1",0.34,"soundHit2",0.33,"soundHit3",0.33],
        "soundfly": ["A3|Sounds_F|weapons|Rockets|rocket_fly_1",0.562341,1,1500],
        # Class: CfgAmmo|Missile_AA_04_F|Hiteffects [Indent level: 1],
        "hiteffects": {
            "hitwater": "ImpactEffectsSmall"
        },
        "soundsetexplosion": ["RocketsMedium_Exp_SoundSet","RocketsMedium_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "explosionsoundeffect": "DefaultExplosion",
        "soundengine": ["",1,1,50],
        "supersoniccracknear": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_close",0.398107,1,20],
        "supersoniccrackfar": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_50meters",0.316228,1,50],
        "deflecting": 0,
        "dangerradiushit": -1,
        "suppressionradiushit": 30,
        "htmin": 60,
        "htmax": 1800,
        "afmax": 200,
        "mfmax": 100,
        "mfact": 0,
        "tbody": 0,
        # Class: CfgAmmo|MissileBase|EventHandlers [Indent level: 1],
        "eventhandlers": {
            # Class: CfgAmmo|MissileBase|EventHandlers|RHS_APS_FiredEH [Indent level: 2]
            "rhs_aps_firedeh": {
                "fired": "_this spawn rhs_fnc_aps_missileFired"
            }
        },
        "simulation": "shotMissile",
        "visiblefire": 32,
        "audiblefire": 32,
        "visiblefiretime": 20,
        "soundhit": ["",100,1],
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
        "tracercolor": [0.7,0.7,0.5,0.04],
        "tracercolorr": [0.7,0.7,0.5,0.04],
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
        "deflectionslowdown": 0.8,
        "explosive": 1,
        "craterwatereffects": "ImpactEffectsWater",
        "effectssmoke": "SmokeShellWhite",
        "effectsfire": "CannonFire",
        "effectflare": "FlareShell",
        "effectfly": "",
        "minejumpeffects": "",
        "watereffectoffset": 0.45,
        "directionalexplosion": 0,
        "explosiondir": "explosionDir",
        "explosionpos": "explosionPos",
        "explosioneffectsdir": "explosionDir",
        "minimumsafezone": 0.1,
        "soundtrigger": [],
        "soundactivation": [],
        "sounddeactivation": [],
        "mintimetolive": 0,
        "artillerylock": 0,
        "hitonwater": 0,
        "lockseekradius": 100,
        "locktype": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "autoseektarget": 0,
        "shootdistraction": -1,
        "explosiontime": 0,
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
        "suppressionradiusbulletclose": -1,
        "dangerradiusbulletclose": -1,
        "caliber": 1,
        "whistleonfire": 0,
        # Class: CfgAmmo|Default|NVGMarkers [Indent level: 1],
        "nvgmarkers": {
        },
        "mindamageforcamshakehit": 0.55,
    },
    "mindamageforcamshakehit": "rhs_ammo_aim9m",
    "pylonweapon": "rhs_weap_aim9m",
    "scope": 2,
    "displaynameshort": "IR",
    "descriptionshort": "Sidewinder, IR-homing",
    "count": 1,
    "initspeed": 0,
    "maxleadspeed": 450,
    "namesound": "missiles",
    "model": "A3|Weapons_F|DynamicLoadout|PylonPod_1x_Missile_AA_04_F.p3d",
    "hardpoints": ["RHS_HP_AIM9","RHS_HP_AIM9_2x"],
    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_ammoname [Indent level: 2]
        "rhs_a10a_ammoname": {
            # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_ammoname|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_ammoname|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_ammoname|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "MFD_PYLON_NAME",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.005,0.02],1],
                    "right": [[0.05,0.02],1],
                    "down": [[0.005,0.105],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_box [Indent level: 2],
        "rhs_a10a_box": {
            # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_box|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_box|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_box|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "PylonAmmoRelative>=0.001",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_box|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,-0.04],1],[[0.015,-0.04],1],[[0.015,0.04],1],[[-0.015,0.04],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_box|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_box|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,0.05],1],[[0.015,0.05],1],[[0.015,0.13],1],[[-0.015,0.13],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_box|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative<=0",
                    "color": [0.87,0,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_a10a_box|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.02,0.05],1],[[0.05,0.05],1],[[0.05,0.13],1],[[0.02,0.13],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon [Indent level: 2],
        "rhs_f22_pylon": {
            # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|material [Indent level: 3]
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Bones [Indent level: 3],
            "bones": {
                # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Bones|Center [Indent level: 4]
                "center": {
                    "type": "fixed",
                    "pos": [0,0]
                }
            },
            # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Default [Indent level: 4]
                "default": {
                    "condition": "PylonAmmoRelative>0",
                    "color": [0.15,1,0.15],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0205729],1],["Center",[0.01,-0.0178161],1],["Center",[0.01732,-0.0102865],1],["Center",[0.02,0],1],["Center",[0.01732,0.0102865],1],["Center",[0.01,0.0178161],1],["Center",[0,0.0205729],1],["Center",[-0.01,0.0178161],1],["Center",[-0.01732,0.0102865],1],["Center",[-0.02,0],1],["Center",[-0.01732,-0.0102865],1],["Center",[-0.01,-0.0178161],1],["Center",[0,-0.0205729],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "M",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": ["Center",1,[-0,-0.015],1],
                        "right": ["Center",1,[0.03,-0.015],1],
                        "down": ["Center",1,[-0,0.02],1]
                    }
                },
                # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "alpha": 1,
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0205729],1],["Center",[0.01,-0.0178161],1],["Center",[0.01732,-0.0102865],1],["Center",[0.02,0],1],["Center",[0.01732,0.0102865],1],["Center",[0.01,0.0178161],1],["Center",[0,0.0205729],1],["Center",[-0.01,0.0178161],1],["Center",[-0.01732,0.0102865],1],["Center",[-0.02,0],1],["Center",[-0.01732,-0.0102865],1],["Center",[-0.01,-0.0178161],1],["Center",[0,-0.0205729],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Selected|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "M",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": ["Center",1,[-0,-0.015],1],
                        "right": ["Center",1,[0.03,-0.015],1],
                        "down": ["Center",1,[-0,0.02],1]
                    },
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Selected|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[["Center",1,[0,0],1],["Center",[0.0141421,-0.0145472],1],["Center",[0.02,8.99271e-010],1],["Center",[0.0141421,0.0145472],1]],[["Center",1,[0,0],1],["Center",[0.0141421,0.0145472],1],["Center",[-1.74846e-009,0.0205729],1],["Center",[-0.0141421,0.0145472],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,0.0145472],1],["Center",[-0.02,-2.4533e-010],1],["Center",[-0.0141421,-0.0145472],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,-0.0145472],1],["Center",[3.49691e-009,-0.0205729],1],["Center",[0.0141421,-0.0145472],1]]]
                    },
                    "color": [0.15,1,0.15]
                },
                # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative <= 0",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0205729],1],["Center",[0.01,-0.0178161],1],["Center",[0.01732,-0.0102865],1],["Center",[0.02,0],1],["Center",[0.01732,0.0102865],1],["Center",[0.01,0.0178161],1],["Center",[0,0.0205729],1],["Center",[-0.01,0.0178161],1],["Center",[-0.01732,0.0102865],1],["Center",[-0.02,0],1],["Center",[-0.01732,-0.0102865],1],["Center",[-0.01,-0.0178161],1],["Center",[0,-0.0205729],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Empty|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "M",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": ["Center",1,[-0,-0.015],1],
                        "right": ["Center",1,[0.03,-0.015],1],
                        "down": ["Center",1,[-0,0.02],1]
                    },
                    # Class: CfgMagazines|rhs_mag_Sidewinder|mfdElements|rhs_f22_pylon|Draw|Empty|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[["Center",1,[0,0],1],["Center",[0.0141421,-0.0145472],1],["Center",[0.02,8.99271e-010],1],["Center",[0.0141421,0.0145472],1]],[["Center",1,[0,0],1],["Center",[0.0141421,0.0145472],1],["Center",[-1.74846e-009,0.0205729],1],["Center",[-0.0141421,0.0145472],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,0.0145472],1],["Center",[-0.02,-2.4533e-010],1],["Center",[-0.0141421,-0.0145472],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,-0.0145472],1],["Center",[3.49691e-009,-0.0205729],1],["Center",[0.0141421,-0.0145472],1]]]
                    },
                    "alpha": 1
                }
            }
        }
    },
    "author": "Bohemia Interactive",
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