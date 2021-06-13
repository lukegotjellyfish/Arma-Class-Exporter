rhs_mag_ub16_ka52_s5 = {
    "model": "rhsafrf|addons|rhs_a2port_air|data|rhs_pylon_r_ub16_ka52.p3d",
    "hardpoints": ["RHS_HP_UB16_KA52"],
    # Ammo: CfgMagazines|rhs_mag_ub16_s5|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "rhs_ammo_s5",
        "submunitionammo": "",
        "proxyshape": "rhsafrf|addons|rhs_airweapons|s5_rockets|rhs_r_s5m1",
        "model": "rhsafrf|addons|rhs_airweapons|s5_rockets|rhs_r_s5m1_fly",
        "hit": 220,
        "indirecthit": 20,
        "indirecthitrange": 9,
        "inittime": 0.02,
        "thrusttime": 0.675,
        "timetolive": 12.5,
        "sideairfriction": 0.004,
        "missilelockmaxdistance": 1800,
        # Class: CfgAmmo|rhs_ammo_s5|CamShakeExplode [Indent level: 1],
        "camshakeexplode": {
            "power": 11.4,
            "duration": 1.6,
            "frequency": 20,
            "distance": 140.399
        },
        # Class: CfgAmmo|rhs_ammo_s5|CamShakeHit [Indent level: 1],
        "camshakehit": {
            "power": 57,
            "duration": 0.6,
            "frequency": 20,
            "distance": 1
        },
        # Class: CfgAmmo|rhs_ammo_s5|CamShakeFire [Indent level: 1],
        "camshakefire": {
            "power": 2.7477,
            "duration": 1.6,
            "frequency": 20,
            "distance": 60.3987
        },
        # Class: CfgAmmo|rhs_ammo_s5|CamShakePlayerFire [Indent level: 1],
        "camshakeplayerfire": {
            "power": 2,
            "duration": 0.1,
            "frequency": 20,
            "distance": 1
        },
        "aiammousageflags": "64+128+512",
        "cost": 100,
        "effectsmissile": "RHS_Rocket_Fired",
        "effectsmissileinit": "RHS_Rocket_Init",
        "soundfly": ["A3|Sounds_F|weapons|Rockets|rocket_fly_2",1,1.5,700],
        "submunitiondirectiontype": "SubmunitionModelDirection",
        "submunitioninitialoffset": [0,0,-0.1],
        "submunitionparentspeedcoef": 0,
        "submunitioninitspeed": 1053,
        "triggeronimpact": 1,
        "deleteparentwhentriggered": 0,
        "missilelockmindistance": 700,
        "warheadname": "HE",
        "maxspeed": 590,
        "thrust": 1060,
        "airfriction": 0.09,
        "fusedistance": 50,
        "whistledist": 30,
        "muzzleeffect": "",
        "simulation": "shotMissile",
        "soundsetexplosion": ["RocketsMedium_Exp_SoundSet","RocketsMedium_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "dangerradiushit": -1,
        "suppressionradiushit": 30,
        "soundhit": ["A3|Sounds_F|weapons|Rockets|explosion_missile_02",2.51189,1,2500],
        "explosionsoundeffect": "DefaultExplosion",
        "soundengine": ["",1,1,20],
        "supersoniccracknear": ["",1,1,50],
        "supersoniccrackfar": ["",1,1,150],
        "cratereffects": "HERocketCrater",
        "explosioneffects": "HERocketExplosion",
        # Class: CfgAmmo|RocketBase|HitEffects [Indent level: 1],
        "hiteffects": {
            "hitwater": "ImpactEffectsWaterRocket"
        },
        # Class: CfgAmmo|RocketBase|EventHandlers [Indent level: 1],
        "eventhandlers": {
            # Class: CfgAmmo|RocketBase|EventHandlers|RHS_APS_FiredEH [Indent level: 2]
            "rhs_aps_firedeh": {
                "fired": "_this spawn rhs_fnc_aps_missileFired"
            }
        },
        "simulationstep": 0.05,
        "maneuvrability": 0,
        "maxcontrolrange": 0,
        "visiblefire": 32,
        "audiblefire": 32,
        "visiblefiretime": 20,
        "deflecting": 5,
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
        "irlock": 0,
        "airlock": 0,
        "laserlock": 0,
        "nvlock": 0,
        "artillerylock": 0,
        "hitonwater": 0,
        "lockseekradius": 100,
        "manualcontrol": 0,
        "tracklead": 1,
        "trackoversteer": 1,
        "missilelockcone": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "locktype": 0,
        "maverickweaponindexoffset": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "autoseektarget": 0,
        "shootdistraction": -1,
        "explosiontime": 0,
        "icon": "",
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
    "mindamageforcamshakehit": "rhs_ammo_s5",
    "count": 16,
    "mass": 118,
    "weight": 118,
    "pylonweapon": "rhs_weap_s5",
    "scope": 2,
    "displayname": "S-5 GP",
    "displaynameshort": "S-5",
    "descriptionshort": "General purpose",
    "maxleadspeed": 200,
    "initspeed": 44,
    "namesound": "rockets",
    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_ammoname [Indent level: 2]
        "rhs_rus_ammoname": {
            # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_ammoname|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_ammoname|Draw [Indent level: 3],
            "draw": {
                "condition": "PylonSelected",
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_ammoname|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "С5",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[-0.005,0.02],1],
                    "right": [[0.045,0.02],1],
                    "down": [[-0.005,0.065],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_ammoname_right [Indent level: 2],
        "rhs_rus_ammoname_right": {
            # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_ammoname_right|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_ammoname_right|Draw [Indent level: 3],
            "draw": {
                "condition": "PylonSelected",
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_ammoname_right|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "С5",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[-0.005,0.02],1],
                    "right": [[0.045,0.02],1],
                    "down": [[-0.005,0.065],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_su25_box [Indent level: 2],
        "rhs_su25_box": {
            # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_su25_box|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_su25_box|Draw [Indent level: 3],
            "draw": {
                "condition": "1-pylonMagazineEmpty",
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_su25_box|Draw|Shape [Indent level: 4],
                "shape": {
                    "type": "polygon",
                    "width": 4,
                    "points": [[[[-0.022,-0.04],1],[[0.022,-0.04],1],[[0.022,0.04],1],[[-0.022,0.04],1]]]
                },
                # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_su25_box|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.58,0.23,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_su25_box|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.022,0.18],1],[[0.022,0.18],1],[[0.022,0.26],1],[[-0.022,0.26],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle [Indent level: 2],
        "rhs_rus_circle": {
            # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Bones [Indent level: 3]
            "bones": {
                # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Bones|Center [Indent level: 4]
                "center": {
                    "type": "fixed",
                    "pos": [0,0]
                }
            },
            # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "1-PylonSelected-pylonMagazineEmpty",
                    "color": [1,1,1],
                    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Default|PylonValue1 [Indent level: 5],
                    "pylonvalue1": {
                        "type": "text",
                        "source": "pylonAmmo",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "С5",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.12],1],
                        "right": [[0.035,0.12],1],
                        "down": [[-0.005,0.16],1]
                    },
                    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0305474],1],["Center",[0.0135,-0.0264541],1],["Center",[0.023382,-0.0152737],1],["Center",[0.027,0],1],["Center",[0.023382,0.0152737],1],["Center",[0.0135,0.0264541],1],["Center",[0,0.0305474],1],["Center",[-0.0135,0.0264541],1],["Center",[-0.023382,0.0152737],1],["Center",[-0.027,0],1],["Center",[-0.023382,-0.0152737],1],["Center",[-0.0135,-0.0264541],1],["Center",[0,-0.0305474],1],[],["Center",[0.0124097,-0.0140402],1],["Center",[0.0105005,-0.0118802],1],[],["Center",[0.01755,8.67926e-010],1],["Center",[0.01485,7.34399e-010],1],[],["Center",[0.0124097,0.0140402],1],["Center",[0.0105005,0.0118802],1],[],["Center",[-1.53427e-009,0.0198558],1],["Center",[-1.29823e-009,0.0168011],1],[],["Center",[-0.0124097,0.0140402],1],["Center",[-0.0105005,0.0118802],1],[],["Center",[-0.01755,-2.36779e-010],1],["Center",[-0.01485,-2.00351e-010],1],[],["Center",[-0.0124097,-0.0140402],1],["Center",[-0.0105005,-0.0118802],1],[],["Center",[3.06854e-009,-0.0198558],1],["Center",[2.59646e-009,-0.0168011],1],[],["Center",[0.00668216,-0.00756011],1],["Center",[0.00477297,-0.00540008],1],[],["Center",[0.00668216,0.00756011],1],["Center",[0.00477297,0.00540008],1],[],["Center",[-0.00668216,0.00756011],1],["Center",[-0.00477297,0.00540008],1],[],["Center",[-0.00668216,-0.00756011],1],["Center",[-0.00477297,-0.00540008],1],[]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Selected|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "С5",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.12],1],
                        "right": [[0.035,0.12],1],
                        "down": [[-0.005,0.16],1]
                    },
                    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Selected|PylonValue1 [Indent level: 5],
                    "pylonvalue1": {
                        "type": "text",
                        "source": "pylonAmmo",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0305474],1],["Center",[0.0135,-0.0264541],1],["Center",[0.023382,-0.0152737],1],["Center",[0.027,0],1],["Center",[0.023382,0.0152737],1],["Center",[0.0135,0.0264541],1],["Center",[0,0.0305474],1],["Center",[-0.0135,0.0264541],1],["Center",[-0.023382,0.0152737],1],["Center",[-0.027,0],1],["Center",[-0.023382,-0.0152737],1],["Center",[-0.0135,-0.0264541],1],["Center",[0,-0.0305474],1],[],["Center",[0.0124097,-0.0140402],1],["Center",[0.0105005,-0.0118802],1],[],["Center",[0.01755,8.67926e-010],1],["Center",[0.01485,7.34399e-010],1],[],["Center",[0.0124097,0.0140402],1],["Center",[0.0105005,0.0118802],1],[],["Center",[-1.53427e-009,0.0198558],1],["Center",[-1.29823e-009,0.0168011],1],[],["Center",[-0.0124097,0.0140402],1],["Center",[-0.0105005,0.0118802],1],[],["Center",[-0.01755,-2.36779e-010],1],["Center",[-0.01485,-2.00351e-010],1],[],["Center",[-0.0124097,-0.0140402],1],["Center",[-0.0105005,-0.0118802],1],[],["Center",[3.06854e-009,-0.0198558],1],["Center",[2.59646e-009,-0.0168011],1],[],["Center",[0.00668216,-0.00756011],1],["Center",[0.00477297,-0.00540008],1],[],["Center",[0.00668216,0.00756011],1],["Center",[0.00477297,0.00540008],1],[],["Center",[-0.00668216,0.00756011],1],["Center",[-0.00477297,0.00540008],1],[],["Center",[-0.00668216,-0.00756011],1],["Center",[-0.00477297,-0.00540008],1],[]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "pylonMagazineEmpty",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Empty|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "С5",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.12],1],
                        "right": [[0.035,0.12],1],
                        "down": [[-0.005,0.16],1]
                    },
                    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Empty|PylonValue1 [Indent level: 5],
                    "pylonvalue1": {
                        "type": "text",
                        "source": "pylonAmmo",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines|rhs_mag_s5_32|mfdElements|rhs_rus_circle|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0305474],1],["Center",[0.0135,-0.0264541],1],["Center",[0.023382,-0.0152737],1],["Center",[0.027,0],1],["Center",[0.023382,0.0152737],1],["Center",[0.0135,0.0264541],1],["Center",[0,0.0305474],1],["Center",[-0.0135,0.0264541],1],["Center",[-0.023382,0.0152737],1],["Center",[-0.027,0],1],["Center",[-0.023382,-0.0152737],1],["Center",[-0.0135,-0.0264541],1],["Center",[0,-0.0305474],1],[],["Center",[0.0124097,-0.0140402],1],["Center",[0.0105005,-0.0118802],1],[],["Center",[0.01755,8.67926e-010],1],["Center",[0.01485,7.34399e-010],1],[],["Center",[0.0124097,0.0140402],1],["Center",[0.0105005,0.0118802],1],[],["Center",[-1.53427e-009,0.0198558],1],["Center",[-1.29823e-009,0.0168011],1],[],["Center",[-0.0124097,0.0140402],1],["Center",[-0.0105005,0.0118802],1],[],["Center",[-0.01755,-2.36779e-010],1],["Center",[-0.01485,-2.00351e-010],1],[],["Center",[-0.0124097,-0.0140402],1],["Center",[-0.0105005,-0.0118802],1],[],["Center",[3.06854e-009,-0.0198558],1],["Center",[2.59646e-009,-0.0168011],1],[],["Center",[0.00668216,-0.00756011],1],["Center",[0.00477297,-0.00540008],1],[],["Center",[0.00668216,0.00756011],1],["Center",[0.00477297,0.00540008],1],[],["Center",[-0.00668216,0.00756011],1],["Center",[-0.00477297,0.00540008],1],[],["Center",[-0.00668216,-0.00756011],1],["Center",[-0.00477297,-0.00540008],1],[]]
                    },
                    "alpha": 0.22
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