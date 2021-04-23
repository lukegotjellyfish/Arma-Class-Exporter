rhs_l159_cdf = {
    "editorpreview": "rhsgref|addons|rhsgref_editorPreviews|data|rhs_l159_CDF.paa",
    "author": "Red Hammer Studios",
    "scope": 2,
    "side": 2,
    "dlc": "RHS_GREF",
    "rhs_decalparameters": ["['Number',[4,5],'AviaCDF']","['Label',[2],'Aviation', 5]","['Label',[3],'AviationSquadronsCDFGrey']"],
    "faction": "rhsgref_faction_cdf_air",
    "crew": "rhsgref_cdf_air_pilot",
    "typicalcargo": ["rhsgref_cdf_air_pilot"],
    "model": "rhsgref|addons|rhsgref_air|L159|rhs_l159.p3d",
    "displayname": "L-159 ALCA",
    "vehicleclass": "rhs_vehclass_aircraft",
    "selectiondashboard": "podsvit pristroju",
    "unitinfotype": "RHSGREF_RscUnitInfoJet",
    "driverlefthandanimname": "throttle_pilot",
    "driverrighthandanimname": "stick_pilot",
    # Class: CfgVehicles|RHS_L159_base|pilotCamera [Indent level: 1],
    "pilotcamera": {
    },
    # Class: CfgVehicles|RHS_L159_base|EjectionSystem [Indent level: 1],
    "ejectionsystem": {
    },
    "drivercaneject": 1,
    # Class: CfgVehicles|RHS_L159_base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        "hit": "",
        # Class: CfgVehicles|RHS_L159_base|EventHandlers|RHS_EventHandlers [Indent level: 2],
        "rhs_eventhandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "init": "_this call rhs_fnc_decalsReadParams",
            "getout": "[_this select 0, _this select 2] call rhs_fnc_vs1_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    # Class: CfgVehicles|RHS_L159_base|UserActions [Indent level: 1],
    "useractions": {
    },
    # Class: CfgVehicles|RHS_L159_base|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2 [Indent level: 2]
        "hitglass2": {
            "armor": 1,
            "material": -1,
            "name": "glass2",
            "convexcomponent": "glass2",
            "visual": "glass2",
            "passthrough": 0,
            # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass1 [Indent level: 4],
                "brokenglass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass2 [Indent level: 4],
                "brokenglass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass3 [Indent level: 4],
                "brokenglass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass4 [Indent level: 4],
                "brokenglass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass5 [Indent level: 4],
                "brokenglass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass6 [Indent level: 4],
                "brokenglass6": {
                    "simulation": "particles",
                    "type": "BrokenGlass6N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass7 [Indent level: 4],
                "brokenglass7": {
                    "simulation": "particles",
                    "type": "BrokenGlass7N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass1S [Indent level: 4],
                "brokenglass1s": {
                    "simulation": "particles",
                    "type": "BrokenGlass1S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass2S [Indent level: 4],
                "brokenglass2s": {
                    "simulation": "particles",
                    "type": "BrokenGlass2S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass3S [Indent level: 4],
                "brokenglass3s": {
                    "simulation": "particles",
                    "type": "BrokenGlass3S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass4S [Indent level: 4],
                "brokenglass4s": {
                    "simulation": "particles",
                    "type": "BrokenGlass4S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass5S [Indent level: 4],
                "brokenglass5s": {
                    "simulation": "particles",
                    "type": "BrokenGlass5S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass6S [Indent level: 4],
                "brokenglass6s": {
                    "simulation": "particles",
                    "type": "BrokenGlass6S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|BrokenGlass7S [Indent level: 4],
                "brokenglass7s": {
                    "simulation": "particles",
                    "type": "BrokenGlass7S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifetime": 0.05
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "glass2_effect",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "glass2_effect",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.005
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitGlass2|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "glass2_effect",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                }
            }
        },
        # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon1 [Indent level: 2],
        "hitpylon1": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_1",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon1|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon1|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon2 [Indent level: 2],
        "hitpylon2": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_2",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon2|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon2|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon3 [Indent level: 2],
        "hitpylon3": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_3",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon3|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon3|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon4 [Indent level: 2],
        "hitpylon4": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_4",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon4|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon4|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon5 [Indent level: 2],
        "hitpylon5": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_5",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon5|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon5|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon5|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon5|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon5|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon6 [Indent level: 2],
        "hitpylon6": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_6",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon6|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon6|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon6|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon6|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon6|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon7 [Indent level: 2],
        "hitpylon7": {
            "armor": -30,
            "material": -1,
            "name": "hit_pylon_7",
            "passthrough": 0,
            "minimalhit": -0.5,
            "explosionshielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon7|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon7|DestructionEffects|RHS_Pylon_Flash [Indent level: 4],
                "rhs_pylon_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon7|DestructionEffects|RHS_Pylon_Sound [Indent level: 4],
                "rhs_pylon_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon7|DestructionEffects|RHS_Pylon_Smoke [Indent level: 4],
                "rhs_pylon_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_L159_base|HitPoints|HitPylon7|DestructionEffects|RHS_Pylon_Shard [Indent level: 4],
                "rhs_pylon_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitHull [Indent level: 2],
        "hithull": {
            "armor": 4,
            "explosionshielding": 3,
            "name": "HitHull",
            "passthrough": 1,
            "visual": "Hit_Hull",
            "radius": 0.3,
            "minimalhit": 0.05,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 3,
            "explosionshielding": 4,
            "name": "HitEngine",
            "passthrough": 1,
            "visual": "Hit_Engine",
            "radius": 0.3,
            "minimalhit": 0.05,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitAvionics [Indent level: 2],
        "hitavionics": {
            "armor": 3,
            "explosionshielding": 3.5,
            "name": "HitAvionics",
            "passthrough": 0.5,
            "visual": "",
            "radius": 0.2,
            "minimalhit": 0.05,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 4.5,
            "explosionshielding": 4,
            "name": "HitFuel",
            "passthrough": 0.8,
            "visual": "",
            "radius": 0.3,
            "minimalhit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitFuel_Lead_Left [Indent level: 2],
        "hitfuel_lead_left": {
            "armor": 1.8,
            "explosionshielding": 3,
            "name": "HitFuel1_Leads",
            "passthrough": 0,
            "visual": "Hit_AileronL",
            "radius": 0.13,
            "minimalhit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitFuel_Lead_Right [Indent level: 2],
        "hitfuel_lead_right": {
            "armor": 1.8,
            "explosionshielding": 3,
            "name": "HitFuel2_leads",
            "passthrough": 0,
            "visual": "Hit_AileronR",
            "radius": 0.13,
            "minimalhit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitFuel_Left [Indent level: 2],
        "hitfuel_left": {
            "armor": 2.5,
            "explosionshielding": 5,
            "name": "HitFuel1",
            "passthrough": 0.2,
            "visual": "Hit_Fuel2a",
            "radius": 0.2,
            "minimalhit": 0.1,
            "depends": "HitFuel_Lead_Left",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitFuel_Right [Indent level: 2],
        "hitfuel_right": {
            "armor": 2.5,
            "explosionshielding": 5,
            "name": "HitFuel2",
            "passthrough": 0.2,
            "visual": "Hit_Fuel2b",
            "radius": 0.2,
            "minimalhit": 0.1,
            "depends": "HitFuel_Lead_Right",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitFuel2 [Indent level: 2],
        "hitfuel2": {
            "armor": 999,
            "explosionshielding": 0,
            "name": "HitFuel2",
            "passthrough": 0.2,
            "visual": "",
            "radius": 0.2,
            "minimalhit": 0.1,
            "depends": "(HitFuel_Left + HitFuel_Right)*0.5",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "armor": 1.2,
            "explosionshielding": 3,
            "name": "HitGlass1",
            "passthrough": 0,
            "visual": "glass1",
            "radius": 0.2,
            "minimalhit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "armor": 1.2,
            "explosionshielding": 3,
            "name": "HitGlass3",
            "passthrough": 0,
            "visual": "glass3",
            "radius": 0.2,
            "minimalhit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitLAileron_Link [Indent level: 2],
        "hitlaileron_link": {
            "armor": 1.8,
            "explosionshielding": 3.5,
            "name": "HitLAileron_Link",
            "passthrough": 0,
            "visual": "Hit_AileronL",
            "radius": 0.09,
            "minimalhit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitRAileron_Link [Indent level: 2],
        "hitraileron_link": {
            "armor": 1.8,
            "explosionshielding": 3.5,
            "name": "HitRAileron_Link",
            "passthrough": 0,
            "visual": "Hit_AileronR",
            "radius": 0.09,
            "minimalhit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitLAileron [Indent level: 2],
        "hitlaileron": {
            "armor": 1.5,
            "explosionshielding": 3,
            "name": "HitLAileron",
            "passthrough": 0.3,
            "visual": "Hit_AileronL",
            "radius": 0.3,
            "minimalhit": 0.05,
            "depends": "HitLAileron_Link",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitRAileron [Indent level: 2],
        "hitraileron": {
            "armor": 1.5,
            "explosionshielding": 3,
            "name": "HitRAileron",
            "passthrough": 0.3,
            "visual": "Hit_AileronR",
            "radius": 0.3,
            "minimalhit": 0.05,
            "depends": "HitRAileron_Link",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitLCRudder [Indent level: 2],
        "hitlcrudder": {
            "armor": 2,
            "explosionshielding": 3,
            "name": "HitLCRudder",
            "passthrough": 0.3,
            "visual": "Hit_RudderC",
            "radius": 0.3,
            "minimalhit": 0.05,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitLCElevator [Indent level: 2],
        "hitlcelevator": {
            "armor": 1.5,
            "explosionshielding": 3,
            "name": "HitLCElevator",
            "passthrough": 0.3,
            "visual": "Hit_ElevatorL",
            "radius": 0.3,
            "minimalhit": 0.05,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|HitPoints|HitRElevator [Indent level: 2],
        "hitrelevator": {
            "armor": 1.5,
            "explosionshielding": 3,
            "name": "HitRElevator",
            "passthrough": 0.3,
            "visual": "Hit_ElevatorR",
            "radius": 0.3,
            "minimalhit": 0.05,
            "depends": "0",
            "material": -1
        }
    },
    # Class: CfgVehicles|RHS_L159_base|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|HitGlass2 [Indent level: 2]
        "hitglass2": {
            "source": "Hit",
            "hitpoint": "HitGlass2",
            "raw": 1
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|eject [Indent level: 2],
        "eject": {
            "source": "user",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|eject_hide [Indent level: 2],
        "eject_hide": {
            "source": "user",
            "animperiod": 0.6,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|Damper_1_source [Indent level: 2],
        "damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|Damper_2_source [Indent level: 2],
        "damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|Damper_3_source [Indent level: 2],
        "damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|Wheel_1_source [Indent level: 2],
        "wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|Wheel_2_source [Indent level: 2],
        "wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|Wheel_3_source [Indent level: 2],
        "wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|hit_pylon_1_source [Indent level: 2],
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|hit_pylon_2_source [Indent level: 2],
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|hit_pylon_3_source [Indent level: 2],
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|hit_pylon_4_source [Indent level: 2],
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|hit_pylon_5_source [Indent level: 2],
        "hit_pylon_5_source": {
            "source": "Hit",
            "hitpoint": "HitPylon5"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|hit_pylon_6_source [Indent level: 2],
        "hit_pylon_6_source": {
            "source": "Hit",
            "hitpoint": "HitPylon6"
        },
        # Class: CfgVehicles|RHS_L159_base|AnimationSources|hit_pylon_7_source [Indent level: 2],
        "hit_pylon_7_source": {
            "source": "Hit",
            "hitpoint": "HitPylon7"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|AddScalpel [Indent level: 2],
        "addscalpel": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|AddAsraam_out [Indent level: 2],
        "addasraam_out": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|AddAsraam_mid [Indent level: 2],
        "addasraam_mid": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|AddMk82 [Indent level: 2],
        "addmk82": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|AddGbu12 [Indent level: 2],
        "addgbu12": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|AddZephyr [Indent level: 2],
        "addzephyr": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|AddDar [Indent level: 2],
        "adddar": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|Muzzle_flash [Indent level: 2],
        "muzzle_flash": {
            "source": "ammorandom",
            "weapon": "Twin_Cannon_20mm"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|HitGlass1 [Indent level: 2],
        "hitglass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|HitGlass3 [Indent level: 2],
        "hitglass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|HitAvionics [Indent level: 2],
        "hitavionics": {
            "source": "Hit",
            "hitpoint": "HitAvionics",
            "raw": 1
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|HideWeapons [Indent level: 2],
        "hideweapons": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|canopy_hide [Indent level: 2],
        "canopy_hide": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|ejection_seat_hide [Indent level: 2],
        "ejection_seat_hide": {
            "source": "user",
            "animperiod": 0.001,
            "initphase": 0
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|AnimationSources|ejection_seat_motion [Indent level: 2],
        "ejection_seat_motion": {
            "source": "user",
            "animperiod": 0.25,
            "initphase": 0
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightRed_source [Indent level: 2],
        "collisionlightred_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionRed"
        },
        # Class: CfgVehicles|Air|AnimationSources|CollisionLightWhite_source [Indent level: 2],
        "collisionlightwhite_source": {
            "source": "MarkerLight",
            "markerlight": "CollisionWhite"
        }
    },
    "hiddenselections": ["camo1","camo2","i1","i2","n1","n2"],
    "hiddenselectionstextures": ["|rhsgref|addons|rhsgref_air|l159|data|l159_body_1_co.paa","|rhsgref|addons|rhsgref_air|l159|Data|l159_body_2_co.paa"],
    # Class: CfgVehicles|RHS_L159_base|Library [Indent level: 1],
    "library": {
        "libtextdesc": "The A-143 Buzzard is a single seat light multi-purpose combat aircraft able to carry a wide range of equipment and weaponry. A-143 has seven weapon hardpoints, three under each wing and one under the fuselage. Standard armament consists of 20mm cannon, and a mixture of AA and AG rockets."
    },
    # Class: CfgVehicles|RHS_L159_base|MarkerLights [Indent level: 1],
    "markerlights": {
        # Class: CfgVehicles|RHS_L159_base|MarkerLights|PositionRed [Indent level: 2]
        "positionred": {
            "color": [1,0,0],
            "ambient": [0.1,0,0],
            "intensity": 75,
            "name": "cerveny pozicni",
            "drawlight": 1,
            "drawlightsize": 0.15,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|RHS_L159_base|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|RHS_L159_base|MarkerLights|PositionGreen [Indent level: 2],
        "positiongreen": {
            "color": [0,1,0],
            "ambient": [0,0.1,0],
            "name": "zeleny pozicni",
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.15,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|RHS_L159_base|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        },
        # Class: CfgVehicles|RHS_L159_base|MarkerLights|PositionWhite [Indent level: 2],
        "positionwhite": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "light_nav_back",
            "intensity": 75,
            "drawlight": 1,
            "drawlightsize": 0.15,
            "drawlightcentersize": 0.04,
            "activelight": 0,
            "blinking": 0,
            "daylight": 0,
            "useflare": 0,
            # Class: CfgVehicles|RHS_L159_base|MarkerLights|PositionRed|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardlimitstart": 0.75,
                "hardlimitend": 1
            }
        }
    },
    # Class: CfgVehicles|RHS_L159_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|RHS_L159_base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "position": "l svetlo",
            "selection": "l svetlo",
            "direction": "konec l svetla",
            "hitpoint": "l svetlo",
            "innerangle": 20,
            "outerangle": 60,
            "conefadecoef": 10,
            "intensity": 50,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 1,
            "size": 1,
            # Class: CfgVehicles|RHS_L159_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardlimitstart": 150,
                "hardlimitend": 300
            }
        },
        # Class: CfgVehicles|RHS_L159_base|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "p svetlo",
            "direction": "konec p svetla",
            "hitpoint": "p svetlo",
            "selection": "p svetlo",
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "innerangle": 20,
            "outerangle": 60,
            "conefadecoef": 10,
            "intensity": 50,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 1,
            "size": 1,
            # Class: CfgVehicles|RHS_L159_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardlimitstart": 150,
                "hardlimitend": 300
            }
        },
        # Class: CfgVehicles|RHS_L159_base|Reflectors|Center [Indent level: 2],
        "center": {
            "position": "svetlo",
            "direction": "svetlo dir",
            "hitpoint": "svetlo",
            "selection": "svetlo",
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "innerangle": 20,
            "outerangle": 60,
            "conefadecoef": 10,
            "intensity": 50,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 1,
            "size": 1,
            # Class: CfgVehicles|RHS_L159_base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardlimitstart": 150,
                "hardlimitend": 300
            }
        }
    },
    "aggregatereflectors": [["Left"],["Right"],["Center"]],
    # Class: CfgVehicles|RHS_L159_base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|RHS_L159_base|Exhausts|Exhaust_1 [Indent level: 2]
        "exhaust_1": {
            "position": "exhaust_start",
            "direction": "exhaust_dir",
            "effect": "ExhaustsEffectJet"
        }
    },
    # Class: CfgVehicles|RHS_L159_base|WingVortices [Indent level: 1],
    "wingvortices": {
        # Class: CfgVehicles|RHS_L159_base|WingVortices|WingTipLeft [Indent level: 2]
        "wingtipleft": {
            "effectname": "WingVortices",
            "position": "cerveny pozicni"
        },
        # Class: CfgVehicles|RHS_L159_base|WingVortices|WingTipRight [Indent level: 2],
        "wingtipright": {
            "effectname": "WingVortices",
            "position": "zeleny pozicni"
        },
        # Class: CfgVehicles|RHS_L159_base|WingVortices|BodyLeft [Indent level: 2],
        "bodyleft": {
            "effectname": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles|RHS_L159_base|WingVortices|BodyRight [Indent level: 2],
        "bodyright": {
            "effectname": "BodyVortices",
            "position": "body_vapour_R_S"
        }
    },
    "driveraction": "RHS_L159_pilot",
    "envelope": [0,0.15,1.1,3,5,5.83,6,5.85,5.5,4.8,3.6,1.8,0],
    "weapons": [],
    "magazines": [],
    # Class: CfgVehicles|RHS_L159_base|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsgref|addons|rhsgref_air|L159|data|L159_body_1.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_body_1_damage.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_body_1_destruct.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_body_2.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_body_2_damage.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_body_2_destruct.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass_damage.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass_destruct.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass_in.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass_damage.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass_destruct.rvmat"]
    },
    # Class: CfgVehicles|RHS_L159_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|RHS_L159_base|Components|TransportPylonsComponent [Indent level: 2]
        "transportpylonscomponent": {
            "uipicture": "A3|Air_F_Gamma|Plane_Fighter_03|Data|UI|Plane_A143_3DEN_CA.paa",
            # Class: CfgVehicles|RHS_L159_base|Components|TransportPylonsComponent|Pylons [Indent level: 3],
            "pylons": {
                # Class: CfgVehicles|RHS_L159_base|Components|TransportPylonsComponent|Pylons|Pylons1 [Indent level: 4]
                "pylons1": {
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_AIM9","RHS_HP_AIM120"],
                    "attachment": "rhs_mag_Sidewinder",
                    "priority": 5,
                    "maxweight": 200,
                    "uiposition": [0.35,0.08],
                    "hitpoint": "HitPylon1"
                },
                # Class: CfgVehicles|RHS_L159_base|Components|TransportPylonsComponent|Pylons|Pylons2 [Indent level: 4],
                "pylons2": {
                    "priority": 4,
                    "attachment": "rhs_mag_FFAR_7_USAF",
                    "maxweight": 320,
                    "uiposition": [0.345,0.13],
                    "hitpoint": "HitPylon2",
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_AIM9","RHS_HP_AIM120"]
                },
                # Class: CfgVehicles|RHS_L159_base|Components|TransportPylonsComponent|Pylons|Pylons3 [Indent level: 4],
                "pylons3": {
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_LGB_500","RHS_HP_BOMB_500_3x","RHS_HP_AIM9","RHS_HP_AIM120","RHS_HP_ZPL20","RHS_HP_L159_FUELPOD"],
                    "priority": 3,
                    "attachment": "rhs_mag_mk82",
                    "maxweight": 400,
                    "uiposition": [0.34,0.18],
                    "hitpoint": "HitPylon3"
                },
                # Class: CfgVehicles|RHS_L159_base|Components|TransportPylonsComponent|Pylons|Pylons4 [Indent level: 4],
                "pylons4": {
                    "priority": 2,
                    "attachment": "rhs_mag_zpl20_hei",
                    "maxweight": 500,
                    "uiposition": [0.27,0.28],
                    "hardpoints": ["RHS_HP_ZPL20","RHS_HP_L159_FUELPOD"],
                    "hitpoint": "HitPylon4"
                },
                # Class: CfgVehicles|RHS_L159_base|Components|TransportPylonsComponent|Pylons|Pylons5 [Indent level: 4],
                "pylons5": {
                    "uiposition": [0.33,0.38],
                    "mirroredmissilepos": 3,
                    "hitpoint": "HitPylon5",
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_LGB_500","RHS_HP_BOMB_500_3x","RHS_HP_AIM9","RHS_HP_AIM120","RHS_HP_ZPL20","RHS_HP_L159_FUELPOD"],
                    "priority": 3,
                    "attachment": "rhs_mag_mk82",
                    "maxweight": 400
                },
                # Class: CfgVehicles|RHS_L159_base|Components|TransportPylonsComponent|Pylons|Pylons6 [Indent level: 4],
                "pylons6": {
                    "uiposition": [0.33,0.43],
                    "mirroredmissilepos": 2,
                    "hitpoint": "HitPylon6",
                    "priority": 4,
                    "attachment": "rhs_mag_FFAR_7_USAF",
                    "maxweight": 320,
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_AIM9","RHS_HP_AIM120"]
                },
                # Class: CfgVehicles|RHS_L159_base|Components|TransportPylonsComponent|Pylons|Pylons7 [Indent level: 4],
                "pylons7": {
                    "uiposition": [0.34,0.48],
                    "mirroredmissilepos": 1,
                    "hitpoint": "HitPylon7",
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_AIM9","RHS_HP_AIM120"],
                    "attachment": "rhs_mag_Sidewinder",
                    "priority": 5,
                    "maxweight": 200
                },
                # Class: CfgVehicles|RHS_L159_base|Components|TransportPylonsComponent|Pylons|cmDispenser [Indent level: 4],
                "cmdispenser": {
                    "hardpoints": ["RHSUSF_cm_ANALE40","RHSUSF_cm_ANALE40_x2"],
                    "priority": 1,
                    "attachment": "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x2",
                    "maxweight": 800,
                    "uiposition": [0.625,0.275]
                }
            }
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent [Indent level: 2],
        "sensorsmanagercomponent": {
            # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|IRSensorComponent [Indent level: 4]
                "irsensorcomponent": {
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|IRSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 500,
                        "maxrange": 4000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|IRSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 500,
                        "maxrange": 3000,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "anglerangehorizontal": 26,
                    "anglerangevertical": 20,
                    "maxtrackablespeed": 100,
                    "aimdown": 0,
                    "animdirection": "PilotCamera_V",
                    "componenttype": "IRSensorComponent",
                    "typerecognitiondistance": 2000,
                    "maxfogseethrough": 0.995,
                    "color": [1,0,0,1],
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|VisualSensorComponent [Indent level: 4],
                "visualsensorcomponent": {
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|VisualSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 500,
                        "maxrange": 3000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": 1
                    },
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|VisualSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 500,
                        "maxrange": 2000,
                        "objectdistancelimitcoef": 1,
                        "viewdistancelimitcoef": 1
                    },
                    "anglerangehorizontal": 26,
                    "anglerangevertical": 20,
                    "maxtrackablespeed": 100,
                    "aimdown": 0,
                    "animdirection": "PilotCamera_V",
                    "componenttype": "VisualSensorComponent",
                    "nightrangecoef": 0,
                    "maxfogseethrough": 0.94,
                    "color": [1,1,0.5,0.8],
                    "typerecognitiondistance": 2000,
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "mintrackablespeed": -1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent [Indent level: 4],
                "activeradarsensorcomponent": {
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|AirTarget [Indent level: 5]
                    "airtarget": {
                        "minrange": 8000,
                        "maxrange": 8000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|ActiveRadarSensorComponent|GroundTarget [Indent level: 5],
                    "groundtarget": {
                        "minrange": 4000,
                        "maxrange": 4000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 90,
                    "anglerangevertical": 90,
                    "componenttype": "ActiveRadarSensorComponent",
                    "typerecognitiondistance": 3000,
                    "groundnoisedistancecoef": 0.5,
                    "maxgroundnoisedistance": 200,
                    "minspeedthreshold": 20.8333,
                    "maxspeedthreshold": 27.7778,
                    "color": [0,1,1,1],
                    "allowsmarking": 1,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|PassiveRadarSensorComponent [Indent level: 4],
                "passiveradarsensorcomponent": {
                    "componenttype": "PassiveRadarSensorComponent",
                    # Class: SensorTemplatePassiveRadar|AirTarget [Indent level: 0],
                    "airtarget": {
                        "minrange": 16000,
                        "maxrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: SensorTemplatePassiveRadar|GroundTarget [Indent level: 0],
                    "groundtarget": {
                        "minrange": 16000,
                        "maxrange": 16000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "typerecognitiondistance": 12000,
                    "anglerangehorizontal": 360,
                    "anglerangevertical": 360,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "color": [0.5,1,0.5,0.5],
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010,
                    "allowsmarking": 0
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|LaserSensorComponent [Indent level: 4],
                "lasersensorcomponent": {
                    "componenttype": "LaserSensorComponent",
                    # Class: SensorTemplateLaser|AirTarget [Indent level: 0],
                    "airtarget": {
                        "minrange": 6000,
                        "maxrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: SensorTemplateLaser|GroundTarget [Indent level: 0],
                    "groundtarget": {
                        "minrange": 6000,
                        "maxrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 180,
                    "anglerangevertical": 180,
                    "typerecognitiondistance": 0,
                    "color": [1,1,1,0],
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|SensorsManagerComponent|Components|NVSensorComponent [Indent level: 4],
                "nvsensorcomponent": {
                    "componenttype": "NVSensorComponent",
                    "color": [1,1,1,0],
                    # Class: SensorTemplateLaser|AirTarget [Indent level: 0],
                    "airtarget": {
                        "minrange": 6000,
                        "maxrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    # Class: SensorTemplateLaser|GroundTarget [Indent level: 0],
                    "groundtarget": {
                        "minrange": 6000,
                        "maxrange": 6000,
                        "objectdistancelimitcoef": -1,
                        "viewdistancelimitcoef": -1
                    },
                    "anglerangehorizontal": 180,
                    "anglerangevertical": 180,
                    "typerecognitiondistance": 0,
                    "allowsmarking": 1,
                    "groundnoisedistancecoef": -1,
                    "maxgroundnoisedistance": -1,
                    "minspeedthreshold": 0,
                    "maxspeedthreshold": 0,
                    "animdirection": "",
                    "aimdown": 0,
                    "mintrackablespeed": -1e+010,
                    "maxtrackablespeed": 1e+010,
                    "mintrackableatl": -1e+010,
                    "maxtrackableatl": 1e+010
                }
            }
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components [Indent level: 3]
            "components": {
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components|UAVDisplay [Indent level: 4],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components|VehicleDriverDisplay [Indent level: 4],
                "vehicledriverdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Driver"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components|VehicleMissileDisplay [Indent level: 4],
                "vehiclemissiledisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Missile"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentLeft|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [8000,4000,2000,16000],
                    "resource": "RscCustomInfoSensors"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            "defaultdisplay": "SensorDisplay",
            # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components|EmptyDisplay [Indent level: 4]
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components|MinimapDisplay [Indent level: 4],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components|UAVDisplay [Indent level: 4],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components|VehicleDriverDisplay [Indent level: 4],
                "vehicledriverdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Driver"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components|VehicleMissileDisplay [Indent level: 4],
                "vehiclemissiledisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Missile"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|Components|VehicleSystemsDisplayManagerComponentRight|Components|SensorDisplay [Indent level: 4],
                "sensordisplay": {
                    "componenttype": "SensorsDisplayComponent",
                    "range": [8000,4000,2000,16000],
                    "resource": "RscCustomInfoSensors"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Air|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    "features": "Randomization: No						<br />Camo selections: 2 - the main body, wings and lower part of body						<br />Script door sources: None						<br />Script animations: AddScalpel, AddAsraam_out, AddAsraam_mid, AddMk82, AddGbu12, AddZephyr, AddDar						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: None",
    "mapsize": 13.02,
    "_generalmacro": "Plane_Fighter_03_base_F",
    "icon": "A3|Air_F_Gamma|Plane_Fighter_03|Data|UI|Map_Plane_Fighter_03_CA.paa",
    "picture": "A3|Air_F_Gamma|Plane_Fighter_03|Data|UI|Plane_Fighter_03_CA.paa",
    "editorsubcategory": "EdSubcat_Planes",
    "accuracy": 0.2,
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "armor": 55,
    "armorstructural": 2,
    "armorlights": 0.1,
    "mintotaldamagethreshold": 0.008,
    "waterleakiness": 1.5,
    "epeimpulsedamagecoef": 50,
    "damageresistance": 0.004,
    "destrtype": "DestructWreck",
    "slingloadcargomemorypoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "viewdrivershadowdiff": 0.5,
    "viewdrivershadowamb": 0.5,
    "radartargetsize": 0.8,
    "visualtargetsize": 0.8,
    "irtargetsize": 0.8,
    "lockdetectionsystem": 8,
    "incomingmissiledetectionsystem": "8 + 16",
    "cost": 3e+006,
    # Class: CfgVehicles|Plane_Fighter_03_base_F|Turrets [Indent level: 1],
    "turrets": {
    },
    # Class: CfgVehicles|Plane_Fighter_03_base_F|TransportItems [Indent level: 1],
    "transportitems": {
    },
    "attenuationeffecttype": "PlaneAttenuation",
    "soundgetin": ["A3|Sounds_F|air|Plane_Fighter_03|buzzard_getin",1,1,40],
    "soundgetout": ["A3|Sounds_F|air|Plane_Fighter_03|getout",1,1,40],
    "cabinopensound": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinOpen",1.77828,1,40],
    "cabinclosesound": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinClose",1.77828,1,40],
    "cabinopensoundinternal": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinOpen",10,1,40],
    "cabinclosesoundinternal": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinClose",10,1,40],
    "sounddammage": ["A3|Sounds_F|debugsound",1.77828,1,100],
    "soundengineonint": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-start_int",1,1],
    "soundengineonext": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-start_ext",1.77828,1,500],
    "soundengineoffint": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-stop_int",1,1],
    "soundengineoffext": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-stop_ext",1.77828,1,500],
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.316228,1],
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_1",0.316228,1.5],
    "soundgearup": ["A3|Sounds_F_EPC|CAS_02|gear_up",0.794328,1,150],
    "soundgeardown": ["A3|Sounds_F_EPC|CAS_02|gear_down",0.794328,1,150],
    "soundflapsup": ["A3|Sounds_F_EPC|CAS_02|Flaps_Up",0.630957,1,100],
    "soundflapsdown": ["A3|Sounds_F_EPC|CAS_02|Flaps_Down",0.630957,1,100],
    "buildcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "buildcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "buildcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "buildcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundbuildingcrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "woodcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_1",3.16228,1,900],
    "woodcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_2",3.16228,1,900],
    "woodcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_6",3.16228,1,900],
    "woodcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_wood_ext_8",3.16228,1,900],
    "soundwoodcrash": ["woodCrash0",0.25,"woodCrash1",0.25,"woodCrash2",0.25,"woodCrash3",0.25],
    "armorcrash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "armorcrash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "armorcrash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "armorcrash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundarmorcrash": ["ArmorCrash0",0.25,"ArmorCrash1",0.25,"ArmorCrash2",0.25,"ArmorCrash3",0.25],
    "crash0": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_1",1,1,900],
    "crash1": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_2",1,1,900],
    "crash2": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_3",1,1,900],
    "crash3": ["A3|Sounds_F|vehicles|crashes|cars|cars_coll_big_default_ext_4",1,1,900],
    "soundcrashes": ["Crash0",0.25,"Crash1",0.25,"Crash2",0.25,"Crash3",0.25],
    "soundwatercollision1": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_1",1.41254,1,500],
    "soundwatercollision2": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_2",1.41254,1,500],
    "soundwatercrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "landingsoundint0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int1",1,1,100],
    "landingsoundint1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int2",1,1,100],
    "landingsoundint": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingsoundout0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext1",1.77828,1,100],
    "landingsoundout1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext2",1.77828,1,100],
    "landingsoundout": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    # Class: CfgVehicles|Plane_Fighter_03_base_F|scrubLandInt [Indent level: 1],
    "scrublandint": {
        "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
        "frequency": 1,
        "volume": "(scrubLand factor[0.01, 0.20])"
    },
    # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|EngineLowOut [Indent level: 2]
        "enginelowout": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03_low_ext",1.41254,1,1200],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "camPos*2*(rpm factor[0.95, 0])*(rpm factor[0, 0.95])"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|EngineHighOut [Indent level: 2],
        "enginehighout": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03_engi_ext",1.41254,1.2,1400],
            "frequency": "1",
            "volume": "camPos*4*(rpm factor[0.5, 1.1])*(rpm factor[1.1, 0.5])"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|ForsageOut [Indent level: 2],
        "forsageout": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-fors_ext",1.12202,0.99,1700],
            "frequency": "1",
            "volume": "engineOn*camPos*(thrust factor[0.6, 1.0])",
            "cone": [3.14,3.92,2,0.5]
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|WindNoiseOut [Indent level: 2],
        "windnoiseout": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|noise",0.562341,1,150],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "camPos*(speed factor[1, 150])"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|EngineLowIn [Indent level: 2],
        "enginelowin": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03_low_int",1,1],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "(1-camPos)*((rpm factor[0.7, 0.1])*(rpm factor[0.1, 0.7]))"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|EngineHighIn [Indent level: 2],
        "enginehighin": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03_engi_int",0.562341,1.2],
            "frequency": "1",
            "volume": "(1-camPos)*(rpm factor[0.85, 1.0])"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|ForsageIn [Indent level: 2],
        "forsagein": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-fors_int",0.562341,1],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.6, 1.0]))"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|WindNoiseIn [Indent level: 2],
        "windnoisein": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|noise_int",0.398107,1],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "(1-camPos)*(speed factor[1, 150])"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|RainExt [Indent level: 2],
        "rainext": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1.77828,1,100],
            "frequency": 1,
            "volume": "camPos * rain * (speed factor[50, 0])"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|RainInt [Indent level: 2],
        "rainint": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos) * rain * (speed factor[50, 0])"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|Waternoise_ext [Indent level: 2],
        "waternoise_ext": {
            "sound": ["A3|Sounds_F|vehicles|noises|air_driving_in_water",0.707946,1,300],
            "frequency": "1",
            "volume": "(speed factor[0, 5]) * water * camPos + (speed factor[-0.1, -5]) * water * camPos"
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Sounds|Waternoise_int [Indent level: 2],
        "waternoise_int": {
            "sound": ["A3|Sounds_F|vehicles|noises|soft_driving_in_water_int",0.562341,1,100],
            "frequency": "1",
            "volume": "(speed factor[0, 5]) * water * (1-camPos) + (speed factor[-0.1, -5]) * water * (1-camPos)"
        }
    },
    "maxomega": 2000,
    "antirollbarforcecoef": 0,
    "antirollbarforcelimit": 0,
    "antirollbarspeedmin": 50,
    "antirollbarspeedmax": 300,
    # Class: CfgVehicles|Plane_Fighter_03_base_F|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Wheels|Wheel_1 [Indent level: 2]
        "wheel_1": {
            "bonename": "Wheel_1",
            "steering": 1,
            "side": "left",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.4,
            "mass": 20,
            "moi": 0.4,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxbraketorque": 0,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "suspforceapppointoffset": "Wheel_1_center",
            "tireforceapppointoffset": "Wheel_1_center",
            "maxcompression": 0.1,
            "maxdroop": 0.1,
            "sprungmass": 1500,
            "springstrength": 150000,
            "springdamperrate": 30000,
            "longitudinalstiffnessperunitgravity": 300,
            "latstiffx": 3,
            "latstiffy": 20,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Wheels|Wheel_2 [Indent level: 2],
        "wheel_2": {
            "steering": 0,
            "bonename": "Wheel_2",
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "mass": 35,
            "moi": 1.575,
            "width": 0.6,
            "maxbraketorque": 1500,
            "maxcompression": 0.05,
            "maxdroop": 0.05,
            "sprungmass": 3350,
            "springstrength": 335000,
            "springdamperrate": 67000,
            "longitudinalstiffnessperunitgravity": 500,
            "suspforceapppointoffset": "Wheel_2_center",
            "tireforceapppointoffset": "Wheel_2_center",
            "side": "left",
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "latstiffx": 3,
            "latstiffy": 20,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|Wheels|Wheel_3 [Indent level: 2],
        "wheel_3": {
            "bonename": "Wheel_3",
            "side": "right",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspforceapppointoffset": "Wheel_3_center",
            "tireforceapppointoffset": "Wheel_3_center",
            "steering": 0,
            "mass": 35,
            "moi": 1.575,
            "width": 0.6,
            "maxbraketorque": 1500,
            "maxcompression": 0.05,
            "maxdroop": 0.05,
            "sprungmass": 3350,
            "springstrength": 335000,
            "springdamperrate": 67000,
            "longitudinalstiffnessperunitgravity": 500,
            "dampingrate": 0.1,
            "dampingratedamaged": 1,
            "dampingratedestroyed": 1000,
            "maxhandbraketorque": 0,
            "susptraveldirection": [0,-1,0],
            "latstiffx": 3,
            "latstiffy": 20,
            "frictionvsslipgraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    "maxspeed": 800,
    "landingaoa": "6*3.1415/180",
    "landingspeed": 215,
    "stallspeed": 190,
    "stallwarningtreshold": 0.1,
    "wheelsteeringsensitivity": 2,
    "airbrake": 1,
    "airbrakefrictioncoef": 2.2,
    "flaps": 1,
    "flapsfrictioncoef": 0.32,
    "gearsupfrictioncoef": 0.6,
    "airfrictioncoefs0": [0,0,0],
    "airfrictioncoefs1": [0.1,0.5,0.0066],
    "airfrictioncoefs2": [0.001,0.005,6.8e-005],
    "angleofindicence": "-2*3.1415/180",
    "altnoforce": 13000,
    "altfullforce": 2000,
    "thrustcoef": [1.42,1.38,1.34,1.3,1.25,1.2,1.19,1.18,1.17,1.17,1.16,1.16,0.1,0,0,0,0],
    "aileronsensitivity": 1,
    "aileroncoef": [0,0.11,0.45,0.81,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.43,1.45,1.47,1.4,1.2,0.8],
    "elevatorsensitivity": 1.1,
    "elevatorcoef": [0,0.14,0.54,0.62,0.58,0.56,0.54,0.52,0.48,0.43,0.38,0.35,0.3,0.25,0.2,0.15,0.1],
    "rudderinfluence": 0.866,
    "ruddercoef": [0,0.8,2,2.2,2.3,2.4,2.3,2.2,2.1,2,1.2],
    "aileroncontrolssensitivitycoef": 3.6,
    "elevatorcontrolssensitivitycoef": 3.4,
    "ruddercontrolssensitivitycoef": 3.8,
    "draconicforcexcoef": 8,
    "draconicforceycoef": 1.4,
    "draconicforcezcoef": 1,
    "draconictorquexcoef": [4.8,5,5.5,6.2,7,7.7,9.4,11.1,12,14,15],
    "draconictorqueycoef": [12,10,6,2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
    # Class: CfgVehicles|Plane_Fighter_03_base_F|TextureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|Plane_Fighter_03_base_F|TextureSources|Hex [Indent level: 2]
        "hex": {
            "displayname": "Hex",
            "author": "Bohemia Interactive",
            "factions": ["OPF_F","OPF_T_F"],
            "textures": ["|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_1_brownhex_CO.paa","|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_2_brownhex_CO.paa"]
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|TextureSources|Green [Indent level: 2],
        "green": {
            "displayname": "AAF",
            "author": "Bohemia Interactive",
            "factions": ["IND_F"],
            "textures": ["|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_1_INDP_CO.paa","|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_2_INDP_CO.paa"]
        },
        # Class: CfgVehicles|Plane_Fighter_03_base_F|TextureSources|Grey [Indent level: 2],
        "grey": {
            "displayname": "Grey",
            "author": "Bohemia Interactive",
            "factions": ["OPF_F","OPF_T_F"],
            "textures": ["|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_1_greyhex_CO.paa","|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_2_greyhex_CO.paa"]
        }
    },
    "driveoncomponent": [],
    "irscanrangemin": 500,
    "irscanrangemax": 5000,
    "irscantoeyefactor": 2,
    "laserscanner": 1,
    "showalltargets": 4,
    "gunaimdown": 0.029,
    "extcameraposition": [0,3.8,-15],
    # Class: CfgVehicles|Plane_Fighter_03_base_F|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": -3,
        "initfov": 0.75,
        "minfov": 0.25,
        "maxfov": 1.25,
        "initangley": 0,
        "minanglex": -65,
        "maxanglex": 85,
        "minangley": -150,
        "maxangley": 150,
        "minmovex": -0.2,
        "maxmovex": 0.2,
        "minmovey": -0.1,
        "maxmovey": 0.1,
        "minmovez": -0.1,
        "maxmovez": 0.2,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "memorypointlrocket": "Rocket_1",
    "memorypointrrocket": "Rocket_2",
    "minfiretime": 30,
    "threat": [0.8,1,0.8],
    "memorypointdriveroptics": "PilotCamera_pos",
    "driverweaponsinfotype": "RscOptics_CAS_01_TGP",
    "defaultusermfdvalues": [0,0.5,0.4,1],
    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD [Indent level: 2]
        "airplanehud": {
            "enableparallax": 1,
            "topleft": "HUD_1_top_left",
            "topright": "HUD_1_top_right",
            "bottomleft": "HUD_1_bottom_left",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,0.5,0.4,1],
            # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|PlaneW [Indent level: 4]
                "planew": {
                    "type": "fixed",
                    "pos": [0.4975,0.38]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|Center [Indent level: 4],
                "center": {
                    "type": "fixed",
                    "pos": [0.4975,0.383]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|ImpactPoint [Indent level: 4],
                "impactpoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|WPPoint [Indent level: 4],
                "wppoint": {
                    "type": "vector",
                    "source": "WPPoint",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|TargetingPodDir [Indent level: 4],
                "targetingpoddir": {
                    "source": "pilotcamera",
                    "type": "vector",
                    "pos0": [0.4975,0.383],
                    "pos10": [1.4475,1.453]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|TargetingPodTarget [Indent level: 4],
                "targetingpodtarget": {
                    "source": "pilotcameratarget",
                    "type": "vector",
                    "pos0": [0.4975,0.383],
                    "pos10": [1.4475,1.453]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|Limit0109 [Indent level: 4],
                "limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot1 [Indent level: 4],
                "missileflighttimerot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minangle": 0,
                    "maxangle": 18,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot2 [Indent level: 4],
                "missileflighttimerot2": {
                    "maxangle": 36,
                    "max": 1,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot3 [Indent level: 4],
                "missileflighttimerot3": {
                    "maxangle": 54,
                    "max": 1.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot4 [Indent level: 4],
                "missileflighttimerot4": {
                    "maxangle": 72,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot5 [Indent level: 4],
                "missileflighttimerot5": {
                    "maxangle": 90,
                    "max": 2.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot6 [Indent level: 4],
                "missileflighttimerot6": {
                    "maxangle": 108,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot7 [Indent level: 4],
                "missileflighttimerot7": {
                    "maxangle": 126,
                    "max": 3.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot8 [Indent level: 4],
                "missileflighttimerot8": {
                    "maxangle": 144,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot9 [Indent level: 4],
                "missileflighttimerot9": {
                    "maxangle": 162,
                    "max": 4.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot10 [Indent level: 4],
                "missileflighttimerot10": {
                    "maxangle": 180,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot11 [Indent level: 4],
                "missileflighttimerot11": {
                    "maxangle": 198,
                    "max": 5.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot12 [Indent level: 4],
                "missileflighttimerot12": {
                    "maxangle": 216,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot13 [Indent level: 4],
                "missileflighttimerot13": {
                    "maxangle": 234,
                    "max": 6.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot14 [Indent level: 4],
                "missileflighttimerot14": {
                    "maxangle": 252,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot15 [Indent level: 4],
                "missileflighttimerot15": {
                    "maxangle": 270,
                    "max": 7.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot16 [Indent level: 4],
                "missileflighttimerot16": {
                    "maxangle": 288,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|MissileFlightTimeRot17 [Indent level: 4],
                "missileflighttimerot17": {
                    "maxangle": 306,
                    "max": 8.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourcescale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|Target [Indent level: 4],
                "target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.4975,0.383],
                    "pos10": [1.4475,1.453]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|Velocity [Indent level: 4],
                "velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|ILS_H [Indent level: 4],
                "ils_h": {
                    "type": "ils",
                    "pos0": [0.5,0.383],
                    "pos3": [0.785,0.383]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|ILS_W [Indent level: 4],
                "ils_w": {
                    "pos3": [0.5,0.704],
                    "type": "ils",
                    "pos0": [0.5,0.383]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|ASL_Instrument [Indent level: 4],
                "asl_instrument": {
                    "type": "rotational",
                    "source": "altitudeASL",
                    "center": [0.9,0.337895],
                    "min": 0,
                    "max": 20000,
                    "minangle": 0,
                    "maxangle": 72000,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|Speed_Instrument [Indent level: 4],
                "speed_instrument": {
                    "source": "speed",
                    "center": [0.1,0.337895],
                    "max": 555.556,
                    "maxangle": 7200,
                    "type": "rotational",
                    "min": 0,
                    "minangle": 0,
                    "aspectratio": 1.12632
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|HorizonBankRot [Indent level: 4],
                "horizonbankrot": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "center": [0.4975,0.38],
                    "min": -0.5236,
                    "max": 0.5236,
                    "minangle": 159.25,
                    "maxangle": 200.75,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|AOAindexer [Indent level: 4],
                "aoaindexer": {
                    "type": "linear",
                    "source": "aoa",
                    "min": -0.7854,
                    "max": 0.7854,
                    "maxpos": [0,-1.9],
                    "minpos": [0,2.1],
                    "aspectratio": 1
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|HorizonBankRotFull [Indent level: 4],
                "horizonbankrotfull": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "center": [0,0],
                    "min": -3.1416,
                    "max": 3.1416,
                    "minangle": -180,
                    "maxangle": 180,
                    "aspectratio": 1
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|Level0 [Indent level: 4],
                "level0": {
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP5 [Indent level: 4],
                "levelp5": {
                    "angle": 5,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM5 [Indent level: 4],
                "levelm5": {
                    "angle": -5,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP10 [Indent level: 4],
                "levelp10": {
                    "angle": 10,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM10 [Indent level: 4],
                "levelm10": {
                    "angle": -10,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP15 [Indent level: 4],
                "levelp15": {
                    "angle": 15,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM15 [Indent level: 4],
                "levelm15": {
                    "angle": -15,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP20 [Indent level: 4],
                "levelp20": {
                    "angle": 20,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM20 [Indent level: 4],
                "levelm20": {
                    "angle": -20,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP25 [Indent level: 4],
                "levelp25": {
                    "angle": 25,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM25 [Indent level: 4],
                "levelm25": {
                    "angle": -25,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP30 [Indent level: 4],
                "levelp30": {
                    "angle": 30,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM30 [Indent level: 4],
                "levelm30": {
                    "angle": -30,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP35 [Indent level: 4],
                "levelp35": {
                    "angle": 35,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM35 [Indent level: 4],
                "levelm35": {
                    "angle": -35,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP40 [Indent level: 4],
                "levelp40": {
                    "angle": 40,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM40 [Indent level: 4],
                "levelm40": {
                    "angle": -40,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP45 [Indent level: 4],
                "levelp45": {
                    "angle": 45,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM45 [Indent level: 4],
                "levelm45": {
                    "angle": -45,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP50 [Indent level: 4],
                "levelp50": {
                    "angle": 50,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM50 [Indent level: 4],
                "levelm50": {
                    "angle": -50,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP55 [Indent level: 4],
                "levelp55": {
                    "angle": 55,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM55 [Indent level: 4],
                "levelm55": {
                    "angle": -55,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP60 [Indent level: 4],
                "levelp60": {
                    "angle": 60,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM60 [Indent level: 4],
                "levelm60": {
                    "angle": -60,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP65 [Indent level: 4],
                "levelp65": {
                    "angle": 65,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM65 [Indent level: 4],
                "levelm65": {
                    "angle": -65,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP70 [Indent level: 4],
                "levelp70": {
                    "angle": 70,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM70 [Indent level: 4],
                "levelm70": {
                    "angle": -70,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP75 [Indent level: 4],
                "levelp75": {
                    "angle": 75,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM75 [Indent level: 4],
                "levelm75": {
                    "angle": -75,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP80 [Indent level: 4],
                "levelp80": {
                    "angle": 80,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM80 [Indent level: 4],
                "levelm80": {
                    "angle": -80,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP85 [Indent level: 4],
                "levelp85": {
                    "angle": 85,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM85 [Indent level: 4],
                "levelm85": {
                    "angle": -85,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelP90 [Indent level: 4],
                "levelp90": {
                    "angle": 90,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|LevelM90 [Indent level: 4],
                "levelm90": {
                    "angle": -90,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|Airport1 [Indent level: 4],
                "airport1": {
                    "type": "vector",
                    "source": "airportCorner1",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|Airport2 [Indent level: 4],
                "airport2": {
                    "source": "airportCorner2",
                    "type": "vector",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|Airport3 [Indent level: 4],
                "airport3": {
                    "source": "airportCorner3",
                    "type": "vector",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Bones|Airport4 [Indent level: 4],
                "airport4": {
                    "source": "airportCorner4",
                    "type": "vector",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                }
            },
            # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw [Indent level: 3],
            "draw": {
                "alpha": "user3",
                "color": ["user0","user1","user2"],
                "condition": "on",
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|PlaneW [Indent level: 4],
                "planew": {
                    "type": "line",
                    "points": [["PlaneW",[-0.03,0],1],["PlaneW",[-0.01,0],1],[],["PlaneW",[0.03,0],1],["PlaneW",[0.01,0],1],[],["PlaneW",[0,-0.0337895],1],["PlaneW",[0,-0.0112632],1],[],["PlaneW",[0,0.0337895],1],["PlaneW",[0,0.0112632],1]]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|PlaneHeading [Indent level: 4],
                "planeheading": {
                    "type": "line",
                    "points": [["Velocity",1,"Limit0109",1,[0,-0.0225263],1],["Velocity",1,"Limit0109",1,[0.014,-0.0157684],1],["Velocity",1,"Limit0109",1,[0.02,0],1],["Velocity",1,"Limit0109",1,[0.014,0.0157684],1],["Velocity",1,"Limit0109",1,[0,0.0225263],1],["Velocity",1,"Limit0109",1,[-0.014,0.0157684],1],["Velocity",1,"Limit0109",1,[-0.02,0],1],["Velocity",1,"Limit0109",1,[-0.014,-0.0157684],1],["Velocity",1,"Limit0109",1,[0,-0.0225263],1],[],["Velocity",1,"Limit0109",1,[0.04,0],1],["Velocity",1,"Limit0109",1,[0.02,0],1],[],["Velocity",1,"Limit0109",1,[-0.04,0],1],["Velocity",1,"Limit0109",1,[-0.02,0],1],[],["Velocity",1,"Limit0109",1,[0,-0.0450526],1],["Velocity",1,"Limit0109",1,[0,-0.0225263],1]]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|AOAIndexer [Indent level: 4],
                "aoaindexer": {
                    "condition": "ils",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|AOAIndexer|lines [Indent level: 5],
                    "lines": {
                        "type": "line",
                        "points": [["Velocity",1,"Limit0109",1,["AOAindexer",-0.04,0.112632],1],["Velocity",1,"Limit0109",1,["AOAindexer",-0.06,0.112632],1],["Velocity",1,"Limit0109",1,["AOAindexer",-0.06,0],1],["Velocity",1,"Limit0109",1,["AOAindexer",-0.05,0],1],[],["Velocity",1,"Limit0109",1,["AOAindexer",-0.06,0],1],["Velocity",1,"Limit0109",1,["AOAindexer",-0.06,-0.112632],1],["Velocity",1,"Limit0109",1,["AOAindexer",-0.04,-0.112632],1]]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Static [Indent level: 4],
                "static": {
                    "type": "line",
                    "points": [[[0.0925,0.442079],1],[[0.1075,0.442079],1],[],[[0.1,0.433632],1],[[0.1,0.450526],1],[],[[0.14687,0.422182],1],[[0.16187,0.422182],1],[],[[0.15437,0.413734],1],[[0.15437,0.430629],1],[],[[0.180473,0.370089],1],[[0.195473,0.370089],1],[],[[0.187973,0.361642],1],[[0.187973,0.378537],1],[],[[0.180473,0.3057],1],[[0.195473,0.3057],1],[],[[0.187973,0.297253],1],[[0.187973,0.314147],1],[],[[0.14687,0.253608],1],[[0.16187,0.253608],1],[],[[0.15437,0.245161],1],[[0.15437,0.262055],1],[],[[0.0925,0.233711],1],[[0.1075,0.233711],1],[],[[0.1,0.225263],1],[[0.1,0.242158],1],[],[[0.0381299,0.253608],1],[[0.0531299,0.253608],1],[],[[0.0456299,0.245161],1],[[0.0456299,0.262055],1],[],[[0.00452726,0.3057],1],[[0.0195273,0.3057],1],[],[[0.0120273,0.297253],1],[[0.0120273,0.314147],1],[],[[0.00452728,0.370089],1],[[0.0195273,0.370089],1],[],[[0.0120273,0.361642],1],[[0.0120273,0.378537],1],[],[[0.0381299,0.422182],1],[[0.0531299,0.422182],1],[],[[0.0456299,0.413734],1],[[0.0456299,0.430629],1],[],["Speed_Instrument",[0,0.065],1],["Speed_Instrument",[0,0.085],1],[],[[0.8925,0.442079],1],[[0.9075,0.442079],1],[],[[0.9,0.433632],1],[[0.9,0.450526],1],[],[[0.94687,0.422182],1],[[0.96187,0.422182],1],[],[[0.95437,0.413734],1],[[0.95437,0.430629],1],[],[[0.980473,0.370089],1],[[0.995473,0.370089],1],[],[[0.987973,0.361642],1],[[0.987973,0.378537],1],[],[[0.980473,0.3057],1],[[0.995473,0.3057],1],[],[[0.987973,0.297253],1],[[0.987973,0.314147],1],[],[[0.94687,0.253608],1],[[0.96187,0.253608],1],[],[[0.95437,0.245161],1],[[0.95437,0.262055],1],[],[[0.8925,0.233711],1],[[0.9075,0.233711],1],[],[[0.9,0.225263],1],[[0.9,0.242158],1],[],[[0.83813,0.253608],1],[[0.85313,0.253608],1],[],[[0.84563,0.245161],1],[[0.84563,0.262055],1],[],[[0.804527,0.3057],1],[[0.819527,0.3057],1],[],[[0.812027,0.297253],1],[[0.812027,0.314147],1],[],[[0.804527,0.370089],1],[[0.819527,0.370089],1],[],[[0.812027,0.361642],1],[[0.812027,0.378537],1],[],[[0.83813,0.422182],1],[[0.85313,0.422182],1],[],[[0.84563,0.413734],1],[[0.84563,0.430629],1],[],["ASL_Instrument",[0,0.065],1],["ASL_Instrument",[0,0.085],1],[],[[0.5,0.107],1],[[0.51,0.129526],1],[[0.49,0.129526],1],[[0.5,0.107],1],[],[[0.619959,0.712986],1],[[0.631439,0.744203],1],[],[[0.58291,0.739019],1],[[0.588087,0.760778],1],[],[[0.540574,0.748504],1],[[0.543184,0.770838],1],[],[[0.4975,0.740421],1],[[0.4975,0.77421],1],[],[[0.454426,0.748504],1],[[0.451816,0.770838],1],[],[[0.41209,0.739019],1],[[0.406913,0.760778],1],[],[[0.375041,0.712986],1],[[0.363561,0.744203],1]]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|HorizonBankRot [Indent level: 4],
                "horizonbankrot": {
                    "type": "line",
                    "points": [["HorizonBankRot",[0,0.39421],1],["HorizonBankRot",[0.01,0.416737],1],["HorizonBankRot",[-0.01,0.416737],1],["HorizonBankRot",[0,0.39421],1]]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont [Indent level: 4],
                "horizont": {
                    "cliptl": [0,0.15],
                    "clipbr": [1,0.75],
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed [Indent level: 5],
                    "dimmed": {
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|Level0 [Indent level: 6]
                        "level0": {
                            "type": "line",
                            "points": [["Level0",[0.4,0],1],["Level0",[0.05,0],1],[],["Level0",[-0.05,0],1],["Level0",[-0.4,0],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM5 [Indent level: 6],
                        "levelm5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.2,0.005],1],["LevelM5",[-0.17,0.004],1],[],["LevelM5",[-0.14,0.003],1],["LevelM5",[-0.11,0.002],1],[],["LevelM5",[-0.08,0.001],1],["LevelM5",[-0.05,0],1],["LevelM5",[-0.05,-0.03],1],[],["LevelM5",[0.05,-0.03],1],["LevelM5",[0.05,0],1],["LevelM5",[0.08,0.001],1],[],["LevelM5",[0.11,0.002],1],["LevelM5",[0.14,0.003],1],[],["LevelM5",[0.17,0.004],1],["LevelM5",[0.2,0.005],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_5 [Indent level: 6],
                        "valm_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM5",[-0.18,-0.082],1],
                            "right": ["LevelM5",[-0.1,-0.082],1],
                            "down": ["LevelM5",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP5 [Indent level: 6],
                        "levelp5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.2,0.03],1],["LevelP5",[-0.2,0],1],["LevelP5",[-0.05,0],1],[],["LevelP5",[0.05,0],1],["LevelP5",[0.2,0],1],["LevelP5",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_5 [Indent level: 6],
                        "valp_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP5",[-0.18,0.032],1],
                            "right": ["LevelP5",[-0.1,0.032],1],
                            "down": ["LevelP5",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM10 [Indent level: 6],
                        "levelm10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.2,0.01],1],["LevelM10",[-0.17,0.008],1],[],["LevelM10",[-0.14,0.006],1],["LevelM10",[-0.11,0.004],1],[],["LevelM10",[-0.08,0.002],1],["LevelM10",[-0.05,0],1],["LevelM10",[-0.05,-0.03],1],[],["LevelM10",[0.05,-0.03],1],["LevelM10",[0.05,0],1],["LevelM10",[0.08,0.002],1],[],["LevelM10",[0.11,0.004],1],["LevelM10",[0.14,0.006],1],[],["LevelM10",[0.17,0.008],1],["LevelM10",[0.2,0.01],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_10 [Indent level: 6],
                        "valm_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM10",[-0.18,-0.082],1],
                            "right": ["LevelM10",[-0.1,-0.082],1],
                            "down": ["LevelM10",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP10 [Indent level: 6],
                        "levelp10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.2,0.03],1],["LevelP10",[-0.2,0],1],["LevelP10",[-0.05,0],1],[],["LevelP10",[0.05,0],1],["LevelP10",[0.2,0],1],["LevelP10",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_10 [Indent level: 6],
                        "valp_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP10",[-0.18,0.032],1],
                            "right": ["LevelP10",[-0.1,0.032],1],
                            "down": ["LevelP10",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM15 [Indent level: 6],
                        "levelm15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.2,0.015],1],["LevelM15",[-0.17,0.012],1],[],["LevelM15",[-0.14,0.009],1],["LevelM15",[-0.11,0.006],1],[],["LevelM15",[-0.08,0.003],1],["LevelM15",[-0.05,0],1],["LevelM15",[-0.05,-0.03],1],[],["LevelM15",[0.05,-0.03],1],["LevelM15",[0.05,0],1],["LevelM15",[0.08,0.003],1],[],["LevelM15",[0.11,0.006],1],["LevelM15",[0.14,0.009],1],[],["LevelM15",[0.17,0.012],1],["LevelM15",[0.2,0.015],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_15 [Indent level: 6],
                        "valm_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM15",[-0.18,-0.082],1],
                            "right": ["LevelM15",[-0.1,-0.082],1],
                            "down": ["LevelM15",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP15 [Indent level: 6],
                        "levelp15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.2,0.03],1],["LevelP15",[-0.2,0],1],["LevelP15",[-0.05,0],1],[],["LevelP15",[0.05,0],1],["LevelP15",[0.2,0],1],["LevelP15",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_15 [Indent level: 6],
                        "valp_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP15",[-0.18,0.032],1],
                            "right": ["LevelP15",[-0.1,0.032],1],
                            "down": ["LevelP15",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM20 [Indent level: 6],
                        "levelm20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.2,0.02],1],["LevelM20",[-0.17,0.016],1],[],["LevelM20",[-0.14,0.012],1],["LevelM20",[-0.11,0.008],1],[],["LevelM20",[-0.08,0.004],1],["LevelM20",[-0.05,0],1],["LevelM20",[-0.05,-0.03],1],[],["LevelM20",[0.05,-0.03],1],["LevelM20",[0.05,0],1],["LevelM20",[0.08,0.004],1],[],["LevelM20",[0.11,0.008],1],["LevelM20",[0.14,0.012],1],[],["LevelM20",[0.17,0.016],1],["LevelM20",[0.2,0.02],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_20 [Indent level: 6],
                        "valm_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM20",[-0.18,-0.082],1],
                            "right": ["LevelM20",[-0.1,-0.082],1],
                            "down": ["LevelM20",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP20 [Indent level: 6],
                        "levelp20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.2,0.03],1],["LevelP20",[-0.2,0],1],["LevelP20",[-0.05,0],1],[],["LevelP20",[0.05,0],1],["LevelP20",[0.2,0],1],["LevelP20",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_20 [Indent level: 6],
                        "valp_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP20",[-0.18,0.032],1],
                            "right": ["LevelP20",[-0.1,0.032],1],
                            "down": ["LevelP20",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM25 [Indent level: 6],
                        "levelm25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.2,0.025],1],["LevelM25",[-0.17,0.02],1],[],["LevelM25",[-0.14,0.015],1],["LevelM25",[-0.11,0.01],1],[],["LevelM25",[-0.08,0.005],1],["LevelM25",[-0.05,0],1],["LevelM25",[-0.05,-0.03],1],[],["LevelM25",[0.05,-0.03],1],["LevelM25",[0.05,0],1],["LevelM25",[0.08,0.005],1],[],["LevelM25",[0.11,0.01],1],["LevelM25",[0.14,0.015],1],[],["LevelM25",[0.17,0.02],1],["LevelM25",[0.2,0.025],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_25 [Indent level: 6],
                        "valm_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM25",[-0.18,-0.082],1],
                            "right": ["LevelM25",[-0.1,-0.082],1],
                            "down": ["LevelM25",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP25 [Indent level: 6],
                        "levelp25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.2,0.03],1],["LevelP25",[-0.2,0],1],["LevelP25",[-0.05,0],1],[],["LevelP25",[0.05,0],1],["LevelP25",[0.2,0],1],["LevelP25",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_25 [Indent level: 6],
                        "valp_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP25",[-0.18,0.032],1],
                            "right": ["LevelP25",[-0.1,0.032],1],
                            "down": ["LevelP25",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM30 [Indent level: 6],
                        "levelm30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.2,0.03],1],["LevelM30",[-0.17,0.024],1],[],["LevelM30",[-0.14,0.018],1],["LevelM30",[-0.11,0.012],1],[],["LevelM30",[-0.08,0.006],1],["LevelM30",[-0.05,0],1],["LevelM30",[-0.05,-0.03],1],[],["LevelM30",[0.05,-0.03],1],["LevelM30",[0.05,0],1],["LevelM30",[0.08,0.006],1],[],["LevelM30",[0.11,0.012],1],["LevelM30",[0.14,0.018],1],[],["LevelM30",[0.17,0.024],1],["LevelM30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_30 [Indent level: 6],
                        "valm_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM30",[-0.18,-0.082],1],
                            "right": ["LevelM30",[-0.1,-0.082],1],
                            "down": ["LevelM30",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP30 [Indent level: 6],
                        "levelp30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.2,0.03],1],["LevelP30",[-0.2,0],1],["LevelP30",[-0.05,0],1],[],["LevelP30",[0.05,0],1],["LevelP30",[0.2,0],1],["LevelP30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_30 [Indent level: 6],
                        "valp_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP30",[-0.18,0.032],1],
                            "right": ["LevelP30",[-0.1,0.032],1],
                            "down": ["LevelP30",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM35 [Indent level: 6],
                        "levelm35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.2,0.035],1],["LevelM35",[-0.17,0.028],1],[],["LevelM35",[-0.14,0.021],1],["LevelM35",[-0.11,0.014],1],[],["LevelM35",[-0.08,0.007],1],["LevelM35",[-0.05,0],1],["LevelM35",[-0.05,-0.03],1],[],["LevelM35",[0.05,-0.03],1],["LevelM35",[0.05,0],1],["LevelM35",[0.08,0.007],1],[],["LevelM35",[0.11,0.014],1],["LevelM35",[0.14,0.021],1],[],["LevelM35",[0.17,0.028],1],["LevelM35",[0.2,0.035],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_35 [Indent level: 6],
                        "valm_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM35",[-0.18,-0.082],1],
                            "right": ["LevelM35",[-0.1,-0.082],1],
                            "down": ["LevelM35",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP35 [Indent level: 6],
                        "levelp35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.2,0.03],1],["LevelP35",[-0.2,0],1],["LevelP35",[-0.05,0],1],[],["LevelP35",[0.05,0],1],["LevelP35",[0.2,0],1],["LevelP35",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_35 [Indent level: 6],
                        "valp_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP35",[-0.18,0.032],1],
                            "right": ["LevelP35",[-0.1,0.032],1],
                            "down": ["LevelP35",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM40 [Indent level: 6],
                        "levelm40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.2,0.04],1],["LevelM40",[-0.17,0.032],1],[],["LevelM40",[-0.14,0.024],1],["LevelM40",[-0.11,0.016],1],[],["LevelM40",[-0.08,0.008],1],["LevelM40",[-0.05,0],1],["LevelM40",[-0.05,-0.03],1],[],["LevelM40",[0.05,-0.03],1],["LevelM40",[0.05,0],1],["LevelM40",[0.08,0.008],1],[],["LevelM40",[0.11,0.016],1],["LevelM40",[0.14,0.024],1],[],["LevelM40",[0.17,0.032],1],["LevelM40",[0.2,0.04],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_40 [Indent level: 6],
                        "valm_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM40",[-0.18,-0.082],1],
                            "right": ["LevelM40",[-0.1,-0.082],1],
                            "down": ["LevelM40",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP40 [Indent level: 6],
                        "levelp40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.2,0.03],1],["LevelP40",[-0.2,0],1],["LevelP40",[-0.05,0],1],[],["LevelP40",[0.05,0],1],["LevelP40",[0.2,0],1],["LevelP40",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_40 [Indent level: 6],
                        "valp_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP40",[-0.18,0.032],1],
                            "right": ["LevelP40",[-0.1,0.032],1],
                            "down": ["LevelP40",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM45 [Indent level: 6],
                        "levelm45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.2,0.045],1],["LevelM45",[-0.17,0.036],1],[],["LevelM45",[-0.14,0.027],1],["LevelM45",[-0.11,0.018],1],[],["LevelM45",[-0.08,0.009],1],["LevelM45",[-0.05,0],1],["LevelM45",[-0.05,-0.03],1],[],["LevelM45",[0.05,-0.03],1],["LevelM45",[0.05,0],1],["LevelM45",[0.08,0.009],1],[],["LevelM45",[0.11,0.018],1],["LevelM45",[0.14,0.027],1],[],["LevelM45",[0.17,0.036],1],["LevelM45",[0.2,0.045],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_45 [Indent level: 6],
                        "valm_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM45",[-0.18,-0.082],1],
                            "right": ["LevelM45",[-0.1,-0.082],1],
                            "down": ["LevelM45",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP45 [Indent level: 6],
                        "levelp45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.2,0.03],1],["LevelP45",[-0.2,0],1],["LevelP45",[-0.05,0],1],[],["LevelP45",[0.05,0],1],["LevelP45",[0.2,0],1],["LevelP45",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_45 [Indent level: 6],
                        "valp_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP45",[-0.18,0.032],1],
                            "right": ["LevelP45",[-0.1,0.032],1],
                            "down": ["LevelP45",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM50 [Indent level: 6],
                        "levelm50": {
                            "type": "line",
                            "points": [["LevelM50",[-0.2,0.05],1],["LevelM50",[-0.17,0.04],1],[],["LevelM50",[-0.14,0.03],1],["LevelM50",[-0.11,0.02],1],[],["LevelM50",[-0.08,0.01],1],["LevelM50",[-0.05,0],1],["LevelM50",[-0.05,-0.03],1],[],["LevelM50",[0.05,-0.03],1],["LevelM50",[0.05,0],1],["LevelM50",[0.08,0.01],1],[],["LevelM50",[0.11,0.02],1],["LevelM50",[0.14,0.03],1],[],["LevelM50",[0.17,0.04],1],["LevelM50",[0.2,0.05],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_50 [Indent level: 6],
                        "valm_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM50",[-0.18,-0.082],1],
                            "right": ["LevelM50",[-0.1,-0.082],1],
                            "down": ["LevelM50",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP50 [Indent level: 6],
                        "levelp50": {
                            "type": "line",
                            "points": [["LevelP50",[-0.2,0.03],1],["LevelP50",[-0.2,0],1],["LevelP50",[-0.05,0],1],[],["LevelP50",[0.05,0],1],["LevelP50",[0.2,0],1],["LevelP50",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_50 [Indent level: 6],
                        "valp_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP50",[-0.18,0.032],1],
                            "right": ["LevelP50",[-0.1,0.032],1],
                            "down": ["LevelP50",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM55 [Indent level: 6],
                        "levelm55": {
                            "type": "line",
                            "points": [["LevelM55",[-0.2,0.055],1],["LevelM55",[-0.17,0.044],1],[],["LevelM55",[-0.14,0.033],1],["LevelM55",[-0.11,0.022],1],[],["LevelM55",[-0.08,0.011],1],["LevelM55",[-0.05,0],1],["LevelM55",[-0.05,-0.03],1],[],["LevelM55",[0.05,-0.03],1],["LevelM55",[0.05,0],1],["LevelM55",[0.08,0.011],1],[],["LevelM55",[0.11,0.022],1],["LevelM55",[0.14,0.033],1],[],["LevelM55",[0.17,0.044],1],["LevelM55",[0.2,0.055],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_55 [Indent level: 6],
                        "valm_1_55": {
                            "type": "text",
                            "source": "static",
                            "text": -55,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM55",[-0.18,-0.082],1],
                            "right": ["LevelM55",[-0.1,-0.082],1],
                            "down": ["LevelM55",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP55 [Indent level: 6],
                        "levelp55": {
                            "type": "line",
                            "points": [["LevelP55",[-0.2,0.03],1],["LevelP55",[-0.2,0],1],["LevelP55",[-0.05,0],1],[],["LevelP55",[0.05,0],1],["LevelP55",[0.2,0],1],["LevelP55",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_55 [Indent level: 6],
                        "valp_1_55": {
                            "type": "text",
                            "source": "static",
                            "text": "55",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP55",[-0.18,0.032],1],
                            "right": ["LevelP55",[-0.1,0.032],1],
                            "down": ["LevelP55",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM60 [Indent level: 6],
                        "levelm60": {
                            "type": "line",
                            "points": [["LevelM60",[-0.2,0.06],1],["LevelM60",[-0.17,0.048],1],[],["LevelM60",[-0.14,0.036],1],["LevelM60",[-0.11,0.024],1],[],["LevelM60",[-0.08,0.012],1],["LevelM60",[-0.05,0],1],["LevelM60",[-0.05,-0.03],1],[],["LevelM60",[0.05,-0.03],1],["LevelM60",[0.05,0],1],["LevelM60",[0.08,0.012],1],[],["LevelM60",[0.11,0.024],1],["LevelM60",[0.14,0.036],1],[],["LevelM60",[0.17,0.048],1],["LevelM60",[0.2,0.06],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_60 [Indent level: 6],
                        "valm_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM60",[-0.18,-0.082],1],
                            "right": ["LevelM60",[-0.1,-0.082],1],
                            "down": ["LevelM60",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP60 [Indent level: 6],
                        "levelp60": {
                            "type": "line",
                            "points": [["LevelP60",[-0.2,0.03],1],["LevelP60",[-0.2,0],1],["LevelP60",[-0.05,0],1],[],["LevelP60",[0.05,0],1],["LevelP60",[0.2,0],1],["LevelP60",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_60 [Indent level: 6],
                        "valp_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP60",[-0.18,0.032],1],
                            "right": ["LevelP60",[-0.1,0.032],1],
                            "down": ["LevelP60",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM65 [Indent level: 6],
                        "levelm65": {
                            "type": "line",
                            "points": [["LevelM65",[-0.2,0.065],1],["LevelM65",[-0.17,0.052],1],[],["LevelM65",[-0.14,0.039],1],["LevelM65",[-0.11,0.026],1],[],["LevelM65",[-0.08,0.013],1],["LevelM65",[-0.05,0],1],["LevelM65",[-0.05,-0.03],1],[],["LevelM65",[0.05,-0.03],1],["LevelM65",[0.05,0],1],["LevelM65",[0.08,0.013],1],[],["LevelM65",[0.11,0.026],1],["LevelM65",[0.14,0.039],1],[],["LevelM65",[0.17,0.052],1],["LevelM65",[0.2,0.065],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_65 [Indent level: 6],
                        "valm_1_65": {
                            "type": "text",
                            "source": "static",
                            "text": -65,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM65",[-0.18,-0.082],1],
                            "right": ["LevelM65",[-0.1,-0.082],1],
                            "down": ["LevelM65",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP65 [Indent level: 6],
                        "levelp65": {
                            "type": "line",
                            "points": [["LevelP65",[-0.2,0.03],1],["LevelP65",[-0.2,0],1],["LevelP65",[-0.05,0],1],[],["LevelP65",[0.05,0],1],["LevelP65",[0.2,0],1],["LevelP65",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_65 [Indent level: 6],
                        "valp_1_65": {
                            "type": "text",
                            "source": "static",
                            "text": "65",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP65",[-0.18,0.032],1],
                            "right": ["LevelP65",[-0.1,0.032],1],
                            "down": ["LevelP65",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM70 [Indent level: 6],
                        "levelm70": {
                            "type": "line",
                            "points": [["LevelM70",[-0.2,0.07],1],["LevelM70",[-0.17,0.056],1],[],["LevelM70",[-0.14,0.042],1],["LevelM70",[-0.11,0.028],1],[],["LevelM70",[-0.08,0.014],1],["LevelM70",[-0.05,0],1],["LevelM70",[-0.05,-0.03],1],[],["LevelM70",[0.05,-0.03],1],["LevelM70",[0.05,0],1],["LevelM70",[0.08,0.014],1],[],["LevelM70",[0.11,0.028],1],["LevelM70",[0.14,0.042],1],[],["LevelM70",[0.17,0.056],1],["LevelM70",[0.2,0.07],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_70 [Indent level: 6],
                        "valm_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM70",[-0.18,-0.082],1],
                            "right": ["LevelM70",[-0.1,-0.082],1],
                            "down": ["LevelM70",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP70 [Indent level: 6],
                        "levelp70": {
                            "type": "line",
                            "points": [["LevelP70",[-0.2,0.03],1],["LevelP70",[-0.2,0],1],["LevelP70",[-0.05,0],1],[],["LevelP70",[0.05,0],1],["LevelP70",[0.2,0],1],["LevelP70",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_70 [Indent level: 6],
                        "valp_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": "70",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP70",[-0.18,0.032],1],
                            "right": ["LevelP70",[-0.1,0.032],1],
                            "down": ["LevelP70",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM75 [Indent level: 6],
                        "levelm75": {
                            "type": "line",
                            "points": [["LevelM75",[-0.2,0.075],1],["LevelM75",[-0.17,0.06],1],[],["LevelM75",[-0.14,0.045],1],["LevelM75",[-0.11,0.03],1],[],["LevelM75",[-0.08,0.015],1],["LevelM75",[-0.05,0],1],["LevelM75",[-0.05,-0.03],1],[],["LevelM75",[0.05,-0.03],1],["LevelM75",[0.05,0],1],["LevelM75",[0.08,0.015],1],[],["LevelM75",[0.11,0.03],1],["LevelM75",[0.14,0.045],1],[],["LevelM75",[0.17,0.06],1],["LevelM75",[0.2,0.075],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_75 [Indent level: 6],
                        "valm_1_75": {
                            "type": "text",
                            "source": "static",
                            "text": -75,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM75",[-0.18,-0.082],1],
                            "right": ["LevelM75",[-0.1,-0.082],1],
                            "down": ["LevelM75",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP75 [Indent level: 6],
                        "levelp75": {
                            "type": "line",
                            "points": [["LevelP75",[-0.2,0.03],1],["LevelP75",[-0.2,0],1],["LevelP75",[-0.05,0],1],[],["LevelP75",[0.05,0],1],["LevelP75",[0.2,0],1],["LevelP75",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_75 [Indent level: 6],
                        "valp_1_75": {
                            "type": "text",
                            "source": "static",
                            "text": "75",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP75",[-0.18,0.032],1],
                            "right": ["LevelP75",[-0.1,0.032],1],
                            "down": ["LevelP75",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM80 [Indent level: 6],
                        "levelm80": {
                            "type": "line",
                            "points": [["LevelM80",[-0.2,0.08],1],["LevelM80",[-0.17,0.064],1],[],["LevelM80",[-0.14,0.048],1],["LevelM80",[-0.11,0.032],1],[],["LevelM80",[-0.08,0.016],1],["LevelM80",[-0.05,0],1],["LevelM80",[-0.05,-0.03],1],[],["LevelM80",[0.05,-0.03],1],["LevelM80",[0.05,0],1],["LevelM80",[0.08,0.016],1],[],["LevelM80",[0.11,0.032],1],["LevelM80",[0.14,0.048],1],[],["LevelM80",[0.17,0.064],1],["LevelM80",[0.2,0.08],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_80 [Indent level: 6],
                        "valm_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM80",[-0.18,-0.082],1],
                            "right": ["LevelM80",[-0.1,-0.082],1],
                            "down": ["LevelM80",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP80 [Indent level: 6],
                        "levelp80": {
                            "type": "line",
                            "points": [["LevelP80",[-0.2,0.03],1],["LevelP80",[-0.2,0],1],["LevelP80",[-0.05,0],1],[],["LevelP80",[0.05,0],1],["LevelP80",[0.2,0],1],["LevelP80",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_80 [Indent level: 6],
                        "valp_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": "80",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP80",[-0.18,0.032],1],
                            "right": ["LevelP80",[-0.1,0.032],1],
                            "down": ["LevelP80",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM85 [Indent level: 6],
                        "levelm85": {
                            "type": "line",
                            "points": [["LevelM85",[-0.2,0.085],1],["LevelM85",[-0.17,0.068],1],[],["LevelM85",[-0.14,0.051],1],["LevelM85",[-0.11,0.034],1],[],["LevelM85",[-0.08,0.017],1],["LevelM85",[-0.05,0],1],["LevelM85",[-0.05,-0.03],1],[],["LevelM85",[0.05,-0.03],1],["LevelM85",[0.05,0],1],["LevelM85",[0.08,0.017],1],[],["LevelM85",[0.11,0.034],1],["LevelM85",[0.14,0.051],1],[],["LevelM85",[0.17,0.068],1],["LevelM85",[0.2,0.085],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_85 [Indent level: 6],
                        "valm_1_85": {
                            "type": "text",
                            "source": "static",
                            "text": -85,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM85",[-0.18,-0.082],1],
                            "right": ["LevelM85",[-0.1,-0.082],1],
                            "down": ["LevelM85",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP85 [Indent level: 6],
                        "levelp85": {
                            "type": "line",
                            "points": [["LevelP85",[-0.2,0.03],1],["LevelP85",[-0.2,0],1],["LevelP85",[-0.05,0],1],[],["LevelP85",[0.05,0],1],["LevelP85",[0.2,0],1],["LevelP85",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_85 [Indent level: 6],
                        "valp_1_85": {
                            "type": "text",
                            "source": "static",
                            "text": "85",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP85",[-0.18,0.032],1],
                            "right": ["LevelP85",[-0.1,0.032],1],
                            "down": ["LevelP85",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelM90 [Indent level: 6],
                        "levelm90": {
                            "type": "line",
                            "points": [["LevelM90",[-0.2,0.09],1],["LevelM90",[-0.17,0.072],1],[],["LevelM90",[-0.14,0.054],1],["LevelM90",[-0.11,0.036],1],[],["LevelM90",[-0.08,0.018],1],["LevelM90",[-0.05,0],1],["LevelM90",[-0.05,-0.03],1],[],["LevelM90",[0.05,-0.03],1],["LevelM90",[0.05,0],1],["LevelM90",[0.08,0.018],1],[],["LevelM90",[0.11,0.036],1],["LevelM90",[0.14,0.054],1],[],["LevelM90",[0.17,0.072],1],["LevelM90",[0.2,0.09],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALM_1_90 [Indent level: 6],
                        "valm_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": -90,
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelM90",[-0.18,-0.082],1],
                            "right": ["LevelM90",[-0.1,-0.082],1],
                            "down": ["LevelM90",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|LevelP90 [Indent level: 6],
                        "levelp90": {
                            "type": "line",
                            "points": [["LevelP90",[-0.2,0.03],1],["LevelP90",[-0.2,0],1],["LevelP90",[-0.05,0],1],[],["LevelP90",[0.05,0],1],["LevelP90",[0.2,0],1],["LevelP90",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Horizont|Dimmed|VALP_1_90 [Indent level: 6],
                        "valp_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": "90",
                            "align": "right",
                            "scale": 1,
                            "sourcescale": 1,
                            "pos": ["LevelP90",[-0.18,0.032],1],
                            "right": ["LevelP90",[-0.1,0.032],1],
                            "down": ["LevelP90",[-0.18,0.082],1]
                        }
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|SpeedNumber [Indent level: 4],
                "speednumber": {
                    "type": "text",
                    "source": "speed",
                    "sourcescale": 3.6,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.1,0.309737],1],
                    "right": [[0.16,0.309737],1],
                    "down": [[0.1,0.366053],1]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|AltNumber [Indent level: 4],
                "altnumber": {
                    "source": "altitudeASL",
                    "sourcescale": 1,
                    "pos": [[0.9,0.309737],1],
                    "right": [[0.96,0.309737],1],
                    "down": [[0.9,0.366053],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|AltNumberAGL [Indent level: 4],
                "altnumberagl": {
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|AltNumberAGL|Text [Indent level: 5]
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "H",
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.8,0.535],1],
                        "right": [[0.86,0.535],1],
                        "down": [[0.8,0.591316],1]
                    },
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|AltNumberAGL|Box [Indent level: 5],
                    "box": {
                        "type": "line",
                        "points": [[[0.81,0.591316],1],[[1,0.591316],1],[[1,0.535],1],[[0.81,0.535],1],[[0.81,0.591316],1]]
                    },
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|AltNumberAGL|AltNumber [Indent level: 5],
                    "altnumber": {
                        "type": "text",
                        "source": "altitudeAGL",
                        "sourcescale": 1,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.99,0.535],1],
                        "right": [[1.05,0.535],1],
                        "down": [[0.99,0.591316],1]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Gear [Indent level: 4],
                "gear": {
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Gear|Highlighted [Indent level: 5]
                    "highlighted": {
                        "condition": "ils",
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Gear|Highlighted|Text [Indent level: 6],
                        "text": {
                            "type": "text",
                            "source": "static",
                            "text": "GEAR",
                            "align": "left",
                            "scale": 1,
                            "pos": [[0.99,0.816579],1],
                            "right": [[1.05,0.816579],1],
                            "down": [[0.99,0.872895],1]
                        }
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Flaps [Indent level: 4],
                "flaps": {
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Flaps|Highlighted [Indent level: 5]
                    "highlighted": {
                        "condition": "flaps",
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Flaps|Highlighted|Text [Indent level: 6],
                        "text": {
                            "type": "text",
                            "source": "static",
                            "text": "FLAPS",
                            "align": "left",
                            "scale": 1,
                            "pos": [[0.99,0.872895],1],
                            "right": [[1.05,0.872895],1],
                            "down": [[0.99,0.92921],1]
                        }
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Lights [Indent level: 4],
                "lights": {
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Lights|Highlighted [Indent level: 5]
                    "highlighted": {
                        "condition": "lights",
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Lights|Highlighted|Text [Indent level: 6],
                        "text": {
                            "type": "text",
                            "source": "static",
                            "text": "LIGHTS",
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.01,0.816579],1],
                            "right": [[0.07,0.816579],1],
                            "down": [[0.01,0.872895],1]
                        }
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|CollisionLights [Indent level: 4],
                "collisionlights": {
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|CollisionLights|Highlighted [Indent level: 5]
                    "highlighted": {
                        "condition": "collisionlights",
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|CollisionLights|Highlighted|Text [Indent level: 6],
                        "text": {
                            "type": "text",
                            "source": "static",
                            "text": "ANTI-COL",
                            "align": "right",
                            "scale": 1,
                            "pos": [[0.01,0.872895],1],
                            "right": [[0.07,0.872895],1],
                            "down": [[0.01,0.92921],1]
                        }
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|RadarTargets [Indent level: 4],
                "radartargets": {
                    "condition": "1-ils",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|RadarTargets|RadarBoxes [Indent level: 5],
                    "radarboxes": {
                        "type": "radar",
                        "pos0": [0.4975,0.383],
                        "pos10": [1.4475,1.453],
                        "width": 4,
                        "points": [[[-0.02,-0.0225263],1],[[0.02,-0.0225263],1],[[0.02,0.0225263],1],[[-0.02,0.0225263],1],[[-0.02,-0.0225263],1]]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|TargetDiamond [Indent level: 4],
                "targetdiamond": {
                    "condition": "1-ils",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|TargetDiamond|shape [Indent level: 5],
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0,-0.0337895],1],["Target",1,"Limit0109",1,[0.03,0],1],["Target",1,"Limit0109",1,[0,0.0337895],1],["Target",1,"Limit0109",1,[-0.03,0],1],["Target",1,"Limit0109",1,[0,-0.0337895],1]]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|TargetingPodGroup [Indent level: 4],
                "targetingpodgroup": {
                    "condition": "1-pilotcameralock",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|TargetingPodGroup|TargetingPodDir [Indent level: 5],
                    "targetingpoddir": {
                        "type": "line",
                        "width": 3,
                        "points": [["TargetingPodDir",1,[0,-0.0450526],1],["TargetingPodDir",1,[0,-0.0394211],1],[],["TargetingPodDir",1,[0,-0.0337895],1],["TargetingPodDir",1,[0,-0.0281579],1],[],["TargetingPodDir",1,[0,-0.0225263],1],["TargetingPodDir",1,[0,-0.0168947],1],[],["TargetingPodDir",1,[0,-0.0112632],1],["TargetingPodDir",1,[0,-0.00563158],1],[],["TargetingPodDir",1,[0,0.0450526],1],["TargetingPodDir",1,[0,0.0394211],1],[],["TargetingPodDir",1,[0,0.0337895],1],["TargetingPodDir",1,[0,0.0281579],1],[],["TargetingPodDir",1,[0,0.0225263],1],["TargetingPodDir",1,[0,0.0168947],1],[],["TargetingPodDir",1,[0,0.0112632],1],["TargetingPodDir",1,[0,0.00563158],1],[],["TargetingPodDir",1,[-0.04,0],1],["TargetingPodDir",1,[-0.035,0],1],[],["TargetingPodDir",1,[-0.03,0],1],["TargetingPodDir",1,[-0.025,0],1],[],["TargetingPodDir",1,[-0.02,0],1],["TargetingPodDir",1,[-0.015,0],1],[],["TargetingPodDir",1,[-0.01,0],1],["TargetingPodDir",1,[-0.005,0],1],[],["TargetingPodDir",1,[0.04,0],1],["TargetingPodDir",1,[0.035,0],1],[],["TargetingPodDir",1,[0.03,0],1],["TargetingPodDir",1,[0.025,0],1],[],["TargetingPodDir",1,[0.02,0],1],["TargetingPodDir",1,[0.015,0],1],[],["TargetingPodDir",1,[0.01,0],1],["TargetingPodDir",1,[0.005,0],1],[]]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|TargetingPodGroupOn [Indent level: 4],
                "targetingpodgroupon": {
                    "condition": "pilotcameralock",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|TargetingPodGroupOn|TargetingPodDir [Indent level: 5],
                    "targetingpoddir": {
                        "type": "line",
                        "width": 3,
                        "points": [["TargetingPodTarget",1,"Limit0109",1,[0,-0.0450526],1],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0394211],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0337895],1],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0281579],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0225263],1],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0168947],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0112632],1],["TargetingPodTarget",1,"Limit0109",1,[0,-0.00563158],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,0.0450526],1],["TargetingPodTarget",1,"Limit0109",1,[0,0.0394211],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,0.0337895],1],["TargetingPodTarget",1,"Limit0109",1,[0,0.0281579],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,0.0225263],1],["TargetingPodTarget",1,"Limit0109",1,[0,0.0168947],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,0.0112632],1],["TargetingPodTarget",1,"Limit0109",1,[0,0.00563158],1],[],["TargetingPodTarget",1,"Limit0109",1,[-0.04,0],1],["TargetingPodTarget",1,"Limit0109",1,[-0.035,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[-0.03,0],1],["TargetingPodTarget",1,"Limit0109",1,[-0.025,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[-0.02,0],1],["TargetingPodTarget",1,"Limit0109",1,[-0.015,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[-0.01,0],1],["TargetingPodTarget",1,"Limit0109",1,[-0.005,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[0.04,0],1],["TargetingPodTarget",1,"Limit0109",1,[0.035,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[0.03,0],1],["TargetingPodTarget",1,"Limit0109",1,[0.025,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[0.02,0],1],["TargetingPodTarget",1,"Limit0109",1,[0.015,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[0.01,0],1],["TargetingPodTarget",1,"Limit0109",1,[0.005,0],1],[]]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Stall [Indent level: 4],
                "stall": {
                    "condition": "stall",
                    "color": [1,0,0],
                    "blinkingpattern": [0.2,0.2],
                    "blinkingstartson": 1,
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Stall|Text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "STALL",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.5,0.202737],1],
                        "right": [[0.56,0.202737],1],
                        "down": [[0.5,0.259053],1]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|IncomingMissile [Indent level: 4],
                "incomingmissile": {
                    "condition": "incomingmissile",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|IncomingMissile|Text [Indent level: 5],
                    "text": {
                        "text": "!INCOMING!",
                        "pos": [[0.485,0.473053],1],
                        "right": [[0.545,0.473053],1],
                        "down": [[0.485,0.529368],1],
                        "type": "text",
                        "source": "static",
                        "align": "center",
                        "scale": 1
                    },
                    "color": [1,0,0],
                    "blinkingpattern": [0.2,0.2],
                    "blinkingstartson": 1
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Ammo [Indent level: 4],
                "ammo": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.5,0.816579],1],
                    "right": [[0.56,0.816579],1],
                    "down": [[0.5,0.872895],1]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Weapons [Indent level: 4],
                "weapons": {
                    "type": "text",
                    "source": "weapon",
                    "sourcescale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.5,0.872895],1],
                    "right": [[0.56,0.872895],1],
                    "down": [[0.5,0.92921],1]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|WeaponsLocking [Indent level: 4],
                "weaponslocking": {
                    "condition": "missilelocking",
                    "blinkingpattern": [0.2,0.2],
                    "blinkingstartson": 1,
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|WeaponsLocking|Text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": ">LOCKING<",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.485,0.625105],1],
                        "right": [[0.545,0.625105],1],
                        "down": [[0.485,0.681421],1]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|WeaponsLocked [Indent level: 4],
                "weaponslocked": {
                    "condition": "missilelocked",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|WeaponsLocked|Text [Indent level: 5],
                    "text": {
                        "type": "text",
                        "source": "static",
                        "text": "<LOCKED>",
                        "align": "center",
                        "scale": 1,
                        "pos": [[0.485,0.625105],1],
                        "right": [[0.545,0.625105],1],
                        "down": [[0.485,0.681421],1]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|WP [Indent level: 4],
                "wp": {
                    "condition": "wpvalid",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|WP|WPdist [Indent level: 5],
                    "wpdist": {
                        "type": "text",
                        "source": "wpdist",
                        "sourcescale": 0.01,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.945,0.703947],1],
                        "right": [[1.005,0.703947],1],
                        "down": [[0.945,0.760263],1]
                    },
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|WP|WPstatic [Indent level: 5],
                    "wpstatic": {
                        "type": "text",
                        "source": "static",
                        "text": ">",
                        "align": "center",
                        "scale": 2,
                        "pos": [[0.96,0.703947],1],
                        "right": [[0.98,0.703947],1],
                        "down": [[0.96,0.760263],1]
                    },
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|WP|WPIndex [Indent level: 5],
                    "wpindex": {
                        "type": "text",
                        "source": "wpIndex",
                        "sourcescale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.97,0.703947],1],
                        "right": [[1.03,0.703947],1],
                        "down": [[0.97,0.760263],1]
                    },
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|WP|WP [Indent level: 5],
                    "wp": {
                        "type": "line",
                        "points": [["wppoint",1,"Limit0109",1,["HorizonBankRotFull",0.015,-0.035],1],["wppoint",1,"Limit0109",1,["HorizonBankRotFull",0,0],1],["wppoint",1,"Limit0109",1,["HorizonBankRotFull",-0.015,-0.035],1]]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|HeadingScale [Indent level: 4],
                "headingscale": {
                    "type": "scale",
                    "horizontal": 1,
                    "source": "Heading",
                    "sourcescale": 0.1,
                    "top": 0.2,
                    "center": 0.5,
                    "bottom": 0.8,
                    "linexleft": 0.101368,
                    "lineyright": 0.0901053,
                    "linexleftmajor": 0.101368,
                    "lineyrightmajor": 0.0788421,
                    "majorlineeach": 5,
                    "numbereach": 5,
                    "step": 0.2,
                    "stepsize": 0.03,
                    "align": "center",
                    "scale": 1,
                    "pos": [0.2,0.0197105],
                    "right": [0.26,0.0197105],
                    "down": [0.2,0.0760263]
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|ILS [Indent level: 4],
                "ils": {
                    "condition": "ils",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|ILS|Glideslope [Indent level: 5],
                    "glideslope": {
                        "cliptl": [0,0],
                        "clipbr": [1,1],
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|ILS|Glideslope|ILS [Indent level: 6],
                        "ils": {
                            "type": "line",
                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[-0.24,-0.0270316],1],["ILS_W",[-0.24,0.0270316],1],[],["ILS_W",[-0.12,-0.0202737],1],["ILS_W",[-0.12,0.0202737],1],[],["ILS_W",[0,-0.0270316],1],["ILS_W",[0,0.0270316],1],[],["ILS_W",[0.12,-0.0202737],1],["ILS_W",[0.12,0.0202737],1],[],["ILS_W",[0.24,-0.0270316],1],["ILS_W",[0.24,0.0270316],1],[],["ILS_H",[0,-0.270316],1],["ILS_H",[0,0.270316],1],[],["ILS_H",[-0.024,-0.270316],1],["ILS_H",[0.024,-0.270316],1],[],["ILS_H",[-0.018,-0.135158],1],["ILS_H",[0.018,-0.135158],1],[],["ILS_H",[-0.024,0],1],["ILS_H",[0.024,0],1],[],["ILS_H",[-0.018,0.135158],1],["ILS_H",[0.018,0.135158],1],[],["ILS_H",[-0.024,0.270316],1],["ILS_H",[0.024,0.270316],1]]
                        },
                        # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|ILS|Glideslope|airport [Indent level: 6],
                        "airport": {
                            "type": "line",
                            "points": [["airport1",1],["airport2",1],["airport4",1],["airport3",1],["airport1",1]]
                        }
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Bomb [Indent level: 4],
                "bomb": {
                    "condition": "bomb",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|Bomb|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["ImpactPoint",[0,-0.112632],1],["ImpactPoint",[0.01736,-0.11092],1],["ImpactPoint",[0.0342,-0.10584],1],["ImpactPoint",[0.05,-0.0975389],1],["ImpactPoint",[0.06428,-0.0862758],1],["ImpactPoint",[0.0766,-0.0723996],1],["ImpactPoint",[0.0866,-0.0563158],1],["ImpactPoint",[0.09397,-0.03852],1],["ImpactPoint",[0.09848,-0.0195528],1],["ImpactPoint",[0.1,0],1],["ImpactPoint",[0.09848,0.0195528],1],["ImpactPoint",[0.09397,0.03852],1],["ImpactPoint",[0.0866,0.0563158],1],["ImpactPoint",[0.0766,0.0723996],1],["ImpactPoint",[0.06428,0.0862758],1],["ImpactPoint",[0.05,0.0975389],1],["ImpactPoint",[0.0342,0.10584],1],["ImpactPoint",[0.01736,0.11092],1],["ImpactPoint",[0,0.112632],1],["ImpactPoint",[-0.01736,0.11092],1],["ImpactPoint",[-0.0342,0.10584],1],["ImpactPoint",[-0.05,0.0975389],1],["ImpactPoint",[-0.06428,0.0862758],1],["ImpactPoint",[-0.0766,0.0723996],1],["ImpactPoint",[-0.0866,0.0563158],1],["ImpactPoint",[-0.09397,0.03852],1],["ImpactPoint",[-0.09848,0.0195528],1],["ImpactPoint",[-0.1,0],1],["ImpactPoint",[-0.09848,-0.0195528],1],["ImpactPoint",[-0.09397,-0.03852],1],["ImpactPoint",[-0.0866,-0.0563158],1],["ImpactPoint",[-0.0766,-0.0723996],1],["ImpactPoint",[-0.06428,-0.0862758],1],["ImpactPoint",[-0.05,-0.0975389],1],["ImpactPoint",[-0.0342,-0.10584],1],["ImpactPoint",[-0.01736,-0.11092],1],["ImpactPoint",[0,-0.112632],1],[],["ImpactPoint",1,"Limit0109",1,[0,-0.0225263],1],["ImpactPoint",1,"Limit0109",1,[0.014,-0.0157684],1],["ImpactPoint",1,"Limit0109",1,["+ 0.02",0],1],["ImpactPoint",1,"Limit0109",1,[0.014,0.0157684],1],["ImpactPoint",1,"Limit0109",1,[0,0.0225263],1],["ImpactPoint",1,"Limit0109",1,[-0.014,0.0157684],1],["ImpactPoint",1,"Limit0109",1,["- 0.02",0],1],["ImpactPoint",1,"Limit0109",1,[-0.014,-0.0157684],1],["ImpactPoint",1,"Limit0109",1,[0,-0.0225263],1],[],["Velocity",0.001,"ImpactPoint",1,"Limit0109",1,[0,0],1],["Velocity",1,"Limit0109",1,[0,0],1]]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|MGun [Indent level: 4],
                "mgun": {
                    "condition": "mgun",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|MGun|Ball [Indent level: 5],
                    "ball": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.00156283,-0.00998284],1],["ImpactPoint",[0.00307818,-0.00952552],1],["ImpactPoint",[0.0045,-0.00877876],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.0045,-0.00877876],1],["ImpactPoint",[0.00578509,-0.00776527],1],["ImpactPoint",[0.0068944,-0.00651584],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.0068944,-0.00651584],1],["ImpactPoint",[0.00779423,-0.00506842],1],["ImpactPoint",[0.00845723,-0.003467],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.00845723,-0.003467],1],["ImpactPoint",[0.00886327,-0.00176024],1],["ImpactPoint",[0.009,4.43095e-010],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.009,4.43095e-010],1],["ImpactPoint",[0.00886327,0.00176024],1],["ImpactPoint",[0.00845723,0.003467],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.00845723,0.003467],1],["ImpactPoint",[0.00779423,0.00506842],1],["ImpactPoint",[0.0068944,0.00651584],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.0068944,0.00651584],1],["ImpactPoint",[0.00578509,0.00776527],1],["ImpactPoint",[0.0045,0.00877876],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.0045,0.00877876],1],["ImpactPoint",[0.00307818,0.00952552],1],["ImpactPoint",[0.00156283,0.00998284],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.00156283,0.00998284],1],["ImpactPoint",[-7.86805e-010,0.0101368],1],["ImpactPoint",[-0.00156284,0.00998284],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.00156284,0.00998284],1],["ImpactPoint",[-0.00307818,0.00952552],1],["ImpactPoint",[-0.0045,0.00877876],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.0045,0.00877876],1],["ImpactPoint",[-0.00578509,0.00776527],1],["ImpactPoint",[-0.0068944,0.00651583],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.0068944,0.00651583],1],["ImpactPoint",[-0.00779423,0.00506842],1],["ImpactPoint",[-0.00845723,0.003467],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.00845723,0.003467],1],["ImpactPoint",[-0.00886327,0.00176024],1],["ImpactPoint",[-0.009,-1.20881e-010],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.009,-1.20881e-010],1],["ImpactPoint",[-0.00886327,-0.00176025],1],["ImpactPoint",[-0.00845723,-0.003467],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.00845723,-0.003467],1],["ImpactPoint",[-0.00779423,-0.00506842],1],["ImpactPoint",[-0.0068944,-0.00651583],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.0068944,-0.00651583],1],["ImpactPoint",[-0.00578509,-0.00776527],1],["ImpactPoint",[-0.0045,-0.00877876],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.0045,-0.00877876],1],["ImpactPoint",[-0.00307818,-0.00952551],1],["ImpactPoint",[-0.00156283,-0.00998284],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.00156283,-0.00998284],1],["ImpactPoint",[1.57361e-009,-0.0101368],1],["ImpactPoint",[0.00156283,-0.00998284],1]],[["ImpactPoint",[0,0.0394211],1],["ImpactPoint",[-0.00435779,0.0561015],1],["ImpactPoint",[0,0.0732105],1],["ImpactPoint",[0.00435779,0.0561015],1]],[["ImpactPoint",[0.0247487,0.0278749],1],["ImpactPoint",[0.0321394,0.0431404],1],["ImpactPoint",[0.0459619,0.0517677],1],["ImpactPoint",[0.0383022,0.0361991],1]],[["ImpactPoint",[0.035,-1.72315e-009],1],["ImpactPoint",[0.0498097,0.00490825],1],["ImpactPoint",[0.065,-3.20013e-009],1],["ImpactPoint",[0.0498097,-0.00490825],1]],[["ImpactPoint",[0.0247487,-0.0278749],1],["ImpactPoint",[0.0383022,-0.0361991],1],["ImpactPoint",[0.0459619,-0.0517677],1],["ImpactPoint",[0.0321394,-0.0431404],1]],[["ImpactPoint",[-3.0598e-009,-0.0394211],1],["ImpactPoint",[0.00435778,-0.0561015],1],["ImpactPoint",[-5.68248e-009,-0.0732105],1],["ImpactPoint",[-0.00435779,-0.0561015],1]],[["ImpactPoint",[-0.0247487,-0.0278749],1],["ImpactPoint",[-0.0321394,-0.0431404],1],["ImpactPoint",[-0.0459619,-0.0517677],1],["ImpactPoint",[-0.0383022,-0.0361991],1]],[["ImpactPoint",[-0.035,4.70091e-010],1],["ImpactPoint",[-0.0498097,-0.00490824],1],["ImpactPoint",[-0.065,8.73027e-010],1],["ImpactPoint",[-0.0498097,0.00490824],1]],[["ImpactPoint",[-0.0247487,0.0278749],1],["ImpactPoint",[-0.0383022,0.0361991],1],["ImpactPoint",[-0.0459619,0.0517676],1],["ImpactPoint",[-0.0321394,0.0431404],1]]]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|AAMissile [Indent level: 4],
                "aamissile": {
                    "condition": "AAmissile",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|AAMissile|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["center",[0,-0.225263],1],["center",[0.03472,-0.221839],1],["center",[0.0684,-0.21168],1],["center",[0.1,-0.195078],1],["center",[0.12856,-0.172552],1],["center",[0.1532,-0.144799],1],["center",[0.1732,-0.112632],1],["center",[0.18794,-0.07704],1],["center",[0.19696,-0.0391057],1],["center",[0.2,0],1],["center",[0.19696,0.0391057],1],["center",[0.18794,0.07704],1],["center",[0.1732,0.112632],1],["center",[0.1532,0.144799],1],["center",[0.12856,0.172552],1],["center",[0.1,0.195078],1],["center",[0.0684,0.21168],1],["center",[0.03472,0.221839],1],["center",[0,0.225263],1],["center",[-0.03472,0.221839],1],["center",[-0.0684,0.21168],1],["center",[-0.1,0.195078],1],["center",[-0.12856,0.172552],1],["center",[-0.1532,0.144799],1],["center",[-0.1732,0.112632],1],["center",[-0.18794,0.07704],1],["center",[-0.19696,0.0391057],1],["center",[-0.2,0],1],["center",[-0.19696,-0.0391057],1],["center",[-0.18794,-0.07704],1],["center",[-0.1732,-0.112632],1],["center",[-0.1532,-0.144799],1],["center",[-0.12856,-0.172552],1],["center",[-0.1,-0.195078],1],["center",[-0.0684,-0.21168],1],["center",[-0.03472,-0.221839],1],["center",[0,-0.225263],1]]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|ATMissile [Indent level: 4],
                "atmissile": {
                    "condition": "ATmissile",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|ATMissile|Circle [Indent level: 5],
                    "circle": {
                        "type": "line",
                        "points": [["center",[0,-0.180211],1],["center",[0.027776,-0.177471],1],["center",[0.05472,-0.169344],1],["center",[0.08,-0.156062],1],["center",[0.102848,-0.138041],1],["center",[0.12256,-0.115839],1],["center",[0.13856,-0.0901053],1],["center",[0.150352,-0.061632],1],["center",[0.157568,-0.0312845],1],["center",[0.16,0],1],["center",[0.157568,0.0312845],1],["center",[0.150352,0.061632],1],["center",[0.13856,0.0901053],1],["center",[0.12256,0.115839],1],["center",[0.102848,0.138041],1],["center",[0.08,0.156062],1],["center",[0.05472,0.169344],1],["center",[0.027776,0.177471],1],["center",[0,0.180211],1],["center",[-0.027776,0.177471],1],["center",[-0.05472,0.169344],1],["center",[-0.08,0.156062],1],["center",[-0.102848,0.138041],1],["center",[-0.12256,0.115839],1],["center",[-0.13856,0.0901053],1],["center",[-0.150352,0.061632],1],["center",[-0.157568,0.0312845],1],["center",[-0.16,0],1],["center",[-0.157568,-0.0312845],1],["center",[-0.150352,-0.061632],1],["center",[-0.13856,-0.0901053],1],["center",[-0.12256,-0.115839],1],["center",[-0.102848,-0.138041],1],["center",[-0.08,-0.156062],1],["center",[-0.05472,-0.169344],1],["center",[-0.027776,-0.177471],1],["center",[0,-0.180211],1]]
                    },
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|ATMissile|Time [Indent level: 5],
                    "time": {
                        "type": "line",
                        "width": 4,
                        "points": [["center",[0,-0.135158],1],["center",[0,-0.168947],1],["MissileFlightTimeRot1",[0,0.15],1,"center",1],["MissileFlightTimeRot2",[0,0.15],1,"center",1],["MissileFlightTimeRot3",[0,0.15],1,"center",1],["MissileFlightTimeRot4",[0,0.15],1,"center",1],["MissileFlightTimeRot5",[0,0.15],1,"center",1],["MissileFlightTimeRot6",[0,0.15],1,"center",1],["MissileFlightTimeRot7",[0,0.15],1,"center",1],["MissileFlightTimeRot8",[0,0.15],1,"center",1],["MissileFlightTimeRot9",[0,0.15],1,"center",1],["MissileFlightTimeRot10",[0,0.15],1,"center",1],["MissileFlightTimeRot11",[0,0.15],1,"center",1],["MissileFlightTimeRot12",[0,0.15],1,"center",1],["MissileFlightTimeRot13",[0,0.15],1,"center",1],["MissileFlightTimeRot14",[0,0.15],1,"center",1],["MissileFlightTimeRot15",[0,0.15],1,"center",1],["MissileFlightTimeRot16",[0,0.15],1,"center",1],["MissileFlightTimeRot17",[0,0.15],1,"center",1],["MissileFlightTimeRot17",[0,0.12],1,"center",1]]
                    }
                },
                # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|RocketCrosshair [Indent level: 4],
                "rocketcrosshair": {
                    "type": "group",
                    "condition": "Rocket",
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|RocketCrosshair|BombCrosshair [Indent level: 5],
                    "bombcrosshair": {
                        "type": "line",
                        "width": 4,
                        "points": [["Velocity",0.001,"ImpactPoint",1,"Limit0109",1,[0,0],1],["Velocity",1,"Limit0109",1,[0,0],1],[],["ImpactPoint",[0,-0.118263],1],["ImpactPoint",[0.018228,-0.116466],1],["ImpactPoint",[0.03591,-0.111132],1],["ImpactPoint",[0.0525,-0.102416],1],["ImpactPoint",[0.067494,-0.0905896],1],["ImpactPoint",[0.08043,-0.0760195],1],["ImpactPoint",[0.09093,-0.0591316],1],["ImpactPoint",[0.0986685,-0.040446],1],["ImpactPoint",[0.103404,-0.0205305],1],["ImpactPoint",[0.105,0],1],["ImpactPoint",[0.103404,0.0205305],1],["ImpactPoint",[0.0986685,0.040446],1],["ImpactPoint",[0.09093,0.0591316],1],["ImpactPoint",[0.08043,0.0760195],1],["ImpactPoint",[0.067494,0.0905896],1],["ImpactPoint",[0.0525,0.102416],1],["ImpactPoint",[0.03591,0.111132],1],["ImpactPoint",[0.018228,0.116466],1],["ImpactPoint",[0,0.118263],1],["ImpactPoint",[-0.018228,0.116466],1],["ImpactPoint",[-0.03591,0.111132],1],["ImpactPoint",[-0.0525,0.102416],1],["ImpactPoint",[-0.067494,0.0905896],1],["ImpactPoint",[-0.08043,0.0760195],1],["ImpactPoint",[-0.09093,0.0591316],1],["ImpactPoint",[-0.0986685,0.040446],1],["ImpactPoint",[-0.103404,0.0205305],1],["ImpactPoint",[-0.105,0],1],["ImpactPoint",[-0.103404,-0.0205305],1],["ImpactPoint",[-0.0986685,-0.040446],1],["ImpactPoint",[-0.09093,-0.0591316],1],["ImpactPoint",[-0.08043,-0.0760195],1],["ImpactPoint",[-0.067494,-0.0905896],1],["ImpactPoint",[-0.0525,-0.102416],1],["ImpactPoint",[-0.03591,-0.111132],1],["ImpactPoint",[-0.018228,-0.116466],1],["ImpactPoint",[0,-0.118263],1]]
                    },
                    # Class: CfgVehicles|Plane_Fighter_03_base_F|MFD|AirplaneHUD|Draw|RocketCrosshair|Time [Indent level: 5],
                    "time": {
                        "type": "line",
                        "width": 6,
                        "points": [["ImpactPoint",[0,-0.0901053],1],["ImpactPoint",[0,-0.112632],1],["MissileFlightTimeRot1",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.08],1,"ImpactPoint",1]]
                    }
                }
            }
        }
    },
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "waterlineardampingcoefy": 0,
    "waterlineardampingcoefx": 5,
    "waterresistancecoef": 0.04,
    "ejectspeed": [0,60,0],
    "transportmaxweapons": 6,
    "transportmaxmagazines": 24,
    "transportmaxbackpacks": 6,
    "maximumload": 500,
    "supplyradius": 2,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Plane_Base_F|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
    },
    # Class: CfgVehicles|Plane_Base_F|TransportMagazines [Indent level: 1],
    "transportmagazines": {
    },
    # Class: CfgVehicles|Plane_Base_F|TransportWeapons [Indent level: 1],
    "transportweapons": {
    },
    # Class: CfgVehicles|Plane_Base_F|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minspeed": 1
    },
    "mingforce": 0.3,
    "maxgforce": 3,
    "gforceshakeattenuation": 0.5,
    # Class: CfgVehicles|Plane_Base_F|NewTurret [Indent level: 1],
    "newturret": {
        "body": "mainTurret",
        "gun": "mainGun",
        "animationsourcebody": "mainTurret",
        "animationsourcegun": "mainGun",
        "animationsourcehatch": "hatchGunner",
        "animationsourcecamelev": "camElev",
        "proxytype": "CPGunner",
        "proxyindex": 1,
        "gunnername": "Gunner",
        "gunnertype": "",
        "primarygunner": 1,
        "primaryobserver": 0,
        "weapons": [],
        "magazines": [],
        "soundservo": ["",0.00316228,1],
        "soundelevation": ["",0.00316228,1],
        "minelev": -4,
        "maxelev": 20,
        "initelev": 0,
        "minturn": -360,
        "maxturn": 360,
        "initturn": 0,
        "minoutelev": -4,
        "maxoutelev": 20,
        "initoutelev": 0,
        "minoutturn": -60,
        "maxoutturn": 60,
        "initoutturn": 0,
        "maxhorizontalrotspeed": 1.2,
        "maxverticalrotspeed": 1.2,
        "mincamelev": -90,
        "maxcamelev": 90,
        "initcamelev": 0,
        "stabilizedinaxes": 3,
        "primary": 1,
        "hasgunner": 1,
        "commanding": 1,
        "gunnergetinaction": "",
        "gunnergetoutaction": "",
        "turretcansee": 0,
        "canusescanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewGunner [Indent level: 2],
        "viewgunner": {
            "initanglex": 5,
            "minanglex": -75,
            "maxanglex": 85,
            "initangley": 0,
            "minangley": -150,
            "maxangley": 150,
            "minfov": 0.25,
            "maxfov": 1.25,
            "initfov": 0.75,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "continuous": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "turretspec": {
            "showheadphones": 0
        },
        "gunneropticsmodel": "",
        "gunneropticscolor": [0,0,0,1],
        "gunnerforceoptics": 1,
        "gunneropticsshowcursor": 0,
        "turretinfotype": "",
        "gunneroutopticsmodel": "",
        "gunneroutopticscolor": [0,0,0,1],
        "gunneropticseffect": [],
        "gunneroutopticseffect": [],
        "memorypointgunneroutoptics": "",
        "gunneroutforceoptics": 0,
        "gunneroutopticsshowcursor": 0,
        "gunnerfirealsoininternalcamera": 1,
        "gunneroutfirealsoininternalcamera": 1,
        "gunnerusespilotview": 0,
        "castgunnershadow": 0,
        "viewgunnershadow": 1,
        "viewgunnershadowdiff": 1,
        "viewgunnershadowamb": 1,
        "ejectdeadgunner": 0,
        "hideweaponsgunner": 1,
        "canhidegunner": -1,
        "forcehidegunner": 0,
        "outgunnermayfire": 0,
        "ingunnermayfire": 1,
        "showhmd": 0,
        "viewgunnerinexternal": 0,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "gunnercompartments": "Compartment1",
        "lodturnedin": -1,
        "lodturnedout": -1,
        "startengine": 1,
        "memorypointsgetingunnerprecise": "",
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "armorlights": 0.4,
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "reflectors": {
        },
        "aggregatereflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
        "gunfire": {
            "access": 0,
            "cloudletduration": 0.2,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletFire",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: WeaponFireGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
        "gunclouds": {
            "access": 0,
            "cloudletduration": 0.3,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 1,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletaccy": 0.4,
            "cloudletminyspeed": 0.2,
            "cloudletmaxyspeed": 0.8,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
        "mgunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints [Indent level: 2],
        "hitpoints": {
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitTurret [Indent level: 3]
            "hitturret": {
                "armor": 0.8,
                "material": 51,
                "name": "turret",
                "visual": "turret",
                "passthrough": 1,
                "explosionshielding": 1
            },
            # Class: CfgVehicles|AllVehicles|NewTurret|HitPoints|HitGun [Indent level: 3],
            "hitgun": {
                "armor": 0.6,
                "material": 52,
                "name": "gun",
                "visual": "gun",
                "passthrough": 1,
                "explosionshielding": 1
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "turrets": {
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
        "viewoptics": {
            "initanglex": 0,
            "minanglex": -30,
            "maxanglex": 30,
            "initangley": 0,
            "minangley": -100,
            "maxangley": 100,
            "initfov": 0.3,
            "minfov": 0.07,
            "maxfov": 0.35,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        "forcenvg": 0,
        "iscopilot": 0,
        "caneject": 1,
        "gunnerlefthandanimname": "",
        "gunnerrighthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnerrightleganimname": "",
        "gunnerdoor": "",
        "precisegetinout": 0,
        "turretfollowfreelook": 0,
        "allowtablock": 1,
        "showalltargets": 0,
        "dontcreateai": 0,
        "disablesoundattenuation": 0,
        "slingloadoperator": 0,
        "playerposition": 0,
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "turnin": {
            "turnoffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
        "turnout": {
            "turnoffset": 0
        },
        "gunnerinaction": "ManActTestDriver",
        "gunneraction": "ManActTestDriver",
        "gunbeg": "usti hlavne",
        "gunend": "konec hlavne",
        "memorypointgunneroptics": "gunnerview",
        "memorypointsgetingunner": "pos gunner",
        "memorypointsgetingunnerdir": "pos gunner dir",
        "memorypointgun": "kulas",
        "selectionfireanim": "zasleh",
        "showcrewaim": 0
    },
    "formationx": 200,
    "formationz": 300,
    "precision": 200,
    "brakedistance": 500,
    "steeraheadsimul": 1,
    "steeraheadplan": 2,
    "gearretracting": 1,
    "cabinopening": 1,
    "durationgetin": 0.99,
    "durationgetout": 0.99,
    "vtol": 0,
    "tailhook": 0,
    "lightongear": 1,
    "gearuptime": 3.33,
    "geardowntime": 2,
    "ejectdamagelimit": 0.45,
    "simulation": "airplanex",
    "mingunelev": 0,
    "maxgunelev": 0,
    "mingunturn": 0,
    "maxgunturn": 0,
    "vtolyawinfluence": 2,
    "vtolpitchinfluence": 2,
    "vtolrollinfluence": 2,
    # Class: CfgVehicles|Plane|ViewOptics [Indent level: 1],
    "viewoptics": {
        "initanglex": 0,
        "minanglex": 0,
        "maxanglex": 0,
        "initangley": 0,
        "minangley": 0,
        "maxangley": 0,
        "initfov": 0.5,
        "minfov": 0.5,
        "maxfov": 0.5,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    "selectionrotorstill": "vrtule staticka",
    "selectionrotormove": "vrtule blur",
    "memorypointldust": "levy prach",
    "memorypointrdust": "pravy prach",
    "selectionfireanim": "zasleh",
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "dusteffect": "HeliDust",
    "watereffect": "HeliWater",
    # Class: CfgVehicles|Plane|GunFire [Indent level: 1],
    "gunfire": {
        "access": 0,
        "cloudletduration": 0.2,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletgrowup": 0.2,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 0.5,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletFire",
        "cloudletcolor": [1,1,1,0],
        "interval": 0.01,
        "size": 3,
        "sourcesize": 0.5,
        "timetolive": 0,
        "initt": 4500,
        "deltat": -3000,
        # Class: WeaponFireGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponFireGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun|Table|T1 [Indent level: 1],
            "t1": {
                "maxt": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun|Table|T2 [Indent level: 1],
            "t2": {
                "maxt": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun|Table|T3 [Indent level: 1],
            "t3": {
                "maxt": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun|Table|T4 [Indent level: 1],
            "t4": {
                "maxt": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun|Table|T5 [Indent level: 1],
            "t5": {
                "maxt": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun|Table|T6 [Indent level: 1],
            "t6": {
                "maxt": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun|Table|T7 [Indent level: 1],
            "t7": {
                "maxt": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun|Table|T8 [Indent level: 1],
            "t8": {
                "maxt": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun|Table|T9 [Indent level: 1],
            "t9": {
                "maxt": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun|Table|T10 [Indent level: 1],
            "t10": {
                "maxt": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun|Table|T11 [Indent level: 1],
            "t11": {
                "maxt": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun|Table|T12 [Indent level: 1],
            "t12": {
                "maxt": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun|Table|T13 [Indent level: 1],
            "t13": {
                "maxt": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun|Table|T14 [Indent level: 1],
            "t14": {
                "maxt": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun|Table|T15 [Indent level: 1],
            "t15": {
                "maxt": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun|Table|T16 [Indent level: 1],
            "t16": {
                "maxt": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun|Table|T17 [Indent level: 1],
            "t17": {
                "maxt": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun|Table|T18 [Indent level: 1],
            "t18": {
                "maxt": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun|Table|T19 [Indent level: 1],
            "t19": {
                "maxt": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun|Table|T20 [Indent level: 1],
            "t20": {
                "maxt": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun|Table|T21 [Indent level: 1],
            "t21": {
                "maxt": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun|Table|T22 [Indent level: 1],
            "t22": {
                "maxt": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|Plane|GunClouds [Indent level: 1],
    "gunclouds": {
        "access": 0,
        "cloudletduration": 0.3,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletgrowup": 1,
        "cloudletfadein": 0.01,
        "cloudletfadeout": 1,
        "cloudletaccy": 0.4,
        "cloudletminyspeed": 0.2,
        "cloudletmaxyspeed": 0.8,
        "cloudletshape": "cloudletClouds",
        "cloudletcolor": [1,1,1,0],
        "interval": 0.05,
        "size": 3,
        "sourcesize": 0.5,
        "timetolive": 0,
        "initt": 0,
        "deltat": 0,
        # Class: WeaponCloudsGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|Plane|MGunFire [Indent level: 1],
    "mgunfire": {
        "cloudletduration": 0,
        "cloudletgrowup": 0.06,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.12,
        "interval": 0.005,
        "size": 0.12,
        "sourcesize": 0.01,
        "initt": 3200,
        "deltat": -4000,
        "access": 0,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 1,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletFire",
        "cloudletcolor": [1,1,1,0],
        "timetolive": 0,
        # Class: WeaponFireGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponFireGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [0.82,0.95,0.93,0]
            },
            # Class: WeaponFireGun|Table|T1 [Indent level: 1],
            "t1": {
                "maxt": 200,
                "color": [0.75,0.77,0.9,0]
            },
            # Class: WeaponFireGun|Table|T2 [Indent level: 1],
            "t2": {
                "maxt": 400,
                "color": [0.56,0.62,0.67,0]
            },
            # Class: WeaponFireGun|Table|T3 [Indent level: 1],
            "t3": {
                "maxt": 600,
                "color": [0.39,0.46,0.47,0]
            },
            # Class: WeaponFireGun|Table|T4 [Indent level: 1],
            "t4": {
                "maxt": 800,
                "color": [0.24,0.31,0.31,0]
            },
            # Class: WeaponFireGun|Table|T5 [Indent level: 1],
            "t5": {
                "maxt": 1000,
                "color": [0.23,0.31,0.29,0]
            },
            # Class: WeaponFireGun|Table|T6 [Indent level: 1],
            "t6": {
                "maxt": 1500,
                "color": [0.21,0.29,0.27,0]
            },
            # Class: WeaponFireGun|Table|T7 [Indent level: 1],
            "t7": {
                "maxt": 2000,
                "color": [0.19,0.23,0.21,0]
            },
            # Class: WeaponFireGun|Table|T8 [Indent level: 1],
            "t8": {
                "maxt": 2300,
                "color": [0.22,0.19,0.1,0]
            },
            # Class: WeaponFireGun|Table|T9 [Indent level: 1],
            "t9": {
                "maxt": 2500,
                "color": [0.35,0.2,0.02,0]
            },
            # Class: WeaponFireGun|Table|T10 [Indent level: 1],
            "t10": {
                "maxt": 2600,
                "color": [0.62,0.29,0.03,0]
            },
            # Class: WeaponFireGun|Table|T11 [Indent level: 1],
            "t11": {
                "maxt": 2650,
                "color": [0.59,0.35,0.05,0]
            },
            # Class: WeaponFireGun|Table|T12 [Indent level: 1],
            "t12": {
                "maxt": 2700,
                "color": [0.75,0.37,0.03,0]
            },
            # Class: WeaponFireGun|Table|T13 [Indent level: 1],
            "t13": {
                "maxt": 2750,
                "color": [0.88,0.34,0.03,0]
            },
            # Class: WeaponFireGun|Table|T14 [Indent level: 1],
            "t14": {
                "maxt": 2800,
                "color": [0.91,0.5,0.17,0]
            },
            # Class: WeaponFireGun|Table|T15 [Indent level: 1],
            "t15": {
                "maxt": 2850,
                "color": [1,0.6,0.2,0]
            },
            # Class: WeaponFireGun|Table|T16 [Indent level: 1],
            "t16": {
                "maxt": 2900,
                "color": [1,0.71,0.3,0]
            },
            # Class: WeaponFireGun|Table|T17 [Indent level: 1],
            "t17": {
                "maxt": 2950,
                "color": [0.98,0.83,0.41,0]
            },
            # Class: WeaponFireGun|Table|T18 [Indent level: 1],
            "t18": {
                "maxt": 3000,
                "color": [0.98,0.91,0.54,0]
            },
            # Class: WeaponFireGun|Table|T19 [Indent level: 1],
            "t19": {
                "maxt": 3100,
                "color": [0.98,0.99,0.6,0]
            },
            # Class: WeaponFireGun|Table|T20 [Indent level: 1],
            "t20": {
                "maxt": 3300,
                "color": [0.96,0.99,0.72,0]
            },
            # Class: WeaponFireGun|Table|T21 [Indent level: 1],
            "t21": {
                "maxt": 3600,
                "color": [1,0.98,0.91,0]
            },
            # Class: WeaponFireGun|Table|T22 [Indent level: 1],
            "t22": {
                "maxt": 4200,
                "color": [1,1,1,0]
            }
        }
    },
    # Class: CfgVehicles|Plane|MGunClouds [Indent level: 1],
    "mgunclouds": {
        "access": 0,
        "cloudletgrowup": 0.05,
        "cloudletfadein": 0,
        "cloudletfadeout": 0.1,
        "cloudletduration": 0.05,
        "cloudletanimperiod": 1,
        "cloudletsize": 1,
        "cloudletalpha": 0.3,
        "cloudletaccy": 0,
        "cloudletminyspeed": -100,
        "cloudletmaxyspeed": 100,
        "cloudletshape": "cloudletClouds",
        "cloudletcolor": [1,1,1,0],
        "timetolive": 0,
        "interval": 0.02,
        "size": 0.3,
        "sourcesize": 0.02,
        "initt": 0,
        "deltat": 0,
        # Class: WeaponCloudsMGun|Table [Indent level: 0],
        "table": {
            # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
            "t0": {
                "maxt": 0,
                "color": [1,1,1,0]
            }
        }
    },
    "numberphysicalwheels": 3,
    # Class: CfgVehicles|Plane|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|Plane|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_air_plane_s"],
            "speechplural": ["veh_air_plane_p"]
        }
    },
    "textsingular": "fast mover",
    "textplural": "fast movers",
    "namesound": "veh_air_plane_s",
    "type": 2,
    "memorypointgun": "kulomet",
    "fuelexplosionpower": 10,
    "crewcrashprotection": 0.15,
    "damageeffect": "AirDestructionEffects",
    "getinaction": "GetInHigh",
    "getoutaction": "GetOutHigh",
    "cargogetinaction": ["GetInHigh"],
    "cargogetoutaction": ["GetOutHigh"],
    "gunnergetinaction": "GetInHigh",
    "gunnergetoutaction": "GetOutHigh",
    "getinradius": 1.2,
    "camouflage": 100,
    "audible": 60,
    # Class: CfgVehicles|Plane|CamShake [Indent level: 1],
    "camshake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minspeed": 200
    },
    "camshakecoef": 0,
    "headgforceleaningfactor": [0.005,0.001,0.025],
    "explosionshielding": 2,
    # Class: CfgVehicles|Plane|DestructionEffects [Indent level: 1],
    "destructioneffects": {
    },
    "formationtime": 10,
    "fuelcapacity": 1000,
    "insidesoundcoef": 0.0316228,
    "outsidesoundfilter": 1,
    "occludesoundswhenin": 0.316228,
    "obstructsoundswhenin": 0.316228,
    "nightvision": 0,
    "drivercompartments": 0,
    "cargocompartments": [0],
    "enablegps": 1,
    "weaponsgroup1": "1 + 		2",
    "weaponsgroup2": 4,
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    # Class: CfgVehicles|Air|DustEffects [Indent level: 1],
    "dusteffects": {
        # Class: CfgDustEffectsAir|Both [Indent level: 0]
        "both": {
        },
        # Class: CfgDustEffectsAir|Left [Indent level: 0],
        "left": {
            "default": ["LDustEffectsAir"],
            "gdtstratisconcrete": ["LDustEffectsAir","LDirtEffects"],
            "gdtstratisbeach": ["LDustEffectsAir","LStonesEffects"],
            "gdtstratisdirt": ["LDustEffectsAir","LDirtEffects"],
            "gdtstratisseabedcluttered": ["LDustEffectsAir"],
            "gdtstratisseabed": ["LDustEffectsAir"],
            "gdtstratisdrygrass": ["LDustEffectsAir","LGrassDryEffects","LDirtEffects"],
            "gdtstratisgreengrass": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstratisrocky": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstratisthistles": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtconcrete": ["LDustEffectsAir","LDirtEffects"],
            "gdtasphalt": ["LDustEffectsAir","LDirtEffects"],
            "gdtrubble": ["LDustEffectsAir","LDirtEffects"],
            "gdtsoil": ["LDustEffectsAir","LDirtEffects"],
            "gdtbeach": ["LDustEffectsAir","LStonesEffects"],
            "gdtrock": ["LDustEffectsAir","LDirtEffects"],
            "gdtdead": ["LDustEffectsAir","LDirtEffects"],
            "gdtdesert1": ["LDustEffectsAir","LSandEffects","LDirtEffects","LStonesEffects"],
            "gdtdesert2": ["LDustEffectsAir","LSandEffects","LGrassEffects","LDirtEffects"],
            "gdtdirt": ["LDustEffectsAir","LDirtEffects"],
            "gdtgrassgreen": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtgrassdry": ["LDustEffectsAir","LGrassDryEffects","LDirtEffects"],
            "gdtgrasswild": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtwildfield": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtweed1": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtweed2": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtthorn": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstony": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstonygreen": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtstonythistle": ["LDustEffectsAir","LGrassEffects","LDirtEffects"],
            "gdtseabeddeep": ["LDustEffectsAir"],
            "gdtseabed": ["LDustEffectsAir"],
            "surfroaddirt": ["LDustEffectsAir"],
            "surfroadconcrete": ["LDustEffectsAir"],
            "surfroadtarmac": ["LDustEffectsAir"],
            "surfwood": ["LDustEffectsAir"],
            "surfmetal": ["LDustEffectsAir"],
            "surfrooftin": ["LDustEffectsAir"],
            "surfrooftiles": ["LDustEffectsAir"],
            "surfintwood": ["LDustEffectsAir"],
            "surfintconcrete": ["LDustEffectsAir"],
            "surfinttiles": ["LDustEffectsAir"],
            "surfintmetal": ["LDustEffectsAir"],
            "gdtgrassshort": ["LDustEffectsAir","LGrassEffects"],
            "gdtgrasstall": ["LDustEffectsAir","LGrassEffects"],
            "gdtreddirt": ["LDustEffectsAirRed"],
            "gdtfield": ["LDustEffectsAir"],
            "gdtforest": ["LDustEffectsAir"],
            "gdtvolcano": ["LDustEffectsAir","LStonesEffects"],
            "gdtcliff": ["LDustEffectsAir"],
            "gdtvolcanobeach": ["LDustEffectsAir"],
            "surfroaddirt_exp": ["LDustEffectsAirRed"],
            "surfroadconcrete_exp": ["LDustEffectsAir"],
            "surfroadtarmac_exp": ["LDustEffectsAir"],
            "gdtkldirt": ["LDustEffectsAir"],
            "gdtklgrass1": ["LDustEffectsAir","LGrassEffects"],
            "gdtklgrass2": ["LDustEffectsAir","LGrassEffects"],
            "gdtklforestcon": ["LDustEffectsAir"],
            "gdtklforestdec": ["LDustEffectsAir"],
            "gdtklmud": ["LDustEffectsAir"],
            "gdtklsoil": ["LDustEffectsAir"],
            "gdtkltarmac": ["LDustEffectsAir"],
            "gdtklstubble": ["LDustEffectsAir"],
            "gdtklstones": ["LDustEffectsAir"],
            "surfroaddirt_enoch": ["LDustEffectsAir"],
            "surftraildirt_enoch": ["LDustEffectsAir"],
            "surfroadtarmac1_enoch": ["LDustEffectsAir"],
            "surfroadtarmac2_enoch": ["LDustEffectsAir"],
            "surfroadtarmac3_enoch": ["LDustEffectsAir"]
        },
        # Class: CfgDustEffectsAir|Right [Indent level: 0],
        "right": {
            "default": ["RDustEffectsAir"],
            "gdtstratisconcrete": ["RDustEffectsAir","RDirtEffects"],
            "gdtstratisbeach": ["RDustEffectsAir","RStonesEffects"],
            "gdtstratisdirt": ["RDustEffectsAir","RDirtEffects"],
            "gdtstratisseabedcluttered": ["RDustEffectsAir"],
            "gdtstratisseabed": ["RDustEffectsAir"],
            "gdtstratisdrygrass": ["RDustEffectsAir","RGrassDryEffects","RDirtEffects"],
            "gdtstratisgreengrass": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstratisrocky": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstratisthistles": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtconcrete": ["RDustEffectsAir","RDirtEffects"],
            "gdtasphalt": ["RDustEffectsAir","RDirtEffects"],
            "gdtrubble": ["RDustEffectsAir","RDirtEffects"],
            "gdtsoil": ["RDustEffectsAir","RDirtEffects"],
            "gdtbeach": ["RDustEffectsAir","RStonesEffects"],
            "gdtrock": ["RDustEffectsAir","RDirtEffects"],
            "gdtdead": ["RDustEffectsAir","RDirtEffects"],
            "gdtdesert1": ["RDustEffectsAir","RSandEffects","RDirtEffects","RStonesEffects"],
            "gdtdesert2": ["RDustEffectsAir","RSandEffects","RGrassEffects","RDirtEffects"],
            "gdtdirt": ["RDustEffectsAir","RDirtEffects"],
            "gdtgrassgreen": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtgrassdry": ["RDustEffectsAir","RGrassDryEffects","RDirtEffects"],
            "gdtgrasswild": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtwildfield": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtweed1": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtweed2": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtthorn": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstony": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstonygreen": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtstonythistle": ["RDustEffectsAir","RGrassEffects","RDirtEffects"],
            "gdtseabeddeep": ["RDustEffectsAir"],
            "gdtseabed": ["RDustEffectsAir"],
            "surfroaddirt": ["RDustEffectsAir"],
            "surfroadconcrete": ["RDustEffectsAir"],
            "surfroadtarmac": ["RDustEffectsAir"],
            "surfwood": ["RDustEffectsAir"],
            "surfmetal": ["RDustEffectsAir"],
            "surfrooftin": ["RDustEffectsAir"],
            "surfrooftiles": ["RDustEffectsAir"],
            "surfintwood": ["RDustEffectsAir"],
            "surfintconcrete": ["RDustEffectsAir"],
            "surfinttiles": ["RDustEffectsAir"],
            "surfintmetal": ["RDustEffectsAir"],
            "gdtgrassshort": ["RDustEffectsAir","RGrassEffects"],
            "gdtgrasstall": ["RDustEffectsAir","RGrassEffects"],
            "gdtreddirt": ["RDustEffectsAirRed"],
            "gdtfield": ["RDustEffectsAir"],
            "gdtforest": ["RDustEffectsAir"],
            "gdtvolcano": ["RDustEffectsAir","RStonesEffects"],
            "gdtcliff": ["RDustEffectsAir"],
            "gdtvolcanobeach": ["RDustEffectsAir"],
            "surfroaddirt_exp": ["RDustEffectsAirRed"],
            "surfroadconcrete_exp": ["RDustEffectsAir"],
            "surfroadtarmac_exp": ["RDustEffectsAir"],
            "gdtkldirt": ["RDustEffectsAir"],
            "gdtklgrass1": ["RDustEffectsAir","RGrassEffects"],
            "gdtklgrass2": ["RDustEffectsAir","RGrassEffects"],
            "gdtklforestcon": ["RDustEffectsAir"],
            "gdtklforestdec": ["RDustEffectsAir"],
            "gdtklmud": ["RDustEffectsAir"],
            "gdtklsoil": ["RDustEffectsAir"],
            "gdtkltarmac": ["RDustEffectsAir"],
            "gdtklstubble": ["RDustEffectsAir"],
            "gdtklstones": ["RDustEffectsAir"],
            "surfroaddirt_enoch": ["RDustEffectsAir"],
            "surftraildirt_enoch": ["RDustEffectsAir"],
            "surfroadtarmac1_enoch": ["RDustEffectsAir"],
            "surfroadtarmac2_enoch": ["RDustEffectsAir"],
            "surfroadtarmac3_enoch": ["RDustEffectsAir"]
        }
    },
    "maxfordingdepth": 0.001,
    "waterresistance": 1,
    "impacteffectssea": "ImpactEffectsAir",
    "flarevelocity": 100,
    "enableradio": 1,
    "memorypointcm": ["flare_launcher1","flare_launcher2"],
    "memorypointcmdir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "radartype": 4,
    "radartarget": 1,
    "visualtarget": 1,
    "countermeasureactivationradius": 10000,
    # Class: CfgVehicles|Air|camShakeDamage [Indent level: 1],
    "camshakedamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minspeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "secondaryexplosion": -1,
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "squadtitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetincargo": "pos cargo",
    "memorypointsgetincargodir": "pos cargo dir",
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsgetincargoprecise": ["pos cargo"],
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "selectionclan": "clan",
    "selectionshowdamage": "poskozeni",
    "selectionbacklights": "zadni svetlo",
    # Class: CfgVehicles|AllVehicles|ViewCargo [Indent level: 1],
    "viewcargo": {
        "initanglex": 5,
        "minanglex": -75,
        "maxanglex": 85,
        "initangley": 0,
        "minangley": -150,
        "maxangley": 150,
        "minfov": 0.25,
        "maxfov": 1.25,
        "initfov": 0.75,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|AllVehicles|PilotSpec [Indent level: 1],
    "pilotspec": {
        "showheadphones": 0
    },
    # Class: CfgVehicles|AllVehicles|CargoSpec [Indent level: 1],
    "cargospec": {
        # Class: CfgVehicles|AllVehicles|CargoSpec|Cargo1 [Indent level: 2]
        "cargo1": {
            "showheadphones": 0
        }
    },
    # Class: CfgVehicles|AllVehicles|SoundEvents [Indent level: 1],
    "soundevents": {
    },
    "tracksspeed": 0,
    "selectionleftoffset": "",
    "selectionrightoffset": "",
    # Class: CfgVehicles|AllVehicles|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    "cargoproxyindexes": [],
    "driverleftleganimname": "",
    "driverrightleganimname": "",
    "driverdoor": "",
    "cargodoors": [],
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
    "availableforsupporttypes": [],
    "waterppinvehicle": 1,
    "htmin": 60,
    "htmax": 1800,
    "afmax": 200,
    "mfmax": 100,
    "mfact": 0.2,
    "tbody": 150,
    "impacteffectspeedlimit": 8,
    "showcrewaim": 0,
    # Class: CfgVehicles|AllVehicles|CargoTurret [Indent level: 1],
    "cargoturret": {
        # Class: CfgVehicles|AllVehicles|CargoTurret|ViewGunner [Indent level: 2]
        "viewgunner": {
            "initanglex": 5,
            "minanglex": -75,
            "maxanglex": 85,
            "initangley": 0,
            "minangley": -150,
            "maxangley": 150,
            "minfov": 0.25,
            "maxfov": 1.25,
            "initfov": 0.75,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        # Class: CfgVehicles|AllVehicles|CargoTurret|Hitpoints [Indent level: 2],
        "hitpoints": {
        },
        "animationsourcebody": "",
        "animationsourcegun": "",
        "body": "",
        "caneject": 1,
        "commanding": 0,
        "dontcreateai": 1,
        "gun": "",
        "gunnergetinaction": "GetInLow",
        "gunnergetoutaction": "GetOutLow",
        "gunnername": "cargo",
        "hideweaponsgunner": 0,
        "iscopilot": 0,
        "memorypointsgetingunner": "pos cargo",
        "memorypointsgetingunnerdir": "pos cargo dir",
        "primarygunner": 0,
        "proxytype": "CPCargo",
        "startengine": 0,
        "turretfollowfreelook": 0,
        "viewgunnerinexternal": 1,
        "disablesoundattenuation": 1,
        "outgunnermayfire": 1,
        "ispersonturret": 1,
        "showascargo": 1,
        "maxelev": 45,
        "minelev": -45,
        "maxturn": 95,
        "minturn": -95,
        "animationsourcehatch": "hatchGunner",
        "animationsourcecamelev": "camElev",
        "proxyindex": 1,
        "gunnertype": "",
        "primaryobserver": 0,
        "weapons": [],
        "magazines": [],
        "soundservo": ["",0.00316228,1],
        "soundelevation": ["",0.00316228,1],
        "initelev": 0,
        "initturn": 0,
        "minoutelev": -4,
        "maxoutelev": 20,
        "initoutelev": 0,
        "minoutturn": -60,
        "maxoutturn": 60,
        "initoutturn": 0,
        "maxhorizontalrotspeed": 1.2,
        "maxverticalrotspeed": 1.2,
        "mincamelev": -90,
        "maxcamelev": 90,
        "initcamelev": 0,
        "stabilizedinaxes": 3,
        "primary": 1,
        "hasgunner": 1,
        "turretcansee": 0,
        "canusescanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "turretspec": {
            "showheadphones": 0
        },
        "gunneropticsmodel": "",
        "gunneropticscolor": [0,0,0,1],
        "gunnerforceoptics": 1,
        "gunneropticsshowcursor": 0,
        "turretinfotype": "",
        "gunneroutopticsmodel": "",
        "gunneroutopticscolor": [0,0,0,1],
        "gunneropticseffect": [],
        "gunneroutopticseffect": [],
        "memorypointgunneroutoptics": "",
        "gunneroutforceoptics": 0,
        "gunneroutopticsshowcursor": 0,
        "gunnerfirealsoininternalcamera": 1,
        "gunneroutfirealsoininternalcamera": 1,
        "gunnerusespilotview": 0,
        "castgunnershadow": 0,
        "viewgunnershadow": 1,
        "viewgunnershadowdiff": 1,
        "viewgunnershadowamb": 1,
        "ejectdeadgunner": 0,
        "canhidegunner": -1,
        "forcehidegunner": 0,
        "ingunnermayfire": 1,
        "showhmd": 0,
        "lockwhendriverout": 0,
        "lockwhenvehiclespeed": -1,
        "gunnercompartments": "Compartment1",
        "lodturnedin": -1,
        "lodturnedout": -1,
        "memorypointsgetingunnerprecise": "",
        "missilebeg": "spice rakety",
        "missileend": "konec rakety",
        "armorlights": 0.4,
        # Class: CfgVehicles|AllVehicles|NewTurret|Reflectors [Indent level: 2],
        "reflectors": {
        },
        "aggregatereflectors": [],
        # Class: CfgVehicles|AllVehicles|NewTurret|GunFire [Indent level: 2],
        "gunfire": {
            "access": 0,
            "cloudletduration": 0.2,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 0.2,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 0.5,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletFire",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.01,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 4500,
            "deltat": -3000,
            # Class: WeaponFireGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponFireGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [0.82,0.95,0.93,0]
                },
                # Class: WeaponFireGun|Table|T1 [Indent level: 1],
                "t1": {
                    "maxt": 200,
                    "color": [0.75,0.77,0.9,0]
                },
                # Class: WeaponFireGun|Table|T2 [Indent level: 1],
                "t2": {
                    "maxt": 400,
                    "color": [0.56,0.62,0.67,0]
                },
                # Class: WeaponFireGun|Table|T3 [Indent level: 1],
                "t3": {
                    "maxt": 600,
                    "color": [0.39,0.46,0.47,0]
                },
                # Class: WeaponFireGun|Table|T4 [Indent level: 1],
                "t4": {
                    "maxt": 800,
                    "color": [0.24,0.31,0.31,0]
                },
                # Class: WeaponFireGun|Table|T5 [Indent level: 1],
                "t5": {
                    "maxt": 1000,
                    "color": [0.23,0.31,0.29,0]
                },
                # Class: WeaponFireGun|Table|T6 [Indent level: 1],
                "t6": {
                    "maxt": 1500,
                    "color": [0.21,0.29,0.27,0]
                },
                # Class: WeaponFireGun|Table|T7 [Indent level: 1],
                "t7": {
                    "maxt": 2000,
                    "color": [0.19,0.23,0.21,0]
                },
                # Class: WeaponFireGun|Table|T8 [Indent level: 1],
                "t8": {
                    "maxt": 2300,
                    "color": [0.22,0.19,0.1,0]
                },
                # Class: WeaponFireGun|Table|T9 [Indent level: 1],
                "t9": {
                    "maxt": 2500,
                    "color": [0.35,0.2,0.02,0]
                },
                # Class: WeaponFireGun|Table|T10 [Indent level: 1],
                "t10": {
                    "maxt": 2600,
                    "color": [0.62,0.29,0.03,0]
                },
                # Class: WeaponFireGun|Table|T11 [Indent level: 1],
                "t11": {
                    "maxt": 2650,
                    "color": [0.59,0.35,0.05,0]
                },
                # Class: WeaponFireGun|Table|T12 [Indent level: 1],
                "t12": {
                    "maxt": 2700,
                    "color": [0.75,0.37,0.03,0]
                },
                # Class: WeaponFireGun|Table|T13 [Indent level: 1],
                "t13": {
                    "maxt": 2750,
                    "color": [0.88,0.34,0.03,0]
                },
                # Class: WeaponFireGun|Table|T14 [Indent level: 1],
                "t14": {
                    "maxt": 2800,
                    "color": [0.91,0.5,0.17,0]
                },
                # Class: WeaponFireGun|Table|T15 [Indent level: 1],
                "t15": {
                    "maxt": 2850,
                    "color": [1,0.6,0.2,0]
                },
                # Class: WeaponFireGun|Table|T16 [Indent level: 1],
                "t16": {
                    "maxt": 2900,
                    "color": [1,0.71,0.3,0]
                },
                # Class: WeaponFireGun|Table|T17 [Indent level: 1],
                "t17": {
                    "maxt": 2950,
                    "color": [0.98,0.83,0.41,0]
                },
                # Class: WeaponFireGun|Table|T18 [Indent level: 1],
                "t18": {
                    "maxt": 3000,
                    "color": [0.98,0.91,0.54,0]
                },
                # Class: WeaponFireGun|Table|T19 [Indent level: 1],
                "t19": {
                    "maxt": 3100,
                    "color": [0.98,0.99,0.6,0]
                },
                # Class: WeaponFireGun|Table|T20 [Indent level: 1],
                "t20": {
                    "maxt": 3300,
                    "color": [0.96,0.99,0.72,0]
                },
                # Class: WeaponFireGun|Table|T21 [Indent level: 1],
                "t21": {
                    "maxt": 3600,
                    "color": [1,0.98,0.91,0]
                },
                # Class: WeaponFireGun|Table|T22 [Indent level: 1],
                "t22": {
                    "maxt": 4200,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|GunClouds [Indent level: 2],
        "gunclouds": {
            "access": 0,
            "cloudletduration": 0.3,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 1,
            "cloudletgrowup": 1,
            "cloudletfadein": 0.01,
            "cloudletfadeout": 1,
            "cloudletaccy": 0.4,
            "cloudletminyspeed": 0.2,
            "cloudletmaxyspeed": 0.8,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "interval": 0.05,
            "size": 3,
            "sourcesize": 0.5,
            "timetolive": 0,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|MGunClouds [Indent level: 2],
        "mgunclouds": {
            "access": 0,
            "cloudletgrowup": 0.05,
            "cloudletfadein": 0,
            "cloudletfadeout": 0.1,
            "cloudletduration": 0.05,
            "cloudletanimperiod": 1,
            "cloudletsize": 1,
            "cloudletalpha": 0.3,
            "cloudletaccy": 0,
            "cloudletminyspeed": -100,
            "cloudletmaxyspeed": 100,
            "cloudletshape": "cloudletClouds",
            "cloudletcolor": [1,1,1,0],
            "timetolive": 0,
            "interval": 0.02,
            "size": 0.3,
            "sourcesize": 0.02,
            "initt": 0,
            "deltat": 0,
            # Class: WeaponCloudsMGun|Table [Indent level: 0],
            "table": {
                # Class: WeaponCloudsMGun|Table|T0 [Indent level: 1]
                "t0": {
                    "maxt": 0,
                    "color": [1,1,1,0]
                }
            }
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|Turrets [Indent level: 2],
        "turrets": {
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|ViewOptics [Indent level: 2],
        "viewoptics": {
            "initanglex": 0,
            "minanglex": -30,
            "maxanglex": 30,
            "initangley": 0,
            "minangley": -100,
            "maxangley": 100,
            "initfov": 0.3,
            "minfov": 0.07,
            "maxfov": 0.35,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        },
        "forcenvg": 0,
        "gunnerlefthandanimname": "",
        "gunnerrighthandanimname": "",
        "gunnerleftleganimname": "",
        "gunnerrightleganimname": "",
        "gunnerdoor": "",
        "precisegetinout": 0,
        "allowtablock": 1,
        "showalltargets": 0,
        "slingloadoperator": 0,
        "playerposition": 0,
        "allowlauncherin": 0,
        "allowlauncherout": 0,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnIn [Indent level: 2],
        "turnin": {
            "turnoffset": 0
        },
        # Class: CfgVehicles|AllVehicles|NewTurret|TurnOut [Indent level: 2],
        "turnout": {
            "turnoffset": 0
        },
        "gunnerinaction": "ManActTestDriver",
        "gunneraction": "ManActTestDriver",
        "gunbeg": "usti hlavne",
        "gunend": "konec hlavne",
        "memorypointgunneroptics": "gunnerview",
        "memorypointgun": "kulas",
        "selectionfireanim": "zasleh",
        "showcrewaim": 0
    },
    "curatorinfotype": "RscDisplayAttributesVehicle",
    "curatorinfotypeempty": "RscDisplayAttributesVehicleEmpty",
    "access": 0,
    "reversed": 1,
    "autocenter": 1,
    "animated": 1,
    "shadow": 1,
    "featuretype": 0,
    "speechsingular": [],
    "speechplural": [],
    "maxdetectrange": 20,
    "detectskill": 20,
    "minealerticonrange": 200,
    "killfriendlyexpcoef": 1,
    "weaponslots": 0,
    "spotabledarknightlightsoff": 0.001,
    "spotablenightlightsoff": 0.02,
    "spotablenightlightson": 4,
    "accuracydarknightlightsoff": 0.001,
    "accuracynightlightsoff": 0.006,
    "accuracynightlightson": 0.1,
    "obstructsoundlfratio": 0,
    "occludesoundlfratio": 0.25,
    "unloadincombat": 0,
    "slowspeedforwardcoef": 0.3,
    "normalspeedforwardcoef": 0.85,
    "gunnerhasflares": 1,
    "enablemanualfire": 1,
    "sensitivity": 2.5,
    "sensitivityear": 0.0075,
    "portrait": "",
    "ghostpreview": "",
    "crewvulnerable": 1,
    "replacedamaged": "",
    "replacedamagedlimit": 0.9,
    "replacedamagedhitpoints": [],
    "keepinepesceneafterdeath": 0,
    "fuelconsumptionrate": 0.01,
    "groupcameraposition": [0,5,-30],
    "extcameraparams": [1],
    "camerasmoothspeed": 5,
    "predictturnsimul": 1.2,
    "predictturnplan": 1,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitciviliancoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "alwaystarget": 0,
    "irtarget": 1,
    "irscanground": 1,
    "lasertarget": 0,
    "nvtarget": 0,
    "nvscanner": 0,
    "artillerytarget": 0,
    "artilleryscanner": 0,
    "canusescanners": 1,
    "preferroads": 0,
    "unitinfotypelite": 0,
    "hideunitinfo": 0,
    "limitedspeedcoef": 0.22,
    "hasdriver": 1,
    "driverforceoptics": 0,
    "hideweaponsdriver": 1,
    "hideweaponscargo": 0,
    "enablewatch": 0,
    "useprecisegetinaction": 0,
    "allowtablock": 1,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
    "wheelcircumference": 1,
    "waterangulardampingcoef": 0,
    "shownvgdriver": 0,
    "shownvgcommander": 0,
    "shownvggunner": 0,
    "shownvgcargo": [0],
    "soundattenuationcargo": [1],
    "countsforscoreboard": 1,
    "hulldamagecauseexplosion": 0,
    # Class: CfgVehicles|All|NVGMarkers [Indent level: 1],
    "nvgmarkers": {
    },
    # Class: CfgVehicles|All|NVGMarker [Indent level: 1],
    "nvgmarker": {
        "diffuse": [1,1,1,1],
        "ambient": [1,1,1,1],
        "brightness": 1,
        "blinking": 0,
        "onlyinnvg": 0
    },
    # Class: CfgVehicles|All|HeadLimits [Indent level: 1],
    "headlimits": {
        "initanglex": 5,
        "minanglex": -30,
        "maxanglex": 40,
        "initangley": 0,
        "minangley": -90,
        "maxangley": 90,
        "minanglez": -45,
        "maxanglez": 45,
        "rotzradius": 0.2
    },
    "transportsoldier": 0,
    "transportammo": 0,
    "isbackpack": 0,
    "transportfuel": 0,
    "transportrepair": 0,
    "transportvehiclescount": 0,
    "transportvehiclesmass": 0,
    "attendant": 0,
    "engineer": 0,
    "uavhacker": 0,
    "soundengine": ["",1,1],
    "soundenviron": ["",1,1],
    # Class: CfgVehicles|All|SoundEnvironExt [Indent level: 1],
    "soundenvironext": {
    },
    # Class: CfgVehicles|All|SoundEquipment [Indent level: 1],
    "soundequipment": {
    },
    # Class: CfgVehicles|All|SoundGear [Indent level: 1],
    "soundgear": {
    },
    # Class: CfgVehicles|All|SoundBreath [Indent level: 1],
    "soundbreath": {
    },
    # Class: CfgVehicles|All|SoundBreathSwimming [Indent level: 1],
    "soundbreathswimming": {
    },
    # Class: CfgVehicles|All|SoundBreathInjured [Indent level: 1],
    "soundbreathinjured": {
    },
    # Class: CfgVehicles|All|SoundHitScream [Indent level: 1],
    "soundhitscream": {
    },
    # Class: CfgVehicles|All|SoundInjured [Indent level: 1],
    "soundinjured": {
    },
    # Class: CfgVehicles|All|SoundBreathAutomatic [Indent level: 1],
    "soundbreathautomatic": {
    },
    # Class: CfgVehicles|All|SoundDrown [Indent level: 1],
    "sounddrown": {
    },
    # Class: CfgVehicles|All|SoundChoke [Indent level: 1],
    "soundchoke": {
    },
    # Class: CfgVehicles|All|SoundRecovered [Indent level: 1],
    "soundrecovered": {
    },
    # Class: CfgVehicles|All|SoundBurning [Indent level: 1],
    "soundburning": {
    },
    # Class: CfgVehicles|All|PulsationSound [Indent level: 1],
    "pulsationsound": {
    },
    # Class: CfgVehicles|All|SoundDrowning [Indent level: 1],
    "sounddrowning": {
    },
    "soundcrash": ["",0.316228,1],
    "soundlandcrash": ["",1,1],
    "soundwatercrash": ["",0.177828,1],
    "soundservo": ["",0.00316228,0.5],
    "soundelevation": ["",0.00316228,0.5],
    "sounddamage": ["",1,1],
    "soundlandcrashes": ["soundLandCrash",1],
    "emptysound": ["",0,1],
    "soundbushcrash": ["emptySound",0],
    "driverinaction": "",
    "cargoaction": [],
    "cargoiscodriver": [0],
    "driveropticsmodel": "",
    "driveropticseffect": [],
    "driveropticscolor": [1,1,1,1],
    "hideproxyincombat": 0,
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 1,
    "viewcargoshadowamb": 1,
    "ejectdeaddriver": 0,
    "ejectdeadcargo": 0,
    "hiddenselectionsmaterials": [],
    "hiddenunderwaterselections": [],
    "shownunderwaterselections": [],
    "hiddenunderwaterselectionstextures": [],
    # Class: CfgVehicles|All|FxExplo [Indent level: 1],
    "fxexplo": {
        "access": 1
    },
    "selectiondamage": "zbytek",
    "headaimdown": 0,
    "cargocaneject": 1,
    "fireresistance": 10,
    "aircapacity": 10,
    "waterdamageengine": 0.2,
    "damagetexdelay": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "windsockexist": 0,
    "slingloadcargomemorypointsdir": [],
    "damagehalf": [],
    "damagefull": [],
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "insidedetectcoef": 0.05,
}