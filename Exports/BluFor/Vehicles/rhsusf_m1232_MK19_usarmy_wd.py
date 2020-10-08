rhsusf_m1232_MK19_usarmy_wd = {
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|rhsusf_M1232_MK19_usarmy_wd.paa",
    "displayName": "M1232 (Mk19)",
    "faction": "rhs_faction_usarmy_wd",
    "crew": "rhsusf_army_ucp_driver_armored",
    "author": "Red Hammer Studios",
    "HiddenSelectionsTextures": ["rhsusf|addons|rhsusf_RG33L|data|RG33_Body_WD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Chassis_WD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Accessory2_WD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Armor_WD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_TurretWD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Wheels_WD_CO.paa","rhsusf|addons|rhsusf_hmmwv|textures|mk64mount_w_co.paa","rhsusf|addons|rhsusf_RG33L|data|MCTAGS_CO.paa","rhsusf|addons|rhsusf_rg33l|Data|rhsusf_camonet_wdl_co.paa","rhsusf|addons|rhsusf_RG33L|Decals|RG33_USARMY_Decal_ca.paa"],
    "model": "rhsusf|addons|rhsusf_rg33l|M1232_MK19",
    "accuracy": 0.5,
    # Class: CfgVehicles|rhsusf_M1232_MK19_usarmy_d|AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles|rhsusf_M1232_MK19_usarmy_d|AnimationSources|belt_rotation [Indent level: 2],

        "belt_rotation": {

            "source": "reload",

            "weapon": "RHS_MK19"
        },
        # Class: CfgVehicles|rhsusf_M1232_MK19_usarmy_d|AnimationSources|ReloadMagazine [Indent level: 2],
        "ReloadMagazine": {
            "source": "reloadmagazine",
            "weapon": "RHS_MK19"
        },
        # Class: CfgVehicles|rhsusf_M1232_MK19_usarmy_d|AnimationSources|Revolving [Indent level: 2],
        "Revolving": {
            "source": "revolving",
            "weapon": "RHS_MK19"
        },
        # Class: CfgVehicles|rhsusf_M1232_M2_usarmy_d|AnimationSources|ReloadAnim [Indent level: 2],
        "ReloadAnim": {
            "source": "reload",
            "weapon": "RHS_M2"
        },
        # Class: CfgVehicles|rhsusf_M1232_M2_usarmy_d|AnimationSources|muzzle_rot_MG [Indent level: 2],
        "muzzle_rot_MG": {
            "source": "ammorandom",
            "weapon": "RHS_M2"
        },
        # Class: CfgVehicles|rhsusf_RG33L_GPK_base|AnimationSources|hide_ogpkover [Indent level: 2],
        "hide_ogpkover": {
            "author": "Red Hammer Studios",
            "displayName": "hide overhead protection",
            "source": "user",
            "mass": -20,
            "animPeriod": 1e-005,
            "initPhase": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_GPK_base|AnimationSources|hide_ogpknet [Indent level: 2],
        "hide_ogpknet": {
            "author": "Red Hammer Studios",
            "displayName": "hide camo net",
            "source": "user",
            "mass": 0,
            "animPeriod": 1e-005,
            "initPhase": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_GPK_base|AnimationSources|hide_ogpkbust [Indent level: 2],
        "hide_ogpkbust": {
            "author": "Red Hammer Studios",
            "displayName": "hide turret bustle",
            "source": "user",
            "mass": -20,
            "animPeriod": 1e-005,
            "initPhase": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|longlights_hide [Indent level: 2],
        "longlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|shortlights_hide [Indent level: 2],
        "shortlights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|lights_hide [Indent level: 2],
        "lights_hide": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-006
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|light_bo [Indent level: 2],
        "light_bo": {
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|light_stop [Indent level: 2],
        "light_stop": {
            "source": "user",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|light_svc [Indent level: 2],
        "light_svc": {
            "initPhase": 1,
            "source": "user",
            "animPeriod": 1e-005
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|DoorL [Indent level: 2],
        "DoorL": {
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHSUSF_Truck_Door",
            "soundPosition": "osa_dvere_lp"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|DoorR [Indent level: 2],
        "DoorR": {
            "soundPosition": "osa_dvere_pp",
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHSUSF_Truck_Door"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|DoorB [Indent level: 2],
        "DoorB": {
            "animPeriod": 1.8,
            "soundPosition": "osa_dvere_pp",
            "source": "door",
            "sound": "RHSUSF_Truck_Door"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|hatch1_door [Indent level: 2],
        "hatch1_door": {
            "soundPosition": "osa_dvere_pp",
            "initPhase": 0,
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHSUSF_Truck_Door"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|hatch2_door [Indent level: 2],
        "hatch2_door": {
            "soundPosition": "osa_dvere_pp",
            "initPhase": 0,
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHSUSF_Truck_Door"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|hatch3_door [Indent level: 2],
        "hatch3_door": {
            "soundPosition": "osa_dvere_pp",
            "initPhase": 0,
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHSUSF_Truck_Door"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|hatch4_door [Indent level: 2],
        "hatch4_door": {
            "soundPosition": "osa_dvere_pp",
            "initPhase": 0,
            "source": "door",
            "animPeriod": 0.8,
            "sound": "RHSUSF_Truck_Door"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|DUKE_Hide [Indent level: 2],
        "DUKE_Hide": {
            "source": "user",
            "mass": -20,
            "displayName": "hide DUKE antennas",
            "author": "Red Hammer Studios",
            "animPeriod": 1e-005,
            "initPhase": 0,
            "onPhaseChanged": "_this call rhs_fnc_duke_vg;"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitDuke1 [Indent level: 2],
        "HitDuke1": {
            "source": "Hit",
            "hitpoint": "HitDuke1"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitDuke2 [Indent level: 2],
        "HitDuke2": {
            "hitpoint": "HitDuke2",
            "source": "Hit"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass7 [Indent level: 2],
        "HitGlass7": {
            "hitpoint": "HitGlass7",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass8 [Indent level: 2],
        "HitGlass8": {
            "hitpoint": "HitGlass8",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass9 [Indent level: 2],
        "HitGlass9": {
            "hitpoint": "HitGlass9",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass10 [Indent level: 2],
        "HitGlass10": {
            "hitpoint": "HitGlass10",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass11 [Indent level: 2],
        "HitGlass11": {
            "hitpoint": "HitGlass11",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass12 [Indent level: 2],
        "HitGlass12": {
            "hitpoint": "HitGlass12",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass13 [Indent level: 2],
        "HitGlass13": {
            "hitpoint": "HitGlass13",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass14 [Indent level: 2],
        "HitGlass14": {
            "hitpoint": "HitGlass14",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass15 [Indent level: 2],
        "HitGlass15": {
            "hitpoint": "HitGlass15",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass16 [Indent level: 2],
        "HitGlass16": {
            "hitpoint": "HitGlass16",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass17 [Indent level: 2],
        "HitGlass17": {
            "hitpoint": "HitGlass17",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass18 [Indent level: 2],
        "HitGlass18": {
            "hitpoint": "HitGlass18",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass19 [Indent level: 2],
        "HitGlass19": {
            "hitpoint": "HitGlass19",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass20 [Indent level: 2],
        "HitGlass20": {
            "hitpoint": "HitGlass20",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|HitGlass21 [Indent level: 2],
        "HitGlass21": {
            "hitpoint": "HitGlass21",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|AnimationSources|dve_fold [Indent level: 2],
        "dve_fold": {
            "source": "user",
            "animPeriod": 1.5,
            "initPhase": 0
        },
        # Class: CfgVehicles|MRAP_01_base_F|AnimationSources|HitReserveWheel [Indent level: 2],
        "HitReserveWheel": {
            "source": "Hit",
            "hitpoint": "HitReserveWheel",
            "raw": 1
        },
        # Class: CfgVehicles|MRAP_01_base_F|AnimationSources|Door_LF [Indent level: 2],
        "Door_LF": {
            "source": "door",
            "animPeriod": 0.8
        },
        # Class: CfgVehicles|MRAP_01_base_F|AnimationSources|Door_RF [Indent level: 2],
        "Door_RF": {
            "source": "door",
            "animPeriod": 0.8
        },
        # Class: CfgVehicles|MRAP_01_base_F|AnimationSources|Door_LB [Indent level: 2],
        "Door_LB": {
            "source": "door",
            "animPeriod": 0.8
        },
        # Class: CfgVehicles|MRAP_01_base_F|AnimationSources|Door_RB [Indent level: 2],
        "Door_RB": {
            "source": "door",
            "animPeriod": 0.8
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitLFWheel [Indent level: 2],
        "HitLFWheel": {
            "source": "Hit",
            "hitpoint": "HitLFWheel",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitRFWheel [Indent level: 2],
        "HitRFWheel": {
            "hitpoint": "HitRFWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitLBWheel [Indent level: 2],
        "HitLBWheel": {
            "hitpoint": "HitLF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitRBWheel [Indent level: 2],
        "HitRBWheel": {
            "hitpoint": "HitRF2Wheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitLF2Wheel [Indent level: 2],
        "HitLF2Wheel": {
            "hitpoint": "HitLBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitRF2Wheel [Indent level: 2],
        "HitRF2Wheel": {
            "hitpoint": "HitRBWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitLMWheel [Indent level: 2],
        "HitLMWheel": {
            "hitpoint": "HitLMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitRMWheel [Indent level: 2],
        "HitRMWheel": {
            "hitpoint": "HitRMWheel",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitGlass3 [Indent level: 2],
        "HitGlass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitGlass4 [Indent level: 2],
        "HitGlass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitGlass5 [Indent level: 2],
        "HitGlass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Car_F|AnimationSources|HitGlass6 [Indent level: 2],
        "HitGlass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit",
            "raw": 1
        }
    },
    "threat": [0.9,0.3,0.1],
    "showNVGGunner": 1,
    # Class: CfgVehicles|rhsusf_M1232_MK19_usarmy_d|Turrets [Indent level: 1],
    "Turrets": {
        # Class: CfgVehicles|rhsusf_M1232_MK19_usarmy_d|Turrets|M2_Turret [Indent level: 2],

        "M2_Turret": {

            "discreteDistance": [100,200,300,400,500,600,800,1000,1100,1200,1300,1400,1500],

            "discreteDistanceInitIndex": 2,

            "gunnerLeftHandAnimName": "OtocHlaven",

            "gunnerRightHandAnimName": "OtocHlaven",

            "weapons": ["RHS_MK19"],

            "magazines": ["RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M430A1","RHS_48Rnd_40mm_MK19_M1001","RHS_48Rnd_40mm_MK19_M1001","RHS_48Rnd_40mm_MK19_M1001"],

            "body": "mainTurret",

            "gun": "mainGun",

            "animationSourceBody": "mainTurret",

            "animationSourceGun": "mainGun",

            "turretInfoType": "RscOptics_Offroad_01",

            "gunnerForceOptics": 0,

            "gunnerOutOpticsShowCursor": 0,

            "minElev": -10,

            "maxElev": 40,

            "soundServo": ["A3|sounds_f|dummysound",1e-006,1],

            "gunnerAction": "RHS_HMMWV_Gunner03",

            "gunnerInAction": "RHS_HMMWV_Gunner03_in",

            "lodTurnedIn": 0,

            "lodTurnedOut": 1000,

            "lodOpticsOut": 1000,

            "canhideGunner": 1,

            "inGunnerMayFire": 0,

            "outGunnerMayFire": 1,

            "viewGunnerInExternal": 1,

            "gunnerGetInAction": "GetInMRAP_01_cargo",

            "gunnerGetOutAction": "GetOutMRAP_01",

            "gunnerDoor": "DoorR",

            "gunnerCompartments": "Compartment1",

            "ejectDeadGunner": 0,

            "castGunnerShadow": 1,

            "stabilizedInAxes": 0,

            "gunBeg": "usti hlavne",

            "gunEnd": "konec hlavne",

            "memoryPointGunnerOptics": "",

            "memoryPointGunnerOutOptics": "gunnerview",

            "gunnerOpticsModel": "",

            "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",

            "optics": 0,

            "disableSoundAttenuation": 1,

            "memoryPointsGetInGunner": "pos codriver",

            "memoryPointsGetInGunnerDir": "pos codriver dir",

            # Class: CfgVehicles|rhsusf_M1232_M2_usarmy_d|Turrets|M2_Turret|ViewOptics [Indent level: 3],

            "ViewOptics": {

                "initFov": 0.7,

                "minFov": 0.25,

                "maxFov": 1.1,

                "initAngleX": 0,

                "minAngleX": -30,

                "maxAngleX": 30,

                "initAngleY": 0,

                "minAngleY": -100,

                "maxAngleY": 100,

                "minMoveX": 0,

                "maxMoveX": 0,

                "minMoveY": 0,

                "maxMoveY": 0,

                "minMoveZ": 0,

                "maxMoveZ": 0,

                "speedZoomMaxSpeed": 1e+010,

                "speedZoomMaxFOV": 0
            },

            # Class: CfgVehicles|rhsusf_M1232_M2_usarmy_d|Turrets|M2_Turret|ViewGunner [Indent level: 3],

            "ViewGunner": {

                "initFov": 0.7,

                "minFov": 0.25,

                "maxFov": 1.1,

                "initAngleX": 0,

                "minAngleX": -30,

                "maxAngleX": 30,

                "initAngleY": 0,

                "minAngleY": -100,

                "maxAngleY": 100,

                "minMoveX": 0,

                "maxMoveX": 0,

                "minMoveY": 0,

                "maxMoveY": 0,

                "minMoveZ": 0,

                "maxMoveZ": 0,

                "speedZoomMaxSpeed": 1e+010,

                "speedZoomMaxFOV": 0
            },

            "memoryPointGun": "machinegun",

            "minTurn": -360,

            "maxTurn": 360,

            "primaryGunner": 1,

            "enableManualFire": 0,

            "startEngine": 0,

            # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints [Indent level: 3],

            "HitPoints": {

                # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4],


                "HitTurret": {


                    "armor": 0.8,


                    "material": -1,


                    "name": "vez",


                    "visual": "vez",


                    "passThrough": 0.5,


                    "explosionShielding": 0.4
                },

                # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],

                "HitGun": {

                    "armor": 0.4,

                    "material": -1,

                    "name": "zbran",

                    "visual": "zbran",

                    "passThrough": 0,

                    "explosionShielding": 0.2
                }
            },

            # Class: CfgVehicles|Car_F|Turrets|MainTurret|Components [Indent level: 3],

            "Components": {
            },

            "animationSourceHatch": "hatchGunner",

            "animationSourceCamElev": "camElev",

            "proxyType": "CPGunner",

            "proxyIndex": 1,

            "gunnerName": "Gunner",

            "gunnerType": "",

            "primaryObserver": 0,

            "soundElevation": ["",0.00316228,1],

            "initElev": 0,

            "initTurn": 0,

            "minOutElev": -4,

            "maxOutElev": 20,

            "initOutElev": 0,

            "minOutTurn": -60,

            "maxOutTurn": 60,

            "initOutTurn": 0,

            "maxHorizontalRotSpeed": 1.2,

            "maxVerticalRotSpeed": 1.2,

            "minCamElev": -90,

            "maxCamElev": 90,

            "initCamElev": 0,

            "primary": 1,

            "hasGunner": 1,

            "commanding": 1,

            "turretCanSee": 0,

            "canUseScanners": 1,

            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],

            "TurretSpec": {

                "showHeadPhones": 0
            },

            "gunnerOpticsColor": [0,0,0,1],

            "gunnerOpticsShowCursor": 0,

            "gunnerOutOpticsColor": [0,0,0,1],

            "gunnerOpticsEffect": [],

            "gunnerOutOpticsEffect": [],

            "gunnerOutForceOptics": 0,

            "gunnerFireAlsoInInternalCamera": 1,

            "gunnerOutFireAlsoInInternalCamera": 1,

            "gunnerUsesPilotView": 0,

            "viewGunnerShadow": 1,

            "viewGunnerShadowDiff": 1,

            "viewGunnerShadowAmb": 1,

            "hideWeaponsGunner": 1,

            "forceHideGunner": 0,

            "showHMD": 0,

            "lockWhenDriverOut": 0,

            "lockWhenVehicleSpeed": -1,

            "memoryPointsGetInGunnerPrecise": "",

            "missileBeg": "spice rakety",

            "missileEnd": "konec rakety",

            "armorLights": 0.4,

            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],

            "Reflectors": {
            },

            "aggregateReflectors": [],

            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],

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

                "interval": 0.01,

                "size": 3,

                "sourceSize": 0.5,

                "timeToLive": 0,

                "initT": 4500,

                "deltaT": -3000,

                # Class: WeaponFireGun|Table [Indent level: 0],

                "Table": {

                    # Class: WeaponFireGun|Table|T0 [Indent level: 1],


                    "T0": {


                        "maxT": 0,


                        "color": [0.82,0.95,0.93,0]
                    },

                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],

                    "T1": {

                        "maxT": 200,

                        "color": [0.75,0.77,0.9,0]
                    },

                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],

                    "T2": {

                        "maxT": 400,

                        "color": [0.56,0.62,0.67,0]
                    },

                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],

                    "T3": {

                        "maxT": 600,

                        "color": [0.39,0.46,0.47,0]
                    },

                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],

                    "T4": {

                        "maxT": 800,

                        "color": [0.24,0.31,0.31,0]
                    },

                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],

                    "T5": {

                        "maxT": 1000,

                        "color": [0.23,0.31,0.29,0]
                    },

                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],

                    "T6": {

                        "maxT": 1500,

                        "color": [0.21,0.29,0.27,0]
                    },

                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],

                    "T7": {

                        "maxT": 2000,

                        "color": [0.19,0.23,0.21,0]
                    },

                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],

                    "T8": {

                        "maxT": 2300,

                        "color": [0.22,0.19,0.1,0]
                    },

                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],

                    "T9": {

                        "maxT": 2500,

                        "color": [0.35,0.2,0.02,0]
                    },

                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],

                    "T10": {

                        "maxT": 2600,

                        "color": [0.62,0.29,0.03,0]
                    },

                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],

                    "T11": {

                        "maxT": 2650,

                        "color": [0.59,0.35,0.05,0]
                    },

                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],

                    "T12": {

                        "maxT": 2700,

                        "color": [0.75,0.37,0.03,0]
                    },

                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],

                    "T13": {

                        "maxT": 2750,

                        "color": [0.88,0.34,0.03,0]
                    },

                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],

                    "T14": {

                        "maxT": 2800,

                        "color": [0.91,0.5,0.17,0]
                    },

                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],

                    "T15": {

                        "maxT": 2850,

                        "color": [1,0.6,0.2,0]
                    },

                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],

                    "T16": {

                        "maxT": 2900,

                        "color": [1,0.71,0.3,0]
                    },

                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],

                    "T17": {

                        "maxT": 2950,

                        "color": [0.98,0.83,0.41,0]
                    },

                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],

                    "T18": {

                        "maxT": 3000,

                        "color": [0.98,0.91,0.54,0]
                    },

                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],

                    "T19": {

                        "maxT": 3100,

                        "color": [0.98,0.99,0.6,0]
                    },

                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],

                    "T20": {

                        "maxT": 3300,

                        "color": [0.96,0.99,0.72,0]
                    },

                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],

                    "T21": {

                        "maxT": 3600,

                        "color": [1,0.98,0.91,0]
                    },

                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],

                    "T22": {

                        "maxT": 4200,

                        "color": [1,1,1,0]
                    }
                }
            },

            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],

            "GunClouds": {

                "access": 0,

                "cloudletDuration": 0.3,

                "cloudletAnimPeriod": 1,

                "cloudletSize": 1,

                "cloudletAlpha": 1,

                "cloudletGrowUp": 1,

                "cloudletFadeIn": 0.01,

                "cloudletFadeOut": 1,

                "cloudletAccY": 0.4,

                "cloudletMinYSpeed": 0.2,

                "cloudletMaxYSpeed": 0.8,

                "cloudletShape": "cloudletClouds",

                "cloudletColor": [1,1,1,0],

                "interval": 0.05,

                "size": 3,

                "sourceSize": 0.5,

                "timeToLive": 0,

                "initT": 0,

                "deltaT": 0,

                # Class: WeaponCloudsGun|Table [Indent level: 0],

                "Table": {

                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],


                    "T0": {


                        "maxT": 0,


                        "color": [1,1,1,0]
                    }
                }
            },

            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],

            "MGunClouds": {

                "access": 0,

                "cloudletGrowUp": 0.05,

                "cloudletFadeIn": 0,

                "cloudletFadeOut": 0.1,

                "cloudletDuration": 0.05,

                "cloudletAnimPeriod": 1,

                "cloudletSize": 1,

                "cloudletAlpha": 0.3,

                "cloudletAccY": 0,

                "cloudletMinYSpeed": -100,

                "cloudletMaxYSpeed": 100,

                "cloudletShape": "cloudletClouds",

                "cloudletColor": [1,1,1,0],

                "timeToLive": 0,

                "interval": 0.02,

                "size": 0.3,

                "sourceSize": 0.02,

                "initT": 0,

                "deltaT": 0,

                # Class: WeaponCloudsMGun|Table [Indent level: 0],

                "Table": {

                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],


                    "T0": {


                        "maxT": 0,


                        "color": [1,1,1,0]
                    }
                }
            },

            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],

            "Turrets": {
            },

            "forceNVG": 0,

            "isCopilot": 0,

            "canEject": 1,

            "gunnerLeftLegAnimName": "",

            "gunnerRightLegAnimName": "",

            "preciseGetInOut": 0,

            "turretFollowFreeLook": 0,

            "allowTabLock": 1,

            "showAllTargets": 0,

            "dontCreateAI": 0,

            "slingLoadOperator": 0,

            "playerPosition": 0,

            "allowLauncherIn": 0,

            "allowLauncherOut": 0,

            # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],

            "TurnIn": {

                "turnOffset": 0
            },

            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],

            "TurnOut": {

                "turnOffset": 0
            },

            "selectionFireAnim": "zasleh",

            "showCrewAim": 0
        },
        # Class: CfgVehicles|rhsusf_M1232_MK19_usarmy_d|Turrets|CargoTurret_01 [Indent level: 2],
        "CargoTurret_01": {
            # Class: CfgVehicles|rhsusf_M1232_M2_usarmy_d|Turrets|CargoTurret_01|TurnOut [Indent level: 3],

            "TurnOut": {

                "limitsArrayTop": [[45,-160],[45,160]],

                "limitsArrayBottom": [[-13.8259,-132.419],[2.0787,-124.814],[6.2968,-91.8814],[2.6767,-84.6096],[-7.7983,-74.6288],[-8.8897,-72.2775],[-13.2618,-71.3303],[-24.2613,71.6531],[-14.4574,78.2305],[-13.4463,81.1107],[-13.5018,85.979],[-7.8903,86.9097],[-8.0675,116.021],[-8.9988,117.599],[-14.5298,120.226],[-14.128,123.07],[-11.482,125.244],[-10.9541,132.396],[-12.4393,139.876],[-14.6103,145.936]]
            },
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "vehicle_turnout_1",
            "gunnerInAction": "RHS_rg33l_Cargo01_FFV",
            "animationSourceHatch": "hatch1",
            "enabledByAnimationSource": "hatch1_door",
            "isPersonTurret": 2,
            "gunnerGetInAction": "GetInMantis",
            "gunnerGetOutAction": "GetOutMantis",
            "memoryPointsGetInGunner": "pos cargoFFV1",
            "memoryPointsGetInGunnerDir": "pos cargoFFV1 dir",
            "rhs_hatch_control": 1,
            "gunnerName": "Passenger (Left Front Hatch)",
            "gunnerCompartments": "Compartment1",
            "gunnerDoor": "DoorB",
            "memoryPointGunnerOptics": "",
            "selectionFireAnim": "",
            "canHideGunner": 1,
            "commanding": -2,
            "LODTurnedIn": 1200,
            "LODTurnedOut": 0,
            "proxyIndex": 6,
            "maxElev": 45,
            "minElev": -35,
            "maxTurn": 61,
            "minTurn": -65,
            # Class: CfgVehicles|rhsusf_RG33L_base|Turrets|CargoTurret_01|TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[0,0],[0,0]],
                "limitsArrayBottom": [[0,0],[0,0]]
            },
            # Class: CfgVehicles|rhsusf_RG33L_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
            "Hitpoints": {
            },
            # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2],
            "ViewGunner": {
                "initAngleX": 5,
                "minAngleX": -75,
                "maxAngleX": 85,
                "initAngleY": 0,
                "minAngleY": -150,
                "maxAngleY": 150,
                "minFov": 0.25,
                "maxFov": 1.25,
                "initFov": 0.75,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "animationSourceBody": "",
            "animationSourceGun": "",
            "body": "",
            "canEject": 1,
            "dontCreateAI": 1,
            "gun": "",
            "hideWeaponsGunner": 0,
            "isCopilot": 0,
            "primaryGunner": 0,
            "proxyType": "CPCargo",
            "startEngine": 0,
            "turretFollowFreeLook": 0,
            "viewGunnerInExternal": 1,
            "disableSoundAttenuation": 1,
            "outGunnerMayFire": 1,
            "showAsCargo": 1,
            "animationSourceCamElev": "camElev",
            "gunnerType": "",
            "primaryObserver": 0,
            "magazines": [],
            "soundServo": ["",0.00316228,1],
            "soundElevation": ["",0.00316228,1],
            "initElev": 0,
            "initTurn": 0,
            "minOutElev": -4,
            "maxOutElev": 20,
            "initOutElev": 0,
            "minOutTurn": -60,
            "maxOutTurn": 60,
            "initOutTurn": 0,
            "maxHorizontalRotSpeed": 1.2,
            "maxVerticalRotSpeed": 1.2,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "stabilizedInAxes": 3,
            "primary": 1,
            "hasGunner": 1,
            "turretCanSee": 0,
            "canUseScanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsModel": "",
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerForceOptics": 1,
            "gunnerOpticsShowCursor": 0,
            "turretInfoType": "",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOpticsEffect": [],
            "gunnerOutOpticsEffect": [],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "castGunnerShadow": 0,
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "forceHideGunner": 0,
            "inGunnerMayFire": 1,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
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
                "interval": 0.01,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 4500,
                "deltaT": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "GunClouds": {
                "access": 0,
                "cloudletDuration": 0.3,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 1,
                "cloudletGrowUp": 1,
                "cloudletFadeIn": 0.01,
                "cloudletFadeOut": 1,
                "cloudletAccY": 0.4,
                "cloudletMinYSpeed": 0.2,
                "cloudletMaxYSpeed": 0.8,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "MGunClouds": {
                "access": 0,
                "cloudletGrowUp": 0.05,
                "cloudletFadeIn": 0,
                "cloudletFadeOut": 0.1,
                "cloudletDuration": 0.05,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 0.3,
                "cloudletAccY": 0,
                "cloudletMinYSpeed": -100,
                "cloudletMaxYSpeed": 100,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "timeToLive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourceSize": 0.02,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "Turrets": {
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.3,
                "minFov": 0.07,
                "maxFov": 0.35,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "forceNVG": 0,
            "gunnerLeftHandAnimName": "",
            "gunnerRightHandAnimName": "",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        },
        # Class: CfgVehicles|rhsusf_M1232_MK19_usarmy_d|Turrets|CargoTurret_02 [Indent level: 2],
        "CargoTurret_02": {
            # Class: CfgVehicles|rhsusf_M1232_M2_usarmy_d|Turrets|CargoTurret_02|TurnOut [Indent level: 3],

            "TurnOut": {

                "limitsArrayTop": [[45,-160],[45,160]],

                "limitsArrayBottom": [[-8.4929,-121.755],[-7.8962,-110.538],[-14.1648,-108.604],[-14.3219,-90.5885],[-10.2817,-87.7792],[-9.0565,-75.9969],[-15.5082,-66.9248],[-32.8865,-45.8966],[-34.2066,64.135],[-16.2796,77.8835],[-6.7441,84.5794],[-4.5728,87.2431],[-2.2958,89.0149],[4.2706,97.8377],[5.679,104.009],[2.2804,134.332],[-13.281,135.801],[-17.2118,157.544]]
            },
            "proxyIndex": 7,
            "gunnerInAction": "RHS_rg33l_Cargo03_FFV",
            "enabledByAnimationSource": "hatch2_door",
            "animationSourceHatch": "hatch2",
            "gunnerName": "Passenger (Right Front Hatch)",
            "memoryPointsGetInGunner": "pos cargoFFV2",
            "memoryPointsGetInGunnerDir": "pos cargoFFV2 dir",
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "vehicle_turnout_1",
            "isPersonTurret": 2,
            "gunnerGetInAction": "GetInMantis",
            "gunnerGetOutAction": "GetOutMantis",
            "rhs_hatch_control": 1,
            "gunnerCompartments": "Compartment1",
            "gunnerDoor": "DoorB",
            "memoryPointGunnerOptics": "",
            "selectionFireAnim": "",
            "canHideGunner": 1,
            "commanding": -2,
            "LODTurnedIn": 1200,
            "LODTurnedOut": 0,
            "maxElev": 45,
            "minElev": -35,
            "maxTurn": 61,
            "minTurn": -65,
            # Class: CfgVehicles|rhsusf_RG33L_base|Turrets|CargoTurret_01|TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[0,0],[0,0]],
                "limitsArrayBottom": [[0,0],[0,0]]
            },
            # Class: CfgVehicles|rhsusf_RG33L_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
            "Hitpoints": {
            },
            # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2],
            "ViewGunner": {
                "initAngleX": 5,
                "minAngleX": -75,
                "maxAngleX": 85,
                "initAngleY": 0,
                "minAngleY": -150,
                "maxAngleY": 150,
                "minFov": 0.25,
                "maxFov": 1.25,
                "initFov": 0.75,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "animationSourceBody": "",
            "animationSourceGun": "",
            "body": "",
            "canEject": 1,
            "dontCreateAI": 1,
            "gun": "",
            "hideWeaponsGunner": 0,
            "isCopilot": 0,
            "primaryGunner": 0,
            "proxyType": "CPCargo",
            "startEngine": 0,
            "turretFollowFreeLook": 0,
            "viewGunnerInExternal": 1,
            "disableSoundAttenuation": 1,
            "outGunnerMayFire": 1,
            "showAsCargo": 1,
            "animationSourceCamElev": "camElev",
            "gunnerType": "",
            "primaryObserver": 0,
            "magazines": [],
            "soundServo": ["",0.00316228,1],
            "soundElevation": ["",0.00316228,1],
            "initElev": 0,
            "initTurn": 0,
            "minOutElev": -4,
            "maxOutElev": 20,
            "initOutElev": 0,
            "minOutTurn": -60,
            "maxOutTurn": 60,
            "initOutTurn": 0,
            "maxHorizontalRotSpeed": 1.2,
            "maxVerticalRotSpeed": 1.2,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "stabilizedInAxes": 3,
            "primary": 1,
            "hasGunner": 1,
            "turretCanSee": 0,
            "canUseScanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsModel": "",
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerForceOptics": 1,
            "gunnerOpticsShowCursor": 0,
            "turretInfoType": "",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOpticsEffect": [],
            "gunnerOutOpticsEffect": [],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "castGunnerShadow": 0,
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "forceHideGunner": 0,
            "inGunnerMayFire": 1,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
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
                "interval": 0.01,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 4500,
                "deltaT": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "GunClouds": {
                "access": 0,
                "cloudletDuration": 0.3,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 1,
                "cloudletGrowUp": 1,
                "cloudletFadeIn": 0.01,
                "cloudletFadeOut": 1,
                "cloudletAccY": 0.4,
                "cloudletMinYSpeed": 0.2,
                "cloudletMaxYSpeed": 0.8,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "MGunClouds": {
                "access": 0,
                "cloudletGrowUp": 0.05,
                "cloudletFadeIn": 0,
                "cloudletFadeOut": 0.1,
                "cloudletDuration": 0.05,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 0.3,
                "cloudletAccY": 0,
                "cloudletMinYSpeed": -100,
                "cloudletMaxYSpeed": 100,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "timeToLive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourceSize": 0.02,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "Turrets": {
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.3,
                "minFov": 0.07,
                "maxFov": 0.35,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "forceNVG": 0,
            "gunnerLeftHandAnimName": "",
            "gunnerRightHandAnimName": "",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        },
        # Class: CfgVehicles|rhsusf_M1232_MK19_usarmy_d|Turrets|CargoTurret_03 [Indent level: 2],
        "CargoTurret_03": {
            # Class: CfgVehicles|rhsusf_M1232_M2_usarmy_d|Turrets|CargoTurret_03|TurnOut [Indent level: 3],

            "TurnOut": {

                "limitsArrayTop": [[45,-160],[45,160]],

                "limitsArrayBottom": [[-8.3014,-121.163],[-6.9716,-114.795],[3.2541,-111.381],[3.6021,-87.3033],[1.1921,-83.8334],[-6.8407,-79.3857],[-11.3016,-74.2475],[-19.8969,-61.7452],[-34.5781,-35.0912],[-35.0492,55.5252],[-29.5614,68.0467],[-14.5186,74.2655],[-9.8469,102.176],[-5.5565,133.274],[-6.8999,146.12]]
            },
            "proxyIndex": 9,
            "gunnerInAction": "RHS_rg33l_Cargo02_FFV",
            "enabledByAnimationSource": "hatch3_door",
            "animationSourceHatch": "hatch3",
            "gunnerName": "Passenger (Left Rear Hatch)",
            "memoryPointsGetInGunner": "pos cargoFFV3",
            "memoryPointsGetInGunnerDir": "pos cargoFFV3 dir",
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "vehicle_turnout_1",
            "isPersonTurret": 2,
            "gunnerGetInAction": "GetInMantis",
            "gunnerGetOutAction": "GetOutMantis",
            "rhs_hatch_control": 1,
            "gunnerCompartments": "Compartment1",
            "gunnerDoor": "DoorB",
            "memoryPointGunnerOptics": "",
            "selectionFireAnim": "",
            "canHideGunner": 1,
            "commanding": -2,
            "LODTurnedIn": 1200,
            "LODTurnedOut": 0,
            "maxElev": 45,
            "minElev": -35,
            "maxTurn": 61,
            "minTurn": -65,
            # Class: CfgVehicles|rhsusf_RG33L_base|Turrets|CargoTurret_01|TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[0,0],[0,0]],
                "limitsArrayBottom": [[0,0],[0,0]]
            },
            # Class: CfgVehicles|rhsusf_RG33L_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
            "Hitpoints": {
            },
            # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2],
            "ViewGunner": {
                "initAngleX": 5,
                "minAngleX": -75,
                "maxAngleX": 85,
                "initAngleY": 0,
                "minAngleY": -150,
                "maxAngleY": 150,
                "minFov": 0.25,
                "maxFov": 1.25,
                "initFov": 0.75,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "animationSourceBody": "",
            "animationSourceGun": "",
            "body": "",
            "canEject": 1,
            "dontCreateAI": 1,
            "gun": "",
            "hideWeaponsGunner": 0,
            "isCopilot": 0,
            "primaryGunner": 0,
            "proxyType": "CPCargo",
            "startEngine": 0,
            "turretFollowFreeLook": 0,
            "viewGunnerInExternal": 1,
            "disableSoundAttenuation": 1,
            "outGunnerMayFire": 1,
            "showAsCargo": 1,
            "animationSourceCamElev": "camElev",
            "gunnerType": "",
            "primaryObserver": 0,
            "magazines": [],
            "soundServo": ["",0.00316228,1],
            "soundElevation": ["",0.00316228,1],
            "initElev": 0,
            "initTurn": 0,
            "minOutElev": -4,
            "maxOutElev": 20,
            "initOutElev": 0,
            "minOutTurn": -60,
            "maxOutTurn": 60,
            "initOutTurn": 0,
            "maxHorizontalRotSpeed": 1.2,
            "maxVerticalRotSpeed": 1.2,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "stabilizedInAxes": 3,
            "primary": 1,
            "hasGunner": 1,
            "turretCanSee": 0,
            "canUseScanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsModel": "",
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerForceOptics": 1,
            "gunnerOpticsShowCursor": 0,
            "turretInfoType": "",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOpticsEffect": [],
            "gunnerOutOpticsEffect": [],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "castGunnerShadow": 0,
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "forceHideGunner": 0,
            "inGunnerMayFire": 1,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
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
                "interval": 0.01,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 4500,
                "deltaT": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "GunClouds": {
                "access": 0,
                "cloudletDuration": 0.3,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 1,
                "cloudletGrowUp": 1,
                "cloudletFadeIn": 0.01,
                "cloudletFadeOut": 1,
                "cloudletAccY": 0.4,
                "cloudletMinYSpeed": 0.2,
                "cloudletMaxYSpeed": 0.8,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "MGunClouds": {
                "access": 0,
                "cloudletGrowUp": 0.05,
                "cloudletFadeIn": 0,
                "cloudletFadeOut": 0.1,
                "cloudletDuration": 0.05,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 0.3,
                "cloudletAccY": 0,
                "cloudletMinYSpeed": -100,
                "cloudletMaxYSpeed": 100,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "timeToLive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourceSize": 0.02,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "Turrets": {
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.3,
                "minFov": 0.07,
                "maxFov": 0.35,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "forceNVG": 0,
            "gunnerLeftHandAnimName": "",
            "gunnerRightHandAnimName": "",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        },
        # Class: CfgVehicles|rhsusf_M1232_MK19_usarmy_d|Turrets|CargoTurret_04 [Indent level: 2],
        "CargoTurret_04": {
            # Class: CfgVehicles|rhsusf_M1232_M2_usarmy_d|Turrets|CargoTurret_04|TurnOut [Indent level: 3],

            "TurnOut": {

                "limitsArrayTop": [[45,-160],[45,160]],

                "limitsArrayBottom": [[-28.5738,-127.529],[-33.7087,-92.9864],[-21.1149,-88.4307],[-16.48,-68.1569],[-20.6228,-55.8327],[-35.0127,-28.8438],[-34.4964,62.7092],[-18.33,75.6292],[-12.2273,78.4947],[-5.0579,85.8318],[-1.974,89.1489],[2.6311,94.9857],[2.2924,108.561],[1.4529,119.358],[-0.9739,121.321],[-10.3261,123.401],[-16.7879,151.699]]
            },
            "proxyIndex": 8,
            "gunnerInAction": "RHS_rg33l_Cargo04_FFV",
            "enabledByAnimationSource": "hatch4_door",
            "animationSourceHatch": "hatch4",
            "gunnerName": "Passenger (Right Rear Hatch)",
            "memoryPointsGetInGunner": "pos cargoFFV4",
            "memoryPointsGetInGunnerDir": "pos cargoFFV4 dir",
            "weapons": ["rhsusf_weap_DummyLauncher"],
            "gunnerAction": "vehicle_turnout_1",
            "isPersonTurret": 2,
            "gunnerGetInAction": "GetInMantis",
            "gunnerGetOutAction": "GetOutMantis",
            "rhs_hatch_control": 1,
            "gunnerCompartments": "Compartment1",
            "gunnerDoor": "DoorB",
            "memoryPointGunnerOptics": "",
            "selectionFireAnim": "",
            "canHideGunner": 1,
            "commanding": -2,
            "LODTurnedIn": 1200,
            "LODTurnedOut": 0,
            "maxElev": 45,
            "minElev": -35,
            "maxTurn": 61,
            "minTurn": -65,
            # Class: CfgVehicles|rhsusf_RG33L_base|Turrets|CargoTurret_01|TurnIn [Indent level: 3],
            "TurnIn": {
                "limitsArrayTop": [[0,0],[0,0]],
                "limitsArrayBottom": [[0,0],[0,0]]
            },
            # Class: CfgVehicles|rhsusf_RG33L_base|Turrets|CargoTurret_01|Hitpoints [Indent level: 3],
            "Hitpoints": {
            },
            # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2],
            "ViewGunner": {
                "initAngleX": 5,
                "minAngleX": -75,
                "maxAngleX": 85,
                "initAngleY": 0,
                "minAngleY": -150,
                "maxAngleY": 150,
                "minFov": 0.25,
                "maxFov": 1.25,
                "initFov": 0.75,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "animationSourceBody": "",
            "animationSourceGun": "",
            "body": "",
            "canEject": 1,
            "dontCreateAI": 1,
            "gun": "",
            "hideWeaponsGunner": 0,
            "isCopilot": 0,
            "primaryGunner": 0,
            "proxyType": "CPCargo",
            "startEngine": 0,
            "turretFollowFreeLook": 0,
            "viewGunnerInExternal": 1,
            "disableSoundAttenuation": 1,
            "outGunnerMayFire": 1,
            "showAsCargo": 1,
            "animationSourceCamElev": "camElev",
            "gunnerType": "",
            "primaryObserver": 0,
            "magazines": [],
            "soundServo": ["",0.00316228,1],
            "soundElevation": ["",0.00316228,1],
            "initElev": 0,
            "initTurn": 0,
            "minOutElev": -4,
            "maxOutElev": 20,
            "initOutElev": 0,
            "minOutTurn": -60,
            "maxOutTurn": 60,
            "initOutTurn": 0,
            "maxHorizontalRotSpeed": 1.2,
            "maxVerticalRotSpeed": 1.2,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "stabilizedInAxes": 3,
            "primary": 1,
            "hasGunner": 1,
            "turretCanSee": 0,
            "canUseScanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsModel": "",
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerForceOptics": 1,
            "gunnerOpticsShowCursor": 0,
            "turretInfoType": "",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOpticsEffect": [],
            "gunnerOutOpticsEffect": [],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "castGunnerShadow": 0,
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "forceHideGunner": 0,
            "inGunnerMayFire": 1,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
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
                "interval": 0.01,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 4500,
                "deltaT": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "GunClouds": {
                "access": 0,
                "cloudletDuration": 0.3,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 1,
                "cloudletGrowUp": 1,
                "cloudletFadeIn": 0.01,
                "cloudletFadeOut": 1,
                "cloudletAccY": 0.4,
                "cloudletMinYSpeed": 0.2,
                "cloudletMaxYSpeed": 0.8,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "MGunClouds": {
                "access": 0,
                "cloudletGrowUp": 0.05,
                "cloudletFadeIn": 0,
                "cloudletFadeOut": 0.1,
                "cloudletDuration": 0.05,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 0.3,
                "cloudletAccY": 0,
                "cloudletMinYSpeed": -100,
                "cloudletMaxYSpeed": 100,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "timeToLive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourceSize": 0.02,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "Turrets": {
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.3,
                "minFov": 0.07,
                "maxFov": 0.35,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "forceNVG": 0,
            "gunnerLeftHandAnimName": "",
            "gunnerRightHandAnimName": "",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "preciseGetInOut": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "memoryPointGun": "kulas",
            "showCrewAim": 0
        },
        # Class: CfgVehicles|Car_F|Turrets|MainTurret [Indent level: 2],
        "MainTurret": {
            "stabilizedInAxes": 4,
            "outGunnerMayFire": 1,
            "memoryPointGun": "machinegun",
            "body": "",
            "gun": "",
            "gunnerAction": "ManActTestDriverOut",
            "gunnerGetInAction": "GetInLow",
            "gunnerGetOutAction": "GetOutLow",
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "soundServo": ["A3|sounds_f|dummysound",0.316228,1,15],
            "minElev": -5,
            "maxElev": 40,
            "minTurn": -360,
            "maxTurn": 360,
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "primaryGunner": 1,
            "enableManualFire": 0,
            "gunnerForceOptics": 0,
            "startEngine": 0,
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints [Indent level: 3],
            "HitPoints": {
                # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4],

                "HitTurret": {

                    "armor": 0.8,

                    "material": -1,

                    "name": "vez",

                    "visual": "vez",

                    "passThrough": 0.5,

                    "explosionShielding": 0.4
                },
                # Class: CfgVehicles|Car_F|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "HitGun": {
                    "armor": 0.4,
                    "material": -1,
                    "name": "zbran",
                    "visual": "zbran",
                    "passThrough": 0,
                    "explosionShielding": 0.2
                }
            },
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|ViewOptics [Indent level: 3],
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.3,
                "minFov": 0.07,
                "maxFov": 0.35,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|ViewGunner [Indent level: 3],
            "ViewGunner": {
                "initAngleX": 5,
                "minAngleX": -75,
                "maxAngleX": 85,
                "initAngleY": 0,
                "minAngleY": -150,
                "maxAngleY": 150,
                "minFov": 0.25,
                "maxFov": 1.25,
                "initFov": 0.75,
                "minMoveX": 0,
                "maxMoveX": 0,
                "minMoveY": 0,
                "maxMoveY": 0,
                "minMoveZ": 0,
                "maxMoveZ": 0,
                "continuous": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            # Class: CfgVehicles|Car_F|Turrets|MainTurret|Components [Indent level: 3],
            "Components": {
            },
            "disableSoundAttenuation": 0,
            "animationSourceBody": "mainTurret",
            "animationSourceGun": "mainGun",
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerName": "Gunner",
            "gunnerType": "",
            "primaryObserver": 0,
            "weapons": [],
            "magazines": [],
            "soundElevation": ["",0.00316228,1],
            "initElev": 0,
            "initTurn": 0,
            "minOutElev": -4,
            "maxOutElev": 20,
            "initOutElev": 0,
            "minOutTurn": -60,
            "maxOutTurn": 60,
            "initOutTurn": 0,
            "maxHorizontalRotSpeed": 1.2,
            "maxVerticalRotSpeed": 1.2,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "primary": 1,
            "hasGunner": 1,
            "commanding": 1,
            "turretCanSee": 0,
            "canUseScanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOpticsShowCursor": 0,
            "turretInfoType": "",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOpticsEffect": [],
            "gunnerOutOpticsEffect": [],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "castGunnerShadow": 0,
            "viewGunnerShadow": 1,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "forceHideGunner": 0,
            "inGunnerMayFire": 1,
            "showHMD": 0,
            "viewGunnerInExternal": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "gunnerCompartments": "Compartment1",
            "LODTurnedIn": -1,
            "LODTurnedOut": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
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
                "interval": 0.01,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 4500,
                "deltaT": -3000,
                # Class: WeaponFireGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponFireGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
            "GunClouds": {
                "access": 0,
                "cloudletDuration": 0.3,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 1,
                "cloudletGrowUp": 1,
                "cloudletFadeIn": 0.01,
                "cloudletFadeOut": 1,
                "cloudletAccY": 0.4,
                "cloudletMinYSpeed": 0.2,
                "cloudletMaxYSpeed": 0.8,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "interval": 0.05,
                "size": 3,
                "sourceSize": 0.5,
                "timeToLive": 0,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
            "MGunClouds": {
                "access": 0,
                "cloudletGrowUp": 0.05,
                "cloudletFadeIn": 0,
                "cloudletFadeOut": 0.1,
                "cloudletDuration": 0.05,
                "cloudletAnimPeriod": 1,
                "cloudletSize": 1,
                "cloudletAlpha": 0.3,
                "cloudletAccY": 0,
                "cloudletMinYSpeed": -100,
                "cloudletMaxYSpeed": 100,
                "cloudletShape": "cloudletClouds",
                "cloudletColor": [1,1,1,0],
                "timeToLive": 0,
                "interval": 0.02,
                "size": 0.3,
                "sourceSize": 0.02,
                "initT": 0,
                "deltaT": 0,
                # Class: WeaponCloudsMGun|Table [Indent level: 0],
                "Table": {
                    # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

                    "T0": {

                        "maxT": 0,

                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
            "Turrets": {
            },
            "forceNVG": 0,
            "isCopilot": 0,
            "canEject": 1,
            "gunnerLeftHandAnimName": "",
            "gunnerRightHandAnimName": "",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "gunnerDoor": "",
            "preciseGetInOut": 0,
            "turretFollowFreeLook": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "dontCreateAI": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
            "TurnIn": {
                "turnOffset": 0
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
            "TurnOut": {
                "turnOffset": 0
            },
            "gunnerInAction": "ManActTestDriver",
            "memoryPointGunnerOptics": "gunnerview",
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "selectionFireAnim": "zasleh",
            "showCrewAim": 0
        }
    },
    "picture": "rhsusf|addons|rhsusf_rg33l|pictures|rhs_rg33l_armed_pic_ca.paa",
    "scope": 2,
    "animationList": ["hide_ogpkover",0.5,"hide_ogpknet",0.5,"hide_ogpkbust",0.5],
    # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets [Indent level: 1],
    "RenderTargets": {
        # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets|LeftMirror [Indent level: 2],

        "LeftMirror": {

            "renderTarget": "rendertarget0",

            # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets|LeftMirror|CameraView1 [Indent level: 3],

            "CameraView1": {

                "pointPosition": "m1p",

                "pointDirection": "m1d",

                "renderQuality": 2,

                "renderVisionMode": 4,

                "fov": 0.7
            },

            "BBoxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets|RightMirror [Indent level: 2],
        "RightMirror": {
            "renderTarget": "rendertarget1",
            # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets|RightMirror|CameraView1 [Indent level: 3],
            "CameraView1": {
                "pointPosition": "m2p",
                "pointDirection": "m2d",
                "renderQuality": 2,
                "renderVisionMode": 4,
                "fov": 0.7
            },
            "BBoxes": ["PIP_2_TL","PIP_2_TR","PIP_2_BL","PIP_2_BR"]
        },
        # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets|LeftMirror2 [Indent level: 2],
        "LeftMirror2": {
            "renderTarget": "rendertarget2",
            # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets|LeftMirror2|CameraView1 [Indent level: 3],
            "CameraView1": {
                "pointPosition": "pp4",
                "pointDirection": "pd4",
                "renderQuality": 2,
                "renderVisionMode": 4,
                "fov": 0.7
            },
            "BBoxes": ["PIP_4_TL","PIP_4_TR","PIP_4_BL","PIP_4_BR"]
        },
        # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets|RightMirror2 [Indent level: 2],
        "RightMirror2": {
            "renderTarget": "rendertarget3",
            # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets|RightMirror2|CameraView1 [Indent level: 3],
            "CameraView1": {
                "pointPosition": "pp3",
                "pointDirection": "pd3",
                "renderQuality": 2,
                "renderVisionMode": 4,
                "fov": 0.7
            },
            "BBoxes": ["PIP_3_TL","PIP_3_TR","PIP_3_BL","PIP_3_BR"]
        },
        # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets|DVE_Monitor [Indent level: 2],
        "DVE_Monitor": {
            "renderTarget": "rendertarget_dve",
            # Class: CfgVehicles|rhsusf_RG33L_GPK_base|RenderTargets|DVE_Monitor|CameraView1 [Indent level: 3],
            "CameraView1": {
                "pointPosition": "dve_view_pos",
                "pointDirection": "dve_view_dir",
                "renderQuality": 2,
                "renderVisionMode": 2,
                "fov": 0.6
            },
            "BBoxes": ["PIP_DVE_TL","PIP_DVE_TR","PIP_DVE_BL","PIP_DVE_BR"]
        }
    },
    "dlc": "RHS_USAF",
    "category": "Car",
    "side": 1,
    "editorSubcategory": "rhs_EdSubcat_mrap",
    "vehicleClass": "rhs_vehclass_MRAP",
    "insideSoundCoef": 0.4,
    "unitInfoType": "RscUnitInfo",
    "weapons": ["TruckHorn2","rhsusf_weap_duke"],
    "magazines": ["rhsusf_mag_duke"],
    "smokeLauncherGrenadeCount": 1,
    "smokeLauncherVelocity": 14,
    "smokeLauncherOnTurret": 0,
    "smokeLauncherAngle": 150,
    "Icon": "a3|soft_f_beta|Truck_01|Data|UI|map_truck_01_CA.paa",
    "mapSize": 12.02,
    "transportMaxBackpacks": 25,
    "transportSoldier": 5,
    "destrType": "DestructDefault",
    "crewExplosionProtection": 1,
    "camShakeCoef": 0.3,
    # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines [Indent level: 1],
    "TransportMagazines": {
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2],

        "_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag": {

            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",

            "count": 25
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhsusf_100Rnd_556x45_soft_pouch [Indent level: 2],
        "_xx_rhsusf_100Rnd_556x45_soft_pouch": {
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch",
            "count": 11
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhsusf_100Rnd_762x51 [Indent level: 2],
        "_xx_rhsusf_100Rnd_762x51": {
            "magazine": "rhsusf_100Rnd_762x51",
            "count": 11
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_fgm148_magazine_AT [Indent level: 2],
        "_xx_rhs_fgm148_magazine_AT": {
            "magazine": "rhs_fgm148_magazine_AT",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_m136_mag [Indent level: 2],
        "_xx_rhs_m136_mag": {
            "magazine": "rhs_m136_mag",
            "count": 2
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_mag_M441_HE [Indent level: 2],
        "_xx_rhs_mag_M441_HE": {
            "magazine": "rhs_mag_M441_HE",
            "count": 20
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_mag_M714_white [Indent level: 2],
        "_xx_rhs_mag_M714_white": {
            "magazine": "rhs_mag_M714_white",
            "count": 8
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_mag_M662_red [Indent level: 2],
        "_xx_rhs_mag_M662_red": {
            "magazine": "rhs_mag_M662_red",
            "count": 4
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 10
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 4
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 4
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 10
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportMagazines|_xx_rhs_m136_hedp_mag [Indent level: 2],
        "_xx_rhs_m136_hedp_mag": {
            "magazine": "rhs_m136_hedp_mag",
            "count": 2
        }
    },
    # Class: CfgVehicles|rhsusf_RG33L_base|TransportItems [Indent level: 1],
    "TransportItems": {
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportItems|_xx_FirstAidKit [Indent level: 2],

        "_xx_FirstAidKit": {

            "name": "FirstAidKit",

            "count": 10
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_Toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhsusf_RG33L_base|TransportWeapons [Indent level: 1],
    "TransportWeapons": {
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportWeapons|_xx_rhs_weap_m4_carryhandle [Indent level: 2],

        "_xx_rhs_weap_m4_carryhandle": {

            "weapon": "rhs_weap_m4_carryhandle",

            "count": 2
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportWeapons|_xx_rhs_weap_M136 [Indent level: 2],
        "_xx_rhs_weap_M136": {
            "weapon": "rhs_weap_M136",
            "count": 2
        }
    },
    "dustFrontLeftPos": "wheel_1_1_bound",
    "dustFrontRightPos": "wheel_2_1_bound",
    "dustBackLeftPos": "wheel_1_3_bound",
    "dustBackRightPos": "wheel_2_3_bound",
    "tf_hasLRradio_api": 1,
    "selectionBrakeLights": "light_brake",
    "selectionBackLights": "light_drive",
    "driverAction": "RHS_HMMWV_Driver",
    "driverInAction": "RHS_HMMWV_Driver",
    "viewDriverInExternal": 1,
    "forceHideDriver": 1,
    "driverLeftHandAnimName": "drivewheel",
    "driverRightHandAnimName": "drivewheel",
    "cargoProxyIndexes": [1,2,3,4,5],
    "getInProxyOrder": [1,2,3,4,5,6,7,8,9],
    "memoryPointsGetInCargo": ["pos codriver","pos cargo"],
    "memoryPointsGetInCargoDir": ["pos codriver dir","pos cargo dir"],
    "getInAction": "GetInMRAP_01",
    "getOutAction": "GetOutMRAP_01",
    "driverDoor": "DoorL",
    "cargoDoors": ["DoorR","DoorB"],
    "hiddenSelections": ["camo","camo1","camo2","camo3","camo4","camo5","pintle","camo7","camo8","camo9"],
    # Class: CfgVehicles|rhsusf_RG33L_base|textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles|rhsusf_RG33L_base|textureSources|rhs_desert [Indent level: 2],

        "rhs_desert": {

            "displayName": "Desert",

            "author": "Red Hammer Studios",

            "textures": ["rhsusf|addons|rhsusf_RG33L|data|RG33_Body_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Chassis_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Accessory2_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Armor_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_TurretD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Wheels_CO.paa","rhsusf|addons|rhsusf_hmmwv|textures|mk64mount_d_co.paa","rhsusf|addons|rhsusf_RG33L|data|MCTAGS_CO.paa","rhsusf|addons|rhsusf_rg33l|Data|rhsusf_camonet_des_co.paa"],

            "factions": []
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|textureSources|rhs_woodland [Indent level: 2],
        "rhs_woodland": {
            "displayName": "Woodland",
            "author": "Red Hammer Studios",
            "textures": ["rhsusf|addons|rhsusf_RG33L|data|RG33_Body_WD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Chassis_WD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Accessory2_WD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Armor_WD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_TurretWD_CO.paa","rhsusf|addons|rhsusf_RG33L|data|RG33_Wheels_WD_CO.paa","rhsusf|addons|rhsusf_hmmwv|textures|mk64mount_w_co.paa","rhsusf|addons|rhsusf_RG33L|data|MCTAGS_WD_CO.paa","rhsusf|addons|rhsusf_rg33l|Data|rhsusf_camonet_wdl_co.paa"],
            "factions": []
        }
    },
    "textureList": [],
    # Class: CfgVehicles|rhsusf_RG33L_base|Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles|rhsusf_RG33L_base|Attributes|ObjectTexture [Indent level: 2],

        "ObjectTexture": {

            "control": "ObjectTexture",

            "data": "ObjectTexture",

            "displayName": "Skin",

            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Attributes|rhs_hideDUKE [Indent level: 2],
        "rhs_hideDUKE": {
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "displayName": "hide DUKE antennas",
            "property": "rhs_hideDUKE",
            "expression": "_this animate ['DUKE_Hide',_value,true];if(_value isEqualTo 1)then{_this removeWeaponTurret ['rhsusf_weap_duke',[-1]]};"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Attributes|DoorB [Indent level: 2],
        "DoorB": {
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "displayName": "Open rear door",
            "property": "Door_B",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Attributes|DoorL [Indent level: 2],
        "DoorL": {
            "displayName": "Open left door",
            "property": "Door_L",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Attributes|DoorR [Indent level: 2],
        "DoorR": {
            "displayName": "Open right door",
            "property": "Door_R",
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "expression": "_this animateDoor ['%s',_value,true]"
        }
    },
    "cargoCompartments": [1,1],
    # Class: CfgVehicles|rhsusf_RG33L_base|DriverOpticsIn [Indent level: 1],
    "DriverOpticsIn": {
        # Class: CfgVehicles|rhsusf_RG33L_base|DriverOpticsIn|DVE_Wide [Indent level: 2],

        "DVE_Wide": {

            "camPos": "dve_view_pos",

            "opticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_DVE_4x3",

            "visionMode": ["TI"],

            "thermalMode": [0,1],

            "initFov": 0.6,

            "minFov": 0.6,

            "maxFov": 0.6,

            "hitpoint": "Hit_Optic_DVEA",

            "initAngleX": 0,

            "minAngleX": -30,

            "maxAngleX": 30,

            "initAngleY": 0,

            "minAngleY": -100,

            "maxAngleY": 100,

            "minMoveX": 0,

            "maxMoveX": 0,

            "minMoveY": 0,

            "maxMoveY": 0,

            "minMoveZ": 0,

            "maxMoveZ": 0,

            "speedZoomMaxSpeed": 1e+010,

            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|DriverOpticsIn|DVS_Rear [Indent level: 2],
        "DVS_Rear": {
            "camPos": "dve_view_rear_pos",
            "camDir": "dve_view_rear_dir",
            "initFov": 0.875,
            "minFov": 0.875,
            "maxFov": 0.875,
            "hitpoint": "Hit_Optic_Driver_Rear",
            "opticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_DVE_4x3",
            "visionMode": ["TI"],
            "thermalMode": [0,1],
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        }
    },
    # Class: CfgVehicles|rhsusf_RG33L_base|UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles|rhsusf_RG33L_base|UserActions|light_bo_off [Indent level: 2],

        "light_bo_off": {

            "displayName": "B.O. Light off",

            "position": "pos_driverpos",

            "radius": 2,

            "onlyForplayer": 0,

            "condition": "(player == driver this) && this animationPhase 'light_bo'<0.5;",

            "statement": "this animate ['light_bo', 1];this animate ['light_brake_bo', 1]"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|UserActions|toggle_dve [Indent level: 2],
        "toggle_dve": {
            "displayName": "Toggle DVE monitor",
            "position": "zamerny",
            "radius": 12,
            "showwindow": 0,
            "condition": "((driver this) isEqualTo (call rhs_fnc_findPlayer))",
            "statement": "this animateSource ['dve_fold',abs((this AnimationSourcePhase 'dve_fold') - 1)]",
            "onlyForplayer": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|UserActions|light_bo_on [Indent level: 2],
        "light_bo_on": {
            "displayName": "B.O. Light on",
            "condition": "(player == driver this) && this animationPhase 'light_bo'==1;",
            "statement": "this animate ['light_bo', 0];this animate ['light_brake_bo', 0]",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyForplayer": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|UserActions|light_stop_off [Indent level: 2],
        "light_stop_off": {
            "displayName": "Stop Light off",
            "condition": "(player == driver this) && this animationPhase 'light_stop'<0.5",
            "statement": "this animate ['light_stop', 1]",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyForplayer": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|UserActions|light_stop_on [Indent level: 2],
        "light_stop_on": {
            "displayName": "Stop Light on",
            "condition": "(player == driver this) && this animationPhase 'light_stop'==1",
            "statement": "this animate ['light_stop', 0]",
            "position": "pos_driverpos",
            "radius": 2,
            "onlyForplayer": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|UserActions|lights_toggle [Indent level: 2],
        "lights_toggle": {
            "displayName": "Toggle short/long lights",
            "position": "",
            "shortcut": "vehLockTargets",
            "radius": 12,
            "priority": 1.5,
            "showWindow": 0,
            "onlyForplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)",
            "statement": "[this,0] call rhsusf_fnc_carLightToggle"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|UserActions|cabinlights_toggle [Indent level: 2],
        "cabinlights_toggle": {
            "shortcut": "lockTarget",
            "displayName": "Toggle cabin lights",
            "statement": "[this,1] call rhsusf_fnc_carLightToggle",
            "position": "",
            "radius": 12,
            "priority": 1.5,
            "showWindow": 0,
            "onlyForplayer": 1,
            "condition": "(player == driver this) AND (isLightOn this)"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|UserActions|OpenCargoDoor [Indent level: 2],
        "OpenCargoDoor": {
            "displayName": "Open Rear Door",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "this doorPhase 'DoorB' == 0 and {(call rhsusf_fnc_findPlayer) in this};",
            "statement": "this animateDoor ['DoorB', 1];this setVariable ['ramp_handler',1,true]",
            "onlyforplayer": 1,
            "shortcut": "user12"
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|UserActions|CloseCargoDoor [Indent level: 2],
        "CloseCargoDoor": {
            "displayName": "Close Rear Door",
            "condition": "this doorPhase 'DoorB' > 0 and {(call rhsusf_fnc_findPlayer) in this};",
            "statement": "this animateDoor ['DoorB', 0];this setVariable ['ramp_handler',0,true]",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1,
            "shortcut": "user12"
        }
    },
    "hullDamageCauseExplosion": 1,
    "armorStructural": 8,
    # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints [Indent level: 1],
    "HitPoints": {
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitHull [Indent level: 2],

        "HitHull": {

            "armor": 0.75,

            "passThrough": 1,

            "name": "karoserie",

            "visual": "zbytek",

            "minimalhit": 0.05,

            "explosionShielding": 0.01,

            "radius": 0.22,

            "material": -1
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitFuel [Indent level: 2],
        "HitFuel": {
            "armor": 1.5,
            "material": -1,
            "name": "palivo",
            "visual": "-",
            "explosionShielding": 0.5,
            "passThrough": 0.2
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitEngine [Indent level: 2],
        "HitEngine": {
            "armor": 0.9,
            "material": -1,
            "name": "motor",
            "visual": "zbytek",
            "passThrough": 0.2,
            # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire [Indent level: 4],
                "RHS_Engine_Fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks [Indent level: 4],
                "RHS_Engine_Sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                }
            }
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitDuke1 [Indent level: 2],
        "HitDuke1": {
            "armor": 0.75,
            "material": -1,
            "name": "duke1",
            "visual": "-",
            "passThrough": 0,
            "MinimalHit": 0.05,
            "explosionShielding": 0.01,
            "radius": 0.15
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitDuke2 [Indent level: 2],
        "HitDuke2": {
            "name": "duke2",
            "visual": "-",
            "armor": 0.75,
            "material": -1,
            "passThrough": 0,
            "MinimalHit": 0.05,
            "explosionShielding": 0.01,
            "radius": 0.15
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass7 [Indent level: 2],
        "HitGlass7": {
            "name": "glass7",
            "visual": "glass7",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass8 [Indent level: 2],
        "HitGlass8": {
            "name": "glass8",
            "visual": "glass8",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass9 [Indent level: 2],
        "HitGlass9": {
            "name": "glass9",
            "visual": "glass9",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass10 [Indent level: 2],
        "HitGlass10": {
            "name": "glass10",
            "visual": "glass10",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass11 [Indent level: 2],
        "HitGlass11": {
            "name": "glass11",
            "visual": "glass11",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass12 [Indent level: 2],
        "HitGlass12": {
            "name": "glass12",
            "visual": "glass12",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass13 [Indent level: 2],
        "HitGlass13": {
            "name": "glass13",
            "visual": "glass13",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass14 [Indent level: 2],
        "HitGlass14": {
            "name": "glass14",
            "visual": "glass14",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass15 [Indent level: 2],
        "HitGlass15": {
            "name": "glass15",
            "visual": "glass15",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass16 [Indent level: 2],
        "HitGlass16": {
            "name": "glass16",
            "visual": "glass16",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass17 [Indent level: 2],
        "HitGlass17": {
            "name": "glass17",
            "visual": "glass17",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass18 [Indent level: 2],
        "HitGlass18": {
            "name": "glass18",
            "visual": "glass18",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass19 [Indent level: 2],
        "HitGlass19": {
            "name": "glass19",
            "visual": "glass19",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass20 [Indent level: 2],
        "HitGlass20": {
            "name": "glass20",
            "visual": "glass20",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|HitPoints|HitGlass21 [Indent level: 2],
        "HitGlass21": {
            "name": "glass21",
            "visual": "glass21",
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "passThrough": 0
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitLFWheel [Indent level: 2],
        "HitLFWheel": {
            "radius": 0.33,
            "visual": "wheel_1_1_damage",
            "armorComponent": "wheel_1_1_hide",
            "armor": -250,
            "minimalHit": -0.016,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_1_1_steering"
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitLF2Wheel [Indent level: 2],
        "HitLF2Wheel": {
            "radius": 0.33,
            "visual": "wheel_1_2_damage",
            "armorComponent": "wheel_1_2_hide",
            "armor": -250,
            "minimalHit": -0.016,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_1_2_steering"
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitRFWheel [Indent level: 2],
        "HitRFWheel": {
            "radius": 0.33,
            "visual": "wheel_2_1_damage",
            "armorComponent": "wheel_2_1_hide",
            "armor": -250,
            "minimalHit": -0.016,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_2_1_steering"
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitRF2Wheel [Indent level: 2],
        "HitRF2Wheel": {
            "radius": 0.33,
            "visual": "wheel_2_2_damage",
            "armorComponent": "wheel_2_2_hide",
            "armor": -250,
            "minimalHit": -0.016,
            "explosionShielding": 4,
            "passThrough": 0,
            "material": -1,
            "name": "wheel_2_2_steering"
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitBody [Indent level: 2],
        "HitBody": {
            "armor": 6,
            "material": -1,
            "name": "karoserie",
            "visual": "zbytek",
            "passThrough": 1,
            "minimalHit": 0.01,
            "explosionShielding": 1.5,
            "radius": 0.45
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "passThrough": 0
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitGlass3 [Indent level: 2],
        "HitGlass3": {
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "name": "glass3",
            "visual": "glass3",
            "passThrough": 0
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitGlass4 [Indent level: 2],
        "HitGlass4": {
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "name": "glass4",
            "visual": "glass4",
            "passThrough": 0
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitGlass5 [Indent level: 2],
        "HitGlass5": {
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "name": "glass5",
            "visual": "glass5",
            "passThrough": 0
        },
        # Class: CfgVehicles|MRAP_01_base_F|HitPoints|HitGlass6 [Indent level: 2],
        "HitGlass6": {
            "armor": 1.5,
            "explosionShielding": 3,
            "radius": 0.25,
            "material": -1,
            "name": "glass6",
            "visual": "glass6",
            "passThrough": 0
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitRGlass [Indent level: 2],
        "HitRGlass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni P",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitLGlass [Indent level: 2],
        "HitLGlass": {
            "armor": 0.2,
            "material": -1,
            "name": "sklo predni L",
            "passThrough": 0,
            "explosionShielding": 2
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitLBWheel [Indent level: 2],
        "HitLBWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_4_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitLMWheel [Indent level: 2],
        "HitLMWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_1_3_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitRBWheel [Indent level: 2],
        "HitRBWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_4_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        },
        # Class: CfgVehicles|Car_F|HitPoints|HitRMWheel [Indent level: 2],
        "HitRMWheel": {
            "armor": 0.2,
            "material": -1,
            "name": "wheel_2_3_steering",
            "visual": "-",
            "passThrough": 0.3,
            "explosionShielding": 4
        }
    },
    # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Left [Indent level: 2],

        "Left": {

            "color": [1900,1300,950],

            "ambient": [5,5,5],

            "position": "Light_L",

            "direction": "Light_L_end",

            "hitpoint": "Light_L",

            "selection": "Light_L",

            "size": 1,

            "innerAngle": 100,

            "outerAngle": 179,

            "coneFadeCoef": 10,

            "intensity": 1,

            "useFlare": 0,

            "dayLight": 0,

            "flareSize": 1,

            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Left|Attenuation [Indent level: 3],

            "Attenuation": {

                "start": 1,

                "constant": 0,

                "linear": 0,

                "quadratic": 0.25,

                "hardLimitStart": 30,

                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Right [Indent level: 2],
        "Right": {
            "position": "Light_R",
            "direction": "Light_R_end",
            "hitpoint": "Light_R",
            "selection": "Light_R",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Left|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Right2 [Indent level: 2],
        "Right2": {
            "position": "light_R_flare",
            "useFlare": 1,
            "direction": "Light_R_end",
            "hitpoint": "Light_R",
            "selection": "Light_R",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Left|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Left2 [Indent level: 2],
        "Left2": {
            "position": "light_L_flare",
            "useFlare": 1,
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerAngle": 100,
            "outerAngle": 179,
            "coneFadeCoef": 10,
            "intensity": 1,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Left|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Long_Left [Indent level: 2],
        "Long_Left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L_Long",
            "direction": "Light_L_Long_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerAngle": 22,
            "outerAngle": 26,
            "coneFadeCoef": 1,
            "intensity": 100,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750,
            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Long_Left|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Long_Right [Indent level: 2],
        "Long_Right": {
            "position": "Light_R_Long",
            "direction": "Light_R_Long_end",
            "hitpoint": "Light_R",
            "selection": "Light_R",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerAngle": 22,
            "outerAngle": 26,
            "coneFadeCoef": 1,
            "intensity": 100,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750,
            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Long_Left|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0.1,
                "quadratic": 0,
                "hardLimitStart": 500,
                "hardLimitEnd": 750
            }
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Long_Right2 [Indent level: 2],
        "Long_Right2": {
            "useFlare": 1,
            "position": "light_R_Long_flare",
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Long_Right2|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "direction": "Light_R_Long_end",
            "hitpoint": "Light_R",
            "selection": "Light_R",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Long_Left2 [Indent level: 2],
        "Long_Left2": {
            "useFlare": 1,
            "position": "light_L_Long_flare",
            "innerAngle": 50,
            "outerAngle": 179,
            "coneFadeCoef": 51,
            "intensity": 1,
            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|Long_Left2|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 50,
                "hardLimitStart": 0,
                "hardLimitEnd": 3
            },
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "direction": "Light_L_Long_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "dayLight": 0,
            "flareSize": 1.5,
            "flareMaxDistance": 750
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|cabin1 [Indent level: 2],
        "cabin1": {
            "color": [800,900,650],
            "ambient": [5,5,5],
            "intensity": 4,
            "size": 1,
            "innerAngle": 90,
            "outerAngle": 165,
            "coneFadeCoef": 1,
            "position": "cabin_light1",
            "direction": "cabin_light1_dir",
            "hitpoint": "cabin_light1",
            "selection": "cabin_light1",
            "useFlare": 1,
            "flareSize": 1,
            "flareMaxDistance": 5,
            "dayLight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|cabin1|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 70,
                "hardLimitStart": 2,
                "hardLimitEnd": 2.5
            }
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|cabin2 [Indent level: 2],
        "cabin2": {
            "position": "cabin_light2",
            "direction": "cabin_light2_dir",
            "hitpoint": "cabin_light2",
            "selection": "cabin_light2",
            "color": [800,900,650],
            "ambient": [5,5,5],
            "intensity": 4,
            "size": 1,
            "innerAngle": 90,
            "outerAngle": 165,
            "coneFadeCoef": 1,
            "useFlare": 1,
            "flareSize": 1,
            "flareMaxDistance": 5,
            "dayLight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|cabin1|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 70,
                "hardLimitStart": 2,
                "hardLimitEnd": 2.5
            }
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|cabin3 [Indent level: 2],
        "cabin3": {
            "position": "cabin_light3",
            "direction": "cabin_light3_dir",
            "hitpoint": "cabin_light3",
            "selection": "cabin_light3",
            "color": [800,900,650],
            "ambient": [5,5,5],
            "intensity": 4,
            "size": 1,
            "innerAngle": 90,
            "outerAngle": 165,
            "coneFadeCoef": 1,
            "useFlare": 1,
            "flareSize": 1,
            "flareMaxDistance": 5,
            "dayLight": 0,
            "blinking": 0,
            # Class: CfgVehicles|rhsusf_RG33L_base|Reflectors|cabin1|Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 70,
                "hardLimitStart": 2,
                "hardLimitEnd": 2.5
            }
        }
    },
    "aggregateReflectors": [["Left","Left2"],["Right","Right2"]],
    "armorLights": 0.01,
    "normalSpeedForwardCoef": 0.9,
    "turnCoef": 3.5,
    "terrainCoef": 0.5,
    "simulation": "carx",
    "precision": 9,
    "brakeDistance": 3,
    "acceleration": 15,
    "fireResistance": 5,
    "maxSpeed": 105,
    "fuelCapacity": 20,
    "wheelCircumference": 2.95,
    "brakeIdleSpeed": 2,
    "maxFordingDepth": 0.4,
    "waterSpeedFactor": 0.3,
    "waterResistance": 10,
    "waterResistanceCoef": 0.2,
    "waterLeakiness": 250,
    # Class: CfgVehicles|rhsusf_RG33L_base|complexGearbox [Indent level: 1],
    "complexGearbox": {
        "GearboxRatios": ["R1",-5.03,"N",0,"D1",3.49,"D2",1.86,"D3",1.41,"D4",1,"D5",0.75,"D6",0.55],
        "TransmissionRatios": ["High",8.2],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R"
    },
    "changeGearMinEffectivity": [0.95,0,0.99,0.99,0.99,0.99,0.99,0.99],
    "switchTime": 0.31,
    "latency": 1.3,
    "transmissionLosses": 18,
    "dampersBumpCoef": 6,
    "differentialType": "all_limited",
    "frontRearSplit": 0.5,
    "frontBias": 1.3,
    "rearBias": 1.3,
    "centreBias": 1.3,
    "clutchStrength": 85,
    "dampingRateFullThrottle": 0.078,
    "dampingRateZeroThrottleClutchEngaged": 1.35,
    "dampingRateZeroThrottleClutchDisengaged": 0.35,
    "torqueCurve": [[0.318182,0.457898],[0.454545,0.786724],[0.590909,1],[0.636364,1],[0.727273,0.990781],[0.909091,0.974186],[0.954545,0.940381],[1.05273,0]],
    "enginePower": 336,
    "peakTorque": 2277.8,
    "minOmega": 65,
    "maxOmega": 230.38,
    "idleRPM": 700,
    "redRPM": 2200,
    "engineLosses": 12,
    "thrustDelay": 1,
    "engineBrakeCoef": 0.8,
    "antiRollbarForceCoef": 1.5,
    "antiRollbarForceLimit": 2.5,
    "antiRollbarSpeedMin": 10,
    "antiRollbarSpeedMax": 65,
    "accelAidForceSpd": 2.23,
    "accelAidForceCoef": 4,
    "accelAidForceYOffset": -1.3,
    # Class: CfgVehicles|rhsusf_RG33L_base|Wheels [Indent level: 1],
    "Wheels": {
        # Class: CfgVehicles|rhsusf_RG33L_base|Wheels|L1 [Indent level: 2],

        "L1": {

            "side": "left",

            "boneName": "wheel_1_1_damper",

            "center": "wheel_1_1_axis",

            "boundary": "wheel_1_1_bound",

            "suspForceAppPointOffset": "wheel_1_1_axis",

            "tireForceAppPointOffset": "wheel_1_1_axis",

            "suspTravelDirection": [-0.125,-1,0],

            "width": 0.37,

            "steering": 1,

            "mass": 80,

            "MOI": 25,

            "dampingRate": 0.1,

            "dampingRateDamaged": 1,

            "dampingRateDestroyed": 1000,

            "maxBrakeTorque": 35000,

            "maxHandBrakeTorque": 0,

            "maxCompression": 0.15,

            "maxDroop": 0.15,

            "sprungMass": -1,

            "springStrength": 305000,

            "springDamperRate": 45725,

            "longitudinalStiffnessPerUnitGravity": 10000,

            "latStiffX": 40,

            "latStiffY": 180,

            "frictionVsSlipGraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Wheels|L2 [Indent level: 2],
        "L2": {
            "boneName": "wheel_1_2_damper",
            "steering": 0,
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "suspForceAppPointOffset": "wheel_1_2_axis",
            "tireForceAppPointOffset": "wheel_1_2_axis",
            "side": "left",
            "suspTravelDirection": [-0.125,-1,0],
            "width": 0.37,
            "mass": 80,
            "MOI": 25,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 35000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": -1,
            "springStrength": 305000,
            "springDamperRate": 45725,
            "longitudinalStiffnessPerUnitGravity": 10000,
            "latStiffX": 40,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Wheels|L3 [Indent level: 2],
        "L3": {
            "boneName": "wheel_1_3_damper",
            "steering": 0,
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "suspForceAppPointOffset": "wheel_1_3_axis",
            "tireForceAppPointOffset": "wheel_1_3_axis",
            "maxHandBrakeTorque": 300000,
            "side": "left",
            "suspTravelDirection": [-0.125,-1,0],
            "width": 0.37,
            "mass": 80,
            "MOI": 25,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 35000,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": -1,
            "springStrength": 305000,
            "springDamperRate": 45725,
            "longitudinalStiffnessPerUnitGravity": 10000,
            "latStiffX": 40,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Wheels|R1 [Indent level: 2],
        "R1": {
            "boneName": "wheel_2_1_damper",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "suspForceAppPointOffset": "wheel_2_1_axis",
            "tireForceAppPointOffset": "wheel_2_1_axis",
            "steering": 1,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": 0.37,
            "mass": 80,
            "MOI": 25,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 35000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": -1,
            "springStrength": 305000,
            "springDamperRate": 45725,
            "longitudinalStiffnessPerUnitGravity": 10000,
            "latStiffX": 40,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Wheels|R2 [Indent level: 2],
        "R2": {
            "boneName": "wheel_2_2_damper",
            "steering": 0,
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "suspForceAppPointOffset": "wheel_2_2_axis",
            "tireForceAppPointOffset": "wheel_2_2_axis",
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": 0.37,
            "mass": 80,
            "MOI": 25,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 35000,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": -1,
            "springStrength": 305000,
            "springDamperRate": 45725,
            "longitudinalStiffnessPerUnitGravity": 10000,
            "latStiffX": 40,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,2.5],[0.5,2.3],[1,2]]
        },
        # Class: CfgVehicles|rhsusf_RG33L_base|Wheels|R3 [Indent level: 2],
        "R3": {
            "boneName": "wheel_2_3_damper",
            "steering": 0,
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "suspForceAppPointOffset": "wheel_2_3_axis",
            "tireForceAppPointOffset": "wheel_2_3_axis",
            "maxHandBrakeTorque": 300000,
            "side": "right",
            "suspTravelDirection": [0.125,-1,0],
            "width": 0.37,
            "mass": 80,
            "MOI": 25,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 35000,
            "maxCompression": 0.15,
            "maxDroop": 0.15,
            "sprungMass": -1,
            "springStrength": 305000,
            "springDamperRate": 45725,
            "longitudinalStiffnessPerUnitGravity": 10000,
            "latStiffX": 40,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,2.5],[0.5,2.3],[1,2]]
        }
    },
    # Class: CfgVehicles|rhsusf_RG33L_base|Damage [Indent level: 1],
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_rg33l|data|RG33_Body.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Body_dam.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_destruction.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Armor.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Armor_dam.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_destruction.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Accessory2.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Accessory2_dam.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_destruction.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Interior.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Interior_dam.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_destruction.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Wheels.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Wheels_dam.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_destruction.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Chassis.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_Chassis_dam.rvmat","rhsusf|addons|rhsusf_rg33l|data|RG33_destruction.rvmat","rhsusf|addons|rhsusf_rg33|data|glass.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_int.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|glass_veh_armored_damage.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles|rhsusf_RG33L_base|EventHandlers [Indent level: 1],
    "EventHandlers": {
        "init": "if (local (_this select 0)) then {[(_this select 0), `, [], false] call bis_fnc_initVehicle;};",
        # Class: CfgVehicles|rhsusf_RG33L_base|EventHandlers|RHSUSF_EventHandlers [Indent level: 2],
        "RHSUSF_EventHandlers": {
            "seatSwitched": "if(not(_this select 1 in [driver (_this select 0),gunner (_this select 0)]))then{ (_this select 1) action ['turnIn',_this select 0]}",
            "turnIn": "([0] + _this)  call rhsusf_fnc_turretAction;",
            "turnOut": "([1] + _this) call rhsusf_fnc_turretAction;"
        },
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    # Class: CfgVehicles|rhsusf_RG33L_base|TransportBackpacks [Indent level: 1],
    "TransportBackpacks": {
        # Class: CfgVehicles|rhsusf_RG33L_base|TransportBackpacks|_xx_rhsusf_falconii [Indent level: 2],

        "_xx_rhsusf_falconii": {

            "backpack": "rhsusf_falconii",

            "count": 1
        }
    },
    "soundGetIn": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|handling|getin|mrap_1.ogg",0.5,1],
    "soundGetOut": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|handling|getout|mrap_1.ogg",0.5,1,40],
    "soundDammage": [".ogg",0.5,1],
    "soundEngineOnInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_01|mrap_01_start_int.ogg",1,1],
    "soundEngineOffInt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_01|mrap_01_shut_int.ogg",1,1],
    "soundEngineOnExt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_01|mrap_01_start_ext.ogg",1,1,125],
    "soundEngineOffExt": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|engines|mrap_01|mrap_01_shut_ext.ogg",1,1,100],
    "buildCrash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_01.ogg",1.5,1,300],
    "buildCrash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_02.ogg",1.5,1,300],
    "buildCrash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_03.ogg",1.5,1,300],
    "buildCrash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_building_04.ogg",1.5,1,300],
    "buildCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "buildCrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "buildCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "buildCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundBuildingCrash": ["buildcrash0",0.25,"buildcrash1",0.25,"buildcrash2",0.25,"buildcrash3",0.25],
    "WoodCrash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_01.ogg",1.5,1,300],
    "WoodCrash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_02.ogg",1.5,1,300],
    "WoodCrash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_03.ogg",1.5,1,300],
    "WoodCrash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_04.ogg",1.5,1,300],
    "WoodCrash4": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_05.ogg",1.5,1,300],
    "WoodCrash5": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_mix_wood_06.ogg",1.5,1,300],
    "WoodCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_07",1.99526,1,75],
    "WoodCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_Wood_08",1.99526,1,75],
    "soundWoodCrash": ["woodcrash0",0.166,"woodcrash1",0.166,"woodcrash2",0.166,"woodcrash3",0.166,"woodcrash4",0.166,"woodcrash5",0.166],
    "armorCrash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_01.ogg",1.5,1,300],
    "armorCrash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_02.ogg",1.5,1,300],
    "armorCrash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_03.ogg",1.5,1,300],
    "armorCrash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_04.ogg",1.5,1,300],
    "armorCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_05",1.99526,1,75],
    "armorCrash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "armorCrash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "armorCrash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundArmorCrash": ["armorcrash0",0.25,"armorcrash1",0.25,"armorcrash2",0.25,"armorcrash3",0.25],
    "Crash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_01.ogg",1.5,1,300],
    "Crash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_02.ogg",1.5,1,300],
    "Crash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_03.ogg",1.5,1,300],
    "Crash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_04.ogg",1.5,1,300],
    "Crash4": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_05.ogg",1.5,1,300],
    "Crash5": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_06",1.99526,1,75],
    "Crash6": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_07",1.99526,1,75],
    "Crash7": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Medium_08",1.99526,1,75],
    "soundCrashes": ["crash0",0.2,"crash1",0.2,"crash2",0.2,"crash3",0.2,"crash4",0.2],
    "BushCrash1": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_01",0.630957,1,50],
    "BushCrash2": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_02",0.630957,1,50],
    "BushCrash3": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_03",0.630957,1,50],
    "BushCrash4": ["A3|Sounds_F|vehicles2|soft|shared|collisions|Vehicle_Soft_Collision_Light_Bush_03",0.630957,0.8,50],
    "soundBushCrash": ["BushCrash1",0.25,"BushCrash2",0.25,"BushCrash3",0.25,"BushCrash4",0.25],
    # Class: CfgVehicles|MRAP_01_base_F|Sounds [Indent level: 1],
    "Sounds": {
        "soundSetsInt": ["jsrs_mrap_01_idle_interior_soundset","jsrs_mrap_01_low_interior_soundset","jsrs_mrap_01_high_interior_soundset","jsrs_mrap_01_low_off_interior_soundset","jsrs_mrap_01_high_off_interior_soundset","jsrs_mrap_01_start_interior_soundset","jsrs_vehicle_interior_silent_soundset","jsrs_wheeled_driving_noises_soundset","jsrs_wheeled_offroad_driving_noises_soundset","jsrs_light_vehicle_rain_int_soundset","jsrs_wheeled_medium_rattle_int_soundset","jsrs_wheeled_medium_offroad_rattle_int_soundset","jsrs_tires_asphalt_slow_int_soundset","jsrs_tires_asphalt_fast_int_soundset","jsrs_tires_offroad_slow_int_soundset","jsrs_tires_offroad_fast_int_soundset","jsrs_tires_grass_int_soundset","jsrs_medium_vehicle_water_moving_int_soundset"],
        "soundSetsExt": ["jsrs_mrap_01_idle_exterior_soundset","jsrs_mrap_01_low_exterior_soundset","jsrs_mrap_01_high_exterior_soundset","jsrs_mrap_01_low_off_exterior_soundset","jsrs_mrap_01_high_off_exterior_soundset","jsrs_mrap_01_start_exterior_soundset","jsrs_mrap_01_distance_soundset","jsrs_light_vehicle_rain_ext_soundset","jsrs_wheeled_medium_rattle_ext_soundset","jsrs_wheeled_medium_offroad_rattle_ext_soundset","jsrs_tires_asphalt_slow_ext_soundset","jsrs_tires_asphalt_fast_ext_soundset","jsrs_tires_offroad_slow_ext_soundset","jsrs_tires_offroad_fast_ext_soundset","jsrs_tires_grass_ext_soundset","jsrs_tires_close_dry_soundset","jsrs_tires_close_wet_soundset","jsrs_tires_distance_soundset","jsrs_light_vehicle_water_moving_ext_soundset"]
    },
    "features": "Randomization: No						<br />Camo selections: 2 - the body, wheels and cover						<br />Script door sources: Door_LF, Door_RF, Door_LB, Door_RB						<br />Script animations: None						<br />Executed scripts: None						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: 1 to 3",
    # Class: CfgVehicles|MRAP_01_base_F|SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles|MRAP_01_base_F|SpeechVariants|Default [Indent level: 2],

        "Default": {

            "speechSingular": ["veh_vehicle_MRAP_s"],

            "speechPlural": ["veh_vehicle_MRAP_p"]
        }
    },
    "textSingular": "MRAP",
    "textPlural": "MRAPs",
    "nameSound": "veh_vehicle_MRAP_s",
    "_generalMacro": "MRAP_01_base_F",
    # Class: CfgVehicles|MRAP_01_base_F|Library [Indent level: 1],
    "Library": {
        "libTextDesc": "The Hunter is a Mine-Resistant Ambush Protected (MRAP) vehicle manufactured by US arms factories to provide troops with enhanced protection. The armored hull can withstand light weapons and protects the crew against landmines and improvised explosive devices. Even though the heavy armor and powerful engine cause increased fuel consumption, it has been favored by frontline troops over the lighter vehicles for its easy maintenance and good protection level.<br />Armed version of the sturdy Hunter MRAP vehicle is fitted with a Remotely Controlled Weapons System turret. The turret is fitted with the universal 12.7 mm heavy machinegun or the multi-role 40 mm Grenade Machine Gun. The armed Hunters are used for troop transport in combat zones, as light reconnaissance vehicles or even in fire support role in COIN operations."
    },
    "crewVulnerable": 0,
    "crewCrashProtection": 1.35,
    "enableRadio": 1,
    "enableGPS": 1,
    "armor": 200,
    "cost": 500000,
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "slingLoadCargoMemoryPoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    # Class: CfgVehicles|MRAP_01_base_F|Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles|MRAP_01_base_F|Exhausts|Exhaust1 [Indent level: 2],

        "Exhaust1": {

            "position": "exhaust_pos",

            "direction": "exhaust_dir",

            "effect": "ExhaustEffectHTruck"
        }
    },
    "wheelDamageThreshold": 0.18,
    "wheelDamageRadiusCoef": 0.75,
    "wheelDestroyRadiusCoef": 0.48,
    "cargoAction": ["passenger_MRAP_01_front","passenger_MRAP_01_back","passenger_generic01_foldhands"],
    "cargoGetInAction": ["GetInMRAP_01_cargo"],
    "cargoGetOutAction": ["GetOutMRAP_01"],
    "sensorPosition": "sensorPos",
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 1,
    "extCameraPosition": [0,2.2,-8],
    "attenuationeffecttype": "jsrs_mrap_attenuation",
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
    "secondaryExplosion": -10,
    "fuelExplosionPower": 3,
    "dammageHalf": [],
    "dammageFull": [],
    "explosionShielding": 1,
    "minTotalDamageThreshold": 0.01,
    "gunnerHasFlares": 0,
    "steerAheadSimul": 0.5,
    "steerAheadPlan": 0.35,
    "predictTurnPlan": 2,
    "predictTurnSimul": 1.5,
    "epeImpulseDamageCoef": 15,
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    # Class: CfgVehicles|Car_F|PlayerSteeringCoefficients [Indent level: 1],
    "PlayerSteeringCoefficients": {
        "turnIncreaseConst": 1,
        "turnIncreaseLinear": 1,
        "turnIncreaseTime": 0,
        "turnDecreaseConst": 5,
        "turnDecreaseLinear": 0,
        "turnDecreaseTime": 0,
        "maxTurnHundred": 1
    },
    # Class: CfgVehicles|Car_F|ViewPilot [Indent level: 1],
    "ViewPilot": {
        "initFov": 0.9,
        "minFov": 0.25,
        "maxFov": 1.25,
        "initAngleX": 0,
        "initAngleY": 0,
        "minAngleX": -65,
        "maxAngleX": 85,
        "minAngleY": -150,
        "maxAngleY": 150,
        "minMoveX": -0.2,
        "maxMoveX": 0.2,
        "minMoveY": -0.1,
        "maxMoveY": 0.1,
        "minMoveZ": -0.1,
        "maxMoveZ": 0.2,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    "headGforceLeaningFactor": [0.01,0.01,0.015],
    # Class: CfgVehicles|Car_F|NewTurret [Indent level: 1],
    "NewTurret": {
        "body": "mainTurret",
        "gun": "mainGun",
        "animationSourceBody": "mainTurret",
        "animationSourceGun": "mainGun",
        "animationSourceHatch": "hatchGunner",
        "animationSourceCamElev": "camElev",
        "proxyType": "CPGunner",
        "proxyIndex": 1,
        "gunnerName": "Gunner",
        "gunnerType": "",
        "primaryGunner": 1,
        "primaryObserver": 0,
        "weapons": [],
        "magazines": [],
        "soundServo": ["",0.00316228,1],
        "soundElevation": ["",0.00316228,1],
        "minElev": -4,
        "maxElev": 20,
        "initElev": 0,
        "minTurn": -360,
        "maxTurn": 360,
        "initTurn": 0,
        "minOutElev": -4,
        "maxOutElev": 20,
        "initOutElev": 0,
        "minOutTurn": -60,
        "maxOutTurn": 60,
        "initOutTurn": 0,
        "maxHorizontalRotSpeed": 1.2,
        "maxVerticalRotSpeed": 1.2,
        "minCamElev": -90,
        "maxCamElev": 90,
        "initCamElev": 0,
        "stabilizedInAxes": 3,
        "primary": 1,
        "hasGunner": 1,
        "commanding": 1,
        "gunnerGetInAction": "",
        "gunnerGetOutAction": "",
        "turretCanSee": 0,
        "canUseScanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewGunner [Indent level: 2],
        "ViewGunner": {
            "initAngleX": 5,
            "minAngleX": -75,
            "maxAngleX": 85,
            "initAngleY": 0,
            "minAngleY": -150,
            "maxAngleY": 150,
            "minFov": 0.25,
            "maxFov": 1.25,
            "initFov": 0.75,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "continuous": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "TurretSpec": {
            "showHeadPhones": 0
        },
        "gunnerOpticsModel": "",
        "gunnerOpticsColor": [0,0,0,1],
        "gunnerForceOptics": 1,
        "gunnerOpticsShowCursor": 0,
        "turretInfoType": "",
        "gunnerOutOpticsModel": "",
        "gunnerOutOpticsColor": [0,0,0,1],
        "gunnerOpticsEffect": [],
        "gunnerOutOpticsEffect": [],
        "memoryPointGunnerOutOptics": "",
        "gunnerOutForceOptics": 0,
        "gunnerOutOpticsShowCursor": 0,
        "gunnerFireAlsoInInternalCamera": 1,
        "gunnerOutFireAlsoInInternalCamera": 1,
        "gunnerUsesPilotView": 0,
        "castGunnerShadow": 0,
        "viewGunnerShadow": 1,
        "viewGunnerShadowDiff": 1,
        "viewGunnerShadowAmb": 1,
        "ejectDeadGunner": 0,
        "hideWeaponsGunner": 1,
        "canHideGunner": -1,
        "forceHideGunner": 0,
        "outGunnerMayFire": 0,
        "inGunnerMayFire": 1,
        "showHMD": 0,
        "viewGunnerInExternal": 0,
        "lockWhenDriverOut": 0,
        "lockWhenVehicleSpeed": -1,
        "gunnerCompartments": "Compartment1",
        "LODTurnedIn": -1,
        "LODTurnedOut": -1,
        "startEngine": 1,
        "memoryPointsGetInGunnerPrecise": "",
        "missileBeg": "spice rakety",
        "missileEnd": "konec rakety",
        "armorLights": 0.4,
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
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
            "interval": 0.01,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 4500,
            "deltaT": -3000,
            # Class: WeaponFireGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
        "GunClouds": {
            "access": 0,
            "cloudletDuration": 0.3,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 1,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 1,
            "cloudletAccY": 0.4,
            "cloudletMinYSpeed": 0.2,
            "cloudletMaxYSpeed": 0.8,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
        "MGunClouds": {
            "access": 0,
            "cloudletGrowUp": 0.05,
            "cloudletFadeIn": 0,
            "cloudletFadeOut": 0.1,
            "cloudletDuration": 0.05,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 0.3,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "timeToLive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourceSize": 0.02,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints [Indent level: 2],
        "HitPoints": {
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitTurret [Indent level: 3],

            "HitTurret": {

                "armor": 0.8,

                "material": 51,

                "name": "turret",

                "visual": "turret",

                "passThrough": 1,

                "explosionShielding": 1
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitGun [Indent level: 3],
            "HitGun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passThrough": 1,
                "explosionShielding": 1
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "Turrets": {
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
        "ViewOptics": {
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "initFov": 0.3,
            "minFov": 0.07,
            "maxFov": 0.35,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        "forceNVG": 0,
        "isCopilot": 0,
        "canEject": 1,
        "gunnerLeftHandAnimName": "",
        "gunnerRightHandAnimName": "",
        "gunnerLeftLegAnimName": "",
        "gunnerRightLegAnimName": "",
        "gunnerDoor": "",
        "preciseGetInOut": 0,
        "turretFollowFreeLook": 0,
        "allowTabLock": 1,
        "showAllTargets": 0,
        "dontCreateAI": 0,
        "disableSoundAttenuation": 0,
        "slingLoadOperator": 0,
        "playerPosition": 0,
        "allowLauncherIn": 0,
        "allowLauncherOut": 0,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
        "TurnOut": {
            "turnOffset": 0
        },
        "gunnerInAction": "ManActTestDriver",
        "gunnerAction": "ManActTestDriver",
        "gunBeg": "usti hlavne",
        "gunEnd": "konec hlavne",
        "memoryPointGunnerOptics": "gunnerview",
        "memoryPointsGetInGunner": "pos gunner",
        "memoryPointsGetInGunnerDir": "pos gunner dir",
        "memoryPointGun": "kulas",
        "selectionFireAnim": "zasleh",
        "showCrewAim": 0
    },
    "driverLeftLegAnimName": "",
    "driverRightLegAnimName": "pedal_thrust",
    "holdOffroadFormation": 1,
    # Class: CfgVehicles|Car_F|NVGMarkers [Indent level: 1],
    "NVGMarkers": {
        # Class: CfgVehicles|Car_F|NVGMarkers|NVGMarker01 [Indent level: 2],

        "NVGMarker01": {

            "name": "nvg_marker",

            "color": [0.03,0.003,0.003,1],

            "ambient": [0.003,0.0003,0.0003,1],

            "brightness": 0.001,

            "blinking": 1
        }
    },
    "viewCargoShadowDiff": 1,
    "viewCargoShadowAmb": 1,
    "audible": 5,
    "soundEnviron": ["",0.000562341,1],
    "soundCrash": ["A3|sounds_f|dummysound",1,1],
    "soundGear": ["",1e-005,1],
    "collisionEffect": "collisionEffect",
    "hideUnitInfo": 0,
    "htMin": 60,
    "htMax": 1800,
    "afMax": 100,
    "mfMax": 80,
    "mFact": 1,
    "tBody": 150,
    "transportMaxWeapons": 12,
    "transportMaxMagazines": 64,
    "maximumLoad": 2000,
    "supplyRadius": -1,
    "memoryPointSupply": "doplnovani",
    "brakeTorque": 6000,
    "longStiff": 15000,
    "latStiffX": 2000,
    "latStiffY": 18000,
    "wheelMask": "wheel_X_X",
    "numberPhysicalWheels": 4,
    "maxGForce": 3,
    # Class: CfgVehicles|Car_F|camShakeGForce [Indent level: 1],
    "camShakeGForce": {
        "power": 2,
        "frequency": 60,
        "distance": 0,
        "minSpeed": 60
    },
    # Class: CfgVehicles|Car_F|Components [Indent level: 1],
    "Components": {
        # Class: CfgVehicles|Car|Components|AICarSteeringComponent [Indent level: 2],

        "AICarSteeringComponent": {

            "steeringPIDWeights": [2.9,0.1,0.2],

            "speedPIDWeights": [0.7,0.2,0],

            "convoyPIDWeights": [1,0.01,0.01],

            "doRemapSpeed": 1,

            "remapSpeedRange": [30,70],

            "remapSpeedScalar": [1,0.35],

            "doPredictForward": 1,

            "predictForwardRange": [1,20],

            "steerAheadSaturation": [0.01,0.4],

            "speedPredictionMethod": 2,

            "wheelAngleCoef": 0.7,

            "forwardAngleCoef": 0.7,

            "steeringAngleCoef": 1,

            "differenceAngleCoef": 0.4,

            "stuckMaxTime": 3,

            "allowOvertaking": 1,

            "allowDrifting": 0,

            "allowCollisionAvoidance": 1,

            "maxWheelAngleDiff": 0.2616,

            "minSpeedToKeep": 0.1,

            "commandTurnFactor": 1
        },
        # Class: CfgVehicles|LandVehicle|Components|TransportCountermeasuresComponent [Indent level: 2],
        "TransportCountermeasuresComponent": {
        }
    },
    "unloadInCombat": 1,
    "canFloat": 0,
    "limitedSpeedCoef": 0.5,
    # Class: CfgVehicles|Car|PlateInfos [Indent level: 1],
    "PlateInfos": {
        "name": "spz",
        "color": [0,0,0,0.75]
    },
    "selectionFireAnim": "zasleh",
    "alphaTracks": 0.2,
    "memoryPointTrackFLL": "Stopa PLL",
    "memoryPointTrackFLR": "Stopa PLP",
    "memoryPointTrackBLL": "Stopa ZLL",
    "memoryPointTrackBLR": "Stopa ZLP",
    "memoryPointTrackFRL": "Stopa PPL",
    "memoryPointTrackFRR": "Stopa PPP",
    "memoryPointTrackBRL": "Stopa ZPL",
    "memoryPointTrackBRR": "Stopa ZPP",
    "memoryPointCirculumReference": "circulumReference",
    "gearBox": [-8,0,10,6.15,4.44,3.33],
    "Scudeffect": "ScudEffect",
    "preferRoads": 1,
    "formationX": 20,
    "formationZ": 20,
    "type": 0,
    "typicalCargo": ["Soldier"],
    "scudModel": "",
    "damperSize": 0.1,
    "damperForce": 1,
    "damperDamping": 1,
    "inputTurnCurve": [[0,[0,0,1,1]],[30,[0,0,0.2,0.008,0.4,0.032,0.6,0.216,0.8,0.512,1,1]]],
    "soundEngine": ["",1.77828,0.9],
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffects"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffects"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffects"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffects"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","LDustEffects"]],
    # Class: CfgVehicles|Car|DestructionEffects [Indent level: 1],
    "DestructionEffects": {
        # Class: CfgVehicles|Car|DestructionEffects|Light1 [Indent level: 2],

        "Light1": {

            "simulation": "light",

            "type": "ObjectDestructionLight",

            "position": "destructionEffect1",

            "intensity": 0.001,

            "interval": 1,

            "lifeTime": 3,

            "enabled": "distToWater"
        },
        # Class: CfgVehicles|Car|DestructionEffects|Sound [Indent level: 2],
        "Sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles|Car|DestructionEffects|Fire1 [Indent level: 2],
        "Fire1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1Small",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles|Car|DestructionEffects|Refract1 [Indent level: 2],
        "Refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefractSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles|Car|DestructionEffects|Smoke1 [Indent level: 2],
        "Smoke1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmokeSmall",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles|Car|DestructionEffects|Sparks1 [Indent level: 2],
        "Sparks1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifeTime": 0
        },
        # Class: CfgVehicles|Car|DestructionEffects|FireSparks1 [Indent level: 2],
        "FireSparks1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2.8
        },
        # Class: CfgVehicles|Car|DestructionEffects|Fire2 [Indent level: 2],
        "Fire2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles|Car|DestructionEffects|Smoke1_2 [Indent level: 2],
        "Smoke1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2Small",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles|Car|DestructionEffects|Smoke2 [Indent level: 2],
        "Smoke2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 3.2
        }
    },
    "sensitivityEar": 0.125,
    "sensitivity": 1.75,
    "memoryPointMissile": ["spice rakety","usti hlavne"],
    "memoryPointMissileDir": ["konec rakety","konec hlavne"],
    "engineStartSpeed": 1.5,
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "leftWaterEffect": "LWaterEffects",
    "rightWaterEffect": "RWaterEffects",
    "leftFastWaterEffect": "LWaterEffects",
    "rightFastWaterEffect": "RWaterEffects",
    "tracksSpeed": 0,
    "selectionLeftOffset": "PasOffsetL",
    "selectionRightOffset": "PasOffsetP",
    "explosionEffect": "FuelExplosion",
    # Class: CfgVehicles|LandVehicle|CommanderOptics [Indent level: 1],
    "CommanderOptics": {
        "proxyType": "CPCommander",
        "proxyIndex": 1,
        "gunnerName": "Commander",
        "primaryGunner": 0,
        "primaryObserver": 1,
        "stabilizedInAxes": 0,
        "body": "obsTurret",
        "gun": "obsGun",
        "animationSourceBody": "obsTurret",
        "animationSourceGun": "obsGun",
        "animationSourceHatch": "hatchCommander",
        "animationSourceCamElev": "camElev",
        "soundServo": ["A3|sounds_f|dummysound",0.01,1,10],
        "gunBeg": "",
        "gunEnd": "",
        "minElev": -4,
        "maxElev": 20,
        "initElev": 0,
        "minTurn": -360,
        "maxTurn": 360,
        "initTurn": 0,
        "commanding": 2,
        "outGunnerMayFire": 1,
        "inGunnerMayFire": 1,
        "viewGunnerInExternal": 0,
        "gunnerOpticsModel": "A3|weapons_f|reticle|Optics_Commander_02_F",
        "gunnerOutOpticsModel": "A3|weapons_f|reticle|optics_empty",
        "gunnerOutOpticsColor": [0,0,0,1],
        "gunnerOutForceOptics": 0,
        "gunnerOutOpticsShowCursor": 0,
        "gunnerOpticsEffect": [],
        "gunnerOutOpticsEffect": [],
        "memoryPointGunnerOutOptics": "commander_weapon_view",
        "memoryPointGunnerOptics": "commanderview",
        "memoryPointsGetInGunner": "pos commander",
        "memoryPointsGetInGunnerDir": "pos commander dir",
        "gunnerGetInAction": "GetInHigh",
        "gunnerGetOutAction": "GetOutHigh",
        "memoryPointGun": "gun_muzzle",
        "selectionFireAnim": "zasleh_1",
        # Class: CfgVehicles|LandVehicle|CommanderOptics|ViewOptics [Indent level: 2],
        "ViewOptics": {
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "initFov": 0.3,
            "minFov": 0.07,
            "maxFov": 0.35,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles|LandVehicle|CommanderOptics|ViewGunner [Indent level: 2],
        "ViewGunner": {
            "initAngleX": 5,
            "minAngleX": -75,
            "maxAngleX": 85,
            "initAngleY": 0,
            "minAngleY": -150,
            "maxAngleY": 150,
            "minFov": 0.25,
            "maxFov": 1.25,
            "initFov": 0.75,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        "gunnerType": "",
        "weapons": [],
        "magazines": [],
        "soundElevation": ["",0.00316228,1],
        "minOutElev": -4,
        "maxOutElev": 20,
        "initOutElev": 0,
        "minOutTurn": -60,
        "maxOutTurn": 60,
        "initOutTurn": 0,
        "maxHorizontalRotSpeed": 1.2,
        "maxVerticalRotSpeed": 1.2,
        "minCamElev": -90,
        "maxCamElev": 90,
        "initCamElev": 0,
        "primary": 1,
        "hasGunner": 1,
        "turretCanSee": 0,
        "canUseScanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "TurretSpec": {
            "showHeadPhones": 0
        },
        "gunnerOpticsColor": [0,0,0,1],
        "gunnerForceOptics": 1,
        "gunnerOpticsShowCursor": 0,
        "turretInfoType": "",
        "gunnerFireAlsoInInternalCamera": 1,
        "gunnerOutFireAlsoInInternalCamera": 1,
        "gunnerUsesPilotView": 0,
        "castGunnerShadow": 0,
        "viewGunnerShadow": 1,
        "viewGunnerShadowDiff": 1,
        "viewGunnerShadowAmb": 1,
        "ejectDeadGunner": 0,
        "hideWeaponsGunner": 1,
        "canHideGunner": -1,
        "forceHideGunner": 0,
        "showHMD": 0,
        "lockWhenDriverOut": 0,
        "lockWhenVehicleSpeed": -1,
        "gunnerCompartments": "Compartment1",
        "LODTurnedIn": -1,
        "LODTurnedOut": -1,
        "startEngine": 1,
        "memoryPointsGetInGunnerPrecise": "",
        "missileBeg": "spice rakety",
        "missileEnd": "konec rakety",
        "armorLights": 0.4,
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
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
            "interval": 0.01,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 4500,
            "deltaT": -3000,
            # Class: WeaponFireGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
        "GunClouds": {
            "access": 0,
            "cloudletDuration": 0.3,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 1,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 1,
            "cloudletAccY": 0.4,
            "cloudletMinYSpeed": 0.2,
            "cloudletMaxYSpeed": 0.8,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
        "MGunClouds": {
            "access": 0,
            "cloudletGrowUp": 0.05,
            "cloudletFadeIn": 0,
            "cloudletFadeOut": 0.1,
            "cloudletDuration": 0.05,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 0.3,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "timeToLive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourceSize": 0.02,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints [Indent level: 2],
        "HitPoints": {
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitTurret [Indent level: 3],

            "HitTurret": {

                "armor": 0.8,

                "material": 51,

                "name": "turret",

                "visual": "turret",

                "passThrough": 1,

                "explosionShielding": 1
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitGun [Indent level: 3],
            "HitGun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passThrough": 1,
                "explosionShielding": 1
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "Turrets": {
        },
        "forceNVG": 0,
        "isCopilot": 0,
        "canEject": 1,
        "gunnerLeftHandAnimName": "",
        "gunnerRightHandAnimName": "",
        "gunnerLeftLegAnimName": "",
        "gunnerRightLegAnimName": "",
        "gunnerDoor": "",
        "preciseGetInOut": 0,
        "turretFollowFreeLook": 0,
        "allowTabLock": 1,
        "showAllTargets": 0,
        "dontCreateAI": 0,
        "disableSoundAttenuation": 0,
        "slingLoadOperator": 0,
        "playerPosition": 0,
        "allowLauncherIn": 0,
        "allowLauncherOut": 0,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
        "TurnOut": {
            "turnOffset": 0
        },
        "gunnerInAction": "ManActTestDriver",
        "gunnerAction": "ManActTestDriver",
        "showCrewAim": 0
    },
    "wheelDestroyThreshold": 0.99,
    "weaponsGroup1": 1,
    "weaponsGroup2": "2 + 		4",
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "SquadTitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memoryPointDriverOptics": ["driverview","pilot"],
    "memoryPointsGetInDriver": "pos driver",
    "memoryPointsGetInDriverDir": "pos driver dir",
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInDriverPrecise": "pos driver",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
    "selectionShowDamage": "poskozeni",
    # Class: CfgVehicles|AllVehicles|ViewCargo [Indent level: 1],
    "ViewCargo": {
        "initAngleX": 5,
        "minAngleX": -75,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -150,
        "maxAngleY": 150,
        "minFov": 0.25,
        "maxFov": 1.25,
        "initFov": 0.75,
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": 0,
        "maxMoveY": 0,
        "minMoveZ": 0,
        "maxMoveZ": 0,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    # Class: CfgVehicles|AllVehicles|ViewOptics [Indent level: 1],
    "ViewOptics": {
        "initAngleX": 0,
        "minAngleX": -30,
        "maxAngleX": 30,
        "initAngleY": 0,
        "minAngleY": -100,
        "maxAngleY": 100,
        "initFov": 0.7,
        "minFov": 0.42,
        "maxFov": 0.85,
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": 0,
        "maxMoveY": 0,
        "minMoveZ": 0,
        "maxMoveZ": 0,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    # Class: CfgVehicles|AllVehicles|PilotSpec [Indent level: 1],
    "PilotSpec": {
        "showHeadPhones": 0
    },
    # Class: CfgVehicles|AllVehicles|CargoSpec [Indent level: 1],
    "CargoSpec": {
        # Class: CfgVehicles|AllVehicles|CargoSpec|Cargo1 [Indent level: 2],

        "Cargo1": {

            "showHeadPhones": 0
        }
    },
    # Class: CfgVehicles|AllVehicles|MFD [Indent level: 1],
    "MFD": {
    },
    # Class: CfgVehicles|AllVehicles|SoundEvents [Indent level: 1],
    "SoundEvents": {
    },
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "preciseGetInOut": 0,
    "cargoPreciseGetInOut": [0],
    "availableForSupportTypes": [],
    "waterPPInVehicle": 1,
    "impactEffectsSea": "ImpactEffectsSea",
    "impactEffectSpeedLimit": 8,
    "showCrewAim": 0,
    # Class: CfgVehicles|AllVehicles|CargoTurret [Indent level: 1],
    "CargoTurret": {
        # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2],

        "ViewGunner": {

            "initAngleX": 5,

            "minAngleX": -75,

            "maxAngleX": 85,

            "initAngleY": 0,

            "minAngleY": -150,

            "maxAngleY": 150,

            "minFov": 0.25,

            "maxFov": 1.25,

            "initFov": 0.75,

            "minMoveX": 0,

            "maxMoveX": 0,

            "minMoveY": 0,

            "maxMoveY": 0,

            "minMoveZ": 0,

            "maxMoveZ": 0,

            "speedZoomMaxSpeed": 1e+010,

            "speedZoomMaxFOV": 0
        },
        # Class: CfgVehicles|AllVehicles|CargoTurret|Hitpoints [Indent level: 2],
        "Hitpoints": {
        },
        "animationSourceBody": "",
        "animationSourceGun": "",
        "body": "",
        "canEject": 1,
        "commanding": 0,
        "dontCreateAI": 1,
        "gun": "",
        "gunnerGetInAction": "GetInLow",
        "gunnerGetOutAction": "GetOutLow",
        "gunnerName": "cargo",
        "hideWeaponsGunner": 0,
        "isCopilot": 0,
        "memoryPointsGetInGunner": "pos cargo",
        "memoryPointsGetInGunnerDir": "pos cargo dir",
        "primaryGunner": 0,
        "proxyType": "CPCargo",
        "startEngine": 0,
        "turretFollowFreeLook": 0,
        "viewGunnerInExternal": 1,
        "disableSoundAttenuation": 1,
        "outGunnerMayFire": 1,
        "isPersonTurret": 1,
        "showAsCargo": 1,
        "maxElev": 45,
        "minElev": -45,
        "maxTurn": 95,
        "minTurn": -95,
        "animationSourceHatch": "hatchGunner",
        "animationSourceCamElev": "camElev",
        "proxyIndex": 1,
        "gunnerType": "",
        "primaryObserver": 0,
        "weapons": [],
        "magazines": [],
        "soundServo": ["",0.00316228,1],
        "soundElevation": ["",0.00316228,1],
        "initElev": 0,
        "initTurn": 0,
        "minOutElev": -4,
        "maxOutElev": 20,
        "initOutElev": 0,
        "minOutTurn": -60,
        "maxOutTurn": 60,
        "initOutTurn": 0,
        "maxHorizontalRotSpeed": 1.2,
        "maxVerticalRotSpeed": 1.2,
        "minCamElev": -90,
        "maxCamElev": 90,
        "initCamElev": 0,
        "stabilizedInAxes": 3,
        "primary": 1,
        "hasGunner": 1,
        "turretCanSee": 0,
        "canUseScanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "TurretSpec": {
            "showHeadPhones": 0
        },
        "gunnerOpticsModel": "",
        "gunnerOpticsColor": [0,0,0,1],
        "gunnerForceOptics": 1,
        "gunnerOpticsShowCursor": 0,
        "turretInfoType": "",
        "gunnerOutOpticsModel": "",
        "gunnerOutOpticsColor": [0,0,0,1],
        "gunnerOpticsEffect": [],
        "gunnerOutOpticsEffect": [],
        "memoryPointGunnerOutOptics": "",
        "gunnerOutForceOptics": 0,
        "gunnerOutOpticsShowCursor": 0,
        "gunnerFireAlsoInInternalCamera": 1,
        "gunnerOutFireAlsoInInternalCamera": 1,
        "gunnerUsesPilotView": 0,
        "castGunnerShadow": 0,
        "viewGunnerShadow": 1,
        "viewGunnerShadowDiff": 1,
        "viewGunnerShadowAmb": 1,
        "ejectDeadGunner": 0,
        "canHideGunner": -1,
        "forceHideGunner": 0,
        "inGunnerMayFire": 1,
        "showHMD": 0,
        "lockWhenDriverOut": 0,
        "lockWhenVehicleSpeed": -1,
        "gunnerCompartments": "Compartment1",
        "LODTurnedIn": -1,
        "LODTurnedOut": -1,
        "memoryPointsGetInGunnerPrecise": "",
        "missileBeg": "spice rakety",
        "missileEnd": "konec rakety",
        "armorLights": 0.4,
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
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
            "interval": 0.01,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 4500,
            "deltaT": -3000,
            # Class: WeaponFireGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
        "GunClouds": {
            "access": 0,
            "cloudletDuration": 0.3,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 1,
            "cloudletGrowUp": 1,
            "cloudletFadeIn": 0.01,
            "cloudletFadeOut": 1,
            "cloudletAccY": 0.4,
            "cloudletMinYSpeed": 0.2,
            "cloudletMaxYSpeed": 0.8,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourceSize": 0.5,
            "timeToLive": 0,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
        "MGunClouds": {
            "access": 0,
            "cloudletGrowUp": 0.05,
            "cloudletFadeIn": 0,
            "cloudletFadeOut": 0.1,
            "cloudletDuration": 0.05,
            "cloudletAnimPeriod": 1,
            "cloudletSize": 1,
            "cloudletAlpha": 0.3,
            "cloudletAccY": 0,
            "cloudletMinYSpeed": -100,
            "cloudletMaxYSpeed": 100,
            "cloudletShape": "cloudletClouds",
            "cloudletColor": [1,1,1,0],
            "timeToLive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourceSize": 0.02,
            "initT": 0,
            "deltaT": 0,
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

                "T0": {

                    "maxT": 0,

                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "Turrets": {
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
        "ViewOptics": {
            "initAngleX": 0,
            "minAngleX": -30,
            "maxAngleX": 30,
            "initAngleY": 0,
            "minAngleY": -100,
            "maxAngleY": 100,
            "initFov": 0.3,
            "minFov": 0.07,
            "maxFov": 0.35,
            "minMoveX": 0,
            "maxMoveX": 0,
            "minMoveY": 0,
            "maxMoveY": 0,
            "minMoveZ": 0,
            "maxMoveZ": 0,
            "speedZoomMaxSpeed": 1e+010,
            "speedZoomMaxFOV": 0
        },
        "forceNVG": 0,
        "gunnerLeftHandAnimName": "",
        "gunnerRightHandAnimName": "",
        "gunnerLeftLegAnimName": "",
        "gunnerRightLegAnimName": "",
        "gunnerDoor": "",
        "preciseGetInOut": 0,
        "allowTabLock": 1,
        "showAllTargets": 0,
        "slingLoadOperator": 0,
        "playerPosition": 0,
        "allowLauncherIn": 0,
        "allowLauncherOut": 0,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
        "TurnOut": {
            "turnOffset": 0
        },
        "gunnerInAction": "ManActTestDriver",
        "gunnerAction": "ManActTestDriver",
        "gunBeg": "usti hlavne",
        "gunEnd": "konec hlavne",
        "memoryPointGunnerOptics": "gunnerview",
        "memoryPointGun": "kulas",
        "selectionFireAnim": "zasleh",
        "showCrewAim": 0
    },
    "curatorInfoType": "RscDisplayAttributesVehicle",
    "curatorInfoTypeEmpty": "RscDisplayAttributesVehicleEmpty",
    "access": 0,
    "reversed": 1,
    "autocenter": 1,
    "animated": 1,
    "shadow": 1,
    "featureType": 0,
    "speechSingular": [],
    "speechPlural": [],
    "maxDetectRange": 20,
    "detectSkill": 20,
    "mineAlertIconRange": 200,
    "killFriendlyExpCoef": 1,
    "weaponSlots": 0,
    "camouflage": 2,
    "spotableDarkNightLightsOff": 0.001,
    "spotableNightLightsOff": 0.02,
    "spotableNightLightsOn": 4,
    "accuracyDarkNightLightsOff": 0.001,
    "accuracyNightLightsOff": 0.006,
    "accuracyNightLightsOn": 0.1,
    "outsideSoundFilter": 0,
    "obstructSoundLFRatio": 0,
    "occludeSoundLFRatio": 0.25,
    "slowSpeedForwardCoef": 0.3,
    "enableManualFire": 1,
    "portrait": "",
    "ghostPreview": "",
    "damageResistance": 0.004,
    "replaceDamaged": "",
    "replaceDamagedLimit": 0.9,
    "replaceDamagedHitpoints": [],
    "keepInEPESceneAfterDeath": 0,
    "fuelConsumptionRate": 0.01,
    "groupCameraPosition": [0,5,-30],
    "extCameraParams": [1],
    "cameraSmoothSpeed": 5,
    "minFireTime": 20,
    "indirectHitEnemyCoefAI": 10,
    "indirectHitFriendlyCoefAI": -20,
    "indirectHitCivilianCoefAI": -20,
    "indirectHitUnknownCoefAI": -0.5,
    "formationTime": 5,
    "alwaysTarget": 0,
    "irTarget": 1,
    "irScanRangeMin": 0,
    "irScanRangeMax": 0,
    "irScanToEyeFactor": 1,
    "irScanGround": 1,
    "laserTarget": 0,
    "laserScanner": 0,
    "nvTarget": 0,
    "nvScanner": 0,
    "artilleryTarget": 0,
    "artilleryScanner": 0,
    "canUseScanners": 1,
    "unitInfoTypeLite": 0,
    "nightVision": 0,
    "radarType": 0,
    "hasDriver": 1,
    "driverForceOptics": 0,
    "getInRadius": 2.5,
    "enableWatch": 0,
    "lockDetectionSystem": 0,
    "incomingMissileDetectionSystem": 0,
    "usePreciseGetInAction": 0,
    "allowTabLock": 1,
    "showAllTargets": 0,
    "waterLinearDampingCoefX": 0,
    "waterLinearDampingCoefY": 0,
    "waterAngularDampingCoef": 0,
    "showNVGDriver": 0,
    "showNVGCommander": 0,
    "showNVGCargo": [0],
    "soundAttenuationCargo": [1],
    "countsForScoreboard": 1,
    # Class: CfgVehicles|All|MarkerLights [Indent level: 1],
    "MarkerLights": {
    },
    # Class: CfgVehicles|All|NVGMarker [Indent level: 1],
    "NVGMarker": {
        "diffuse": [1,1,1,1],
        "ambient": [1,1,1,1],
        "brightness": 1,
        "blinking": 0,
        "onlyInNvg": 0
    },
    # Class: CfgVehicles|All|HeadLimits [Indent level: 1],
    "HeadLimits": {
        "initAngleX": 5,
        "minAngleX": -30,
        "maxAngleX": 40,
        "initAngleY": 0,
        "minAngleY": -90,
        "maxAngleY": 90,
        "minAngleZ": -45,
        "maxAngleZ": 45,
        "rotZRadius": 0.2
    },
    "transportAmmo": 0,
    "isbackpack": 0,
    "transportFuel": 0,
    "transportRepair": 0,
    "transportVehiclesCount": 0,
    "transportVehiclesMass": 0,
    "attendant": 0,
    "engineer": 0,
    "uavHacker": 0,
    # Class: CfgVehicles|All|SoundEnvironExt [Indent level: 1],
    "SoundEnvironExt": {
    },
    # Class: CfgVehicles|All|SoundEquipment [Indent level: 1],
    "SoundEquipment": {
    },
    # Class: CfgVehicles|All|SoundBreath [Indent level: 1],
    "SoundBreath": {
    },
    # Class: CfgVehicles|All|SoundBreathSwimming [Indent level: 1],
    "SoundBreathSwimming": {
    },
    # Class: CfgVehicles|All|SoundBreathInjured [Indent level: 1],
    "SoundBreathInjured": {
    },
    # Class: CfgVehicles|All|SoundHitScream [Indent level: 1],
    "SoundHitScream": {
    },
    # Class: CfgVehicles|All|SoundInjured [Indent level: 1],
    "SoundInjured": {
    },
    # Class: CfgVehicles|All|SoundBreathAutomatic [Indent level: 1],
    "SoundBreathAutomatic": {
    },
    # Class: CfgVehicles|All|SoundDrown [Indent level: 1],
    "SoundDrown": {
    },
    # Class: CfgVehicles|All|SoundChoke [Indent level: 1],
    "SoundChoke": {
    },
    # Class: CfgVehicles|All|SoundRecovered [Indent level: 1],
    "SoundRecovered": {
    },
    # Class: CfgVehicles|All|SoundBurning [Indent level: 1],
    "SoundBurning": {
    },
    # Class: CfgVehicles|All|PulsationSound [Indent level: 1],
    "PulsationSound": {
    },
    # Class: CfgVehicles|All|SoundDrowning [Indent level: 1],
    "SoundDrowning": {
    },
    "soundLandCrash": ["",1,1],
    "soundWaterCrash": ["",0.177828,1],
    "soundServo": ["",0.00316228,0.5],
    "soundElevation": ["",0.00316228,0.5],
    "sounddamage": ["",1,1],
    "soundGearUp": ["",1,1],
    "soundGearDown": ["",1,1],
    "soundFlapsUp": ["",1,1],
    "soundFlapsDown": ["",1,1],
    "cabinOpenSound": ["",1,1],
    "cabinCloseSound": ["",1,1],
    "cabinOpenSoundInternal": ["",1,1],
    "cabinCloseSoundInternal": ["",1,1],
    "soundLandCrashes": ["soundLandCrash",1],
    "soundWaterCrashes": ["soundWaterCrash",1],
    "emptySound": ["",0,1],
    "soundLocked": ["",1,1],
    "soundIncommingMissile": ["",1,1],
    "cargoIsCoDriver": [0],
    "driverCompartments": "Compartment1",
    "driverOpticsModel": "",
    "driverOpticsEffect": [],
    "driverOpticsColor": [1,1,1,1],
    "hideProxyInCombat": 0,
    "canHideDriver": -1,
    "castDriverShadow": 0,
    "castCargoShadow": 0,
    "viewDriverShadow": 1,
    "viewDriverShadowDiff": 1,
    "viewDriverShadowAmb": 1,
    "viewCargoShadow": 1,
    "ejectDeadDriver": 0,
    "ejectDeadCargo": 0,
    "hiddenSelectionsMaterials": [],
    "hiddenUnderwaterSelections": [],
    "shownUnderWaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    # Class: CfgVehicles|All|FxExplo [Indent level: 1],
    "FxExplo": {
        "access": 1
    },
    # Class: CfgVehicles|All|GunFire [Indent level: 1],
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
        "interval": 0.01,
        "size": 3,
        "sourceSize": 0.5,
        "timeToLive": 0,
        "initT": 4500,
        "deltaT": -3000,
        # Class: WeaponFireGun|Table [Indent level: 0],
        "Table": {
            # Class: WeaponFireGun|Table|T0 [Indent level: 1],

            "T0": {

                "maxT": 0,

                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun|Table|T1 [Indent level: 1],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun|Table|T2 [Indent level: 1],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun|Table|T3 [Indent level: 1],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun|Table|T4 [Indent level: 1],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun|Table|T5 [Indent level: 1],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun|Table|T6 [Indent level: 1],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun|Table|T7 [Indent level: 1],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun|Table|T8 [Indent level: 1],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun|Table|T9 [Indent level: 1],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun|Table|T10 [Indent level: 1],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun|Table|T11 [Indent level: 1],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun|Table|T12 [Indent level: 1],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun|Table|T13 [Indent level: 1],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun|Table|T14 [Indent level: 1],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun|Table|T15 [Indent level: 1],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun|Table|T16 [Indent level: 1],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun|Table|T17 [Indent level: 1],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun|Table|T18 [Indent level: 1],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun|Table|T19 [Indent level: 1],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun|Table|T20 [Indent level: 1],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun|Table|T21 [Indent level: 1],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun|Table|T22 [Indent level: 1],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|All|GunClouds [Indent level: 1],
    "GunClouds": {
        "access": 0,
        "cloudletDuration": 0.3,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 1,
        "cloudletGrowUp": 1,
        "cloudletFadeIn": 0.01,
        "cloudletFadeOut": 1,
        "cloudletAccY": 0.4,
        "cloudletMinYSpeed": 0.2,
        "cloudletMaxYSpeed": 0.8,
        "cloudletShape": "cloudletClouds",
        "cloudletColor": [1,1,1,0],
        "interval": 0.05,
        "size": 3,
        "sourceSize": 0.5,
        "timeToLive": 0,
        "initT": 0,
        "deltaT": 0,
        # Class: WeaponCloudsGun|Table [Indent level: 0],
        "Table": {
            # Class: WeaponCloudsGun|Table|T0 [Indent level: 1],

            "T0": {

                "maxT": 0,

                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|All|MGunClouds [Indent level: 1],
    "MGunClouds": {
        "access": 0,
        "cloudletGrowUp": 0.05,
        "cloudletFadeIn": 0,
        "cloudletFadeOut": 0.1,
        "cloudletDuration": 0.05,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 0.3,
        "cloudletAccY": 0,
        "cloudletMinYSpeed": -100,
        "cloudletMaxYSpeed": 100,
        "cloudletShape": "cloudletClouds",
        "cloudletColor": [1,1,1,0],
        "timeToLive": 0,
        "interval": 0.02,
        "size": 0.3,
        "sourceSize": 0.02,
        "initT": 0,
        "deltaT": 0,
        # Class: WeaponCloudsMGun|Table [Indent level: 0],
        "Table": {
            # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1],

            "T0": {

                "maxT": 0,

                "color": [1,1,1,0]
            }
        }
    },
    "selectionDamage": "zbytek",
    "HeadAimDown": 0,
    "cargoCanEject": 1,
    "driverCanEject": 1,
    "airCapacity": 10,
    "waterDamageEngine": 0.2,
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "coefSpeedInside": 2,
    "windSockExist": 0,
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    "minGForce": 0.2,
    "gForceShakeAttenuation": 0.5,
    # Class: CfgVehicles|All|camShakeDamage [Indent level: 1],
    "camShakeDamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minSpeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "soundTurnIn": ["",0.000316228,1],
    "soundTurnOut": ["",0.000316228,1],
    "soundTurnInInternal": ["",0.000316228,1],
    "soundTurnOutInternal": ["",0.000316228,1],
    "insideDetectCoef": 0.05,
}