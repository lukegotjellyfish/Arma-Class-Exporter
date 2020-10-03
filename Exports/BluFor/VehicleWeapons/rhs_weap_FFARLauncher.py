rhs_weap_FFARLauncher = {
    "magazines": ["rhs_mag_M151_19","rhs_mag_M151_19_green","rhs_mag_M151_7","rhs_mag_M151_7_green","rhs_mag_M151_7_USAF_LAU131","rhs_mag_M151_21_USAF_LAU131_3","rhs_mag_FFAR_7_USAF","rhs_mag_FFAR_21_USAF_LAU68_3","rhs_mag_FFAR_19_USAF","rhs_mag_FFAR_57_USAF_LAU61_3"],
    "displayName": "Hydra (M151 HE)",
    "modes": ["Far_AI","Single","Two","Four","Eight","Twelve","TwentyFour","Burst"],
    "cursor": "rocket",
    "cursorAim": "EmptyCursor",
    "cursorSize": 0,
    # Class: CfgWeapons\rhs_weap_FFARLauncher\Far_AI [Indent level: 1],
    "Far_AI": {
        "displayName": "Hydra",
        "burst": 1,
        "reloadTime": 0.08,
        "autoFire": 0,
        "showToPlayer": 0,
        "soundBurst": 0,
        "dispersion": 0.011,
        "minRange": 150,
        "minRangeProbab": 0.6,
        "midRange": 600,
        "midRangeProbab": 0.9,
        "maxRange": 2500,
        "maxRangeProbab": 0.12,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_FFARLauncher\Far_AI\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_1",2.4,1,1400],
            "soundBegin": ["begin1",0.5,"begin2",0.5],
            "begin2": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_2",2.4,1,1400]
        },
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursorAim": "rocket",
        "type": 65536,
        "magazineReloadTime": 0.2,
        "canLock": 2,
        "weaponLockDelay": 3,
        "nameSound": "rockets",
        "textureType": "semi",
        "aiDispersionCoefY": 0.5,
        "aiDispersionCoefX": 0.5,
        "dexterity": 0.5,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDistance": 300,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
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
        "multiplier": 1,
        "magazineReloadSwitchPhase": 1,
        "sound": ["",1,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": ["sound",1],
        "soundLoop": ["sound",1],
        "soundContinuous": 0,
        "weaponSoundEffect": "",
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
        "lockAcquire": 1,
        "enableAttack": 1,
        "ffMagnitude": 0,
        "ffFrequency": 1,
        "ffCount": 1,
        "recoil": "empty",
        "recoilProne": "",
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
        "autoReload": 1,
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
        "reloadAction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "handAnim": [],
        "lockingTargetSound": ["",0.000316228,2],
        "lockedTargetSound": ["",0.000316228,6],
        "detectRange": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "fireAnims": [],
        # Class: CfgWeapons\Default\Library [Indent level: 1],
        "Library": {
            "libTextDesc": ""
        },
        "descriptionShort": "",
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
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_FFARLauncher\Burst [Indent level: 1],
    "Burst": {
        "displayName": "ALL",
        "burst": 1,
        "salvo": 2,
        "reloadTime": 0.08,
        "soundContinuous": 0,
        "autoFire": 1,
        "aiDispersionCoefX": 1.5,
        "aiDispersionCoefY": 1,
        "dispersion": 0.012,
        "textureType": "fullAuto",
        "minRange": 1,
        "minRangeProbab": 0.001,
        "midRange": 2,
        "midRangeProbab": 0.001,
        "maxRange": 3,
        "maxRangeProbab": 0.001,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_FFARLauncher\Burst\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_1",2.4,1,1400],
            "soundBegin": ["begin1",0.5,"begin2",0.5],
            "begin2": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_2",2.4,1,1400]
        },
        "soundBurst": 0,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursorAim": "rocket",
        "type": 65536,
        "magazineReloadTime": 0.2,
        "canLock": 2,
        "weaponLockDelay": 3,
        "nameSound": "rockets",
        "dexterity": 0.5,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDistance": 300,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
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
        "multiplier": 1,
        "magazineReloadSwitchPhase": 1,
        "sound": ["",1,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": ["sound",1],
        "soundLoop": ["sound",1],
        "weaponSoundEffect": "",
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
        "lockAcquire": 1,
        "enableAttack": 1,
        "ffMagnitude": 0,
        "ffFrequency": 1,
        "ffCount": 1,
        "recoil": "empty",
        "recoilProne": "",
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
        "autoReload": 1,
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
        "reloadAction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "handAnim": [],
        "lockingTargetSound": ["",0.000316228,2],
        "lockedTargetSound": ["",0.000316228,6],
        "detectRange": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "fireAnims": [],
        # Class: CfgWeapons\Default\Library [Indent level: 1],
        "Library": {
            "libTextDesc": ""
        },
        "descriptionShort": "",
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
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_FFARLauncher\Single [Indent level: 1],
    "Single": {
        "displayName": "1",
        "autoFire": 0,
        "salvo": 1,
        "textureType": "semi",
        "burst": 1,
        "reloadTime": 0.08,
        "soundContinuous": 0,
        "aiDispersionCoefX": 1.5,
        "aiDispersionCoefY": 1,
        "dispersion": 0.012,
        "minRange": 1,
        "minRangeProbab": 0.001,
        "midRange": 2,
        "midRangeProbab": 0.001,
        "maxRange": 3,
        "maxRangeProbab": 0.001,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_FFARLauncher\Burst\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_1",2.4,1,1400],
            "soundBegin": ["begin1",0.5,"begin2",0.5],
            "begin2": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_2",2.4,1,1400]
        },
        "soundBurst": 0,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursorAim": "rocket",
        "type": 65536,
        "magazineReloadTime": 0.2,
        "canLock": 2,
        "weaponLockDelay": 3,
        "nameSound": "rockets",
        "dexterity": 0.5,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDistance": 300,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
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
        "multiplier": 1,
        "magazineReloadSwitchPhase": 1,
        "sound": ["",1,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": ["sound",1],
        "soundLoop": ["sound",1],
        "weaponSoundEffect": "",
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
        "lockAcquire": 1,
        "enableAttack": 1,
        "ffMagnitude": 0,
        "ffFrequency": 1,
        "ffCount": 1,
        "recoil": "empty",
        "recoilProne": "",
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
        "autoReload": 1,
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
        "reloadAction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "handAnim": [],
        "lockingTargetSound": ["",0.000316228,2],
        "lockedTargetSound": ["",0.000316228,6],
        "detectRange": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "fireAnims": [],
        # Class: CfgWeapons\Default\Library [Indent level: 1],
        "Library": {
            "libTextDesc": ""
        },
        "descriptionShort": "",
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
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_FFARLauncher\Two [Indent level: 1],
    "Two": {
        "displayName": "2",
        "salvo": 2,
        "burst": 1,
        "autoFire": 0,
        "textureType": "semi",
        "reloadTime": 0.08,
        "soundContinuous": 0,
        "aiDispersionCoefX": 1.5,
        "aiDispersionCoefY": 1,
        "dispersion": 0.012,
        "minRange": 1,
        "minRangeProbab": 0.001,
        "midRange": 2,
        "midRangeProbab": 0.001,
        "maxRange": 3,
        "maxRangeProbab": 0.001,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_FFARLauncher\Burst\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_1",2.4,1,1400],
            "soundBegin": ["begin1",0.5,"begin2",0.5],
            "begin2": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_2",2.4,1,1400]
        },
        "soundBurst": 0,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursorAim": "rocket",
        "type": 65536,
        "magazineReloadTime": 0.2,
        "canLock": 2,
        "weaponLockDelay": 3,
        "nameSound": "rockets",
        "dexterity": 0.5,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDistance": 300,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
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
        "multiplier": 1,
        "magazineReloadSwitchPhase": 1,
        "sound": ["",1,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": ["sound",1],
        "soundLoop": ["sound",1],
        "weaponSoundEffect": "",
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
        "lockAcquire": 1,
        "enableAttack": 1,
        "ffMagnitude": 0,
        "ffFrequency": 1,
        "ffCount": 1,
        "recoil": "empty",
        "recoilProne": "",
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
        "autoReload": 1,
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
        "reloadAction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "handAnim": [],
        "lockingTargetSound": ["",0.000316228,2],
        "lockedTargetSound": ["",0.000316228,6],
        "detectRange": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "fireAnims": [],
        # Class: CfgWeapons\Default\Library [Indent level: 1],
        "Library": {
            "libTextDesc": ""
        },
        "descriptionShort": "",
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
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_FFARLauncher\Four [Indent level: 1],
    "Four": {
        "displayName": "4",
        "salvo": 2,
        "burst": 2,
        "autoFire": 0,
        "textureType": "semi",
        "reloadTime": 0.08,
        "soundContinuous": 0,
        "aiDispersionCoefX": 1.5,
        "aiDispersionCoefY": 1,
        "dispersion": 0.012,
        "minRange": 1,
        "minRangeProbab": 0.001,
        "midRange": 2,
        "midRangeProbab": 0.001,
        "maxRange": 3,
        "maxRangeProbab": 0.001,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_FFARLauncher\Burst\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_1",2.4,1,1400],
            "soundBegin": ["begin1",0.5,"begin2",0.5],
            "begin2": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_2",2.4,1,1400]
        },
        "soundBurst": 0,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursorAim": "rocket",
        "type": 65536,
        "magazineReloadTime": 0.2,
        "canLock": 2,
        "weaponLockDelay": 3,
        "nameSound": "rockets",
        "dexterity": 0.5,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDistance": 300,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
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
        "multiplier": 1,
        "magazineReloadSwitchPhase": 1,
        "sound": ["",1,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": ["sound",1],
        "soundLoop": ["sound",1],
        "weaponSoundEffect": "",
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
        "lockAcquire": 1,
        "enableAttack": 1,
        "ffMagnitude": 0,
        "ffFrequency": 1,
        "ffCount": 1,
        "recoil": "empty",
        "recoilProne": "",
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
        "autoReload": 1,
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
        "reloadAction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "handAnim": [],
        "lockingTargetSound": ["",0.000316228,2],
        "lockedTargetSound": ["",0.000316228,6],
        "detectRange": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "fireAnims": [],
        # Class: CfgWeapons\Default\Library [Indent level: 1],
        "Library": {
            "libTextDesc": ""
        },
        "descriptionShort": "",
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
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_FFARLauncher\Eight [Indent level: 1],
    "Eight": {
        "displayName": "8",
        "burst": 8,
        "salvo": 2,
        "autoFire": 0,
        "textureType": "semi",
        "reloadTime": 0.08,
        "soundContinuous": 0,
        "aiDispersionCoefX": 1.5,
        "aiDispersionCoefY": 1,
        "dispersion": 0.012,
        "minRange": 1,
        "minRangeProbab": 0.001,
        "midRange": 2,
        "midRangeProbab": 0.001,
        "maxRange": 3,
        "maxRangeProbab": 0.001,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_FFARLauncher\Burst\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_1",2.4,1,1400],
            "soundBegin": ["begin1",0.5,"begin2",0.5],
            "begin2": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_2",2.4,1,1400]
        },
        "soundBurst": 0,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursorAim": "rocket",
        "type": 65536,
        "magazineReloadTime": 0.2,
        "canLock": 2,
        "weaponLockDelay": 3,
        "nameSound": "rockets",
        "dexterity": 0.5,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDistance": 300,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
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
        "multiplier": 1,
        "magazineReloadSwitchPhase": 1,
        "sound": ["",1,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": ["sound",1],
        "soundLoop": ["sound",1],
        "weaponSoundEffect": "",
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
        "lockAcquire": 1,
        "enableAttack": 1,
        "ffMagnitude": 0,
        "ffFrequency": 1,
        "ffCount": 1,
        "recoil": "empty",
        "recoilProne": "",
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
        "autoReload": 1,
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
        "reloadAction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "handAnim": [],
        "lockingTargetSound": ["",0.000316228,2],
        "lockedTargetSound": ["",0.000316228,6],
        "detectRange": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "fireAnims": [],
        # Class: CfgWeapons\Default\Library [Indent level: 1],
        "Library": {
            "libTextDesc": ""
        },
        "descriptionShort": "",
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
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_FFARLauncher\Twelve [Indent level: 1],
    "Twelve": {
        "displayName": "12",
        "burst": 12,
        "salvo": 2,
        "autoFire": 0,
        "textureType": "semi",
        "reloadTime": 0.08,
        "soundContinuous": 0,
        "aiDispersionCoefX": 1.5,
        "aiDispersionCoefY": 1,
        "dispersion": 0.012,
        "minRange": 1,
        "minRangeProbab": 0.001,
        "midRange": 2,
        "midRangeProbab": 0.001,
        "maxRange": 3,
        "maxRangeProbab": 0.001,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_FFARLauncher\Burst\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_1",2.4,1,1400],
            "soundBegin": ["begin1",0.5,"begin2",0.5],
            "begin2": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_2",2.4,1,1400]
        },
        "soundBurst": 0,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursorAim": "rocket",
        "type": 65536,
        "magazineReloadTime": 0.2,
        "canLock": 2,
        "weaponLockDelay": 3,
        "nameSound": "rockets",
        "dexterity": 0.5,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDistance": 300,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
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
        "multiplier": 1,
        "magazineReloadSwitchPhase": 1,
        "sound": ["",1,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": ["sound",1],
        "soundLoop": ["sound",1],
        "weaponSoundEffect": "",
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
        "lockAcquire": 1,
        "enableAttack": 1,
        "ffMagnitude": 0,
        "ffFrequency": 1,
        "ffCount": 1,
        "recoil": "empty",
        "recoilProne": "",
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
        "autoReload": 1,
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
        "reloadAction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "handAnim": [],
        "lockingTargetSound": ["",0.000316228,2],
        "lockedTargetSound": ["",0.000316228,6],
        "detectRange": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "fireAnims": [],
        # Class: CfgWeapons\Default\Library [Indent level: 1],
        "Library": {
            "libTextDesc": ""
        },
        "descriptionShort": "",
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
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_FFARLauncher\TwentyFour [Indent level: 1],
    "TwentyFour": {
        "displayName": "24",
        "burst": 24,
        "salvo": 2,
        "autoFire": 0,
        "textureType": "semi",
        "reloadTime": 0.08,
        "soundContinuous": 0,
        "aiDispersionCoefX": 1.5,
        "aiDispersionCoefY": 1,
        "dispersion": 0.012,
        "minRange": 1,
        "minRangeProbab": 0.001,
        "midRange": 2,
        "midRangeProbab": 0.001,
        "maxRange": 3,
        "maxRangeProbab": 0.001,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_FFARLauncher\Burst\StandardSound [Indent level: 2],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_1",2.4,1,1400],
            "soundBegin": ["begin1",0.5,"begin2",0.5],
            "begin2": ["rhsusf|addons|rhsusf_sounds|launcher_small|launcher_small_2",2.4,1,1400]
        },
        "soundBurst": 0,
        "scope": 1,
        "cursor": "EmptyCursor",
        "cursorAim": "rocket",
        "type": 65536,
        "magazineReloadTime": 0.2,
        "canLock": 2,
        "weaponLockDelay": 3,
        "nameSound": "rockets",
        "dexterity": 0.5,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDistance": 300,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
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
        "multiplier": 1,
        "magazineReloadSwitchPhase": 1,
        "sound": ["",1,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": ["sound",1],
        "soundLoop": ["sound",1],
        "weaponSoundEffect": "",
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
        "lockAcquire": 1,
        "enableAttack": 1,
        "ffMagnitude": 0,
        "ffFrequency": 1,
        "ffCount": 1,
        "recoil": "empty",
        "recoilProne": "",
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
        "autoReload": 1,
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
        "reloadAction": "",
        "muzzles": ["this"],
        "magazines": [],
        "modes": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "handAnim": [],
        "lockingTargetSound": ["",0.000316228,2],
        "lockedTargetSound": ["",0.000316228,6],
        "detectRange": 0,
        "artilleryDispersion": 1,
        "artilleryCharge": 1,
        "fireAnims": [],
        # Class: CfgWeapons\Default\Library [Indent level: 1],
        "Library": {
            "libTextDesc": ""
        },
        "descriptionShort": "",
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
        "aimTransitionSpeed": 1
    },
    "scope": 1,
    "type": 65536,
    "reloadTime": 0.2,
    "magazineReloadTime": 0.2,
    "minRange": 50,
    "minRangeProbab": 0.1,
    "midRange": 600,
    "midRangeProbab": 0.25,
    "maxRange": 2500,
    "maxRangeProbab": 0.05,
    "canLock": 2,
    "weaponLockDelay": 3,
    "nameSound": "rockets",
    "textureType": "semi",
    "aiDispersionCoefY": 0.5,
    "aiDispersionCoefX": 0.5,
    "dexterity": 0.5,
    "aiRateOfFire": 0.5,
    "aiRateOfFireDistance": 300,
    "count": 1,
    "inertia": 1,
    "access": 3,
    "value": 2,
    "picture": "",
    "uiPicture": "",
    "ammo": "",
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
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    "recoil": "empty",
    "recoilProne": "",
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
    "aiRateOfFireDispersion": 0,
    "fireLightDuration": 0.05,
    "fireLightIntensity": 0.2,
    "fireLightDiffuse": [0.937,0.631,0.259],
    "fireLightAmbient": [0,0,0],
    # Class: CfgWeapons\Default\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "muzzles": ["this"],
    "useAction": 0,
    "useActionTitle": "",
    "canDrop": 1,
    "weaponLockSystem": 0,
    "cmImmunity": 1,
    "weight": 0,
    "handAnim": [],
    "lockingTargetSound": ["",0.000316228,2],
    "lockedTargetSound": ["",0.000316228,6],
    "detectRange": 0,
    "artilleryDispersion": 1,
    "artilleryCharge": 1,
    "fireAnims": [],
    # Class: CfgWeapons\Default\Library [Indent level: 1],
    "Library": {
        "libTextDesc": ""
    },
    "descriptionShort": "",
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
    "aimTransitionSpeed": 1,
}