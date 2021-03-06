rhs_mag_mk82_3 = {
    "count": 3,
    "displayname": "Mk82 (BRU-42)",
    "descriptionshort": "×3 500lb bomb",
    "model": "rhsusf|addons|rhsusf_a2port_air|data|proxy|rhsusf_pylon_m_mk82_3x",
    "hardpoints": ["RHS_HP_BOMB_500_3x","RHS_HP_LGB_500_3x","RHS_HP_JDAM_500_3x"],
    "mirrormissilesindexes": [2,1,3],
    # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_ammoname [Indent level: 2]
        "rhs_a10a_ammoname": {
            # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_ammoname|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_ammoname|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_ammoname|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "MK-82",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[0.005,0.02],1],
                    "right": [[0.05,0.02],1],
                    "down": [[0.005,0.105],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_box [Indent level: 2],
        "rhs_a10a_box": {
            # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_box|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_box|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_box|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "PylonAmmoRelative>=0.001",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_box|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,-0.04],1],[[0.015,-0.04],1],[[0.015,0.04],1],[[-0.015,0.04],1]],[[[0.02,-0.04],1],[[0.05,-0.04],1],[[0.05,0.04],1],[[0.02,0.04],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_box|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_box|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.015,0.05],1],[[0.015,0.05],1],[[0.015,0.13],1],[[-0.015,0.13],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_box|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative<=0",
                    "color": [0.87,0,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|rhs_a10a_box|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[0.02,0.05],1],[[0.05,0.05],1],[[0.05,0.13],1],[[0.02,0.13],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD [Indent level: 2],
        "rhs_a29_weap_mfd": {
            # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD|Draw|BackgroundGroup [Indent level: 4]
                "backgroundgroup": {
                    "color": [0,0,0],
                    # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD|Draw|BackgroundGroup|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[-0.019,-0.07],1],[[0.029,-0.07],1],[[0.029,0.05],1],[[-0.019,0.05],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "PylonAmmoRelative>0",
                    "color": [0,0.12,0],
                    # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.00859459,0.0258108],1],[[0.0121081,0.0258108],1],[],[[-0.00302703,0.0258108],1],[[0.000486486,0.0258108],1],[],[[-0.00762162,-0.0468919],1],[[0.0167027,-0.0468919],1],[],[[-0.00762162,0.00932432],1],[[0.0167027,0.00932432],1],[],[[0.000756755,0.0466216],1],[[0.000756755,0.0182432],1],[[0.00291892,0.0168919],1],[[0.00454054,0.0163513],1],[[0.00859459,0.0201351],1],[[0.00805406,0.0463514],1],[],[[0.00454054,0.0528378],1],[[0.00724325,0.0517568],1],[[0.00805406,0.049054],1],[[0.00805406,0.0463514],1],[[0.0196757,0.0504054],1],[[0.0196757,0.0290541],1],[[0.0121081,0.0258108],1],[[0.0167027,0.00959459],1],[[0.0167027,-0.0463514],1],[[0.0167027,-0.0531081],1],[[0.0153514,-0.0582432],1],[[0.0137297,-0.0612162],1],[[0.011027,-0.0636486],1],[[0.00832433,-0.065],1],[[0.00454054,-0.0655405],1],[[0.000756755,-0.065],1],[[-0.00194594,-0.0633784],1],[[-0.00464865,-0.060946],1],[[-0.00627027,-0.057973],1],[[-0.00762162,-0.0531081],1],[[-0.00762162,-0.0463514],1],[[-0.00762162,0.00959459],1],[[-0.00302703,0.0258108],1],[[-0.0103243,0.0293243],1],[[-0.0103243,0.0498649],1],[[0.000756755,0.0466216],1],[[0.00454054,0.0528378],1],[]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "color": [0.99,0.94,0.59],
                    # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.00859459,0.0258108],1],[[0.0121081,0.0258108],1],[],[[-0.00302703,0.0258108],1],[[0.000486486,0.0258108],1],[],[[-0.00762162,-0.0468919],1],[[0.0167027,-0.0468919],1],[],[[-0.00762162,0.00932432],1],[[0.0167027,0.00932432],1],[],[[0.000756755,0.0466216],1],[[0.000756755,0.0182432],1],[[0.00291892,0.0168919],1],[[0.00454054,0.0163513],1],[[0.00859459,0.0201351],1],[[0.00805406,0.0463514],1],[],[[0.00454054,0.0528378],1],[[0.00724325,0.0517568],1],[[0.00805406,0.049054],1],[[0.00805406,0.0463514],1],[[0.0196757,0.0504054],1],[[0.0196757,0.0290541],1],[[0.0121081,0.0258108],1],[[0.0167027,0.00959459],1],[[0.0167027,-0.0463514],1],[[0.0167027,-0.0531081],1],[[0.0153514,-0.0582432],1],[[0.0137297,-0.0612162],1],[[0.011027,-0.0636486],1],[[0.00832433,-0.065],1],[[0.00454054,-0.0655405],1],[[0.000756755,-0.065],1],[[-0.00194594,-0.0633784],1],[[-0.00464865,-0.060946],1],[[-0.00627027,-0.057973],1],[[-0.00762162,-0.0531081],1],[[-0.00762162,-0.0463514],1],[[-0.00762162,0.00959459],1],[[-0.00302703,0.0258108],1],[[-0.0103243,0.0293243],1],[[-0.0103243,0.0498649],1],[[0.000756755,0.0466216],1],[[0.00454054,0.0528378],1],[]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative <= 0",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.00859459,0.0258108],1],[[0.0121081,0.0258108],1],[],[[-0.00302703,0.0258108],1],[[0.000486486,0.0258108],1],[],[[-0.00762162,-0.0468919],1],[[0.0167027,-0.0468919],1],[],[[-0.00762162,0.00932432],1],[[0.0167027,0.00932432],1],[],[[0.000756755,0.0466216],1],[[0.000756755,0.0182432],1],[[0.00291892,0.0168919],1],[[0.00454054,0.0163513],1],[[0.00859459,0.0201351],1],[[0.00805406,0.0463514],1],[],[[0.00454054,0.0528378],1],[[0.00724325,0.0517568],1],[[0.00805406,0.049054],1],[[0.00805406,0.0463514],1],[[0.0196757,0.0504054],1],[[0.0196757,0.0290541],1],[[0.0121081,0.0258108],1],[[0.0167027,0.00959459],1],[[0.0167027,-0.0463514],1],[[0.0167027,-0.0531081],1],[[0.0153514,-0.0582432],1],[[0.0137297,-0.0612162],1],[[0.011027,-0.0636486],1],[[0.00832433,-0.065],1],[[0.00454054,-0.0655405],1],[[0.000756755,-0.065],1],[[-0.00194594,-0.0633784],1],[[-0.00464865,-0.060946],1],[[-0.00627027,-0.057973],1],[[-0.00762162,-0.0531081],1],[[-0.00762162,-0.0463514],1],[[-0.00762162,0.00959459],1],[[-0.00302703,0.0258108],1],[[-0.0103243,0.0293243],1],[[-0.0103243,0.0498649],1],[[0.000756755,0.0466216],1],[[0.00454054,0.0528378],1],[]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD_Inventory [Indent level: 2],
        "rhs_a29_weap_mfd_inventory": {
            # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD_Inventory|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonText1 [Indent level: 4]
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "MK82",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0,0.02],1],
                    "right": [[0.025,0.02],1],
                    "down": [[0,0.04],1]
                },
                # Class: CfgMagazines|rhs_mag_mk82_3|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonText2 [Indent level: 4],
                "pylontext2": {
                    "type": "text",
                    "source": "static",
                    "text": "FIXED",
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
    # Ammo: CfgMagazines|rhs_mag_mk82|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "rhs_ammo_mk82",
        "hit": 5000,
        "indirecthit": 1150,
        "cost": 50,
        "sideairfriction": 0.25,
        "aiammousageflags": "64 + 128 + 512",
        "maverickweaponindexoffset": 0,
        "indirecthitrange": 12,
        "dangerradiushit": 1250,
        "suppressionradiushit": 100,
        "irlock": 0,
        "laserlock": 0,
        "airfriction": 0.08,
        "maneuvrability": 4.6,
        "tracklead": 0,
        "maxspeed": 100,
        "timetolive": 120,
        "inittime": 0,
        "thrusttime": 0,
        "thrust": 0,
        "soundhit1": ["A3|Sounds_F|weapons|Explosion|expl_big_1",2.51189,1,1500],
        "soundhit2": ["A3|Sounds_F|weapons|Explosion|expl_big_2",2.51189,1,1500],
        "soundhit3": ["A3|Sounds_F|weapons|Explosion|expl_big_3",2.51189,1,1500],
        "soundhit4": ["A3|Sounds_F|weapons|Explosion|expl_shell_1",2.51189,1,1500],
        "soundhit5": ["A3|Sounds_F|weapons|Explosion|expl_shell_2",2.51189,1,1500],
        "multisoundhit": ["soundHit1",0.2,"soundHit2",0.2,"soundHit3",0.2,"soundHit4",0.2,"soundHit5",0.2],
        "explosionsoundeffect": "DefaultExplosion",
        "model": "A3|Weapons_F|Ammo|Bomb_02_F",
        "proxyshape": "A3|Weapons_F|Ammo|Bomb_02_F",
        "cratereffects": "BombCrater",
        "explosioneffects": "BombExplosion",
        "whistledist": 24,
        "soundsetexplosion": ["BombsHeavy_Exp_SoundSet","BombsHeavy_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "maxcontrolrange": 0,
        "simulation": "shotMissile",
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
        "lockseekradius": 100,
        "manualcontrol": 0,
        "trackoversteer": 1,
        "missilelockcone": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "locktype": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "autoseektarget": 0,
        "visiblefire": 0,
        "audiblefire": 0,
        "shootdistraction": -1,
        "visiblefiretime": 0,
        "explosiontime": 0,
        "fusedistance": 0,
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
    "eventhandlers": "rhs_ammo_mk82",
    "pylonweapon": "rhs_weap_mk82",
    "displaynamemfdformat": "MK82|%1",
    "author": "Bohemia Interactive",
    "scope": 2,
    "displaynameshort": "Bomb",
    "initspeed": 0,
    "maxleadspeed": 25,
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