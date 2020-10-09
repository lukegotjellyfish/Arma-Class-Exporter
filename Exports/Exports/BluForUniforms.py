"H_Cap_headphones": {
    "author": "Bohemia Interactive",
    "_generalMacro": "H_Cap_headphones",
    "scope": 2,
    "displayName": "Rangemaster Cap",
    "picture": "A3\\Characters_F\\data\\ui\\icon_H_Cap_headphones_khk_CA.paa",
    "model": "A3\\Characters_F\\common\\capb_headphones.p3d",
    "hiddenSelectionsTextures": ["\\a3\\characters_f\\common\\data\\capb_headphones_co.paa"],
    # Class: CfgWeapons\\H_Cap_headphones\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 8,
        "uniformModel": "A3\\Characters_F\\common\\capb_headphones.p3d",
        "modelSides": [6],
        "hiddenSelections": [],
        "allowedSlots": [801,901,701,605],
        # Class: CfgWeapons\\HelmetBase\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\HelmetBase\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "weaponPoolAvailable": 1,
    "hiddenSelections": ["camo"],
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
"rhsgref_alice_webbing": {
    "author": "Red Hammer Studios",
    "picture": "rhsgref\\addons\\rhsgref_inventoryicons\\data\\Vests\\rhsgref_alice_webbing_ca.paa",
    "Scope": 2,
    "dlc": "RHS_GREF",
    "displayName": "ALICE Webbing",
    "hiddenSelections": [],
    "hiddenSelectionsTextures": [],
    "model": "rhsgref\\addons\\rhsgref_infantry\\gear_cdf\\vests\\rhs_alice_webbing",
    "descriptionShort": "No Armor",
    # Class: CfgWeapons\\rhsgref_alice_webbing\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsgref\\addons\\rhsgref_infantry\\gear_cdf\\vests\\rhs_alice_webbing",
        "containerClass": "Supply120",
        "mass": 15,
        # Class: CfgWeapons\\rhsgref_alice_webbing\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsgref_alice_webbing\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3]
            "Body": {
                "hitpointName": "HitBody",
                "armor": 0,
                "passThrough": 1
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
"rhsgref_Booniehat_alpen": {
    "author": "Red Hammer Studios",
    "picture": "rhsgref\\addons\\rhsgref_inventoryicons\\data\\Headgear\\rhsgref_Booniehat_alpen_ca.paa",
    "dlc": "RHS_GREF",
    "scope": 2,
    "displayName": "Booniehat Alpenflage",
    "weaponPoolAvailable": 1,
    "model": "A3\\Characters_F\\Common\\booniehat",
    "hiddenSelections": ["camo"],
    "hiddenSelectionsTextures": ["\\rhsgref\\addons\\rhsgref_infantry\\data_gue\\alpenflage_booniehat_co.paa"],
    # Class: CfgWeapons\\rhsgref_Booniehat_alpen\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 10,
        "allowedSlots": [801,901,701,605],
        "uniformModel": "A3\\Characters_F\\Common\\booniehat",
        "modelSides": [6],
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
"rhsgref_uniform_alpenflage": {
    "author": "Red Hammer Studios",
    "picture": "rhsgref\\addons\\rhsgref_inventoryicons\\data\\uniform\\rhsgref_uniform_alpenflage_ca.paa",
    "scope": 2,
    "dlc": "RHS_GREF",
    "displayName": "M93 (Alpenflage)",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    # Class: CfgWeapons\\rhsgref_uniform_alpenflage\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "rhsgref_nat_alpenflage",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
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
"rhsusf_ach_helmet_camo_ocp": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_ach_helmet_camo_ocp_ca.paa",
    "displayName": "ACH OEF-CP (Netting)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\ach_camo",
    "hiddenSelections": ["Camo","Camo1","Camo2"],
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\rhs_helmet_ach_ocp_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\ach_acc_tan_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\camo_net_co.paa"],
    # Class: CfgWeapons\\rhsusf_ach_helmet_camo_ocp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\ach_camo",
        "hiddenSelections": ["Camo","Camo1","Camo2"],
        "mass": 40,
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "allowedFacewear": ["",7,"rhs_ess_black",2,"rhs_googles_black",1],
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
"rhsusf_ach_helmet_ocp": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_ach_helmet_ocp_ca.paa",
    "displayName": "ACH OEF-CP",
    "allowedFacewear": ["",7,"rhs_ess_black",2,"rhs_googles_black",1],
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\ach_01",
    "hiddenSelections": ["Camo","Camo1"],
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\rhs_helmet_ach_ocp_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\ach_acc_tan_co.paa"],
    # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 40,
        "hiddenSelections": ["Camo","Camo1"],
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\ach_01",
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
"rhsusf_ach_helmet_ucp": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_ach_helmet_ucp_ca.paa",
    "displayName": "ACH UCP",
    "hiddenSelections": ["Camo","Camo1"],
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\rhs_helmet_ach_ucp_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\rhs_helmet_ach_acc_co.paa"],
    "allowedFacewear": ["",7,"rhs_ess_black",2,"rhs_googles_black",1],
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\ach_01",
    # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 40,
        "hiddenSelections": ["Camo","Camo1"],
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\ach_01",
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
"rhsusf_cvc_ess": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_cvc_ess_ca.paa",
    "displayName": "ACVC-H, MK-1697 (Tan/ESS)",
    "allowedFacewear": ["",2,"rhs_googles_black",3,"rhs_googles_clear",1,"rhsusf_shemagh2_tan",4],
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\cvc\\data\\rhs_cvc_alt_co.paa"],
    "model": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\cvc\\rhs_cvc_alt_ess",
    # Class: CfgWeapons\\rhsusf_cvc_ess\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\cvc\\rhs_cvc_alt_ess",
        "hiddenSelections": ["Camo1"],
        "mass": 40,
        "armor": 6,
        "modelSides": [3,1],
        "allowedSlots": [801,901,701,605],
        # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "scope": 2,
    "descriptionshort": "OpsCore FAST Ballistic Helmet",
    "hiddenSelections": ["opscore","comtac","NSW","contour","UNCOV_FLAG","ms2000"],
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
"rhsusf_cvc_green_ess": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_cvc_green_ess_ca.paa",
    "displayName": "ACVC-H, MK-1697 (ESS)",
    "allowedFacewear": ["",2,"rhs_googles_black",3,"rhs_googles_clear",1,"rhsusf_shemagh2_od",4],
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\cvc\\data\\rhs_cvc_green_alt_co.paa"],
    "model": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\cvc\\rhs_cvc_alt_ess",
    # Class: CfgWeapons\\rhsusf_cvc_ess\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\cvc\\rhs_cvc_alt_ess",
        "hiddenSelections": ["Camo1"],
        "mass": 40,
        "armor": 6,
        "modelSides": [3,1],
        "allowedSlots": [801,901,701,605],
        # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "scope": 2,
    "descriptionshort": "OpsCore FAST Ballistic Helmet",
    "hiddenSelections": ["opscore","comtac","NSW","contour","UNCOV_FLAG","ms2000"],
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
"rhsusf_hgu56p_saf": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_hgu56p_saf_ca.paa",
    "displayName": "HGU-56/P (SAF)",
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hgu56\\Data\\rhs_hgu56_saf_co.paa"],
    "model": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hgu56\\rhs_hgu56_visor_mask",
    # Class: CfgWeapons\\rhsusf_hgu56p_saf\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hgu56\\rhs_hgu56",
        "hiddenSelections": ["camo","patches"],
        "mass": 40,
        "armor": 6,
        "modelSides": [3,1],
        "allowedSlots": [801,901,701,605],
        # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "allowedFacewear": [],
    "scope": 2,
    "hiddenSelections": ["camo","patches"],
    "hiddenSelectionsMaterials": ["\\rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hgu56\\Data\\rhs_hgu56.rvmat","\\rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hgu56\\Data\\rhs_hgu56_patches.rvmat"],
    "descriptionshort": "OpsCore FAST Ballistic Helmet",
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
"rhsusf_hgu56p_visor_green": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_hgu56p_visor_green_ca.paa",
    "displayName": "HGU-56/P (Green/Visor)",
    "model": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hgu56\\rhs_hgu56_visor",
    # Class: CfgWeapons\\rhsusf_hgu56p_visor_green\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hgu56\\rhs_hgu56_visor",
        "hiddenSelections": ["camo","patches"],
        "mass": 40,
        "armor": 6,
        "modelSides": [3,1],
        "allowedSlots": [801,901,701,605],
        # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hgu56\\Data\\rhs_hgu56_green_co.paa"],
    "allowedFacewear": [],
    "scope": 2,
    "hiddenSelections": ["camo","patches"],
    "hiddenSelectionsMaterials": ["\\rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hgu56\\Data\\rhs_hgu56.rvmat","\\rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hgu56\\Data\\rhs_hgu56_patches.rvmat"],
    "descriptionshort": "OpsCore FAST Ballistic Helmet",
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
"rhsusf_iotv_ocp": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_iotv_ocp_ca.paa",
    "scope": 2,
    "displayName": "IOTV (OEF-CP)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv",
    "hiddenSelections": ["camo","camob","camo1","camo2"],
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_iotv_ocp_01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv1_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv2_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv3_co.paa"],
    "dlc": "RHS_USAF",
    "descriptionShort": "Armor Level IV",
    # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["camo","camob","camo1","camo2"],
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv",
        "containerClass": "Supply20",
        "mass": 100,
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 12,
                "PassThrough": 0.4
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 28,
                "passThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.1
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
"rhsusf_iotv_ocp_SAW": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_iotv_ocp_SAW_ca.paa",
    "scope": 2,
    "displayName": "IOTV (SAW/OCP)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv_SAW",
    # Class: CfgWeapons\\rhsusf_iotv_ocp_SAW\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv_SAW",
        "containerClass": "Supply150",
        "mass": 140,
        # Class: CfgWeapons\\rhsusf_iotv_ocp_SAW\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_iotv_ocp_SAW\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 12,
                "PassThrough": 0.4
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_SAW\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_SAW\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "28 + 		3",
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_SAW\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 28,
                "passThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_SAW\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.1
            }
        },
        "hiddenSelections": ["camo","camob","camo1","camo2"],
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_USAF",
    "hiddenSelections": ["camo","camob","camo1","camo2"],
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_iotv_ocp_01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv1_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv2_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv3_co.paa"],
    "descriptionShort": "Armor Level IV",
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
"rhsusf_iotv_ocp_Teamleader": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_iotv_ocp_Teamleader_ca.paa",
    "scope": 2,
    "displayName": "IOTV (Teamleader/OCP)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv_Teamleader",
    # Class: CfgWeapons\\rhsusf_iotv_ocp_Teamleader\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv_Teamleader",
        "containerClass": "Supply150",
        "mass": 140,
        # Class: CfgWeapons\\rhsusf_iotv_ocp_Teamleader\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_iotv_ocp_Teamleader\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 12,
                "PassThrough": 0.4
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_Teamleader\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_Teamleader\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "28 + 		3",
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_Teamleader\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 28,
                "passThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_Teamleader\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.1
            }
        },
        "hiddenSelections": ["camo","camob","camo1","camo2"],
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_USAF",
    "hiddenSelections": ["camo","camob","camo1","camo2"],
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_iotv_ocp_01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv1_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv2_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv3_co.paa"],
    "descriptionShort": "Armor Level IV",
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
"rhsusf_iotv_ucp": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_iotv_ucp_ca.paa",
    "displayName": "IOTV (UCP)",
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_iotv_ucp_01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv1_ucp_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv2_ucp_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv3_ucp_co.paa"],
    "scope": 2,
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv",
    "hiddenSelections": ["camo","camob","camo1","camo2"],
    "dlc": "RHS_USAF",
    "descriptionShort": "Armor Level IV",
    # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["camo","camob","camo1","camo2"],
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv",
        "containerClass": "Supply20",
        "mass": 100,
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 12,
                "PassThrough": 0.4
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 28,
                "passThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ocp_base\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.1
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
"rhsusf_iotv_ucp_SAW": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_iotv_ucp_SAW_ca.paa",
    "scope": 2,
    "displayName": "IOTV (SAW/UCP)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv_SAW",
    # Class: CfgWeapons\\rhsusf_iotv_ucp_SAW\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv_SAW",
        "containerClass": "Supply150",
        "mass": 140,
        # Class: CfgWeapons\\rhsusf_iotv_ucp_SAW\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_iotv_ucp_SAW\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 12,
                "PassThrough": 0.4
            },
            # Class: CfgWeapons\\rhsusf_iotv_ucp_SAW\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ucp_SAW\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "28 + 		3",
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ucp_SAW\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 28,
                "passThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ucp_SAW\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.1
            }
        },
        "hiddenSelections": ["camo","camob","camo1","camo2"],
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_iotv_ucp_01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv1_ucp_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv2_ucp_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv3_ucp_co.paa"],
    "dlc": "RHS_USAF",
    "hiddenSelections": ["camo","camob","camo1","camo2"],
    "descriptionShort": "Armor Level IV",
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
"rhsusf_iotv_ucp_Teamleader": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_iotv_ucp_Teamleader_ca.paa",
    "scope": 2,
    "displayName": "IOTV (Teamleader/UCP)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv_Teamleader",
    # Class: CfgWeapons\\rhsusf_iotv_ucp_Teamleader\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_iotv_Teamleader",
        "containerClass": "Supply150",
        "mass": 140,
        # Class: CfgWeapons\\rhsusf_iotv_ucp_Teamleader\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_iotv_ucp_Teamleader\\ItemInfo\\HitpointsProtectionInfo\\Neck [Indent level: 3]
            "Neck": {
                "HitpointName": "HitNeck",
                "armor": 12,
                "PassThrough": 0.4
            },
            # Class: CfgWeapons\\rhsusf_iotv_ucp_Teamleader\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3],
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ucp_Teamleader\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "28 + 		3",
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ucp_Teamleader\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 28,
                "passThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_iotv_ucp_Teamleader\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.1
            }
        },
        "hiddenSelections": ["camo","camob","camo1","camo2"],
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_iotv_ucp_01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv1_ucp_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv2_ucp_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_vest_iotv3_ucp_co.paa"],
    "dlc": "RHS_USAF",
    "hiddenSelections": ["camo","camob","camo1","camo2"],
    "descriptionShort": "Armor Level IV",
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
"rhsusf_lwh_helmet_marpatd_headset": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_lwh_helmet_marpatd_headset_ca.paa",
    "displayName": "LWH MARPAT-D (Headset/ESS)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\lwh_wd_headset",
    "hiddenSelections": ["camo","Camo2"],
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\lwh_d_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\lwh_acc_d_co.paa"],
    # Class: CfgWeapons\\rhsusf_lwh_helmet_marpatd_headset\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\lwh_wd_headset",
        "hiddenSelections": ["camo","Camo2"],
        "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\lwh_d_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\lwh_acc_d_co.paa"],
        "mass": 40,
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhsusf_lwh_helmet_marpatd\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_lwh_helmet_marpatd\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "allowedFacewear": ["",6,"rhs_googles_black",3,"rhs_googles_clear",1],
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
"rhsusf_lwh_helmet_marpatwd_headset": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_lwh_helmet_marpatwd_headset_ca.paa",
    "displayName": "LWH MARPAT-WD (Headset/Tan ESS)",
    "hiddenSelections": ["camo","Camo2"],
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\lwh_wd_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\lwh_acc_d_co.paa"],
    # Class: CfgWeapons\\rhsusf_lwh_helmet_marpatwd_headset\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["camo","Camo2"],
        "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\lwh_wd_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\lwh_acc_d_co.paa"],
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\lwh_wd_headset",
        "mass": 40,
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhsusf_lwh_helmet_marpatd\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_lwh_helmet_marpatd\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\lwh_wd_headset",
    "allowedFacewear": ["",6,"rhs_googles_black",3,"rhs_googles_clear",1],
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
"rhsusf_mbav_mg": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_mbav_mg_ca.paa",
    "displayName": "MBAV (Machinegunner)",
    "model": "rhsusf\\addons\\rhsusf_infantry2\\gear\\vests\\mbav\\mbav_mgunner",
    # Class: CfgWeapons\\rhsusf_mbav_mg\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry2\\gear\\vests\\mbav\\mbav_mgunner",
        "containerClass": "Supply160",
        "hiddenSelections": ["camo","camo2"],
        "mass": 80,
        # Class: CfgWeapons\\rhsusf_mbav_light\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_mbav_light\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3]
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_mbav_light\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "28 + 		3",
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_mbav_light\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.4
            }
        },
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "hiddenSelections": ["camo","camo2"],
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry2\\gear\\vests\\mbav\\data\\mbav_tan_co.paa","rhsusf\\addons\\rhsusf_infantry2\\gear\\vests\\mbav\\data\\mbav_gear_co.paa"],
    "scope": 2,
    "descriptionShort": "Armor Level IV",
    "dlc": "RHS_USAF",
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
"rhsusf_mich_bare_norotos_arc_semi_headset": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_mich_bare_norotos_arc_semi_headset_ca.paa",
    "displayName": "MICH 2000 (Semi-Arid/Norotos/ARC/Headset)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\mich_bare_01_nor1_arc_bowman",
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\bare_mich_norotos_painted_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\mich_acc_painted_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\ach_acc_tan_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\bowman_base_co.paa"],
    # Class: CfgWeapons\\rhsusf_mich_bare_norotos_arc_semi_headset\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\mich_bare_01_nor1_arc_bowman",
        "mass": 40,
        "hiddenSelections": ["Camo","Camo1","Camo2","bowman"],
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhsusf_mich_helmet_marpatwd\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_mich_helmet_marpatwd\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "hiddenSelections": ["Camo","Camo1","Camo2","bowman"],
    "scope": 2,
    "allowedFacewear": ["",6,"rhs_googles_black",3,"rhs_googles_clear",1],
    "_generalMacro": "H_HelmetB",
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
"rhsusf_mich_bare_norotos_tan_headset": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_mich_bare_norotos_tan_headset_ca.paa",
    "displayName": "MICH 2000 (Tan/Norotos/Headset)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\mich_bare_01_nor1_bowman",
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\bare_mich_norotos_tan_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\mich_acc_tan_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\ach_acc_tan_co.paa","\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\bowman_base_co.paa"],
    # Class: CfgWeapons\\rhsusf_mich_bare_norotos_tan_headset\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\mich_bare_01_nor1_bowman",
        "mass": 40,
        "hiddenSelections": ["Camo","Camo1","Camo2","bowman"],
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        # Class: CfgWeapons\\rhsusf_mich_helmet_marpatwd\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_mich_helmet_marpatwd\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "hiddenSelections": ["Camo","Camo1","Camo2","bowman"],
    "scope": 2,
    "allowedFacewear": ["",6,"rhs_googles_black",3,"rhs_googles_clear",1],
    "_generalMacro": "H_HelmetB",
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
"rhsusf_opscore_bk_pelt": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_opscore_bk_pelt_ca.paa",
    "scope": 2,
    "displayName": "FAST Ballistic (Black/Headset)",
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\data\\opscore_blk_co.paa","\\rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\data\\comtac_fg_co.paa"],
    "descriptionshort": "OpsCore FAST Ballistic Helmet",
    "model": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\opscore",
    "hiddenSelections": ["opscore","comtac","NSW","contour","UNCOV_FLAG","ms2000"],
    # Class: CfgWeapons\\rhsusf_opscore_01\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 30,
        "armor": 6,
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\opscore",
        "modelSides": [3,1],
        "hiddenSelections": ["opscore","comtac","NSW","contour","UNCOV_FLAG","ms2000"],
        "allowedSlots": [801,901,701,605],
        # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "allowedFacewear": ["",7,"rhs_ess_black",2,"rhs_googles_black",1],
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
"rhsusf_opscore_mar_fg_pelt": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_opscore_mar_fg_pelt_ca.paa",
    "scope": 2,
    "displayName": "FAST Maritime (Foliage Green/Headset)",
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\data\\maritime_od.paa","rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\data\\od2_co.paa","rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\data\\comtac_fg_co.paa"],
    "descriptionshort": "OpsCore FAST Maritime Helmet",
    "model": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\maritime",
    "hiddenSelections": ["Camo1","Camo2","comtac"],
    # Class: CfgWeapons\\rhsusf_opscore_mar_01\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 30,
        "armor": 6,
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\maritime",
        "modelSides": [3,1],
        "hiddenSelections": ["Camo1","Camo2","comtac"],
        "allowedSlots": [801,901,701,605],
        # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "allowedFacewear": ["",7,"rhs_ess_black",2,"rhs_googles_black",1],
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
"rhsusf_opscore_mar_ut_pelt": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_opscore_mar_ut_pelt_ca.paa",
    "scope": 2,
    "displayName": "FAST Maritime (Urban Tan/Headset)",
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\data\\maritime_tan.paa","rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\data\\tan2_co.paa","rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\data\\comtac_co.paa"],
    "descriptionshort": "OpsCore FAST Maritime Helmet",
    "model": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\maritime",
    "hiddenSelections": ["Camo1","Camo2","comtac"],
    # Class: CfgWeapons\\rhsusf_opscore_mar_01\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 30,
        "armor": 6,
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\opscore\\maritime",
        "modelSides": [3,1],
        "hiddenSelections": ["Camo1","Camo2","comtac"],
        "allowedSlots": [801,901,701,605],
        # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_ach_helmet_ocp\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
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
    "allowedFacewear": ["",7,"rhs_ess_black",2,"rhs_googles_black",1],
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
"rhsusf_patrolcap_ocp": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_patrolcap_ocp_ca.paa",
    "displayName": "Patrol Cap OEF-CP",
    "allowedFacewear": ["",6,"rhs_googles_black",3,"rhs_googles_clear",1],
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\rhsusf_patrolcap",
    "hiddenSelections": [],
    "hiddenSelectionsTextures": [],
    # Class: CfgWeapons\\rhsusf_patrolcap_ocp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 5,
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\rhsusf_patrolcap",
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "hiddenSelections": [],
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
"rhsusf_patrolcap_ucp": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhsusf_patrolcap_ucp_ca.paa",
    "displayName": "Patrol Cap UCP",
    "hiddenSelections": ["camo1"],
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\patrolcap_ucp_co.paa"],
    # Class: CfgWeapons\\rhsusf_patrolcap_ucp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["camo1"],
        "mass": 5,
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\rhsusf_patrolcap",
        "allowedSlots": [801,901,701,605],
        "modelSides": [6],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "type": 605,
        "scope": 0
    },
    "allowedFacewear": ["",6,"rhs_googles_black",3,"rhs_googles_clear",1],
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\head\\rhsusf_patrolcap",
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
"rhsusf_spc": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_spc_ca.paa",
    "scope": 2,
    "displayName": "SPC",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_spc",
    "hiddenSelections": ["camo","camo1","camo2","camo3"],
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_spc01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_spc_gear1_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_spc_gear2_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_usmc_camelbak_co.paa"],
    "descriptionShort": "Armor Level IV",
    # Class: CfgWeapons\\rhsusf_spc\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["camo","camo1","camo2","camo3"],
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_spc",
        "containerClass": "Supply20",
        "mass": 80,
        # Class: CfgWeapons\\rhsusf_spc\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_spc\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3]
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_spc\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_spc\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.4
            }
        },
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_USAF",
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
"rhsusf_spcs_ocp": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_spcs_ocp_ca.paa",
    "scope": 2,
    "displayName": "SPCS (OEF-CP)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_spcs",
    "hiddenSelections": ["camo","camo1","camo2"],
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_spcs_ocp_01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_camelback_ocp_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_gear1_iotv_oCP_co.paa"],
    "descriptionShort": "Armor Level IV",
    # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["camo","camo1","camo2"],
        "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_spcs_ocp_01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_camelback_ocp_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_gear1_iotv_oCP_co.paa"],
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_spcs",
        "containerClass": "Supply140",
        "mass": 100,
        # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3]
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "passThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 12,
                "passThrough": 0.4
            },
            # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.4
            }
        },
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "dlc": "RHS_USAF",
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
"rhsusf_spcs_ucp": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_spcs_ucp_ca.paa",
    "displayName": "SPCS (UCP)",
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_spcs_ucp_01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_camelback_ucp_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_gear1_iotv_UCP_co.paa"],
    # Class: CfgWeapons\\rhsusf_spcs_ucp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_spcs_ucp_01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_camelback_ucp_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_gear1_iotv_UCP_co.paa"],
        "hiddenSelections": ["camo","camo1","camo2"],
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_spcs",
        "containerClass": "Supply140",
        "mass": 100,
        # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3]
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "passThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 12,
                "passThrough": 0.4
            },
            # Class: CfgWeapons\\rhsusf_spcs_ocp\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.4
            }
        },
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "scope": 2,
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_spcs",
    "hiddenSelections": ["camo","camo1","camo2"],
    "descriptionShort": "Armor Level IV",
    "dlc": "RHS_USAF",
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
"rhsusf_spc_teamleader": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\vests\\rhsusf_spc_teamleader_ca.paa",
    "displayName": "SPC (Teamleader)",
    "model": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_spc_teamleader",
    # Class: CfgWeapons\\rhsusf_spc_teamleader\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\rhs_spc_teamleader",
        "containerClass": "Supply160",
        "mass": 120,
        # Class: CfgWeapons\\rhsusf_spc_rifleman\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\rhsusf_spc_rifleman\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3]
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 28,
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_spc_rifleman\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": "28 + 		3",
                "PassThrough": 0.1
            },
            # Class: CfgWeapons\\rhsusf_spc_rifleman\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 3,
                "passThrough": 0.6
            },
            # Class: CfgWeapons\\rhsusf_spc_rifleman\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.4
            }
        },
        "hiddenSelections": ["camo","camo1","camo2","camo3"],
        "armor": 20,
        "descriptionShort": "Armor Level IV",
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "scope": 2,
    "hiddenSelections": ["camo","camo1","camo2","camo3"],
    "hiddenSelectionsTextures": ["rhsusf\\addons\\rhsusf_infantry\\data\\rhs_spc01_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_spc_gear1_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_spc_gear2_co.paa","rhsusf\\addons\\rhsusf_infantry\\gear\\vests\\data\\rhs_usmc_camelbak_co.paa"],
    "descriptionShort": "Armor Level IV",
    "dlc": "RHS_USAF",
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
"rhs_8point_marpatd": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhs_8point_marpatd_ca.paa",
    "scope": 2,
    "displayName": "Utility Cap MARPAT-D",
    "weaponPoolAvailable": 1,
    "allowedFacewear": ["",6,"rhs_googles_black",3,"rhs_googles_clear",1],
    "model": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hats\\8point",
    "hiddenSelections": ["camo"],
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hats\\data\\uniform_bdu_caps_marpatd_co"],
    # Class: CfgWeapons\\rhs_8point_marpatd\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 10,
        "allowedSlots": [801,901,701,605],
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hats\\8point",
        "modelSides": [6],
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
"rhs_8point_marpatwd": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhs_8point_marpatwd_ca.paa",
    "scope": 2,
    "displayName": "Utility Cap MARPAT-WD",
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hats\\data\\uniform_bdu_caps_marpatwd_co"],
    "weaponPoolAvailable": 1,
    "allowedFacewear": ["",6,"rhs_googles_black",3,"rhs_googles_clear",1],
    "model": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hats\\8point",
    "hiddenSelections": ["camo"],
    # Class: CfgWeapons\\rhs_8point_marpatd\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 10,
        "allowedSlots": [801,901,701,605],
        "uniformModel": "rhsusf\\addons\\rhsusf_infantry2\\gear\\head\\hats\\8point",
        "modelSides": [6],
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
"rhs_Booniehat_ucp": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\rhs_Booniehat_ucp_ca.paa",
    "scope": 2,
    "displayName": "Booniehat UCP",
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\booniehat_ucp_co"],
    "model": "A3\\Characters_F\\Common\\booniehat",
    "hiddenSelections": ["camo"],
    "allowedFacewear": ["",6,"rhs_googles_black",3,"rhs_googles_clear",1],
    # Class: CfgWeapons\\rhs_Booniehat_ocp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 10,
        "allowedSlots": [801,901,701,605],
        "uniformModel": "A3\\Characters_F\\Common\\booniehat",
        "modelSides": [6],
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
"RHS_jetpilot_usaf": {
    "author": "Red Hammer Studios",
    "dlc": "RHS_USAF",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\headgear\\RHS_jetpilot_usaf_ca.paa",
    "scope": 2,
    "displayName": "Jet Pilot Helmet",
    "hiddenSelectionsTextures": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\rhs_jetpilot.paa"],
    "hiddenSelectionsMaterials": ["\\rhsusf\\addons\\rhsusf_infantry\\gear\\head\\data\\rhs_jetpilot_helmet.rvmat"],
    "model": "A3\\Characters_F\\Common\\headgear_helmet_pilot",
    # Class: CfgWeapons\\RHS_jetpilot_usaf\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "mass": 50,
        "uniformModel": "A3\\Characters_F\\Common\\headgear_helmet_pilot",
        "modelSides": [1,3],
        # Class: CfgWeapons\\RHS_jetpilot_usaf\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\RHS_jetpilot_usaf\\ItemInfo\\HitpointsProtectionInfo\\Head [Indent level: 3]
            "Head": {
                "hitpointName": "HitHead",
                "armor": 1,
                "passThrough": 0.5
            }
        },
        "hiddenSelections": ["camo"],
        "author": "Bohemia Interactive",
        "_generalMacro": "HeadgearItem",
        "allowedSlots": [901,605],
        "type": 605,
        "scope": 0
    },
    "_generalMacro": "H_HelmetB",
    "weaponPoolAvailable": 1,
    "hiddenSelections": ["camo"],
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
"rhs_uniform_acu_ocp": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\uniform\\rhs_uniform_acu_ocp_ca.paa",
    "dlc": "RHS_USAF",
    "scope": 2,
    "displayName": "Army Combat Uniform (OCP)",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    # Class: CfgWeapons\\rhs_uniform_acu_ocp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "rhsusf_army_acu_ocp_uniform",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
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
"rhs_uniform_acu_ucp": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\uniform\\rhs_uniform_acu_ucp_ca.paa",
    "dlc": "RHS_USAF",
    "scope": 2,
    "displayName": "Army Combat Uniform (UCP)",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    # Class: CfgWeapons\\rhs_uniform_acu_ucp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "rhsusf_army_acu_uniform",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
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
"rhs_uniform_cu_ocp": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\uniform\\rhs_uniform_cu_ocp_ca.paa",
    "dlc": "RHS_USAF",
    "scope": 2,
    "displayName": "Combat Uniform OCP",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    # Class: CfgWeapons\\rhs_uniform_cu_ocp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "rhsusf_army_ocp_crewman",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
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
"rhs_uniform_cu_ucp": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\uniform\\rhs_uniform_cu_ucp_ca.paa",
    "displayName": "Combat Uniform UCP",
    # Class: CfgWeapons\\rhs_uniform_cu_ucp\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "rhsusf_army_ucp_crewman",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_USAF",
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
"rhs_uniform_FROG01_d": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\uniform\\rhs_uniform_FROG01_d_ca.paa",
    "displayName": "FROG MARPAT-D",
    # Class: CfgWeapons\\rhs_uniform_FROG01_d\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "rhsusf_usmc_marpat_d_crewman",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_USAF",
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
"rhs_uniform_FROG01_wd": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\uniform\\rhs_uniform_FROG01_wd_ca.paa",
    "scope": 2,
    "displayName": "FROG MARPAT-WD",
    # Class: CfgWeapons\\rhs_uniform_FROG01_wd\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "rhsusf_usmc_marpat_wd_rifleman",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
    "dlc": "RHS_USAF",
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
"rhs_uniform_g3_blk": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\uniform\\rhs_uniform_g3_blk_ca.paa",
    "dlc": "RHS_USAF",
    "scope": 2,
    "displayName": "G3 Uniform (Black)",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    # Class: CfgWeapons\\rhs_uniform_g3_blk\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "rhsusf_socom_g3_blk_uniform",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
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
"rhs_uniform_g3_rgr": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\uniform\\rhs_uniform_g3_rgr_ca.paa",
    "dlc": "RHS_USAF",
    "scope": 2,
    "displayName": "G3 Uniform (Ranger Green)",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    # Class: CfgWeapons\\rhs_uniform_g3_rgr\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "rhsusf_socom_g3_rgr_uniform",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
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
"rhs_uniform_g3_tan": {
    "author": "Red Hammer Studios",
    "picture": "rhsusf\\addons\\rhsusf_inventoryicons\\data\\uniform\\rhs_uniform_g3_tan_ca.paa",
    "dlc": "RHS_USAF",
    "scope": 2,
    "displayName": "G3 Uniform (Tan)",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_blufor_diver",
    # Class: CfgWeapons\\rhs_uniform_g3_tan\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "rhsusf_socom_g3_tan_uniform",
        "containerClass": "Supply40",
        "mass": 40,
        "type": 801,
        "scope": 0
    },
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
"U_B_HeliPilotCoveralls": {
    "author": "Bohemia Interactive",
    "scope": 2,
    "displayName": "Heli Pilot Coveralls [NATO]",
    "picture": "A3\\characters_f\\data\\ui\\icon_U_B_coveralls_ca.paa",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_civilian_F.p3d",
    "hiddenSelections": ["camo"],
    "hiddenSelectionsTextures": ["\\A3\\Characters_F\\Common\\Data\\coveralls_sage_co.paa"],
    # Class: CfgWeapons\\U_B_HeliPilotCoveralls\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "B_Helipilot_F",
        "containerClass": "Supply40",
        "mass": 60,
        "type": 801,
        "scope": 0
    },
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
"U_B_PilotCoveralls": {
    "author": "Bohemia Interactive",
    "scope": 2,
    "displayName": "Pilot Coveralls [NATO]",
    "picture": "A3\\characters_f\\data\\ui\\icon_U_B_PilotCoveralls_ca.paa",
    "model": "A3\\Characters_F\\Common\\Suitpacks\\suitpack_civilian_F.p3d",
    "hiddenSelections": ["camo"],
    "hiddenSelectionsTextures": ["\\A3\\Characters_F\\Common\\Data\\pilot_suit_nato_co.paa"],
    # Class: CfgWeapons\\U_B_PilotCoveralls\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "-",
        "uniformClass": "B_Pilot_F",
        "containerClass": "Supply60",
        "mass": 80,
        "type": 801,
        "scope": 0
    },
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
    "aimTransitionSpeed": 1,
},
"V_PlateCarrier2_blk": {
    "author": "Bohemia Interactive",
    "_generalMacro": "V_PlateCarrier2_blk",
    "scope": 2,
    "displayName": "Carrier Rig (Black)",
    "picture": "A3\\Characters_F\\data\\ui\\icon_V_plate_carrier_2_blk_CA.paa",
    "hiddenSelections": ["camo"],
    "hiddenSelectionsTextures": ["\\A3\\Characters_F\\BLUFOR\\Data\\vests_blk_co.paa"],
    # Class: CfgWeapons\\V_PlateCarrier2_blk\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "hiddenSelections": ["camo"],
        "uniformModel": "A3\\Characters_F\\BLUFOR\\equip_b_vest01",
        "containerClass": "Supply140",
        "mass": 100,
        # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3]
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 20,
                "PassThrough": 0.2
            },
            # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 20,
                "PassThrough": 0.2
            },
            # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 20,
                "passThrough": 0.2
            },
            # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.2
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
    "model": "A3\\Characters_F\\BLUFOR\\equip_b_vest01.p3d",
    "descriptionShort": "Armor Level IV",
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
"V_PlateCarrier2_rgr": {
    "author": "Bohemia Interactive",
    "_generalMacro": "V_PlateCarrier2_rgr",
    "scope": 2,
    "displayName": "Carrier Rig (Green)",
    "picture": "A3\\characters_f\\Data\\UI\\icon_V_plate_carrier_2_CA.paa",
    "model": "A3\\Characters_F\\BLUFOR\\equip_b_vest01.p3d",
    "descriptionShort": "Armor Level IV",
    # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "A3\\Characters_F\\BLUFOR\\equip_b_vest01",
        "containerClass": "Supply140",
        "mass": 100,
        # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3]
            "Chest": {
                "HitpointName": "HitChest",
                "armor": 20,
                "PassThrough": 0.2
            },
            # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "HitpointName": "HitDiaphragm",
                "armor": 20,
                "PassThrough": 0.2
            },
            # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 20,
                "passThrough": 0.2
            },
            # Class: CfgWeapons\\V_PlateCarrier2_rgr\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.2
            }
        },
        "hiddenSelections": [],
        "author": "Bohemia Interactive",
        "_generalMacro": "VestItem",
        "type": 701,
        "uniformType": "Default",
        "overlaySelectionsInfo": ["Ghillie_hide"],
        "showHolsteredPistol": 0,
        "scope": 0
    },
    "weaponPoolAvailable": 1,
    "allowedSlots": [901],
    "hiddenSelections": [],
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
"V_TacVest_khk": {
    "author": "Bohemia Interactive",
    "_generalMacro": "V_TacVest_khk",
    "scope": 2,
    "displayName": "Tactical Vest (Khaki)",
    "picture": "A3\\characters_f\\Data\\UI\\icon_V_TacVest_khk_CA.paa",
    "model": "A3\\Characters_F\\Common\\equip_tacticalvest",
    "hiddenSelectionsTextures": ["\\A3\\Characters_F\\Common\\Data\\tacticalvest_khaki_co.paa"],
    "descriptionShort": "Armor Level I",
    # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "A3\\Characters_F\\Common\\equip_tacticalvest",
        "containerClass": "Supply100",
        "mass": 40,
        # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3]
            "Chest": {
                "hitpointName": "HitChest",
                "armor": 8,
                "passThrough": 0.5
            },
            # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "hitpointName": "HitDiaphragm",
                "armor": 8,
                "passThrough": 0.5
            },
            # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 8,
                "passThrough": 0.5
            },
            # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.5
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
"V_TacVest_oli": {
    "author": "Bohemia Interactive",
    "_generalMacro": "V_TacVest_oli",
    "displayName": "Tactical Vest (Olive)",
    "picture": "A3\\Characters_F\\data\\ui\\icon_V_TacVest_oli_CA.paa",
    "hiddenSelectionsTextures": ["\\A3\\Characters_F\\Common\\Data\\tacticalvest_olive_co.paa"],
    "scope": 2,
    "model": "A3\\Characters_F\\Common\\equip_tacticalvest",
    "descriptionShort": "Armor Level I",
    # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "uniformModel": "A3\\Characters_F\\Common\\equip_tacticalvest",
        "containerClass": "Supply100",
        "mass": 40,
        # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo\\HitpointsProtectionInfo [Indent level: 2],
        "HitpointsProtectionInfo": {
            # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo\\HitpointsProtectionInfo\\Chest [Indent level: 3]
            "Chest": {
                "hitpointName": "HitChest",
                "armor": 8,
                "passThrough": 0.5
            },
            # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo\\HitpointsProtectionInfo\\Diaphragm [Indent level: 3],
            "Diaphragm": {
                "hitpointName": "HitDiaphragm",
                "armor": 8,
                "passThrough": 0.5
            },
            # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo\\HitpointsProtectionInfo\\Abdomen [Indent level: 3],
            "Abdomen": {
                "hitpointName": "HitAbdomen",
                "armor": 8,
                "passThrough": 0.5
            },
            # Class: CfgWeapons\\V_TacVest_khk\\ItemInfo\\HitpointsProtectionInfo\\Body [Indent level: 3],
            "Body": {
                "hitpointName": "HitBody",
                "passThrough": 0.5
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
    "aimTransitionSpeed": 1
}