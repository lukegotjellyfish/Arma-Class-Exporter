rhs_mag_dagr_8 = {
    "count": 8,
    "displayname": "DAGR (M310)",
    "descriptionshort": "×8 Laser-homing 70mm rockets",
    "weight": 64,
    "hardpoints": ["RHS_HP_HELLFIRE_RACK","RHS_HP_LONGBOW_RACK","RHS_HP_MELB"],
    "model": "rhsusf|addons|rhsusf_airweapons|proxypylon|rhsusf_pylon_r_DAGR_8x",
    "mirrormissilesindexes": [2,1,4,3,6,5,8,7],
    # Ammo: CfgMagazines|rhs_mag_DAGR_4|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "RHS_Ammo_DAGR",
        "maverickweaponindexoffset": 80,
        "model": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_r_DAGR_fly",
        "proxyshape": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_r_DAGR",
        "hit": 300,
        "indirecthit": 50,
        "indirecthitrange": 6,
        "cost": 100,
        "maxspeed": 720,
        "irlock": 0,
        "airlock": 0,
        "laserlock": 1,
        "maxcontrolrange": 8000,
        "trackoversteer": 1,
        "tracklead": 1,
        "maneuvrability": 14,
        "timetolive": 20,
        "simulationstep": 0.01,
        "airfriction": 0.1,
        "sideairfriction": 0.3,
        "inittime": 0.002,
        "thrusttime": 1.57,
        "thrust": 825,
        "fusedistance": 50,
        "whistledist": 4,
        "muzzleeffect": "",
        "effectsmissileinit": "MissileDAR1",
        "effectsmissile": "rhs_missile1",
        "explosioneffects": "ATMissileExplosion",
        "weaponlocksystem": 4,
        "manualcontrol": 1,
        "aiammousageflags": "64 + 128+512",
        "autoseektarget": 1,
        "lockseekradius": 1000,
        "missilelockmaxdistance": 6000,
        "missilelockmindistance": 1000,
        "missilelockmaxspeed": 56,
        "missilelockcone": 25,
        "missilekeeplockedcone": 25,
        "flightprofiles": ["Direct","LoalDistance"],
        # Class: CfgAmmo|RHS_Ammo_DAGR|Direct [Indent level: 1],
        "direct": {
        },
        # Class: CfgAmmo|RHS_Ammo_DAGR|LoalDistance [Indent level: 1],
        "loaldistance": {
            "lockseekdistancefromparent": 200
        },
        # Class: CfgAmmo|RHS_Ammo_DAGR|Components [Indent level: 1],
        "components": {
            # Class: CfgAmmo|RHS_Ammo_DAGR|Components|SensorsManagerComponent [Indent level: 2]
            "sensorsmanagercomponent": {
                # Class: CfgAmmo|RHS_Ammo_DAGR|Components|SensorsManagerComponent|Components [Indent level: 3]
                "components": {
                    # Class: CfgAmmo|RHS_Ammo_DAGR|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4]
                    "lasersensorcomponent": {
                        # Class: CfgAmmo|RHS_Ammo_DAGR|Components|SensorsManagerComponent|Components|LaserSensorComponent|AirTarget [Indent level: 5]
                        "airtarget": {
                            "minrange": 5000,
                            "maxrange": 5000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        # Class: CfgAmmo|RHS_Ammo_DAGR|Components|SensorsManagerComponent|Components|LaserSensorComponent|GroundTarget [Indent level: 5],
                        "groundtarget": {
                            "minrange": 5000,
                            "maxrange": 5000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        "maxtrackablespeed": 55,
                        "anglerangehorizontal": 14,
                        "anglerangevertical": 14,
                        "maxgroundnoisedistance": 0,
                        "maxfogseethrough": 0.3,
                        "componenttype": "LaserSensorComponent",
                        "typerecognitiondistance": 0,
                        "color": [1,1,1,0],
                        "allowsmarking": 1,
                        "groundnoisedistancecoef": -1,
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
        # Class: CfgAmmo|RHS_Ammo_DAGR|CamShakeExplode [Indent level: 1],
        "camshakeexplode": {
            "power": 24.4,
            "duration": 2.2,
            "frequency": 20,
            "distance": 208.363
        },
        # Class: CfgAmmo|RHS_Ammo_DAGR|CamShakeHit [Indent level: 1],
        "camshakehit": {
            "power": 122,
            "duration": 0.6,
            "frequency": 20,
            "distance": 1
        },
        # Class: CfgAmmo|RHS_Ammo_DAGR|CamShakeFire [Indent level: 1],
        "camshakefire": {
            "power": 3.32346,
            "duration": 2.2,
            "frequency": 20,
            "distance": 88.3629
        },
        # Class: CfgAmmo|RHS_Ammo_DAGR|CamShakePlayerFire [Indent level: 1],
        "camshakeplayerfire": {
            "power": 2,
            "duration": 0.1,
            "frequency": 20,
            "distance": 1
        },
        "soundhit1": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_01",2.51189,1,2000],
        "soundhit2": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_02",2.51189,1,2000],
        "soundhit3": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_03",2.51189,1,2000],
        "multisoundhit": ["soundHit1",0.34,"soundHit2",0.33,"soundHit3",0.33],
        "explosionsoundeffect": "DefaultExplosion",
        "soundfly": ["",1,1,400],
        "soundengine": ["",1,1,50],
        "supersoniccracknear": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_close",0.398107,1,20],
        "supersoniccrackfar": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_50meters",0.316228,1,50],
        "cratereffects": "ATMissileCrater",
        "deflecting": 0,
        "cmimmunity": 0.9,
        "dangerradiushit": -1,
        "suppressionradiushit": 30,
        # Class: CfgAmmo|MissileBase|HitEffects [Indent level: 1],
        "hiteffects": {
            "hitwater": "ImpactEffectsWaterRocket"
        },
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
        "explosionangle": 60,
        "explosiondir": "explosionDir",
        "explosionpos": "explosionPos",
        "explosioneffectsdir": "explosionDir",
        "minimumsafezone": 0.1,
        "soundtrigger": [],
        "soundactivation": [],
        "sounddeactivation": [],
        "mintimetolive": 0,
        "nvlock": 0,
        "artillerylock": 0,
        "hitonwater": 0,
        "locktype": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
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
    "mindamageforcamshakehit": "RHS_Ammo_DAGR",
    "displaynameshort": "SALH",
    "pylonweapon": "RHS_weap_DAGR_Launcher",
    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_ammoname [Indent level: 2]
        "rhs_a10a_ammoname": {
            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_ammoname|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_ammoname|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_ammoname|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "LG",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.005,0.02],1],
                    "right": [[0.05,0.02],1],
                    "down": [[0.005,0.105],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_box [Indent level: 2],
        "rhs_a10a_box": {
            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_box|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_box|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_box|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "PylonAmmoRelative>=0.001",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_box|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,-0.04],1],[[0.015,-0.04],1],[[0.015,0.04],1],[[-0.015,0.04],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_box|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_box|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,0.05],1],[[0.015,0.05],1],[[0.015,0.13],1],[[-0.015,0.13],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_box|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative<=0",
                    "color": [0.87,0,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_a10a_box|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.02,0.05],1],[[0.05,0.05],1],[[0.05,0.13],1],[[0.02,0.13],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_ah64_ammoname [Indent level: 2],
        "rhs_ah64_ammoname": {
            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_ah64_ammoname|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_ah64_ammoname|Draw [Indent level: 3],
            "draw": {
                "condition": "pylonSelected",
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_ah64_ammoname|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "LG",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.005,0.02],1],
                    "right": [[0.05,0.02],1],
                    "down": [[0.005,0.105],1]
                },
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|rhs_ah64_ammoname|Draw|PylonAmmo [Indent level: 4],
                "pylonammo": {
                    "type": "text",
                    "source": "ammo",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.015,0.02],1],
                    "right": [[0.06,0.02],1],
                    "down": [[0.015,0.105],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD [Indent level: 2],
        "rhs_a29_weap_mfd": {
            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default [Indent level: 4]
                "default": {
                    "condition": "PylonAmmoRelative>0",
                    "color": [0,0.12,0],
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup [Indent level: 5],
                    "backgroundgroup": {
                        "color": [0,0,0],
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup|Background [Indent level: 6],
                        "background": {
                            "type": "polygon",
                            "points": [[[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1]]]
                        }
                    },
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1],[[-0.0225,-0.06],1],[],[[-0.0225,-0.06],1],[[-0.02025,-0.06625],1],[[-0.018,-0.0675],1],[[-0.01575,-0.06625],1],[[-0.0135,-0.06],1],[],[[-0.0135,-0.06],1],[[-0.01125,-0.06625],1],[[-0.009,-0.0675],1],[[-0.00675,-0.06625],1],[[-0.0045,-0.06],1],[],[[-0.0045,-0.06],1],[[-0.00225,-0.06625],1],[[-1.86265e-009,-0.0675],1],[[0.00225,-0.06625],1],[[0.0045,-0.06],1],[],[[0.0045,-0.06],1],[[0.00675,-0.06625],1],[[0.009,-0.0675],1],[[0.01125,-0.06625],1],[[0.0135,-0.06],1],[],[[0.0135,-0.06],1],[[0.01575,-0.06625],1],[[0.018,-0.0675],1],[[0.02025,-0.06625],1],[[0.0225,-0.06],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "LG",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.03+-0.03",-0.01],1],
                        "right": [[0.015,-0.01],1],
                        "down": [["0.03+-0.03",0.005],1]
                    }
                },
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "color": [0.99,0.94,0.59],
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "width": 8,
                        "type": "line",
                        "points": [[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1],[[-0.0225,-0.06],1],[],[[-0.0225,-0.06],1],[[-0.02025,-0.06625],1],[[-0.018,-0.0675],1],[[-0.01575,-0.06625],1],[[-0.0135,-0.06],1],[],[[-0.0135,-0.06],1],[[-0.01125,-0.06625],1],[[-0.009,-0.0675],1],[[-0.00675,-0.06625],1],[[-0.0045,-0.06],1],[],[[-0.0045,-0.06],1],[[-0.00225,-0.06625],1],[[-1.86265e-009,-0.0675],1],[[0.00225,-0.06625],1],[[0.0045,-0.06],1],[],[[0.0045,-0.06],1],[[0.00675,-0.06625],1],[[0.009,-0.0675],1],[[0.01125,-0.06625],1],[[0.0135,-0.06],1],[],[[0.0135,-0.06],1],[[0.01575,-0.06625],1],[[0.018,-0.0675],1],[[0.02025,-0.06625],1],[[0.0225,-0.06],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BackgroundGroup [Indent level: 5],
                    "backgroundgroup": {
                        "color": [0.99,0.94,0.59],
                        "alpha": 0.1,
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BackgroundGroup|Background [Indent level: 6],
                        "background": {
                            "type": "polygon",
                            "points": [[[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1]]]
                        }
                    },
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText [Indent level: 5],
                    "blacktext": {
                        "color": [0,0,0],
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText1 [Indent level: 6],
                        "pylontext1": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText2 [Indent level: 6],
                        "pylontext2": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText3 [Indent level: 6],
                        "pylontext3": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText4 [Indent level: 6],
                        "pylontext4": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText5 [Indent level: 6],
                        "pylontext5": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText6 [Indent level: 6],
                        "pylontext6": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        "condition": "PylonAmmoRelative>0",
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup [Indent level: 5],
                        "backgroundgroup": {
                            "color": [0,0,0],
                            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup|Background [Indent level: 6],
                            "background": {
                                "type": "polygon",
                                "points": [[[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1]]]
                            }
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|Shape [Indent level: 5],
                        "shape": {
                            "type": "line",
                            "width": 4,
                            "points": [[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1],[[-0.0225,-0.06],1],[],[[-0.0225,-0.06],1],[[-0.02025,-0.06625],1],[[-0.018,-0.0675],1],[[-0.01575,-0.06625],1],[[-0.0135,-0.06],1],[],[[-0.0135,-0.06],1],[[-0.01125,-0.06625],1],[[-0.009,-0.0675],1],[[-0.00675,-0.06625],1],[[-0.0045,-0.06],1],[],[[-0.0045,-0.06],1],[[-0.00225,-0.06625],1],[[-1.86265e-009,-0.0675],1],[[0.00225,-0.06625],1],[[0.0045,-0.06],1],[],[[0.0045,-0.06],1],[[0.00675,-0.06625],1],[[0.009,-0.0675],1],[[0.01125,-0.06625],1],[[0.0135,-0.06],1],[],[[0.0135,-0.06],1],[[0.01575,-0.06625],1],[[0.018,-0.0675],1],[[0.02025,-0.06625],1],[[0.0225,-0.06],1],[]]
                        }
                    },
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "LG",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.03+-0.03",-0.01],1],
                        "right": [[0.015,-0.01],1],
                        "down": [["0.03+-0.03",0.005],1]
                    }
                },
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative <= 0",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "width": 8,
                        "type": "line",
                        "points": [[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1],[[-0.0225,-0.06],1],[],[[-0.0225,-0.06],1],[[-0.02025,-0.06625],1],[[-0.018,-0.0675],1],[[-0.01575,-0.06625],1],[[-0.0135,-0.06],1],[],[[-0.0135,-0.06],1],[[-0.01125,-0.06625],1],[[-0.009,-0.0675],1],[[-0.00675,-0.06625],1],[[-0.0045,-0.06],1],[],[[-0.0045,-0.06],1],[[-0.00225,-0.06625],1],[[-1.86265e-009,-0.0675],1],[[0.00225,-0.06625],1],[[0.0045,-0.06],1],[],[[0.0045,-0.06],1],[[0.00675,-0.06625],1],[[0.009,-0.0675],1],[[0.01125,-0.06625],1],[[0.0135,-0.06],1],[],[[0.0135,-0.06],1],[[0.01575,-0.06625],1],[[0.018,-0.0675],1],[[0.02025,-0.06625],1],[[0.0225,-0.06],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText [Indent level: 5],
                    "blacktext": {
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText1 [Indent level: 6]
                        "pylontext1": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText2 [Indent level: 6],
                        "pylontext2": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText3 [Indent level: 6],
                        "pylontext3": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText4 [Indent level: 6],
                        "pylontext4": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText5 [Indent level: 6],
                        "pylontext5": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText6 [Indent level: 6],
                        "pylontext6": {
                            "type": "text",
                            "source": "static",
                            "text": "LG",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        "color": [0,0,0],
                        "condition": "PylonAmmoRelative>0",
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup [Indent level: 5],
                        "backgroundgroup": {
                            "color": [0,0,0],
                            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup|Background [Indent level: 6],
                            "background": {
                                "type": "polygon",
                                "points": [[[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1]]]
                            }
                        },
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|Shape [Indent level: 5],
                        "shape": {
                            "type": "line",
                            "width": 4,
                            "points": [[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1],[[-0.0225,-0.06],1],[],[[-0.0225,-0.06],1],[[-0.02025,-0.06625],1],[[-0.018,-0.0675],1],[[-0.01575,-0.06625],1],[[-0.0135,-0.06],1],[],[[-0.0135,-0.06],1],[[-0.01125,-0.06625],1],[[-0.009,-0.0675],1],[[-0.00675,-0.06625],1],[[-0.0045,-0.06],1],[],[[-0.0045,-0.06],1],[[-0.00225,-0.06625],1],[[-1.86265e-009,-0.0675],1],[[0.00225,-0.06625],1],[[0.0045,-0.06],1],[],[[0.0045,-0.06],1],[[0.00675,-0.06625],1],[[0.009,-0.0675],1],[[0.01125,-0.06625],1],[[0.0135,-0.06],1],[],[[0.0135,-0.06],1],[[0.01575,-0.06625],1],[[0.018,-0.0675],1],[[0.02025,-0.06625],1],[[0.0225,-0.06],1],[]]
                        }
                    },
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BackgroundGroup [Indent level: 5],
                    "backgroundgroup": {
                        "color": [0.99,0.94,0.59],
                        "alpha": 0.1,
                        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BackgroundGroup|Background [Indent level: 6],
                        "background": {
                            "type": "polygon",
                            "points": [[[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1]]]
                        }
                    },
                    # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "LG",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.03+-0.03",-0.01],1],
                        "right": [[0.015,-0.01],1],
                        "down": [["0.03+-0.03",0.005],1]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD_Inventory [Indent level: 2],
        "rhs_a29_weap_mfd_inventory": {
            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD_Inventory|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonText1 [Indent level: 4]
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "DAGR",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0,0.02],1],
                    "right": [[0.025,0.02],1],
                    "down": [[0,0.04],1]
                },
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonText2 [Indent level: 4],
                "pylontext2": {
                    "type": "text",
                    "source": "static",
                    "text": "LG",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0,0.054],1],
                    "right": [[0.025,0.054],1],
                    "down": [[0,0.074],1]
                },
                # Class: CfgMagazines|rhs_mag_DAGR_4|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonAmo [Indent level: 4],
                "pylonamo": {
                    "type": "text",
                    "source": "pylonammo",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "left",
                    "pos": [[0.16,0.054],1],
                    "right": [[0.185,0.054],1],
                    "down": [[0.16,0.074],1]
                }
            }
        }
    },
    "author": "Bohemia Interactive",
    "scope": 2,
    "initspeed": 0,
    "maxleadspeed": 41.6667,
    "namesound": "missiles",
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