rhs_mag_agm114m = {
    "displayname": "AGM-114M",
    "displaynameshort": "LG HE",
    "descriptionshort": "HE/FRAG Hellfire, Laser-homing",
    # Ammo: CfgMagazines|rhs_mag_AGM114M|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "RHS_ammo_AGM_114M",
        "submunitionammo": "",
        "indirecthit": 140,
        "indirecthitrange": 11,
        "dangerradiushit": 1250,
        "suppressionradiushit": 120,
        # Class: CfgAmmo|RHS_ammo_AGM_114M|CamShakeExplode [Indent level: 1],
        "camshakeexplode": {
            "power": "(122*0.2)",
            "duration": "((round (122^0.5))*0.2 max 0.2)",
            "frequency": 20,
            "distance": "((10 + 122^0.5)*8)"
        },
        # Class: CfgAmmo|RHS_ammo_AGM_114M|CamShakeHit [Indent level: 1],
        "camshakehit": {
            "power": 122,
            "duration": "((round (122^0.25))*0.2 max 0.2)",
            "frequency": 20,
            "distance": 1
        },
        # Class: CfgAmmo|RHS_ammo_AGM_114M|CamShakeFire [Indent level: 1],
        "camshakefire": {
            "power": "(122^0.25)",
            "duration": "((round (122^0.5))*0.2 max 0.2)",
            "frequency": 20,
            "distance": "((122^0.5)*8)"
        },
        # Class: CfgAmmo|RHS_ammo_AGM_114M|CamShakePlayerFire [Indent level: 1],
        "camshakeplayerfire": {
            "power": 2,
            "duration": 0.1,
            "frequency": 20,
            "distance": 1
        },
        "soundsetexplosion": ["RocketsHeavy_Exp_SoundSet","RocketsHeavy_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "model": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_m_AGM114K_fly",
        "proxyshape": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_m_AGM114K",
        "cost": 250,
        "airlock": 0,
        "irlock": 1,
        "laserlock": 1,
        "muzzleeffect": "",
        "effectsmissileinit": "MissileDAR1",
        "effectsmissile": "rhs_missile2",
        "whistledist": 4,
        "aiammousageflags": "64+128 + 512",
        "missilelockmaxdistance": 8000,
        "missilelockmindistance": 400,
        "missilelockmaxspeed": 56,
        "missilelockcone": 40,
        "missilekeeplockedcone": 40,
        "missilemanualcontrolcone": 40,
        "weaponlocksystem": "4 + 16",
        "lockseekradius": 1000,
        "weapontype": "missileAA",
        # Class: CfgAmmo|RHS_ammo_AGM_114K|Components [Indent level: 1],
        "components": {
            # Class: CfgAmmo|RHS_ammo_AGM_114K|Components|SensorsManagerComponent [Indent level: 2]
            "sensorsmanagercomponent": {
                # Class: CfgAmmo|RHS_ammo_AGM_114K|Components|SensorsManagerComponent|Components [Indent level: 3]
                "components": {
                    # Class: CfgAmmo|RHS_ammo_AGM_114K|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4]
                    "lasersensorcomponent": {
                        # Class: CfgAmmo|RHS_ammo_AGM_114K|Components|SensorsManagerComponent|Components|LaserSensorComponent|AirTarget [Indent level: 5]
                        "airtarget": {
                            "minrange": 7000,
                            "maxrange": 7000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        # Class: CfgAmmo|RHS_ammo_AGM_114K|Components|SensorsManagerComponent|Components|LaserSensorComponent|GroundTarget [Indent level: 5],
                        "groundtarget": {
                            "minrange": 7000,
                            "maxrange": 7000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        "anglerangehorizontal": 30,
                        "anglerangevertical": 50,
                        "typerecognitiondistance": -1,
                        "maxgroundnoisedistance": 0,
                        "maxfogseethrough": 0.3,
                        "allowsmarking": 1,
                        "componenttype": "LaserSensorComponent",
                        "color": [1,1,1,0],
                        "groundnoisedistancecoef": -1,
                        "minspeedthreshold": 0,
                        "maxspeedthreshold": 0,
                        "animdirection": "",
                        "aimdown": 0,
                        "mintrackablespeed": -1e+010,
                        "maxtrackablespeed": 1e+010,
                        "mintrackableatl": -1e+010,
                        "maxtrackableatl": 1e+010
                    }
                }
            }
        },
        "submunitiondirectiontype": "SubmunitionModelDirection",
        "submunitioninitialoffset": [0,0,-0.2],
        "submunitionparentspeedcoef": 0,
        "submunitioninitspeed": 1000,
        "triggeronimpact": 1,
        "deleteparentwhentriggered": 0,
        "hit": 400,
        "maxspeed": 425,
        "simulationstep": 0.005,
        "airfriction": 0.03,
        "sideairfriction": 0.15,
        "inittime": 0,
        "thrusttime": 3,
        "thrust": 199,
        "fusedistance": 5,
        "manualcontrol": 0,
        "maxcontrolrange": 8000,
        "trackoversteer": 1,
        "tracklead": 0.2,
        "maneuvrability": 21,
        "timetolive": 70,
        "autoseektarget": 1,
        "maneuvdependsonspeedcoef": 0.018,
        "flightprofiles": ["TopDown","LoalDistance","Cruise"],
        # Class: CfgAmmo|rhs_ammo_Hellfire_AT|Direct [Indent level: 1],
        "direct": {
        },
        # Class: CfgAmmo|rhs_ammo_Hellfire_AT|TopDown [Indent level: 1],
        "topdown": {
            "ascendangle": 39,
            "ascendheight": 360,
            "mindistance": 600,
            "descenddistance": 3000
        },
        # Class: CfgAmmo|rhs_ammo_Hellfire_AT|LoalDistance [Indent level: 1],
        "loaldistance": {
            "lockseekdistancefromparent": 1000
        },
        # Class: CfgAmmo|rhs_ammo_Hellfire_AT|Cruise [Indent level: 1],
        "cruise": {
            "preferredflightaltitude": 500,
            "lockdistancetotarget": 500
        },
        # Class: CfgAmmo|rhs_ammo_Hellfire_AT|Eventhandlers [Indent level: 1],
        "eventhandlers": {
            # Class: CfgAmmo|rhs_ammo_Hellfire_AT|Eventhandlers|RHS_EH [Indent level: 2]
            "rhs_eh": {
                "fired": "_this call rhs_fnc_agm114_helper"
            },
            # Class: CfgAmmo|MissileBase|EventHandlers|RHS_APS_FiredEH [Indent level: 2],
            "rhs_aps_firedeh": {
                "fired": "_this spawn rhs_fnc_aps_missileFired"
            }
        },
        "maverickweaponindexoffset": 2,
        "warheadname": "HE",
        "cameraviewavailable": 1,
        "cmimmunity": 0.5,
        "typicalspeed": 270,
        "cratereffects": "AAMissileCrater",
        "explosioneffects": "AAMissileExplosion",
        "soundfly": ["A3|Sounds_F|weapons|Rockets|rocket_fly_2",0.501187,1,1700],
        "soundhit1": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_01",2.51189,1,2000],
        "soundhit2": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_02",2.51189,1,2000],
        "soundhit3": ["A3|Sounds_F|arsenal|weapons|Launchers|Titan|Explosion_titan_missile_03",2.51189,1,2000],
        "multisoundhit": ["soundHit1",0.34,"soundHit2",0.33,"soundHit3",0.33],
        "explosionsoundeffect": "DefaultExplosion",
        "soundengine": ["",1,1,50],
        "supersoniccracknear": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_close",0.398107,1,20],
        "supersoniccrackfar": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_50meters",0.316228,1,50],
        "deflecting": 0,
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
        "simulation": "shotMissile",
        "visiblefire": 32,
        "audiblefire": 32,
        "visiblefiretime": 20,
        "soundhit": ["",100,1],
        "access": 3,
        "underwaterhitrangecoef": 1,
        "explosionforcecoef": 1,
        "iscrateroriented": 0,
        "cratershape": "",
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
    "mindamageforcamshakehit": "RHS_ammo_AGM_114M",
    "maxleadspeed": 100,
    "count": 1,
    "weight": 45,
    "pylonweapon": "RHS_weap_AGM114M_Launcher",
    # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD [Indent level: 2]
        "rhs_a29_weap_mfd": {
            # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD|Draw|BackgroundGroup [Indent level: 4]
                "backgroundgroup": {
                    "color": [0,0,0],
                    # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD|Draw|BackgroundGroup|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[-0.022,-0.05],1],[[0.022,-0.05],1],[[0.022,0.034],1],[[-0.022,0.034],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "PylonAmmoRelative>0",
                    "color": [0,0.12,0],
                    # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.0132609,-0.0382749],1],[[-0.00239129,-0.0303647],1],[[-0.018913,-0.0382749],1],[],[[0.0132609,0.0289621],1],[[0.0132609,-0.0382749],1],[[0.0132609,-0.04223],1],[[0.0115217,-0.045526],1],[[0.00978261,-0.0481627],1],[[0.00630435,-0.0494811],1],[[0.00282609,-0.0507994],1],[[0.000217393,-0.0514586],1],[[-0.00239129,-0.0521178],1],[[-0.00326087,-0.0521178],1],[[-0.00586955,-0.0514586],1],[[-0.00847825,-0.0507994],1],[[-0.0119565,-0.0494811],1],[[-0.0145652,-0.0481627],1],[[-0.0171739,-0.045526],1],[[-0.0180435,-0.04223],1],[[-0.018913,-0.0382749],1],[[-0.018913,0.0289621],1],[[0.0132609,0.0289621],1],[]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "color": [0.99,0.94,0.59],
                    # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.0132609,-0.0382749],1],[[-0.00239129,-0.0303647],1],[[-0.018913,-0.0382749],1],[],[[0.0132609,0.0289621],1],[[0.0132609,-0.0382749],1],[[0.0132609,-0.04223],1],[[0.0115217,-0.045526],1],[[0.00978261,-0.0481627],1],[[0.00630435,-0.0494811],1],[[0.00282609,-0.0507994],1],[[0.000217393,-0.0514586],1],[[-0.00239129,-0.0521178],1],[[-0.00326087,-0.0521178],1],[[-0.00586955,-0.0514586],1],[[-0.00847825,-0.0507994],1],[[-0.0119565,-0.0494811],1],[[-0.0145652,-0.0481627],1],[[-0.0171739,-0.045526],1],[[-0.0180435,-0.04223],1],[[-0.018913,-0.0382749],1],[[-0.018913,0.0289621],1],[[0.0132609,0.0289621],1],[]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative <= 0",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.0132609,-0.0382749],1],[[-0.00239129,-0.0303647],1],[[-0.018913,-0.0382749],1],[],[[0.0132609,0.0289621],1],[[0.0132609,-0.0382749],1],[[0.0132609,-0.04223],1],[[0.0115217,-0.045526],1],[[0.00978261,-0.0481627],1],[[0.00630435,-0.0494811],1],[[0.00282609,-0.0507994],1],[[0.000217393,-0.0514586],1],[[-0.00239129,-0.0521178],1],[[-0.00326087,-0.0521178],1],[[-0.00586955,-0.0514586],1],[[-0.00847825,-0.0507994],1],[[-0.0119565,-0.0494811],1],[[-0.0145652,-0.0481627],1],[[-0.0171739,-0.045526],1],[[-0.0180435,-0.04223],1],[[-0.018913,-0.0382749],1],[[-0.018913,0.0289621],1],[[0.0132609,0.0289621],1],[]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD_Inventory [Indent level: 2],
        "rhs_a29_weap_mfd_inventory": {
            # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD_Inventory|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonText1 [Indent level: 4]
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "AGM-114M",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0,0.02],1],
                    "right": [[0.025,0.02],1],
                    "down": [[0,0.04],1]
                },
                # Class: CfgMagazines|rhs_mag_AGM114M|mfdElements|RHS_A29_Weap_MFD_Inventory|Draw|PylonText2 [Indent level: 4],
                "pylontext2": {
                    "type": "text",
                    "source": "static",
                    "text": "LASER",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[0,0.054],1],
                    "right": [[0.025,0.054],1],
                    "down": [[0,0.074],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD [Indent level: 2],
        "rhs_ah64_weap_mfd": {
            # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|BackgroundGroup [Indent level: 4]
                "backgroundgroup": {
                    "color": [0,0,0],
                    # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|BackgroundGroup|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[-0.005,-0.03],1],[[0.065,-0.03],1],[[0.065,0.15],1],[[-0.005,0.15],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "PylonAmmoRelative>0",
                    "color": [0,0.12,0],
                    # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.0553333,0.00176638],1],[[0.0313333,0.0174929],1],[[0.00600001,0.00176638],1],[],[[0.0553333,0.135442],1],[[0.0553333,0.00176638],1],[[0.0553333,-0.00609687],1],[[0.0526667,-0.0126496],1],[[0.05,-0.0178917],1],[[0.0446667,-0.0205128],1],[[0.0393333,-0.0231339],1],[[0.0353333,-0.0244445],1],[[0.0313333,-0.025755],1],[[0.03,-0.025755],1],[[0.026,-0.0244445],1],[[0.022,-0.0231339],1],[[0.0166667,-0.0205128],1],[[0.0126667,-0.0178917],1],[[0.00866666,-0.0126496],1],[[0.00733334,-0.00609687],1],[[0.00600001,0.00176638],1],[[0.00600001,0.135442],1],[[0.0553333,0.135442],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "L",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.03,0.05],1],
                        "right": [[0.06,0.05],1],
                        "down": [[0.03,0.075],1]
                    }
                },
                # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "color": [0.99,0.94,0.59],
                    # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.0553333,0.00176638],1],[[0.0313333,0.0174929],1],[[0.00600001,0.00176638],1],[],[[0.0553333,0.135442],1],[[0.0553333,0.00176638],1],[[0.0553333,-0.00609687],1],[[0.0526667,-0.0126496],1],[[0.05,-0.0178917],1],[[0.0446667,-0.0205128],1],[[0.0393333,-0.0231339],1],[[0.0353333,-0.0244445],1],[[0.0313333,-0.025755],1],[[0.03,-0.025755],1],[[0.026,-0.0244445],1],[[0.022,-0.0231339],1],[[0.0166667,-0.0205128],1],[[0.0126667,-0.0178917],1],[[0.00866666,-0.0126496],1],[[0.00733334,-0.00609687],1],[[0.00600001,0.00176638],1],[[0.00600001,0.135442],1],[[0.0553333,0.135442],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|Selected|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "L",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.03,0.05],1],
                        "right": [[0.06,0.05],1],
                        "down": [[0.03,0.075],1]
                    }
                },
                # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative <= 0",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [[[0.0553333,0.00176638],1],[[0.0313333,0.0174929],1],[[0.00600001,0.00176638],1],[],[[0.0553333,0.135442],1],[[0.0553333,0.00176638],1],[[0.0553333,-0.00609687],1],[[0.0526667,-0.0126496],1],[[0.05,-0.0178917],1],[[0.0446667,-0.0205128],1],[[0.0393333,-0.0231339],1],[[0.0353333,-0.0244445],1],[[0.0313333,-0.025755],1],[[0.03,-0.025755],1],[[0.026,-0.0244445],1],[[0.022,-0.0231339],1],[[0.0166667,-0.0205128],1],[[0.0126667,-0.0178917],1],[[0.00866666,-0.0126496],1],[[0.00733334,-0.00609687],1],[[0.00600001,0.00176638],1],[[0.00600001,0.135442],1],[[0.0553333,0.135442],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD|Draw|Empty|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "L",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[0.03,0.05],1],
                        "right": [[0.06,0.05],1],
                        "down": [[0.03,0.075],1]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD_Inventory [Indent level: 2],
        "rhs_ah64_weap_mfd_inventory": {
            # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD_Inventory|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_Hellfire_base|mfdElements|RHS_AH64_Weap_MFD_Inventory|Draw [Indent level: 3],
            "draw": {
            }
        }
    },
    "hardpoints": ["RHS_HP_HELLFIRE_SINGLE","RHS_HP_LONGBOW_SINGLE"],
    "scope": 2,
    "model": "rhsusf|addons|rhsusf_airweapons|proxypylon|rhsusf_pylon_m_agm114_1x",
    "namesound": "missiles",
    "initspeed": 0,
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