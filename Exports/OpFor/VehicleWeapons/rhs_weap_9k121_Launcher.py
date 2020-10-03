rhs_weap_9k121_Launcher = {
    "airateoffire": 5,
    "airateoffiredistance": 4000,
    "displayname": "9K121M",
    "magazines": ["rhs_mag_apu6_9m127_ka52","rhs_mag_apu6_9m127m_ka52"],
    "canlock": 1,
    "reloadtime": 1.5,
    "weaponlockdelay": 4,
    "modes": ["Single","Burst"],
    # Class: CfgWeapons\rhs_weap_9k121_Launcher\Single [Indent level: 1],
    "Single": {
        "airateoffire": 5,
        "airateoffiredistance": 4000,
        "maxrange": 11500,
        "maxrangeprobab": 0.65,
        "midrange": 4000,
        "midrangeprobab": 0.95,
        "minrange": 50,
        "minrangeprobab": 0.6,
        "reloadtime": 0.05,
        "displayname": "Kh-29L",
        "magazines": ["rhs_mag_kh29l"],
        "canLock": 2,
        "cursor": "missile",
        "cursoraim": "EmptyCursor",
        "cursorsize": 0,
        "weaponLockSystem": 4,
        "weaponLockDelay": 0.5,
        "cmImmunity": 0.3,
        "modes": ["this"],
        # Class: CfgWeapons\rhs_weap_kh25_Launcher\EventHandlers [Indent level: 1],
        "EventHandlers": {
            # Class: CfgWeapons\rhs_weap_kh25_Launcher\EventHandlers\RHS_KlenPS [Indent level: 2]
            "RHS_KlenPS": {
                "fired": "_this call rhs_fnc_klenpsGuide"
            }
        },
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_kh25_Launcher\StandardSound [Indent level: 1],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsafrf|addons|rhs_sounds|atgm|atgm_1",2.35,1,1400],
            "begin2": ["rhsafrf|addons|rhs_sounds|atgm|atgm_2",2.35,1,1400],
            "soundBegin": ["begin1",0.5,"begin2",0.5],
            "soundsetshot": ["RocketsMedium_Shot_SoundSet"]
        },
        "holdsterAnimValue": 3,
        "magazineReloadTime": 0.1,
        "showAimCursorInternal": 0,
        "textureType": "semi",
        "lockingTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.562341,1],
        "lockedTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.562341,2.5],
        # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\Direct [Indent level: 1],
        "Direct": {
            "textureType": "semi",
            "displayName": "Macer",
            "reloadTime": 0.1,
            "magazineReloadTime": 0.1,
            "sounds": ["StandardSound"],
            # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\Direct\StandardSound [Indent level: 2],
            "StandardSound": {
                "begin1": ["A3|Sounds_F_EPC|Weapons|missile_epc_1",1.77828,1,3500],
                "soundBegin": ["begin1",1]
            },
            "lockingTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.562341,1],
            "lockedTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.562341,2.5],
            "minRange": 360,
            "minRangeProbab": 0.4,
            "midRange": 1500,
            "midRangeProbab": 1,
            "maxRange": 8000,
            "maxRangeProbab": 0.95,
            "scope": 1,
            "type": 65536,
            "nameSound": "MissileLauncher",
            "cursor": "EmptyCursor",
            "cursorAim": "missile",
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
            "burst": 1,
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
            "magazines": [],
            "modes": ["this"],
            "useAction": 0,
            "useActionTitle": "",
            "canDrop": 1,
            "weaponLockDelay": 0,
            "weaponLockSystem": 0,
            "cmImmunity": 1,
            "weight": 0,
            "handAnim": [],
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
        # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\TopDown [Indent level: 1],
        "TopDown": {
            "textureType": "topDown",
            "displayName": "Macer",
            "reloadTime": 0.1,
            "magazineReloadTime": 0.1,
            "sounds": ["StandardSound"],
            # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\Direct\StandardSound [Indent level: 2],
            "StandardSound": {
                "begin1": ["A3|Sounds_F_EPC|Weapons|missile_epc_1",1.77828,1,3500],
                "soundBegin": ["begin1",1]
            },
            "lockingTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.562341,1],
            "lockedTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.562341,2.5],
            "minRange": 360,
            "minRangeProbab": 0.4,
            "midRange": 1500,
            "midRangeProbab": 1,
            "maxRange": 8000,
            "maxRangeProbab": 0.95,
            "scope": 1,
            "type": 65536,
            "nameSound": "MissileLauncher",
            "cursor": "EmptyCursor",
            "cursorAim": "missile",
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
            "burst": 1,
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
            "magazines": [],
            "modes": ["this"],
            "useAction": 0,
            "useActionTitle": "",
            "canDrop": 1,
            "weaponLockDelay": 0,
            "weaponLockSystem": 0,
            "cmImmunity": 1,
            "weight": 0,
            "handAnim": [],
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
        "nameSound": "MissileLauncher",
        "dexterity": 0.5,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
        "picture": "",
        "uiPicture": "",
        "ammo": "",
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
        "backgroundReload": 0,
        "reloadAction": "",
        "muzzles": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weight": 0,
        "handAnim": [],
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
    # Class: CfgWeapons\rhs_weap_9k121_Launcher\Burst [Indent level: 1],
    "Burst": {
        "reloadtime": 0.05,
        "multiplier": 1,
        "burst": 2,
        "textureType": "burst",
        "airateoffire": 5,
        "airateoffiredistance": 4000,
        "maxrange": 11500,
        "maxrangeprobab": 0.65,
        "midrange": 4000,
        "midrangeprobab": 0.95,
        "minrange": 50,
        "minrangeprobab": 0.6,
        "displayname": "Kh-29L",
        "magazines": ["rhs_mag_kh29l"],
        "canLock": 2,
        "cursor": "missile",
        "cursoraim": "EmptyCursor",
        "cursorsize": 0,
        "weaponLockSystem": 4,
        "weaponLockDelay": 0.5,
        "cmImmunity": 0.3,
        "modes": ["this"],
        # Class: CfgWeapons\rhs_weap_kh25_Launcher\EventHandlers [Indent level: 1],
        "EventHandlers": {
            # Class: CfgWeapons\rhs_weap_kh25_Launcher\EventHandlers\RHS_KlenPS [Indent level: 2]
            "RHS_KlenPS": {
                "fired": "_this call rhs_fnc_klenpsGuide"
            }
        },
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_kh25_Launcher\StandardSound [Indent level: 1],
        "StandardSound": {
            "weaponSoundEffect": "DefaultRifle",
            "begin1": ["rhsafrf|addons|rhs_sounds|atgm|atgm_1",2.35,1,1400],
            "begin2": ["rhsafrf|addons|rhs_sounds|atgm|atgm_2",2.35,1,1400],
            "soundBegin": ["begin1",0.5,"begin2",0.5],
            "soundsetshot": ["RocketsMedium_Shot_SoundSet"]
        },
        "holdsterAnimValue": 3,
        "magazineReloadTime": 0.1,
        "showAimCursorInternal": 0,
        "lockingTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.562341,1],
        "lockedTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.562341,2.5],
        # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\Direct [Indent level: 1],
        "Direct": {
            "textureType": "semi",
            "displayName": "Macer",
            "reloadTime": 0.1,
            "magazineReloadTime": 0.1,
            "sounds": ["StandardSound"],
            # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\Direct\StandardSound [Indent level: 2],
            "StandardSound": {
                "begin1": ["A3|Sounds_F_EPC|Weapons|missile_epc_1",1.77828,1,3500],
                "soundBegin": ["begin1",1]
            },
            "lockingTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.562341,1],
            "lockedTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.562341,2.5],
            "minRange": 360,
            "minRangeProbab": 0.4,
            "midRange": 1500,
            "midRangeProbab": 1,
            "maxRange": 8000,
            "maxRangeProbab": 0.95,
            "scope": 1,
            "type": 65536,
            "nameSound": "MissileLauncher",
            "cursor": "EmptyCursor",
            "cursorAim": "missile",
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
            "burst": 1,
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
            "magazines": [],
            "modes": ["this"],
            "useAction": 0,
            "useActionTitle": "",
            "canDrop": 1,
            "weaponLockDelay": 0,
            "weaponLockSystem": 0,
            "cmImmunity": 1,
            "weight": 0,
            "handAnim": [],
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
        # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\TopDown [Indent level: 1],
        "TopDown": {
            "textureType": "topDown",
            "displayName": "Macer",
            "reloadTime": 0.1,
            "magazineReloadTime": 0.1,
            "sounds": ["StandardSound"],
            # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\Direct\StandardSound [Indent level: 2],
            "StandardSound": {
                "begin1": ["A3|Sounds_F_EPC|Weapons|missile_epc_1",1.77828,1,3500],
                "soundBegin": ["begin1",1]
            },
            "lockingTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.562341,1],
            "lockedTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.562341,2.5],
            "minRange": 360,
            "minRangeProbab": 0.4,
            "midRange": 1500,
            "midRangeProbab": 1,
            "maxRange": 8000,
            "maxRangeProbab": 0.95,
            "scope": 1,
            "type": 65536,
            "nameSound": "MissileLauncher",
            "cursor": "EmptyCursor",
            "cursorAim": "missile",
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
            "burst": 1,
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
            "magazines": [],
            "modes": ["this"],
            "useAction": 0,
            "useActionTitle": "",
            "canDrop": 1,
            "weaponLockDelay": 0,
            "weaponLockSystem": 0,
            "cmImmunity": 1,
            "weight": 0,
            "handAnim": [],
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
        "nameSound": "MissileLauncher",
        "dexterity": 0.5,
        "count": 1,
        "inertia": 1,
        "access": 3,
        "value": 2,
        "picture": "",
        "uiPicture": "",
        "ammo": "",
        "cursorAimOn": "",
        "laser": 0,
        "hiddenSelections": [],
        "hiddenSelectionsTextures": [],
        "hiddenUnderwaterSelections": [],
        "shownUnderwaterSelections": [],
        "hiddenUnderwaterSelectionsTextures": [],
        "simulation": "Weapon",
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
        "backgroundReload": 0,
        "reloadAction": "",
        "muzzles": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weight": 0,
        "handAnim": [],
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
    "holdsterAnimValue": 1,
    # Class: CfgWeapons\rhs_weap_9k121_Launcher\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "maxrange": 10000,
    "maxrangeprobab": 0.05,
    "midrange": 5000,
    "midrangeprobab": 0.9,
    "minrange": 2000,
    "minrangeprobab": 0.5,
    "cursor": "missile",
    "cursoraim": "EmptyCursor",
    "cursorsize": 0,
    "weaponLockSystem": 4,
    "cmImmunity": 0.3,
    "sounds": ["StandardSound"],
    # Class: CfgWeapons\rhs_weap_kh25_Launcher\StandardSound [Indent level: 1],
    "StandardSound": {
        "weaponSoundEffect": "DefaultRifle",
        "begin1": ["rhsafrf|addons|rhs_sounds|atgm|atgm_1",2.35,1,1400],
        "begin2": ["rhsafrf|addons|rhs_sounds|atgm|atgm_2",2.35,1,1400],
        "soundBegin": ["begin1",0.5,"begin2",0.5],
        "soundsetshot": ["RocketsMedium_Shot_SoundSet"]
    },
    "magazineReloadTime": 0.1,
    "showAimCursorInternal": 0,
    "textureType": "semi",
    "lockingTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.562341,1],
    "lockedTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.562341,2.5],
    # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\Direct [Indent level: 1],
    "Direct": {
        "textureType": "semi",
        "displayName": "Macer",
        "reloadTime": 0.1,
        "magazineReloadTime": 0.1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\Direct\StandardSound [Indent level: 2],
        "StandardSound": {
            "begin1": ["A3|Sounds_F_EPC|Weapons|missile_epc_1",1.77828,1,3500],
            "soundBegin": ["begin1",1]
        },
        "lockingTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.562341,1],
        "lockedTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.562341,2.5],
        "minRange": 360,
        "minRangeProbab": 0.4,
        "midRange": 1500,
        "midRangeProbab": 1,
        "maxRange": 8000,
        "maxRangeProbab": 0.95,
        "scope": 1,
        "type": 65536,
        "nameSound": "MissileLauncher",
        "cursor": "EmptyCursor",
        "cursorAim": "missile",
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
        "burst": 1,
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
        "magazines": [],
        "modes": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockDelay": 0,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "handAnim": [],
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
    # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\TopDown [Indent level: 1],
    "TopDown": {
        "textureType": "topDown",
        "displayName": "Macer",
        "reloadTime": 0.1,
        "magazineReloadTime": 0.1,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\Missile_AGM_02_Plane_CAS_01_F\Direct\StandardSound [Indent level: 2],
        "StandardSound": {
            "begin1": ["A3|Sounds_F_EPC|Weapons|missile_epc_1",1.77828,1,3500],
            "soundBegin": ["begin1",1]
        },
        "lockingTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.562341,1],
        "lockedTargetSound": ["|A3|Sounds_F|weapons|Rockets|locked_3",0.562341,2.5],
        "minRange": 360,
        "minRangeProbab": 0.4,
        "midRange": 1500,
        "midRangeProbab": 1,
        "maxRange": 8000,
        "maxRangeProbab": 0.95,
        "scope": 1,
        "type": 65536,
        "nameSound": "MissileLauncher",
        "cursor": "EmptyCursor",
        "cursorAim": "missile",
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
        "burst": 1,
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
        "magazines": [],
        "modes": ["this"],
        "useAction": 0,
        "useActionTitle": "",
        "canDrop": 1,
        "weaponLockDelay": 0,
        "weaponLockSystem": 0,
        "cmImmunity": 1,
        "weight": 0,
        "handAnim": [],
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
    "nameSound": "MissileLauncher",
    "dexterity": 0.5,
    "count": 1,
    "inertia": 1,
    "access": 3,
    "value": 2,
    "picture": "",
    "uiPicture": "",
    "ammo": "",
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
    "aiDispersionCoefX": 1,
    "aiDispersionCoefY": 1,
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
    "backgroundReload": 0,
    "reloadAction": "",
    "muzzles": ["this"],
    "useAction": 0,
    "useActionTitle": "",
    "canDrop": 1,
    "weight": 0,
    "handAnim": [],
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