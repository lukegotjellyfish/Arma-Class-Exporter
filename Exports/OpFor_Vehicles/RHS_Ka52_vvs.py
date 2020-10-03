RHS_Ka52_vvs = {
    "editorPreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_Ka52_vvs.paa",
    "scope": 2,
    "faction": "rhs_faction_vvs",
    "author": "Red Hammer Studios",
    "availableForSupportTypes": ["CAS_Heli"],
    "accuracy": 0.5,
    "hiddenSelectionsTextures": ["|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01_co.paa","|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02_co.paa","a3|data_f|clear_empty.paa","a3|data_f|clear_empty.paa","rhsafrf|addons|rhs_decals|data|labels|aviation|vvs_ca.paa","|rhsafrf|addons|rhs_a2port_air|Ka52|Data|rhs_ka52_samshin_wfov.paa"],
    "dlc": "RHS_AFRF",
    "rhs_decalParameters": ["['Number',cRHSAIRKA52NumberPlaces,'AviaYellow']"],
    "category": "Air",
    # Class: CfgVehicles\RHS_Ka52_base\RotorLibHelicopterProperties,
    "RotorLibHelicopterProperties": {
        "RTDconfig": "rhsafrf|addons|rhs_c_a2port_air|ka52|RTD_Heli_Attack_02.xml",
        "autoHoverCorrection": [3.2,0,0],
        "defaultCollective": 0.805,
        "retreatBladeStallWarningSpeed": 83,
        "maxTorque": 3300,
        "stressDamagePerSec": 0.01,
        "maxHorizontalStabilizerLeftStress": 8000,
        "maxHorizontalStabilizerRightStress": 8000,
        "maxVerticalStabilizerStress": 4000,
        "horizontalWingsAngleCollMin": 0,
        "horizontalWingsAngleCollMax": 0,
        "maxMainRotorStress": 225000,
        "maxTailRotorStress": 225000
    },
    "numberPhysicalWheels": 3,
    "maxSpeed": 395,
    "bodyFrictionCoef": 0.426,
    "liftForceCoef": 6,
    "cyclicForwardForceCoef": 1,
    "backRotorForceCoef": 1.35,
    "maxMainRotorDive": 7,
    "minMainRotorDive": -7,
    "neutralMainRotorDive": 0,
    "gearRetracting": 1,
    "mainRotorSpeed": -1,
    "backRotorSpeed": -1,
    "mainBladeRadius": 6.9,
    "tailBladeRadius": 6.9,
    "tailBladeCenter": "tail_blade_center",
    "mainBladeCenter": "main_blade_center",
    "LESH_canBeTowed": 1,
    "LESH_towFromFront": 1,
    "LESH_AxisOffsetTarget": [0,6.5,-1.05],
    "LESH_WheelOffset": [0,-1],
    "side": 0,
    "crew": "rhs_pilot_combat_heli",
    "typicalCargo": ["rhs_pilot_combat_heli"],
    "fuelCapacity": 1870,
    "RHS_fuelCapacity": 1870,
    "driverCanEject": 1,
    "driverCompartments": 1,
    "ejectSpeed": [1,0,11],
    "destrType": "DestructWreck",
    "armor": 55,
    "displayName": "Ka-52",
    "vehicleClass": "rhs_vehclass_helicopter",
    "editorSubcategory": "rhs_EdSubcat_helicopter",
    "model": "rhsafrf|addons|rhs_a2port_air|ka52|KA52.p3d",
    "icon": "rhsafrf|addons|rhs_a2port_air|data|map_ico|Icon_ka52_CA.paa",
    "picture": "rhsafrf|addons|rhs_a2port_air|data|ico|rhs_ka52_pic_ca.paa",
    "mapSize": 15,
    "castDriverShadow": 1,
    "viewCargoShadow": 1,
    "camShakeCoef": 0.8,
    "transportsoldier": 0,
    "driverDoor": "DoorL",
    "driverLeftHandAnimName": "lever_pilot",
    "driverRightHandAnimName": "stick_pilot",
    "driveOnComponent": ["F_gear_d3","L_gear_d3","R_gear_d3"],
    "getInRadius": 1.5,
    "precisegetinout": 1,
    "memoryPointsGetInDriverPrecise": "pos driver",
    "getInAction": "Heli_Attack_01_Pilot_Enter",
    "getOutAction": "Heli_Attack_01_Pilot_Exit",
    "selectionHRotorStill": "velka vrtule staticka",
    "selectionHRotorMove": "velka vrtule blur",
    "selectionVRotorStill": "mala vrtule staticka",
    "selectionVRotorMove": "mala vrtule blur",
    "memoryPointLRocket": "l raketa",
    "memoryPointRRocket": "p raketa",
    "memoryPointLMissile": "l strela",
    "memoryPointRMissile": "p strela",
    "memoryPointGun": ["chase01","chase02","chase03","chase04"],
    "gunBeg": ["chase01dir","chase02dir","chase03dir","chase04dir"],
    "gunEnd": ["chase01","chase02","chase03","chase04"],
    # Class: CfgVehicles\RHS_Ka52_base\PilotCamera,
    "PilotCamera": {
    },
    "unitInfoType": "RHS_RscUnitInfoAir_Ka52",
    "receiveRemoteTargets": 1,
    "reportRemoteTargets": 1,
    "reportOwnPosition": 1,
    "irTarget": 1,
    "irTargetSize": 0.9,
    "visualTarget": 1,
    "visualTargetSize": 0.9,
    "radarTarget": 1,
    "radarTargetSize": 1,
    "threat": [0.6,1,0.8],
    "weapons": ["rhs_weap_MASTERSAFE","rhs_weap_DIRCM_Vitebsk"],
    "magazines": ["rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk","rhs_mag_DIRCM_Vitebsk"],
    "weaponsGroup1": 128,
    "weaponsGroup4": 64,
    "driverAction": "RHS_KA52_Pilot",
    "driverInAction": "RHS_KA52_Pilot",
    # Class: CfgVehicles\RHS_Ka52_base\HitPoints,
    "HitPoints": {
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitHRotor
        "HitHRotor": {
            "armor": 0.3,
            "radius": 0.4,
            "minimalHit": 0.1,
            "explosionShielding": 2,
            "name": "main_rotor_hit",
            "convexComponent": "main_rotor_hit",
            "visual": "main rotor static",
            "material": 51,
            "passThrough": 0.1
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass1,
        "HitGlass1": {
            "armor": 3,
            "name": "glass1",
            "visual": "glass1",
            "radius": 0.2,
            "explosionShielding": 2,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass2,
        "HitGlass2": {
            "armor": 3,
            "name": "glass2",
            "visual": "glass2",
            "radius": 0.35,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3,
        "HitGlass3": {
            "armor": 1,
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass6,
                "BrokenGlass6": {
                    "simulation": "particles",
                    "type": "BrokenGlass6N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass7,
                "BrokenGlass7": {
                    "simulation": "particles",
                    "type": "BrokenGlass7N_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass5S,
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass6S,
                "BrokenGlass6S": {
                    "simulation": "particles",
                    "type": "BrokenGlass6S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\BrokenGlass7S,
                "BrokenGlass7S": {
                    "simulation": "particles",
                    "type": "BrokenGlass7S_0850_2250",
                    "position": "glass3_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\RHS_ERA_Flash,
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "glass3_effect",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\RHS_ERA_Sound,
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "glass3_effect",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass3\DestructionEffects\RHS_ERA_Smoke,
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "glass3_effect",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                }
            },
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4,
        "HitGlass4": {
            "armor": 1,
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass6,
                "BrokenGlass6": {
                    "simulation": "particles",
                    "type": "BrokenGlass6N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass7,
                "BrokenGlass7": {
                    "simulation": "particles",
                    "type": "BrokenGlass7N_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass5S,
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass6S,
                "BrokenGlass6S": {
                    "simulation": "particles",
                    "type": "BrokenGlass6S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\BrokenGlass7S,
                "BrokenGlass7S": {
                    "simulation": "particles",
                    "type": "BrokenGlass7S_0850_2250",
                    "position": "glass4_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\RHS_ERA_Flash,
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "glass4_effect",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\RHS_ERA_Sound,
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "glass4_effect",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitGlass4\DestructionEffects\RHS_ERA_Smoke,
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "glass4_effect",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                }
            },
            "name": "glass4",
            "visual": "glass4",
            "radius": 0.22,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor1,
        "HitRotor1": {
            "armor": 1,
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor1\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor1\DestructionEffects\RHS_ERA_Flash,
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "rotor1_pos",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor1\DestructionEffects\RHS_ERA_Sound,
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "rotor1_pos",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor1\DestructionEffects\RHS_ERA_Smoke,
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "rotor1_pos",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                }
            },
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor2,
        "HitRotor2": {
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor2\DestructionEffects
            "DestructionEffects": {
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor2\DestructionEffects\RHS_ERA_Flash
                "RHS_ERA_Flash": {
                    "position": "rotor2_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor2\DestructionEffects\RHS_ERA_Sound,
                "RHS_ERA_Sound": {
                    "position": "rotor2_pos",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor2\DestructionEffects\RHS_ERA_Smoke,
                "RHS_ERA_Smoke": {
                    "position": "rotor2_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                "ammoExplosionEffect": ""
            },
            "armor": 1,
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor3,
        "HitRotor3": {
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor3\DestructionEffects
            "DestructionEffects": {
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor3\DestructionEffects\RHS_ERA_Flash
                "RHS_ERA_Flash": {
                    "position": "rotor3_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor3\DestructionEffects\RHS_ERA_Sound,
                "RHS_ERA_Sound": {
                    "position": "rotor3_pos",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor3\DestructionEffects\RHS_ERA_Smoke,
                "RHS_ERA_Smoke": {
                    "position": "rotor3_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                "ammoExplosionEffect": ""
            },
            "armor": 1,
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor4,
        "HitRotor4": {
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor4\DestructionEffects
            "DestructionEffects": {
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor4\DestructionEffects\RHS_ERA_Flash
                "RHS_ERA_Flash": {
                    "position": "rotor4_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor4\DestructionEffects\RHS_ERA_Sound,
                "RHS_ERA_Sound": {
                    "position": "rotor4_pos",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor4\DestructionEffects\RHS_ERA_Smoke,
                "RHS_ERA_Smoke": {
                    "position": "rotor4_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                "ammoExplosionEffect": ""
            },
            "armor": 1,
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor5,
        "HitRotor5": {
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor5\DestructionEffects
            "DestructionEffects": {
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor5\DestructionEffects\RHS_ERA_Flash
                "RHS_ERA_Flash": {
                    "position": "rotor5_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor5\DestructionEffects\RHS_ERA_Sound,
                "RHS_ERA_Sound": {
                    "position": "rotor5_pos",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor5\DestructionEffects\RHS_ERA_Smoke,
                "RHS_ERA_Smoke": {
                    "position": "rotor5_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                "ammoExplosionEffect": ""
            },
            "armor": 1,
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor6,
        "HitRotor6": {
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor6\DestructionEffects
            "DestructionEffects": {
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor6\DestructionEffects\RHS_ERA_Flash
                "RHS_ERA_Flash": {
                    "position": "rotor6_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor6\DestructionEffects\RHS_ERA_Sound,
                "RHS_ERA_Sound": {
                    "position": "rotor6_pos",
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitRotor6\DestructionEffects\RHS_ERA_Smoke,
                "RHS_ERA_Smoke": {
                    "position": "rotor6_pos",
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                "ammoExplosionEffect": ""
            },
            "armor": 1,
            "name": "glass3",
            "visual": "glass3",
            "radius": 0.34,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon1,
        "HitPylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon1\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Shard,
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon2,
        "HitPylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon2\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Shard,
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon3,
        "HitPylon3": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_3",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon3\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Shard,
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon4,
        "HitPylon4": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_4",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon4\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_Ka52_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Shard,
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitHull,
        "HitHull": {
            "armor": 999,
            "visual": "camo1",
            "minimalHit": 0.05,
            "depends": "Total",
            "radius": 0.01,
            "name": "hull_hit",
            "convexComponent": "hull_hit",
            "explosionShielding": 1,
            "material": 51,
            "passThrough": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitFuel,
        "HitFuel": {
            "armor": 2,
            "radius": 0.125,
            "minimalHit": 0.05,
            "explosionShielding": 2,
            "name": "fuel_hit",
            "convexComponent": "fuel_hit",
            "visual": "zbytek",
            "material": 51,
            "passThrough": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitAvionics,
        "HitAvionics": {
            "armor": 1.5,
            "radius": 0.4,
            "minimalHit": 0.15,
            "explosionShielding": 1.5,
            "visual": "podsvit pristroju",
            "name": "avionics_hit",
            "convexComponent": "avionics_hit",
            "material": 51,
            "passThrough": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitEngine1,
        "HitEngine1": {
            "armor": 3,
            "radius": 0.35,
            "name": "engine_1_hit",
            "explosionShielding": 3,
            "minimalHit": 0.1,
            "visual": "motor",
            "passThrough": 1,
            "convexComponent": "engine_1_hit",
            "material": 51
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitEngine2,
        "HitEngine2": {
            "name": "engine_2_hit",
            "convexComponent": "engine_2_hit",
            "armor": 3,
            "radius": 0.35,
            "explosionShielding": 3,
            "minimalHit": 0.1,
            "visual": "motor",
            "passThrough": 1,
            "material": 51
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitEngine,
        "HitEngine": {
            "armor": 999,
            "radius": 0.05,
            "minimalHit": 1,
            "visual": "camo2",
            "depends": "0.5 * (HitEngine1 + HitEngine2)",
            "name": "engine_hit",
            "convexComponent": "engine_hit",
            "explosionShielding": 1,
            "material": 51,
            "passThrough": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitVRotor,
        "HitVRotor": {
            "armor": 2.6,
            "radius": 0.4,
            "minimalHit": 0.1,
            "explosionShielding": 2,
            "name": "tail_rotor_hit",
            "convexComponent": "tail_rotor_hit",
            "visual": "tail rotor static",
            "material": 51,
            "passThrough": 0.3
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass7,
        "HitGlass7": {
            "name": "glass7",
            "visual": "glass7",
            "radius": 0.35,
            "armor": 3,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass5,
        "HitGlass5": {
            "name": "glass5",
            "visual": "glass5",
            "radius": 0.25,
            "armor": 4.5,
            "explosionShielding": 2,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass6,
        "HitGlass6": {
            "name": "glass6",
            "visual": "glass6",
            "radius": 0.18,
            "armor": 3,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass8,
        "HitGlass8": {
            "name": "glass8",
            "visual": "glass8",
            "radius": 0.34,
            "armor": 3,
            "explosionShielding": 1.5,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass9,
        "HitGlass9": {
            "name": "glass9",
            "visual": "glass9",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass10,
        "HitGlass10": {
            "name": "glass10",
            "visual": "glass10",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass11,
        "HitGlass11": {
            "name": "glass11",
            "visual": "glass11",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass12,
        "HitGlass12": {
            "name": "glass12",
            "visual": "glass12",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass13,
        "HitGlass13": {
            "name": "glass13",
            "visual": "glass13",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass14,
        "HitGlass14": {
            "name": "glass14",
            "visual": "glass14",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitGlass15,
        "HitGlass15": {
            "name": "glass15",
            "visual": "glass15",
            "radius": 0.24,
            "armor": 0.8,
            "explosionShielding": 1,
            "minimalHit": 0.05,
            "material": -1,
            "convexComponent": "glass1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitWinch,
        "HitWinch": {
            # Class: CfgVehicles\Heli_Attack_02_base_F\HitPoints\HitWinch\DestructionEffects
            "DestructionEffects": {
            },
            "armor": -40,
            "material": 51,
            "name": "slingLoad0",
            "visual": "",
            "passThrough": 0,
            "radius": 0.1
        },
        # Class: CfgVehicles\Helicopter_Base_F\HitPoints\HitMissiles,
        "HitMissiles": {
            "name": "ammo_hit",
            "convexComponent": "ammo_hit",
            "explosionShielding": 1,
            "armor": 0.1,
            "material": 51,
            "visual": "munice",
            "passThrough": 0.5
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitRGlass,
        "HitRGlass": {
            "convexComponent": "sklo predni P",
            "explosionShielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni P",
            "visual": "sklo predni P",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitLGlass,
        "HitLGlass": {
            "convexComponent": "sklo predni L",
            "explosionShielding": 1,
            "armor": 0.1,
            "material": 51,
            "name": "sklo predni L",
            "visual": "sklo predni L",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitEngine3,
        "HitEngine3": {
            "name": "engine_3_hit",
            "convexComponent": "engine_3_hit",
            "explosionShielding": 1,
            "armor": 0.25,
            "material": 51,
            "visual": "motor",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitTransmission,
        "HitTransmission": {
            "armor": 0.8,
            "material": -1,
            "name": "transmission",
            "passThrough": 0.8
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitLight,
        "HitLight": {
            "armor": 0.1,
            "material": -1,
            "name": "light",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitHydraulics,
        "HitHydraulics": {
            "armor": 0.8,
            "material": -1,
            "name": "hydraulics",
            "passThrough": 0.8
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitGear,
        "HitGear": {
            "armor": 0.9,
            "material": -1,
            "name": "gear",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitHStabilizerL1,
        "HitHStabilizerL1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerL1",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitHStabilizerR1,
        "HitHStabilizerR1": {
            "armor": 0.8,
            "material": -1,
            "name": "HStabilizerR1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitVStabilizer1,
        "HitVStabilizer1": {
            "armor": 0.8,
            "material": -1,
            "name": "VStabilizer1",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitTail,
        "HitTail": {
            "armor": 0.8,
            "material": -1,
            "name": "tail boom",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitPitotTube,
        "HitPitotTube": {
            "armor": 0.5,
            "material": -1,
            "name": "pitot tube",
            "passThrough": 0.2
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStaticPort,
        "HitStaticPort": {
            "armor": 0.1,
            "material": -1,
            "name": "static port",
            "passThrough": 1
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStarter1,
        "HitStarter1": {
            "armor": 0.1,
            "material": -1,
            "name": "starter1",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStarter2,
        "HitStarter2": {
            "armor": 0.1,
            "material": -1,
            "name": "starter2",
            "passThrough": 0
        },
        # Class: CfgVehicles\Helicopter\HitPoints\HitStarter3,
        "HitStarter3": {
            "armor": 0.1,
            "material": -1,
            "name": "starter3",
            "passThrough": 0
        }
    },
    # Class: CfgVehicles\RHS_Ka52_base\TransportMagazines,
    "TransportMagazines": {
        # Class: CfgVehicles\RHS_Ka52_base\TransportMagazines\_xx_rhs_30Rnd_545x39_7N10_AK
        "_xx_rhs_30Rnd_545x39_7N10_AK": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": 6
        },
        # Class: CfgVehicles\RHS_Ka52_base\TransportMagazines\_xx_rhs_mag_rgd5,
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 2
        },
        # Class: CfgVehicles\RHS_Ka52_base\TransportMagazines\_xx_rhs_mag_nspn_red,
        "_xx_rhs_mag_nspn_red": {
            "magazine": "rhs_mag_nspn_red",
            "count": 4
        },
        # Class: CfgVehicles\RHS_Ka52_base\TransportMagazines\_xx_rhs_mag_rdg2_white,
        "_xx_rhs_mag_rdg2_white": {
            "magazine": "rhs_mag_rdg2_white",
            "count": 4
        }
    },
    # Class: CfgVehicles\RHS_Ka52_base\TransportItems,
    "TransportItems": {
        # Class: CfgVehicles\RHS_Ka52_base\TransportItems\_xx_FirstAidKit
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 2
        }
    },
    # Class: CfgVehicles\RHS_Ka52_base\TransportWeapons,
    "TransportWeapons": {
    },
    # Class: CfgVehicles\RHS_Ka52_base\TransportBackpacks,
    "TransportBackpacks": {
    },
    "gunnerCanSee": 55,
    "driverCanSee": 55,
    "laserScanner": 1,
    "LockDetectionSystem": "8 + 4",
    "incomingMissileDetectionSystem": "8 + 16",
    # Class: CfgVehicles\RHS_Ka52_base\Components,
    "Components": {
        # Class: CfgVehicles\RHS_Ka52_base\Components\SensorsManagerComponent
        "SensorsManagerComponent": {
            # Class: CfgVehicles\RHS_Ka52_base\Components\SensorsManagerComponent\Components
            "Components": {
                # Class: CfgVehicles\RHS_Ka52_base\Components\SensorsManagerComponent\Components\LaserSensorComponent
                "LaserSensorComponent": {
                    # Class: CfgVehicles\RHS_Ka52_base\Components\SensorsManagerComponent\Components\LaserSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 9000,
                        "maxRange": 9000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: CfgVehicles\RHS_Ka52_base\Components\SensorsManagerComponent\Components\LaserSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 9000,
                        "maxRange": 9000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "angleRangeHorizontal": 75,
                    "angleRangeVertical": 75,
                    "typeRecognitionDistance": -1,
                    "maxGroundNoiseDistance": 0,
                    "maxFogSeeThrough": 0.3,
                    "animDirection": "mainGun",
                    "componentType": "LaserSensorComponent",
                    "color": [1,1,1,0],
                    "allowsMarking": 1,
                    "groundNoiseDistanceCoef": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "aimDown": 0,
                    "minTrackableSpeed": -1e+010,
                    "maxTrackableSpeed": 1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\SensorsManagerComponent\Components\PassiveRadarSensorComponent,
                "PassiveRadarSensorComponent": {
                    "componentType": "PassiveRadarSensorComponent",
                    # Class: SensorTemplatePassiveRadar\AirTarget,
                    "AirTarget": {
                        "minRange": 16000,
                        "maxRange": 16000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: SensorTemplatePassiveRadar\GroundTarget,
                    "GroundTarget": {
                        "minRange": 16000,
                        "maxRange": 16000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "typeRecognitionDistance": 12000,
                    "angleRangeHorizontal": 360,
                    "angleRangeVertical": 360,
                    "groundNoiseDistanceCoef": -1,
                    "maxGroundNoiseDistance": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "animDirection": "",
                    "aimDown": 0,
                    "color": [0.5,1,0.5,0.5],
                    "minTrackableSpeed": -1e+010,
                    "maxTrackableSpeed": 1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010,
                    "allowsMarking": 0
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent,
                "ActiveRadarSensorComponent": {
                    # Class: CfgVehicles\RHS_Ka52_base\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 11000,
                        "maxRange": 11000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: CfgVehicles\RHS_Ka52_base\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 11000,
                        "maxRange": 11000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "angleRangeHorizontal": 120,
                    "angleRangeVertical": 100,
                    "typeRecognitionDistance": 4000,
                    "maxFogSeeThrough": 1,
                    "groundNoiseDistanceCoef": -1,
                    "maxGroundNoiseDistance": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "maxTrackableSpeed": 125,
                    "componentType": "ActiveRadarSensorComponent",
                    "color": [0,1,1,1],
                    "allowsMarking": 1,
                    "animDirection": "",
                    "aimDown": 0,
                    "minTrackableSpeed": -1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\SensorsManagerComponent\Components\DataLinkSensorComponent,
                "DataLinkSensorComponent": {
                    "componentType": "DataLinkSensorComponent",
                    "allowsMarking": 1,
                    "typeRecognitionDistance": 0,
                    "color": [1,1,1,0],
                    # Class: SensorTemplatePassiveRadar\AirTarget,
                    "AirTarget": {
                        "minRange": 16000,
                        "maxRange": 16000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: SensorTemplatePassiveRadar\GroundTarget,
                    "GroundTarget": {
                        "minRange": 16000,
                        "maxRange": 16000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "angleRangeHorizontal": 360,
                    "angleRangeVertical": 360,
                    "groundNoiseDistanceCoef": -1,
                    "maxGroundNoiseDistance": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "animDirection": "",
                    "aimDown": 0,
                    "minTrackableSpeed": -1e+010,
                    "maxTrackableSpeed": 1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                }
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentLeft,
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components
            "Components": {
                # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay,
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SensorDisplay,
                "SensorDisplay": {
                    "componentType": "SensorsDisplayComponent",
                    "range": [8000,16000,24000,4000],
                    "resource": "RscCustomInfoSensors"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MineDetectorDisplay,
                "MineDetectorDisplay": {
                    "componentType": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\SlingLoadDisplay,
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent"
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultDisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentRight,
        "VehicleSystemsDisplayManagerComponentRight": {
            "defaultDisplay": "SensorDisplay",
            # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentRight\Components,
            "Components": {
                # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay,
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent",
                    "resource": "RscCustomInfoCrew"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoMiniMap"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\VehicleSystemsDisplayManagerComponentRight\Components\SensorDisplay,
                "SensorDisplay": {
                    "componentType": "SensorsDisplayComponent",
                    "range": [8000,16000,24000,4000],
                    "resource": "RscCustomInfoSensors"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MineDetectorDisplay,
                "MineDetectorDisplay": {
                    "componentType": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\SlingLoadDisplay,
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent"
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent,
        "TransportPylonsComponent": {
            "UIPicture": "rhsafrf|addons|rhs_a2port_air|data|loadouts|RHS_Ka52_EDEN_CA.paa",
            # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\pylons,
            "pylons": {
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\pylons\pylon1
                "pylon1": {
                    "hardpoints": ["RHS_HP_FAB250_KA52","RHS_HP_FAB500_KA52","RHS_HP_KMGU2_KA52","RHS_HP_B13L1_KA52","RHS_HP_B8V20_KA52","RHS_HP_UB16_KA52","RHS_HP_UB32_KA52","RHS_HP_UPK23_KA52"],
                    "priority": 1,
                    "attachment": "rhs_mag_b8v20a_ka52_s8kom",
                    "maxweight": 650,
                    "UIposition": [0.504,0.4],
                    "turret": [],
                    "hitpoint": "HitPylon1"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\pylons\pylon2,
                "pylon2": {
                    "UIposition": [0.165,0.4],
                    "mirroredMissilePos": 1,
                    "hitpoint": "HitPylon2",
                    "hardpoints": ["RHS_HP_FAB250_KA52","RHS_HP_FAB500_KA52","RHS_HP_KMGU2_KA52","RHS_HP_B13L1_KA52","RHS_HP_B8V20_KA52","RHS_HP_UB16_KA52","RHS_HP_UB32_KA52","RHS_HP_UPK23_KA52"],
                    "priority": 1,
                    "attachment": "rhs_mag_b8v20a_ka52_s8kom",
                    "maxweight": 650,
                    "turret": []
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\pylons\pylon3,
                "pylon3": {
                    "hardpoints": ["RHS_HP_FAB250","RHS_HP_B13L1_KA52","RHS_HP_B8V20_KA52","RHS_HP_UB16_KA52","RHS_HP_UB32_KA52","RHS_HP_UPK23_KA52","RHS_HP_APU6_9m127_KA52"],
                    "attachment": "rhs_mag_apu6_9m127m_ka52",
                    "maxweight": 450,
                    "priority": 2,
                    "UIposition": [0.584,0.35],
                    "turret": [0],
                    "hitpoint": "HitPylon3"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\pylons\pylon4,
                "pylon4": {
                    "UIposition": [0.085,0.35],
                    "mirroredMissilePos": 3,
                    "hitpoint": "HitPylon4",
                    "hardpoints": ["RHS_HP_FAB250","RHS_HP_B13L1_KA52","RHS_HP_B8V20_KA52","RHS_HP_UB16_KA52","RHS_HP_UB32_KA52","RHS_HP_UPK23_KA52","RHS_HP_APU6_9m127_KA52"],
                    "attachment": "rhs_mag_apu6_9m127m_ka52",
                    "maxweight": 450,
                    "priority": 2,
                    "turret": [0]
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\pylons\cmDispenser,
                "cmDispenser": {
                    "hardpoints": ["RHS_cm_UV26","RHS_cm_UV26_x2","RHS_cm_UV26_x4"],
                    "priority": 1,
                    "attachment": "rhs_UV26_CMFlare_Chaff_Magazine_x4",
                    "maxweight": 800,
                    "UIposition": [0.33,0]
                }
            },
            # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\Presets,
            "Presets": {
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\Presets\Bomb
                "Bomb": {
                    "attachment": ["rhs_mag_fab250_ka52","rhs_mag_fab250_ka52","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Bomb"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\Presets\ClusterMine,
                "ClusterMine": {
                    "attachment": ["rhs_mag_kmgu2_pfm1_ka52","rhs_mag_kmgu2_pfm1_ka52","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "KMGU-2 (AP Mines)"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\Presets\ClusterHE,
                "ClusterHE": {
                    "attachment": ["rhs_mag_kmgu2_ao25_ka52","rhs_mag_kmgu2_ao25_ka52","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "KMGU-2 (HE)"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\Presets\UPK,
                "UPK": {
                    "attachment": ["rhs_mag_upk23_ka52_mixed","rhs_mag_upk23_ka52_mixed","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "UPK-23-250"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\Presets\CAS,
                "CAS": {
                    "attachment": ["rhs_mag_b8v20a_ka52_s8kom","rhs_mag_b8v20a_ka52_s8kom","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Close Air Support"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Components\TransportPylonsComponent\Presets\HeavyCAS,
                "HeavyCAS": {
                    "attachment": ["rhs_mag_b13l1_ka52_s13b","rhs_mag_b13l1_ka52_s13b","rhs_mag_apu6_9m127m_ka52","rhs_mag_apu6_9m127m_ka52","rhs_UV26_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Close Air Support (S-13)"
                }
            }
        },
        # Class: CfgVehicles\Air\Components\TransportCountermeasuresComponent,
        "TransportCountermeasuresComponent": {
        }
    },
    # Class: CfgVehicles\RHS_Ka52_base\ViewPilot,
    "ViewPilot": {
        "initAngleX": -4,
        "initAngleY": 0,
        "initFov": 0.9,
        "minFov": 0.25,
        "maxFov": 1.25,
        "minAngleX": -65,
        "maxAngleX": 85,
        "minAngleY": -150,
        "maxAngleY": 150,
        "minMoveX": -0.075,
        "maxMoveX": 0.075,
        "minMoveY": -0.075,
        "maxMoveY": 0.075,
        "minMoveZ": -0.075,
        "maxMoveZ": 0.1
    },
    # Class: CfgVehicles\RHS_Ka52_base\Viewoptics,
    "Viewoptics": {
        "initAngleX": 0,
        "minAngleX": 0,
        "maxAngleX": 0,
        "initAngleY": 0,
        "minAngleY": 0,
        "maxAngleY": 0,
        "initFov": 0.1,
        "minFov": 0.1,
        "maxFov": 1.2
    },
    "hiddenSelections": ["camo1","camo2","n1","n2","tail_decals","mfd_gun_tex"],
    # Class: CfgVehicles\RHS_Ka52_base\textureSources,
    "textureSources": {
        # Class: CfgVehicles\RHS_Ka52_base\textureSources\standard
        "standard": {
            "displayName": "Grey",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01_co.paa","|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02_co.paa"],
            "factions": ["rhs_faction_vvs_c","rhs_faction_vvs"]
        },
        # Class: CfgVehicles\RHS_Ka52_base\textureSources\Camo,
        "Camo": {
            "displayName": "Camo",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01_RU_co.paa","|rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02_RU_co.paa"],
            "factions": ["rhs_faction_vvs_c","rhs_faction_vvs"]
        }
    },
    "textureList": [],
    # Class: CfgVehicles\RHS_Ka52_base\Attributes,
    "Attributes": {
        # Class: CfgVehicles\RHS_Ka52_base\Attributes\ObjectTexture
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type,
        "rhs_decalNumber_type": {
            "displayName": "Define font type of side number",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHSAIRKA52NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values,
            "values": {
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\NoChange
                "NoChange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\AviaYellow,
                "AviaYellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\AviaBlue,
                "AviaBlue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultValue": "AviaBlue"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\AviaRed,
                "AviaRed": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\AviaWhiteOut,
                "AviaWhiteOut": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\AviaCDF,
                "AviaCDF": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\Default,
                "Default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\DefaultRed,
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\BoldRed,
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\CDF,
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\Handpaint,
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\HandpaintBlack,
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber_type\values\Iraqi,
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalNumber,
        "rhs_decalNumber": {
            "displayName": "Set side number",
            "tooltip": "Set side number. 2 numbers are required. Type 0 to hide numbers completly",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typeName": "Number",
            "defaultValue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRKA52NumberPlaces}else{[_this, [['Number', cRHSAIRKA52NumberPlaces, _this getVariable ['rhs_decalNumber_type','AviaYellow'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalTail,
        "rhs_decalTail": {
            "displayName": "Define tail decal",
            "tooltip": "Define tail decalthat will be drawn on vehicle",
            "property": "rhs_decalTail",
            "control": "Combo",
            "expression": "[_this,[['Label', cRHSAIRKA52TailPlaces, 'Aviation',_value]]] call rhs_fnc_decalsInit",
            "defaultValue": -1,
            "typeName": "Number",
            # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalTail\values,
            "values": {
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalTail\values\Default
                "Default": {
                    "name": "Default",
                    "value": -1
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalTail\values\Empty,
                "Empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles\RHS_Ka52_base\Attributes\rhs_decalTail\values\VVS,
                "VVS": {
                    "name": "VVS Russia",
                    "value": 3,
                    "defaultValue": 3
                }
            }
        }
    },
    # Class: CfgVehicles\RHS_Ka52_base\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\DoorL
        "DoorL": {
            "source": "door",
            "animPeriod": 1.4
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\DoorR,
        "DoorR": {
            "source": "door",
            "animPeriod": 1.4
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\landingLights,
        "landingLights": {
            "source": "door",
            "animPeriod": 1.4
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\eject,
        "eject": {
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\k37_pilot_rocket_hide,
        "k37_pilot_rocket_hide": {
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\k37_gunner_rocket_hide,
        "k37_gunner_rocket_hide": {
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\elev,
        "elev": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\elev_bank,
        "elev_bank": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\offset,
        "offset": {
            "source": "user",
            "animperiod": 0.0002
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\mfd_right_gun_tg,
        "mfd_right_gun_tg": {
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 1
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\mfd_right_gun_ta,
        "mfd_right_gun_ta": {
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 1
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\mfd_left_toggle,
        "mfd_left_toggle": {
            "initPhase": 0,
            "source": "user",
            "animPeriod": 1e-007
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\muzzle_rot_cannon,
        "muzzle_rot_cannon": {
            "weapon": "rhs_weap_2a42",
            "source": "ammorandom"
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\muzzle_hide_upk23,
        "muzzle_hide_upk23": {
            "weapon": "RHS_Weap_GSh23Lx2",
            "source": "reload"
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\muzzle_rot_upk23,
        "muzzle_rot_upk23": {
            "weapon": "RHS_Weap_GSh23Lx2",
            "source": "ammorandom"
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\hit_pylon_1_source,
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\hit_pylon_2_source,
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\hit_pylon_3_source,
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles\RHS_Ka52_base\AnimationSources\hit_pylon_4_source,
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass1,
        "HitGlass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass2,
        "HitGlass2": {
            "hitpoint": "HitGlass2",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass3,
        "HitGlass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass4,
        "HitGlass4": {
            "hitpoint": "HitGlass4",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass5,
        "HitGlass5": {
            "hitpoint": "HitGlass5",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass6,
        "HitGlass6": {
            "hitpoint": "HitGlass6",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass7,
        "HitGlass7": {
            "hitpoint": "HitGlass7",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass8,
        "HitGlass8": {
            "hitpoint": "HitGlass8",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass9,
        "HitGlass9": {
            "hitpoint": "HitGlass9",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass10,
        "HitGlass10": {
            "hitpoint": "HitGlass10",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass11,
        "HitGlass11": {
            "hitpoint": "HitGlass11",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass12,
        "HitGlass12": {
            "hitpoint": "HitGlass12",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass13,
        "HitGlass13": {
            "hitpoint": "HitGlass13",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HitGlass14,
        "HitGlass14": {
            "hitpoint": "HitGlass14",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\Gatling,
        "Gatling": {
            "source": "revolving",
            "weapon": "gatling_30mm"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\Muzzle_flash,
        "Muzzle_flash": {
            "source": "ammorandom",
            "weapon": "gatling_30mm"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\Missiles_revolving,
        "Missiles_revolving": {
            "source": "revolving",
            "weapon": "rockets_Skyfire"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\Hide,
        "Hide": {
            "source": "user",
            "animPeriod": 0,
            "initPhase": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\door_L,
        "door_L": {
            "source": "door",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\door_R,
        "door_R": {
            "source": "door",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\door_L_pop,
        "door_L_pop": {
            "source": "door",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\door_R_pop,
        "door_R_pop": {
            "source": "door",
            "animPeriod": 1,
            "initPhase": 0
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\AnimationSources\HideWeapons,
        "HideWeapons": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Helicopter\AnimationSources\HitEngine1,
        "HitEngine1": {
            "source": "hit",
            "hitpoint": "HitEngine1",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter\AnimationSources\HitEngine2,
        "HitEngine2": {
            "source": "hit",
            "hitpoint": "HitEngine2",
            "raw": 1
        },
        # Class: CfgVehicles\Helicopter\AnimationSources\HitWinch_Source,
        "HitWinch_Source": {
            "source": "hit",
            "hitpoint": "HitWinch",
            "raw": 1
        },
        # Class: CfgVehicles\Air\AnimationSources\CollisionLightRed_source,
        "CollisionLightRed_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionRed"
        },
        # Class: CfgVehicles\Air\AnimationSources\CollisionLightWhite_source,
        "CollisionLightWhite_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionWhite"
        }
    },
    # Class: CfgVehicles\RHS_Ka52_base\UserActions,
    "UserActions": {
        # Class: CfgVehicles\RHS_Ka52_base\UserActions\SAFEMODE
        "SAFEMODE": {
            "displayName": "<t color='#00FF7F'>MASTERSAFE</t>",
            "condition": "(call rhs_fnc_findPlayer) in this",
            "statement": "(call rhs_fnc_findPlayer) action ['SwitchWeapon', this, (call rhs_fnc_findPlayer), (weapons this) find 'rhs_weap_MASTERSAFE'];",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showWindow": 0,
            "shortcut": "user13",
            "hideOnUse": 1
        },
        # Class: CfgVehicles\RHS_Ka52_base\UserActions\MFD_Left_Toggle,
        "MFD_Left_Toggle": {
            "displayName": "Toggle MFD",
            "position": "",
            "priority": 0.01,
            "radius": 3,
            "onlyForplayer": 1,
            "showWindow": 0,
            "condition": "(call rhs_fnc_findPlayer) isEqualTo (driver this)",
            "statement": "this animateSource ['mfd_left_toggle',1-(this animationSourcePhase 'mfd_left_toggle')]"
        },
        # Class: CfgVehicles\RHS_Ka52_base\UserActions\openDoor,
        "openDoor": {
            "displayName": "Lights up",
            "position": "",
            "priority": 0.01,
            "radius": 3,
            "onlyForplayer": 1,
            "showWindow": 0,
            "condition": "this doorPhase 'landingLights' < 0.5 AND alive this",
            "statement": "this animateDoor ['landingLights',1]"
        },
        # Class: CfgVehicles\RHS_Ka52_base\UserActions\closeDoor,
        "closeDoor": {
            "displayName": "Lights down",
            "condition": "this doorPhase 'landingLights' > 0.5 AND alive this",
            "statement": "this animateDoor ['landingLights',0]",
            "position": "",
            "priority": 0.01,
            "radius": 3,
            "onlyForplayer": 1,
            "showWindow": 0
        }
    },
    "enableManualFire": 1,
    # Class: CfgVehicles\RHS_Ka52_base\Turrets,
    "Turrets": {
        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret
        "MainTurret": {
            "gunnerDoor": "doorR",
            "gunnerLeftHandAnimName": "lever_gunner",
            "gunnerRightHandAnimName": "stick_gunner",
            "gunnerLeftLegAnimName": "pedalL",
            "gunnerRightLegAnimName": "pedalR",
            "gunnerAction": "RHS_KA52_Gunner",
            "gunnerInAction": "RHS_KA52_Gunner",
            "gunnerGetInAction": "pilot_Heli_Light_02_Enter",
            "gunnerGetOutAction": "pilot_Heli_Light_02_exit",
            "isCopilot": 1,
            "startEngine": 0,
            "outGunnerMayFire": 1,
            "commanding": -1,
            "primaryGunner": 1,
            "usePIP": 1,
            "castGunnerShadow": 1,
            "viewGunnerShadow": 1,
            "CanEject": 1,
            "memoryPointsGetInGunner": "Pos_Gunner",
            "memoryPointsGetInGunnerDir": "Pos_Gunner_dir",
            "memoryPointsGetInGunnerPrecise": "pos gunner",
            "precisegetinout": 1,
            "minElev": -80,
            "maxElev": 15,
            "initElev": 0,
            "minTurn": -120,
            "maxTurn": 120,
            "initTurn": 0,
            "gunBeg": "gunstart",
            "gunEnd": "gunend",
            "body": "MainTurret",
            "gun": "MainGun",
            "memoryPointGun": "machinegun",
            "memoryPointGunnerOptics": "pilotview",
            "selectionFireAnim": "zasleh",
            "turretInfoType": "RHS_RscWeaponKa52_FCS",
            "canUseScanners": 0,
            "allowTabLock": 0,
            # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Viewoptics,
            "Viewoptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "initFov": 0.067,
                "minFov": 0.019,
                "maxFov": 0.067
            },
            "gunnerOpticsEffect": ["TankCommanderOptics1"],
            # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\OpticsIn\Samshin_WFOV
                "Samshin_WFOV": {
                    "opticsDisplayName": "3",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_samshin_WFOV",
                    "initanglex": 0,
                    "initangley": 0,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "minanglex": -30,
                    "minangley": -100,
                    "initfov": 0.233333,
                    "maxfov": 0.233333,
                    "minfov": 0.233333,
                    "thermalmode": [0,1],
                    "visionmode": ["Normal","TI"]
                },
                # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\OpticsIn\Samshin_NFOV,
                "Samshin_NFOV": {
                    "opticsDisplayName": "15",
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_samshin",
                    "initfov": 0.0466667,
                    "maxfov": 0.0466667,
                    "minfov": 0.0466667,
                    "initanglex": 0,
                    "initangley": 0,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "minanglex": -30,
                    "minangley": -100,
                    "thermalmode": [0,1],
                    "visionmode": ["Normal","TI"]
                },
                # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\OpticsIn\Samshin_NFOV_Stabilised,
                "Samshin_NFOV_Stabilised": {
                    "opticsDisplayName": "22",
                    "initfov": 0.0318182,
                    "maxfov": 0.0318182,
                    "minfov": 0.0318182,
                    "directionStabilized": 1,
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_samshin",
                    "initanglex": 0,
                    "initangley": 0,
                    "maxanglex": 30,
                    "maxangley": 100,
                    "minanglex": -30,
                    "minangley": -100,
                    "thermalmode": [0,1],
                    "visionmode": ["Normal","TI"]
                }
            },
            # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components,
            "Components": {
                # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components
                    "Components": {
                        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\CrewDisplay,
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\MinimapDisplay,
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\UAVDisplay,
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SensorDisplay,
                        "SensorDisplay": {
                            "componentType": "SensorsDisplayComponent",
                            "range": [8000,16000,24000,4000],
                            "resource": "RscCustomInfoSensors"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MineDetectorDisplay,
                        "MineDetectorDisplay": {
                            "componentType": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\SlingLoadDisplay,
                        "SlingLoadDisplay": {
                            "componentType": "SlingLoadDisplayComponent"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultDisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    "defaultDisplay": "SensorDisplay",
                    # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components,
                    "Components": {
                        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\CrewDisplay,
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent",
                            "resource": "RscCustomInfoCrew"
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\MinimapDisplay,
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent",
                            "resource": "RscCustomInfoMiniMap"
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\UAVDisplay,
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\Components\SensorDisplay,
                        "SensorDisplay": {
                            "componentType": "SensorsDisplayComponent",
                            "resource": "RscCustomInfoSensors",
                            "range": [8000,16000,24000,4000]
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MineDetectorDisplay,
                        "MineDetectorDisplay": {
                            "componentType": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\SlingLoadDisplay,
                        "SlingLoadDisplay": {
                            "componentType": "SlingLoadDisplayComponent"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
            "gunnerForceOptics": 0,
            "weapons": ["rhs_weap_MASTERSAFE_Holdster15","rhs_weap_fcs_mi24","rhs_weap_2a42"],
            "magazines": ["rhs_laserfcsmag","rhs_mag_3uor6_230","rhs_mag_3ubr8_230"],
            # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\HitTurret,
            "HitTurret": {
                "armor": 0.8,
                "material": -1,
                "name": "gun1",
                "visual": "gun1",
                "passThrough": 0.5
            },
            # Class: CfgVehicles\RHS_Ka52_base\Turrets\MainTurret\HitGun,
            "HitGun": {
                "armor": 0.4,
                "material": -1,
                "name": "gun2",
                "visual": "gun2",
                "passThrough": 0.2
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\Turrets\MainTurret\OpticsOut,
            "OpticsOut": {
                # Class: CfgVehicles\Heli_Attack_02_base_F\Turrets\MainTurret\OpticsOut\Monocular
                "Monocular": {
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
                    "visionMode": ["Normal","NVG"],
                    "gunnerOpticsModel": "",
                    "gunnerOpticsEffect": []
                }
            },
            "soundServo": ["",0.01,1],
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "discreteDistance": [100,200,300,400,500,600,700,800,1000,1200,1500,1800,2100,2500],
            "discreteDistanceInitIndex": 5,
            "showHMD": 0,
            "showAllTargets": 4,
            "maxHorizontalRotSpeed": 1.8,
            "maxVerticalRotSpeed": 1.5,
            # Class: CfgVehicles\Heli_Attack_02_base_F\Turrets\MainTurret\HitPoints,
            "HitPoints": {
                # Class: CfgVehicles\Heli_Attack_02_base_F\Turrets\MainTurret\HitPoints\HitTurret
                "HitTurret": {
                    "armor": 1,
                    "material": -1,
                    "name": "main_turret_hit",
                    "visual": "gun",
                    "passThrough": 0.3,
                    "radius": 0.35
                },
                # Class: CfgVehicles\Heli_Attack_02_base_F\Turrets\MainTurret\HitPoints\HitGun,
                "HitGun": {
                    "armor": 1,
                    "material": -1,
                    "name": "main_gun_hit",
                    "visual": "gun",
                    "passThrough": 0.3,
                    "radius": 0.35
                }
            },
            "turretCanSee": "1 + 2 + 4 + 8 + 32",
            # Class: CfgVehicles\Helicopter\Turrets\MainTurret\TurretSpec,
            "TurretSpec": {
                "showHeadPhones": 1
            },
            "enableManualFire": 0,
            "animationSourceBody": "mainTurret",
            "animationSourceGun": "mainGun",
            "animationSourceHatch": "hatchGunner",
            "animationSourceCamElev": "camElev",
            "proxyType": "CPGunner",
            "proxyIndex": 1,
            "gunnerName": "Gunner",
            "gunnerType": "",
            "primaryObserver": 0,
            "soundElevation": ["",0.00316228,1],
            "minOutElev": -4,
            "maxOutElev": 20,
            "initOutElev": 0,
            "minOutTurn": -60,
            "maxOutTurn": 60,
            "initOutTurn": 0,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "stabilizedInAxes": 3,
            "primary": 1,
            "hasGunner": 1,
            # Class: CfgVehicles\AllVehicles\NewTurret\ViewGunner,
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
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOpticsShowCursor": 0,
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
            "gunnerOutOpticsEffect": [],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "forceHideGunner": 0,
            "inGunnerMayFire": 1,
            "viewGunnerInExternal": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "gunnerCompartments": "Compartment1",
            "LODTurnedIn": -1,
            "LODTurnedOut": -1,
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
            "armorLights": 0.4,
            # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
            "Reflectors": {
            },
            "aggregateReflectors": [],
            # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
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
                # Class: WeaponFireGun\Table,
                "Table": {
                    # Class: WeaponFireGun\Table\T0
                    "T0": {
                        "maxT": 0,
                        "color": [0.82,0.95,0.93,0]
                    },
                    # Class: WeaponFireGun\Table\T1,
                    "T1": {
                        "maxT": 200,
                        "color": [0.75,0.77,0.9,0]
                    },
                    # Class: WeaponFireGun\Table\T2,
                    "T2": {
                        "maxT": 400,
                        "color": [0.56,0.62,0.67,0]
                    },
                    # Class: WeaponFireGun\Table\T3,
                    "T3": {
                        "maxT": 600,
                        "color": [0.39,0.46,0.47,0]
                    },
                    # Class: WeaponFireGun\Table\T4,
                    "T4": {
                        "maxT": 800,
                        "color": [0.24,0.31,0.31,0]
                    },
                    # Class: WeaponFireGun\Table\T5,
                    "T5": {
                        "maxT": 1000,
                        "color": [0.23,0.31,0.29,0]
                    },
                    # Class: WeaponFireGun\Table\T6,
                    "T6": {
                        "maxT": 1500,
                        "color": [0.21,0.29,0.27,0]
                    },
                    # Class: WeaponFireGun\Table\T7,
                    "T7": {
                        "maxT": 2000,
                        "color": [0.19,0.23,0.21,0]
                    },
                    # Class: WeaponFireGun\Table\T8,
                    "T8": {
                        "maxT": 2300,
                        "color": [0.22,0.19,0.1,0]
                    },
                    # Class: WeaponFireGun\Table\T9,
                    "T9": {
                        "maxT": 2500,
                        "color": [0.35,0.2,0.02,0]
                    },
                    # Class: WeaponFireGun\Table\T10,
                    "T10": {
                        "maxT": 2600,
                        "color": [0.62,0.29,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T11,
                    "T11": {
                        "maxT": 2650,
                        "color": [0.59,0.35,0.05,0]
                    },
                    # Class: WeaponFireGun\Table\T12,
                    "T12": {
                        "maxT": 2700,
                        "color": [0.75,0.37,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T13,
                    "T13": {
                        "maxT": 2750,
                        "color": [0.88,0.34,0.03,0]
                    },
                    # Class: WeaponFireGun\Table\T14,
                    "T14": {
                        "maxT": 2800,
                        "color": [0.91,0.5,0.17,0]
                    },
                    # Class: WeaponFireGun\Table\T15,
                    "T15": {
                        "maxT": 2850,
                        "color": [1,0.6,0.2,0]
                    },
                    # Class: WeaponFireGun\Table\T16,
                    "T16": {
                        "maxT": 2900,
                        "color": [1,0.71,0.3,0]
                    },
                    # Class: WeaponFireGun\Table\T17,
                    "T17": {
                        "maxT": 2950,
                        "color": [0.98,0.83,0.41,0]
                    },
                    # Class: WeaponFireGun\Table\T18,
                    "T18": {
                        "maxT": 3000,
                        "color": [0.98,0.91,0.54,0]
                    },
                    # Class: WeaponFireGun\Table\T19,
                    "T19": {
                        "maxT": 3100,
                        "color": [0.98,0.99,0.6,0]
                    },
                    # Class: WeaponFireGun\Table\T20,
                    "T20": {
                        "maxT": 3300,
                        "color": [0.96,0.99,0.72,0]
                    },
                    # Class: WeaponFireGun\Table\T21,
                    "T21": {
                        "maxT": 3600,
                        "color": [1,0.98,0.91,0]
                    },
                    # Class: WeaponFireGun\Table\T22,
                    "T22": {
                        "maxT": 4200,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
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
                # Class: WeaponCloudsGun\Table,
                "Table": {
                    # Class: WeaponCloudsGun\Table\T0
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
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
                # Class: WeaponCloudsMGun\Table,
                "Table": {
                    # Class: WeaponCloudsMGun\Table\T0
                    "T0": {
                        "maxT": 0,
                        "color": [1,1,1,0]
                    }
                }
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\Turrets,
            "Turrets": {
            },
            "forceNVG": 0,
            "turretFollowFreeLook": 0,
            "dontCreateAI": 0,
            "disableSoundAttenuation": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
            "TurnIn": {
                "turnOffset": 0
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
            "TurnOut": {
                "turnOffset": 0
            },
            "showCrewAim": 0
        },
        # Class: CfgVehicles\Helicopter_Base_F\Turrets\CopilotTurret,
        "CopilotTurret": {
        }
    },
    # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights,
    "compartmentsLights": {
        # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights\Comp1
        "Comp1": {
            # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights\Comp1\Light_Pilot
            "Light_Pilot": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights\Comp1\Light_Pilot\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.5,
                    "hardLimitEnd": 0.6
                },
                "point": "light_pilot"
            },
            # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights\Comp1\Light_Gunner,
            "Light_Gunner": {
                "point": "light_gunner",
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights\Comp1\Light_Pilot\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.5,
                    "hardLimitEnd": 0.6
                }
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights\Comp2,
        "Comp2": {
            # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights\Comp2\Light_Pilot
            "Light_Pilot": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights\Comp1\Light_Pilot\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.5,
                    "hardLimitEnd": 0.6
                },
                "point": "light_pilot"
            },
            # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights\Comp2\Light_Gunner,
            "Light_Gunner": {
                "point": "light_gunner",
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\RHS_Ka52_base\compartmentsLights\Comp1\Light_Pilot\Attenuation,
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.5,
                    "hardLimitEnd": 0.6
                }
            }
        }
    },
    # Class: CfgVehicles\RHS_Ka52_base\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\RHS_Ka52_base\Reflectors\LSvetla
        "LSvetla": {
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "intensity": 50,
            "size": 1,
            "innerAngle": 5,
            "outerAngle": 75,
            "coneFadeCoef": 10,
            "position": "L svetlo",
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 0.75,
            # Class: CfgVehicles\RHS_Ka52_base\Reflectors\LSvetla\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardLimitStart": 200,
                "hardLimitEnd": 250
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\Reflectors\LSvetlaFlare,
        "LSvetlaFlare": {
            "position": "L_Flare",
            "useFlare": 1,
            "color": [10,10,9],
            "ambient": [10,10,9],
            "intensity": 50,
            "size": 1,
            "innerAngle": 5,
            "outerAngle": 75,
            "coneFadeCoef": 10,
            "direction": "konec L svetla",
            "hitpoint": "L svetlo",
            "selection": "L svetlo",
            "dayLight": 0,
            "flareSize": 0.75,
            # Class: CfgVehicles\RHS_Ka52_base\Reflectors\LSvetla\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardLimitStart": 200,
                "hardLimitEnd": 250
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\Reflectors\RSvetla,
        "RSvetla": {
            "position": "P svetlo",
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "color": [7000,7500,10000],
            "ambient": [70,75,100],
            "intensity": 50,
            "size": 1,
            "innerAngle": 5,
            "outerAngle": 75,
            "coneFadeCoef": 10,
            "useFlare": 0,
            "dayLight": 0,
            "flareSize": 0.75,
            # Class: CfgVehicles\RHS_Ka52_base\Reflectors\LSvetla\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardLimitStart": 200,
                "hardLimitEnd": 250
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\Reflectors\RSvetlaFlare,
        "RSvetlaFlare": {
            "position": "R_Flare",
            "useFlare": 1,
            "color": [10,10,9],
            "ambient": [10,10,9],
            "direction": "konec P svetla",
            "hitpoint": "P svetlo",
            "selection": "P svetlo",
            "intensity": 50,
            "size": 1,
            "innerAngle": 5,
            "outerAngle": 75,
            "coneFadeCoef": 10,
            "dayLight": 0,
            "flareSize": 0.75,
            # Class: CfgVehicles\RHS_Ka52_base\Reflectors\LSvetla\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 1,
                "quadratic": 0,
                "hardLimitStart": 200,
                "hardLimitEnd": 250
            }
        }
    },
    # Class: CfgVehicles\RHS_Ka52_base\markerlights,
    "markerlights": {
        # Class: CfgVehicles\RHS_Ka52_base\markerlights\GreenStill
        "GreenStill": {
            "activeLight": 0,
            "color": [0,0.8,0],
            "ambient": [0,0.08,0],
            "intensity": 55,
            "blinking": 0,
            "brightness": 0.01,
            "flareSize": 0.5,
            "name": "zeleny pozicni",
            "useFlare": 1,
            "drawLight": 1,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.08
        },
        # Class: CfgVehicles\RHS_Ka52_base\markerlights\RedStill,
        "RedStill": {
            "color": [0.8,0,0],
            "ambient": [0.08,0,0],
            "name": "cerveny pozicni",
            "activeLight": 0,
            "intensity": 55,
            "blinking": 0,
            "brightness": 0.01,
            "flareSize": 0.5,
            "useFlare": 1,
            "drawLight": 1,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.08
        },
        # Class: CfgVehicles\RHS_Ka52_base\markerlights\WhiteStill,
        "WhiteStill": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "bily pozicni",
            "activeLight": 0,
            "intensity": 55,
            "blinking": 0,
            "brightness": 0.01,
            "flareSize": 0.5,
            "useFlare": 1,
            "drawLight": 1,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.08
        },
        # Class: CfgVehicles\RHS_Ka52_base\markerlights\WhiteBlicking,
        "WhiteBlicking": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "blinking": 1,
            "name": "bily pozicni blik",
            "activeLight": 0,
            "intensity": 55,
            "brightness": 0.01,
            "flareSize": 0.5,
            "useFlare": 1,
            "drawLight": 1,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.08
        },
        # Class: CfgVehicles\RHS_Ka52_base\markerlights\RedBlinking,
        "RedBlinking": {
            "color": [0.9,0.15,0.1],
            "ambient": [0.09,0.015,0.01],
            "name": "cerveny pozicni blik",
            "blinking": 1,
            "activeLight": 0,
            "intensity": 55,
            "brightness": 0.01,
            "flareSize": 0.5,
            "useFlare": 1,
            "drawLight": 1,
            "drawLightSize": 0.25,
            "drawLightCenterSize": 0.08
        }
    },
    "dammageHalf": ["|rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_cauges_CO.paa","|rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_caugesmf_CO.paa"],
    "dammageFull": ["|rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_cauges_CO.paa","|rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_caugesmf_CO.paa"],
    # Class: CfgVehicles\RHS_Ka52_base\Damage,
    "Damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_01_destruct.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_02_destruct.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass_in.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass_in_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|ka52_glass_in_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_cauges_light.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_cauges_bug.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_cauges_bug.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_weapons.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_weapons_damage.rvmat","rhsafrf|addons|rhs_a2port_air|ka52|data|Ka52_weapons_destruct.rvmat"]
    },
    # Class: CfgVehicles\RHS_Ka52_base\MFD,
    "MFD": {
        # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Left_Compass
        "MFD_Left_Compass": {
            "topLeft": "mfd_2_nav_tl",
            "topRight": "mfd_2_nav_tr",
            "bottomLeft": "mfd_2_nav_bl",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_var",
            "enableParallax": 0,
            # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Left_Compass\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Left_Compass\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Left_Compass\Draw,
            "Draw": {
                "alpha": 0.95,
                "color": [0,0.83,0.83],
                "condition": "on",
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Left_Compass\Draw\Text,
                "Text": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "Heading",
                    "sourceScale": 1,
                    "pos": [[0.498,0.19],1],
                    "right": [[0.543,0.19],1],
                    "down": [[0.498,0.24],1]
                }
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Right_Gun,
        "MFD_Right_Gun": {
            "topLeft": "mfd_3_gun_tl",
            "topRight": "mfd_3_gun_tr",
            "bottomLeft": "mfd_3_gun_bl",
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_var",
            "turret": [0],
            # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Right_Gun\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Right_Gun\Draw,
            "Draw": {
                "alpha": 0.95,
                "color": [0.45,0.7,0.29],
                "condition": "on",
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Right_Gun\Draw\Speed,
                "Speed": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "speed",
                    "sourceScale": 3.6,
                    "sourceLength": 1,
                    "pos": [[0.425,0.165],1],
                    "right": [[0.46,0.165],1],
                    "down": [[0.425,0.21],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Right_Gun\Draw\Height,
                "Height": {
                    "source": "altitudeAGL",
                    "sourceOffset": -2,
                    "sourceScale": 1,
                    "sourceLength": 1,
                    "pos": [[0.625,0.165],1],
                    "right": [[0.66,0.165],1],
                    "down": [[0.625,0.21],1],
                    "type": "text",
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Right_Gun\Draw\TurretDirection,
                "TurretDirection": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "userText",
                    "sourceIndex": 2,
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "pos": [[0.515,0.165],1],
                    "right": [[0.55,0.165],1],
                    "down": [[0.515,0.21],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Right_Gun\Draw\TurretElevation,
                "TurretElevation": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "userText",
                    "sourceIndex": 3,
                    "sourceScale": 1,
                    "sourceLength": 1,
                    "sourcePrecision": 1,
                    "pos": [[0.88,0.385],1],
                    "right": [[0.895,0.385],1],
                    "down": [[0.88,0.405],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Right_Gun\Draw\DistanceToTarget,
                "DistanceToTarget": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "userText",
                    "sourceIndex": 1,
                    "sourceScale": 1,
                    "sourceLength": 1,
                    "sourcePrecision": 1,
                    "pos": [[0.515,0.74],1],
                    "right": [[0.55,0.74],1],
                    "down": [[0.515,0.785],1]
                }
            },
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "enableParallax": 0,
            # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Left_Compass\Bones,
            "Bones": {
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_left_Gun,
        "MFD_left_Gun": {
            "topLeft": "mfd_2_gun_tl",
            "topRight": "mfd_2_gun_tr",
            "bottomLeft": "mfd_2_gun_bl",
            "color": [0,1,0,0.1],
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_left_Gun\material,
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [400,200,200,1]
            },
            # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_left_Gun\Draw,
            "Draw": {
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_left_Gun\Draw\Speed
                "Speed": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "speed",
                    "sourceScale": 3.6,
                    "sourceLength": 1,
                    "pos": [[0.425,0.165],1],
                    "right": [[0.46,0.165],1],
                    "down": [[0.425,0.21],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_left_Gun\Draw\Height,
                "Height": {
                    "source": "altitudeAGL",
                    "sourceOffset": -2,
                    "sourceScale": 1,
                    "sourceLength": 1,
                    "pos": [[0.625,0.165],1],
                    "right": [[0.66,0.165],1],
                    "down": [[0.625,0.21],1],
                    "type": "text",
                    "align": "left",
                    "scale": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_left_Gun\Draw\TurretDirection,
                "TurretDirection": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "userText",
                    "sourceIndex": 2,
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "pos": [[0.515,0.165],1],
                    "right": [[0.55,0.165],1],
                    "down": [[0.515,0.21],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_left_Gun\Draw\TurretElevation,
                "TurretElevation": {
                    "type": "text",
                    "align": "left",
                    "scale": 1,
                    "source": "userText",
                    "sourceIndex": 3,
                    "sourceScale": 1,
                    "sourceLength": 1,
                    "sourcePrecision": 1,
                    "pos": [[0.88,0.385],1],
                    "right": [[0.895,0.385],1],
                    "down": [[0.88,0.405],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_left_Gun\Draw\DistanceToTarget,
                "DistanceToTarget": {
                    "type": "text",
                    "align": "center",
                    "scale": 1,
                    "source": "userText",
                    "sourceIndex": 1,
                    "sourceScale": 1,
                    "sourceLength": 1,
                    "sourcePrecision": 1,
                    "pos": [[0.515,0.74],1],
                    "right": [[0.55,0.74],1],
                    "down": [[0.515,0.785],1]
                },
                "alpha": 0.95,
                "color": [0.45,0.7,0.29],
                "condition": "on"
            },
            "turret": [0],
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "enableParallax": 0,
            # Class: CfgVehicles\RHS_Ka52_base\MFD\MFD_Left_Compass\Bones,
            "Bones": {
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\MFD\CrossGunner,
        "CrossGunner": {
            "topLeft": "HUD LH",
            "topRight": "HUD PH",
            "bottomLeft": "HUD LD",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,1,0,0.1],
            "enableParallax": 1,
            "turret": [0],
            # Class: CfgVehicles\RHS_Ka52_base\MFD\CrossGunner\Bones,
            "Bones": {
                # Class: CfgVehicles\RHS_Ka52_base\MFD\CrossGunner\Bones\WeaponAim
                "WeaponAim": {
                    "type": "vector",
                    "source": "turretworld",
                    "pos0": [0.5,0.41],
                    "pos10": [1.15,1.75]
                }
            },
            # Class: CfgVehicles\RHS_Ka52_base\MFD\CrossGunner\Draw,
            "Draw": {
                "alpha": 0.95,
                "color": [0,0.3,0.05],
                "condition": "on",
                # Class: CfgVehicles\RHS_Ka52_base\MFD\CrossGunner\Draw\MGun,
                "MGun": {
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\CrossGunner\Draw\MGun\Circle
                    "Circle": {
                        "type": "line",
                        "width": 4,
                        "points": [["WeaponAim",[0,0.02],1],["WeaponAim",[0,0.01],1],[],["WeaponAim",[0,-0.01],1],["WeaponAim",[0,-0.02],1],[],["WeaponAim",[0.02,0],1],["WeaponAim",[0.01,0],1],[],["WeaponAim",[-0.01,0],1],["WeaponAim",[-0.02,0],1],[]]
                    }
                }
            }
        },
        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD,
        "AirplaneHUD": {
            # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Pos10Vector
            "Pos10Vector": {
                "type": "vector",
                "pos0": [0.502,0.49],
                "pos10": [1.112,1.03]
            },
            "topLeft": "HUD LH",
            "topRight": "HUD PH",
            "bottomLeft": "HUD LD",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,1,0,0.1],
            "enableParallax": 1,
            "turret": [-1],
            "font": "rhs_digital_font_rus",
            # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones,
            "Bones": {
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\PlaneW
                "PlaneW": {
                    "type": "fixed",
                    "pos": [0.502,0.49]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\ImpactPoint,
                "ImpactPoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.39],
                    "pos10": [1.134,0.96]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\Limit0109,
                "Limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot1,
                "MissileFlightTimeRot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minAngle": 0,
                    "maxAngle": 18,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot2,
                "MissileFlightTimeRot2": {
                    "maxAngle": 37,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot3,
                "MissileFlightTimeRot3": {
                    "maxAngle": 55.5,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot4,
                "MissileFlightTimeRot4": {
                    "maxAngle": 74,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot5,
                "MissileFlightTimeRot5": {
                    "maxAngle": 92.5,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot6,
                "MissileFlightTimeRot6": {
                    "maxAngle": 111,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot7,
                "MissileFlightTimeRot7": {
                    "maxAngle": 129.5,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot8,
                "MissileFlightTimeRot8": {
                    "maxAngle": 148,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot9,
                "MissileFlightTimeRot9": {
                    "maxAngle": 166.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot10,
                "MissileFlightTimeRot10": {
                    "maxAngle": 185,
                    "max": 10,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot11,
                "MissileFlightTimeRot11": {
                    "maxAngle": 203.5,
                    "max": 11,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot12,
                "MissileFlightTimeRot12": {
                    "maxAngle": 222,
                    "max": 12,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot13,
                "MissileFlightTimeRot13": {
                    "maxAngle": 240.5,
                    "max": 13,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot14,
                "MissileFlightTimeRot14": {
                    "maxAngle": 259,
                    "max": 14,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot15,
                "MissileFlightTimeRot15": {
                    "maxAngle": 277.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot16,
                "MissileFlightTimeRot16": {
                    "maxAngle": 296,
                    "max": 16,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot17,
                "MissileFlightTimeRot17": {
                    "maxAngle": 314.5,
                    "max": 17,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot18,
                "MissileFlightTimeRot18": {
                    "maxAngle": 333,
                    "max": 18,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot19,
                "MissileFlightTimeRot19": {
                    "maxAngle": 351.5,
                    "max": 19,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot20,
                "MissileFlightTimeRot20": {
                    "maxAngle": 370,
                    "max": 20,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.899054
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\ForwardVector,
                "ForwardVector": {
                    "type": "vector",
                    "source": "forward",
                    "pos0": [0,0],
                    "pos10": [0.347,0.345]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\Target,
                "Target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.5,0.39],
                    "pos10": [1.134,0.96]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\Velocity,
                "Velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.502,0.49],
                    "pos10": [0.563,0.544]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\SliderSpeedSource,
                "SliderSpeedSource": {
                    "type": "linear",
                    "source": "speed",
                    "min": 0,
                    "max": 138.889,
                    "minPos": [0.255,0.2],
                    "maxPos": [0.255,0.525]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\AGLMove,
                "AGLMove": {
                    "type": "linear",
                    "source": "altitudeAGL",
                    "min": 0,
                    "max": 50,
                    "minPos": [0,"0.15*0.65"],
                    "maxPos": [0,"0.65*0.65"]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\Heading,
                "Heading": {
                    "type": "linear",
                    "source": "Heading",
                    "min": -36,
                    "max": 36,
                    "minPos": [0,0],
                    "maxPos": [1,0]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\TargetDistanceMissile,
                "TargetDistanceMissile": {
                    "type": "rotational",
                    "source": "targetDist",
                    "center": [0,0],
                    "min": 100,
                    "max": 3000,
                    "minAngle": -120,
                    "maxAngle": 120
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\vspeed,
                "vspeed": {
                    "source": "vspeed",
                    "type": "linear",
                    "min": -30,
                    "max": 30,
                    "minPos": [0,0.06],
                    "maxPos": [0,0.3]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\HorizonBankMGun,
                "HorizonBankMGun": {
                    "type": "rotational",
                    "source": "HorizonBank",
                    "center": [0,0],
                    "min": -6.28319,
                    "max": 6.28319,
                    "minAngle": -360,
                    "maxAngle": 360,
                    "aspectRatio": 0.885246
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\HorizonDive,
                "HorizonDive": {
                    "source": "horizonDive",
                    "type": "linear",
                    "min": -1,
                    "max": 1,
                    "minPos": [0.502,2.49],
                    "maxPos": [0.502,-1.51]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\HorizonBankReverted,
                "HorizonBankReverted": {
                    "center": [0.5,0.6016],
                    "type": "rotational",
                    "source": "HorizonBank",
                    "min": "-3.14159265*2",
                    "max": "3.14159265*2",
                    "minAngle": 360,
                    "maxAngle": -360,
                    "aspectRatio": 0.8
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\Level0,
                "Level0": {
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelP5,
                "LevelP5": {
                    "angle": 5,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelM5,
                "LevelM5": {
                    "angle": -5,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelP10,
                "LevelP10": {
                    "angle": 10,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelM10,
                "LevelM10": {
                    "angle": -10,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelP15,
                "LevelP15": {
                    "angle": 15,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelM15,
                "LevelM15": {
                    "angle": -15,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelP20,
                "LevelP20": {
                    "angle": 20,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelM20,
                "LevelM20": {
                    "angle": -20,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelP25,
                "LevelP25": {
                    "angle": 25,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelM25,
                "LevelM25": {
                    "angle": -25,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelP30,
                "LevelP30": {
                    "angle": 30,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelM30,
                "LevelM30": {
                    "angle": -30,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelP35,
                "LevelP35": {
                    "angle": 35,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelM35,
                "LevelM35": {
                    "angle": -35,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelP40,
                "LevelP40": {
                    "angle": 40,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelM40,
                "LevelM40": {
                    "angle": -40,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelP45,
                "LevelP45": {
                    "angle": 45,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Bones\LevelM45,
                "LevelM45": {
                    "angle": -45,
                    "pos0": [0.5,0.58],
                    "pos10": [1.384,1.3652],
                    "type": "horizon"
                }
            },
            # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw,
            "Draw": {
                "alpha": 0.95,
                "color": [0,0.3,0.05],
                "condition": "on",
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\MGunD,
                "MGunD": {
                    "condition": "mgun+rocket+bomb",
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\MGunD\Cross,
                    "Cross": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0269716],1],["ImpactPoint",[0,-0.0359621],1],[],["ImpactPoint",[0.02,-0.024],1],["ImpactPoint",[0.025,-0.031],1],[],["ImpactPoint",[0,-0.002],1],["ImpactPoint",[0,0.002],1],[],["ImpactPoint",[-0.002,0],1],["ImpactPoint",[0.002,0],1],[]]
                    },
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\MGunD\Circle,
                    "Circle": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0314669],1],["MissileFlightTimeRot1",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot18",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot19",[0,0.035],1,"ImpactPoint",1],["MissileFlightTimeRot20",[0,0.035],1,"ImpactPoint",1]]
                    },
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\MGunD\Circle_Min_Range,
                    "Circle_Min_Range": {
                        "type": "line",
                        "width": 3,
                        "points": [["ImpactPoint",[0,-0.0269716],1],["ImpactPoint",[0.005208,-0.0265616],1],["ImpactPoint",[0.01026,-0.0253452],1],["ImpactPoint",[0.015,-0.0233574],1],["ImpactPoint",[0.019284,-0.0206603],1],["ImpactPoint",[0.02298,-0.0173373],1],["ImpactPoint",[0.02598,-0.0134858],1],["ImpactPoint",[0.028191,-0.00922429],1],["ImpactPoint",[0.029544,-0.00468227],1],["ImpactPoint",[0.03,0],1],["ImpactPoint",[0.029544,0.00468227],1],["ImpactPoint",[0.028191,0.00922429],1],["ImpactPoint",[0.02598,0.0134858],1],["ImpactPoint",[0.02298,0.0173373],1],["ImpactPoint",[0.019284,0.0206603],1],["ImpactPoint",[0.015,0.0233574],1],["ImpactPoint",[0.01026,0.0253452],1],["ImpactPoint",[0.005208,0.0265616],1],["ImpactPoint",[0,0.0269716],1],["ImpactPoint",[-0.005208,0.0265616],1],["ImpactPoint",[-0.01026,0.0253452],1],["ImpactPoint",[-0.015,0.0233574],1],["ImpactPoint",[-0.019284,0.0206603],1],["ImpactPoint",[-0.02298,0.0173373],1],["ImpactPoint",[-0.02598,0.0134858],1],["ImpactPoint",[-0.028191,0.00922429],1],["ImpactPoint",[-0.029544,0.00468227],1],["ImpactPoint",[-0.03,0],1],["ImpactPoint",[-0.029544,-0.00468227],1],["ImpactPoint",[-0.028191,-0.00922429],1],["ImpactPoint",[-0.02598,-0.0134858],1],["ImpactPoint",[-0.02298,-0.0173373],1],["ImpactPoint",[-0.019284,-0.0206603],1],["ImpactPoint",[-0.015,-0.0233574],1],["ImpactPoint",[-0.01026,-0.0253452],1],["ImpactPoint",[-0.005208,-0.0265616],1],["ImpactPoint",[0,-0.0269716],1]]
                    },
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\MGunD\Distance,
                    "Distance": {
                        "type": "text",
                        "source": "ImpactDistance",
                        "sourceScale": 0.001,
                        "sourcePrecision": 1,
                        "max": 15,
                        "align": "center",
                        "scale": 1,
                        "pos": ["ImpactPoint",[-0.002,-0.08],1],
                        "right": ["ImpactPoint",[0.045,-0.08],1],
                        "down": ["ImpactPoint",[-0.002,-0.04],1]
                    }
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Static2,
                "Static2": {
                    "clipTL": [0,0.5],
                    "clipBR": [1,0],
                    "points": [["PlaneW",[-0.21,"7.34351e-009--0.12"],1],["PlaneW",[-0.28,"9.79135e-009--0.12"],1],[],["PlaneW",[0.21,"-2.00338e-009--0.12"],1],["PlaneW",[0.28,"-2.67117e-009--0.12"],1],[],["PlaneW",[-0.105,"0.145492--0.12"],1],["PlaneW",[-0.14,"0.19399--0.12"],1],[],["PlaneW",[0.105,"0.145492--0.12"],1],["PlaneW",[0.14,"0.19399--0.12"],1],[],["PlaneW",[-0.181865,"0.084--0.12"],1],["PlaneW",[-0.242487,"0.112--0.12"],1],[],["PlaneW",[0.181865,"0.084--0.12"],1],["PlaneW",[0.242487,"0.112--0.12"],1],[],["PlaneW",[-0.202844,"0.0434816--0.12"],1],["PlaneW",[-0.270459,"0.0579755--0.12"],1],[],["PlaneW",[0.202844,"0.0434816--0.12"],1],["PlaneW",[0.270459,"0.0579755--0.12"],1],[],["PlaneW",[-0.209201,"0.0146422--0.12"],1],["PlaneW",[-0.244068,"0.0170825--0.12"],1],[],["PlaneW",[-0.20681,"0.0291729--0.12"],1],["PlaneW",[-0.241278,"0.034035--0.12"],1],[],["PlaneW",[0.20681,"0.0291729--0.12"],1],["PlaneW",[0.241278,"0.034035--0.12"],1],[],["PlaneW",[0.209201,"0.0146422--0.12"],1],["PlaneW",[0.244068,"0.0170825--0.12"],1],[]],
                    "type": "line"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\HorizonBank,
                "HorizonBank": {
                    "points": [["PlaneW",1,"HorizonBankReverted",["0.21-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.14-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.11-0.50","-0.035-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.08-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0.03-0.50","0-0.50"],1],[],["PlaneW",1,"HorizonBankReverted",["-0.21-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.14-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.11-0.50","-0.035-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.08-0.50","0-0.50"],1],["PlaneW",1,"HorizonBankReverted",["-0.03-0.50","0-0.50"],1],[],["PlaneW",1,"HorizonBankReverted",["0-0.50","-0.004-0.50"],1],["PlaneW",1,"HorizonBankReverted",["0-0.50","0.004-0.50"],1]],
                    "type": "line"
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\CollectiveGroup,
                "CollectiveGroup": {
                    "condition": "simulRTD",
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\CollectiveGroup\CollectiveText,
                    "CollectiveText": {
                        "type": "text",
                        "source": "static",
                        "text": "%",
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.2,0.2],1],
                        "right": [[0.26,0.2],1],
                        "down": [[0.2,0.25],1]
                    },
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\CollectiveGroup\CollectiveNumber,
                    "CollectiveNumber": {
                        "type": "text",
                        "source": "rtdCollective",
                        "sourceScale": 100,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.2,0.2],1],
                        "right": [[0.26,0.2],1],
                        "down": [[0.2,0.25],1]
                    }
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont,
                "Horizont": {
                    "clipTL": [0.25,0.25],
                    "clipBR": [0.75,0.75],
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed,
                    "Dimmed": {
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\Level0
                        "Level0": {
                            "type": "line",
                            "width": 4,
                            "points": [["Level0",[-0.28,0],1],["Level0",[-0.175,0],1],[],["Level0",[-0.063,0],1],["Level0",[-0.007,0],1],[],["Level0",[0.007,0],1],["Level0",[0.063,0],1],[],["Level0",[0.175,0],1],["Level0",[0.28,0],1]]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM5,
                        "LevelM5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.32,0],1],["LevelM5",[-0.22,0],1],[],["LevelM5",[0.22,0],1],["LevelM5",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_5,
                        "VALM_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM5",[-0.21,-0.021],1],
                            "right": ["LevelM5",[-0.15,-0.021],1],
                            "down": ["LevelM5",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_5L,
                        "VALM_1_5L": {
                            "align": "left",
                            "pos": ["LevelM5",[0.21,-0.021],1],
                            "right": ["LevelM5",[0.27,-0.021],1],
                            "down": ["LevelM5",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP5,
                        "LevelP5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.32,0],1],["LevelP5",[-0.22,0],1],[],["LevelP5",[0.22,0],1],["LevelP5",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_5,
                        "VALP_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP5",[-0.21,-0.021],1],
                            "right": ["LevelP5",[-0.15,-0.021],1],
                            "down": ["LevelP5",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_5L,
                        "VALP_1_5L": {
                            "align": "left",
                            "pos": ["LevelP5",[0.21,-0.021],1],
                            "right": ["LevelP5",[0.27,-0.021],1],
                            "down": ["LevelP5",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM10,
                        "LevelM10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.32,0],1],["LevelM10",[-0.22,0],1],[],["LevelM10",[0.22,0],1],["LevelM10",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_10,
                        "VALM_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM10",[-0.21,-0.021],1],
                            "right": ["LevelM10",[-0.15,-0.021],1],
                            "down": ["LevelM10",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_10L,
                        "VALM_1_10L": {
                            "align": "left",
                            "pos": ["LevelM10",[0.21,-0.021],1],
                            "right": ["LevelM10",[0.27,-0.021],1],
                            "down": ["LevelM10",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP10,
                        "LevelP10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.32,0],1],["LevelP10",[-0.22,0],1],[],["LevelP10",[0.22,0],1],["LevelP10",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_10,
                        "VALP_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP10",[-0.21,-0.021],1],
                            "right": ["LevelP10",[-0.15,-0.021],1],
                            "down": ["LevelP10",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_10L,
                        "VALP_1_10L": {
                            "align": "left",
                            "pos": ["LevelP10",[0.21,-0.021],1],
                            "right": ["LevelP10",[0.27,-0.021],1],
                            "down": ["LevelP10",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM15,
                        "LevelM15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.32,0],1],["LevelM15",[-0.22,0],1],[],["LevelM15",[0.22,0],1],["LevelM15",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_15,
                        "VALM_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM15",[-0.21,-0.021],1],
                            "right": ["LevelM15",[-0.15,-0.021],1],
                            "down": ["LevelM15",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_15L,
                        "VALM_1_15L": {
                            "align": "left",
                            "pos": ["LevelM15",[0.21,-0.021],1],
                            "right": ["LevelM15",[0.27,-0.021],1],
                            "down": ["LevelM15",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP15,
                        "LevelP15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.32,0],1],["LevelP15",[-0.22,0],1],[],["LevelP15",[0.22,0],1],["LevelP15",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_15,
                        "VALP_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP15",[-0.21,-0.021],1],
                            "right": ["LevelP15",[-0.15,-0.021],1],
                            "down": ["LevelP15",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_15L,
                        "VALP_1_15L": {
                            "align": "left",
                            "pos": ["LevelP15",[0.21,-0.021],1],
                            "right": ["LevelP15",[0.27,-0.021],1],
                            "down": ["LevelP15",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM20,
                        "LevelM20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.32,0],1],["LevelM20",[-0.22,0],1],[],["LevelM20",[0.22,0],1],["LevelM20",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_20,
                        "VALM_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM20",[-0.21,-0.021],1],
                            "right": ["LevelM20",[-0.15,-0.021],1],
                            "down": ["LevelM20",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_20L,
                        "VALM_1_20L": {
                            "align": "left",
                            "pos": ["LevelM20",[0.21,-0.021],1],
                            "right": ["LevelM20",[0.27,-0.021],1],
                            "down": ["LevelM20",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP20,
                        "LevelP20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.32,0],1],["LevelP20",[-0.22,0],1],[],["LevelP20",[0.22,0],1],["LevelP20",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_20,
                        "VALP_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP20",[-0.21,-0.021],1],
                            "right": ["LevelP20",[-0.15,-0.021],1],
                            "down": ["LevelP20",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_20L,
                        "VALP_1_20L": {
                            "align": "left",
                            "pos": ["LevelP20",[0.21,-0.021],1],
                            "right": ["LevelP20",[0.27,-0.021],1],
                            "down": ["LevelP20",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM25,
                        "LevelM25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.32,0],1],["LevelM25",[-0.22,0],1],[],["LevelM25",[0.22,0],1],["LevelM25",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_25,
                        "VALM_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM25",[-0.21,-0.021],1],
                            "right": ["LevelM25",[-0.15,-0.021],1],
                            "down": ["LevelM25",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_25L,
                        "VALM_1_25L": {
                            "align": "left",
                            "pos": ["LevelM25",[0.21,-0.021],1],
                            "right": ["LevelM25",[0.27,-0.021],1],
                            "down": ["LevelM25",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP25,
                        "LevelP25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.32,0],1],["LevelP25",[-0.22,0],1],[],["LevelP25",[0.22,0],1],["LevelP25",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_25,
                        "VALP_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP25",[-0.21,-0.021],1],
                            "right": ["LevelP25",[-0.15,-0.021],1],
                            "down": ["LevelP25",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_25L,
                        "VALP_1_25L": {
                            "align": "left",
                            "pos": ["LevelP25",[0.21,-0.021],1],
                            "right": ["LevelP25",[0.27,-0.021],1],
                            "down": ["LevelP25",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM30,
                        "LevelM30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.32,0],1],["LevelM30",[-0.22,0],1],[],["LevelM30",[0.22,0],1],["LevelM30",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_30,
                        "VALM_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM30",[-0.21,-0.021],1],
                            "right": ["LevelM30",[-0.15,-0.021],1],
                            "down": ["LevelM30",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_30L,
                        "VALM_1_30L": {
                            "align": "left",
                            "pos": ["LevelM30",[0.21,-0.021],1],
                            "right": ["LevelM30",[0.27,-0.021],1],
                            "down": ["LevelM30",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP30,
                        "LevelP30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.32,0],1],["LevelP30",[-0.22,0],1],[],["LevelP30",[0.22,0],1],["LevelP30",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_30,
                        "VALP_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP30",[-0.21,-0.021],1],
                            "right": ["LevelP30",[-0.15,-0.021],1],
                            "down": ["LevelP30",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_30L,
                        "VALP_1_30L": {
                            "align": "left",
                            "pos": ["LevelP30",[0.21,-0.021],1],
                            "right": ["LevelP30",[0.27,-0.021],1],
                            "down": ["LevelP30",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM35,
                        "LevelM35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.32,0],1],["LevelM35",[-0.22,0],1],[],["LevelM35",[0.22,0],1],["LevelM35",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_35,
                        "VALM_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM35",[-0.21,-0.021],1],
                            "right": ["LevelM35",[-0.15,-0.021],1],
                            "down": ["LevelM35",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_35L,
                        "VALM_1_35L": {
                            "align": "left",
                            "pos": ["LevelM35",[0.21,-0.021],1],
                            "right": ["LevelM35",[0.27,-0.021],1],
                            "down": ["LevelM35",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP35,
                        "LevelP35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.32,0],1],["LevelP35",[-0.22,0],1],[],["LevelP35",[0.22,0],1],["LevelP35",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_35,
                        "VALP_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP35",[-0.21,-0.021],1],
                            "right": ["LevelP35",[-0.15,-0.021],1],
                            "down": ["LevelP35",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_35L,
                        "VALP_1_35L": {
                            "align": "left",
                            "pos": ["LevelP35",[0.21,-0.021],1],
                            "right": ["LevelP35",[0.27,-0.021],1],
                            "down": ["LevelP35",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM40,
                        "LevelM40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.32,0],1],["LevelM40",[-0.22,0],1],[],["LevelM40",[0.22,0],1],["LevelM40",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_40,
                        "VALM_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM40",[-0.21,-0.021],1],
                            "right": ["LevelM40",[-0.15,-0.021],1],
                            "down": ["LevelM40",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_40L,
                        "VALM_1_40L": {
                            "align": "left",
                            "pos": ["LevelM40",[0.21,-0.021],1],
                            "right": ["LevelM40",[0.27,-0.021],1],
                            "down": ["LevelM40",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP40,
                        "LevelP40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.32,0],1],["LevelP40",[-0.22,0],1],[],["LevelP40",[0.22,0],1],["LevelP40",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_40,
                        "VALP_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP40",[-0.21,-0.021],1],
                            "right": ["LevelP40",[-0.15,-0.021],1],
                            "down": ["LevelP40",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_40L,
                        "VALP_1_40L": {
                            "align": "left",
                            "pos": ["LevelP40",[0.21,-0.021],1],
                            "right": ["LevelP40",[0.27,-0.021],1],
                            "down": ["LevelP40",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM45,
                        "LevelM45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.32,0],1],["LevelM45",[-0.22,0],1],[],["LevelM45",[0.22,0],1],["LevelM45",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_45,
                        "VALM_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM45",[-0.21,-0.021],1],
                            "right": ["LevelM45",[-0.15,-0.021],1],
                            "down": ["LevelM45",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_45L,
                        "VALM_1_45L": {
                            "align": "left",
                            "pos": ["LevelM45",[0.21,-0.021],1],
                            "right": ["LevelM45",[0.27,-0.021],1],
                            "down": ["LevelM45",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "scale": 1,
                            "sourceScale": 1
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP45,
                        "LevelP45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.32,0],1],["LevelP45",[-0.22,0],1],[],["LevelP45",[0.22,0],1],["LevelP45",[0.32,0],1]],
                            "width": 4
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_45,
                        "VALP_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP45",[-0.21,-0.021],1],
                            "right": ["LevelP45",[-0.15,-0.021],1],
                            "down": ["LevelP45",[-0.21,0.024],1]
                        },
                        # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_45L,
                        "VALP_1_45L": {
                            "align": "left",
                            "pos": ["LevelP45",[0.21,-0.021],1],
                            "right": ["LevelP45",[0.27,-0.021],1],
                            "down": ["LevelP45",[0.21,0.024],1],
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "scale": 1,
                            "sourceScale": 1
                        }
                    }
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\Static,
                "Static": {
                    "type": "line",
                    "width": 4,
                    "points": [["vspeed",[0.22,0.56],1],["vspeed",[0.205,0.55],1],["vspeed",[0.22,0.54],1],["vspeed",[0.22,0.56],1],[],[[0.2,0.598],1],[[0.2,0.782],1],[],[[0.2,0.61],1],[[0.18,0.61],1],[],[[0.195,0.77],1],[[0.18,0.77],1],[],[[0.195,0.65],1],[[0.18,0.65],1],[],[[0.195,0.69],1],[[0.18,0.69],1],[],[[0.195,0.73],1],[[0.18,0.73],1],[],["vspeed",[0.78,0.56],1],["vspeed",[0.795,0.55],1],["vspeed",[0.78,0.54],1],["vspeed",[0.78,0.56],1],[],[[0.8,0.598],1],[[0.8,0.862],1],[],[[0.8,0.61],1],[[0.83,0.61],1],[],[[0.805,0.85],1],[[0.83,0.85],1],[],[[0.805,0.65],1],[[0.82,0.65],1],[],[[0.805,0.69],1],[[0.82,0.69],1],[],[[0.805,0.73],1],[[0.83,0.73],1],[],[[0.805,0.77],1],[[0.82,0.77],1],[],[[0.805,0.81],1],[[0.82,0.81],1],[],[[0.52,0.14],1],[[0.5,0.12],1],[[0.48,0.14],1],[],[[0.3,0.115],1],[[0.7,0.115],1],[]]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\SpeedGroup,
                "SpeedGroup": {
                    "condition": "speed-2.78",
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\SpeedGroup\Static,
                    "Static": {
                        "type": "line",
                        "width": 4,
                        "points": [["SliderSpeedSource",["0.015-0.03",0.01],1],["SliderSpeedSource",["0.000-0.03",0],1],["SliderSpeedSource",["0.015-0.03",-0.01],1],["SliderSpeedSource",["0.015-0.03",0.01],1],[],[["0.25-0.03",0.2],1],[["0.25-0.03",0.525],1],[],[["0.25-0.03",0.2],1],[["0.23-0.03",0.2],1],[],[["0.24-0.03",0.265],1],[["0.23-0.03",0.265],1],[],[["0.24-0.03",0.33],1],[["0.23-0.03",0.33],1],[],[["0.24-0.03",0.395],1],[["0.23-0.03",0.395],1],[],[["0.24-0.03",0.46],1],[["0.23-0.03",0.46],1],[],[["0.25-0.03",0.525],1],[["0.23-0.03",0.525],1],[]]
                    },
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\SpeedGroup\SpeedStatic500,
                    "SpeedStatic500": {
                        "type": "text",
                        "source": "static",
                        "text": "500",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [["0.220-0.03",0.183],1],
                        "right": [[0.23,0.183],1],
                        "down": [["0.220-0.03",0.213],1]
                    },
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\SpeedGroup\SpeedStatic0,
                    "SpeedStatic0": {
                        "type": "text",
                        "source": "static",
                        "text": "0",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "left",
                        "pos": [["0.220-0.03",0.508],1],
                        "right": [[0.23,0.508],1],
                        "down": [["0.220-0.03",0.538],1]
                    }
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\AGL_Radar,
                "AGL_Radar": {
                    "condition": "50-altitudeAGL",
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\AGL_Radar\Panel,
                    "Panel": {
                        "width": 4,
                        "type": "line",
                        "points": [["AGLMove",[0.73,0.11],1],["AGLMove",[0.745,0.1],1],["AGLMove",[0.73,0.09],1],["AGLMove",[0.73,0.11],1],[],[[0.75,0.1975],1],[[0.75,0.5225],1],[],[[0.75,0.1975],1],[[0.77,0.1975],1],[],[[0.725,0.5225],1],[[0.775,0.5225],1],[],[[0.755,0.2625],1],[[0.77,0.2625],1],[],[[0.755,0.3275],1],[[0.77,0.3275],1],[],[[0.755,0.3925],1],[[0.77,0.3925],1],[],[[0.755,0.4575],1],[[0.77,0.4575],1],[]]
                    },
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\AGL_Radar\AltStatic50,
                    "AltStatic50": {
                        "type": "text",
                        "source": "static",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "right",
                        "text": 50,
                        "pos": [[0.79,0.17],1],
                        "right": [[0.83,0.17],1],
                        "down": [[0.79,0.205],1]
                    }
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\RadarBoxes,
                "RadarBoxes": {
                    "type": "radar",
                    "pos0": [0.5,0.39],
                    "pos10": [1.134,0.96],
                    "width": 4,
                    "points": [[[-0.002,-0.00179811],1],[[0.002,-0.00179811],1],[[0.002,0.00179811],1],[[-0.002,0.00179811],1],[[-0.002,-0.00179811],1]]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\TargetDiamond,
                "TargetDiamond": {
                    # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\TargetDiamond\shape
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0.02,0.0179811],1],["Target",1,"Limit0109",1,[-0.02,0.0179811],1],["Target",1,"Limit0109",1,[-0.02,-0.0179811],1],["Target",1,"Limit0109",1,[0.02,-0.0179811],1],["Target",1,"Limit0109",1,[0.02,0.0179811],1]]
                    }
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\SpeedNumber,
                "SpeedNumber": {
                    "type": "text",
                    "align": "right",
                    "source": "speed",
                    "sourceScale": 3.6,
                    "sourceLength": 3,
                    "scale": 1,
                    "pos": [[0.07,0.07],1],
                    "right": [[0.15,0.07],1],
                    "down": [[0.07,0.12],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\AltNumber,
                "AltNumber": {
                    "source": "altitudeAGL",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "sourceOffset": -2,
                    "align": "right",
                    "pos": [[0.76,0.07],1],
                    "right": [[0.84,0.07],1],
                    "down": [[0.76,0.12],1],
                    "type": "text",
                    "scale": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\AltNumberStatic,
                "AltNumberStatic": {
                    "type": "text",
                    "source": "static",
                    "align": "right",
                    "text": "р",
                    "scale": 1,
                    "sourceScale": 1,
                    "pos": [[0.88,0.09],1],
                    "right": [[0.93,0.09],1],
                    "down": [[0.88,0.13],1],
                    "sourceLength": 3,
                    "sourceOffset": -2
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\VspeedNumber,
                "VspeedNumber": {
                    "source": "vspeed",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "align": "left",
                    "pos": [[0.81,0.55],1],
                    "right": [[0.89,0.55],1],
                    "down": [[0.81,0.6],1],
                    "type": "text",
                    "scale": 1
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\VspeedNumberStaticP30,
                "VspeedNumberStaticP30": {
                    "type": "text",
                    "source": "static",
                    "text": "+30",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.835,0.59],1],
                    "right": [[0.885,0.59],1],
                    "down": [[0.835,0.63],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\VspeedNumberStaticZERO,
                "VspeedNumberStaticZERO": {
                    "type": "text",
                    "source": "static",
                    "text": "0",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.835,0.71],1],
                    "right": [[0.885,0.71],1],
                    "down": [[0.835,0.75],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\VspeedNumberStaticM30,
                "VspeedNumberStaticM30": {
                    "type": "text",
                    "source": "static",
                    "text": "-30",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.835,0.83],1],
                    "right": [[0.885,0.83],1],
                    "down": [[0.835,0.87],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\NevimStatic3,
                "NevimStatic3": {
                    "type": "text",
                    "source": "static",
                    "text": "3",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.14,0.59],1],
                    "right": [[0.19,0.59],1],
                    "down": [[0.14,0.63],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\NevimStaticZERO,
                "NevimStaticZERO": {
                    "type": "text",
                    "source": "static",
                    "text": "0",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.14,0.71],1],
                    "right": [[0.19,0.71],1],
                    "down": [[0.14,0.75],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\NevimStatic1,
                "NevimStatic1": {
                    "type": "text",
                    "source": "static",
                    "text": "1",
                    "scale": 1,
                    "sourceScale": 1,
                    "align": "right",
                    "pos": [[0.14,0.75],1],
                    "right": [[0.19,0.75],1],
                    "down": [[0.14,0.79],1]
                },
                # Class: CfgVehicles\RHS_Ka52_base\MFD\AirplaneHUD\Draw\HeadingScale,
                "HeadingScale": {
                    "type": "scale",
                    "source": "heading",
                    "horizontal": 1,
                    "sourceScale": 0.1,
                    "width": 4,
                    "top": 0.3,
                    "center": 0.5,
                    "bottom": 0.7,
                    "lineXleft": 0.11,
                    "lineYright": 0.1,
                    "lineXleftMajor": 0.11,
                    "lineYrightMajor": 0.09,
                    "majorLineEach": 2,
                    "numberEach": 2,
                    "step": 0.5,
                    "stepSize": 0.0555556,
                    "align": "center",
                    "scale": 1,
                    "pos": ["0.32-0.01","0.0+0.05"],
                    "right": ["0.38-0.01","0.0+0.05"],
                    "down": ["0.32-0.01","0.04+0.05"]
                }
            }
        }
    },
    # Class: CfgVehicles\RHS_Ka52_base\EventHandlers,
    "EventHandlers": {
        "hit": "",
        # Class: CfgVehicles\RHS_Ka52_base\EventHandlers\RHS_EventHandlers,
        "RHS_EventHandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "init": "_this call rhs_fnc_air_init",
            "getout": "_this spawn rhs_fnc_ka52_ejection",
            "engine": "_this call rhs_fnc_addParachutes;"
        },
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "init": "",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "features": "Randomization: No						<br />Camo selections: 2 - main body, turret with engines and wings						<br />Script door sources: door_L, door_R, door_L_pop, door_R_pop						<br />Script animations: None 						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: No						<br />Cargo proxy indexes: 1 to 8",
    # Class: CfgVehicles\Heli_Attack_02_base_F\SpeechVariants,
    "SpeechVariants": {
        # Class: CfgVehicles\Heli_Attack_02_base_F\SpeechVariants\Default
        "Default": {
            "speechSingular": ["veh_air_gunship_s"],
            "speechPlural": ["veh_air_gunship_p"]
        }
    },
    "textSingular": "gunship",
    "textPlural": "gunships",
    "nameSound": "veh_air_gunship_s",
    "_generalMacro": "Heli_Attack_02_base_F",
    "fuelConsumptionRate": 0.138,
    "altFullForce": 4000,
    "altNoForce": 6000,
    "crewVulnerable": 0,
    # Class: CfgVehicles\Heli_Attack_02_base_F\Library,
    "Library": {
        "libTextDesc": "A multi-purpose successor to the Mi-24, the Mi-48 Kajman (BLUFOR designation `Hornet`) is a large gunship and attack helicopter with troop transport capacity for 8 passengers. The front part of the helicopter is based on the Mi-28 attack helicopter, but the hull is modified for passenger transport. The Kajman has a coaxial rotor providing increased stability. It is armed with a 30mm three-barrel Minigun, unguided Skyfire rockets and guided Skalpel AT missiles."
    },
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "maxFordingDepth": 0.75,
    "tailBladeVertical": 0,
    "supplyRadius": 2.5,
    "maximumLoad": 2000,
    "cargoCanEject": 1,
    "cost": 3e+006,
    "showAllTargets": 4,
    "cargoAction": ["passenger_generic01_leanleft","passenger_generic01_foldhands","passenger_generic01_leanright","passenger_generic01_leanleft","passenger_generic01_leanright","passenger_generic01_leanleft","passenger_generic01_foldhands","passenger_generic01_leanleft"],
    "cargoDoors": [],
    "memoryPointDriverOptics": "PilotCamera_pos",
    "driverWeaponsInfoType": "RscOptics_Heli_Attack_02_pilot",
    "attenuationEffectType": "HeliAttenuation",
    "emptySound": ["",0,1],
    "soundGeneralCollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_1",3.16228,1,500],
    "soundGeneralCollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_2",3.16228,1,500],
    "soundGeneralCollision3": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_default_int_3",3.16228,1,500],
    "soundCrashes": ["soundGeneralCollision1",0.33,"soundGeneralCollision2",0.33,"soundGeneralCollision3",0.33],
    "soundLandCrashes": ["emptySound",0],
    "soundBuildingCrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundArmorCrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundWoodCrash": ["soundGeneralCollision1",1,"soundGeneralCollision2",1,"soundGeneralCollision3",1],
    "soundBushCollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_1",3.16228,1,500],
    "soundBushCollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_2",3.16228,1,500],
    "soundBushCollision3": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_bush_int_3",3.16228,1,500],
    "soundBushCrash": ["soundBushCollision1",0.33,"soundBushCollision2",0.33,"soundBushCollision3",0.33],
    "soundWaterCollision1": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_water_ext_1",3.16228,1,300],
    "soundWaterCollision2": ["A3|Sounds_F|vehicles|crashes|helis|Heli_coll_water_ext_2",3.16228,1,300],
    "soundWaterCrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "soundDammage": ["A3|Sounds_F|vehicles|crashes|helis|Heli_crash_default_int_1",10,1],
    "soundGetIn": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_door",1,1],
    "soundGetOut": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_door",1,1,50],
    "soundEngineOnInt": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_start2",0.158489,1],
    "soundEngineOnExt": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_start2",0.794328,1,600],
    "soundEngineOffInt": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_stop2",0.199526,1],
    "soundEngineOffExt": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_stop2",0.794328,1,600],
    "soundLocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",1,1],
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_4",0.398107,1],
    "rotorDamageInt": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_int_2",1,1],
    "rotorDamageOut": ["A3|Sounds_F|vehicles|air|noises|heli_damage_rotor_ext_2",2.51189,1,300],
    "rotorDamage": ["rotorDamageInt","rotorDamageOut"],
    "tailDamageInt": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1],
    "tailDamageOut": ["A3|Sounds_F|vehicles|air|noises|heli_damage_tail",1,1,300],
    "tailDamage": ["tailDamageInt","tailDamageOut"],
    "landingSoundInt0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int1",1,1,100],
    "landingSoundInt1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int2",1,1,100],
    "landingSoundInt": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingSoundOut0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext1",5.62341,1,500],
    "landingSoundOut1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext2",5.62341,1,500],
    "landingSoundOut": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    "slingCargoAttach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEndINT",1,1],
    "slingCargoAttach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookLock",1.77828,1,200],
    "slingCargoAttach": ["slingCargoAttach0","slingCargoAttach1"],
    "slingCargoDetach0": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEndINT",1,1],
    "slingCargoDetach1": ["A3|Sounds_F|vehicles|air|noises|SL_1hookUnlock",1.77828,1,200],
    "slingCargoDetach": ["slingCargoDetach0","slingCargoDetach1"],
    "slingCargoDetachAir0": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_int",1,1],
    "slingCargoDetachAir1": ["A3|Sounds_F|vehicles|air|noises|SL_unhook_air_ext",1,1,300],
    "slingCargoDetachAir": ["slingCargoDetach0","slingCargoDetach1"],
    "slingCargoRopeBreak0": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_int",1,1],
    "slingCargoRopeBreak1": ["A3|Sounds_F|vehicles|air|noises|SL_rope_break_ext",1,1,200],
    "slingCargoRopeBreak": ["slingCargoDetach0","slingCargoDetach1"],
    # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds,
    "Sounds": {
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\EngineExt
        "EngineExt": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_engine",1.77828,1,900],
            "frequency": "rotorSpeed",
            "volume": "camPos*((rotorSpeed-0.72)*4)"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\RotorExt,
        "RotorExt": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_rotor",1.12202,1,2000],
            "frequency": "rotorSpeed*(1-rotorThrust/8)*1.2",
            "volume": "2*camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)",
            "cone": [1.6,3.14,1.6,0.95]
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\RotorNoiseExt,
        "RotorNoiseExt": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|rotor_swist",1,1,400],
            "frequency": 1,
            "volume": "camPos * (rotorThrust factor [0.7, 0.9])",
            "cone": [0.7,1.3,1,0]
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\EngineInt,
        "EngineInt": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_engine",1.12202,1],
            "frequency": "rotorSpeed",
            "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\RotorInt,
        "RotorInt": {
            "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_rotor",0.891251,1],
            "frequency": "rotorSpeed*(1-rotorThrust/8)*1.2",
            "volume": "(1-camPos)*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\TransmissionDamageExt_phase1,
        "TransmissionDamageExt_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\TransmissionDamageExt_phase2,
        "TransmissionDamageExt_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\TransmissionDamageInt_phase1,
        "TransmissionDamageInt_phase1": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\TransmissionDamageInt_phase2,
        "TransmissionDamageInt_phase2": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
            "frequency": "0.66 + rotorSpeed / 3",
            "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\damageAlarmInt,
        "damageAlarmInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\damageAlarmExt,
        "damageAlarmExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\rotorLowAlarmInt,
        "rotorLowAlarmInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
            "frequency": 1,
            "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\rotorLowAlarmExt,
        "rotorLowAlarmExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
            "frequency": 1,
            "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\scrubLandInt,
        "scrubLandInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
            "frequency": 1,
            "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\scrubLandExt,
        "scrubLandExt": {
            "sound": ["A3|Sounds_F|dummysound",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\scrubBuildingInt,
        "scrubBuildingInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos) * (scrubBuilding factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\scrubBuildingExt,
        "scrubBuildingExt": {
            "sound": ["A3|Sounds_F|dummysound",1,1,100],
            "frequency": 1,
            "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\scrubTreeInt,
        "scrubTreeInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeInt",1,1,100],
            "frequency": 1,
            "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\scrubTreeExt,
        "scrubTreeExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
            "frequency": 1,
            "volume": "camPos * ((scrubTree) factor [0, 0.01])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\RainExt,
        "RainExt": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
            "frequency": 1,
            "volume": "camPos * (rain - rotorSpeed/2) * 2"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\RainInt,
        "RainInt": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\SlingLoadDownExt,
        "SlingLoadDownExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1.25893,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\SlingLoadUpExt,
        "SlingLoadUpExt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1.25893,1,500],
            "frequency": 1,
            "volume": "camPos*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\SlingLoadDownInt,
        "SlingLoadDownInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\SlingLoadUpInt,
        "SlingLoadUpInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
            "frequency": 1,
            "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\WindInt,
        "WindInt": {
            "sound": ["A3|Sounds_F|vehicles|air|noises|wind_closed",0.562341,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\GStress,
        "GStress": {
            "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2e",0.501187,1,50],
            "frequency": 1,
            "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Sounds\SpeedStress,
        "SpeedStress": {
            "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress3",1,1,50],
            "frequency": 1,
            "volume": "(1-camPos)*(speed factor[40,60])"
        }
    },
    # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt,
    "SoundsExt": {
        # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\SoundEvents
        "SoundEvents": {
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds,
        "Sounds": {
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\EngineExt
            "EngineExt": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_engine",1.77828,1,900],
                "frequency": "rotorSpeed",
                "volume": "camPos*((rotorSpeed-0.72)*4)"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\RotorExt,
            "RotorExt": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_ext_rotor",1.12202,1,2000],
                "frequency": "rotorSpeed*(1-rotorThrust/8)*1.2",
                "volume": "2*camPos*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)",
                "cone": [1.6,3.14,1.6,0.95]
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\RotorNoiseExt,
            "RotorNoiseExt": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|rotor_swist",1,1,400],
                "frequency": 1,
                "volume": "camPos * (rotorThrust factor [0.7, 0.9])",
                "cone": [0.7,1.3,1,0]
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\EngineInt,
            "EngineInt": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_engine",1.12202,1],
                "frequency": "rotorSpeed",
                "volume": "(1-camPos)*((rotorSpeed-0.75)*4)"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\RotorInt,
            "RotorInt": {
                "sound": ["A3|Sounds_F|vehicles|air|Heli_Attack_02|Mixxx_int_rotor",0.891251,1],
                "frequency": "rotorSpeed*(1-rotorThrust/8)*1.2",
                "volume": "(1-camPos)*(0 max (rotorSpeed-0.1))*(1 + rotorThrust)"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\TransmissionDamageExt_phase1,
            "TransmissionDamageExt_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\TransmissionDamageExt_phase2,
            "TransmissionDamageExt_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_ext_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "camPos * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\TransmissionDamageInt_phase1,
            "TransmissionDamageInt_phase1": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_1",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.3, 0.35]) * (transmissionDamage factor [0.5, 0.45]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\TransmissionDamageInt_phase2,
            "TransmissionDamageInt_phase2": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_damage_transmission_int_2",1,1,150],
                "frequency": "0.66 + rotorSpeed / 3",
                "volume": "(1 - camPos) * (transmissionDamage factor [0.45, 0.5]) * (rotorSpeed factor [0.2, 0.5])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\damageAlarmInt,
            "damageAlarmInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0.0, 0.001])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\damageAlarmExt,
            "damageAlarmExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_opfor",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * ( 1 - ((transmissionDamage factor [0.61, 0.60]) * (motorDamage factor [0.61, 0.60]) * (rotorDamage factor [0.51, 0.50]))) * (rotorSpeed factor [0, 0.001])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\rotorLowAlarmInt,
            "rotorLowAlarmInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.316228,1],
                "frequency": 1,
                "volume": "engineOn * (1 - camPos) * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\rotorLowAlarmExt,
            "rotorLowAlarmExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|heli_alarm_rotor_low",0.223872,1,20],
                "frequency": 1,
                "volume": "engineOn * camPos * (rotorSpeed factor [0.9, 0.8999]) * (rotorSpeed factor [-0.5, 1]) * (speed factor [3, 3.01])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\scrubLandInt,
            "scrubLandInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
                "frequency": 1,
                "volume": "2 * (1-camPos) * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\scrubLandExt,
            "scrubLandExt": {
                "sound": ["A3|Sounds_F|dummysound",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubLand factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\scrubBuildingInt,
            "scrubBuildingInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos) * (scrubBuilding factor[0.02, 0.05]) * (1 - (lateralMovement factor [0.7,1]))"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\scrubBuildingExt,
            "scrubBuildingExt": {
                "sound": ["A3|Sounds_F|dummysound",1,1,100],
                "frequency": 1,
                "volume": "camPos * (scrubBuilding factor[0.02, 0.05])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\scrubTreeInt,
            "scrubTreeInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeInt",1,1,100],
                "frequency": 1,
                "volume": "(1 - camPos) * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\scrubTreeExt,
            "scrubTreeExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|scrubTreeExt",1,1,100],
                "frequency": 1,
                "volume": "camPos * ((scrubTree) factor [0, 0.01])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\RainExt,
            "RainExt": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1,1,100],
                "frequency": 1,
                "volume": "camPos * (rain - rotorSpeed/2) * 2"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\RainInt,
            "RainInt": {
                "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
                "frequency": 1,
                "volume": "(1-camPos)*(rain - rotorSpeed/2)*2"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\SlingLoadDownExt,
            "SlingLoadDownExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\SlingLoadUpExt,
            "SlingLoadUpExt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpEXT",1,1,500],
                "frequency": 1,
                "volume": "camPos*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\SlingLoadDownInt,
            "SlingLoadDownInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineDownINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,-1])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\SlingLoadUpInt,
            "SlingLoadUpInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|SL_engineUpINT",1,1,500],
                "frequency": 1,
                "volume": "(1-camPos)*(slingLoadActive factor [0,1])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\WindInt,
            "WindInt": {
                "sound": ["A3|Sounds_F|vehicles|air|noises|wind_closed",0.562341,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[5, 50])*(speed factor[5, 50])"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\GStress,
            "GStress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress2e",0.501187,1,50],
                "frequency": 1,
                "volume": "engineOn * (1-camPos) * ((gmeterZ factor[1.5, 2.5]) + (gmeterZ factor[0.5, -0.5]))"
            },
            # Class: CfgVehicles\Heli_Attack_02_base_F\SoundsExt\Sounds\SpeedStress,
            "SpeedStress": {
                "sound": ["A3|Sounds_F|vehicles|noises|vehicle_stress3",1,1,50],
                "frequency": 1,
                "volume": "(1-camPos)*(speed factor[40,60])"
            }
        }
    },
    # Class: CfgVehicles\Heli_Attack_02_base_F\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\Heli_Attack_02_base_F\Exhausts\Exhaust1
        "Exhaust1": {
            "position": "exhaust1",
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectHeliBig"
        },
        # Class: CfgVehicles\Heli_Attack_02_base_F\Exhausts\Exhaust2,
        "Exhaust2": {
            "position": "exhaust2",
            "direction": "exhaust2_dir",
            "effect": "ExhaustsEffectHeliBig"
        }
    },
    "defaultUserMFDvalues": [0.25,1,0.25,1],
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "washDownStrength": "1.0f",
    "washDownDiameter": "40.0f",
    "minSmokeDamage": 0.3,
    "maxSmokeDamage": 0.99,
    "driverLeftLegAnimName": "pedalL",
    "driverRightLegAnimName": "pedalR",
    # Class: CfgVehicles\Helicopter_Base_F\CamShake,
    "CamShake": {
        "power": 30,
        "frequency": 20,
        "distance": 50,
        "minSpeed": 50
    },
    "simulation": "helicopterrtd",
    "unitInfoTypeRTD": "RscUnitInfoAirRTDFullDigital",
    "unitInfoTypeLite": "RscUnitInfoAirRTDBasic",
    "dustEffect": "HeliDust",
    "waterEffect": "HeliWater",
    "gearUpTime": 3.33,
    "gearDownTime": 2,
    "gearMinAlt": 0.5,
    # Class: CfgVehicles\Helicopter\CargoSpec,
    "CargoSpec": {
        # Class: CfgVehicles\Helicopter\CargoSpec\Cargo1
        "Cargo1": {
            "showHeadPhones": 1
        },
        # Class: CfgVehicles\Helicopter\CargoSpec\Cargo2,
        "Cargo2": {
            "showHeadPhones": 0
        }
    },
    "startDuration": 20,
    "maxBackRotorDive": 0,
    "minBackRotorDive": 0,
    "neutralBackRotorDive": 0,
    "cyclicAsideForceCoef": 1,
    "memoryPointPilot": "pilot",
    "_mainBladeCenter": "rotor_center",
    "selectionFireAnim": "zasleh",
    "enableSweep": 1,
    "envelope": [0,0.2,0.9,2.1,2.5,3.3,3.5,3.6,3.7,3.8,3.8,3,0.9,0.7,0.5],
    "minFireTime": 20,
    "steerAheadSimul": 0.5,
    "steerAheadPlan": 0.7,
    "soundLandingGear": ["",1,1],
    "slingLoadMemoryPoint": "slingLoad0",
    "slingLoadMaxCargoMass": 0,
    "extCameraParams": [-1],
    "camouflage": 100,
    "audible": 50,
    "epeImpulseDamageCoef": 50,
    "crewCrashProtection": 0.25,
    "headGforceLeaningFactor": [0.01,0.0025,0.01],
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "damageEffect": "AirDestructionEffects",
    "type": 2,
    "transportMaxBackpacks": 1,
    "armorStructural": 4,
    "explosionShielding": 4,
    "minTotalDamageThreshold": 0.005,
    # Class: CfgVehicles\Helicopter\DestructionEffects,
    "DestructionEffects": {
    },
    "slingLoadMinCargoMass": 0,
    "formationX": 50,
    "formationZ": 100,
    "precision": 100,
    "brakeDistance": 200,
    "formationTime": 10,
    "gearsUpFrictionCoef": 0.5,
    "airBrakeFrictionCoef": 3,
    "airFrictionCoefs2": [0.001,0.0005,6e-005],
    "airFrictionCoefs1": [0.1,0.05,0.006],
    "airFrictionCoefs0": [0,0,0],
    "insideSoundCoef": 0.0316228,
    "outsideSoundFilter": 1,
    "occludeSoundsWhenIn": 0.316228,
    "obstructSoundsWhenIn": 0.316228,
    "irScanRangeMin": 2000,
    "irScanRangeMax": 10000,
    "irScanToEyeFactor": 2,
    "nightVision": 0,
    "cargoCompartments": [0],
    "transportMaxMagazines": 20,
    "transportMaxWeapons": 3,
    "enableGPS": 1,
    "weaponsGroup2": 4,
    "weaponsGroup3": "8 + 	16 + 	32",
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    "waterLeakiness": 100,
    "waterResistance": 1,
    "impactEffectsSea": "ImpactEffectsAir",
    "flareVelocity": 100,
    "enableRadio": 1,
    "memoryPointCM": ["flare_launcher1","flare_launcher2"],
    "memoryPointCMDir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "radarType": 4,
    "countermeasureActivationRadius": 10000,
    # Class: CfgVehicles\Air\camShakeGForce,
    "camShakeGForce": {
        "power": 0.2,
        "frequency": 3,
        "distance": 0,
        "minSpeed": 1
    },
    # Class: CfgVehicles\Air\camShakeDamage,
    "camShakeDamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minSpeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "minGForce": 0.2,
    "maxGForce": 2,
    "gForceShakeAttenuation": 0.5,
    "secondaryExplosion": -1,
    "fuelExplosionPower": 1,
    # Class: CfgVehicles\AllVehicles\SquadTitles,
    "SquadTitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memoryPointsGetInDriver": "pos driver",
    "memoryPointsGetInDriverDir": "pos driver dir",
    "memoryPointsGetInCargo": "pos cargo",
    "memoryPointsGetInCargoDir": "pos cargo dir",
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
    "selectionShowDamage": "poskozeni",
    "selectionBackLights": "zadni svetlo",
    # Class: CfgVehicles\AllVehicles\NewTurret,
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
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewGunner,
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
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
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
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
            # Class: WeaponFireGun\Table,
            "Table": {
                # Class: WeaponFireGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1,
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2,
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3,
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4,
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5,
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6,
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7,
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8,
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9,
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10,
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11,
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12,
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13,
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14,
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15,
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16,
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17,
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18,
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19,
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20,
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21,
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22,
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
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
            # Class: WeaponCloudsGun\Table,
            "Table": {
                # Class: WeaponCloudsGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
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
            # Class: WeaponCloudsMGun\Table,
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints,
        "HitPoints": {
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitTurret
            "HitTurret": {
                "armor": 0.8,
                "material": 51,
                "name": "turret",
                "visual": "turret",
                "passThrough": 1,
                "explosionShielding": 1
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitGun,
            "HitGun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passThrough": 1,
                "explosionShielding": 1
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets,
        "Turrets": {
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics,
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
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
    # Class: CfgVehicles\AllVehicles\ViewCargo,
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
    # Class: CfgVehicles\AllVehicles\PilotSpec,
    "PilotSpec": {
        "showHeadPhones": 0
    },
    # Class: CfgVehicles\AllVehicles\SoundEvents,
    "SoundEvents": {
    },
    "tracksSpeed": 0,
    "selectionLeftOffset": "",
    "selectionRightOffset": "",
    # Class: CfgVehicles\AllVehicles\RenderTargets,
    "RenderTargets": {
    },
    "cargoProxyIndexes": [],
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "cargoPreciseGetInOut": [0],
    "waterPPInVehicle": 1,
    "htMin": 60,
    "htMax": 1800,
    "afMax": 200,
    "mfMax": 100,
    "mFact": 0.2,
    "tBody": 150,
    "impactEffectSpeedLimit": 8,
    "showCrewAim": 0,
    # Class: CfgVehicles\AllVehicles\CargoTurret,
    "CargoTurret": {
        # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner
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
        # Class: CfgVehicles\AllVehicles\CargoTurret\Hitpoints,
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
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
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors,
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire,
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
            # Class: WeaponFireGun\Table,
            "Table": {
                # Class: WeaponFireGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1,
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2,
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3,
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4,
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5,
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6,
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7,
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8,
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9,
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10,
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11,
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12,
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13,
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14,
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15,
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16,
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17,
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18,
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19,
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20,
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21,
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22,
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds,
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
            # Class: WeaponCloudsGun\Table,
            "Table": {
                # Class: WeaponCloudsGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds,
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
            # Class: WeaponCloudsMGun\Table,
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets,
        "Turrets": {
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics,
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
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
    "spotableDarkNightLightsOff": 0.001,
    "spotableNightLightsOff": 0.02,
    "spotableNightLightsOn": 4,
    "accuracyDarkNightLightsOff": 0.001,
    "accuracyNightLightsOff": 0.006,
    "accuracyNightLightsOn": 0.1,
    "obstructSoundLFRatio": 0,
    "occludeSoundLFRatio": 0.25,
    "unloadInCombat": 0,
    "antiRollbarForceCoef": 0,
    "antiRollbarForceLimit": 5,
    "antiRollbarSpeedMin": 20,
    "antiRollbarSpeedMax": 60,
    "slowSpeedForwardCoef": 0.3,
    "normalSpeedForwardCoef": 0.85,
    "gunnerHasFlares": 1,
    "sensitivity": 2.5,
    "sensitivityEar": 0.0075,
    "portrait": "",
    "ghostPreview": "",
    "armorLights": 0.4,
    "damageResistance": 0.004,
    "replaceDamaged": "",
    "replaceDamagedLimit": 0.9,
    "replaceDamagedHitpoints": [],
    "keepInEPESceneAfterDeath": 0,
    "extCameraPosition": [0,2,-20],
    "groupCameraPosition": [0,5,-30],
    "cameraSmoothSpeed": 5,
    "predictTurnSimul": 1.2,
    "predictTurnPlan": 1,
    "indirectHitEnemyCoefAI": 10,
    "indirectHitFriendlyCoefAI": -20,
    "indirectHitCivilianCoefAI": -20,
    "indirectHitUnknownCoefAI": -0.5,
    "alwaysTarget": 0,
    "irScanGround": 1,
    "laserTarget": 0,
    "nvTarget": 0,
    "nvScanner": 0,
    "artilleryTarget": 0,
    "artilleryScanner": 0,
    "canUseScanners": 1,
    "preferRoads": 0,
    "hideUnitInfo": 0,
    "limitedSpeedCoef": 0.22,
    "hasDriver": 1,
    "driverForceOptics": 0,
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 0,
    "memoryPointSupply": "doplnovani",
    "enableWatch": 0,
    "usePreciseGetInAction": 0,
    "allowTabLock": 1,
    "dustFrontLeftPos": "dustFrontLeft",
    "dustFrontRightPos": "dustFrontRight",
    "dustBackLeftPos": "dustBackLeft",
    "dustBackRightPos": "dustBackRight",
    "wheelCircumference": 1,
    "waterResistanceCoef": 0.5,
    "waterLinearDampingCoefX": 0,
    "waterLinearDampingCoefY": 0,
    "waterAngularDampingCoef": 0,
    "showNVGDriver": 0,
    "showNVGCommander": 0,
    "showNVGGunner": 0,
    "showNVGCargo": [0],
    "soundAttenuationCargo": [1],
    "countsForScoreboard": 1,
    "hullDamageCauseExplosion": 0,
    # Class: CfgVehicles\All\NVGMarkers,
    "NVGMarkers": {
    },
    # Class: CfgVehicles\All\NVGMarker,
    "NVGMarker": {
        "diffuse": [1,1,1,1],
        "ambient": [1,1,1,1],
        "brightness": 1,
        "blinking": 0,
        "onlyInNvg": 0
    },
    # Class: CfgVehicles\All\HeadLimits,
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
    "soundEngine": ["",1,1],
    "soundEnviron": ["",1,1],
    # Class: CfgVehicles\All\SoundEnvironExt,
    "SoundEnvironExt": {
    },
    # Class: CfgVehicles\All\SoundEquipment,
    "SoundEquipment": {
    },
    # Class: CfgVehicles\All\SoundGear,
    "SoundGear": {
    },
    # Class: CfgVehicles\All\SoundBreath,
    "SoundBreath": {
    },
    # Class: CfgVehicles\All\SoundBreathSwimming,
    "SoundBreathSwimming": {
    },
    # Class: CfgVehicles\All\SoundBreathInjured,
    "SoundBreathInjured": {
    },
    # Class: CfgVehicles\All\SoundHitScream,
    "SoundHitScream": {
    },
    # Class: CfgVehicles\All\SoundInjured,
    "SoundInjured": {
    },
    # Class: CfgVehicles\All\SoundBreathAutomatic,
    "SoundBreathAutomatic": {
    },
    # Class: CfgVehicles\All\SoundDrown,
    "SoundDrown": {
    },
    # Class: CfgVehicles\All\SoundChoke,
    "SoundChoke": {
    },
    # Class: CfgVehicles\All\SoundRecovered,
    "SoundRecovered": {
    },
    # Class: CfgVehicles\All\SoundBurning,
    "SoundBurning": {
    },
    # Class: CfgVehicles\All\PulsationSound,
    "PulsationSound": {
    },
    # Class: CfgVehicles\All\SoundDrowning,
    "SoundDrowning": {
    },
    "soundCrash": ["",0.316228,1],
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
    "aggregateReflectors": [],
    "cargoIsCoDriver": [0],
    "driverOpticsModel": "",
    "driverOpticsEffect": [],
    "driverOpticsColor": [1,1,1,1],
    "hideProxyInCombat": 0,
    "forceHideDriver": 0,
    "canHideDriver": -1,
    "castCargoShadow": 0,
    "viewDriverShadow": 1,
    "viewDriverShadowDiff": 1,
    "viewDriverShadowAmb": 1,
    "viewCargoShadowDiff": 1,
    "viewCargoShadowAmb": 1,
    "ejectDeadDriver": 0,
    "ejectDeadCargo": 0,
    "hiddenSelectionsMaterials": [],
    "hiddenUnderwaterSelections": [],
    "shownUnderWaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    # Class: CfgVehicles\All\FxExplo,
    "FxExplo": {
        "access": 1
    },
    # Class: CfgVehicles\All\GunFire,
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
        # Class: WeaponFireGun\Table,
        "Table": {
            # Class: WeaponFireGun\Table\T0
            "T0": {
                "maxT": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun\Table\T1,
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun\Table\T2,
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun\Table\T3,
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun\Table\T4,
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun\Table\T5,
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun\Table\T6,
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun\Table\T7,
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun\Table\T8,
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun\Table\T9,
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun\Table\T10,
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun\Table\T11,
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun\Table\T12,
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun\Table\T13,
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun\Table\T14,
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun\Table\T15,
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun\Table\T16,
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun\Table\T17,
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun\Table\T18,
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun\Table\T19,
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun\Table\T20,
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun\Table\T21,
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun\Table\T22,
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\All\GunClouds,
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
        # Class: WeaponCloudsGun\Table,
        "Table": {
            # Class: WeaponCloudsGun\Table\T0
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\All\MGunClouds,
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
        # Class: WeaponCloudsMGun\Table,
        "Table": {
            # Class: WeaponCloudsMGun\Table\T0
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "selectionDamage": "zbytek",
    "HeadAimDown": 0,
    "fireResistance": 10,
    "airCapacity": 10,
    "waterDamageEngine": 0.2,
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "coefSpeedInside": 2,
    "windSockExist": 0,
    "slingLoadCargoMemoryPoints": [],
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    "soundTurnIn": ["",0.000316228,1],
    "soundTurnOut": ["",0.000316228,1],
    "soundTurnInInternal": ["",0.000316228,1],
    "soundTurnOutInternal": ["",0.000316228,1],
    "insideDetectCoef": 0.05,
}