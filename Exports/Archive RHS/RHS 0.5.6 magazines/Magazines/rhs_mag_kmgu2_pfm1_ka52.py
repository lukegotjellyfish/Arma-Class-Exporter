rhs_mag_kmgu2_pfm1_ka52 = {
    "model": "rhsafrf|addons|rhs_airweapons|rhs_pylon_m_kmgu2_ka52",
    "hardpoints": ["RHS_HP_KMGU2_KA52"],
    # Ammo: CfgMagazines|rhs_mag_kmgu2_pfm1|ammo [Indent level: 1],
    "ammo": {
        "_dictAmmoName": "rhs_ammo_kmgu2_pfm1",
        # Ammo: CfgAmmo|rhs_ammo_kmgu2_pfm1|submunitionAmmo [Indent level: 1],
        "submunitionammo1": {
            "_dictAmmoName": "rhs_ammo_pfm1_deploy",
            "_dictAmmoChance": "1",
            "model": "rhsafrf|addons|rhs_airweapons|rhs_m_pfm1",
            # Ammo: CfgAmmo|rhs_ammo_pfm1_deploy|submunitionAmmo [Indent level: 1],
            "submunitionammo": {
                "_dictAmmoName": "rhs_ammo_pfm1",
                "hit": 9,
                "indirecthit": 8,
                "indirecthitrange": 2,
                "model": "rhsafrf|addons|rhs_airweapons|rhs_m_pfm1_d",
                "minemodeldisabled": "rhsafrf|addons|rhs_airweapons|rhs_m_pfm1_d",
                "defaultmagazine": "rhs_mag_mine_pfm1",
                "cost": 200,
                "mineinconspicuousness": 60,
                "minetrigger": "RangeTriggerShort",
                "minefloating": 1e+007,
                "icon": "iconExplosiveAP",
                "soundhit1": ["A3|Sounds_F|arsenal|explosives|mines|AP_mines_explosion_01",3.16228,1,1500],
                "soundhit2": ["A3|Sounds_F|arsenal|explosives|mines|AP_mines_explosion_02",3.16228,1,2000],
                "multisoundhit": ["soundHit1",0.5,"soundHit2",0.5],
                "soundtrigger": ["A3|Sounds_F_Orange|arsenal|explosives|Handling|ApersMine_Trigger_01",2.51189,1,20],
                "soundactivation": ["A3|Sounds_F_Orange|arsenal|explosives|Handling|ApersMine_Placement_01",0.398107,1,20],
                "sounddeactivation": ["A3|Sounds_F_Orange|arsenal|explosives|Handling|ApersMine_Deactivate_01",1.41254,1,20],
                "explosioneffects": "MineExplosion",
                "cratereffects": "MineCrater",
                "whistledist": 8,
                "soundsetexplosion": ["APmine_Exp_SoundSet","APmine_Tail_SoundSet","Explosion_Debris_SoundSet"],
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
                "minejumpeffects": "",
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
                "submunitionammo": "",
                "mineboundingtime": 3,
                "mineboundingdist": 3,
                "minedivespeed": 1,
                "mineplacedist": 0.5,
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
            "eventhandlers": "rhs_ammo_pfm1",
            "simulation": "shotDeploy",
            "simulationstep": 0.05,
            "timetolive": 180,
            "cost": 1000,
            "soundhit": ["",316.228,1],
            "soundfly": ["",0.0316228,4],
            "hitonwater": 1,
            "artillerylock": 1,
            "indirecthitrange": 8,
            "visiblefire": 16,
            "audiblefire": 16,
            "visiblefiretime": 10,
            "deflecting": 5,
            "access": 3,
            "hit": 0,
            "indirecthit": 0,
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
            "deflectionslowdown": 0.8,
            "explosive": 1,
            "explosioneffects": "ExplosionEffects",
            "cratereffects": "ImpactEffectsMedium",
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
            "explosionsoundeffect": "",
            "mintimetolive": 0,
            "irlock": 0,
            "airlock": 0,
            "laserlock": 0,
            "nvlock": 0,
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
            "icon": "",
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
            "suppressionradiushit": -1,
            "dangerradiusbulletclose": -1,
            "dangerradiushit": -1,
            "caliber": 1,
            "whistledist": 0,
            "whistleonfire": 0,
            # Class: CfgAmmo|Default|NVGMarkers [Indent level: 1],
            "nvgmarkers": {
            },
            "mindamageforcamshakehit": 0.55,
            # Class: CfgAmmo|Default|EventHandlers [Indent level: 1],
            "eventhandlers": {
            },
        },
        "eventhandlers": ["rhs_ammo_pfm1_deploy",1],
        "submunitionconetype": ["random",40],
        "model": "rhsafrf|addons|rhs_airweapons|rhs_m_ao25_x12_fly",
        "proxyshape": "rhsafrf|addons|rhs_airweapons|rhs_m_ao25_x12",
        "triggertime": 2.5,
        "submunitionconeangle": 14,
        "triggerspeedcoef": [0.8,1.1],
        "laserlock": 0,
        "allowagainstinfantry": 1,
        "autoseektarget": 0,
        "aiammousageflags": "64 + 128 + 512",
        "weaponlocksystem": 1,
        "maverickweaponindexoffset": 0,
        "simulation": "shotMissile",
        "triggerdistance": 250,
        # Class: CfgAmmo|rhs_ammo_rbk250_ao1|Components [Indent level: 1],
        "components": {
            # Class: CfgAmmo|rhs_ammo_rbk250_ao1|Components|SensorsManagerComponent [Indent level: 2]
            "sensorsmanagercomponent": {
                # Class: CfgAmmo|rhs_ammo_rbk250_ao1|Components|SensorsManagerComponent|Components [Indent level: 3]
                "components": {
                }
            }
        },
        "hit": 5000,
        "indirecthit": 1140,
        "indirecthitrange": 15,
        "dangerradiushit": 1250,
        "suppressionradiushit": 100,
        "cost": 50,
        "flightprofiles": ["Direct"],
        # Class: CfgAmmo|rhs_ammo_fab100|Direct [Indent level: 1],
        "direct": {
        },
        "explosionforcecoef": 10,
        "irlock": 0,
        "soundfakefall0": ["a3|Sounds_F|weapons|falling_bomb|fall_01",3.16228,1,1000],
        "soundfakefall1": ["a3|Sounds_F|weapons|falling_bomb|fall_02",3.16228,1,1000],
        "soundfakefall2": ["a3|Sounds_F|weapons|falling_bomb|fall_03",3.16228,1,1000],
        "soundfakefall3": ["a3|Sounds_F|weapons|falling_bomb|fall_04",3.16228,1,1000],
        "soundfakefall": ["soundFakeFall0",0.25,"soundFakeFall1",0.25,"soundFakeFall2",0.25,"soundFakeFall3",0.25],
        "soundsetexplosion": ["BombsHeavy_Exp_SoundSet","BombsHeavy_Tail_SoundSet","Explosion_Debris_SoundSet"],
        "maneuvrability": 10,
        "fusedistance": 50,
        "tracklead": 0.95,
        "trackoversteer": 1,
        "airfriction": 0.06,
        "sideairfriction": 0.12,
        "cratereffects": "BombCrater",
        "explosioneffects": "BombExplosion",
        "explosionsoundeffect": "DefaultExplosion",
        "explosiontime": 2,
        "multisoundhit": ["soundHit1",0.2,"soundHit2",0.2,"soundHit3",0.2,"soundHit4",0.2,"soundHit5",0.2],
        "soundhit1": ["|A3|Sounds_F|weapons|Explosion|expl_big_1",2.51189,1,2400],
        "soundhit2": ["|A3|Sounds_F|weapons|Explosion|expl_big_2",2.51189,1,2400],
        "soundhit3": ["|A3|Sounds_F|weapons|Explosion|expl_big_3",2.51189,1,2400],
        "soundhit4": ["|A3|Sounds_F|weapons|Explosion|expl_shell_1",2.51189,1,2400],
        "soundhit5": ["|A3|Sounds_F|weapons|Explosion|expl_shell_2",2.51189,1,2400],
        "whistledist": 24,
        "missilelockcone": 120,
        "missilekeeplockedcone": 120,
        "missilelockmaxdistance": 5000,
        "missilelockmindistance": 100,
        "missilelockmaxspeed": 30,
        "lockseekradius": 500,
        "cmimmunity": 0.3,
        # Class: CfgAmmo|ammo_Bomb_LaserGuidedBase|LoalAltitude [Indent level: 1],
        "loalaltitude": {
            "lockseekaltitude": 500
        },
        "maxcontrolrange": 100000,
        "maxspeed": 100,
        "timetolive": 120,
        "inittime": 0,
        "thrusttime": 0,
        "thrust": 0,
        "access": 3,
        "underwaterhitrangecoef": 1,
        "typicalspeed": 900,
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
        "manualcontrol": 0,
        "locktype": 0,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "visiblefire": 0,
        "audiblefire": 0,
        "shootdistraction": -1,
        "visiblefiretime": 0,
        "icon": "",
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
    "eventhandlers": "rhs_ammo_kmgu2_pfm1",
    "displayname": "KMGU-2 PFM-1",
    "displaynameshort": "Cluster AP Mine",
    "pylonweapon": "rhs_weap_kmgu2_pfm1",
    "ejectspeed": [1,0,0],
    "initspeed": 0,
    "initspeedy": -5,
    "initspeedz": 0,
    "weight": 500,
    "mass": 500,
    "count": 8,
    # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements [Indent level: 1],
    "mfdelements": {
        # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_ammoname [Indent level: 2]
        "rhs_rus_ammoname": {
            # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_ammoname|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_ammoname|Draw [Indent level: 3],
            "draw": {
                "condition": "PylonSelected",
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_ammoname|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "КМГ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "center",
                    "pos": [[-0.005,0.02],1],
                    "right": [[0.045,0.02],1],
                    "down": [[-0.005,0.065],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_ammoname_right [Indent level: 2],
        "rhs_rus_ammoname_right": {
            # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_ammoname_right|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_ammoname_right|Draw [Indent level: 3],
            "draw": {
                "condition": "PylonSelected",
                "color": [0.15,1,0.15],
                "alpha": 1,
                # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_ammoname_right|Draw|PylonText1 [Indent level: 4],
                "pylontext1": {
                    "type": "text",
                    "source": "static",
                    "text": "КМГ",
                    "scale": 1,
                    "sourcescale": 1,
                    "align": "right",
                    "pos": [[-0.005,0.02],1],
                    "right": [[0.045,0.02],1],
                    "down": [[-0.005,0.065],1]
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_su25_box [Indent level: 2],
        "rhs_su25_box": {
            # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_su25_box|Bones [Indent level: 3]
            "bones": {
            },
            # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_su25_box|Draw [Indent level: 3],
            "draw": {
                "condition": "1-pylonMagazineEmpty",
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_su25_box|Draw|Shape [Indent level: 4],
                "shape": {
                    "type": "polygon",
                    "width": 4,
                    "points": [[[[-0.022,-0.04],1],[[0.022,-0.04],1],[[0.022,0.04],1],[[-0.022,0.04],1]]]
                },
                # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_su25_box|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.58,0.23,0],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_su25_box|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[[[-0.022,0.18],1],[[0.022,0.18],1],[[0.022,0.26],1],[[-0.022,0.26],1]]]
                    }
                }
            }
        },
        # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle [Indent level: 2],
        "rhs_rus_circle": {
            # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Bones [Indent level: 3]
            "bones": {
                # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Bones|Center [Indent level: 4]
                "center": {
                    "type": "fixed",
                    "pos": [0,0]
                }
            },
            # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw [Indent level: 3],
            "draw": {
                "color": [0.15,1,0.15,1],
                "alpha": 0.22,
                # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Default [Indent level: 4],
                "default": {
                    "condition": "1-PylonSelected-pylonMagazineEmpty",
                    "color": [1,1,1],
                    # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Default|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "КМГ",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Default|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0282847],1],["Center",[0.0125,-0.0244945],1],["Center",[0.02165,-0.0141423],1],["Center",[0.025,0],1],["Center",[0.02165,0.0141423],1],["Center",[0.0125,0.0244945],1],["Center",[0,0.0282847],1],["Center",[-0.0125,0.0244945],1],["Center",[-0.02165,0.0141423],1],["Center",[-0.025,0],1],["Center",[-0.02165,-0.0141423],1],["Center",[-0.0125,-0.0244945],1],["Center",[0,-0.0282847],1],[],["Center",[0.0176777,-0.0200003],1],["Center",[0.0282843,-0.0320005],1],[],["Center",[0.0176777,0.0200003],1],["Center",[0.0282843,0.0320005],1],[],["Center",[-0.0176777,0.0200003],1],["Center",[-0.0282843,0.0320005],1],[],["Center",[-0.0176777,-0.0200003],1],["Center",[-0.0282843,-0.0320004],1],[]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Selected [Indent level: 4],
                "selected": {
                    "condition": "PylonSelected*(PylonAmmoRelative>=0.001)",
                    "color": [0.15,1,0.15,1],
                    "alpha": 0.22,
                    # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Selected|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "КМГ",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Selected|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0282847],1],["Center",[0.0125,-0.0244945],1],["Center",[0.02165,-0.0141423],1],["Center",[0.025,0],1],["Center",[0.02165,0.0141423],1],["Center",[0.0125,0.0244945],1],["Center",[0,0.0282847],1],["Center",[-0.0125,0.0244945],1],["Center",[-0.02165,0.0141423],1],["Center",[-0.025,0],1],["Center",[-0.02165,-0.0141423],1],["Center",[-0.0125,-0.0244945],1],["Center",[0,-0.0282847],1],[],["Center",[0.0176777,-0.0200003],1],["Center",[0.0282843,-0.0320005],1],[],["Center",[0.0176777,0.0200003],1],["Center",[0.0282843,0.0320005],1],[],["Center",[-0.0176777,0.0200003],1],["Center",[-0.0282843,0.0320005],1],[],["Center",[-0.0176777,-0.0200003],1],["Center",[-0.0282843,-0.0320004],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Selected|Polygon [Indent level: 5],
                    "polygon": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[["Center",1,[0,0],1],["Center",[0.0176777,-0.0200003],1],["Center",[0.025,1.23636e-009],1],["Center",[0.0176777,0.0200003],1]],[["Center",1,[0,0],1],["Center",[0.0176777,0.0200003],1],["Center",[-2.18557e-009,0.0282847],1],["Center",[-0.0176777,0.0200003],1]],[["Center",1,[0,0],1],["Center",[-0.0176777,0.0200003],1],["Center",[-0.025,-3.37291e-010],1],["Center",[-0.0176777,-0.0200003],1]],[["Center",1,[0,0],1],["Center",[-0.0176777,-0.0200003],1],["Center",[4.37114e-009,-0.0282847],1],["Center",[0.0176777,-0.0200003],1]]]
                    }
                },
                # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Empty [Indent level: 4],
                "empty": {
                    "condition": "pylonMagazineEmpty",
                    "color": [1,0,0,1],
                    # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Empty|PylonText1 [Indent level: 5],
                    "pylontext1": {
                        "type": "text",
                        "source": "static",
                        "text": "КМГ",
                        "scale": 1,
                        "sourcescale": 1,
                        "align": "center",
                        "pos": [[-0.005,0.06],1],
                        "right": [[0.04,0.06],1],
                        "down": [[-0.005,0.105],1]
                    },
                    # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Empty|Shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Center",[0,-0.0282847],1],["Center",[0.0125,-0.0244945],1],["Center",[0.02165,-0.0141423],1],["Center",[0.025,0],1],["Center",[0.02165,0.0141423],1],["Center",[0.0125,0.0244945],1],["Center",[0,0.0282847],1],["Center",[-0.0125,0.0244945],1],["Center",[-0.02165,0.0141423],1],["Center",[-0.025,0],1],["Center",[-0.02165,-0.0141423],1],["Center",[-0.0125,-0.0244945],1],["Center",[0,-0.0282847],1],[],["Center",[0.0176777,-0.0200003],1],["Center",[0.0282843,-0.0320005],1],[],["Center",[0.0176777,0.0200003],1],["Center",[0.0282843,0.0320005],1],[],["Center",[-0.0176777,0.0200003],1],["Center",[-0.0282843,0.0320005],1],[],["Center",[-0.0176777,-0.0200003],1],["Center",[-0.0282843,-0.0320004],1],[]]
                    },
                    # Class: CfgMagazines|rhs_mag_kmgu2_ao25|mfdElements|rhs_rus_circle|Draw|Empty|Polygon [Indent level: 5],
                    "polygon": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[["Center",1,[0,0],1],["Center",[0.0176777,-0.0200003],1],["Center",[0.025,1.23636e-009],1],["Center",[0.0176777,0.0200003],1]],[["Center",1,[0,0],1],["Center",[0.0176777,0.0200003],1],["Center",[-2.18557e-009,0.0282847],1],["Center",[-0.0176777,0.0200003],1]],[["Center",1,[0,0],1],["Center",[-0.0176777,0.0200003],1],["Center",[-0.025,-3.37291e-010],1],["Center",[-0.0176777,-0.0200003],1]],[["Center",1,[0,0],1],["Center",[-0.0176777,-0.0200003],1],["Center",[4.37114e-009,-0.0282847],1],["Center",[0.0176777,-0.0200003],1]]]
                    },
                    "alpha": 0.22
                }
            }
        }
    },
    "scope": 2,
    "maxleadspeed": 5,
    "namesound": "",
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
    "descriptionshort": "",
    "maxthrowholdtime": 2,
    "minthrowintensitycoef": 0.3,
    "maxthrowintensitycoef": 1.4,
    "quickreload": 0,
}