d = {
    "ammo": {
        "_dictAmmoName": "rhs_ammo_9m119f",
        "access": 3,
        "afmax": 200,
        "aiammousageflags": "64+128+256",
        "airfriction": 0.085,
        "airlock": 1,
        "allowagainstinfantry": 1,
        "animated": 0,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "artillerylock": 0,
        "audiblefire": 32,
        "autoseektarget": 0,
        "caliber": 1,
        "camshakeexplode": {
            "distance": "((5 + 210^0.5)*8)",
            "duration": "((round (210^0.5))*0.2 max 0.2)",
            "frequency": 20,
            "power": "(210*0.2)"
        },
        "camshakefire": {
            "distance": 30,
            "duration": 0.5,
            "frequency": 20,
            "power": 10
        },
        "camshakehit": {
            "distance": 1,
            "duration": 0.6,
            "frequency": 20,
            "power": 110
        },
        "camshakeplayerfire": {
            "duration": 0.1,
            "frequency": 20,
            "power": 5
        },
        "canlock": 0,
        "cartridge": "",
        "cmimmunity": 0.4,
        "components": {
            "sensorsmanagercomponent": {
                "components": {
                    "visualsensorcomponent": {
                        "aimdown": 0,
                        "airtarget": {
                            "maxrange": 5000,
                            "minrange": 500,
                            "objectdistancelimitcoef": -1,
                            "viewdistancelimitcoef": 1
                        },
                        "allowsmarking": 1,
                        "anglerangehorizontal": 5,
                        "anglerangevertical": 5,
                        "animdirection": "",
                        "color": [
                            1,
                            1,
                            0.5,
                            0.8
                        ],
                        "componenttype": "VisualSensorComponent",
                        "groundnoisedistancecoef": -1,
                        "groundtarget": {
                            "maxrange": 5000,
                            "minrange": 500,
                            "objectdistancelimitcoef": 1,
                            "viewdistancelimitcoef": 1
                        },
                        "maxfogseethrough": 0.94,
                        "maxgroundnoisedistance": -1,
                        "maxspeedthreshold": 0,
                        "maxtrackableatl": 10000000000.0,
                        "maxtrackablespeed": 35,
                        "minspeedthreshold": 0,
                        "mintrackableatl": -10000000000.0,
                        "mintrackablespeed": -10000000000.0,
                        "nightrangecoef": 0.8,
                        "typerecognitiondistance": 2000
                    }
                }
            }
        },
        "cost": 100,
        "cratereffects": "ArtyShellCrater",
        "cratershape": "",
        "craterwatereffects": "ImpactEffectsWater",
        "dangerradiusbulletclose": -1,
        "dangerradiushit": -1,
        "deflecting": 0,
        "deflectionslowdown": 0.8,
        "deleteparentwhentriggered": 0,
        "direct": {},
        "directionalexplosion": 0,
        "effectflare": "FlareShell",
        "effectfly": "",
        "effectsfire": "CannonFire",
        "effectsmissile": "missile3",
        "effectsmissileinit": "RHS_ATGM_Pusher_Eject",
        "effectssmoke": "SmokeShellWhite",
        "eventhandlers": {
            "rhs_aps_firedeh": {
                "fired": "_this spawn rhs_fnc_aps_missileFired"
            },
            "rhs_guidance": {
                "fired": "_this call RHS_fnc_saclosGuide"
            }
        },
        "explosionangle": 60,
        "explosiondir": "explosionDir",
        "explosioneffects": "RHS_FAE_Explosion",
        "explosioneffectsdir": "explosionDir",
        "explosionforcecoef": 1,
        "explosionpos": "explosionPos",
        "explosionsoundeffect": "DefaultExplosion",
        "explosiontime": 0,
        "explosiontype": "explosive",
        "explosive": 1,
        "flightprofiles": [
            "Direct"
        ],
        "fusedistance": 50,
        "grenadeburningsound": [],
        "grenadefiresound": [],
        "hit": 100,
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
        "indirecthit": 70,
        "indirecthitrange": 12,
        "inittime": 0.1,
        "irlock": 1,
        "iscrateroriented": 0,
        "laserlock": 0,
        "lockseekradius": 100,
        "locktype": 0,
        "maneuvrability": 9,
        "manualcontrol": 0,
        "maverickweaponindexoffset": 0,
        "maxcontrolrange": 5000,
        "maxspeed": 420,
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
        "missilekeeplockedcone": 160,
        "missilelockcone": 4.5,
        "missilelockmaxdistance": 2000,
        "missilelockmaxspeed": 35,
        "missilelockmindistance": 50,
        "missilemanualcontrolcone": 50,
        "model": "rhsafrf/addons/rhs_heavyweapons/atgm/rhs_atgm_base",
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
        "proxyshape": "",
        "rhs_ballisticmode": 1,
        "rhs_guidemode": "BEAMRIDER",
        "rhs_saclos": 1,
        "scope": 2,
        "shadow": 0,
        "shootdistraction": -1,
        "sideairfriction": 0.1,
        "simulation": "shotMissile",
        "simulationstep": 0.005,
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
            "A3/Sounds_F/weapons/Rockets/rocket_fly_2",
            1,
            1,
            800
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
            "RocketsHeavy_Exp_SoundSet",
            "RocketsHeavy_Tail_SoundSet",
            "Explosion_Debris_SoundSet"
        ],
        "soundtrigger": [],
        "submunitionammo": [],
        "submunitiondirectiontype": "SubmunitionModelDirection",
        "submunitioninitialoffset": [
            0,
            0,
            -0.2
        ],
        "submunitioninitspeed": 1000,
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
        "texturetype": "semi",
        "thrust": 112,
        "thrusttime": 6,
        "timetolive": 30,
        "topdown": {
            "ascendangle": 30,
            "ascendheight": 150,
            "descenddistance": 180,
            "mindistance": 180
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
        "tracklead": 0.3,
        "trackoversteer": 0.3,
        "triggeronimpact": 1,
        "typicalspeed": 120,
        "underwaterhitrangecoef": 1,
        "visiblefire": 32,
        "visiblefiretime": 20,
        "warheadname": "HE",
        "watereffectoffset": 0.45,
        "weaponlocksystem": "1+4",
        "weapontype": "Default",
        "whistledist": 2,
        "whistleonfire": 0
    },
    "author": "Bohemia Interactive",
    "count": 40,
    "descriptionshort": "",
    "displayname": "ATGM 9M119F",
    "displaynameshort": "9M119F",
    "initspeed": 125,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "magazinereloadtime": 30,
    "mass": 8,
    "maxleadspeed": 50,
    "maxthrowholdtime": 2,
    "maxthrowintensitycoef": 1.4,
    "mindamageforcamshakehit": "rhs_ammo_9m119f",
    "minthrowintensitycoef": 0.3,
    "model": "A3/weapons_F/ammo/mag_univ.p3d",
    "modelspecial": "",
    "namesound": "missiles",
    "picture": "",
    "quickreload": 0,
    "reloadaction": "",
    "reloadtime": 30,
    "rhs_magazineindex": 4,
    "scope": 2,
    "selectionfireanim": "zasleh",
    "simulation": "ProxyMagazines",
    "type": 0,
    "useaction": 0,
    "useactiontitle": "",
    "value": 1,
    "weaponpoolavailable": 0,
    "weight": 0
}