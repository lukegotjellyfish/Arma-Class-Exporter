RHS_M2_M1117 = {
    # Class: CfgWeapons\RHS_M2_M1117\GunParticles [Indent level: 1]    "GunParticles": {        # Class: CfgWeapons\RHS_M2_M1117\GunParticles\effect1 [Indent level: 2]        "effect1": {            "positionname": "kulas",            "directionname": "ZaslehKulas",            "effectname": "MachineGunCloud"
        },        # Class: CfgWeapons\RHS_M2_M1117\GunParticles\RHSUSF_BarrelRefract [Indent level: 2],        "RHSUSF_BarrelRefract": {            "effectName": "RHSUSF_BarrelRefractHeavy",            "positionname": "kulas",            "directionname": "ZaslehKulas"
        }
    },
    "type": 1,
    "ballisticsComputer": 2,
    "canLock": 0,
    "initspeed": 0,
    "cursor": "EmptyCursor",
    "cursoraimon": "EmptyCursor",
    "magazines": ["rhs_mag_100rnd_127x99_mag","rhs_mag_100rnd_127x99_mag_Tracer_Red","rhs_mag_100rnd_127x99_mag_Tracer_Green","rhs_mag_100rnd_127x99_mag_Tracer_Yellow","rhs_mag_100rnd_127x99_SLAP_mag","rhs_mag_100rnd_127x99_SLAP_mag_Tracer_Red","rhs_mag_100rnd_127x99_SLAP_mag_Tracer_Green","rhs_mag_100rnd_127x99_SLAP_mag_Tracer_Yellow","rhs_mag_200rnd_127x99_mag","rhs_mag_200rnd_127x99_mag_Tracer_Red","rhs_mag_200rnd_127x99_SLAP_mag","rhs_mag_200rnd_127x99_SLAP_mag_Tracer_Red"],
    # Class: CfgWeapons\RHS_M2\manual [Indent level: 1],
    "manual": {
        # Class: CfgWeapons\RHS_M2\manual\StandardSound [Indent level: 2]
        "StandardSound": {
            "soundSetShot": ["RHSUSF_veh_m2_Shot_SoundSet","RHSUSF_veh_m2_int_Shot_SoundSet","RHSUSF_veh_rifle2_Tail_SoundSet"]
        },
        "dispersion": 0.00144,
        "reloadTime": 0.1,
        "sounds": ["StandardSound"],
        "soundContinuous": 0,
        "soundBurst": 0,
        "displayName": "12.7mm HMG",
        "aiRateOfFire": 1,
        "aiRateOfFireDistance": 10,
        "minRange": 0,
        "minRangeProbab": 0.01,
        "midRange": 1,
        "midRangeProbab": 0.01,
        "maxRange": 2,
        "maxRangeProbab": 0.01,
        "type": 65536,
        "cursor": "EmptyCursor",
        "cursoraim": "mg",
        "nameSound": "mgun",
        "autoFire": 1,
        "reloadAction": "ManActReloadMagazine",
        "reloadMagazineSound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
        "initSpeed": 0,
        "flash": "gunfire",
        "flashSize": 0.5,
        "optics": 0,
        "textureType": "fullAuto",
        "dexterity": 0.5,
        "inertia": 0.7,
        "access": 3,
        "scope": 0,
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
        "count": 0,
        "multiplier": 1,
        "burst": 1,
        "magazineReloadTime": 0,
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
        "emptySound": ["",1,1],
        "soundBullet": ["emptySound",1],
        "ballisticsComputer": 0,
        "irDistance": 0,
        "irDotIntensity": 0.001,
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
    # Class: CfgWeapons\RHS_M2\close [Indent level: 1],
    "close": {
        # Class: CfgWeapons\RHS_M2\close\StandardSound [Indent level: 2]
        "StandardSound": {
            "soundSetShot": ["RHSUSF_veh_m2_Shot_SoundSet","RHSUSF_veh_m2_int_Shot_SoundSet","RHSUSF_veh_rifle2_Tail_SoundSet"]
        },
        "aiBurstTerminable": 1,
        "showToPlayer": 0,
        "burst": 6,
        "burstRangeMax": 20,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDispersion": 1.5,
        "aiRateOfFireDistance": 50,
        "minRange": 0,
        "minRangeProbab": 0.7,
        "midRange": 100,
        "midRangeProbab": 0.7,
        "maxRange": 200,
        "maxRangeProbab": 0.2,
        "dispersion": 0.00144,
        "reloadTime": 0.1,
        "sounds": ["StandardSound"],
        "soundContinuous": 0,
        "soundBurst": 0,
        "displayName": "12.7mm HMG",
        "type": 65536,
        "cursor": "EmptyCursor",
        "cursoraim": "mg",
        "nameSound": "mgun",
        "autoFire": 1,
        "reloadAction": "ManActReloadMagazine",
        "reloadMagazineSound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
        "initSpeed": 0,
        "flash": "gunfire",
        "flashSize": 0.5,
        "optics": 0,
        "textureType": "fullAuto",
        "dexterity": 0.5,
        "inertia": 0.7,
        "access": 3,
        "scope": 0,
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
        "count": 0,
        "multiplier": 1,
        "magazineReloadTime": 0,
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
        "emptySound": ["",1,1],
        "soundBullet": ["emptySound",1],
        "ballisticsComputer": 0,
        "irDistance": 0,
        "irDotIntensity": 0.001,
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
        "fireLightDuration": 0.05,
        "fireLightIntensity": 0.2,
        "fireLightDiffuse": [0.937,0.631,0.259],
        "fireLightAmbient": [0,0,0],
        # Class: CfgWeapons\Default\Eventhandlers [Indent level: 1],
        "Eventhandlers": {
        },
        "backgroundReload": 0,
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
    # Class: CfgWeapons\RHS_M2\short [Indent level: 1],
    "short": {
        # Class: CfgWeapons\RHS_M2\short\StandardSound [Indent level: 2]
        "StandardSound": {
            "soundSetShot": ["RHSUSF_veh_m2_Shot_SoundSet","RHSUSF_veh_m2_int_Shot_SoundSet","RHSUSF_veh_rifle2_Tail_SoundSet"]
        },
        "aiBurstTerminable": 1,
        "showToPlayer": 0,
        "burst": 6,
        "burstRangeMax": 16,
        "aiRateOfFire": 1,
        "aiRateOfFireDispersion": 2,
        "aiRateOfFireDistance": 150,
        "minRange": 100,
        "minRangeProbab": 0.7,
        "midRange": 300,
        "midRangeProbab": 0.75,
        "maxRange": 600,
        "maxRangeProbab": 0.2,
        "dispersion": 0.00144,
        "reloadTime": 0.1,
        "sounds": ["StandardSound"],
        "soundContinuous": 0,
        "soundBurst": 0,
        "displayName": "12.7mm HMG",
        "type": 65536,
        "cursor": "EmptyCursor",
        "cursoraim": "mg",
        "nameSound": "mgun",
        "autoFire": 1,
        "reloadAction": "ManActReloadMagazine",
        "reloadMagazineSound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
        "initSpeed": 0,
        "flash": "gunfire",
        "flashSize": 0.5,
        "optics": 0,
        "textureType": "fullAuto",
        "dexterity": 0.5,
        "inertia": 0.7,
        "access": 3,
        "scope": 0,
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
        "count": 0,
        "multiplier": 1,
        "magazineReloadTime": 0,
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
        "emptySound": ["",1,1],
        "soundBullet": ["emptySound",1],
        "ballisticsComputer": 0,
        "irDistance": 0,
        "irDotIntensity": 0.001,
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
        "fireLightDuration": 0.05,
        "fireLightIntensity": 0.2,
        "fireLightDiffuse": [0.937,0.631,0.259],
        "fireLightAmbient": [0,0,0],
        # Class: CfgWeapons\Default\Eventhandlers [Indent level: 1],
        "Eventhandlers": {
        },
        "backgroundReload": 0,
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
    # Class: CfgWeapons\RHS_M2\medium [Indent level: 1],
    "medium": {
        # Class: CfgWeapons\RHS_M2\medium\StandardSound [Indent level: 2]
        "StandardSound": {
            "soundSetShot": ["RHSUSF_veh_m2_Shot_SoundSet","RHSUSF_veh_m2_int_Shot_SoundSet","RHSUSF_veh_rifle2_Tail_SoundSet"]
        },
        "aiBurstTerminable": 1,
        "showToPlayer": 0,
        "burst": 4,
        "burstRangeMax": 12,
        "aiRateOfFire": 2,
        "aiRateOfFireDispersion": 2,
        "aiRateOfFireDistance": 300,
        "minRange": 300,
        "minRangeProbab": 0.75,
        "midRange": 600,
        "midRangeProbab": 0.7,
        "maxRange": 800,
        "maxRangeProbab": 0.2,
        "dispersion": 0.00144,
        "reloadTime": 0.1,
        "sounds": ["StandardSound"],
        "soundContinuous": 0,
        "soundBurst": 0,
        "displayName": "12.7mm HMG",
        "type": 65536,
        "cursor": "EmptyCursor",
        "cursoraim": "mg",
        "nameSound": "mgun",
        "autoFire": 1,
        "reloadAction": "ManActReloadMagazine",
        "reloadMagazineSound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
        "initSpeed": 0,
        "flash": "gunfire",
        "flashSize": 0.5,
        "optics": 0,
        "textureType": "fullAuto",
        "dexterity": 0.5,
        "inertia": 0.7,
        "access": 3,
        "scope": 0,
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
        "count": 0,
        "multiplier": 1,
        "magazineReloadTime": 0,
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
        "emptySound": ["",1,1],
        "soundBullet": ["emptySound",1],
        "ballisticsComputer": 0,
        "irDistance": 0,
        "irDotIntensity": 0.001,
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
        "fireLightDuration": 0.05,
        "fireLightIntensity": 0.2,
        "fireLightDiffuse": [0.937,0.631,0.259],
        "fireLightAmbient": [0,0,0],
        # Class: CfgWeapons\Default\Eventhandlers [Indent level: 1],
        "Eventhandlers": {
        },
        "backgroundReload": 0,
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
    # Class: CfgWeapons\RHS_M2\far [Indent level: 1],
    "far": {
        # Class: CfgWeapons\RHS_M2\far\StandardSound [Indent level: 2]
        "StandardSound": {
            "soundSetShot": ["RHSUSF_veh_m2_Shot_SoundSet","RHSUSF_veh_m2_int_Shot_SoundSet","RHSUSF_veh_rifle2_Tail_SoundSet"]
        },
        "aiBurstTerminable": 1,
        "showToPlayer": 0,
        "burst": 3,
        "burstRangeMax": 12,
        "aiRateOfFire": 4,
        "aiRateOfFireDispersion": 4,
        "aiRateOfFireDistance": 600,
        "minRange": 600,
        "minRangeProbab": 0.65,
        "midRange": 1000,
        "midRangeProbab": 0.25,
        "maxRange": 1500,
        "maxRangeProbab": 0.05,
        "dispersion": 0.00144,
        "reloadTime": 0.1,
        "sounds": ["StandardSound"],
        "soundContinuous": 0,
        "soundBurst": 0,
        "displayName": "12.7mm HMG",
        "type": 65536,
        "cursor": "EmptyCursor",
        "cursoraim": "mg",
        "nameSound": "mgun",
        "autoFire": 1,
        "reloadAction": "ManActReloadMagazine",
        "reloadMagazineSound": ["A3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",10,1,20],
        "initSpeed": 0,
        "flash": "gunfire",
        "flashSize": 0.5,
        "optics": 0,
        "textureType": "fullAuto",
        "dexterity": 0.5,
        "inertia": 0.7,
        "access": 3,
        "scope": 0,
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
        "count": 0,
        "multiplier": 1,
        "magazineReloadTime": 0,
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
        "emptySound": ["",1,1],
        "soundBullet": ["emptySound",1],
        "ballisticsComputer": 0,
        "irDistance": 0,
        "irDotIntensity": 0.001,
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
        "fireLightDuration": 0.05,
        "fireLightIntensity": 0.2,
        "fireLightDiffuse": [0.937,0.631,0.259],
        "fireLightAmbient": [0,0,0],
        # Class: CfgWeapons\Default\Eventhandlers [Indent level: 1],
        "Eventhandlers": {
        },
        "backgroundReload": 0,
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
    "reloadMagazineSound": ["a3|Sounds_F|arsenal|weapons_static|Static_HMG|reload_static_HMG",1,1,10],
    "displayName": "M2 HMG .50",
    "magazineReloadTime": 10,
    "aiDispersionCoefY": 5,
    "aiDispersionCoefX": 6,
    "drySound": ["A3|Sounds_F|arsenal|weapons_vehicles|HMG_050|HMG050_dry",1,1,10],
    "showAimCursorInternal": 1,
    "scope": 1,
    "maxZeroing": 2000,
    # Class: CfgWeapons\LMG_RCWS\GunClouds [Indent level: 1],
    "GunClouds": {
    },
    "bullet1": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Metal_01",0.281838,1,10],
    "bullet2": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Metal_02",0.281838,1,10],
    "bullet3": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Metal_03",0.281838,1,10],
    "bullet4": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Metal_04",0.281838,1,10],
    "bullet5": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Dirt_01",0.281838,1,10],
    "bullet6": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Dirt_02",0.281838,1,10],
    "bullet7": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Dirt_03",0.281838,1,10],
    "bullet8": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Dirt_04",0.281838,1,10],
    "bullet9": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Grass_01",0.281838,1,10],
    "bullet10": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Grass_02",0.281838,1,10],
    "bullet11": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Grass_03",0.281838,1,10],
    "bullet12": ["A3|sounds_f|weapons|shells|5_56|Shellcase_556_Grass_04",0.281838,1,10],
    "soundBullet": ["bullet1",0.08,"bullet2",0.084,"bullet3",0.084,"bullet4",0.084,"bullet5",0.093,"bullet6",0.093,"bullet7",0.074,"bullet8",0.074,"bullet9",0.084,"bullet10",0.085,"bullet11",0.083,"bullet12",0.083],
    "modes": ["manual","close","short","medium","far"],
    "FCSMaxLeadSpeed": 0,
    "FCSZeroingDelay": 1,
    "cursoraim": "mg",
    "nameSound": "mgun",
    "reloadTime": 0.25,
    "autoFire": 1,
    "reloadAction": "ManActReloadMagazine",
    "sounds": ["StandardSound"],
    # Class: CfgWeapons\MGun\StandardSound [Indent level: 1],
    "StandardSound": {
        "begin1": ["A3|Sounds_F|arsenal|weapons_vehicles|HMG_050|HMG_050_01",1.58489,1,2100],
        "begin2": ["A3|Sounds_F|arsenal|weapons_vehicles|HMG_050|HMG_050_02",1.58489,1,2100],
        "begin3": ["A3|Sounds_F|arsenal|weapons_vehicles|HMG_050|HMG_050_03",1.58489,1,2100],
        "soundBegin": ["begin1",0.33,"begin2",0.33,"begin3",0.34],
        "soundsetshot": ["HMG050_Shot_SoundSet","HMG050_Tail_SoundSet"]
    },
    "soundContinuous": 0,
    "flash": "gunfire",
    "flashSize": 0.5,
    "optics": 0,
    "textureType": "fullAuto",
    "dexterity": 0.5,
    "aiRateOfFire": 0.5,
    "aiRateOfFireDistance": 400,
    "inertia": 0.7,
    "access": 3,
    "value": 2,
    "picture": "",
    "uiPicture": "",
    "ammo": "",
    "cursorSize": 1,
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
    "magazineReloadSwitchPhase": 1,
    "sound": ["",1,1],
    "soundBegin": ["sound",1],
    "soundBeginWater": ["sound",1],
    "soundClosure": ["sound",1],
    "soundEnd": ["sound",1],
    "soundLoop": ["sound",1],
    "weaponSoundEffect": "",
    "soundBurst": 1,
    "zeroingSound": ["",1,1],
    "reloadSound": ["",1,1],
    "changeFiremodeSound": ["",1,1],
    "emptySound": ["",1,1],
    "irDistance": 0,
    "irDotIntensity": 0.001,
    "dispersion": 0.002,
    "lockAcquire": 1,
    "enableAttack": 1,
    "ffMagnitude": 0,
    "ffFrequency": 1,
    "ffCount": 1,
    # Recoil Array: recoil,
    "recoil": [],
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
    "aimTransitionSpeed": 1,
}