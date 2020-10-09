"rhs_6b13_EMR_6sh92": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b13_EMR_6sh92_ca.paa",
    "displayName": "6B13 EMR (6Sh92)",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b13_emr_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_digi_co.paa"],
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b13_6sh92",
    "descriptionShort": "Armor Level 6",
    # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b13_6sh92",
        "containerClass": "Supply100",
        "mass": 95,
        # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 16,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_3"
            },
            # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": "28 + 		3",
                "PassThrough": 0.1,
                "simulation": "RHS_Gost_6"
            },
            # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "28 + 		3",
                "PassThrough": 0.1,
                "simulation": "RHS_Gost_6"
            },
            # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 22,
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            }
        },
        "hiddenSelections": ["Camo1","Camo2"],
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "hiddenSelections": ["Camo1","Camo2"],
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b13_Flora_6sh92": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b13_Flora_6sh92_ca.paa",
    "displayName": "6B13 (6Sh92)",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b13_Flora_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_co.paa"],
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b13_6sh92",
    "descriptionShort": "Armor Level 6",
    # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b13_6sh92",
        "containerClass": "Supply100",
        "mass": 95,
        # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 16,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_3"
            },
            # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": "28 + 		3",
                "PassThrough": 0.1,
                "simulation": "RHS_Gost_6"
            },
            # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "28 + 		3",
                "PassThrough": 0.1,
                "simulation": "RHS_Gost_6"
            },
            # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 22,
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b13_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            }
        },
        "hiddenSelections": ["Camo1","Camo2"],
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "hiddenSelections": ["Camo1","Camo2"],
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b23": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b23_ca.paa",
    "dlc": "RHS_AFRF",
    "scope": 2,
    "displayName": "6B23",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23",
    "hiddenSelections": ["Camo1","Camo2"],
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_co.paa"],
    "descriptionShort": "Armor Level 4",
    # Class: CfgWeapons\\rhs_6b23\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["Camo1","Camo2"],
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23",
        "containerClass": "Supply20",
        "mass": 60,
        # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 8,
                "PassThrough": 0.4,
                "simulation": "RHS_Gost_2"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 22,
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_3"
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b23_6sh116_od": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b23_6sh116_od_ca.paa",
    "displayName": "6B23 (6Sh116)",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_olive_co.paa","rhsafrf\\addons\\rhs_infantry2\\data\\rhs_6sh116_od_co.paa","rhsafrf\\addons\\rhs_infantry2\\data\\rhs_6sh116_gear1_od_co.paa"],
    "model": "rhsafrf\\addons\\rhs_infantry2\\gear\\vests\\rhs_6b23_6sh116",
    "hiddenSelections": ["Camo1","Camo2","Camo3"],
    # Class: CfgWeapons\\rhs_6b23_6sh116\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry2\\gear\\vests\\rhs_6b23_6sh116",
        "hiddenSelections": ["Camo1","Camo2","Camo3"],
        "containerClass": "Supply140",
        "mass": 80,
        # Class: CfgWeapons\\rhs_6b23_6sh116\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b23_6sh116\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 12,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_3"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh116\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh116\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "22 + 		3",
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh116\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": "22 + 		3",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh116\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_3"
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "descriptionShort": "Armor Level 4",
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b23_digi_6sh92_Spetsnaz": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b23_digi_6sh92_Spetsnaz_ca.paa",
    "displayName": "6B23 EMR-Summer (6Sh92/Radio) SpNz",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_6sh92_radio_spetsnaz",
    # Class: CfgWeapons\\rhs_6b23_digi_6sh92_Spetsnaz\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_6sh92_radio_spetsnaz",
        "containerClass": "Supply100",
        "mass": 70,
        # Class: CfgWeapons\\rhs_6b23_digi_6sh92_Spetsnaz\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b23_digi_6sh92_Spetsnaz\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 8,
                "PassThrough": 0.4,
                "simulation": "RHS_Gost_2"
            },
            # Class: CfgWeapons\\rhs_6b23_digi_6sh92_Spetsnaz\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_digi_6sh92_Spetsnaz\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "22 + 		3",
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_digi_6sh92_Spetsnaz\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": "22 + 		3",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_digi_6sh92_Spetsnaz\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_3"
            }
        },
        "hiddenSelections": ["Camo1","Camo2"],
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_digi_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_digi_co.paa"],
    "dlc": "RHS_AFRF",
    "scope": 2,
    "hiddenSelections": ["Camo1","Camo2"],
    "descriptionShort": "Armor Level 4",
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b23_digi_6sh92_spetsnaz2": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b23_digi_6sh92_spetsnaz2_ca.paa",
    "displayName": "6b23 EMR-Summer (6Sh92) SpNz",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_6sh92_spetsnaz",
    # Class: CfgWeapons\\rhs_6b23_digi_6sh92_spetsnaz2\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_6sh92_spetsnaz",
        "containerClass": "Supply100",
        "mass": 75,
        # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 12,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_3"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "22 + 		3",
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": "22 + 		3",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_3"
            }
        },
        "hiddenSelections": ["Camo1","Camo2"],
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_digi_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_digi_co.paa"],
    "dlc": "RHS_AFRF",
    "scope": 2,
    "hiddenSelections": ["Camo1","Camo2"],
    "descriptionShort": "Armor Level 4",
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b23_digi_6sh92_Vog_Radio_Spetsnaz": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b23_digi_6sh92_Vog_Radio_Spetsnaz_ca.paa",
    "displayName": "6B23 EMR-Summer (6Sh92/VOG/Radio) SpNz",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_6sh92_vog_radio_spetsnaz",
    # Class: CfgWeapons\\rhs_6b23_digi_6sh92_Vog_Radio_Spetsnaz\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_6sh92_vog_radio_spetsnaz",
        "containerClass": "Supply120",
        "mass": 75,
        # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 12,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_3"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "22 + 		3",
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": "22 + 		3",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_3"
            }
        },
        "hiddenSelections": ["Camo1","Camo2"],
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_digi_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_digi_co.paa"],
    "dlc": "RHS_AFRF",
    "scope": 2,
    "hiddenSelections": ["Camo1","Camo2"],
    "descriptionShort": "Armor Level 4",
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b23_digi_rifleman": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b23_digi_rifleman_ca.paa",
    "displayName": "6B23 EMR-Summer (Rifleman)",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_digi_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_digi_co.paa"],
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_rifleman",
    # Class: CfgWeapons\\rhs_6b23_rifleman\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_rifleman",
        "containerClass": "Supply80",
        "mass": 65,
        "hiddenSelections": ["Camo1","Camo2"],
        # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 8,
                "PassThrough": 0.4,
                "simulation": "RHS_Gost_2"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 22,
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_3"
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "hiddenSelections": ["Camo1","Camo2"],
    "descriptionShort": "Armor Level 4",
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b23_ML_rifleman": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b23_ML_rifleman_ca.paa",
    "displayName": "6B23 Mountain Les (Rifleman)",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_ML_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_ML_co.paa"],
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_rifleman",
    # Class: CfgWeapons\\rhs_6b23_rifleman\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_rifleman",
        "containerClass": "Supply80",
        "mass": 65,
        "hiddenSelections": ["Camo1","Camo2"],
        # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 8,
                "PassThrough": 0.4,
                "simulation": "RHS_Gost_2"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 22,
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_3"
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "hiddenSelections": ["Camo1","Camo2"],
    "descriptionShort": "Armor Level 4",
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b23_rifleman": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b23_rifleman_ca.paa",
    "displayName": "6B23 (Rifleman)",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_rifleman",
    # Class: CfgWeapons\\rhs_6b23_rifleman\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6b23_rifleman",
        "containerClass": "Supply80",
        "mass": 65,
        "hiddenSelections": ["Camo1","Camo2"],
        # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 8,
                "PassThrough": 0.4,
                "simulation": "RHS_Gost_2"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 22,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 22,
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b23\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_3"
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "hiddenSelections": ["Camo1","Camo2"],
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_co.paa"],
    "descriptionShort": "Armor Level 4",
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b27m_ess": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_6b27m_ess_ca.paa",
    "allowedFacewear": ["",7,"rhs_scarf",2,"G_Aviator",1],
    "displayName": "6B27M Flora (ESS)",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_6b27m_ess",
    # Class: CfgWeapons\\rhs_6b27m_ess\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 40,
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_6b27m_ess",
        "hiddenSelections": ["Camo1"],
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhs_6b27m\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b27m\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 6,
                "passThrough": 0.5
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "hiddenSelections": ["Camo1"],
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b27_co.paa"],
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b27m_ml_ess": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_6b27m_ml_ess_ca.paa",
    "displayName": "6B27M Mountain Les (ESS)",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b27_ml_co.paa"],
    "allowedFacewear": ["",7,"rhs_scarf",2,"G_Aviator",1],
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_6b27m_ess",
    # Class: CfgWeapons\\rhs_6b27m_ess\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 40,
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_6b27m_ess",
        "hiddenSelections": ["Camo1"],
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhs_6b27m\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b27m\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 6,
                "passThrough": 0.5
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "hiddenSelections": ["Camo1"],
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b28_ess": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_6b28_ess_ca.paa",
    "displayName": "6B28 EMR-Summer (ESS)",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_6b28_ess",
    # Class: CfgWeapons\\rhs_6b28_ess\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 40,
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_6b28_ess",
        # Class: CfgWeapons\\rhs_6b28\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b28\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 6,
                "passThrough": 0.5
            }
        },
        "hiddenSelections": ["Camo1"],
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "allowedFacewear": ["",7,"rhs_scarf",2,"G_Aviator",1],
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\rhs_6b28_cover_co"],
    "dlc": "RHS_AFRF",
    "hiddenSelections": ["Camo1"],
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b43": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6b43_ca.paa",
    "displayName": "6B43",
    "model": "rhsafrf\\addons\\rhs_infantry2\\gear\\vests\\rhs_6b43_m",
    "hiddenSelections": ["Camo1"],
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry2\\data\\6B43_co.paa"],
    "descriptionShort": "Armor Level 6",
    # Class: CfgWeapons\\rhs_6b43\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry2\\gear\\vests\\rhs_6b43_m",
        "containerClass": "Supply20",
        "mass": 80,
        # Class: CfgWeapons\\rhs_6b43\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b43\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 16,
                "PassThrough": 0.3,
                "simulation": "RHS_Gost_3"
            },
            # Class: CfgWeapons\\rhs_6b43\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "PassThrough": 0.1,
                "simulation": "RHS_Gost_6"
            },
            # Class: CfgWeapons\\rhs_6b43\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 28,
                "PassThrough": 0.1,
                "simulation": "RHS_Gost_6"
            },
            # Class: CfgWeapons\\rhs_6b43\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 22,
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            },
            # Class: CfgWeapons\\rhs_6b43\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.3,
                "simulation": "RHS_Gost_4"
            }
        },
        "hiddenSelections": ["Camo1","Camo2"],
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b47": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_6b47_ca.paa",
    "allowedFacewear": ["",7,"rhs_scarf",2,"G_Aviator",1],
    "displayName": "6B47",
    "model": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_6b47",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_6b7-1m_co.paa"],
    # Class: CfgWeapons\\rhs_6b47\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_6b47",
        "mass": 40,
        # Class: CfgWeapons\\rhs_6b28\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b28\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 6,
                "passThrough": 0.5
            }
        },
        "hiddenSelections": ["Camo1"],
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "hiddenSelections": ["Camo1"],
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b5_rifleman_khaki": {
    "author": "Red Hammer Studios",
    "picture": "rhsgref\\addons\\rhsgref_inventoryicons\\data\\Vests\\rhs_6b5_rifleman_khaki_ca.paa",
    "displayName": "6B5-19 (6Sh46)",
    "hiddenSelections": ["camo1"],
    "hiddenSelectionsTextures": ["rhsgref\\addons\\rhsgref_infantry\\data_cdf\\6b5_khaki_co.paa"],
    "model": "rhsgref\\addons\\rhsgref_infantry\\gear_cdf\\vests\\rhs_6b5_6sh46_rifleman",
    # Class: CfgWeapons\\rhs_6b5_rifleman\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsgref\\addons\\rhsgref_infantry\\gear_cdf\\vests\\rhs_6b5_6sh46_rifleman",
        "containerClass": "Supply130",
        "mass": 147,
        # Class: CfgWeapons\\rhs_6b5\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b5\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 8,
                "PassThrough": 0.5
            },
            # Class: CfgWeapons\\rhs_6b5\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 25,
                "PassThrough": 0.2
            },
            # Class: CfgWeapons\\rhs_6b5\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 25,
                "PassThrough": 0.2
            },
            # Class: CfgWeapons\\rhs_6b5\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 25,
                "passThrough": 0.2
            },
            # Class: CfgWeapons\\rhs_6b5\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "armor": 8,
                "passThrough": 0.5
            }
        },
        "hiddenSelections": ["Camo1","Camo2"],
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "descriptionShort": "Armor Level 6",
    "dlc": "RHS_AFRF",
    "scope": 2,
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b7_1m_bala1_flora": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_6b7_1m_bala1_flora_ca.paa",
    "displayName": "6B7-1M (Flora/Balaclava)",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_6b7-1m_co.paa","rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_6b7-1m_flora_co.paa","rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_bala1_olive_co.paa"],
    # Class: CfgWeapons\\rhs_6b7_1m_bala1_flora\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["Camo1","Camo2","Camo3"],
        "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_6b7-1m_co.paa","rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_6b7-1m_flora_co.paa","rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_bala1_olive_co.paa"],
        "uniformModel": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_6b7_1m_cover_balaclava1",
        "mass": 40,
        # Class: CfgWeapons\\rhs_6b28\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b28\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 6,
                "passThrough": 0.5
            }
        },
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "allowedFacewear": [],
    "model": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_6b7_1m_cover_balaclava1",
    "hiddenSelections": ["Camo1","Camo2","Camo3"],
    "dlc": "RHS_AFRF",
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6b7_1m_emr_ess_bala": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_6b7_1m_emr_ess_bala_ca.paa",
    "allowedFacewear": [],
    "displayName": "6B7-1M (EMR/ESS/Balaclava)",
    "model": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_6b7_1m_cover_ess_bala",
    "hiddenSelections": ["Camo1","Camo2","Camo3"],
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_6b7-1m_co.paa","rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_6b7-1m_emr_co.paa","rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_bala2_olive_co.paa"],
    # Class: CfgWeapons\\rhs_6b7_1m_emr_ess_bala\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["Camo1","Camo2","Camo3"],
        "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_6b7-1m_co.paa","rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_6b7-1m_emr_co.paa","rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_bala2_olive_co.paa"],
        "uniformModel": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_6b7_1m_cover_ess_bala",
        "mass": 40,
        # Class: CfgWeapons\\rhs_6b28\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6b28\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 6,
                "passThrough": 0.5
            }
        },
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6sh92": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6sh92_ca.paa",
    "dlc": "RHS_AFRF",
    "scope": 2,
    "displayName": "6Sh92",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6sh92",
    "hiddenSelections": ["Camo1","Camo2"],
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_co.paa"],
    "descriptionShort": "No Armor",
    # Class: CfgWeapons\\rhs_6sh92\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["Camo1","Camo2"],
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6sh92",
        "containerClass": "Supply100",
        "mass": 15,
        # Class: CfgWeapons\\rhs_6sh92\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3]
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 3,
                "passThrough": 0.6
            },
            # Class: CfgWeapons\\rhs_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "armor": 0,
                "passThrough": 0.8
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6sh92_digi_vog_headset": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6sh92_digi_vog_headset_ca.paa",
    "displayName": "6Sh92 EMR-Summer (VOG/Headset)",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_digi_co.paa","rhsafrf\\addons\\rhs_infantry\\data\\gearpack1_6sh92_digi_co.paa"],
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6sh92_vog_headset",
    # Class: CfgWeapons\\rhs_6sh92_vog_headset\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6sh92_vog_headset",
        "containerClass": "Supply120",
        "mass": 20,
        "hiddenSelections": ["Camo1","Camo2"],
        # Class: CfgWeapons\\rhs_6sh92\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3]
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 3,
                "passThrough": 0.6
            },
            # Class: CfgWeapons\\rhs_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "armor": 0,
                "passThrough": 0.8
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "hiddenSelections": ["Camo1","Camo2"],
    "descriptionShort": "No Armor",
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_6sh92_vsr": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_6sh92_vsr_ca.paa",
    "displayName": "6Sh92 VSR",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\6b23_olive_co.paa","rhsafrf\\addons\\rhs_infantry2\\data\\gearpack1_6sh92_vsr_co.paa"],
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6sh92",
    "hiddenSelections": ["Camo1","Camo2"],
    "descriptionShort": "No Armor",
    # Class: CfgWeapons\\rhs_6sh92\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["Camo1","Camo2"],
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_6sh92",
        "containerClass": "Supply100",
        "mass": 15,
        # Class: CfgWeapons\\rhs_6sh92\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3]
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 3,
                "passThrough": 0.6
            },
            # Class: CfgWeapons\\rhs_6sh92\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "armor": 0,
                "passThrough": 0.8
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_altyn_visordown": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_altyn_visordown_ca.paa",
    "displayName": "Altyn (Visor Down)",
    "model": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_altyn_visordown",
    # Class: CfgWeapons\\rhs_altyn_visordown\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_altyn_visordown",
        # Class: CfgWeapons\\rhs_altyn_visordown\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_altyn_visordown\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 6,
                "passThrough": 0.5
            },
            # Class: CfgWeapons\\rhs_altyn_visordown\\ItemInfo\\HitpointsProtectionInfo\\Face [Indent level: 3],
            "Face": {
                "hitpointName": "HitFace",
                "armor": 6,
                "passThrough": 0.5
            }
        },
        "hiddenSelections": ["Camo1"],
        "mass": 40,
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "allowedFacewear": [],
    "hiddenSelections": ["Camo1"],
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_altyn_co.paa"],
    "dlc": "RHS_AFRF",
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_beanie_green": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_beanie_green_ca.paa",
    "displayName": "Beanie",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\beanie_green_co.paa"],
    "dlc": "RHS_AFRF",
    "allowedFacewear": ["",8,"rhs_scarf",1,"G_Aviator",1],
    "Scope": 2,
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_beanie",
    "hiddenSelections": ["Camo1"],
    "descriptionShort": "No Armor",
    # Class: CfgWeapons\\rhs_beanie\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["Camo1"],
        "mass": 5,
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_beanie",
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhs_beanie\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_beanie\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 0,
                "passThrough": 1
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "_generalMacro": "H_HelmetB",
    "weaponPoolAvailable": 1,
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_beret_mp1": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_beret_mp1_ca.paa",
    "displayName": "Beret (MP)",
    "model": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_mp_beret",
    "hiddenSelectionsTextures": ["\\rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_mp_beret_co.paa"],
    # Class: CfgWeapons\\rhs_beret_mp1\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_mp_beret",
        "mass": 5,
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "hiddenSelections": ["Camo1"],
        # Class: CfgWeapons\\rhs_beret_vdv1\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_beret_vdv1\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 0,
                "passThrough": 1
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "allowedFacewear": ["",8,"rhs_scarf",1,"G_Aviator",1],
    "weaponPoolAvailable": 1,
    "hiddenSelections": ["Camo1"],
    "descriptionShort": "No Armor",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_beret_vdv3": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_beret_vdv3_ca.paa",
    "displayName": "Beret (VDV)",
    "hiddenSelectionsTextures": ["\\rhsafrf\\addons\\rhs_infantry2\\gear\\head\\data\\rhs_vdv_beret3_co.paa"],
    "model": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_milp_beret",
    # Class: CfgWeapons\\rhs_beret_milp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_milp_beret",
        "mass": 5,
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "hiddenSelections": ["Camo1"],
        # Class: CfgWeapons\\rhs_beret_vdv1\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_beret_vdv1\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 0,
                "passThrough": 1
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "allowedFacewear": ["",8,"rhs_scarf",1,"G_Aviator",1],
    "weaponPoolAvailable": 1,
    "hiddenSelections": ["Camo1"],
    "descriptionShort": "No Armor",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_Booniehat_digi": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_Booniehat_digi_ca.paa",
    "dlc": "RHS_AFRF",
    "scope": 2,
    "allowedFacewear": ["",7,"rhs_scarf",2,"G_Aviator",1],
    "displayName": "Boonie Hat EMR-Summer",
    "weaponPoolAvailable": 1,
    "model": "A3\\Characters_F\\Common\\booniehat",
    "hiddenSelections": ["camo"],
    "hiddenSelectionsTextures": ["\\rhsafrf\\addons\\rhs_infantry\\Data\\boonie_emr_co.paa"],
    "descriptionShort": "No Armor",
    # Class: CfgWeapons\\rhs_Booniehat_digi\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 10,
        "allowedSlots": [801,901,701,605],
        "uniformModel": "A3\\Characters_F\\Common\\booniehat",
        "modelSides": [6],
        # Class: CfgWeapons\\rhs_Booniehat_digi\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_Booniehat_digi\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 0,
                "passThrough": 1
            }
        },
        "hiddenSelections": ["camo"],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_fieldcap_digi2": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_fieldcap_digi2_ca.paa",
    "displayName": "Field Cap EMR-Summer (Alt)",
    "model": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_fieldcap_digi2",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry2\\data\\rhs_fieldcap_digi2_co.paa"],
    # Class: CfgWeapons\\rhs_fieldcap_digi2\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry2\\gear\\head\\rhs_fieldcap_digi2",
        "hiddenSelections": ["Camo1"],
        "mass": 5,
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhs_fieldcap\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_fieldcap\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 0,
                "passThrough": 1
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "allowedFacewear": ["",8,"rhs_scarf",1,"G_Aviator",1],
    "hiddenSelections": ["Camo1"],
    "descriptionShort": "No Armor",
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_fieldcap_vsr": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_fieldcap_vsr_ca.paa",
    "displayName": "Field Cap VSR",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry2\\data\\6b27_vsr_co.paa"],
    "dlc": "RHS_AFRF",
    "allowedFacewear": ["",8,"rhs_scarf",1,"G_Aviator",1],
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_fieldcap",
    "hiddenSelections": ["Camo1"],
    "descriptionShort": "No Armor",
    # Class: CfgWeapons\\rhs_fieldcap\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["Camo1"],
        "mass": 5,
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_fieldcap",
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhs_fieldcap\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_fieldcap\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 0,
                "passThrough": 1
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_ssh68": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_ssh68_ca.paa",
    "allowedFacewear": ["",8,"rhs_scarf",1,"G_Aviator",1],
    "displayName": "SSh-68",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_ssh68",
    "hiddenSelections": ["camo1"],
    "hiddenSelectionsTextures": ["\\rhsafrf\\addons\\rhs_infantry\\data\\ssh68_co.paa"],
    # Class: CfgWeapons\\rhs_ssh68\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["camo1"],
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_ssh68",
        # Class: CfgWeapons\\rhs_ssh68\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_ssh68\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 2,
                "passThrough": 0.5
            }
        },
        "mass": 40,
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_tsh4": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_tsh4_ca.paa",
    "dlc": "RHS_AFRF",
    "allowedFacewear": ["",3,"rhs_scarf",5,"G_Aviator",2],
    "displayName": "TSh-4",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_tsh4",
    "hiddenSelections": ["camo1"],
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\crew_equip_co.paa"],
    # Class: CfgWeapons\\rhs_tsh4\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 5,
        "hiddenSelections": ["camo1"],
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_tsh4",
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_df15": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_df15_ca.paa",
    "displayName": "DF-15-2",
    # Class: CfgWeapons\\rhs_uniform_df15\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_pilot_base",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_df15_tan": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_df15_tan_ca.paa",
    "displayName": "DF-15-2 (Tan)",
    # Class: CfgWeapons\\rhs_uniform_df15_tan\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_pilot_tan_base",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_emr_patchless": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_emr_patchless_ca.paa",
    "displayName": "EMR-Summer",
    # Class: CfgWeapons\\rhs_uniform_emr_patchless\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_msv_emr_rifleman_patchless",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_flora_patchless": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_flora_patchless_ca.paa",
    "displayName": "Flora",
    # Class: CfgWeapons\\rhs_uniform_flora_patchless\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_msv_rifleman_patchless",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_flora_patchless_alt": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_flora_patchless_alt_ca.paa",
    "displayName": "Flora (Alt.)",
    # Class: CfgWeapons\\rhs_uniform_flora_patchless_alt\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_msv_rifleman_patchless_alt",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_gorka_r_g": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_gorka_r_g_ca.paa",
    "displayName": "Gorka-R (Green)",
    # Class: CfgWeapons\\rhs_uniform_gorka_r_g\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_vdv_gorka_r_g_rifleman",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_gorka_r_y": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_gorka_r_y_ca.paa",
    "displayName": "Gorka-R (Yellow)",
    # Class: CfgWeapons\\rhs_uniform_gorka_r_y\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_vdv_gorka_r_y_rifleman",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_m88_patchless": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_m88_patchless_ca.paa",
    "displayName": "M88",
    # Class: CfgWeapons\\rhs_uniform_m88_patchless\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_msv_rifleman_m88_patchless",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_mflora_patchless": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_mflora_patchless_ca.paa",
    "displayName": "Mountain Flora",
    # Class: CfgWeapons\\rhs_uniform_mflora_patchless\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_msv_mflora_rifleman_patchless",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_vdv_emr": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_vdv_emr_ca.paa",
    "displayName": "EMR-Summer (VDV)",
    # Class: CfgWeapons\\rhs_uniform_vdv_emr\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_vdv_rifleman",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_vdv_emr_des": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_vdv_emr_des_ca.paa",
    "displayName": "EMR-Desert (VDV)",
    # Class: CfgWeapons\\rhs_uniform_vdv_emr_des\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_vdv_des_rifleman",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_vdv_flora": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_vdv_flora_ca.paa",
    "displayName": "Flora (VDV)",
    # Class: CfgWeapons\\rhs_uniform_vdv_flora\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_vdv_flora_rifleman",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_uniform_vmf_flora": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\uniform\\rhs_uniform_vmf_flora_ca.paa",
    "displayName": "Flora (VMF)",
    # Class: CfgWeapons\\rhs_uniform_vmf_flora\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformClass": "rhs_vmf_flora_rifleman",
        "uniformModel": "-",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
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
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_vest_commander": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_vest_commander_ca.paa",
    "dlc": "RHS_AFRF",
    "scope": 2,
    "displayName": "Mapcase and Holster",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_commander",
    "hiddenSelectionsTextures": [],
    "descriptionShort": "No Armor",
    # Class: CfgWeapons\\rhs_vest_commander\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_commander",
        "containerClass": "Supply40",
        "mass": 20,
        # Class: CfgWeapons\\rhs_vest_commander\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_vest_commander\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3]
            "Body": {
                "hitpointName": "HitBody",
                "armor": 0,
                "passThrough": 1
            }
        },
        "hiddenSelections": ["camo"],
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "hiddenSelections": ["camo"],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_vydra_3m": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\vests\\rhs_vydra_3m_ca.paa",
    "dlc": "RHS_AFRF",
    "scope": 2,
    "displayName": "Vydra-3M",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_vydra_3m",
    "hiddenSelectionsTextures": ["rhsafrf\\addons\\rhs_infantry\\data\\crew_equip_co.paa"],
    "descriptionShort": "No Armor",
    # Class: CfgWeapons\\rhs_vydra_3m\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["Camo1"],
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\vests\\rhs_vydra_3m",
        "containerClass": "Supply80",
        "mass": 15,
        # Class: CfgWeapons\\rhs_vydra_3m\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_vydra_3m\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3]
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 3,
                "passThrough": 0.6
            },
            # Class: CfgWeapons\\rhs_vydra_3m\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "armor": 0,
                "passThrough": 0.8
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "_generalMacro": "Vest_Camo_Base",
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "hiddenSelections": ["camo"],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_zsh7a_alt": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_zsh7a_alt_ca.paa",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_zsh7_alt",
    # Class: CfgWeapons\\rhs_zsh7a_alt\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_zsh7_alt",
        "mass": 11,
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "hiddenSelections": ["camo1"],
        "hiddenSelectionsTextures": ["\\rhsafrf\\addons\\rhs_infantry\\data\\rhs_zsh7a_co.paa"],
        # Class: CfgWeapons\\rhs_zsh7a\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_zsh7a\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 2,
                "passThrough": 0.5
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "displayName": "ZSh-7A (KM-35)",
    "hiddenSelections": ["camo1"],
    "hiddenSelectionsTextures": ["\\rhsafrf\\addons\\rhs_infantry\\data\\rhs_zsh7a_co.paa"],
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"rhs_zsh7a_mike_alt": {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf\\addons\\rhs_inventoryicons\\data\\headgear\\rhs_zsh7a_mike_alt_ca.paa",
    "displayName": "ZSh-7A",
    "model": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_zsh7_mike_alt",
    # Class: CfgWeapons\\rhs_zsh7a_mike_alt\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsafrf\\addons\\rhs_infantry\\gear\\head\\rhs_zsh7_mike_alt",
        "mass": 11,
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "hiddenSelections": ["camo1"],
        "hiddenSelectionsTextures": ["\\rhsafrf\\addons\\rhs_infantry\\data\\rhs_zsh7a_co.paa"],
        # Class: CfgWeapons\\rhs_zsh7a\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhs_zsh7a\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 2,
                "passThrough": 0.5
            }
        },
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "dlc": "RHS_AFRF",
    "hiddenSelections": ["camo1"],
    "hiddenSelectionsTextures": ["\\rhsafrf\\addons\\rhs_infantry\\data\\rhs_zsh7a_co.paa"],
    "_generalMacro": "H_HelmetB",
    "scope": 2,
    "weaponPoolAvailable": 1,
    "descriptionShort": "Armor Level II",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"U_O_FullGhillie_ard": {
    "author": "Bohemia Interactive",
    "scope": 2,
    "displayName": "Full Ghillie (Arid) [CSAT]",
    "picture": "A3\\characters_f_mark\\data\\ui\\icon_U_O_FullGhillie_ard_ca.paa",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_universal_F.p3d",
    "hiddenSelections": ["camo"],
    "hiddenSelectionsTextures": ["\\A3\\Characters_F\\Common\\Suitpacks\\data\\suitpack_soldier_opfor_co.paa"],
    # Class: CfgWeapons\\U_O_FullGhillie_ard\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "O_ghillie_ard_F",
        "containerClass": "Supply60",
        "mass": 120,
        "type": 801,
        "scope": 0
    },
    "DLC": "Mark",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"U_O_FullGhillie_lsh": {
    "author": "Bohemia Interactive",
    "scope": 2,
    "displayName": "Full Ghillie (Lush) [CSAT]",
    "picture": "A3\\characters_f_mark\\data\\ui\\icon_U_O_FullGhillie_lsh_ca.paa",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_universal_F.p3d",
    "hiddenSelections": ["camo"],
    "hiddenSelectionsTextures": ["\\A3\\Characters_F\\Common\\Suitpacks\\data\\suitpack_soldier_opfor_co.paa"],
    # Class: CfgWeapons\\U_O_FullGhillie_lsh\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "O_ghillie_lsh_F",
        "containerClass": "Supply60",
        "mass": 120,
        "type": 801,
        "scope": 0
    },
    "DLC": "Mark",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"U_O_FullGhillie_sard": {
    "author": "Bohemia Interactive",
    "scope": 2,
    "displayName": "Full Ghillie (Semi-Arid) [CSAT]",
    "picture": "A3\\characters_f_mark\\data\\ui\\icon_U_O_FullGhillie_sard_ca.paa",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_universal_F.p3d",
    "hiddenSelections": ["camo"],
    "hiddenSelectionsTextures": ["\\A3\\Characters_F\\Common\\Suitpacks\\data\\suitpack_soldier_opfor_co.paa"],
    # Class: CfgWeapons\\U_O_FullGhillie_sard\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "O_ghillie_sard_F",
        "containerClass": "Supply60",
        "mass": 120,
        "type": 801,
        "scope": 0
    },
    "DLC": "Mark",
    "allowedSlots": [901],
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
},
"V_Chestrig_khk": {
    "author": "Bohemia Interactive",
    "_generalMacro": "V_Chestrig_khk",
    "scope": 2,
    "displayName": "Chest Rig (Khaki)",
    "picture": "A3\\characters_f\\Data\\UI\\icon_V_Chestrig_khk_CA.paa",
    "model": "A3\\Characters_F\\Common\\equip_chestrig",
    "hiddenSelections": ["Camo1","Camo2"],
    "hiddenSelectionsTextures": ["\\A3\\Characters_F\\Common\\Data\\equip_chestrig_khk_co.paa","\\A3\\Characters_F\\BLUFOR\\Data\\vests_khk_co.paa"],
    # Class: CfgWeapons\\V_Chestrig_khk\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "A3\\Characters_F\\Common\\equip_chestrig.p3d",
        "containerClass": "Supply140",
        "mass": 20,
        "hiddenSelections": ["camo1","camo2"],
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        # Class: CfgWeapons\\VestItem\\HitpointsProtectionInfo [Indent level: 1],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\VestItem\\HitpointsProtectionInfo\\Body [Indent level: 2]
            "Body": {
                "hitpointName": "HitBody",
                "armor": 0,
                "passThrough": 1
            }
        },
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "descriptionShort": "No Armor",
    "muzzles": [],
    # Class: CfgWeapons\\ItemCore\\Armory [Indent level: 1],
    "Armory": {
        "disabled": 1
    },
    "type": 131072,
    "access": 3,
    "value": 2,
    "uiPicture": "",
    "ammo": "",
    "cursor": "",
    "cursorAim": "",
    "cursorSize": 1,
    "showAimCursorInternal": 1,
    "cursorAimOn": "",
    "laser": 0,
    "hiddenUnderwaterSelections": [],
    "shownUnderwaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    "simulation": "Weapon",
    "nameSound": "",
    "count": 0,
    "multiplier": 1,
    "burst": 1,
    "magazineReloadTime": 0,
    "reloadTime": 1,
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "soundContinuous": 0,
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "drySound": ["",1,1],
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "reloadMagazineSound": ["",1,1],
    "emptySound": ["",1,1],
    "soundBullet": ["emptySound",1],
    "initSpeed": 0,
    "ballisticsComputer": 0,
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
    "canLock": 2,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "modelOptics": "",
    "opticsPPEffects": [],
    "opticsFlare": 1,
    "optics": 1,
    "forceOptics": 0,
    "useAsBinocular": 0,
    "opticsDisablePeripherialVision": 0.67,
    "opticsZoomMin": 0.25,
    "opticsZoomMax": 1.25,
    "opticsZoomInit": 0.75,
    "distanceZoomMin": 400,
    "distanceZoomMax": 400,
    "primary": 10,
    "showSwitchAction": 0,
    "showEmpty": 1,
    "autoFire": 0,
    "autoReload": 1,
    "showToPlayer": 1,
    "canShootInWater": 0,
    "aiRateOfFire": 5,
    "aiRateOfFireDistance": 500,
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\\Default\\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "magazines": [],
    "modes": ["this"],
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
    # Class: CfgWeapons\\Default\\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
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
            # Class: CfgWeapons\\Default\\GunFire\\Table\\T0 [Indent level: 3]
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
            # Class: CfgWeapons\\Default\\GunClouds\\Table\\T0 [Indent level: 3]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1
}