rhs_l159_cdf_b_CDF = {
    "editorPreview": "rhsgref|addons|rhsgref_editorPreviews|data|rhs_l159_cdf_b_CDF.paa",
    "faction": "rhsgref_faction_cdf_air_b",
    "crew": "rhsgref_cdf_b_air_pilot",
    "side": 1,
    "author": "Red Hammer Studios",
    "forceInGarage": 0,
    "scope": 2,
    "scopeCurator": 2,
    "dlc": "RHS_GREF",
    "rhs_decalParameters": ["['Number',[4,5],'AviaCDF']","['Label',[2],'Aviation', 5]","['Label',[3],'AviationSquadronsCDFGrey']"],
    "typicalCargo": ["rhsgref_cdf_air_pilot"],
    "model": "rhsgref|addons|rhsgref_air|L159|rhs_l159.p3d",
    "displayName": "L-159 ALCA",
    "vehicleClass": "rhs_vehclass_aircraft",
    "selectionDashboard": "podsvit pristroju",
    "unitInfoType": "RHSGREF_RscUnitInfoJet",
    "driverLeftHandAnimName": "throttle_pilot",
    "driverRightHandAnimName": "stick_pilot",
    # Class: CfgVehicles\RHS_L159_base\pilotCamera,
    "pilotCamera": {
    },
    # Class: CfgVehicles\RHS_L159_base\EjectionSystem,
    "EjectionSystem": {
    },
    "driverCanEject": 1,
    # Class: CfgVehicles\RHS_L159_base\EventHandlers,
    "EventHandlers": {
        "hit": "",
        # Class: CfgVehicles\RHS_L159_base\EventHandlers\RHS_EventHandlers,
        "RHS_EventHandlers": {
            "hit": "_this call RHS_fnc_AI_eject",
            "init": "_this call rhs_fnc_decalsReadParams",
            "getout": "[_this select 0, _this select 2] call rhs_fnc_vs1_seatEjection",
            "engine": "[_this select 0,_this select 1,10] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_addParachutes"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    # Class: CfgVehicles\RHS_L159_base\UserActions,
    "UserActions": {
    },
    # Class: CfgVehicles\RHS_L159_base\HitPoints,
    "HitPoints": {
        # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2
        "HitGlass2": {
            "armor": 1,
            "material": -1,
            "name": "glass2",
            "convexComponent": "glass2",
            "visual": "glass2",
            "passThrough": 0,
            # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass1,
                "BrokenGlass1": {
                    "simulation": "particles",
                    "type": "BrokenGlass1N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass2,
                "BrokenGlass2": {
                    "simulation": "particles",
                    "type": "BrokenGlass2N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass3,
                "BrokenGlass3": {
                    "simulation": "particles",
                    "type": "BrokenGlass3N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass4,
                "BrokenGlass4": {
                    "simulation": "particles",
                    "type": "BrokenGlass4N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass5,
                "BrokenGlass5": {
                    "simulation": "particles",
                    "type": "BrokenGlass5N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass6,
                "BrokenGlass6": {
                    "simulation": "particles",
                    "type": "BrokenGlass6N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass7,
                "BrokenGlass7": {
                    "simulation": "particles",
                    "type": "BrokenGlass7N_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass1S,
                "BrokenGlass1S": {
                    "simulation": "particles",
                    "type": "BrokenGlass1S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass2S,
                "BrokenGlass2S": {
                    "simulation": "particles",
                    "type": "BrokenGlass2S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass3S,
                "BrokenGlass3S": {
                    "simulation": "particles",
                    "type": "BrokenGlass3S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass4S,
                "BrokenGlass4S": {
                    "simulation": "particles",
                    "type": "BrokenGlass4S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass5S,
                "BrokenGlass5S": {
                    "simulation": "particles",
                    "type": "BrokenGlass5S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass6S,
                "BrokenGlass6S": {
                    "simulation": "particles",
                    "type": "BrokenGlass6S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\BrokenGlass7S,
                "BrokenGlass7S": {
                    "simulation": "particles",
                    "type": "BrokenGlass7S_0850_2250",
                    "position": "glass2_effect",
                    "intensity": 0.15,
                    "interval": 1,
                    "lifeTime": 0.05
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\RHS_ERA_Flash,
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "glass2_effect",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\RHS_ERA_Sound,
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "glass2_effect",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.005
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitGlass2\DestructionEffects\RHS_ERA_Smoke,
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "glass2_effect",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                }
            }
        },
        # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon1,
        "HitPylon1": {
            "armor": -40,
            "material": -1,
            "name": "hit_pylon_1",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon1\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon1\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon2,
        "HitPylon2": {
            "armor": -40,
            "material": -1,
            "name": "hit_pylon_2",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon2\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon2\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon3,
        "HitPylon3": {
            "armor": -40,
            "material": -1,
            "name": "hit_pylon_3",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon3\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon3\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon4,
        "HitPylon4": {
            "armor": -40,
            "material": -1,
            "name": "hit_pylon_4",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon4\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon4\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon5,
        "HitPylon5": {
            "armor": -40,
            "material": -1,
            "name": "hit_pylon_5",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon5\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon5\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon5\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_5",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon5\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon5\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon6,
        "HitPylon6": {
            "armor": -40,
            "material": -1,
            "name": "hit_pylon_6",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon6\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon6\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon6\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_6",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon6\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon6\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon7,
        "HitPylon7": {
            "armor": -40,
            "material": -1,
            "name": "hit_pylon_7",
            "passThrough": 0,
            "minimalHit": 0.8,
            "explosionShielding": 0.1,
            "radius": 0.7,
            "visual": "-",
            # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon7\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon7\DestructionEffects\RHS_Pylon_Flash,
                "RHS_Pylon_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_pylon_7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon7\DestructionEffects\RHS_Pylon_Sound,
                "RHS_Pylon_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_pylon_7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon7\DestructionEffects\RHS_Pylon_Smoke,
                "RHS_Pylon_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_pylon_7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_L159_base\HitPoints\HitPylon7\DestructionEffects\RHS_Pylon_Shard,
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
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitHull,
        "HitHull": {
            "armor": 4,
            "explosionShielding": 3,
            "name": "HitHull",
            "passThrough": 1,
            "visual": "Hit_Hull",
            "radius": 0.3,
            "minimalHit": 0.05,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitEngine,
        "HitEngine": {
            "armor": 3,
            "explosionShielding": 4,
            "name": "HitEngine",
            "passThrough": 1,
            "visual": "Hit_Engine",
            "radius": 0.3,
            "minimalHit": 0.05,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitAvionics,
        "HitAvionics": {
            "armor": 3,
            "explosionShielding": 3.5,
            "name": "HitAvionics",
            "passThrough": 0.5,
            "visual": "",
            "radius": 0.2,
            "minimalHit": 0.05,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitFuel,
        "HitFuel": {
            "armor": 4.5,
            "explosionShielding": 4,
            "name": "HitFuel",
            "passThrough": 0.8,
            "visual": "",
            "radius": 0.3,
            "minimalHit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitFuel_Lead_Left,
        "HitFuel_Lead_Left": {
            "armor": 1.8,
            "explosionShielding": 3,
            "name": "HitFuel1_Leads",
            "passThrough": 0,
            "visual": "Hit_AileronL",
            "radius": 0.13,
            "minimalHit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitFuel_Lead_Right,
        "HitFuel_Lead_Right": {
            "armor": 1.8,
            "explosionShielding": 3,
            "name": "HitFuel2_leads",
            "passThrough": 0,
            "visual": "Hit_AileronR",
            "radius": 0.13,
            "minimalHit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitFuel_Left,
        "HitFuel_Left": {
            "armor": 2.5,
            "explosionShielding": 5,
            "name": "HitFuel1",
            "passThrough": 0.2,
            "visual": "Hit_Fuel2a",
            "radius": 0.2,
            "minimalHit": 0.1,
            "depends": "HitFuel_Lead_Left",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitFuel_Right,
        "HitFuel_Right": {
            "armor": 2.5,
            "explosionShielding": 5,
            "name": "HitFuel2",
            "passThrough": 0.2,
            "visual": "Hit_Fuel2b",
            "radius": 0.2,
            "minimalHit": 0.1,
            "depends": "HitFuel_Lead_Right",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitFuel2,
        "HitFuel2": {
            "armor": 999,
            "explosionShielding": 0,
            "name": "HitFuel2",
            "passThrough": 0.2,
            "visual": "",
            "radius": 0.2,
            "minimalHit": 0.1,
            "depends": "(HitFuel_Left + HitFuel_Right)*0.5",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitGlass1,
        "HitGlass1": {
            "armor": 1.2,
            "explosionShielding": 3,
            "name": "HitGlass1",
            "passThrough": 0,
            "visual": "glass1",
            "radius": 0.2,
            "minimalHit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitGlass3,
        "HitGlass3": {
            "armor": 1.2,
            "explosionShielding": 3,
            "name": "HitGlass3",
            "passThrough": 0,
            "visual": "glass3",
            "radius": 0.2,
            "minimalHit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitLAileron_Link,
        "HitLAileron_Link": {
            "armor": 1.8,
            "explosionShielding": 3.5,
            "name": "HitLAileron_Link",
            "passThrough": 0,
            "visual": "Hit_AileronL",
            "radius": 0.09,
            "minimalHit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitRAileron_Link,
        "HitRAileron_Link": {
            "armor": 1.8,
            "explosionShielding": 3.5,
            "name": "HitRAileron_Link",
            "passThrough": 0,
            "visual": "Hit_AileronR",
            "radius": 0.09,
            "minimalHit": 0.1,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitLAileron,
        "HitLAileron": {
            "armor": 1.5,
            "explosionShielding": 3,
            "name": "HitLAileron",
            "passThrough": 0.3,
            "visual": "Hit_AileronL",
            "radius": 0.3,
            "minimalHit": 0.05,
            "depends": "HitLAileron_Link",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitRAileron,
        "HitRAileron": {
            "armor": 1.5,
            "explosionShielding": 3,
            "name": "HitRAileron",
            "passThrough": 0.3,
            "visual": "Hit_AileronR",
            "radius": 0.3,
            "minimalHit": 0.05,
            "depends": "HitRAileron_Link",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitLCRudder,
        "HitLCRudder": {
            "armor": 2,
            "explosionShielding": 3,
            "name": "HitLCRudder",
            "passThrough": 0.3,
            "visual": "Hit_RudderC",
            "radius": 0.3,
            "minimalHit": 0.05,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitLCElevator,
        "HitLCElevator": {
            "armor": 1.5,
            "explosionShielding": 3,
            "name": "HitLCElevator",
            "passThrough": 0.3,
            "visual": "Hit_ElevatorL",
            "radius": 0.3,
            "minimalHit": 0.05,
            "depends": "0",
            "material": -1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\HitPoints\HitRElevator,
        "HitRElevator": {
            "armor": 1.5,
            "explosionShielding": 3,
            "name": "HitRElevator",
            "passThrough": 0.3,
            "visual": "Hit_ElevatorR",
            "radius": 0.3,
            "minimalHit": 0.05,
            "depends": "0",
            "material": -1
        }
    },
    # Class: CfgVehicles\RHS_L159_base\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\HitGlass2
        "HitGlass2": {
            "source": "Hit",
            "hitpoint": "HitGlass2",
            "raw": 1
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\eject,
        "eject": {
            "source": "user",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\eject_hide,
        "eject_hide": {
            "source": "user",
            "animPeriod": 0.6,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\Damper_1_source,
        "Damper_1_source": {
            "source": "damper",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\Damper_2_source,
        "Damper_2_source": {
            "source": "damper",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\Damper_3_source,
        "Damper_3_source": {
            "source": "damper",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\Wheel_1_source,
        "Wheel_1_source": {
            "source": "wheel",
            "wheel": "Wheel_1"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\Wheel_2_source,
        "Wheel_2_source": {
            "source": "wheel",
            "wheel": "Wheel_2"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\Wheel_3_source,
        "Wheel_3_source": {
            "source": "wheel",
            "wheel": "Wheel_3"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\hit_pylon_1_source,
        "hit_pylon_1_source": {
            "source": "Hit",
            "hitpoint": "HitPylon1"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\hit_pylon_2_source,
        "hit_pylon_2_source": {
            "source": "Hit",
            "hitpoint": "HitPylon2"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\hit_pylon_3_source,
        "hit_pylon_3_source": {
            "source": "Hit",
            "hitpoint": "HitPylon3"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\hit_pylon_4_source,
        "hit_pylon_4_source": {
            "source": "Hit",
            "hitpoint": "HitPylon4"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\hit_pylon_5_source,
        "hit_pylon_5_source": {
            "source": "Hit",
            "hitpoint": "HitPylon5"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\hit_pylon_6_source,
        "hit_pylon_6_source": {
            "source": "Hit",
            "hitpoint": "HitPylon6"
        },
        # Class: CfgVehicles\RHS_L159_base\AnimationSources\hit_pylon_7_source,
        "hit_pylon_7_source": {
            "source": "Hit",
            "hitpoint": "HitPylon7"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\AddScalpel,
        "AddScalpel": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\AddAsraam_out,
        "AddAsraam_out": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\AddAsraam_mid,
        "AddAsraam_mid": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\AddMk82,
        "AddMk82": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\AddGbu12,
        "AddGbu12": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\AddZephyr,
        "AddZephyr": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\AddDar,
        "AddDar": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\Muzzle_flash,
        "Muzzle_flash": {
            "source": "ammorandom",
            "weapon": "Twin_Cannon_20mm"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\HitGlass1,
        "HitGlass1": {
            "source": "Hit",
            "hitpoint": "HitGlass1",
            "raw": 1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\HitGlass3,
        "HitGlass3": {
            "hitpoint": "HitGlass3",
            "source": "Hit",
            "raw": 1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\HitAvionics,
        "HitAvionics": {
            "source": "Hit",
            "hitpoint": "HitAvionics",
            "raw": 1
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\HideWeapons,
        "HideWeapons": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\canopy_hide,
        "canopy_hide": {
            "source": "user",
            "animPeriod": 0.001,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\ejection_seat_hide,
        "ejection_seat_hide": {
            "source": "user",
            "animPeriod": 0.001,
            "initPhase": 0
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\AnimationSources\ejection_seat_motion,
        "ejection_seat_motion": {
            "source": "user",
            "animPeriod": 0.25,
            "initPhase": 0
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
    "hiddenselections": ["camo1","camo2","i1","i2","n1","n2"],
    "hiddenselectionstextures": ["|rhsgref|addons|rhsgref_air|l159|data|l159_body_1_co.paa","|rhsgref|addons|rhsgref_air|l159|Data|l159_body_2_co.paa"],
    # Class: CfgVehicles\RHS_L159_base\Library,
    "Library": {
        "libTextDesc": "The A-143 Buzzard is a single seat light multi-purpose combat aircraft able to carry a wide range of equipment and weaponry. A-143 has seven weapon hardpoints, three under each wing and one under the fuselage. Standard armament consists of 20mm cannon, and a mixture of AA and AG rockets."
    },
    # Class: CfgVehicles\RHS_L159_base\MarkerLights,
    "MarkerLights": {
        # Class: CfgVehicles\RHS_L159_base\MarkerLights\PositionRed
        "PositionRed": {
            "color": [1,0,0],
            "ambient": [0.1,0,0],
            "intensity": 75,
            "name": "cerveny pozicni",
            "drawLight": 1,
            "drawLightSize": 0.15,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\RHS_L159_base\MarkerLights\PositionRed\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\RHS_L159_base\MarkerLights\PositionGreen,
        "PositionGreen": {
            "color": [0,1,0],
            "ambient": [0,0.1,0],
            "name": "zeleny pozicni",
            "intensity": 75,
            "drawLight": 1,
            "drawLightSize": 0.15,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\RHS_L159_base\MarkerLights\PositionRed\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        },
        # Class: CfgVehicles\RHS_L159_base\MarkerLights\PositionWhite,
        "PositionWhite": {
            "color": [1,1,1],
            "ambient": [0.1,0.1,0.1],
            "name": "light_nav_back",
            "intensity": 75,
            "drawLight": 1,
            "drawLightSize": 0.15,
            "drawLightCenterSize": 0.04,
            "activeLight": 0,
            "blinking": 0,
            "dayLight": 0,
            "useFlare": 0,
            # Class: CfgVehicles\RHS_L159_base\MarkerLights\PositionRed\Attenuation,
            "Attenuation": {
                "start": 0,
                "constant": 0,
                "linear": 25,
                "quadratic": 50,
                "hardLimitStart": 0.75,
                "hardLimitEnd": 1
            }
        }
    },
    # Class: CfgVehicles\RHS_L159_base\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\RHS_L159_base\Reflectors\Left
        "Left": {
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "position": "l svetlo",
            "selection": "l svetlo",
            "direction": "konec l svetla",
            "hitpoint": "l svetlo",
            "innerAngle": 20,
            "outerAngle": 60,
            "coneFadeCoef": 10,
            "intensity": 50,
            "useFlare": 1,
            "dayLight": 0,
            "FlareSize": 1,
            "size": 1,
            # Class: CfgVehicles\RHS_L159_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardLimitStart": 150,
                "hardLimitEnd": 300
            }
        },
        # Class: CfgVehicles\RHS_L159_base\Reflectors\Right,
        "Right": {
            "position": "p svetlo",
            "direction": "konec p svetla",
            "hitpoint": "p svetlo",
            "selection": "p svetlo",
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "innerAngle": 20,
            "outerAngle": 60,
            "coneFadeCoef": 10,
            "intensity": 50,
            "useFlare": 1,
            "dayLight": 0,
            "FlareSize": 1,
            "size": 1,
            # Class: CfgVehicles\RHS_L159_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardLimitStart": 150,
                "hardLimitEnd": 300
            }
        },
        # Class: CfgVehicles\RHS_L159_base\Reflectors\Center,
        "Center": {
            "position": "svetlo",
            "direction": "svetlo dir",
            "hitpoint": "svetlo",
            "selection": "svetlo",
            "color": [7000,7500,10000,1],
            "ambient": [100,100,100],
            "innerAngle": 20,
            "outerAngle": 60,
            "coneFadeCoef": 10,
            "intensity": 50,
            "useFlare": 1,
            "dayLight": 0,
            "FlareSize": 1,
            "size": 1,
            # Class: CfgVehicles\RHS_L159_base\Reflectors\Left\Attenuation,
            "Attenuation": {
                "constant": 0,
                "linear": 0,
                "quadratic": 4,
                "start": 1,
                "hardLimitStart": 150,
                "hardLimitEnd": 300
            }
        }
    },
    "aggregateReflectors": [["Left"],["Right"],["Center"]],
    # Class: CfgVehicles\RHS_L159_base\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\RHS_L159_base\Exhausts\Exhaust_1
        "Exhaust_1": {
            "position": "exhaust_start",
            "direction": "exhaust_dir",
            "effect": "ExhaustsEffectJet"
        }
    },
    # Class: CfgVehicles\RHS_L159_base\WingVortices,
    "WingVortices": {
        # Class: CfgVehicles\RHS_L159_base\WingVortices\WingTipLeft
        "WingTipLeft": {
            "effectName": "WingVortices",
            "position": "cerveny pozicni"
        },
        # Class: CfgVehicles\RHS_L159_base\WingVortices\WingTipRight,
        "WingTipRight": {
            "effectName": "WingVortices",
            "position": "zeleny pozicni"
        },
        # Class: CfgVehicles\RHS_L159_base\WingVortices\BodyLeft,
        "BodyLeft": {
            "effectName": "BodyVortices",
            "position": "body_vapour_L_S"
        },
        # Class: CfgVehicles\RHS_L159_base\WingVortices\BodyRight,
        "BodyRight": {
            "effectName": "BodyVortices",
            "position": "body_vapour_R_S"
        }
    },
    "driverAction": "RHS_L159_pilot",
    "envelope": [0,0.15,1.1,3,5,5.83,6,5.85,5.5,4.8,3.6,1.8,0],
    "weapons": [],
    "magazines": [],
    # Class: CfgVehicles\RHS_L159_base\Damage,
    "Damage": {
        "tex": [],
        "mat": ["rhsgref|addons|rhsgref_air|L159|data|L159_body_1.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_body_1_damage.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_body_1_destruct.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_body_2.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_body_2_damage.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_body_2_destruct.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass_damage.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass_destruct.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass_in.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass_damage.rvmat","rhsgref|addons|rhsgref_air|L159|data|L159_glass_destruct.rvmat"]
    },
    # Class: CfgVehicles\RHS_L159_base\Components,
    "Components": {
        # Class: CfgVehicles\RHS_L159_base\Components\TransportPylonsComponent
        "TransportPylonsComponent": {
            "uiPicture": "A3|Air_F_Gamma|Plane_Fighter_03|Data|UI|Plane_A143_3DEN_CA.paa",
            # Class: CfgVehicles\RHS_L159_base\Components\TransportPylonsComponent\Pylons,
            "Pylons": {
                # Class: CfgVehicles\RHS_L159_base\Components\TransportPylonsComponent\Pylons\Pylons1
                "Pylons1": {
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_AIM9","RHS_HP_AIM120"],
                    "attachment": "rhs_mag_Sidewinder",
                    "priority": 5,
                    "maxweight": 200,
                    "UIposition": [0.35,0.08],
                    "hitpoint": "HitPylon1"
                },
                # Class: CfgVehicles\RHS_L159_base\Components\TransportPylonsComponent\Pylons\Pylons2,
                "Pylons2": {
                    "priority": 4,
                    "attachment": "rhs_mag_FFAR_7_USAF",
                    "maxweight": 320,
                    "UIposition": [0.345,0.13],
                    "hitpoint": "HitPylon2",
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_AIM9","RHS_HP_AIM120"]
                },
                # Class: CfgVehicles\RHS_L159_base\Components\TransportPylonsComponent\Pylons\Pylons3,
                "Pylons3": {
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_LGB_500","RHS_HP_BOMB_500_3x","RHS_HP_AIM9","RHS_HP_AIM120","RHS_HP_ZPL20","RHS_HP_L159_FUELPOD"],
                    "priority": 3,
                    "attachment": "rhs_mag_mk82",
                    "maxweight": 400,
                    "UIposition": [0.34,0.18],
                    "hitpoint": "HitPylon3"
                },
                # Class: CfgVehicles\RHS_L159_base\Components\TransportPylonsComponent\Pylons\Pylons4,
                "Pylons4": {
                    "priority": 2,
                    "attachment": "rhs_mag_zpl20_hei",
                    "maxweight": 500,
                    "UIposition": [0.27,0.28],
                    "hardpoints": ["RHS_HP_ZPL20","RHS_HP_L159_FUELPOD"],
                    "hitpoint": "HitPylon4"
                },
                # Class: CfgVehicles\RHS_L159_base\Components\TransportPylonsComponent\Pylons\Pylons5,
                "Pylons5": {
                    "UIposition": [0.33,0.38],
                    "mirroredMissilePos": 3,
                    "hitpoint": "HitPylon5",
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_LGB_500","RHS_HP_BOMB_500_3x","RHS_HP_AIM9","RHS_HP_AIM120","RHS_HP_ZPL20","RHS_HP_L159_FUELPOD"],
                    "priority": 3,
                    "attachment": "rhs_mag_mk82",
                    "maxweight": 400
                },
                # Class: CfgVehicles\RHS_L159_base\Components\TransportPylonsComponent\Pylons\Pylons6,
                "Pylons6": {
                    "UIposition": [0.33,0.43],
                    "mirroredMissilePos": 2,
                    "hitpoint": "HitPylon6",
                    "priority": 4,
                    "attachment": "rhs_mag_FFAR_7_USAF",
                    "maxweight": 320,
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_AIM9","RHS_HP_AIM120"]
                },
                # Class: CfgVehicles\RHS_L159_base\Components\TransportPylonsComponent\Pylons\Pylons7,
                "Pylons7": {
                    "UIposition": [0.34,0.48],
                    "mirroredMissilePos": 1,
                    "hitpoint": "HitPylon7",
                    "hardpoints": ["RHS_HP_AGM65","RHS_HP_FFAR_USAF","RHS_HP_Hydra_USAF","RHS_HP_AIM9","RHS_HP_AIM120"],
                    "attachment": "rhs_mag_Sidewinder",
                    "priority": 5,
                    "maxweight": 200
                },
                # Class: CfgVehicles\RHS_L159_base\Components\TransportPylonsComponent\Pylons\cmDispenser,
                "cmDispenser": {
                    "hardpoints": ["RHSUSF_cm_ANALE40","RHSUSF_cm_ANALE40_x2"],
                    "priority": 1,
                    "attachment": "rhsusf_ANALE40_CMFlare_Chaff_Magazine_x2",
                    "maxweight": 800,
                    "UIposition": [0.625,0.275]
                }
            }
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent,
        "SensorsManagerComponent": {
            # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components
            "Components": {
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\IRSensorComponent
                "IRSensorComponent": {
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\IRSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 500,
                        "maxRange": 4000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": 1
                    },
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\IRSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 500,
                        "maxRange": 3000,
                        "objectDistanceLimitCoef": 1,
                        "viewDistanceLimitCoef": 1
                    },
                    "angleRangeHorizontal": 26,
                    "angleRangeVertical": 20,
                    "maxTrackableSpeed": 100,
                    "aimDown": 0,
                    "animDirection": "PilotCamera_V",
                    "componentType": "IRSensorComponent",
                    "typeRecognitionDistance": 2000,
                    "maxFogSeeThrough": 0.995,
                    "color": [1,0,0,1],
                    "allowsMarking": 1,
                    "groundNoiseDistanceCoef": -1,
                    "maxGroundNoiseDistance": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "minTrackableSpeed": -1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\VisualSensorComponent,
                "VisualSensorComponent": {
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\VisualSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 500,
                        "maxRange": 3000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": 1
                    },
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\VisualSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 500,
                        "maxRange": 2000,
                        "objectDistanceLimitCoef": 1,
                        "viewDistanceLimitCoef": 1
                    },
                    "angleRangeHorizontal": 26,
                    "angleRangeVertical": 20,
                    "maxTrackableSpeed": 100,
                    "aimDown": 0,
                    "animDirection": "PilotCamera_V",
                    "componentType": "VisualSensorComponent",
                    "nightRangeCoef": 0,
                    "maxFogSeeThrough": 0.94,
                    "color": [1,1,0.5,0.8],
                    "typeRecognitionDistance": 2000,
                    "allowsMarking": 1,
                    "groundNoiseDistanceCoef": -1,
                    "maxGroundNoiseDistance": -1,
                    "minSpeedThreshold": 0,
                    "maxSpeedThreshold": 0,
                    "minTrackableSpeed": -1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent,
                "ActiveRadarSensorComponent": {
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent\AirTarget
                    "AirTarget": {
                        "minRange": 8000,
                        "maxRange": 8000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\ActiveRadarSensorComponent\GroundTarget,
                    "GroundTarget": {
                        "minRange": 4000,
                        "maxRange": 4000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "angleRangeHorizontal": 90,
                    "angleRangeVertical": 90,
                    "componentType": "ActiveRadarSensorComponent",
                    "typeRecognitionDistance": 3000,
                    "groundNoiseDistanceCoef": 0.5,
                    "maxGroundNoiseDistance": 200,
                    "minSpeedThreshold": 20.8333,
                    "maxSpeedThreshold": 27.7778,
                    "color": [0,1,1,1],
                    "allowsMarking": 1,
                    "animDirection": "",
                    "aimDown": 0,
                    "minTrackableSpeed": -1e+010,
                    "maxTrackableSpeed": 1e+010,
                    "minTrackableATL": -1e+010,
                    "maxTrackableATL": 1e+010
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\PassiveRadarSensorComponent,
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
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\LaserSensorComponent,
                "LaserSensorComponent": {
                    "componentType": "LaserSensorComponent",
                    # Class: SensorTemplateLaser\AirTarget,
                    "AirTarget": {
                        "minRange": 6000,
                        "maxRange": 6000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: SensorTemplateLaser\GroundTarget,
                    "GroundTarget": {
                        "minRange": 6000,
                        "maxRange": 6000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "angleRangeHorizontal": 180,
                    "angleRangeVertical": 180,
                    "typeRecognitionDistance": 0,
                    "color": [1,1,1,0],
                    "allowsMarking": 1,
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
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\SensorsManagerComponent\Components\NVSensorComponent,
                "NVSensorComponent": {
                    "componentType": "NVSensorComponent",
                    "color": [1,1,1,0],
                    # Class: SensorTemplateLaser\AirTarget,
                    "AirTarget": {
                        "minRange": 6000,
                        "maxRange": 6000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    # Class: SensorTemplateLaser\GroundTarget,
                    "GroundTarget": {
                        "minRange": 6000,
                        "maxRange": 6000,
                        "objectDistanceLimitCoef": -1,
                        "viewDistanceLimitCoef": -1
                    },
                    "angleRangeHorizontal": 180,
                    "angleRangeVertical": 180,
                    "typeRecognitionDistance": 0,
                    "allowsMarking": 1,
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
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentLeft,
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentLeft\Components
            "Components": {
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentLeft\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentLeft\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentLeft\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentLeft\Components\VehicleDriverDisplay,
                "VehicleDriverDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Driver"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentLeft\Components\VehicleMissileDisplay,
                "VehicleMissileDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Missile"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentLeft\Components\SensorDisplay,
                "SensorDisplay": {
                    "componentType": "SensorsDisplayComponent",
                    "range": [8000,4000,2000,16000],
                    "resource": "RscCustomInfoSensors"
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultDisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentRight,
        "VehicleSystemsDisplayManagerComponentRight": {
            "defaultDisplay": "SensorDisplay",
            # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentRight\Components,
            "Components": {
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentRight\Components\EmptyDisplay
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentRight\Components\MinimapDisplay,
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent",
                    "resource": "RscCustomInfoAirborneMiniMap"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentRight\Components\UAVDisplay,
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentRight\Components\VehicleDriverDisplay,
                "VehicleDriverDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Driver"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentRight\Components\VehicleMissileDisplay,
                "VehicleMissileDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Missile"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\Components\VehicleSystemsDisplayManagerComponentRight\Components\SensorDisplay,
                "SensorDisplay": {
                    "componentType": "SensorsDisplayComponent",
                    "range": [8000,4000,2000,16000],
                    "resource": "RscCustomInfoSensors"
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "right": 1,
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles\Air\Components\TransportCountermeasuresComponent,
        "TransportCountermeasuresComponent": {
        }
    },
    "features": "Randomization: No						<br />Camo selections: 2 - the main body, wings and lower part of body						<br />Script door sources: None						<br />Script animations: AddScalpel, AddAsraam_out, AddAsraam_mid, AddMk82, AddGbu12, AddZephyr, AddDar						<br />Executed scripts: None 						<br />Firing from vehicles: No						<br />Slingload: Slingloadable						<br />Cargo proxy indexes: None",
    "mapSize": 13.02,
    "_generalMacro": "Plane_Fighter_03_base_F",
    "icon": "A3|Air_F_Gamma|Plane_Fighter_03|Data|UI|Map_Plane_Fighter_03_CA.paa",
    "picture": "A3|Air_F_Gamma|Plane_Fighter_03|Data|UI|Plane_Fighter_03_CA.paa",
    "editorSubcategory": "EdSubcat_Planes",
    "accuracy": 0.2,
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "armor": 55,
    "armorStructural": 2,
    "armorLights": 0.1,
    "minTotalDamageThreshold": 0.008,
    "waterLeakiness": 1.5,
    "epeImpulseDamageCoef": 50,
    "damageResistance": 0.004,
    "destrType": "DestructWreck",
    "slingLoadCargoMemoryPoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "viewDriverShadowDiff": 0.5,
    "viewDriverShadowAmb": 0.5,
    "radarTargetSize": 0.8,
    "visualTargetSize": 0.8,
    "irTargetSize": 0.8,
    "lockDetectionSystem": 8,
    "incomingMissileDetectionSystem": "8 + 16",
    "cost": 3e+006,
    # Class: CfgVehicles\Plane_Fighter_03_base_F\Turrets,
    "Turrets": {
    },
    # Class: CfgVehicles\Plane_Fighter_03_base_F\TransportItems,
    "TransportItems": {
    },
    "attenuationEffectType": "PlaneAttenuation",
    "soundGetIn": ["A3|Sounds_F|air|Plane_Fighter_03|buzzard_getin",1,1,40],
    "soundGetOut": ["A3|Sounds_F|air|Plane_Fighter_03|getout",1,1,40],
    "cabinOpenSound": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinOpen",1.77828,1,40],
    "cabinCloseSound": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinClose",1.77828,1,40],
    "cabinOpenSoundInternal": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinOpen",10,1,40],
    "cabinCloseSoundInternal": ["A3|Sounds_F|air|noises|Plane_Fighter03_CabinClose",10,1,40],
    "soundDammage": ["A3|Sounds_F|debugsound",1.77828,1,100],
    "soundEngineOnInt": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-start_int",1,1],
    "soundEngineOnExt": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-start_ext",1.77828,1,500],
    "soundEngineOffInt": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-stop_int",1,1],
    "soundEngineOffExt": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-stop_ext",1.77828,1,500],
    "soundLocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",0.316228,1],
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_1",0.316228,1.5],
    "soundGearUp": ["A3|Sounds_F_EPC|CAS_02|gear_up",0.794328,1,150],
    "soundGearDown": ["A3|Sounds_F_EPC|CAS_02|gear_down",0.794328,1,150],
    "soundFlapsUp": ["A3|Sounds_F_EPC|CAS_02|Flaps_Up",0.630957,1,100],
    "soundFlapsDown": ["A3|Sounds_F_EPC|CAS_02|Flaps_Down",0.630957,1,100],
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
    "soundWaterCollision1": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_1",1.41254,1,500],
    "soundWaterCollision2": ["A3|Sounds_F|vehicles|crashes|planes|plane_crash_water_2",1.41254,1,500],
    "soundWaterCrashes": ["soundWaterCollision1",0.5,"soundWaterCollision2",0.5],
    "landingSoundInt0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int1",1,1,100],
    "landingSoundInt1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_large_int2",1,1,100],
    "landingSoundInt": ["landingSoundInt0",0.5,"landingSoundInt1",0.5],
    "landingSoundOut0": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext1",1.77828,1,100],
    "landingSoundOut1": ["A3|Sounds_F|vehicles|air|noises|landing_wheels_ext2",1.77828,1,100],
    "landingSoundOut": ["landingSoundOut0",0.5,"landingSoundOut1",0.5],
    # Class: CfgVehicles\Plane_Fighter_03_base_F\scrubLandInt,
    "scrubLandInt": {
        "sound": ["A3|Sounds_F|vehicles|air|noises|wheelsInt",1,1,100],
        "frequency": 1,
        "volume": "(scrubLand factor[0.01, 0.20])"
    },
    # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds,
    "Sounds": {
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\EngineLowOut
        "EngineLowOut": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03_low_ext",1.41254,1,1200],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "camPos*2*(rpm factor[0.95, 0])*(rpm factor[0, 0.95])"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\EngineHighOut,
        "EngineHighOut": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03_engi_ext",1.41254,1.2,1400],
            "frequency": "1",
            "volume": "camPos*4*(rpm factor[0.5, 1.1])*(rpm factor[1.1, 0.5])"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\ForsageOut,
        "ForsageOut": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-fors_ext",1.12202,0.99,1700],
            "frequency": "1",
            "volume": "engineOn*camPos*(thrust factor[0.6, 1.0])",
            "cone": [3.14,3.92,2,0.5]
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\WindNoiseOut,
        "WindNoiseOut": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|noise",0.562341,1,150],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "camPos*(speed factor[1, 150])"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\EngineLowIn,
        "EngineLowIn": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03_low_int",1,1],
            "frequency": "1.0 min (rpm + 0.5)",
            "volume": "(1-camPos)*((rpm factor[0.7, 0.1])*(rpm factor[0.1, 0.7]))"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\EngineHighIn,
        "EngineHighIn": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03_engi_int",0.562341,1.2],
            "frequency": "1",
            "volume": "(1-camPos)*(rpm factor[0.85, 1.0])"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\ForsageIn,
        "ForsageIn": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|Plane_Fighter_03-fors_int",0.562341,1],
            "frequency": "1",
            "volume": "(1-camPos)*(engineOn*(thrust factor[0.6, 1.0]))"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\WindNoiseIn,
        "WindNoiseIn": {
            "sound": ["A3|Sounds_F|air|Plane_Fighter_03|noise_int",0.398107,1],
            "frequency": "(0.1+(1.2*(speed factor[1, 150])))",
            "volume": "(1-camPos)*(speed factor[1, 150])"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\RainExt,
        "RainExt": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_ext",1.77828,1,100],
            "frequency": 1,
            "volume": "camPos * rain * (speed factor[50, 0])"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\RainInt,
        "RainInt": {
            "sound": ["A3|Sounds_F|vehicles|noises|rain1_int",1,1,100],
            "frequency": 1,
            "volume": "(1-camPos) * rain * (speed factor[50, 0])"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\Waternoise_ext,
        "Waternoise_ext": {
            "sound": ["A3|Sounds_F|vehicles|noises|air_driving_in_water",0.707946,1,300],
            "frequency": "1",
            "volume": "(speed factor[0, 5]) * water * camPos + (speed factor[-0.1, -5]) * water * camPos"
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Sounds\Waternoise_int,
        "Waternoise_int": {
            "sound": ["A3|Sounds_F|vehicles|noises|soft_driving_in_water_int",0.562341,1,100],
            "frequency": "1",
            "volume": "(speed factor[0, 5]) * water * (1-camPos) + (speed factor[-0.1, -5]) * water * (1-camPos)"
        }
    },
    "maxOmega": 2000,
    "antiRollbarForceCoef": 0,
    "antiRollbarForceLimit": 0,
    "antiRollbarSpeedMin": 50,
    "antiRollbarSpeedMax": 300,
    # Class: CfgVehicles\Plane_Fighter_03_base_F\Wheels,
    "Wheels": {
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Wheels\Wheel_1
        "Wheel_1": {
            "boneName": "Wheel_1",
            "steering": 1,
            "side": "left",
            "center": "Wheel_1_center",
            "boundary": "Wheel_1_rim",
            "width": 0.4,
            "mass": 20,
            "MOI": 0.4,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxBrakeTorque": 0,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "suspForceAppPointOffset": "Wheel_1_center",
            "tireForceAppPointOffset": "Wheel_1_center",
            "maxCompression": 0.1,
            "maxDroop": 0.1,
            "sprungMass": 1500,
            "springStrength": 150000,
            "springDamperRate": 30000,
            "longitudinalStiffnessPerUnitGravity": 300,
            "latStiffX": 3,
            "latStiffY": 20,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Wheels\Wheel_2,
        "Wheel_2": {
            "steering": 0,
            "boneName": "Wheel_2",
            "center": "Wheel_2_center",
            "boundary": "Wheel_2_rim",
            "mass": 35,
            "MOI": 1.575,
            "width": 0.6,
            "maxBrakeTorque": 1500,
            "maxCompression": 0.05,
            "maxDroop": 0.05,
            "sprungMass": 3350,
            "springStrength": 335000,
            "springDamperRate": 67000,
            "longitudinalStiffnessPerUnitGravity": 500,
            "suspForceAppPointOffset": "Wheel_2_center",
            "tireForceAppPointOffset": "Wheel_2_center",
            "side": "left",
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "latStiffX": 3,
            "latStiffY": 20,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\Wheels\Wheel_3,
        "Wheel_3": {
            "boneName": "Wheel_3",
            "side": "right",
            "center": "Wheel_3_center",
            "boundary": "Wheel_3_rim",
            "suspForceAppPointOffset": "Wheel_3_center",
            "tireForceAppPointOffset": "Wheel_3_center",
            "steering": 0,
            "mass": 35,
            "MOI": 1.575,
            "width": 0.6,
            "maxBrakeTorque": 1500,
            "maxCompression": 0.05,
            "maxDroop": 0.05,
            "sprungMass": 3350,
            "springStrength": 335000,
            "springDamperRate": 67000,
            "longitudinalStiffnessPerUnitGravity": 500,
            "dampingRate": 0.1,
            "dampingRateDamaged": 1,
            "dampingRateDestroyed": 1000,
            "maxHandBrakeTorque": 0,
            "suspTravelDirection": [0,-1,0],
            "latStiffX": 3,
            "latStiffY": 20,
            "frictionVsSlipGraph": [[0,1],[0.5,1],[1,1]]
        }
    },
    "maxSpeed": 800,
    "landingAoa": "6*3.1415/180",
    "landingSpeed": 215,
    "stallSpeed": 190,
    "stallWarningTreshold": 0.1,
    "wheelSteeringSensitivity": 2,
    "airBrake": 1,
    "airBrakeFrictionCoef": 2.2,
    "flaps": 1,
    "flapsFrictionCoef": 0.32,
    "gearsUpFrictionCoef": 0.6,
    "airFrictionCoefs0": [0,0,0],
    "airFrictionCoefs1": [0.1,0.5,0.0066],
    "airFrictionCoefs2": [0.001,0.005,6.8e-005],
    "angleOfIndicence": "-2*3.1415/180",
    "altNoForce": 13000,
    "altFullForce": 2000,
    "thrustCoef": [1.42,1.38,1.34,1.3,1.25,1.2,1.19,1.18,1.17,1.17,1.16,1.16,0.1,0,0,0,0],
    "aileronSensitivity": 1,
    "aileronCoef": [0,0.11,0.45,0.81,1.1,1.15,1.2,1.25,1.3,1.35,1.4,1.43,1.45,1.47,1.4,1.2,0.8],
    "elevatorSensitivity": 1.1,
    "elevatorCoef": [0,0.14,0.54,0.62,0.58,0.56,0.54,0.52,0.48,0.43,0.38,0.35,0.3,0.25,0.2,0.15,0.1],
    "rudderInfluence": 0.866,
    "rudderCoef": [0,0.8,2,2.2,2.3,2.4,2.3,2.2,2.1,2,1.2],
    "aileronControlsSensitivityCoef": 3.6,
    "elevatorControlsSensitivityCoef": 3.4,
    "rudderControlsSensitivityCoef": 3.8,
    "draconicForceXCoef": 8,
    "draconicForceYCoef": 1.4,
    "draconicForceZCoef": 1,
    "draconicTorqueXCoef": [4.8,5,5.5,6.2,7,7.7,9.4,11.1,12,14,15],
    "draconicTorqueYCoef": [12,10,6,2,0.2,0,0,0,0,0,0,0,0,0,0,0,0],
    # Class: CfgVehicles\Plane_Fighter_03_base_F\TextureSources,
    "TextureSources": {
        # Class: CfgVehicles\Plane_Fighter_03_base_F\TextureSources\Hex
        "Hex": {
            "displayName": "Hex",
            "author": "Bohemia Interactive",
            "factions": ["OPF_F","OPF_T_F"],
            "textures": ["|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_1_brownhex_CO.paa","|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_2_brownhex_CO.paa"]
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\TextureSources\Green,
        "Green": {
            "displayName": "AAF",
            "author": "Bohemia Interactive",
            "factions": ["IND_F"],
            "textures": ["|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_1_INDP_CO.paa","|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_2_INDP_CO.paa"]
        },
        # Class: CfgVehicles\Plane_Fighter_03_base_F\TextureSources\Grey,
        "Grey": {
            "displayName": "Grey",
            "author": "Bohemia Interactive",
            "factions": ["OPF_F","OPF_T_F"],
            "textures": ["|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_1_greyhex_CO.paa","|a3|Air_F_Gamma|Plane_Fighter_03|Data|Plane_Fighter_03_body_2_greyhex_CO.paa"]
        }
    },
    "driveOnComponent": [],
    "irScanRangeMin": 500,
    "irScanRangeMax": 5000,
    "irScanToEyeFactor": 2,
    "laserScanner": 1,
    "showAllTargets": 4,
    "gunAimDown": 0.029,
    "extCameraPosition": [0,3.8,-15],
    # Class: CfgVehicles\Plane_Fighter_03_base_F\ViewPilot,
    "ViewPilot": {
        "initAngleX": -3,
        "initFov": 0.75,
        "minFov": 0.25,
        "maxFov": 1.25,
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
    "memoryPointLRocket": "Rocket_1",
    "memoryPointRRocket": "Rocket_2",
    "minFireTime": 30,
    "threat": [0.8,1,0.8],
    "memoryPointDriverOptics": "PilotCamera_pos",
    "driverWeaponsInfoType": "RscOptics_CAS_01_TGP",
    "defaultUserMFDvalues": [0,0.5,0.4,1],
    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD,
    "MFD": {
        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD
        "AirplaneHUD": {
            "enableParallax": 1,
            "topLeft": "HUD_1_top_left",
            "topRight": "HUD_1_top_right",
            "bottomLeft": "HUD_1_bottom_left",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,0.5,0.4,1],
            # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones,
            "Bones": {
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\PlaneW
                "PlaneW": {
                    "type": "fixed",
                    "pos": [0.4975,0.38]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\Center,
                "Center": {
                    "type": "fixed",
                    "pos": [0.4975,0.383]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\ImpactPoint,
                "ImpactPoint": {
                    "type": "vector",
                    "source": "ImpactPoint",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\WPPoint,
                "WPPoint": {
                    "type": "vector",
                    "source": "WPPoint",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\TargetingPodDir,
                "TargetingPodDir": {
                    "source": "pilotcamera",
                    "type": "vector",
                    "pos0": [0.4975,0.383],
                    "pos10": [1.4475,1.453]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\TargetingPodTarget,
                "TargetingPodTarget": {
                    "source": "pilotcameratarget",
                    "type": "vector",
                    "pos0": [0.4975,0.383],
                    "pos10": [1.4475,1.453]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\Limit0109,
                "Limit0109": {
                    "type": "limit",
                    "limits": [0.1,0.1,0.9,0.9]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot1,
                "MissileFlightTimeRot1": {
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "max": 0.5,
                    "minAngle": 0,
                    "maxAngle": 18,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot2,
                "MissileFlightTimeRot2": {
                    "maxAngle": 36,
                    "max": 1,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot3,
                "MissileFlightTimeRot3": {
                    "maxAngle": 54,
                    "max": 1.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot4,
                "MissileFlightTimeRot4": {
                    "maxAngle": 72,
                    "max": 2,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot5,
                "MissileFlightTimeRot5": {
                    "maxAngle": 90,
                    "max": 2.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot6,
                "MissileFlightTimeRot6": {
                    "maxAngle": 108,
                    "max": 3,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot7,
                "MissileFlightTimeRot7": {
                    "maxAngle": 126,
                    "max": 3.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot8,
                "MissileFlightTimeRot8": {
                    "maxAngle": 144,
                    "max": 4,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot9,
                "MissileFlightTimeRot9": {
                    "maxAngle": 162,
                    "max": 4.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot10,
                "MissileFlightTimeRot10": {
                    "maxAngle": 180,
                    "max": 5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot11,
                "MissileFlightTimeRot11": {
                    "maxAngle": 198,
                    "max": 5.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot12,
                "MissileFlightTimeRot12": {
                    "maxAngle": 216,
                    "max": 6,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot13,
                "MissileFlightTimeRot13": {
                    "maxAngle": 234,
                    "max": 6.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot14,
                "MissileFlightTimeRot14": {
                    "maxAngle": 252,
                    "max": 7,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot15,
                "MissileFlightTimeRot15": {
                    "maxAngle": 270,
                    "max": 7.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot16,
                "MissileFlightTimeRot16": {
                    "maxAngle": 288,
                    "max": 8,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\MissileFlightTimeRot17,
                "MissileFlightTimeRot17": {
                    "maxAngle": 306,
                    "max": 8.5,
                    "type": "rotational",
                    "source": "MissileFlightTime",
                    "sourceScale": 1,
                    "center": [0,0],
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\Target,
                "Target": {
                    "source": "target",
                    "type": "vector",
                    "pos0": [0.4975,0.383],
                    "pos10": [1.4475,1.453]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\Velocity,
                "Velocity": {
                    "type": "vector",
                    "source": "velocity",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\ILS_H,
                "ILS_H": {
                    "type": "ils",
                    "pos0": [0.5,0.383],
                    "pos3": [0.785,0.383]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\ILS_W,
                "ILS_W": {
                    "pos3": [0.5,0.704],
                    "type": "ils",
                    "pos0": [0.5,0.383]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\ASL_Instrument,
                "ASL_Instrument": {
                    "type": "rotational",
                    "source": "altitudeASL",
                    "center": [0.9,0.337895],
                    "min": 0,
                    "max": 20000,
                    "minAngle": 0,
                    "maxAngle": 72000,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\Speed_Instrument,
                "Speed_Instrument": {
                    "source": "speed",
                    "center": [0.1,0.337895],
                    "max": 555.556,
                    "maxAngle": 7200,
                    "type": "rotational",
                    "min": 0,
                    "minAngle": 0,
                    "aspectRatio": 1.12632
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\HorizonBankRot,
                "HorizonBankRot": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "center": [0.4975,0.38],
                    "min": -0.5236,
                    "max": 0.5236,
                    "minAngle": 159.25,
                    "maxAngle": 200.75,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\AOAindexer,
                "AOAindexer": {
                    "type": "linear",
                    "source": "aoa",
                    "min": -0.7854,
                    "max": 0.7854,
                    "maxPos": [0,-1.9],
                    "minPos": [0,2.1],
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\HorizonBankRotFull,
                "HorizonBankRotFull": {
                    "type": "rotational",
                    "source": "horizonBank",
                    "center": [0,0],
                    "min": -3.1416,
                    "max": 3.1416,
                    "minAngle": -180,
                    "maxAngle": 180,
                    "aspectRatio": 1
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\Level0,
                "Level0": {
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon",
                    "angle": 0
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP5,
                "LevelP5": {
                    "angle": 5,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM5,
                "LevelM5": {
                    "angle": -5,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP10,
                "LevelP10": {
                    "angle": 10,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM10,
                "LevelM10": {
                    "angle": -10,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP15,
                "LevelP15": {
                    "angle": 15,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM15,
                "LevelM15": {
                    "angle": -15,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP20,
                "LevelP20": {
                    "angle": 20,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM20,
                "LevelM20": {
                    "angle": -20,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP25,
                "LevelP25": {
                    "angle": 25,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM25,
                "LevelM25": {
                    "angle": -25,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP30,
                "LevelP30": {
                    "angle": 30,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM30,
                "LevelM30": {
                    "angle": -30,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP35,
                "LevelP35": {
                    "angle": 35,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM35,
                "LevelM35": {
                    "angle": -35,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP40,
                "LevelP40": {
                    "angle": 40,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM40,
                "LevelM40": {
                    "angle": -40,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP45,
                "LevelP45": {
                    "angle": 45,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM45,
                "LevelM45": {
                    "angle": -45,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP50,
                "LevelP50": {
                    "angle": 50,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM50,
                "LevelM50": {
                    "angle": -50,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP55,
                "LevelP55": {
                    "angle": 55,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM55,
                "LevelM55": {
                    "angle": -55,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP60,
                "LevelP60": {
                    "angle": 60,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM60,
                "LevelM60": {
                    "angle": -60,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP65,
                "LevelP65": {
                    "angle": 65,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM65,
                "LevelM65": {
                    "angle": -65,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP70,
                "LevelP70": {
                    "angle": 70,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM70,
                "LevelM70": {
                    "angle": -70,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP75,
                "LevelP75": {
                    "angle": 75,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM75,
                "LevelM75": {
                    "angle": -75,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP80,
                "LevelP80": {
                    "angle": 80,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM80,
                "LevelM80": {
                    "angle": -80,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP85,
                "LevelP85": {
                    "angle": 85,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM85,
                "LevelM85": {
                    "angle": -85,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelP90,
                "LevelP90": {
                    "angle": 90,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\LevelM90,
                "LevelM90": {
                    "angle": -90,
                    "pos0": [0.4975,0.38],
                    "pos10": [1.4475,1.45],
                    "type": "horizon"
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\Airport1,
                "Airport1": {
                    "type": "vector",
                    "source": "airportCorner1",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\Airport2,
                "Airport2": {
                    "source": "airportCorner2",
                    "type": "vector",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\Airport3,
                "Airport3": {
                    "source": "airportCorner3",
                    "type": "vector",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Bones\Airport4,
                "Airport4": {
                    "source": "airportCorner4",
                    "type": "vector",
                    "pos0": [0.5,0.383],
                    "pos10": [1.45,1.453]
                }
            },
            # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw,
            "Draw": {
                "alpha": "user3",
                "color": ["user0","user1","user2"],
                "condition": "on",
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\PlaneW,
                "PlaneW": {
                    "type": "line",
                    "points": [["PlaneW",[-0.03,0],1],["PlaneW",[-0.01,0],1],[],["PlaneW",[0.03,0],1],["PlaneW",[0.01,0],1],[],["PlaneW",[0,-0.0337895],1],["PlaneW",[0,-0.0112632],1],[],["PlaneW",[0,0.0337895],1],["PlaneW",[0,0.0112632],1]]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\PlaneHeading,
                "PlaneHeading": {
                    "type": "line",
                    "points": [["Velocity",1,"Limit0109",1,[0,-0.0225263],1],["Velocity",1,"Limit0109",1,[0.014,-0.0157684],1],["Velocity",1,"Limit0109",1,[0.02,0],1],["Velocity",1,"Limit0109",1,[0.014,0.0157684],1],["Velocity",1,"Limit0109",1,[0,0.0225263],1],["Velocity",1,"Limit0109",1,[-0.014,0.0157684],1],["Velocity",1,"Limit0109",1,[-0.02,0],1],["Velocity",1,"Limit0109",1,[-0.014,-0.0157684],1],["Velocity",1,"Limit0109",1,[0,-0.0225263],1],[],["Velocity",1,"Limit0109",1,[0.04,0],1],["Velocity",1,"Limit0109",1,[0.02,0],1],[],["Velocity",1,"Limit0109",1,[-0.04,0],1],["Velocity",1,"Limit0109",1,[-0.02,0],1],[],["Velocity",1,"Limit0109",1,[0,-0.0450526],1],["Velocity",1,"Limit0109",1,[0,-0.0225263],1]]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\AOAIndexer,
                "AOAIndexer": {
                    "condition": "ils",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\AOAIndexer\lines,
                    "lines": {
                        "type": "line",
                        "points": [["Velocity",1,"Limit0109",1,["AOAindexer",-0.04,0.112632],1],["Velocity",1,"Limit0109",1,["AOAindexer",-0.06,0.112632],1],["Velocity",1,"Limit0109",1,["AOAindexer",-0.06,0],1],["Velocity",1,"Limit0109",1,["AOAindexer",-0.05,0],1],[],["Velocity",1,"Limit0109",1,["AOAindexer",-0.06,0],1],["Velocity",1,"Limit0109",1,["AOAindexer",-0.06,-0.112632],1],["Velocity",1,"Limit0109",1,["AOAindexer",-0.04,-0.112632],1]]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Static,
                "Static": {
                    "type": "line",
                    "points": [[[0.0925,0.442079],1],[[0.1075,0.442079],1],[],[[0.1,0.433632],1],[[0.1,0.450526],1],[],[[0.14687,0.422182],1],[[0.16187,0.422182],1],[],[[0.15437,0.413734],1],[[0.15437,0.430629],1],[],[[0.180473,0.370089],1],[[0.195473,0.370089],1],[],[[0.187973,0.361642],1],[[0.187973,0.378537],1],[],[[0.180473,0.3057],1],[[0.195473,0.3057],1],[],[[0.187973,0.297253],1],[[0.187973,0.314147],1],[],[[0.14687,0.253608],1],[[0.16187,0.253608],1],[],[[0.15437,0.245161],1],[[0.15437,0.262055],1],[],[[0.0925,0.233711],1],[[0.1075,0.233711],1],[],[[0.1,0.225263],1],[[0.1,0.242158],1],[],[[0.0381299,0.253608],1],[[0.0531299,0.253608],1],[],[[0.0456299,0.245161],1],[[0.0456299,0.262055],1],[],[[0.00452726,0.3057],1],[[0.0195273,0.3057],1],[],[[0.0120273,0.297253],1],[[0.0120273,0.314147],1],[],[[0.00452728,0.370089],1],[[0.0195273,0.370089],1],[],[[0.0120273,0.361642],1],[[0.0120273,0.378537],1],[],[[0.0381299,0.422182],1],[[0.0531299,0.422182],1],[],[[0.0456299,0.413734],1],[[0.0456299,0.430629],1],[],["Speed_Instrument",[0,0.065],1],["Speed_Instrument",[0,0.085],1],[],[[0.8925,0.442079],1],[[0.9075,0.442079],1],[],[[0.9,0.433632],1],[[0.9,0.450526],1],[],[[0.94687,0.422182],1],[[0.96187,0.422182],1],[],[[0.95437,0.413734],1],[[0.95437,0.430629],1],[],[[0.980473,0.370089],1],[[0.995473,0.370089],1],[],[[0.987973,0.361642],1],[[0.987973,0.378537],1],[],[[0.980473,0.3057],1],[[0.995473,0.3057],1],[],[[0.987973,0.297253],1],[[0.987973,0.314147],1],[],[[0.94687,0.253608],1],[[0.96187,0.253608],1],[],[[0.95437,0.245161],1],[[0.95437,0.262055],1],[],[[0.8925,0.233711],1],[[0.9075,0.233711],1],[],[[0.9,0.225263],1],[[0.9,0.242158],1],[],[[0.83813,0.253608],1],[[0.85313,0.253608],1],[],[[0.84563,0.245161],1],[[0.84563,0.262055],1],[],[[0.804527,0.3057],1],[[0.819527,0.3057],1],[],[[0.812027,0.297253],1],[[0.812027,0.314147],1],[],[[0.804527,0.370089],1],[[0.819527,0.370089],1],[],[[0.812027,0.361642],1],[[0.812027,0.378537],1],[],[[0.83813,0.422182],1],[[0.85313,0.422182],1],[],[[0.84563,0.413734],1],[[0.84563,0.430629],1],[],["ASL_Instrument",[0,0.065],1],["ASL_Instrument",[0,0.085],1],[],[[0.5,0.107],1],[[0.51,0.129526],1],[[0.49,0.129526],1],[[0.5,0.107],1],[],[[0.619959,0.712986],1],[[0.631439,0.744203],1],[],[[0.58291,0.739019],1],[[0.588087,0.760778],1],[],[[0.540574,0.748504],1],[[0.543184,0.770838],1],[],[[0.4975,0.740421],1],[[0.4975,0.77421],1],[],[[0.454426,0.748504],1],[[0.451816,0.770838],1],[],[[0.41209,0.739019],1],[[0.406913,0.760778],1],[],[[0.375041,0.712986],1],[[0.363561,0.744203],1]]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\HorizonBankRot,
                "HorizonBankRot": {
                    "type": "line",
                    "points": [["HorizonBankRot",[0,0.39421],1],["HorizonBankRot",[0.01,0.416737],1],["HorizonBankRot",[-0.01,0.416737],1],["HorizonBankRot",[0,0.39421],1]]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont,
                "Horizont": {
                    "clipTL": [0,0.15],
                    "clipBR": [1,0.75],
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed,
                    "Dimmed": {
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\Level0
                        "Level0": {
                            "type": "line",
                            "points": [["Level0",[0.4,0],1],["Level0",[0.05,0],1],[],["Level0",[-0.05,0],1],["Level0",[-0.4,0],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM5,
                        "LevelM5": {
                            "type": "line",
                            "points": [["LevelM5",[-0.2,0.005],1],["LevelM5",[-0.17,0.004],1],[],["LevelM5",[-0.14,0.003],1],["LevelM5",[-0.11,0.002],1],[],["LevelM5",[-0.08,0.001],1],["LevelM5",[-0.05,0],1],["LevelM5",[-0.05,-0.03],1],[],["LevelM5",[0.05,-0.03],1],["LevelM5",[0.05,0],1],["LevelM5",[0.08,0.001],1],[],["LevelM5",[0.11,0.002],1],["LevelM5",[0.14,0.003],1],[],["LevelM5",[0.17,0.004],1],["LevelM5",[0.2,0.005],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_5,
                        "VALM_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": -5,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM5",[-0.18,-0.082],1],
                            "right": ["LevelM5",[-0.1,-0.082],1],
                            "down": ["LevelM5",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP5,
                        "LevelP5": {
                            "type": "line",
                            "points": [["LevelP5",[-0.2,0.03],1],["LevelP5",[-0.2,0],1],["LevelP5",[-0.05,0],1],[],["LevelP5",[0.05,0],1],["LevelP5",[0.2,0],1],["LevelP5",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_5,
                        "VALP_1_5": {
                            "type": "text",
                            "source": "static",
                            "text": "5",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP5",[-0.18,0.032],1],
                            "right": ["LevelP5",[-0.1,0.032],1],
                            "down": ["LevelP5",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM10,
                        "LevelM10": {
                            "type": "line",
                            "points": [["LevelM10",[-0.2,0.01],1],["LevelM10",[-0.17,0.008],1],[],["LevelM10",[-0.14,0.006],1],["LevelM10",[-0.11,0.004],1],[],["LevelM10",[-0.08,0.002],1],["LevelM10",[-0.05,0],1],["LevelM10",[-0.05,-0.03],1],[],["LevelM10",[0.05,-0.03],1],["LevelM10",[0.05,0],1],["LevelM10",[0.08,0.002],1],[],["LevelM10",[0.11,0.004],1],["LevelM10",[0.14,0.006],1],[],["LevelM10",[0.17,0.008],1],["LevelM10",[0.2,0.01],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_10,
                        "VALM_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": -10,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM10",[-0.18,-0.082],1],
                            "right": ["LevelM10",[-0.1,-0.082],1],
                            "down": ["LevelM10",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP10,
                        "LevelP10": {
                            "type": "line",
                            "points": [["LevelP10",[-0.2,0.03],1],["LevelP10",[-0.2,0],1],["LevelP10",[-0.05,0],1],[],["LevelP10",[0.05,0],1],["LevelP10",[0.2,0],1],["LevelP10",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_10,
                        "VALP_1_10": {
                            "type": "text",
                            "source": "static",
                            "text": "10",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP10",[-0.18,0.032],1],
                            "right": ["LevelP10",[-0.1,0.032],1],
                            "down": ["LevelP10",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM15,
                        "LevelM15": {
                            "type": "line",
                            "points": [["LevelM15",[-0.2,0.015],1],["LevelM15",[-0.17,0.012],1],[],["LevelM15",[-0.14,0.009],1],["LevelM15",[-0.11,0.006],1],[],["LevelM15",[-0.08,0.003],1],["LevelM15",[-0.05,0],1],["LevelM15",[-0.05,-0.03],1],[],["LevelM15",[0.05,-0.03],1],["LevelM15",[0.05,0],1],["LevelM15",[0.08,0.003],1],[],["LevelM15",[0.11,0.006],1],["LevelM15",[0.14,0.009],1],[],["LevelM15",[0.17,0.012],1],["LevelM15",[0.2,0.015],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_15,
                        "VALM_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": -15,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM15",[-0.18,-0.082],1],
                            "right": ["LevelM15",[-0.1,-0.082],1],
                            "down": ["LevelM15",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP15,
                        "LevelP15": {
                            "type": "line",
                            "points": [["LevelP15",[-0.2,0.03],1],["LevelP15",[-0.2,0],1],["LevelP15",[-0.05,0],1],[],["LevelP15",[0.05,0],1],["LevelP15",[0.2,0],1],["LevelP15",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_15,
                        "VALP_1_15": {
                            "type": "text",
                            "source": "static",
                            "text": "15",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP15",[-0.18,0.032],1],
                            "right": ["LevelP15",[-0.1,0.032],1],
                            "down": ["LevelP15",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM20,
                        "LevelM20": {
                            "type": "line",
                            "points": [["LevelM20",[-0.2,0.02],1],["LevelM20",[-0.17,0.016],1],[],["LevelM20",[-0.14,0.012],1],["LevelM20",[-0.11,0.008],1],[],["LevelM20",[-0.08,0.004],1],["LevelM20",[-0.05,0],1],["LevelM20",[-0.05,-0.03],1],[],["LevelM20",[0.05,-0.03],1],["LevelM20",[0.05,0],1],["LevelM20",[0.08,0.004],1],[],["LevelM20",[0.11,0.008],1],["LevelM20",[0.14,0.012],1],[],["LevelM20",[0.17,0.016],1],["LevelM20",[0.2,0.02],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_20,
                        "VALM_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": -20,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM20",[-0.18,-0.082],1],
                            "right": ["LevelM20",[-0.1,-0.082],1],
                            "down": ["LevelM20",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP20,
                        "LevelP20": {
                            "type": "line",
                            "points": [["LevelP20",[-0.2,0.03],1],["LevelP20",[-0.2,0],1],["LevelP20",[-0.05,0],1],[],["LevelP20",[0.05,0],1],["LevelP20",[0.2,0],1],["LevelP20",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_20,
                        "VALP_1_20": {
                            "type": "text",
                            "source": "static",
                            "text": "20",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP20",[-0.18,0.032],1],
                            "right": ["LevelP20",[-0.1,0.032],1],
                            "down": ["LevelP20",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM25,
                        "LevelM25": {
                            "type": "line",
                            "points": [["LevelM25",[-0.2,0.025],1],["LevelM25",[-0.17,0.02],1],[],["LevelM25",[-0.14,0.015],1],["LevelM25",[-0.11,0.01],1],[],["LevelM25",[-0.08,0.005],1],["LevelM25",[-0.05,0],1],["LevelM25",[-0.05,-0.03],1],[],["LevelM25",[0.05,-0.03],1],["LevelM25",[0.05,0],1],["LevelM25",[0.08,0.005],1],[],["LevelM25",[0.11,0.01],1],["LevelM25",[0.14,0.015],1],[],["LevelM25",[0.17,0.02],1],["LevelM25",[0.2,0.025],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_25,
                        "VALM_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": -25,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM25",[-0.18,-0.082],1],
                            "right": ["LevelM25",[-0.1,-0.082],1],
                            "down": ["LevelM25",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP25,
                        "LevelP25": {
                            "type": "line",
                            "points": [["LevelP25",[-0.2,0.03],1],["LevelP25",[-0.2,0],1],["LevelP25",[-0.05,0],1],[],["LevelP25",[0.05,0],1],["LevelP25",[0.2,0],1],["LevelP25",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_25,
                        "VALP_1_25": {
                            "type": "text",
                            "source": "static",
                            "text": "25",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP25",[-0.18,0.032],1],
                            "right": ["LevelP25",[-0.1,0.032],1],
                            "down": ["LevelP25",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM30,
                        "LevelM30": {
                            "type": "line",
                            "points": [["LevelM30",[-0.2,0.03],1],["LevelM30",[-0.17,0.024],1],[],["LevelM30",[-0.14,0.018],1],["LevelM30",[-0.11,0.012],1],[],["LevelM30",[-0.08,0.006],1],["LevelM30",[-0.05,0],1],["LevelM30",[-0.05,-0.03],1],[],["LevelM30",[0.05,-0.03],1],["LevelM30",[0.05,0],1],["LevelM30",[0.08,0.006],1],[],["LevelM30",[0.11,0.012],1],["LevelM30",[0.14,0.018],1],[],["LevelM30",[0.17,0.024],1],["LevelM30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_30,
                        "VALM_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": -30,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM30",[-0.18,-0.082],1],
                            "right": ["LevelM30",[-0.1,-0.082],1],
                            "down": ["LevelM30",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP30,
                        "LevelP30": {
                            "type": "line",
                            "points": [["LevelP30",[-0.2,0.03],1],["LevelP30",[-0.2,0],1],["LevelP30",[-0.05,0],1],[],["LevelP30",[0.05,0],1],["LevelP30",[0.2,0],1],["LevelP30",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_30,
                        "VALP_1_30": {
                            "type": "text",
                            "source": "static",
                            "text": "30",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP30",[-0.18,0.032],1],
                            "right": ["LevelP30",[-0.1,0.032],1],
                            "down": ["LevelP30",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM35,
                        "LevelM35": {
                            "type": "line",
                            "points": [["LevelM35",[-0.2,0.035],1],["LevelM35",[-0.17,0.028],1],[],["LevelM35",[-0.14,0.021],1],["LevelM35",[-0.11,0.014],1],[],["LevelM35",[-0.08,0.007],1],["LevelM35",[-0.05,0],1],["LevelM35",[-0.05,-0.03],1],[],["LevelM35",[0.05,-0.03],1],["LevelM35",[0.05,0],1],["LevelM35",[0.08,0.007],1],[],["LevelM35",[0.11,0.014],1],["LevelM35",[0.14,0.021],1],[],["LevelM35",[0.17,0.028],1],["LevelM35",[0.2,0.035],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_35,
                        "VALM_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": -35,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM35",[-0.18,-0.082],1],
                            "right": ["LevelM35",[-0.1,-0.082],1],
                            "down": ["LevelM35",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP35,
                        "LevelP35": {
                            "type": "line",
                            "points": [["LevelP35",[-0.2,0.03],1],["LevelP35",[-0.2,0],1],["LevelP35",[-0.05,0],1],[],["LevelP35",[0.05,0],1],["LevelP35",[0.2,0],1],["LevelP35",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_35,
                        "VALP_1_35": {
                            "type": "text",
                            "source": "static",
                            "text": "35",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP35",[-0.18,0.032],1],
                            "right": ["LevelP35",[-0.1,0.032],1],
                            "down": ["LevelP35",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM40,
                        "LevelM40": {
                            "type": "line",
                            "points": [["LevelM40",[-0.2,0.04],1],["LevelM40",[-0.17,0.032],1],[],["LevelM40",[-0.14,0.024],1],["LevelM40",[-0.11,0.016],1],[],["LevelM40",[-0.08,0.008],1],["LevelM40",[-0.05,0],1],["LevelM40",[-0.05,-0.03],1],[],["LevelM40",[0.05,-0.03],1],["LevelM40",[0.05,0],1],["LevelM40",[0.08,0.008],1],[],["LevelM40",[0.11,0.016],1],["LevelM40",[0.14,0.024],1],[],["LevelM40",[0.17,0.032],1],["LevelM40",[0.2,0.04],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_40,
                        "VALM_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": -40,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM40",[-0.18,-0.082],1],
                            "right": ["LevelM40",[-0.1,-0.082],1],
                            "down": ["LevelM40",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP40,
                        "LevelP40": {
                            "type": "line",
                            "points": [["LevelP40",[-0.2,0.03],1],["LevelP40",[-0.2,0],1],["LevelP40",[-0.05,0],1],[],["LevelP40",[0.05,0],1],["LevelP40",[0.2,0],1],["LevelP40",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_40,
                        "VALP_1_40": {
                            "type": "text",
                            "source": "static",
                            "text": "40",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP40",[-0.18,0.032],1],
                            "right": ["LevelP40",[-0.1,0.032],1],
                            "down": ["LevelP40",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM45,
                        "LevelM45": {
                            "type": "line",
                            "points": [["LevelM45",[-0.2,0.045],1],["LevelM45",[-0.17,0.036],1],[],["LevelM45",[-0.14,0.027],1],["LevelM45",[-0.11,0.018],1],[],["LevelM45",[-0.08,0.009],1],["LevelM45",[-0.05,0],1],["LevelM45",[-0.05,-0.03],1],[],["LevelM45",[0.05,-0.03],1],["LevelM45",[0.05,0],1],["LevelM45",[0.08,0.009],1],[],["LevelM45",[0.11,0.018],1],["LevelM45",[0.14,0.027],1],[],["LevelM45",[0.17,0.036],1],["LevelM45",[0.2,0.045],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_45,
                        "VALM_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": -45,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM45",[-0.18,-0.082],1],
                            "right": ["LevelM45",[-0.1,-0.082],1],
                            "down": ["LevelM45",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP45,
                        "LevelP45": {
                            "type": "line",
                            "points": [["LevelP45",[-0.2,0.03],1],["LevelP45",[-0.2,0],1],["LevelP45",[-0.05,0],1],[],["LevelP45",[0.05,0],1],["LevelP45",[0.2,0],1],["LevelP45",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_45,
                        "VALP_1_45": {
                            "type": "text",
                            "source": "static",
                            "text": "45",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP45",[-0.18,0.032],1],
                            "right": ["LevelP45",[-0.1,0.032],1],
                            "down": ["LevelP45",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM50,
                        "LevelM50": {
                            "type": "line",
                            "points": [["LevelM50",[-0.2,0.05],1],["LevelM50",[-0.17,0.04],1],[],["LevelM50",[-0.14,0.03],1],["LevelM50",[-0.11,0.02],1],[],["LevelM50",[-0.08,0.01],1],["LevelM50",[-0.05,0],1],["LevelM50",[-0.05,-0.03],1],[],["LevelM50",[0.05,-0.03],1],["LevelM50",[0.05,0],1],["LevelM50",[0.08,0.01],1],[],["LevelM50",[0.11,0.02],1],["LevelM50",[0.14,0.03],1],[],["LevelM50",[0.17,0.04],1],["LevelM50",[0.2,0.05],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_50,
                        "VALM_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": -50,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM50",[-0.18,-0.082],1],
                            "right": ["LevelM50",[-0.1,-0.082],1],
                            "down": ["LevelM50",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP50,
                        "LevelP50": {
                            "type": "line",
                            "points": [["LevelP50",[-0.2,0.03],1],["LevelP50",[-0.2,0],1],["LevelP50",[-0.05,0],1],[],["LevelP50",[0.05,0],1],["LevelP50",[0.2,0],1],["LevelP50",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_50,
                        "VALP_1_50": {
                            "type": "text",
                            "source": "static",
                            "text": "50",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP50",[-0.18,0.032],1],
                            "right": ["LevelP50",[-0.1,0.032],1],
                            "down": ["LevelP50",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM55,
                        "LevelM55": {
                            "type": "line",
                            "points": [["LevelM55",[-0.2,0.055],1],["LevelM55",[-0.17,0.044],1],[],["LevelM55",[-0.14,0.033],1],["LevelM55",[-0.11,0.022],1],[],["LevelM55",[-0.08,0.011],1],["LevelM55",[-0.05,0],1],["LevelM55",[-0.05,-0.03],1],[],["LevelM55",[0.05,-0.03],1],["LevelM55",[0.05,0],1],["LevelM55",[0.08,0.011],1],[],["LevelM55",[0.11,0.022],1],["LevelM55",[0.14,0.033],1],[],["LevelM55",[0.17,0.044],1],["LevelM55",[0.2,0.055],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_55,
                        "VALM_1_55": {
                            "type": "text",
                            "source": "static",
                            "text": -55,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM55",[-0.18,-0.082],1],
                            "right": ["LevelM55",[-0.1,-0.082],1],
                            "down": ["LevelM55",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP55,
                        "LevelP55": {
                            "type": "line",
                            "points": [["LevelP55",[-0.2,0.03],1],["LevelP55",[-0.2,0],1],["LevelP55",[-0.05,0],1],[],["LevelP55",[0.05,0],1],["LevelP55",[0.2,0],1],["LevelP55",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_55,
                        "VALP_1_55": {
                            "type": "text",
                            "source": "static",
                            "text": "55",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP55",[-0.18,0.032],1],
                            "right": ["LevelP55",[-0.1,0.032],1],
                            "down": ["LevelP55",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM60,
                        "LevelM60": {
                            "type": "line",
                            "points": [["LevelM60",[-0.2,0.06],1],["LevelM60",[-0.17,0.048],1],[],["LevelM60",[-0.14,0.036],1],["LevelM60",[-0.11,0.024],1],[],["LevelM60",[-0.08,0.012],1],["LevelM60",[-0.05,0],1],["LevelM60",[-0.05,-0.03],1],[],["LevelM60",[0.05,-0.03],1],["LevelM60",[0.05,0],1],["LevelM60",[0.08,0.012],1],[],["LevelM60",[0.11,0.024],1],["LevelM60",[0.14,0.036],1],[],["LevelM60",[0.17,0.048],1],["LevelM60",[0.2,0.06],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_60,
                        "VALM_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": -60,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM60",[-0.18,-0.082],1],
                            "right": ["LevelM60",[-0.1,-0.082],1],
                            "down": ["LevelM60",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP60,
                        "LevelP60": {
                            "type": "line",
                            "points": [["LevelP60",[-0.2,0.03],1],["LevelP60",[-0.2,0],1],["LevelP60",[-0.05,0],1],[],["LevelP60",[0.05,0],1],["LevelP60",[0.2,0],1],["LevelP60",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_60,
                        "VALP_1_60": {
                            "type": "text",
                            "source": "static",
                            "text": "60",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP60",[-0.18,0.032],1],
                            "right": ["LevelP60",[-0.1,0.032],1],
                            "down": ["LevelP60",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM65,
                        "LevelM65": {
                            "type": "line",
                            "points": [["LevelM65",[-0.2,0.065],1],["LevelM65",[-0.17,0.052],1],[],["LevelM65",[-0.14,0.039],1],["LevelM65",[-0.11,0.026],1],[],["LevelM65",[-0.08,0.013],1],["LevelM65",[-0.05,0],1],["LevelM65",[-0.05,-0.03],1],[],["LevelM65",[0.05,-0.03],1],["LevelM65",[0.05,0],1],["LevelM65",[0.08,0.013],1],[],["LevelM65",[0.11,0.026],1],["LevelM65",[0.14,0.039],1],[],["LevelM65",[0.17,0.052],1],["LevelM65",[0.2,0.065],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_65,
                        "VALM_1_65": {
                            "type": "text",
                            "source": "static",
                            "text": -65,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM65",[-0.18,-0.082],1],
                            "right": ["LevelM65",[-0.1,-0.082],1],
                            "down": ["LevelM65",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP65,
                        "LevelP65": {
                            "type": "line",
                            "points": [["LevelP65",[-0.2,0.03],1],["LevelP65",[-0.2,0],1],["LevelP65",[-0.05,0],1],[],["LevelP65",[0.05,0],1],["LevelP65",[0.2,0],1],["LevelP65",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_65,
                        "VALP_1_65": {
                            "type": "text",
                            "source": "static",
                            "text": "65",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP65",[-0.18,0.032],1],
                            "right": ["LevelP65",[-0.1,0.032],1],
                            "down": ["LevelP65",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM70,
                        "LevelM70": {
                            "type": "line",
                            "points": [["LevelM70",[-0.2,0.07],1],["LevelM70",[-0.17,0.056],1],[],["LevelM70",[-0.14,0.042],1],["LevelM70",[-0.11,0.028],1],[],["LevelM70",[-0.08,0.014],1],["LevelM70",[-0.05,0],1],["LevelM70",[-0.05,-0.03],1],[],["LevelM70",[0.05,-0.03],1],["LevelM70",[0.05,0],1],["LevelM70",[0.08,0.014],1],[],["LevelM70",[0.11,0.028],1],["LevelM70",[0.14,0.042],1],[],["LevelM70",[0.17,0.056],1],["LevelM70",[0.2,0.07],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_70,
                        "VALM_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": -70,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM70",[-0.18,-0.082],1],
                            "right": ["LevelM70",[-0.1,-0.082],1],
                            "down": ["LevelM70",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP70,
                        "LevelP70": {
                            "type": "line",
                            "points": [["LevelP70",[-0.2,0.03],1],["LevelP70",[-0.2,0],1],["LevelP70",[-0.05,0],1],[],["LevelP70",[0.05,0],1],["LevelP70",[0.2,0],1],["LevelP70",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_70,
                        "VALP_1_70": {
                            "type": "text",
                            "source": "static",
                            "text": "70",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP70",[-0.18,0.032],1],
                            "right": ["LevelP70",[-0.1,0.032],1],
                            "down": ["LevelP70",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM75,
                        "LevelM75": {
                            "type": "line",
                            "points": [["LevelM75",[-0.2,0.075],1],["LevelM75",[-0.17,0.06],1],[],["LevelM75",[-0.14,0.045],1],["LevelM75",[-0.11,0.03],1],[],["LevelM75",[-0.08,0.015],1],["LevelM75",[-0.05,0],1],["LevelM75",[-0.05,-0.03],1],[],["LevelM75",[0.05,-0.03],1],["LevelM75",[0.05,0],1],["LevelM75",[0.08,0.015],1],[],["LevelM75",[0.11,0.03],1],["LevelM75",[0.14,0.045],1],[],["LevelM75",[0.17,0.06],1],["LevelM75",[0.2,0.075],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_75,
                        "VALM_1_75": {
                            "type": "text",
                            "source": "static",
                            "text": -75,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM75",[-0.18,-0.082],1],
                            "right": ["LevelM75",[-0.1,-0.082],1],
                            "down": ["LevelM75",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP75,
                        "LevelP75": {
                            "type": "line",
                            "points": [["LevelP75",[-0.2,0.03],1],["LevelP75",[-0.2,0],1],["LevelP75",[-0.05,0],1],[],["LevelP75",[0.05,0],1],["LevelP75",[0.2,0],1],["LevelP75",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_75,
                        "VALP_1_75": {
                            "type": "text",
                            "source": "static",
                            "text": "75",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP75",[-0.18,0.032],1],
                            "right": ["LevelP75",[-0.1,0.032],1],
                            "down": ["LevelP75",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM80,
                        "LevelM80": {
                            "type": "line",
                            "points": [["LevelM80",[-0.2,0.08],1],["LevelM80",[-0.17,0.064],1],[],["LevelM80",[-0.14,0.048],1],["LevelM80",[-0.11,0.032],1],[],["LevelM80",[-0.08,0.016],1],["LevelM80",[-0.05,0],1],["LevelM80",[-0.05,-0.03],1],[],["LevelM80",[0.05,-0.03],1],["LevelM80",[0.05,0],1],["LevelM80",[0.08,0.016],1],[],["LevelM80",[0.11,0.032],1],["LevelM80",[0.14,0.048],1],[],["LevelM80",[0.17,0.064],1],["LevelM80",[0.2,0.08],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_80,
                        "VALM_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": -80,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM80",[-0.18,-0.082],1],
                            "right": ["LevelM80",[-0.1,-0.082],1],
                            "down": ["LevelM80",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP80,
                        "LevelP80": {
                            "type": "line",
                            "points": [["LevelP80",[-0.2,0.03],1],["LevelP80",[-0.2,0],1],["LevelP80",[-0.05,0],1],[],["LevelP80",[0.05,0],1],["LevelP80",[0.2,0],1],["LevelP80",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_80,
                        "VALP_1_80": {
                            "type": "text",
                            "source": "static",
                            "text": "80",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP80",[-0.18,0.032],1],
                            "right": ["LevelP80",[-0.1,0.032],1],
                            "down": ["LevelP80",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM85,
                        "LevelM85": {
                            "type": "line",
                            "points": [["LevelM85",[-0.2,0.085],1],["LevelM85",[-0.17,0.068],1],[],["LevelM85",[-0.14,0.051],1],["LevelM85",[-0.11,0.034],1],[],["LevelM85",[-0.08,0.017],1],["LevelM85",[-0.05,0],1],["LevelM85",[-0.05,-0.03],1],[],["LevelM85",[0.05,-0.03],1],["LevelM85",[0.05,0],1],["LevelM85",[0.08,0.017],1],[],["LevelM85",[0.11,0.034],1],["LevelM85",[0.14,0.051],1],[],["LevelM85",[0.17,0.068],1],["LevelM85",[0.2,0.085],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_85,
                        "VALM_1_85": {
                            "type": "text",
                            "source": "static",
                            "text": -85,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM85",[-0.18,-0.082],1],
                            "right": ["LevelM85",[-0.1,-0.082],1],
                            "down": ["LevelM85",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP85,
                        "LevelP85": {
                            "type": "line",
                            "points": [["LevelP85",[-0.2,0.03],1],["LevelP85",[-0.2,0],1],["LevelP85",[-0.05,0],1],[],["LevelP85",[0.05,0],1],["LevelP85",[0.2,0],1],["LevelP85",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_85,
                        "VALP_1_85": {
                            "type": "text",
                            "source": "static",
                            "text": "85",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP85",[-0.18,0.032],1],
                            "right": ["LevelP85",[-0.1,0.032],1],
                            "down": ["LevelP85",[-0.18,0.082],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelM90,
                        "LevelM90": {
                            "type": "line",
                            "points": [["LevelM90",[-0.2,0.09],1],["LevelM90",[-0.17,0.072],1],[],["LevelM90",[-0.14,0.054],1],["LevelM90",[-0.11,0.036],1],[],["LevelM90",[-0.08,0.018],1],["LevelM90",[-0.05,0],1],["LevelM90",[-0.05,-0.03],1],[],["LevelM90",[0.05,-0.03],1],["LevelM90",[0.05,0],1],["LevelM90",[0.08,0.018],1],[],["LevelM90",[0.11,0.036],1],["LevelM90",[0.14,0.054],1],[],["LevelM90",[0.17,0.072],1],["LevelM90",[0.2,0.09],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALM_1_90,
                        "VALM_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": -90,
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelM90",[-0.18,-0.082],1],
                            "right": ["LevelM90",[-0.1,-0.082],1],
                            "down": ["LevelM90",[-0.18,-0.032],1]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\LevelP90,
                        "LevelP90": {
                            "type": "line",
                            "points": [["LevelP90",[-0.2,0.03],1],["LevelP90",[-0.2,0],1],["LevelP90",[-0.05,0],1],[],["LevelP90",[0.05,0],1],["LevelP90",[0.2,0],1],["LevelP90",[0.2,0.03],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Horizont\Dimmed\VALP_1_90,
                        "VALP_1_90": {
                            "type": "text",
                            "source": "static",
                            "text": "90",
                            "align": "right",
                            "scale": 1,
                            "sourceScale": 1,
                            "pos": ["LevelP90",[-0.18,0.032],1],
                            "right": ["LevelP90",[-0.1,0.032],1],
                            "down": ["LevelP90",[-0.18,0.082],1]
                        }
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\SpeedNumber,
                "SpeedNumber": {
                    "type": "text",
                    "source": "speed",
                    "sourceScale": 3.6,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.1,0.309737],1],
                    "right": [[0.16,0.309737],1],
                    "down": [[0.1,0.366053],1]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\AltNumber,
                "AltNumber": {
                    "source": "altitudeASL",
                    "sourceScale": 1,
                    "pos": [[0.9,0.309737],1],
                    "right": [[0.96,0.309737],1],
                    "down": [[0.9,0.366053],1],
                    "type": "text",
                    "align": "center",
                    "scale": 1
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\AltNumberAGL,
                "AltNumberAGL": {
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\AltNumberAGL\Text
                    "Text": {
                        "type": "text",
                        "source": "static",
                        "text": "H",
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.8,0.535],1],
                        "right": [[0.86,0.535],1],
                        "down": [[0.8,0.591316],1]
                    },
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\AltNumberAGL\Box,
                    "Box": {
                        "type": "line",
                        "points": [[[0.81,0.591316],1],[[1,0.591316],1],[[1,0.535],1],[[0.81,0.535],1],[[0.81,0.591316],1]]
                    },
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\AltNumberAGL\AltNumber,
                    "AltNumber": {
                        "type": "text",
                        "source": "altitudeAGL",
                        "sourceScale": 1,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.99,0.535],1],
                        "right": [[1.05,0.535],1],
                        "down": [[0.99,0.591316],1]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Gear,
                "Gear": {
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Gear\Highlighted
                    "Highlighted": {
                        "condition": "ils",
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Gear\Highlighted\Text,
                        "Text": {
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
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Flaps,
                "Flaps": {
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Flaps\Highlighted
                    "Highlighted": {
                        "condition": "flaps",
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Flaps\Highlighted\Text,
                        "Text": {
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
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Lights,
                "Lights": {
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Lights\Highlighted
                    "Highlighted": {
                        "condition": "lights",
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Lights\Highlighted\Text,
                        "Text": {
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
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\CollisionLights,
                "CollisionLights": {
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\CollisionLights\Highlighted
                    "Highlighted": {
                        "condition": "collisionlights",
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\CollisionLights\Highlighted\Text,
                        "Text": {
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
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\RadarTargets,
                "RadarTargets": {
                    "condition": "1-ils",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\RadarTargets\RadarBoxes,
                    "RadarBoxes": {
                        "type": "radar",
                        "pos0": [0.4975,0.383],
                        "pos10": [1.4475,1.453],
                        "width": 4,
                        "points": [[[-0.02,-0.0225263],1],[[0.02,-0.0225263],1],[[0.02,0.0225263],1],[[-0.02,0.0225263],1],[[-0.02,-0.0225263],1]]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\TargetDiamond,
                "TargetDiamond": {
                    "condition": "1-ils",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\TargetDiamond\shape,
                    "shape": {
                        "type": "line",
                        "width": 4,
                        "points": [["Target",1,"Limit0109",1,[0,-0.0337895],1],["Target",1,"Limit0109",1,[0.03,0],1],["Target",1,"Limit0109",1,[0,0.0337895],1],["Target",1,"Limit0109",1,[-0.03,0],1],["Target",1,"Limit0109",1,[0,-0.0337895],1]]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\TargetingPodGroup,
                "TargetingPodGroup": {
                    "condition": "1-pilotcameralock",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\TargetingPodGroup\TargetingPodDir,
                    "TargetingPodDir": {
                        "type": "line",
                        "width": 3,
                        "points": [["TargetingPodDir",1,[0,-0.0450526],1],["TargetingPodDir",1,[0,-0.0394211],1],[],["TargetingPodDir",1,[0,-0.0337895],1],["TargetingPodDir",1,[0,-0.0281579],1],[],["TargetingPodDir",1,[0,-0.0225263],1],["TargetingPodDir",1,[0,-0.0168947],1],[],["TargetingPodDir",1,[0,-0.0112632],1],["TargetingPodDir",1,[0,-0.00563158],1],[],["TargetingPodDir",1,[0,0.0450526],1],["TargetingPodDir",1,[0,0.0394211],1],[],["TargetingPodDir",1,[0,0.0337895],1],["TargetingPodDir",1,[0,0.0281579],1],[],["TargetingPodDir",1,[0,0.0225263],1],["TargetingPodDir",1,[0,0.0168947],1],[],["TargetingPodDir",1,[0,0.0112632],1],["TargetingPodDir",1,[0,0.00563158],1],[],["TargetingPodDir",1,[-0.04,0],1],["TargetingPodDir",1,[-0.035,0],1],[],["TargetingPodDir",1,[-0.03,0],1],["TargetingPodDir",1,[-0.025,0],1],[],["TargetingPodDir",1,[-0.02,0],1],["TargetingPodDir",1,[-0.015,0],1],[],["TargetingPodDir",1,[-0.01,0],1],["TargetingPodDir",1,[-0.005,0],1],[],["TargetingPodDir",1,[0.04,0],1],["TargetingPodDir",1,[0.035,0],1],[],["TargetingPodDir",1,[0.03,0],1],["TargetingPodDir",1,[0.025,0],1],[],["TargetingPodDir",1,[0.02,0],1],["TargetingPodDir",1,[0.015,0],1],[],["TargetingPodDir",1,[0.01,0],1],["TargetingPodDir",1,[0.005,0],1],[]]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\TargetingPodGroupOn,
                "TargetingPodGroupOn": {
                    "condition": "pilotcameralock",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\TargetingPodGroupOn\TargetingPodDir,
                    "TargetingPodDir": {
                        "type": "line",
                        "width": 3,
                        "points": [["TargetingPodTarget",1,"Limit0109",1,[0,-0.0450526],1],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0394211],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0337895],1],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0281579],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0225263],1],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0168947],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,-0.0112632],1],["TargetingPodTarget",1,"Limit0109",1,[0,-0.00563158],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,0.0450526],1],["TargetingPodTarget",1,"Limit0109",1,[0,0.0394211],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,0.0337895],1],["TargetingPodTarget",1,"Limit0109",1,[0,0.0281579],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,0.0225263],1],["TargetingPodTarget",1,"Limit0109",1,[0,0.0168947],1],[],["TargetingPodTarget",1,"Limit0109",1,[0,0.0112632],1],["TargetingPodTarget",1,"Limit0109",1,[0,0.00563158],1],[],["TargetingPodTarget",1,"Limit0109",1,[-0.04,0],1],["TargetingPodTarget",1,"Limit0109",1,[-0.035,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[-0.03,0],1],["TargetingPodTarget",1,"Limit0109",1,[-0.025,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[-0.02,0],1],["TargetingPodTarget",1,"Limit0109",1,[-0.015,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[-0.01,0],1],["TargetingPodTarget",1,"Limit0109",1,[-0.005,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[0.04,0],1],["TargetingPodTarget",1,"Limit0109",1,[0.035,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[0.03,0],1],["TargetingPodTarget",1,"Limit0109",1,[0.025,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[0.02,0],1],["TargetingPodTarget",1,"Limit0109",1,[0.015,0],1],[],["TargetingPodTarget",1,"Limit0109",1,[0.01,0],1],["TargetingPodTarget",1,"Limit0109",1,[0.005,0],1],[]]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Stall,
                "Stall": {
                    "condition": "stall",
                    "color": [1,0,0],
                    "blinkingPattern": [0.2,0.2],
                    "blinkingStartsOn": 1,
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Stall\Text,
                    "Text": {
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
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\IncomingMissile,
                "IncomingMissile": {
                    "condition": "incomingmissile",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\IncomingMissile\Text,
                    "Text": {
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
                    "blinkingPattern": [0.2,0.2],
                    "blinkingStartsOn": 1
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Ammo,
                "Ammo": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.5,0.816579],1],
                    "right": [[0.56,0.816579],1],
                    "down": [[0.5,0.872895],1]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Weapons,
                "Weapons": {
                    "type": "text",
                    "source": "weapon",
                    "sourceScale": 1,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.5,0.872895],1],
                    "right": [[0.56,0.872895],1],
                    "down": [[0.5,0.92921],1]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\WeaponsLocking,
                "WeaponsLocking": {
                    "condition": "missilelocking",
                    "blinkingPattern": [0.2,0.2],
                    "blinkingStartsOn": 1,
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\WeaponsLocking\Text,
                    "Text": {
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
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\WeaponsLocked,
                "WeaponsLocked": {
                    "condition": "missilelocked",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\WeaponsLocked\Text,
                    "Text": {
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
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\WP,
                "WP": {
                    "condition": "wpvalid",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\WP\WPdist,
                    "WPdist": {
                        "type": "text",
                        "source": "wpdist",
                        "sourceScale": 0.01,
                        "align": "left",
                        "scale": 1,
                        "pos": [[0.945,0.703947],1],
                        "right": [[1.005,0.703947],1],
                        "down": [[0.945,0.760263],1]
                    },
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\WP\WPstatic,
                    "WPstatic": {
                        "type": "text",
                        "source": "static",
                        "text": ">",
                        "align": "center",
                        "scale": 2,
                        "pos": [[0.96,0.703947],1],
                        "right": [[0.98,0.703947],1],
                        "down": [[0.96,0.760263],1]
                    },
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\WP\WPIndex,
                    "WPIndex": {
                        "type": "text",
                        "source": "wpIndex",
                        "sourceScale": 1,
                        "align": "right",
                        "scale": 1,
                        "pos": [[0.97,0.703947],1],
                        "right": [[1.03,0.703947],1],
                        "down": [[0.97,0.760263],1]
                    },
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\WP\WP,
                    "WP": {
                        "type": "line",
                        "points": [["wppoint",1,"Limit0109",1,["HorizonBankRotFull",0.015,-0.035],1],["wppoint",1,"Limit0109",1,["HorizonBankRotFull",0,0],1],["wppoint",1,"Limit0109",1,["HorizonBankRotFull",-0.015,-0.035],1]]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\HeadingScale,
                "HeadingScale": {
                    "type": "scale",
                    "horizontal": 1,
                    "source": "Heading",
                    "sourceScale": 0.1,
                    "top": 0.2,
                    "center": 0.5,
                    "bottom": 0.8,
                    "lineXleft": 0.101368,
                    "lineYright": 0.0901053,
                    "lineXleftMajor": 0.101368,
                    "lineYrightMajor": 0.0788421,
                    "majorLineEach": 5,
                    "numberEach": 5,
                    "step": 0.2,
                    "StepSize": 0.03,
                    "align": "center",
                    "scale": 1,
                    "pos": [0.2,0.0197105],
                    "right": [0.26,0.0197105],
                    "down": [0.2,0.0760263]
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\ILS,
                "ILS": {
                    "condition": "ils",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\ILS\Glideslope,
                    "Glideslope": {
                        "clipTL": [0,0],
                        "clipBR": [1,1],
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\ILS\Glideslope\ILS,
                        "ILS": {
                            "type": "line",
                            "points": [["ILS_W",[-0.24,0],1],["ILS_W",[0.24,0],1],[],["ILS_W",[-0.24,-0.0270316],1],["ILS_W",[-0.24,0.0270316],1],[],["ILS_W",[-0.12,-0.0202737],1],["ILS_W",[-0.12,0.0202737],1],[],["ILS_W",[0,-0.0270316],1],["ILS_W",[0,0.0270316],1],[],["ILS_W",[0.12,-0.0202737],1],["ILS_W",[0.12,0.0202737],1],[],["ILS_W",[0.24,-0.0270316],1],["ILS_W",[0.24,0.0270316],1],[],["ILS_H",[0,-0.270316],1],["ILS_H",[0,0.270316],1],[],["ILS_H",[-0.024,-0.270316],1],["ILS_H",[0.024,-0.270316],1],[],["ILS_H",[-0.018,-0.135158],1],["ILS_H",[0.018,-0.135158],1],[],["ILS_H",[-0.024,0],1],["ILS_H",[0.024,0],1],[],["ILS_H",[-0.018,0.135158],1],["ILS_H",[0.018,0.135158],1],[],["ILS_H",[-0.024,0.270316],1],["ILS_H",[0.024,0.270316],1]]
                        },
                        # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\ILS\Glideslope\airport,
                        "airport": {
                            "type": "line",
                            "points": [["airport1",1],["airport2",1],["airport4",1],["airport3",1],["airport1",1]]
                        }
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Bomb,
                "Bomb": {
                    "condition": "bomb",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\Bomb\Circle,
                    "Circle": {
                        "type": "line",
                        "points": [["ImpactPoint",[0,-0.112632],1],["ImpactPoint",[0.01736,-0.11092],1],["ImpactPoint",[0.0342,-0.10584],1],["ImpactPoint",[0.05,-0.0975389],1],["ImpactPoint",[0.06428,-0.0862758],1],["ImpactPoint",[0.0766,-0.0723996],1],["ImpactPoint",[0.0866,-0.0563158],1],["ImpactPoint",[0.09397,-0.03852],1],["ImpactPoint",[0.09848,-0.0195528],1],["ImpactPoint",[0.1,0],1],["ImpactPoint",[0.09848,0.0195528],1],["ImpactPoint",[0.09397,0.03852],1],["ImpactPoint",[0.0866,0.0563158],1],["ImpactPoint",[0.0766,0.0723996],1],["ImpactPoint",[0.06428,0.0862758],1],["ImpactPoint",[0.05,0.0975389],1],["ImpactPoint",[0.0342,0.10584],1],["ImpactPoint",[0.01736,0.11092],1],["ImpactPoint",[0,0.112632],1],["ImpactPoint",[-0.01736,0.11092],1],["ImpactPoint",[-0.0342,0.10584],1],["ImpactPoint",[-0.05,0.0975389],1],["ImpactPoint",[-0.06428,0.0862758],1],["ImpactPoint",[-0.0766,0.0723996],1],["ImpactPoint",[-0.0866,0.0563158],1],["ImpactPoint",[-0.09397,0.03852],1],["ImpactPoint",[-0.09848,0.0195528],1],["ImpactPoint",[-0.1,0],1],["ImpactPoint",[-0.09848,-0.0195528],1],["ImpactPoint",[-0.09397,-0.03852],1],["ImpactPoint",[-0.0866,-0.0563158],1],["ImpactPoint",[-0.0766,-0.0723996],1],["ImpactPoint",[-0.06428,-0.0862758],1],["ImpactPoint",[-0.05,-0.0975389],1],["ImpactPoint",[-0.0342,-0.10584],1],["ImpactPoint",[-0.01736,-0.11092],1],["ImpactPoint",[0,-0.112632],1],[],["ImpactPoint",1,"Limit0109",1,[0,-0.0225263],1],["ImpactPoint",1,"Limit0109",1,[0.014,-0.0157684],1],["ImpactPoint",1,"Limit0109",1,["+ 0.02",0],1],["ImpactPoint",1,"Limit0109",1,[0.014,0.0157684],1],["ImpactPoint",1,"Limit0109",1,[0,0.0225263],1],["ImpactPoint",1,"Limit0109",1,[-0.014,0.0157684],1],["ImpactPoint",1,"Limit0109",1,["- 0.02",0],1],["ImpactPoint",1,"Limit0109",1,[-0.014,-0.0157684],1],["ImpactPoint",1,"Limit0109",1,[0,-0.0225263],1],[],["Velocity",0.001,"ImpactPoint",1,"Limit0109",1,[0,0],1],["Velocity",1,"Limit0109",1,[0,0],1]]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\MGun,
                "MGun": {
                    "condition": "mgun",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\MGun\Ball,
                    "Ball": {
                        "type": "polygon",
                        "width": 4,
                        "points": [[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.00156283,-0.00998284],1],["ImpactPoint",[0.00307818,-0.00952552],1],["ImpactPoint",[0.0045,-0.00877876],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.0045,-0.00877876],1],["ImpactPoint",[0.00578509,-0.00776527],1],["ImpactPoint",[0.0068944,-0.00651584],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.0068944,-0.00651584],1],["ImpactPoint",[0.00779423,-0.00506842],1],["ImpactPoint",[0.00845723,-0.003467],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.00845723,-0.003467],1],["ImpactPoint",[0.00886327,-0.00176024],1],["ImpactPoint",[0.009,4.43095e-010],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.009,4.43095e-010],1],["ImpactPoint",[0.00886327,0.00176024],1],["ImpactPoint",[0.00845723,0.003467],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.00845723,0.003467],1],["ImpactPoint",[0.00779423,0.00506842],1],["ImpactPoint",[0.0068944,0.00651584],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.0068944,0.00651584],1],["ImpactPoint",[0.00578509,0.00776527],1],["ImpactPoint",[0.0045,0.00877876],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.0045,0.00877876],1],["ImpactPoint",[0.00307818,0.00952552],1],["ImpactPoint",[0.00156283,0.00998284],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[0.00156283,0.00998284],1],["ImpactPoint",[-7.86805e-010,0.0101368],1],["ImpactPoint",[-0.00156284,0.00998284],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.00156284,0.00998284],1],["ImpactPoint",[-0.00307818,0.00952552],1],["ImpactPoint",[-0.0045,0.00877876],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.0045,0.00877876],1],["ImpactPoint",[-0.00578509,0.00776527],1],["ImpactPoint",[-0.0068944,0.00651583],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.0068944,0.00651583],1],["ImpactPoint",[-0.00779423,0.00506842],1],["ImpactPoint",[-0.00845723,0.003467],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.00845723,0.003467],1],["ImpactPoint",[-0.00886327,0.00176024],1],["ImpactPoint",[-0.009,-1.20881e-010],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.009,-1.20881e-010],1],["ImpactPoint",[-0.00886327,-0.00176025],1],["ImpactPoint",[-0.00845723,-0.003467],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.00845723,-0.003467],1],["ImpactPoint",[-0.00779423,-0.00506842],1],["ImpactPoint",[-0.0068944,-0.00651583],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.0068944,-0.00651583],1],["ImpactPoint",[-0.00578509,-0.00776527],1],["ImpactPoint",[-0.0045,-0.00877876],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.0045,-0.00877876],1],["ImpactPoint",[-0.00307818,-0.00952551],1],["ImpactPoint",[-0.00156283,-0.00998284],1]],[["ImpactPoint",1,[0,0],1],["ImpactPoint",[-0.00156283,-0.00998284],1],["ImpactPoint",[1.57361e-009,-0.0101368],1],["ImpactPoint",[0.00156283,-0.00998284],1]],[["ImpactPoint",[0,0.0394211],1],["ImpactPoint",[-0.00435779,0.0561015],1],["ImpactPoint",[0,0.0732105],1],["ImpactPoint",[0.00435779,0.0561015],1]],[["ImpactPoint",[0.0247487,0.0278749],1],["ImpactPoint",[0.0321394,0.0431404],1],["ImpactPoint",[0.0459619,0.0517677],1],["ImpactPoint",[0.0383022,0.0361991],1]],[["ImpactPoint",[0.035,-1.72315e-009],1],["ImpactPoint",[0.0498097,0.00490825],1],["ImpactPoint",[0.065,-3.20013e-009],1],["ImpactPoint",[0.0498097,-0.00490825],1]],[["ImpactPoint",[0.0247487,-0.0278749],1],["ImpactPoint",[0.0383022,-0.0361991],1],["ImpactPoint",[0.0459619,-0.0517677],1],["ImpactPoint",[0.0321394,-0.0431404],1]],[["ImpactPoint",[-3.0598e-009,-0.0394211],1],["ImpactPoint",[0.00435778,-0.0561015],1],["ImpactPoint",[-5.68248e-009,-0.0732105],1],["ImpactPoint",[-0.00435779,-0.0561015],1]],[["ImpactPoint",[-0.0247487,-0.0278749],1],["ImpactPoint",[-0.0321394,-0.0431404],1],["ImpactPoint",[-0.0459619,-0.0517677],1],["ImpactPoint",[-0.0383022,-0.0361991],1]],[["ImpactPoint",[-0.035,4.70091e-010],1],["ImpactPoint",[-0.0498097,-0.00490824],1],["ImpactPoint",[-0.065,8.73027e-010],1],["ImpactPoint",[-0.0498097,0.00490824],1]],[["ImpactPoint",[-0.0247487,0.0278749],1],["ImpactPoint",[-0.0383022,0.0361991],1],["ImpactPoint",[-0.0459619,0.0517676],1],["ImpactPoint",[-0.0321394,0.0431404],1]]]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\AAMissile,
                "AAMissile": {
                    "condition": "AAmissile",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\AAMissile\Circle,
                    "Circle": {
                        "type": "line",
                        "points": [["center",[0,-0.225263],1],["center",[0.03472,-0.221839],1],["center",[0.0684,-0.21168],1],["center",[0.1,-0.195078],1],["center",[0.12856,-0.172552],1],["center",[0.1532,-0.144799],1],["center",[0.1732,-0.112632],1],["center",[0.18794,-0.07704],1],["center",[0.19696,-0.0391057],1],["center",[0.2,0],1],["center",[0.19696,0.0391057],1],["center",[0.18794,0.07704],1],["center",[0.1732,0.112632],1],["center",[0.1532,0.144799],1],["center",[0.12856,0.172552],1],["center",[0.1,0.195078],1],["center",[0.0684,0.21168],1],["center",[0.03472,0.221839],1],["center",[0,0.225263],1],["center",[-0.03472,0.221839],1],["center",[-0.0684,0.21168],1],["center",[-0.1,0.195078],1],["center",[-0.12856,0.172552],1],["center",[-0.1532,0.144799],1],["center",[-0.1732,0.112632],1],["center",[-0.18794,0.07704],1],["center",[-0.19696,0.0391057],1],["center",[-0.2,0],1],["center",[-0.19696,-0.0391057],1],["center",[-0.18794,-0.07704],1],["center",[-0.1732,-0.112632],1],["center",[-0.1532,-0.144799],1],["center",[-0.12856,-0.172552],1],["center",[-0.1,-0.195078],1],["center",[-0.0684,-0.21168],1],["center",[-0.03472,-0.221839],1],["center",[0,-0.225263],1]]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\ATMissile,
                "ATMissile": {
                    "condition": "ATmissile",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\ATMissile\Circle,
                    "Circle": {
                        "type": "line",
                        "points": [["center",[0,-0.180211],1],["center",[0.027776,-0.177471],1],["center",[0.05472,-0.169344],1],["center",[0.08,-0.156062],1],["center",[0.102848,-0.138041],1],["center",[0.12256,-0.115839],1],["center",[0.13856,-0.0901053],1],["center",[0.150352,-0.061632],1],["center",[0.157568,-0.0312845],1],["center",[0.16,0],1],["center",[0.157568,0.0312845],1],["center",[0.150352,0.061632],1],["center",[0.13856,0.0901053],1],["center",[0.12256,0.115839],1],["center",[0.102848,0.138041],1],["center",[0.08,0.156062],1],["center",[0.05472,0.169344],1],["center",[0.027776,0.177471],1],["center",[0,0.180211],1],["center",[-0.027776,0.177471],1],["center",[-0.05472,0.169344],1],["center",[-0.08,0.156062],1],["center",[-0.102848,0.138041],1],["center",[-0.12256,0.115839],1],["center",[-0.13856,0.0901053],1],["center",[-0.150352,0.061632],1],["center",[-0.157568,0.0312845],1],["center",[-0.16,0],1],["center",[-0.157568,-0.0312845],1],["center",[-0.150352,-0.061632],1],["center",[-0.13856,-0.0901053],1],["center",[-0.12256,-0.115839],1],["center",[-0.102848,-0.138041],1],["center",[-0.08,-0.156062],1],["center",[-0.05472,-0.169344],1],["center",[-0.027776,-0.177471],1],["center",[0,-0.180211],1]]
                    },
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\ATMissile\Time,
                    "Time": {
                        "type": "line",
                        "width": 4,
                        "points": [["center",[0,-0.135158],1],["center",[0,-0.168947],1],["MissileFlightTimeRot1",[0,0.15],1,"center",1],["MissileFlightTimeRot2",[0,0.15],1,"center",1],["MissileFlightTimeRot3",[0,0.15],1,"center",1],["MissileFlightTimeRot4",[0,0.15],1,"center",1],["MissileFlightTimeRot5",[0,0.15],1,"center",1],["MissileFlightTimeRot6",[0,0.15],1,"center",1],["MissileFlightTimeRot7",[0,0.15],1,"center",1],["MissileFlightTimeRot8",[0,0.15],1,"center",1],["MissileFlightTimeRot9",[0,0.15],1,"center",1],["MissileFlightTimeRot10",[0,0.15],1,"center",1],["MissileFlightTimeRot11",[0,0.15],1,"center",1],["MissileFlightTimeRot12",[0,0.15],1,"center",1],["MissileFlightTimeRot13",[0,0.15],1,"center",1],["MissileFlightTimeRot14",[0,0.15],1,"center",1],["MissileFlightTimeRot15",[0,0.15],1,"center",1],["MissileFlightTimeRot16",[0,0.15],1,"center",1],["MissileFlightTimeRot17",[0,0.15],1,"center",1],["MissileFlightTimeRot17",[0,0.12],1,"center",1]]
                    }
                },
                # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\RocketCrosshair,
                "RocketCrosshair": {
                    "type": "group",
                    "condition": "Rocket",
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\RocketCrosshair\BombCrosshair,
                    "BombCrosshair": {
                        "type": "line",
                        "width": 4,
                        "points": [["Velocity",0.001,"ImpactPoint",1,"Limit0109",1,[0,0],1],["Velocity",1,"Limit0109",1,[0,0],1],[],["ImpactPoint",[0,-0.118263],1],["ImpactPoint",[0.018228,-0.116466],1],["ImpactPoint",[0.03591,-0.111132],1],["ImpactPoint",[0.0525,-0.102416],1],["ImpactPoint",[0.067494,-0.0905896],1],["ImpactPoint",[0.08043,-0.0760195],1],["ImpactPoint",[0.09093,-0.0591316],1],["ImpactPoint",[0.0986685,-0.040446],1],["ImpactPoint",[0.103404,-0.0205305],1],["ImpactPoint",[0.105,0],1],["ImpactPoint",[0.103404,0.0205305],1],["ImpactPoint",[0.0986685,0.040446],1],["ImpactPoint",[0.09093,0.0591316],1],["ImpactPoint",[0.08043,0.0760195],1],["ImpactPoint",[0.067494,0.0905896],1],["ImpactPoint",[0.0525,0.102416],1],["ImpactPoint",[0.03591,0.111132],1],["ImpactPoint",[0.018228,0.116466],1],["ImpactPoint",[0,0.118263],1],["ImpactPoint",[-0.018228,0.116466],1],["ImpactPoint",[-0.03591,0.111132],1],["ImpactPoint",[-0.0525,0.102416],1],["ImpactPoint",[-0.067494,0.0905896],1],["ImpactPoint",[-0.08043,0.0760195],1],["ImpactPoint",[-0.09093,0.0591316],1],["ImpactPoint",[-0.0986685,0.040446],1],["ImpactPoint",[-0.103404,0.0205305],1],["ImpactPoint",[-0.105,0],1],["ImpactPoint",[-0.103404,-0.0205305],1],["ImpactPoint",[-0.0986685,-0.040446],1],["ImpactPoint",[-0.09093,-0.0591316],1],["ImpactPoint",[-0.08043,-0.0760195],1],["ImpactPoint",[-0.067494,-0.0905896],1],["ImpactPoint",[-0.0525,-0.102416],1],["ImpactPoint",[-0.03591,-0.111132],1],["ImpactPoint",[-0.018228,-0.116466],1],["ImpactPoint",[0,-0.118263],1]]
                    },
                    # Class: CfgVehicles\Plane_Fighter_03_base_F\MFD\AirplaneHUD\Draw\RocketCrosshair\Time,
                    "Time": {
                        "type": "line",
                        "width": 6,
                        "points": [["ImpactPoint",[0,-0.0901053],1],["ImpactPoint",[0,-0.112632],1],["MissileFlightTimeRot1",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot2",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot3",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot4",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot5",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot6",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot7",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot8",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot9",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot10",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot11",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot12",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot13",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot14",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot15",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot16",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.1],1,"ImpactPoint",1],["MissileFlightTimeRot17",[0,0.08],1,"ImpactPoint",1]]
                    }
                }
            }
        }
    },
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
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
    # Class: CfgVehicles\Plane_Base_F\TransportBackpacks,
    "TransportBackpacks": {
    },
    # Class: CfgVehicles\Plane_Base_F\TransportMagazines,
    "TransportMagazines": {
    },
    # Class: CfgVehicles\Plane_Base_F\TransportWeapons,
    "TransportWeapons": {
    },
    # Class: CfgVehicles\Plane_Base_F\camShakeGForce,
    "camShakeGForce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minSpeed": 1
    },
    "minGForce": 0.3,
    "maxGForce": 3,
    "gForceShakeAttenuation": 0.5,
    # Class: CfgVehicles\Plane_Base_F\NewTurret,
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
    "formationX": 200,
    "formationZ": 300,
    "precision": 200,
    "brakeDistance": 500,
    "steerAheadSimul": 1,
    "steerAheadPlan": 2,
    "gearRetracting": 1,
    "cabinOpening": 1,
    "durationGetIn": 0.99,
    "durationGetOut": 0.99,
    "vtol": 0,
    "tailHook": 0,
    "lightOnGear": 1,
    "gearUpTime": 3.33,
    "gearDownTime": 2,
    "ejectDamageLimit": 0.45,
    "simulation": "airplanex",
    "minGunElev": 0,
    "maxGunElev": 0,
    "minGunTurn": 0,
    "maxGunTurn": 0,
    "VTOLYawInfluence": 2,
    "VTOLPitchInfluence": 2,
    "VTOLRollInfluence": 2,
    # Class: CfgVehicles\Plane\ViewOptics,
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
    "memoryPointLDust": "levy prach",
    "memoryPointRDust": "pravy prach",
    "selectionFireAnim": "zasleh",
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "dustEffect": "HeliDust",
    "waterEffect": "HeliWater",
    # Class: CfgVehicles\Plane\GunFire,
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
    # Class: CfgVehicles\Plane\GunClouds,
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
    # Class: CfgVehicles\Plane\MGunFire,
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
    # Class: CfgVehicles\Plane\MGunClouds,
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
    "numberPhysicalWheels": 3,
    # Class: CfgVehicles\Plane\SpeechVariants,
    "SpeechVariants": {
        # Class: CfgVehicles\Plane\SpeechVariants\Default
        "Default": {
            "speechSingular": ["veh_air_plane_s"],
            "speechPlural": ["veh_air_plane_p"]
        }
    },
    "textSingular": "fast mover",
    "textPlural": "fast movers",
    "nameSound": "veh_air_plane_s",
    "type": 2,
    "memoryPointGun": "kulomet",
    "fuelExplosionPower": 10,
    "crewCrashProtection": 0.15,
    "damageEffect": "AirDestructionEffects",
    "getInAction": "GetInHigh",
    "getOutAction": "GetOutHigh",
    "cargoGetInAction": ["GetInHigh"],
    "cargoGetOutAction": ["GetOutHigh"],
    "gunnerGetInAction": "GetInHigh",
    "gunnerGetOutAction": "GetOutHigh",
    "getInRadius": 1.2,
    "camouflage": 100,
    "audible": 60,
    # Class: CfgVehicles\Plane\CamShake,
    "CamShake": {
        "power": 50,
        "frequency": 20,
        "distance": 50,
        "minSpeed": 200
    },
    "camShakeCoef": 0,
    "headGforceLeaningFactor": [0.005,0.001,0.025],
    "explosionShielding": 2,
    # Class: CfgVehicles\Plane\DestructionEffects,
    "DestructionEffects": {
    },
    "formationTime": 10,
    "fuelCapacity": 1000,
    "insideSoundCoef": 0.0316228,
    "outsideSoundFilter": 1,
    "occludeSoundsWhenIn": 0.316228,
    "obstructSoundsWhenIn": 0.316228,
    "nightVision": 0,
    "driverCompartments": 0,
    "cargoCompartments": [0],
    "enableGPS": 1,
    "weaponsGroup1": "1 + 		2",
    "weaponsGroup2": 4,
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffectsAir"],["GdtKLGrass1","RDustEffectsAir"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffectsAir"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffectsAir"],["GdtKLForestDec","RDustEffectsAir"],["GdtKlMud","RDustEffectsAir"],["GdtKlSoil","RDustEffectsAir"],["GdtKlTarmac","RDustEffectsAir"],["GdtKlStubble","RDustEffectsAir"],["GdtKlStones","RDustEffectsAir"],["SurfRoadDirt_Enoch","RDustEffectsAir"],["SurfTrailDirt_Enoch","RDustEffectsAir"],["SurfRoadTarmac1_Enoch","RDustEffectsAir"],["SurfRoadTarmac2_Enoch","RDustEffectsAir"],["SurfRoadTarmac3_Enoch","RDustEffectsAir"],["GdtGrassShort","RDustEffectsAir"],["GdtGrassShort","RGrassEffects"],["GdtGrassTall","RDustEffectsAir"],["GdtGrassTall","RGrassEffects"],["GdtRedDirt","RDustEffectsAirRed"],["GdtField","RDustEffectsAir"],["GdtForest","RDustEffectsAir"],["GdtVolcano","RDustEffectsAir"],["GdtVolcano","RStonesEffects"],["GdtCliff","RDustEffectsAir"],["GdtVolcanoBeach","RDustEffectsAir"],["SurfRoadDirt_exp","RDustEffectsAirRed"],["SurfRoadConcrete_exp","RDustEffectsAir"],["SurfRoadTarmac_exp","RDustEffectsAir"],["GdtStratisConcrete","RDustEffectsAir"],["GdtStratisConcrete","RDirtEffects"],["GdtStratisBeach","RDustEffectsAir"],["GdtStratisBeach","RStonesEffects"],["GdtStratisDirt","RDustEffectsAir"],["GdtStratisDirt","RDirtEffects"],["GdtStratisSeabedCluttered","RDustEffectsAir"],["GdtStratisSeabed","RDustEffectsAir"],["GdtStratisDryGrass","RDustEffectsAir"],["GdtStratisDryGrass","RGrassDryEffects"],["GdtStratisDryGrass","RDirtEffects"],["GdtStratisGreenGrass","RDustEffectsAir"],["GdtStratisGreenGrass","RGrassEffects"],["GdtStratisGreenGrass","RDirtEffects"],["GdtStratisRocky","RDustEffectsAir"],["GdtStratisRocky","RGrassEffects"],["GdtStratisRocky","RDirtEffects"],["GdtStratisThistles","RDustEffectsAir"],["GdtStratisThistles","RGrassEffects"],["GdtStratisThistles","RDirtEffects"],["GdtConcrete","RDustEffectsAir"],["GdtConcrete","RDirtEffects"],["GdtAsphalt","RDustEffectsAir"],["GdtAsphalt","RDirtEffects"],["GdtRubble","RDustEffectsAir"],["GdtRubble","RDirtEffects"],["GdtSoil","RDustEffectsAir"],["GdtSoil","RDirtEffects"],["GdtBeach","RDustEffectsAir"],["GdtBeach","RStonesEffects"],["GdtRock","RDustEffectsAir"],["GdtRock","RDirtEffects"],["GdtDead","RDustEffectsAir"],["GdtDead","RDirtEffects"],["Default","RDustEffectsAir"],["GdtDesert1","RDustEffectsAir"],["GdtDesert1","RSandEffects"],["GdtDesert1","RDirtEffects"],["GdtDesert1","RStonesEffects"],["GdtDesert2","RDustEffectsAir"],["GdtDesert2","RSandEffects"],["GdtDesert2","RGrassEffects"],["GdtDesert2","RDirtEffects"],["GdtDirt","RDustEffectsAir"],["GdtDirt","RDirtEffects"],["GdtGrassGreen","RDustEffectsAir"],["GdtGrassGreen","RGrassEffects"],["GdtGrassGreen","RDirtEffects"],["GdtGrassDry","RDustEffectsAir"],["GdtGrassDry","RGrassDryEffects"],["GdtGrassDry","RDirtEffects"],["GdtGrassWild","RDustEffectsAir"],["GdtGrassWild","RGrassEffects"],["GdtGrassWild","RDirtEffects"],["GdtWildField","RDustEffectsAir"],["GdtWildField","RGrassEffects"],["GdtWildField","RDirtEffects"],["GdtWeed1","RDustEffectsAir"],["GdtWeed1","RGrassEffects"],["GdtWeed1","RDirtEffects"],["GdtWeed2","RDustEffectsAir"],["GdtWeed2","RGrassEffects"],["GdtWeed2","RDirtEffects"],["GdtThorn","RDustEffectsAir"],["GdtThorn","RGrassEffects"],["GdtThorn","RDirtEffects"],["GdtStony","RDustEffectsAir"],["GdtStony","RGrassEffects"],["GdtStony","RDirtEffects"],["GdtStonyGreen","RDustEffectsAir"],["GdtStonyGreen","RGrassEffects"],["GdtStonyGreen","RDirtEffects"],["GdtStonyThistle","RDustEffectsAir"],["GdtStonyThistle","RGrassEffects"],["GdtStonyThistle","RDirtEffects"],["GdtSeabedDeep","RDustEffectsAir"],["GdtSeabed","RDustEffectsAir"],["SurfRoadDirt","RDustEffectsAir"],["SurfRoadConcrete","RDustEffectsAir"],["SurfRoadTarmac","RDustEffectsAir"],["SurfWood","RDustEffectsAir"],["SurfMetal","RDustEffectsAir"],["SurfRoofTin","RDustEffectsAir"],["SurfRoofTiles","RDustEffectsAir"],["SurfIntWood","RDustEffectsAir"],["SurfIntConcrete","RDustEffectsAir"],["SurfIntTiles","RDustEffectsAir"],["SurfIntMetal","RDustEffectsAir"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffectsAir"],["GdtKLGrass1","LDustEffectsAir"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffectsAir"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffectsAir"],["GdtKLForestDec","LDustEffectsAir"],["GdtKlMud","LDustEffectsAir"],["GdtKlSoil","LDustEffectsAir"],["GdtKlTarmac","LDustEffectsAir"],["GdtKlStubble","LDustEffectsAir"],["GdtKlStones","LDustEffectsAir"],["SurfRoadDirt_Enoch","LDustEffectsAir"],["SurfTrailDirt_Enoch","LDustEffectsAir"],["SurfRoadTarmac1_Enoch","LDustEffectsAir"],["SurfRoadTarmac2_Enoch","LDustEffectsAir"],["SurfRoadTarmac3_Enoch","LDustEffectsAir"],["GdtGrassShort","LDustEffectsAir"],["GdtGrassShort","LGrassEffects"],["GdtGrassTall","LDustEffectsAir"],["GdtGrassTall","LGrassEffects"],["GdtRedDirt","LDustEffectsAirRed"],["GdtField","LDustEffectsAir"],["GdtForest","LDustEffectsAir"],["GdtVolcano","LDustEffectsAir"],["GdtVolcano","LStonesEffects"],["GdtCliff","LDustEffectsAir"],["GdtVolcanoBeach","LDustEffectsAir"],["SurfRoadDirt_exp","LDustEffectsAirRed"],["SurfRoadConcrete_exp","LDustEffectsAir"],["SurfRoadTarmac_exp","LDustEffectsAir"],["GdtStratisConcrete","LDustEffectsAir"],["GdtStratisConcrete","LDirtEffects"],["GdtStratisBeach","LDustEffectsAir"],["GdtStratisBeach","LStonesEffects"],["GdtStratisDirt","LDustEffectsAir"],["GdtStratisDirt","LDirtEffects"],["GdtStratisSeabedCluttered","LDustEffectsAir"],["GdtStratisSeabed","LDustEffectsAir"],["GdtStratisDryGrass","LDustEffectsAir"],["GdtStratisDryGrass","LGrassDryEffects"],["GdtStratisDryGrass","LDirtEffects"],["GdtStratisGreenGrass","LDustEffectsAir"],["GdtStratisGreenGrass","LGrassEffects"],["GdtStratisGreenGrass","LDirtEffects"],["GdtStratisRocky","LDustEffectsAir"],["GdtStratisRocky","LGrassEffects"],["GdtStratisRocky","LDirtEffects"],["GdtStratisThistles","LDustEffectsAir"],["GdtStratisThistles","LGrassEffects"],["GdtStratisThistles","LDirtEffects"],["GdtConcrete","LDustEffectsAir"],["GdtConcrete","LDirtEffects"],["GdtAsphalt","LDustEffectsAir"],["GdtAsphalt","LDirtEffects"],["GdtRubble","LDustEffectsAir"],["GdtRubble","LGrassEffects"],["GdtRubble","LDirtEffects"],["GdtSoil","LDustEffectsAir"],["GdtSoil","LDirtEffects"],["GdtBeach","LDustEffectsAir"],["GdtBeach","LStonesEffects"],["GdtRock","LDustEffectsAir"],["GdtRock","LDirtEffects"],["GdtDead","LDustEffectsAir"],["GdtDead","LDirtEffects"],["Default","LDustEffectsAir"],["GdtDesert1","LDustEffectsAir"],["GdtDesert1","LSandEffects"],["GdtDesert1","LDirtEffects"],["GdtDesert1","LStonesEffects"],["GdtDesert2","LDustEffectsAir"],["GdtDesert2","LSandEffects"],["GdtDesert2","LGrassEffects"],["GdtDesert2","LDirtEffects"],["GdtDirt","LDustEffectsAir"],["GdtDirt","LDirtEffects"],["GdtGrassGreen","LDustEffectsAir"],["GdtGrassGreen","LGrassEffects"],["GdtGrassGreen","LDirtEffects"],["GdtGrassDry","LDustEffectsAir"],["GdtGrassDry","LGrassDryEffects"],["GdtGrassDry","LDirtEffects"],["GdtGrassWild","LDustEffectsAir"],["GdtGrassWild","LGrassEffects"],["GdtGrassWild","LDirtEffects"],["GdtWildField","LDustEffectsAir"],["GdtWildField","LGrassEffects"],["GdtWildField","LDirtEffects"],["GdtWeed1","LDustEffectsAir"],["GdtWeed1","LGrassEffects"],["GdtWeed1","LDirtEffects"],["GdtWeed2","LDustEffectsAir"],["GdtWeed2","LGrassEffects"],["GdtWeed2","LDirtEffects"],["GdtThorn","LDustEffectsAir"],["GdtThorn","LGrassEffects"],["GdtThorn","LDirtEffects"],["GdtStony","LDustEffectsAir"],["GdtStony","LGrassEffects"],["GdtStony","LDirtEffects"],["GdtStonyGreen","LDustEffectsAir"],["GdtStonyGreen","LGrassEffects"],["GdtStonyGreen","LDirtEffects"],["GdtStonyThistle","LDustEffectsAir"],["GdtStonyThistle","LGrassEffects"],["GdtStonyThistle","LDirtEffects"],["GdtSeabedDeep","LDustEffectsAir"],["GdtSeabed","LDustEffectsAir"],["SurfRoadDirt","LDustEffectsAir"],["SurfRoadConcrete","LDustEffectsAir"],["SurfRoadTarmac","LDustEffectsAir"],["SurfWood","LDustEffectsAir"],["SurfMetal","LDustEffectsAir"],["SurfRoofTin","LDustEffectsAir"],["SurfRoofTiles","LDustEffectsAir"],["SurfIntWood","LDustEffectsAir"],["SurfIntConcrete","LDustEffectsAir"],["SurfIntTiles","LDustEffectsAir"],["SurfIntMetal","LDustEffectsAir"]],
    "maxFordingDepth": 0.001,
    "waterResistance": 1,
    "impactEffectsSea": "ImpactEffectsAir",
    "flareVelocity": 100,
    "enableRadio": 1,
    "memoryPointCM": ["flare_launcher1","flare_launcher2"],
    "memoryPointCMDir": ["flare_launcher1_dir","flare_launcher2_dir"],
    "radarType": 4,
    "radarTarget": 1,
    "visualTarget": 1,
    "countermeasureActivationRadius": 10000,
    # Class: CfgVehicles\Air\camShakeDamage,
    "camShakeDamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minSpeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "secondaryExplosion": -1,
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
    "memoryPointsGetInDriverPrecise": "pos driver",
    "memoryPointsGetInCargoPrecise": ["pos cargo"],
    "memoryPointsLeftWaterEffect": "waterEffectL",
    "memoryPointsRightWaterEffect": "waterEffectR",
    "selectionClan": "clan",
    "selectionShowDamage": "poskozeni",
    "selectionBackLights": "zadni svetlo",
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
    # Class: CfgVehicles\AllVehicles\CargoSpec,
    "CargoSpec": {
        # Class: CfgVehicles\AllVehicles\CargoSpec\Cargo1
        "Cargo1": {
            "showHeadPhones": 0
        }
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
    "driverLeftLegAnimName": "",
    "driverRightLegAnimName": "",
    "driverDoor": "",
    "cargoDoors": [],
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "preciseGetInOut": 0,
    "cargoPreciseGetInOut": [0],
    "availableForSupportTypes": [],
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
    "irTarget": 1,
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
    "allowTabLock": 1,
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
    # Class: CfgVehicles\All\FxExplo,
    "FxExplo": {
        "access": 1
    },
    "selectionDamage": "zbytek",
    "HeadAimDown": 0,
    "cargoCanEject": 1,
    "fireResistance": 10,
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
    "soundTurnIn": ["",0.000316228,1],
    "soundTurnOut": ["",0.000316228,1],
    "soundTurnInInternal": ["",0.000316228,1],
    "soundTurnOutInternal": ["",0.000316228,1],
    "insideDetectCoef": 0.05,
}