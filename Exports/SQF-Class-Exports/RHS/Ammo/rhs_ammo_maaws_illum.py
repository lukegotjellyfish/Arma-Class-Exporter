d = {
    "access": 3,
    "airfriction": 0.01,
    "airlock": 0,
    "allowagainstinfantry": 0,
    "animated": 0,
    "artillerycharge": 1,
    "artillerydispersion": 1,
    "artillerylock": 0,
    "audiblefire": 20,
    "autoseektarget": 0,
    "caliber": 1,
    "camshakeexplode": {
        "distance": "((5 + 55^0.5)*8)",
        "duration": "((round (55^0.5))*0.2 max 0.2)",
        "frequency": 20,
        "power": "(55*0.2)"
    },
    "camshakefire": {
        "distance": "((20^0.5)*8)",
        "duration": "((round (20^0.5))*0.2 max 0.2)",
        "frequency": 20,
        "power": 5
    },
    "camshakehit": {
        "distance": 1,
        "duration": "((round (110^0.25))*0.2 max 0.2)",
        "frequency": 20,
        "power": 110
    },
    "camshakeplayerfire": {
        "distance": 1,
        "duration": 0.2,
        "frequency": 8,
        "power": 2
    },
    "cartridge": "",
    "cmimmunity": 1,
    "cost": 300,
    "cratereffects": "ExploAmmoCrater",
    "cratershape": "",
    "craterwatereffects": "ImpactEffectsWater",
    "dangerradiusbulletclose": -1,
    "dangerradiushit": -1,
    "deflecting": 5,
    "deflectionslowdown": 0.8,
    "directionalexplosion": 0,
    "effectflare": "FlareShell",
    "effectfly": "ArtilleryTrails",
    "effectsfire": "CannonFire",
    "effectsmissile": "RHSUSF_SMAW_MissileTrail",
    "effectsmissileinit": "",
    "effectssmoke": "SmokeShellWhite",
    "eventhandlers": {
        "rhs_aps_firedeh": {
            "fired": "_this spawn rhs_fnc_aps_missileFired"
        }
    },
    "explosionangle": 60,
    "explosiondir": "explosionDir",
    "explosioneffects": "ExplosionEffects",
    "explosioneffectsdir": "explosionDir",
    "explosionforcecoef": 1,
    "explosionpos": "explosionPos",
    "explosionsoundeffect": "DefaultExplosion",
    "explosiontime": 0,
    "explosiontype": "explosive",
    "explosive": 1,
    "fusedistance": 0,
    "grenadeburningsound": [],
    "grenadefiresound": [],
    "hit": 30,
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
    "indirecthit": 0,
    "indirecthitrange": 1,
    "inittime": 0,
    "irlock": 0,
    "iscrateroriented": 0,
    "laserlock": 0,
    "lockseekradius": 100,
    "locktype": 0,
    "maneuvrability": 0,
    "manualcontrol": 0,
    "maverickweaponindexoffset": 0,
    "maxcontrolrange": 0,
    "maxspeed": 255,
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
    "model": "rhsusf/addons/rhsusf_weapons2/m3maaws/ammo_m3maaws.p3d",
    "multisoundhit": [
        "soundHit1",
        0.25,
        "soundHit2",
        0.25,
        "soundHit3",
        0.25,
        "soundHit4",
        0.25
    ],
    "muzzleeffect": "BIS_fnc_effectFiredRocket",
    "nvgmarkers": {},
    "nvlock": 0,
    "proxyshape": "",
    "shadow": 0,
    "shootdistraction": -1,
    "sideairfriction": 0,
    "simulation": "shotRocket",
    "simulationstep": 0.02,
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
        1.1,
        900
    ],
    "soundhit": [
        "A3/Sounds_F/weapons/Rockets/explosion_missile_02",
        2.51189,
        1,
        2500
    ],
    "soundhit1": [
        "A3/Sounds_F/arsenal/explosives/shells/Artillery_tank_shell_155mm_explosion_01",
        2.51189,
        1,
        1900
    ],
    "soundhit2": [
        "A3/Sounds_F/arsenal/explosives/shells/Artillery_tank_shell_155mm_explosion_02",
        2.51189,
        1,
        1900
    ],
    "soundhit3": [
        "A3/Sounds_F/arsenal/explosives/shells/Artillery_tank_shell_155mm_explosion_03",
        2.51189,
        1,
        1900
    ],
    "soundhit4": [
        "A3/Sounds_F/arsenal/explosives/shells/Artillery_tank_shell_155mm_explosion_04",
        2.51189,
        1,
        1900
    ],
    "soundimpact": [
        "",
        1,
        1
    ],
    "soundtrigger": [],
    "submunitionammo": "",
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
    "thrust": 0.1,
    "thrusttime": 0.1,
    "timetolive": 25,
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
    "typicalspeed": 900,
    "underwaterhitrangecoef": 1,
    "visiblefire": 15,
    "visiblefiretime": 20,
    "watereffectoffset": 0.45,
    "weaponlocksystem": 0,
    "weapontype": "Default",
    "whistledist": 0,
    "whistleonfire": 0
}