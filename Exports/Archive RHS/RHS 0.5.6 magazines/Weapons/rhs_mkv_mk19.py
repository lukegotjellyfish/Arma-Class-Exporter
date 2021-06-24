rhs_mkv_mk19 = {
    "displayname": "Stbd MK19",
    # Class: CfgWeapons|RHS_MKV_MK19|GunParticles [Indent level: 1],
    "gunparticles": {
        # Class: CfgWeapons|RHS_MKV_MK19|GunParticles|effect1 [Indent level: 2]
        "effect1": {
            "positionname": "mk19_s_muzzle",
            "directionname": "mk19_s_endBarrel",
            "effectname": "GrenadeLauncherCloud"
        }
    },
    "type": 1,
    "scope": 1,
    "ballisticscomputer": 2,
    "autoreload": 1,
    "canlock": 0,
    "initspeed": 0,
    "maxzeroing": 1500,
    "dispersion": 0.006,
    "aidispersioncoefy": 6,
    "aidispersioncoefx": 5,
    "reloadtime": 0.4,
    "magazinereloadtime": 6,
    # Class: CfgWeapons|RHS_MK19|manual [Indent level: 1],
    "manual": {
        "displayname": "Mk. 19 Grenade Launcher",
        "sounds": ["StandardSound"],
        "soundburst": 0,
        "aiburstterminable": 1,
        "minrange": 1,
        "minrangeprobab": 0.01,
        "midrange": 2,
        "midrangeprobab": 0.01,
        "maxrange": 3,
        "maxrangeprobab": 0.01,
        "reloadtime": 0.15,
        # Class: CfgWeapons|RHS_MK19|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHSUSF_mk19_Shot_SoundSet","RHSUSF_lmg1_Tail_SoundSet"]
        },
        "dispersion": 0.005,
        "magazinereloadtime": 10,
        "autoreload": 1,
        "airateoffire": 4,
        "airateoffiredistance": 500,
        "canlock": 0,
        "ballisticscomputer": "2 + 16",
        "fcsmaxleadspeed": 0,
        "fcszeroingdelay": 1,
        "maxzeroing": 1500,
        "autofire": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "gl",
        "type": 65536,
        "namesound": "mgun",
        "reloadaction": "ManActReloadMagazine",
        "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
        "soundcontinuous": 0,
        "initspeed": 0,
        "flash": "gunfire",
        "flashsize": 0.5,
        "optics": 0,
        "texturetype": "fullAuto",
        "dexterity": 0.5,
        "inertia": 0.7,
        "access": 3,
        "scope": 0,
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
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazinereloadswitchphase": 1,
        "sound": ["",1,1],
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "weaponsoundeffect": "",
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "reloadsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "irdistance": 0,
        "irdotintensity": 0.001,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
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
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
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
    # Class: CfgWeapons|RHS_MK19|close [Indent level: 1],
    "close": {
        "burst": 5,
        "burstrangemax": 8,
        "airateoffire": 1,
        "airateoffiredistance": 50,
        "minrange": 8,
        "minrangeprobab": 0.05,
        "midrange": 20,
        "midrangeprobab": 0.7,
        "maxrange": 50,
        "maxrangeprobab": 0.1,
        "showtoplayer": 0,
        "displayname": "Mk. 19 Grenade Launcher",
        "sounds": ["StandardSound"],
        "soundburst": 0,
        "aiburstterminable": 1,
        "reloadtime": 0.15,
        # Class: CfgWeapons|RHS_MK19|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHSUSF_mk19_Shot_SoundSet","RHSUSF_lmg1_Tail_SoundSet"]
        },
        "dispersion": 0.005,
        "magazinereloadtime": 10,
        "autoreload": 1,
        "canlock": 0,
        "ballisticscomputer": "2 + 16",
        "fcsmaxleadspeed": 0,
        "fcszeroingdelay": 1,
        "maxzeroing": 1500,
        "autofire": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "gl",
        "type": 65536,
        "namesound": "mgun",
        "reloadaction": "ManActReloadMagazine",
        "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
        "soundcontinuous": 0,
        "initspeed": 0,
        "flash": "gunfire",
        "flashsize": 0.5,
        "optics": 0,
        "texturetype": "fullAuto",
        "dexterity": 0.5,
        "inertia": 0.7,
        "access": 3,
        "scope": 0,
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
        "count": 0,
        "multiplier": 1,
        "magazinereloadswitchphase": 1,
        "sound": ["",1,1],
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "weaponsoundeffect": "",
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "reloadsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "irdistance": 0,
        "irdotintensity": 0.001,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
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
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
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
    # Class: CfgWeapons|RHS_MK19|short [Indent level: 1],
    "short": {
        "burst": 4,
        "burstrangemax": 8,
        "airateoffire": 2,
        "airateoffiredistance": 300,
        "minrange": 50,
        "minrangeprobab": 0.05,
        "midrange": 150,
        "midrangeprobab": 0.7,
        "maxrange": 300,
        "maxrangeprobab": 0.1,
        "showtoplayer": 0,
        "displayname": "Mk. 19 Grenade Launcher",
        "sounds": ["StandardSound"],
        "soundburst": 0,
        "aiburstterminable": 1,
        "reloadtime": 0.15,
        # Class: CfgWeapons|RHS_MK19|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHSUSF_mk19_Shot_SoundSet","RHSUSF_lmg1_Tail_SoundSet"]
        },
        "dispersion": 0.005,
        "magazinereloadtime": 10,
        "autoreload": 1,
        "canlock": 0,
        "ballisticscomputer": "2 + 16",
        "fcsmaxleadspeed": 0,
        "fcszeroingdelay": 1,
        "maxzeroing": 1500,
        "autofire": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "gl",
        "type": 65536,
        "namesound": "mgun",
        "reloadaction": "ManActReloadMagazine",
        "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
        "soundcontinuous": 0,
        "initspeed": 0,
        "flash": "gunfire",
        "flashsize": 0.5,
        "optics": 0,
        "texturetype": "fullAuto",
        "dexterity": 0.5,
        "inertia": 0.7,
        "access": 3,
        "scope": 0,
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
        "count": 0,
        "multiplier": 1,
        "magazinereloadswitchphase": 1,
        "sound": ["",1,1],
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "weaponsoundeffect": "",
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "reloadsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "irdistance": 0,
        "irdotintensity": 0.001,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
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
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
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
    # Class: CfgWeapons|RHS_MK19|medium [Indent level: 1],
    "medium": {
        "burst": 2,
        "burstrangemax": 6,
        "airateoffire": 4,
        "airateoffiredistance": 600,
        "minrange": 200,
        "minrangeprobab": 0.05,
        "midrange": 400,
        "midrangeprobab": 0.7,
        "maxrange": 600,
        "maxrangeprobab": 0.1,
        "showtoplayer": 0,
        "displayname": "Mk. 19 Grenade Launcher",
        "sounds": ["StandardSound"],
        "soundburst": 0,
        "aiburstterminable": 1,
        "reloadtime": 0.15,
        # Class: CfgWeapons|RHS_MK19|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHSUSF_mk19_Shot_SoundSet","RHSUSF_lmg1_Tail_SoundSet"]
        },
        "dispersion": 0.005,
        "magazinereloadtime": 10,
        "autoreload": 1,
        "canlock": 0,
        "ballisticscomputer": "2 + 16",
        "fcsmaxleadspeed": 0,
        "fcszeroingdelay": 1,
        "maxzeroing": 1500,
        "autofire": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "gl",
        "type": 65536,
        "namesound": "mgun",
        "reloadaction": "ManActReloadMagazine",
        "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
        "soundcontinuous": 0,
        "initspeed": 0,
        "flash": "gunfire",
        "flashsize": 0.5,
        "optics": 0,
        "texturetype": "fullAuto",
        "dexterity": 0.5,
        "inertia": 0.7,
        "access": 3,
        "scope": 0,
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
        "count": 0,
        "multiplier": 1,
        "magazinereloadswitchphase": 1,
        "sound": ["",1,1],
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "weaponsoundeffect": "",
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "reloadsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "irdistance": 0,
        "irdotintensity": 0.001,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
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
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
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
    # Class: CfgWeapons|RHS_MK19|far [Indent level: 1],
    "far": {
        "burst": 2,
        "burstrangemax": 6,
        "airateoffire": 5,
        "airateoffiredistance": 1000,
        "minrange": 400,
        "minrangeprobab": 0.05,
        "midrange": 750,
        "midrangeprobab": 0.4,
        "maxrange": 1000,
        "maxrangeprobab": 0.01,
        "showtoplayer": 0,
        "displayname": "Mk. 19 Grenade Launcher",
        "sounds": ["StandardSound"],
        "soundburst": 0,
        "aiburstterminable": 1,
        "reloadtime": 0.15,
        # Class: CfgWeapons|RHS_MK19|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHSUSF_mk19_Shot_SoundSet","RHSUSF_lmg1_Tail_SoundSet"]
        },
        "dispersion": 0.005,
        "magazinereloadtime": 10,
        "autoreload": 1,
        "canlock": 0,
        "ballisticscomputer": "2 + 16",
        "fcsmaxleadspeed": 0,
        "fcszeroingdelay": 1,
        "maxzeroing": 1500,
        "autofire": 1,
        "cursor": "EmptyCursor",
        "cursoraim": "gl",
        "type": 65536,
        "namesound": "mgun",
        "reloadaction": "ManActReloadMagazine",
        "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
        "soundcontinuous": 0,
        "initspeed": 0,
        "flash": "gunfire",
        "flashsize": 0.5,
        "optics": 0,
        "texturetype": "fullAuto",
        "dexterity": 0.5,
        "inertia": 0.7,
        "access": 3,
        "scope": 0,
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
        "count": 0,
        "multiplier": 1,
        "magazinereloadswitchphase": 1,
        "sound": ["",1,1],
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "weaponsoundeffect": "",
        "drysound": ["",1,1],
        "zeroingsound": ["",1,1],
        "reloadsound": ["",1,1],
        "changefiremodesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "irdistance": 0,
        "irdotintensity": 0.001,
        "aidispersioncoefx": 1,
        "aidispersioncoefy": 1,
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
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useaction": 0,
        "useactiontitle": "",
        "candrop": 1,
        "weaponlockdelay": 0,
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
    # Compatible Magazines: magazines parameter (+ inherited),
    "magazines": [
        "rhs_48rnd_40mm_mk19","rhs_48rnd_40mm_mk19_m430i","rhs_48rnd_40mm_mk19_m430a1","rhs_48rnd_40mm_mk19_m1001",
        "rhs_96rnd_40mm_mk19","rhs_96rnd_40mm_mk19_m430i","rhs_96rnd_40mm_mk19_m430a1","rhs_96rnd_40mm_mk19_m1001",
    ],
    "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_GMG|GMG20mm_static_reload",1,1,10],
    # Class: CfgWeapons|GMG_20mm|GunClouds [Indent level: 1],
    "gunclouds": {
    },
    "modes": ["manual","close","short","medium","far"],
    "drysound": ["A3|Sounds_F|arsenal|weapons_static|Static_GMG|GMG20mm_static_dry",1,1,10],
    "airateoffire": 4,
    "airateoffiredistance": 500,
    "minrange": 8,
    "minrangeprobab": 0.6,
    "midrange": 500,
    "midrangeprobab": 0.7,
    "maxrange": 1500,
    "maxrangeprobab": 0.1,
    "fcsmaxleadspeed": 0,
    "fcszeroingdelay": 1,
    "autofire": 1,
    "cursor": "EmptyCursor",
    "cursoraim": "gl",
    "namesound": "mgun",
    "reloadaction": "ManActReloadMagazine",
    "sounds": ["StandardSound"],
    # Class: CfgWeapons|MGun|StandardSound [Indent level: 1],
    "standardsound": {
        "begin1": ["A3|Sounds_F|arsenal|weapons_vehicles|HMG_050|HMG_050_01",1.58489,1,2100],
        "begin2": ["A3|Sounds_F|arsenal|weapons_vehicles|HMG_050|HMG_050_02",1.58489,1,2100],
        "begin3": ["A3|Sounds_F|arsenal|weapons_vehicles|HMG_050|HMG_050_03",1.58489,1,2100],
        "soundbegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34],
        "soundsetshot": ["HMG050_Shot_SoundSet","HMG050_Tail_SoundSet"]
    },
    "soundcontinuous": 0,
    "flash": "gunfire",
    "flashsize": 0.5,
    "optics": 0,
    "texturetype": "fullAuto",
    "dexterity": 0.5,
    "inertia": 0.7,
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
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazinereloadswitchphase": 1,
    "sound": ["",1,1],
    "soundbegin": ["sound",1],
    "soundbeginwater": ["sound",1],
    "soundclosure": ["sound",1],
    "soundend": ["sound",1],
    "soundloop": ["sound",1],
    "weaponsoundeffect": "",
    "soundburst": 1,
    "zeroingsound": ["",1,1],
    "reloadsound": ["",1,1],
    "changefiremodesound": ["",1,1],
    "emptysound": ["",1,1],
    "soundbullet": ["emptySound",1],
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
    "muzzles": ["this"],
    "useaction": 0,
    "useactiontitle": "",
    "candrop": 1,
    "weaponlockdelay": 0,
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