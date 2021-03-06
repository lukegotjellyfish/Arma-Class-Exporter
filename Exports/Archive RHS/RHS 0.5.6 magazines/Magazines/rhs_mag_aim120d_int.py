rhs_mag_aim120d_int = {
    # Ammo: CfgMagazines|rhs_mag_aim120d_int|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "rhs_ammo_aim120d",
        "proxyshape": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_m_AIM120D",
        "model": "rhsusf|addons|rhsusf_airweapons|proxyammo|rhsusf_m_AIM120D_fly.p3d",
        "missilelockmaxdistance": 28000,
        "missilelockmindistance": 2000,
        "missilelockmaxspeed": 3000,
        "missilelockcone": 60,
        "missilekeeplockedcone": 90,
        "thrusttime": 9,
        "thrust": 260,
        # Class: CfgAmmo|rhs_ammo_aim120d|Components [Indent level: 1],
        "components": {
            # Class: CfgAmmo|rhs_ammo_aim120d|Components|SensorsManagerComponent [Indent level: 2]
            "sensorsmanagercomponent": {
                # Class: CfgAmmo|rhs_ammo_aim120d|Components|SensorsManagerComponent|Components [Indent level: 3]
                "components": {
                    # Class: CfgAmmo|rhs_ammo_aim120d|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent [Indent level: 4]
                    "activeradarsensorcomponent": {
                        # Class: CfgAmmo|rhs_ammo_aim120d|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|AirTarget [Indent level: 5]
                        "airtarget": {
                            "minrange": 30000,
                            "maxrange": 30000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        # Class: CfgAmmo|rhs_ammo_aim120d|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|GroundTarget [Indent level: 5],
                        "groundtarget": {
                            "minrange": 30000,
                            "maxrange": 30000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        "typerecognitiondistance": -1,
                        "anglerangehorizontal": 60,
                        "anglerangevertical": 60,
                        "groundnoisedistancecoef": 0.1,
                        "maxgroundnoisedistance": 200,
                        "minspeedthreshold": 12,
                        "maxspeedthreshold": 42,
                        "maxfogseethrough": 1,
                        "mintrackablespeed": 12,
                        "maxtrackablespeed": 833,
                        "mintrackableatl": 70,
                        "maxtrackableatl": 1e+010,
                        "componenttype": "ActiveRadarSensorComponent",
                        "color": [0,1,1,1],
                        "allowsmarking": 1,
                        "animdirection": "",
                        "aimdown": 0
                    }
                }
            }
        },
        "cmimmunity": 0.92,
        "timetolive": 120,
        "inittime": 0.5,
        "cost": 1000,
        "hit": 230,
        "indirecthit": 140,
        "indirecthitrange": 16,
        "proximityexplosiondistance": 25,
        "maverickweaponindexoffset": 0,
        "airfriction": 0.014,
        "sideairfriction": 0.23,
        "trackoversteer": 0.9,
        "tracklead": 1,
        "maxspeed": 1300,
        "weaponlocksystem": "8 + 16",
        "autoseektarget": 1,
        "lockseekradius": 1000,
        "maneuvrability": 30,
        "simulationstep": 0.001,
        "airlock": 2,
        "irlock": 1,
        "fusedistance": 300,
        "explosionangle": 60,
        "cratereffects": "AAMissileCrater",
        "explosioneffects": "AAMissileExplosion",
        "effectsmissile": "rhs_missile3",
        "whistledist": 20,
        "warheadname": "HE",
        "laserlock": 0,
        "nvlock": 0,
        "manualcontrol": 0,
        "maxcontrolrange": 4500,
        "aiammousageflags": 256,
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
    "mindamageforcamshakehit": "rhs_ammo_aim120d",
    "model": "rhsusf|addons|rhsusf_airweapons|proxypylon|rhsusf_pylon_m_LAU142_1x",
    "hardpoints": ["RHS_HP_aim120_int"],
    "pylonweapon": "rhs_weap_AIM120D",
    # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon [Indent level: 2]
        "rhs_f22_pylon": {
            # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|material [Indent level: 3]
            "material": {
                "ambient": [3,3,3,1],
                "diffuse": [10,10,10,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Bones [Indent level: 3],
            "bones": {
                # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Bones|Center [Indent level: 4]
                "center": {
                    "type": "fixed",
                    "pos": [0,0]
                }
            },
            # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw [Indent level: 3],
            "draw": {
                # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Default [Indent level: 4]
                "default": {
                    "condition": "PylonAmmoRelative>0",
                    "color": [0.15,1,0.15],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0205729],1],["Center",[0.01,-0.0178161],1],["Center",[0.01732,-0.0102865],1],["Center",[0.02,0],1],["Center",[0.01732,0.0102865],1],["Center",[0.01,0.0178161],1],["Center",[0,0.0205729],1],["Center",[-0.01,0.0178161],1],["Center",[-0.01732,0.0102865],1],["Center",[-0.02,0],1],["Center",[-0.01732,-0.0102865],1],["Center",[-0.01,-0.0178161],1],["Center",[0,-0.0205729],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "C",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": ["Center",1,[-0,-0.015],1],
                        "right": ["Center",1,[0.03,-0.015],1],
                        "down": ["Center",1,[-0,0.02],1]
                    }
                },
                # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "(PylonSelected +  PylonAmmoRelative)/2",
                    "alpha": 1,
                    # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0205729],1],["Center",[0.01,-0.0178161],1],["Center",[0.01732,-0.0102865],1],["Center",[0.02,0],1],["Center",[0.01732,0.0102865],1],["Center",[0.01,0.0178161],1],["Center",[0,0.0205729],1],["Center",[-0.01,0.0178161],1],["Center",[-0.01732,0.0102865],1],["Center",[-0.02,0],1],["Center",[-0.01732,-0.0102865],1],["Center",[-0.01,-0.0178161],1],["Center",[0,-0.0205729],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Selected|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "C",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": ["Center",1,[-0,-0.015],1],
                        "right": ["Center",1,[0.03,-0.015],1],
                        "down": ["Center",1,[-0,0.02],1]
                    },
                    # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Selected|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[["Center",1,[0,0],1],["Center",[0.0141421,-0.0145472],1],["Center",[0.02,8.99271e-010],1],["Center",[0.0141421,0.0145472],1]],[["Center",1,[0,0],1],["Center",[0.0141421,0.0145472],1],["Center",[-1.74846e-009,0.0205729],1],["Center",[-0.0141421,0.0145472],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,0.0145472],1],["Center",[-0.02,-2.4533e-010],1],["Center",[-0.0141421,-0.0145472],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,-0.0145472],1],["Center",[3.49691e-009,-0.0205729],1],["Center",[0.0141421,-0.0145472],1]]]
                    },
                    "color": [0.15,1,0.15]
                },
                # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "PylonAmmoRelative <= 0",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0205729],1],["Center",[0.01,-0.0178161],1],["Center",[0.01732,-0.0102865],1],["Center",[0.02,0],1],["Center",[0.01732,0.0102865],1],["Center",[0.01,0.0178161],1],["Center",[0,0.0205729],1],["Center",[-0.01,0.0178161],1],["Center",[-0.01732,0.0102865],1],["Center",[-0.02,0],1],["Center",[-0.01732,-0.0102865],1],["Center",[-0.01,-0.0178161],1],["Center",[0,-0.0205729],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Empty|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "C",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": ["Center",1,[-0,-0.015],1],
                        "right": ["Center",1,[0.03,-0.015],1],
                        "down": ["Center",1,[-0,0.02],1]
                    },
                    # Class: CfgMagazines|rhs_mag_aim120d_int|mfdElements|rhs_f22_pylon|Draw|Empty|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[["Center",1,[0,0],1],["Center",[0.0141421,-0.0145472],1],["Center",[0.02,8.99271e-010],1],["Center",[0.0141421,0.0145472],1]],[["Center",1,[0,0],1],["Center",[0.0141421,0.0145472],1],["Center",[-1.74846e-009,0.0205729],1],["Center",[-0.0141421,0.0145472],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,0.0145472],1],["Center",[-0.02,-2.4533e-010],1],["Center",[-0.0141421,-0.0145472],1]],[["Center",1,[0,0],1],["Center",[-0.0141421,-0.0145472],1],["Center",[3.49691e-009,-0.0205729],1],["Center",[0.0141421,-0.0145472],1]]]
                    },
                    "alpha": 1
                }
            }
        }
    },
    "displayname": "AIM-120D",
    "displaynamemfdformat": "%1 AIM-120D",
    "displaynameshort": "Radar",
    "descriptionshort": "Radar-homing, BVRAAM",
    "count": 1,
    "initspeed": 0,
    "maxleadspeed": 450,
    "namesound": "missiles",
    "scope": 2,
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