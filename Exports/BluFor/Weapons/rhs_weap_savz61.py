rhs_weap_savz61 = {
    "author": "Red Hammer Studios",
    "picture": "rhsgref|addons|rhsgref_inventoryicons|data|weapons|rhs_weap_savz61_ca.paa",
    "dlc": "RHS_GREF",
    "displayName": "Sa vz. 61",
    "scope": 2,
    "weaponInfoType": "rhs_rscOptics_vz61",
    "rhs_fold": "rhs_weap_savz61_folded",
    "magazines": ["rhsgref_20rnd_765x17_vz61","rhsgref_10rnd_765x17_vz61"],
    "magazineWell": ["CBA_32ACP_Vz61"],
    # Class: CfgWeapons\rhs_weap_savz61\Library [Indent level: 1],
    "Library": {
        "libTextDesc": "The Škorpion vz. 61 is a Czechoslovak 7.65 mm machine pistol developed in 1959 by Miroslav Rybář (1924–1970) and produced under the official designation Samopal vzor 61 by the Česká zbrojovka arms factory in Uherský Brod from 1961 to 1979."
    },
    "model": "rhsgref|addons|rhsgref_weapons|savz61|rhs_savz61",
    "reloadAction": "GestureReloadSMG_02",
    "maxRecoilSway": 0.0125,
    "swayDecaySpeed": 1.25,
    # Class: CfgWeapons\rhs_weap_savz61\GunParticles [Indent level: 1],
    "GunParticles": {
        # Class: CfgWeapons\rhs_weap_savz61\GunParticles\FirstEffect [Indent level: 2]
        "FirstEffect": {
            "effectName": "PistolCloud",
            "positionName": "Usti hlavne",
            "directionName": "Konec hlavne"
        },
        # Class: CfgWeapons\rhs_weap_savz61\GunParticles\SecondEffect [Indent level: 2],
        "SecondEffect": {
            "positionName": "Nabojnicestart",
            "directionName": "Nabojniceend",
            "effectName": "CaselessAmmoCloud"
        }
    },
    # Class: CfgWeapons\rhs_weap_savz61\WeaponSlotsInfo [Indent level: 1],
    "WeaponSlotsInfo": {
        "mass": 28.16,
        "allowedSlots": [901],
        # Class: CfgWeapons\rhs_weap_savz61\WeaponSlotsInfo\MuzzleSlot [Indent level: 2],
        "MuzzleSlot": {
            "linkProxy": "A3|data_f|proxies|weapon_slots|MUZZLE",
            "compatibleItems": [],
            "iconPosition": [0,0.45],
            "iconScale": 0.2,
            "iconPicture": "A3|Weapons_F|Data|UI|attachment_muzzle.paa",
            "iconPinpoint": "Center",
            "displayName": "$str_a3_cfgweapons_abr_base_f_weaponslotsinfo_muzzleslot0",
            "access": 1,
            "scope": 0
        },
        # Class: CfgWeapons\rhs_weap_savz61\WeaponSlotsInfo\CowsSlot [Indent level: 2],
        "CowsSlot": {
            "iconPosition": [0.5,0.35],
            "iconScale": 0.2,
            "compatibleItems": [],
            "linkProxy": "A3|data_f|proxies|weapon_slots|TOP",
            "displayName": "Optics Slot",
            "iconPicture": "A3|Weapons_F|Data|UI|attachment_top.paa",
            "iconPinpoint": "Bottom",
            "access": 1,
            "scope": 0
        },
        # Class: CfgWeapons\rhs_weap_savz61\WeaponSlotsInfo\PointerSlot [Indent level: 2],
        "PointerSlot": {
        }
    },
    "opticsZoomMin": 0.375,
    "opticsZoomMax": 1.1,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 300,
    "distanceZoomMax": 300,
    "descriptionShort": "Sub-machine gun <br/>Caliber: 7.65x17 mm",
    "handAnim": ["OFP2_ManSkeleton","|rhsgref|addons|rhsgref_c_weapons|anims|rhs_hand_savz61.rtm"],
    "selectionfireanim": "zasleh",
    "discreteDistance": [75,150],
    "modes": ["Single","FullAuto"],
    # Class: CfgWeapons\rhs_weap_savz61\Single [Indent level: 1],
    "Single": {
        "reloadTime": 0.075,
        "dispersion": 0.0005,
        "minRange": 2,
        "minRangeProbab": 0.3,
        "midRange": 200,
        "midRangeProbab": 0.7,
        "maxRange": 350,
        "maxRangeProbab": 0.05,
        "aiRateOfFire": 2,
        "aiRateOfFireDistance": 500,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_savz61\Single\StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSGREF_scorp_Shot_SoundSet","RHSGREF_pistol1_Tail_SoundSet"]
        },
        # Class: CfgWeapons\SMG_01_Base\Single\BaseSoundModeType [Indent level: 2],
        "BaseSoundModeType": {
            "closure1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_01",0.562341,1,10],
            "closure2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_02",0.562341,1.1,10],
            "soundClosure": ["closure1",0.5,"closure2",0.5]
        },
        # Class: CfgWeapons\SMG_01_Base\Single\SilencedSound [Indent level: 2],
        "SilencedSound": {
            "begin1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_short_01",0.891251,1,400],
            "begin2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_short_02",0.891251,1,400],
            "begin3": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_short_03",0.891251,1,400],
            "soundBegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34],
            # Class: CfgWeapons\SMG_01_Base\Single\SilencedSound\SoundTails [Indent level: 3],
            "SoundTails": {
                # Class: CfgWeapons\SMG_01_Base\Single\SilencedSound\SoundTails\TailInterior [Indent level: 4]
                "TailInterior": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_tail_interior",1,1,400],
                    "frequency": 1,
                    "volume": "interior"
                },
                # Class: CfgWeapons\SMG_01_Base\Single\SilencedSound\SoundTails\TailTrees [Indent level: 4],
                "TailTrees": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_Tail_trees",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*trees"
                },
                # Class: CfgWeapons\SMG_01_Base\Single\SilencedSound\SoundTails\TailForest [Indent level: 4],
                "TailForest": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|silencer_Vermin_tail_forest",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*forest"
                },
                # Class: CfgWeapons\SMG_01_Base\Single\SilencedSound\SoundTails\TailMeadows [Indent level: 4],
                "TailMeadows": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_Tail_meadows",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*(meadows/2 max sea/2)"
                },
                # Class: CfgWeapons\SMG_01_Base\Single\SilencedSound\SoundTails\TailHouses [Indent level: 4],
                "TailHouses": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_Tail_houses",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*houses"
                }
            },
            "SoundSetShot": ["SMGVermin_silencerShot_SoundSet","SMGVermin_silencerTail_SoundSet","SMGVermin_silencerInteriorTail_SoundSet"],
            "closure1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_01",0.562341,1,10],
            "closure2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_02",0.562341,1.1,10],
            "soundClosure": ["closure1",0.5,"closure2",0.5]
        },
        "recoil": "recoil_single_SMG_01",
        "recoilProne": "recoil_single_prone_SMG_01",
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
        "aiDispersionCoefY": 1.7,
        "aiDispersionCoefX": 1.4,
        "soundBurst": 0,
        "requiredOpticType": -1,
        "aiRateOfFireDispersion": 1
    },
    # Class: CfgWeapons\rhs_weap_savz61\FullAuto [Indent level: 1],
    "FullAuto": {
        "reloadTime": 0.075,
        "dispersion": 0.0005,
        "minRange": 0,
        "minRangeProbab": 0.1,
        "midRange": 25,
        "midRangeProbab": 0.7,
        "maxRange": 70,
        "maxRangeProbab": 0.05,
        "aiRateOfFire": 0.2,
        "aiRateOfFireDistance": 50,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_savz61\FullAuto\StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHSGREF_scorp_Shot_SoundSet","RHSGREF_pistol1_Tail_SoundSet"]
        },
        # Class: CfgWeapons\SMG_01_Base\FullAuto\BaseSoundModeType [Indent level: 2],
        "BaseSoundModeType": {
            "closure1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_01",0.562341,1,10],
            "closure2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_02",0.562341,1.1,10],
            "soundClosure": ["closure1",0.5,"closure2",0.5]
        },
        # Class: CfgWeapons\SMG_01_Base\FullAuto\SilencedSound [Indent level: 2],
        "SilencedSound": {
            "begin1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_short_01",0.891251,1,400],
            "begin2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_short_02",0.891251,1,400],
            "begin3": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_short_03",0.891251,1,400],
            "soundBegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34],
            # Class: CfgWeapons\SMG_01_Base\FullAuto\SilencedSound\SoundTails [Indent level: 3],
            "SoundTails": {
                # Class: CfgWeapons\SMG_01_Base\FullAuto\SilencedSound\SoundTails\TailInterior [Indent level: 4]
                "TailInterior": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_tail_interior",1,1,400],
                    "frequency": 1,
                    "volume": "interior"
                },
                # Class: CfgWeapons\SMG_01_Base\FullAuto\SilencedSound\SoundTails\TailTrees [Indent level: 4],
                "TailTrees": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_Tail_trees",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*trees"
                },
                # Class: CfgWeapons\SMG_01_Base\FullAuto\SilencedSound\SoundTails\TailForest [Indent level: 4],
                "TailForest": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|silencer_Vermin_tail_forest",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*forest"
                },
                # Class: CfgWeapons\SMG_01_Base\FullAuto\SilencedSound\SoundTails\TailMeadows [Indent level: 4],
                "TailMeadows": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_Tail_meadows",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*(meadows/2 max sea/2)"
                },
                # Class: CfgWeapons\SMG_01_Base\FullAuto\SilencedSound\SoundTails\TailHouses [Indent level: 4],
                "TailHouses": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_Tail_houses",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*houses"
                }
            },
            "SoundSetShot": ["SMGVermin_silencerShot_SoundSet","SMGVermin_silencerTail_SoundSet","SMGVermin_silencerInteriorTail_SoundSet"],
            "closure1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_01",0.562341,1,10],
            "closure2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_02",0.562341,1.1,10],
            "soundClosure": ["closure1",0.5,"closure2",0.5]
        },
        "recoil": "recoil_auto_smg_01",
        "recoilProne": "recoil_auto_prone_smg_01",
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
        "aiRateOfFireDispersion": 1
    },
    "baseWeapon": "rhs_weap_savz61",
    "_generalMacro": "SMG_01_F",
    "inertia": 0.3,
    "aimTransitionSpeed": 1.4,
    "dexterity": 1.7,
    "initSpeed": 280,
    "UiPicture": "A3|Weapons_F|data|UI|icon_regular_CA.paa",
    "maxZeroing": 400,
    "recoil": "recoil_smg_01",
    "cursor": "smg",
    "discreteDistanceInitIndex": 0,
    "aiDispersionCoefY": 8,
    "aiDispersionCoefX": 9,
    "hiddenSelections": ["camo1","camo2","camo3"],
    "hiddenSelectionsTextures": ["|a3|weapons_f_beta|smgs|smg_01|data|smg_01_co.paa","|a3|weapons_f|data|vectoratt_co.paa","|a3|weapons_f|acc|data|battlesight_co.paa"],
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
    "soundBullet": ["bullet1",0.083,"bullet2",0.083,"bullet3",0.083,"bullet4",0.083,"bullet5",0.083,"bullet6",0.083,"bullet7",0.083,"bullet8",0.083,"bullet9",0.083,"bullet10",0.083,"bullet11",0.083,"bullet12",0.083],
    "drySound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Dry_Vermin",0.501187,1,10],
    "reloadMagazineSound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|reload_vermin",1,1,10],
    "changeFiremodeSound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|firemode_Vermin",0.251189,1,5],
    # Class: CfgWeapons\SMG_01_Base\Burst [Indent level: 1],
    "Burst": {
        "sounds": ["StandardSound","SilencedSound"],
        # Class: CfgWeapons\SMG_01_Base\Burst\BaseSoundModeType [Indent level: 2],
        "BaseSoundModeType": {
            "closure1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_01",0.562341,1,10],
            "closure2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_02",0.562341,1.1,10],
            "soundClosure": ["closure1",0.5,"closure2",0.5]
        },
        # Class: CfgWeapons\SMG_01_Base\Burst\StandardSound [Indent level: 2],
        "StandardSound": {
            "begin1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Vermin_short_01",2.81838,1,1200],
            "begin2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Vermin_short_02",2.81838,1,1200],
            "begin3": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Vermin_short_03",2.81838,1,1200],
            "soundBegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34],
            # Class: CfgWeapons\SMG_01_Base\Burst\StandardSound\SoundTails [Indent level: 3],
            "SoundTails": {
                # Class: CfgWeapons\SMG_01_Base\Burst\StandardSound\SoundTails\TailInterior [Indent level: 4]
                "TailInterior": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Vermin_tail_interior",1.58489,1,1200],
                    "frequency": 1,
                    "volume": "interior"
                },
                # Class: CfgWeapons\SMG_01_Base\Burst\StandardSound\SoundTails\TailTrees [Indent level: 4],
                "TailTrees": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Vermin_tail_trees",1,1,1200],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*trees"
                },
                # Class: CfgWeapons\SMG_01_Base\Burst\StandardSound\SoundTails\TailForest [Indent level: 4],
                "TailForest": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Vermin_tail_forest",1,1,1200],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*forest"
                },
                # Class: CfgWeapons\SMG_01_Base\Burst\StandardSound\SoundTails\TailMeadows [Indent level: 4],
                "TailMeadows": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Vermin_tail_meadows",1,1,1200],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*(meadows/2 max sea/2)"
                },
                # Class: CfgWeapons\SMG_01_Base\Burst\StandardSound\SoundTails\TailHouses [Indent level: 4],
                "TailHouses": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Vermin_tail_houses",1,1,1200],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*houses"
                }
            },
            "SoundSetShot": ["SMGVermin_Shot_SoundSet","SMGVermin_Tail_SoundSet","SMGVermin_InteriorTail_SoundSet"],
            "closure1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_01",0.562341,1,10],
            "closure2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_02",0.562341,1.1,10],
            "soundClosure": ["closure1",0.5,"closure2",0.5]
        },
        # Class: CfgWeapons\SMG_01_Base\Burst\SilencedSound [Indent level: 2],
        "SilencedSound": {
            "begin1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_short_01",0.891251,1,400],
            "begin2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_short_02",0.891251,1,400],
            "begin3": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_short_03",0.891251,1,400],
            "soundBegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34],
            # Class: CfgWeapons\SMG_01_Base\Burst\SilencedSound\SoundTails [Indent level: 3],
            "SoundTails": {
                # Class: CfgWeapons\SMG_01_Base\Burst\SilencedSound\SoundTails\TailInterior [Indent level: 4]
                "TailInterior": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_tail_interior",1,1,400],
                    "frequency": 1,
                    "volume": "interior"
                },
                # Class: CfgWeapons\SMG_01_Base\Burst\SilencedSound\SoundTails\TailTrees [Indent level: 4],
                "TailTrees": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_Tail_trees",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*trees"
                },
                # Class: CfgWeapons\SMG_01_Base\Burst\SilencedSound\SoundTails\TailForest [Indent level: 4],
                "TailForest": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|silencer_Vermin_tail_forest",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*forest"
                },
                # Class: CfgWeapons\SMG_01_Base\Burst\SilencedSound\SoundTails\TailMeadows [Indent level: 4],
                "TailMeadows": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_Tail_meadows",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*(meadows/2 max sea/2)"
                },
                # Class: CfgWeapons\SMG_01_Base\Burst\SilencedSound\SoundTails\TailHouses [Indent level: 4],
                "TailHouses": {
                    "sound": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|Silencer_Vermin_Tail_houses",1,1,400],
                    "frequency": 1,
                    "volume": "(1-interior/1.4)*houses"
                }
            },
            "SoundSetShot": ["SMGVermin_silencerShot_SoundSet","SMGVermin_silencerTail_SoundSet","SMGVermin_silencerInteriorTail_SoundSet"],
            "closure1": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_01",0.562341,1,10],
            "closure2": ["A3|Sounds_F|arsenal|weapons|SMG|Vermin|closure_Vermin_02",0.562341,1.1,10],
            "soundClosure": ["closure1",0.5,"closure2",0.5]
        },
        "soundBurst": 0,
        "textureType": "dual",
        "burst": 2,
        "reloadTime": 0.05,
        "dispersion": 0.00131,
        "recoil": "recoil_burst_smg_01",
        "recoilProne": "recoil_burst_prone_smg_01",
        "minRange": 2,
        "minRangeProbab": 0.3,
        "midRange": 50,
        "midRangeProbab": 0.7,
        "maxRange": 100,
        "maxRangeProbab": 0.05,
        "aiRateOfFire": 1,
        "aiRateOfFireDistance": 250,
        "sound": ["",10,1],
        "soundLoop": ["sound",1],
        "soundEnd": ["sound",1],
        "displayName": "Burst",
        "aiDispersionCoefY": 2.4,
        "aiDispersionCoefX": 1.9,
        "multiplier": 1,
        "burstRangeMax": -1,
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
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
        "requiredOpticType": -1,
        "aiRateOfFireDispersion": 1
    },
    "deployedPivot": "bipod",
    "htMin": 1,
    "htMax": 600,
    "afMax": 0,
    "mfMax": 0,
    "mFact": 1,
    "tBody": 100,
    "autoFire": 1,
    "soundContinuous": 0,
    "optics": 0,
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
    "recoilProne": "assaultRifleBase",
    "ffMagnitude": 0.5,
    "ffFrequency": 11,
    "ffCount": 3,
    "weaponPoolAvailable": 1,
    "zeroingSound": ["A3|Sounds_F|arsenal|sfx|shared|zeroing_knob_tick_metal",0.316228,1,5],
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
    # Class: CfgWeapons\Default\Eventhandlers [Indent level: 1],
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
    "lockingTargetSound": ["",0.000316228,2],
    "lockedTargetSound": ["",0.000316228,6],
    "detectRange": 0,
    "artilleryDispersion": 1,
    "artilleryCharge": 1,
    "fireAnims": [],
    # Class: CfgWeapons\Default\GunFire [Indent level: 1],
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
        # Class: CfgWeapons\Default\GunFire\Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons\Default\GunFire\Table\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T1 [Indent level: 3],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T2 [Indent level: 3],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T3 [Indent level: 3],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T4 [Indent level: 3],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T5 [Indent level: 3],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T6 [Indent level: 3],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T7 [Indent level: 3],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T8 [Indent level: 3],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T9 [Indent level: 3],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T10 [Indent level: 3],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T11 [Indent level: 3],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T12 [Indent level: 3],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T13 [Indent level: 3],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T14 [Indent level: 3],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T15 [Indent level: 3],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T16 [Indent level: 3],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T17 [Indent level: 3],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T18 [Indent level: 3],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T19 [Indent level: 3],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T20 [Indent level: 3],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T21 [Indent level: 3],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: CfgWeapons\Default\GunFire\Table\T22 [Indent level: 3],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgWeapons\Default\GunClouds [Indent level: 1],
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
        # Class: CfgWeapons\Default\GunClouds\Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons\Default\GunClouds\Table\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
}