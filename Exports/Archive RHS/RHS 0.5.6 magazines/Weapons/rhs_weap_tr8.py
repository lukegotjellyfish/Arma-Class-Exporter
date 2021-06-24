rhs_weap_tr8 = {
    "author": "Red Hammer Studios",
    "dlc": "RHS_AFRF",
    "magazines": [],
    # Class: CfgWeapons|rhs_weap_tr8|Library [Indent level: 1],
    "library": {
        "libtextdesc": ""
    },
    "optics": 1,
    "scope": 2,
    "muzzlepos": "eye",
    "muzzleend": "eye_dir",
    "weaponinfotype": "RscWeaponZeroing",
    "discretedistance": [0],
    "discretedistanceinitindex": 0,
    "displayname": "TR-8 Periscope",
    "descriptionshort": "<t color='#9cf953'>Use: </t>Toggle Binoculars",
    "model": "rhsafrf|addons|rhs_weapons2|misc|tr8|rhs_tr8_periscope _weap.p3d",
    "modeloptics": "rhsafrf|addons|rhs_weapons2|misc|tr8|rhs_tr8_reticle.p3d",
    "picture": "rhsafrf|addons|rhs_weapons2|icons|rhs_tr8_inventory_ca.paa",
    "uipicture": "A3|weapons_f|data|UI|icon_regular_CA.paa",
    # Class: CfgWeapons|rhs_weap_tr8|OpticsModes [Indent level: 1],
    "opticsmodes": {
        # Class: CfgWeapons|rhs_weap_tr8|OpticsModes|periscope [Indent level: 2]
        "periscope": {
            "opticsid": 1,
            "opticsppeffects": ["OpticsCHAbera1","OpticsBlur1"],
            "modeloptics": "rhsafrf|addons|rhs_weapons2|misc|tr8|rhs_tr8_reticle.p3d",
            "usemodeloptics": 1,
            "opticsflare": 0,
            "opticsdisableperipherialvision": 0,
            "opticszoommin": "0.35/8",
            "opticszoommax": "0.35/8",
            "opticszoominit": "0.35/8",
            "visionmode": "",
            "discretedistanceinitindex": 0,
            "discretedistance": [100],
            "memorypointcamera": "eye",
            "cameradir": "eye_dir",
            "distancezoommin": 300,
            "distancezoommax": 300
        }
    },
    # Class: CfgWeapons|rhs_weap_tr8|WeaponSlotsInfo [Indent level: 1],
    "weaponslotsinfo": {
        "mass": 19.36,
        "holsterscale": 0
    },
    "sounds": ["StandardSound"],
    # Class: CfgWeapons|rhs_weap_tr8|BaseSoundModeType [Indent level: 1],
    "basesoundmodetype": {
        "weaponsoundeffect": "DefaultRifle",
        "closure1": ["",1.03514,1,10],
        "closure2": ["",1.03514,1.1,10],
        "soundclosure": ["closure1",0.5,"closure2",0.5]
    },
    # Class: CfgWeapons|rhs_weap_tr8|StandardSound [Indent level: 1],
    "standardsound": {
        "weaponsoundeffect": "DefaultRifle",
        "closure1": ["",1.03514,1,10],
        "closure2": ["",1.03514,1.1,10],
        "soundclosure": ["closure1",0.5,"closure2",0.5]
    },
    "handanim": ["OFP2_ManSkeleton","|rhsafrf|addons|rhs_c_weapons|anims|tr8_holdinganim.rtm"],
    "dexterity": 1.8,
    "baseweapon": "rhs_weap_tr8",
    "bullet1": ["A3|sounds_f|weapons|shells|9mm|metal_9mm_01",0.562341,1,15],
    "bullet2": ["A3|sounds_f|weapons|shells|9mm|metal_9mm_02",0.562341,1,15],
    "bullet3": ["A3|sounds_f|weapons|shells|9mm|metal_9mm_03",0.562341,1,15],
    "bullet4": ["A3|sounds_f|weapons|shells|9mm|metal_9mm_04",0.562341,1,15],
    "bullet5": ["A3|sounds_f|weapons|shells|9mm|dirt_9mm_01",0.562341,1,15],
    "bullet6": ["A3|sounds_f|weapons|shells|9mm|dirt_9mm_02",0.562341,1,15],
    "bullet7": ["A3|sounds_f|weapons|shells|9mm|dirt_9mm_03",0.562341,1,15],
    "bullet8": ["A3|sounds_f|weapons|shells|9mm|dirt_9mm_04",0.562341,1,15],
    "bullet9": ["A3|sounds_f|weapons|shells|9mm|grass_9mm_01",0.562341,1,15],
    "bullet10": ["A3|sounds_f|weapons|shells|9mm|grass_9mm_02",0.562341,1,15],
    "bullet11": ["A3|sounds_f|weapons|shells|9mm|grass_9mm_03",0.562341,1,15],
    "bullet12": ["A3|sounds_f|weapons|shells|9mm|grass_9mm_04",0.562341,1,15],
    "soundbullet": ["bullet1",0.083,"bullet2",0.083,"bullet3",0.083,"bullet4",0.083,"bullet5",0.083,"bullet6",0.083,"bullet7",0.083,"bullet8",0.083,"bullet9",0.083,"bullet10",0.083,"bullet11",0.083,"bullet12",0.083],
    "opticszoommin": 0.25,
    "opticszoommax": 1.25,
    "opticszoominit": 0.75,
    "cursor": "hgun",
    "cursoraim": "cursorAim",
    "minrange": 0,
    "minrangeprobab": 0.1,
    "midrange": 30,
    "midrangeprobab": 0.3,
    "maxrange": 50,
    "maxrangeprobab": 0.04,
    "reloadaction": "GestureReloadPistol",
    # Recoil Class: recoil,
    # Class: CfgRecoils|recoil_default [Indent level: 0],
    "recoil": {
        "muzzleouter": [0.3,1,0.3,0.2],
        "muzzleinner": [0,0,0.1,0.1],
        "kickback": [0.03,0.06],
        "permanent": 0.1,
        "temporary": 0.01
    },
    "recoil": "recoil_default",
    "weaponpoolavailable": 1,
    "texturetype": "semi",
    # Class: CfgWeapons|Pistol_Base_F|GunParticles [Indent level: 1],
    "gunparticles": {
        # Class: CfgWeapons|Pistol_Base_F|GunParticles|FirstEffect [Indent level: 2]
        "firsteffect": {
            "effectname": "PistolCloud",
            "positionname": "Usti hlavne",
            "directionname": "Konec hlavne"
        }
    },
    "htmin": 1,
    "htmax": 300,
    "afmax": 0,
    "mfmax": 0,
    "mfact": 1,
    "tbody": 100,
    "autoreload": 0,
    "maxzeroing": 100,
    "magazinereloadtime": 2,
    "opticsflare": 0,
    "namesound": "Pistol",
    "type": 2,
    "canlock": 0,
    "inertia": 0.1,
    "access": 3,
    "value": 2,
    "ammo": "",
    "cursorsize": 1,
    "showaimcursorinternal": 1,
    "cursoraimon": "",
    "laser": 0,
    "hiddenselections": [],
    "hiddenselectionstextures": [],
    "hiddenunderwaterselections": [],
    "shownunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    "simulation": "Weapon",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "reloadtime": 1,
    "magazinereloadswitchphase": 1,
    "sound": ["",1,1],
    "soundbegin": ["sound",1],
    "soundbeginwater": ["sound",1],
    "soundclosure": ["sound",1],
    "soundend": ["sound",1],
    "soundloop": ["sound",1],
    "soundcontinuous": 0,
    "weaponsoundeffect": "",
    "soundburst": 1,
    "drysound": ["",1,1],
    "zeroingsound": ["",1,1],
    "reloadsound": ["",1,1],
    "changefiremodesound": ["",1,1],
    "reloadmagazinesound": ["",1,1],
    "emptysound": ["",1,1],
    "initspeed": 0,
    "ballisticscomputer": 0,
    "irdistance": 0,
    "irdotintensity": 0.001,
    "dispersion": 0.002,
    "aidispersioncoefx": 1,
    "aidispersioncoefy": 1,
    "lockacquire": 1,
    "enableattack": 1,
    "ffmagnitude": 0,
    "fffrequency": 1,
    "ffcount": 1,
    "recoilprone": "",
    "maxrecoilsway": 0.008,
    "swaydecayspeed": 2,
    "modelspecial": "",
    "modelmagazine": "",
    "irlaserpos": "laser pos",
    "irlaserend": "laser dir",
    "cartridgepos": "nabojnicestart",
    "cartridgevel": "nabojniceend",
    "selectionfireanim": "zasleh",
    "memorypointcamera": "eye",
    "firespreadangle": 3,
    "usemodeloptics": 1,
    "opticsid": 0,
    "opticsppeffects": [],
    "forceoptics": 0,
    "useasbinocular": 0,
    "opticsdisableperipherialvision": 0.67,
    "distancezoommin": 400,
    "distancezoommax": 400,
    "primary": 10,
    "showswitchaction": 0,
    "showempty": 1,
    "autofire": 0,
    "showtoplayer": 1,
    "canshootinwater": 0,
    "airateoffire": 5,
    "airateoffiredistance": 500,
    "airateoffiredispersion": 0,
    "firelightduration": 0.05,
    "firelightintensity": 0.2,
    "firelightdiffuse": [0.937,0.631,0.259],
    "firelightambient": [0,0,0],
    # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
    "eventhandlers": {
    },
    "backgroundreload": 0,
    "muzzles": ["this"],
    "modes": ["this"],
    "useaction": 0,
    "useactiontitle": "",
    "candrop": 1,
    "weaponlockdelay": 0,
    "weaponlocksystem": 0,
    "cmimmunity": 1,
    "weight": 0,
    "lockingtargetsound": ["",0.000316228,2],
    "lockedtargetsound": ["",0.000316228,6],
    "detectrange": 0,
    "artillerydispersion": 1,
    "artillerycharge": 1,
    "fireanims": [],
    # Class: CfgWeapons|Default|GunFire [Indent level: 1],
    "gunfire": {
        "access": 0,
        "cloudletduration": 0.2,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletgrowup": 0.2,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 0.5,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletFire",
        "cloudletcolor": [1,1,1,0],
        "cloudletdensitycoef": -1,
        "interval": -0.01,
        "size": 3,
        "sourcesize": 0.5,
        "timetolive": 0,
        "initt": 4500,
        "deltat": -3000,
        # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
        "table": {
            # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3]
            "t0": {
                "maxt": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
            "t1": {
                "maxt": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
            "t2": {
                "maxt": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
            "t3": {
                "maxt": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
            "t4": {
                "maxt": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
            "t5": {
                "maxt": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
            "t6": {
                "maxt": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
            "t7": {
                "maxt": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
            "t8": {
                "maxt": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
            "t9": {
                "maxt": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
            "t10": {
                "maxt": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
            "t11": {
                "maxt": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
            "t12": {
                "maxt": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
            "t13": {
                "maxt": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
            "t14": {
                "maxt": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
            "t15": {
                "maxt": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
            "t16": {
                "maxt": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
            "t17": {
                "maxt": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
            "t18": {
                "maxt": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
            "t19": {
                "maxt": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
            "t20": {
                "maxt": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
            "t21": {
                "maxt": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
            "t22": {
                "maxt": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
    "gunclouds": {
        "access": 0,
        "cloudletgrowup": 0.05,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.1,
        "cloudletduration": 0.05,
        "cloudletalpha": 0.3,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "interval": -0.02,
        "size": 0.3,
        "sourcesize": 0.02,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletshape": "cloudletClouds",
        "cloudletcolor": [1,1,1,0],
        "timetolive": 0,
        "initt": 0,
        "deltat": 0,
        # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
        "table": {
            # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3]
            "t0": {
                "maxt": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "aimtransitionspeed": 1,
}