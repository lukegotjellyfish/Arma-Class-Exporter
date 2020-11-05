rhs_mag_ffar_7_usaf = {
    "scope": 2,
    "displayname": "M151 FFAR (LAU-68)",
    "displaynameshort": "HE",
    "descriptionshort": "×7 10lb HE FFAR",
    # Ammo: CfgMagazines|rhs_mag_FFAR_7_USAF|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "rhs_ammo_FFAR_M151",
        "maverickweapon": 1,
        "maverickweaponindexoffset": 0,
        "model": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_r_M151_FFAR_fly",
        "proxyshape": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_r_M151",
        "hit": 190,
        "indirecthit": 50,
        "indirecthitrange": 10,
        "cost": 75,
        "maxspeed": 740,
        "thrusttime": 1.1,
        "thrust": 800,
        "sideairfriction": 0.004,
        "timetolive": 60,
        "fusedistance": 40,
        "whistledist": 24,
        "warheadname": "HE",
        "manualcontrol": 0,
        "maxcontrolrange": 0,
        "airlock": 0,
        "irlock": 0,
        "laserlock": 0,
        "nvlock": 0,
        "weaponlocksystem": 0,
        "aiammousageflags": "64 + 128",
        "missilelockmindistance": 500,
        "missilelockmaxdistance": 3000,
        "inittime": 0.002,
        "airfriction": 0.09,
        "maneuvrability": 0,
        "effectsmissileinit": "PylonBackEffectsFFAR",
        "muzzleeffect": "",
        "soundfly": ["A3|Sounds_F|weapons|Rockets|rocket_fly_1",0.630957,1.2,1700],
        # Class: CfgAmmo|Rocket_04_HE_F|CamShakeExplode [Indent level: 1],
        "camshakeexplode": {
            "power": 16,
            "duration": 1.8,
            "frequency": 20,
            "distance": 191.554
        },
        # Class: CfgAmmo|Rocket_04_HE_F|CamShakeHit [Indent level: 1],
        "camshakehit": {
            "power": 80,
            "duration": 0.6,
            "frequency": 20,
            "distance": 1
        },
        # Class: CfgAmmo|Rocket_04_HE_F|CamShakeFire [Indent level: 1],
        "camshakefire": {
            "power": 2.9907,
            "duration": 1.8,
            "frequency": 20,
            "distance": 71.5542
        },
        # Class: CfgAmmo|Rocket_04_HE_F|CamShakePlayerFire [Indent level: 1],
        "camshakeplayerfire": {
            "power": 2,
            "duration": 0.1,
            "frequency": 20,
            "distance": 1
        },
        "soundsetexplosion": ["RocketsLight_Exp_SoundSet","RocketsLight_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "simulationstep": 0.01,
        "soundhit1": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_01",2.51189,1,2000],
        "soundhit2": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_02",2.51189,1,2000],
        "soundhit3": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_03",2.51189,1,2000],
        "multisoundhit": ["soundHit1",0.34,"soundHit2",0.33,"soundHit3",0.33],
        "explosionsoundeffect": "DefaultExplosion",
        "soundengine": ["",1,1,50],
        "supersoniccracknear": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_close",0.398107,1,20],
        "supersoniccrackfar": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_50meters",0.316228,1,50],
        "cratereffects": "ATMissileCrater",
        "explosioneffects": "ATMissileExplosion",
        "effectsmissile": "missile4",
        "deflecting": 0,
        "cmimmunity": 0.9,
        "dangerradiushit": -1,
        "suppressionradiushit": 30,
        # Class: CfgAmmo|MissileBase|HitEffects [Indent level: 1],
        "hiteffects": {
            "hitwater": "ImpactEffectsWaterRocket"
        },
        # Class: CfgAmmo|MissileBase|Components [Indent level: 1],
        "components": {
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
        "missilelockcone": 50,
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
        "artillerylock": 0,
        "hitonwater": 0,
        "lockseekradius": 100,
        "tracklead": 1,
        "trackoversteer": 1,
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
    "mindamageforcamshakehit": "rhs_ammo_FFAR_M151",
    "count": 7,
    "initspeed": 44,
    "maxleadspeed": 200,
    "namesound": "rockets",
    "hardpoints": ["RHS_HP_FFAR_USAF","RHS_HP_FFAR_USAF_green"],
    "pylonweapon": "rhs_weap_FFARLauncher",
    "model": "rhsusf|addons|rhsusf_airweapons|proxypylon|rhsusf_pylon_r_FFAR_7x_LAU68",
    "displaynamemfdformat": "RKT|%2|%1",
    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_ammoname [Indent level: 2]
        "rhs_a10a_ammoname": {
            # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_ammoname|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_ammoname|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_ammoname|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "RKT",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.005,0.02],1],
                    "right": [[0.05,0.02],1],
                    "down": [[0.005,0.105],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_box [Indent level: 2],
        "rhs_a10a_box": {
            # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_box|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_box|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_box|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "PylonAmmoRelative>=0.001",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_box|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,-0.04],1],[[0.015,-0.04],1],[[0.015,0.04],1],[[-0.015,0.04],1]],[[[0.02,-0.04],1],[[0.05,-0.04],1],[[0.05,0.04],1],[[0.02,0.04],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_box|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_box|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,0.05],1],[[0.015,0.05],1],[[0.015,0.13],1],[[-0.015,0.13],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_box|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative<=0",
                    "color": [0.87,0,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|rhs_a10a_box|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.02,0.05],1],[[0.05,0.05],1],[[0.05,0.13],1],[[0.02,0.13],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD [Indent level: 2],
        "rhs_a29_weap_mfd": {
            # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default [Indent level: 4]
                "default": {
                    "condition": "PylonAmmoRelative>0",
                    "color": [0,0.12,0],
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup [Indent level: 5],
                    "backgroundgroup": {
                        "color": [0,0,0],
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup|Background [Indent level: 6],
                        "background": {
                            "type": "polygon",
                            "points": [[[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1]]]
                        }
                    },
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1],[[-0.0225,-0.06],1],[],[[-0.0225,-0.06],1],[[-0.02025,-0.06625],1],[[-0.018,-0.0675],1],[[-0.01575,-0.06625],1],[[-0.0135,-0.06],1],[],[[-0.0135,-0.06],1],[[-0.01125,-0.06625],1],[[-0.009,-0.0675],1],[[-0.00675,-0.06625],1],[[-0.0045,-0.06],1],[],[[-0.0045,-0.06],1],[[-0.00225,-0.06625],1],[[-1.86265e-009,-0.0675],1],[[0.00225,-0.06625],1],[[0.0045,-0.06],1],[],[[0.0045,-0.06],1],[[0.00675,-0.06625],1],[[0.009,-0.0675],1],[[0.01125,-0.06625],1],[[0.0135,-0.06],1],[],[[0.0135,-0.06],1],[[0.01575,-0.06625],1],[[0.018,-0.0675],1],[[0.02025,-0.06625],1],[[0.0225,-0.06],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "6RC",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.03+-0.03",-0.01],1],
                        "right": [[0.015,-0.01],1],
                        "down": [["0.03+-0.03",0.005],1]
                    }
                },
                # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "color": [0.99,0.94,0.59],
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "width": 8,
                        "type": "line",
                        "points": [[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1],[[-0.0225,-0.06],1],[],[[-0.0225,-0.06],1],[[-0.02025,-0.06625],1],[[-0.018,-0.0675],1],[[-0.01575,-0.06625],1],[[-0.0135,-0.06],1],[],[[-0.0135,-0.06],1],[[-0.01125,-0.06625],1],[[-0.009,-0.0675],1],[[-0.00675,-0.06625],1],[[-0.0045,-0.06],1],[],[[-0.0045,-0.06],1],[[-0.00225,-0.06625],1],[[-1.86265e-009,-0.0675],1],[[0.00225,-0.06625],1],[[0.0045,-0.06],1],[],[[0.0045,-0.06],1],[[0.00675,-0.06625],1],[[0.009,-0.0675],1],[[0.01125,-0.06625],1],[[0.0135,-0.06],1],[],[[0.0135,-0.06],1],[[0.01575,-0.06625],1],[[0.018,-0.0675],1],[[0.02025,-0.06625],1],[[0.0225,-0.06],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BackgroundGroup [Indent level: 5],
                    "backgroundgroup": {
                        "color": [0.99,0.94,0.59],
                        "alpha": 0.1,
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BackgroundGroup|Background [Indent level: 6],
                        "background": {
                            "type": "polygon",
                            "points": [[[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1]]]
                        }
                    },
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText [Indent level: 5],
                    "blacktext": {
                        "color": [0,0,0],
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText1 [Indent level: 6],
                        "pylontext1": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText2 [Indent level: 6],
                        "pylontext2": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText3 [Indent level: 6],
                        "pylontext3": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText4 [Indent level: 6],
                        "pylontext4": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText5 [Indent level: 6],
                        "pylontext5": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BlackText|PylonText6 [Indent level: 6],
                        "pylontext6": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        "condition": "PylonAmmoRelative>0",
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup [Indent level: 5],
                        "backgroundgroup": {
                            "color": [0,0,0],
                            # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup|Background [Indent level: 6],
                            "background": {
                                "type": "polygon",
                                "points": [[[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1]]]
                            }
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|Shape [Indent level: 5],
                        "shape": {
                            "type": "line",
                            "width": 4,
                            "points": [[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1],[[-0.0225,-0.06],1],[],[[-0.0225,-0.06],1],[[-0.02025,-0.06625],1],[[-0.018,-0.0675],1],[[-0.01575,-0.06625],1],[[-0.0135,-0.06],1],[],[[-0.0135,-0.06],1],[[-0.01125,-0.06625],1],[[-0.009,-0.0675],1],[[-0.00675,-0.06625],1],[[-0.0045,-0.06],1],[],[[-0.0045,-0.06],1],[[-0.00225,-0.06625],1],[[-1.86265e-009,-0.0675],1],[[0.00225,-0.06625],1],[[0.0045,-0.06],1],[],[[0.0045,-0.06],1],[[0.00675,-0.06625],1],[[0.009,-0.0675],1],[[0.01125,-0.06625],1],[[0.0135,-0.06],1],[],[[0.0135,-0.06],1],[[0.01575,-0.06625],1],[[0.018,-0.0675],1],[[0.02025,-0.06625],1],[[0.0225,-0.06],1],[]]
                        }
                    },
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "6RC",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [["0.03+-0.03",-0.01],1],
                        "right": [[0.015,-0.01],1],
                        "down": [["0.03+-0.03",0.005],1]
                    }
                },
                # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative <= 0",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "width": 8,
                        "type": "line",
                        "points": [[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1],[[-0.0225,-0.06],1],[],[[-0.0225,-0.06],1],[[-0.02025,-0.06625],1],[[-0.018,-0.0675],1],[[-0.01575,-0.06625],1],[[-0.0135,-0.06],1],[],[[-0.0135,-0.06],1],[[-0.01125,-0.06625],1],[[-0.009,-0.0675],1],[[-0.00675,-0.06625],1],[[-0.0045,-0.06],1],[],[[-0.0045,-0.06],1],[[-0.00225,-0.06625],1],[[-1.86265e-009,-0.0675],1],[[0.00225,-0.06625],1],[[0.0045,-0.06],1],[],[[0.0045,-0.06],1],[[0.00675,-0.06625],1],[[0.009,-0.0675],1],[[0.01125,-0.06625],1],[[0.0135,-0.06],1],[],[[0.0135,-0.06],1],[[0.01575,-0.06625],1],[[0.018,-0.0675],1],[[0.02025,-0.06625],1],[[0.0225,-0.06],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText [Indent level: 5],
                    "blacktext": {
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText1 [Indent level: 6]
                        "pylontext1": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText2 [Indent level: 6],
                        "pylontext2": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText3 [Indent level: 6],
                        "pylontext3": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText4 [Indent level: 6],
                        "pylontext4": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText5 [Indent level: 6],
                        "pylontext5": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|BlackText|PylonText6 [Indent level: 6],
                        "pylontext6": {
                            "type": "text",
                            "source": "static",
                            "text": "6RC",
                            "scale": 1,
                            "sourcescale": 1,
                            "align": "center",
                            "pos": [["0.03+-0.03",-0.01],1],
                            "right": [[0.015,-0.01],1],
                            "down": [["0.03+-0.03",0.005],1]
                        },
                        "color": [0,0,0],
                        "condition": "PylonAmmoRelative>0",
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup [Indent level: 5],
                        "backgroundgroup": {
                            "color": [0,0,0],
                            # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|BackgroundGroup|Background [Indent level: 6],
                            "background": {
                                "type": "polygon",
                                "points": [[[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1]]]
                            }
                        },
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|Shape [Indent level: 5],
                        "shape": {
                            "type": "line",
                            "width": 4,
                            "points": [[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1],[[-0.0225,-0.06],1],[],[[-0.0225,-0.06],1],[[-0.02025,-0.06625],1],[[-0.018,-0.0675],1],[[-0.01575,-0.06625],1],[[-0.0135,-0.06],1],[],[[-0.0135,-0.06],1],[[-0.01125,-0.06625],1],[[-0.009,-0.0675],1],[[-0.00675,-0.06625],1],[[-0.0045,-0.06],1],[],[[-0.0045,-0.06],1],[[-0.00225,-0.06625],1],[[-1.86265e-009,-0.0675],1],[[0.00225,-0.06625],1],[[0.0045,-0.06],1],[],[[0.0045,-0.06],1],[[0.00675,-0.06625],1],[[0.009,-0.0675],1],[[0.01125,-0.06625],1],[[0.0135,-0.06],1],[],[[0.0135,-0.06],1],[[0.01575,-0.06625],1],[[0.018,-0.0675],1],[[0.02025,-0.06625],1],[[0.0225,-0.06],1],[]]
                        }
                    },
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BackgroundGroup [Indent level: 5],
                    "backgroundgroup": {
                        "color": [0.99,0.94,0.59],
                        "alpha": 0.1,
                        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|BackgroundGroup|Background [Indent level: 6],
                        "background": {
                            "type": "polygon",
                            "points": [[[[-0.0225,-0.06],1],[[0.0225,-0.06],1],[[0.0225,0.03],1],[[-0.0225,0.03],1]]]
                        }
                    },
                    # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "6RC",
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
        # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD_Inventory [Indent level: 2],
        "rhs_a29_weap_mfd_inventory": {
            # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD_Inventory|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonText1 [Indent level: 4]
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "M151",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0,0.02],1],
                    "right": [[0.025,0.02],1],
                    "down": [[0,0.04],1]
                },
                # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonText2 [Indent level: 4],
                "pylontext2": {
                    "type": "text",
                    "source": "static",
                    "text": "6RC",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0,0.054],1],
                    "right": [[0.025,0.054],1],
                    "down": [[0,0.074],1]
                },
                # Class: CfgMagazines|rhs_mag_FFAR_7_USAF|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonAmo [Indent level: 4],
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