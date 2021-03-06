rhs_weap_savz61 = {
    "author": "Red Hammer Studios",
    "picture": "rhsgref|addons|rhsgref_inventoryicons|data|weapons|rhs_weap_savz61_ca.paa",
    "dlc": "RHS_GREF",
    "displayname": "Sa vz. 61",
    "scope": 2,
    "weaponinfotype": "rhs_rscOptics_vz61",
    "rhs_fold": "rhs_weap_savz61_folded",
    "magazines": ["rhsgref_20rnd_765x17_vz61","rhsgref_10rnd_765x17_vz61"],
    "magazinewell": ["CBA_32ACP_Vz61"],
    # Class: CfgWeapons|rhs_weap_savz61|Library [Indent level: 1],
    "library": {
        "libtextdesc": "The Škorpion vz. 61 is a Czechoslovak 7.65 mm machine pistol developed in 1959 by Miroslav Rybář (1924–1970) and produced under the official designation Samopal vzor 61 by the Česká zbrojovka arms factory in Uherský Brod from 1961 to 1979."
    },
    "model": "rhsgref|addons|rhsgref_weapons|savz61|rhs_savz61",
    "reloadaction": "GestureReloadSMG_02",
    "maxrecoilsway": 0.0125,
    "swaydecayspeed": 1.25,
    # Class: CfgWeapons|rhs_weap_savz61|GunParticles [Indent level: 1],
    "gunparticles": {
        # Class: CfgWeapons|rhs_weap_savz61|GunParticles|FirstEffect [Indent level: 2]
        "firsteffect": {
            "effectname": "PistolCloud",
            "positionname": "Usti hlavne",
            "directionname": "Konec hlavne"
        },
        # Class: CfgWeapons|rhs_weap_savz61|GunParticles|SecondEffect [Indent level: 2],
        "secondeffect": {
            "positionname": "Nabojnicestart",
            "directionname": "Nabojniceend",
            "effectname": "CaselessAmmoCloud"
        }
    },
    # Class: CfgWeapons|rhs_weap_savz61|WeaponSlotsInfo [Indent level: 1],
    "weaponslotsinfo": {
        "mass": 28.16,
        "allowedslots": [901],
        # Class: CfgWeapons|rhs_weap_savz61|WeaponSlotsInfo|MuzzleSlot [Indent level: 2],
        "muzzleslot": {
            "linkproxy": "A3|data_f|proxies|weapon_slots|MUZZLE",
            "compatibleitems": [],
            "iconposition": [0,0.45],
            "iconscale": 0.2,
            "iconpicture": "A3|Weapons_F|Data|UI|attachment_muzzle.paa",
            "iconpinpoint": "Center",
            "displayname": "$str_a3_cfgweapons_abr_base_f_weaponslotsinfo_muzzleslot0",
            "access": 1,
            "scope": 0
        },
        # Class: CfgWeapons|rhs_weap_savz61|WeaponSlotsInfo|CowsSlot [Indent level: 2],
        "cowsslot": {
            "iconposition": [0.5,0.35],
            "iconscale": 0.2,
            "compatibleitems": [],
            "linkproxy": "A3|data_f|proxies|weapon_slots|TOP",
            "displayname": "Optics Slot",
            "iconpicture": "A3|Weapons_F|Data|UI|attachment_top.paa",
            "iconpinpoint": "Bottom",
            "access": 1,
            "scope": 0
        },
        # Class: CfgWeapons|rhs_weap_savz61|WeaponSlotsInfo|PointerSlot [Indent level: 2],
        "pointerslot": {
        }
    },
    "opticszoommin": 0.375,
    "opticszoommax": 1.1,
    "opticszoominit": 0.75,
    "distancezoommin": 300,
    "distancezoommax": 300,
    "descriptionshort": "Sub-machine gun <br/>Caliber: 7.65x17 mm",
    "handanim": ["OFP2_ManSkeleton","|rhsgref|addons|rhsgref_c_weapons|anims|rhs_hand_savz61.rtm"],
    "selectionfireanim": "zasleh",
    "discretedistance": [75,150],
    "modes": ["Single","FullAuto"],
    # Class: CfgWeapons|rhs_weap_savz61|Single [Indent level: 1],
    "single": {
        "reloadtime": 0.075,
        "dispersion": 0.002909,
        "minrange": 2,
        "minrangeprobab": 0.3,
        "midrange": 200,
        "midrangeprobab": 0.7,
        "maxrange": 350,
        "maxrangeprobab": 0.05,
        "airateoffire": 2,
        "airateoffiredistance": 500,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_savz61|Single|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHSGREF_scorp_Shot_SoundSet","RHSGREF_pistol1_Tail_SoundSet"]
        },
        # Class: CfgWeapons|SMG_01_Base|Single|BaseSoundModeType [Indent level: 2],
        "basesoundmodetype": {
        },
        # Class: CfgWeapons|SMG_01_Base|Single|SilencedSound [Indent level: 2],
        "silencedsound": {
            "soundsetshot": ["SMGVermin_silencerShot_SoundSet","SMGVermin_silencerTail_SoundSet","SMGVermin_silencerInteriorTail_SoundSet"]
        },
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.014348,0.03,0.0159085,0.0060048,0.03,0.0138285,0.0042784,0.06,0.0066492,0.001824,0.06,-0.0007206,-0.001152,0.06,-0.001765,-0.001128,0.06,-0.0018385,-0.000588,0.06,-0.0009414,-0.00025,0.06,0,0],
        # Recoil Array: recoilprone,
        "recoilprone": [0,0,0,0.03,0.0110829,0.0050218,0.03,0.0159085,0.0027522,0.03,0.0138285,0.002292,0.06,0.0066492,0.001083,0.06,-0.0007206,-0.000384,0.06,-0.001765,-0.000282,0.06,-0.0018385,-0.000147,0.06,-0.0009414,-7.5e-005,0.06,0,0],
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
    # Class: CfgWeapons|rhs_weap_savz61|FullAuto [Indent level: 1],
    "fullauto": {
        "reloadtime": 0.075,
        "dispersion": 0.002909,
        "minrange": 0,
        "minrangeprobab": 0.1,
        "midrange": 25,
        "midrangeprobab": 0.7,
        "maxrange": 70,
        "maxrangeprobab": 0.05,
        "airateoffire": 0.2,
        "airateoffiredistance": 50,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_savz61|FullAuto|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["RHSGREF_scorp_Shot_SoundSet","RHSGREF_pistol1_Tail_SoundSet"]
        },
        # Class: CfgWeapons|SMG_01_Base|FullAuto|BaseSoundModeType [Indent level: 2],
        "basesoundmodetype": {
        },
        # Class: CfgWeapons|SMG_01_Base|FullAuto|SilencedSound [Indent level: 2],
        "silencedsound": {
            "soundsetshot": ["SMGVermin_silencerShot_SoundSet","SMGVermin_silencerTail_SoundSet","SMGVermin_silencerInteriorTail_SoundSet"]
        },
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.06,0.0221658,0.0050218,0.06,0.031817,0.0032526,0.06,0.027657,0.0024448,0.06,0.0132984,0.00114,0.03,-0.0014412,-0.001152,0.03,-0.00353,-0.001128,0.03,-0.003677,-0.000588,0.06,-0.0018828,-0.00025,0.06,0,0],
        # Recoil Array: recoilprone,
        "recoilprone": [0,0,0,0.06,0.0221658,0.0021522,0.06,0.031817,0.0017514,0.06,0.027657,0.0016808,0.06,0.0132984,0.000855,0.03,-0.0014412,-0.000768,0.03,-0.00353,-0.000564,0.03,-0.003677,-0.000294,0.06,-0.0018828,-0.00025,0.06,0,0],
        "sound": ["",10,1],
        "soundend": ["sound",1],
        "soundcontinuous": 0,
        "autofire": 1,
        "displayname": "Full",
        "texturetype": "fullAuto",
        "aidispersioncoefy": 3,
        "aidispersioncoefx": 2,
        "soundburst": 0,
        "multiplier": 1,
        "burst": 1,
        "burstrangemax": -1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
        "soundloop": [],
        "weaponsoundeffect": "",
        "ffcount": 1,
        "ffmagnitude": 0.5,
        "fffrequency": 11,
        "flash": "gunfire",
        "flashsize": 0.1,
        "useaction": 0,
        "useactiontitle": "",
        "showtoplayer": 1,
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "canshootinwater": 0,
        "requiredoptictype": -1,
        "airateoffiredispersion": 1
    },
    "baseweapon": "rhs_weap_savz61",
    "_generalmacro": "SMG_01_F",
    "inertia": 0.3,
    "aimtransitionspeed": 1.4,
    "dexterity": 1.7,
    "initspeed": 280,
    "uipicture": "A3|Weapons_F|data|UI|icon_regular_CA.paa",
    "maxzeroing": 400,
    # Recoil Class: recoil,
    # Class: CfgRecoils|recoil_smg_01 [Indent level: 0],
    "recoil": {
        "muzzleouter": [0.1,0.4,0.2,0.3],
        "kickback": [0.01,0.03],
        "temporary": 0.01,
        "muzzleinner": [0,0,0.1,0.1],
        "permanent": 0.1
    },
    "cursor": "smg",
    "discretedistanceinitindex": 0,
    "aidispersioncoefy": 8,
    "aidispersioncoefx": 9,
    "hiddenselections": ["camo1","camo2","camo3"],
    "hiddenselectionstextures": ["|a3|weapons_f_beta|smgs|smg_01|data|smg_01_co.paa","|a3|weapons_f|data|vectoratt_co.paa","|a3|weapons_f|acc|data|battlesight_co.paa"],
    "bullet1": ["A3|sounds_f|weapons|shells|9mm|metal_9mm_01",0.501187,1,15],
    "bullet2": ["A3|sounds_f|weapons|shells|9mm|metal_9mm_02",0.501187,1,15],
    "bullet3": ["A3|sounds_f|weapons|shells|9mm|metal_9mm_03",0.501187,1,15],
    "bullet4": ["A3|sounds_f|weapons|shells|9mm|metal_9mm_04",0.501187,1,15],
    "bullet5": ["A3|sounds_f|weapons|shells|9mm|dirt_9mm_01",0.562341,1,15],
    "bullet6": ["A3|sounds_f|weapons|shells|9mm|dirt_9mm_02",0.562341,1,15],
    "bullet7": ["A3|sounds_f|weapons|shells|9mm|dirt_9mm_03",0.562341,1,15],
    "bullet8": ["A3|sounds_f|weapons|shells|9mm|dirt_9mm_04",0.562341,1,15],
    "bullet9": ["A3|sounds_f|weapons|shells|9mm|grass_9mm_01",0.398107,1,15],
    "bullet10": ["A3|sounds_f|weapons|shells|9mm|grass_9mm_02",0.398107,1,15],
    "bullet11": ["A3|sounds_f|weapons|shells|9mm|grass_9mm_03",0.398107,1,15],
    "bullet12": ["A3|sounds_f|weapons|shells|9mm|grass_9mm_04",0.398107,1,15],
    "soundbullet": ["bullet1",0.083,"bullet2",0.083,"bullet3",0.083,"bullet4",0.083,"bullet5",0.083,"bullet6",0.083,"bullet7",0.083,"bullet8",0.083,"bullet9",0.083,"bullet10",0.083,"bullet11",0.083,"bullet12",0.083],
    "drysound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Dry_Vermin",0.501187,1,10],
    "reloadmagazinesound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|reload_vermin",1,1,10],
    "changefiremodesound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|firemode_Vermin",0.251189,1,5],
    # Class: CfgWeapons|SMG_01_Base|Burst [Indent level: 1],
    "burst": {
        "sounds": ["StandardSound","SilencedSound"],
        # Class: CfgWeapons|SMG_01_Base|Burst|BaseSoundModeType [Indent level: 2],
        "basesoundmodetype": {
        },
        # Class: CfgWeapons|SMG_01_Base|Burst|StandardSound [Indent level: 2],
        "standardsound": {
            "soundsetshot": ["SMGVermin_Shot_SoundSet","SMGVermin_Tail_SoundSet","SMGVermin_InteriorTail_SoundSet"]
        },
        # Class: CfgWeapons|SMG_01_Base|Burst|SilencedSound [Indent level: 2],
        "silencedsound": {
            "soundsetshot": ["SMGVermin_silencerShot_SoundSet","SMGVermin_silencerTail_SoundSet","SMGVermin_silencerInteriorTail_SoundSet"]
        },
        "soundburst": 0,
        "texturetype": "dual",
        "burst": 2,
        "reloadtime": 0.05,
        "dispersion": 0.00131,
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.007174,0.03,0.0159085,0.0035028,0.03,0.0138285,0.003056,0.03,0.0066492,0.001254,0.03,-0.0007206,-0.001728,0.03,-0.001765,-0.001974,0.03,-0.0018385,-0.00147,0.03,-0.0009414,-0.00025,0.06,0,0],
        # Recoil Array: recoilprone,
        "recoilprone": [0,0,0,0.03,0.0110829,0.0021522,0.03,0.0159085,0.0017514,0.03,0.0138285,0.0016808,0.06,0.0066492,0.000855,0.06,-0.0007206,-0.000768,0.06,-0.001765,-0.000564,0.06,-0.0018385,-0.000294,0.06,-0.0009414,-0.00025,0.06,0,0],
        "minrange": 2,
        "minrangeprobab": 0.3,
        "midrange": 50,
        "midrangeprobab": 0.7,
        "maxrange": 100,
        "maxrangeprobab": 0.05,
        "airateoffire": 1,
        "airateoffiredistance": 250,
        "sound": ["",10,1],
        "soundloop": ["sound",1],
        "soundend": ["sound",1],
        "displayname": "Burst",
        "aidispersioncoefy": 2.4,
        "aidispersioncoefx": 1.9,
        "multiplier": 1,
        "burstrangemax": -1,
        "soundbegin": ["sound",1],
        "soundbeginwater": ["sound",1],
        "soundclosure": ["sound",1],
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
        "requiredoptictype": -1,
        "airateoffiredispersion": 1
    },
    "deployedpivot": "bipod",
    "htmin": 1,
    "htmax": 600,
    "afmax": 0,
    "mfmax": 0,
    "mfact": 1,
    "tbody": 100,
    "autofire": 1,
    "soundcontinuous": 0,
    "optics": 0,
    "cursoraim": "CursorAim",
    "value": 4,
    "namesound": "rifle",
    "reloadtime": 0.15,
    "modeloptics": "-",
    "sound": [],
    "opticsflare": 0,
    "autoreload": 0,
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
    "zeroingsound": ["A3|Sounds_F|arsenal|sfx|shared|zeroing_knob_tick_metal",0.316228,1,5],
    "type": 1,
    "airateoffire": 0.5,
    "airateoffiredistance": 500,
    "access": 3,
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
    "emptysound": ["",1,1],
    "ballisticscomputer": 0,
    "irdistance": 0,
    "irdotintensity": 0.001,
    "lockacquire": 1,
    "enableattack": 1,
    "modelspecial": "",
    "modelmagazine": "",
    "muzzlepos": "usti hlavne",
    "muzzleend": "konec hlavne",
    "irlaserpos": "laser pos",
    "irlaserend": "laser dir",
    "cartridgepos": "nabojnicestart",
    "cartridgevel": "nabojniceend",
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
    "minrange": 1,
    "minrangeprobab": 0.3,
    "midrange": 150,
    "midrangeprobab": 0.58,
    "maxrange": 500,
    "maxrangeprobab": 0.04,
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
    "texturetype": "default",
}