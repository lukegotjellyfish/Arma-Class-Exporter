RHS_Su25SM_vvs = {
    "editorPreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_Su25SM_vvs.paa",
    "faction": "rhs_faction_vvs",
    "scope": 2,
    "displayName": "Su-25",
    "author": "Red Hammer Studios",
    "hiddenselectionstextures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_co.paa","a3|data_f|clear_empty.paa","a3|data_f|clear_empty.paa","a3|data_f|clear_empty.paa","a3|data_f|clear_empty.paa","rhsafrf|addons|rhs_decals|data|labels|aviation|vvs_ca.paa"],
    "accuracy": 0.5,
    "side": 0,
    "vehicleClass": "rhs_vehclass_aircraft",
    "dlc": "RHS_AFRF",
    "rhs_decalParameters": ["['Number',cRHSAIRSU25NumberPlaces,'AviaRed']","['Label', cRHSAIRSU25NosePlaces, 'Su25NoseArt']","['Label', cRHSAIRSU25SidePlaces, 'Su25Ex']"],
    "irTarget": 1,
    "irTargetSize": 1,
    "visualTarget": 1,
    "visualTargetSize": 0.9,
    "radarTarget": 1,
    "radarTargetSize": 1,
    "LESH_canBeTowed": 1,
    "LESH_towFromFront": 1,
    "LESH_AxisOffsetTarget": [0,6.8,-2.04],
    "LESH_WheelOffset": [0,-0.7],
    "category": "Air",
    "crew": "rhs_pilot",
    "typicalCargo": ["rhs_pilot"],
    "availableForSupportTypes": ["CAS_Bombing"],
    "model": "rhsafrf|addons|rhs_a2port_air|su25|su25",
    "picture": "rhsafrf|addons|rhs_a2port_air|data|ico|rhs_su25sm_pic_ca.paa",
    "icon": "rhsafrf|addons|rhs_a2port_air|data|map_ico|icomap_su25.paa",
    "mapSize": 20,
    "textSingular": "Su25",
    "driverAction": "rhs_su25_pilot",
    "driverLeftHandAnimName": "lever_pilot",
    "driverRightHandAnimName": "stick_pilot",
    "driverLeftLegAnimName": "pedal_L",
    "driverRightLegAnimName": "pedal_R",
    "memoryPointsGetInDriver": "pos driver",
    "memoryPointsGetInDriverDir": "pos driver dir",
    "memoryPointsGetInDriverPrecise": "pos driver",
    "unitInfoType": "RHS_RscUnitInfoAir_Su25",
    "driverWeaponsInfoType": "RHS_RscOptics_Su25_KlenPS",
    "HeadAimDown": 6,
    "headGforceLeaningFactor": [0.005,0.001,0.015],
    "camShakeCoef": 0.7,
    "driverCanSee": "2+4+8+16",
    "allowTabLock": 0,
    "driverCanEject": 1,
    "driverCompartments": 1,
    # Class: CfgVehicles\RHS_su25_base\EjectionSystem [Indent level: 1],
    "EjectionSystem": {
    },
    "ejectDamageLimit": 1,
    "memoryPointDriverOptics": "pilotCamera",
    # Class: CfgVehicles\RHS_su25_base\PilotCamera [Indent level: 1],
    "PilotCamera": {
        # Class: CfgVehicles\RHS_su25_base\PilotCamera\OpticsIn [Indent level: 2]
        "OpticsIn": {
            # Class: CfgVehicles\RHS_su25_base\PilotCamera\OpticsIn\Wide [Indent level: 3]
            "Wide": {
                "opticsDisplayName": "WFOV",
                "initAngleX": 0,
                "minAngleX": 0,
                "maxAngleX": 0,
                "initAngleY": 0,
                "minAngleY": 0,
                "maxAngleY": 0,
                "initFov": "(10 / 120)",
                "minFov": "(60 / 120)",
                "maxFov": "(60 / 120)",
                "directionStabilized": 1,
                "visionMode": ["Normal"],
                "gunneropticsmodel": "",
                "opticsPPEffects": ["OpticsCHAbera2","OpticsBlur2"]
            }
        },
        "minTurn": -12,
        "maxTurn": 12,
        "initTurn": 0,
        "minElev": -6,
        "maxElev": 16,
        "initElev": 0,
        "maxXRotSpeed": 1,
        "maxYRotSpeed": 1,
        "maxMouseXRotSpeed": 0.5,
        "maxMouseYRotSpeed": 0.5,
        "pilotOpticsShowCursor": 1,
        "controllable": 1
    },
    # Class: CfgVehicles\RHS_su25_base\ViewPilot [Indent level: 1],
    "ViewPilot": {
        "initAngleX": -0,
        "initFov": 1,
        "minFov": 0.3,
        "maxFov": 1.2,
        "minAngleX": -75,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -170,
        "maxAngleY": 170,
        "minMoveX": -0.2,
        "maxMoveX": 0.2,
        "minMoveY": -0.025,
        "maxMoveY": 0.1,
        "minMoveZ": -0.2,
        "maxMoveZ": 0.2,
        "speedZoomMaxSpeed": 0,
        "speedZoomMaxFOV": 1
    },
    "weapons": ["rhs_weap_MASTERSAFE","rhs_weap_klen_ps","rhs_weap_GSh302"],
    "magazines": ["rhs_lasermag","rhs_mag_gsh30_bt_250"],
    "weaponsGroup1": 128,
    "weaponsGroup4": 64,
    "memoryPointGun": ["kulomet","kulomet2"],
    "gunBeg": ["muzzle_1","muzzle_2"],
    "gunEnd": ["chamber_1","chamber_2"],
    "selectionFireAnim": "zasleh",
    "memoryPointLDust": "levy prach",
    "memoryPointRDust": "pravy prach",
    "memoryPointLRocket": "rocket_1",
    "memoryPointRRocket": "rocket_2",
    "memoryPointLMissile": "missile_1",
    "memoryPointRMissile": "missile_2",
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "selectionDamage": "trup",
    "selectionShowDamage": "poskozeni",
    "armor": 60,
    "damageResistance": 0.0048,
    "armorStructural": 2,
    "epeImpulseDamageCoef": 1,
    # Class: CfgVehicles\RHS_su25_base\Hitpoints [Indent level: 1],
    "Hitpoints": {
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitHull [Indent level: 2]
        "HitHull": {
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0.01,
            "minimalHit": 1,
            "radius": 0.15,
            "material": -1,
            "name": "hit_hull",
            "visual": "-",
            "depends": "Total"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitAvionics [Indent level: 2],
        "HitAvionics": {
            "armor": 1,
            "explosionShielding": 0.6,
            "passThrough": 0.05,
            "minimalHit": 0.1,
            "radius": 0.08,
            "material": -1,
            "name": "hit_avionics",
            "visual": "vis_avionics",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitEngine [Indent level: 2],
        "HitEngine": {
            "armor": 1,
            "explosionShielding": 0.25,
            "passThrough": 0.2,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_l",
            "visual": "vis_engine_l",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitEngine2 [Indent level: 2],
        "HitEngine2": {
            "armor": 1,
            "explosionShielding": 0.25,
            "passThrough": 0.2,
            "minimalHit": 0.01,
            "radius": 0.07,
            "material": -1,
            "name": "hit_engine_r",
            "visual": "vis_engine_r",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitFuel [Indent level: 2],
        "HitFuel": {
            "armor": 1.4,
            "explosionShielding": 0.2,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel",
            "visual": "vis_fuel",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitFuel_left [Indent level: 2],
        "HitFuel_left": {
            "armor": 1,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel_wing_l",
            "visual": "vis_wing_l",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitFuel_right [Indent level: 2],
        "HitFuel_right": {
            "armor": 1,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.1,
            "material": -1,
            "name": "hit_fuel_wing_r",
            "visual": "vis_wing_r",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitFuel2 [Indent level: 2],
        "HitFuel2": {
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0.1,
            "minimalHit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "ind_fuel_r",
            "depends": "(HitFuel_left+HitFuel_right)*0.5"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitLAileron_link [Indent level: 2],
        "HitLAileron_link": {
            "armor": 0.6,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_l",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitRAileron_link [Indent level: 2],
        "HitRAileron_link": {
            "armor": 0.6,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_aileron_link_r",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitLAileron [Indent level: 2],
        "HitLAileron": {
            "armor": 0.6,
            "explosionShielding": 0.5,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_l",
            "visual": "vis_wing_l",
            "depends": "HitLAileron_link*0.7"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitRAileron [Indent level: 2],
        "HitRAileron": {
            "armor": 0.6,
            "explosionShielding": 0.5,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.13,
            "material": -1,
            "name": "hit_aileron_r",
            "visual": "vis_wing_r",
            "depends": "HitRAileron_link*0.7"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitControlRear [Indent level: 2],
        "HitControlRear": {
            "armor": 0.6,
            "explosionShielding": 0.1,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.04,
            "material": -1,
            "name": "hit_control_rear",
            "visual": "-",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitLCElevator [Indent level: 2],
        "HitLCElevator": {
            "armor": 0.6,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_l",
            "visual": "vis_elevator_l",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitRElevator [Indent level: 2],
        "HitRElevator": {
            "armor": 0.6,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_elevator_r",
            "visual": "vis_elevator_r",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitLCRudder [Indent level: 2],
        "HitLCRudder": {
            "armor": 0.6,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.12,
            "material": -1,
            "name": "hit_rudder",
            "visual": "vis_rudder",
            "depends": "HitControlRear"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitGlass1 [Indent level: 2],
        "HitGlass1": {
            "armor": 0.5,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.3,
            "material": -1,
            "name": "glass1",
            "visual": "glass1",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitGlass2 [Indent level: 2],
        "HitGlass2": {
            "armor": 0.5,
            "explosionShielding": 0.6,
            "passThrough": 0.1,
            "minimalHit": 0.1,
            "radius": 0.3,
            "material": -1,
            "name": "glass2",
            "visual": "glass2",
            "depends": "0"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\Ind_Fire1 [Indent level: 2],
        "Ind_Fire1": {
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0,
            "minimalHit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "ind_fire",
            "depends": "HitEngine*0.5"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\Ind_Fire2 [Indent level: 2],
        "Ind_Fire2": {
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0,
            "minimalHit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "ind_fire",
            "depends": "HitEngine2*0.5"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\Ind_Hydr_L [Indent level: 2],
        "Ind_Hydr_L": {
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0,
            "minimalHit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "ind_hydr_l",
            "depends": "(HitLAileron+HitLCElevator+HitLCRudder)*0.5"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\Ind_Hydr_R [Indent level: 2],
        "Ind_Hydr_R": {
            "armor": 999,
            "explosionShielding": 0,
            "passThrough": 0,
            "minimalHit": 1,
            "radius": 0.01,
            "material": -1,
            "name": "hit_fuel",
            "visual": "ind_hydr_r",
            "depends": "(HitRAileron+HitRElevator)*0.5"
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon1 [Indent level: 2],
        "HitPylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon1\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon1\DestructionEffects\RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon1\DestructionEffects\RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon1\DestructionEffects\RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon1\DestructionEffects\RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon2 [Indent level: 2],
        "HitPylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon2\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon2\DestructionEffects\RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon2\DestructionEffects\RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon2\DestructionEffects\RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon2\DestructionEffects\RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon3 [Indent level: 2],
        "HitPylon3": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_3",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon3\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon3\DestructionEffects\RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon3\DestructionEffects\RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon3\DestructionEffects\RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon3\DestructionEffects\RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon4 [Indent level: 2],
        "HitPylon4": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_4",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon4\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon4\DestructionEffects\RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon4\DestructionEffects\RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon4\DestructionEffects\RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon4\DestructionEffects\RHS_Pylon_Shard [Indent level: 4],
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
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon5 [Indent level: 2],
        "HitPylon5": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_5",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon5\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon5\DestructionEffects\RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon5\DestructionEffects\RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon5\DestructionEffects\RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon5\DestructionEffects\RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon6 [Indent level: 2],
        "HitPylon6": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_6",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon6\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon6\DestructionEffects\RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon6\DestructionEffects\RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon6\DestructionEffects\RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon6\DestructionEffects\RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon7 [Indent level: 2],
        "HitPylon7": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_7",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon7\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon7\DestructionEffects\RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon7\DestructionEffects\RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon7\DestructionEffects\RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon7\DestructionEffects\RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon8 [Indent level: 2],
        "HitPylon8": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_8",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon8\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon8\DestructionEffects\RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_8",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon8\DestructionEffects\RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_8",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon8\DestructionEffects\RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_8",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon8\DestructionEffects\RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_8",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon9 [Indent level: 2],
        "HitPylon9": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_9",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon9\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon9\DestructionEffects\RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_9",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon9\DestructionEffects\RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_9",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon9\DestructionEffects\RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_9",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon9\DestructionEffects\RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_9",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon10 [Indent level: 2],
        "HitPylon10": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_10",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.75,
            "visual": "-",
            # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon10\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon10\DestructionEffects\RHS_Pylon_Flash [Indent level: 4],
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_10",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon10\DestructionEffects\RHS_Pylon_Sound [Indent level: 4],
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_10",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon10\DestructionEffects\RHS_Pylon_Smoke [Indent level: 4],
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_10",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_su25_base\Hitpoints\HitPylon10\DestructionEffects\RHS_Pylon_Shard [Indent level: 4],
                "RHS_Pylon_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_10",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        }
    },
    "incomingMissileDetectionSystem": 8,
    "lockDetectionSystem": 8,
    "hiddenselections": ["camo1","camo2","n1","n2","i1","i2","tail_decals"],
    # Class: CfgVehicles\RHS_su25_base\textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles\RHS_su25_base\textureSources\standard [Indent level: 2]
        "standard": {
            "displayName": "Blue",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_alt_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_alt_co.paa"],
            "factions": ["rhs_faction_vvs"]
        },
        # Class: CfgVehicles\RHS_su25_base\textureSources\standard2 [Indent level: 2],
        "standard2": {
            "displayName": "Grey",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_co.paa"],
            "factions": ["rhs_faction_vvs"]
        },
        # Class: CfgVehicles\RHS_su25_base\textureSources\Camo [Indent level: 2],
        "Camo": {
            "displayName": "Camo #1",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_rus_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_rus_co.paa"],
            "factions": ["rhs_faction_vvs_c"]
        },
        # Class: CfgVehicles\RHS_su25_base\textureSources\Camo1 [Indent level: 2],
        "Camo1": {
            "displayName": "Camo #2",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|camo|su25_body1_camo1_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|camo|su25_body2_camo1_co.paa"],
            "factions": ["rhs_faction_vvs_c"]
        },
        # Class: CfgVehicles\RHS_su25_base\textureSources\Camo2 [Indent level: 2],
        "Camo2": {
            "displayName": "CDF",
            "author": "Red Hammer Studios",
            "textures": ["|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_cdf_co.paa","|rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_cdf_co.paa"],
            "factions": ["rhs_faction_vvs"]
        }
    },
    "textureList": [],
    # Class: CfgVehicles\RHS_su25_base\Components [Indent level: 1],
    "Components": {
        # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent [Indent level: 2]
        "TransportPylonsComponent": {
            "UIPicture": "rhsafrf|addons|rhs_a2port_air|data|loadouts|RHS_Su25_EDEN_CA.paa",
            # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\pylon1 [Indent level: 4]
                "pylon1": {
                    "hardpoints": ["RHS_HP_KH29","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 9,
                    "attachment": "rhs_mag_fab250",
                    "hitpoint": "HitPylon1",
                    "maxweight": 1200,
                    "UIposition": [0.32,0.35]
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\pylon2 [Indent level: 4],
                "pylon2": {
                    "UIposition": [0.32,0.2],
                    "mirroredMissilePos": 1,
                    "hitpoint": "HitPylon2",
                    "hardpoints": ["RHS_HP_KH29","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 9,
                    "attachment": "rhs_mag_fab250",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\pylon3 [Indent level: 4],
                "pylon3": {
                    "hardpoints": ["RHS_HP_KH25","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 7,
                    "hitpoint": "HitPylon3",
                    "UIposition": [0.33,0.4],
                    "attachment": "rhs_mag_fab250",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\pylon4 [Indent level: 4],
                "pylon4": {
                    "UIposition": [0.33,0.15],
                    "mirroredMissilePos": 3,
                    "hitpoint": "HitPylon4",
                    "hardpoints": ["RHS_HP_KH25","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 7,
                    "attachment": "rhs_mag_fab250",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\pylon5 [Indent level: 4],
                "pylon5": {
                    "hardpoints": ["RHS_HP_KH25","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 10,
                    "attachment": "rhs_mag_b8m1_s8kom",
                    "hitpoint": "HitPylon5",
                    "maxweight": 1200,
                    "UIposition": [0.34,0.45]
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\pylon6 [Indent level: 4],
                "pylon6": {
                    "UIposition": [0.34,0.1],
                    "mirroredMissilePos": 5,
                    "hitpoint": "HitPylon6",
                    "hardpoints": ["RHS_HP_KH25","RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 10,
                    "attachment": "rhs_mag_b8m1_s8kom",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\pylon7 [Indent level: 4],
                "pylon7": {
                    "hardpoints": ["RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 11,
                    "attachment": "rhs_mag_b8m1_s8df",
                    "hitpoint": "HitPylon7",
                    "maxweight": 1200,
                    "UIposition": [0.35,0.5]
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\pylon8 [Indent level: 4],
                "pylon8": {
                    "UIposition": [0.35,0.05],
                    "mirroredMissilePos": 7,
                    "hitpoint": "HitPylon8",
                    "hardpoints": ["RHS_HP_FAB100","RHS_HP_FAB100_MBD3_U4T","RHS_HP_FAB100_MBD3_U6","RHS_HP_FAB250","RHS_HP_FAB500","RHS_HP_KMGU2","RHS_HP_O25L","RHS_HP_APU68M3_S24","RHS_HP_B13L","RHS_HP_B8M1","RHS_HP_UB16","RHS_HP_UB32","RHS_HP_R73"],
                    "priority": 11,
                    "attachment": "rhs_mag_b8m1_s8df",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\pylon9 [Indent level: 4],
                "pylon9": {
                    "hardpoints": ["RHS_HP_R60"],
                    "priority": 12,
                    "attachment": "rhs_mag_R60M",
                    "hitpoint": "HitPylon9",
                    "maxweight": 1200,
                    "UIposition": [0.36,0.55]
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\pylon10 [Indent level: 4],
                "pylon10": {
                    "UIposition": [0.36,0],
                    "mirroredMissilePos": 9,
                    "hitpoint": "HitPylon10",
                    "hardpoints": ["RHS_HP_R60"],
                    "priority": 12,
                    "attachment": "rhs_mag_R60M",
                    "maxweight": 1200
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\pylons\cmDispenser [Indent level: 4],
                "cmDispenser": {
                    "hardpoints": ["RHS_cm_ASO2","RHS_cm_ASO2_x2","RHS_cm_ASO2_x4"],
                    "priority": 1,
                    "attachment": "rhs_ASO2_CMFlare_Chaff_Magazine_x4",
                    "maxweight": 800,
                    "UIposition": [0.625,0.275]
                }
            },
            # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets [Indent level: 3],
            "Presets": {
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets\CAS [Indent level: 4]
                "CAS": {
                    "attachment": ["rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Close Air Support"
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets\HeavyCAS [Indent level: 4],
                "HeavyCAS": {
                    "attachment": ["rhs_mag_b13l_s13b","rhs_mag_b13l_s13b","rhs_mag_b13l_s13t","rhs_mag_b13l_s13t","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Close Air Support (S-13)"
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets\GroundSupress_S24B [Indent level: 4],
                "GroundSupress_S24B": {
                    "attachment": ["rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_apu68m3_s24b","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Ground Supress (S-24B)"
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets\Bomb [Indent level: 4],
                "Bomb": {
                    "attachment": ["rhs_mag_fab250","rhs_mag_fab250","rhs_mag_fab250","rhs_mag_fab250","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Bomb (FAB-250)"
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets\HeavyBomb [Indent level: 4],
                "HeavyBomb": {
                    "attachment": ["rhs_mag_fab500","rhs_mag_fab500","rhs_mag_fab500","rhs_mag_fab500","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Bomb (FAB-500)"
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets\AT [Indent level: 4],
                "AT": {
                    "attachment": ["rhs_mag_fab250","rhs_mag_fab250","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Anti Tank (Kh-25ML)"
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets\HeavyAT [Indent level: 4],
                "HeavyAT": {
                    "attachment": ["rhs_mag_kh29ML","rhs_mag_kh29ML","rhs_mag_fab250","rhs_mag_fab250","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Anti Tank (Kh-29ML)"
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets\HeavyATMix [Indent level: 4],
                "HeavyATMix": {
                    "attachment": ["rhs_mag_kh29ML","rhs_mag_kh29ML","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_kh25ML","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Anti Tank (Mixed)"
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets\Cluster [Indent level: 4],
                "Cluster": {
                    "attachment": ["rhs_mag_rbk250_ao1","rhs_mag_rbk250_ao1","rhs_mag_rbk250_ao1","rhs_mag_rbk250_ao1","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "Heavy CAS (S-13)"
                },
                # Class: CfgVehicles\RHS_su25_base\Components\TransportPylonsComponent\Presets\KMGU [Indent level: 4],
                "KMGU": {
                    "attachment": ["rhs_mag_kmgu2_ao25","rhs_mag_kmgu2_ao25","rhs_mag_kmgu2_ao25","rhs_mag_kmgu2_ao25","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8kom","rhs_mag_b8m1_s8df","rhs_mag_b8m1_s8df","rhs_mag_R60M","rhs_mag_R60M","rhs_ASO2_CMFlare_Chaff_Magazine_x4"],
                    "displayname": "KMGU-2"
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Components\SensorsManagerComponent [Indent level: 2],
        "SensorsManagerComponent": {
            # Class: CfgVehicles\RHS_su25_base\Components\SensorsManagerComponent\Components [Indent level: 3]
            "Components": {
                # Class: CfgVehicles\RHS_su25_base\Components\SensorsManagerComponent\Components\PassiveRadarSensorComponent [Indent level: 4]
                "PassiveRadarSensorComponent": {
                    "componentType": "PassiveRadarSensorComponent",
                    # Class: SensorTemplatePassiveRadar\AirTarget [Indent level: 0],
                    "AirTarget": {
                        "minRange": 16000,
                        "maxRange": 16000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: SensorTemplatePassiveRadar\GroundTarget [Indent level: 0],
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
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Components\TransportCountermeasuresComponent [Indent level: 2],
        "TransportCountermeasuresComponent": {
        }
    },
    # Class: CfgVehicles\RHS_su25_base\Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles\RHS_su25_base\Attributes\ObjectTexture [Indent level: 2]
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type [Indent level: 2],
        "rhs_decalNumber_type": {
            "displayName": "Define font type of side number",
            "tooltip": "Define kind of font that will be drawn on vehicle",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "if(_value != 'NoChange')then{ _this setVariable ['%s', _value];[_this,[['Number', cRHSAIRSU25NumberPlaces, _value]]] call rhs_fnc_decalsInit}",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\NoChange [Indent level: 4]
                "NoChange": {
                    "name": "Default",
                    "value": "NoChange"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\AviaYellow [Indent level: 4],
                "AviaYellow": {
                    "name": "Aviation Yellow",
                    "value": "AviaYellow"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\AviaBlue [Indent level: 4],
                "AviaBlue": {
                    "name": "Aviation Blue",
                    "value": "AviaBlue",
                    "defaultValue": "AviaBlue"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\AviaRed [Indent level: 4],
                "AviaRed": {
                    "name": "Aviation Red",
                    "value": "AviaRed"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\AviaWhiteOut [Indent level: 4],
                "AviaWhiteOut": {
                    "name": "Aviation White Out",
                    "value": "AviaWhiteOut"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\AviaCDF [Indent level: 4],
                "AviaCDF": {
                    "name": "Aviation CDF",
                    "value": "AviaCDF"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\Default [Indent level: 4],
                "Default": {
                    "name": "Default (White)",
                    "value": "Default"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\DefaultRed [Indent level: 4],
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\BoldRed [Indent level: 4],
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\CDF [Indent level: 4],
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\Handpaint [Indent level: 4],
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\HandpaintBlack [Indent level: 4],
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber_type\values\Iraqi [Indent level: 4],
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNumber [Indent level: 2],
        "rhs_decalNumber": {
            "displayName": "Set side number",
            "tooltip": "Set side number. 2 numbers are required. Type 0 to hide numbers completly",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "defaultValue": "-1",
            "typeName": "Number",
            "expression": "if(_value >= 0)then{if(_value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSAIRSU25NumberPlaces}else{[_this, [['Number', cRHSAIRSU25NumberPlaces, _this getVariable ['rhs_decalNumber_type','AviaYellow'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNoseArt [Indent level: 2],
        "rhs_decalNoseArt": {
            "displayName": "Define Nose Art",
            "tooltip": "Define Nose Art texture located near the cabin. Appears on both sides",
            "property": "rhs_decalNoseArt",
            "control": "Combo",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cRHSAIRSU25NosePlaces, 'Su25NoseArt',_value] ] ] call rhs_fnc_decalsInit};",
            "defaultValue": "-1",
            "typeName": "Number",
            # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNoseArt\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNoseArt\values\Random [Indent level: 4]
                "Random": {
                    "name": "Random",
                    "value": -1,
                    "defaultValue": -1
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNoseArt\values\Empty [Indent level: 4],
                "Empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNoseArt\values\Arrows [Indent level: 4],
                "Arrows": {
                    "name": "Aviation emblem",
                    "value": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNoseArt\values\Thunders [Indent level: 4],
                "Thunders": {
                    "name": "Thunders",
                    "value": 2
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNoseArt\values\Eyes [Indent level: 4],
                "Eyes": {
                    "name": "Eyes",
                    "value": 3
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalNoseArt\values\Stars [Indent level: 4],
                "Stars": {
                    "name": "Stars",
                    "value": 4
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalSideArt [Indent level: 2],
        "rhs_decalSideArt": {
            "displayName": "Define Side Art",
            "tooltip": "Define Side Art texture located near the jet intake. Appears on both sides",
            "property": "rhs_decalSideArt",
            "expression": "if(_value >= 0)then{ [_this, [ [ 'Label', cRHSAIRSU25SidePlaces, 'Su25Ex',_value] ] ] call rhs_fnc_decalsInit};",
            # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalSideArt\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalSideArt\values\Random [Indent level: 4]
                "Random": {
                    "name": "Random",
                    "value": -1,
                    "defaultValue": -1
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalSideArt\values\Empty [Indent level: 4],
                "Empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalSideArt\values\Crow [Indent level: 4],
                "Crow": {
                    "name": "Crow",
                    "value": 1
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalSideArt\values\Russia [Indent level: 4],
                "Russia": {
                    "name": "Russia emblem",
                    "value": 2
                }
            },
            "control": "Combo",
            "defaultValue": "-1",
            "typeName": "Number"
        },
        # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalTail [Indent level: 2],
        "rhs_decalTail": {
            "displayName": "Define tail decal",
            "tooltip": "Define tail decal that will be drawn on vehicle",
            "property": "rhs_decalTail",
            "control": "Combo",
            "expression": "[_this,[['Label', cRHSAIRSU25TailPlaces, 'Aviation',_value]]] call rhs_fnc_decalsInit",
            "defaultValue": -1,
            "typeName": "Number",
            # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalTail\values [Indent level: 3],
            "values": {
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalTail\values\Default [Indent level: 4]
                "Default": {
                    "name": "Default",
                    "value": -1
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalTail\values\Empty [Indent level: 4],
                "Empty": {
                    "name": "Empty",
                    "value": 0
                },
                # Class: CfgVehicles\RHS_su25_base\Attributes\rhs_decalTail\values\VVS [Indent level: 4],
                "VVS": {
                    "name": "VVS Russia",
                    "value": 3,
                    "defaultValue": 3
                }
            }
        }
    },
    # Class: CfgVehicles\RHS_su25_base\Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles\RHS_su25_base\Exhausts\Exhaust1 [Indent level: 2]
        "Exhaust1": {
            "position": "exhaust1",
            "direction": "exhaust1_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineIndex": 0
        },
        # Class: CfgVehicles\RHS_su25_base\Exhausts\Exhaust2 [Indent level: 2],
        "Exhaust2": {
            "position": "exhaust2",
            "direction": "exhaust2_dir",
            "effect": "ExhaustsEffectPlaneHP",
            "engineIndex": 1
        }
    },
    # Class: CfgVehicles\RHS_su25_base\RenderTargets [Indent level: 1],
    "RenderTargets": {
        # Class: CfgVehicles\RHS_su25_base\RenderTargets\Periscope [Indent level: 2]
        "Periscope": {
            "renderTarget": "rendertarget0",
            # Class: CfgVehicles\RHS_su25_base\RenderTargets\Periscope\CameraView1 [Indent level: 3],
            "CameraView1": {
                "pointPosition": "PIP0_pos",
                "pointDirection": "PIP0_dir",
                "renderVisionMode": 0,
                "renderQuality": 2,
                "fov": 0.5
            }
        }
    },
    # Class: CfgVehicles\RHS_su25_base\compartmentsLights [Indent level: 1],
    "compartmentsLights": {
        # Class: CfgVehicles\RHS_su25_base\compartmentsLights\Comp1 [Indent level: 2]
        "Comp1": {
            # Class: CfgVehicles\RHS_su25_base\compartmentsLights\Comp1\Light_General [Indent level: 3]
            "Light_General": {
                "color": [40,20,20],
                "ambient": [0,0,0],
                "intensity": 2.5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\RHS_su25_base\compartmentsLights\Comp1\Light_General\Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 1.45,
                    "hardLimitEnd": 2.45
                },
                "point": "light_general"
            }
        }
    },
    # Class: CfgVehicles\RHS_su25_base\Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles\RHS_su25_base\Reflectors\Left [Indent level: 2]
        "Left": {
            "ambient": [100,100,100,0],
            "color": [7000,7500,10000,1],
            "coneFadeCoef": 10,
            "dayLight": 0,
            "direction": "konec l svetla",
            "flareSize": 4,
            "hitpoint": "l svetlo",
            "innerAngle": 20,
            "intensity": 50,
            "outerAngle": 60,
            "position": "l svetlo",
            "selection": "l svetlo",
            "size": 1,
            "useFlare": 1,
            # Class: CfgVehicles\RHS_su25_base\Reflectors\Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Reflectors\Left_Flare [Indent level: 2],
        "Left_Flare": {
            "intensity": 0.5,
            "useFlare": 1,
            "innerAngle": 5,
            "outerAngle": 175,
            "ambient": [100,100,100,0],
            "color": [7000,7500,10000,1],
            "coneFadeCoef": 10,
            "dayLight": 0,
            "direction": "konec l svetla",
            "flareSize": 4,
            "hitpoint": "l svetlo",
            "position": "l svetlo",
            "selection": "l svetlo",
            "size": 1,
            # Class: CfgVehicles\RHS_su25_base\Reflectors\Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Reflectors\Right [Indent level: 2],
        "Right": {
            "position": "p svetlo",
            "direction": "konec p svetla",
            "hitpoint": "p svetlo",
            "selection": "p svetlo",
            "ambient": [100,100,100,0],
            "color": [7000,7500,10000,1],
            "coneFadeCoef": 10,
            "dayLight": 0,
            "flareSize": 4,
            "innerAngle": 20,
            "intensity": 50,
            "outerAngle": 60,
            "size": 1,
            "useFlare": 1,
            # Class: CfgVehicles\RHS_su25_base\Reflectors\Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            }
        },
        # Class: CfgVehicles\RHS_su25_base\Reflectors\Right_Flare [Indent level: 2],
        "Right_Flare": {
            "intensity": 0.5,
            "useFlare": 1,
            "innerAngle": 5,
            "outerAngle": 175,
            "position": "p svetlo",
            "direction": "konec p svetla",
            "hitpoint": "p svetlo",
            "selection": "p svetlo",
            "ambient": [100,100,100,0],
            "color": [7000,7500,10000,1],
            "coneFadeCoef": 10,
            "dayLight": 0,
            "flareSize": 4,
            "size": 1,
            # Class: CfgVehicles\RHS_su25_base\Reflectors\Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1
            }
        }
    },
    "aggregateReflectors": [["Left","Left_Flare"],["Right","Right_Flare"]],
    # Class: CfgVehicles\RHS_su25_base\markerlights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles\RHS_su25_base\markerlights\GreenStill [Indent level: 2]
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
        # Class: CfgVehicles\RHS_su25_base\markerlights\RedStill [Indent level: 2],
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
        # Class: CfgVehicles\RHS_su25_base\markerlights\WhiteStill [Indent level: 2],
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
        # Class: CfgVehicles\RHS_su25_base\markerlights\WhiteBlicking [Indent level: 2],
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
        # Class: CfgVehicles\RHS_su25_base\markerlights\RedBlinking [Indent level: 2],
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
    # Class: CfgVehicles\RHS_su25_base\Damage [Indent level: 1],
    "Damage": {
        "tex": ["rhsafrf|addons|rhs_a2port_air|su25|data|rhs_su25_warningLights_empty_ca.paa","rhsafrf|addons|rhs_a2port_air|su25|data|rhs_su25_warningLights_ca.paa"],
        "mat": ["rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_in.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_in_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_in_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body1_destruct.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_body2_destruct.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_damage.rvmat","rhsafrf|addons|rhs_a2port_air|su25|data|su25_glass_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles\RHS_su25_base\AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\eject [Indent level: 2]
        "eject": {
            "source": "door",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\eject_hide [Indent level: 2],
        "eject_hide": {
            "source": "user",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\throttle_source [Indent level: 2],
        "throttle_source": {
            "animPeriod": 10,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\rwr_lights_lock [Indent level: 2],
        "rwr_lights_lock": {
            "source": "user",
            "initPhase": 0,
            "animPeriod": 8
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\rwr_lock_dir_primary [Indent level: 2],
        "rwr_lock_dir_primary": {
            "animPeriod": 0.1,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\rwr_lock_primary [Indent level: 2],
        "rwr_lock_primary": {
            "animPeriod": 1e-007,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\rwr_signal_strenght [Indent level: 2],
        "rwr_signal_strenght": {
            "animPeriod": 1e-007,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\rwr_lights [Indent level: 2],
        "rwr_lights": {
            "animPeriod": 1e-007,
            "source": "user",
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\hit_pylon_1_source [Indent level: 2],
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\hit_pylon_2_source [Indent level: 2],
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\hit_pylon_3_source [Indent level: 2],
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\hit_pylon_4_source [Indent level: 2],
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\hit_pylon_5_source [Indent level: 2],
        "hit_pylon_5_source": {
            "source": "Hit",
            "hitpoint": "HitPylon5"
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\hit_pylon_6_source [Indent level: 2],
        "hit_pylon_6_source": {
            "source": "Hit",
            "hitpoint": "HitPylon6"
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\hit_pylon_7_source [Indent level: 2],
        "hit_pylon_7_source": {
            "source": "Hit",
            "hitpoint": "HitPylon7"
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\hit_pylon_8_source [Indent level: 2],
        "hit_pylon_8_source": {
            "source": "Hit",
            "hitpoint": "HitPylon8"
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\hit_pylon_9_source [Indent level: 2],
        "hit_pylon_9_source": {
            "source": "Hit",
            "hitpoint": "HitPylon9"
        },
        # Class: CfgVehicles\RHS_su25_base\AnimationSources\hit_pylon_10_source [Indent level: 2],
        "hit_pylon_10_source": {
            "source": "Hit",
            "hitpoint": "HitPylon10"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Cannon_30mm_ammorandom [Indent level: 2],
        "Cannon_30mm_ammorandom": {
            "source": "ammorandom",
            "weapon": "Cannon_30mm_Plane_CAS_02_F"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Cannon_30mm_revolving [Indent level: 2],
        "Cannon_30mm_revolving": {
            "source": "revolving",
            "weapon": "Cannon_30mm_Plane_CAS_02_F"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Missile_AA_03_revolving [Indent level: 2],
        "Missile_AA_03_revolving": {
            "source": "revolving",
            "weapon": "Missile_AA_03_Plane_CAS_02_F"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Missile_AGM_01_revolving [Indent level: 2],
        "Missile_AGM_01_revolving": {
            "source": "revolving",
            "weapon": "Missile_AGM_01_Plane_CAS_02_F"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Rocket_03_HE_revolving [Indent level: 2],
        "Rocket_03_HE_revolving": {
            "source": "revolving",
            "weapon": "Rocket_03_HE_Plane_CAS_02_F"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Rocket_03_AP_revolving [Indent level: 2],
        "Rocket_03_AP_revolving": {
            "source": "revolving",
            "weapon": "Rocket_03_AP_Plane_CAS_02_F"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Bomb_03_revolving [Indent level: 2],
        "Bomb_03_revolving": {
            "source": "revolving",
            "weapon": "Bomb_03_Plane_CAS_02_F"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Damper_1_source [Indent level: 2],
        "Damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Damper_2_source [Indent level: 2],
        "Damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Damper_3_source [Indent level: 2],
        "Damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Wheel_1_source [Indent level: 2],
        "Wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Wheel_2_source [Indent level: 2],
        "Wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\Wheel_3_source [Indent level: 2],
        "Wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\HitAvionics [Indent level: 2],
        "HitAvionics": {
            "source": "Hit",
            "hitpoint": "HitAvionics",
            "raw": 1
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\HideWeapons [Indent level: 2],
        "HideWeapons": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\canopy_hide [Indent level: 2],
        "canopy_hide": {
            "source": "user",
            "animPeriod": 0.001,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\ejection_seat_hide [Indent level: 2],
        "ejection_seat_hide": {
            "source": "user",
            "animPeriod": 0.001,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\AnimationSources\ejection_seat_motion [Indent level: 2],
        "ejection_seat_motion": {
            "source": "user",
            "animPeriod": 0.25,
            "initPhase": 0
        },
        # Class: CfgVehicles\Air\AnimationSources\CollisionLightRed_source [Indent level: 2],
        "CollisionLightRed_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionRed"
        },
        # Class: CfgVehicles\Air\AnimationSources\CollisionLightWhite_source [Indent level: 2],
        "CollisionLightWhite_source": {
            "source": "MarkerLight",
            "markerLight": "CollisionWhite"
        }
    },
    # Class: CfgVehicles\RHS_su25_base\WingVortices [Indent level: 1],
    "WingVortices": {
        # Class: CfgVehicles\RHS_su25_base\WingVortices\WingTipLeft [Indent level: 2]
        "WingTipLeft": {
            "effectName": "WingVortices",
            "position": "cerveny pozicni"
        },
        # Class: CfgVehicles\RHS_su25_base\WingVortices\WingTipRight [Indent level: 2],
        "WingTipRight": {
            "effectName": "WingVortices",
            "position": "zeleny pozicni"
        },
        # Class: CfgVehicles\RHS_su25_base\WingVortices\BodyLeft [Indent level: 2],
        "BodyLeft": {
            "effectName": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles\RHS_su25_base\WingVortices\BodyRight [Indent level: 2],
        "BodyRight": {
            "effectName": "BodyVortices",
            "position": "body_vapour_R_S"
        }
    },
    "threat": [1,1,1],
    "driveOnComponent": ["gear_f1","gear_l1","gear_r1"],
    "defaultUserMFDvalues": [0,0,0,0,0,0],
    # Class: CfgVehicles\RHS_su25_base\MFD [Indent level: 1],
    "MFD": {
        # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD [Indent level: 2]
        "AirplaneHUD": {
            "enableParallax": 1,
            "topLeft": "HUD LH",
            "topRight": "HUD PH",
            "bottomLeft": "HUD LD",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Pos10Vector [Indent level: 3],
            "Pos10Vector": {
                "pos0": [0.52,0.03],
                "pos10": [2.02,1.23],
                "type": "vector"
            },
            "color": [0,1,0,0.1],
            # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones [Indent level: 3],
            "Bones": {
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\PlaneW [Indent level: 4]
                "PlaneW": {
                    "pos": [0.5,0.5],
                    "type": "fixed"
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\HorizonBankMGun [Indent level: 4],
                "HorizonBankMGun": {
                    "center": [0,0],
                    "type": "rotational",
                    "source": "HorizonBank",
                    "min": -6.28319,
                    "max": 6.28319,
                    "minAngle": -360,
                    "maxAngle": 360,
                    "aspectRatio": 0.8
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\HorizonBankReverted [Indent level: 4],
                "HorizonBankReverted": {
                    "pos0": [-0,-0],
                    "pos10": [0,0],
                    "center": [0,0],
                    "type": "rotational",
                    "source": "HorizonBank",
                    "min": -6.28319,
                    "max": 6.28319,
                    "minAngle": 360,
                    "maxAngle": -360,
                    "aspectRatio": 0.8
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\ImpactPoint [Indent level: 4],
                "ImpactPoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.23],
                    "pos10": [1.38,1.46]
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\TargetingPodDir [Indent level: 4],
                "TargetingPodDir": {
                    "type": "vector",
                    "source": "pilotcamera",
                    "pos0": ["0.50+0.034","0.27-0.0455"],
                    "pos10": [2.02,1.47]
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\TargetingPodTarget [Indent level: 4],
                "TargetingPodTarget": {
                    "type": "vector",
                    "source": "pilotcamera",
                    "pos0": ["0.50+0.034","0.27-0.0455"],
                    "pos10": [2.02,1.47]
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot1 [Indent level: 4],
                "MissileFlightTimeRot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minAngle": 0,
                    "maxAngle": 18,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot2 [Indent level: 4],
                "MissileFlightTimeRot2": {
                    "maxAngle": 37,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot3 [Indent level: 4],
                "MissileFlightTimeRot3": {
                    "maxAngle": 55.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot4 [Indent level: 4],
                "MissileFlightTimeRot4": {
                    "maxAngle": 74,
                    "max": 12,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot5 [Indent level: 4],
                "MissileFlightTimeRot5": {
                    "maxAngle": 92.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot6 [Indent level: 4],
                "MissileFlightTimeRot6": {
                    "maxAngle": 111,
                    "max": 18,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot7 [Indent level: 4],
                "MissileFlightTimeRot7": {
                    "maxAngle": 129.5,
                    "max": 21,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot8 [Indent level: 4],
                "MissileFlightTimeRot8": {
                    "maxAngle": 148,
                    "max": 24,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot9 [Indent level: 4],
                "MissileFlightTimeRot9": {
                    "maxAngle": 166.5,
                    "max": 27,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot10 [Indent level: 4],
                "MissileFlightTimeRot10": {
                    "maxAngle": 185,
                    "max": 30,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot11 [Indent level: 4],
                "MissileFlightTimeRot11": {
                    "maxAngle": 203.5,
                    "max": 33,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot12 [Indent level: 4],
                "MissileFlightTimeRot12": {
                    "maxAngle": 222,
                    "max": 36,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot13 [Indent level: 4],
                "MissileFlightTimeRot13": {
                    "maxAngle": 240.5,
                    "max": 39,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot14 [Indent level: 4],
                "MissileFlightTimeRot14": {
                    "maxAngle": 259,
                    "max": 42,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot15 [Indent level: 4],
                "MissileFlightTimeRot15": {
                    "maxAngle": 277.5,
                    "max": 45,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot16 [Indent level: 4],
                "MissileFlightTimeRot16": {
                    "maxAngle": 296,
                    "max": 48,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot17 [Indent level: 4],
                "MissileFlightTimeRot17": {
                    "maxAngle": 314.5,
                    "max": 51,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot18 [Indent level: 4],
                "MissileFlightTimeRot18": {
                    "maxAngle": 333,
                    "max": 54,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot19 [Indent level: 4],
                "MissileFlightTimeRot19": {
                    "maxAngle": 351.5,
                    "max": 57,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\MissileFlightTimeRot20 [Indent level: 4],
                "MissileFlightTimeRot20": {
                    "maxAngle": 370,
                    "max": 60,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 2.5,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot1 [Indent level: 4],
                "UserRot1": {
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minAngle": 0,
                    "maxAngle": 18,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot2 [Indent level: 4],
                "UserRot2": {
                    "maxAngle": 37,
                    "max": 6,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot3 [Indent level: 4],
                "UserRot3": {
                    "maxAngle": 55.5,
                    "max": 9,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot4 [Indent level: 4],
                "UserRot4": {
                    "maxAngle": 74,
                    "max": 12,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot5 [Indent level: 4],
                "UserRot5": {
                    "maxAngle": 92.5,
                    "max": 15,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot6 [Indent level: 4],
                "UserRot6": {
                    "maxAngle": 111,
                    "max": 18,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot7 [Indent level: 4],
                "UserRot7": {
                    "maxAngle": 129.5,
                    "max": 21,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot8 [Indent level: 4],
                "UserRot8": {
                    "maxAngle": 148,
                    "max": 24,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot9 [Indent level: 4],
                "UserRot9": {
                    "maxAngle": 166.5,
                    "max": 27,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot10 [Indent level: 4],
                "UserRot10": {
                    "maxAngle": 185,
                    "max": 30,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot11 [Indent level: 4],
                "UserRot11": {
                    "maxAngle": 203.5,
                    "max": 33,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot12 [Indent level: 4],
                "UserRot12": {
                    "maxAngle": 222,
                    "max": 36,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot13 [Indent level: 4],
                "UserRot13": {
                    "maxAngle": 240.5,
                    "max": 39,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot14 [Indent level: 4],
                "UserRot14": {
                    "maxAngle": 259,
                    "max": 42,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot15 [Indent level: 4],
                "UserRot15": {
                    "maxAngle": 277.5,
                    "max": 45,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot16 [Indent level: 4],
                "UserRot16": {
                    "maxAngle": 296,
                    "max": 48,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot17 [Indent level: 4],
                "UserRot17": {
                    "maxAngle": 314.5,
                    "max": 51,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot18 [Indent level: 4],
                "UserRot18": {
                    "maxAngle": 333,
                    "max": 54,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot19 [Indent level: 4],
                "UserRot19": {
                    "maxAngle": 351.5,
                    "max": 57,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Bones\UserRot20 [Indent level: 4],
                "UserRot20": {
                    "maxAngle": 370,
                    "max": 60,
                    "type": "rotational",
                    "source": "user",
                    "sourceIndex": 4,
                    "sourceScale": 0.004,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 0.840909
                }
            },
            # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw [Indent level: 3],
            "Draw": {
                "color": [0.69,0.22,0],
                "alpha": 1,
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\ImpactPoint [Indent level: 4],
                "ImpactPoint": {
                    "condition": "1 - atmissile",
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\ImpactPoint\Cros [Indent level: 5],
                    "Cros": {
                        "type": "line",
                        "points": [["ImpactPoint",1,[0.111111,0],1],["ImpactPoint",1,[0.0277778,0],1],[],["ImpactPoint",1,[-0.111111,0],1],["ImpactPoint",1,[-0.0277778,0],1],[],["ImpactPoint",1,[0,0.0934343],1],["ImpactPoint",1,[0,0.0233586],1],[],["ImpactPoint",1,[0,-0.0934343],1],["ImpactPoint",1,[0,-0.0233586],1],[]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\ImpactPoint\Dot [Indent level: 5],
                    "Dot": {
                        "type": "line",
                        "points": [["ImpactPoint",[0,0.0035],1],["ImpactPoint",[0.0035,-0],1],["ImpactPoint",[0,-0.0035],1],["ImpactPoint",[-0.0035,-0],1],["ImpactPoint",[0,0.0035],1]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\ImpactPoint\Ring [Indent level: 5],
                    "Ring": {
                        "type": "line",
                        "points": [["ImpactPoint",[0.187939,0.0575216],1],["ImpactPoint",[0.193185,0.0435287],1],["ImpactPoint",[0.196962,0.0292045],1],["ImpactPoint",[0.199239,0.014658],1],["ImpactPoint",[0.2,7.35146e-009],1],["ImpactPoint",[0.199239,-0.014658],1],["ImpactPoint",[0.196962,-0.0292045],1],["ImpactPoint",[0.193185,-0.0435286],1],["ImpactPoint",[0.187939,-0.0575216],1],["ImpactPoint",[0.181262,-0.0710767],1],["ImpactPoint",[0.173205,-0.0840909],1],["ImpactPoint",[0.16383,-0.0964651],1],["ImpactPoint",[0.153209,-0.108105],1],["ImpactPoint",[0.141421,-0.118923],1],["ImpactPoint",[0.128558,-0.128835],1],["ImpactPoint",[0.114715,-0.137766],1],["ImpactPoint",[0.1,-0.14565],1],["ImpactPoint",[0.0845237,-0.152424],1],["ImpactPoint",[0.068404,-0.158039],1],["ImpactPoint",[0.0517638,-0.162451],1],["ImpactPoint",[0.0347296,-0.165627],1],["ImpactPoint",[0.0174311,-0.167542],1],["ImpactPoint",[0,-0.168182],1],[],["ImpactPoint",[0.187939,0.0575216],1],["ImpactPoint",[0.169145,0.0517694],1],[],["ImpactPoint",[0.196962,0.0292045],1],["ImpactPoint",[0.187113,0.0277442],1],[],["ImpactPoint",[0.2,7.35146e-009],1],["ImpactPoint",[0.18,6.61632e-009],1],[],["ImpactPoint",[0.196962,-0.0292045],1],["ImpactPoint",[0.187113,-0.0277442],1],[],["ImpactPoint",[0.187939,-0.0575216],1],["ImpactPoint",[0.178542,-0.0546455],1],[],["ImpactPoint",[0.173205,-0.0840909],1],["ImpactPoint",[0.155885,-0.0756818],1],[],["ImpactPoint",[0.153209,-0.108105],1],["ImpactPoint",[0.145548,-0.1027],1],[],["ImpactPoint",[0.128558,-0.128835],1],["ImpactPoint",[0.12213,-0.122393],1],[],["ImpactPoint",[0.1,-0.14565],1],["ImpactPoint",[0.09,-0.131085],1],[],["ImpactPoint",[0.068404,-0.158039],1],["ImpactPoint",[0.0649838,-0.150137],1],[],["ImpactPoint",[0.0347296,-0.165627],1],["ImpactPoint",[0.0329932,-0.157345],1],[],["ImpactPoint",[0,-0.168182],1],["ImpactPoint",[0,-0.151364],1],[]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\ImpactPoint\Triangle [Indent level: 5],
                    "Triangle": {
                        "type": "line",
                        "width": 9,
                        "points": [["ImpactPoint",1,["HorizonBankReverted",0,0.192],1],["ImpactPoint",1,["HorizonBankReverted",0.01,0.177],1],["ImpactPoint",1,["HorizonBankReverted",-0.01,0.177],1],["ImpactPoint",1,["HorizonBankReverted",0,0.192],1]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\ImpactPoint\LaunchAutorization [Indent level: 5],
                    "LaunchAutorization": {
                        "type": "line",
                        "width": 14,
                        "points": [["ImpactPoint",[0,-0.172386],1],["MissileFlightTimeRot1",[0,0.205],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.205],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.205],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.205],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.205],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.205],1,"ImpactPoint",1]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\ImpactPoint\LaunchAutorizationBig [Indent level: 5],
                    "LaunchAutorizationBig": {
                        "type": "line",
                        "width": 24,
                        "points": [["MissileFlightTimeRot1",[0,0.215],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.215],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.215],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.215],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.215],1,"ImpactPoint",1]]
                    }
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPod [Indent level: 4],
                "TargetingPod": {
                    "condition": "atmissile-pilotcameralock",
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPod\Cros [Indent level: 5],
                    "Cros": {
                        "type": "line",
                        "points": [["TargetingPodDir",1,[0.111111,0],1],["TargetingPodDir",1,[0.0277778,0],1],[],["TargetingPodDir",1,[-0.111111,0],1],["TargetingPodDir",1,[-0.0277778,0],1],[],["TargetingPodDir",1,[0,0.0934343],1],["TargetingPodDir",1,[0,0.0233586],1],[],["TargetingPodDir",1,[0,-0.0934343],1],["TargetingPodDir",1,[0,-0.0233586],1],[]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPod\Dot [Indent level: 5],
                    "Dot": {
                        "type": "line",
                        "points": [["TargetingPodDir",[0,0.0035],1],["TargetingPodDir",[0.0035,-0],1],["TargetingPodDir",[0,-0.0035],1],["TargetingPodDir",[-0.0035,-0],1],["TargetingPodDir",[0,0.0035],1]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPod\Ring [Indent level: 5],
                    "Ring": {
                        "type": "line",
                        "points": [["TargetingPodDir",[0.187939,0.0575216],1],["TargetingPodDir",[0.193185,0.0435287],1],["TargetingPodDir",[0.196962,0.0292045],1],["TargetingPodDir",[0.199239,0.014658],1],["TargetingPodDir",[0.2,7.35146e-009],1],["TargetingPodDir",[0.199239,-0.014658],1],["TargetingPodDir",[0.196962,-0.0292045],1],["TargetingPodDir",[0.193185,-0.0435286],1],["TargetingPodDir",[0.187939,-0.0575216],1],["TargetingPodDir",[0.181262,-0.0710767],1],["TargetingPodDir",[0.173205,-0.0840909],1],["TargetingPodDir",[0.16383,-0.0964651],1],["TargetingPodDir",[0.153209,-0.108105],1],["TargetingPodDir",[0.141421,-0.118923],1],["TargetingPodDir",[0.128558,-0.128835],1],["TargetingPodDir",[0.114715,-0.137766],1],["TargetingPodDir",[0.1,-0.14565],1],["TargetingPodDir",[0.0845237,-0.152424],1],["TargetingPodDir",[0.068404,-0.158039],1],["TargetingPodDir",[0.0517638,-0.162451],1],["TargetingPodDir",[0.0347296,-0.165627],1],["TargetingPodDir",[0.0174311,-0.167542],1],["TargetingPodDir",[0,-0.168182],1],[],["TargetingPodDir",[0.187939,0.0575216],1],["TargetingPodDir",[0.169145,0.0517694],1],[],["TargetingPodDir",[0.196962,0.0292045],1],["TargetingPodDir",[0.187113,0.0277442],1],[],["TargetingPodDir",[0.2,7.35146e-009],1],["TargetingPodDir",[0.18,6.61632e-009],1],[],["TargetingPodDir",[0.196962,-0.0292045],1],["TargetingPodDir",[0.187113,-0.0277442],1],[],["TargetingPodDir",[0.187939,-0.0575216],1],["TargetingPodDir",[0.178542,-0.0546455],1],[],["TargetingPodDir",[0.173205,-0.0840909],1],["TargetingPodDir",[0.155885,-0.0756818],1],[],["TargetingPodDir",[0.153209,-0.108105],1],["TargetingPodDir",[0.145548,-0.1027],1],[],["TargetingPodDir",[0.128558,-0.128835],1],["TargetingPodDir",[0.12213,-0.122393],1],[],["TargetingPodDir",[0.1,-0.14565],1],["TargetingPodDir",[0.09,-0.131085],1],[],["TargetingPodDir",[0.068404,-0.158039],1],["TargetingPodDir",[0.0649838,-0.150137],1],[],["TargetingPodDir",[0.0347296,-0.165627],1],["TargetingPodDir",[0.0329932,-0.157345],1],[],["TargetingPodDir",[0,-0.168182],1],["TargetingPodDir",[0,-0.151364],1],[]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPod\Triangle [Indent level: 5],
                    "Triangle": {
                        "type": "line",
                        "width": 9,
                        "points": [["TargetingPodDir",1,["HorizonBankReverted",0,0.192],1],["TargetingPodDir",1,["HorizonBankReverted",0.01,0.177],1],["TargetingPodDir",1,["HorizonBankReverted",-0.01,0.177],1],["TargetingPodDir",1,["HorizonBankReverted",0,0.192],1]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPod\LaunchAutorization [Indent level: 5],
                    "LaunchAutorization": {
                        "type": "line",
                        "width": 14,
                        "points": [["TargetingPodDir",[0,-0.172386],1],["UserRot1",[0,0.205],1,"TargetingPodDir",1],["UserRot2",[0,0.205],1,"TargetingPodDir",1],["UserRot3",[0,0.205],1,"TargetingPodDir",1],["UserRot4",[0,0.205],1,"TargetingPodDir",1],["UserRot5",[0,0.205],1,"TargetingPodDir",1],["UserRot6",[0,0.205],1,"TargetingPodDir",1]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPod\LaunchAutorizationBig [Indent level: 5],
                    "LaunchAutorizationBig": {
                        "type": "line",
                        "width": 24,
                        "points": [["UserRot1",[0,0.215],1,"TargetingPodDir",1],["UserRot2",[0,0.215],1,"TargetingPodDir",1],["UserRot3",[0,0.215],1,"TargetingPodDir",1],["UserRot4",[0,0.215],1,"TargetingPodDir",1],["UserRot5",[0,0.215],1,"TargetingPodDir",1]]
                    }
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPodTarget [Indent level: 4],
                "TargetingPodTarget": {
                    "condition": "(atmissile)*(pilotcameralock>=0)*laseron",
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPodTarget\Cros [Indent level: 5],
                    "Cros": {
                        "type": "line",
                        "points": [["TargetingPodTarget",1,[0.111111,0],1],["TargetingPodTarget",1,[0.0277778,0],1],[],["TargetingPodTarget",1,[-0.111111,0],1],["TargetingPodTarget",1,[-0.0277778,0],1],[],["TargetingPodTarget",1,[0,0.0934343],1],["TargetingPodTarget",1,[0,0.0233586],1],[],["TargetingPodTarget",1,[0,-0.0934343],1],["TargetingPodTarget",1,[0,-0.0233586],1],[]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPodTarget\Dot [Indent level: 5],
                    "Dot": {
                        "type": "line",
                        "points": [["TargetingPodTarget",[0,0.0035],1],["TargetingPodTarget",[0.0035,-0],1],["TargetingPodTarget",[0,-0.0035],1],["TargetingPodTarget",[-0.0035,-0],1],["TargetingPodTarget",[0,0.0035],1]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPodTarget\Ring [Indent level: 5],
                    "Ring": {
                        "type": "line",
                        "points": [["TargetingPodTarget",[0.187939,0.0575216],1],["TargetingPodTarget",[0.193185,0.0435287],1],["TargetingPodTarget",[0.196962,0.0292045],1],["TargetingPodTarget",[0.199239,0.014658],1],["TargetingPodTarget",[0.2,7.35146e-009],1],["TargetingPodTarget",[0.199239,-0.014658],1],["TargetingPodTarget",[0.196962,-0.0292045],1],["TargetingPodTarget",[0.193185,-0.0435286],1],["TargetingPodTarget",[0.187939,-0.0575216],1],["TargetingPodTarget",[0.181262,-0.0710767],1],["TargetingPodTarget",[0.173205,-0.0840909],1],["TargetingPodTarget",[0.16383,-0.0964651],1],["TargetingPodTarget",[0.153209,-0.108105],1],["TargetingPodTarget",[0.141421,-0.118923],1],["TargetingPodTarget",[0.128558,-0.128835],1],["TargetingPodTarget",[0.114715,-0.137766],1],["TargetingPodTarget",[0.1,-0.14565],1],["TargetingPodTarget",[0.0845237,-0.152424],1],["TargetingPodTarget",[0.068404,-0.158039],1],["TargetingPodTarget",[0.0517638,-0.162451],1],["TargetingPodTarget",[0.0347296,-0.165627],1],["TargetingPodTarget",[0.0174311,-0.167542],1],["TargetingPodTarget",[0,-0.168182],1],[],["TargetingPodTarget",[0.187939,0.0575216],1],["TargetingPodTarget",[0.169145,0.0517694],1],[],["TargetingPodTarget",[0.196962,0.0292045],1],["TargetingPodTarget",[0.187113,0.0277442],1],[],["TargetingPodTarget",[0.2,7.35146e-009],1],["TargetingPodTarget",[0.18,6.61632e-009],1],[],["TargetingPodTarget",[0.196962,-0.0292045],1],["TargetingPodTarget",[0.187113,-0.0277442],1],[],["TargetingPodTarget",[0.187939,-0.0575216],1],["TargetingPodTarget",[0.178542,-0.0546455],1],[],["TargetingPodTarget",[0.173205,-0.0840909],1],["TargetingPodTarget",[0.155885,-0.0756818],1],[],["TargetingPodTarget",[0.153209,-0.108105],1],["TargetingPodTarget",[0.145548,-0.1027],1],[],["TargetingPodTarget",[0.128558,-0.128835],1],["TargetingPodTarget",[0.12213,-0.122393],1],[],["TargetingPodTarget",[0.1,-0.14565],1],["TargetingPodTarget",[0.09,-0.131085],1],[],["TargetingPodTarget",[0.068404,-0.158039],1],["TargetingPodTarget",[0.0649838,-0.150137],1],[],["TargetingPodTarget",[0.0347296,-0.165627],1],["TargetingPodTarget",[0.0329932,-0.157345],1],[],["TargetingPodTarget",[0,-0.168182],1],["TargetingPodTarget",[0,-0.151364],1],[]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPodTarget\Triangle [Indent level: 5],
                    "Triangle": {
                        "type": "line",
                        "width": 9,
                        "points": [["TargetingPodTarget",1,["HorizonBankReverted",0,0.192],1],["TargetingPodTarget",1,["HorizonBankReverted",0.01,0.177],1],["TargetingPodTarget",1,["HorizonBankReverted",-0.01,0.177],1],["TargetingPodTarget",1,["HorizonBankReverted",0,0.192],1]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPodTarget\LaunchAutorization [Indent level: 5],
                    "LaunchAutorization": {
                        "type": "line",
                        "width": 14,
                        "points": [["TargetingPodTarget",[0,-0.172386],1],["UserRot1",[0,0.205],1,"TargetingPodTarget",1],["UserRot2",[0,0.205],1,"TargetingPodTarget",1],["UserRot3",[0,0.205],1,"TargetingPodTarget",1],["UserRot4",[0,0.205],1,"TargetingPodTarget",1],["UserRot5",[0,0.205],1,"TargetingPodTarget",1],["UserRot6",[0,0.205],1,"TargetingPodTarget",1]]
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\TargetingPodTarget\LaunchAutorizationBig [Indent level: 5],
                    "LaunchAutorizationBig": {
                        "type": "line",
                        "width": 24,
                        "points": [["UserRot1",[0,0.215],1,"TargetingPodTarget",1],["UserRot2",[0,0.215],1,"TargetingPodTarget",1],["UserRot3",[0,0.215],1,"TargetingPodTarget",1],["UserRot4",[0,0.215],1,"TargetingPodTarget",1],["UserRot5",[0,0.215],1,"TargetingPodTarget",1]]
                    }
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\StaticReticle [Indent level: 4],
                "StaticReticle": {
                    "condition": "user5",
                    # Class: CfgVehicles\RHS_su25_base\MFD\AirplaneHUD\Draw\StaticReticle\Shape [Indent level: 5],
                    "Shape": {
                        "type": "polygon",
                        "texture": "rhsafrf|addons|rhs_c_a2port_air|Su25|rhs_su25_reticle_static_ca.paa",
                        "points": [[[[0.055,0.145],1],[[0.955,0.145],1],[[0.955,0.845],1],[[0.055,0.845],1]]]
                    }
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1 [Indent level: 2],
        "MFD_1": {
            "topLeft": "MFD_WS_TL",
            "topRight": "MFD_WS_TR",
            "bottomLeft": "MFD_WS_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            "font": "PuristaMedium",
            # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw [Indent level: 3],
            "Draw": {
                "alpha": 0.5,
                "color": [1,1,1],
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo [Indent level: 4],
                "MgunAmmo": {
                    "condition": "ammo2>=1",
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo\BlackBackground [Indent level: 5],
                    "BlackBackground": {
                        "color": [0,0,0],
                        "alpha": 1,
                        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo\BlackBackground\AmmoBox [Indent level: 6],
                        "AmmoBox": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0.838,0.825],1],[[0.922,0.825],1],[[0.922,0.975],1],[[0.838,0.975],1]]]
                        }
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo\Full [Indent level: 5],
                    "Full": {
                        "condition": "ammo2>=212",
                        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo\Full\AmmoText [Indent level: 6],
                        "AmmoText": {
                            "type": "text",
                            "source": "static",
                            "text": "К",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0.875,0.82],1],
                            "right": [[0.91,0.82],1],
                            "down": [[0.875,0.96],1]
                        }
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo\AlmostFull [Indent level: 5],
                    "AlmostFull": {
                        "condition": "(ammo2>=137)*(ammo2<=211)",
                        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo\AlmostFull\AmmoText [Indent level: 6],
                        "AmmoText": {
                            "type": "text",
                            "source": "static",
                            "text": "3/4",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0.875,0.82],1],
                            "right": [[0.91,0.82],1],
                            "down": [[0.875,0.96],1]
                        }
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo\Half [Indent level: 5],
                    "Half": {
                        "condition": "(ammo2>=63)*(ammo2<=136)",
                        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo\Half\AmmoText [Indent level: 6],
                        "AmmoText": {
                            "type": "text",
                            "source": "static",
                            "text": "1/2",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0.875,0.82],1],
                            "right": [[0.91,0.82],1],
                            "down": [[0.875,0.96],1]
                        }
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo\AlmostEmpty [Indent level: 5],
                    "AlmostEmpty": {
                        "condition": "(ammo2<=62)",
                        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\MgunAmmo\AlmostEmpty\AmmoText [Indent level: 6],
                        "AmmoText": {
                            "type": "text",
                            "source": "static",
                            "text": "1/4",
                            "scale": 1,
                            "sourceScale": 1,
                            "align": "center",
                            "pos": [[0.875,0.82],1],
                            "right": [[0.91,0.82],1],
                            "down": [[0.875,0.96],1]
                        }
                    }
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeRocket [Indent level: 4],
                "WeaponTypeRocket": {
                    "condition": "rocket",
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeRocket\BlackBackground [Indent level: 5],
                    "BlackBackground": {
                        "color": [0,0,0],
                        "alpha": 1,
                        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeRocket\BlackBackground\AmmoBox [Indent level: 6],
                        "AmmoBox": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0.838,0.125],1],[[0.922,0.125],1],[[0.922,0.275],1],[[0.838,0.275],1]]]
                        }
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeRocket\AmmoText [Indent level: 5],
                    "AmmoText": {
                        "type": "text",
                        "source": "static",
                        "text": "НРС",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[0.875,0.11],1],
                        "right": [[0.91,0.11],1],
                        "down": [[0.875,0.25],1]
                    }
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeMissiles [Indent level: 4],
                "WeaponTypeMissiles": {
                    "condition": "missile",
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeMissiles\BlackBackground [Indent level: 5],
                    "BlackBackground": {
                        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeMissiles\BlackBackground\AmmoBox [Indent level: 6]
                        "AmmoBox": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0.838,0.125],1],[[0.922,0.125],1],[[0.922,0.275],1],[[0.838,0.275],1]]]
                        },
                        "color": [0,0,0],
                        "alpha": 1
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeMissiles\AmmoText [Indent level: 5],
                    "AmmoText": {
                        "type": "text",
                        "source": "static",
                        "text": "УР",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[0.875,0.11],1],
                        "right": [[0.91,0.11],1],
                        "down": [[0.875,0.25],1]
                    }
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeBombs [Indent level: 4],
                "WeaponTypeBombs": {
                    "condition": "bomb",
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeBombs\BlackBackground [Indent level: 5],
                    "BlackBackground": {
                        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeBombs\BlackBackground\AmmoBox [Indent level: 6]
                        "AmmoBox": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0.838,0.125],1],[[0.922,0.125],1],[[0.922,0.275],1],[[0.838,0.275],1]]]
                        },
                        "color": [0,0,0],
                        "alpha": 1
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeBombs\AmmoText [Indent level: 5],
                    "AmmoText": {
                        "type": "text",
                        "source": "static",
                        "text": "Б",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[0.875,0.11],1],
                        "right": [[0.91,0.11],1],
                        "down": [[0.875,0.25],1]
                    }
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeMgun [Indent level: 4],
                "WeaponTypeMgun": {
                    "condition": "mgun",
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeMgun\BlackBackground [Indent level: 5],
                    "BlackBackground": {
                        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeMgun\BlackBackground\AmmoBox [Indent level: 6]
                        "AmmoBox": {
                            "type": "polygon",
                            "width": 4,
                            "points": [[[[0.838,0.125],1],[[0.922,0.125],1],[[0.922,0.275],1],[[0.838,0.275],1]]]
                        },
                        "color": [0,0,0],
                        "alpha": 1
                    },
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\WeaponTypeMgun\AmmoText [Indent level: 5],
                    "AmmoText": {
                        "type": "text",
                        "source": "static",
                        "text": "ВПУ",
                        "scale": 1,
                        "sourceScale": 1,
                        "align": "center",
                        "pos": [[0.875,0.11],1],
                        "right": [[0.91,0.11],1],
                        "down": [[0.875,0.25],1]
                    }
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\Pylon1 [Indent level: 4],
                "Pylon1": {
                    "type": "pylonicon",
                    "pos": [[0.345,0.34],1],
                    "pylon": 1,
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\Pylon2 [Indent level: 4],
                "Pylon2": {
                    "pylon": 2,
                    "pos": [[0.405,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\Pylon3 [Indent level: 4],
                "Pylon3": {
                    "pylon": 3,
                    "pos": [[0.281,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\Pylon4 [Indent level: 4],
                "Pylon4": {
                    "pylon": 4,
                    "pos": [[0.469,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\Pylon5 [Indent level: 4],
                "Pylon5": {
                    "pylon": 5,
                    "pos": [[0.217,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\Pylon6 [Indent level: 4],
                "Pylon6": {
                    "pylon": 6,
                    "pos": [[0.533,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\Pylon7 [Indent level: 4],
                "Pylon7": {
                    "pylon": 7,
                    "pos": [[0.153,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\Pylon8 [Indent level: 4],
                "Pylon8": {
                    "pylon": 8,
                    "pos": [[0.597,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\Pylon9 [Indent level: 4],
                "Pylon9": {
                    "pylon": 9,
                    "pos": [[0.094,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_1\Draw\Pylon10 [Indent level: 4],
                "Pylon10": {
                    "pylon": 10,
                    "pos": [[0.661,0.32],1],
                    "type": "pylonicon",
                    "name": "rhs_su25_box"
                }
            }
        },
        # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2 [Indent level: 2],
        "MFD_2": {
            "topLeft": "MFD_Lights_TL",
            "topRight": "MFD_Lights_TR",
            "bottomLeft": "MFD_Lights_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.15,1,0.15,1],
            "enableParallax": 0,
            # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2\Draw [Indent level: 3],
            "Draw": {
                "alpha": 1,
                "color": [1,1,1],
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2\Draw\Launch_Authorized [Indent level: 4],
                "Launch_Authorized": {
                    "condition": "((impactDistance/LarTop)>=LarAmmoMin)*((impactDistance/LarTop)<=LarAmmoMax)+(user1>=1)+missilelocked",
                    "color": [0.69,0.22,0],
                    "alpha": 0.2,
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2\Draw\Launch_Authorized\Bulb [Indent level: 5],
                    "Bulb": {
                        "type": "polygon",
                        "texture": "a3|Data_f|light_flare_ca.paa",
                        "points": [[[[0.898,0.085],1],[[0.982,0.085],1],[[0.982,0.515],1],[[0.898,0.515],1]]]
                    }
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2\Draw\Laser_Active [Indent level: 4],
                "Laser_Active": {
                    "color": [0,0.49,0],
                    "alpha": 0.1,
                    "condition": "laseron",
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2\Draw\Laser_Active\Bulb [Indent level: 5],
                    "Bulb": {
                        "type": "polygon",
                        "texture": "a3|Data_f|light_flare_ca.paa",
                        "points": [[[[0.018,0.085],1],[[0.102,0.085],1],[[0.102,0.515],1],[[0.018,0.515],1]]]
                    }
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2\Draw\Laser_Cooldown [Indent level: 4],
                "Laser_Cooldown": {
                    "condition": "user0",
                    "blinkingPattern": [0.3,0.3],
                    "blinkingStartsOn": 1,
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2\Draw\Laser_Cooldown\Bulb [Indent level: 5],
                    "Bulb": {
                        "type": "polygon",
                        "texture": "a3|Data_f|light_flare_ca.paa",
                        "points": [[[[0.018,0.085],1],[[0.102,0.085],1],[[0.102,0.515],1],[[0.018,0.515],1]]]
                    },
                    "color": [0,0.49,0],
                    "alpha": 0.1
                },
                # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2\Draw\Launch_Disengage [Indent level: 4],
                "Launch_Disengage": {
                    "condition": "(((impactDistance/LarTop)<=LarAmmoMin)+((impactDistance/LarTop)>=LarAmmoMax))*rocket+(user1<=-1)",
                    "color": [0.94,0.01,0],
                    "alpha": 0.07,
                    # Class: CfgVehicles\RHS_su25_base\MFD\MFD_2\Draw\Launch_Disengage\Bulb [Indent level: 5],
                    "Bulb": {
                        "type": "polygon",
                        "texture": "a3|Data_f|light_flare_ca.paa",
                        "points": [[[[0.018,0.485],1],[[0.102,0.485],1],[[0.102,0.915],1],[[0.018,0.915],1]]]
                    }
                }
            }
        }
    },
    "maxOmega": 2000,
    "engineMOI": 16,
    # Class: CfgVehicles\RHS_su25_base\Wheels [Indent level: 1],
    "Wheels": {
        "disableWheelsWhenDestroyed": 1,
        # Class: CfgVehicles\RHS_su25_base\Wheels\Wheel_1 [Indent level: 2],
        "Wheel_1": {
            "side": "left",
            "boneName": "Wheel_1",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "suspForceAppPointOffset": "Wheel_1_center",
            "tireForceAppPointOffset": "Wheel_1_center",
            "suspTravelDirection": [0,-1,0],
            "steering": 1,
            "width": 0.16,
            "mass": 150,
            "MOI": 40,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 21500,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.2105,
            "maxDroop": 0.015,
            "sprungMass": 4066,
            "springStrength": 56600,
            "springDamperRate": 215570,
            "longitudinalStiffnessPerUnitGravity": 8000,
            "latStiffX": 25,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\RHS_su25_base\Wheels\Wheel_1_fake [Indent level: 2],
        "Wheel_1_fake": {
            "side": "left",
            "boneName": "Wheel_1",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "suspForceAppPointOffset": "Wheel_1_center",
            "tireForceAppPointOffset": "Wheel_1_center",
            "suspTravelDirection": [0,-1,0],
            "steering": 1,
            "width": 0.16,
            "mass": 150,
            "MOI": 40,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 21500,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.2105,
            "maxDroop": 0.015,
            "sprungMass": 4066,
            "springStrength": 56600,
            "springDamperRate": 215570,
            "longitudinalStiffnessPerUnitGravity": 8000,
            "latStiffX": 25,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\RHS_su25_base\Wheels\Wheel_2 [Indent level: 2],
        "Wheel_2": {
            "boneName": "Wheel_2",
            "steering": 0,
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "width": 0.28,
            "springDamperRate": 220570,
            "sprungMass": 6652,
            "springStrength": 151000,
            "suspForceAppPointOffset": "Wheel_2_center",
            "tireForceAppPointOffset": "Wheel_2_center",
            "side": "left",
            "suspTravelDirection": [0,-1,0],
            "mass": 150,
            "MOI": 40,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 21500,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.2105,
            "maxDroop": 0.015,
            "longitudinalStiffnessPerUnitGravity": 8000,
            "latStiffX": 25,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\RHS_su25_base\Wheels\Wheel_3 [Indent level: 2],
        "Wheel_3": {
            "boneName": "Wheel_3",
            "side": "right",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspForceAppPointOffset": "Wheel_3_center",
            "tireForceAppPointOffset": "Wheel_3_center",
            "steering": 0,
            "width": 0.28,
            "springDamperRate": 220570,
            "sprungMass": 6652,
            "springStrength": 151000,
            "suspTravelDirection": [0,-1,0],
            "mass": 150,
            "MOI": 40,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 21500,
            "maxHandBrakeTorque": 0,
            "maxCompression": 0.2105,
            "maxDroop": 0.015,
            "longitudinalStiffnessPerUnitGravity": 8000,
            "latStiffX": 25,
            "latStiffY": 180,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    "maxSpeed": 900,
    "landingAoa": 0.113446,
    "landingSpeed": 250,
    "stallSpeed": 190,
    "stallWarningTreshold": 0.07,
    "wheelSteeringSensitivity": 1.3,
    "airBrake": 1,
    "airBrakeFrictionCoef": 2.2,
    "flaps": 1,
    "flapsFrictionCoef": 0.32,
    "gearsUpFrictionCoef": 0.55,
    "airFrictionCoefs0": [0,0,0],
    "airFrictionCoefs1": [0.1,0.52,0.0067],
    "airFrictionCoefs2": [0.001,0.0054,7e-005],
    "angleOfIndicence": -0.00872665,
    "envelope": [0,0.07,0.28,0.83,1.11,1.74,2.51,3.41,4.46,5.64,6.96,8.42,8.8,9.11,9.38,9.45,9.43,9,8,7,6],
    "altNoForce": 15000,
    "altFullForce": 4000,
    "thrustCoef": [1.28,1.33,1.77,1.4,1.41,1.39,1.36,1.33,1.29,1.25,1.2,1.15,1.05,0.5,0,0,0,0,0],
    "aileronSensitivity": 0.85,
    "aileronCoef": [0,0.1,0.3,0.6,0.8,0.95,1,1.02,1.03,1.04,1.04,1,0.9,0.7,0.3,0.2,0.15,0.1,0.1],
    "elevatorSensitivity": 0.95,
    "elevatorCoef": [0,0.2,0.95,0.8,0.75,0.7,0.65,0.6,0.55,0.5,0.46,0.32,0.29,0.16,0.14,0.12,0.1,0.09,0.08],
    "rudderInfluence": 0.966,
    "rudderCoef": [0,0.6,1.2,1.5,1.8,2,3.2,3.4,3.45,3.5,3.55,3.6,2.2,1.3,0.3,0.2,0.15,0.1,0.1],
    "aileronControlsSensitivityCoef": 3.6,
    "elevatorControlsSensitivityCoef": 3.4,
    "rudderControlsSensitivityCoef": 3.4,
    "draconicForceXCoef": 13,
    "draconicForceYCoef": 1.3,
    "draconicForceZCoef": 1,
    "draconicTorqueXCoef": [4.8,5,5.5,6.2,6.6,7.4,8,8.5,8,8.4,8.6,8.7,8.8,8.9,9,9.1],
    "draconicTorqueYCoef": [12,7.5,4,1.5,0.1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    "soundIncommingMissile": ["|rhsafrf|addons|rhs_c_a2port_air|sounds|alarm_beep",1.09811,1],
    "soundLocked": ["",1.58489,1],
    # Class: CfgVehicles\RHS_su25_base\UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles\RHS_su25_base\UserActions\SAFEMODE [Indent level: 2]
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
        # Class: CfgVehicles\RHS_su25_base\UserActions\RETICLE [Indent level: 2],
        "RETICLE": {
            "displayName": "<t color='#FBB829'>Toggle reticle</t>",
            "position": "",
            "radius": 10,
            "priority": 10.5,
            "onlyforplayer": 1,
            "showWindow": 0,
            "hideOnUse": 1,
            "condition": "(call rhs_fnc_findPlayer) in this",
            "shortcut": "user10",
            "statement": "if(((getUserMFDvalue this) select 5) isEqualTo 0)then{this setUserMFDvalue [5,1];}else{this setUserMFDvalue [5,0];};"
        }
    },
    # Class: CfgVehicles\RHS_su25_base\EventHandlers [Indent level: 1],
    "EventHandlers": {
        "hit": "",
        # Class: CfgVehicles\RHS_su25_base\EventHandlers\RHS_EventHandlers [Indent level: 2],
        "RHS_EventHandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "init": "_this call rhs_fnc_air_init",
            "getout": "[_this select 0, _this select 2,'rhs_su25_canopy'] call rhs_fnc_K36D_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes;"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers [Indent level: 0],
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        },
        # Class: DefaultEventHandlers\CBA_Extended_EventHandlers [Indent level: 0],
        "CBA_Extended_EventHandlers": {
            "init": "call cba_xeh_fnc_init",
            "fired": "call cba_xeh_fnc_fired",
            "animChanged": "call cba_xeh_fnc_animChanged",
            "animDone": "call cba_xeh_fnc_animDone",
            "animStateChanged": "call cba_xeh_fnc_animStateChanged",
            "containerClosed": "call cba_xeh_fnc_containerClosed",
            "containerOpened": "call cba_xeh_fnc_containerOpened",
            "controlsShifted": "call cba_xeh_fnc_controlsShifted",
            "dammaged": "call cba_xeh_fnc_dammaged",
            "engine": "call cba_xeh_fnc_engine",
            "epeContact": "call cba_xeh_fnc_epeContact",
            "epeContactEnd": "call cba_xeh_fnc_epeContactEnd",
            "epeContactStart": "call cba_xeh_fnc_epeContactStart",
            "explosion": "call cba_xeh_fnc_explosion",
            "firedNear": "call cba_xeh_fnc_firedNear",
            "fuel": "call cba_xeh_fnc_cba_xeh_fuel",
            "gear": "call cba_xeh_fnc_gear",
            "getIn": "call cba_xeh_fnc_getIn",
            "getInMan": "call cba_xeh_fnc_getInMan",
            "getOut": "call cba_xeh_fnc_getOut",
            "getOutMan": "call cba_xeh_fnc_getOutMan",
            "handleHeal": "call cba_xeh_fnc_handleHeal",
            "hit": "call cba_xeh_fnc_hit",
            "hitPart": "call cba_xeh_fnc_hitPart",
            "incomingMissile": "call cba_xeh_fnc_incomingMissile",
            "inventoryClosed": "call cba_xeh_fnc_inventoryClosed",
            "inventoryOpened": "call cba_xeh_fnc_inventoryOpened",
            "killed": "call cba_xeh_fnc_killed",
            "landedTouchDown": "call cba_xeh_fnc_landedTouchDown",
            "landedStopped": "call cba_xeh_fnc_landedStopped",
            "local": "call cba_xeh_fnc_local",
            "respawn": "call cba_xeh_fnc_respawn",
            "put": "call cba_xeh_fnc_put",
            "take": "call cba_xeh_fnc_take",
            "seatSwitched": "call cba_xeh_fnc_seatSwitched",
            "seatSwitchedMan": "call cba_xeh_fnc_seatSwitchedMan",
            "soundPlayed": "call cba_xeh_fnc_soundPlayed",
            "weaponAssembled": "call cba_xeh_fnc_weaponAssembled",
            "weaponDisassembled": "call cba_xeh_fnc_weaponDisassembled",
            "weaponDeployed": "call cba_xeh_fnc_weaponDeployed",
            "weaponRested": "call cba_xeh_fnc_weaponRested",
            "reloaded": "call cba_xeh_fnc_reloaded",
            "firedMan": "call cba_xeh_fnc_firedMan",
            "turnIn": "call cba_xeh_fnc_turnIn",
            "turnOut": "call cba_xeh_fnc_turnOut",
            "deleted": "call cba_xeh_fnc_deleted"
        }
    },
    "ace_refuel_fuelCapacity": 3600,
    # Class: CfgVehicles\O_Plane_CAS_02_F\SimpleObject [Indent level: 1],
    "SimpleObject": {
        "eden": 0,
        "animate": [["airintake_1_front_rot",0.07],["airintake_2_front_rot",0.07],["airintake_1_top_1_rot",0.07],["airintake_2_top_1_rot",0.07],["airintake_1_top_2_move",0.07],["airintake_2_top_2_move",0.07],["rotor_1_1_rot",0],["rotor_1_2_rot",0],["rotor_2_1_rot",0],["rotor_2_2_rot",0],["aileron_1_rot_1",0],["aileron_2_rot_1",0],["airbrake_rot_1",0],["airbrake_piston_1_move_1",0],["airbrake_piston_2_rot_1",0],["elevator_1_rot",0],["elevator_2_rot",0],["flap_1_rot",0],["flap_2_rot",0],["slat_1_1_rot",0],["slat_1_2_rot",0],["slat_2_1_rot",0],["slat_2_2_rot",0],["rudder_rot",0],["wheel_1_rot",0],["wheel_2_rot",0],["wheel_3_rot",0],["gear_1_rot",0],["gear_1_hatch_1_rot",0],["gear_1_hatch_2_rot",0],["gear_1_hatch_3_rot",0],["gear_1_hatch_4_rot",0],["gear_1_hatch_5_rot",0],["gear_1_steering_rot",0],["gear_1_damper_move",0],["gear_1_stabil_1_rot",0],["gear_1_stabil_2_rot",0],["gear_2_rot",0],["gear_2_hatch_1_rot",0],["gear_2_hatch_2_rot",0],["gear_2_hatch_3_rot",0],["gear_2_piston_1_rot",0],["gear_2_stabil_1_rot",0],["gear_2_stabil_2_rot",0],["gear_2_damper_move",0],["gear_3_rot",0],["gear_3_hatch_1_rot",0],["gear_3_hatch_2_rot",0],["gear_3_hatch_3_rot",0],["gear_3_piston_1_rot",0],["gear_3_stabil_1_rot",0],["gear_3_stabil_2_rot",0],["gear_3_damper_move",0],["canopy_rot",0],["ladder_hatch_l_rot",0],["ladder_hatch_r_rot",0],["display_off_hide",0],["avionics_damage",0],["display_cannon_rot",1],["display_cannon_rot_1",0],["display_cannon_rot_2",0],["display_missile_aa_1_rot",1],["display_missile_aa_1_rot_1",0],["display_missile_aa_1_rot_2",0],["display_missile_aa_2_rot",1],["display_missile_aa_2_rot_1",0],["display_missile_aa_2_rot_2",0],["display_missile_agm_2_1_rot",1],["display_missile_agm_2_1_rot_1",0],["display_missile_agm_2_1_rot_2",0],["display_missile_agm_1_1_rot",1],["display_missile_agm_1_1_rot_1",0],["display_missile_agm_1_1_rot_2",0],["display_missile_agm_2_2_rot",1],["display_missile_agm_2_2_rot_1",0],["display_missile_agm_2_2_rot_2",0],["display_missile_agm_1_2_rot",1],["display_missile_agm_1_2_rot_1",0],["display_missile_agm_1_2_rot_2",0],["display_rocketpod_2_rot",1],["display_rocketpod_2_rot_1",0],["display_rocketpod_2_rot_2",0],["display_rocketpod_1_rot",1],["display_rocketpod_1_rot_1",0],["display_rocketpod_1_rot_2",0],["display_bomb_1_rot",1],["display_bomb_1_rot_1",0],["display_bomb_1_rot_2",0],["display_bomb_2_rot",1],["display_bomb_2_rot_1",0],["display_bomb_2_rot_2",0],["display_cannon_slider_move",1],["display_rocketpod_1_slider_move",1],["display_rocketpod_2_slider_move",1],["display_horizon_rot_1",-0.03],["display_horizon_rot_2",0],["display_speed_rot",0],["display_compass_rot",0],["display_altitude_large_rot",7.98],["display_altitude_small_rot",7.98],["display_climb_rot",0],["display_engine_1_rot",0],["display_engine_2_rot",0],["display_engine_1_slider_move",0],["display_engine_2_slider_move",0],["display_gear_down_move",0],["display_gear_up_move",0],["controlstick_pitch_rot",0],["controlstick_roll_rot",0],["compass_rot",0],["cannon_muzzleflash_rot",514],["positionlights",0],["collisionlight_red_blinking",0],["pilotcamera_h",0],["pilotcamera_v",0.26],["unhidemfd",0]],
        "hide": ["clan","cannon_muzzleflash","gear_2_light_1_hide","gear_2_light_2_hide","gear_3_light_1_hide","gear_3_light_2_hide","gear_1_light_1_hide","gear_1_light_2_hide","zadni svetlo","podsvit pristroju","poskozeni"],
        "verticalOffset": 2.872,
        "verticalOffsetWorld": -0.108,
        "init": "[this, '', []] call bis_fnc_initVehicle"
    },
    "_generalMacro": "O_Plane_CAS_02_F",
    "features": "Randomization: No						<br />Camo selections: 2 - the main body, wings lower part of body						<br />Script door sources: None						<br />Script animations: None						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: None",
    "editorSubcategory": "EdSubcat_Planes",
    "destrType": "DestructWreck",
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "slingLoadCargoMemoryPoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    # Class: CfgVehicles\Plane_CAS_02_base_F\Library [Indent level: 1],
    "Library": {
        "libTextDesc": "The To-199 Neophron is a new addition to CSAT air forces. An agile single-seat aircraft is used for close air support but can also take down air threats. It cannot carry as much payload as NATO's A-164 and has to rearm more often, but it can take-off from even the roughest terrain, not being so dependent on air bases or aircraft carriers. Neophron in CAS variant is fitted with 30 mm Cannon, Sahr-3 short range air-to-air missiles, Sharur air-to-ground missiles, Tratnyr rockets (HE and AP variants) and LOM-250G bombs."
    },
    "getinAction": "pilot_plane_cas_02_Enter",
    "getoutaction": "pilot_plane_cas_02_Exit",
    "precisegetinout": 1,
    "viewDriverShadowDiff": 0.5,
    "viewDriverShadowAmb": 0.5,
    # Class: CfgVehicles\Plane_CAS_02_base_F\Turrets [Indent level: 1],
    "Turrets": {
    },
    # Class: CfgVehicles\Plane_CAS_02_base_F\TransportItems [Indent level: 1],
    "TransportItems": {
    },
    "attenuationEffectType": "PlaneAttenuation",
    "soundGetIn": ["A3|Sounds_F_EPC|CAS_02|TO_getin",1,1],
    "soundGetOut": ["A3|Sounds_F_EPC|CAS_02|getout",1,1,40],
    "cabinOpenSound": ["A3|Sounds_F|air|noises|Plane_CAS02_CabinOpen",3.16228,1,40],
    "cabinCloseSound": ["A3|Sounds_F|air|noises|Plane_CAS02_CabinClose",3.16228,1,40],
    "cabinOpenSoundInternal": ["A3|Sounds_F|air|noises|Plane_CAS02_CabinOpen",10,1,40],
    "cabinCloseSoundInternal": ["A3|Sounds_F|air|noises|Plane_CAS02_CabinClose",10,1,40],
    "soundDammage": ["",0.562341,1],
    "soundEngineOnInt": ["A3|Sounds_F_EPC|CAS_02|CAS_02_start_int",0.794328,1],
    "soundEngineOnExt": ["A3|Sounds_F_EPC|CAS_02|CAS_02_start_ext",1,1,500],
    "soundEngineOffInt": ["A3|Sounds_F_EPC|CAS_02|CAS_02_stop_int",0.794328,1],
    "soundEngineOffExt": ["A3|Sounds_F_EPC|CAS_02|CAS_02_stop_ext",1,1,500],
    "soundGearUp": ["A3|Sounds_F_EPC|CAS_02|gear_up",0.794328,1,150],
    "soundGearDown": ["A3|Sounds_F_EPC|CAS_02|gear_down",0.794328,1,150],
    "soundFlapsUp": ["A3|Sounds_F_EPC|CAS_02|Flaps_Up",0.630957,1,100],
    "soundFlapsDown": ["A3|Sounds_F_EPC|CAS_02|Flaps_Down",0.630957,1,100],
    "soundWaterCollision1": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_1",1.41254,1,500],
    "soundWaterCollision2": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_2",1.41254,1,500],
    "soundWaterCrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "buildCrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "buildCrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "buildCrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "buildCrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundBuildingCrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "WoodCrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_1",3.16228,1,900],
    "WoodCrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_2",3.16228,1,900],
    "WoodCrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_6",3.16228,1,900],
    "WoodCrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_8",3.16228,1,900],
    "soundWoodCrash": ["woodCrash0",0.25,"woodCrash1",0.25,"woodCrash2",0.25,"woodCrash3",0.25],
    "armorCrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "armorCrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "armorCrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "armorCrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundArmorCrash": ["ArmorCrash0",0.25,"ArmorCrash1",0.25,"ArmorCrash2",0.25,"ArmorCrash3",0.25],
    "Crash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "Crash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "Crash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "Crash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundCrashes": ["Crash0",0.25,"Crash1",0.25,"Crash2",0.25,"Crash3",0.25],
    # Class: CfgVehicles\Plane_CAS_02_base_F\scrubLandInt [Indent level: 1],
    "scrubLandInt": {
        "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
        "frequency": 1,
        "volume": "(scrubLand factor[0.01, 0.20])"
    },
    # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds [Indent level: 1],
    "Sounds": {
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\EngineLowOut [Indent level: 2]
        "EngineLowOut": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_engine_idle_ext",1,1,2100],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "camPos*2*(rpm factor[0.95, 0])*(rpm factor[0, 0.95])"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\EngineHighOut [Indent level: 2],
        "EngineHighOut": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_engine_max_ext",1,1.2,2500],
            "frequency": "1",
            "volume": "camPos*4*(rpm factor[0.5, 1.1])*(rpm factor[1.1, 0.5])"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\ForsageOut [Indent level: 2],
        "ForsageOut": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_forsage_ext",1.41254,1.2,2800],
            "frequency": "1",
            "volume": "engineOn*camPos*(thrust factor[0.6, 1.0])",
            "cone": [3.14,3.92,2,0.5]
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\WindNoiseOut [Indent level: 2],
        "WindNoiseOut": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|noise",0.562341,1,150],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "camPos*(speed factor[1, 150])"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\EngineLowIn [Indent level: 2],
        "EngineLowIn": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_engine_idle_int",0.562341,1],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "(1-camPos)*((rpm factor[0.7, 0.1])*(rpm factor[0.1, 0.7]))"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\EngineHighIn [Indent level: 2],
        "EngineHighIn": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_engine_max_int",0.316228,1.2],
            "frequency": "1",
            "volume": "(1-camPos)*(rpm factor[0.85, 1.0])"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\ForsageIn [Indent level: 2],
        "ForsageIn": {
            "sound": ["A3|Sounds_F_EPC|CAS_02|CAS_02_forsage_int",0.501187,1.2],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.6, 1.0]))"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\WindNoiseIn [Indent level: 2],
        "WindNoiseIn": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|noise_int",0.316228,1],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "(1-camPos)*(speed factor[1, 150])"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\RainExt [Indent level: 2],
        "RainExt": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1.77828,1,100],
            "frequency": 1,
            "volume": "camPos * rain * (speed factor[50, 0])"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\RainInt [Indent level: 2],
        "RainInt": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos) * rain * (speed factor[50, 0])"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\Waternoise_ext [Indent level: 2],
        "Waternoise_ext": {
            "sound": ["A3|Sounds_F|vehicles|noises|air_driving_in_water",0.707946,1,300],
            "frequency": "1",
            "volume": "(speed factor[0, 5]) * water * camPos + (speed factor[-0.1, -5]) * water * camPos"
        },
        # Class: CfgVehicles\Plane_CAS_02_base_F\Sounds\Waternoise_int [Indent level: 2],
        "Waternoise_int": {
            "sound": ["A3|Sounds_F|vehicles|noises|soft_driving_in_water_int",0.562341,1,100],
            "frequency": "1",
            "volume": "(speed factor[0, 5]) * water * (1-camPos) + (speed factor[-0.1, -5]) * water * (1-camPos)"
        }
    },
    "clutchStrength": 100,
    "dampingRateFullThrottle": 0.4,
    "irScanRangeMin": 500,
    "irScanRangeMax": 5000,
    "irScanToEyeFactor": 2,
    "laserScanner": 1,
    "showAllTargets": 4,
    "minFireTime": 30,
    "gunAimDown": 0,
    "extCameraPosition": [0,4.1,-20],
    "cabinOpening": 1,
    "explosionShielding": 1,
    "armorLights": 0.1,
    "waterLeakiness": 1.5,
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "waterLinearDampingCoefY": 0,
    "waterLinearDampingCoefX": 5,
    "waterResistanceCoef": 0.04,
    "ejectSpeed": [0,60,0],
    "transportMaxWeapons": 6,
    "transportMaxMagazines": 24,
    "transportMaxBackpacks": 6,
    "maximumLoad": 500,
    "supplyRadius": 2,
    "memoryPointSupply": "doplnovani",
    # Class: CfgVehicles\Plane_Base_F\TransportBackpacks [Indent level: 1],
    "TransportBackpacks": {
    },
    # Class: CfgVehicles\Plane_Base_F\TransportMagazines [Indent level: 1],
    "TransportMagazines": {
    },
    # Class: CfgVehicles\Plane_Base_F\TransportWeapons [Indent level: 1],
    "TransportWeapons": {
    },
    # Class: CfgVehicles\Plane_Base_F\camShakeGForce [Indent level: 1],
    "camShakeGForce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minSpeed": 1
    },
    "minGForce": 0.3,
    "maxGForce": 3,
    "gForceShakeAttenuation": 0.5,
    # Class: CfgVehicles\Plane_Base_F\NewTurret [Indent level: 1],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewGunner [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors [Indent level: 2],
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire [Indent level: 2],
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
            # Class: WeaponFireGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponFireGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1 [Indent level: 1],
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2 [Indent level: 1],
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3 [Indent level: 1],
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4 [Indent level: 1],
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5 [Indent level: 1],
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6 [Indent level: 1],
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7 [Indent level: 1],
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8 [Indent level: 1],
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9 [Indent level: 1],
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10 [Indent level: 1],
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11 [Indent level: 1],
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12 [Indent level: 1],
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13 [Indent level: 1],
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14 [Indent level: 1],
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15 [Indent level: 1],
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16 [Indent level: 1],
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17 [Indent level: 1],
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18 [Indent level: 1],
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19 [Indent level: 1],
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20 [Indent level: 1],
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21 [Indent level: 1],
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22 [Indent level: 1],
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds [Indent level: 2],
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
            # Class: WeaponCloudsGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds [Indent level: 2],
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
            # Class: WeaponCloudsMGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints [Indent level: 2],
        "HitPoints": {
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitTurret [Indent level: 3]
            "HitTurret": {
                "armor": 0.8,
                "material": 51,
                "name": "turret",
                "visual": "turret",
                "passThrough": 1,
                "explosionShielding": 1
            },
            # Class: CfgVehicles\AllVehicles\NewTurret\HitPoints\HitGun [Indent level: 3],
            "HitGun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passThrough": 1,
                "explosionShielding": 1
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets [Indent level: 2],
        "Turrets": {
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn [Indent level: 2],
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
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
        "showCrewAim": 0,
        "ace_fcs_Enabled": 0,
        "ace_fcs_MinDistance": 200,
        "ace_fcs_MaxDistance": 5500,
        "ace_fcs_DistanceInterval": 5
    },
    "formationX": 200,
    "formationZ": 300,
    "precision": 200,
    "brakeDistance": 500,
    "steerAheadSimul": 1,
    "steerAheadPlan": 2,
    "gearRetracting": 1,
    "durationGetIn": 0.99,
    "durationGetOut": 0.99,
    "vtol": 0,
    "tailHook": 0,
    "lightOnGear": 1,
    "gearUpTime": 3.33,
    "gearDownTime": 2,
    "cost": 2e+006,
    "simulation": "airplanex",
    "minGunElev": 0,
    "maxGunElev": 0,
    "minGunTurn": 0,
    "maxGunTurn": 0,
    "VTOLYawInfluence": 2,
    "VTOLPitchInfluence": 2,
    "VTOLRollInfluence": 2,
    # Class: CfgVehicles\Plane\ViewOptics [Indent level: 1],
    "ViewOptics": {
        "initAngleX": 0,
        "minAngleX": 0,
        "maxAngleX": 0,
        "initAngleY": 0,
        "minAngleY": 0,
        "maxAngleY": 0,
        "initFov": 0.5,
        "minFov": 0.5,
        "maxFov": 0.5,
        "minMoveX": 0,
        "maxMoveX": 0,
        "minMoveY": 0,
        "maxMoveY": 0,
        "minMoveZ": 0,
        "maxMoveZ": 0,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    "selectionRotorStill": "vrtule staticka",
    "selectionRotorMove": "vrtule blur",
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "dustEffect": "HeliDust",
    "waterEffect": "HeliWater",
    # Class: CfgVehicles\Plane\GunFire [Indent level: 1],
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
        # Class: WeaponFireGun\Table [Indent level: 0],
        "Table": {
            # Class: WeaponFireGun\Table\T0 [Indent level: 1]
            "T0": {
                "maxT": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun\Table\T1 [Indent level: 1],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun\Table\T2 [Indent level: 1],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun\Table\T3 [Indent level: 1],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun\Table\T4 [Indent level: 1],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun\Table\T5 [Indent level: 1],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun\Table\T6 [Indent level: 1],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun\Table\T7 [Indent level: 1],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun\Table\T8 [Indent level: 1],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun\Table\T9 [Indent level: 1],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun\Table\T10 [Indent level: 1],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun\Table\T11 [Indent level: 1],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun\Table\T12 [Indent level: 1],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun\Table\T13 [Indent level: 1],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun\Table\T14 [Indent level: 1],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun\Table\T15 [Indent level: 1],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun\Table\T16 [Indent level: 1],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun\Table\T17 [Indent level: 1],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun\Table\T18 [Indent level: 1],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun\Table\T19 [Indent level: 1],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun\Table\T20 [Indent level: 1],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun\Table\T21 [Indent level: 1],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun\Table\T22 [Indent level: 1],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\Plane\GunClouds [Indent level: 1],
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
        # Class: WeaponCloudsGun\Table [Indent level: 0],
        "Table": {
            # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\Plane\MGunFire [Indent level: 1],
    "MGunFire": {
        "cloudletDuration": 0,
        "cloudletGrowUp": 0.06,
        "cloudletFadeIn": 0,
        "cloudletFadeOut": 0.12,
        "interval": 0.005,
        "size": 0.12,
        "sourceSize": 0.01,
        "initT": 3200,
        "deltaT": -4000,
        "access": 0,
        "cloudletAnimPeriod": 1,
        "cloudletSize": 1,
        "cloudletAlpha": 1,
        "cloudletAccY": 0,
        "cloudletMinYSpeed": -100,
        "cloudletMaxYSpeed": 100,
        "cloudletShape": "cloudletFire",
        "cloudletColor": [1,1,1,0],
        "timeToLive": 0,
        # Class: WeaponFireGun\Table [Indent level: 0],
        "Table": {
            # Class: WeaponFireGun\Table\T0 [Indent level: 1]
            "T0": {
                "maxT": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun\Table\T1 [Indent level: 1],
            "T1": {
                "maxT": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun\Table\T2 [Indent level: 1],
            "T2": {
                "maxT": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun\Table\T3 [Indent level: 1],
            "T3": {
                "maxT": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun\Table\T4 [Indent level: 1],
            "T4": {
                "maxT": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun\Table\T5 [Indent level: 1],
            "T5": {
                "maxT": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun\Table\T6 [Indent level: 1],
            "T6": {
                "maxT": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun\Table\T7 [Indent level: 1],
            "T7": {
                "maxT": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun\Table\T8 [Indent level: 1],
            "T8": {
                "maxT": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun\Table\T9 [Indent level: 1],
            "T9": {
                "maxT": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun\Table\T10 [Indent level: 1],
            "T10": {
                "maxT": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun\Table\T11 [Indent level: 1],
            "T11": {
                "maxT": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun\Table\T12 [Indent level: 1],
            "T12": {
                "maxT": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun\Table\T13 [Indent level: 1],
            "T13": {
                "maxT": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun\Table\T14 [Indent level: 1],
            "T14": {
                "maxT": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun\Table\T15 [Indent level: 1],
            "T15": {
                "maxT": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun\Table\T16 [Indent level: 1],
            "T16": {
                "maxT": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun\Table\T17 [Indent level: 1],
            "T17": {
                "maxT": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun\Table\T18 [Indent level: 1],
            "T18": {
                "maxT": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun\Table\T19 [Indent level: 1],
            "T19": {
                "maxT": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun\Table\T20 [Indent level: 1],
            "T20": {
                "maxT": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun\Table\T21 [Indent level: 1],
            "T21": {
                "maxT": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun\Table\T22 [Indent level: 1],
            "T22": {
                "maxT": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles\Plane\MGunClouds [Indent level: 1],
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
        # Class: WeaponCloudsMGun\Table [Indent level: 0],
        "Table": {
            # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
            "T0": {
                "maxT": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "numberPhysicalWheels": 3,
    # Class: CfgVehicles\Plane\SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles\Plane\SpeechVariants\Default [Indent level: 2]
        "Default": {
            "speechSingular": ["veh_air_plane_s"],
            "speechPlural": ["veh_air_plane_p"]
        }
    },
    "textPlural": "fast movers",
    "nameSound": "veh_air_plane_s",
    "type": 2,
    "fuelExplosionPower": 10,
    "crewCrashProtection": 0.15,
    "damageEffect": "AirDestructionEffects",
    "cargoGetInAction": ["GetInHigh"],
    "cargoGetOutAction": ["GetOutHigh"],
    "gunnerGetInAction": "GetInHigh",
    "gunnerGetOutAction": "GetOutHigh",
    "getInRadius": 1.2,
    "camouflage": 100,
    "audible": 60,
    # Class: CfgVehicles\Plane\CamShake [Indent level: 1],
    "CamShake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minSpeed": 200
    },
    "minTotalDamageThreshold": 0.005,
    # Class: CfgVehicles\Plane\DestructionEffects [Indent level: 1],
    "DestructionEffects": {
    },
    # Class: CfgVehicles\Plane\ACE_Actions [Indent level: 1],
    "ACE_Actions": {
        # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions [Indent level: 2]
        "ACE_MainActions": {
            "displayName": "Interactions",
            "position": "[_target,ace_interact_menu_cameraPosASL] call ace_interaction_fnc_getVehiclePosComplex",
            "selection": "",
            "distance": 4,
            "condition": "true",
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\ACE_Passengers [Indent level: 3],
            "ACE_Passengers": {
                "displayName": "Passengers",
                "condition": "alive _target",
                "statement": "",
                "exceptions": ["isNotSwimming"],
                "insertChildren": "_this call ace_interaction_fnc_addPassengersActions"
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\ace_quickmount_GetIn [Indent level: 3],
            "ace_quickmount_GetIn": {
                "displayName": "Get In",
                "condition": "call ace_quickmount_fnc_canShowFreeSeats",
                "statement": "call ace_quickmount_fnc_getInNearest",
                "exceptions": ["isNotSwimming"],
                "insertChildren": "(_this select 2) param [0,[]]"
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\ace_rearm_Rearm [Indent level: 3],
            "ace_rearm_Rearm": {
                "displayName": "Rearm",
                "distance": 9,
                "condition": "_this call ace_rearm_fnc_canRearm",
                "statement": "_this call ace_rearm_fnc_rearm",
                "exceptions": ["isNotInside"],
                "icon": "z|ace|addons|rearm|ui|icon_rearm_interact.paa"
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\ace_repair_Repair [Indent level: 3],
            "ace_repair_Repair": {
                "displayName": "Repair",
                "condition": "true",
                "statement": "",
                "runOnHover": 1,
                "showDisabled": 0,
                "icon": "A3|ui_f|data|igui|cfg|actions|repair_ca.paa",
                "distance": 4,
                "exceptions": ["isNotSwimming","isNotOnLadder"]
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\ACE_unlockVehicle [Indent level: 3],
            "ACE_unlockVehicle": {
                "displayName": "Unlock Vehicle",
                "distance": 4,
                "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [2, 3]}",
                "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,false],[_target]] call CBA_fnc_targetEvent",
                "exceptions": ["isNotSwimming"],
                "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\ACE_lockVehicle [Indent level: 3],
            "ACE_lockVehicle": {
                "displayName": "Lock Vehicle",
                "distance": 4,
                "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [0, 1]}",
                "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,true],[_target]] call CBA_fnc_targetEvent",
                "exceptions": ["isNotSwimming"],
                "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\ACE_lockpickVehicle [Indent level: 3],
            "ACE_lockpickVehicle": {
                "displayName": "Lockpick Vehicle",
                "distance": 4,
                "condition": "[_player,_target,'canLockpick'] call ace_vehiclelock_fnc_lockpick",
                "statement": "[_player,_target,'startLockpick'] call ace_vehiclelock_fnc_lockpick",
                "exceptions": ["isNotSwimming"]
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\AIME_vehicle_seats_getInAction [Indent level: 3],
            "AIME_vehicle_seats_getInAction": {
                "displayName": "Get In",
                "condition": "call AIME_vehicle_seats_fnc_getin_condition",
                "statement": "call AIME_vehicle_seats_fnc_getin_run",
                "icon": "a3|ui_f|data|igui|cfg|actions|obsolete|ui_action_getin_ca.paa",
                "insertChildren": "call AIME_vehicle_seats_fnc_change_submenus"
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\ace_attach_AttachVehicle [Indent level: 3],
            "ace_attach_AttachVehicle": {
                "displayName": "Attach item",
                "condition": "_this call ace_attach_fnc_canAttach",
                "insertChildren": "_this call ace_attach_fnc_getChildrenActions",
                "exceptions": ["isNotSwimming"],
                "showDisabled": 0,
                "icon": "z|ace|addons|attach|UI|attach_ca.paa"
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\ace_attach_DetachVehicle [Indent level: 3],
            "ace_attach_DetachVehicle": {
                "displayName": "Detach item",
                "condition": "_this call ace_attach_fnc_canDetach",
                "statement": "_this call ace_attach_fnc_detach",
                "exceptions": ["isNotSwimming"],
                "showDisabled": 0,
                "icon": "z|ace|addons|attach|UI|detach_ca.paa"
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\ace_captives_LoadCaptive [Indent level: 3],
            "ace_captives_LoadCaptive": {
                "displayName": "Load Captive",
                "distance": 4,
                "condition": "[_player,objNull,_target] call ace_captives_fnc_canLoadCaptive",
                "statement": "[_player,objNull,_target] call ace_captives_fnc_doLoadCaptive",
                "exceptions": ["isNotEscorting","isNotSwimming"]
            },
            # Class: CfgVehicles\Plane\ACE_Actions\ACE_MainActions\AIME_inventory_openAction [Indent level: 3],
            "AIME_inventory_openAction": {
                "displayName": "Inventory",
                "condition": "AIME_inventory_settingOpenAction				 && { alive _target }				 && { _target call AIME_inventory_fnc_has_inventory }",
                "statement": "_player action [`Gear`, _target]",
                "icon": "A3|ui_f|data|igui|cfg|actions|gear_ca.paa",
                "exceptions": ["isNotSwimming"]
            }
        }
    },
    # Class: CfgVehicles\Plane\ACE_SelfActions [Indent level: 1],
    "ACE_SelfActions": {
        # Class: CfgVehicles\Plane\ACE_SelfActions\ACE_Passengers [Indent level: 2]
        "ACE_Passengers": {
            "displayName": "Passengers",
            "condition": "alive _target",
            "statement": "",
            "insertChildren": "_this call ace_interaction_fnc_addPassengersActions"
        },
        # Class: CfgVehicles\Plane\ACE_SelfActions\ace_quickmount_ChangeSeat [Indent level: 2],
        "ace_quickmount_ChangeSeat": {
            "displayName": "Change seat",
            "condition": "call ace_quickmount_fnc_canShowFreeSeats",
            "statement": "",
            "insertChildren": "(_this select 2) param [0,[]]"
        },
        # Class: CfgVehicles\Plane\ACE_SelfActions\ACE_unlockVehicle [Indent level: 2],
        "ACE_unlockVehicle": {
            "displayName": "Unlock Vehicle",
            "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [2, 3]}",
            "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,false],[_target]] call CBA_fnc_targetEvent",
            "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
        },
        # Class: CfgVehicles\Plane\ACE_SelfActions\ACE_lockVehicle [Indent level: 2],
        "ACE_lockVehicle": {
            "displayName": "Lock Vehicle",
            "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [0, 1]}",
            "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,true],[_target]] call CBA_fnc_targetEvent",
            "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
        },
        # Class: CfgVehicles\Plane\ACE_SelfActions\ACE_lockpickVehicle [Indent level: 2],
        "ACE_lockpickVehicle": {
            "displayName": "Lockpick Vehicle",
            "condition": "[_player,_target,'canLockpick'] call ace_vehiclelock_fnc_lockpick",
            "statement": "[_player,_target,'startLockpick'] call ace_vehiclelock_fnc_lockpick"
        }
    },
    "ace_refuel_canReceive": 1,
    "ace_refuel_flowRate": 16,
    # Class: CfgVehicles\Plane\ViewGunner [Indent level: 1],
    "ViewGunner": {
    },
    "ace_cargo_space": 0,
    "ace_cargo_hasCargo": 0,
    "formationTime": 10,
    "fuelCapacity": 1000,
    "insideSoundCoef": 0.0316228,
    "outsideSoundFilter": 1,
    "occludeSoundsWhenIn": 0.316228,
    "obstructSoundsWhenIn": 0.316228,
    "nightVision": 0,
    "cargoCompartments": [0],
    "enableGPS": 1,
    "weaponsGroup2": 4,
    "weaponsGroup3": "8 + 	16 + 	32",
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    "maxFordingDepth": 0.001,
    "waterResistance": 1,
    "impactEffectsSea": "ImpactEffectsAir",
    "flareVelocity": 100,
    "enableRadio": 1,
    "radarType": 4,
    "countermeasureActivationRadius": 10000,
    # Class: CfgVehicles\Air\camShakeDamage [Indent level: 1],
    "camShakeDamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minSpeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "secondaryExplosion": -1,
    "tf_hasLRradio": 1,
    "tf_isolatedAmount": 0.1,
    # Class: CfgVehicles\AllVehicles\SquadTitles [Indent level: 1],
    "SquadTitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memoryPointsGetInCargo": "pos cargo",
    "memoryPointsGetInCargoDir": "pos cargo dir",
    "memoryPointsGetInCoDriver": "pos codriver",
    "memoryPointsGetInCoDriverDir": "pos codriver dir",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionDashboard": "podsvit pristroju",
    "selectionBackLights": "zadni svetlo",
    # Class: CfgVehicles\AllVehicles\ViewCargo [Indent level: 1],
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
    # Class: CfgVehicles\AllVehicles\PilotSpec [Indent level: 1],
    "PilotSpec": {
        "showHeadPhones": 0
    },
    # Class: CfgVehicles\AllVehicles\CargoSpec [Indent level: 1],
    "CargoSpec": {
        # Class: CfgVehicles\AllVehicles\CargoSpec\Cargo1 [Indent level: 2]
        "Cargo1": {
            "showHeadPhones": 0
        }
    },
    # Class: CfgVehicles\AllVehicles\SoundEvents [Indent level: 1],
    "SoundEvents": {
    },
    "tracksSpeed": 0,
    "selectionLeftOffset": "",
    "selectionRightOffset": "",
    "cargoProxyIndexes": [],
    "driverDoor": "",
    "cargoDoors": [],
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "cargoPreciseGetInOut": [0],
    "waterPPInVehicle": 1,
    "impactEffectSpeedLimit": 8,
    "showCrewAim": 0,
    # Class: CfgVehicles\AllVehicles\CargoTurret [Indent level: 1],
    "CargoTurret": {
        # Class: CfgVehicles\AllVehicles\CargoTurret\ViewGunner [Indent level: 2]
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
        # Class: CfgVehicles\AllVehicles\CargoTurret\Hitpoints [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\Reflectors [Indent level: 2],
        "Reflectors": {
        },
        "aggregateReflectors": [],
        # Class: CfgVehicles\AllVehicles\NewTurret\GunFire [Indent level: 2],
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
            # Class: WeaponFireGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponFireGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun\Table\T1 [Indent level: 1],
                "T1": {
                    "maxT": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun\Table\T2 [Indent level: 1],
                "T2": {
                    "maxT": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun\Table\T3 [Indent level: 1],
                "T3": {
                    "maxT": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun\Table\T4 [Indent level: 1],
                "T4": {
                    "maxT": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun\Table\T5 [Indent level: 1],
                "T5": {
                    "maxT": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun\Table\T6 [Indent level: 1],
                "T6": {
                    "maxT": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun\Table\T7 [Indent level: 1],
                "T7": {
                    "maxT": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun\Table\T8 [Indent level: 1],
                "T8": {
                    "maxT": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun\Table\T9 [Indent level: 1],
                "T9": {
                    "maxT": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun\Table\T10 [Indent level: 1],
                "T10": {
                    "maxT": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun\Table\T11 [Indent level: 1],
                "T11": {
                    "maxT": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun\Table\T12 [Indent level: 1],
                "T12": {
                    "maxT": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun\Table\T13 [Indent level: 1],
                "T13": {
                    "maxT": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun\Table\T14 [Indent level: 1],
                "T14": {
                    "maxT": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun\Table\T15 [Indent level: 1],
                "T15": {
                    "maxT": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun\Table\T16 [Indent level: 1],
                "T16": {
                    "maxT": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun\Table\T17 [Indent level: 1],
                "T17": {
                    "maxT": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun\Table\T18 [Indent level: 1],
                "T18": {
                    "maxT": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun\Table\T19 [Indent level: 1],
                "T19": {
                    "maxT": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun\Table\T20 [Indent level: 1],
                "T20": {
                    "maxT": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun\Table\T21 [Indent level: 1],
                "T21": {
                    "maxT": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun\Table\T22 [Indent level: 1],
                "T22": {
                    "maxT": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\GunClouds [Indent level: 2],
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
            # Class: WeaponCloudsGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\MGunClouds [Indent level: 2],
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
            # Class: WeaponCloudsMGun\Table [Indent level: 0],
            "Table": {
                # Class: WeaponCloudsMGun\Table\T0 [Indent level: 1]
                "T0": {
                    "maxT": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\Turrets [Indent level: 2],
        "Turrets": {
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\ViewOptics [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn [Indent level: 2],
        "TurnIn": {
            "turnOffset": 0
        },
        # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut [Indent level: 2],
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
        "showCrewAim": 0,
        "ace_fcs_Enabled": 0,
        "ace_fcs_MinDistance": 200,
        "ace_fcs_MaxDistance": 5500,
        "ace_fcs_DistanceInterval": 5
    },
    "curatorInfoType": "RscDisplayAttributesVehicle",
    "curatorInfoTypeEmpty": "RscDisplayAttributesVehicleEmpty",
    "htMin": 60,
    "htMax": 1800,
    "afMax": 70,
    "mfMax": 50,
    "mFact": 0,
    "tBody": 0,
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
    "enableManualFire": 1,
    "sensitivity": 2.5,
    "sensitivityEar": 0.0075,
    "portrait": "",
    "ghostPreview": "",
    "crewVulnerable": 1,
    "replaceDamaged": "",
    "replaceDamagedLimit": 0.9,
    "replaceDamagedHitpoints": [],
    "keepInEPESceneAfterDeath": 0,
    "fuelConsumptionRate": 0.01,
    "groupCameraPosition": [0,5,-30],
    "extCameraParams": [1],
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
    "unitInfoTypeLite": 0,
    "hideUnitInfo": 0,
    "limitedSpeedCoef": 0.22,
    "hasDriver": 1,
    "driverForceOptics": 0,
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 0,
    "enableWatch": 0,
    "usePreciseGetInAction": 0,
    "dustFrontLeftPos": "dustFrontLeft",
    "dustFrontRightPos": "dustFrontRight",
    "dustBackLeftPos": "dustBackLeft",
    "dustBackRightPos": "dustBackRight",
    "wheelCircumference": 1,
    "waterAngularDampingCoef": 0,
    "showNVGDriver": 0,
    "showNVGCommander": 0,
    "showNVGGunner": 0,
    "showNVGCargo": [0],
    "soundAttenuationCargo": [1],
    "countsForScoreboard": 1,
    "hullDamageCauseExplosion": 0,
    # Class: CfgVehicles\All\NVGMarkers [Indent level: 1],
    "NVGMarkers": {
    },
    # Class: CfgVehicles\All\NVGMarker [Indent level: 1],
    "NVGMarker": {
        "diffuse": [1,1,1,1],
        "ambient": [1,1,1,1],
        "brightness": 1,
        "blinking": 0,
        "onlyInNvg": 0
    },
    # Class: CfgVehicles\All\HeadLimits [Indent level: 1],
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
    "transportSoldier": 0,
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
    # Class: CfgVehicles\All\SoundEnvironExt [Indent level: 1],
    "SoundEnvironExt": {
    },
    # Class: CfgVehicles\All\SoundEquipment [Indent level: 1],
    "SoundEquipment": {
    },
    # Class: CfgVehicles\All\SoundGear [Indent level: 1],
    "SoundGear": {
    },
    # Class: CfgVehicles\All\SoundBreath [Indent level: 1],
    "SoundBreath": {
    },
    # Class: CfgVehicles\All\SoundBreathSwimming [Indent level: 1],
    "SoundBreathSwimming": {
    },
    # Class: CfgVehicles\All\SoundBreathInjured [Indent level: 1],
    "SoundBreathInjured": {
    },
    # Class: CfgVehicles\All\SoundHitScream [Indent level: 1],
    "SoundHitScream": {
    },
    # Class: CfgVehicles\All\SoundInjured [Indent level: 1],
    "SoundInjured": {
    },
    # Class: CfgVehicles\All\SoundBreathAutomatic [Indent level: 1],
    "SoundBreathAutomatic": {
    },
    # Class: CfgVehicles\All\SoundDrown [Indent level: 1],
    "SoundDrown": {
    },
    # Class: CfgVehicles\All\SoundChoke [Indent level: 1],
    "SoundChoke": {
    },
    # Class: CfgVehicles\All\SoundRecovered [Indent level: 1],
    "SoundRecovered": {
    },
    # Class: CfgVehicles\All\SoundBurning [Indent level: 1],
    "SoundBurning": {
    },
    # Class: CfgVehicles\All\PulsationSound [Indent level: 1],
    "PulsationSound": {
    },
    # Class: CfgVehicles\All\SoundDrowning [Indent level: 1],
    "SoundDrowning": {
    },
    "soundCrash": ["",0.316228,1],
    "soundLandCrash": ["",1,1],
    "soundWaterCrash": ["",0.177828,1],
    "soundServo": ["",0.00316228,0.5],
    "soundElevation": ["",0.00316228,0.5],
    "sounddamage": ["",1,1],
    "soundLandCrashes": ["soundLandCrash",1],
    "emptySound": ["",0,1],
    "soundBushCrash": ["emptySound",0],
    "driverInAction": "",
    "cargoAction": [],
    "cargoIsCoDriver": [0],
    "driverOpticsModel": "",
    "driverOpticsEffect": [],
    "driverOpticsColor": [1,1,1,1],
    "hideProxyInCombat": 0,
    "forceHideDriver": 0,
    "canHideDriver": -1,
    "castDriverShadow": 0,
    "castCargoShadow": 0,
    "viewDriverShadow": 1,
    "viewCargoShadow": 1,
    "viewCargoShadowDiff": 1,
    "viewCargoShadowAmb": 1,
    "ejectDeadDriver": 0,
    "ejectDeadCargo": 0,
    "hiddenSelectionsMaterials": [],
    "hiddenUnderwaterSelections": [],
    "shownUnderWaterSelections": [],
    "hiddenUnderwaterSelectionsTextures": [],
    # Class: CfgVehicles\All\FxExplo [Indent level: 1],
    "FxExplo": {
        "access": 1
    },
    "cargoCanEject": 1,
    "fireResistance": 10,
    "airCapacity": 10,
    "waterDamageEngine": 0.2,
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    "soundTurnIn": ["",0.000316228,1],
    "soundTurnOut": ["",0.000316228,1],
    "soundTurnInInternal": ["",0.000316228,1],
    "soundTurnOutInternal": ["",0.000316228,1],
    "insideDetectCoef": 0.05,
    "coefSpeedInside": 1,
    "windSockExist": 0,
    "SLX_XEH_DISABLED": 0,
}