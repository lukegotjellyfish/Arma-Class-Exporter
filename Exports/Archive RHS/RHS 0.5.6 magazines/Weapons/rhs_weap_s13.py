rhs_weap_s13 = {
    "displayname": "S13",
    # Compatible Magazines: magazines parameter (+ inherited),
    "magazines": [
        "rhs_mag_s13b_10","rhs_mag_b13l_s13b","rhs_mag_b13l1_s13b","rhs_mag_b13l1_ka52_s13b",
        "rhs_mag_b13l_bd3_umk2a_s13b",],
    # Class: CfgWeapons|rhs_weap_s13|AI_Burst [Indent level: 1],
    "ai_burst": {
        "reloadtime": 0.15,
        "dispersion": 0.02,
        "displayname": "S13",
        "showtoplayer": 0,
        "maxrange": 1500,
        "maxrangeprobab": 0.05,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "rocket",
        "type": 65536,
        "magazinereloadtime": 0.2,
        "minrange": 50,
        "minrangeprobab": 0.1,
        "midrange": 600,
        "midrangeprobab": 0.25,
        "canlock": 2,
        "weaponlockdelay": 3,
        "namesound": "rockets",
        "texturetype": "semi",
        "aidispersioncoefy": 0.5,
        "aidispersioncoefx": 0.5,
        "dexterity": 0.5,
        "airateoffire": 0.5,
        "airateoffiredistance": 300,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
        "picture": "",
        "uipicture": "",
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
        "lockacquire": 1,
        "enableattack": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
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
        "canshootinwater": 0,
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
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
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
        "descriptionshort": "",
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
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|rhs_weap_s13|Burst [Indent level: 1],
    "burst": {
        "reloadtime": 0.15,
        "dispersion": 0.02,
        "displayname": "S13",
        "showtoplayer": 1,
        "airateoffire": 0.5,
        "airateoffiredistance": 300,
        "burst": 1,
        "salvo": 2,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 0,
        "midrangeprobab": 0.25,
        "maxrange": 0,
        "maxrangeprobab": 0.05,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_s5|Burst|StandardSound [Indent level: 2],
        "standardsound": {
            "weaponsoundeffect": "DefaultRifle",
            "begin1": ["rhsafrf|addons|rhs_sounds|atgm|atgm_1",2.35,1,1400],
            "begin2": ["rhsafrf|addons|rhs_sounds|atgm|atgm_2",2.35,1,1400],
            "soundbegin": ["begin1",0.5,"begin2",0.5],
            "soundsetshot": ["RocketsMedium_Shot_SoundSet"]
        },
        "texturetype": "fullAuto",
        "autofire": 1,
        "soundcontinuous": 0,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "rocket",
        "type": 65536,
        "magazinereloadtime": 0.2,
        "canlock": 2,
        "weaponlockdelay": 3,
        "namesound": "rockets",
        "aidispersioncoefy": 0.5,
        "aidispersioncoefx": 0.5,
        "dexterity": 0.5,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
        "picture": "",
        "uipicture": "",
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
        "magazinereloadswitchphase": 1,
        "sound": ["",1,1],
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
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
        "lockacquire": 1,
        "enableattack": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
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
        "autoreload": 1,
        "canshootinwater": 0,
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
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
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
        "descriptionshort": "",
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
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|rhs_weap_s8|Far_AI [Indent level: 1],
    "far_ai": {
        "displayname": "S8",
        "airateoffire": 5,
        "airateoffiredistance": 1000,
        "minrange": 500,
        "minrangeprobab": 0.05,
        "midrange": 600,
        "midrangeprobab": 0.4,
        "maxrange": 800,
        "maxrangeprobab": 0.01,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_s5|Far_AI|StandardSound [Indent level: 2],
        "standardsound": {
            "weaponsoundeffect": "DefaultRifle",
            "begin1": ["rhsafrf|addons|rhs_sounds|atgm|atgm_1",2.35,1,1400],
            "begin2": ["rhsafrf|addons|rhs_sounds|atgm|atgm_2",2.35,1,1400],
            "soundbegin": ["begin1",0.5,"begin2",0.5],
            "soundsetshot": ["RocketsMedium_Shot_SoundSet"]
        },
        "autofire": 0,
        "reloadtime": 0.08,
        "dispersion": 0.025,
        "aiburstterminable": 1,
        "showtoplayer": 0,
        "burst": 1,
        "burstrangemax": 4,
        "airateoffiredispersion": 4,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "rocket",
        "type": 65536,
        "magazinereloadtime": 0.2,
        "canlock": 2,
        "weaponlockdelay": 3,
        "namesound": "rockets",
        "texturetype": "semi",
        "aidispersioncoefy": 0.5,
        "aidispersioncoefx": 0.5,
        "dexterity": 0.5,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
        "picture": "",
        "uipicture": "",
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
        "lockacquire": 1,
        "enableattack": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
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
        "autoreload": 1,
        "canshootinwater": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
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
        "descriptionshort": "",
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
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|rhs_weap_s8|Medium_AI [Indent level: 1],
    "medium_ai": {
        "displayname": "S8",
        "airateoffire": 3,
        "airateoffiredistance": 600,
        "minrange": 300,
        "minrangeprobab": 0.05,
        "midrange": 400,
        "midrangeprobab": 0.7,
        "maxrange": 600,
        "maxrangeprobab": 0.1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_s5|Medium_AI|StandardSound [Indent level: 2],
        "standardsound": {
            "weaponsoundeffect": "DefaultRifle",
            "begin1": ["rhsafrf|addons|rhs_sounds|atgm|atgm_1",2.35,1,1400],
            "begin2": ["rhsafrf|addons|rhs_sounds|atgm|atgm_2",2.35,1,1400],
            "soundbegin": ["begin1",0.5,"begin2",0.5],
            "soundsetshot": ["RocketsMedium_Shot_SoundSet"]
        },
        "aiburstterminable": 1,
        "showtoplayer": 0,
        "burst": 1,
        "burstrangemax": 6,
        "airateoffiredispersion": 3,
        "autofire": 0,
        "reloadtime": 0.08,
        "dispersion": 0.025,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "rocket",
        "type": 65536,
        "magazinereloadtime": 0.2,
        "canlock": 2,
        "weaponlockdelay": 3,
        "namesound": "rockets",
        "texturetype": "semi",
        "aidispersioncoefy": 0.5,
        "aidispersioncoefx": 0.5,
        "dexterity": 0.5,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
        "picture": "",
        "uipicture": "",
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
        "lockacquire": 1,
        "enableattack": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
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
        "autoreload": 1,
        "canshootinwater": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
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
        "descriptionshort": "",
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
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|rhs_weap_s8|Close_AI [Indent level: 1],
    "close_ai": {
        "displayname": "S8",
        "airateoffire": 0.5,
        "airateoffiredistance": 50,
        "minrange": 0,
        "minrangeprobab": 0.05,
        "midrange": 300,
        "midrangeprobab": 0.7,
        "maxrange": 400,
        "maxrangeprobab": 0.1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_s5|Close_AI|StandardSound [Indent level: 2],
        "standardsound": {
            "weaponsoundeffect": "DefaultRifle",
            "begin1": ["rhsafrf|addons|rhs_sounds|atgm|atgm_1",2.35,1,1400],
            "begin2": ["rhsafrf|addons|rhs_sounds|atgm|atgm_2",2.35,1,1400],
            "soundbegin": ["begin1",0.5,"begin2",0.5],
            "soundsetshot": ["RocketsMedium_Shot_SoundSet"]
        },
        "aiburstterminable": 1,
        "showtoplayer": 0,
        "burst": 1,
        "burstrangemax": 42,
        "airateoffiredispersion": 1,
        "autofire": 0,
        "reloadtime": 0.08,
        "dispersion": 0.025,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "rocket",
        "type": 65536,
        "magazinereloadtime": 0.2,
        "canlock": 2,
        "weaponlockdelay": 3,
        "namesound": "rockets",
        "texturetype": "semi",
        "aidispersioncoefy": 0.5,
        "aidispersioncoefx": 0.5,
        "dexterity": 0.5,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
        "picture": "",
        "uipicture": "",
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
        "lockacquire": 1,
        "enableattack": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
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
        "autoreload": 1,
        "canshootinwater": 0,
        "firelightduration": 0.05,
        "firelightintensity": 0.2,
        "firelightdiffuse": [0.937,0.631,0.259],
        "firelightambient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "eventhandlers": {
        },
        "backgroundreload": 0,
        "reloadaction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
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
        "descriptionshort": "",
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
        "aimtransitionspeed": 1
    },
    "aidispersioncoefy": 1,
    "aidispersioncoefx": 1.5,
    "cursor": "missile",
    "cursoraim": "EmptyCursor",
    "cursorsize": 0,
    "proxyshape": "rhsafrf|addons|rhs_a2port_air|data|proxy|ub16",
    # Class: CfgWeapons|rhs_weap_s5|gunClouds [Indent level: 1],
    "gunclouds": {
    },
    "firelightambient": [0,0,0],
    "firelightdiffuse": [0.93,0.63,0.25],
    "firelightduration": 0.051,
    "firelightintensity": 0.2,
    "canlock": 1,
    "weaponlockdelay": 8,
    "showtoplayer": 1,
    "modes": ["AI_Burst","Burst"],
    # Class: CfgWeapons|rhs_weap_s5|Burst_AI [Indent level: 1],
    "burst_ai": {
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_s5|Burst_AI|StandardSound [Indent level: 2],
        "standardsound": {
            "weaponsoundeffect": "DefaultRifle",
            "begin1": ["rhsafrf|addons|rhs_sounds|atgm|atgm_1",2.35,1,1400],
            "begin2": ["rhsafrf|addons|rhs_sounds|atgm|atgm_2",2.35,1,1400],
            "soundbegin": ["begin1",0.5,"begin2",0.5],
            "soundsetshot": ["RocketsMedium_Shot_SoundSet"]
        },
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "rocket",
        "type": 65536,
        "reloadtime": 0.2,
        "magazinereloadtime": 0.2,
        "minrange": 50,
        "minrangeprobab": 0.1,
        "midrange": 600,
        "midrangeprobab": 0.25,
        "maxrange": 2500,
        "maxrangeprobab": 0.05,
        "canlock": 2,
        "weaponlockdelay": 3,
        "namesound": "rockets",
        "texturetype": "semi",
        "aidispersioncoefy": 0.5,
        "aidispersioncoefx": 0.5,
        "dexterity": 0.5,
        "airateoffire": 0.5,
        "airateoffiredistance": 300,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
        "picture": "",
        "uipicture": "",
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
        "displayname": "",
        "multiplier": 1,
        "burst": 1,
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
        "lockacquire": 1,
        "enableattack": 1,
        "ffmagnitude": 0,
        "fffrequency": 1,
        "ffcount": 1,
        # Recoil Array: recoil,
        "recoil": [],
        "recoil": "empty",
        "recoilprone": "",
        "maxrecoilsway": 0.008,
        "swaydecayspeed": 2,
        "model": "",
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
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlocksystem": 0,
        "cmimmunity": 1,
        "weight": 0,
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
        "descriptionshort": "",
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
        "aimtransitionspeed": 1
    },
    "ballisticscomputer": 8,
    "scope": 1,
    "type": 65536,
    "reloadtime": 0.2,
    "magazinereloadtime": 0.2,
    "minrange": 50,
    "minrangeprobab": 0.1,
    "midrange": 600,
    "midrangeprobab": 0.25,
    "maxrange": 2500,
    "maxrangeprobab": 0.05,
    "namesound": "rockets",
    "texturetype": "semi",
    "dexterity": 0.5,
    "airateoffire": 0.5,
    "airateoffiredistance": 300,
    "count": 1,
    "inertia": 1,
    "access": 3,
    "value": 2,
    "picture": "",
    "uipicture": "",
    "ammo": "",
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
    "irdistance": 0,
    "irdotintensity": 0.001,
    "dispersion": 0.002,
    "lockacquire": 1,
    "enableattack": 1,
    "ffmagnitude": 0,
    "fffrequency": 1,
    "ffcount": 1,
    # Recoil Array: recoil,
    "recoil": [],
    "recoil": "empty",
    "recoilprone": "",
    "maxrecoilsway": 0.008,
    "swaydecayspeed": 2,
    "model": "",
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
    "canshootinwater": 0,
    "airateoffiredispersion": 0,
    # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
    "eventhandlers": {
    },
    "backgroundreload": 0,
    "reloadaction": "",
    "muzzles": ["this"],
    "useaction": 0,
    "useactiontitle": "",
    "candrop": 1,
    "weaponlocksystem": 0,
    "cmimmunity": 1,
    "weight": 0,
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
    "descriptionshort": "",
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
    "aimtransitionspeed": 1,
}