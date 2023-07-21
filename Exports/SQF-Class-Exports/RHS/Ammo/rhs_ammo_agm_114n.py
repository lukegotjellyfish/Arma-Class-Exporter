d = {
    "access": 3,
    "afmax": 200,
    "aiammousageflags": "64+128",
    "airfriction": 0.03,
    "airlock": 0,
    "allowagainstinfantry": 1,
    "animated": 0,
    "artillerycharge": 1,
    "artillerydispersion": 1,
    "artillerylock": 0,
    "audiblefire": 32,
    "autoseektarget": 1,
    "caliber": 1,
    "cameraviewavailable": 1,
    "camshakeexplode": {
        "distance": "((5 + 110^0.5)*8)",
        "duration": "((round (110^0.5))*0.2 max 0.2)",
        "frequency": 20,
        "power": "(110*0.2)"
    },
    "camshakefire": {
        "distance": "((122^0.5)*8)",
        "duration": "((round (122^0.5))*0.2 max 0.2)",
        "frequency": 20,
        "power": "(122^0.25)"
    },
    "camshakehit": {
        "distance": 1,
        "duration": "((round (122^0.25))*0.2 max 0.2)",
        "frequency": 20,
        "power": 122
    },
    "camshakeplayerfire": {
        "distance": 1,
        "duration": 0.1,
        "frequency": 20,
        "power": 2
    },
    "cartridge": "",
    "cmimmunity": 0.5,
    "components": {
        "sensorsmanagercomponent": {
            "components": {
                "lasersensorcomponent": {
                    "aimdown": 0,
                    "airtarget": {
                        "maxrange": 7000,
                        "minrange": 7000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "allowsmarking": 1,
                    "anglerangehorizontal": 30,
                    "anglerangevertical": 50,
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
                        "maxrange": 7000,
                        "minrange": 7000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "maxfogseethrough": 0.3,
                    "maxgroundnoisedistance": 0,
                    "maxspeedthreshold": 0,
                    "maxtrackableatl": 10000000000.0,
                    "maxtrackablespeed": 10000000000.0,
                    "minspeedthreshold": 0,
                    "mintrackableatl": -10000000000.0,
                    "mintrackablespeed": -10000000000.0,
                    "typerecognitiondistance": -1
                }
            }
        }
    },
    "cost": 100,
    "cratereffects": "AAMissileCrater",
    "cratershape": "",
    "craterwatereffects": "ImpactEffectsWater",
    "cruise": {
        "lockdistancetotarget": 500,
        "preferredflightaltitude": 500
    },
    "dangerradiusbulletclose": -1,
    "dangerradiushit": 1250,
    "deflecting": 0,
    "deflectionslowdown": 0.8,
    "deleteparentwhentriggered": 0,
    "direct": {},
    "directionalexplosion": 0,
    "effectflare": "FlareShell",
    "effectfly": "",
    "effectsfire": "CannonFire",
    "effectsmissile": "rhs_missile2",
    "effectsmissileinit": "MissileDAR1",
    "effectssmoke": "SmokeShellWhite",
    "eventhandlers": {
        "rhs_aps_firedeh": {
            "fired": "_this spawn rhs_fnc_aps_missileFired"
        },
        "rhs_eh": {
            "fired": "_this call rhs_fnc_agm114_helper"
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
        "TopDown",
        "LoalDistance",
        "Cruise"
    ],
    "fusedistance": 5,
    "grenadeburningsound": [],
    "grenadefiresound": [],
    "hit": 210,
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
    "indirecthit": 85,
    "indirecthitrange": 20,
    "inittime": 0,
    "irlock": 1,
    "iscrateroriented": 0,
    "laserlock": 1,
    "loaldistance": {
        "lockseekdistancefromparent": 1000
    },
    "lockseekradius": 1000,
    "locktype": 0,
    "maneuvdependsonspeedcoef": 0.018,
    "maneuvrability": 21,
    "manualcontrol": 0,
    "maverickweaponindexoffset": 2,
    "maxcontrolrange": 8000,
    "maxspeed": 425,
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
    "missilekeeplockedcone": 40,
    "missilelockcone": 40,
    "missilelockmaxdistance": 8000,
    "missilelockmaxspeed": 56,
    "missilelockmindistance": 400,
    "missilemanualcontrolcone": 40,
    "model": "rhsusf/addons/rhsusf_airweapons/proxyammo/rhsusf_m_AGM114K_fly",
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
    "proxyshape": "rhsusf/addons/rhsusf_airweapons/proxyammo/rhsusf_m_AGM114K",
    "shadow": 0,
    "shootdistraction": -1,
    "sideairfriction": 0.15,
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
        0.501187,
        1,
        1700
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
    "suppressionradiushit": 120,
    "tbody": 0,
    "thrust": 199,
    "thrusttime": 3,
    "timetolive": 70,
    "topdown": {
        "ascendangle": 39,
        "ascendheight": 360,
        "descenddistance": 3000,
        "mindistance": 600
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
    "tracklead": 0.2,
    "trackoversteer": 1,
    "triggeronimpact": 1,
    "typicalspeed": 270,
    "underwaterhitrangecoef": 1,
    "visiblefire": 32,
    "visiblefiretime": 20,
    "warheadname": "HE",
    "watereffectoffset": 0.45,
    "weaponlocksystem": "4 + 16",
    "weapontype": "missileAA",
    "whistledist": 4,
    "whistleonfire": 0
}