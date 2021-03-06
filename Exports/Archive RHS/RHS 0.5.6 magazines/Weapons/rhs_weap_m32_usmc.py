rhs_weap_m32_usmc = {
    # Class: CfgWeapons|rhs_weap_m32_usmc|LinkedItems [Indent level: 1]
    "linkeditems": {
        # Class: CfgWeapons|rhs_weap_m32_usmc|LinkedItems|LinkedItemsOptic [Indent level: 2]
        "linkeditemsoptic": {
            "slot": "CowsSlot",
            "item": "rhsusf_acc_M2A1"
        }
    },
    "author": "Red Hammer Studios",
    "picture": "rhsusf|addons|rhsusf_inventoryicons|data|weapons|rhs_weap_m32_ca.paa",
    "scope": 2,
    "displayname": "M32 MGL",
    "descriptionshort": "Multiple Grenade Launcher<br />Caliber: 40mm",
    "dlc": "RHS_USAF",
    "uipicture": "A3|weapons_f|data|UI|icon_regular_CA.paa",
    "model": "rhsusf|addons|rhsusf_weapons2|M32|rhs_m32",
    # Compatible Magazines: magazines parameter (+ inherited),
    "magazines": [
        "rhsusf_mag_6rnd_m441_he","rhsusf_mag_6rnd_m433_hedp","rhsusf_mag_6rnd_m397_het","rhsusf_mag_6rnd_m576_buckshot",
        "rhsusf_mag_6rnd_m4009","rhsusf_mag_6rnd_m583a1_white","rhsusf_mag_6rnd_m661_green","rhsusf_mag_6rnd_m662_red",
        "rhsusf_mag_6rnd_m713_red","rhsusf_mag_6rnd_m714_white","rhsusf_mag_6rnd_m715_green","rhsusf_mag_6rnd_m716_yellow",
        "rhsusf_mag_6rnd_m781_practice",],
    "magazinewell": ["CBA_40mm_M203_6rnds"],
    # Class: CfgWeapons|rhs_weap_m32_Base_F|Library [Indent level: 1],
    "library": {
        "libtextdesc": ""
    },
    "optics": 0,
    "reloadaction": "GestureReloadKatibaUGL",
    "maxrecoilsway": 0.0125,
    "swaydecayspeed": 1.25,
    # Recoil Class: recoil,
    # Class: CfgRecoils|recoil_gm6 [Indent level: 0],
    "recoil": {
        "muzzleouter": [1.4,3.5,0.7,0.8],
        "kickback": [0.1,0.12],
        "temporary": 0.025,
        "muzzleinner": [0,0,0.1,0.1],
        "permanent": 0.1
    },
    "recoil": "recoil_gm6",
    # Class: CfgWeapons|rhs_weap_m32_Base_F|GunParticles [Indent level: 1],
    "gunparticles": {
        # Class: CfgWeapons|rhs_weap_m32_Base_F|GunParticles|SecondEffect [Indent level: 2]
        "secondeffect": {
            "positionname": "Nabojnicestart",
            "directionname": "Nabojniceend",
            "effectname": "RifleAssaultCloud"
        },
        # Class: CfgWeapons|Rifle_Base_F|GunParticles|FirstEffect [Indent level: 2],
        "firsteffect": {
            "effectname": "RifleAssaultCloud",
            "positionname": "Usti hlavne",
            "directionname": "Konec hlavne"
        }
    },
    "weaponinfotype": "RscWeaponZeroing",
    "cameradir": "gl_look",
    "discretedistance": [50,100,150,200,250,300,350,375],
    "discretedistancecamerapoint": ["gl_eye_50m","gl_eye_100m","gl_eye_150m","gl_eye_200m","gl_eye_250m","gl_eye_300m","gl_eye_350m","gl_eye_375m"],
    "discretedistanceinitindex": 1,
    "opticszoommin": 0.275,
    "opticszoommax": 1.1,
    "opticszoominit": 0.75,
    "distancezoommin": 50,
    "distancezoommax": 375,
    # Class: CfgWeapons|rhs_weap_m32_Base_F|WeaponSlotsInfo [Indent level: 1],
    "weaponslotsinfo": {
        "mass": 116.6,
        # Class: CfgWeapons|rhs_weap_m32_Base_F|WeaponSlotsInfo|CowsSlot [Indent level: 2],
        "cowsslot": {
        },
        # Class: CfgWeapons|rhs_weap_m32_Base_F|WeaponSlotsInfo|PointerSlot [Indent level: 2],
        "pointerslot": {
            "iconposition": [0,0],
            "iconscale": 1,
            "iconpicture": "A3|Weapons_F|Data|clear_empty.paa",
            "iconpinpoint": "Left",
            # Class: rhs_western_rifle_laser_slot|compatibleItems [Indent level: 0],
            "compatibleitems": {
                "rhsusf_acc_anpeq15": 0,
                "rhsusf_acc_anpeq15_top": 0,
                "rhsusf_acc_anpeq15_light": 0,
                "rhsusf_acc_anpeq15_bk": 0,
                "rhsusf_acc_anpeq15_bk_top": 0,
                "rhsusf_acc_anpeq15_bk_light": 0,
                "rhsusf_acc_anpeq15_wmx": 0,
                "rhsusf_acc_anpeq15_wmx_light": 0,
                "rhsusf_acc_anpeq16a_top": 0,
                "rhsusf_acc_anpeq16a_light_top": 0,
                "rhsusf_acc_anpeq16a_top_h": 0,
                "rhsusf_acc_anpeq16a_light_top_h": 0,
                "rhs_acc_2dpzenit_ris": 1,
                "rhs_acc_perst1ik_ris": 1,
                "rhs_acc_perst3": 1,
                "acc_flashlight": 1,
                "acc_pointer_ir": 1,
                "rhsusf_acc_wmx": 1,
                "rhsusf_acc_wmx_bk": 1,
                "rhsusf_acc_m952v": 1,
                "rhsusf_acc_anpeq15a": 1,
                "rhsusf_acc_anpeq15_h": 1,
                "rhsusf_acc_anpeq15_light_h": 1,
                "rhsusf_acc_anpeq15_top_h": 1,
                "rhsusf_acc_anpeq15_sc": 1,
                "rhsusf_acc_anpeq15_light_sc": 1,
                "rhsusf_acc_anpeq15_top_sc": 1,
                "rhsusf_acc_anpeq15side": 1,
                "rhsusf_acc_anpeq15_bk_h": 1,
                "rhsusf_acc_anpeq15_bk_light_h": 1,
                "rhsusf_acc_anpeq15_bk_top_h": 1,
                "rhsusf_acc_anpeq15_bk_sc": 1,
                "rhsusf_acc_anpeq15_bk_light_sc": 1,
                "rhsusf_acc_anpeq15_bk_top_sc": 1,
                "rhsusf_acc_anpeq15side_bk": 1,
                "rhsusf_acc_anpeq15_wmx_h": 1,
                "rhsusf_acc_anpeq15_wmx_light_h": 1,
                "rhsusf_acc_anpeq15_wmx_sc": 1,
                "rhsusf_acc_anpeq15_wmx_light_sc": 1,
                "rhsusf_acc_anpeq16a": 1,
                "rhsusf_acc_anpeq16a_light": 1,
                "rhsusf_acc_anpeq16a_top_sc": 1,
                "rhsusf_acc_anpeq16a_light_top_sc": 1
            },
            "linkproxy": "a3|data_f|proxies|weapon_slots|side",
            "displayname": "Pointer Slot"
        },
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
        "allowedslots": [901]
    },
    "handanim": ["OFP2_ManSkeleton","|rhsusf|addons|rhsusf_c_weapons|anims|rhs_hand_M32.rtm"],
    "dexterity": 1.8,
    "aimtransitionspeed": 0.65,
    "caseless": ["",1,1,1],
    "soundbullet": ["caseless",1],
    "modes": ["Single","far_optic1","medium_optic2","far_optic2"],
    # Class: CfgWeapons|rhs_weap_m32_Base_F|Single [Indent level: 1],
    "single": {
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_m32_Base_F|Single|StandardSound [Indent level: 2],
        "standardsound": {
            "weaponsoundeffect": "DefaultRifle",
            "soundclosure": ["closure1",0.5,"closure2",0.5],
            "begin1": ["rhsusf|addons|rhsusf_sounds|m32|m32_1",1.95,1,800],
            "begin2": ["rhsusf|addons|rhsusf_sounds|m32|m32_2",1.95,1,800],
            "soundbegin": ["begin1",0.5,"begin2",0.5],
            "closure1": ["rhsusf|addons|rhsusf_sounds|m32|Closure_1",2.4,1,35],
            "closure2": ["rhsusf|addons|rhsusf_sounds|m32|Closure_2",2.4,1,35],
            "soundsetshot": ["rhs_m32gl_shot_SoundSet","UGL_Tail_SoundSet","UGL_InteriorTail_SoundSet"]
        },
        "reloadtime": 0.075,
        "dispersion": 0.0002909,
        "minrange": 2,
        "minrangeprobab": 0.3,
        "midrange": 250,
        "midrangeprobab": 0.7,
        "maxrange": 400,
        "maxrangeprobab": 0.04,
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
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        "recoil": "recoil_single_primary_3outof10",
        # Recoil Array: recoilprone,
        "recoilprone": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "recoilprone": "recoil_single_primary_prone_3outof10",
        "aidispersioncoefy": 1.7,
        "aidispersioncoefx": 1.4,
        "soundburst": 0,
        "requiredoptictype": -1,
        "airateoffire": 2,
        "airateoffiredispersion": 1,
        "airateoffiredistance": 500
    },
    # Class: CfgWeapons|rhs_weap_m32_Base_F|far_optic1 [Indent level: 1],
    "far_optic1": {
        "showtoplayer": 0,
        "minrange": 150,
        "minrangeprobab": 0.1,
        "midrange": 500,
        "midrangeprobab": 0.7,
        "maxrange": 1000,
        "maxrangeprobab": 0.3,
        "airateoffire": 5,
        "airateoffiredistance": 700,
        "requiredoptictype": 1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_m32_Base_F|Single|StandardSound [Indent level: 2],
        "standardsound": {
            "weaponsoundeffect": "DefaultRifle",
            "soundclosure": ["closure1",0.5,"closure2",0.5],
            "begin1": ["rhsusf|addons|rhsusf_sounds|m32|m32_1",1.95,1,800],
            "begin2": ["rhsusf|addons|rhsusf_sounds|m32|m32_2",1.95,1,800],
            "soundbegin": ["begin1",0.5,"begin2",0.5],
            "closure1": ["rhsusf|addons|rhsusf_sounds|m32|Closure_1",2.4,1,35],
            "closure2": ["rhsusf|addons|rhsusf_sounds|m32|Closure_2",2.4,1,35],
            "soundsetshot": ["rhs_m32gl_shot_SoundSet","UGL_Tail_SoundSet","UGL_InteriorTail_SoundSet"]
        },
        "reloadtime": 0.075,
        "dispersion": 0.0002909,
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
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "canshootinwater": 0,
        "displayname": "Semi",
        "texturetype": "semi",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        "recoil": "recoil_single_primary_3outof10",
        # Recoil Array: recoilprone,
        "recoilprone": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "recoilprone": "recoil_single_primary_prone_3outof10",
        "aidispersioncoefy": 1.7,
        "aidispersioncoefx": 1.4,
        "soundburst": 0,
        "airateoffiredispersion": 1
    },
    # Class: CfgWeapons|rhs_weap_m32_Base_F|medium_optic2 [Indent level: 1],
    "medium_optic2": {
        "showtoplayer": 0,
        "minrange": 250,
        "minrangeprobab": 0.1,
        "midrange": 750,
        "midrangeprobab": 0.7,
        "maxrange": 1000,
        "maxrangeprobab": 0.3,
        "airateoffire": 6,
        "airateoffiredistance": 1000,
        "requiredoptictype": 2,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_m32_Base_F|Single|StandardSound [Indent level: 2],
        "standardsound": {
            "weaponsoundeffect": "DefaultRifle",
            "soundclosure": ["closure1",0.5,"closure2",0.5],
            "begin1": ["rhsusf|addons|rhsusf_sounds|m32|m32_1",1.95,1,800],
            "begin2": ["rhsusf|addons|rhsusf_sounds|m32|m32_2",1.95,1,800],
            "soundbegin": ["begin1",0.5,"begin2",0.5],
            "closure1": ["rhsusf|addons|rhsusf_sounds|m32|Closure_1",2.4,1,35],
            "closure2": ["rhsusf|addons|rhsusf_sounds|m32|Closure_2",2.4,1,35],
            "soundsetshot": ["rhs_m32gl_shot_SoundSet","UGL_Tail_SoundSet","UGL_InteriorTail_SoundSet"]
        },
        "reloadtime": 0.075,
        "dispersion": 0.0002909,
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
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "canshootinwater": 0,
        "displayname": "Semi",
        "texturetype": "semi",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        "recoil": "recoil_single_primary_3outof10",
        # Recoil Array: recoilprone,
        "recoilprone": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "recoilprone": "recoil_single_primary_prone_3outof10",
        "aidispersioncoefy": 1.7,
        "aidispersioncoefx": 1.4,
        "soundburst": 0,
        "airateoffiredispersion": 1
    },
    # Class: CfgWeapons|rhs_weap_m32_Base_F|far_optic2 [Indent level: 1],
    "far_optic2": {
        "minrange": 500,
        "minrangeprobab": 0.1,
        "midrange": 1050,
        "midrangeprobab": 0.7,
        "maxrange": 2000,
        "maxrangeprobab": 0.3,
        "airateoffire": 8,
        "airateoffiredistance": 2000,
        "requiredoptictype": 2,
        "showtoplayer": 0,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons|rhs_weap_m32_Base_F|Single|StandardSound [Indent level: 2],
        "standardsound": {
            "weaponsoundeffect": "DefaultRifle",
            "soundclosure": ["closure1",0.5,"closure2",0.5],
            "begin1": ["rhsusf|addons|rhsusf_sounds|m32|m32_1",1.95,1,800],
            "begin2": ["rhsusf|addons|rhsusf_sounds|m32|m32_2",1.95,1,800],
            "soundbegin": ["begin1",0.5,"begin2",0.5],
            "closure1": ["rhsusf|addons|rhsusf_sounds|m32|Closure_1",2.4,1,35],
            "closure2": ["rhsusf|addons|rhsusf_sounds|m32|Closure_2",2.4,1,35],
            "soundsetshot": ["rhs_m32gl_shot_SoundSet","UGL_Tail_SoundSet","UGL_InteriorTail_SoundSet"]
        },
        "reloadtime": 0.075,
        "dispersion": 0.0002909,
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
        "artillerydispersion": 1,
        "artillerycharge": 1,
        "canshootinwater": 0,
        "displayname": "Semi",
        "texturetype": "semi",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        "recoil": "recoil_single_primary_3outof10",
        # Recoil Array: recoilprone,
        "recoilprone": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "recoilprone": "recoil_single_primary_prone_3outof10",
        "aidispersioncoefy": 1.7,
        "aidispersioncoefx": 1.4,
        "soundburst": 0,
        "airateoffiredispersion": 1
    },
    "aidispersioncoefy": 10,
    "aidispersioncoefx": 8,
    "drysound": ["A3|sounds_f|weapons|Other|dry_1",0.01,1],
    "deployedpivot": "bipod",
    "htmin": 1,
    "htmax": 600,
    "afmax": 0,
    "mfmax": 0,
    "mfact": 1,
    "tbody": 100,
    "autofire": 1,
    "soundcontinuous": 0,
    "cursor": "arifle",
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
    "recoilprone": "assaultRifleBase",
    "ffmagnitude": 0.5,
    "fffrequency": 11,
    "ffcount": 3,
    "weaponpoolavailable": 1,
    "maxzeroing": 1000,
    "zeroingsound": ["A3|Sounds_F|arsenal|sfx|shared|zeroing_knob_tick_metal",0.316228,1,5],
    "type": 1,
    "airateoffire": 0.5,
    "airateoffiredistance": 500,
    "inertia": 0.5,
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
    "changefiremodesound": ["",1,1],
    "reloadmagazinesound": ["",1,1],
    "emptysound": ["",1,1],
    "initspeed": 0,
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