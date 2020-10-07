RHS_weap_AZP23 = {
    "scope": 1,
    "ballisticsComputer": 4,
    "displayName": "AZP-23",
    "nameSound": "cannon",
    "cartridgePos": "eject1",
    "cartridgeVel": "eject1dir",
    "cursor": "emptyCursor",
    "cursorAim": "mg",
    "cursorAimOn": "",
    "cursorSize": 1,
    "canLock": 2,
    "weaponLockSystem": 8,
    "flash": "gunfire",
    "flashSize": 0.1,
    # Class: CfgWeapons\rhs_weap_azp23\gunParticles [Indent level: 1],
    "gunParticles": {
        # Class: CfgWeapons\rhs_weap_azp23\gunParticles\effect1 [Indent level: 2]
        "effect1": {
            "positionName": "eject1",
            "directionName": "eject1dir",
            "effectName": "MachineGunCartridge2"
        },
        # Class: CfgWeapons\rhs_weap_azp23\gunParticles\effect2 [Indent level: 2],
        "effect2": {
            "positionName": "eject2",
            "directionName": "eject2dir",
            "effectName": "MachineGunCartridge2"
        },
        # Class: CfgWeapons\rhs_weap_azp23\gunParticles\effect3 [Indent level: 2],
        "effect3": {
            "positionName": "eject3",
            "directionName": "eject3dir",
            "effectName": "MachineGunCartridge2"
        },
        # Class: CfgWeapons\rhs_weap_azp23\gunParticles\effect4 [Indent level: 2],
        "effect4": {
            "positionName": "eject4",
            "directionName": "eject4dir",
            "effectName": "MachineGunCartridge2"
        },
        # Class: CfgWeapons\rhs_weap_azp23\gunParticles\mg1 [Indent level: 2],
        "mg1": {
            "positionName": "chase01e",
            "directionName": "chase01dir",
            "effectName": "MachineGun1"
        },
        # Class: CfgWeapons\rhs_weap_azp23\gunParticles\mg2 [Indent level: 2],
        "mg2": {
            "positionName": "chase03e",
            "directionName": "chase03dir",
            "effectName": "MachineGun1"
        },
        # Class: CfgWeapons\rhs_weap_azp23\gunParticles\mg3 [Indent level: 2],
        "mg3": {
            "positionName": "chase03e",
            "directionName": "chase03dir",
            "effectName": "MachineGun1"
        },
        # Class: CfgWeapons\rhs_weap_azp23\gunParticles\mg4 [Indent level: 2],
        "mg4": {
            "positionName": "chase04e",
            "directionName": "chase04dir",
            "effectName": "MachineGun1"
        }
    },
    "magazines": ["rhs_mag_AZP23_2000","rhs_mag_AZP23_2000_mixed","RHS_mag_AZP23_250","RHS_mag_AZP23_250_mixed","rhs_mag_AZP23_250_ap"],
    "magazineReloadTime": 14,
    "modes": ["manual","close","short","medium","far"],
    # Class: CfgWeapons\rhs_weap_azp23\manual [Indent level: 1],
    "manual": {
        "displayName": "AZP-23",
        "autoFire": 1,
        "reloadTime": 0.024,
        "dispersion": 0.005,
        "multiplier": 2,
        "soundContinuous": 0,
        "showToPlayer": 1,
        "burst": 1,
        "aiRateOfFire": 0.5,
        "aiRateOfFireDistance": 50,
        "minRange": 1,
        "minRangeProbab": 0.01,
        "midRange": 2,
        "midRangeProbab": 0.01,
        "maxRange": 3,
        "maxRangeProbab": 0.01,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_azp23\manual\StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHS_KPVT_Closure_SoundSet","RHS_KPVT_Shot_SoundSet","RHS_KPVT_Int_Shot_SoundSet","RHS_autocannon_Tail_SoundSet"]
        },
        "type": 65536,
        # Class: CfgWeapons\CannonCore\GunClouds [Indent level: 1],
        "GunClouds": {
        },
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
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
        "magazineReloadTime": 0,
        "magazineReloadSwitchPhase": 1,
        "sound": ["",1,1],
        "soundBegin": ["sound",1],
        "soundBeginWater": ["sound",1],
        "soundClosure": ["sound",1],
        "soundEnd": ["sound",1],
        "soundLoop": ["sound",1],
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
        "textureType": "default",
        "inertia": 0.5,
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_azp23\close [Indent level: 1],
    "close": {
        "showToPlayer": 0,
        "soundBurst": 0,
        "burst": 10,
        "burstRangeMax": 15,
        "aiRateOfFire": 2,
        "aiRateOfFireDistance": 1000,
        "aiRateOfFireDispersion": 2,
        "minRange": 0,
        "minRangeProbab": 0.05,
        "midRange": 1000,
        "midRangeProbab": 0.58,
        "maxRange": 1600,
        "maxRangeProbab": 0.3,
        "displayName": "AZP-23",
        "autoFire": 1,
        "reloadTime": 0.024,
        "dispersion": 0.005,
        "multiplier": 2,
        "soundContinuous": 0,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_azp23\manual\StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHS_KPVT_Closure_SoundSet","RHS_KPVT_Shot_SoundSet","RHS_KPVT_Int_Shot_SoundSet","RHS_autocannon_Tail_SoundSet"]
        },
        "type": 65536,
        # Class: CfgWeapons\CannonCore\GunClouds [Indent level: 1],
        "GunClouds": {
        },
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
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
        "reloadMagazineSound": ["",1,1],
        "emptySound": ["",1,1],
        "soundBullet": ["emptySound",1],
        "initSpeed": 0,
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
        "textureType": "default",
        "inertia": 0.5,
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_azp23\short [Indent level: 1],
    "short": {
        "burst": 10,
        "burstRangeMax": 16,
        "aiRateOfFire": 4,
        "aiRateOfFireDistance": 1600,
        "aiRateOfFireDispersion": 3,
        "minRange": 1000,
        "minRangeProbab": 0.3,
        "midRange": 1600,
        "midRangeProbab": 0.58,
        "maxRange": 2200,
        "maxRangeProbab": 0.3,
        "showToPlayer": 0,
        "soundBurst": 0,
        "displayName": "AZP-23",
        "autoFire": 1,
        "reloadTime": 0.024,
        "dispersion": 0.005,
        "multiplier": 2,
        "soundContinuous": 0,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_azp23\manual\StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHS_KPVT_Closure_SoundSet","RHS_KPVT_Shot_SoundSet","RHS_KPVT_Int_Shot_SoundSet","RHS_autocannon_Tail_SoundSet"]
        },
        "type": 65536,
        # Class: CfgWeapons\CannonCore\GunClouds [Indent level: 1],
        "GunClouds": {
        },
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
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
        "reloadMagazineSound": ["",1,1],
        "emptySound": ["",1,1],
        "soundBullet": ["emptySound",1],
        "initSpeed": 0,
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
        "textureType": "default",
        "inertia": 0.5,
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_azp23\medium [Indent level: 1],
    "medium": {
        "burst": 15,
        "burstRangeMax": 25,
        "aiRateOfFire": 4,
        "aiRateOfFireDistance": 2200,
        "aiRateOfFireDispersion": 3,
        "minRange": 1600,
        "minRangeProbab": 0.3,
        "midRange": 2000,
        "midRangeProbab": 0.58,
        "maxRange": 2800,
        "maxRangeProbab": 0.3,
        "showToPlayer": 0,
        "soundBurst": 0,
        "displayName": "AZP-23",
        "autoFire": 1,
        "reloadTime": 0.024,
        "dispersion": 0.005,
        "multiplier": 2,
        "soundContinuous": 0,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_azp23\manual\StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHS_KPVT_Closure_SoundSet","RHS_KPVT_Shot_SoundSet","RHS_KPVT_Int_Shot_SoundSet","RHS_autocannon_Tail_SoundSet"]
        },
        "type": 65536,
        # Class: CfgWeapons\CannonCore\GunClouds [Indent level: 1],
        "GunClouds": {
        },
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
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
        "reloadMagazineSound": ["",1,1],
        "emptySound": ["",1,1],
        "soundBullet": ["emptySound",1],
        "initSpeed": 0,
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
        "textureType": "default",
        "inertia": 0.5,
        "aimTransitionSpeed": 1
    },
    # Class: CfgWeapons\rhs_weap_azp23\far [Indent level: 1],
    "far": {
        "burst": 9,
        "burstRangeMax": 18,
        "aiRateOfFire": 5,
        "aiRateOfFireDistance": 3000,
        "aiRateOfFireDispersion": 4,
        "minRange": 1600,
        "minRangeProbab": 0.3,
        "midRange": 2200,
        "midRangeProbab": 0.4,
        "maxRange": 8500,
        "maxRangeProbab": 0.01,
        "showToPlayer": 0,
        "soundBurst": 0,
        "displayName": "AZP-23",
        "autoFire": 1,
        "reloadTime": 0.024,
        "dispersion": 0.005,
        "multiplier": 2,
        "soundContinuous": 0,
        "sounds": ["StandardSound"],
        # Class: CfgWeapons\rhs_weap_azp23\manual\StandardSound [Indent level: 2],
        "StandardSound": {
            "soundSetShot": ["RHS_KPVT_Closure_SoundSet","RHS_KPVT_Shot_SoundSet","RHS_KPVT_Int_Shot_SoundSet","RHS_autocannon_Tail_SoundSet"]
        },
        "type": 65536,
        # Class: CfgWeapons\CannonCore\GunClouds [Indent level: 1],
        "GunClouds": {
        },
        "access": 3,
        "scope": 0,
        "value": 2,
        "picture": "",
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
        "reloadMagazineSound": ["",1,1],
        "emptySound": ["",1,1],
        "soundBullet": ["emptySound",1],
        "initSpeed": 0,
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
        "textureType": "default",
        "inertia": 0.5,
        "aimTransitionSpeed": 1
    },
    "type": 65536,
    # Class: CfgWeapons\CannonCore\GunClouds [Indent level: 1],
    "GunClouds": {
    },
    "access": 3,
    "value": 2,
    "picture": "",
    "uiPicture": "",
    "ammo": "",
    "showAimCursorInternal": 1,
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
    # Class: CfgWeapons\Default\Eventhandlers [Indent level: 1],
    "Eventhandlers": {
    },
    "backgroundReload": 0,
    "reloadAction": "",
    "muzzles": ["this"],
    "useAction": 0,
    "useActionTitle": "",
    "canDrop": 1,
    "weaponLockDelay": 0,
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
    "textureType": "default",
    "inertia": 0.5,
    "aimTransitionSpeed": 1,
}