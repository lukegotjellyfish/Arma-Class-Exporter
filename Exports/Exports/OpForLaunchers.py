"rhs_weap_igla": {
    "author": "Red Hammer Studios",
    "scope": 2,
    "displayname": "9K38 Igla",
    "descriptionShort": "Missile launcher<br/>Caliber: 72mm<br/>Type: Surface-to-air",
    "model": "rhsafrf\\addons\\rhs_weapons\\igla_bis\\igla",
    "picture": "rhsafrf\\addons\\rhs_weapons\\icons\\w_igla_ca.paa",
    "handanim": ["OFP2_ManSkeleton","\\rhsafrf\\addons\\rhs_c_weapons\\anims\\igla.rtm"],
    "magazines": ["rhs_mag_9k38_rocket"],
    "cmimmunity": 0.8,
    "airateoffire": 5,
    "airateoffiredistance": 3100,
    "maxleadspeed": 320,
    "dexterity": 0.5,
    # Class: CfgWeapons\\rhs_weap_igla\\WeaponSlotsInfo [Indent level: 1],
    "WeaponSlotsInfo": {
        "mass": 156.2
    },
    "reloadMagazineSound": ["A3\\Sounds_F\\weapons\\Reloads\\reload_magazine_MissileLauncher",0.891251,1,10],
    "sounds": ["StandardSound"],
    # Class: CfgWeapons\\rhs_weap_igla\\StandardSound [Indent level: 1],
    "StandardSound": {
        "begin1": ["A3\\Sounds_F\\weapons\\Rockets\\titan_4",1.41254,1,1100],
        "soundBegin": ["begin1",1],
        "weaponSoundEffect": "DefaultRifle"
    },
    "dlc": "RHS_AFRF",
    "htmax": 420,
    "htmin": 1,
    "afmax": 0,
    "mfact": 1,
    "mfmax": 0,
    "tbody": 100,
    "value": 15,
    "mass": 114.4,
    "lockAcquire": 1,
    "weaponlockdelay": 5,
    "weaponlocksystem": 2,
    "shotPos": "usti hlavne",
    "shotEnd": "konec hlavne",
    "cursorsize": 1,
    "cursorAim": "",
    "cursorAimOn": "",
    # Class: CfgWeapons\\rhs_weap_strela\\OpticsModes [Indent level: 1],
    "OpticsModes": {
        # Class: CfgWeapons\\rhs_weap_strela\\OpticsModes\\StepScope [Indent level: 2],

        "StepScope": {

            "opticsID": 1,

            "useModelOptics": 1,

            "opticsPPEffects": ["OpticsCHAbera1","OpticsBlur1"],

            "opticsFlare": 1,

            "opticsZoomMin": 0.25,

            "opticsZoomMax": 1.1,

            "opticsZoomInit": 0.75,

            "distanceZoomMin": 300,

            "distanceZoomMax": 300,

            "memoryPointCamera": "eye",

            "cameraDir": "look",

            "visionMode": ["Normal"],

            "thermalMode": [],

            "opticsDisablePeripherialVision": 1
        }
    },
    "maxrange": 4200,
    "maxrangeprobab": 0.1,
    "midrange": 2350,
    "midrangeprobab": 0.8,
    "minrange": 10,
    "minrangeprobab": 0.3,
    "modeloptics": "-",
    "weaponInfoType": "RscWeaponZeroing",
    # Class: CfgWeapons\\rhs_weap_strela\\GunParticles [Indent level: 1],
    "GunParticles": {
        # Class: CfgWeapons\\rhs_weap_strela\\GunParticles\\effect1 [Indent level: 2],

        "effect1": {

            "positionName": "missile_start",

            "directionName": "missile_end",

            "effectName": "RHS_9k32_Backfire"
        }
    },
    # Class: CfgWeapons\\rhs_weap_strela\\Library [Indent level: 1],
    "Library": {
        "libtextdesc": "The 9K32 Strela-2 (NATO name SA-7 Grail) is a man-portable, shoulder-fired surface-to-air missile (SAM) with passive infrared homing guidance, similar to the US Army Stinger.<br/>The 9K32 is a tail-chase missile dependent on the operatoro??s ability to lock it onto the heat source of low-flying jets and helicopters."
    },
    "_generalMacro": "launch_O_Titan_F",
    "hiddenSelectionsTextures": ["A3\\Weapons_F_Beta\\Launchers\\Titan\\Data\\Launcher_OPFOR_CO.paa","A3\\Weapons_F_Beta\\Launchers\\Titan\\Data\\TubeL_OPFOR_CO.paa"],
    "UiPicture": "A3\\Weapons_F\\Data\\UI\\icon_aa_CA.paa",
    "nameSound": "aalauncher",
    "magazineWell": ["Titan_Long"],
    "cursor": "missile",
    "reloadAction": "ReloadRPG",
    # Recoil Class: recoil,
    # Class: CfgRecoils\\recoil_titan_long [Indent level: 0],
    "recoil": {
        "muzzleOuter": [0.2,0.3,0.25,0.12],
        "kickBack": [0.1,0.12],
        "temporary": 0.15,
        "muzzleInner": [0,0,0.1,0.1],
        "permanent": 0.1
    },
    "maxZeroing": 2000,
    "modes": ["Single","TopDown"],
    # Class: CfgWeapons\\launch_Titan_base\\Single [Indent level: 1],
    "Single": {
        "sounds": ["standardsound"],
        # Class: CfgWeapons\\launch_Titan_base\\Single\\BaseSoundModeType [Indent level: 2],
        "BaseSoundModeType": {
        },
        # Class: CfgWeapons\\launch_Titan_base\\Single\\StandardSound [Indent level: 2],
        "StandardSound": {
            "begin1": ["A3\\Sounds_F\\arsenal\\weapons\\Launchers\\Titan\\Titan",3.16228,1,2000],
            "soundBegin": ["begin1",1],
            "soundSetShot": ["jsrs_mprl_shot_soundset","jsrs_warhead_reverb_soundset"]
        },
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.01,0,0.05,0.025,0,0],
        "aiRateOfFire": 7,
        "aiRateOfFireDistance": 1500,
        "minRange": 70,
        "minRangeProbab": 0.6,
        "midRange": 150,
        "midRangeProbab": 0.85,
        "maxRange": 3450,
        "maxRangeProbab": 0.85,
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
        "showToPlayer": 1,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "canShootInWater": 0,
        "displayName": "Semi",
        "textureType": "semi",
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "aiDispersionCoefY": 1.7,
        "aiDispersionCoefX": 1.4,
        "soundBurst": 0,
        "requiredOpticType": -1,
        "aiRateOfFireDispersion": 1
    },
    # Class: CfgWeapons\\launch_Titan_base\\TopDown [Indent level: 1],
    "TopDown": {
        "textureType": "topDown",
        "displayName": "Top-down Attack",
        "aiRateOfFire": 7,
        "aiRateOfFireDistance": 1500,
        "minRange": 150,
        "minRangeProbab": 0.8,
        "midRange": 500,
        "midRangeProbab": 0.95,
        "maxRange": 2000,
        "maxRangeProbab": 0.95,
        "sounds": ["standardsound"],
        # Class: CfgWeapons\\launch_Titan_base\\Single\\BaseSoundModeType [Indent level: 2],
        "BaseSoundModeType": {
        },
        # Class: CfgWeapons\\launch_Titan_base\\Single\\StandardSound [Indent level: 2],
        "StandardSound": {
            "begin1": ["A3\\Sounds_F\\arsenal\\weapons\\Launchers\\Titan\\Titan",3.16228,1,2000],
            "soundBegin": ["begin1",1],
            "soundSetShot": ["jsrs_mprl_shot_soundset","jsrs_warhead_reverb_soundset"]
        },
        # Recoil Array: recoil,
        "recoil": [0,0,0,0.01,0,0.05,0.025,0,0],
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
        "showToPlayer": 1,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "canShootInWater": 0,
        # Recoil Array: recoilProne,
        "recoilProne": [0,0,0,0.03,0.0110829,0.0021522,0.04,0.0095451,0.0007506,0.05,0.0059265,0.0004584,0.06,0.0022164,0.000171,0.06,0,0,0.06,-0.0007206,-2.88e-005,0.06,-0.001059,-8.46e-005,0.06,-0.0011031,-8.82e-005,0.06,-0.0009414,-7.5e-005,0.06,-0.0006618,-5.28e-005,0.06,-0.0003531,-2.82e-005,0.06,-0.0001029,-8.4e-006,0.06,-4.5e-005,0,0.06,0,0],
        "aiDispersionCoefY": 1.7,
        "aiDispersionCoefX": 1.4,
        "soundBurst": 0,
        "requiredOpticType": -1,
        "aiRateOfFireDispersion": 1
    },
    "drySound": ["A3\\Sounds_F\\arsenal\\weapons\\Launchers\\Titan\\Dry_Titan",0.158489,1,18],
    "lockingTargetSound": ["A3\\Sounds_F\\arsenal\\weapons\\Launchers\\Titan\\locking_Titan",0.316228,1],
    "lockedTargetSound": ["A3\\Sounds_F\\arsenal\\weapons\\Launchers\\Titan\\locked_Titan",0.316228,2.5],
    "canLock": 2,
    "inertia": 1.2,
    "aimTransitionSpeed": 0.6,
    # Class: CfgWeapons\\launch_Titan_base\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "priority": 3
    },
    "hiddenSelections": ["camo_launcher","camo_tube"],
    "soundFly": ["\\jsrs_soundmod_complete\\JSRS_Soundmod_Soundfiles\\warfare\\SoundFly1.ogg",1,1.5,500],
    "swayCoef": 0.5,
    "sound": ["A3\\Sounds_F\\weapons\\Launcher\\rocket_launcher_5",1,1,800],
    "weaponPoolAvailable": 1,
    "textureType": "semi",
    "autoAimEnabled": 0,
    "opticsDisablePeripherialVision": 1,
    "magazineReloadTime": 12,
    "reloadTime": 0,
    "initSpeed": 30,
    "autoReload": 0,
    "ffMagnitude": 0.1,
    "ffFrequency": 1,
    "ffCount": 1,
    "optics": 1,
    "primary": 0,
    "opticsZoomMin": 0.375,
    "opticsZoomMax": 1.1,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 100,
    "distanceZoomMax": 100,
    "type": 4,
    "count": 1,
    "access": 3,
    "ammo": "",
    "showAimCursorInternal": 1,
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "multiplier": 1,
    "burst": 1,
    "magazineReloadSwitchPhase": 1,
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
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
    "opticsFlare": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "muzzles": ["this"],
    "useAction": 0,
    "useActionTitle": "",
    "canDrop": 1,
    "weight": 0,
    "detectRange": 0,
    "artilleryDispersion": 1,
    "artilleryCharge": 1,
    "fireAnims": [],
    # Class: CfgWeapons\\Default\\GunFire [Indent level: 1],
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
        # Class: CfgWeapons\\Default\\GunFire\\Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3],

            "T0": {

                "maxT": 0,

                "color": [0.82,0.95,0.93,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T1 [Indent level: 3],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T2 [Indent level: 3],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T3 [Indent level: 3],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T4 [Indent level: 3],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T5 [Indent level: 3],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T6 [Indent level: 3],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T7 [Indent level: 3],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T8 [Indent level: 3],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T9 [Indent level: 3],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T10 [Indent level: 3],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T11 [Indent level: 3],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T12 [Indent level: 3],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T13 [Indent level: 3],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T14 [Indent level: 3],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T15 [Indent level: 3],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T16 [Indent level: 3],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T17 [Indent level: 3],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T18 [Indent level: 3],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T19 [Indent level: 3],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T20 [Indent level: 3],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T21 [Indent level: 3],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T22 [Indent level: 3],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgWeapons\\Default\\GunClouds [Indent level: 1],
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
        # Class: CfgWeapons\\Default\\GunClouds\\Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3],

            "T0": {

                "maxT": 0,

                "color": [1,1,1,0]
            }
        }
    },
},
"rhs_weap_rpg26": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\weapons\\rhs_weap_rpg26_ca.paa",
    "dlc": "RHS_AFRF",
    "scope": 2,
    "displayName": "RPG-26",
    "descriptionShort": "Rocket launcher<br/>Caliber: 72.5mm<br/>Type: Single-shot Anti-tank",
    "rhs_disposable": 1,
    "reloadTime": 1,
    "magazineReloadTime": 1,
    "model": "rhsafrf\\addons\\rhs_weapons\\rpg26\\rpg26",
    "modelOptics": "-",
    "aimTransitionSpeed": 0.75,
    # Recoil Array: recoil,
    "recoil": [0,0,0,0.03,0.0073886,0.0028696,0.04,0.0063634,0.0010008,0.05,0.003951,0.0006112,0.06,0.0014776,0.000228,0.06,0,0,0.06,-0.0004804,-7.68e-005,0.06,-0.000706,-0.0001128,0.06,-0.0007354,-0.0001176,0.06,-0.0006276,-0.0001,0.06,-0.0004412,-7.04e-005,0.06,-0.0002354,-3.76e-005,0.06,-6.86e-005,-1.12e-005,0.06,-3e-005,0,0.06,0,0],
    # Class: CfgWeapons\\rhs_weap_rpg26\\GunParticles [Indent level: 1],
    "GunParticles": {
        # Class: CfgWeapons\\rhs_weap_rpg26\\GunParticles\\effect1 [Indent level: 2],

        "effect1": {

            "positionName": "konec hlavne",

            "directionName": "usti hlavne",

            "effectName": "RocketBackEffectsRPGNT"
        }
    },
    "magazines": ["rhs_rpg26_mag"],
    "reloadAction": "ReloadRPG",
    "handAnim": ["OFP2_ManSkeleton","\\rhsafrf\\addons\\rhs_c_weapons\\anims\\RPG26.rtm"],
    "sounds": ["StandardSound"],
    # Class: CfgWeapons\\rhs_weap_rpg26\\StandardSound [Indent level: 1],
    "StandardSound": {
        "begin1": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_1",2.35,1,1100],
        "soundBegin": ["begin1",0.5,"begin2",0.5],
        "weaponSoundEffect": "DefaultRifle",
        "begin2": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_2",2.35,1,1100]
    },
    "drySound": ["A3\\sounds_f\\weapons\\other\\dry6",0.0316228,1,10],
    "reloadMagazineSound": ["A3\\sounds_f\\weapons\\rockets\\titan_reload_final",0.562341,1,50],
    "soundFly": ["A3\\sounds_f\\weapons\\rockets\\rocket_fly_1",0.316228,1.5,700],
    "showToPlayer": 1,
    "minRange": 10,
    "minRangeProbab": 0.9,
    "midRange": 200,
    "midRangeProbab": 0.7,
    "maxRange": 350,
    "maxRangeProbab": 0.1,
    "aiRateOfFire": 7,
    "aiRateOfFireDistance": 300,
    "dispersion": 0.18,
    "weaponInfoType": "rhs_rscOptics_disposable",
    "optics": 1,
    # Class: CfgWeapons\\rhs_weap_rpg26\\OpticsModes [Indent level: 1],
    "OpticsModes": {
        # Class: CfgWeapons\\rhs_weap_rpg26\\OpticsModes\\ironsight [Indent level: 2],

        "ironsight": {

            "opticsID": 2,

            "opticsPPEffects": ["OpticsCHAbera1","OpticsBlur1"],

            "useModelOptics": 0,

            "opticsFlare": 0,

            "opticsDisablePeripherialVision": 0,

            "opticsZoomMin": 0.25,

            "opticsZoomMax": 0.6,

            "opticsZoomInit": 0.6,

            "visionMode": "",

            "discreteDistanceInitIndex": 0,

            "discreteDistance": [100,0],

            "cameraDir": "op_look2",

            "discreteDistanceCameraPoint": ["eye_ironsight","eye_rangefinder"],

            "distanceZoomMin": 100,

            "distanceZoomMax": 100
        },
        # Class: CfgWeapons\\rhs_weap_rpg26\\OpticsModes\\ironsight2 [Indent level: 2],
        "ironsight2": {
            "opticsID": 1,
            "discreteDistance": [50,150,250],
            "discreteDistanceCameraPoint": ["eye","OP_eye1","OP_eye2"],
            "cameraDir": "op_look",
            "distanceZoomMin": 50,
            "distanceZoomMax": 250,
            "opticsPPEffects": ["OpticsCHAbera1","OpticsBlur1"],
            "useModelOptics": 0,
            "opticsFlare": 0,
            "opticsDisablePeripherialVision": 0,
            "opticsZoomMin": 0.25,
            "opticsZoomMax": 0.6,
            "opticsZoomInit": 0.6,
            "visionMode": "",
            "discreteDistanceInitIndex": 0
        }
    },
    # Class: CfgWeapons\\rhs_weap_rpg26\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": "The RPG-26 Aglen is a disposable anti-tank rocket launcher developed by the Soviet Union."
    },
    # Class: CfgWeapons\\rhs_weap_rpg26\\WeaponSlotsInfo [Indent level: 1],
    "WeaponSlotsInfo": {
        "allowedSlots": [901],
        "mass": 63.8
    },
    # Class: CfgWeapons\\rhs_weap_rpg26\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "priority": 3,
        "RMBhint": "RPG-26",
        "onHoverText": "RPG-26"
    },
    # Class: CfgWeapons\\rhs_weap_rpg26\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
        # Class: CfgWeapons\\rhs_weap_rpg26\\Eventhandlers\\RHS_DisposableWeapon [Indent level: 2],

        "RHS_DisposableWeapon": {

            "fired": "_this call rhs_fnc_disposable;"
        }
    },
    "htMin": 1,
    "htMax": 460,
    "afMax": 0,
    "mfMax": 0,
    "mFact": 1,
    "tBody": 100,
    "UiPicture": "A3\\Weapons_F\\Data\\UI\\icon_at_CA.paa",
    "dexterity": 1.7,
    "swayCoef": 0.5,
    "sound": ["A3\\Sounds_F\\weapons\\Launcher\\rocket_launcher_5",1,1,800],
    "weaponPoolAvailable": 1,
    "shotPos": "usti hlavne",
    "shotEnd": "konec hlavne",
    "cursorAim": "EmptyCursor",
    "cursor": "rocket",
    "textureType": "semi",
    "autoAimEnabled": 0,
    "opticsDisablePeripherialVision": 1,
    "value": 10,
    "nameSound": "atlauncher",
    "initSpeed": 30,
    "canLock": 0,
    "autoReload": 0,
    "ffMagnitude": 0.1,
    "ffFrequency": 1,
    "ffCount": 1,
    "primary": 0,
    "opticsZoomMin": 0.375,
    "opticsZoomMax": 1.1,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 100,
    "distanceZoomMax": 100,
    "maxZeroing": 1000,
    "type": 4,
    "count": 1,
    "inertia": 1,
    "access": 3,
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
    "multiplier": 1,
    "burst": 1,
    "magazineReloadSwitchPhase": 1,
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
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
    "opticsFlare": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "canShootInWater": 0,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    "backgroundReload": 0,
    "muzzles": ["this"],
    "modes": ["this"],
    "useAction": 0,
    "useActionTitle": "",
    "canDrop": 1,
    "weaponLockDelay": 0,
    "weaponLockSystem": 0,
    "cmImmunity": 1,
    "weight": 0,
    "lockingTargetSound": ["",0.000316228,2],
    "lockedTargetSound": ["",0.000316228,6],
    "detectRange": 0,
    "artilleryDispersion": 1,
    "artilleryCharge": 1,
    "fireAnims": [],
    # Class: CfgWeapons\\Default\\GunFire [Indent level: 1],
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
        # Class: CfgWeapons\\Default\\GunFire\\Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3],

            "T0": {

                "maxT": 0,

                "color": [0.82,0.95,0.93,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T1 [Indent level: 3],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T2 [Indent level: 3],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T3 [Indent level: 3],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T4 [Indent level: 3],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T5 [Indent level: 3],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T6 [Indent level: 3],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T7 [Indent level: 3],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T8 [Indent level: 3],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T9 [Indent level: 3],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T10 [Indent level: 3],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T11 [Indent level: 3],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T12 [Indent level: 3],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T13 [Indent level: 3],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T14 [Indent level: 3],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T15 [Indent level: 3],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T16 [Indent level: 3],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T17 [Indent level: 3],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T18 [Indent level: 3],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T19 [Indent level: 3],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T20 [Indent level: 3],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T21 [Indent level: 3],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T22 [Indent level: 3],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgWeapons\\Default\\GunClouds [Indent level: 1],
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
        # Class: CfgWeapons\\Default\\GunClouds\\Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3],

            "T0": {

                "maxT": 0,

                "color": [1,1,1,0]
            }
        }
    },
},
"rhs_weap_rpg7": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\weapons\\rhs_weap_rpg7_ca.paa",
    "dlc": "RHS_AFRF",
    "scope": 2,
    "displayName": "RPG-7V2",
    "descriptionShort": "Rocket launcher<br/>Caliber: 70mm<br/>Type: Rocket-propelled grenade launcher",
    "model": "rhsafrf\\addons\\rhs_weapons\\rpg7\\rhs_rpg7v2",
    "modelOptics": "-",
    "reloadAction": "RHS_GestureReloadRPG7",
    "handAnim": ["OFP2_ManSkeleton","\\rhsafrf\\addons\\rhs_c_weapons\\anims\\RPG7gripPrevraceny.rtm"],
    # Class: CfgWeapons\\rhs_weap_rpg7\\GunParticles [Indent level: 1],
    "GunParticles": {
        # Class: CfgWeapons\\rhs_weap_rpg7\\GunParticles\\effect1 [Indent level: 2],

        "effect1": {

            "positionName": "konec hlavne",

            "directionName": "usti hlavne",

            "effectName": "RocketBackEffectsRPGNT"
        }
    },
    "magazineReloadSwitchPhase": 0.3,
    "magazines": ["rhs_rpg7_PG7V_mag","rhs_rpg7_PG7VL_mag","rhs_rpg7_PG7VR_mag","rhs_rpg7_OG7V_mag","rhs_rpg7_TBG7V_mag","rhs_rpg7_TYPE69_airburst_mag"],
    "magazineWell": ["RPG7","CBA_RPG7"],
    "modes": ["single","single_optics1","single_optics2"],
    # Class: CfgWeapons\\rhs_weap_rpg7\\single [Indent level: 1],
    "single": {
        "reloadTime": 0.1,
        "minRange": 10,
        "minRangeProbab": 0.5,
        "midRange": 100,
        "midRangeProbab": 0.7,
        "maxRange": 200,
        "maxRangeProbab": 0.3,
        "aiRateOfFire": 6,
        "aiRateOfFireDistance": 300,
        "aiRateOfFireDispersion": 6,
        "dispersion": 0.013,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\\rhs_weap_rpg7\\single\\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_1",2.35,1,1100],
            "begin2": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_2",2.35,1,1100],
            "soundBegin": ["begin1",0.5,"begin2",0.5]
        },
        "sound": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_1",2.35,1,900],
        "multiplier": 1,
        "burst": 1,
        "burstRangeMax": -1,
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
        "requiredOpticType": -1
    },
    # Class: CfgWeapons\\rhs_weap_rpg7\\single_optics1 [Indent level: 1],
    "single_optics1": {
        "requiredOpticType": 1,
        "showToPlayer": 0,
        "minRange": 10,
        "minRangeProbab": 0.4,
        "midRange": 250,
        "midRangeProbab": 0.7,
        "maxRange": 400,
        "maxRangeProbab": 0.2,
        "reloadTime": 0.1,
        "aiRateOfFire": 6,
        "aiRateOfFireDistance": 300,
        "aiRateOfFireDispersion": 6,
        "dispersion": 0.013,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\\rhs_weap_rpg7\\single\\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_1",2.35,1,1100],
            "begin2": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_2",2.35,1,1100],
            "soundBegin": ["begin1",0.5,"begin2",0.5]
        },
        "sound": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_1",2.35,1,900],
        "multiplier": 1,
        "burst": 1,
        "burstRangeMax": -1,
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
    # Class: CfgWeapons\\rhs_weap_rpg7\\single_optics2 [Indent level: 1],
    "single_optics2": {
        "requiredOpticType": 2,
        "minRange": 10,
        "midRange": 300,
        "maxRange": 400,
        "showToPlayer": 0,
        "minRangeProbab": 0.4,
        "midRangeProbab": 0.7,
        "maxRangeProbab": 0.2,
        "reloadTime": 0.1,
        "aiRateOfFire": 6,
        "aiRateOfFireDistance": 300,
        "aiRateOfFireDispersion": 6,
        "dispersion": 0.013,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\\rhs_weap_rpg7\\single\\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_1",2.35,1,1100],
            "begin2": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_2",2.35,1,1100],
            "soundBegin": ["begin1",0.5,"begin2",0.5]
        },
        "sound": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_1",2.35,1,900],
        "multiplier": 1,
        "burst": 1,
        "burstRangeMax": -1,
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
    "weaponInfoType": "rhs_rscOptics_RPG7",
    "discreteDistance": [100,150,200,300],
    "discreteDistanceCameraPoint": ["eye_100","eye_150","eye_200","eye_300"],
    "discreteDistanceInitIndex": 0,
    "cameraDir": "eye_look",
    "inertia": 0.8,
    "dexterity": 1.2,
    "aimTransitionSpeed": 0.5,
    "maxZeroing": 500,
    # Recoil Class: recoil,
    # Class: CfgRecoils\\recoil_rpg [Indent level: 0],
    "recoil": {
        "muzzleOuter": [0.2,0.3,0.25,0.12],
        "kickBack": [0.08,0.1],
        "temporary": 0.1,
        "muzzleInner": [0,0,0.1,0.1],
        "permanent": 0.1
    },
    "sound": ["A3\\Sounds_F\\weapons\\Launcher\\rpg32",1.99526,1,800],
    "drySound": ["A3\\sounds_f\\weapons\\other\\dry6",0.0316228,1,10],
    "reloadMagazineSound": ["A3\\sounds_f\\weapons\\rockets\\titan_reload_final",0.562341,1,50],
    # Class: CfgWeapons\\rhs_weap_rpg7\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": "The RPG-7V2 is a portable, unguided, shoulder-launched, anti-tank rocket-propelled grenade launcher."
    },
    # Class: CfgWeapons\\rhs_weap_rpg7\\WeaponSlotsInfo [Indent level: 1],
    "WeaponSlotsInfo": {
        "mass": 126.7,
        # Class: CfgWeapons\\rhs_weap_rpg7\\WeaponSlotsInfo\\CowsSlot [Indent level: 2],
        "CowsSlot": {
            "linkProxy": "A3\\data_f\\proxies\\weapon_slots\\TOP",
            "displayName": "Optics Slot",
            "iconPosition": [0,0],
            "iconScale": 1,
            "iconPicture": "A3\\Weapons_F\\Data\\clear_empty.paa",
            "iconPinPoint": "Left",
            # Class: rhs_russian_rpg7_scopes_slot\\compatibleItems [Indent level: 0],
            "compatibleItems": {
                "rhs_acc_1pn93_1": 1,
                "rhs_acc_pgo7v": 1,
                "rhs_acc_pgo7v_ak": 1,
                "rhs_acc_pgo7v_asval": 1,
                "rhs_acc_pgo7v_pkp": 1,
                "rhs_acc_pgo7v2": 1,
                "rhs_acc_pgo7v2_ak": 1,
                "rhs_acc_pgo7v2_asval": 1,
                "rhs_acc_pgo7v2_pkp": 1,
                "rhs_acc_pgo7v3": 1,
                "rhs_acc_pgo7v3_ak": 1,
                "rhs_acc_pgo7v3_asval": 1,
                "rhs_acc_pgo7v3_pkp": 1,
                "rhs_acc_1pn93_2": 1
            },
            "access": 1,
            "scope": 0
        },
        # Class: CfgWeapons\\rhs_weap_rpg7\\WeaponSlotsInfo\\PointerSlot [Indent level: 2],
        "PointerSlot": {
        },
        "allowedSlots": []
    },
    # Class: CfgWeapons\\rhs_weap_rpg7\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "priority": 3,
        "RMBhint": "RPG-7V2",
        "onHoverText": "RPG-7V2"
    },
    "baseWeapon": "rhs_weap_rpg7",
    "rhs_pgo7v_type": "rhs_acc_pgo7v",
    "rhs_pgo7v2_type": "rhs_acc_pgo7v2",
    "rhs_pgo7v3_type": "rhs_acc_pgo7v3",
    "htMin": 1,
    "htMax": 460,
    "afMax": 0,
    "mfMax": 0,
    "mFact": 1,
    "tBody": 100,
    "UiPicture": "A3\\Weapons_F\\Data\\UI\\icon_at_CA.paa",
    "swayCoef": 0.5,
    "soundFly": ["A3\\sounds_f\\weapons\\rockets\\rocket_fly_1",0.316228,1.5,700],
    "weaponPoolAvailable": 1,
    "shotPos": "usti hlavne",
    "shotEnd": "konec hlavne",
    "cursorAim": "EmptyCursor",
    "cursor": "rocket",
    "textureType": "semi",
    "autoAimEnabled": 0,
    "opticsDisablePeripherialVision": 1,
    "value": 10,
    "nameSound": "atlauncher",
    "magazineReloadTime": 12,
    "reloadTime": 0,
    "initSpeed": 30,
    "canLock": 0,
    "autoReload": 0,
    "ffMagnitude": 0.1,
    "ffFrequency": 1,
    "ffCount": 1,
    "aiRateOfFire": 10,
    "aiRateOfFireDistance": 500,
    "optics": 1,
    "primary": 0,
    "opticsZoomMin": 0.375,
    "opticsZoomMax": 1.1,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 100,
    "distanceZoomMax": 100,
    "minRange": 20,
    "minRangeProbab": 0.3,
    "midRange": 150,
    "midRangeProbab": 0.58,
    "maxRange": 500,
    "maxRangeProbab": 0.04,
    "type": 4,
    "count": 1,
    "access": 3,
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
    "multiplier": 1,
    "burst": 1,
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
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
    "opticsFlare": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
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
    "lockingTargetSound": ["",0.000316228,2],
    "lockedTargetSound": ["",0.000316228,6],
    "detectRange": 0,
    "artilleryDispersion": 1,
    "artilleryCharge": 1,
    "fireAnims": [],
    # Class: CfgWeapons\\Default\\GunFire [Indent level: 1],
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
        # Class: CfgWeapons\\Default\\GunFire\\Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3],

            "T0": {

                "maxT": 0,

                "color": [0.82,0.95,0.93,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T1 [Indent level: 3],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T2 [Indent level: 3],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T3 [Indent level: 3],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T4 [Indent level: 3],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T5 [Indent level: 3],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T6 [Indent level: 3],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T7 [Indent level: 3],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T8 [Indent level: 3],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T9 [Indent level: 3],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T10 [Indent level: 3],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T11 [Indent level: 3],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T12 [Indent level: 3],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T13 [Indent level: 3],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T14 [Indent level: 3],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T15 [Indent level: 3],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T16 [Indent level: 3],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T17 [Indent level: 3],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T18 [Indent level: 3],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T19 [Indent level: 3],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T20 [Indent level: 3],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T21 [Indent level: 3],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T22 [Indent level: 3],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgWeapons\\Default\\GunClouds [Indent level: 1],
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
        # Class: CfgWeapons\\Default\\GunClouds\\Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3],

            "T0": {

                "maxT": 0,

                "color": [1,1,1,0]
            }
        }
    },
},
"rhs_weap_rshg2": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\weapons\\rhs_weap_rshg2_ca.paa",
    "scope": 2,
    "displayName": "RShG-2",
    "descriptionShort": "Rocket launcher<br/>Caliber: 72.5mm<br/>Type: Single-shot Assault-weapon",
    "magazines": ["rhs_rshg2_mag"],
    "model": "rhsafrf\\addons\\rhs_weapons\\rpg26\\rshg2",
    "modelOptics": "-",
    "dispersion": 0.18,
    # Class: CfgWeapons\\rhs_weap_rshg2\\OpticsModes [Indent level: 1],
    "OpticsModes": {
        # Class: CfgWeapons\\rhs_weap_rshg2\\OpticsModes\\ironsight [Indent level: 2],

        "ironsight": {

            "opticsID": 2,

            "opticsPPEffects": ["OpticsCHAbera1","OpticsBlur1"],

            "useModelOptics": 0,

            "opticsFlare": 0,

            "opticsDisablePeripherialVision": 0,

            "opticsZoomMin": 0.25,

            "opticsZoomMax": 0.6,

            "opticsZoomInit": 0.6,

            "visionMode": "",

            "discreteDistanceInitIndex": 0,

            "discreteDistance": [100,0],

            "cameraDir": "op_look2",

            "discreteDistanceCameraPoint": ["eye_ironsight","eye_rangefinder"],

            "distanceZoomMin": 100,

            "distanceZoomMax": 100
        },
        # Class: CfgWeapons\\rhs_weap_rshg2\\OpticsModes\\ironsight2 [Indent level: 2],
        "ironsight2": {
            "opticsID": 1,
            "discreteDistance": [50,100,150,200,250,300,350],
            "discreteDistanceCameraPoint": ["eye","OP_eye1","OP_eye2","OP_eye3","OP_eye4","OP_eye5","OP_eye6"],
            "cameraDir": "op_look",
            "distanceZoomMin": 50,
            "distanceZoomMax": 350,
            "opticsPPEffects": ["OpticsCHAbera1","OpticsBlur1"],
            "useModelOptics": 0,
            "opticsFlare": 0,
            "opticsDisablePeripherialVision": 0,
            "opticsZoomMin": 0.25,
            "opticsZoomMax": 0.6,
            "opticsZoomInit": 0.6,
            "visionMode": "",
            "discreteDistanceInitIndex": 0
        }
    },
    # Class: CfgWeapons\\rhs_weap_rshg2\\GunParticles [Indent level: 1],
    "GunParticles": {
        # Class: CfgWeapons\\rhs_weap_rshg2\\GunParticles\\effect1 [Indent level: 2],

        "effect1": {

            "positionName": "konec hlavne",

            "directionName": "usti hlavne",

            "effectName": "RocketBackEffectsRPGNT"
        }
    },
    # Class: CfgWeapons\\rhs_weap_rshg2\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": "The RShG-2 is a disposable thermobaric rocket launcher derived from the RPG-26."
    },
    # Class: CfgWeapons\\rhs_weap_rshg2\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "priority": 3,
        "RMBhint": "RShG-2",
        "onHoverText": "RShG-2"
    },
    # Class: CfgWeapons\\rhs_weap_rshg2\\WeaponSlotsInfo [Indent level: 1],
    "WeaponSlotsInfo": {
        "allowedSlots": [901],
        "mass": 83.6
    },
    "dlc": "RHS_AFRF",
    "rhs_disposable": 1,
    "reloadTime": 1,
    "magazineReloadTime": 1,
    "aimTransitionSpeed": 0.75,
    # Recoil Array: recoil,
    "recoil": [0,0,0,0.03,0.0073886,0.0028696,0.04,0.0063634,0.0010008,0.05,0.003951,0.0006112,0.06,0.0014776,0.000228,0.06,0,0,0.06,-0.0004804,-7.68e-005,0.06,-0.000706,-0.0001128,0.06,-0.0007354,-0.0001176,0.06,-0.0006276,-0.0001,0.06,-0.0004412,-7.04e-005,0.06,-0.0002354,-3.76e-005,0.06,-6.86e-005,-1.12e-005,0.06,-3e-005,0,0.06,0,0],
    "reloadAction": "ReloadRPG",
    "handAnim": ["OFP2_ManSkeleton","\\rhsafrf\\addons\\rhs_c_weapons\\anims\\RPG26.rtm"],
    "sounds": ["StandardSound"],
    # Class: CfgWeapons\\rhs_weap_rpg26\\StandardSound [Indent level: 1],
    "StandardSound": {
        "begin1": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_1",2.35,1,1100],
        "soundBegin": ["begin1",0.5,"begin2",0.5],
        "weaponSoundEffect": "DefaultRifle",
        "begin2": ["rhsafrf\\addons\\rhs_sounds\\rpg\\rpg_2",2.35,1,1100]
    },
    "drySound": ["A3\\sounds_f\\weapons\\other\\dry6",0.0316228,1,10],
    "reloadMagazineSound": ["A3\\sounds_f\\weapons\\rockets\\titan_reload_final",0.562341,1,50],
    "soundFly": ["A3\\sounds_f\\weapons\\rockets\\rocket_fly_1",0.316228,1.5,700],
    "showToPlayer": 1,
    "minRange": 10,
    "minRangeProbab": 0.9,
    "midRange": 200,
    "midRangeProbab": 0.7,
    "maxRange": 350,
    "maxRangeProbab": 0.1,
    "aiRateOfFire": 7,
    "aiRateOfFireDistance": 300,
    "weaponInfoType": "rhs_rscOptics_disposable",
    "optics": 1,
    # Class: CfgWeapons\\rhs_weap_rpg26\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
        # Class: CfgWeapons\\rhs_weap_rpg26\\Eventhandlers\\RHS_DisposableWeapon [Indent level: 2],

        "RHS_DisposableWeapon": {

            "fired": "_this call rhs_fnc_disposable;"
        }
    },
    "htMin": 1,
    "htMax": 460,
    "afMax": 0,
    "mfMax": 0,
    "mFact": 1,
    "tBody": 100,
    "UiPicture": "A3\\Weapons_F\\Data\\UI\\icon_at_CA.paa",
    "dexterity": 1.7,
    "swayCoef": 0.5,
    "sound": ["A3\\Sounds_F\\weapons\\Launcher\\rocket_launcher_5",1,1,800],
    "weaponPoolAvailable": 1,
    "shotPos": "usti hlavne",
    "shotEnd": "konec hlavne",
    "cursorAim": "EmptyCursor",
    "cursor": "rocket",
    "textureType": "semi",
    "autoAimEnabled": 0,
    "opticsDisablePeripherialVision": 1,
    "value": 10,
    "nameSound": "atlauncher",
    "initSpeed": 30,
    "canLock": 0,
    "autoReload": 0,
    "ffMagnitude": 0.1,
    "ffFrequency": 1,
    "ffCount": 1,
    "primary": 0,
    "opticsZoomMin": 0.375,
    "opticsZoomMax": 1.1,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 100,
    "distanceZoomMax": 100,
    "maxZeroing": 1000,
    "type": 4,
    "count": 1,
    "inertia": 1,
    "access": 3,
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
    "multiplier": 1,
    "burst": 1,
    "magazineReloadSwitchPhase": 1,
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
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
    "opticsFlare": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "canShootInWater": 0,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    "backgroundReload": 0,
    "muzzles": ["this"],
    "modes": ["this"],
    "useAction": 0,
    "useActionTitle": "",
    "canDrop": 1,
    "weaponLockDelay": 0,
    "weaponLockSystem": 0,
    "cmImmunity": 1,
    "weight": 0,
    "lockingTargetSound": ["",0.000316228,2],
    "lockedTargetSound": ["",0.000316228,6],
    "detectRange": 0,
    "artilleryDispersion": 1,
    "artilleryCharge": 1,
    "fireAnims": [],
    # Class: CfgWeapons\\Default\\GunFire [Indent level: 1],
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
        # Class: CfgWeapons\\Default\\GunFire\\Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3],

            "T0": {

                "maxT": 0,

                "color": [0.82,0.95,0.93,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T1 [Indent level: 3],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T2 [Indent level: 3],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T3 [Indent level: 3],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T4 [Indent level: 3],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T5 [Indent level: 3],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T6 [Indent level: 3],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T7 [Indent level: 3],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T8 [Indent level: 3],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T9 [Indent level: 3],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T10 [Indent level: 3],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T11 [Indent level: 3],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T12 [Indent level: 3],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T13 [Indent level: 3],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T14 [Indent level: 3],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T15 [Indent level: 3],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T16 [Indent level: 3],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T17 [Indent level: 3],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T18 [Indent level: 3],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T19 [Indent level: 3],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T20 [Indent level: 3],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T21 [Indent level: 3],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T22 [Indent level: 3],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgWeapons\\Default\\GunClouds [Indent level: 1],
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
        # Class: CfgWeapons\\Default\\GunClouds\\Table [Indent level: 2],
        "Table": {
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3],

            "T0": {

                "maxT": 0,

                "color": [1,1,1,0]
            }
        }
    }
}