rhs_weap_pkm_tigr = {
    "ballisticscomputer": 2,
    "magazinereloadtime": 5,
    "displayname": "PKM",
    # Class: CfgWeapons|rhs_weap_pkm_tigr|GunParticles [Indent level: 1],
    "gunparticles": {
        # Class: CfgWeapons|rhs_weap_pkm_tigr|GunParticles|effect1 [Indent level: 2]
        "effect1": {
            "positionname": "weapon_pkm_end",
            "directionname": "weapon_pkm_start",
            "effectname": "MachineGunCloud"
        },
        # Class: CfgWeapons|rhs_weap_pkm_tigr|GunParticles|effect2 [Indent level: 2],
        "effect2": {
            "positionname": "weapon_pkm_eject_pos",
            "directionname": "weapon_pkm_eject_dir",
            "effectname": "MachineGunCartridge2"
        },
        # Class: CfgWeapons|rhs_weap_pkm_tigr|GunParticles|SecondEffect [Indent level: 2],
        "secondeffect": {
            "positionname": "weapon_pkm_eject_pos",
            "directionname": "weapon_pkm_eject_dir",
            "effectname": "RifleAssaultCloud"
        },
        # Class: CfgWeapons|rhs_weap_pkm_tigr|GunParticles|RHS_BarrelRefract [Indent level: 2],
        "rhs_barrelrefract": {
            "positionname": "weapon_pkm_end",
            "directionname": "weapon_pkm_end_up",
            "effectname": "RHS_BarrelRefract"
        }
    },
    "aidispersioncoefy": 14,
    "aidispersioncoefx": 8,
    "modes": ["manual","close","short","medium","far"],
    # Class: CfgWeapons|rhs_weap_pkm_tigr|manual [Indent level: 1],
    "manual": {
        "displayname": "PKM",
        "autofire": 1,
        "reloadtime": 0.075,
        "dispersion": 0.00125,
        "showtoplayer": 1,
        "soundcontinuous": 0,
        "burst": 1,
        "aiburstterminable": 1,
        "airateoffire": 0.5,
        "airateoffiredistance": 50,
        "minrange": 1,
        "minrangeprobab": 0.01,
        "midrange": 2,
        "midrangeprobab": 0.01,
        "maxrange": 3,
        "maxrangeprobab": 0.01,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_pkt|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHS_veh_PK_Shot_SoundSet","RHS_veh_PK_int_Shot_SoundSet","RHS_VEH_MMG1_Tail_SoundSet"]
        },
        "type": 65536,
        "cursor": "EmptyCursor",
        "cursoraim": "mg",
        "namesound": "mgun",
        "reloadaction": "ManActReloadMagazine",
        "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
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
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
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
    # Class: CfgWeapons|rhs_weap_pkm_tigr|close [Indent level: 1],
    "close": {
        "showtoplayer": 0,
        "soundburst": 0,
        "burst": 12,
        "burstrangemax": 16,
        "airateoffire": 1,
        "airateoffiredistance": 50,
        "airateoffiredispersion": 4,
        "minrange": 0,
        "minrangeprobab": 0.05,
        "midrange": 20,
        "midrangeprobab": 0.7,
        "maxrange": 50,
        "maxrangeprobab": 0.04,
        "displayname": "PKM",
        "autofire": 1,
        "reloadtime": 0.075,
        "dispersion": 0.00125,
        "soundcontinuous": 0,
        "aiburstterminable": 1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_pkt|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHS_veh_PK_Shot_SoundSet","RHS_veh_PK_int_Shot_SoundSet","RHS_VEH_MMG1_Tail_SoundSet"]
        },
        "type": 65536,
        "cursor": "EmptyCursor",
        "cursoraim": "mg",
        "namesound": "mgun",
        "reloadaction": "ManActReloadMagazine",
        "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
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
        "magazinereloadtime": 0,
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
    # Class: CfgWeapons|rhs_weap_pkm_tigr|short [Indent level: 1],
    "short": {
        "burst": 10,
        "burstrangemax": 14,
        "airateoffire": 2,
        "airateoffiredistance": 300,
        "airateoffiredispersion": 4,
        "minrange": 50,
        "minrangeprobab": 0.05,
        "midrange": 200,
        "midrangeprobab": 0.7,
        "maxrange": 300,
        "maxrangeprobab": 0.1,
        "showtoplayer": 0,
        "soundburst": 0,
        "displayname": "PKM",
        "autofire": 1,
        "reloadtime": 0.075,
        "dispersion": 0.00125,
        "soundcontinuous": 0,
        "aiburstterminable": 1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_pkt|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHS_veh_PK_Shot_SoundSet","RHS_veh_PK_int_Shot_SoundSet","RHS_VEH_MMG1_Tail_SoundSet"]
        },
        "type": 65536,
        "cursor": "EmptyCursor",
        "cursoraim": "mg",
        "namesound": "mgun",
        "reloadaction": "ManActReloadMagazine",
        "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
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
        "magazinereloadtime": 0,
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
    # Class: CfgWeapons|rhs_weap_pkm_tigr|medium [Indent level: 1],
    "medium": {
        "burst": 7,
        "burstrangemax": 11,
        "airateoffire": 4,
        "airateoffiredistance": 600,
        "airateoffiredispersion": 3,
        "minrange": 200,
        "minrangeprobab": 0.05,
        "midrange": 500,
        "midrangeprobab": 0.7,
        "maxrange": 600,
        "maxrangeprobab": 0.1,
        "showtoplayer": 0,
        "soundburst": 0,
        "displayname": "PKM",
        "autofire": 1,
        "reloadtime": 0.075,
        "dispersion": 0.00125,
        "soundcontinuous": 0,
        "aiburstterminable": 1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_pkt|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHS_veh_PK_Shot_SoundSet","RHS_veh_PK_int_Shot_SoundSet","RHS_VEH_MMG1_Tail_SoundSet"]
        },
        "type": 65536,
        "cursor": "EmptyCursor",
        "cursoraim": "mg",
        "namesound": "mgun",
        "reloadaction": "ManActReloadMagazine",
        "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
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
        "magazinereloadtime": 0,
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
    # Class: CfgWeapons|rhs_weap_pkm_tigr|far [Indent level: 1],
    "far": {
        "burst": 6,
        "burstrangemax": 10,
        "airateoffire": 5,
        "airateoffiredistance": 1000,
        "airateoffiredispersion": 3,
        "minrange": 400,
        "minrangeprobab": 0.05,
        "midrange": 850,
        "midrangeprobab": 0.4,
        "maxrange": 1100,
        "maxrangeprobab": 0.01,
        "showtoplayer": 0,
        "soundburst": 0,
        "displayname": "PKM",
        "autofire": 1,
        "reloadtime": 0.075,
        "dispersion": 0.00125,
        "soundcontinuous": 0,
        "aiburstterminable": 1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_pkt|manual|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHS_veh_PK_Shot_SoundSet","RHS_veh_PK_int_Shot_SoundSet","RHS_VEH_MMG1_Tail_SoundSet"]
        },
        "type": 65536,
        "cursor": "EmptyCursor",
        "cursoraim": "mg",
        "namesound": "mgun",
        "reloadaction": "ManActReloadMagazine",
        "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
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
        "magazinereloadtime": 0,
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
    "type": 1,
    "showaimcursorinternal": 1,
    "scope": 1,
    # Compatible Magazines: magazines parameter (+ inherited),
    "magazines": [
        "rhs_mag_762x54mm_100","rhs_mag_762x54mm_250","rhs_mag_762x54mm_500","rhs_mag_762x54mm_1000",
        "rhs_mag_762x54mm_2000",],
    "initspeed": 0,
    "reloadtime": 0.075,
    "autofire": 1,
    "soundcontinuous": 0,
    "dispersion": 0.003,
    "minrange": 2,
    "minrangeprobab": 0.1,
    "midrange": 200,
    "midrangeprobab": 0.7,
    "maxrange": 600,
    "maxrangeprobab": 0.01,
    "maxleadspeed": 600,
    "canlock": 0,
    "cursor": "EmptyCursor",
    "cursoraim": "mg",
    "namesound": "mgun",
    "reloadaction": "ManActReloadMagazine",
    "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
    "sounds": ["StandardSound"],
    # Class: CfgWeapons|MGun|StandardSound [Indent level: 1],
    "standardsound": {
        "begin1": ["A3|Sounds_F|arsenal|weapons_vehicles|HMG_050|HMG_050_01",1.58489,1,2100],
        "begin2": ["A3|Sounds_F|arsenal|weapons_vehicles|HMG_050|HMG_050_02",1.58489,1,2100],
        "begin3": ["A3|Sounds_F|arsenal|weapons_vehicles|HMG_050|HMG_050_03",1.58489,1,2100],
        "soundbegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34],
        "soundsetshot": ["HMG050_Shot_SoundSet","HMG050_Tail_SoundSet"]
    },
    "flash": "gunfire",
    "flashsize": 0.5,
    "optics": 0,
    "texturetype": "fullAuto",
    "dexterity": 0.5,
    "airateoffire": 0.5,
    "airateoffiredistance": 400,
    "inertia": 0.7,
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