RHS_M2A2_BUSKI_WD = {
    "scope": 2,
    "faction": "rhs_faction_usarmy_wd",
    "crew": "rhsusf_army_ucp_crewman",
    "author": "Red Hammer Studios",
    "editorPreview": "rhsusf|addons|rhsusf_editorPreviews|data|RHS_M2A2_BUSKI_WD.paa",
    "hiddenSelections": ["camo1","camo2","camo3","selection_stinger","selection_tow"],
    "hiddenSelectionsTextures": ["|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|a3_buski_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|ultralp_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa"],
    "displayName": "M2A2ODS (BUSK I)",
    "model": "rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|M2A2_ERA",
    "damageResistance": 0.01101,
    # Class: CfgVehicles\RHS_M2A2_BUSKI\textureSources [Indent level: 1],
    "textureSources": {
        # Class: CfgVehicles\RHS_M2A2_BUSKI\textureSources\standard [Indent level: 2]
        "standard": {
            "displayName": "Woodland",
            "textures": ["|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|a3_buski_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|ultralp_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa"],
            "factions": ["rhs_faction_usarmy_wd"]
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\textureSources\Desert [Indent level: 2],
        "Desert": {
            "displayName": "Desert",
            "textures": ["|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|a3_buski_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|ultralp_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|base_co.paa"],
            "factions": ["rhs_faction_usarmy_d"]
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\textureSources\Olive [Indent level: 2],
        "Olive": {
            "displayName": "Olive",
            "author": "Red Hammer Studios",
            "textures": ["|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|m6_base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|m6_a3_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|ultralp_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|m6_base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|m6_base_co.paa"],
            "factions": ["rhs_faction_usarmy_wd"]
        }
    },
    # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources [Indent level: 1],
    "AnimationSources": {
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\Select_TOW [Indent level: 2]
        "Select_TOW": {
            "scope": 0,
            "author": "Red Hammer Studios",
            "displayName": "add Stinger launcher",
            "forceAnimatePhase": 1,
            "forceAnimate": ["Select_Stinger",0],
            "source": "user",
            "animPeriod": 1e-007,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\Select_Stinger [Indent level: 2],
        "Select_Stinger": {
            "scope": 0,
            "initPhase": 1,
            "forceAnimatePhase": 1,
            "displayName": "add TOW launcher",
            "forceAnimate": ["Select_TOW",0],
            "onPhaseChanged": "_this call rhs_fnc_m2_handleWeaponVG",
            "author": "Red Hammer Studios",
            "source": "user",
            "animPeriod": 1e-007
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_1_source [Indent level: 2],
        "era_1_source": {
            "source": "Hit",
            "hitpoint": "era_1_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_2_source [Indent level: 2],
        "era_2_source": {
            "source": "Hit",
            "hitpoint": "era_2_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_3_source [Indent level: 2],
        "era_3_source": {
            "source": "Hit",
            "hitpoint": "era_3_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_4_source [Indent level: 2],
        "era_4_source": {
            "source": "Hit",
            "hitpoint": "era_4_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_5_source [Indent level: 2],
        "era_5_source": {
            "source": "Hit",
            "hitpoint": "era_5_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_6_source [Indent level: 2],
        "era_6_source": {
            "source": "Hit",
            "hitpoint": "era_6_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_7_source [Indent level: 2],
        "era_7_source": {
            "source": "Hit",
            "hitpoint": "era_7_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_8_source [Indent level: 2],
        "era_8_source": {
            "source": "Hit",
            "hitpoint": "era_8_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_9_source [Indent level: 2],
        "era_9_source": {
            "source": "Hit",
            "hitpoint": "era_9_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_10_source [Indent level: 2],
        "era_10_source": {
            "source": "Hit",
            "hitpoint": "era_10_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_11_source [Indent level: 2],
        "era_11_source": {
            "source": "Hit",
            "hitpoint": "era_11_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_12_source [Indent level: 2],
        "era_12_source": {
            "source": "Hit",
            "hitpoint": "era_12_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_13_source [Indent level: 2],
        "era_13_source": {
            "source": "Hit",
            "hitpoint": "era_13_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_14_source [Indent level: 2],
        "era_14_source": {
            "source": "Hit",
            "hitpoint": "era_14_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_15_source [Indent level: 2],
        "era_15_source": {
            "source": "Hit",
            "hitpoint": "era_15_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_16_source [Indent level: 2],
        "era_16_source": {
            "source": "Hit",
            "hitpoint": "era_16_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_17_source [Indent level: 2],
        "era_17_source": {
            "source": "Hit",
            "hitpoint": "era_17_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_18_source [Indent level: 2],
        "era_18_source": {
            "source": "Hit",
            "hitpoint": "era_18_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_19_source [Indent level: 2],
        "era_19_source": {
            "source": "Hit",
            "hitpoint": "era_19_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_20_source [Indent level: 2],
        "era_20_source": {
            "source": "Hit",
            "hitpoint": "era_20_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_21_source [Indent level: 2],
        "era_21_source": {
            "source": "Hit",
            "hitpoint": "era_21_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_22_source [Indent level: 2],
        "era_22_source": {
            "source": "Hit",
            "hitpoint": "era_22_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_23_source [Indent level: 2],
        "era_23_source": {
            "source": "Hit",
            "hitpoint": "era_23_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_24_source [Indent level: 2],
        "era_24_source": {
            "source": "Hit",
            "hitpoint": "era_24_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_25_source [Indent level: 2],
        "era_25_source": {
            "source": "Hit",
            "hitpoint": "era_25_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_26_source [Indent level: 2],
        "era_26_source": {
            "source": "Hit",
            "hitpoint": "era_26_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_27_source [Indent level: 2],
        "era_27_source": {
            "source": "Hit",
            "hitpoint": "era_27_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_28_source [Indent level: 2],
        "era_28_source": {
            "source": "Hit",
            "hitpoint": "era_28_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_29_source [Indent level: 2],
        "era_29_source": {
            "source": "Hit",
            "hitpoint": "era_29_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_30_source [Indent level: 2],
        "era_30_source": {
            "source": "Hit",
            "hitpoint": "era_30_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_31_source [Indent level: 2],
        "era_31_source": {
            "source": "Hit",
            "hitpoint": "era_31_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_32_source [Indent level: 2],
        "era_32_source": {
            "source": "Hit",
            "hitpoint": "era_32_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_33_source [Indent level: 2],
        "era_33_source": {
            "source": "Hit",
            "hitpoint": "era_33_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_34_source [Indent level: 2],
        "era_34_source": {
            "source": "Hit",
            "hitpoint": "era_34_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_35_source [Indent level: 2],
        "era_35_source": {
            "source": "Hit",
            "hitpoint": "era_35_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_36_source [Indent level: 2],
        "era_36_source": {
            "source": "Hit",
            "hitpoint": "era_36_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_37_source [Indent level: 2],
        "era_37_source": {
            "source": "Hit",
            "hitpoint": "era_37_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_38_source [Indent level: 2],
        "era_38_source": {
            "source": "Hit",
            "hitpoint": "era_38_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_39_source [Indent level: 2],
        "era_39_source": {
            "source": "Hit",
            "hitpoint": "era_39_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_40_source [Indent level: 2],
        "era_40_source": {
            "source": "Hit",
            "hitpoint": "era_40_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_41_source [Indent level: 2],
        "era_41_source": {
            "source": "Hit",
            "hitpoint": "era_41_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_42_source [Indent level: 2],
        "era_42_source": {
            "source": "Hit",
            "hitpoint": "era_42_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_43_source [Indent level: 2],
        "era_43_source": {
            "source": "Hit",
            "hitpoint": "era_43_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_44_source [Indent level: 2],
        "era_44_source": {
            "source": "Hit",
            "hitpoint": "era_44_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\AnimationSources\era_45_source [Indent level: 2],
        "era_45_source": {
            "source": "Hit",
            "hitpoint": "era_45_hitpoint"
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\smoke_revolving_source [Indent level: 2],
        "smoke_revolving_source": {
            "source": "revolving",
            "weapon": "rhsusf_weap_M257_8"
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\cargolights_hide [Indent level: 2],
        "cargolights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animPeriod": 1e-006,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\IFF_Panels_Hide [Indent level: 2],
        "IFF_Panels_Hide": {
            "source": "user",
            "mass": -20,
            "displayName": "hide IFF Panels",
            "author": "Red Hammer Studios",
            "animPeriod": 1e-005,
            "initPhase": 0
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\recoil_source [Indent level: 2],
        "recoil_source": {
            "source": "reload",
            "weapon": "RHS_weap_M242BC"
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\muzzle_hide_hmg [Indent level: 2],
        "muzzle_hide_hmg": {
            "source": "reload",
            "weapon": "RHS_weap_M242BC"
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "RHS_weap_M242BC"
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\muzzle_rot_hmg2 [Indent level: 2],
        "muzzle_rot_hmg2": {
            "weapon": "rhs_weap_m240_bradley_coax",
            "source": "ammorandom"
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\HatchC [Indent level: 2],
        "HatchC": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\HatchG [Indent level: 2],
        "HatchG": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\HatchD [Indent level: 2],
        "HatchD": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\ramp [Indent level: 2],
        "ramp": {
            "source": "door",
            "animPeriod": 3.285,
            "initPhase": 0,
            "sound": "rhs_ramp",
            "soundPosition": "ramp_axis"
        },
        # Class: CfgVehicles\RHS_M2A2\AnimationSources\rear_hatch [Indent level: 2],
        "rear_hatch": {
            "source": "door",
            "animPeriod": 0.8,
            "initPhase": 0
        }
    },
    # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints [Indent level: 1],
    "HitPoints": {
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_1_hitpoint [Indent level: 2]
        "era_1_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e1",
            "armorComponent": "e1",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_1_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_1_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_1_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_1_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_1_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e1",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_2_hitpoint [Indent level: 2],
        "era_2_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e2",
            "armorComponent": "e2",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_2_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_2_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_2_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_2_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_2_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e2",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_3_hitpoint [Indent level: 2],
        "era_3_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e3",
            "armorComponent": "e3",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_3_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_3_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_3_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_3_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_3_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e3",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_4_hitpoint [Indent level: 2],
        "era_4_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e4",
            "armorComponent": "e4",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_4_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_4_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_4_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_4_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_4_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e4",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_5_hitpoint [Indent level: 2],
        "era_5_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e5",
            "armorComponent": "e5",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_5_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_5_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_5_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e5",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_5_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_5_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e5",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_6_hitpoint [Indent level: 2],
        "era_6_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e6",
            "armorComponent": "e6",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_6_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_6_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_6_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e6",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_6_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_6_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e6",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_7_hitpoint [Indent level: 2],
        "era_7_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e7",
            "armorComponent": "e7",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_7_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_7_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_7_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_7_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_7_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e7",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_8_hitpoint [Indent level: 2],
        "era_8_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e8",
            "armorComponent": "e8",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_8_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_8_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e8",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_8_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e8",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_8_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e8",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_8_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e8",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_9_hitpoint [Indent level: 2],
        "era_9_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e9",
            "armorComponent": "e9",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_9_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_9_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e9",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_9_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e9",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_9_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e9",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_9_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e9",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_10_hitpoint [Indent level: 2],
        "era_10_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e10",
            "armorComponent": "e10",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_10_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_10_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e10",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_10_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e10",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_10_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e10",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_10_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e10",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_11_hitpoint [Indent level: 2],
        "era_11_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e11",
            "armorComponent": "e11",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_11_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_11_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e11",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_11_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e11",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_11_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e11",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_11_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e11",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_12_hitpoint [Indent level: 2],
        "era_12_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e12",
            "armorComponent": "e12",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_12_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_12_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e12",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_12_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e12",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_12_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e12",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_12_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e12",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_13_hitpoint [Indent level: 2],
        "era_13_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e13",
            "armorComponent": "e13",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_13_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_13_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e13",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_13_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e13",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_13_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e13",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_13_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e13",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_14_hitpoint [Indent level: 2],
        "era_14_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e14",
            "armorComponent": "e14",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_14_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_14_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e14",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_14_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e14",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_14_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e14",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_14_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e14",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_15_hitpoint [Indent level: 2],
        "era_15_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e15",
            "armorComponent": "e15",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_15_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_15_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e15",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_15_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e15",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_15_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e15",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_15_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e15",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_16_hitpoint [Indent level: 2],
        "era_16_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e16",
            "armorComponent": "e16",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_16_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_16_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e16",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_16_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e16",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_16_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e16",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_16_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e16",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_17_hitpoint [Indent level: 2],
        "era_17_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e17",
            "armorComponent": "e17",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_17_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_17_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e17",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_17_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e17",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_17_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e17",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_17_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e17",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_18_hitpoint [Indent level: 2],
        "era_18_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e18",
            "armorComponent": "e18",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_18_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_18_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e18",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_18_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e18",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_18_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e18",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_18_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e18",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_19_hitpoint [Indent level: 2],
        "era_19_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e19",
            "armorComponent": "e19",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_19_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_19_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e19",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_19_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e19",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_19_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e19",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_19_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e19",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_20_hitpoint [Indent level: 2],
        "era_20_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e20",
            "armorComponent": "e20",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_20_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_20_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e20",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_20_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e20",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_20_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e20",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_20_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e20",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_21_hitpoint [Indent level: 2],
        "era_21_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e21",
            "armorComponent": "e21",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_21_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_21_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e21",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_21_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e21",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_21_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e21",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_21_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e21",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_22_hitpoint [Indent level: 2],
        "era_22_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e22",
            "armorComponent": "e22",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_22_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_22_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e22",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_22_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e22",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_22_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e22",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_22_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e22",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_23_hitpoint [Indent level: 2],
        "era_23_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e23",
            "armorComponent": "e23",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_23_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_23_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e23",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_23_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e23",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_23_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e23",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_23_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e23",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_24_hitpoint [Indent level: 2],
        "era_24_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e24",
            "armorComponent": "e24",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_24_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_24_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e24",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_24_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e24",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_24_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e24",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_24_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e24",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_25_hitpoint [Indent level: 2],
        "era_25_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e25",
            "armorComponent": "e25",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_25_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_25_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e25",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_25_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e25",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_25_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e25",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_25_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e25",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_26_hitpoint [Indent level: 2],
        "era_26_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e26",
            "armorComponent": "e26",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_26_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_26_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e26",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_26_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e26",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_26_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e26",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_26_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e26",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_27_hitpoint [Indent level: 2],
        "era_27_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e27",
            "armorComponent": "e27",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_27_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_27_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e27",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_27_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e27",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_27_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e27",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_27_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e27",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_28_hitpoint [Indent level: 2],
        "era_28_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e28",
            "armorComponent": "e28",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_28_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_28_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e28",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_28_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e28",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_28_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e28",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_28_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e28",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_29_hitpoint [Indent level: 2],
        "era_29_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e29",
            "armorComponent": "e29",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_29_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_29_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e29",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_29_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e29",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_29_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e29",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_29_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e29",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_30_hitpoint [Indent level: 2],
        "era_30_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e30",
            "armorComponent": "e30",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_30_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_30_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e30",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_30_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e30",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_30_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e30",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_30_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e30",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_31_hitpoint [Indent level: 2],
        "era_31_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e31",
            "armorComponent": "e31",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_31_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_31_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e31",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_31_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e31",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_31_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e31",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_31_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e31",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_32_hitpoint [Indent level: 2],
        "era_32_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e32",
            "armorComponent": "e32",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_32_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_32_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e32",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_32_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e32",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_32_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e32",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_32_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e32",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_33_hitpoint [Indent level: 2],
        "era_33_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e33",
            "armorComponent": "e33",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_33_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_33_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e33",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_33_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e33",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_33_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e33",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_33_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e33",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_34_hitpoint [Indent level: 2],
        "era_34_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e34",
            "armorComponent": "e34",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_34_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_34_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e34",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_34_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e34",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_34_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e34",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_34_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e34",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_35_hitpoint [Indent level: 2],
        "era_35_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e35",
            "armorComponent": "e35",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_35_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_35_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e35",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_35_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e35",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_35_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e35",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_35_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e35",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_36_hitpoint [Indent level: 2],
        "era_36_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e36",
            "armorComponent": "e36",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_36_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_36_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e36",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_36_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e36",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_36_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e36",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_36_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e36",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_37_hitpoint [Indent level: 2],
        "era_37_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e37",
            "armorComponent": "e37",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_37_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_37_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e37",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_37_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e37",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_37_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e37",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_37_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e37",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_38_hitpoint [Indent level: 2],
        "era_38_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e38",
            "armorComponent": "e38",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_38_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_38_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e38",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_38_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e38",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_38_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e38",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_38_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e38",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_39_hitpoint [Indent level: 2],
        "era_39_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e39",
            "armorComponent": "e39",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_39_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_39_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e39",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_39_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e39",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_39_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e39",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_39_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e39",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_40_hitpoint [Indent level: 2],
        "era_40_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e40",
            "armorComponent": "e40",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_40_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_40_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e40",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_40_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e40",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_40_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e40",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_40_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e40",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_41_hitpoint [Indent level: 2],
        "era_41_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e41",
            "armorComponent": "e41",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_41_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_41_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e41",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_41_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e41",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_41_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e41",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_41_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e41",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_42_hitpoint [Indent level: 2],
        "era_42_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e42",
            "armorComponent": "e42",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_42_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_42_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e42",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_42_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e42",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_42_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e42",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_42_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e42",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_43_hitpoint [Indent level: 2],
        "era_43_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e43",
            "armorComponent": "e43",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_43_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_43_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e43",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_43_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e43",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_43_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e43",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_43_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e43",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_44_hitpoint [Indent level: 2],
        "era_44_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e44",
            "armorComponent": "e44",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_44_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_44_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e44",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_44_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e44",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_44_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e44",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_44_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e44",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_45_hitpoint [Indent level: 2],
        "era_45_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e45",
            "armorComponent": "e45",
            "passThrough": 0,
            "minimalHit": -0.4,
            "explosionShielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_45_hitpoint\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                "effectRadius": 1,
                "ignoreFuel": 1,
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_45_hitpoint\DestructionEffects\RHS_ERA_Flash [Indent level: 4],
                "RHS_ERA_Flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e45",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 0.006
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_45_hitpoint\DestructionEffects\RHS_ERA_Sound [Indent level: 4],
                "RHS_ERA_Sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e45",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 1
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_45_hitpoint\DestructionEffects\RHS_ERA_Smoke [Indent level: 4],
                "RHS_ERA_Smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e45",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifeTime": 0.04
                },
                # Class: CfgVehicles\RHS_M2A2_BUSKI\HitPoints\era_45_hitpoint\DestructionEffects\RHS_ERA_Shard [Indent level: 4],
                "RHS_ERA_Shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e45",
                    "intensity": 1,
                    "interval": 1,
                    "lifeTime": 0.03
                }
            }
        },
        # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitHull_Structural [Indent level: 2],
        "HitHull_Structural": {
            "armor": -600,
            "name": "Hit_Engine",
            "visual": "-",
            "passThrough": 0,
            "minimalHit": -0.22,
            "explosionShielding": 0,
            "radius": 0
        },
        # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitHull [Indent level: 2],
        "HitHull": {
            "armor": -110,
            "name": "Hit_Hull",
            "armorComponent": "Hit_Hull",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": -0.15,
            "explosionShielding": 0.01,
            "radius": 0.1,
            "depends": "HitHull_Structural",
            "material": -1
        },
        # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitEngine [Indent level: 2],
        "HitEngine": {
            "armor": -100,
            "name": "Hit_Engine",
            "armorComponent": "Hit_Engine",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.14,
            "explosionShielding": 0.009,
            "radius": 0.17,
            # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitEngine\DestructionEffects [Indent level: 3],
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke [Indent level: 4],
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Fire [Indent level: 4],
                "RHS_Engine_Fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sparks [Indent level: 4],
                "RHS_Engine_Sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds [Indent level: 4],
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1 [Indent level: 4],
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2 [Indent level: 4],
                "RHS_Engine_Smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                }
            },
            "material": -1
        },
        # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitLTrack [Indent level: 2],
        "HitLTrack": {
            "armor": -150,
            "armorComponent": "Hit_TrackL",
            "name": "Hit_TrackL",
            "passThrough": 0,
            "minimalHit": -0.25,
            "explosionShielding": 0.5,
            "radius": 0.3,
            "material": -1,
            "visual": "pas_L"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\HitRTrack [Indent level: 2],
        "HitRTrack": {
            "armor": -150,
            "armorComponent": "Hit_TrackR",
            "name": "Hit_TrackR",
            "passThrough": 0,
            "minimalHit": -0.25,
            "explosionShielding": 0.5,
            "radius": 0.3,
            "material": -1,
            "visual": "pas_P"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\Hit_LightL [Indent level: 2],
        "Hit_LightL": {
            "armor": -10,
            "name": "l svetlo",
            "visual": "-",
            "passThrough": 0,
            "minimalHit": -0.1,
            "explosionShielding": 1,
            "radius": 0
        },
        # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\Hit_LightR [Indent level: 2],
        "Hit_LightR": {
            "name": "p svetlo",
            "armor": -10,
            "visual": "-",
            "passThrough": 0,
            "minimalHit": -0.1,
            "explosionShielding": 1,
            "radius": 0
        },
        # Class: CfgVehicles\RHS_M2A2_Base\HitPoints\Hit_Optics_Dvr_Peri [Indent level: 2],
        "Hit_Optics_Dvr_Peri": {
            "armor": -40,
            "explosionShielding": 0,
            "name": "",
            "visual": "vis_optics_Dvr_Peri",
            "armorComponent": "Hit_Optics_Dvr_Peri",
            "passThrough": 0
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitFuel [Indent level: 2],
        "HitFuel": {
            "armor": 0.5,
            "material": -1,
            "armorComponent": "hit_fuel",
            "name": "hit_fuel_point",
            "visual": "-",
            "passThrough": 0.3,
            "minimalHit": 0.1,
            "explosionShielding": 0.6,
            "radius": 0.3
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_Left_1 [Indent level: 2],
        "HitSLAT_Left_1": {
            "simulation": "Armor_SLAT",
            "armorComponent": "cage_left_1_geo",
            "name": "cage_left_1_point",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_Left_2 [Indent level: 2],
        "HitSLAT_Left_2": {
            "armorComponent": "cage_left_2_geo",
            "name": "cage_left_2_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_Left_3 [Indent level: 2],
        "HitSLAT_Left_3": {
            "armorComponent": "cage_left_3_geo",
            "name": "cage_left_3_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_Right_1 [Indent level: 2],
        "HitSLAT_Right_1": {
            "armorComponent": "cage_right_1_geo",
            "name": "cage_right_1_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_Right_2 [Indent level: 2],
        "HitSLAT_Right_2": {
            "armorComponent": "cage_right_2_geo",
            "name": "cage_right_2_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_Right_3 [Indent level: 2],
        "HitSLAT_Right_3": {
            "armorComponent": "cage_right_3_geo",
            "name": "cage_right_3_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_top_back [Indent level: 2],
        "HitSLAT_top_back": {
            "armorComponent": "cage_top_back_geo",
            "name": "cage_top_back_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_top_left [Indent level: 2],
        "HitSLAT_top_left": {
            "armorComponent": "cage_top_left_geo",
            "name": "cage_top_left_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_top_right [Indent level: 2],
        "HitSLAT_top_right": {
            "armorComponent": "cage_top_right_geo",
            "name": "cage_top_right_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_back [Indent level: 2],
        "HitSLAT_back": {
            "armorComponent": "cage_back_geo",
            "name": "cage_back_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\HitPoints\HitSLAT_front [Indent level: 2],
        "HitSLAT_front": {
            "armorComponent": "cage_front_geo",
            "name": "cage_front_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalHit": 0.3,
            "passThrough": 0,
            "visual": "-",
            "explosionShielding": 2,
            "radius": 0.25
        }
    },
    "side": 1,
    # Class: CfgVehicles\RHS_M2A2\Library [Indent level: 1],
    "Library": {
        "libTextDesc": "The M2 Bradley IFV (Infantry Fighting Vehicle) is an US infantry fighting vehicle. It is designed to transport infantry with armor protection while providing covering fire to suppressing enemy troops and armored vehicles.<br/>The A2 variant features improvements based on lessons learned during Gulf War in 1991."
    },
    "cargoDoors": ["ramp"],
    # Class: CfgVehicles\RHS_M2A2\Damage [Indent level: 1],
    "Damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV1.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV1_damage.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV1_destruct.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2_damage.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2_destruct.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2_ERAon.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2_ERAon_damage.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2_ERAon_destruct.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|M2_tracks.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|M2_tracks_damage.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|M2_tracks_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    "dlc": "RHS_USAF",
    "category": "Armored",
    "destrType": "DestructDefault",
    "soundGetIn": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1],
    "soundGetOut": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1,20],
    "soundDammage": ["",0.562341,1],
    "soundEngineOnInt": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_start",0.630957,1],
    "soundEngineOnExt": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_start",1,1,200],
    "soundEngineOffInt": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_stop",0.630957,1],
    "soundEngineOffExt": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_stop",1,1,200],
    "buildCrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "buildCrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "buildCrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "buildCrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "soundBuildingCrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "WoodCrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "WoodCrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "WoodCrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "WoodCrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "WoodCrash4": ["A3|sounds_f|Vehicles|crashes|crash_01",1,1,200],
    "WoodCrash5": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "soundWoodCrash": ["woodCrash0",0.166,"woodCrash1",0.166,"woodCrash2",0.166,"woodCrash3",0.166,"woodCrash4",0.166,"woodCrash5",0.166],
    "ArmorCrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "ArmorCrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "ArmorCrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "ArmorCrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "soundArmorCrash": ["ArmorCrash0",0.25,"ArmorCrash1",0.25,"ArmorCrash2",0.25,"ArmorCrash3",0.25],
    # Class: CfgVehicles\RHS_M2A2_Base\Sounds [Indent level: 1],
    "Sounds": {
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Idle_ext [Indent level: 2]
        "Idle_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_1",0.562341,1,160],
            "frequency": "0.3	+	((rpm/	2600) factor[(100/	2600),(250/	2600)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2600) factor[(100/	2600),(400/	2600)])	*	((rpm/	2600) factor[(730/	2600),(610/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine [Indent level: 2],
        "Engine": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_2",0.794328,1,200],
            "frequency": "0.8	+	((rpm/	2600) factor[(600/	2600),(1100/	2600)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2600) factor[(550/	2600),(700/	2600)])	*	((rpm/	2600) factor[(1100/	2600),(760/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine1_ext [Indent level: 2],
        "Engine1_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_3",0.891251,1,260],
            "frequency": "0.8	+	((rpm/	2600) factor[(770/	2600),(1400/	2600)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2600) factor[(720/	2600),(1060/	2600)])	*	((rpm/	2600) factor[(1400/	2600),(1180/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine2_ext [Indent level: 2],
        "Engine2_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_4",1,1,280],
            "frequency": "0.8	+	((rpm/	2600) factor[(1150/	2600),(1700/	2600)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2600) factor[(1130/	2600),(1370/	2600)])	*	((rpm/	2600) factor[(1700/	2600),(1500/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine3_ext [Indent level: 2],
        "Engine3_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_5",1.12202,1,300],
            "frequency": "0.8	+	((rpm/	2600) factor[(1500/	2600),(2100/	2600)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2600) factor[(1460/	2600),(1670/	2600)])	*	((rpm/	2600) factor[(2100/	2600),(1800/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine4_ext [Indent level: 2],
        "Engine4_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_6",1.25893,1,320],
            "frequency": "0.8	+	((rpm/	2600) factor[(1800/	2600),(2600/	2600)])*0.1",
            "volume": "engineOn*camPos*((rpm/	2600) factor[(1750/	2600),(2050/	2600)])"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\IdleThrust [Indent level: 2],
        "IdleThrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_1",1,1,250],
            "frequency": "0.8	+	((rpm/	2600) factor[(500/	2600),(650/	2600)])*0.15",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(100/	2600),(400/	2600)])	*	((rpm/	2600) factor[(730/	2600),(610/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\EngineThrust [Indent level: 2],
        "EngineThrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_2",1.12202,1,280],
            "frequency": "0.8	+	((rpm/	2600) factor[(600/	2600),(1100/	2600)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(550/	2600),(700/	2600)])	*	((rpm/	2600) factor[(1100/	2600),(760/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine1_Thrust_ext [Indent level: 2],
        "Engine1_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_3",1.25893,1,300],
            "frequency": "0.8	+	((rpm/	2600) factor[(770/	2600),(1400/	2600)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(720/	2600),(1060/	2600)])	*	((rpm/	2600) factor[(1400/	2600),(1180/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine2_Thrust_ext [Indent level: 2],
        "Engine2_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_4",1.41254,1,340],
            "frequency": "0.8	+	((rpm/	2600) factor[(1150/	2600),(1700/	2600)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(1130/	2600),(1370/	2600)])	*	((rpm/	2600) factor[(1700/	2600),(1500/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine3_Thrust_ext [Indent level: 2],
        "Engine3_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_5",1.77828,1,360],
            "frequency": "0.8	+	((rpm/	2600) factor[(1500/	2600),(2100/	2600)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(1460/	2600),(1670/	2600)])	*	((rpm/	2600) factor[(2100/	2600),(1800/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine4_Thrust_ext [Indent level: 2],
        "Engine4_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_6",1.99526,1,380],
            "frequency": "0.8	+	((rpm/	2600) factor[(1800/	2600),(2600/	2600)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	2600) factor[(1750/	2600),(2050/	2600)])"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Idle_int [Indent level: 2],
        "Idle_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_1",0.316228,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(500/	2600),(650/	2600)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	2600) factor[(100/	2600),(400/	2600)])	*	((rpm/	2600) factor[(730/	2600),(610/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine_int [Indent level: 2],
        "Engine_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_2",0.354813,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(600/	2600),(1100/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2600) factor[(550/	2600),(700/	2600)])	*	((rpm/	2600) factor[(1100/	2600),(760/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine1_int [Indent level: 2],
        "Engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_3",0.398107,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(770/	2600),(1400/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2600) factor[(720/	2600),(1060/	2600)])	*	((rpm/	2600) factor[(1400/	2600),(1180/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine2_int [Indent level: 2],
        "Engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_4",0.446684,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1150/	2600),(1700/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2600) factor[(1130/	2600),(1370/	2600)])	*	((rpm/	2600) factor[(1700/	2600),(1500/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine3_int [Indent level: 2],
        "Engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_5",0.501187,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1500/	2600),(2100/	2600)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	2600) factor[(1460/	2600),(1670/	2600)])	*	((rpm/	2600) factor[(2100/	2600),(1800/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine4_int [Indent level: 2],
        "Engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_6",0.562341,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1800/	2600),(2600/	2600)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	2600) factor[(1750/	2600),(2050/	2600)])"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\IdleThrust_int [Indent level: 2],
        "IdleThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_1",0.354813,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(500/	2600),(650/	2600)])*0.15",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(100/	2600),(400/	2600)])	*	((rpm/	2600) factor[(730/	2600),(610/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\EngineThrust_int [Indent level: 2],
        "EngineThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_2",0.398107,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(600/	2600),(1100/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(550/	2600),(700/	2600)])	*	((rpm/	2600) factor[(1100/	2600),(760/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine1_Thrust_int [Indent level: 2],
        "Engine1_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_3",0.446684,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(770/	2600),(1400/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(720/	2600),(1060/	2600)])	*	((rpm/	2600) factor[(1400/	2600),(1180/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine2_Thrust_int [Indent level: 2],
        "Engine2_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_4",0.446684,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1150/	2600),(1700/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(1130/	2600),(1370/	2600)])	*	((rpm/	2600) factor[(1700/	2600),(1500/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine3_Thrust_int [Indent level: 2],
        "Engine3_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_5",0.501187,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1500/	2600),(2100/	2600)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(1460/	2600),(1670/	2600)])	*	((rpm/	2600) factor[(2100/	2600),(1800/	2600)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\Engine4_Thrust_int [Indent level: 2],
        "Engine4_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_6",0.562341,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1800/	2600),(2600/	2600)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	2600) factor[(1750/	2600),(2050/	2600)])"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\NoiseInt [Indent level: 2],
        "NoiseInt": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_int_1",3.16228,1],
            "frequency": "1",
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\NoiseExt [Indent level: 2],
        "NoiseExt": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_ext_1",3.16228,1,250],
            "frequency": "1",
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsOutH0 [Indent level: 2],
        "ThreadsOutH0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_01",0.398107,1,140],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-0) max 0)/	95),(((-10) max 10)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-25) max 25)/	95),(((-15) max 15)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsOutH1 [Indent level: 2],
        "ThreadsOutH1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_02",0.446684,1,160],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-20) max 20)/	95),(((-35) max 35)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-55) max 55)/	95),(((-40) max 40)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsOutH2 [Indent level: 2],
        "ThreadsOutH2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_03",0.501187,1,180],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-45) max 45)/	95),(((-55) max 55)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-70) max 70)/	95),(((-60) max 60)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsOutH3 [Indent level: 2],
        "ThreadsOutH3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_04",0.562341,1,200],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-65) max 65)/	95),(((-70) max 70)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-85) max 85)/	95),(((-80) max 80)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsOutH4 [Indent level: 2],
        "ThreadsOutH4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_05",0.562341,1,220],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)/	95) factor[(((-80) max 80)/	95),(((-90) max 90)/	95)])"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsOutS0 [Indent level: 2],
        "ThreadsOutS0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_01",0.316228,1,120],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-0) max 0)/	95),(((-10) max 10)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-25) max 25)/	95),(((-15) max 15)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsOutS1 [Indent level: 2],
        "ThreadsOutS1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_02",0.354813,1,140],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-20) max 20)/	95),(((-35) max 35)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-55) max 55)/	95),(((-40) max 40)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsOutS2 [Indent level: 2],
        "ThreadsOutS2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_03",0.398107,1,160],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-45) max 45)/	95),(((-55) max 55)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-70) max 70)/	95),(((-60) max 60)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsOutS3 [Indent level: 2],
        "ThreadsOutS3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_04",0.446684,1,180],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-65) max 65)/	95),(((-70) max 70)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-85) max 85)/	95),(((-80) max 80)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsOutS4 [Indent level: 2],
        "ThreadsOutS4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_05",0.501187,1,200],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)/	95) factor[(((-80) max 80)/	95),(((-90) max 90)/	95)])"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsInH0 [Indent level: 2],
        "ThreadsInH0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_01",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-0) max 0)/	95),(((-10) max 10)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-25) max 25)/	95),(((-15) max 15)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsInH1 [Indent level: 2],
        "ThreadsInH1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_02",0.501187,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-20) max 20)/	95),(((-35) max 35)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-55) max 55)/	95),(((-40) max 40)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsInH2 [Indent level: 2],
        "ThreadsInH2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_03",0.562341,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-45) max 45)/	95),(((-55) max 55)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-70) max 70)/	95),(((-60) max 60)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsInH3 [Indent level: 2],
        "ThreadsInH3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_04",0.630957,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-65) max 65)/	95),(((-70) max 70)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-85) max 85)/	95),(((-80) max 80)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsInH4 [Indent level: 2],
        "ThreadsInH4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_05",0.707946,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)/	95) factor[(((-80) max 80)/	95),(((-90) max 90)/	95)])"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsInS0 [Indent level: 2],
        "ThreadsInS0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_01",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-0) max 0)/	95),(((-10) max 10)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-25) max 25)/	95),(((-15) max 15)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsInS1 [Indent level: 2],
        "ThreadsInS1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_02",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-20) max 20)/	95),(((-35) max 35)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-55) max 55)/	95),(((-40) max 40)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsInS2 [Indent level: 2],
        "ThreadsInS2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_03",0.501187,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-45) max 45)/	95),(((-55) max 55)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-70) max 70)/	95),(((-60) max 60)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsInS3 [Indent level: 2],
        "ThreadsInS3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_04",0.630957,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-65) max 65)/	95),(((-70) max 70)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-85) max 85)/	95),(((-80) max 80)/	95)]))"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Sounds\ThreadsInS4 [Indent level: 2],
        "ThreadsInS4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_05",0.707946,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)/	95) factor[(((-80) max 80)/	95),(((-90) max 90)/	95)])"
        }
    },
    "simulation": "tankX",
    "normalSpeedForwardCoef": 0.6,
    "slowSpeedForwardCoef": 0.45,
    "fuelCapacity": 24.15,
    "RHS_fuelCapacity": 462,
    "maxSpeed": 66,
    "tracksSpeed": 10,
    "maxFordingDepth": 0,
    "waterResistance": 0,
    "waterDamageEngine": 0.2,
    "waterLeakiness": 10,
    "tankTurnForce": 450000,
    "tankTurnForceAngMinSpd": 0.7,
    "tankTurnForceAngSpd": 0.87,
    "accelAidForceCoef": 2,
    "accelAidForceYOffset": -4,
    "accelAidForceSpd": 4.23,
    "torqueCurve": [[0.307692,0.518072],[0.384615,0.855422],[0.538462,1],[0.576923,0.945783],[0.653846,0.909639],[0.769231,0.873494],[0.903846,0.843373],[1.02962,0]],
    "engineMOI": 5,
    "enginePower": 447,
    "peakTorque": 1660,
    "minOmega": 84,
    "maxOmega": 272.27,
    "idleRPM": 800,
    "redRPM": 2600,
    "thrustDelay": 0.3,
    "brakeIdleSpeed": 1.78,
    "switchTime": 0.1,
    "latency": 1,
    "clutchStrength": 35,
    "engineLosses": 25,
    "transmissionLosses": 15,
    "changeGearType": "rpmratio",
    "changeGearOmegaRatios": [1,0.384615,0.384615,0,0.923077,0.384615,0.961538,0.538462,0.961538,0.576923,1,0.692308],
    # Class: CfgVehicles\RHS_M2A2_Base\complexGearbox [Indent level: 1],
    "complexGearbox": {
        "GearboxRatios": ["R1",-2.2,"N",0,"D1",4.2,"D2",2.23,"D3",1.22,"D4",0.839],
        "TransmissionRatios": ["High",14.75],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R"
    },
    # Class: CfgVehicles\RHS_M2A2_Base\Wheels [Indent level: 1],
    "Wheels": {
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\L2 [Indent level: 2]
        "L2": {
            "suspTravelDirection": [-0.125,-1,0],
            "boneName": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\L3 [Indent level: 2],
        "L3": {
            "boneName": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\L4 [Indent level: 2],
        "L4": {
            "boneName": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\L5 [Indent level: 2],
        "L5": {
            "boneName": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\L6 [Indent level: 2],
        "L6": {
            "boneName": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\L7 [Indent level: 2],
        "L7": {
            "boneName": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\L9 [Indent level: 2],
        "L9": {
            "boneName": "wheel_podkolol9",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\L1 [Indent level: 2],
        "L1": {
            "boneName": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\R2 [Indent level: 2],
        "R2": {
            "suspTravelDirection": [0.125,-1,0],
            "boneName": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\R3 [Indent level: 2],
        "R3": {
            "boneName": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\R4 [Indent level: 2],
        "R4": {
            "boneName": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\R5 [Indent level: 2],
        "R5": {
            "boneName": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\R6 [Indent level: 2],
        "R6": {
            "boneName": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\R7 [Indent level: 2],
        "R7": {
            "boneName": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\R9 [Indent level: 2],
        "R9": {
            "boneName": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Wheels\R1 [Indent level: 2],
        "R1": {
            "boneName": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "suspTravelDirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "MOI": 10.0392,
            "maxBrakeTorque": 6520,
            "sprungMass": 2500,
            "springStrength": 256250,
            "springDamperRate": 14811,
            "dampingRate": 1088,
            "dampingRateInAir": 1088,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3.5,
            "latStiffY": 45,
            "longitudinalStiffnessPerUnitGravity": 14000,
            "frictionVsSlipGraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        }
    },
    "vehicleClass": "rhs_vehclass_ifv",
    "editorSubcategory": "rhs_EdSubcat_ifv",
    # Class: CfgVehicles\RHS_M2A2_Base\SpeechVariants [Indent level: 1],
    "SpeechVariants": {
        # Class: CfgVehicles\RHS_M2A2_Base\SpeechVariants\Default [Indent level: 2]
        "Default": {
            "speechSingular": ["veh_vehicle_APC_s"],
            "speechPlural": ["veh_vehicle_APC_p"]
        }
    },
    "textSingular": "IFV",
    "textPlural": "IFVs",
    "nameSound": "veh_vehicle_APC_s",
    "driveOnComponent": ["slide","trackL","trackR"],
    "unitInfoType": "RHSUSF_RscUnitInfoWestTank",
    "picture": "rhsusf|addons|rhsusf_a2port_armor|pictures|rhs_m2a2_pic_ca.paa",
    "Icon": "rhsusf|addons|rhsusf_a2port_armor|Data|UI|Icon_m2a2_CA.paa",
    "MapSize": 7,
    "accuracy": 0.3,
    "transportSoldier": 6,
    "getInAction": "GetInHigh",
    "getOutAction": "GetOutHigh",
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "memoryPointsGetInCargo": ["pos cargo","pos cargo 1","pos cargo 2","pos cargo 3"],
    "memoryPointsGetInCargoDir": ["pos cargo dir","pos cargo 1 dir","pos cargo dir","pos cargo 2 dir","pos cargo 3 dir"],
    "cargoProxyIndexes": [1,2,3,4,5,6],
    "getInProxyOrder": [1,2,3,4,5,6],
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "rhs_hasSmokeCap": 1,
    "reportOwnPosition": 1,
    "LODDriverTurnedIn": 1100,
    "LODDriverTurnedOut": 0,
    "LODDriverOpticsIn": 0,
    "viewDriverInExternal": 1,
    "viewCargoShadow": 1,
    "viewCargoShadowDiff": 0.05,
    "viewCargoShadowAmb": 0.5,
    "headGforceLeaningFactor": [0.015,0.011,0.015],
    # Class: CfgVehicles\RHS_M2A2_Base\RenderTargets [Indent level: 1],
    "RenderTargets": {
    },
    "driverLeftHandAnimName": "yoke",
    "driverRightHandAnimName": "yoke",
    "textureList": [],
    "driverOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_vision_block",
    "forceHideDriver": 0,
    "DriverForceOptics": 0,
    "driverDoor": "hatchD",
    "dustFrontLeftPos": "wheel_1_4_bound",
    "dustFrontRightPos": "wheel_2_4_bound",
    "dustBackLeftPos": "wheel_1_7_bound",
    "dustBackRightPos": "wheel_2_7_bound",
    "radarType": 1,
    "LockDetectionSystem": 0,
    "incomingMissileDetectionSystem": 0,
    "irtarget": 1,
    "irScanGround": 0,
    "threat": [0.9,0.9,0.4],
    "armor": 290,
    "armorStructural": 280,
    "explosionShielding": 15,
    # Class: CfgVehicles\RHS_M2A2_Base\Turrets [Indent level: 1],
    "Turrets": {
        # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret [Indent level: 2]
        "MainTurret": {
            "lockWhenDriverOut": 1,
            "turretInfoType": "RHS_RscODS_ISU",
            "discreteDistance": [0,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000],
            "discreteDistanceInitIndex": 2,
            "gunnerHasFlares": 0,
            "gunnerForceOptics": 1,
            "gunnerAction": "RHS_M2A2_GunnerOut",
            "gunnerInAction": "RHS_M2A2_Gunner",
            "gunnerGetInAction": "GetInHigh",
            "gunnerGetOutAction": "GetOutHigh",
            "gunnerDoor": "hatchG",
            "minElev": -9,
            "maxElev": 57,
            "initElev": 0,
            "viewGunnerInExternal": 1,
            "showCrewAim": 0,
            "allowTabLock": 0,
            "maxhorizontalrotspeed": 1.04,
            "maxverticalrotspeed": 1.04,
            "stabilizedinaxes": 3,
            "startengine": 0,
            "hideWeaponsGunner": 1,
            "selectionFireAnim": "zasleh2",
            "weapons": ["RHS_weap_M242BC","rhs_weap_m240_bradley_coax","Rhs_weap_TOW_Launcher","rhs_weap_fcs_ammo"],
            "magazines": ["rhs_mag_1100Rnd_762x51_M240","rhs_mag_1100Rnd_762x51_M240","rhs_mag_230Rnd_25mm_M242_HEI","rhs_mag_230Rnd_25mm_M242_HEI","rhs_mag_230Rnd_25mm_M242_HEI","rhs_mag_70Rnd_25mm_M242_APFSDS","rhs_mag_70Rnd_25mm_M242_APFSDS","rhs_mag_70Rnd_25mm_M242_APFSDS","rhs_mag_2Rnd_TOW2A","rhs_mag_2Rnd_TOW2A","rhs_mag_2Rnd_TOW2A","rhs_mag_2Rnd_TOW2BB","rhs_laserfcsmag"],
            # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\OpticsIn [Indent level: 3],
            "OpticsIn": {
                # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\OpticsIn\Wide [Indent level: 4]
                "Wide": {
                    "opticsDisplayName": "WIDE",
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "initFov": 0.175,
                    "minFov": 0.175,
                    "maxFov": 0.175,
                    "visionMode": ["Normal","Ti"],
                    "thermalMode": [4],
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_ISU",
                    "gunnerOpticsEffect": [],
                    "hitPoint": "Hit_Optics_Gnr"
                },
                # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\OpticsIn\Narrow [Indent level: 4],
                "Narrow": {
                    "opticsDisplayName": "NARROW",
                    "initFov": 0.0583333,
                    "minFov": 0.0583333,
                    "maxFov": 0.0583333,
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "visionMode": ["Normal","Ti"],
                    "thermalMode": [4],
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_ISU",
                    "gunnerOpticsEffect": [],
                    "hitPoint": "Hit_Optics_Gnr"
                }
            },
            # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets [Indent level: 3],
            "Turrets": {
                # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics [Indent level: 4]
                "CommanderOptics": {
                    "body": "obsTurret",
                    "gun": "obsGun",
                    "animationSourceBody": "obsTurret",
                    "animationSourceGun": "obsGun",
                    "memoryPointGunnerOptics": "commanderview",
                    "minElev": -5,
                    "maxElev": 5,
                    "initElev": 0,
                    "minTurn": -360,
                    "maxTurn": 360,
                    "initTurn": 0,
                    "hideWeaponsGunner": 1,
                    "weapons": ["rhsusf_weap_M257_8"],
                    "magazines": ["rhsusf_mag_L8A3_8"],
                    "turretInfoType": "RHS_RscODS_ISU",
                    "gunnerAction": "RHS_M2A2_CommanderOut",
                    "gunnerInAction": "RHS_M2A2_Commander",
                    "gunnerGetInAction": "GetInHigh",
                    "gunnerGetOutAction": "GetOutHigh",
                    "gunnerForceOptics": 1,
                    "gunnerDoor": "hatchC",
                    "gunnerOpticsModel": "rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|gunnerOptics_M2A2_2",
                    "gunnerOpticsEffect": [],
                    # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\ViewOptics [Indent level: 5],
                    "ViewOptics": {
                        "initAngleX": 0,
                        "minAngleX": -30,
                        "maxAngleX": 30,
                        "initAngleY": 0,
                        "minAngleY": -100,
                        "maxAngleY": 100,
                        "initFov": 0.155,
                        "minFov": 0.067,
                        "maxFov": 0.155
                    },
                    # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn [Indent level: 5],
                    "OpticsIn": {
                        # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\VisionBlock [Indent level: 6]
                        "VisionBlock": {
                            "opticsDisplayName": "periscope",
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "initfov": 0.7,
                            "minFov": 0.7,
                            "maxFov": 0.7,
                            "visionMode": ["Normal","NVG"],
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_vision_block",
                            "gunnerOpticsEffect": [],
                            "hitPoint": "Hit_Optics_Cdr_Peri"
                        },
                        # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Wide [Indent level: 6],
                        "Wide": {
                            "camPos": "gunnerview",
                            "opticsDisplayName": "WIDE",
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "initFov": 0.175,
                            "minFov": 0.175,
                            "maxFov": 0.175,
                            "visionMode": ["Normal","Ti"],
                            "thermalMode": [4],
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_ISU",
                            "gunnerOpticsEffect": [],
                            "hitPoint": "Hit_Optics_Gnr"
                        },
                        # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Narrow [Indent level: 6],
                        "Narrow": {
                            "opticsDisplayName": "NARROW",
                            "initFov": 0.0583333,
                            "minFov": 0.0583333,
                            "maxFov": 0.0583333,
                            "camPos": "gunnerview",
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "visionMode": ["Normal","Ti"],
                            "thermalMode": [4],
                            "gunnerOpticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_ISU",
                            "gunnerOpticsEffect": [],
                            "hitPoint": "Hit_Optics_Gnr"
                        }
                    },
                    "startEngine": 0,
                    "gunnerHasFlares": 1,
                    "viewGunnerInExternal": 1,
                    "outGunnerMayFire": 1,
                    "inGunnerMayFire": 1,
                    "showCrewAim": 0,
                    "allowTabLock": 0,
                    # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints [Indent level: 5],
                    "HitPoints": {
                        # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitTurretCom [Indent level: 6]
                        "HitTurretCom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.03,
                            "explosionShielding": 0.001,
                            "radius": 0.25,
                            "isTurret": 1
                        },
                        # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitGunCom [Indent level: 6],
                        "HitGunCom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.03,
                            "explosionShielding": 0.001,
                            "radius": 0.25,
                            "isGun": 1
                        },
                        # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\Hit_Optics_Cdr_Peri [Indent level: 6],
                        "Hit_Optics_Cdr_Peri": {
                            "armor": -40,
                            "explosionShielding": 0,
                            "name": "",
                            "visual": "vis_optics_Cdr_Peri",
                            "armorComponent": "Hit_Optics_Cdr_Peri",
                            "passThrough": 0
                        }
                    },
                    # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\Reflectors [Indent level: 5],
                    "Reflectors": {
                        # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\Reflectors\cabin [Indent level: 6]
                        "cabin": {
                            "color": [800,900,650],
                            "ambient": [5,5,5],
                            "intensity": 0.3,
                            "size": 1,
                            "innerAngle": 90,
                            "outerAngle": 165,
                            "coneFadeCoef": 1,
                            "position": "cabin_light",
                            "direction": "cabin_light_dir",
                            "hitpoint": "cabin_light",
                            "selection": "cabin_light",
                            "useFlare": 1,
                            "flareSize": 1,
                            "flareMaxDistance": 5,
                            "dayLight": 1,
                            "blinking": 0,
                            # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\Reflectors\cabin\Attenuation [Indent level: 7],
                            "Attenuation": {
                                "start": 0,
                                "constant": 0,
                                "linear": 1,
                                "quadratic": 50,
                                "hardLimitStart": 1,
                                "hardLimitEnd": 1.5
                            }
                        },
                        # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\Reflectors\cargo_light_1 [Indent level: 6],
                        "cargo_light_1": {
                            "color": [800,900,650],
                            "position": "cargo_light_1",
                            "direction": "cargo_light_1_dir",
                            "hitpoint": "cargo_light_1",
                            "selection": "cargo_light_1",
                            "intensity": 3,
                            "useFlare": 0,
                            "coneFadeCoef": 0.1,
                            "innerAngle": 140,
                            "outerAngle": 175,
                            # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\Turrets\CommanderOptics\Reflectors\cargo_light_1\Attenuation [Indent level: 7],
                            "Attenuation": {
                                "start": 0,
                                "constant": 0,
                                "linear": 1,
                                "quadratic": 70,
                                "hardLimitStart": 1.4,
                                "hardLimitEnd": 2
                            },
                            "ambient": [5,5,5],
                            "size": 1,
                            "flareSize": 1,
                            "flareMaxDistance": 5,
                            "dayLight": 1,
                            "blinking": 0
                        }
                    },
                    "memoryPointGunnerOutOptics": "commanderview",
                    "soundServo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",0.562341,1,30],
                    "soundServoVertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",0.562341,1,30],
                    "gunnerOutOpticsModel": "",
                    "isPersonTurret": 1,
                    "personTurretAction": "vehicle_turnout_1",
                    "minOutElev": -10,
                    "maxOutElev": 15,
                    "initOutElev": 0,
                    "minOutTurn": -45,
                    "maxOutTurn": 90,
                    "initOutTurn": 0,
                    "usePip": 2,
                    "animationSourceStickX": "com_turret_control_x",
                    "animationSourceStickY": "com_turret_control_y",
                    "gunnerRightHandAnimName": "com_turret_control",
                    "turretFollowFreeLook": 2,
                    "viewGunnerShadowAmb": 0.5,
                    "viewGunnerShadowDiff": 0.05,
                    "LODTurnedIn": 1000,
                    "LODOpticsIn": 0,
                    # Class: CfgVehicles\APC_Tracked_03_base_F\Turrets\MainTurret\Turrets\CommanderOptics\ViewGunner [Indent level: 5],
                    "ViewGunner": {
                        "initAngleX": -5,
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
                        "maxMoveZ": 0.1,
                        "speedZoomMaxSpeed": 1e+010,
                        "speedZoomMaxFOV": 0
                    },
                    "stabilizedInAxes": 3,
                    "maxHorizontalRotSpeed": 1.8,
                    "maxVerticalRotSpeed": 1.8,
                    # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Turrets\CommanderOptics\Components [Indent level: 5],
                    "Components": {
                        # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "VehicleSystemsDisplayManagerComponentLeft": {
                            # Class: VehicleSystemsTemplateLeftCommander\Components [Indent level: 0]
                            "Components": {
                                # Class: VehicleSystemsTemplateLeftCommander\Components\VehicleDriverDisplay [Indent level: 1]
                                "VehicleDriverDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateLeftCommander\Components\VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "VehiclePrimaryGunnerDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\EmptyDisplay [Indent level: 1],
                                "EmptyDisplay": {
                                    "componentType": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MinimapDisplay [Indent level: 1],
                                "MinimapDisplay": {
                                    "componentType": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MineDetectorDisplay [Indent level: 1],
                                "MineDetectorDisplay": {
                                    "componentType": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\CrewDisplay [Indent level: 1],
                                "CrewDisplay": {
                                    "componentType": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\UAVDisplay [Indent level: 1],
                                "UAVDisplay": {
                                    "componentType": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\SlingLoadDisplay [Indent level: 1],
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
                        # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "VehicleSystemsDisplayManagerComponentRight": {
                            # Class: VehicleSystemsTemplateRightCommander\Components [Indent level: 0]
                            "Components": {
                                # Class: VehicleSystemsTemplateRightCommander\Components\VehicleDriverDisplay [Indent level: 1]
                                "VehicleDriverDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateRightCommander\Components\VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "VehiclePrimaryGunnerDisplay": {
                                    "componentType": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\EmptyDisplay [Indent level: 1],
                                "EmptyDisplay": {
                                    "componentType": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MinimapDisplay [Indent level: 1],
                                "MinimapDisplay": {
                                    "componentType": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MineDetectorDisplay [Indent level: 1],
                                "MineDetectorDisplay": {
                                    "componentType": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\CrewDisplay [Indent level: 1],
                                "CrewDisplay": {
                                    "componentType": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\UAVDisplay [Indent level: 1],
                                "UAVDisplay": {
                                    "componentType": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\SlingLoadDisplay [Indent level: 1],
                                "SlingLoadDisplay": {
                                    "componentType": "SlingLoadDisplayComponent"
                                }
                            },
                            "componentType": "VehicleSystemsDisplayManager",
                            "right": 1,
                            "defaultDisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "proxyType": "CPCommander",
                    "proxyIndex": 1,
                    "gunnerName": "Commander",
                    "primaryGunner": 0,
                    "primaryObserver": 1,
                    "animationSourceHatch": "hatchCommander",
                    "animationSourceCamElev": "camElev",
                    "gunBeg": "",
                    "gunEnd": "",
                    "commanding": 2,
                    "gunnerOutOpticsColor": [0,0,0,1],
                    "gunnerOutForceOptics": 0,
                    "gunnerOutOpticsShowCursor": 0,
                    "gunnerOutOpticsEffect": [],
                    "memoryPointsGetInGunner": "pos commander",
                    "memoryPointsGetInGunnerDir": "pos commander dir",
                    "memoryPointGun": "gun_muzzle",
                    "selectionFireAnim": "zasleh_1",
                    "gunnerType": "",
                    "soundElevation": ["",0.00316228,1],
                    "minCamElev": -90,
                    "maxCamElev": 90,
                    "initCamElev": 0,
                    "primary": 1,
                    "hasGunner": 1,
                    "turretCanSee": 0,
                    "canUseScanners": 1,
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
                    "TurretSpec": {
                        "showHeadPhones": 0
                    },
                    "gunnerOpticsColor": [0,0,0,1],
                    "gunnerOpticsShowCursor": 0,
                    "gunnerFireAlsoInInternalCamera": 1,
                    "gunnerOutFireAlsoInInternalCamera": 1,
                    "gunnerUsesPilotView": 0,
                    "castGunnerShadow": 0,
                    "viewGunnerShadow": 1,
                    "ejectDeadGunner": 0,
                    "canHideGunner": -1,
                    "forceHideGunner": 0,
                    "showHMD": 0,
                    "lockWhenDriverOut": 0,
                    "lockWhenVehicleSpeed": -1,
                    "gunnerCompartments": "Compartment1",
                    "LODTurnedOut": -1,
                    "memoryPointsGetInGunnerPrecise": "",
                    "missileBeg": "spice rakety",
                    "missileEnd": "konec rakety",
                    "armorLights": 0.4,
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
                    "forceNVG": 0,
                    "isCopilot": 0,
                    "canEject": 1,
                    "gunnerLeftHandAnimName": "",
                    "gunnerLeftLegAnimName": "",
                    "gunnerRightLegAnimName": "",
                    "preciseGetInOut": 0,
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
                    "ace_fcs_Enabled": 0,
                    "ace_fcs_MinDistance": 200,
                    "ace_fcs_MaxDistance": 5500,
                    "ace_fcs_DistanceInterval": 5
                }
            },
            # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\HitPoints [Indent level: 3],
            "HitPoints": {
                # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\HitPoints\HitTurret [Indent level: 4]
                "HitTurret": {
                    "armor": -60,
                    "armorComponent": "Hit_Turret",
                    "name": "vez",
                    "visual": "vez",
                    "passThrough": 0,
                    "minimalHit": -0.3,
                    "explosionShielding": 0.001,
                    "radius": 0.08,
                    "isTurret": 1
                },
                # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\HitPoints\HitGun [Indent level: 4],
                "HitGun": {
                    "armor": -60,
                    "armorComponent": "Hit_Gun",
                    "name": "zbran",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": -0.3,
                    "explosionShielding": 0.001,
                    "radius": 0.1,
                    "isGun": 1
                },
                # Class: CfgVehicles\RHS_M2A2_Base\Turrets\MainTurret\HitPoints\Hit_Optics_Gnr [Indent level: 4],
                "Hit_Optics_Gnr": {
                    "armor": -40,
                    "explosionShielding": 0,
                    "name": "",
                    "visual": "vis_optics_Gnr",
                    "armorComponent": "Hit_Optics_Gnr",
                    "passThrough": 0
                }
            },
            "gunBeg": "Usti hlavne",
            "gunEnd": "Konec hlavne",
            "soundServo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner",0.562341,1,30],
            "soundServoVertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner_vertical",0.562341,1,30],
            "forceHideGunner": 0,
            "memoryPointGunnerOptics": "gunnerview",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsEffect": [],
            "gunnerOpticsEffect": [],
            "usePip": 2,
            "animationSourceStickX": "turret_control_x",
            "animationSourceStickY": "turret_control_y",
            "gunnerLeftHandAnimName": "turret_control",
            "LODTurnedIn": 1000,
            "LODOpticsIn": 0,
            "viewGunnerShadowAmb": 0.5,
            "viewGunnerShadowDiff": 0.05,
            "inGunnerMayFire": 1,
            "commanding": 1,
            # Class: CfgVehicles\APC_Tracked_03_base_F\Turrets\MainTurret\ViewGunner [Indent level: 3],
            "ViewGunner": {
                "initAngleX": -5,
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
                "maxMoveZ": 0.1,
                "continuous": 0,
                "speedZoomMaxSpeed": 1e+010,
                "speedZoomMaxFOV": 0
            },
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "primaryGunner": 1,
            # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Components [Indent level: 3],
            "Components": {
                # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: VehicleSystemsTemplateLeftGunner\Components [Indent level: 0]
                    "Components": {
                        # Class: VehicleSystemsTemplateLeftGunner\Components\VehicleDriverDisplay [Indent level: 1]
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateLeftGunner\Components\VehicleCommanderDisplay [Indent level: 1],
                        "VehicleCommanderDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\EmptyDisplay [Indent level: 1],
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MinimapDisplay [Indent level: 1],
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MineDetectorDisplay [Indent level: 1],
                        "MineDetectorDisplay": {
                            "componentType": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\CrewDisplay [Indent level: 1],
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\UAVDisplay [Indent level: 1],
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\SlingLoadDisplay [Indent level: 1],
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
                # Class: CfgVehicles\Tank_F\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "VehicleSystemsDisplayManagerComponentRight": {
                    # Class: VehicleSystemsTemplateRightGunner\Components [Indent level: 0]
                    "Components": {
                        # Class: VehicleSystemsTemplateRightGunner\Components\VehicleDriverDisplay [Indent level: 1]
                        "VehicleDriverDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateRightGunner\Components\VehicleCommanderDisplay [Indent level: 1],
                        "VehicleCommanderDisplay": {
                            "componentType": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\EmptyDisplay [Indent level: 1],
                        "EmptyDisplay": {
                            "componentType": "EmptyDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MinimapDisplay [Indent level: 1],
                        "MinimapDisplay": {
                            "componentType": "MinimapDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MineDetectorDisplay [Indent level: 1],
                        "MineDetectorDisplay": {
                            "componentType": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\CrewDisplay [Indent level: 1],
                        "CrewDisplay": {
                            "componentType": "CrewDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\UAVDisplay [Indent level: 1],
                        "UAVDisplay": {
                            "componentType": "UAVFeedDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight\Components\SlingLoadDisplay [Indent level: 1],
                        "SlingLoadDisplay": {
                            "componentType": "SlingLoadDisplayComponent"
                        }
                    },
                    "componentType": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "defaultDisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
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
            "primaryObserver": 0,
            "soundElevation": ["",0.00316228,1],
            "minTurn": -360,
            "maxTurn": 360,
            "initTurn": 0,
            "minOutElev": -4,
            "maxOutElev": 20,
            "initOutElev": 0,
            "minOutTurn": -60,
            "maxOutTurn": 60,
            "initOutTurn": 0,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "primary": 1,
            "hasGunner": 1,
            "turretCanSee": 0,
            "canUseScanners": 1,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
            "TurretSpec": {
                "showHeadPhones": 0
            },
            "gunnerOpticsColor": [0,0,0,1],
            "gunnerOpticsShowCursor": 0,
            "gunnerOutOpticsColor": [0,0,0,1],
            "memoryPointGunnerOutOptics": "",
            "gunnerOutForceOptics": 0,
            "gunnerOutOpticsShowCursor": 0,
            "gunnerFireAlsoInInternalCamera": 1,
            "gunnerOutFireAlsoInInternalCamera": 1,
            "gunnerUsesPilotView": 0,
            "castGunnerShadow": 0,
            "viewGunnerShadow": 1,
            "ejectDeadGunner": 0,
            "canHideGunner": -1,
            "outGunnerMayFire": 0,
            "showHMD": 0,
            "lockWhenVehicleSpeed": -1,
            "gunnerCompartments": "Compartment1",
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
            "gunnerRightHandAnimName": "",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "preciseGetInOut": 0,
            "turretFollowFreeLook": 0,
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
            "memoryPointGun": "kulas",
            "ace_fcs_Enabled": 0,
            "ace_fcs_MinDistance": 200,
            "ace_fcs_MaxDistance": 5500,
            "ace_fcs_DistanceInterval": 5
        }
    },
    "driverAction": "RHS_M2A2_DriverOut",
    "driverInAction": "RHS_M2A2_Driver",
    "cargoAction": ["RHS_M113_Cargo03","RHS_M113_Cargo03","RHS_M113_Cargo03","RHS_M113_Cargo02","RHS_M113_Cargo02","RHS_M113_Cargo02"],
    "insideSoundCoef": 0.9,
    # Class: CfgVehicles\RHS_M2A2_Base\Exhausts [Indent level: 1],
    "Exhausts": {
        # Class: CfgVehicles\RHS_M2A2_Base\Exhausts\Exhaust1 [Indent level: 2]
        "Exhaust1": {
            "position": "vyfuk start",
            "direction": "vyfuk konec",
            "effect": "ExhaustEffectTankSide"
        }
    },
    # Class: CfgVehicles\RHS_M2A2_Base\ViewPilot [Indent level: 1],
    "ViewPilot": {
        "initAngleX": 7,
        "minAngleX": -15,
        "maxAngleX": 25,
        "initAngleY": 0,
        "minAngleY": -90,
        "maxAngleY": 90,
        "initFov": 0.9,
        "minFov": 0.25,
        "maxFov": 1.25,
        "minMoveX": -0.075,
        "maxMoveX": 0.075,
        "minMoveY": -0.075,
        "maxMoveY": 0.075,
        "minMoveZ": -0.075,
        "maxMoveZ": 0.1,
        "speedZoomMaxSpeed": 0,
        "speedZoomMaxFOV": 0.7
    },
    # Class: CfgVehicles\RHS_M2A2_Base\ViewOptics [Indent level: 1],
    "ViewOptics": {
        "visionMode": ["Normal","NVG"],
        "initFov": 0.7,
        "minFov": 0.7,
        "maxFov": 0.7,
        "initAngleX": 0,
        "minAngleX": -75,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -170,
        "maxAngleY": 170,
        "minMoveX": -0.5,
        "maxMoveX": 0.5,
        "minMoveY": -0.025,
        "maxMoveY": 0.1,
        "minMoveZ": -0.3,
        "maxMoveZ": 0.5,
        "speedZoomMaxSpeed": 0,
        "speedZoomMaxFOV": 0.7
    },
    # Class: CfgVehicles\RHS_M2A2_Base\DriverOpticsIn [Indent level: 1],
    "DriverOpticsIn": {
        # Class: CfgVehicles\RHS_M2A2_Base\DriverOpticsIn\Wide [Indent level: 2]
        "Wide": {
            "opticsModel": "rhsusf|addons|rhsusf_optics|data|rhsusf_vision_block",
            "hitpoint": "Hit_Optics_Dvr_Peri",
            "visionMode": ["Normal","NVG"],
            "initFov": 0.7,
            "minFov": 0.7,
            "maxFov": 0.7,
            "initAngleX": 0,
            "minAngleX": -75,
            "maxAngleX": 85,
            "initAngleY": 0,
            "minAngleY": -170,
            "maxAngleY": 170,
            "minMoveX": -0.5,
            "maxMoveX": 0.5,
            "minMoveY": -0.025,
            "maxMoveY": 0.1,
            "minMoveZ": -0.3,
            "maxMoveZ": 0.5,
            "speedZoomMaxSpeed": 0,
            "speedZoomMaxFOV": 0.7
        }
    },
    # Class: CfgVehicles\RHS_M2A2_Base\TransportBackpacks [Indent level: 1],
    "TransportBackpacks": {
        # Class: CfgVehicles\RHS_M2A2_Base\TransportBackpacks\_xx_rhsusf_falconii [Indent level: 2]
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 8
        }
    },
    # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines [Indent level: 1],
    "TransportMagazines": {
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 75
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhsusf_100Rnd_556x45_soft_pouch [Indent level: 2],
        "_xx_rhsusf_100Rnd_556x45_soft_pouch": {
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch",
            "count": 11
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhsusf_100Rnd_762x51 [Indent level: 2],
        "_xx_rhsusf_100Rnd_762x51": {
            "magazine": "rhsusf_100Rnd_762x51",
            "count": 11
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhs_fgm148_magazine_AT [Indent level: 2],
        "_xx_rhs_fgm148_magazine_AT": {
            "magazine": "rhs_fgm148_magazine_AT",
            "count": 4
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhs_mag_M441_HE [Indent level: 2],
        "_xx_rhs_mag_M441_HE": {
            "magazine": "rhs_mag_M441_HE",
            "count": 20
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhs_mag_M714_white [Indent level: 2],
        "_xx_rhs_mag_M714_white": {
            "magazine": "rhs_mag_M714_white",
            "count": 8
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhs_mag_M662_red [Indent level: 2],
        "_xx_rhs_mag_M662_red": {
            "magazine": "rhs_mag_M662_red",
            "count": 4
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 10
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 4
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 4
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportMagazines\_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 10
        }
    },
    # Class: CfgVehicles\RHS_M2A2_Base\TransportItems [Indent level: 1],
    "TransportItems": {
        # Class: CfgVehicles\RHS_M2A2_Base\TransportItems\_xx_FirstAidKit [Indent level: 2]
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportItems\_xx_Medikit [Indent level: 2],
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 2
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportItems\_xx_Toolkit [Indent level: 2],
        "_xx_Toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles\RHS_M2A2_Base\TransportWeapons [Indent level: 1],
    "TransportWeapons": {
        # Class: CfgVehicles\RHS_M2A2_Base\TransportWeapons\_xx_rhs_weap_m4_carryhandle_pmag [Indent level: 2]
        "_xx_rhs_weap_m4_carryhandle_pmag": {
            "weapon": "rhs_weap_m4_carryhandle_pmag",
            "count": 4
        },
        # Class: CfgVehicles\RHS_M2A2_Base\TransportWeapons\_xx_rhs_weap_fgm148 [Indent level: 2],
        "_xx_rhs_weap_fgm148": {
            "weapon": "rhs_weap_fgm148",
            "count": 2
        }
    },
    # Class: CfgVehicles\RHS_M2A2_Base\EventHandlers [Indent level: 1],
    "EventHandlers": {
        # Class: CfgVehicles\RHS_M2A2_Base\EventHandlers\RHSUSF_EventHandlers [Indent level: 2]
        "RHSUSF_EventHandlers": {
            "hitpart": "_this call rhsusf_fnc_hitSpall",
            "getIn": "_this call rhs_fnc_m2_doors",
            "getOut": "_this call rhs_fnc_m2_doors",
            "engine": "[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay"
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
    # Class: CfgVehicles\RHS_M2A2_Base\Reflectors [Indent level: 1],
    "Reflectors": {
        # Class: CfgVehicles\RHS_M2A2_Base\Reflectors\Left [Indent level: 2]
        "Left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "l svetlo",
            "direction": "konec l svetla",
            "hitpointClass": "Hit_LightL",
            "selection": "L svetlo",
            "size": 1,
            "innerAngle": 30,
            "outerAngle": 100,
            "coneFadeCoef": 10,
            "intensity": 1,
            "useFlare": 1,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\RHS_M2A2_Base\Reflectors\Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Reflectors\Right [Indent level: 2],
        "Right": {
            "position": "p svetlo",
            "direction": "konec p svetla",
            "hitpointClass": "Hit_LightR",
            "selection": "P svetlo",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerAngle": 30,
            "outerAngle": 100,
            "coneFadeCoef": 10,
            "intensity": 1,
            "useFlare": 1,
            "dayLight": 0,
            "flareSize": 1,
            # Class: CfgVehicles\RHS_M2A2_Base\Reflectors\Left\Attenuation [Indent level: 3],
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardLimitStart": 30,
                "hardLimitEnd": 60
            }
        }
    },
    "aggregateReflectors": [["Left"],["Right"]],
    "armorLights": 0.1,
    # Class: CfgVehicles\RHS_M2A2_Base\UserActions [Indent level: 1],
    "UserActions": {
        # Class: CfgVehicles\RHS_M2A2_Base\UserActions\OpenCargoDoor [Indent level: 2]
        "OpenCargoDoor": {
            "displayName": "Open ramp",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "this doorPhase 'ramp' == 0 and {(call rhsusf_fnc_findPlayer) in this};",
            "statement": "this animateDoor ['ramp', 1];this setVariable ['ramp_handler',1,true]",
            "onlyforplayer": 1,
            "shortcut": "user12"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\UserActions\CloseCargoDoor [Indent level: 2],
        "CloseCargoDoor": {
            "displayName": "Close ramp",
            "condition": "this doorPhase 'ramp' > 0 and {(call rhsusf_fnc_findPlayer) in this};",
            "statement": "this animateDoor ['ramp', 0];this setVariable ['ramp_handler',0,true]",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1,
            "shortcut": "user12"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\UserActions\ToggleLight [Indent level: 2],
        "ToggleLight": {
            "displayName": "Toggle interior light",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "player in this;",
            "statement": "[this,'cargolights_hide',[0,0]] call rhs_fnc_toggleIntLight",
            "onlyforplayer": 1
        }
    },
    # Class: CfgVehicles\RHS_M2A2_Base\Attributes [Indent level: 1],
    "Attributes": {
        # Class: CfgVehicles\RHS_M2A2_Base\Attributes\ObjectTexture [Indent level: 2]
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Attributes\rhs_hideIFFPanel [Indent level: 2],
        "rhs_hideIFFPanel": {
            "displayName": "Hide IFF Panel",
            "property": "rhs_hideIFFPanel",
            "control": "CheckboxNumber",
            "expression": "_this animate ['IFF_Panels_Hide',_value,true]",
            "defaultValue": "0"
        },
        # Class: CfgVehicles\RHS_M2A2_Base\Attributes\OpenRamp [Indent level: 2],
        "OpenRamp": {
            "control": "CheckboxNumber",
            "defaultValue": "0",
            "displayName": "Open rear ramp",
            "property": "OpenRamp",
            "expression": "_this animateDoor ['ramp', _value,true];_this setVariable ['ramp_handler',_value,true]"
        }
    },
    "ace_refuel_fuelCapacity": 746,
    "soundTurnIn": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnOut": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnInInternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundTurnOutInternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "BushCrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_01",0.630957,1,100],
    "BushCrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_02",0.630957,1,100],
    "BushCrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_03",0.630957,1,100],
    "soundBushCrash": ["BushCrash1",0.33,"BushCrash2",0.33,"BushCrash3",0.33],
    "buildCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "buildCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "ArmorCrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "ArmorCrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "_generalMacro": "APC_Tracked_03_base_F",
    "features": "Randomization: No						<br />Camo selections: 2 - turret, hull						<br />Script door sources: None						<br />Script animations: HideTurret						<br />Executed scripts: None						<br />Firing from vehicles: No						<br />Slingload: No						<br />Cargo proxy indexes: 1 to 7",
    "dampingRateFullThrottle": 0.3,
    "dampingRateZeroThrottleClutchEngaged": 3,
    "dampingRateZeroThrottleClutchDisengaged": 0.25,
    "antiRollbarForceCoef": 15,
    "antiRollbarForceLimit": 12,
    "antiRollbarSpeedMin": 30,
    "antiRollbarSpeedMax": 55,
    # Class: CfgVehicles\APC_Tracked_03_base_F\MFD [Indent level: 1],
    "MFD": {
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading [Indent level: 2]
        "MFD_Driver_Heading": {
            "topLeft": "MFD_1_TL",
            "topRight": "MFD_1_TR",
            "bottomLeft": "MFD_1_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading\Draw [Indent level: 3],
            "Draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading\Draw\Driver_Heading [Indent level: 4],
                "Driver_Heading": {
                    "type": "text",
                    "source": "heading",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1,0],1],
                    "down": [[0.5,0.81],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading_text [Indent level: 2],
        "MFD_Driver_Heading_text": {
            "topLeft": "MFD_Driver_1_TL",
            "topRight": "MFD_Driver_1_TR",
            "bottomLeft": "MFD_Driver_1_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading_text\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading_text\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading_text\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading_text\Draw\Driver_Heading [Indent level: 4],
                "Driver_Heading": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.45,0.02],1],
                    "right": [[0.7,0.02],1],
                    "down": [[0.45,0.87],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading_second [Indent level: 2],
        "MFD_Driver_Heading_second": {
            "topLeft": "MFD_Driver_2_TL",
            "topRight": "MFD_Driver_2_TR",
            "bottomLeft": "MFD_Driver_2_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading_second\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading_second\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading_second\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Driver_Heading_second\Draw\Driver_Heading [Indent level: 4],
                "Driver_Heading": {
                    "type": "text",
                    "source": "heading",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.45,0],1],
                    "right": [[0.95,0],1],
                    "down": [[0.45,0.81],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_Damage [Indent level: 2],
        "MFD_Commander_Display_Damage": {
            "topLeft": "mfd_com_TL",
            "topRight": "mfd_com_TR",
            "bottomLeft": "mfd_com_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0,0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_Damage\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_Damage\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_Damage\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_Damage\Draw\Damage_Hull [Indent level: 4],
                "Damage_Hull": {
                    "type": "text",
                    "source": "static",
                    "text": "HULL",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.04,0.18],1],
                    "right": [[0.065,0.18],1],
                    "down": [[0.04,0.44],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_Damage\Draw\Damage_Engine [Indent level: 4],
                "Damage_Engine": {
                    "type": "text",
                    "source": "static",
                    "text": "ENG",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.11,0.18],1],
                    "right": [[0.135,0.18],1],
                    "down": [[0.11,0.44],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_Damage\Draw\Damage_Fuel [Indent level: 4],
                "Damage_Fuel": {
                    "type": "text",
                    "source": "static",
                    "text": "FUEL",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.178,0.18],1],
                    "right": [[0.203,0.18],1],
                    "down": [[0.178,0.44],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_Damage\Draw\Damage_Wheels [Indent level: 4],
                "Damage_Wheels": {
                    "type": "text",
                    "source": "static",
                    "text": "TRK",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.04,0.55],1],
                    "right": [[0.065,0.55],1],
                    "down": [[0.04,0.81],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_Damage\Draw\Damage_Gun [Indent level: 4],
                "Damage_Gun": {
                    "type": "text",
                    "source": "static",
                    "text": "GUN",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.11,0.55],1],
                    "right": [[0.135,0.55],1],
                    "down": [[0.11,0.81],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_Damage\Draw\Damage_Turret [Indent level: 4],
                "Damage_Turret": {
                    "type": "text",
                    "source": "static",
                    "text": "TRT",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.178,0.55],1],
                    "right": [[0.203,0.55],1],
                    "down": [[0.178,0.81],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display [Indent level: 2],
        "MFD_Commander_Display": {
            "topLeft": "mfd_com_TL",
            "topRight": "mfd_com_TR",
            "bottomLeft": "mfd_com_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Bones [Indent level: 3],
            "Bones": {
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Bones\FuelScale [Indent level: 4]
                "FuelScale": {
                    "type": "linear",
                    "source": "fuel",
                    "sourceIndex": 1,
                    "sourceScale": 1,
                    "min": 0,
                    "max": 1,
                    "minPos": [0,0],
                    "maxPos": [-0.09,0]
                }
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Main_Gun [Indent level: 4],
                "Main_Gun": {
                    "type": "text",
                    "source": "static",
                    "text": "MAIN GUN",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.273,0.18],1],
                    "right": [[0.298,0.18],1],
                    "down": [[0.273,0.44],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Main_Gun_Ammo_count [Indent level: 4],
                "Main_Gun_Ammo_count": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 0,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.273,0.55],1],
                    "right": [[0.298,0.55],1],
                    "down": [[0.273,0.81],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Main_Gun_Ammo_Type_text [Indent level: 4],
                "Main_Gun_Ammo_Type_text": {
                    "type": "text",
                    "source": "static",
                    "text": "TYPE",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.385,0.18],1],
                    "right": [[0.41,0.18],1],
                    "down": [[0.385,0.44],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Main_Gun_Ammo_Type [Indent level: 4],
                "Main_Gun_Ammo_Type": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.385,0.55],1],
                    "right": [[0.41,0.55],1],
                    "down": [[0.385,0.81],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Coax [Indent level: 4],
                "Coax": {
                    "type": "text",
                    "source": "static",
                    "text": "COAX",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.498,0.18],1],
                    "right": [[0.523,0.18],1],
                    "down": [[0.498,0.44],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Coax_Ammo_count [Indent level: 4],
                "Coax_Ammo_count": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 1,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.493,0.55],1],
                    "right": [[0.518,0.55],1],
                    "down": [[0.493,0.81],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Azimuth [Indent level: 4],
                "Azimuth": {
                    "type": "text",
                    "source": "static",
                    "text": "GUN AZIM",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.605,0.18],1],
                    "right": [[0.63,0.18],1],
                    "down": [[0.605,0.44],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Azimuth_number [Indent level: 4],
                "Azimuth_number": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.61,0.55],1],
                    "right": [[0.635,0.55],1],
                    "down": [[0.61,0.81],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Smoke [Indent level: 4],
                "Smoke": {
                    "type": "text",
                    "source": "static",
                    "text": "SMOKE",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.717,0.18],1],
                    "right": [[0.742,0.18],1],
                    "down": [[0.717,0.44],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel_background_white [Indent level: 4],
                "Fuel_background_white": {
                    "color": [0.2,0.2,0.2],
                    "alpha": 0.1,
                    "condition": "1",
                    # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel_background_white\Background [Indent level: 5],
                    "Background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],[[0.877,0.7],1],[[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel_background_green [Indent level: 4],
                "Fuel_background_green": {
                    "color": [0,0.7,0],
                    "condition": "fuel>=0.5",
                    # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel_background_green\Background [Indent level: 5],
                    "Background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],["FuelScale",[0.877,0.7],1],["FuelScale",[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel_background_yellow [Indent level: 4],
                "Fuel_background_yellow": {
                    "color": [0.9,0.7,0],
                    "condition": "fuel<0.5",
                    # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel_background_yellow\Background [Indent level: 5],
                    "Background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],["FuelScale",[0.877,0.7],1],["FuelScale",[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel_background_red [Indent level: 4],
                "Fuel_background_red": {
                    "color": [0.7,0,0],
                    "condition": "fuel<0.3",
                    # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel_background_red\Background [Indent level: 5],
                    "Background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],["FuelScale",[0.877,0.7],1],["FuelScale",[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel [Indent level: 4],
                "Fuel": {
                    "type": "text",
                    "source": "static",
                    "text": "FUEL",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.83,0.18],1],
                    "right": [[0.855,0.18],1],
                    "down": [[0.83,0.44],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel_number [Indent level: 4],
                "Fuel_number": {
                    "type": "text",
                    "source": "fuel",
                    "sourceScale": 100,
                    "sourceLength": 1,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.835,0.4],1],
                    "right": [[0.86,0.4],1],
                    "down": [[0.835,0.66],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display\Draw\Fuel_percent_sign [Indent level: 4],
                "Fuel_percent_sign": {
                    "type": "text",
                    "source": "static",
                    "text": "%",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.845,0.4],1],
                    "right": [[0.87,0.4],1],
                    "down": [[0.845,0.66],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_OnScreen [Indent level: 2],
        "MFD_Commander_OnScreen": {
            "topLeft": "PIP_COM_TL",
            "topRight": "PIP_COM_TR",
            "bottomLeft": "PIP_COM_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0,0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_OnScreen\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_OnScreen\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_OnScreen\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_OnScreen\Draw\Azimuth_number [Indent level: 4],
                "Azimuth_number": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.22,0.435],1],
                    "right": [[0.245,0.435],1],
                    "down": [[0.22,0.472],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_OnScreen\Draw\Elevation_Text [Indent level: 4],
                "Elevation_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "E: ",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.2,0.28],1],
                    "right": [[0.225,0.28],1],
                    "down": [[0.2,0.317],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_OnScreen\Draw\Elevation_Number [Indent level: 4],
                "Elevation_Number": {
                    "type": "text",
                    "source": "[y]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "sourcePrecision": 1,
                    "refreshRate": 0,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.23,0.28],1],
                    "right": [[0.255,0.28],1],
                    "down": [[0.23,0.317],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_OnScreen\Draw\Lased_Range [Indent level: 4],
                "Lased_Range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.75,0.28],1],
                    "right": [[0.775,0.28],1],
                    "down": [[0.75,0.317],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_OnScreen\Draw\VisionMode_Text [Indent level: 4],
                "VisionMode_Text": {
                    "type": "text",
                    "source": "static",
                    "text": "WFOV",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.75,0.65],1],
                    "right": [[0.775,0.65],1],
                    "down": [[0.75,0.687],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_OnScreen\Draw\VisionMode_String [Indent level: 4],
                "VisionMode_String": {
                    "type": "text",
                    "source": "visionMode",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.825,0.65],1],
                    "right": [[0.85,0.65],1],
                    "down": [[0.825,0.687],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_MainTurret [Indent level: 2],
        "MFD_Commander_Display_MainTurret": {
            "topLeft": "mfd_com_TL",
            "topRight": "mfd_com_TR",
            "bottomLeft": "mfd_com_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0,0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_MainTurret\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_MainTurret\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_MainTurret\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Display_MainTurret\Draw\Smoke_ammo [Indent level: 4],
                "Smoke_ammo": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "sourceIndex": 0,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.72,0.55],1],
                    "right": [[0.745,0.55],1],
                    "down": [[0.72,0.81],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Heading [Indent level: 2],
        "MFD_Commander_Heading": {
            "topLeft": "mfd_com_dir_TL",
            "topRight": "mfd_com_dir_TR",
            "bottomLeft": "mfd_com_dir_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0,0],
            "font": "LCD14",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Heading\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Heading\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Heading\Draw [Indent level: 3],
            "Draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Commander_Heading\Draw\Driver_Heading [Indent level: 4],
                "Driver_Heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1,0],1],
                    "down": [[0.5,0.81],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Ready_To_Fire [Indent level: 2],
        "MFD_Gunner_Ready_To_Fire": {
            "topLeft": "mfd_gun_cli_TL",
            "topRight": "mfd_gun_cli_TR",
            "bottomLeft": "mfd_gun_cli_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Ready_To_Fire\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Ready_To_Fire\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Ready_To_Fire\Draw [Indent level: 3],
            "Draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Ready_To_Fire\Draw\Top_text [Indent level: 4],
                "Top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "READY TO",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.45,0.05],1],
                    "right": [[0.67,0.05],1],
                    "down": [[0.45,0.55],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Ready_To_Fire\Draw\Bottom_text [Indent level: 4],
                "Bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "FIRE",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.465,0.45],1],
                    "right": [[0.685,0.45],1],
                    "down": [[0.465,0.95],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display [Indent level: 2],
        "MFD_Gunner_Display": {
            "topLeft": "mfd_gun_TL",
            "topRight": "mfd_gun_TR",
            "bottomLeft": "mfd_gun_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\Draw\Main_armament [Indent level: 4],
                "Main_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "MAIN ARMAMENT",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,-0.003],1],
                    "right": [[0.075,-0.003],1],
                    "down": [[0.015,0.075],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\Draw\Machinegun [Indent level: 4],
                "Machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "COAX",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.31],1],
                    "right": [[0.075,0.31],1],
                    "down": [[0.015,0.388],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\Draw\Main_armament_ammo_type [Indent level: 4],
                "Main_armament_ammo_type": {
                    "type": "text",
                    "source": "static",
                    "text": "AMMO TYPE",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.545,-0.003],1],
                    "right": [[0.605,-0.003],1],
                    "down": [[0.545,0.075],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\Draw\Lased_distance_elevation [Indent level: 4],
                "Lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "LASED DST",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.84],1],
                    "right": [[0.075,0.84],1],
                    "down": [[0.015,0.918],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\Draw\Azimut [Indent level: 4],
                "Azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.025,0.915],1],
                    "right": [[0.085,0.915],1],
                    "down": [[0.025,0.993],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\Draw\Damage [Indent level: 4],
                "Damage": {
                    "type": "text",
                    "source": "static",
                    "text": "DAMAGE",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.39],1],
                    "right": [[0.075,0.39],1],
                    "down": [[0.015,0.468],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\Draw\Heading [Indent level: 4],
                "Heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 0.2,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.34,0.915],1],
                    "right": [[0.4,0.915],1],
                    "down": [[0.34,0.993],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Display\Draw\Lased_Range [Indent level: 4],
                "Lased_Range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.335,0.84],1],
                    "right": [[0.395,0.84],1],
                    "down": [[0.335,0.918],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type [Indent level: 2],
        "MFD_Gunner_Main_Armament_Ammo_Type": {
            "topLeft": "mfd_gun_TL",
            "topRight": "mfd_gun_TR",
            "bottomLeft": "mfd_gun_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableParallax": 0,
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Main_Armament_Ammo_Type\Draw\Gunner_AmmoType [Indent level: 4],
                "Gunner_AmmoType": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.56,0.09],1],
                    "right": [[0.62,0.09],1],
                    "down": [[0.56,0.168],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Coax_Ammo [Indent level: 2],
        "MFD_Gunner_Coax_Ammo": {
            "topLeft": "mfd_gun_TL",
            "topRight": "mfd_gun_TR",
            "bottomLeft": "mfd_gun_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Coax_Ammo\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Coax_Ammo\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Coax_Ammo\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Coax_Ammo\Draw\Gunner_Text_1 [Indent level: 4],
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "sourceIndex": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.36,0.31],1],
                    "right": [[0.42,0.31],1],
                    "down": [[0.36,0.388],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament [Indent level: 2],
        "MFD_Gunner_AmmoIndicator_Main_Armament": {
            "topLeft": "mfd_gun_TL",
            "topRight": "mfd_gun_TR",
            "bottomLeft": "mfd_gun_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "EtelkaMonospacePro",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_1 [Indent level: 4],
                "Main_Armament_Ammo_Type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "MP-T",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.065],1],
                    "right": [[0.075,0.065],1],
                    "down": [[0.015,0.143],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Gunner_Text_1 [Indent level: 4],
                "Gunner_Text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 0,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.375,0.065],1],
                    "right": [[0.435,0.065],1],
                    "down": [[0.375,0.143],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Main_Armament_Ammo_Type_2 [Indent level: 4],
                "Main_Armament_Ammo_Type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "APFSDS-T",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshRate": 0.1,
                    "pos": [[0.015,0.125],1],
                    "right": [[0.06,0.125],1],
                    "down": [[0.015,0.203],1]
                },
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoIndicator_Main_Armament\Draw\Gunner_Text_2 [Indent level: 4],
                "Gunner_Text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourceScale": 1,
                    "sourceLength": 2,
                    "sourceIndex": 0,
                    "sourcePrecision": 1,
                    "scale": 1,
                    "align": "left",
                    "refreshRate": 0.1,
                    "pos": [[0.375,0.125],1],
                    "right": [[0.435,0.125],1],
                    "down": [[0.375,0.203],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Range [Indent level: 2],
        "MFD_Gunner_Range": {
            "topLeft": "MFD_5_TL",
            "topRight": "MFD_5_TR",
            "bottomLeft": "MFD_5_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableParallax": 0,
            "turret": [0],
            "font": "LCD14",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Range\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Range\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Range\Draw\Gunner_Range [Indent level: 4],
                "Gunner_Range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourceScale": 1,
                    "sourceLength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.48,-0.1],1],
                    "right": [[0.88,-0.1],1],
                    "down": [[0.48,1],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoType [Indent level: 2],
        "MFD_Gunner_AmmoType": {
            "topLeft": "MFD_4_TL",
            "topRight": "MFD_4_TR",
            "bottomLeft": "MFD_4_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableParallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoType\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoType\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_AmmoType\Draw\Gunner_AmmoType [Indent level: 4],
                "Gunner_AmmoType": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.455,0.2],1],
                    "right": [[0.655,0.2],1],
                    "down": [[0.455,0.7],1]
                }
            }
        },
        # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Heading [Indent level: 2],
        "MFD_Gunner_Heading": {
            "topLeft": "MFD_Gunner_heading_TL",
            "topRight": "MFD_Gunner_heading_TR",
            "bottomLeft": "MFD_Gunner_heading_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "LCD14",
            "turret": [0],
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Heading\Bones [Indent level: 3],
            "Bones": {
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Heading\Draw [Indent level: 3],
            "Draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles\APC_Tracked_03_base_F\MFD\MFD_Gunner_Heading\Draw\Heading [Indent level: 4],
                "Heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourceScale": 1,
                    "sourceLength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshRate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[0.7,0],1],
                    "down": [[0.5,0.9],1]
                }
            }
        }
    },
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 1,
    "wheelCircumference": 1.95,
    "viewDriverShadowAmb": 0.5,
    "viewDriverShadowDiff": 0.05,
    "driverLeftLegAnimName": "pedal_brake",
    "driverRightLegAnimName": "pedal_thrust",
    "driverInfoPanelCameraPos": "driverview_old",
    "extCameraPosition": [0,3,-10],
    "crewExplosionProtection": 0.9995,
    "crewVulnerable": 1,
    "memoryPointTaskMarker": "TaskMarker_1_pos",
    "animationSourceHatch": "",
    "selectionFireAnim": "",
    "cost": 1e+006,
    # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights [Indent level: 1],
    "compartmentsLights": {
        # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1 [Indent level: 2]
        "Comp1": {
            # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light1 [Indent level: 3]
            "Light1": {
                "color": [25,22,16],
                "ambient": [0,0,0],
                "intensity": 0.3,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light1\Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                },
                "point": "light_interior1"
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light2 [Indent level: 3],
            "Light2": {
                "point": "light_interior2",
                "color": [25,22,16],
                "ambient": [0,0,0],
                "intensity": 0.6,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light1\Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light3 [Indent level: 3],
            "Light3": {
                "point": "light_interior3",
                "color": [25,22,16],
                "ambient": [0,0,0],
                "intensity": 0.6,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light1\Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light4 [Indent level: 3],
            "Light4": {
                "point": "light_interior4",
                "color": [25,25,25],
                "ambient": [0,0,0],
                "intensity": 5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light1\Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light5 [Indent level: 3],
            "Light5": {
                "point": "light_interior5",
                "color": [25,25,25],
                "ambient": [0,0,0],
                "intensity": 5,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light1\Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            },
            # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light6 [Indent level: 3],
            "Light6": {
                "point": "light_interior6",
                "color": [25,25,25],
                "ambient": [0,0,0],
                "intensity": 10,
                "size": 0,
                "useFlare": 0,
                "flareSize": 0,
                "flareMaxDistance": 0,
                "dayLight": 0,
                "blinking": 0,
                # Class: CfgVehicles\APC_Tracked_03_base_F\compartmentsLights\Comp1\Light1\Attenuation [Indent level: 4],
                "Attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardLimitStart": 0.15,
                    "hardLimitEnd": 1.15
                }
            }
        }
    },
    "soundLocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",1,1],
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_2",0.316228,1],
    "smokeLauncherGrenadeCount": 10,
    "smokeLauncherVelocity": 14,
    "smokeLauncherOnTurret": 1,
    "smokeLauncherAngle": 120,
    "animationList": ["showBags",0,"showBags2",0,"showCamonetHull",0,"showCamonetTurret",0,"showTools",0,"showSLATHull",0,"showSLATTurret",0],
    "attenuationeffecttype": "jsrs_tank_attenuation",
    "crash0": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_01.ogg",1.5,1,300],
    "crash1": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_02.ogg",1.5,1,300],
    "crash2": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_03.ogg",1.5,1,300],
    "crash3": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_04.ogg",1.5,1,300],
    "crash4": ["|jsrs_soundmod_complete|JSRS_Soundmod_Soundfiles|land_vehicles|noises|crash_light|crash_vehicle_05.ogg",1.5,1,300],
    "soundcrashes": ["crash0",0.2,"crash1",0.2,"crash2",0.2,"crash3",0.2,"crash4",0.2],
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
    "driverCanSee": "1 + 2 + 4 + 8 + 32",
    "gunnerCanSee": "1 + 2 + 4 + 8 + 32",
    "commanderCanSee": "1 + 2 + 4 + 8 + 32",
    "sensorPosition": "gunnerView",
    "audible": 18,
    "sensitivityEar": "0.0075 /3",
    "turnCoef": 5,
    "steerAheadSimul": 0.3,
    "steerAheadPlan": 0.4,
    "brakeDistance": 5,
    "precision": 10,
    "hideProxyInCombat": 1,
    "radarTarget": 1,
    "radarTargetSize": 1.2,
    "visualTarget": 1,
    "visualTargetSize": 1,
    "irTargetSize": 1.2,
    "irScanRangeMax": 0,
    "irScanRangeMin": 0,
    "irScanToEyeFactor": 1,
    "enableRadio": 1,
    "countermeasureActivationRadius": 2000,
    "memoryPointCargoLight": "cargo light",
    "dampersBumpCoef": 4.5,
    "minTotalDamageThreshold": 0.005,
    "crewCrashProtection": 0.25,
    "secondaryExplosion": -1,
    "fuelExplosionPower": 1,
    "transportMaxWeapons": 12,
    "transportMaxMagazines": 128,
    "transportMaxBackpacks": 12,
    "maximumLoad": 3000,
    "supplyRadius": -1,
    "memoryPointSupply": "doplnovani",
    # Class: CfgVehicles\Tank_F\CamShake [Indent level: 1],
    "CamShake": {
        "power": 5,
        "frequency": 20,
        "distance": 20,
        "minSpeed": 5
    },
    "camShakeCoef": 0,
    # Class: CfgVehicles\Tank_F\Components [Indent level: 1],
    "Components": {
        # Class: CfgVehicles\Tank_F\Components\VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: VehicleSystemsTemplateLeftDriver\Components [Indent level: 0]
            "Components": {
                # Class: VehicleSystemsTemplateLeftDriver\Components\VehiclePrimaryGunnerDisplay [Indent level: 1]
                "VehiclePrimaryGunnerDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateLeftDriver\Components\VehicleCommanderDisplay [Indent level: 1],
                "VehicleCommanderDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\EmptyDisplay [Indent level: 1],
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MinimapDisplay [Indent level: 1],
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\MineDetectorDisplay [Indent level: 1],
                "MineDetectorDisplay": {
                    "componentType": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\CrewDisplay [Indent level: 1],
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\UAVDisplay [Indent level: 1],
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft\Components\SlingLoadDisplay [Indent level: 1],
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
        # Class: CfgVehicles\Tank_F\Components\VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "VehicleSystemsDisplayManagerComponentRight": {
            # Class: VehicleSystemsTemplateRightDriver\Components [Indent level: 0]
            "Components": {
                # Class: VehicleSystemsTemplateRightDriver\Components\VehiclePrimaryGunnerDisplay [Indent level: 1]
                "VehiclePrimaryGunnerDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateRightDriver\Components\VehicleCommanderDisplay [Indent level: 1],
                "VehicleCommanderDisplay": {
                    "componentType": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\EmptyDisplay [Indent level: 1],
                "EmptyDisplay": {
                    "componentType": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MinimapDisplay [Indent level: 1],
                "MinimapDisplay": {
                    "componentType": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\MineDetectorDisplay [Indent level: 1],
                "MineDetectorDisplay": {
                    "componentType": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\CrewDisplay [Indent level: 1],
                "CrewDisplay": {
                    "componentType": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\UAVDisplay [Indent level: 1],
                "UAVDisplay": {
                    "componentType": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight\Components\SlingLoadDisplay [Indent level: 1],
                "SlingLoadDisplay": {
                    "componentType": "SlingLoadDisplayComponent"
                }
            },
            "componentType": "VehicleSystemsDisplayManager",
            "right": 1,
            "defaultDisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles\Tank_F\Components\AITankSteeringComponent [Indent level: 2],
        "AITankSteeringComponent": {
            "steeringPIDWeights": [2.9,0.1,0.2],
            "speedPIDWeights": [0.7,0.2,0],
            "doRemapSpeed": 0,
            "remapSpeedRange": [30,70],
            "remapSpeedScalar": [1,0.35],
            "doPredictForward": 1,
            "predictForwardRange": [1,20],
            "steerAheadSaturation": [0.01,0.4],
            "speedPredictionMethod": 3,
            "wheelAngleCoef": 0.7,
            "forwardAngleCoef": 0.7,
            "steeringAngleCoef": 1,
            "differenceAngleCoef": 1,
            "stuckMaxTime": 3,
            "allowOvertaking": 1,
            "allowCollisionAvoidance": 1,
            "allowDrifting": 0,
            "maxWheelAngleDiff": 0.2616,
            "minSpeedToKeep": 0.01,
            "commandTurnFactor": 2,
            "allowTurnAroundInPoint": 1,
            "convoyPIDWeights": [1,0,0],
            "predictForwardMaxSpeed": 15
        },
        # Class: CfgVehicles\LandVehicle\Components\TransportCountermeasuresComponent [Indent level: 2],
        "TransportCountermeasuresComponent": {
        }
    },
    # Class: CfgVehicles\Tank_F\NVGMarkers [Indent level: 1],
    "NVGMarkers": {
        # Class: CfgVehicles\Tank_F\NVGMarkers\NVGMarker01 [Indent level: 2]
        "NVGMarker01": {
            "name": "nvg_marker",
            "color": [0.03,0.003,0.003,1],
            "ambient": [0.003,0.0003,0.0003,1],
            "brightness": 0.001,
            "blinking": 1
        }
    },
    "memoryPointDriverOptics": "driverview",
    "engineStartSpeed": 5,
    "explosionEffect": "FuelExplosionBig",
    "htMin": 60,
    "htMax": 1800,
    "afMax": 100,
    "mfMax": 80,
    "mFact": 1,
    "tBody": 250,
    "numberPhysicalWheels": 16,
    "ace_cookoff_ammoLocation": "HitHull",
    "ace_cookoff_cookoffSelections": ["poklop_gunner","poklop_commander"],
    "ace_cookoff_probability": 0.5,
    # Class: CfgVehicles\Tank_F\ACE_Actions [Indent level: 1],
    "ACE_Actions": {
        # Class: CfgVehicles\Tank_F\ACE_Actions\ACE_MainActions [Indent level: 2]
        "ACE_MainActions": {
            "displayName": "Interactions",
            "position": "call ace_interaction_fnc_getVehiclePos",
            "selection": "",
            "distance": 4,
            "condition": "true",
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ACE_Passengers [Indent level: 3],
            "ACE_Passengers": {
                "displayName": "Passengers",
                "condition": "alive _target",
                "statement": "",
                "exceptions": ["isNotSwimming"],
                "insertChildren": "_this call ace_interaction_fnc_addPassengersActions"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_quickmount_GetIn [Indent level: 3],
            "ace_quickmount_GetIn": {
                "displayName": "Get In",
                "condition": "call ace_quickmount_fnc_canShowFreeSeats",
                "statement": "call ace_quickmount_fnc_getInNearest",
                "exceptions": ["isNotSwimming"],
                "insertChildren": "(_this select 2) param [0,[]]"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_rearm_Rearm [Indent level: 3],
            "ace_rearm_Rearm": {
                "displayName": "Rearm",
                "distance": 9,
                "condition": "_this call ace_rearm_fnc_canRearm",
                "statement": "_this call ace_rearm_fnc_rearm",
                "exceptions": ["isNotInside"],
                "icon": "z|ace|addons|rearm|ui|icon_rearm_interact.paa"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_repair_Repair [Indent level: 3],
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
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ACE_unlockVehicle [Indent level: 3],
            "ACE_unlockVehicle": {
                "displayName": "Unlock Vehicle",
                "distance": 4,
                "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [2, 3]}",
                "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,false],[_target]] call CBA_fnc_targetEvent",
                "exceptions": ["isNotSwimming"],
                "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ACE_lockVehicle [Indent level: 3],
            "ACE_lockVehicle": {
                "displayName": "Lock Vehicle",
                "distance": 4,
                "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [0, 1]}",
                "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,true],[_target]] call CBA_fnc_targetEvent",
                "exceptions": ["isNotSwimming"],
                "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ACE_lockpickVehicle [Indent level: 3],
            "ACE_lockpickVehicle": {
                "displayName": "Lockpick Vehicle",
                "distance": 4,
                "condition": "[_player,_target,'canLockpick'] call ace_vehiclelock_fnc_lockpick",
                "statement": "[_player,_target,'startLockpick'] call ace_vehiclelock_fnc_lockpick",
                "exceptions": ["isNotSwimming"]
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\AIME_vehicle_seats_getInAction [Indent level: 3],
            "AIME_vehicle_seats_getInAction": {
                "displayName": "Get In",
                "condition": "call AIME_vehicle_seats_fnc_getin_condition",
                "statement": "call AIME_vehicle_seats_fnc_getin_run",
                "icon": "a3|ui_f|data|igui|cfg|actions|obsolete|ui_action_getin_ca.paa",
                "insertChildren": "call AIME_vehicle_seats_fnc_change_submenus"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_attach_AttachVehicle [Indent level: 3],
            "ace_attach_AttachVehicle": {
                "displayName": "Attach item",
                "condition": "_this call ace_attach_fnc_canAttach",
                "insertChildren": "_this call ace_attach_fnc_getChildrenActions",
                "exceptions": ["isNotSwimming"],
                "showDisabled": 0,
                "icon": "z|ace|addons|attach|UI|attach_ca.paa"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_attach_DetachVehicle [Indent level: 3],
            "ace_attach_DetachVehicle": {
                "displayName": "Detach item",
                "condition": "_this call ace_attach_fnc_canDetach",
                "statement": "_this call ace_attach_fnc_detach",
                "exceptions": ["isNotSwimming"],
                "showDisabled": 0,
                "icon": "z|ace|addons|attach|UI|detach_ca.paa"
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\ace_captives_LoadCaptive [Indent level: 3],
            "ace_captives_LoadCaptive": {
                "displayName": "Load Captive",
                "distance": 4,
                "condition": "[_player,objNull,_target] call ace_captives_fnc_canLoadCaptive",
                "statement": "[_player,objNull,_target] call ace_captives_fnc_doLoadCaptive",
                "exceptions": ["isNotEscorting","isNotSwimming"]
            },
            # Class: CfgVehicles\Tank\ACE_Actions\ACE_MainActions\AIME_inventory_openAction [Indent level: 3],
            "AIME_inventory_openAction": {
                "displayName": "Inventory",
                "condition": "AIME_inventory_settingOpenAction				 && { alive _target }				 && { _target call AIME_inventory_fnc_has_inventory }",
                "statement": "_player action [`Gear`, _target]",
                "icon": "A3|ui_f|data|igui|cfg|actions|gear_ca.paa",
                "exceptions": ["isNotSwimming"]
            }
        }
    },
    # Class: CfgVehicles\Tank_F\Periscope [Indent level: 1],
    "Periscope": {
    },
    "getInRadius": 3.5,
    "hullDamageCauseExplosion": 1,
    "bounding": "usti hlavne",
    "fireDustEffect": "FDustEffects",
    "gearBox": [-7,0,11,8,5.7,4.2],
    "alphaTracks": 0.7,
    "textureTrackWheel": 0,
    "memoryPointTrack1L": "Stopa LL",
    "memoryPointTrack1R": "Stopa LR",
    "memoryPointTrack2L": "Stopa RL",
    "memoryPointTrack2R": "Stopa RR",
    "predictTurnSimul": 1.2,
    "predictTurnPlan": 1,
    "soundGear": ["",0.000316228,1],
    "outsideSoundFilter": 1,
    "nightVision": 0,
    "formationX": 20,
    "formationZ": 30,
    "canFloat": 0,
    "type": 1,
    "camouflage": 8,
    "driverOpticsColor": [1,1,1,1],
    # Class: CfgVehicles\Tank\CargoLight [Indent level: 1],
    "CargoLight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
    "enableGPS": 1,
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffectsBig"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffectsBig"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffectsBig"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffectsBig"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffectsBig"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffectsBig"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassEffectsDryBig"],["GdtStratisDryGrass","RDirtEffectsBig"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffectsBig"],["GdtStratisGreenGrass","RDirtEffectsBig"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffectsBig"],["GdtStratisRocky","RDirtEffectsBig"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffectsBig"],["GdtStratisThistles","RDirtEffectsBig"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffectsBig"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffectsBig"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffectsBig"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffectsBig"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffectsBig"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffectsBig"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffectsBig"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RDirtEffectsBig"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RDirtEffectsBig"],["GdtDesert1","RStonesEffectsBig"],["GdtDesert2","RDustEffects"],["GdtDesert2","RGrassEffectsBig"],["GdtDesert2","RDirtEffectsBig"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffectsBig"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffectsBig"],["GdtGrassGreen","RDirtEffectsBig"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassEffectsDryBig"],["GdtGrassDry","RDirtEffectsBig"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffectsBig"],["GdtGrassWild","RDirtEffectsBig"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffectsBig"],["GdtWildField","RDirtEffectsBig"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffectsBig"],["GdtWeed1","RDirtEffectsBig"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffectsBig"],["GdtWeed2","RDirtEffectsBig"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffectsBig"],["GdtThorn","RDirtEffectsBig"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffectsBig"],["GdtStony","RDirtEffectsBig"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffectsBig"],["GdtStonyGreen","RDirtEffectsBig"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffectsBig"],["GdtStonyThistle","RDirtEffectsBig"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"],["CRGrass1","RDustEffects"],["CRGrass1","RGrassEffectsBig"],["CRGrass1","RDirtEffectsBig"],["CRGrass2","RDustEffects"],["CRGrass2","RGrassEffectsBig"],["CRGrass2","RDirtEffectsBig"],["CRGrassW1","RDustEffects"],["CRGrassW1","RGrassEffectsBig"],["CRGrassW1","RDirtEffectsBig"],["CRGrassW2","RDustEffects"],["CRGrassW2","RGrassEffectsBig"],["CRGrassW2","RDirtEffectsBig"],["CRField1","RDustEffects"],["CRField1","RGrassEffectsBig"],["CRField1","RDirtEffectsBig"],["CRField2","RDustEffects"],["CRField2","RGrassEffectsBig"],["CRField2","RDirtEffectsBig"],["CRForest1","RDustEffects"],["CRForest1","RGrassEffectsBig"],["CRForest1","RDirtEffectsBig"],["CRForest2","RDustEffects"],["CRForest2","RGrassEffectsBig"],["CRForest2","RDirtEffectsBig"],["CRGrit1","RDustEffects"],["CRGrit1","RDirtEffectsBig"],["CRHeather","RDustEffects"],["CRHeather","RGrassEffectsBig"],["CRHeather","RDirtEffectsBig"],["CRConcrete","RDirtEffectsBig"],["TKAsfalt","RDirtEffectsBig"],["TKBeton","RDustEffects"],["TKPlevel","RDustEffects"],["TKPlevel","RGrassEffectsBig"],["TKPlevel","RDirtEffectsBig"],["TKPole","RDustEffects"],["TKPole","RGrassEffectsDryBig"],["TKPole","RDirtEffectsBig"],["TKPolopoust","RDustEffects"],["TKPolopoust","RSandEffects"],["TKPolopoust","RDirtEffectsBig"],["TKSkala","RDustEffects"],["TKSkala","RStonesEffects"],["TKSkalniSterk","RDustEffects"],["TKSkalniSterk","RStonesEffects"],["TKSterkNaDno","RDustEffects"],["TKSterkNaDno","RStonesEffects"],["TKMoutain","RDustEffects"],["TKMoutain","RStonesEffects"],["TKValouny","RDustEffects"],["TKValouny","RStonesEffects"],["TKTrava","RDustEffects"],["TKTrava","RGrassEffectsDryBig"],["TKTrava","RDirtEffectsBig"],["TKForest","RDustEffects"],["TKForest","RGrassEffectsDryBig"],["TKForest","RDirtEffectsBig"],["ZRAsfalt","RDirtEffectsBig"],["ZRBeton","RDustEffects"],["RoadDirt_EP1","RDustEffects"],["RoadTarmac_EP1","RDirtEffectsBig"],["ZRPlevel","RDustEffects"],["ZRPlevel","RGrassEffectsBig"],["ZRPlevel","RDirtEffectsBig"],["ZRPole","RDustEffects"],["ZRPole","RGrassEffectsDryBig"],["ZRPole","RDirtEffectsBig"],["ZRPolopoust","RDustEffects"],["ZRPolopoust","RSandEffects"],["ZRPolopoust","RDirtEffectsBig"],["ZRSkala","RDustEffects"],["ZRSkala","RStonesEffects"],["ZRSkalniSterk","RDustEffects"],["ZRSkalniSterk","RStonesEffects"],["ZRSterkNaDno","RDustEffects"],["ZRSterkNaDno","RStonesEffects"],["ZRValouny","RDustEffects"],["ZRValouny","RStonesEffects"],["ZRTrava","RDustEffects"],["ZRTrava","RGrassEffectsDryBig"],["ZRTrava","RDirtEffectsBig"],["DEPolopoust","RDustEffects"],["DEPolopoust","RSandEffects"],["DEPolopoust","RDirtEffectsBig"],["DESkalniSterk","RDustEffects"],["DESkalniSterk","RStonesEffects"],["DETrava","RDustEffects"],["DETrava","RGrassEffectsDryBig"],["DETrava","RDirtEffectsBig"],["WLGrass1","RDustEffects"],["WLGrass1","RGrassEffectsBig"],["WLGrass1","RDirtEffectsBig"],["WLGrass2","RDustEffects"],["WLGrass2","RGrassEffectsBig"],["WLGrass2","RDirtEffectsBig"],["WLGrassW1","RDustEffects"],["WLGrassW1","RGrassEffectsBig"],["WLGrassW1","RDirtEffectsBig"],["WLGrassW2","RDustEffects"],["WLGrassW2","RGrassEffectsBig"],["WLGrassW2","RDirtEffectsBig"],["WLField1","RDustEffects"],["WLField1","RGrassEffectsBig"],["WLField1","RDirtEffectsBig"],["WLField2","RDustEffects"],["WLField2","RGrassEffectsBig"],["WLField2","RDirtEffectsBig"],["WLForest1","RDustEffects"],["WLForest1","RGrassEffectsBig"],["WLForest1","RDirtEffectsBig"],["WLForest2","RDustEffects"],["WLForest2","RGrassEffectsBig"],["WLForest2","RDirtEffectsBig"],["WLMudGround","RDustEffects"],["WLMudGround","RGrassEffectsBig"],["WLMudGround","RDirtEffectsBig"],["WLGrit1","RDustEffects"],["WLGrit1","RDirtEffectsBig"],["WLHeather","RDustEffects"],["WLHeather","RGrassEffectsBig"],["WLHeather","RDirtEffectsBig"],["WLConcrete","RDirtEffectsBig"],["GZTrava","RDustEffects"],["GZTrava","RGrassEffectsDryBig"],["GZTrava","RDirtEffectsBig"],["GZforest","RDustEffects"],["GZforest","RGrassEffectsDryBig"],["GZforest","RDirtEffectsBig"],["GZkameny","RDustEffects"],["GZkameny","RStonesEffects"],["GZHlina","RDustEffects"],["GZHlina","RGrassEffectsBig"],["GZHlina","RDi,
    "leftDustEffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffectsBig"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffectsBig"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffectsBig"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffectsBig"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffectsBig"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffectsBig"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassEffectsDryBig"],["GdtStratisDryGrass","LDirtEffectsBig"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffectsBig"],["GdtStratisGreenGrass","LDirtEffectsBig"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffectsBig"],["GdtStratisRocky","LDirtEffectsBig"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffectsBig"],["GdtStratisThistles","LDirtEffectsBig"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffectsBig"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffectsBig"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffectsBig"],["GdtRubble","LDirtEffectsBig"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffectsBig"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffectsBig"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffectsBig"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffectsBig"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LDirtEffectsBig"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LDirtEffectsBig"],["GdtDesert1","LStonesEffectsBig"],["GdtDesert2","LDustEffects"],["GdtDesert2","LGrassEffectsBig"],["GdtDesert2","LDirtEffectsBig"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffectsBig"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffectsBig"],["GdtGrassGreen","LDirtEffectsBig"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassEffectsDryBig"],["GdtGrassDry","LDirtEffectsBig"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffectsBig"],["GdtGrassWild","LDirtEffectsBig"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffectsBig"],["GdtWildField","LDirtEffectsBig"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffectsBig"],["GdtWeed1","LDirtEffectsBig"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffectsBig"],["GdtWeed2","LDirtEffectsBig"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffectsBig"],["GdtThorn","LDirtEffectsBig"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffectsBig"],["GdtStony","LDirtEffectsBig"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffectsBig"],["GdtStonyGreen","LDirtEffectsBig"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffectsBig"],["GdtStonyThistle","LDirtEffectsBig"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","LDustEffects"],["CRGrass1","LDustEffects"],["CRGrass1","LGrassEffectsBig"],["CRGrass1","LDirtEffectsBig"],["CRGrass2","LDustEffects"],["CRGrass2","LGrassEffectsBig"],["CRGrass2","LDirtEffectsBig"],["CRGrassW1","LDustEffects"],["CRGrassW1","LGrassEffectsBig"],["CRGrassW1","LDirtEffectsBig"],["CRGrassW2","LDustEffects"],["CRGrassW2","LGrassEffectsBig"],["CRGrassW2","LDirtEffectsBig"],["CRField1","LDustEffects"],["CRField1","LGrassEffectsBig"],["CRField1","LDirtEffectsBig"],["CRField2","LDustEffects"],["CRField2","LGrassEffectsBig"],["CRField2","LDirtEffectsBig"],["CRForest1","LDustEffects"],["CRForest1","LGrassEffectsBig"],["CRForest1","LDirtEffectsBig"],["CRForest2","LDustEffects"],["CRForest2","LGrassEffectsBig"],["CRForest2","LDirtEffectsBig"],["CRGrit1","LDustEffects"],["CRGrit1","LDirtEffectsBig"],["CRHeather","LDustEffects"],["CRHeather","LGrassEffectsBig"],["CRHeather","LDirtEffectsBig"],["CRConcrete","LDirtEffectsBig"],["TKAsfalt","LDirtEffectsBig"],["TKBeton","LDustEffects"],["RoadDirt_EP1","LDustEffects"],["RoadTarmac_EP11","LDirtEffectsBig"],["TKPlevel","LDustEffects"],["TKPlevel","LGrassEffectsBig"],["TKPlevel","LDirtEffectsBig"],["TKPole","LDustEffects"],["TKPole","LGrassEffectsDryBig"],["TKPole","LDirtEffectsBig"],["TKPolopoust","LDustEffects"],["TKPolopoust","LSandEffects"],["TKPolopoust","LDirtEffectsBig"],["TKSkala","LDustEffects"],["TKSkala","LStonesEffectsBig"],["TKSkalniSterk","LDustEffects"],["TKSkalniSterk","LStonesEffectsBig"],["TKSterkNaDno","LDustEffects"],["TKSterkNaDno","LStonesEffectsBig"],["TKMoutain","LDustEffects"],["TKMoutain","LStonesEffectsBig"],["TKValouny","LDustEffects"],["TKValouny","LStonesEffectsBig"],["TKTrava","LDustEffects"],["TKTrava","LGrassEffectsDryBig"],["TKTrava","LDirtEffectsBig"],["TKForest","LDustEffects"],["TKForest","LGrassEffectsDryBig"],["TKForest","LDirtEffectsBig"],["ZRAsfalt","LDirtEffectsBig"],["ZRBeton","LDustEffects"],["ZRPlevel","LDustEffects"],["ZRPlevel","LGrassEffectsBig"],["ZRPlevel","LDirtEffectsBig"],["ZRPole","LDustEffects"],["ZRPole","LGrassEffectsDryBig"],["ZRPole","LDirtEffectsBig"],["ZRPolopoust","LDustEffects"],["ZRPolopoust","LSandEffects"],["ZRPolopoust","LDirtEffectsBig"],["ZRSkala","LDustEffects"],["ZRSkala","LStonesEffectsBig"],["ZRSkalniSterk","LDustEffects"],["ZRSkalniSterk","LStonesEffectsBig"],["ZRSterkNaDno","LDustEffects"],["ZRSterkNaDno","LStonesEffectsBig"],["ZRValouny","LDustEffects"],["ZRValouny","LStonesEffectsBig"],["ZRTrava","LDustEffects"],["ZRTrava","LGrassEffectsDryBig"],["ZRTrava","LDirtEffectsBig"],["DEPolopoust","LDustEffects"],["DEPolopoust","LSandEffects"],["DEPolopoust","LDirtEffectsBig"],["DESkalniSterk","LDustEffects"],["DESkalniSterk","LStonesEffectsBig"],["DETrava","LDustEffects"],["DETrava","LGrassEffectsDryBig"],["DETrava","LDirtEffectsBig"],["WLGrass1","LDustEffects"],["WLGrass1","LGrassEffectsBig"],["WLGrass1","LDirtEffectsBig"],["WLGrass2","LDustEffects"],["WLGrass2","LGrassEffectsBig"],["WLGrass2","LDirtEffectsBig"],["WLGrassW1","LDustEffects"],["WLGrassW1","LGrassEffectsBig"],["WLGrassW1","LDirtEffectsBig"],["WLGrassW2","LDustEffects"],["WLGrassW2","LGrassEffectsBig"],["WLGrassW2","LDirtEffectsBig"],["WLField1","LDustEffects"],["WLField1","LGrassEffectsBig"],["WLField1","LDirtEffectsBig"],["WLField2","LDustEffects"],["WLField2","LGrassEffectsBig"],["WLField2","LDirtEffectsBig"],["WLForest1","LDustEffects"],["WLForest1","LGrassEffectsBig"],["WLForest1","LDirtEffectsBig"],["WLForest2","LDustEffects"],["WLForest2","LGrassEffectsBig"],["WLForest2","LDirtEffectsBig"],["WLMudGround","LDustEffects"],["WLMudGround","LGrassEffectsBig"],["WLMudGround","LDirtEffectsBig"],["WLGrit1","LDustEffects"],["WLGrit1","LDirtEffectsBig"],["WLHeather","LDustEffects"],["WLHeather","LGrassEffectsBig"],["WLHeather","LDirtEffectsBig"],["WLConcrete","LDirtEffectsBig"],["GZTrava","LDustEffects"],["GZTrava","LGrassEffectsDryBig"],["GZTrava","LDirtEffectsBig"],["GZforest","LDustEffects"],["GZForest","LGrassEffectsDryBig"],["GZForest","LDirtEffectsBig"],["GZkameny","LDustEffects"],["GZkameny","LStonesEffectsBig"],["GZHli,
    # Class: CfgVehicles\Tank\DestructionEffects [Indent level: 1],
    "DestructionEffects": {
        # Class: CfgVehicles\Tank\DestructionEffects\LightBig1 [Indent level: 2]
        "LightBig1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles\Tank\DestructionEffects\Sound [Indent level: 2],
        "Sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireBig1 [Indent level: 2],
        "FireBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\Refract1 [Indent level: 2],
        "Refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefract",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig1 [Indent level: 2],
        "SmokeBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SparksBig1 [Indent level: 2],
        "SparksBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 0
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireSparksBig1 [Indent level: 2],
        "FireSparksBig1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2.8
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireBig2 [Indent level: 2],
        "FireBig2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig1_2 [Indent level: 2],
        "SmokeBig1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig2 [Indent level: 2],
        "SmokeBig2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 3.2
        },
        # Class: CfgVehicles\Tank\DestructionEffects\LightFlames1 [Indent level: 2],
        "LightFlames1": {
            "simulation": "particles",
            "type": "FlameLightBC",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 0.5,
            "enabled": "distToWater"
        }
    },
    "tf_hasLRradio": 1,
    "tf_isolatedAmount": 1,
    # Class: CfgVehicles\Tank\ViewCargo [Indent level: 1],
    "ViewCargo": {
        "initFov": 0.7,
        "minFov": 0.25,
        "maxFov": 1.4,
        "initAngleX": 0,
        "minAngleX": -75,
        "maxAngleX": 85,
        "initAngleY": 0,
        "minAngleY": -170,
        "maxAngleY": 170,
        "minMoveX": -0.5,
        "maxMoveX": 0.5,
        "minMoveY": -0.025,
        "maxMoveY": 0.1,
        "minMoveZ": -0.3,
        "maxMoveZ": 0.5,
        "speedZoomMaxSpeed": 0,
        "speedZoomMaxFOV": 0.7
    },
    # Class: CfgVehicles\Tank\ACE_SelfActions [Indent level: 1],
    "ACE_SelfActions": {
        # Class: CfgVehicles\Tank\ACE_SelfActions\ACE_Passengers [Indent level: 2]
        "ACE_Passengers": {
            "displayName": "Passengers",
            "condition": "alive _target",
            "statement": "",
            "insertChildren": "_this call ace_interaction_fnc_addPassengersActions"
        },
        # Class: CfgVehicles\Tank\ACE_SelfActions\ace_quickmount_ChangeSeat [Indent level: 2],
        "ace_quickmount_ChangeSeat": {
            "displayName": "Change seat",
            "condition": "call ace_quickmount_fnc_canShowFreeSeats",
            "statement": "",
            "insertChildren": "(_this select 2) param [0,[]]"
        },
        # Class: CfgVehicles\Tank\ACE_SelfActions\ACE_unlockVehicle [Indent level: 2],
        "ACE_unlockVehicle": {
            "displayName": "Unlock Vehicle",
            "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [2, 3]}",
            "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,false],[_target]] call CBA_fnc_targetEvent",
            "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
        },
        # Class: CfgVehicles\Tank\ACE_SelfActions\ACE_lockVehicle [Indent level: 2],
        "ACE_lockVehicle": {
            "displayName": "Lock Vehicle",
            "condition": "([_player,_target] call ace_vehiclelock_fnc_hasKeyForVehicle) && {(locked _target) in [0, 1]}",
            "statement": "[`ace_vehiclelock_setVehicleLock`,[_target,true],[_target]] call CBA_fnc_targetEvent",
            "icon": "z|ace|addons|vehiclelock|ui|key_menuIcon_ca.paa"
        },
        # Class: CfgVehicles\Tank\ACE_SelfActions\ACE_lockpickVehicle [Indent level: 2],
        "ACE_lockpickVehicle": {
            "displayName": "Lockpick Vehicle",
            "condition": "[_player,_target,'canLockpick'] call ace_vehiclelock_fnc_lockpick",
            "statement": "[_player,_target,'startLockpick'] call ace_vehiclelock_fnc_lockpick"
        },
        # Class: CfgVehicles\Tank\ACE_SelfActions\ResetFCS [Indent level: 2],
        "ResetFCS": {
            "displayName": "Reset FCS",
            "condition": "_player call ace_fcs_fnc_canResetFCS",
            "statement": "[vehicle _player,[_player] call ace_common_fnc_getTurretIndex] call ace_fcs_fnc_reset;",
            "showDisabled": 0,
            "icon": ""
        }
    },
    "ace_refuel_canReceive": 1,
    "ace_refuel_flowRate": 4,
    "ace_cargo_space": 4,
    "ace_cargo_hasCargo": 1,
    "selectionBrakeLights": "brzdove svetlo",
    "memoryPointMissile": ["spice rakety","usti hlavne"],
    "memoryPointMissileDir": ["konec rakety","konec hlavne"],
    "leftDustEffect": "LDustEffects",
    "rightDustEffect": "RDustEffects",
    "leftWaterEffect": "LWaterEffects",
    "rightWaterEffect": "RWaterEffects",
    "leftFastWaterEffect": "LWaterEffects",
    "rightFastWaterEffect": "RWaterEffects",
    "selectionLeftOffset": "PasOffsetL",
    "selectionRightOffset": "PasOffsetP",
    # Class: CfgVehicles\LandVehicle\CommanderOptics [Indent level: 1],
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
        # Class: CfgVehicles\LandVehicle\CommanderOptics\ViewOptics [Indent level: 2],
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
        # Class: CfgVehicles\LandVehicle\CommanderOptics\ViewGunner [Indent level: 2],
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec [Indent level: 2],
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
        "showCrewAim": 0,
        "ace_fcs_Enabled": 0,
        "ace_fcs_MinDistance": 200,
        "ace_fcs_MaxDistance": 5500,
        "ace_fcs_DistanceInterval": 5
    },
    "tf_range": 30000,
    "wheelDamageThreshold": 0.2,
    "wheelDestroyThreshold": 0.99,
    "wheelDamageRadiusCoef": 0.9,
    "wheelDestroyRadiusCoef": 0.4,
    "weaponsGroup1": 1,
    "weaponsGroup2": "2 + 		4",
    "weaponsGroup3": "8 + 	16 + 	32",
    "weaponsGroup4": "64 + 		128",
    # Class: CfgVehicles\AllVehicles\SquadTitles [Indent level: 1],
    "SquadTitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
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
    "selectionBackLights": "zadni svetlo",
    # Class: CfgVehicles\AllVehicles\NewTurret [Indent level: 1],
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
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "preciseGetInOut": 0,
    "cargoPreciseGetInOut": [0],
    "availableForSupportTypes": [],
    "waterPPInVehicle": 1,
    "impactEffectsSea": "ImpactEffectsSea",
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
    "epeImpulseDamageCoef": 30,
    "gunnerHasFlares": 1,
    "enableManualFire": 1,
    "sensitivity": 2.5,
    "portrait": "",
    "ghostPreview": "",
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
    "laserTarget": 0,
    "laserScanner": 0,
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
    "enableWatch": 0,
    "usePreciseGetInAction": 0,
    "allowTabLock": 1,
    "showAllTargets": 0,
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
    # Class: CfgVehicles\All\MarkerLights [Indent level: 1],
    "MarkerLights": {
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
    "typicalCargo": [],
    "cargoIsCoDriver": [0],
    "driverCompartments": "Compartment1",
    "cargoCompartments": ["Compartment1"],
    "driverOpticsEffect": [],
    "canHideDriver": -1,
    "castDriverShadow": 0,
    "castCargoShadow": 0,
    "viewDriverShadow": 1,
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
    # Class: CfgVehicles\All\GunFire [Indent level: 1],
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
    # Class: CfgVehicles\All\GunClouds [Indent level: 1],
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
    # Class: CfgVehicles\All\MGunClouds [Indent level: 1],
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
    "selectionDamage": "zbytek",
    "HeadAimDown": 0,
    "cargoCanEject": 1,
    "driverCanEject": 1,
    "fireResistance": 10,
    "airCapacity": 10,
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "slingLoadCargoMemoryPoints": [],
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    # Class: CfgVehicles\All\camShakeGForce [Indent level: 1],
    "camShakeGForce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minSpeed": 1,
        "duration": 3
    },
    "minGForce": 0.2,
    "maxGForce": 2,
    "gForceShakeAttenuation": 0.5,
    # Class: CfgVehicles\All\camShakeDamage [Indent level: 1],
    "camShakeDamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minSpeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "insideDetectCoef": 0.05,
    "coefSpeedInside": 1,
    "windSockExist": 0,
    "SLX_XEH_DISABLED": 0,
}