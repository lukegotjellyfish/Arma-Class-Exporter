rhs_mag_kab500 = {
    # Ammo: CfgMagazines|rhs_mag_kab500|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "rhs_ammo_kab500",
        "hit": 8000,
        "indirecthit": 2400,
        "indirecthitrange": 25,
        "cratereffects": "RHS_HeavyBombCrater",
        "explosioneffects": "RHS_HeavyBombExplosion",
        "soundsetexplosion": ["BombsHeavy_Exp_SoundSet","BombsHeavy_Tail_SoundSet","Explosion_Debris_SoundSet"],
        # Class: CfgAmmo|rhs_ammo_kab500|CamShakeExplode [Indent level: 1],
        "camshakeexplode": {
            "power": 240,
            "duration": 7,
            "frequency": 20,
            "distance": 2077.13
        },
        # Class: CfgAmmo|rhs_ammo_kab500|CamShakeHit [Indent level: 1],
        "camshakehit": {
            "power": 1200,
            "duration": 1.2,
            "frequency": 20,
            "distance": 1
        },
        "flightprofiles": ["LoalAltitude"],
        # Class: CfgAmmo|rhs_ammo_kab250|Direct [Indent level: 1],
        "direct": {
        },
        # Class: CfgAmmo|rhs_ammo_kab250|LoalAltitude [Indent level: 1],
        "loalaltitude": {
            "lockseekaltitude": 300
        },
        "explosionforcecoef": 10,
        "model": "rhsafrf|addons|rhs_airweapons|rhs_m_kab250.p3d",
        "proxyshape": "rhsafrf|addons|rhs_airweapons|rhs_m_kab250.p3d",
        "maverickweaponindexoffset": 0,
        "maneuvrability": 10,
        "fusedistance": 50,
        "tracklead": 0.95,
        "trackoversteer": 1,
        "airfriction": 0.06,
        "sideairfriction": 0.12,
        "aiammousageflags": "128 + 512",
        "dangerradiushit": 1000,
        "suppressionradiushit": 120,
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
        "inittime": 0,
        "thrusttime": 0,
        "thrust": 0,
        "access": 3,
        "underwaterhitrangecoef": 1,
        "typicalspeed": 900,
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
    "eventhandlers": "rhs_ammo_kab500",
    "displayname": "KAB-500L",
    "displaynameshort": "LGB",
    "pylonweapon": "rhs_weap_kab500",
    # Class: CfgMagazines|rhs_mag_kab500|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_ammoname [Indent level: 2]
        "rhs_rus_ammoname": {
            # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_ammoname|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_ammoname|Draw [Indent level: 3],
            "draw": {
                "condition": "PylonSelected",
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_ammoname|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "КАБ500",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[-0.005,0.02],1],
                    "right": [[0.045,0.02],1],
                    "down": [[-0.005,0.065],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_ammoname_right [Indent level: 2],
        "rhs_rus_ammoname_right": {
            # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_ammoname_right|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_ammoname_right|Draw [Indent level: 3],
            "draw": {
                "condition": "PylonSelected",
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_ammoname_right|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "КАБ500",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[-0.005,0.02],1],
                    "right": [[0.045,0.02],1],
                    "down": [[-0.005,0.065],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_su25_box [Indent level: 2],
        "rhs_su25_box": {
            # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_su25_box|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_su25_box|Draw [Indent level: 3],
            "draw": {
                "condition": "1-pylonMagazineEmpty",
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_su25_box|Draw|Shape [Indent level: 4],
                "shape": {
                    "type": "polygon",
                    "width": 4,
                    "points": [[[[-0.022,-0.04],1],[[0.022,-0.04],1],[[0.022,0.04],1],[[-0.022,0.04],1]]]
                },
                # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_su25_box|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.58,0.23,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_su25_box|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.022,0.18],1],[[0.022,0.18],1],[[0.022,0.26],1],[[-0.022,0.26],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle [Indent level: 2],
        "rhs_rus_circle": {
            # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Bones [Indent level: 3]
            "bones": {
                # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Bones|Center [Indent level: 4]
                "center": {
                    "type": "fixed",
                    "pos": [0,0]
                }
            },
            # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "1-PylonSelected-pylonMagazineEmpty",
                    "color": [1,1,1],
                    # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "КАБ500",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0226277],1],["Center",[0.01,-0.0195956],1],["Center",[0.01732,-0.0113139],1],["Center",[0.02,0],1],["Center",[0.01732,0.0113139],1],["Center",[0.01,0.0195956],1],["Center",[0,0.0226277],1],["Center",[-0.01,0.0195956],1],["Center",[-0.01732,0.0113139],1],["Center",[-0.02,0],1],["Center",[-0.01732,-0.0113139],1],["Center",[-0.01,-0.0195956],1],["Center",[0,-0.0226277],1],[],["Center",[0.0141421,-0.0160002],1],["Center",[0.0247487,-0.0280004],1],[],["Center",[0.0141421,0.0160002],1],["Center",[0.0247487,0.0280004],1],[],["Center",[-0.0141421,0.0160002],1],["Center",[-0.0247487,0.0280004],1],[],["Center",[-0.0141421,-0.0160002],1],["Center",[-0.0247487,-0.0280004],1],[]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Selected|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "КАБ500",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0226277],1],["Center",[0.01,-0.0195956],1],["Center",[0.01732,-0.0113139],1],["Center",[0.02,0],1],["Center",[0.01732,0.0113139],1],["Center",[0.01,0.0195956],1],["Center",[0,0.0226277],1],["Center",[-0.01,0.0195956],1],["Center",[-0.01732,0.0113139],1],["Center",[-0.02,0],1],["Center",[-0.01732,-0.0113139],1],["Center",[-0.01,-0.0195956],1],["Center",[0,-0.0226277],1],[],["Center",[0.0141421,-0.0160002],1],["Center",[0.0247487,-0.0280004],1],[],["Center",[0.0141421,0.0160002],1],["Center",[0.0247487,0.0280004],1],[],["Center",[-0.0141421,0.0160002],1],["Center",[-0.0247487,0.0280004],1],[],["Center",[-0.0141421,-0.0160002],1],["Center",[-0.0247487,-0.0280004],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Selected|Polygon [Indent level: 5],
                    "polygon": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[["Center",1,[0,0],1],["Center",[0.0141421,-0.0160002],1],["Center",[0.02,9.8909e-010],1],["Center",[0.0141421,0.0160002],1]],[["Center",1,[0,0],1],["Center",[0.0141421,0.0160002],1],["Center",[-1.74846e-009,0.0226277],1],["Center",[-0.0141421,0.0160002],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,0.0160002],1],["Center",[-0.02,-2.69833e-010],1],["Center",[-0.0141421,-0.0160002],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,-0.0160002],1],["Center",[3.49691e-009,-0.0226277],1],["Center",[0.0141421,-0.0160002],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "pylonMagazineEmpty",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Empty|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "КАБ500",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0226277],1],["Center",[0.01,-0.0195956],1],["Center",[0.01732,-0.0113139],1],["Center",[0.02,0],1],["Center",[0.01732,0.0113139],1],["Center",[0.01,0.0195956],1],["Center",[0,0.0226277],1],["Center",[-0.01,0.0195956],1],["Center",[-0.01732,0.0113139],1],["Center",[-0.02,0],1],["Center",[-0.01732,-0.0113139],1],["Center",[-0.01,-0.0195956],1],["Center",[0,-0.0226277],1],[],["Center",[0.0141421,-0.0160002],1],["Center",[0.0247487,-0.0280004],1],[],["Center",[0.0141421,0.0160002],1],["Center",[0.0247487,0.0280004],1],[],["Center",[-0.0141421,0.0160002],1],["Center",[-0.0247487,0.0280004],1],[],["Center",[-0.0141421,-0.0160002],1],["Center",[-0.0247487,-0.0280004],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_kab500|mfdElements|rhs_rus_circle|Draw|Empty|Polygon [Indent level: 5],
                    "polygon": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[["Center",1,[0,0],1],["Center",[0.0141421,-0.0160002],1],["Center",[0.02,9.8909e-010],1],["Center",[0.0141421,0.0160002],1]],[["Center",1,[0,0],1],["Center",[0.0141421,0.0160002],1],["Center",[-1.74846e-009,0.0226277],1],["Center",[-0.0141421,0.0160002],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,0.0160002],1],["Center",[-0.02,-2.69833e-010],1],["Center",[-0.0141421,-0.0160002],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,-0.0160002],1],["Center",[3.49691e-009,-0.0226277],1],["Center",[0.0141421,-0.0160002],1]]]
                    },
                    "alpha": 0.22
                }
            }
        }
    },
    "model": "rhsafrf|addons|rhs_airweapons|rhs_pylon_m_fab500",
    "weight": 500,
    "mass": 500,
    "hardpoints": ["RHS_HP_FAB500"],
    "scope": 2,
    "count": 1,
    "initspeed": 0,
    "maxleadspeed": 5,
    "namesound": "",
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
    "simulation": "ProxyMagazines",
    # Class: CfgMagazines|Default|InventoryPlacements [Indent level: 1],
    "inventoryplacements": {
    },
    # Class: CfgMagazines|Default|Library [Indent level: 1],
    "library": {
        "libtextdesc": ""
    },
    "descriptionshort": "",
    "maxthrowholdtime": 2,
    "minthrowintensitycoef": 0.3,
    "maxthrowintensitycoef": 1.4,
    "quickreload": 0,
}