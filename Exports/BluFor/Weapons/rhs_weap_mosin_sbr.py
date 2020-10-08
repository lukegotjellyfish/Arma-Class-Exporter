rhs_weap_mosin_sbr = {
    "author": "Red Hammer Studios",
    "picture": "rhsgref|addons|rhsgref_inventoryicons|data|weapons|rhs_weap_mosin_sbr_ca.paa",
    "model": "rhsgref|addons|rhsgref_weapons|m38|rhs_mosin_sbr.p3d",
    "handAnim": ["OFP2_ManSkeleton","|rhsgref|addons|rhsgref_c_weapons|anims|rhs_hand_mosin_sbr.rtm"],
    "initSpeed": -0.9,
    "inertia": 0.62,
    # Recoil Class: recoil,
    # Class: CfgRecoils|recoil_mmg_02 [Indent level: 0],
    "recoil": {
        "muzzleOuter": [0.5,1.5,0.6,0.4],
        "kickBack": [0.04,0.08],
        "temporary": 0.005,
        "muzzleInner": [0,0,0.1,0.1],
        "permanent": 0.1
    },
    "displayName": "Mosin SBR",
    "discreteDistance": [100],
    "discreteDistanceInitIndex": 0,
    "discreteDistanceCameraPoint": ["eye"],
    # Class: CfgWeapons|rhs_weap_mosin_sbr|Single [Indent level: 1],
    "Single": {
        "reloadTime": 1.6,
        "dispersion": 0.001635,
        "minRange": 2,
        "minRangeProbab": 0.3,
        "midRange": 250,
        "midRangeProbab": 0.7,
        "maxRange": 400,
        "maxRangeProbab": 0.04,
        "sounds": ["StandardSound","SilencedSound"],
        # Class: CfgWeapons|rhs_weap_mosin_sbr|Single|StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSGREF_sbr_Shot_SoundSet","RHSGREF_rifle2_Tail_SoundSet"]
        },
        # Class: CfgWeapons|rhs_weap_mosin_sbr|Single|SilencedSound [Indent level: 2],
        "SilencedSound": {
            "soundSetShot": ["RHSGREF_sd_sbr_Shot_SoundSet","RHSGREF_sd_mmg1_Tail_SoundSet"]
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
        "displayName": "Semi",
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
    # Class: CfgWeapons|rhs_weap_mosin_sbr|far_optic1 [Indent level: 1],
    "far_optic1": {
        "requiredOpticType": 1,
        "showToPlayer": 0,
        "minRange": 150,
        "minRangeProbab": 0.1,
        "midRange": 500,
        "midRangeProbab": 0.7,
        "maxRange": 1000,
        "maxRangeProbab": 0.3,
        "aiRateOfFire": 3,
        "aiRateOfFireDispersion": 3,
        "aiRateOfFireDistance": 700,
        "reloadTime": 1.6,
        "dispersion": 0.001635,
        "sounds": ["StandardSound","SilencedSound"],
        # Class: CfgWeapons|rhs_weap_mosin_sbr|Single|StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSGREF_sbr_Shot_SoundSet","RHSGREF_rifle2_Tail_SoundSet"]
        },
        # Class: CfgWeapons|rhs_weap_mosin_sbr|Single|SilencedSound [Indent level: 2],
        "SilencedSound": {
            "soundSetShot": ["RHSGREF_sd_sbr_Shot_SoundSet","RHSGREF_sd_mmg1_Tail_SoundSet"]
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
        "displayName": "Semi",
        "textureType": "semi",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "aiDispersionCoefY": 1.7,
        "aiDispersionCoefX": 1.4,
        "soundBurst": 0
    },
    # Class: CfgWeapons|rhs_weap_mosin_sbr|medium_optic2 [Indent level: 1],
    "medium_optic2": {
        "requiredOpticType": 2,
        "minRange": 250,
        "minRangeProbab": 0.1,
        "midRange": 750,
        "midRangeProbab": 0.7,
        "maxRange": 1000,
        "maxRangeProbab": 0.3,
        "aiRateOfFire": 4,
        "aiRateOfFireDispersion": 3,
        "aiRateOfFireDistance": 1000,
        "showToPlayer": 0,
        "reloadTime": 1.6,
        "dispersion": 0.001635,
        "sounds": ["StandardSound","SilencedSound"],
        # Class: CfgWeapons|rhs_weap_mosin_sbr|Single|StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSGREF_sbr_Shot_SoundSet","RHSGREF_rifle2_Tail_SoundSet"]
        },
        # Class: CfgWeapons|rhs_weap_mosin_sbr|Single|SilencedSound [Indent level: 2],
        "SilencedSound": {
            "soundSetShot": ["RHSGREF_sd_sbr_Shot_SoundSet","RHSGREF_sd_mmg1_Tail_SoundSet"]
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
        "displayName": "Semi",
        "textureType": "semi",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "aiDispersionCoefY": 1.7,
        "aiDispersionCoefX": 1.4,
        "soundBurst": 0
    },
    # Class: CfgWeapons|rhs_weap_mosin_sbr|far_optic2 [Indent level: 1],
    "far_optic2": {
        "minRange": 500,
        "minRangeProbab": 0.1,
        "midRange": 1050,
        "midRangeProbab": 0.7,
        "maxRange": 2000,
        "maxRangeProbab": 0.3,
        "aiRateOfFire": 5,
        "aiRateOfFireDispersion": 5,
        "aiRateOfFireDistance": 2000,
        "requiredOpticType": 2,
        "showToPlayer": 0,
        "reloadTime": 1.6,
        "dispersion": 0.001635,
        "sounds": ["StandardSound","SilencedSound"],
        # Class: CfgWeapons|rhs_weap_mosin_sbr|Single|StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSGREF_sbr_Shot_SoundSet","RHSGREF_rifle2_Tail_SoundSet"]
        },
        # Class: CfgWeapons|rhs_weap_mosin_sbr|Single|SilencedSound [Indent level: 2],
        "SilencedSound": {
            "soundSetShot": ["RHSGREF_sd_sbr_Shot_SoundSet","RHSGREF_sd_mmg1_Tail_SoundSet"]
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
        "displayName": "Semi",
        "textureType": "semi",
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.03,0.0110829,0.043044,0.03,0.0159085,0.0170136,0.03,0.0138285,0.0116128,0.06,0.0066492,0.004788,0.06,-0.0007206,-0.002688,0.06,-0.001765,-0.00282,0.06,-0.0018385,-0.001764,0.06,-0.0009414,-0.0005,0.06,0,0],
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "aiDispersionCoefY": 1.7,
        "aiDispersionCoefX": 1.4,
        "soundBurst": 0
    },
    "hiddenSelections": [""],
    # Class: CfgWeapons|rhs_weap_mosin_sbr|WeaponSlotsInfo [Indent level: 1],
    "WeaponSlotsInfo": {
        # Class: CfgWeapons|rhs_weap_mosin_sbr|WeaponSlotsInfo|CowsSlot [Indent level: 2],

        "CowsSlot": {

            "iconPosition": [0.45,0.25],

            "iconScale": 0.2,

            "iconPicture": "A3|Weapons_F|Data|UI|attachment_top.paa",

            "iconPinpoint": "Center",

            "linkProxy": "A3|data_f|proxies|weapon_slots|TOP",

            "displayName": "Optics Slot",

            # Class: asdg_OpticRail1913|compatibleItems [Indent level: 0],

            "compatibleItems": {

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
            }
        },
        # Class: CfgWeapons|rhs_weap_mosin_sbr|WeaponSlotsInfo|MuzzleSlot [Indent level: 2],
        "MuzzleSlot": {
            "iconPosition": [0,0.45],
            "iconScale": 0.2,
            "iconPicture": "A3|Weapons_F|Data|UI|attachment_muzzle.paa",
            "iconPinpoint": "Center",
            # Class: rhs_western_762rifle_muzzle_slot|compatibleItems [Indent level: 0],
            "compatibleItems": {
                "rhsusf_acc_aac_scarh_silencer": 1,
                "rhsusf_acc_aac_762sd_silencer": 1,
                "rhsusf_acc_aac_762sdn6_silencer": 1,
                "rhsgref_sdn6_suppressor": 1
            },
            "displayName": "$str_a3_cfgweapons_abr_base_f_weaponslotsinfo_muzzleslot0",
            "linkProxy": "A3|data_f|proxies|weapon_slots|MUZZLE"
        },
        "mass": 74.8,
        "icon": "rhsgref|addons|rhsgref_weapons|icons|w_m382_inv_ca.paa",
        # Class: CfgWeapons|rhs_weap_m38_Base_F|WeaponSlotsInfo|PointerSlot [Indent level: 2],
        "PointerSlot": {
            "iconPosition": [0,0.45],
            "iconScale": 0.2,
            "iconPicture": "A3|Weapons_F|Data|UI|attachment_muzzle.paa",
            "iconPinpoint": "Center"
        },
        # Class: CfgWeapons|rhs_weap_m38_Base_F|WeaponSlotsInfo|UnderBarrelSlot [Indent level: 2],
        "UnderBarrelSlot": {
            "iconPosition": [0,0.45],
            "iconScale": 0.2,
            "iconPicture": "A3|Weapons_F|Data|UI|attachment_muzzle.paa",
            "iconPinpoint": "Center"
        },
        "allowedSlots": [901]
    },
    "baseWeapon": "rhs_weap_mosin_sbr",
    "scopeArsenal": 2,
    "scope": 2,
    "hiddenSelectionsTextures": ["rhsgref|addons|rhsgref_weapons|m38|data|m38_2_co.paa"],
    "weaponInfoType": "rhs_mosin_handler",
    # Class: CfgWeapons|rhs_weap_m38|ItemInfo [Indent level: 1],
    "ItemInfo": {
        "priority": 1,
        "RMBhint": "m38",
        "onHoverText": "m38"
    },
    "dlc": "RHS_GREF",
    "magazines": ["rhsgref_5Rnd_762x54_m38"],
    "magazineWell": ["CBA_762x54R_Mosin"],
    # Class: CfgWeapons|rhs_weap_m38_Base_F|Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "optics": 0,
    "reloadAction": "RHS_GestureReloadM38",
    "maxRecoilSway": 0.0125,
    "swayDecaySpeed": 1.25,
    # Class: CfgWeapons|rhs_weap_m38_Base_F|GunParticles [Indent level: 1],
    "GunParticles": {
        # Class: CfgWeapons|rhs_weap_m38_Base_F|GunParticles|RHSUSF_BarrelRefract [Indent level: 2],

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
    "cameraDir": "eye_look",
    "opticsZoomMin": 0.275,
    "opticsZoomMax": 1.1,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 300,
    "distanceZoomMax": 300,
    "descriptionShort": "Bolt action Rifle<br/>Caliber: 7.62x54mm",
    "dexterity": 1.8,
    "drySound": ["A3|sounds_f|weapons|Other|dry_1",0.01,1],
    "reloadMagazineSound": ["|rhsgref|addons|rhsgref_weapons|kar98k|data|sounds|1903A1_reload_noscope",0.8,1,10],
    "bullet1": ["A3|sounds_f|weapons|shells|7_62|metal_762_01",0.630957,1,15],
    "bullet2": ["A3|sounds_f|weapons|shells|7_62|metal_762_02",0.630957,1,15],
    "bullet3": ["A3|sounds_f|weapons|shells|7_62|metal_762_03",0.630957,1,15],
    "bullet4": ["A3|sounds_f|weapons|shells|7_62|metal_762_04",0.630957,1,15],
    "bullet5": ["A3|sounds_f|weapons|shells|7_62|dirt_762_01",0.630957,1,15],
    "bullet6": ["A3|sounds_f|weapons|shells|7_62|dirt_762_02",0.630957,1,15],
    "bullet7": ["A3|sounds_f|weapons|shells|7_62|dirt_762_03",0.630957,1,15],
    "bullet8": ["A3|sounds_f|weapons|shells|7_62|dirt_762_04",0.630957,1,15],
    "bullet9": ["A3|sounds_f|weapons|shells|7_62|grass_762_01",0.630957,1,15],
    "bullet10": ["A3|sounds_f|weapons|shells|7_62|grass_762_02",0.630957,1,15],
    "bullet11": ["A3|sounds_f|weapons|shells|7_62|grass_762_03",0.630957,1,15],
    "bullet12": ["A3|sounds_f|weapons|shells|7_62|grass_762_04",0.630957,1,15],
    "soundBullet": ["bullet1",0.083,"bullet2",0.083,"bullet3",0.083,"bullet4",0.083,"bullet5",0.083,"bullet6",0.083,"bullet7",0.083,"bullet8",0.083,"bullet9",0.083,"bullet10",0.083,"bullet11",0.083,"bullet12",0.083],
    "modes": ["Single","far_optic1","medium_optic2","far_optic2"],
    "aiDispersionCoefY": 10,
    "aiDispersionCoefX": 8,
    # Class: CfgWeapons|rhs_weap_m38_Base_F|Eventhandlers [Indent level: 1],
    "Eventhandlers": {
        # Class: CfgWeapons|rhs_weap_m38_Base_F|Eventhandlers|RHS_BoltAction [Indent level: 2],

        "RHS_BoltAction": {

            "fired": "[_this select 0,_this select 1,_this select 1] call rhs_fnc_boltAction;"
        }
    },
    "rhs_boltActionSound": ["rhsgref|addons|rhsgref_weapons|kar98k|data|sounds|kar98k_bolt.wss",1.42,1,20],
    "rhs_boltActionAnim": "RHS_GestureRechamberM38",
    "deployedPivot": "bipod",
    "htMin": 1,
    "htMax": 600,
    "afMax": 0,
    "mfMax": 0,
    "mFact": 1,
    "tBody": 100,
    "autoFire": 1,
    "soundContinuous": 0,
    "cursor": "arifle",
    "cursoraim": "CursorAim",
    "value": 4,
    "nameSound": "rifle",
    "reloadTime": 0.15,
    "modelOptics": "-",
    "sound": [],
    "opticsFlare": 0,
    "autoReload": 0,
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
    "zeroingSound": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|weapons|noises|rifle_zeroing_1.ogg",5,1,5],
    "type": 1,
    "aiRateOfFire": 0.5,
    "aiRateOfFireDistance": 500,
    "access": 3,
    "uiPicture": "",
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
    "magazineReloadSwitchPhase": 1,
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "emptySound": ["",1,1],
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "lockAcquire": 1,
    "enableAttack": 1,
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
    "aimTransitionSpeed": 1,
}