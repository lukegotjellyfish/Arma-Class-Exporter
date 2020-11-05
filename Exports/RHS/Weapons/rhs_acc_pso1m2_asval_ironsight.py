rhs_acc_pso1m2_asval_ironsight = {
    "author": "Red Hammer Studios",
    "scope": 1,
    "scopearsenal": 0,
    # Class: CfgWeapons|rhs_acc_pso1m2_asval_ironsight|ItemInfo [Indent level: 1],
    "iteminfo": {
        # Class: CfgWeapons|rhs_acc_pso1m2_asval_ironsight|ItemInfo|OpticsModes [Indent level: 2]
        "opticsmodes": {
            # Class: CfgWeapons|rhs_acc_pso1m2_asval_ironsight|ItemInfo|OpticsModes|rhs_1p29_iron [Indent level: 3]
            "rhs_1p29_iron": {
                "discretedistance": [100,150,200,220,250,270,300,320,350],
                "discretedistancecamerapoint": ["eye_val","eye_val_150","eye_val_200","eye_val_220","eye_val_250","eye_val_270","eye_val_300","eye_val_320","eye_val_350"],
                "cameradir": "eye_val_look",
                "distancezoommax": 420,
                "opticsid": 1,
                "usemodeloptics": 0,
                "opticsppeffects": [""],
                "opticszoommin": 0.25,
                "opticszoommax": 1.1,
                "opticszoominit": 0.75,
                "memorypointcamera": "eye_svd",
                "discretedistanceinitindex": 0,
                "visionmode": [],
                "opticsflare": 0,
                "opticsdisableperipherialvision": 0,
                "distancezoommin": 300
            },
            # Class: CfgWeapons|rhs_acc_pso1m2_asval_ironsight|ItemInfo|OpticsModes|pso1_scope [Indent level: 3],
            "pso1_scope": {
                "discretedistanceinitindex": "(missionNameSpace getVariable ['rhs_acc_pso_index',2]) min 16 max 0",
                "opticsid": 2,
                "usemodeloptics": 1,
                "opticsppeffects": ["OpticsCHAbera2","OpticsBlur2","rhs_pso1_Blur"],
                "discretedistance": [100,200,300,350,400,450,500,550,600,650,700,750,800,850,900,950,1000],
                "opticszoommin": 0.0875,
                "opticszoommax": 0.0875,
                "opticszoominit": 0.0875,
                "memorypointcamera": "opticView",
                "visionmode": ["Normal"],
                "opticsflare": 1,
                "opticsdisableperipherialvision": 1,
                "distancezoommin": 200,
                "distancezoommax": 1000,
                "cameradir": ""
            }
        },
        "optictype": 2,
        "mass": 13.64,
        "rmbhint": "Optical Sniper Sight",
        "optics": 1,
        "modeloptics": "rhsafrf|addons|rhs_weapons|acc|scopes|optics|rhs_pso_scope",
        "type": 201,
        "muzzlepos": "usti hlavne",
        "muzzleend": "konec hlavne",
        "allowedslots": [801,701,901],
        "mountaction": "MountOptic",
        "unmountaction": "DismountOptic",
        "zeroingsound": ["A3|Sounds_F|arsenal|sfx|shared|zeroing_knob_tick_plastic",0.316228,1,5],
        "scope": 0
    },
    "picture": "rhsafrf|addons|rhs_inventoryicons|data|accessories|rhs_acc_pso1m2_ca.paa",
    "weaponinfotype": "rhs_rscOptics_acc_pso1",
    "inertia": 0.2,
    "rhs_optic_ads": "rhs_acc_pso1m2_ads",
    "rhs_optic_ads_night": "rhs_acc_pso1m2_ads_night",
    "rhs_optic_ads_base": "rhs_acc_pso1m2",
    "dlc": "RHS_AFRF",
    "displayname": "PSO-1M2",
    "model": "rhsafrf|addons|rhs_weapons|acc|scopes|pso1|rhs_pso1",
    "descriptionshort": "Optical Sniper Sight<br />Magnification: 4x",
    "muzzles": [],
    # Class: CfgWeapons|ItemCore|Armory [Indent level: 1],
    "armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uipicture": "",
    "ammo": "",
    "cursor": "",
    "cursoraim": "",
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
    "namesound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazinereloadtime": 0,
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
    "soundbullet": ["emptySound",1],
    "initspeed": 0,
    "ballisticscomputer": 0,
    "irdistance": 0,
    "irdotintensity": 0.001,
    "dispersion": 0.002,
    "aidispersioncoefx": 1,
    "aidispersioncoefy": 1,
    "canlock": 2,
    "lockacquire": 1,
    "enableattack": 1,
    "ffmagnitude": 0,
    "fffrequency": 1,
    "ffcount": 1,
    # Recoil Array: recoil,
    "recoil": [],
    "maxrecoilsway": 0.008,
    "swaydecayspeed": 2,
    "modelspecial": "",
    "modelmagazine": "",
    "muzzlepos": "usti hlavne",
    "muzzleend": "konec hlavne",
    "irlaserpos": "laser pos",
    "irlaserend": "laser dir",
    "cartridgepos": "nabojnicestart",
    "cartridgevel": "nabojniceend",
    "selectionfireanim": "zasleh",
    "memorypointcamera": "eye",
    "firespreadangle": 3,
    "usemodeloptics": 1,
    "opticsid": 0,
    "modeloptics": "",
    "opticsppeffects": [],
    "opticsflare": 1,
    "optics": 1,
    "forceoptics": 0,
    "useasbinocular": 0,
    "opticsdisableperipherialvision": 0.67,
    "opticszoommin": 0.25,
    "opticszoommax": 1.25,
    "opticszoominit": 0.75,
    "distancezoommin": 400,
    "distancezoommax": 400,
    "primary": 10,
    "showswitchaction": 0,
    "showempty": 1,
    "autofire": 0,
    "autoreload": 1,
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
    "reloadaction": "",
    "magazines": [],
    "modes": ["this"],
    "useaction": 0,
    "useactiontitle": "",
    "candrop": 1,
    "weaponlockdelay": 0,
    "weaponlocksystem": 0,
    "cmimmunity": 1,
    "weight": 0,
    "minrange": 1,
    "minrangeprobab": 0.3,
    "midrange": 150,
    "midrangeprobab": 0.58,
    "maxrange": 500,
    "maxrangeprobab": 0.04,
    "handanim": [],
    "lockingtargetsound": ["",0.000316228,2],
    "lockedtargetsound": ["",0.000316228,6],
    "detectrange": 0,
    "artillerydispersion": 1,
    "artillerycharge": 1,
    "fireanims": [],
    # Class: CfgWeapons|Default|Library [Indent level: 1],
    "library": {
        "libtextdesc": ""
    },
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
    "texturetype": "default",
    "aimtransitionspeed": 1,
}