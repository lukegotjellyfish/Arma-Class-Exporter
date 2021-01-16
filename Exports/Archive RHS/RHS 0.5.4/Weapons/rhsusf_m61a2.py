rhsusf_m61a2 = {
    "scope": 2,
    "displayname": "M61A2",
    "displaynamemagazine": "M61A2",
    "shortnamemagazine": "20mm",
    # Class: CfgWeapons|rhsusf_M61A2|manual [Indent level: 1],
    "manual": {
        "reloadtime": 0.01,
        "displayname": "M61A2",
        "autofire": 1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "begin1": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_1",2,1,3000],
            "begin2": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_2",2,1,3000],
            "begin3": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_3",2,1,3000],
            "soundbegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34]
        },
        "dispersion": 0.01,
        "soundcontinuous": 0,
        "showtoplayer": 1,
        "burst": 1,
        "airateoffire": 0.02,
        "airateoffiredistance": 1,
        "minrange": 1,
        "minrangeprobab": 0.01,
        "midrange": 2,
        "midrangeprobab": 0.01,
        "maxrange": 3,
        "maxrangeprobab": 0.01,
        "texturetype": "fullAuto",
        "type": 65536,
        # Class: CfgWeapons|CannonCore|GunClouds [Indent level: 1],
        "gunclouds": {
        },
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
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
        "magazinereloadtime": 0,
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
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    "cursoraim": "EmptyCursor",
    "holdsteranimvalue": 1.5,
    "initspeed": 900,
    "canlock": 2,
    "optics": 1,
    "aidispersioncoefx": 1,
    "aidispersioncoefy": 1,
    "magazines": ["rhsusf_20mm_M61A2"],
    "namesound": "cannon",
    "cursor": "EmptyCursor",
    "showaimcursorinternal": 0,
    "ballisticscomputer": "4 + 8",
    "modes": ["manual","close","short","medium","far"],
    # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|GunParticles [Indent level: 1],
    "gunparticles": {
        # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|GunParticles|Effect [Indent level: 2]
        "effect": {
            "effectname": "MachineGun1",
            "positionname": "pos_nosegun",
            "directionname": "pos_nosegun_dir"
        }
    },
    # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|close [Indent level: 1],
    "close": {
        "showtoplayer": 0,
        "burst": 5,
        "burstrangemax": 25,
        "aiburstterminable": 1,
        "airateoffire": 0.25,
        "airateoffiredistance": 400,
        "airateoffiredispersion": 1,
        "minrange": 0,
        "minrangeprobab": 0.95,
        "midrange": 250,
        "midrangeprobab": 0.9,
        "maxrange": 400,
        "maxrangeprobab": 0.2,
        "displayname": "M61 Minigun 20 mm",
        "autofire": 1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "begin1": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_1",2,1,3000],
            "begin2": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_2",2,1,3000],
            "begin3": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_3",2,1,3000],
            "soundbegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34]
        },
        "reloadtime": 0.015,
        "dispersion": 0.01,
        "soundcontinuous": 0,
        "texturetype": "fullAuto",
        "type": 65536,
        # Class: CfgWeapons|CannonCore|GunClouds [Indent level: 1],
        "gunclouds": {
        },
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
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
        "magazinereloadtime": 0,
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
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|short [Indent level: 1],
    "short": {
        "burstrangemax": 15,
        "airateoffire": 0.5,
        "airateoffiredistance": 600,
        "airateoffiredispersion": 2,
        "minrange": 300,
        "minrangeprobab": 0.55,
        "midrange": 400,
        "midrangeprobab": 0.4,
        "maxrange": 600,
        "maxrangeprobab": 0.1,
        "showtoplayer": 0,
        "burst": 5,
        "aiburstterminable": 1,
        "displayname": "M61 Minigun 20 mm",
        "autofire": 1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "begin1": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_1",2,1,3000],
            "begin2": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_2",2,1,3000],
            "begin3": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_3",2,1,3000],
            "soundbegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34]
        },
        "reloadtime": 0.015,
        "dispersion": 0.01,
        "soundcontinuous": 0,
        "texturetype": "fullAuto",
        "type": 65536,
        # Class: CfgWeapons|CannonCore|GunClouds [Indent level: 1],
        "gunclouds": {
        },
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
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
        "magazinereloadtime": 0,
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
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|medium [Indent level: 1],
    "medium": {
        "burstrangemax": 10,
        "airateoffire": 1,
        "airateoffiredistance": 900,
        "airateoffiredispersion": 4,
        "minrange": 500,
        "minrangeprobab": 0.25,
        "midrange": 700,
        "midrangeprobab": 0.2,
        "maxrange": 900,
        "maxrangeprobab": 0.1,
        "showtoplayer": 0,
        "burst": 5,
        "aiburstterminable": 1,
        "displayname": "M61 Minigun 20 mm",
        "autofire": 1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "begin1": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_1",2,1,3000],
            "begin2": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_2",2,1,3000],
            "begin3": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_3",2,1,3000],
            "soundbegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34]
        },
        "reloadtime": 0.015,
        "dispersion": 0.01,
        "soundcontinuous": 0,
        "texturetype": "fullAuto",
        "type": 65536,
        # Class: CfgWeapons|CannonCore|GunClouds [Indent level: 1],
        "gunclouds": {
        },
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
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
        "magazinereloadtime": 0,
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
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|far [Indent level: 1],
    "far": {
        "burstrangemax": 10,
        "airateoffire": 1,
        "airateoffiredistance": 1500,
        "airateoffiredispersion": 6,
        "minrange": 800,
        "minrangeprobab": 0.15,
        "midrange": 1000,
        "midrangeprobab": 0.1,
        "maxrange": 1500,
        "maxrangeprobab": 0.01,
        "showtoplayer": 0,
        "burst": 5,
        "aiburstterminable": 1,
        "displayname": "M61 Minigun 20 mm",
        "autofire": 1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|weapon_Fighter_Gun20mm_AA|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "begin1": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_1",2,1,3000],
            "begin2": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_2",2,1,3000],
            "begin3": ["|A3|Sounds_F_Jets|weapons|cannons|Fighter_Gun20mm_AA_3",2,1,3000],
            "soundbegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34]
        },
        "reloadtime": 0.015,
        "dispersion": 0.01,
        "soundcontinuous": 0,
        "texturetype": "fullAuto",
        "type": 65536,
        # Class: CfgWeapons|CannonCore|GunClouds [Indent level: 1],
        "gunclouds": {
        },
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
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
        "magazinereloadtime": 0,
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
        "inertia": 0.5,
        "aimtransitionspeed": 1
    },
    "type": 65536,
    # Class: CfgWeapons|CannonCore|GunClouds [Indent level: 1],
    "gunclouds": {
    },
    "access": 3,
    "value": 2,
    "picture": "",
    "uipicture": "",
    "ammo": "",
    "cursorsize": 1,
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
    "muzzles": ["this"],
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
    "texturetype": "default",
    "inertia": 0.5,
    "aimtransitionspeed": 1,
}