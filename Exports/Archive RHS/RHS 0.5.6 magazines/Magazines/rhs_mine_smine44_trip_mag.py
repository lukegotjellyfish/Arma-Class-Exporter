rhs_mine_smine44_trip_mag = {
    "author": "Red Hammer Studios",
    "scope": 2,
    # Ammo: CfgMagazines|rhs_mine_smine44_trip_mag|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "rhs_mine_smine44_trip_ammo",
        "model": "rhsgref|addons|rhsgref_weapons2|mines|Smine44|SMI44_HELPER_TRIP",
        "minemodeldisabled": "rhsgref|addons|rhsgref_weapons2|mines|Smine44|SMI44_ITEM_TRIP",
        "defaultmagazine": "rhs_mine_smine44_trip_mag",
        # Ammo: CfgAmmo|rhs_mine_smine44_trip_ammo|submunitionAmmo [Indent level: 1],
        "submunitionammo1": {
            "_dictAmmoName": "rhs_mine_smine44_trip_explo_ammo",
            "_dictAmmoChance": "1",
            "model": "rhsgref|addons|rhsgref_weapons2|mines|Smine44|SMI44_SUBMUNITION_TRIP",
            "explosiontime": 0.25,
            "hit": 20,
            "indirecthit": 20,
            "indirecthitrange": 20,
            "soundsetexplosion": ["M6slamMine_Exp_SoundSet","M6slamMine_Tail_SoundSet","Explosion_Debris_SoundSet"],
            "supersoniccracknear": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_close",0.316228,1,50],
            "supersoniccrackfar": ["A3|Sounds_F|weapons|Explosion|supersonic_crack_50meters",0.223872,1,150],
            "cratereffects": "HEShellCrater",
            "craterwatereffects": "ImpactEffectsWaterHE",
            "explosioneffects": "HEShellExplosion",
            "visiblefire": 64,
            "audiblefire": 250,
            "dangerradiushit": -1,
            "suppressionradiushit": 30,
            "timetolive": 360,
            "muzzleeffect": "",
            "caliber": 34,
            "deflecting": 10,
            "deflectiondirdistribution": 0.39,
            "penetrationdirdistribution": 0.26,
            "whistleonfire": 2,
            "aiammousageflags": "64 + 128 + 256",
            # Class: CfgAmmo|ShellBase|HitEffects [Indent level: 1],
            "hiteffects": {
                "hitwater": "ImpactEffectsWaterRocket"
            },
            "soundfakefall0": ["a3|Sounds_F|weapons|falling_bomb|fall_01",3.16228,1,1000],
            "soundfakefall1": ["a3|Sounds_F|weapons|falling_bomb|fall_02",3.16228,1,1000],
            "soundfakefall2": ["a3|Sounds_F|weapons|falling_bomb|fall_03",3.16228,1,1000],
            "soundfakefall3": ["a3|Sounds_F|weapons|falling_bomb|fall_04",3.16228,1,1000],
            "soundfakefall": ["soundFakeFall0",0.25,"soundFakeFall1",0.25,"soundFakeFall2",0.25,"soundFakeFall3",0.25],
            "soundsetsoniccrack": ["bulletSonicCrack_SoundSet","bulletSonicCrackTail_SoundSet"],
            "simulation": "shotShell",
            "simulationstep": 0.05,
            "cost": 1000,
            "soundhit": ["",316.228,1],
            "soundfly": ["",0.0316228,4],
            "visiblefiretime": 10,
            "access": 3,
            "underwaterhitrangecoef": 1,
            "typicalspeed": 900,
            "explosionforcecoef": 1,
            "iscrateroriented": 0,
            "proxyshape": "",
            "cratershape": "",
            "weapontype": "Default",
            "animated": 0,
            "shadow": 0,
            "maxspeed": 0,
            "cartridge": "",
            "tracercolor": [0.7,0.7,0.5,0.04],
            "tracercolorr": [0.7,0.7,0.5,0.04],
            "soundengine": ["",1,1],
            "soundfall": ["",1,1],
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
            "explosionsoundeffect": "",
            "mintimetolive": 0,
            "irlock": 0,
            "airlock": 0,
            "laserlock": 0,
            "nvlock": 0,
            "artillerylock": 0,
            "hitonwater": 0,
            "lockseekradius": 100,
            "manualcontrol": 0,
            "maxcontrolrange": 350,
            "maneuvrability": 1,
            "tracklead": 1,
            "trackoversteer": 1,
            "missilelockcone": 0,
            "weaponlocksystem": 0,
            "cmimmunity": 1,
            "locktype": 0,
            "maverickweaponindexoffset": 0,
            "sideairfriction": 1,
            "artillerydispersion": 1,
            "artillerycharge": 1,
            "autoseektarget": 0,
            "shootdistraction": -1,
            "fusedistance": 0,
            "inittime": 0,
            "thrusttime": 1.5,
            "thrust": 210,
            "airfriction": -0.0005,
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
            "whistledist": 0,
            # Class: CfgAmmo|Default|NVGMarkers [Indent level: 1],
            "nvgmarkers": {
            },
            "mindamageforcamshakehit": 0.55,
            # Class: CfgAmmo|Default|EventHandlers [Indent level: 1],
            "eventhandlers": {
            },
        },
        "eventhandlers": ["rhs_mine_smine44_trip_explo_ammo",1],
        "cost": 200,
        "minetrigger": "rhsgref_sMine_tripwire_trigger",
        "mineplacedist": 0.5,
        "submunitioninitspeed": 4,
        "soundhit1": [],
        "soundhit2": [],
        "multisoundhit": [],
        "soundtrigger": [],
        "soundsetexplosion": [],
        "soundactivation": ["A3|Sounds_F_Orange|arsenal|explosives|Handling|ApersMine_Placement_01",0.398107,1,20],
        "sounddeactivation": ["A3|Sounds_F_Orange|arsenal|explosives|Handling|ApersMine_Deactivate_01",1.41254,1,20],
        "explosioneffects": "",
        "cratereffects": "",
        "deleteparentwhentriggered": 1,
        "submunitionconeangle": [0,10],
        "submunitionconeanglehorizontal": 720,
        "submunitionautoleveling": 1,
        "submunitionconetype": ["randomupcone",1],
        "minejumpeffects": "MineJumpEffect",
        # Class: CfgAmmo|rhs_mine_bounding_trigger_base|CamShakeExplode [Indent level: 1],
        "camshakeexplode": {
            "power": 0,
            "duration": 0.2,
            "frequency": 20,
            "distance": 0
        },
        # Class: CfgAmmo|rhs_mine_bounding_trigger_base|CamShakeHit [Indent level: 1],
        "camshakehit": {
            "power": 0,
            "duration": 0.2,
            "frequency": 20,
            "distance": 1
        },
        "hit": 0,
        "indirecthit": 0,
        "indirecthitrange": 0,
        "icon": "iconExplosiveAP",
        "whistledist": 8,
        "mineinconspicuousness": 50,
        "mapsize": 1,
        "explosiontype": "mine",
        "triggerwhendestroyed": 1,
        "underwaterhitrangecoef": 2,
        "aiammousageflags": 16,
        "simulation": "shotMine",
        "simulationstep": 0.1,
        "soundhit": ["",100,1],
        "soundfly": ["",0,1],
        "soundengine": ["",0,1],
        "visiblefire": 0,
        "audiblefire": 0,
        "visiblefiretime": 0,
        "timetolive": 0,
        "minecanbereactivated": 1,
        "access": 3,
        "typicalspeed": 900,
        "explosionforcecoef": 1,
        "iscrateroriented": 0,
        "proxyshape": "",
        "cratershape": "",
        "weapontype": "Default",
        "animated": 0,
        "shadow": 0,
        "maxspeed": 0,
        "cartridge": "",
        "tracercolor": [0.7,0.7,0.5,0.04],
        "tracercolorr": [0.7,0.7,0.5,0.04],
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
        "watereffectoffset": 0.45,
        "directionalexplosion": 0,
        "explosionangle": 60,
        "explosiondir": "explosionDir",
        "explosionpos": "explosionPos",
        "explosioneffectsdir": "explosionDir",
        "minimumsafezone": 0.1,
        "explosionsoundeffect": "",
        "mintimetolive": 0,
        "irlock": 0,
        "airlock": 0,
        "laserlock": 0,
        "nvlock": 0,
        "artillerylock": 0,
        "hitonwater": 0,
        "lockseekradius": 100,
        "manualcontrol": 0,
        "maxcontrolrange": 350,
        "maneuvrability": 1,
        "tracklead": 1,
        "trackoversteer": 1,
        "missilelockcone": 0,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "locktype": 0,
        "maverickweaponindexoffset": 0,
        "sideairfriction": 1,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "autoseektarget": 0,
        "shootdistraction": -1,
        "explosiontime": 0,
        "fusedistance": 0,
        "inittime": 0,
        "thrusttime": 1.5,
        "thrust": 210,
        "airfriction": -0.0005,
        "mineboundingtime": 3,
        "mineboundingdist": 3,
        "minefloating": -1,
        "minedivespeed": 1,
        # Class: CfgAmmo|Default|HitEffects [Indent level: 1],
        "hiteffects": {
            "vehicle": "ImpactMetal",
            "object": "ImpactConcrete"
        },
        "suppressionradiusbulletclose": -1,
        "suppressionradiushit": -1,
        "dangerradiusbulletclose": -1,
        "dangerradiushit": -1,
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
    "eventhandlers": "rhs_mine_smine44_trip_ammo",
    "picture": "rhsgref|addons|rhsgref_weapons2|icons|rhs_inv_smine44_trip_ca.paa",
    "displayname": "S.Mi.44 (S.Mi.Z.44) APB Mine",
    "displaynameshort": "S.Mi.44",
    "descriptionshort": "Schrapnellmine 44 Bounding Anti-Personnel Mine with S.Mi.Z.44 dual-tripwire igniter.",
    "mass": 80,
    "model": "rhsgref|addons|rhsgref_weapons2|mines|Smine44|SMI44_ITEM_TRIP",
    # Class: CfgMagazines|APERSBoundingMine_Range_Mag|Library [Indent level: 1],
    "library": {
        "libtextdesc": "The anti-personnel bounding mine is best suitable for open areas. It is usually burried just bellow the surface of the ground. When triggered, a charge launches the body of the mine one meter into the air. The explosion covers a close area with fragments, killing the whole group."
    },
    "descriptionuse": "<t color='#9cf953'>Use: </t>Place Mine",
    "allowedslots": [901,701],
    "useaction": 1,
    "useactiontitle": "Put %1 (%2 left)",
    "type": "2*		256",
    "value": 5,
    "namesoundweapon": "mine",
    "namesound": "mine",
    "count": 1,
    "initspeed": 0,
    "maxleadspeed": 0,
    "weaponpoolavailable": 1,
    "sound": ["A3|sounds_f|dummysound",0.000316228,1,10],
    "modelspecial": "",
    "reloadaction": "",
    "selectionfireanim": "zasleh",
    "simulation": "ProxyMagazines",
    "weight": 0,
    # Class: CfgMagazines|Default|InventoryPlacements [Indent level: 1],
    "inventoryplacements": {
    },
    "maxthrowholdtime": 2,
    "minthrowintensitycoef": 0.3,
    "maxthrowintensitycoef": 1.4,
    "quickreload": 0,
}