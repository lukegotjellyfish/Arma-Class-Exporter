rhs_weap_m80 = {
    "picture": "rhssaf|addons|rhssaf_inventoryicons|data|weapons|rhs_weap_m80_ca.paa",
    "scope": 2,
    "dlc": "RHS_SAF",
    "author": "Red Hammer Studios",
    "displayname": "RBR-M80",
    "descriptionshort": "Rocket launcher<br/>Caliber: 64mm<br/>Type: Single-shot Anti-Tank",
    "model": "rhssaf|addons|rhssaf_m_weapon_m80|rhssaf_m80",
    # Class: CfgWeapons|rhs_weap_m80|GunParticles [Indent level: 1],
    "gunparticles": {
        # Class: CfgWeapons|rhs_weap_m80|GunParticles|effect1 [Indent level: 2]
        "effect1": {
            "positionname": "konec hlavne",
            "directionname": "usti hlavne",
            "effectname": "RocketBackEffectsRPGNT"
        }
    },
    "sounds": ["StandardSound"],
    # Class: CfgWeapons|rhs_weap_m80|StandardSound [Indent level: 1],
    "standardsound": {
        "weaponsoundeffect": "DefaultRifle",
        "begin1": ["A3|Sounds_F|weapons|Launcher|rpg32",1.99526,1,900],
        "soundbegin": ["begin1",1]
    },
    "drysound": ["A3|sounds_f|weapons|other|dry6",0.0316228,1,10],
    "reloadmagazinesound": ["rhsusf|addons|rhsusf_weapons2|m136|sound|at4prep.ogg",0.562341,1,50],
    "soundfly": ["A3|sounds_f|weapons|rockets|rocket_fly_1",0.316228,1.5,700],
    "magazines": ["rhs_m80_mag"],
    "reloadaction": "ReloadRPG",
    "handanim": ["OFP2_ManSkeleton","|rhssaf|addons|rhssaf_c_weapons|anims|rhssaf_hand_m80.rtm"],
    # Recoil Array: recoil,
    "recoil": [0,0,0,0.03,0.0073886,0.0028696,0.04,0.0063634,0.0010008,0.05,0.003951,0.0006112,0.06,0.0014776,0.000228,0.06,0,0,0.06,-0.0004804,-7.68e-005,0.06,-0.000706,-0.0001128,0.06,-0.0007354,-0.0001176,0.06,-0.0006276,-0.0001,0.06,-0.0004412,-7.04e-005,0.06,-0.0002354,-3.76e-005,0.06,-6.86e-005,-1.12e-005,0.06,-3e-005,0,0.06,0,0],
    "recoil": "recoil_single_law",
    "rhs_disposable": 1,
    "reloadtime": 1,
    "magazinereloadtime": 1,
    "aimtransitionspeed": 0.5,
    "showtoplayer": 1,
    "minrange": 10,
    "minrangeprobab": 0.9,
    "midrange": 200,
    "midrangeprobab": 0.7,
    "maxrange": 350,
    "maxrangeprobab": 0.1,
    "airateoffire": 7,
    "airateoffiredistance": 300,
    "weaponinfotype": "rhs_rscOptics_disposable",
    "modeloptics": "-",
    "optics": 1,
    # Class: CfgWeapons|rhs_weap_m80|OpticsModes [Indent level: 1],
    "opticsmodes": {
        # Class: CfgWeapons|rhs_weap_m80|OpticsModes|ironsight [Indent level: 2]
        "ironsight": {
            "opticsid": 2,
            "opticsppeffects": ["OpticsCHAbera1","OpticsBlur1"],
            "usemodeloptics": 0,
            "opticsflare": 0,
            "opticsdisableperipherialvision": 0,
            "opticszoommin": 0.25,
            "opticszoommax": 1.2,
            "opticszoominit": 0.7,
            "visionmode": "",
            "discretedistanceinitindex": 0,
            "discretedistance": [150,200,250,300,350,400],
            "discretedistancecamerapoint": ["op_eye_150","op_eye_200","op_eye_250","op_eye_300","op_eye_350","op_eye_400"],
            "memorypointcamera": "op_look1",
            "cameradir": "op_look",
            "distancezoommin": 150,
            "distancezoommax": 400
        }
    },
    # Class: CfgWeapons|rhs_weap_m80|WeaponSlotsInfo [Indent level: 1],
    "weaponslotsinfo": {
        "allowedslots": [],
        "mass": 66,
        # Class: CfgWeapons|rhs_weap_m80|WeaponSlotsInfo|PointerSlot [Indent level: 2],
        "pointerslot": {
            "iconposition": [0,0],
            "iconscale": 1,
            "iconpicture": "A3|Weapons_F|Data|clear_empty.paa",
            "iconpinpoint": "Left"
        }
    },
    # Class: CfgWeapons|rhs_weap_m80|Library [Indent level: 1],
    "library": {
        "libtextdesc": "M80 is a portable one-shot 64 mm unguided anti-tank weapon"
    },
    # Class: CfgWeapons|rhs_weap_m80|ItemInfo [Indent level: 1],
    "iteminfo": {
        "priority": 3,
        "rmbhint": "M80",
        "onhovertext": "M80"
    },
    # Class: CfgWeapons|rhs_weap_m80|Eventhandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgWeapons|rhs_weap_m80|Eventhandlers|RHS_DisposableWeapon [Indent level: 2]
        "rhs_disposableweapon": {
            "fired": "_this call rhs_fnc_disposable;"
        }
    },
    "htmin": 1,
    "htmax": 460,
    "afmax": 0,
    "mfmax": 0,
    "mfact": 1,
    "tbody": 100,
    "uipicture": "A3|Weapons_F|Data|UI|icon_at_CA.paa",
    "dexterity": 1.7,
    "swaycoef": 0.5,
    "sound": ["A3|Sounds_F|weapons|Launcher|rocket_launcher_5",1,1,800],
    "weaponpoolavailable": 1,
    "shotpos": "usti hlavne",
    "shotend": "konec hlavne",
    "cursoraim": "EmptyCursor",
    "cursor": "rocket",
    "texturetype": "semi",
    "autoaimenabled": 0,
    "opticsdisableperipherialvision": 1,
    "value": 10,
    "namesound": "atlauncher",
    "initspeed": 30,
    "canlock": 0,
    "autoreload": 0,
    "ffmagnitude": 0.1,
    "fffrequency": 1,
    "ffcount": 1,
    "primary": 0,
    "opticszoommin": 0.375,
    "opticszoommax": 1.1,
    "opticszoominit": 0.75,
    "distancezoommin": 100,
    "distancezoommax": 100,
    "maxzeroing": 1000,
    "type": 4,
    "count": 1,
    "inertia": 1,
    "access": 3,
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
    "multiplier": 1,
    "burst": 1,
    "magazinereloadswitchphase": 1,
    "soundbegin": ["sound",1],
    "soundbeginwater": ["sound",1],
    "soundclosure": ["sound",1],
    "soundend": ["sound",1],
    "soundloop": ["sound",1],
    "soundcontinuous": 0,
    "weaponsoundeffect": "",
    "soundburst": 1,
    "zeroingsound": ["",1,1],
    "reloadsound": ["",1,1],
    "changefiremodesound": ["",1,1],
    "emptysound": ["",1,1],
    "soundbullet": ["emptySound",1],
    "ballisticscomputer": 0,
    "irdistance": 0,
    "irdotintensity": 0.001,
    "dispersion": 0.002,
    "aidispersioncoefx": 1,
    "aidispersioncoefy": 1,
    "lockacquire": 1,
    "enableattack": 1,
    "recoilprone": "",
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
    "opticsppeffects": [],
    "opticsflare": 1,
    "forceoptics": 0,
    "useasbinocular": 0,
    "showswitchaction": 0,
    "showempty": 1,
    "autofire": 0,
    "canshootinwater": 0,
    "airateoffiredispersion": 0,
    "firelightduration": 0.05,
    "firelightintensity": 0.2,
    "firelightdiffuse": [0.937,0.631,0.259],
    "firelightambient": [0,0,0],
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
}