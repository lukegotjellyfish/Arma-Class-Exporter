rhs_weap_rshg2 = {
    "author": "Red Hammer Studios",
    "picture": "rhsafrf|addons|rhs_inventoryicons|data|weapons|rhs_weap_rshg2_ca.paa",
    "scope": 2,
    "displayName": "RShG-2",
    "descriptionShort": "Rocket launcher<br/>Caliber: 72.5mm<br/>Type: Single-shot Assault-weapon",
    "magazines": ["rhs_rshg2_mag"],
    "model": "rhsafrf|addons|rhs_weapons|rpg26|rshg2",
    "modelOptics": "-",
    "dispersion": 0.18,
    # Class: CfgWeapons\rhs_weap_rshg2\OpticsModes [Indent level: 1],
    "OpticsModes": {
        # Class: CfgWeapons\rhs_weap_rshg2\OpticsModes\ironsight [Indent level: 2]
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
        # Class: CfgWeapons\rhs_weap_rshg2\OpticsModes\ironsight2 [Indent level: 2],
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
    # Class: CfgWeapons\rhs_weap_rshg2\GunParticles [Indent level: 1],
    "GunParticles": {
        # Class: CfgWeapons\rhs_weap_rshg2\GunParticles\effect1 [Indent level: 2]
        "effect1": {
            "positionName": "konec hlavne",
            "directionName": "usti hlavne",
            "effectName": "RocketBackEffectsRPGNT"
        }
    },
    # Class: CfgWeapons\rhs_weap_rshg2\Library [Indent level: 1],
    "Library": {
        "libTextDesc": "The RShG-2 is a disposable thermobaric rocket launcher derived from the RPG-26."
    },
    # Class: CfgWeapons\rhs_weap_rshg2\ItemInfo [Indent level: 1],
    "ItemInfo": {
        "priority": 3,
        "RMBhint": "RShG-2",
        "onHoverText": "RShG-2"
    },
    # Class: CfgWeapons\rhs_weap_rshg2\WeaponSlotsInfo [Indent level: 1],
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
    "handAnim": ["OFP2_ManSkeleton","|rhsafrf|addons|rhs_c_weapons|anims|RPG26.rtm"],
    "sounds": ["StandardSound"],
    # Class: CfgWeapons\rhs_weap_rpg26\StandardSound [Indent level: 1],
    "StandardSound": {
        "begin1": ["rhsafrf|addons|rhs_sounds|rpg|rpg_1",2.35,1,1100],
        "soundBegin": ["begin1",0.5,"begin2",0.5],
        "weaponSoundEffect": "DefaultRifle",
        "begin2": ["rhsafrf|addons|rhs_sounds|rpg|rpg_2",2.35,1,1100]
    },
    "drySound": ["A3|sounds_f|weapons|other|dry6",0.0316228,1,10],
    "reloadMagazineSound": ["A3|sounds_f|weapons|rockets|titan_reload_final",0.562341,1,50],
    "soundFly": ["A3|sounds_f|weapons|rockets|rocket_fly_1",0.316228,1.5,700],
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
    # Class: CfgWeapons\rhs_weap_rpg26\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
        # Class: CfgWeapons\rhs_weap_rpg26\Eventhandlers\RHS_DisposableWeapon [Indent level: 2]
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
    "UiPicture": "A3|Weapons_F|Data|UI|icon_at_CA.paa",
    "dexterity": 1.7,
    "swayCoef": 0.5,
    "sound": ["A3|Sounds_F|weapons|Launcher|rocket_launcher_5",1,1,800],
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
    }
}