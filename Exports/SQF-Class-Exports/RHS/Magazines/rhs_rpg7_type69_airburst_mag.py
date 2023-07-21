d = {
    "allowedslots": [
        901
    ],
    "ammo": {
        "_dictAmmoName": "rhs_rpg7v2_type63_airburst",
        "access": 3,
        "aiammousageflags": "64+128+256",
        "airfriction": 0.6,
        "airlock": 1,
        "allowagainstinfantry": 1,
        "animated": 0,
        "artillerycharge": 1,
        "artillerydispersion": 1,
        "artillerylock": 0,
        "audiblefire": 16,
        "autoseektarget": 0,
        "caliber": 0.8,
        "camshakeexplode": {
            "distance": 231.636,
            "duration": 2.2,
            "frequency": 20,
            "power": 24
        },
        "camshakefire": {
            "distance": 87.6356,
            "duration": 2.2,
            "frequency": 20,
            "power": 3.30975
        },
        "camshakehit": {
            "distance": 1,
            "duration": 0.6,
            "frequency": 20,
            "power": 120
        },
        "camshakeplayerfire": {
            "distance": 1,
            "duration": 0.1,
            "frequency": 20,
            "power": 3
        },
        "cartridge": "",
        "cmimmunity": 1,
        "cost": 100,
        "cratereffects": "HEShellCrater",
        "cratershape": "",
        "craterwatereffects": "ImpactEffectsWaterHE",
        "dangerradiusbulletclose": -1,
        "dangerradiushit": -1,
        "deflecting": 0.999999,
        "deflectionslowdown": 0.8,
        "deleteparentwhentriggered": 0,
        "directionalexplosion": 0,
        "effectflare": "FlareShell",
        "effectfly": "",
        "effectsfire": "CannonFire",
        "effectsmissile": "missile3",
        "effectsmissileinit": "RocketBackEffectsRPG",
        "effectssmoke": "SmokeShellWhite",
        "eventhandlers": {
            "rhs_airburst": {
                "fired": "_this call RHS_fnc_rpg_airburst"
            },
            "rhs_aps_firedeh": {
                "fired": "_this spawn rhs_fnc_aps_missileFired"
            }
        },
        "explosionangle": 60,
        "explosiondir": "explosionDir",
        "explosioneffects": "HEShellExplosion",
        "explosioneffectsdir": "explosionDir",
        "explosionforcecoef": 1,
        "explosionpos": "explosionPos",
        "explosionsoundeffect": "DefaultExplosion",
        "explosiontime": 0,
        "explosiontype": "explosive",
        "explosive": 1,
        "fusedistance": 5,
        "grenadeburningsound": [],
        "grenadefiresound": [],
        "hit": 55,
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
        "indirecthit": 16,
        "indirecthitrange": 12,
        "inittime": 0.1,
        "irlock": 0,
        "iscrateroriented": 0,
        "laserlock": 0,
        "lockseekradius": 100,
        "locktype": 0,
        "maneuvrability": 0,
        "manualcontrol": 0,
        "maverickweaponindexoffset": 0,
        "maxcontrolrange": 0,
        "maxspeed": 295,
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
        "missilelockcone": 0,
        "model": "rhsafrf/addons/rhs_weapons/rpg7/projectiles/Type69",
        "multisoundhit": [
            "soundHit1",
            0.34,
            "soundHit2",
            0.33,
            "soundHit3",
            0.33
        ],
        "muzzleeffect": "BIS_fnc_effectFiredRocket",
        "nvgmarkers": {},
        "nvlock": 0,
        "proxyshape": "",
        "shadow": 0,
        "shootdistraction": -1,
        "sideairfriction": 0.1,
        "simulation": "shotRocket",
        "simulationstep": 0.01,
        "soundactivation": [],
        "sounddeactivation": [],
        "soundengine": [
            "",
            1,
            1,
            20
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
            "A3/Sounds_F/arsenal/weapons_static/Missile_Launcher/rocket_fly",
            1.1,
            0.7,
            250
        ],
        "soundhit": [
            "A3/Sounds_F/weapons/Rockets/explosion_missile_02",
            2.51189,
            1,
            2500
        ],
        "soundhit1": [
            "A3/Sounds_F/arsenal/weapons/Launchers/Titan/Explosion_titan_missile_01",
            2.51189,
            1,
            1800
        ],
        "soundhit2": [
            "A3/Sounds_F/arsenal/weapons/Launchers/Titan/Explosion_titan_missile_02",
            2.51189,
            1,
            1800
        ],
        "soundhit3": [
            "A3/Sounds_F/arsenal/weapons/Launchers/Titan/Explosion_titan_missile_03",
            2.51189,
            1,
            1800
        ],
        "soundimpact": [
            "",
            1,
            1
        ],
        "soundsetexplosion": [
            "RocketsLight_Exp_SoundSet",
            "RocketsLight_Tail_SoundSet",
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
            "",
            1,
            1,
            150
        ],
        "supersoniccracknear": [
            "",
            1,
            1,
            50
        ],
        "suppressionradiusbulletclose": -1,
        "suppressionradiushit": 30,
        "thrust": 180,
        "thrusttime": 0.5,
        "timetolive": 8,
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
        "tracklead": 1,
        "trackoversteer": 1,
        "triggeronimpact": 1,
        "typicalspeed": 900,
        "underwaterhitrangecoef": 1,
        "visiblefire": 28,
        "visiblefiretime": 20,
        "warheadname": "HE",
        "watereffectoffset": 0.45,
        "weaponlocksystem": 0,
        "weapontype": "Default",
        "whistledist": 4,
        "whistleonfire": 0
    },
    "author": "Red Hammer Studios",
    "count": 1,
    "descriptionshort": "Type: 40mm Airburst HE-Fragmentation Rocket<br />Rounds: 1<br />Used in: RPG-7",
    "displayname": "Type-69 Airburst",
    "displaynameshort": "AIRBURST",
    "hiddenselections": [
        "camo_1",
        "camo_2"
    ],
    "hiddenselectionstextures": [
        "rhsafrf/addons/rhs_weapons/rpg7/data/rhs_rpg7v2_02_co.paa",
        "rhsafrf/addons/rhs_weapons/rpg7/data/type_69_co.paa"
    ],
    "initspeed": 134,
    "inventoryplacements": {},
    "library": {
        "libtextdesc": ""
    },
    "mass": 28.6,
    "maxleadspeed": 25,
    "maxthrowholdtime": 2,
    "maxthrowintensitycoef": 1.4,
    "mindamageforcamshakehit": "rhs_rpg7v2_type63_airburst",
    "minthrowintensitycoef": 0.3,
    "model": "rhsafrf/addons/rhs_weapons/rpg7/magazines/rhs_Type69_mag",
    "modelspecial": "rhsafrf/addons/rhs_weapons/mag_proxies/rhs_mag_type69",
    "modelspecialisproxy": 1,
    "namesound": "handgrenade",
    "picture": "rhsafrf/addons/rhs_inventoryicons/data/magazines/rhs_rpg7_type69_airburst_mag_ca.paa",
    "quickreload": 0,
    "reloadaction": "",
    "scope": 2,
    "selectionfireanim": "zasleh",
    "simulation": "ProxyMagazines",
    "type": "6 * \t\t256",
    "useaction": 0,
    "useactiontitle": "",
    "value": 5,
    "weaponpoolavailable": 1,
    "weight": 0
}