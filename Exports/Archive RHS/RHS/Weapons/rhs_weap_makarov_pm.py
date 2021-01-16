rhs_weap_makarov_pm = {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf|addons|rhs_inventoryicons|data|weapons|rhs_weap_makarov_pm_ca.paa",
    "scope": 2,
    "displayname": "PM",
    "descriptionshort": "Pistol<br/>Caliber: 9x18mm",
    "model": "rhsafrf|addons|rhs_weapons2|pistols|pm|rhs_makarov_pm",
    "modeloptics": "-",
    # Class: CfgWeapons|rhs_weap_makarov_pm|SAFE_PISTOL [Indent level: 1],
    "safe_pistol": {
        "showtoplayer": 0,
        "magazines": [],
        "displayname": "SAFE",
        "descriptionshort": "SAFE",
        "modes": ["Safe"],
        "discretedistance": [0],
        "discretedistanceinitindex": 0,
        "drysound": ["A3|Sounds_F|arsenal|weapons|Rifles|MX|dry_Mx",0.562341,1,10],
        "changefiremodesound": ["A3|sounds_f|weapons|closure|firemode_changer_2",0.551189,1,5],
        # Class: CfgWeapons|RHS_SAFE_BASE|Safe [Indent level: 1],
        "safe": {
            "sounds": [],
            "displayname": "SAFE",
            "descriptionshort": "SAFE",
            "showtoplayer": 0,
            "minrange": 0,
            "minrangeprobab": 0.001,
            "midrange": 0.001,
            "midrangeprobab": 0.001,
            "maxrange": 0.001,
            "maxrangeprobab": 0.001,
            "multiplier": 1,
            "burst": 1,
            "burstrangemax": -1,
            "dispersion": 0.0002,
            "sound": ["",10,1],
            "soundbegin": ["sound",1],
            "soundbeginwater": ["sound",1],
            "soundclosure": ["sound",1],
            "soundend": [],
            "soundloop": [],
            "soundcontinuous": 0,
            "weaponsoundeffect": "",
            "reloadtime": 0.1,
            "ffcount": 1,
            "ffmagnitude": 0.5,
            "fffrequency": 11,
            "flash": "gunfire",
            "flashsize": 0.1,
            "autofire": 0,
            "useaction": 0,
            "useactiontitle": "",
            "artillerydispersion": 1,
            "artillerycharge": 1,
            "canshootinwater": 0,
            "texturetype": "semi",
            # Recoil Array: recoil,
            "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
            # Recoil Array: recoilprone,
            "recoilprone": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
            "aidispersioncoefy": 1.7,
            "aidispersioncoefx": 1.4,
            "soundburst": 0,
            "requiredoptictype": -1,
            "airateoffire": 2,
            "airateoffiredispersion": 1,
            "airateoffiredistance": 500
        },
        "scope": 0,
        "weaponinfotype": "RscWeaponZeroing",
        # Recoil Class: recoil,
        # Class: CfgRecoils|recoil_default [Indent level: 0],
        "recoil": {
            "muzzleouter": [0.3,1,0.3,0.2],
            "muzzleinner": [0,0,0.1,0.1],
            "kickback": [0.03,0.06],
            "permanent": 0.1,
            "temporary": 0.01
        },
        "deployedpivot": "bipod",
        # Class: CfgWeapons|Rifle_Base_F|GunParticles [Indent level: 1],
        "gunparticles": {
            # Class: CfgWeapons|Rifle_Base_F|GunParticles|FirstEffect [Indent level: 2]
            "firsteffect": {
                "effectname": "RifleAssaultCloud",
                "positionname": "Usti hlavne",
                "directionname": "Konec hlavne"
            }
        },
        "htmin": 1,
        "htmax": 600,
        "afmax": 0,
        "mfmax": 0,
        "mfact": 1,
        "tbody": 100,
        "autofire": 1,
        "reloadaction": "ReloadMagazine",
        "soundcontinuous": 0,
        "optics": 0,
        "cursor": "arifle",
        "cursoraim": "CursorAim",
        "value": 4,
        "namesound": "rifle",
        "reloadtime": 0.15,
        "modeloptics": "-",
        "sound": [],
        "opticsflare": 0,
        "autoreload": 0,
        "aidispersioncoefx": 6,
        "aidispersioncoefy": 6,
        "opticszoommin": 0.25,
        "opticszoommax": 1.25,
        "opticszoominit": 0.75,
        "distancezoommin": 300,
        "distancezoommax": 300,
        "maxleadspeed": 23,
        "canlock": 0,
        "flash": "gunfire",
        "flashsize": 0.5,
        "dispersion": 0.00029,
        # Recoil Array: recoilprone,
        "recoilprone": [0,0,0,0.06,0.01,0.01,0.1,0,-0.02,0.1,-0.01,0.01,0.05,0,0],
        "ffmagnitude": 0.5,
        "fffrequency": 11,
        "ffcount": 3,
        "weaponpoolavailable": 1,
        "maxzeroing": 1000,
        # Class: CfgWeapons|Rifle|WeaponSlotsInfo [Indent level: 1],
        "weaponslotsinfo": {
            "mass": 2,
            # Class: CfgWeapons|Rifle|WeaponSlotsInfo|MuzzleSlot [Indent level: 2],
            "muzzleslot": {
                "linkproxy": "A3|data_f|proxies|weapon_slots|MUZZLE",
                "displayname": "$str_a3_cfgweapons_abr_base_f_weaponslotsinfo_muzzleslot0",
                "compatibleitems": [],
                "iconpicture": "A3|Weapons_F|Data|UI|attachment_muzzle.paa",
                "iconpinpoint": "Center",
                "access": 1,
                "scope": 0,
                "iconposition": [0,0],
                "iconscale": 0
            },
            # Class: CfgWeapons|Rifle|WeaponSlotsInfo|CowsSlot [Indent level: 2],
            "cowsslot": {
                "compatibleitems": ["optic_Nightstalker","optic_tws","optic_tws_mg","optic_NVS","optic_DMS","optic_LRPS","optic_ams","optic_AMS_snd","optic_AMS_khk","optic_KHS_blk","optic_KHS_tan","optic_KHS_hex","optic_KHS_old","optic_SOS","optic_MRCO","optic_Arco","optic_aco","optic_ACO_grn","optic_aco_smg","optic_ACO_grn_smg","optic_hamr","optic_Holosight","optic_Holosight_smg","optic_Hamr_khk_F","optic_SOS_khk_F","optic_Arco_ghex_F","optic_Arco_blk_F","optic_DMS_ghex_F","optic_ERCO_blk_F","optic_ERCO_khk_F","optic_ERCO_snd_F","optic_LRPS_ghex_F","optic_LRPS_tna_F","optic_Holosight_blk_F","optic_Holosight_khk_F","optic_Holosight_smg_blk_F","optic_Holosight_smg_khk_F","optic_Arco_AK_blk_F","optic_Arco_AK_lush_F","optic_Arco_AK_arid_F","optic_DMS_weathered_F","optic_DMS_weathered_Kir_F","optic_Arco_lush_F","optic_Arco_arid_F","optic_Holosight_lush_F","optic_Holosight_arid_F"],
                "linkproxy": "A3|data_f|proxies|weapon_slots|TOP",
                "displayname": "Optics Slot",
                "iconpicture": "A3|Weapons_F|Data|UI|attachment_top.paa",
                "iconpinpoint": "Bottom",
                "access": 1,
                "scope": 0,
                "iconposition": [0,0],
                "iconscale": 0
            },
            # Class: CfgWeapons|Rifle|WeaponSlotsInfo|PointerSlot [Indent level: 2],
            "pointerslot": {
                "compatibleitems": ["acc_flashlight","acc_pointer_IR"],
                "iconpicture": "A3|Weapons_F|Data|UI|attachment_side.paa",
                "iconpinpoint": "Center",
                "linkproxy": "A3|data_f|proxies|weapon_slots|SIDE",
                "displayname": "Pointer Slot",
                "access": 1,
                "scope": 0,
                "iconposition": [0,0],
                "iconscale": 0
            },
            "allowedslots": [901]
        },
        "zeroingsound": ["A3|Sounds_F|arsenal|sfx|shared|zeroing_knob_tick_metal",0.316228,1,5],
        "type": 1,
        "dexterity": 1.7,
        "airateoffire": 0.5,
        "airateoffiredistance": 500,
        "inertia": 0.5,
        "access": 3,
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
        "magazinereloadtime": 0,
        "magazinereloadswitchphase": 1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": ["sound",1],
        "soundloop": ["sound",1],
        "weaponsoundeffect": "",
        "soundburst": 1,
        "reloadsound": ["",1,1],
        "reloadmagazinesound": ["",1,1],
        "emptysound": ["",1,1],
        "soundbullet": ["emptySound",1],
        "initspeed": 0,
        "ballisticscomputer": 0,
        "irdistance": 0,
        "irdotintensity": 0.001,
        "lockacquire": 1,
        "enableattack": 1,
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
        "opticsppeffects": [],
        "forceoptics": 0,
        "useasbinocular": 0,
        "opticsdisableperipherialvision": 0.67,
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
        "aimtransitionspeed": 1
    },
    "muzzles": ["this","SAFE_PISTOL"],
    "weaponinfotype": "rhs_rscOptics_pistol",
    # Class: CfgWeapons|rhs_weap_makarov_pm|WeaponSlotsInfo [Indent level: 1],
    "weaponslotsinfo": {
        "mass": 16.72,
        # Class: CfgWeapons|rhs_weap_makarov_pm|WeaponSlotsInfo|CowsSlot [Indent level: 2],
        "cowsslot": {
            "iconposition": [0,0],
            "iconscale": 1,
            "iconpicture": "A3|Weapons_F|Data|clear_empty.paa",
            "iconpinpoint": "Left"
        },
        # Class: CfgWeapons|rhs_weap_makarov_pm|WeaponSlotsInfo|MuzzleSlot [Indent level: 2],
        "muzzleslot": {
        },
        # Class: CfgWeapons|rhs_weap_makarov_pm|WeaponSlotsInfo|PointerSlot [Indent level: 2],
        "pointerslot": {
        },
        "holsteroffset": "holster",
        "holsterscale": 0.95
    },
    "magazines": ["rhs_mag_9x18_8_57N181S"],
    "magazinewell": ["CBA_9x18_PM"],
    "dispersion": 0.02,
    "ffcount": 1,
    "airateoffire": 0.5,
    "airateoffiredistance": 50,
    "baseweapon": "rhs_weap_makarov_pm",
    "dlc": "RHS_AFRF",
    "minrange": 0,
    "minrangeprobab": 0.1,
    "midrange": 30,
    "midrangeprobab": 0.3,
    "maxrange": 50,
    "maxrangeprobab": 0.04,
    "optics": 1,
    "distancezoommin": 50,
    "distancezoommax": 50,
    "begin1": ["rhsafrf|addons|rhs_weapons|sounds|pya_2",0.794328,1,700],
    "soundbegin": ["begin1",1],
    # Class: CfgWeapons|rhs_weap_pya|Library [Indent level: 1],
    "library": {
        "libtextdesc": "MP-443"
    },
    "sounds": ["StandardSound","SilencedSound"],
    # Class: CfgWeapons|rhs_weap_pya|StandardSound [Indent level: 1],
    "standardsound": {
        "begin1": ["rhsafrf|addons|rhs_sounds|mp-443|mp-443_1",2.55,1,1000],
        "begin2": ["rhsafrf|addons|rhs_sounds|mp-443|mp-443_2",2.55,1,1000],
        "soundbegin": ["begin1",0.5,"begin2",0.5],
        "soundclosure": []
    },
    # Class: CfgWeapons|rhs_weap_pya|SilencedSound [Indent level: 1],
    "silencedsound": {
        "begin1": ["rhsafrf|addons|rhs_sounds|mp-443|mp-443_1",2.55,1,1000],
        "begin2": ["rhsafrf|addons|rhs_sounds|mp-443|mp-443_2",2.55,1,1000],
        "soundbegin": ["begin1",0.5,"begin2",0.5],
        "soundclosure": []
    },
    "_generalmacro": "hgun_Rook40_F",
    "hiddenselections": ["camo"],
    "hiddenselectionstextures": ["|A3|Weapons_F|Pistols|Rook40|data|Rook40_co"],
    "drysound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|dry_Rook40",0.223872,1,20],
    "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|reload_rook40",1,1,10],
    "modes": ["Single"],
    # Class: CfgWeapons|hgun_Rook40_F|Single [Indent level: 1],
    "single": {
        "sounds": ["StandardSound","SilencedSound"],
        # Class: CfgWeapons|hgun_Rook40_F|Single|BaseSoundModeType [Indent level: 2],
        "basesoundmodetype": {
            "closure1": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Closure_Rook40_01",0.158489,1,10],
            "closure2": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Closure_Rook40_02",0.158489,1.1,10],
            "soundclosure": ["closure1",0.5,"closure2",0.5]
        },
        # Class: CfgWeapons|hgun_Rook40_F|Single|StandardSound [Indent level: 2],
        "standardsound": {
            "begin1": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Rook40_short_01",3.16228,1,1200],
            "begin2": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Rook40_short_02",3.16228,1,1200],
            "begin3": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Rook40_short_03",3.16228,1,1200],
            "soundbegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34],
            # Class: CfgWeapons|hgun_Rook40_F|Single|StandardSound|SoundTails [Indent level: 3],
            "soundtails": {
                # Class: CfgWeapons|hgun_Rook40_F|Single|StandardSound|SoundTails|TailInterior [Indent level: 4]
                "tailinterior": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Rook40_tail_interior",1.41254,1,1200],
                    "frequency": 1,
                    "volume": "interior"
                },
                # Class: CfgWeapons|hgun_Rook40_F|Single|StandardSound|SoundTails|TailTrees [Indent level: 4],
                "tailtrees": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Rook40_tail_trees",1,1,1200],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*trees"
                },
                # Class: CfgWeapons|hgun_Rook40_F|Single|StandardSound|SoundTails|TailForest [Indent level: 4],
                "tailforest": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Rook40_tail_forest",1,1,1200],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*forest"
                },
                # Class: CfgWeapons|hgun_Rook40_F|Single|StandardSound|SoundTails|TailMeadows [Indent level: 4],
                "tailmeadows": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Rook40_tail_meadows",1,1,1200],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*(meadows/2 max sea/2)"
                },
                # Class: CfgWeapons|hgun_Rook40_F|Single|StandardSound|SoundTails|TailHouses [Indent level: 4],
                "tailhouses": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Rook40_tail_houses",1,1,1200],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*houses"
                }
            },
            "soundsetshot": ["Rook40_Shot_SoundSet","Rook40_Tail_SoundSet","Rook40_InteriorTail_SoundSet"],
            "closure1": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Closure_Rook40_01",0.158489,1,10],
            "closure2": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Closure_Rook40_02",0.158489,1.1,10],
            "soundclosure": ["closure1",0.5,"closure2",0.5]
        },
        # Class: CfgWeapons|hgun_Rook40_F|Single|SilencedSound [Indent level: 2],
        "silencedsound": {
            "begin1": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Silencer_Rook40_short_01",0.562341,1,400],
            "begin2": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Silencer_Rook40_short_02",0.562341,1,400],
            "begin3": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Silencer_Rook40_short_03",0.562341,1,400],
            "soundbegin": ["begin1",0.33,"begin2",0.33,"begin2",0.34],
            # Class: CfgWeapons|hgun_Rook40_F|Single|SilencedSound|SoundTails [Indent level: 3],
            "soundtails": {
                # Class: CfgWeapons|hgun_Rook40_F|Single|SilencedSound|SoundTails|TailInterior [Indent level: 4]
                "tailinterior": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Silencer_Rook40_tail_interior",1,1,400],
                    "frequency": 1,
                    "volume": "interior"
                },
                # Class: CfgWeapons|hgun_Rook40_F|Single|SilencedSound|SoundTails|TailTrees [Indent level: 4],
                "tailtrees": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Silencer_Rook40_tail_trees",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*trees"
                },
                # Class: CfgWeapons|hgun_Rook40_F|Single|SilencedSound|SoundTails|TailForest [Indent level: 4],
                "tailforest": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Silencer_Rook40_tail_forest",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*forest"
                },
                # Class: CfgWeapons|hgun_Rook40_F|Single|SilencedSound|SoundTails|TailMeadows [Indent level: 4],
                "tailmeadows": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Silencer_Rook40_tail_meadows",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*(meadows/2 max sea/2)"
                },
                # Class: CfgWeapons|hgun_Rook40_F|Single|SilencedSound|SoundTails|TailHouses [Indent level: 4],
                "tailhouses": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Silencer_Rook40_tail_houses",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*houses"
                }
            },
            "soundsetshot": ["Rook40_silencerShot_SoundSet","Rook40_silencerTail_SoundSet","Rook40_silencerInteriorTail_SoundSet"],
            "closure1": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Closure_Rook40_01",0.158489,1,10],
            "closure2": ["A3|Sounds_F|arsenal|weapons|Pistols|Rook40|Closure_Rook40_02",0.158489,1.1,10],
            "soundclosure": ["closure1",0.5,"closure2",0.5]
        },
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.036943,0.0268696,0.09,0.019755,0.006112,0.12,0,0,0.18,-0.003138,-0.001,0.12,-0.001177,-0.000376,0.12,0,0],
        # Recoil Array: recoilprone,
        "recoilprone": [0,0,0,0.03,0.036943,0.0134348,0.09,0.019755,0.003056,0.12,0,0,0.18,-0.003138,-0.0005,0.12,-0.001177,-0.000188,0.12,0,0],
        "reloadtime": 0.1,
        "dispersion": 0.00435,
        "minrange": 5,
        "minrangeprobab": 0.3,
        "midrange": 25,
        "midrangeprobab": 0.6,
        "maxrange": 50,
        "maxrangeprobab": 0.1,
        "airateoffire": 2,
        "airateoffiredistance": 25,
        "multiplier": 1,
        "burst": 1,
        "burstrangemax": -1,
        "sound": ["",10,1],
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundend": [],
        "soundloop": [],
        "soundcontinuous": 0,
        "weaponsoundeffect": "",
        "ffcount": 1,
        "ffmagnitude": 0.5,
        "fffrequency": 11,
        "flash": "gunfire",
        "flashsize": 0.1,
        "autofire": 0,
        "useaction": 0,
        "useactiontitle": "",
        "showtoplayer": 1,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "canshootinwater": 0,
        "displayname": "Semi",
        "texturetype": "semi",
        "aidispersioncoefy": 1.7,
        "aidispersioncoefx": 1.4,
        "soundburst": 0,
        "requiredoptictype": -1,
        "airateoffiredispersion": 1
    },
    "inertia": 0.2,
    "aimtransitionspeed": 1.6,
    "dexterity": 1.8,
    "initspeed": 450,
    # Recoil Class: recoil,
    # Class: CfgRecoils|recoil_pistol_rook40 [Indent level: 0],
    "recoil": {
        "muzzleouter": [0.2,1,0.2,0.3],
        "kickback": [0.03,0.06],
        "temporary": 0.02,
        "muzzleinner": [0,0,0.1,0.1],
        "permanent": 0.1
    },
    "maxzeroing": 100,
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
    "reloadaction": "GestureReloadPistol",
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
    "discretedistance": [50],
    "discretedistanceinitindex": 0,
    "magazinereloadtime": 2,
    "opticsflare": 0,
    "namesound": "Pistol",
    "type": 2,
    "canlock": 0,
    "access": 3,
    "value": 2,
    "uipicture": "",
    "ammo": "",
    "cursorsize": 1,
    "showaimcursorinternal": 1,
    "cursoraimon": "",
    "laser": 0,
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
    "ballisticscomputer": 0,
    "irdistance": 0,
    "irdotintensity": 0.001,
    "aidispersioncoefx": 1,
    "aidispersioncoefy": 1,
    "lockacquire": 1,
    "enableattack": 1,
    "ffmagnitude": 0,
    "fffrequency": 1,
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
    "forceoptics": 0,
    "useasbinocular": 0,
    "opticsdisableperipherialvision": 0.67,
    "primary": 10,
    "showswitchaction": 0,
    "showempty": 1,
    "autofire": 0,
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