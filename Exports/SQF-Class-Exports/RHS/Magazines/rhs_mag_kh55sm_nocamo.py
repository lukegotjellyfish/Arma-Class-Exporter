d = {
    "ammo": {
        "_dictAmmoName": "rhs_ammo_kh55sm_nocamo",
        "access": 3,
        "afmax": 200,
        "aiammousageflags": "128 + 512",
        "airfriction": 0.05,
        "airlock": 0,
        "animated": 0,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "artillerylock": 0,
        "audiblefire": 32,
        "autoseektarget": 0,
        "caliber": 1,
        "cameraviewavailable": 0,
        "camshakeexplode": {
            "distance": 2011.66,
            "duration": 5.2,
            "frequency": 20,
            "power": 140
        },
        "camshakefire": {
            "distance": 71.5542,
            "duration": 1.8,
            "frequency": 20,
            "power": 2.9907
        },
        "camshakehit": {
            "distance": 1,
            "duration": 1,
            "frequency": 20,
            "power": 700
        },
        "camshakeplayerfire": {
            "distance": 1,
            "duration": 0.1,
            "frequency": 20,
            "power": 4
        },
        "cartridge": "",
        "cmimmunity": 0.5,
        "components": {
            "sensorsmanagercomponent": {
                "components": {
                    "lasersensorcomponent": {
                        "aimdown": 0,
                        "airtarget": {
                            "maxrange": 10000,
                            "minrange": 10000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        "allowsmarking": 1,
                        "anglerangehorizontal": 180,
                        "anglerangevertical": 180,
                        "animdirection": "",
                        "color": [
                            1,
                            1,
                            1,
                            0
                        ],
                        "componenttype": "LaserSensorComponent",
                        "groundnoisedistancecoef": -1,
                        "groundtarget": {
                            "maxrange": 10000,
                            "minrange": 10000,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": -1
                        },
                        "maxgroundnoisedistance": -1,
                        "maxspeedthreshold": 0,
                        "maxtrackableatl": 10000000000.0,
                        "maxtrackablespeed": 30,
                        "minspeedthreshold": 0,
                        "mintrackableatl": -10000000000.0,
                        "mintrackablespeed": -10000000000.0,
                        "typerecognitiondistance": 0
                    }
                }
            }
        },
        "cost": 800,
        "cratereffects": "RHS_HeavyBombCrater",
        "cratershape": "",
        "craterwatereffects": "ImpactEffectsWater",
        "dangerradiusbulletclose": -1,
        "dangerradiushit": -1,
        "deflecting": 0,
        "deflectionslowdown": 0.8,
        "deleteparentwhentriggered": 0,
        "directionalexplosion": 0,
        "effectflare": "FlareShell",
        "effectfly": "",
        "effectsfire": "CannonFire",
        "effectsmissile": "missile5",
        "effectsmissileinit": "PylonBackEffects",
        "effectssmoke": "SmokeShellWhite",
        "eventhandlers": {
            "rhs_aps_firedeh": {
                "fired": "_this spawn rhs_fnc_aps_missileFired"
            }
        },
        "explosionangle": 60,
        "explosiondir": "explosionDir",
        "explosioneffects": "RHS_HeavyBombExplosion",
        "explosioneffectsdir": "explosionDir",
        "explosionforcecoef": 1,
        "explosionpos": "explosionPos",
        "explosionsoundeffect": "DefaultExplosion",
        "explosiontime": 0,
        "explosiontype": "explosive",
        "explosive": 1,
        "flightprofiles": [
            "TopDown"
        ],
        "fusedistance": 350,
        "grenadeburningsound": [],
        "grenadefiresound": [],
        "hit": 9920,
        "hitarmor": [
            "soundHit",
            1
        ],
        "hitbuilding": [
            "soundHit",
            1
        ],
        "hitconcrete": [
            "soundHit",
            1
        ],
        "hitdefault": [
            "soundHit",
            1
        ],
        "hiteffects": {
            "hitwater": "ImpactEffectsWaterRocket"
        },
        "hitfoliage": [
            "soundHit",
            1
        ],
        "hitglass": [
            "soundHit",
            1
        ],
        "hitglassarmored": [
            "soundHit",
            1
        ],
        "hitgroundhard": [
            "soundHit",
            1
        ],
        "hitgroundsoft": [
            "soundHit",
            1
        ],
        "hitiron": [
            "soundHit",
            1
        ],
        "hitman": [
            "soundHit",
            1
        ],
        "hitmetal": [
            "soundHit",
            1
        ],
        "hitmetalplate": [
            "soundHit",
            1
        ],
        "hitonwater": 0,
        "hitplastic": [
            "soundHit",
            1
        ],
        "hitrubber": [
            "soundHit",
            1
        ],
        "hittyre": [
            "soundHit",
            1
        ],
        "hitwater": [
            "soundHit",
            1
        ],
        "hitwood": [
            "soundHit",
            1
        ],
        "htmax": 1800,
        "htmin": 60,
        "icon": "",
        "impactarmor": [
            "soundImpact",
            1
        ],
        "impactbuilding": [
            "soundImpact",
            1
        ],
        "impactconcrete": [
            "soundImpact",
            1
        ],
        "impactdefault": [
            "soundImpact",
            1
        ],
        "impactfoliage": [
            "soundImpact",
            1
        ],
        "impactglass": [
            "soundImpact",
            1
        ],
        "impactglassarmored": [
            "soundImpact",
            1
        ],
        "impactgroundhard": [
            "soundImpact",
            1
        ],
        "impactgroundsoft": [
            "soundImpact",
            1
        ],
        "impactiron": [
            "soundImpact",
            1
        ],
        "impactman": [
            "soundImpact",
            1
        ],
        "impactmetal": [
            "soundImpact",
            1
        ],
        "impactmetalplate": [
            "soundImpact",
            1
        ],
        "impactplastic": [
            "soundImpact",
            1
        ],
        "impactrubber": [
            "soundImpact",
            1
        ],
        "impacttyre": [
            "soundImpact",
            1
        ],
        "impactwater": [
            "soundImpact",
            1
        ],
        "impactwood": [
            "soundImpact",
            1
        ],
        "indirecthit": 1300,
        "indirecthitrange": 56,
        "inittime": 6,
        "irlock": 1,
        "iscrateroriented": 0,
        "laserlock": 1,
        "lockseekradius": 120,
        "locktype": 0,
        "maneuvrability": 10,
        "manualcontrol": 0,
        "maverickweaponindexoffset": 0,
        "maxcontrolrange": 350000,
        "maxspeed": 255,
        "mfact": 0,
        "mfmax": 100,
        "mindamageforcamshakehit": 0.55,
        "mineboundingdist": 3,
        "mineboundingtime": 3,
        "minedivespeed": 1,
        "minefloating": -1,
        "mineinconspicuousness": 10,
        "minejumpeffects": "",
        "mineplacedist": 0.5,
        "minetrigger": "RangeTrigger",
        "minimumsafezone": 0.1,
        "mintimetolive": 0,
        "missilekeeplockedcone": 30,
        "missilelockcone": 30,
        "missilelockmaxdistance": 9000,
        "missilelockmaxspeed": 55,
        "missilelockmindistance": 1500,
        "model": "rhsafrf/addons/rhs_airweapons/rhs_m_kh55sm2_fly",
        "multisoundhit": [
            "soundHit1",
            0.34,
            "soundHit2",
            0.33,
            "soundHit3",
            0.33
        ],
        "muzzleeffect": "",
        "nvgmarkers": {},
        "nvlock": 0,
        "proxyshape": "rhsafrf/addons/rhs_airweapons/rhs_m_kh55sm2",
        "rhs_fuserange": 100,
        "rhs_warheadtype": "NUKE",
        "rhs_yield": 50000,
        "shadow": 0,
        "shootdistraction": -1,
        "sideairfriction": 0.001,
        "simulation": "shotMissile",
        "simulationstep": 0.001,
        "soundactivation": [],
        "sounddeactivation": [],
        "soundengine": [
            "",
            1,
            1,
            50
        ],
        "soundfakefall": [
            "soundFall",
            1
        ],
        "soundfall": [
            "",
            1,
            1
        ],
        "soundfly": [
            "A3/Sounds_F/arsenal/weapons/Launchers/NLAW/Fly_NLAW",
            2.5,
            1.5,
            10800
        ],
        "soundhit": [
            "",
            100,
            1
        ],
        "soundhit1": [
            "A3/Sounds_F/arsenal/weapons/Launchers/Titan/Explosion_titan_missile_01",
            2.51189,
            1,
            2000
        ],
        "soundhit2": [
            "A3/Sounds_F/arsenal/weapons/Launchers/Titan/Explosion_titan_missile_02",
            2.51189,
            1,
            2000
        ],
        "soundhit3": [
            "A3/Sounds_F/arsenal/weapons/Launchers/Titan/Explosion_titan_missile_03",
            2.51189,
            1,
            2000
        ],
        "soundimpact": [
            "",
            1,
            1
        ],
        "soundsetexplosion": [
            "BombsHeavy_Exp_SoundSet",
            "BombsHeavy_Tail_SoundSet",
            "Explosion_Debris_SoundSet"
        ],
        "soundtrigger": [],
        "submunitionammo": "",
        "submunitiondirectiontype": "SubmunitionModelDirection",
        "submunitioninitialoffset": [
            0,
            0,
            -0.1
        ],
        "submunitioninitspeed": 1053,
        "submunitionparentspeedcoef": 0,
        "supersoniccrackfar": [
            "A3/Sounds_F/weapons/Explosion/supersonic_crack_50meters",
            0.316228,
            1,
            50
        ],
        "supersoniccracknear": [
            "A3/Sounds_F/weapons/Explosion/supersonic_crack_close",
            0.398107,
            1,
            20
        ],
        "suppressionradiusbulletclose": -1,
        "suppressionradiushit": 30,
        "tbody": 0,
        "thrust": 20,
        "thrusttime": 180,
        "timetolive": 900,
        "topdown": {
            "ascendangle": 0.01,
            "ascendheight": 400,
            "descenddistance": 1000,
            "mindistance": 400
        },
        "tracercolor": [
            0.7,
            0.7,
            0.5,
            0.04
        ],
        "tracercolorr": [
            0.7,
            0.7,
            0.5,
            0.04
        ],
        "tracklead": 0.95,
        "trackoversteer": 50,
        "triggeronimpact": 1,
        "typicalspeed": 270,
        "underwaterhitrangecoef": 1,
        "visiblefire": 32,
        "visiblefiretime": 20,
        "warheadname": "HE",
        "watereffectoffset": 0.45,
        "weaponlocksystem": 16,
        "weapontype": "Default",
        "whistledist": 25,
        "whistleonfire": 0
    },
    "author": "Bohemia Interactive",
    "count": 1,
    "descriptionshort": "Tactical nuke",
    "displayname": "Kh-55SM Nuke",
    "displaynameshort": "Kh-55SM",
    "hardpoints": [
        "RHS_HP_KH55SM_INT",
        "RHS_HP_TU95MS6_INT"
    ],
    "initspeed": 0,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "mass": 1700,
    "maxleadspeed": 100,
    "maxthrowholdtime": 2,
    "maxthrowintensitycoef": 1.4,
    "mindamageforcamshakehit": "rhs_ammo_kh55sm_nocamo",
    "minthrowintensitycoef": 0.3,
    "model": "rhsafrf/addons/rhs_airweapons/rhs_pylon_m_kh55sm",
    "modelspecial": "",
    "namesound": "missiles",
    "picture": "",
    "pylonweapon": "rhs_weap_kh55sm_Dummy_Launcher",
    "quickreload": 0,
    "reloadaction": "",
    "scope": 1,
    "selectionfireanim": "zasleh",
    "simulation": "ProxyMagazines",
    "type": 0,
    "useaction": 0,
    "useactiontitle": "",
    "value": 1,
    "weaponpoolavailable": 0,
    "weight": 0
}