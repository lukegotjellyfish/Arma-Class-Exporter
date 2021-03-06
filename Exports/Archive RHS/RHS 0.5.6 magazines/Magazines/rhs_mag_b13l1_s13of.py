rhs_mag_b13l1_s13of = {
    "displayname": "S-13 OF HE",
    "displaynameshort": "S-13OF",
    # Ammo: CfgMagazines|rhs_mag_b13l1_s13of|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "rhs_ammo_s13of",
        "submunitionammo": "",
        "model": "rhsafrf|addons|rhs_airweapons|s13_rockets|rhs_r_s13of_fly",
        "hit": 270,
        "indirecthit": 120,
        "indirecthitrange": 25,
        "proxyshape": "rhsafrf|addons|rhs_airweapons|s13_rockets|rhs_r_s13_gasket",
        "dangerradiushit": 1250,
        "suppressionradiushit": 120,
        "sideairfriction": 0.001,
        "thrusttime": 0.6,
        # Class: CfgAmmo|rhs_ammo_s13b|CamShakeExplode [Indent level: 1],
        "camshakeexplode": {
            "power": 24.4,
            "duration": 2.2,
            "frequency": 20,
            "distance": 208.363
        },
        # Class: CfgAmmo|rhs_ammo_s13b|CamShakeHit [Indent level: 1],
        "camshakehit": {
            "power": 122,
            "duration": 0.6,
            "frequency": 20,
            "distance": 1
        },
        # Class: CfgAmmo|rhs_ammo_s13b|CamShakeFire [Indent level: 1],
        "camshakefire": {
            "power": 3.32346,
            "duration": 2.2,
            "frequency": 20,
            "distance": 88.3629
        },
        # Class: CfgAmmo|rhs_ammo_s13b|CamShakePlayerFire [Indent level: 1],
        "camshakeplayerfire": {
            "power": 2,
            "duration": 0.1,
            "frequency": 20,
            "distance": 1
        },
        "soundsetexplosion": ["RocketsHeavy_Exp_SoundSet","RocketsHeavy_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "aiammousageflags": "64+128+512",
        "cost": 100,
        "inittime": 0.02,
        "effectsmissile": "RHS_Rocket_Fired",
        "effectsmissileinit": "RHS_Rocket_Init",
        "soundfly": ["A3|Sounds_F|weapons|Rockets|rocket_fly_2",1,1.5,700],
        "submunitiondirectiontype": "SubmunitionModelDirection",
        "submunitioninitialoffset": [0,0,-0.1],
        "submunitionparentspeedcoef": 0,
        "submunitioninitspeed": 1053,
        "triggeronimpact": 1,
        "deleteparentwhentriggered": 0,
        "missilelockmaxdistance": 4000,
        "missilelockmindistance": 700,
        "warheadname": "HE",
        "maxspeed": 590,
        "thrust": 1060,
        "airfriction": 0.09,
        "fusedistance": 50,
        "whistledist": 30,
        "timetolive": 15,
        "muzzleeffect": "",
        "simulation": "shotMissile",
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
    "mindamageforcamshakehit": "rhs_ammo_s13of",
    "mass": 485,
    "weight": 485,
    "pylonweapon": "rhs_weap_s13of",
    "model": "rhsafrf|addons|rhs_airweapons|rhs_pylon_r_b13l1.p3d",
    "count": 5,
    "hardpoints": ["RHS_HP_B13L1"],
    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_ammoname [Indent level: 2]
        "rhs_rus_ammoname": {
            # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_ammoname|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_ammoname|Draw [Indent level: 3],
            "draw": {
                "condition": "PylonSelected",
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_ammoname|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "С13",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[-0.005,0.02],1],
                    "right": [[0.045,0.02],1],
                    "down": [[-0.005,0.065],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_ammoname_right [Indent level: 2],
        "rhs_rus_ammoname_right": {
            # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_ammoname_right|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_ammoname_right|Draw [Indent level: 3],
            "draw": {
                "condition": "PylonSelected",
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_ammoname_right|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "С13",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[-0.005,0.02],1],
                    "right": [[0.045,0.02],1],
                    "down": [[-0.005,0.065],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_su25_box [Indent level: 2],
        "rhs_su25_box": {
            # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_su25_box|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_su25_box|Draw [Indent level: 3],
            "draw": {
                "condition": "1-pylonMagazineEmpty",
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_su25_box|Draw|Shape [Indent level: 4],
                "shape": {
                    "type": "polygon",
                    "width": 4,
                    "points": [[[[-0.022,-0.04],1],[[0.022,-0.04],1],[[0.022,0.04],1],[[-0.022,0.04],1]]]
                },
                # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_su25_box|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.58,0.23,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_su25_box|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.022,0.18],1],[[0.022,0.18],1],[[0.022,0.26],1],[[-0.022,0.26],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle [Indent level: 2],
        "rhs_rus_circle": {
            # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Bones [Indent level: 3]
            "bones": {
                # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Bones|Center [Indent level: 4]
                "center": {
                    "type": "fixed",
                    "pos": [0,0]
                }
            },
            # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "1-PylonSelected-pylonMagazineEmpty",
                    "color": [1,1,1],
                    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Default|PylonValue1 [Indent level: 5],
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
                    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "С13",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.12],1],
                        "right": [[0.035,0.12],1],
                        "down": [[-0.005,0.16],1]
                    },
                    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0339416],1],["Center",[0.015,-0.0293934],1],["Center",[0.02598,-0.0169708],1],["Center",[0.03,0],1],["Center",[0.02598,0.0169708],1],["Center",[0.015,0.0293934],1],["Center",[0,0.0339416],1],["Center",[-0.015,0.0293934],1],["Center",[-0.02598,0.0169708],1],["Center",[-0.03,0],1],["Center",[-0.02598,-0.0169708],1],["Center",[-0.015,-0.0293934],1],["Center",[0,-0.0339416],1],[],["Center",[0.0137886,-0.0156002],1],["Center",[0.0116673,-0.0132002],1],[],["Center",[0.0195,9.64363e-010],1],["Center",[0.0165,8.15999e-010],1],[],["Center",[0.0137886,0.0156002],1],["Center",[0.0116673,0.0132002],1],[],["Center",[-1.70474e-009,0.022062],1],["Center",[-1.44248e-009,0.0186679],1],[],["Center",[-0.0137886,0.0156002],1],["Center",[-0.0116673,0.0132002],1],[],["Center",[-0.0195,-2.63087e-010],1],["Center",[-0.0165,-2.22612e-010],1],[],["Center",[-0.0137886,-0.0156002],1],["Center",[-0.0116673,-0.0132002],1],[],["Center",[3.40949e-009,-0.022062],1],["Center",[2.88495e-009,-0.0186679],1],[],["Center",[0.00742462,-0.00840012],1],["Center",[0.0053033,-0.00600008],1],[],["Center",[0.00742462,0.00840012],1],["Center",[0.0053033,0.00600008],1],[],["Center",[-0.00742462,0.00840012],1],["Center",[-0.0053033,0.00600009],1],[],["Center",[-0.00742462,-0.00840012],1],["Center",[-0.0053033,-0.00600008],1],[]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Selected|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "С13",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.12],1],
                        "right": [[0.035,0.12],1],
                        "down": [[-0.005,0.16],1]
                    },
                    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Selected|PylonValue1 [Indent level: 5],
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
                    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0339416],1],["Center",[0.015,-0.0293934],1],["Center",[0.02598,-0.0169708],1],["Center",[0.03,0],1],["Center",[0.02598,0.0169708],1],["Center",[0.015,0.0293934],1],["Center",[0,0.0339416],1],["Center",[-0.015,0.0293934],1],["Center",[-0.02598,0.0169708],1],["Center",[-0.03,0],1],["Center",[-0.02598,-0.0169708],1],["Center",[-0.015,-0.0293934],1],["Center",[0,-0.0339416],1],[],["Center",[0.0137886,-0.0156002],1],["Center",[0.0116673,-0.0132002],1],[],["Center",[0.0195,9.64363e-010],1],["Center",[0.0165,8.15999e-010],1],[],["Center",[0.0137886,0.0156002],1],["Center",[0.0116673,0.0132002],1],[],["Center",[-1.70474e-009,0.022062],1],["Center",[-1.44248e-009,0.0186679],1],[],["Center",[-0.0137886,0.0156002],1],["Center",[-0.0116673,0.0132002],1],[],["Center",[-0.0195,-2.63087e-010],1],["Center",[-0.0165,-2.22612e-010],1],[],["Center",[-0.0137886,-0.0156002],1],["Center",[-0.0116673,-0.0132002],1],[],["Center",[3.40949e-009,-0.022062],1],["Center",[2.88495e-009,-0.0186679],1],[],["Center",[0.00742462,-0.00840012],1],["Center",[0.0053033,-0.00600008],1],[],["Center",[0.00742462,0.00840012],1],["Center",[0.0053033,0.00600008],1],[],["Center",[-0.00742462,0.00840012],1],["Center",[-0.0053033,0.00600009],1],[],["Center",[-0.00742462,-0.00840012],1],["Center",[-0.0053033,-0.00600008],1],[]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "pylonMagazineEmpty",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Empty|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "С13",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.12],1],
                        "right": [[0.035,0.12],1],
                        "down": [[-0.005,0.16],1]
                    },
                    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Empty|PylonValue1 [Indent level: 5],
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
                    # Class: CfgMagazines|rhs_mag_b13l_s13b|mfdElements|rhs_rus_circle|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
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
    "descriptionshort": "Obstacle penetration/HE",
    "maxleadspeed": 200,
    "initspeed": 44,
    "namesound": "rockets",
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