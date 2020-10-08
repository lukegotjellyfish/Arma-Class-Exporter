rhs_weap_sr25 = {
    "author": "Red Hammer Studios",
    "picture": "rhsusf|addons|rhsusf_inventoryicons|data|weapons|rhs_weap_sr25_ca.paa",
    "baseWeapon": "rhs_weap_sr25",
    "hiddenSelections": ["camo1","camo2","camo3","camo4","camo5","camo6"],
    "hiddenSelectionsTextures": ["rhsusf|addons|rhsusf_weapons2|sr25|data|reciever_co.paa","rhsusf|addons|rhsusf_weapons2|sr25|data|rail_co.paa","rhsusf|addons|rhsusf_weapons2|sr25|data|misc_co.paa","rhsusf|addons|rhsusf_weapons2|sr25|data|buttstock1_co.paa","rhsusf|addons|rhsusf_weapons2|sr25|data|buttstock2_co.paa","rhsusf|addons|rhsusf_weapons|M4|data|kacrailcover_co.paa"],
    "displayName": "Mk 11 Mod 0",
    "descriptionShort": "Sniper rifle<br/>Caliber: 7.62x51mm NATO",
    # Class: CfgWeapons|rhs_weap_sr25|Library [Indent level: 1],
    "Library": {
        "libTextDesc": "An SR 25 rifle manufactured by Knights Armament company"
    },
    "model": "rhsusf|addons|rhsusf_weapons2|sr25|SR25.p3d",
    "handAnim": ["OFP2_ManSkeleton","|rhsusf|addons|rhsusf_c_weapons|anims|rhs_hand_sr25.rtm"],
    "reloadAction": "RHS_GestureReloadSR25",
    "magazines": ["rhsusf_20Rnd_762x51_SR25_m118_special_Mag","rhsusf_20Rnd_762x51_SR25_mk316_special_Mag","rhsusf_20Rnd_762x51_SR25_m993_Mag","rhsusf_20Rnd_762x51_SR25_m62_Mag"],
    "magazineWell": ["CBA_762x51_AR10","CBA_762x51_AR10_L","CBA_762x51_AR10_XL"],
    "discreteDistance": [200,300,400,500,600],
    "discreteDistanceCameraPoint": ["eye","eye_300","eye_400","eye_500","eye_600"],
    "discreteDistanceInitIndex": 0,
    "maxZeroing": 1000,
    "weaponInfoType": "rhs_rscOptics_sr25",
    "dexterity": 1.53,
    "reloadTime": 2,
    # Recoil Class: recoil,
    # Class: CfgRecoils|recoil_ebr [Indent level: 0],
    "recoil": {
        "muzzleOuter": [0.4,1.5,0.6,0.4],
        "kickBack": [0.04,0.07],
        "temporary": 0.01,
        "muzzleInner": [0,0,0.1,0.1],
        "permanent": 0.1
    },
    # Class: CfgWeapons|rhs_weap_sr25|WeaponSlotsInfo [Indent level: 1],
    "WeaponSlotsInfo": {
        "mass": 94.82,
        # Class: CfgWeapons|rhs_weap_sr25|WeaponSlotsInfo|CowsSlot [Indent level: 2],
        "CowsSlot": {
            # Class: asdg_OpticRail1913_long|compatibleItems [Indent level: 0],

            "compatibleItems": {

                "rhsusf_acc_premier_anpvs27": 1,

                "rhsusf_acc_ACOG_anpvs27": 1,

                "rhsusf_acc_T1_low_fwd": 1,

                "rhsusf_acc_T1_low_fwd_ak": 1,

                "rhsusf_acc_RM05_fwd": 1,

                "rhsusf_acc_RM05_fwd_ak": 1,

                "rhsusf_acc_mrds_fwd": 1,

                "rhsusf_acc_mrds_fwd_ak": 1,

                "rhsusf_acc_mrds_fwd_c": 1,

                "rhsusf_acc_mrds_fwd_c_ak": 1,

                "rhs_acc_rakursPM": 1,

                "rhs_acc_dh520x56": 1,

                "rhs_acc_ekp8_18": 1,

                "rhs_acc_ekp8_18b": 1,

                "rhs_acc_ekp8_18c": 1,

                "rhs_acc_ekp8_18d": 1,

                "rhs_acc_1p87": 1,

                "rhs_acc_okp7_picatinny": 1,

                "optic_Nightstalker": 1,

                "optic_tws": 1,

                "optic_tws_mg": 1,

                "optic_NVS": 1,

                "optic_SOS": 1,

                "optic_SOS_khk_F": 1,

                "optic_MRCO": 1,

                "optic_Arco": 1,

                "optic_Arco_ghex_F": 1,

                "optic_Arco_blk_F": 1,

                "optic_aco": 1,

                "optic_ACO_grn": 1,

                "optic_aco_smg": 1,

                "optic_ACO_grn_smg": 1,

                "optic_hamr": 1,

                "optic_Hamr_khk_F": 1,

                "optic_Holosight": 1,

                "optic_Holosight_smg": 1,

                "optic_Holosight_blk_F": 1,

                "optic_Holosight_khk_F": 1,

                "optic_Holosight_smg_blk_F": 1,

                "optic_DMS": 1,

                "optic_DMS_ghex_F": 1,

                "optic_LRPS": 1,

                "optic_LRPS_ghex_F": 1,

                "optic_LRPS_tna_F": 1,

                "optic_AMS": 1,

                "optic_AMS_khk": 1,

                "optic_AMS_snd": 1,

                "optic_KHS_blk": 1,

                "optic_KHS_hex": 1,

                "optic_KHS_old": 1,

                "optic_KHS_tan": 1,

                "optic_ERCO_blk_F": 1,

                "optic_ERCO_khk_F": 1,

                "optic_ERCO_snd_F": 1,

                "rhsusf_acc_LEUPOLDMK4": 1,

                "rhsusf_acc_LEUPOLDMK4_d": 1,

                "rhsusf_acc_LEUPOLDMK4_wd": 1,

                "rhsusf_acc_LEUPOLDMK4_2": 1,

                "rhsusf_acc_LEUPOLDMK4_2_MRDS": 1,

                "rhsusf_acc_LEUPOLDMK4_2_d": 1,

                "rhsusf_acc_premier": 1,

                "rhsusf_acc_premier_mrds": 1,

                "rhsusf_acc_premier_low": 1,

                "rhsusf_acc_M8541": 1,

                "rhsusf_acc_M8541_mrds": 1,

                "rhsusf_acc_M8541_low": 1,

                "rhsusf_acc_M8541_low_d": 1,

                "rhsusf_acc_M8541_low_wd": 1,

                "rhsusf_acc_EOTECH": 1,

                "rhsusf_acc_eotech_552": 1,

                "rhsusf_acc_eotech_552_d": 1,

                "rhsusf_acc_eotech_552_wd": 1,

                "rhsusf_acc_eotech_xps3": 1,

                "rhsusf_acc_g33_xps3": 1,

                "rhsusf_acc_g33_xps3_flip": 1,

                "rhsusf_acc_g33_xps3_tan": 1,

                "rhsusf_acc_g33_xps3_tan_flip": 1,

                "rhsusf_acc_g33_t1": 1,

                "rhsusf_acc_g33_t1_flip": 1,

                "rhsusf_acc_compm4": 1,

                "rhsusf_acc_T1_high": 1,

                "rhsusf_acc_T1_low": 1,

                "rhsusf_acc_RX01": 1,

                "rhsusf_acc_RX01_NoFilter": 1,

                "rhsusf_acc_RX01_tan": 1,

                "rhsusf_acc_RX01_NoFilter_tan": 1,

                "rhsusf_acc_RM05": 1,

                "rhsusf_acc_mrds": 1,

                "rhsusf_acc_mrds_c": 1,

                "rhsusf_acc_ACOG": 1,

                "rhsusf_acc_ACOG2": 1,

                "rhsusf_acc_ACOG3": 1,

                "rhsusf_acc_ACOG_wd": 1,

                "rhsusf_acc_ACOG_d": 1,

                "rhsusf_acc_ACOG_sa": 1,

                "rhsusf_acc_ACOG_USMC": 1,

                "rhsusf_acc_ACOG2_USMC": 1,

                "rhsusf_acc_ACOG3_USMC": 1,

                "rhsusf_acc_ACOG_RMR": 1,

                "rhsusf_acc_ACOG_PIP": 1,

                "rhsusf_acc_ACOG2_pip": 1,

                "rhsusf_acc_ACOG3_pip": 1,

                "rhsusf_acc_ACOG_wd_pip": 1,

                "rhsusf_acc_ACOG_d_pip": 1,

                "rhsusf_acc_ACOG_sa_pip": 1,

                "rhsusf_acc_ACOG_USMC_pip": 1,

                "rhsusf_acc_ACOG2_USMC_pip": 1,

                "rhsusf_acc_ACOG3_USMC_pip": 1,

                "rhsusf_acc_ACOG_RMR_PIP": 1,

                "rhsusf_acc_ACOG_3d": 1,

                "rhsusf_acc_ACOG2_3d": 1,

                "rhsusf_acc_ACOG3_3d": 1,

                "rhsusf_acc_ACOG_wd_3d": 1,

                "rhsusf_acc_ACOG_d_3d": 1,

                "rhsusf_acc_ACOG_sa_3d": 1,

                "rhsusf_acc_ACOG_USMC_3d": 1,

                "rhsusf_acc_ACOG2_USMC_3d": 1,

                "rhsusf_acc_ACOG3_USMC_3d": 1,

                "rhsusf_acc_ACOG_RMR_3d": 1,

                "rhsusf_acc_ELCAN": 1,

                "rhsusf_acc_ELCAN_ard": 1,

                "rhsusf_acc_ELCAN_3d": 1,

                "rhsusf_acc_ELCAN_ard_3d": 1,

                "rhsusf_acc_ELCAN_PIP": 1,

                "rhsusf_acc_ELCAN_ard_PIP": 1,

                "rhsusf_acc_su230": 1,

                "rhsusf_acc_su230_mrds": 1,

                "rhsusf_acc_su230a": 1,

                "rhsusf_acc_su230a_mrds": 1,

                "rhsusf_acc_su230_c": 1,

                "rhsusf_acc_su230_mrds_c": 1,

                "rhsusf_acc_su230a_c": 1,

                "rhsusf_acc_su230a_mrds_c": 1,

                "rhsusf_acc_su230_3d": 1,

                "rhsusf_acc_su230_mrds_3d": 1,

                "rhsusf_acc_su230a_3d": 1,

                "rhsusf_acc_su230a_mrds_3d": 1,

                "rhsusf_acc_su230_c_3d": 1,

                "rhsusf_acc_su230_mrds_c_3d": 1,

                "rhsusf_acc_su230a_c_3d": 1,

                "rhsusf_acc_su230a_mrds_c_3d": 1,

                "rhsusf_acc_SpecterDR": 1,

                "rhsusf_acc_SpecterDR_3d": 1,

                "rhsusf_acc_SpecterDR_A": 1,

                "rhsusf_acc_SpecterDR_A_3d": 1,

                "rhsusf_acc_SpecterDR_CX": 1,

                "rhsusf_acc_SpecterDR_CX_3D": 1,

                "rhsusf_acc_SpecterDR_pvs27": 1,

                "rhsusf_acc_SpecterDR_D": 1,

                "rhsusf_acc_SpecterDR_OD": 1,

                "rhsusf_acc_SpecterDR_D_3D": 1,

                "rhsusf_acc_SpecterDR_OD_3D": 1,

                "rhsusf_acc_anpvs27": 1,

                "rhsusf_acc_anpas13gv1": 1,

                "rhsusf_acc_M2A1": 1,

                "rhsusf_acc_ACOG_MDO": 1,

                "rhsgref_acc_RX01_camo": 1,

                "rhsgref_acc_RX01_NoFilter_camo": 1
            },
            "linkProxy": "A3|data_f|proxies|weapon_slots|TOP",
            "displayName": "Optics Slot"
        },
        # Class: CfgWeapons|rhs_weap_sr25|WeaponSlotsInfo|PointerSlot [Indent level: 2],
        "PointerSlot": {
            "iconPosition": [0,0],
            "iconScale": 1,
            "iconPicture": "A3|Weapons_F|Data|clear_empty.paa",
            "iconPinPoint": "Left",
            # Class: rhs_western_rifle_laser_slot|compatibleItems [Indent level: 0],
            "compatibleItems": {
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
                "rhs_acc_2dpZenit_ris": 1,
                "rhs_acc_perst1ik_ris": 1,
                "rhs_acc_perst3": 1,
                "acc_flashlight": 1,
                "acc_pointer_IR": 1,
                "rhsusf_acc_wmx": 1,
                "rhsusf_acc_wmx_bk": 1,
                "rhsusf_acc_M952V": 1,
                "rhsusf_acc_anpeq15A": 1,
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
            "linkProxy": "a3|data_f|proxies|weapon_slots|side",
            "displayName": "Pointer Slot"
        },
        # Class: CfgWeapons|rhs_weap_sr25|WeaponSlotsInfo|MuzzleSlot [Indent level: 2],
        "MuzzleSlot": {
            "linkProxy": "A3|data_f|proxies|weapon_slots|MUZZLE",
            "compatibleItems": ["rhsusf_acc_sr25S","rhsusf_acc_SR25S_wd","rhsusf_acc_SR25S_d"],
            "access": 1,
            "scope": 0,
            "iconPosition": [0,0],
            "iconScale": 0,
            "iconPicture": "",
            "iconPinpoint": "Center"
        },
        # Class: CfgWeapons|rhs_weap_sr25|WeaponSlotsInfo|UnderBarrelSlot [Indent level: 2],
        "UnderBarrelSlot": {
            "iconPosition": [0,0],
            "iconScale": 1,
            "iconPicture": "A3|Weapons_F|Data|clear_empty.paa",
            "iconPinPoint": "Left",
            # Class: rhs_western_rifle_underbarrel_slot|compatibleItems [Indent level: 0],
            "compatibleItems": {
                "rhs_acc_harris_swivel": 1,
                "bipod_01_F_snd": 1,
                "bipod_01_F_blk": 1,
                "bipod_01_F_mtp": 1,
                "bipod_02_F_blk": 1,
                "bipod_02_F_tan": 1,
                "bipod_02_F_hex": 1,
                "bipod_03_F_blk": 1,
                "bipod_03_F_oli": 1,
                "bipod_01_F_khk": 1,
                "rhsusf_acc_harris_bipod": 1
            },
            "linkProxy": "a3|data_f_mark|Proxies|Weapon_Slots|UNDERBARREL"
        },
        "allowedSlots": [901]
    },
    # Class: CfgWeapons|rhs_weap_sr25|Single [Indent level: 1],
    "Single": {
        "reloadTime": 0.096,
        "dispersion": 0.00028,
        "minRange": 2,
        "minRangeProbab": 0.3,
        "midRange": 350,
        "midRangeProbab": 0.7,
        "maxRange": 500,
        "maxRangeProbab": 0.05,
        "displayName": "",
        # Class: CfgWeapons|rhs_weap_sr25|Single|StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSUSF_m16_Closure_SoundSet","RHSUSF_m14_Shot_SoundSet","RHSUSF_mmg1_Tail_SoundSet"]
        },
        # Class: CfgWeapons|rhs_weap_sr25|Single|SilencedSound [Indent level: 2],
        "SilencedSound": {
            "soundSetShot": ["RHSUSF_m16_Closure_SoundSet","RHSUSF_m14_ShotSD_SoundSet","RHSUSF_Rifle1_SD_Tail_SoundSet"]
        },
        "multiplier": 1,
        "burst": 1,
        "burstRangeMax": -1,
        "sound": ["",10,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": [],
        "soundLoop": [],
        "soundContinuous": 0,
        "weaponSoundEffect": "",
        "ffCount": 1,
        "ffMagnitude": 0.5,
        "ffFrequency": 11,
        "flash": "gunfire",
        "flashSize": 0.1,
        "autoFire": 0,
        "useAction": 0,
        "useActionTitle": "",
        "showToPlayer": 1,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "canShootInWater": 0,
        "sounds": ["StandardSound","SilencedSound"],
        "textureType": "semi",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "aiDispersionCoefY": 1.7,
        "aiDispersionCoefX": 1.4,
        "soundBurst": 0,
        "requiredOpticType": -1,
        "aiRateOfFire": 2,
        "aiRateOfFireDispersion": 1,
        "aiRateOfFireDistance": 500
    },
    # Class: CfgWeapons|rhs_weap_sr25|single_close_optics1 [Indent level: 1],
    "single_close_optics1": {
        "requiredOpticType": 1,
        "showToPlayer": 0,
        "minRange": 2,
        "minRangeProbab": 0.05,
        "midRange": 300,
        "midRangeProbab": 0.8,
        "maxRange": 500,
        "maxRangeProbab": 0.01,
        "aiRateOfFire": 2,
        "aiRateOfFireDistance": 300,
        "reloadTime": 0.096,
        "dispersion": 0.00028,
        "displayName": "",
        # Class: CfgWeapons|rhs_weap_sr25|Single|StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSUSF_m16_Closure_SoundSet","RHSUSF_m14_Shot_SoundSet","RHSUSF_mmg1_Tail_SoundSet"]
        },
        # Class: CfgWeapons|rhs_weap_sr25|Single|SilencedSound [Indent level: 2],
        "SilencedSound": {
            "soundSetShot": ["RHSUSF_m16_Closure_SoundSet","RHSUSF_m14_ShotSD_SoundSet","RHSUSF_Rifle1_SD_Tail_SoundSet"]
        },
        "multiplier": 1,
        "burst": 1,
        "burstRangeMax": -1,
        "sound": ["",10,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": [],
        "soundLoop": [],
        "soundContinuous": 0,
        "weaponSoundEffect": "",
        "ffCount": 1,
        "ffMagnitude": 0.5,
        "ffFrequency": 11,
        "flash": "gunfire",
        "flashSize": 0.1,
        "autoFire": 0,
        "useAction": 0,
        "useActionTitle": "",
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "canShootInWater": 0,
        "sounds": ["StandardSound","SilencedSound"],
        "textureType": "semi",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "aiDispersionCoefY": 1.7,
        "aiDispersionCoefX": 1.4,
        "soundBurst": 0,
        "aiRateOfFireDispersion": 1
    },
    # Class: CfgWeapons|rhs_weap_sr25|single_medium_optics1 [Indent level: 1],
    "single_medium_optics1": {
        "minRange": 300,
        "minRangeProbab": 0.05,
        "midRange": 500,
        "midRangeProbab": 0.7,
        "maxRange": 700,
        "maxRangeProbab": 0.05,
        "aiRateOfFire": 2,
        "aiRateOfFireDistance": 500,
        "requiredOpticType": 1,
        "showToPlayer": 0,
        "reloadTime": 0.096,
        "dispersion": 0.00028,
        "displayName": "",
        # Class: CfgWeapons|rhs_weap_sr25|Single|StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSUSF_m16_Closure_SoundSet","RHSUSF_m14_Shot_SoundSet","RHSUSF_mmg1_Tail_SoundSet"]
        },
        # Class: CfgWeapons|rhs_weap_sr25|Single|SilencedSound [Indent level: 2],
        "SilencedSound": {
            "soundSetShot": ["RHSUSF_m16_Closure_SoundSet","RHSUSF_m14_ShotSD_SoundSet","RHSUSF_Rifle1_SD_Tail_SoundSet"]
        },
        "multiplier": 1,
        "burst": 1,
        "burstRangeMax": -1,
        "sound": ["",10,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": [],
        "soundLoop": [],
        "soundContinuous": 0,
        "weaponSoundEffect": "",
        "ffCount": 1,
        "ffMagnitude": 0.5,
        "ffFrequency": 11,
        "flash": "gunfire",
        "flashSize": 0.1,
        "autoFire": 0,
        "useAction": 0,
        "useActionTitle": "",
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "canShootInWater": 0,
        "sounds": ["StandardSound","SilencedSound"],
        "textureType": "semi",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "aiDispersionCoefY": 1.7,
        "aiDispersionCoefX": 1.4,
        "soundBurst": 0,
        "aiRateOfFireDispersion": 1
    },
    # Class: CfgWeapons|rhs_weap_sr25|single_far_optics1 [Indent level: 1],
    "single_far_optics1": {
        "requiredOpticType": 2,
        "minRange": 300,
        "minRangeProbab": 0.05,
        "midRange": 600,
        "midRangeProbab": 0.4,
        "maxRange": 900,
        "maxRangeProbab": 0.05,
        "aiRateOfFire": 4,
        "aiRateOfFireDistance": 600,
        "showToPlayer": 0,
        "reloadTime": 0.096,
        "dispersion": 0.00028,
        "displayName": "",
        # Class: CfgWeapons|rhs_weap_sr25|Single|StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSUSF_m16_Closure_SoundSet","RHSUSF_m14_Shot_SoundSet","RHSUSF_mmg1_Tail_SoundSet"]
        },
        # Class: CfgWeapons|rhs_weap_sr25|Single|SilencedSound [Indent level: 2],
        "SilencedSound": {
            "soundSetShot": ["RHSUSF_m16_Closure_SoundSet","RHSUSF_m14_ShotSD_SoundSet","RHSUSF_Rifle1_SD_Tail_SoundSet"]
        },
        "multiplier": 1,
        "burst": 1,
        "burstRangeMax": -1,
        "sound": ["",10,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": [],
        "soundLoop": [],
        "soundContinuous": 0,
        "weaponSoundEffect": "",
        "ffCount": 1,
        "ffMagnitude": 0.5,
        "ffFrequency": 11,
        "flash": "gunfire",
        "flashSize": 0.1,
        "autoFire": 0,
        "useAction": 0,
        "useActionTitle": "",
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "canShootInWater": 0,
        "sounds": ["StandardSound","SilencedSound"],
        "textureType": "semi",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "aiDispersionCoefY": 1.7,
        "aiDispersionCoefX": 1.4,
        "soundBurst": 0,
        "aiRateOfFireDispersion": 1
    },
    "scope": 2,
    "cameraDir": "eye_look",
    "inertia": 0.7,
    "modes": ["Single","single_close_optics1","single_medium_optics1","single_far_optics1"],
    "dlc": "RHS_USAF",
    "htMin": 1,
    "htMax": 420,
    "afMax": 0,
    "mfMax": 0,
    "mFact": 1,
    "tBody": 100,
    "reloadMagazineSound": ["A3|Sounds_F_Mark|arsenal|weapons|LongRangeRifles|DMR_06_Mk14|DMR_06_reload",1,1,10],
    "magazineReloadSwitchPhase": 0.33,
    "opticsZoomMin": 0.275,
    "aimTransitionSpeed": 0.75,
    "muzzles": ["this","SAFE"],
    # Class: CfgWeapons|rhs_weap_m14_base|SAFE [Indent level: 1],
    "SAFE": {
        "discreteDistanceCameraPoint": ["eye"],
        "cameraDir": "eye_look",
        "magazines": [],
        "displayName": "SAFE",
        "descriptionShort": "SAFE",
        "showToPlayer": 0,
        "modes": ["Safe"],
        "discreteDistance": [0],
        "discreteDistanceInitIndex": 0,
        "drySound": ["A3|Sounds_F|arsenal|weapons|Rifles|MX|dry_Mx",0.562341,1,10],
        "changeFiremodeSound": ["A3|sounds_f|weapons|closure|firemode_changer_2",0.551189,1,5],
        # Class: CfgWeapons|RHSUSF_SAFE_BASE|Safe [Indent level: 1],
        "Safe": {
            "sounds": [],
            "displayName": "SAFE",
            "descriptionShort": "SAFE",
            "showToPlayer": 0,
            "minRange": 0,
            "minRangeProbab": 0.001,
            "midRange": 0.001,
            "midRangeProbab": 0.001,
            "maxRange": 0.001,
            "maxRangeProbab": 0.001,
            "multiplier": 1,
            "burst": 1,
            "burstRangeMax": -1,
            "dispersion": 0.0002,
            "sound": ["",10,1],
            "soundBegin": ["sound",1],
            "soundBeginWater": ["sound",1],
            "soundClosure": ["sound",1],
            "soundEnd": [],
            "soundLoop": [],
            "soundContinuous": 0,
            "weaponSoundEffect": "",
            "reloadTime": 0.1,
            "ffCount": 1,
            "ffMagnitude": 0.5,
            "ffFrequency": 11,
            "flash": "gunfire",
            "flashSize": 0.1,
            "autoFire": 0,
            "useAction": 0,
            "useActionTitle": "",
            "artilleryDispersion": 1,
            "artilleryCharge": 1,
            "canShootInWater": 0,
            "textureType": "semi",
            # Recoil Array: recoil,
            "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
            # Recoil Array: recoilProne,
            "recoilProne": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
            "aiDispersionCoefY": 1.7,
            "aiDispersionCoefX": 1.4,
            "soundBurst": 0,
            "requiredOpticType": -1,
            "aiRateOfFire": 2,
            "aiRateOfFireDispersion": 1,
            "aiRateOfFireDistance": 500
        },
        "scope": 0,
        "weaponInfoType": "RscWeaponZeroing",
        # Recoil Class: recoil,
        # Class: CfgRecoils|recoil_default [Indent level: 0],
        "recoil": {
            "muzzleOuter": [0.3,1,0.3,0.2],
            "muzzleInner": [0,0,0.1,0.1],
            "kickBack": [0.03,0.06],
            "permanent": 0.1,
            "temporary": 0.01
        },
        "deployedPivot": "bipod",
        # Class: CfgWeapons|Rifle_Base_F|GunParticles [Indent level: 1],
        "GunParticles": {
            # Class: CfgWeapons|Rifle_Base_F|GunParticles|FirstEffect [Indent level: 2],

            "FirstEffect": {

                "effectName": "RifleAssaultCloud",

                "positionName": "Usti hlavne",

                "directionName": "Konec hlavne"
            }
        },
        "htMin": 1,
        "htMax": 600,
        "afMax": 0,
        "mfMax": 0,
        "mFact": 1,
        "tBody": 100,
        "autoFire": 1,
        "reloadAction": "ReloadMagazine",
        "soundContinuous": 0,
        "optics": 0,
        "cursor": "arifle",
        "cursoraim": "CursorAim",
        "value": 4,
        "nameSound": "rifle",
        "reloadTime": 0.15,
        "modelOptics": "-",
        "sound": [],
        "opticsFlare": 0,
        "autoReload": 0,
        "aiDispersionCoefX": 6,
        "aiDispersionCoefY": 6,
        "opticsZoomMin": 0.25,
        "opticsZoomMax": 1.25,
        "opticsZoomInit": 0.75,
        "distanceZoomMin": 300,
        "distanceZoomMax": 300,
        "maxLeadSpeed": 23,
        "canLock": 0,
        "flash": "gunfire",
        "flashSize": 0.5,
        "dispersion": 0.00029,
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.06,0.01,0.01,0.1,0,-0.02,0.1,-0.01,0.01,0.05,0,0],
        "ffMagnitude": 0.5,
        "ffFrequency": 11,
        "ffCount": 3,
        "weaponPoolAvailable": 1,
        "maxZeroing": 1000,
        # Class: CfgWeapons|Rifle|WeaponSlotsInfo [Indent level: 1],
        "WeaponSlotsInfo": {
            "mass": 2,
            # Class: CfgWeapons|Rifle|WeaponSlotsInfo|MuzzleSlot [Indent level: 2],
            "MuzzleSlot": {
                "linkProxy": "A3|data_f|proxies|weapon_slots|MUZZLE",
                "displayName": "$str_a3_cfgweapons_abr_base_f_weaponslotsinfo_muzzleslot0",
                "compatibleItems": [],
                "iconPicture": "A3|Weapons_F|Data|UI|attachment_muzzle.paa",
                "iconPinpoint": "Center",
                "access": 1,
                "scope": 0,
                "iconPosition": [0,0],
                "iconScale": 0
            },
            # Class: CfgWeapons|Rifle|WeaponSlotsInfo|CowsSlot [Indent level: 2],
            "CowsSlot": {
                "compatibleItems": ["optic_Nightstalker","optic_tws","optic_tws_mg","optic_NVS","optic_DMS","optic_LRPS","optic_ams","optic_AMS_snd","optic_AMS_khk","optic_KHS_blk","optic_KHS_tan","optic_KHS_hex","optic_KHS_old","optic_SOS","optic_MRCO","optic_Arco","optic_aco","optic_ACO_grn","optic_aco_smg","optic_ACO_grn_smg","optic_hamr","optic_Holosight","optic_Holosight_smg","optic_Hamr_khk_F","optic_SOS_khk_F","optic_Arco_ghex_F","optic_Arco_blk_F","optic_DMS_ghex_F","optic_ERCO_blk_F","optic_ERCO_khk_F","optic_ERCO_snd_F","optic_LRPS_ghex_F","optic_LRPS_tna_F","optic_Holosight_blk_F","optic_Holosight_khk_F","optic_Holosight_smg_blk_F","optic_Holosight_smg_khk_F","optic_Arco_AK_blk_F","optic_Arco_AK_lush_F","optic_Arco_AK_arid_F","optic_DMS_weathered_F","optic_DMS_weathered_Kir_F","optic_Arco_lush_F","optic_Arco_arid_F","optic_Holosight_lush_F","optic_Holosight_arid_F"],
                "linkProxy": "A3|data_f|proxies|weapon_slots|TOP",
                "displayName": "Optics Slot",
                "iconPicture": "A3|Weapons_F|Data|UI|attachment_top.paa",
                "iconPinpoint": "Bottom",
                "access": 1,
                "scope": 0,
                "iconPosition": [0,0],
                "iconScale": 0
            },
            # Class: CfgWeapons|Rifle|WeaponSlotsInfo|PointerSlot [Indent level: 2],
            "PointerSlot": {
                "compatibleItems": ["acc_flashlight","acc_pointer_IR"],
                "iconPicture": "A3|Weapons_F|Data|UI|attachment_side.paa",
                "iconPinpoint": "Center",
                "linkProxy": "A3|data_f|proxies|weapon_slots|SIDE",
                "displayName": "Pointer Slot",
                "access": 1,
                "scope": 0,
                "iconPosition": [0,0],
                "iconScale": 0
            },
            "allowedSlots": [901]
        },
        "zeroingSound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|noises|rifle_zeroing_1.ogg",5,1,5],
        "type": 1,
        "dexterity": 1.7,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDistance": 500,
        "inertia": 0.5,
        "access": 3,
        "picture": "",
        "uiPicture": "",
        "ammo": "",
        "cursorSize": 1,
        "showAimCursorInternal": 1,
        "cursorAimOn": "",
        "laser": 0,
        "hiddenSelections": [],
        "hiddenSelectionsTextures": [],
        "hiddenUnderwaterSelections": [],
        "shownUnderwaterSelections": [],
        "hiddenUnderwaterSelectionsTextures": [],
        "simulation": "Weapon",
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazineReloadTime": 0,
        "magazineReloadSwitchPhase": 1,
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": ["sound",1],
        "soundLoop": ["sound",1],
        "weaponSoundEffect": "",
        "soundBurst": 1,
        "reloadSound": ["",1,1],
        "reloadMagazineSound": ["",1,1],
        "emptySound": ["",1,1],
        "soundBullet": ["emptySound",1],
        "initSpeed": 0,
        "ballisticsComputer": 0,
        "irDistance": 0,
        "irDotIntensity": 0.001,
        "lockAcquire": 1,
        "enableAttack": 1,
        "maxRecoilSway": 0.008,
        "swayDecaySpeed": 2,
        "model": "",
        "modelSpecial": "",
        "modelMagazine": "",
        "muzzlePos": "usti hlavne",
        "muzzleEnd": "konec hlavne",
        "irLaserPos": "laser pos",
        "irLaserEnd": "laser dir",
        "cartridgePos": "nabojnicestart",
        "cartridgeVel": "nabojniceend",
        "selectionFireAnim": "zasleh",
        "memoryPointCamera": "eye",
        "fireSpreadAngle": 3,
        "useModelOptics": 1,
        "opticsID": 0,
        "opticsPPEffects": [],
        "forceOptics": 0,
        "useAsBinocular": 0,
        "opticsDisablePeripherialVision": 0.67,
        "primary": 10,
        "showSwitchAction": 0,
        "showEmpty": 1,
        "canShootInWater": 0,
        "aiRateOfFireDispersion": 0,
        "fireLightDuration": 0.05,
        "fireLightIntensity": 0.2,
        "fireLightDiffuse": [0.937,0.631,0.259],
        "fireLightAmbient": [0,0,0],
        # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
        "Eventhandlers": {
        },
        "backgroundReload": 0,
        "muzzles": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockDelay": 0,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "minRange": 1,
        "minRangeProbab": 0.3,
        "midRange": 150,
        "midRangeProbab": 0.58,
        "maxRange": 500,
        "maxRangeProbab": 0.04,
        "handAnim": [],
        "lockingTargetSound": ["",0.000316228,2],
        "lockedTargetSound": ["",0.000316228,6],
        "detectRange": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "fireAnims": [],
        # Class: CfgWeapons|Default|Library [Indent level: 1],
        "Library": {
            "libTextDesc": ""
        },
        # Class: CfgWeapons|Default|GunFire [Indent level: 1],
        "GunFire": {
            "access": 0,
            "cloudletDuration": 0.2,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 0.2,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 0.5,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletFire",
            "cloudletColor": [1,1,1,0],
            "cloudletDensityCoef": -1,
            "interval": -0.01,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 4500,
            "deltaT": -3000,
            # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
            "Table": {
                # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3],

                "T0": {

                    "maxT": 0,

                    "color": [0.82,0.95,0.93,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
        "GunClouds": {
            "access": 0,
            "cloudletGrowUp": 0.05,
            "cloudletFadeIn": 0,
            "cloudletFadeOut": 0.1,
            "cloudletDuration": 0.05,
            "cloudletAlpha": 0.3,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "interval": -0.02,
            "size": 0.3,
            "sourceSize": 0.02,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "timeToLive": 0,
            "initT": 0,
            "deltaT": 0,
            # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
            "Table": {
                # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        "textureType": "default",
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons|rhs_weap_m14_base|GunParticles [Indent level: 1],
    "GunParticles": {
        # Class: CfgWeapons|rhs_weap_m14_base|GunParticles|SecondEffect [Indent level: 2],

        "SecondEffect": {

            "positionName": "Nabojnicestart",

            "directionName": "Nabojniceend",

            "effectName": "RifleAssaultCloud"
        },
        # Class: CfgWeapons|rhs_weap_m14_base|GunParticles|RHSUSF_BarrelRefract [Indent level: 2],
        "RHSUSF_BarrelRefract": {
            "positionName": "usti hlavne",
            "directionName": "usti hlavne up",
            "effectName": "RHSUSF_BarrelRefract"
        },
        # Class: CfgWeapons|Rifle_Base_F|GunParticles|FirstEffect [Indent level: 2],
        "FirstEffect": {
            "effectName": "RifleAssaultCloud",
            "positionName": "Usti hlavne",
            "directionName": "Konec hlavne"
        }
    },
    # Class: CfgWeapons|rhs_weap_m14_base|FullAuto [Indent level: 1],
    "FullAuto": {
        "reloadTime": 0.0827586,
        "dispersion": 0.00058,
        "minRange": 0,
        "minRangeProbab": 0.9,
        "midRange": 15,
        "midRangeProbab": 0.7,
        "maxRange": 30,
        "maxRangeProbab": 0.1,
        "aiRateOfFire": 1e-006,
        "sounds": ["Standardsound","SilencedSound"],
        # Class: CfgWeapons|rhs_weap_m14_base|FullAuto|StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSUSF_m14_Shot_SoundSet","RHSUSF_rifle2_Tail_SoundSet","RHSUSF_m14_stereoLayer_SoundSet"]
        },
        # Class: CfgWeapons|rhs_weap_m14_base|FullAuto|SilencedSound [Indent level: 2],
        "SilencedSound": {
            "soundSetShot": ["RHSUSF_sd_M4_Shot_SoundSet","RHSUSF_sd_Rifle1_Tail_SoundSet","RHSUSF_sd_M4_stereoLayer_SoundSet"]
        },
        "sound": ["",10,1],
        "soundEnd": ["sound",1],
        "soundContinuous": 0,
        "autoFire": 1,
        "displayName": "Full",
        "textureType": "fullAuto",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.06,0.0443316,0.0243916,0.06,0.0477255,0.0105084,0.06,0.0335835,0.0073344,0.06,0.0140372,0.003192,0.03,-0.0007206,-0.002688,0.03,-0.001765,-0.00282,0.03,-0.0018385,-0.001764,0.06,0,0],
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.06,0.0110829,0.0021522,0.06,0.0095451,0.0007506,0.06,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0],
        "aiDispersionCoefY": 3,
        "aiDispersionCoefX": 2,
        "soundBurst": 0,
        "multiplier": 1,
        "burst": 1,
        "burstRangeMax": -1,
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundLoop": [],
        "weaponSoundEffect": "",
        "ffCount": 1,
        "ffMagnitude": 0.5,
        "ffFrequency": 11,
        "flash": "gunfire",
        "flashSize": 0.1,
        "useAction": 0,
        "useActionTitle": "",
        "showToPlayer": 1,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "canShootInWater": 0,
        "requiredOpticType": -1,
        "aiRateOfFireDispersion": 1,
        "aiRateOfFireDistance": 500
    },
    "_generalMacro": "srifle_EBR_F",
    "UiPicture": "A3|weapons_f|data|UI|icon_regular_CA.paa",
    # Class: CfgWeapons|srifle_EBR_F|ItemInfo [Indent level: 1],
    "ItemInfo": {
        "priority": 1
    },
    "cursor": "srifle",
    "bullet1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|metal_1.ogg",2.0099,1,10],
    "bullet2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|metal_2.ogg",2.0099,1,10],
    "bullet3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|metal_3.ogg",2.0099,1,10],
    "bullet4": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|metal_4.ogg",2.0099,1,10],
    "bullet5": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|dirt_1.ogg",2.0099,1,10],
    "bullet6": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|dirt_2.ogg",2.0099,1,10],
    "bullet7": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|dirt_3.ogg",2.0099,1,10],
    "bullet8": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|dirt_4.ogg",2.0099,1,10],
    "bullet9": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|grass_1.ogg",2.0099,1,10],
    "bullet10": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|grass_2.ogg",2.0099,1,10],
    "bullet11": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|grass_3.ogg",2.0099,1,10],
    "bullet12": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|shells|medium|grass_4.ogg",2.0099,1,10],
    "soundBullet": ["bullet1",0.08,"bullet2",0.084,"bullet3",0.084,"bullet4",0.084,"bullet5",0.093,"bullet6",0.093,"bullet7",0.074,"bullet8",0.074,"bullet9",0.084,"bullet10",0.085,"bullet11",0.083,"bullet12",0.083],
    "distanceZoomMin": 300,
    "distanceZoomMax": 300,
    "drySound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_dry",0.630957,1,30],
    "changeFiremodeSound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_firemode",0.251189,1,5],
    # Class: CfgWeapons|EBR_base_F|fullauto_medium [Indent level: 1],
    "fullauto_medium": {
        "showToPlayer": 0,
        "burst": 3,
        "minRange": 2,
        "minRangeProbab": 0.5,
        "midRange": 50,
        "midRangeProbab": 0.7,
        "maxRange": 100,
        "maxRangeProbab": 0.05,
        "aiRateOfFire": 2,
        "sounds": ["StandardSound","SilencedSound"],
        # Class: CfgWeapons|EBR_base_F|FullAuto|BaseSoundModeType [Indent level: 2],
        "BaseSoundModeType": {
            "closure1": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_closure_01",0.562341,1,30],
            "closure2": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_closure_02",0.562341,1.2,30],
            "soundClosure": ["closure1",0.5,"closure2",0.5]
        },
        # Class: CfgWeapons|EBR_base_F|FullAuto|StandardSound [Indent level: 2],
        "StandardSound": {
            "begin1": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_short_01",3.98107,1,2000],
            "begin2": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_short_02",3.98107,1,2000],
            "begin3": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_short_03",3.98107,1,2000],
            "soundBegin": ["begin1",0.34,"begin2",0.33,"begin3",0.33],
            # Class: CfgWeapons|EBR_base_F|FullAuto|StandardSound|SoundTails [Indent level: 3],
            "SoundTails": {
                # Class: CfgWeapons|EBR_base_F|FullAuto|StandardSound|SoundTails|TailForest [Indent level: 4],

                "TailForest": {

                    "sound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_tail_forest",1,1,2000],

                    "frequency": 1,

                    "volume": "(1-interior/1.4)*forest"
                },
                # Class: CfgWeapons|EBR_base_F|FullAuto|StandardSound|SoundTails|TailHouses [Indent level: 4],
                "TailHouses": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_tail_houses",1,1,2000],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*houses"
                },
                # Class: CfgWeapons|EBR_base_F|FullAuto|StandardSound|SoundTails|TailInterior [Indent level: 4],
                "TailInterior": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_tail_interior",1.58489,1,2000],
                    "frequency": 1,
                    "volume": "interior"
                },
                # Class: CfgWeapons|EBR_base_F|FullAuto|StandardSound|SoundTails|TailMeadows [Indent level: 4],
                "TailMeadows": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_tail_meadows",1,1,2000],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*(meadows/2 max sea/2)"
                },
                # Class: CfgWeapons|EBR_base_F|FullAuto|StandardSound|SoundTails|TailTrees [Indent level: 4],
                "TailTrees": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_tail_trees",1,1,2000],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*trees"
                }
            },
            "soundSetShot": ["jsrs_mk18_shot_soundset","jsrs_7x62mm_reverb_soundset"],
            "closure1": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_closure_01",0.562341,1,30],
            "closure2": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_closure_02",0.562341,1.2,30],
            "soundClosure": ["closure1",0.5,"closure2",0.5]
        },
        # Class: CfgWeapons|EBR_base_F|FullAuto|SilencedSound [Indent level: 2],
        "SilencedSound": {
            "begin1": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|silencer_Mk18_short_01",1,1,600],
            "begin2": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|silencer_Mk18_short_02",1,1,600],
            "begin3": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|silencer_Mk18_short_03",1,1,600],
            "soundBegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34],
            # Class: CfgWeapons|EBR_base_F|FullAuto|SilencedSound|SoundTails [Indent level: 3],
            "SoundTails": {
                # Class: CfgWeapons|EBR_base_F|FullAuto|SilencedSound|SoundTails|TailForest [Indent level: 4],

                "TailForest": {

                    "sound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|silencer_Mk18_tail_forest",1,1,600],

                    "frequency": 1,

                    "volume": "(1-interior/1.4)*forest"
                },
                # Class: CfgWeapons|EBR_base_F|FullAuto|SilencedSound|SoundTails|TailHouses [Indent level: 4],
                "TailHouses": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|silencer_Mk18_tail_houses",1,1,600],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*houses"
                },
                # Class: CfgWeapons|EBR_base_F|FullAuto|SilencedSound|SoundTails|TailInterior [Indent level: 4],
                "TailInterior": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|silencer_Mk18_tail_interior",1.99526,1,600],
                    "frequency": 1,
                    "volume": "interior"
                },
                # Class: CfgWeapons|EBR_base_F|FullAuto|SilencedSound|SoundTails|TailMeadows [Indent level: 4],
                "TailMeadows": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|silencer_Mk18_tail_meadows",1,1,600],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*(meadows/2 max sea/2)"
                },
                # Class: CfgWeapons|EBR_base_F|FullAuto|SilencedSound|SoundTails|TailTrees [Indent level: 4],
                "TailTrees": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|silencer_Mk18_tail_trees",1,1,600],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*trees"
                }
            },
            "soundsetshot": ["jsrs_mk18_shot_silenced_soundset","jsrs_7x62mm_sd_reverb_soundset"],
            "closure1": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_closure_01",0.562341,1,30],
            "closure2": ["A3|Sounds_F|arsenal|weapons|LongRangeRifles|Mk18|Mk18_closure_02",0.562341,1.2,30],
            "soundClosure": ["closure1",0.5,"closure2",0.5]
        },
        "reloadTime": 0.085,
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0443316,0.0459136,0.03,0.0477255,0.0180144,0.03,0.0335835,0.012224,0.03,0.0140372,0.005016,0.03,-0.0007206,-0.003456,0.03,-0.001765,-0.003948,0.03,-0.0011031,-0.00294,0.03,-0.0009414,-0.0015,0.06,-0.0006618,-0.000352,0.06,0,0],
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.06,0.0110829,0.0086088,0.06,0.0159085,0.0035028,0.06,0.007902,0.0027504,0.06,0.0022164,0.001254,0.06,0,0],
        "dispersion": 0.00073,
        "sound": ["",10,1],
        "soundEnd": ["sound",1],
        "soundContinuous": 0,
        "autoFire": 1,
        "displayName": "Full",
        "textureType": "fullAuto",
        "aiDispersionCoefY": 3,
        "aiDispersionCoefX": 2,
        "soundBurst": 0,
        "multiplier": 1,
        "burstRangeMax": -1,
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundLoop": [],
        "weaponSoundEffect": "",
        "ffCount": 1,
        "ffMagnitude": 0.5,
        "ffFrequency": 11,
        "flash": "gunfire",
        "flashSize": 0.1,
        "useAction": 0,
        "useActionTitle": "",
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "canShootInWater": 0,
        "requiredOpticType": -1,
        "aiRateOfFireDispersion": 1,
        "aiRateOfFireDistance": 500
    },
    "aiDispersionCoefY": 3,
    "aiDispersionCoefX": 2,
    "deployedPivot": "bipod",
    "autoFire": 1,
    "soundContinuous": 0,
    "optics": 0,
    "cursoraim": "CursorAim",
    "value": 4,
    "nameSound": "rifle",
    "modelOptics": "-",
    "sound": [],
    "opticsFlare": 0,
    "autoReload": 0,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "maxLeadSpeed": 23,
    "canLock": 0,
    "flash": "gunfire",
    "flashSize": 0.5,
    "dispersion": 0.00029,
    # Recoil Array: recoilProne,
    "recoilProne": [0,0,0,0.06,0.01,0.01,0.1,0,-0.02,0.1,-0.01,0.01,0.05,0,0],
    "ffMagnitude": 0.5,
    "ffFrequency": 11,
    "ffCount": 3,
    "weaponPoolAvailable": 1,
    "zeroingSound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|noises|rifle_zeroing_1.ogg",5,1,5],
    "type": 1,
    "aiRateOfFire": 0.5,
    "aiRateOfFireDistance": 500,
    "access": 3,
    "ammo": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "reloadSound": ["",1,1],
    "emptySound": ["",1,1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "lockAcquire": 1,
    "enableAttack": 1,
    "maxRecoilSway": 0.008,
    "swayDecaySpeed": 2,
    "modelSpecial": "",
    "modelMagazine": "",
    "muzzlePos": "usti hlavne",
    "muzzleEnd": "konec hlavne",
    "irLaserPos": "laser pos",
    "irLaserEnd": "laser dir",
    "cartridgePos": "nabojnicestart",
    "cartridgeVel": "nabojniceend",
    "selectionFireAnim": "zasleh",
    "memoryPointCamera": "eye",
    "fireSpreadAngle": 3,
    "useModelOptics": 1,
    "opticsID": 0,
    "opticsPPEffects": [],
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons|Default|Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "useAction": 0,
    "useActionTitle": "",
    "canDrop": 1,
    "weaponLockDelay": 0,
    "weaponLockSystem": 0,
    "cmImmunity": 1,
    "weight": 0,
    "minRange": 1,
    "minRangeProbab": 0.3,
    "midRange": 150,
    "midRangeProbab": 0.58,
    "maxRange": 500,
    "maxRangeProbab": 0.04,
    "lockingTargetSound": ["",0.000316228,2],
    "lockedTargetSound": ["",0.000316228,6],
    "detectRange": 0,
    "artilleryDispersion": 1,
    "artilleryCharge": 1,
    "fireAnims": [],
    # Class: CfgWeapons|Default|GunFire [Indent level: 1],
    "GunFire": {
        "access": 0,
        "cloudletDuration": 0.2,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 1,
        "cloudletGrowUp": 0.2,
        "cloudletFadeIn": 0.01,
        "cloudletFadeOut": 0.5,
        "cloudletAccY": 0,
        "cloudletMinYSpeed": -100,
        "cloudletMaxYSpeed": 100,
        "cloudletShape": "cloudletFire",
        "cloudletColor": [1,1,1,0],
        "cloudletDensityCoef": -1,
        "interval": -0.01,
        "size": 3,
        "sourceSize": 0.5,
        "timeToLive": 0,
        "initT": 4500,
        "deltaT": -3000,
        # Class: CfgWeapons|Default|GunFire|Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons|Default|GunFire|Table|T0 [Indent level: 3],

            "T0": {

                "maxT": 0,

                "color": [0.82,0.95,0.93,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T1 [Indent level: 3],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T2 [Indent level: 3],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T3 [Indent level: 3],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T4 [Indent level: 3],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T5 [Indent level: 3],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T6 [Indent level: 3],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T7 [Indent level: 3],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T8 [Indent level: 3],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T9 [Indent level: 3],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T10 [Indent level: 3],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T11 [Indent level: 3],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T12 [Indent level: 3],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T13 [Indent level: 3],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T14 [Indent level: 3],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T15 [Indent level: 3],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T16 [Indent level: 3],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T17 [Indent level: 3],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T18 [Indent level: 3],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T19 [Indent level: 3],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T20 [Indent level: 3],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T21 [Indent level: 3],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: CfgWeapons|Default|GunFire|Table|T22 [Indent level: 3],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgWeapons|Default|GunClouds [Indent level: 1],
    "GunClouds": {
        "access": 0,
        "cloudletGrowUp": 0.05,
        "cloudletFadeIn": 0,
        "cloudletFadeOut": 0.1,
        "cloudletDuration": 0.05,
        "cloudletAlpha": 0.3,
        "cloudletAccY": 0,
        "cloudletMinYSpeed": -100,
        "cloudletMaxYSpeed": 100,
        "interval": -0.02,
        "size": 0.3,
        "sourceSize": 0.02,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletShape": "cloudletClouds",
        "cloudletColor": [1,1,1,0],
        "timeToLive": 0,
        "initT": 0,
        "deltaT": 0,
        # Class: CfgWeapons|Default|GunClouds|Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons|Default|GunClouds|Table|T0 [Indent level: 3],

            "T0": {

                "maxT": 0,

                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
}