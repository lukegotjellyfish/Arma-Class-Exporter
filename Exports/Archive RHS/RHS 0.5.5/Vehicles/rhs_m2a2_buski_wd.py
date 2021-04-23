rhs_m2a2_buski_wd = {
    "scope": 2,
    "faction": "rhs_faction_usarmy_wd",
    "crew": "rhsusf_army_ucp_crewman",
    "author": "Red Hammer Studios",
    "editorpreview": "rhsusf|addons|rhsusf_editorPreviews|data|RHS_M2A2_BUSKI_WD.paa",
    "hiddenselections": ["camo1","camo2","camo3","selection_stinger","selection_tow"],
    "hiddenselectionstextures": ["|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|a3_buski_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|ultralp_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa"],
    "displayname": "M2A2ODS (BUSK I)",
    "model": "rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|M2A2_ERA",
    "damageresistance": 0.01101,
    # Class: CfgVehicles|RHS_M2A2_BUSKI|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|RHS_M2A2_BUSKI|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Woodland",
            "textures": ["|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|a3_buski_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|ultralp_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|base_co.paa"],
            "factions": ["rhs_faction_usarmy_wd"]
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|textureSources|Desert [Indent level: 2],
        "desert": {
            "displayname": "Desert",
            "textures": ["|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|a3_buski_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|ultralp_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|base_co.paa"],
            "factions": ["rhs_faction_usarmy_d"]
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|textureSources|Olive [Indent level: 2],
        "olive": {
            "displayname": "Olive",
            "author": "Red Hammer Studios",
            "textures": ["|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|m6_base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|m6_a3_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|ultralp_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|m6_base_co.paa","|rhsusf|addons|rhsusf_a2port_armor|m2a2_bradley|data|woodland|m6_base_co.paa"],
            "factions": ["rhs_faction_usarmy_wd"]
        }
    },
    # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|Select_TOW [Indent level: 2]
        "select_tow": {
            "scope": 0,
            "author": "Red Hammer Studios",
            "displayname": "add Stinger launcher",
            "forceanimatephase": 1,
            "forceanimate": ["Select_Stinger",0],
            "source": "user",
            "animperiod": 1e-007,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|Select_Stinger [Indent level: 2],
        "select_stinger": {
            "scope": 0,
            "initphase": 1,
            "forceanimatephase": 1,
            "displayname": "add TOW launcher",
            "forceanimate": ["Select_TOW",0],
            "onphasechanged": "_this call rhs_fnc_m2_handleWeaponVG",
            "author": "Red Hammer Studios",
            "source": "user",
            "animperiod": 1e-007
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_1_source [Indent level: 2],
        "era_1_source": {
            "source": "Hit",
            "hitpoint": "era_1_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_2_source [Indent level: 2],
        "era_2_source": {
            "source": "Hit",
            "hitpoint": "era_2_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_3_source [Indent level: 2],
        "era_3_source": {
            "source": "Hit",
            "hitpoint": "era_3_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_4_source [Indent level: 2],
        "era_4_source": {
            "source": "Hit",
            "hitpoint": "era_4_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_5_source [Indent level: 2],
        "era_5_source": {
            "source": "Hit",
            "hitpoint": "era_5_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_6_source [Indent level: 2],
        "era_6_source": {
            "source": "Hit",
            "hitpoint": "era_6_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_7_source [Indent level: 2],
        "era_7_source": {
            "source": "Hit",
            "hitpoint": "era_7_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_8_source [Indent level: 2],
        "era_8_source": {
            "source": "Hit",
            "hitpoint": "era_8_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_9_source [Indent level: 2],
        "era_9_source": {
            "source": "Hit",
            "hitpoint": "era_9_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_10_source [Indent level: 2],
        "era_10_source": {
            "source": "Hit",
            "hitpoint": "era_10_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_11_source [Indent level: 2],
        "era_11_source": {
            "source": "Hit",
            "hitpoint": "era_11_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_12_source [Indent level: 2],
        "era_12_source": {
            "source": "Hit",
            "hitpoint": "era_12_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_13_source [Indent level: 2],
        "era_13_source": {
            "source": "Hit",
            "hitpoint": "era_13_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_14_source [Indent level: 2],
        "era_14_source": {
            "source": "Hit",
            "hitpoint": "era_14_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_15_source [Indent level: 2],
        "era_15_source": {
            "source": "Hit",
            "hitpoint": "era_15_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_16_source [Indent level: 2],
        "era_16_source": {
            "source": "Hit",
            "hitpoint": "era_16_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_17_source [Indent level: 2],
        "era_17_source": {
            "source": "Hit",
            "hitpoint": "era_17_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_18_source [Indent level: 2],
        "era_18_source": {
            "source": "Hit",
            "hitpoint": "era_18_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_19_source [Indent level: 2],
        "era_19_source": {
            "source": "Hit",
            "hitpoint": "era_19_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_20_source [Indent level: 2],
        "era_20_source": {
            "source": "Hit",
            "hitpoint": "era_20_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_21_source [Indent level: 2],
        "era_21_source": {
            "source": "Hit",
            "hitpoint": "era_21_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_22_source [Indent level: 2],
        "era_22_source": {
            "source": "Hit",
            "hitpoint": "era_22_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_23_source [Indent level: 2],
        "era_23_source": {
            "source": "Hit",
            "hitpoint": "era_23_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_24_source [Indent level: 2],
        "era_24_source": {
            "source": "Hit",
            "hitpoint": "era_24_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_25_source [Indent level: 2],
        "era_25_source": {
            "source": "Hit",
            "hitpoint": "era_25_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_26_source [Indent level: 2],
        "era_26_source": {
            "source": "Hit",
            "hitpoint": "era_26_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_27_source [Indent level: 2],
        "era_27_source": {
            "source": "Hit",
            "hitpoint": "era_27_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_28_source [Indent level: 2],
        "era_28_source": {
            "source": "Hit",
            "hitpoint": "era_28_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_29_source [Indent level: 2],
        "era_29_source": {
            "source": "Hit",
            "hitpoint": "era_29_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_30_source [Indent level: 2],
        "era_30_source": {
            "source": "Hit",
            "hitpoint": "era_30_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_31_source [Indent level: 2],
        "era_31_source": {
            "source": "Hit",
            "hitpoint": "era_31_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_32_source [Indent level: 2],
        "era_32_source": {
            "source": "Hit",
            "hitpoint": "era_32_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_33_source [Indent level: 2],
        "era_33_source": {
            "source": "Hit",
            "hitpoint": "era_33_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_34_source [Indent level: 2],
        "era_34_source": {
            "source": "Hit",
            "hitpoint": "era_34_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_35_source [Indent level: 2],
        "era_35_source": {
            "source": "Hit",
            "hitpoint": "era_35_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_36_source [Indent level: 2],
        "era_36_source": {
            "source": "Hit",
            "hitpoint": "era_36_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_37_source [Indent level: 2],
        "era_37_source": {
            "source": "Hit",
            "hitpoint": "era_37_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_38_source [Indent level: 2],
        "era_38_source": {
            "source": "Hit",
            "hitpoint": "era_38_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_39_source [Indent level: 2],
        "era_39_source": {
            "source": "Hit",
            "hitpoint": "era_39_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_40_source [Indent level: 2],
        "era_40_source": {
            "source": "Hit",
            "hitpoint": "era_40_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_41_source [Indent level: 2],
        "era_41_source": {
            "source": "Hit",
            "hitpoint": "era_41_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_42_source [Indent level: 2],
        "era_42_source": {
            "source": "Hit",
            "hitpoint": "era_42_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_43_source [Indent level: 2],
        "era_43_source": {
            "source": "Hit",
            "hitpoint": "era_43_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_44_source [Indent level: 2],
        "era_44_source": {
            "source": "Hit",
            "hitpoint": "era_44_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|AnimationSources|era_45_source [Indent level: 2],
        "era_45_source": {
            "source": "Hit",
            "hitpoint": "era_45_hitpoint"
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|smoke_revolving_source [Indent level: 2],
        "smoke_revolving_source": {
            "source": "revolving",
            "weapon": "rhsusf_weap_M257_8"
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|cargolights_hide [Indent level: 2],
        "cargolights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|cabinlights_hide [Indent level: 2],
        "cabinlights_hide": {
            "source": "user",
            "animperiod": 1e-006,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|IFF_Panels_Hide [Indent level: 2],
        "iff_panels_hide": {
            "source": "user",
            "mass": -20,
            "displayname": "hide IFF Panels",
            "author": "Red Hammer Studios",
            "animperiod": 1e-005,
            "initphase": 0
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|recoil_source [Indent level: 2],
        "recoil_source": {
            "source": "reload",
            "weapon": "RHS_weap_M242BC"
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|muzzle_hide_hmg [Indent level: 2],
        "muzzle_hide_hmg": {
            "source": "reload",
            "weapon": "RHS_weap_M242BC"
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "RHS_weap_M242BC"
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|muzzle_rot_hmg2 [Indent level: 2],
        "muzzle_rot_hmg2": {
            "weapon": "rhs_weap_m240_bradley_coax",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|HatchC [Indent level: 2],
        "hatchc": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|HatchG [Indent level: 2],
        "hatchg": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|HatchD [Indent level: 2],
        "hatchd": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|ramp [Indent level: 2],
        "ramp": {
            "source": "door",
            "animperiod": 3.285,
            "initphase": 0,
            "sound": "rhs_ramp",
            "soundposition": "ramp_axis"
        },
        # Class: CfgVehicles|RHS_M2A2|AnimationSources|rear_hatch [Indent level: 2],
        "rear_hatch": {
            "source": "door",
            "animperiod": 0.8,
            "initphase": 0
        }
    },
    # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_1_hitpoint [Indent level: 2]
        "era_1_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e1",
            "armorcomponent": "e1",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_1_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e1",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_1_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e1",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_2_hitpoint [Indent level: 2],
        "era_2_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e2",
            "armorcomponent": "e2",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_2_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e2",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e2",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_2_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e2",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_3_hitpoint [Indent level: 2],
        "era_3_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e3",
            "armorcomponent": "e3",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_3_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e3",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e3",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_3_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e3",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_4_hitpoint [Indent level: 2],
        "era_4_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e4",
            "armorcomponent": "e4",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_4_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e4",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e4",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_4_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e4",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_5_hitpoint [Indent level: 2],
        "era_5_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e5",
            "armorcomponent": "e5",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_5_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e5",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e5",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_5_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e5",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_6_hitpoint [Indent level: 2],
        "era_6_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e6",
            "armorcomponent": "e6",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_6_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e6",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e6",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_6_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e6",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_7_hitpoint [Indent level: 2],
        "era_7_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e7",
            "armorcomponent": "e7",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_7_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e7",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e7",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_7_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e7",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_8_hitpoint [Indent level: 2],
        "era_8_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e8",
            "armorcomponent": "e8",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_8_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e8",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e8",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e8",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_8_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e8",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_9_hitpoint [Indent level: 2],
        "era_9_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e9",
            "armorcomponent": "e9",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_9_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e9",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e9",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e9",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_9_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e9",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_10_hitpoint [Indent level: 2],
        "era_10_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e10",
            "armorcomponent": "e10",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_10_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e10",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e10",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e10",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_10_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e10",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_11_hitpoint [Indent level: 2],
        "era_11_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e11",
            "armorcomponent": "e11",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_11_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e11",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e11",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e11",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_11_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e11",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_12_hitpoint [Indent level: 2],
        "era_12_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e12",
            "armorcomponent": "e12",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_12_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e12",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e12",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e12",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_12_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e12",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_13_hitpoint [Indent level: 2],
        "era_13_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e13",
            "armorcomponent": "e13",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_13_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e13",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e13",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e13",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_13_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e13",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_14_hitpoint [Indent level: 2],
        "era_14_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e14",
            "armorcomponent": "e14",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_14_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e14",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e14",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e14",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_14_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e14",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_15_hitpoint [Indent level: 2],
        "era_15_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e15",
            "armorcomponent": "e15",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_15_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e15",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e15",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e15",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_15_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e15",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_16_hitpoint [Indent level: 2],
        "era_16_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e16",
            "armorcomponent": "e16",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_16_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e16",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e16",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e16",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_16_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e16",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_17_hitpoint [Indent level: 2],
        "era_17_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e17",
            "armorcomponent": "e17",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_17_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e17",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e17",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e17",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_17_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e17",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_18_hitpoint [Indent level: 2],
        "era_18_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e18",
            "armorcomponent": "e18",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_18_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e18",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e18",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e18",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_18_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e18",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_19_hitpoint [Indent level: 2],
        "era_19_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e19",
            "armorcomponent": "e19",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_19_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e19",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e19",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e19",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_19_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e19",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_20_hitpoint [Indent level: 2],
        "era_20_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e20",
            "armorcomponent": "e20",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_20_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e20",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e20",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e20",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_20_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e20",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_21_hitpoint [Indent level: 2],
        "era_21_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e21",
            "armorcomponent": "e21",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_21_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e21",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e21",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e21",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_21_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e21",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_22_hitpoint [Indent level: 2],
        "era_22_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e22",
            "armorcomponent": "e22",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_22_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e22",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e22",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e22",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_22_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e22",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_23_hitpoint [Indent level: 2],
        "era_23_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e23",
            "armorcomponent": "e23",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_23_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e23",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e23",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e23",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_23_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e23",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_24_hitpoint [Indent level: 2],
        "era_24_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e24",
            "armorcomponent": "e24",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_24_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e24",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e24",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e24",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_24_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e24",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_25_hitpoint [Indent level: 2],
        "era_25_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e25",
            "armorcomponent": "e25",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_25_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e25",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e25",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e25",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_25_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e25",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_26_hitpoint [Indent level: 2],
        "era_26_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e26",
            "armorcomponent": "e26",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_26_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e26",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e26",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e26",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_26_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e26",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_27_hitpoint [Indent level: 2],
        "era_27_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e27",
            "armorcomponent": "e27",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_27_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e27",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e27",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e27",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_27_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e27",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_28_hitpoint [Indent level: 2],
        "era_28_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e28",
            "armorcomponent": "e28",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_28_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e28",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e28",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e28",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_28_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e28",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_29_hitpoint [Indent level: 2],
        "era_29_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e29",
            "armorcomponent": "e29",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_29_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_29_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e29",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_29_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e29",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_29_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e29",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_29_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e29",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_30_hitpoint [Indent level: 2],
        "era_30_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e30",
            "armorcomponent": "e30",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_30_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_30_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e30",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_30_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e30",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_30_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e30",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_30_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e30",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_31_hitpoint [Indent level: 2],
        "era_31_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e31",
            "armorcomponent": "e31",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_31_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_31_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e31",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_31_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e31",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_31_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e31",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_31_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e31",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_32_hitpoint [Indent level: 2],
        "era_32_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e32",
            "armorcomponent": "e32",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_32_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_32_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e32",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_32_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e32",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_32_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e32",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_32_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e32",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_33_hitpoint [Indent level: 2],
        "era_33_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e33",
            "armorcomponent": "e33",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_33_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_33_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e33",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_33_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e33",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_33_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e33",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_33_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e33",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_34_hitpoint [Indent level: 2],
        "era_34_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e34",
            "armorcomponent": "e34",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_34_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_34_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e34",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_34_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e34",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_34_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e34",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_34_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e34",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_35_hitpoint [Indent level: 2],
        "era_35_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e35",
            "armorcomponent": "e35",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_35_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_35_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e35",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_35_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e35",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_35_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e35",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_35_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e35",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_36_hitpoint [Indent level: 2],
        "era_36_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e36",
            "armorcomponent": "e36",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_36_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_36_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e36",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_36_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e36",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_36_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e36",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_36_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e36",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_37_hitpoint [Indent level: 2],
        "era_37_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e37",
            "armorcomponent": "e37",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_37_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_37_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e37",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_37_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e37",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_37_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e37",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_37_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e37",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_38_hitpoint [Indent level: 2],
        "era_38_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e38",
            "armorcomponent": "e38",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_38_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_38_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e38",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_38_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e38",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_38_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e38",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_38_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e38",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_39_hitpoint [Indent level: 2],
        "era_39_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e39",
            "armorcomponent": "e39",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_39_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_39_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e39",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_39_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e39",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_39_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e39",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_39_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e39",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_40_hitpoint [Indent level: 2],
        "era_40_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e40",
            "armorcomponent": "e40",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_40_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_40_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e40",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_40_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e40",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_40_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e40",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_40_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e40",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_41_hitpoint [Indent level: 2],
        "era_41_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e41",
            "armorcomponent": "e41",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_41_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_41_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e41",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_41_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e41",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_41_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e41",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_41_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e41",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_42_hitpoint [Indent level: 2],
        "era_42_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e42",
            "armorcomponent": "e42",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_42_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_42_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e42",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_42_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e42",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_42_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e42",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_42_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e42",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_43_hitpoint [Indent level: 2],
        "era_43_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e43",
            "armorcomponent": "e43",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_43_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_43_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e43",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_43_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e43",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_43_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e43",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_43_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e43",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_44_hitpoint [Indent level: 2],
        "era_44_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e44",
            "armorcomponent": "e44",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_44_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_44_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e44",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_44_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e44",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_44_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e44",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_44_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e44",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_45_hitpoint [Indent level: 2],
        "era_45_hitpoint": {
            "simulation": "RHS_ERA_BUSK",
            "armor": -150,
            "material": -1,
            "name": "e45",
            "armorcomponent": "e45",
            "passthrough": 0,
            "minimalhit": -0.4,
            "explosionshielding": 0.007,
            "radius": 0.16,
            "visual": "-",
            # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_45_hitpoint|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                "effectradius": 1,
                "ignorefuel": 1,
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_45_hitpoint|DestructionEffects|RHS_ERA_Flash [Indent level: 4],
                "rhs_era_flash": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Flash",
                    "position": "fx_e45",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 0.006
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_45_hitpoint|DestructionEffects|RHS_ERA_Sound [Indent level: 4],
                "rhs_era_sound": {
                    "simulation": "sound",
                    "type": "RHS_ERA_Explosion_Sound",
                    "position": "fx_e45",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 1
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_45_hitpoint|DestructionEffects|RHS_ERA_Smoke [Indent level: 4],
                "rhs_era_smoke": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Smoke",
                    "position": "fx_e45",
                    "intensity": 0.1,
                    "interval": 1,
                    "lifetime": 0.04
                },
                # Class: CfgVehicles|RHS_M2A2_BUSKI|HitPoints|era_45_hitpoint|DestructionEffects|RHS_ERA_Shard [Indent level: 4],
                "rhs_era_shard": {
                    "simulation": "particles",
                    "type": "RHS_ERA_Shard",
                    "position": "fx_e45",
                    "intensity": 1,
                    "interval": 1,
                    "lifetime": 0.03
                }
            }
        },
        # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitHull_Structural [Indent level: 2],
        "hithull_structural": {
            "armor": -600,
            "name": "Hit_Engine",
            "visual": "-",
            "passthrough": 0,
            "minimalhit": -0.22,
            "explosionshielding": 0,
            "radius": 0
        },
        # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitHull [Indent level: 2],
        "hithull": {
            "armor": -110,
            "name": "Hit_Hull",
            "armorcomponent": "Hit_Hull",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": -0.15,
            "explosionshielding": 0.01,
            "radius": 0.1,
            "depends": "HitHull_Structural",
            "material": -1
        },
        # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": -100,
            "name": "Hit_Engine",
            "armorcomponent": "Hit_Engine",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.14,
            "explosionshielding": 0.009,
            "radius": 0.17,
            # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "rhs_engine_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire [Indent level: 4],
                "rhs_engine_fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks [Indent level: 4],
                "rhs_engine_sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "rhs_engine_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "rhs_engine_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
                "rhs_engine_smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                }
            },
            "material": -1
        },
        # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitLTrack [Indent level: 2],
        "hitltrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackL",
            "name": "Hit_TrackL",
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "material": -1,
            "visual": "pas_L"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|HitRTrack [Indent level: 2],
        "hitrtrack": {
            "armor": -150,
            "armorcomponent": "Hit_TrackR",
            "name": "Hit_TrackR",
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.5,
            "radius": 0.3,
            "material": -1,
            "visual": "pas_P"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|Hit_LightL [Indent level: 2],
        "hit_lightl": {
            "armor": -10,
            "name": "l svetlo",
            "visual": "-",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 1,
            "radius": 0
        },
        # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|Hit_LightR [Indent level: 2],
        "hit_lightr": {
            "name": "p svetlo",
            "armor": -10,
            "visual": "-",
            "passthrough": 0,
            "minimalhit": -0.1,
            "explosionshielding": 1,
            "radius": 0
        },
        # Class: CfgVehicles|RHS_M2A2_Base|HitPoints|Hit_Optics_Dvr_Peri [Indent level: 2],
        "hit_optics_dvr_peri": {
            "armor": -40,
            "explosionshielding": 0,
            "name": "",
            "visual": "vis_optics_Dvr_Peri",
            "armorcomponent": "Hit_Optics_Dvr_Peri",
            "passthrough": 0
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 0.5,
            "material": -1,
            "armorcomponent": "hit_fuel",
            "name": "hit_fuel_point",
            "visual": "-",
            "passthrough": 0.3,
            "minimalhit": 0.1,
            "explosionshielding": 0.6,
            "radius": 0.3
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_Left_1 [Indent level: 2],
        "hitslat_left_1": {
            "simulation": "Armor_SLAT",
            "armorcomponent": "cage_left_1_geo",
            "name": "cage_left_1_point",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_Left_2 [Indent level: 2],
        "hitslat_left_2": {
            "armorcomponent": "cage_left_2_geo",
            "name": "cage_left_2_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_Left_3 [Indent level: 2],
        "hitslat_left_3": {
            "armorcomponent": "cage_left_3_geo",
            "name": "cage_left_3_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_Right_1 [Indent level: 2],
        "hitslat_right_1": {
            "armorcomponent": "cage_right_1_geo",
            "name": "cage_right_1_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_Right_2 [Indent level: 2],
        "hitslat_right_2": {
            "armorcomponent": "cage_right_2_geo",
            "name": "cage_right_2_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_Right_3 [Indent level: 2],
        "hitslat_right_3": {
            "armorcomponent": "cage_right_3_geo",
            "name": "cage_right_3_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_top_back [Indent level: 2],
        "hitslat_top_back": {
            "armorcomponent": "cage_top_back_geo",
            "name": "cage_top_back_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_top_left [Indent level: 2],
        "hitslat_top_left": {
            "armorcomponent": "cage_top_left_geo",
            "name": "cage_top_left_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_top_right [Indent level: 2],
        "hitslat_top_right": {
            "armorcomponent": "cage_top_right_geo",
            "name": "cage_top_right_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_back [Indent level: 2],
        "hitslat_back": {
            "armorcomponent": "cage_back_geo",
            "name": "cage_back_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|HitPoints|HitSLAT_front [Indent level: 2],
        "hitslat_front": {
            "armorcomponent": "cage_front_geo",
            "name": "cage_front_point",
            "simulation": "Armor_SLAT",
            "armor": -200,
            "minimalhit": 0.3,
            "passthrough": 0,
            "visual": "-",
            "explosionshielding": 2,
            "radius": 0.25
        }
    },
    "side": 1,
    # Class: CfgVehicles|RHS_M2A2|Library [Indent level: 1],
    "library": {
        "libtextdesc": "The M2 Bradley IFV (Infantry Fighting Vehicle) is an US infantry fighting vehicle. It is designed to transport infantry with armor protection while providing covering fire to suppressing enemy troops and armored vehicles.<br/>The A2 variant features improvements based on lessons learned during Gulf War in 1991."
    },
    "cargodoors": ["ramp"],
    # Class: CfgVehicles|RHS_M2A2|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV1.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV1_damage.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV1_destruct.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2_damage.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2_destruct.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2_ERAon.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2_ERAon_damage.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|brad_UV2_ERAon_destruct.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|M2_tracks.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|M2_tracks_damage.rvmat","rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|data|M2_tracks_destruct.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    "dlc": "RHS_USAF",
    "category": "Armored",
    "destrtype": "DestructDefault",
    "soundgetin": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1],
    "soundgetout": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1,20],
    "sounddammage": ["",0.562341,1],
    "soundengineonint": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_start",0.630957,1],
    "soundengineonext": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_start",1,1,200],
    "soundengineoffint": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_stop",0.630957,1],
    "soundengineoffext": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_stop",1,1,200],
    "buildcrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "buildcrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "buildcrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "buildcrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "soundbuildingcrash": ["buildCrash0",0.25,"buildCrash1",0.25,"buildCrash2",0.25,"buildCrash3",0.25],
    "woodcrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "woodcrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "woodcrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "woodcrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "woodcrash4": ["A3|sounds_f|Vehicles|crashes|crash_01",1,1,200],
    "woodcrash5": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "soundwoodcrash": ["woodCrash0",0.166,"woodCrash1",0.166,"woodCrash2",0.166,"woodCrash3",0.166,"woodCrash4",0.166,"woodCrash5",0.166],
    "armorcrash0": ["A3|sounds_f|Vehicles|crashes|crash_08",1,1,200],
    "armorcrash1": ["A3|sounds_f|Vehicles|crashes|crash_09",1,1,200],
    "armorcrash2": ["A3|sounds_f|Vehicles|crashes|crash_10",1,1,200],
    "armorcrash3": ["A3|sounds_f|Vehicles|crashes|crash_11",1,1,200],
    "soundarmorcrash": ["ArmorCrash0",0.25,"ArmorCrash1",0.25,"ArmorCrash2",0.25,"ArmorCrash3",0.25],
    # Class: CfgVehicles|RHS_M2A2_Base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Idle_ext [Indent level: 2]
        "idle_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_1",0.562341,1,160],
            "frequency": "0.3	+	((rpm/	2600) factor[(100/	2600),(250/	2600)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2600) factor[(100/	2600),(400/	2600)])	*	((rpm/	2600) factor[(730/	2600),(610/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine [Indent level: 2],
        "engine": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_2",0.794328,1,200],
            "frequency": "0.8	+	((rpm/	2600) factor[(600/	2600),(1100/	2600)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2600) factor[(550/	2600),(700/	2600)])	*	((rpm/	2600) factor[(1100/	2600),(760/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine1_ext [Indent level: 2],
        "engine1_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_3",0.891251,1,260],
            "frequency": "0.8	+	((rpm/	2600) factor[(770/	2600),(1400/	2600)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2600) factor[(720/	2600),(1060/	2600)])	*	((rpm/	2600) factor[(1400/	2600),(1180/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine2_ext [Indent level: 2],
        "engine2_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_4",1,1,280],
            "frequency": "0.8	+	((rpm/	2600) factor[(1150/	2600),(1700/	2600)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	2600) factor[(1130/	2600),(1370/	2600)])	*	((rpm/	2600) factor[(1700/	2600),(1500/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine3_ext [Indent level: 2],
        "engine3_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_5",1.12202,1,300],
            "frequency": "0.8	+	((rpm/	2600) factor[(1500/	2600),(2100/	2600)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	2600) factor[(1460/	2600),(1670/	2600)])	*	((rpm/	2600) factor[(2100/	2600),(1800/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine4_ext [Indent level: 2],
        "engine4_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_engine_6",1.25893,1,320],
            "frequency": "0.8	+	((rpm/	2600) factor[(1800/	2600),(2600/	2600)])*0.1",
            "volume": "engineOn*camPos*((rpm/	2600) factor[(1750/	2600),(2050/	2600)])"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|IdleThrust [Indent level: 2],
        "idlethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_1",1,1,250],
            "frequency": "0.8	+	((rpm/	2600) factor[(500/	2600),(650/	2600)])*0.15",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(100/	2600),(400/	2600)])	*	((rpm/	2600) factor[(730/	2600),(610/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|EngineThrust [Indent level: 2],
        "enginethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_2",1.12202,1,280],
            "frequency": "0.8	+	((rpm/	2600) factor[(600/	2600),(1100/	2600)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(550/	2600),(700/	2600)])	*	((rpm/	2600) factor[(1100/	2600),(760/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine1_Thrust_ext [Indent level: 2],
        "engine1_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_3",1.25893,1,300],
            "frequency": "0.8	+	((rpm/	2600) factor[(770/	2600),(1400/	2600)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(720/	2600),(1060/	2600)])	*	((rpm/	2600) factor[(1400/	2600),(1180/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine2_Thrust_ext [Indent level: 2],
        "engine2_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_4",1.41254,1,340],
            "frequency": "0.8	+	((rpm/	2600) factor[(1150/	2600),(1700/	2600)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(1130/	2600),(1370/	2600)])	*	((rpm/	2600) factor[(1700/	2600),(1500/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine3_Thrust_ext [Indent level: 2],
        "engine3_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_5",1.77828,1,360],
            "frequency": "0.8	+	((rpm/	2600) factor[(1500/	2600),(2100/	2600)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(1460/	2600),(1670/	2600)])	*	((rpm/	2600) factor[(2100/	2600),(1800/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine4_Thrust_ext [Indent level: 2],
        "engine4_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|ext_exhaust_6",1.99526,1,380],
            "frequency": "0.8	+	((rpm/	2600) factor[(1800/	2600),(2600/	2600)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	2600) factor[(1750/	2600),(2050/	2600)])"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Idle_int [Indent level: 2],
        "idle_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_1",0.316228,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(500/	2600),(650/	2600)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	2600) factor[(100/	2600),(400/	2600)])	*	((rpm/	2600) factor[(730/	2600),(610/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine_int [Indent level: 2],
        "engine_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_2",0.354813,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(600/	2600),(1100/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2600) factor[(550/	2600),(700/	2600)])	*	((rpm/	2600) factor[(1100/	2600),(760/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine1_int [Indent level: 2],
        "engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_3",0.398107,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(770/	2600),(1400/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2600) factor[(720/	2600),(1060/	2600)])	*	((rpm/	2600) factor[(1400/	2600),(1180/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine2_int [Indent level: 2],
        "engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_4",0.446684,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1150/	2600),(1700/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	2600) factor[(1130/	2600),(1370/	2600)])	*	((rpm/	2600) factor[(1700/	2600),(1500/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine3_int [Indent level: 2],
        "engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_5",0.501187,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1500/	2600),(2100/	2600)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	2600) factor[(1460/	2600),(1670/	2600)])	*	((rpm/	2600) factor[(2100/	2600),(1800/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine4_int [Indent level: 2],
        "engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_engine_6",0.562341,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1800/	2600),(2600/	2600)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	2600) factor[(1750/	2600),(2050/	2600)])"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|IdleThrust_int [Indent level: 2],
        "idlethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_1",0.354813,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(500/	2600),(650/	2600)])*0.15",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(100/	2600),(400/	2600)])	*	((rpm/	2600) factor[(730/	2600),(610/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|EngineThrust_int [Indent level: 2],
        "enginethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_2",0.398107,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(600/	2600),(1100/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(550/	2600),(700/	2600)])	*	((rpm/	2600) factor[(1100/	2600),(760/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine1_Thrust_int [Indent level: 2],
        "engine1_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_3",0.446684,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(770/	2600),(1400/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(720/	2600),(1060/	2600)])	*	((rpm/	2600) factor[(1400/	2600),(1180/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine2_Thrust_int [Indent level: 2],
        "engine2_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_4",0.446684,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1150/	2600),(1700/	2600)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(1130/	2600),(1370/	2600)])	*	((rpm/	2600) factor[(1700/	2600),(1500/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine3_Thrust_int [Indent level: 2],
        "engine3_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_5",0.501187,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1500/	2600),(2100/	2600)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	2600) factor[(1460/	2600),(1670/	2600)])	*	((rpm/	2600) factor[(2100/	2600),(1800/	2600)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|Engine4_Thrust_int [Indent level: 2],
        "engine4_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|APC|APC3|int_exhaust_6",0.562341,1],
            "frequency": "0.8	+	((rpm/	2600) factor[(1800/	2600),(2600/	2600)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	2600) factor[(1750/	2600),(2050/	2600)])"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|NoiseInt [Indent level: 2],
        "noiseint": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_int_1",3.16228,1],
            "frequency": "1",
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|NoiseExt [Indent level: 2],
        "noiseext": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_ext_1",3.16228,1,250],
            "frequency": "1",
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 15])"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsOutH0 [Indent level: 2],
        "threadsouth0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_01",0.398107,1,140],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-0) max 0)/	95),(((-10) max 10)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-25) max 25)/	95),(((-15) max 15)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsOutH1 [Indent level: 2],
        "threadsouth1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_02",0.446684,1,160],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-20) max 20)/	95),(((-35) max 35)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-55) max 55)/	95),(((-40) max 40)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsOutH2 [Indent level: 2],
        "threadsouth2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_03",0.501187,1,180],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-45) max 45)/	95),(((-55) max 55)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-70) max 70)/	95),(((-60) max 60)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsOutH3 [Indent level: 2],
        "threadsouth3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_04",0.562341,1,200],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-65) max 65)/	95),(((-70) max 70)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-85) max 85)/	95),(((-80) max 80)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsOutH4 [Indent level: 2],
        "threadsouth4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_hard_05",0.562341,1,220],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)/	95) factor[(((-80) max 80)/	95),(((-90) max 90)/	95)])"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsOutS0 [Indent level: 2],
        "threadsouts0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_01",0.316228,1,120],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-0) max 0)/	95),(((-10) max 10)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-25) max 25)/	95),(((-15) max 15)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsOutS1 [Indent level: 2],
        "threadsouts1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_02",0.354813,1,140],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-20) max 20)/	95),(((-35) max 35)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-55) max 55)/	95),(((-40) max 40)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsOutS2 [Indent level: 2],
        "threadsouts2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_03",0.398107,1,160],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-45) max 45)/	95),(((-55) max 55)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-70) max 70)/	95),(((-60) max 60)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsOutS3 [Indent level: 2],
        "threadsouts3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_04",0.446684,1,180],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-65) max 65)/	95),(((-70) max 70)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-85) max 85)/	95),(((-80) max 80)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsOutS4 [Indent level: 2],
        "threadsouts4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|ext_treads_soft_05",0.501187,1,200],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)/	95) factor[(((-80) max 80)/	95),(((-90) max 90)/	95)])"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsInH0 [Indent level: 2],
        "threadsinh0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_01",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-0) max 0)/	95),(((-10) max 10)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-25) max 25)/	95),(((-15) max 15)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsInH1 [Indent level: 2],
        "threadsinh1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_02",0.501187,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-20) max 20)/	95),(((-35) max 35)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-55) max 55)/	95),(((-40) max 40)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsInH2 [Indent level: 2],
        "threadsinh2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_03",0.562341,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-45) max 45)/	95),(((-55) max 55)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-70) max 70)/	95),(((-60) max 60)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsInH3 [Indent level: 2],
        "threadsinh3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_04",0.630957,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-65) max 65)/	95),(((-70) max 70)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-85) max 85)/	95),(((-80) max 80)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsInH4 [Indent level: 2],
        "threadsinh4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_05",0.707946,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)/	95) factor[(((-80) max 80)/	95),(((-90) max 90)/	95)])"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsInS0 [Indent level: 2],
        "threadsins0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_01",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-0) max 0)/	95),(((-10) max 10)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-25) max 25)/	95),(((-15) max 15)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsInS1 [Indent level: 2],
        "threadsins1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_02",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-20) max 20)/	95),(((-35) max 35)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-55) max 55)/	95),(((-40) max 40)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsInS2 [Indent level: 2],
        "threadsins2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_03",0.501187,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-45) max 45)/	95),(((-55) max 55)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-70) max 70)/	95),(((-60) max 60)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsInS3 [Indent level: 2],
        "threadsins3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_04",0.630957,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	95) factor[(((-65) max 65)/	95),(((-70) max 70)/	95)])	*	((((-speed*3.6) max speed*3.6)/	95) factor[(((-85) max 85)/	95),(((-80) max 80)/	95)]))"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Sounds|ThreadsInS4 [Indent level: 2],
        "threadsins4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_05",0.707946,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)/	95) factor[(((-80) max 80)/	95),(((-90) max 90)/	95)])"
        }
    },
    "simulation": "tankX",
    "normalspeedforwardcoef": 0.6,
    "slowspeedforwardcoef": 0.45,
    "fuelcapacity": 24.15,
    "rhs_fuelcapacity": 462,
    "maxspeed": 66,
    "tracksspeed": 10,
    "maxfordingdepth": 0,
    "waterresistance": 0,
    "waterdamageengine": 0.2,
    "waterleakiness": 10,
    "tankturnforce": 450000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.87,
    "accelaidforcecoef": 2,
    "accelaidforceyoffset": -4,
    "accelaidforcespd": 4.23,
    "torquecurve": [[0.307692,0.518072],[0.384615,0.855422],[0.538462,1],[0.576923,0.945783],[0.653846,0.909639],[0.769231,0.873494],[0.903846,0.843373],[1.02962,0]],
    "enginemoi": 5,
    "enginepower": 447,
    "peaktorque": 1660,
    "minomega": 84,
    "maxomega": 272.27,
    "idlerpm": 800,
    "redrpm": 2600,
    "thrustdelay": 0.3,
    "brakeidlespeed": 1.78,
    "switchtime": 0.1,
    "latency": 1,
    "clutchstrength": 35,
    "enginelosses": 25,
    "transmissionlosses": 15,
    "changegeartype": "rpmratio",
    "changegearomegaratios": [1,0.384615,0.384615,0,0.923077,0.384615,0.961538,0.538462,0.961538,0.576923,1,0.692308],
    # Class: CfgVehicles|RHS_M2A2_Base|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-2.2,"N",0,"D1",4.2,"D2",2.23,"D3",1.22,"D4",0.839],
        "transmissionratios": ["High",14.75],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R"
    },
    # Class: CfgVehicles|RHS_M2A2_Base|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|L2 [Indent level: 2]
        "l2": {
            "susptraveldirection": [-0.125,-1,0],
            "bonename": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|L3 [Indent level: 2],
        "l3": {
            "bonename": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|L4 [Indent level: 2],
        "l4": {
            "bonename": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|L5 [Indent level: 2],
        "l5": {
            "bonename": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|L6 [Indent level: 2],
        "l6": {
            "bonename": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|L7 [Indent level: 2],
        "l7": {
            "bonename": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|L9 [Indent level: 2],
        "l9": {
            "bonename": "wheel_podkolol9",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|L1 [Indent level: 2],
        "l1": {
            "bonename": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|R2 [Indent level: 2],
        "r2": {
            "susptraveldirection": [0.125,-1,0],
            "bonename": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|R3 [Indent level: 2],
        "r3": {
            "bonename": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|R4 [Indent level: 2],
        "r4": {
            "bonename": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|R5 [Indent level: 2],
        "r5": {
            "bonename": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|R6 [Indent level: 2],
        "r6": {
            "bonename": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|R7 [Indent level: 2],
        "r7": {
            "bonename": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|R9 [Indent level: 2],
        "r9": {
            "bonename": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Wheels|R1 [Indent level: 2],
        "r1": {
            "bonename": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "steering": 0,
            "width": 0.4,
            "mass": 130,
            "moi": 10.0392,
            "maxbraketorque": 6520,
            "sprungmass": 2500,
            "springstrength": 256250,
            "springdamperrate": 14811,
            "dampingrate": 1088,
            "dampingrateinair": 1088,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3.5,
            "latstiffy": 45,
            "longitudinalstiffnessperunitgravity": 14000,
            "frictionvsslipgraph": [[0,0.45],[0.32,1],[0.6,0.86]]
        }
    },
    "vehicleclass": "rhs_vehclass_ifv",
    "editorsubcategory": "rhs_EdSubcat_ifv",
    # Class: CfgVehicles|RHS_M2A2_Base|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|RHS_M2A2_Base|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_vehicle_APC_s"],
            "speechplural": ["veh_vehicle_APC_p"]
        }
    },
    "textsingular": "IFV",
    "textplural": "IFVs",
    "namesound": "veh_vehicle_APC_s",
    "driveoncomponent": ["slide","trackL","trackR"],
    "unitinfotype": "RHSUSF_RscUnitInfoWestTank",
    "picture": "rhsusf|addons|rhsusf_a2port_armor|pictures|rhs_m2a2_pic_ca.paa",
    "icon": "rhsusf|addons|rhsusf_a2port_armor|Data|UI|Icon_m2a2_CA.paa",
    "mapsize": 7,
    "accuracy": 0.3,
    "transportsoldier": 6,
    "getinaction": "GetInHigh",
    "getoutaction": "GetOutHigh",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
    "memorypointsgetincargo": ["pos cargo","pos cargo 1","pos cargo 2","pos cargo 3"],
    "memorypointsgetincargodir": ["pos cargo dir","pos cargo 1 dir","pos cargo dir","pos cargo 2 dir","pos cargo 3 dir"],
    "cargoproxyindexes": [1,2,3,4,5,6],
    "getinproxyorder": [1,2,3,4,5,6],
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "rhs_hassmokecap": 1,
    "reportownposition": 1,
    "delaybetweenejects": 0.5,
    "loddriverturnedin": 1100,
    "loddriverturnedout": 0,
    "loddriveropticsin": 0,
    "viewdriverinexternal": 1,
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 0.05,
    "viewcargoshadowamb": 0.5,
    "headgforceleaningfactor": [0.015,0.011,0.015],
    # Class: CfgVehicles|RHS_M2A2_Base|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    "driverlefthandanimname": "yoke",
    "driverrighthandanimname": "yoke",
    "texturelist": [],
    "driveropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_vision_block",
    "forcehidedriver": 0,
    "driverforceoptics": 0,
    "driverdoor": "hatchD",
    "dustfrontleftpos": "wheel_1_4_bound",
    "dustfrontrightpos": "wheel_2_4_bound",
    "dustbackleftpos": "wheel_1_7_bound",
    "dustbackrightpos": "wheel_2_7_bound",
    "radartype": 1,
    "lockdetectionsystem": 0,
    "incomingmissiledetectionsystem": 0,
    "irtarget": 1,
    "irscanground": 0,
    "threat": [0.9,0.9,0.4],
    "armor": 290,
    "armorstructural": 280,
    "explosionshielding": 15,
    # Class: CfgVehicles|RHS_M2A2_Base|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            "lockwhendriverout": 1,
            "turretinfotype": "RHS_RscODS_ISU",
            "discretedistance": [0,200,400,600,800,1000,1200,1400,1600,1800,2000,2200,2400,2600,2800,3000],
            "discretedistanceinitindex": 2,
            "gunnerhasflares": 0,
            "gunnerforceoptics": 1,
            "gunneraction": "RHS_M2A2_GunnerOut",
            "gunnerinaction": "RHS_M2A2_Gunner",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "gunnerdoor": "hatchG",
            "minelev": -9,
            "maxelev": 57,
            "initelev": 0,
            "viewgunnerinexternal": 1,
            "showcrewaim": 0,
            "allowtablock": 0,
            "maxhorizontalrotspeed": 1.04,
            "maxverticalrotspeed": 1.04,
            "stabilizedinaxes": 3,
            "startengine": 0,
            "hideweaponsgunner": 1,
            "selectionfireanim": "zasleh2",
            "weapons": ["RHS_weap_M242BC","rhs_weap_m240_bradley_coax","Rhs_weap_TOW_Launcher","rhs_weap_fcs_ammo"],
            "magazines": ["rhs_mag_1100Rnd_762x51_M240","rhs_mag_1100Rnd_762x51_M240","rhs_mag_230Rnd_25mm_M242_HEI","rhs_mag_230Rnd_25mm_M242_HEI","rhs_mag_230Rnd_25mm_M242_HEI","rhs_mag_70Rnd_25mm_M242_APFSDS","rhs_mag_70Rnd_25mm_M242_APFSDS","rhs_mag_70Rnd_25mm_M242_APFSDS","rhs_mag_2Rnd_TOW2A","rhs_mag_2Rnd_TOW2A","rhs_mag_2Rnd_TOW2A","rhs_mag_2Rnd_TOW2BB","rhs_laserfcsmag"],
            # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|OpticsIn|Wide [Indent level: 4]
                "wide": {
                    "opticsdisplayname": "WIDE",
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "initfov": 0.175,
                    "minfov": 0.175,
                    "maxfov": 0.175,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [4],
                    "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_ISU",
                    "gunneropticseffect": [],
                    "hitpoint": "Hit_Optics_Gnr"
                },
                # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|OpticsIn|Narrow [Indent level: 4],
                "narrow": {
                    "opticsdisplayname": "NARROW",
                    "initfov": 0.0583333,
                    "minfov": 0.0583333,
                    "maxfov": 0.0583333,
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [4],
                    "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_ISU",
                    "gunneropticseffect": [],
                    "hitpoint": "Hit_Optics_Gnr"
                }
            },
            # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets [Indent level: 3],
            "turrets": {
                # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics [Indent level: 4]
                "commanderoptics": {
                    "body": "obsTurret",
                    "gun": "obsGun",
                    "animationsourcebody": "obsTurret",
                    "animationsourcegun": "obsGun",
                    "memorypointgunneroptics": "commanderview",
                    "minelev": -5,
                    "maxelev": 5,
                    "initelev": 0,
                    "minturn": -360,
                    "maxturn": 360,
                    "initturn": 0,
                    "hideweaponsgunner": 1,
                    "weapons": ["rhsusf_weap_M257_8"],
                    "magazines": ["rhsusf_mag_L8A3_8"],
                    "turretinfotype": "RHS_RscODS_ISU",
                    "gunneraction": "RHS_M2A2_CommanderOut",
                    "gunnerinaction": "RHS_M2A2_Commander",
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "gunnerforceoptics": 1,
                    "gunnerdoor": "hatchC",
                    "gunneropticsmodel": "rhsusf|addons|rhsusf_a2port_armor|M2A2_Bradley|gunnerOptics_M2A2_2",
                    "gunneropticseffect": [],
                    # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
                    "viewoptics": {
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "initfov": 0.155,
                        "minfov": 0.067,
                        "maxfov": 0.155
                    },
                    # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|VisionBlock [Indent level: 6]
                        "visionblock": {
                            "opticsdisplayname": "periscope",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "initfov": 0.7,
                            "minfov": 0.7,
                            "maxfov": 0.7,
                            "visionmode": ["Normal","NVG"],
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_vision_block",
                            "gunneropticseffect": [],
                            "hitpoint": "Hit_Optics_Cdr_Peri"
                        },
                        # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Wide [Indent level: 6],
                        "wide": {
                            "campos": "gunnerview",
                            "opticsdisplayname": "WIDE",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "initfov": 0.175,
                            "minfov": 0.175,
                            "maxfov": 0.175,
                            "visionmode": ["Normal","Ti"],
                            "thermalmode": [4],
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_ISU",
                            "gunneropticseffect": [],
                            "hitpoint": "Hit_Optics_Gnr"
                        },
                        # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Narrow [Indent level: 6],
                        "narrow": {
                            "opticsdisplayname": "NARROW",
                            "initfov": 0.0583333,
                            "minfov": 0.0583333,
                            "maxfov": 0.0583333,
                            "campos": "gunnerview",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "visionmode": ["Normal","Ti"],
                            "thermalmode": [4],
                            "gunneropticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_ISU",
                            "gunneropticseffect": [],
                            "hitpoint": "Hit_Optics_Gnr"
                        }
                    },
                    "startengine": 0,
                    "gunnerhasflares": 1,
                    "viewgunnerinexternal": 1,
                    "outgunnermayfire": 1,
                    "ingunnermayfire": 1,
                    "showcrewaim": 0,
                    "allowtablock": 0,
                    # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitTurretCom [Indent level: 6]
                        "hitturretcom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.001,
                            "radius": 0.25,
                            "isturret": 1
                        },
                        # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitGunCom [Indent level: 6],
                        "hitguncom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.03,
                            "explosionshielding": 0.001,
                            "radius": 0.25,
                            "isgun": 1
                        },
                        # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|Hit_Optics_Cdr_Peri [Indent level: 6],
                        "hit_optics_cdr_peri": {
                            "armor": -40,
                            "explosionshielding": 0,
                            "name": "",
                            "visual": "vis_optics_Cdr_Peri",
                            "armorcomponent": "Hit_Optics_Cdr_Peri",
                            "passthrough": 0
                        }
                    },
                    # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|Reflectors [Indent level: 5],
                    "reflectors": {
                        # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|Reflectors|cabin [Indent level: 6]
                        "cabin": {
                            "color": [800,900,650],
                            "ambient": [5,5,5],
                            "intensity": 0.3,
                            "size": 1,
                            "innerangle": 90,
                            "outerangle": 165,
                            "conefadecoef": 1,
                            "position": "cabin_light",
                            "direction": "cabin_light_dir",
                            "hitpoint": "cabin_light",
                            "selection": "cabin_light",
                            "useflare": 1,
                            "flaresize": 1,
                            "flaremaxdistance": 5,
                            "daylight": 1,
                            "blinking": 0,
                            # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|Reflectors|cabin|Attenuation [Indent level: 7],
                            "attenuation": {
                                "start": 0,
                                "constant": 0,
                                "linear": 1,
                                "quadratic": 50,
                                "hardlimitstart": 1,
                                "hardlimitend": 1.5
                            }
                        },
                        # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|Reflectors|cargo_light_1 [Indent level: 6],
                        "cargo_light_1": {
                            "color": [800,900,650],
                            "position": "cargo_light_1",
                            "direction": "cargo_light_1_dir",
                            "hitpoint": "cargo_light_1",
                            "selection": "cargo_light_1",
                            "intensity": 3,
                            "useflare": 0,
                            "conefadecoef": 0.1,
                            "innerangle": 140,
                            "outerangle": 175,
                            # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|Turrets|CommanderOptics|Reflectors|cargo_light_1|Attenuation [Indent level: 7],
                            "attenuation": {
                                "start": 0,
                                "constant": 0,
                                "linear": 1,
                                "quadratic": 70,
                                "hardlimitstart": 1.4,
                                "hardlimitend": 2
                            },
                            "ambient": [5,5,5],
                            "size": 1,
                            "flaresize": 1,
                            "flaremaxdistance": 5,
                            "daylight": 1,
                            "blinking": 0
                        }
                    },
                    "memorypointgunneroutoptics": "commanderview",
                    "soundservo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",0.562341,1,30],
                    "soundservovertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",0.562341,1,30],
                    "gunneroutopticsmodel": "",
                    "ispersonturret": 1,
                    "personturretaction": "vehicle_turnout_1",
                    "minoutelev": -10,
                    "maxoutelev": 15,
                    "initoutelev": 0,
                    "minoutturn": -45,
                    "maxoutturn": 90,
                    "initoutturn": 0,
                    "usepip": 2,
                    "animationsourcestickx": "com_turret_control_x",
                    "animationsourcesticky": "com_turret_control_y",
                    "gunnerrighthandanimname": "com_turret_control",
                    "turretfollowfreelook": 2,
                    "viewgunnershadowamb": 0.5,
                    "viewgunnershadowdiff": 0.05,
                    "lodturnedin": 1000,
                    "lodopticsin": 0,
                    # Class: CfgVehicles|APC_Tracked_03_base_F|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
                    "viewgunner": {
                        "initanglex": -5,
                        "initangley": 0,
                        "initfov": 0.9,
                        "minfov": 0.25,
                        "maxfov": 1.25,
                        "minanglex": -65,
                        "maxanglex": 85,
                        "minangley": -150,
                        "maxangley": 150,
                        "minmovex": -0.075,
                        "maxmovex": 0.075,
                        "minmovey": -0.075,
                        "maxmovey": 0.075,
                        "minmovez": -0.075,
                        "maxmovez": 0.1,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    "stabilizedinaxes": 3,
                    "maxhorizontalrotspeed": 1.8,
                    "maxverticalrotspeed": 1.8,
                    # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: VehicleSystemsTemplateLeftCommander|Components [Indent level: 0]
                            "components": {
                                # Class: VehicleSystemsTemplateLeftCommander|Components|VehicleDriverDisplay [Indent level: 1]
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateLeftCommander|Components|VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "left": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        },
                        # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: VehicleSystemsTemplateRightCommander|Components [Indent level: 0]
                            "components": {
                                # Class: VehicleSystemsTemplateRightCommander|Components|VehicleDriverDisplay [Indent level: 1]
                                "vehicledriverdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "Driver"
                                },
                                # Class: VehicleSystemsTemplateRightCommander|Components|VehiclePrimaryGunnerDisplay [Indent level: 1],
                                "vehicleprimarygunnerdisplay": {
                                    "componenttype": "TransportFeedDisplayComponent",
                                    "source": "PrimaryGunner"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                                "emptydisplay": {
                                    "componenttype": "EmptyDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                                "minimapdisplay": {
                                    "componenttype": "MinimapDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                                "minedetectordisplay": {
                                    "componenttype": "MineDetectorDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                                "crewdisplay": {
                                    "componenttype": "CrewDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                                "uavdisplay": {
                                    "componenttype": "UAVFeedDisplayComponent"
                                },
                                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                                "slingloaddisplay": {
                                    "componenttype": "SlingLoadDisplayComponent"
                                }
                            },
                            "componenttype": "VehicleSystemsDisplayManager",
                            "right": 1,
                            "defaultdisplay": "EmptyDisplay",
                            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                        }
                    },
                    "proxytype": "CPCommander",
                    "proxyindex": 1,
                    "gunnername": "Commander",
                    "primarygunner": 0,
                    "primaryobserver": 1,
                    "animationsourcehatch": "hatchCommander",
                    "animationsourcecamelev": "camElev",
                    "gunbeg": "",
                    "gunend": "",
                    "commanding": 2,
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutforceoptics": 0,
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
                    "memorypointgun": "gun_muzzle",
                    "selectionfireanim": "zasleh_1",
                    "gunnertype": "",
                    "soundelevation": ["",0.00316228,1],
                    "mincamelev": -90,
                    "maxcamelev": 90,
                    "initcamelev": 0,
                    "primary": 1,
                    "hasgunner": 1,
                    "turretcansee": 0,
                    "canusescanners": 1,
                    # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
                    "turretspec": {
                        "showheadphones": 0
                    },
                    "gunneropticscolor": [0,0,0,1],
                    "gunneropticsshowcursor": 0,
                    "gunnerfirealsoininternalcamera": 1,
                    "gunneroutfirealsoininternalcamera": 1,
                    "gunnerusespilotview": 0,
                    "castgunnershadow": 0,
                    "viewgunnershadow": 1,
                    "ejectdeadgunner": 0,
                    "canhidegunner": -1,
                    "forcehidegunner": 0,
                    "showhmd": 0,
                    "lockwhendriverout": 0,
                    "lockwhenvehiclespeed": -1,
                    "gunnercompartments": "Compartment1",
                    "lodturnedout": -1,
                    "memorypointsgetingunnerprecise": "",
                    "missilebeg": "spice rakety",
                    "missileend": "konec rakety",
                    "armorlights": 0.4,
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
                    "forcenvg": 0,
                    "iscopilot": 0,
                    "caneject": 1,
                    "gunnerlefthandanimname": "",
                    "gunnerleftleganimname": "",
                    "gunnerrightleganimname": "",
                    "precisegetinout": 0,
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
                    }
                }
            },
            # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": -60,
                    "armorcomponent": "Hit_Turret",
                    "name": "vez",
                    "visual": "vez",
                    "passthrough": 0,
                    "minimalhit": -0.3,
                    "explosionshielding": 0.001,
                    "radius": 0.08,
                    "isturret": 1
                },
                # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": -60,
                    "armorcomponent": "Hit_Gun",
                    "name": "zbran",
                    "visual": "-",
                    "passthrough": 0,
                    "minimalhit": -0.3,
                    "explosionshielding": 0.001,
                    "radius": 0.1,
                    "isgun": 1
                },
                # Class: CfgVehicles|RHS_M2A2_Base|Turrets|MainTurret|HitPoints|Hit_Optics_Gnr [Indent level: 4],
                "hit_optics_gnr": {
                    "armor": -40,
                    "explosionshielding": 0,
                    "name": "",
                    "visual": "vis_optics_Gnr",
                    "armorcomponent": "Hit_Optics_Gnr",
                    "passthrough": 0
                }
            },
            "gunbeg": "Usti hlavne",
            "gunend": "Konec hlavne",
            "soundservo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner",0.562341,1,30],
            "soundservovertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_gunner_vertical",0.562341,1,30],
            "forcehidegunner": 0,
            "memorypointgunneroptics": "gunnerview",
            "gunneroutopticsmodel": "",
            "gunneroutopticseffect": [],
            "gunneropticseffect": [],
            "usepip": 2,
            "animationsourcestickx": "turret_control_x",
            "animationsourcesticky": "turret_control_y",
            "gunnerlefthandanimname": "turret_control",
            "lodturnedin": 1000,
            "lodopticsin": 0,
            "viewgunnershadowamb": 0.5,
            "viewgunnershadowdiff": 0.05,
            "ingunnermayfire": 1,
            "commanding": 1,
            # Class: CfgVehicles|APC_Tracked_03_base_F|Turrets|MainTurret|ViewGunner [Indent level: 3],
            "viewgunner": {
                "initanglex": -5,
                "initangley": 0,
                "initfov": 0.9,
                "minfov": 0.25,
                "maxfov": 1.25,
                "minanglex": -65,
                "maxanglex": 85,
                "minangley": -150,
                "maxangley": 150,
                "minmovex": -0.075,
                "maxmovex": 0.075,
                "minmovey": -0.075,
                "maxmovey": 0.075,
                "minmovez": -0.075,
                "maxmovez": 0.1,
                "continuous": 0,
                "speedzoommaxspeed": 1e+010,
                "speedzoommaxfov": 0
            },
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "primarygunner": 1,
            # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: VehicleSystemsTemplateLeftGunner|Components [Indent level: 0]
                    "components": {
                        # Class: VehicleSystemsTemplateLeftGunner|Components|VehicleDriverDisplay [Indent level: 1]
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateLeftGunner|Components|VehicleCommanderDisplay [Indent level: 1],
                        "vehiclecommanderdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "left": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                },
                # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    # Class: VehicleSystemsTemplateRightGunner|Components [Indent level: 0]
                    "components": {
                        # Class: VehicleSystemsTemplateRightGunner|Components|VehicleDriverDisplay [Indent level: 1]
                        "vehicledriverdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Driver"
                        },
                        # Class: VehicleSystemsTemplateRightGunner|Components|VehicleCommanderDisplay [Indent level: 1],
                        "vehiclecommanderdisplay": {
                            "componenttype": "TransportFeedDisplayComponent",
                            "source": "Commander"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                        "emptydisplay": {
                            "componenttype": "EmptyDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                        "minimapdisplay": {
                            "componenttype": "MinimapDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                        "minedetectordisplay": {
                            "componenttype": "MineDetectorDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                        "crewdisplay": {
                            "componenttype": "CrewDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                        "uavdisplay": {
                            "componenttype": "UAVFeedDisplayComponent"
                        },
                        # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                        "slingloaddisplay": {
                            "componenttype": "SlingLoadDisplayComponent"
                        }
                    },
                    "componenttype": "VehicleSystemsDisplayManager",
                    "right": 1,
                    "defaultdisplay": "EmptyDisplay",
                    "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
                    "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
                }
            },
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
            "primaryobserver": 0,
            "soundelevation": ["",0.00316228,1],
            "minturn": -360,
            "maxturn": 360,
            "initturn": 0,
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "primary": 1,
            "hasgunner": 1,
            "turretcansee": 0,
            "canusescanners": 1,
            # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
            "turretspec": {
                "showheadphones": 0
            },
            "gunneropticscolor": [0,0,0,1],
            "gunneropticsshowcursor": 0,
            "gunneroutopticscolor": [0,0,0,1],
            "memorypointgunneroutoptics": "",
            "gunneroutforceoptics": 0,
            "gunneroutopticsshowcursor": 0,
            "gunnerfirealsoininternalcamera": 1,
            "gunneroutfirealsoininternalcamera": 1,
            "gunnerusespilotview": 0,
            "castgunnershadow": 0,
            "viewgunnershadow": 1,
            "ejectdeadgunner": 0,
            "canhidegunner": -1,
            "outgunnermayfire": 0,
            "showhmd": 0,
            "lockwhenvehiclespeed": -1,
            "gunnercompartments": "Compartment1",
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
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
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
            "memorypointgun": "kulas"
        }
    },
    "driveraction": "RHS_M2A2_DriverOut",
    "driverinaction": "RHS_M2A2_Driver",
    "cargoaction": ["RHS_M113_Cargo03","RHS_M113_Cargo03","RHS_M113_Cargo03","RHS_M113_Cargo02","RHS_M113_Cargo02","RHS_M113_Cargo02"],
    "insidesoundcoef": 0.9,
    # Class: CfgVehicles|RHS_M2A2_Base|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|RHS_M2A2_Base|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "vyfuk start",
            "direction": "vyfuk konec",
            "effect": "ExhaustEffectTankSide"
        }
    },
    # Class: CfgVehicles|RHS_M2A2_Base|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": 7,
        "minanglex": -15,
        "maxanglex": 25,
        "initangley": 0,
        "minangley": -90,
        "maxangley": 90,
        "initfov": 0.9,
        "minfov": 0.25,
        "maxfov": 1.25,
        "minmovex": -0.075,
        "maxmovex": 0.075,
        "minmovey": -0.075,
        "maxmovey": 0.075,
        "minmovez": -0.075,
        "maxmovez": 0.1,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|RHS_M2A2_Base|ViewOptics [Indent level: 1],
    "viewoptics": {
        "visionmode": ["Normal","NVG"],
        "initfov": 0.7,
        "minfov": 0.7,
        "maxfov": 0.7,
        "initanglex": 0,
        "minanglex": -30,
        "maxanglex": 30,
        "initangley": 0,
        "minangley": -100,
        "maxangley": 100,
        "minmovex": 0,
        "maxmovex": 0,
        "minmovey": 0,
        "maxmovey": 0,
        "minmovez": 0,
        "maxmovez": 0,
        "speedzoommaxspeed": 1e+010,
        "speedzoommaxfov": 0
    },
    # Class: CfgVehicles|RHS_M2A2_Base|DriverOpticsIn [Indent level: 1],
    "driveropticsin": {
        # Class: CfgVehicles|RHS_M2A2_Base|DriverOpticsIn|Wide [Indent level: 2]
        "wide": {
            "opticsmodel": "rhsusf|addons|rhsusf_optics|data|rhsusf_vision_block",
            "hitpoint": "Hit_Optics_Dvr_Peri",
            "visionmode": ["Normal","NVG"],
            "initfov": 0.7,
            "minfov": 0.7,
            "maxfov": 0.7,
            "initanglex": 0,
            "minanglex": -30,
            "maxanglex": 30,
            "initangley": 0,
            "minangley": -100,
            "maxangley": 100,
            "minmovex": 0,
            "maxmovex": 0,
            "minmovey": 0,
            "maxmovey": 0,
            "minmovez": 0,
            "maxmovez": 0,
            "speedzoommaxspeed": 1e+010,
            "speedzoommaxfov": 0
        }
    },
    # Class: CfgVehicles|RHS_M2A2_Base|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|RHS_M2A2_Base|TransportBackpacks|_xx_rhsusf_falconii [Indent level: 2]
        "_xx_rhsusf_falconii": {
            "backpack": "rhsusf_falconii",
            "count": 8
        }
    },
    # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhs_mag_30Rnd_556x45_M855A1_Stanag [Indent level: 2]
        "_xx_rhs_mag_30rnd_556x45_m855a1_stanag": {
            "magazine": "rhs_mag_30Rnd_556x45_M855A1_Stanag",
            "count": 75
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhsusf_100Rnd_556x45_soft_pouch [Indent level: 2],
        "_xx_rhsusf_100rnd_556x45_soft_pouch": {
            "magazine": "rhsusf_100Rnd_556x45_soft_pouch",
            "count": 11
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhsusf_100Rnd_762x51 [Indent level: 2],
        "_xx_rhsusf_100rnd_762x51": {
            "magazine": "rhsusf_100Rnd_762x51",
            "count": 11
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhs_fgm148_magazine_AT [Indent level: 2],
        "_xx_rhs_fgm148_magazine_at": {
            "magazine": "rhs_fgm148_magazine_AT",
            "count": 4
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhs_mag_M441_HE [Indent level: 2],
        "_xx_rhs_mag_m441_he": {
            "magazine": "rhs_mag_M441_HE",
            "count": 20
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhs_mag_M714_white [Indent level: 2],
        "_xx_rhs_mag_m714_white": {
            "magazine": "rhs_mag_M714_white",
            "count": 8
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhs_mag_M662_red [Indent level: 2],
        "_xx_rhs_mag_m662_red": {
            "magazine": "rhs_mag_M662_red",
            "count": 4
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhs_mag_m67 [Indent level: 2],
        "_xx_rhs_mag_m67": {
            "magazine": "rhs_mag_m67",
            "count": 10
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhs_mag_m18_green [Indent level: 2],
        "_xx_rhs_mag_m18_green": {
            "magazine": "rhs_mag_m18_green",
            "count": 4
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhs_mag_m18_red [Indent level: 2],
        "_xx_rhs_mag_m18_red": {
            "magazine": "rhs_mag_m18_red",
            "count": 4
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportMagazines|_xx_rhs_mag_an_m8hc [Indent level: 2],
        "_xx_rhs_mag_an_m8hc": {
            "magazine": "rhs_mag_an_m8hc",
            "count": 10
        }
    },
    # Class: CfgVehicles|RHS_M2A2_Base|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|RHS_M2A2_Base|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 2
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles|RHS_M2A2_Base|TransportWeapons [Indent level: 1],
    "transportweapons": {
        # Class: CfgVehicles|RHS_M2A2_Base|TransportWeapons|_xx_rhs_weap_m4_carryhandle_pmag [Indent level: 2]
        "_xx_rhs_weap_m4_carryhandle_pmag": {
            "weapon": "rhs_weap_m4_carryhandle_pmag",
            "count": 4
        },
        # Class: CfgVehicles|RHS_M2A2_Base|TransportWeapons|_xx_rhs_weap_fgm148 [Indent level: 2],
        "_xx_rhs_weap_fgm148": {
            "weapon": "rhs_weap_fgm148",
            "count": 2
        }
    },
    # Class: CfgVehicles|RHS_M2A2_Base|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|RHS_M2A2_Base|EventHandlers|RHSUSF_EventHandlers [Indent level: 2]
        "rhsusf_eventhandlers": {
            "hitpart": "_this call rhsusf_fnc_hitSpall",
            "getin": "_this call rhs_fnc_m2_doors",
            "getout": "_this call rhs_fnc_m2_doors",
            "engine": "[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay;_this call rhs_fnc_engineCheckDamage"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');"
    },
    # Class: CfgVehicles|RHS_M2A2_Base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|RHS_M2A2_Base|Reflectors|Left [Indent level: 2]
        "left": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "l svetlo",
            "direction": "konec l svetla",
            "hitpointclass": "Hit_LightL",
            "selection": "L svetlo",
            "size": 1,
            "innerangle": 30,
            "outerangle": 100,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|RHS_M2A2_Base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Reflectors|Right [Indent level: 2],
        "right": {
            "position": "p svetlo",
            "direction": "konec p svetla",
            "hitpointclass": "Hit_LightR",
            "selection": "P svetlo",
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "size": 1,
            "innerangle": 30,
            "outerangle": 100,
            "conefadecoef": 10,
            "intensity": 1,
            "useflare": 1,
            "daylight": 0,
            "flaresize": 1,
            # Class: CfgVehicles|RHS_M2A2_Base|Reflectors|Left|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.25,
                "hardlimitstart": 30,
                "hardlimitend": 60
            }
        }
    },
    "aggregatereflectors": [["Left"],["Right"]],
    "armorlights": 0.1,
    # Class: CfgVehicles|RHS_M2A2_Base|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|RHS_M2A2_Base|UserActions|OpenCargoDoor [Indent level: 2]
        "opencargodoor": {
            "displayname": "Open ramp",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "this doorPhase 'ramp' == 0 and {(call rhsusf_fnc_findPlayer) in this};",
            "statement": "this animateDoor ['ramp', 1];this setVariable ['ramp_handler',1,true]",
            "onlyforplayer": 1,
            "shortcut": "user12"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|UserActions|CloseCargoDoor [Indent level: 2],
        "closecargodoor": {
            "displayname": "Close ramp",
            "condition": "this doorPhase 'ramp' > 0 and {(call rhsusf_fnc_findPlayer) in this};",
            "statement": "this animateDoor ['ramp', 0];this setVariable ['ramp_handler',0,true]",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "onlyforplayer": 1,
            "shortcut": "user12"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|UserActions|ToggleLight [Indent level: 2],
        "togglelight": {
            "displayname": "Toggle interior light",
            "position": "pos driver",
            "radius": 15,
            "showwindow": 0,
            "condition": "player in this;",
            "statement": "[this,'cargolights_hide',[0,0]] call rhs_fnc_toggleIntLight",
            "onlyforplayer": 1
        }
    },
    # Class: CfgVehicles|RHS_M2A2_Base|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|RHS_M2A2_Base|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Attributes|rhs_hideIFFPanel [Indent level: 2],
        "rhs_hideiffpanel": {
            "displayname": "Hide IFF Panel",
            "property": "rhs_hideIFFPanel",
            "control": "CheckboxNumber",
            "expression": "_this animate ['IFF_Panels_Hide',_value,true]",
            "defaultvalue": "0"
        },
        # Class: CfgVehicles|RHS_M2A2_Base|Attributes|OpenRamp [Indent level: 2],
        "openramp": {
            "control": "CheckboxNumber",
            "defaultvalue": "0",
            "displayname": "Open rear ramp",
            "property": "OpenRamp",
            "expression": "_this animateDoor ['ramp', _value,true];_this setVariable ['ramp_handler',_value,true]"
        }
    },
    "attenuationeffecttype": "TankAttenuation",
    "soundturnin": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnout": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnininternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "soundturnoutinternal": ["A3|Sounds_F|vehicles|noises|Turn_in_out",1.77828,1,20],
    "bushcrash1": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_01",0.630957,1,100],
    "bushcrash2": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_02",0.630957,1,100],
    "bushcrash3": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_Collision_Light_Bush_03",0.630957,1,100],
    "soundbushcrash": ["BushCrash1",0.33,"BushCrash2",0.33,"BushCrash3",0.33],
    "buildcrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "buildcrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "armorcrash4": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_05",3.16228,1,200],
    "armorcrash5": ["A3|Sounds_F|vehicles2|armor|shared|collisions|Vehicle_Armor_General_Collision_06",3.16228,1,200],
    "_generalmacro": "APC_Tracked_03_base_F",
    "features": "Randomization: No						<br />Camo selections: 2 - turret, hull						<br />Script door sources: None						<br />Script animations: HideTurret						<br />Executed scripts: None						<br />Firing from vehicles: No						<br />Slingload: No						<br />Cargo proxy indexes: 1 to 7",
    "dampingratefullthrottle": 0.3,
    "dampingratezerothrottleclutchengaged": 3,
    "dampingratezerothrottleclutchdisengaged": 0.25,
    "antirollbarforcecoef": 15,
    "antirollbarforcelimit": 12,
    "antirollbarspeedmin": 30,
    "antirollbarspeedmax": 55,
    # Class: CfgVehicles|APC_Tracked_03_base_F|MFD [Indent level: 1],
    "mfd": {
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading [Indent level: 2]
        "mfd_driver_heading": {
            "topleft": "MFD_1_TL",
            "topright": "MFD_1_TR",
            "bottomleft": "MFD_1_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading|Draw|Driver_Heading [Indent level: 4],
                "driver_heading": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1,0],1],
                    "down": [[0.5,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading_text [Indent level: 2],
        "mfd_driver_heading_text": {
            "topleft": "MFD_Driver_1_TL",
            "topright": "MFD_Driver_1_TR",
            "bottomleft": "MFD_Driver_1_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading_text|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading_text|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading_text|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading_text|Draw|Driver_Heading [Indent level: 4],
                "driver_heading": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.45,0.02],1],
                    "right": [[0.7,0.02],1],
                    "down": [[0.45,0.87],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading_second [Indent level: 2],
        "mfd_driver_heading_second": {
            "topleft": "MFD_Driver_2_TL",
            "topright": "MFD_Driver_2_TR",
            "bottomleft": "MFD_Driver_2_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "RobotoCondensedLight",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading_second|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading_second|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading_second|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Driver_Heading_second|Draw|Driver_Heading [Indent level: 4],
                "driver_heading": {
                    "type": "text",
                    "source": "heading",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.45,0],1],
                    "right": [[0.95,0],1],
                    "down": [[0.45,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_Damage [Indent level: 2],
        "mfd_commander_display_damage": {
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "bottomleft": "mfd_com_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0,0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_Damage|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_Damage|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_Damage|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Hull [Indent level: 4],
                "damage_hull": {
                    "type": "text",
                    "source": "static",
                    "text": "HULL",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.04,0.18],1],
                    "right": [[0.065,0.18],1],
                    "down": [[0.04,0.44],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Engine [Indent level: 4],
                "damage_engine": {
                    "type": "text",
                    "source": "static",
                    "text": "ENG",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.11,0.18],1],
                    "right": [[0.135,0.18],1],
                    "down": [[0.11,0.44],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Fuel [Indent level: 4],
                "damage_fuel": {
                    "type": "text",
                    "source": "static",
                    "text": "FUEL",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.178,0.18],1],
                    "right": [[0.203,0.18],1],
                    "down": [[0.178,0.44],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Wheels [Indent level: 4],
                "damage_wheels": {
                    "type": "text",
                    "source": "static",
                    "text": "TRK",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.04,0.55],1],
                    "right": [[0.065,0.55],1],
                    "down": [[0.04,0.81],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Gun [Indent level: 4],
                "damage_gun": {
                    "type": "text",
                    "source": "static",
                    "text": "GUN",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.11,0.55],1],
                    "right": [[0.135,0.55],1],
                    "down": [[0.11,0.81],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_Damage|Draw|Damage_Turret [Indent level: 4],
                "damage_turret": {
                    "type": "text",
                    "source": "static",
                    "text": "TRT",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.178,0.55],1],
                    "right": [[0.203,0.55],1],
                    "down": [[0.178,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display [Indent level: 2],
        "mfd_commander_display": {
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "bottomleft": "mfd_com_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Bones [Indent level: 3],
            "bones": {
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Bones|FuelScale [Indent level: 4]
                "fuelscale": {
                    "type": "linear",
                    "source": "fuel",
                    "sourceindex": 1,
                    "sourcescale": 1,
                    "min": 0,
                    "max": 1,
                    "minpos": [0,0],
                    "maxpos": [-0.09,0]
                }
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Main_Gun [Indent level: 4],
                "main_gun": {
                    "type": "text",
                    "source": "static",
                    "text": "MAIN GUN",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.273,0.18],1],
                    "right": [[0.298,0.18],1],
                    "down": [[0.273,0.44],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Main_Gun_Ammo_count [Indent level: 4],
                "main_gun_ammo_count": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 0,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.273,0.55],1],
                    "right": [[0.298,0.55],1],
                    "down": [[0.273,0.81],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Main_Gun_Ammo_Type_text [Indent level: 4],
                "main_gun_ammo_type_text": {
                    "type": "text",
                    "source": "static",
                    "text": "TYPE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.385,0.18],1],
                    "right": [[0.41,0.18],1],
                    "down": [[0.385,0.44],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Main_Gun_Ammo_Type [Indent level: 4],
                "main_gun_ammo_type": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.385,0.55],1],
                    "right": [[0.41,0.55],1],
                    "down": [[0.385,0.81],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Coax [Indent level: 4],
                "coax": {
                    "type": "text",
                    "source": "static",
                    "text": "COAX",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.498,0.18],1],
                    "right": [[0.523,0.18],1],
                    "down": [[0.498,0.44],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Coax_Ammo_count [Indent level: 4],
                "coax_ammo_count": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 1,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.493,0.55],1],
                    "right": [[0.518,0.55],1],
                    "down": [[0.493,0.81],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Azimuth [Indent level: 4],
                "azimuth": {
                    "type": "text",
                    "source": "static",
                    "text": "GUN AZIM",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.605,0.18],1],
                    "right": [[0.63,0.18],1],
                    "down": [[0.605,0.44],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Azimuth_number [Indent level: 4],
                "azimuth_number": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.61,0.55],1],
                    "right": [[0.635,0.55],1],
                    "down": [[0.61,0.81],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Smoke [Indent level: 4],
                "smoke": {
                    "type": "text",
                    "source": "static",
                    "text": "SMOKE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.717,0.18],1],
                    "right": [[0.742,0.18],1],
                    "down": [[0.717,0.44],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_white [Indent level: 4],
                "fuel_background_white": {
                    "color": [0.2,0.2,0.2],
                    "alpha": 0.1,
                    "condition": "1",
                    # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_white|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],[[0.877,0.7],1],[[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_green [Indent level: 4],
                "fuel_background_green": {
                    "color": [0,0.7,0],
                    "condition": "fuel>=0.5",
                    # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_green|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],["FuelScale",[0.877,0.7],1],["FuelScale",[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_yellow [Indent level: 4],
                "fuel_background_yellow": {
                    "color": [0.9,0.7,0],
                    "condition": "fuel<0.5",
                    # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_yellow|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],["FuelScale",[0.877,0.7],1],["FuelScale",[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_red [Indent level: 4],
                "fuel_background_red": {
                    "color": [0.7,0,0],
                    "condition": "fuel<0.3",
                    # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel_background_red|Background [Indent level: 5],
                    "background": {
                        "type": "polygon",
                        "points": [[[[0.787,0.7],1],["FuelScale",[0.877,0.7],1],["FuelScale",[0.877,0.9],1],[[0.787,0.9],1]]]
                    }
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel [Indent level: 4],
                "fuel": {
                    "type": "text",
                    "source": "static",
                    "text": "FUEL",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.83,0.18],1],
                    "right": [[0.855,0.18],1],
                    "down": [[0.83,0.44],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel_number [Indent level: 4],
                "fuel_number": {
                    "type": "text",
                    "source": "fuel",
                    "sourcescale": 100,
                    "sourcelength": 1,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.835,0.4],1],
                    "right": [[0.86,0.4],1],
                    "down": [[0.835,0.66],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display|Draw|Fuel_percent_sign [Indent level: 4],
                "fuel_percent_sign": {
                    "type": "text",
                    "source": "static",
                    "text": "%",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.845,0.4],1],
                    "right": [[0.87,0.4],1],
                    "down": [[0.845,0.66],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_OnScreen [Indent level: 2],
        "mfd_commander_onscreen": {
            "topleft": "PIP_COM_TL",
            "topright": "PIP_COM_TR",
            "bottomleft": "PIP_COM_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0,0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_OnScreen|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_OnScreen|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_OnScreen|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_OnScreen|Draw|Azimuth_number [Indent level: 4],
                "azimuth_number": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.22,0.435],1],
                    "right": [[0.245,0.435],1],
                    "down": [[0.22,0.472],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_OnScreen|Draw|Elevation_Text [Indent level: 4],
                "elevation_text": {
                    "type": "text",
                    "source": "static",
                    "text": "E: ",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.2,0.28],1],
                    "right": [[0.225,0.28],1],
                    "down": [[0.2,0.317],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_OnScreen|Draw|Elevation_Number [Indent level: 4],
                "elevation_number": {
                    "type": "text",
                    "source": "[y]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "sourceprecision": 1,
                    "refreshrate": 0,
                    "align": "center",
                    "scale": 1,
                    "pos": [[0.23,0.28],1],
                    "right": [[0.255,0.28],1],
                    "down": [[0.23,0.317],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_OnScreen|Draw|Lased_Range [Indent level: 4],
                "lased_range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.75,0.28],1],
                    "right": [[0.775,0.28],1],
                    "down": [[0.75,0.317],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_OnScreen|Draw|VisionMode_Text [Indent level: 4],
                "visionmode_text": {
                    "type": "text",
                    "source": "static",
                    "text": "WFOV",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.75,0.65],1],
                    "right": [[0.775,0.65],1],
                    "down": [[0.75,0.687],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_OnScreen|Draw|VisionMode_String [Indent level: 4],
                "visionmode_string": {
                    "type": "text",
                    "source": "visionMode",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.825,0.65],1],
                    "right": [[0.85,0.65],1],
                    "down": [[0.825,0.687],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_MainTurret [Indent level: 2],
        "mfd_commander_display_mainturret": {
            "topleft": "mfd_com_TL",
            "topright": "mfd_com_TR",
            "bottomleft": "mfd_com_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0,0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_MainTurret|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_MainTurret|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_MainTurret|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Display_MainTurret|Draw|Smoke_ammo [Indent level: 4],
                "smoke_ammo": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "sourceindex": 0,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.72,0.55],1],
                    "right": [[0.745,0.55],1],
                    "down": [[0.72,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Heading [Indent level: 2],
        "mfd_commander_heading": {
            "topleft": "mfd_com_dir_TL",
            "topright": "mfd_com_dir_TR",
            "bottomleft": "mfd_com_dir_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0,0],
            "font": "LCD14",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Heading|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Heading|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Heading|Draw [Indent level: 3],
            "draw": {
                "color": [0.61,0.62,0],
                "alpha": 1,
                "condition": "on",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Commander_Heading|Draw|Driver_Heading [Indent level: 4],
                "driver_heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[1,0],1],
                    "down": [[0.5,0.81],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Ready_To_Fire [Indent level: 2],
        "mfd_gunner_ready_to_fire": {
            "topleft": "mfd_gun_cli_TL",
            "topright": "mfd_gun_cli_TR",
            "bottomleft": "mfd_gun_cli_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0,0,0],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Ready_To_Fire|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Ready_To_Fire|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw [Indent level: 3],
            "draw": {
                "color": [0,0,0],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw|Top_text [Indent level: 4],
                "top_text": {
                    "type": "text",
                    "source": "static",
                    "text": "READY TO",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.45,0.05],1],
                    "right": [[0.67,0.05],1],
                    "down": [[0.45,0.55],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Ready_To_Fire|Draw|Bottom_text [Indent level: 4],
                "bottom_text": {
                    "type": "text",
                    "source": "static",
                    "text": "FIRE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.465,0.45],1],
                    "right": [[0.685,0.45],1],
                    "down": [[0.465,0.95],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display [Indent level: 2],
        "mfd_gunner_display": {
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "bottomleft": "mfd_gun_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|Draw|Main_armament [Indent level: 4],
                "main_armament": {
                    "type": "text",
                    "source": "static",
                    "text": "MAIN ARMAMENT",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,-0.003],1],
                    "right": [[0.075,-0.003],1],
                    "down": [[0.015,0.075],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|Draw|Machinegun [Indent level: 4],
                "machinegun": {
                    "type": "text",
                    "source": "static",
                    "text": "COAX",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.31],1],
                    "right": [[0.075,0.31],1],
                    "down": [[0.015,0.388],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|Draw|Main_armament_ammo_type [Indent level: 4],
                "main_armament_ammo_type": {
                    "type": "text",
                    "source": "static",
                    "text": "AMMO TYPE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.545,-0.003],1],
                    "right": [[0.605,-0.003],1],
                    "down": [[0.545,0.075],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|Draw|Lased_distance_elevation [Indent level: 4],
                "lased_distance_elevation": {
                    "type": "text",
                    "source": "static",
                    "text": "LASED DST",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.84],1],
                    "right": [[0.075,0.84],1],
                    "down": [[0.015,0.918],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|Draw|Azimut [Indent level: 4],
                "azimut": {
                    "type": "text",
                    "source": "static",
                    "text": "AZIMUTH",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.025,0.915],1],
                    "right": [[0.085,0.915],1],
                    "down": [[0.025,0.993],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|Draw|Damage [Indent level: 4],
                "damage": {
                    "type": "text",
                    "source": "static",
                    "text": "DAMAGE",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.39],1],
                    "right": [[0.075,0.39],1],
                    "down": [[0.015,0.468],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|Draw|Heading [Indent level: 4],
                "heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 0.2,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.34,0.915],1],
                    "right": [[0.4,0.915],1],
                    "down": [[0.34,0.993],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Display|Draw|Lased_Range [Indent level: 4],
                "lased_range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.335,0.84],1],
                    "right": [[0.395,0.84],1],
                    "down": [[0.335,0.918],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type [Indent level: 2],
        "mfd_gunner_main_armament_ammo_type": {
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "bottomleft": "mfd_gun_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableparallax": 0,
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Main_Armament_Ammo_Type|Draw|Gunner_AmmoType [Indent level: 4],
                "gunner_ammotype": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.56,0.09],1],
                    "right": [[0.62,0.09],1],
                    "down": [[0.56,0.168],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Coax_Ammo [Indent level: 2],
        "mfd_gunner_coax_ammo": {
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "bottomleft": "mfd_gun_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "EtelkaMonospaceProBold",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Coax_Ammo|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Coax_Ammo|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Coax_Ammo|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Coax_Ammo|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "sourceindex": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.36,0.31],1],
                    "right": [[0.42,0.31],1],
                    "down": [[0.36,0.388],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament [Indent level: 2],
        "mfd_gunner_ammoindicator_main_armament": {
            "topleft": "mfd_gun_TL",
            "topright": "mfd_gun_TR",
            "bottomleft": "mfd_gun_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "EtelkaMonospacePro",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|material [Indent level: 3],
            "material": {
                "ambient": [1,1,1,1],
                "diffuse": [1,1,1,1],
                "emissive": [1000,1000,1000,1]
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_1 [Indent level: 4],
                "main_armament_ammo_type_1": {
                    "type": "text",
                    "source": "static",
                    "text": "MP-T",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.065],1],
                    "right": [[0.075,0.065],1],
                    "down": [[0.015,0.143],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_1 [Indent level: 4],
                "gunner_text_1": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 0,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.375,0.065],1],
                    "right": [[0.435,0.065],1],
                    "down": [[0.375,0.143],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Main_Armament_Ammo_Type_2 [Indent level: 4],
                "main_armament_ammo_type_2": {
                    "type": "text",
                    "source": "static",
                    "text": "APFSDS-T",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "right",
                    "refreshrate": 0.1,
                    "pos": [[0.015,0.125],1],
                    "right": [[0.06,0.125],1],
                    "down": [[0.015,0.203],1]
                },
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoIndicator_Main_Armament|Draw|Gunner_Text_2 [Indent level: 4],
                "gunner_text_2": {
                    "type": "text",
                    "source": "ammo",
                    "sourcescale": 1,
                    "sourcelength": 2,
                    "sourceindex": 0,
                    "sourceprecision": 1,
                    "scale": 1,
                    "align": "left",
                    "refreshrate": 0.1,
                    "pos": [[0.375,0.125],1],
                    "right": [[0.435,0.125],1],
                    "down": [[0.375,0.203],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Range [Indent level: 2],
        "mfd_gunner_range": {
            "topleft": "MFD_5_TL",
            "topright": "MFD_5_TR",
            "bottomleft": "MFD_5_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "enableparallax": 0,
            "turret": [0],
            "font": "LCD14",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Range|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Range|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Range|Draw|Gunner_Range [Indent level: 4],
                "gunner_range": {
                    "type": "text",
                    "source": "laserDist",
                    "sourcescale": 1,
                    "sourcelength": 4,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.48,-0.1],1],
                    "right": [[0.88,-0.1],1],
                    "down": [[0.48,1],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoType [Indent level: 2],
        "mfd_gunner_ammotype": {
            "topleft": "MFD_4_TL",
            "topright": "MFD_4_TR",
            "bottomleft": "MFD_4_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [0.84,0.86,0.84],
            "alpha": 0.5,
            "turret": [0],
            "enableparallax": 0,
            "font": "LCD14",
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoType|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoType|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_AmmoType|Draw|Gunner_AmmoType [Indent level: 4],
                "gunner_ammotype": {
                    "type": "text",
                    "source": "ammoFormat",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.455,0.2],1],
                    "right": [[0.655,0.2],1],
                    "down": [[0.455,0.7],1]
                }
            }
        },
        # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Heading [Indent level: 2],
        "mfd_gunner_heading": {
            "topleft": "MFD_Gunner_heading_TL",
            "topright": "MFD_Gunner_heading_TR",
            "bottomleft": "MFD_Gunner_heading_BL",
            "borderleft": 0,
            "borderright": 0,
            "bordertop": 0,
            "borderbottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableparallax": 0,
            "font": "LCD14",
            "turret": [0],
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Heading|Bones [Indent level: 3],
            "bones": {
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Heading|Draw [Indent level: 3],
            "draw": {
                "color": [1,1,1],
                "alpha": 1,
                "condition": "1",
                # Class: CfgVehicles|APC_Tracked_03_base_F|MFD|MFD_Gunner_Heading|Draw|Heading [Indent level: 4],
                "heading": {
                    "type": "text",
                    "source": "[x]turretworld",
                    "sourcescale": 1,
                    "sourcelength": 3,
                    "scale": 1,
                    "align": "center",
                    "refreshrate": 0.1,
                    "pos": [[0.5,0],1],
                    "right": [[0.7,0],1],
                    "down": [[0.5,0.9],1]
                }
            }
        }
    },
    "hideweaponsdriver": 1,
    "hideweaponscargo": 1,
    "wheelcircumference": 1.95,
    "viewdrivershadowamb": 0.5,
    "viewdrivershadowdiff": 0.05,
    "driverleftleganimname": "pedal_brake",
    "driverrightleganimname": "pedal_thrust",
    "driverinfopanelcamerapos": "driverview_old",
    "extcameraposition": [0,3,-10],
    "crewexplosionprotection": 0.9995,
    "crewvulnerable": 1,
    "memorypointtaskmarker": "TaskMarker_1_pos",
    "animationsourcehatch": "",
    "selectionfireanim": "",
    "cost": 1e+006,
    # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights [Indent level: 1],
    "compartmentslights": {
        # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1 [Indent level: 2]
        "comp1": {
            # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light1 [Indent level: 3]
            "light1": {
                "color": [25,22,16],
                "ambient": [0,0,0],
                "intensity": 0.3,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                },
                "point": "light_interior1"
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light2 [Indent level: 3],
            "light2": {
                "point": "light_interior2",
                "color": [25,22,16],
                "ambient": [0,0,0],
                "intensity": 0.6,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light3 [Indent level: 3],
            "light3": {
                "point": "light_interior3",
                "color": [25,22,16],
                "ambient": [0,0,0],
                "intensity": 0.6,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light4 [Indent level: 3],
            "light4": {
                "point": "light_interior4",
                "color": [25,25,25],
                "ambient": [0,0,0],
                "intensity": 5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light5 [Indent level: 3],
            "light5": {
                "point": "light_interior5",
                "color": [25,25,25],
                "ambient": [0,0,0],
                "intensity": 5,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            },
            # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light6 [Indent level: 3],
            "light6": {
                "point": "light_interior6",
                "color": [25,25,25],
                "ambient": [0,0,0],
                "intensity": 10,
                "size": 0,
                "useflare": 0,
                "flaresize": 0,
                "flaremaxdistance": 0,
                "daylight": 0,
                "blinking": 0,
                # Class: CfgVehicles|APC_Tracked_03_base_F|compartmentsLights|Comp1|Light1|Attenuation [Indent level: 4],
                "attenuation": {
                    "start": 0,
                    "constant": 0,
                    "linear": 1,
                    "quadratic": 70,
                    "hardlimitstart": 0.15,
                    "hardlimitend": 1.15
                }
            }
        }
    },
    "soundlocked": ["|A3|Sounds_F|weapons|Rockets|locked_1",1,1],
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_2",0.316228,1],
    "smokelaunchergrenadecount": 10,
    "smokelaunchervelocity": 14,
    "smokelauncheronturret": 1,
    "smokelauncherangle": 120,
    "animationlist": ["showBags",0,"showBags2",0,"showCamonetHull",0,"showCamonetTurret",0,"showTools",0,"showSLATHull",0,"showSLATTurret",0],
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
    "drivercansee": "1 + 2 + 4 + 8 + 32",
    "gunnercansee": "1 + 2 + 4 + 8 + 32",
    "commandercansee": "1 + 2 + 4 + 8 + 32",
    "sensorposition": "gunnerView",
    "audible": 18,
    "sensitivityear": "0.0075 /3",
    "turncoef": 5,
    "steeraheadsimul": 0.3,
    "steeraheadplan": 0.4,
    "brakedistance": 5,
    "precision": 10,
    "hideproxyincombat": 1,
    "radartarget": 1,
    "radartargetsize": 1.2,
    "visualtarget": 1,
    "visualtargetsize": 1,
    "irtargetsize": 1.2,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "enableradio": 1,
    "countermeasureactivationradius": 2000,
    "memorypointcargolight": "cargo light",
    "dampersbumpcoef": 4.5,
    "mintotaldamagethreshold": 0.005,
    "crewcrashprotection": 0.25,
    "secondaryexplosion": -1,
    "fuelexplosionpower": 1,
    "transportmaxweapons": 12,
    "transportmaxmagazines": 128,
    "transportmaxbackpacks": 12,
    "maximumload": 3000,
    "supplyradius": -1,
    "memorypointsupply": "doplnovani",
    # Class: CfgVehicles|Tank_F|CamShake [Indent level: 1],
    "camshake": {
        "power": 5,
        "frequency": 20,
        "distance": 20,
        "minspeed": 5
    },
    "camshakecoef": 0,
    # Class: CfgVehicles|Tank_F|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|Tank_F|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: VehicleSystemsTemplateLeftDriver|Components [Indent level: 0]
            "components": {
                # Class: VehicleSystemsTemplateLeftDriver|Components|VehiclePrimaryGunnerDisplay [Indent level: 1]
                "vehicleprimarygunnerdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateLeftDriver|Components|VehicleCommanderDisplay [Indent level: 1],
                "vehiclecommanderdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|EmptyDisplay [Indent level: 1],
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MinimapDisplay [Indent level: 1],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|MineDetectorDisplay [Indent level: 1],
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|CrewDisplay [Indent level: 1],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|UAVDisplay [Indent level: 1],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerLeft|Components|SlingLoadDisplay [Indent level: 1],
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "left": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_X`,	(safezoneX + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFOLEFT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Tank_F|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            # Class: VehicleSystemsTemplateRightDriver|Components [Indent level: 0]
            "components": {
                # Class: VehicleSystemsTemplateRightDriver|Components|VehiclePrimaryGunnerDisplay [Indent level: 1]
                "vehicleprimarygunnerdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "PrimaryGunner"
                },
                # Class: VehicleSystemsTemplateRightDriver|Components|VehicleCommanderDisplay [Indent level: 1],
                "vehiclecommanderdisplay": {
                    "componenttype": "TransportFeedDisplayComponent",
                    "source": "Commander"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|EmptyDisplay [Indent level: 1],
                "emptydisplay": {
                    "componenttype": "EmptyDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MinimapDisplay [Indent level: 1],
                "minimapdisplay": {
                    "componenttype": "MinimapDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|MineDetectorDisplay [Indent level: 1],
                "minedetectordisplay": {
                    "componenttype": "MineDetectorDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|CrewDisplay [Indent level: 1],
                "crewdisplay": {
                    "componenttype": "CrewDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|UAVDisplay [Indent level: 1],
                "uavdisplay": {
                    "componenttype": "UAVFeedDisplayComponent"
                },
                # Class: DefaultVehicleSystemsDisplayManagerRight|Components|SlingLoadDisplay [Indent level: 1],
                "slingloaddisplay": {
                    "componenttype": "SlingLoadDisplayComponent"
                }
            },
            "componenttype": "VehicleSystemsDisplayManager",
            "right": 1,
            "defaultdisplay": "EmptyDisplay",
            "x": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_X`,	((safezoneX + safezoneW) - (		(10 * 			(			((safezoneW / safezoneH) min 1.2) / 40)) + 0.5 * 			(			((safezoneW / safezoneH) min 1.2) / 40)))])",
            "y": "(profilenamespace getvariable [`IGUI_GRID_CUSTOMINFORIGHT_Y`,	(safezoneY + safezoneH - 21 * 			(			(			((safezoneW / safezoneH) min 1.2) / 1.2) / 25))])"
        },
        # Class: CfgVehicles|Tank_F|Components|AITankSteeringComponent [Indent level: 2],
        "aitanksteeringcomponent": {
            "steeringpidweights": [2.9,0.1,0.2],
            "speedpidweights": [0.7,0.2,0],
            "doremapspeed": 0,
            "remapspeedrange": [30,70],
            "remapspeedscalar": [1,0.35],
            "dopredictforward": 1,
            "predictforwardrange": [1,20],
            "steeraheadsaturation": [0.01,0.4],
            "speedpredictionmethod": 3,
            "wheelanglecoef": 0.7,
            "forwardanglecoef": 0.7,
            "steeringanglecoef": 1,
            "differenceanglecoef": 1,
            "stuckmaxtime": 3,
            "allowovertaking": 1,
            "allowcollisionavoidance": 1,
            "allowdrifting": 0,
            "maxwheelanglediff": 0.2616,
            "minspeedtokeep": 0.01,
            "commandturnfactor": 2,
            "allowturnaroundinpoint": 1,
            "convoypidweights": [1,0,0],
            "predictforwardmaxspeed": 15
        },
        # Class: CfgVehicles|LandVehicle|Components|TransportCountermeasuresComponent [Indent level: 2],
        "transportcountermeasurescomponent": {
        }
    },
    # Class: CfgVehicles|Tank_F|NVGMarkers [Indent level: 1],
    "nvgmarkers": {
        # Class: CfgVehicles|Tank_F|NVGMarkers|NVGMarker01 [Indent level: 2]
        "nvgmarker01": {
            "name": "nvg_marker",
            "color": [0.03,0.003,0.003,1],
            "ambient": [0.003,0.0003,0.0003,1],
            "brightness": 0.001,
            "blinking": 1
        }
    },
    "memorypointdriveroptics": "driverview",
    "enginestartspeed": 5,
    "explosioneffect": "FuelExplosionBig",
    "htmin": 60,
    "htmax": 1800,
    "afmax": 100,
    "mfmax": 80,
    "mfact": 1,
    "tbody": 250,
    "numberphysicalwheels": 16,
    "getinradius": 3.5,
    "hulldamagecauseexplosion": 1,
    "bounding": "usti hlavne",
    "firedusteffect": "FDustEffects",
    "gearbox": [-7,0,11,8,5.7,4.2],
    "alphatracks": 0.7,
    "texturetrackwheel": 0,
    "memorypointtrack1l": "Stopa LL",
    "memorypointtrack1r": "Stopa LR",
    "memorypointtrack2l": "Stopa RL",
    "memorypointtrack2r": "Stopa RR",
    "predictturnsimul": 1.2,
    "predictturnplan": 1,
    "soundgear": ["",0.000316228,1],
    "outsidesoundfilter": 1,
    "nightvision": 0,
    "formationx": 20,
    "formationz": 30,
    "canfloat": 0,
    "type": 1,
    "camouflage": 8,
    "driveropticscolor": [1,1,1,1],
    # Class: CfgVehicles|Tank|CargoLight [Indent level: 1],
    "cargolight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
    "enablegps": 1,
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffectsBig"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffectsBig"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffectsBig"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffectsBig"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffectsBig"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffectsBig"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassEffectsDryBig"],["GdtStratisDryGrass","RDirtEffectsBig"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffectsBig"],["GdtStratisGreenGrass","RDirtEffectsBig"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffectsBig"],["GdtStratisRocky","RDirtEffectsBig"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffectsBig"],["GdtStratisThistles","RDirtEffectsBig"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffectsBig"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffectsBig"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffectsBig"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffectsBig"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffectsBig"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffectsBig"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffectsBig"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RDirtEffectsBig"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RDirtEffectsBig"],["GdtDesert1","RStonesEffectsBig"],["GdtDesert2","RDustEffects"],["GdtDesert2","RGrassEffectsBig"],["GdtDesert2","RDirtEffectsBig"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffectsBig"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffectsBig"],["GdtGrassGreen","RDirtEffectsBig"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassEffectsDryBig"],["GdtGrassDry","RDirtEffectsBig"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffectsBig"],["GdtGrassWild","RDirtEffectsBig"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffectsBig"],["GdtWildField","RDirtEffectsBig"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffectsBig"],["GdtWeed1","RDirtEffectsBig"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffectsBig"],["GdtWeed2","RDirtEffectsBig"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffectsBig"],["GdtThorn","RDirtEffectsBig"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffectsBig"],["GdtStony","RDirtEffectsBig"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffectsBig"],["GdtStonyGreen","RDirtEffectsBig"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffectsBig"],["GdtStonyThistle","RDirtEffectsBig"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffectsBig"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffectsBig"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffectsBig"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffectsBig"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffectsBig"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffectsBig"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassEffectsDryBig"],["GdtStratisDryGrass","LDirtEffectsBig"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffectsBig"],["GdtStratisGreenGrass","LDirtEffectsBig"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffectsBig"],["GdtStratisRocky","LDirtEffectsBig"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffectsBig"],["GdtStratisThistles","LDirtEffectsBig"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffectsBig"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffectsBig"],["GdtRubble","LDustEffects"],["GdtRubble","LDirtEffectsBig"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffectsBig"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffectsBig"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffectsBig"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffectsBig"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LDirtEffectsBig"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LDirtEffectsBig"],["GdtDesert1","LStonesEffectsBig"],["GdtDesert2","LDustEffects"],["GdtDesert2","LGrassEffectsBig"],["GdtDesert2","LDirtEffectsBig"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffectsBig"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffectsBig"],["GdtGrassGreen","LDirtEffectsBig"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassEffectsDryBig"],["GdtGrassDry","LDirtEffectsBig"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffectsBig"],["GdtGrassWild","LDirtEffectsBig"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffectsBig"],["GdtWildField","LDirtEffectsBig"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffectsBig"],["GdtWeed1","LDirtEffectsBig"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffectsBig"],["GdtWeed2","LDirtEffectsBig"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffectsBig"],["GdtThorn","LDirtEffectsBig"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffectsBig"],["GdtStony","LDirtEffectsBig"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffectsBig"],["GdtStonyGreen","LDirtEffectsBig"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffectsBig"],["GdtStonyThistle","LDirtEffectsBig"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","RDustEffects"]],
    # Class: CfgVehicles|Tank|DustEffects [Indent level: 1],
    "dusteffects": {
        # Class: CfgDustEffectsTank|Both [Indent level: 0]
        "both": {
        },
        # Class: CfgDustEffectsTank|Left [Indent level: 0],
        "left": {
            "default": ["LDustEffects"],
            "gdtstratisconcrete": ["LDustEffects","LDirtEffectsBig"],
            "gdtstratisbeach": ["LDustEffects","LStonesEffectsBig"],
            "gdtstratisdirt": ["LDustEffects","LDirtEffectsBig"],
            "gdtstratisseabedcluttered": ["LDustEffects"],
            "gdtstratisseabed": ["LDustEffects"],
            "gdtstratisdrygrass": ["LDustEffects","LGrassEffectsDryBig","LDirtEffectsBig"],
            "gdtstratisgreengrass": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtstratisrocky": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtstratisthistles": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtconcrete": ["LDustEffects","LDirtEffectsBig"],
            "gdtasphalt": ["LDustEffects","LDirtEffectsBig"],
            "gdtrubble": ["LDustEffects","LDirtEffectsBig"],
            "gdtsoil": ["LDustEffects","LDirtEffectsBig"],
            "gdtbeach": ["LDustEffects","LStonesEffectsBig"],
            "gdtrock": ["LDustEffects","LDirtEffectsBig"],
            "gdtdead": ["LDustEffects","LDirtEffectsBig"],
            "gdtdesert": ["LDustEffects","LDirtEffectsBig","LStonesEffects"],
            "gdtdesert1": ["LDustEffects","LDirtEffectsBig","LStonesEffectsBig"],
            "gdtdesert2": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtdirt": ["LDustEffects","LDirtEffectsBig"],
            "gdtgrassgreen": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtgrassdry": ["LDustEffects","LGrassEffectsDryBig","LDirtEffectsBig"],
            "gdtgrasswild": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtwildfield": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtweed1": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtweed2": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtthorn": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtstony": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtstonygreen": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtstonythistle": ["LDustEffects","LGrassEffectsBig","LDirtEffectsBig"],
            "gdtseabeddeep": ["LDustEffects"],
            "gdtseabed": ["LDustEffects"],
            "surfroaddirt": ["LDustEffects"],
            "surfroadconcrete": ["LDustEffects"],
            "surfroadtarmac": ["LDustEffects"],
            "surfwood": ["LDustEffects"],
            "surfmetal": ["LDustEffects"],
            "surfrooftin": ["LDustEffects"],
            "surfrooftiles": ["LDustEffects"],
            "surfintwood": ["LDustEffects"],
            "surfintconcrete": ["LDustEffects"],
            "surfinttiles": ["LDustEffects"],
            "surfintmetal": ["LDustEffects"],
            "gdtgrassshort": ["LDustEffects","LGrassEffectsBig"],
            "gdtgrasstall": ["LDustEffects","LGrassEffectsBig"],
            "gdtreddirt": ["LDustEffectsRed"],
            "gdtfield": ["LDustEffects"],
            "gdtforest": ["LDustEffects"],
            "gdtvolcano": ["LDustEffects","LStonesEffectsBig"],
            "gdtcliff": ["LDustEffects"],
            "gdtvolcanobeach": ["LDustEffects"],
            "surfroaddirt_exp": ["LDustEffectsRed"],
            "surfroadconcrete_exp": ["LDustEffects"],
            "surfroadtarmac_exp": ["LDustEffects"],
            "gdtkldirt": ["LDustEffects"],
            "gdtklgrass1": ["LDustEffects","LGrassEffects"],
            "gdtklgrass2": ["LDustEffects","LGrassEffects"],
            "gdtklforestcon": ["LDustEffects"],
            "gdtklforestdec": ["LDustEffects"],
            "gdtklmud": ["LDustEffects"],
            "gdtklsoil": ["LDustEffects"],
            "gdtkltarmac": ["LDustEffects"],
            "gdtklstubble": ["LDustEffects"],
            "gdtklstones": ["LStonesEffects"],
            "surfroaddirt_enoch": ["LDustEffects"],
            "surftraildirt_enoch": ["LDustEffects"],
            "surfroadtarmac1_enoch": ["LDustEffects"],
            "surfroadtarmac2_enoch": ["LDustEffects"],
            "surfroadtarmac3_enoch": ["LDustEffects"],
            "dirtrunway": ["LDustEffects"]
        },
        # Class: CfgDustEffectsTank|Right [Indent level: 0],
        "right": {
            "default": ["RDustEffects"],
            "gdtstratisconcrete": ["RDustEffects","RDirtEffectsBig"],
            "gdtstratisbeach": ["RDustEffects","RStonesEffectsBig"],
            "gdtstratisdirt": ["RDustEffects","RDirtEffectsBig"],
            "gdtstratisseabedcluttered": ["RDustEffects"],
            "gdtstratisseabed": ["RDustEffects"],
            "gdtstratisdrygrass": ["RDustEffects","RGrassEffectsDryBig","RDirtEffectsBig"],
            "gdtstratisgreengrass": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtstratisrocky": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtstratisthistles": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtconcrete": ["RDustEffects","RDirtEffectsBig"],
            "gdtasphalt": ["RDustEffects","RDirtEffectsBig"],
            "gdtrubble": ["RDustEffects","RDirtEffectsBig"],
            "gdtsoil": ["RDustEffects","RDirtEffectsBig"],
            "gdtbeach": ["RDustEffects","RStonesEffectsBig"],
            "gdtrock": ["RDustEffects","RDirtEffectsBig"],
            "gdtdead": ["RDustEffects","RDirtEffectsBig"],
            "gdtdesert": ["RDustEffects","RDirtEffectsBig","RStonesEffects"],
            "gdtdesert1": ["RDustEffects","RDirtEffectsBig","RStonesEffectsBig"],
            "gdtdesert2": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtdirt": ["RDustEffects","RDirtEffectsBig"],
            "gdtgrassgreen": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtgrassdry": ["RDustEffects","RGrassEffectsDryBig","RDirtEffectsBig"],
            "gdtgrasswild": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtwildfield": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtweed1": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtweed2": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtthorn": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtstony": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtstonygreen": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtstonythistle": ["RDustEffects","RGrassEffectsBig","RDirtEffectsBig"],
            "gdtseabeddeep": ["RDustEffects"],
            "gdtseabed": ["RDustEffects"],
            "surfroaddirt": ["RDustEffects"],
            "surfroadconcrete": ["RDustEffects"],
            "surfroadtarmac": ["RDustEffects"],
            "surfwood": ["RDustEffects"],
            "surfmetal": ["RDustEffects"],
            "surfrooftin": ["RDustEffects"],
            "surfrooftiles": ["RDustEffects"],
            "surfintwood": ["RDustEffects"],
            "surfintconcrete": ["RDustEffects"],
            "surfinttiles": ["RDustEffects"],
            "surfintmetal": ["RDustEffects"],
            "gdtgrassshort": ["RDustEffects","RGrassEffectsBig"],
            "gdtgrasstall": ["RDustEffects","RGrassEffectsBig"],
            "gdtreddirt": ["RDustEffectsRed"],
            "gdtfield": ["RDustEffects"],
            "gdtforest": ["RDustEffects"],
            "gdtvolcano": ["RDustEffects","RStonesEffectsBig"],
            "gdtcliff": ["RDustEffects"],
            "gdtvolcanobeach": ["RDustEffects"],
            "surfroaddirt_exp": ["RDustEffectsRed"],
            "surfroadconcrete_exp": ["RDustEffects"],
            "surfroadtarmac_exp": ["RDustEffects"],
            "gdtkldirt": ["RDustEffects"],
            "gdtklgrass1": ["RDustEffects","RGrassEffects"],
            "gdtklgrass2": ["RDustEffects","RGrassEffects"],
            "gdtklforestcon": ["RDustEffects"],
            "gdtklforestdec": ["RDustEffects"],
            "gdtklmud": ["RDustEffects"],
            "gdtklsoil": ["RDustEffects"],
            "gdtkltarmac": ["RDustEffects"],
            "gdtklstubble": ["RDustEffects"],
            "gdtklstones": ["RStonesEffects"],
            "surfroaddirt_enoch": ["RDustEffects"],
            "surftraildirt_enoch": ["RDustEffects"],
            "surfroadtarmac1_enoch": ["RDustEffects"],
            "surfroadtarmac2_enoch": ["RDustEffects"],
            "surfroadtarmac3_enoch": ["RDustEffects"],
            "dirtrunway": ["RDustEffects"]
        }
    },
    # Class: CfgVehicles|Tank|DestructionEffects [Indent level: 1],
    "destructioneffects": {
        # Class: CfgVehicles|Tank|DestructionEffects|LightBig1 [Indent level: 2]
        "lightbig1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 0.001,
            "interval": 1,
            "lifetime": 3,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles|Tank|DestructionEffects|Sound [Indent level: 2],
        "sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifetime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles|Tank|DestructionEffects|FireBig1 [Indent level: 2],
        "firebig1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Tank|DestructionEffects|Refract1 [Indent level: 2],
        "refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefract",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SmokeBig1 [Indent level: 2],
        "smokebig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SparksBig1 [Indent level: 2],
        "sparksbig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifetime": 0
        },
        # Class: CfgVehicles|Tank|DestructionEffects|FireSparksBig1 [Indent level: 2],
        "firesparksbig1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifetime": 2.8
        },
        # Class: CfgVehicles|Tank|DestructionEffects|FireBig2 [Indent level: 2],
        "firebig2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SmokeBig1_2 [Indent level: 2],
        "smokebig1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifetime": 3.5
        },
        # Class: CfgVehicles|Tank|DestructionEffects|SmokeBig2 [Indent level: 2],
        "smokebig2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifetime": 3.2
        }
    },
    "selectionbrakelights": "brzdove svetlo",
    "memorypointmissile": ["spice rakety","usti hlavne"],
    "memorypointmissiledir": ["konec rakety","konec hlavne"],
    "leftdusteffect": "LDustEffects",
    "rightdusteffect": "RDustEffects",
    "leftwatereffect": "LWaterEffects",
    "rightwatereffect": "RWaterEffects",
    "leftfastwatereffect": "LWaterEffects",
    "rightfastwatereffect": "RWaterEffects",
    "selectionleftoffset": "PasOffsetL",
    "selectionrightoffset": "PasOffsetP",
    # Class: CfgVehicles|LandVehicle|CommanderOptics [Indent level: 1],
    "commanderoptics": {
        "proxytype": "CPCommander",
        "proxyindex": 1,
        "gunnername": "Commander",
        "primarygunner": 0,
        "primaryobserver": 1,
        "stabilizedinaxes": 0,
        "body": "obsTurret",
        "gun": "obsGun",
        "animationsourcebody": "obsTurret",
        "animationsourcegun": "obsGun",
        "animationsourcehatch": "hatchCommander",
        "animationsourcecamelev": "camElev",
        "soundservo": ["A3|sounds_f|dummysound",0.01,1,10],
        "gunbeg": "",
        "gunend": "",
        "minelev": -4,
        "maxelev": 20,
        "initelev": 0,
        "minturn": -360,
        "maxturn": 360,
        "initturn": 0,
        "commanding": 2,
        "outgunnermayfire": 1,
        "ingunnermayfire": 1,
        "viewgunnerinexternal": 0,
        "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Commander_02_F",
        "gunneroutopticsmodel": "A3|weapons_f|reticle|optics_empty",
        "gunneroutopticscolor": [0,0,0,1],
        "gunneroutforceoptics": 0,
        "gunneroutopticsshowcursor": 0,
        "gunneropticseffect": [],
        "gunneroutopticseffect": [],
        "memorypointgunneroutoptics": "commander_weapon_view",
        "memorypointgunneroptics": "commanderview",
        "memorypointsgetingunner": "pos commander",
        "memorypointsgetingunnerdir": "pos commander dir",
        "gunnergetinaction": "GetInHigh",
        "gunnergetoutaction": "GetOutHigh",
        "memorypointgun": "gun_muzzle",
        "selectionfireanim": "zasleh_1",
        # Class: CfgVehicles|LandVehicle|CommanderOptics|ViewOptics [Indent level: 2],
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
        # Class: CfgVehicles|LandVehicle|CommanderOptics|ViewGunner [Indent level: 2],
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
        "gunnertype": "",
        "weapons": [],
        "magazines": [],
        "soundelevation": ["",0.00316228,1],
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
        "primary": 1,
        "hasgunner": 1,
        "turretcansee": 0,
        "canusescanners": 1,
        # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
        "turretspec": {
            "showheadphones": 0
        },
        "gunneropticscolor": [0,0,0,1],
        "gunnerforceoptics": 1,
        "gunneropticsshowcursor": 0,
        "turretinfotype": "",
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
        "showhmd": 0,
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
        "showcrewaim": 0
    },
    "wheeldamagethreshold": 0.2,
    "wheeldestroythreshold": 0.99,
    "wheeldamageradiuscoef": 0.9,
    "wheeldestroyradiuscoef": 0.4,
    "weaponsgroup1": 1,
    "weaponsgroup2": "2 + 		4",
    "weaponsgroup3": "8 + 	16 + 	32",
    "weaponsgroup4": "64 + 		128",
    # Class: CfgVehicles|AllVehicles|SquadTitles [Indent level: 1],
    "squadtitles": {
        "name": "clan_sign",
        "color": [0,0,0,0.75]
    },
    "memorypointsgetindriver": "pos driver",
    "memorypointsgetindriverdir": "pos driver dir",
    "memorypointsgetincodriver": "pos codriver",
    "memorypointsgetincodriverdir": "pos codriver dir",
    "memorypointsgetindriverprecise": "pos driver",
    "memorypointsgetincargoprecise": ["pos cargo"],
    "memorypointsleftwatereffect": "waterEffectL",
    "memorypointsrightwatereffect": "waterEffectR",
    "selectionclan": "clan",
    "selectiondashboard": "podsvit pristroju",
    "selectionshowdamage": "poskozeni",
    "selectionbacklights": "zadni svetlo",
    # Class: CfgVehicles|AllVehicles|NewTurret [Indent level: 1],
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
    "hasterminal": 0,
    "getinoutonproxy": 0,
    "precisegetinout": 0,
    "cargoprecisegetinout": [0],
    "availableforsupporttypes": [],
    "waterppinvehicle": 1,
    "impacteffectssea": "ImpactEffectsSea",
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
    "epeimpulsedamagecoef": 30,
    "gunnerhasflares": 1,
    "enablemanualfire": 1,
    "sensitivity": 2.5,
    "portrait": "",
    "ghostpreview": "",
    "replacedamaged": "",
    "replacedamagedlimit": 0.9,
    "replacedamagedhitpoints": [],
    "keepinepesceneafterdeath": 0,
    "fuelconsumptionrate": 0.01,
    "groupcameraposition": [0,5,-30],
    "extcameraparams": [1],
    "camerasmoothspeed": 5,
    "minfiretime": 20,
    "indirecthitenemycoefai": 10,
    "indirecthitfriendlycoefai": -20,
    "indirecthitciviliancoefai": -20,
    "indirecthitunknowncoefai": -0.5,
    "formationtime": 5,
    "alwaystarget": 0,
    "lasertarget": 0,
    "laserscanner": 0,
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
    "enablewatch": 0,
    "useprecisegetinaction": 0,
    "allowtablock": 1,
    "showalltargets": 0,
    "waterresistancecoef": 0.5,
    "waterlineardampingcoefx": 0,
    "waterlineardampingcoefy": 0,
    "waterangulardampingcoef": 0,
    "shownvgdriver": 0,
    "shownvgcommander": 0,
    "shownvggunner": 0,
    "shownvgcargo": [0],
    "soundattenuationcargo": [1],
    "countsforscoreboard": 1,
    # Class: CfgVehicles|All|MarkerLights [Indent level: 1],
    "markerlights": {
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
    "soundgearup": ["",1,1],
    "soundgeardown": ["",1,1],
    "soundflapsup": ["",1,1],
    "soundflapsdown": ["",1,1],
    "cabinopensound": ["",1,1],
    "cabinclosesound": ["",1,1],
    "cabinopensoundinternal": ["",1,1],
    "cabinclosesoundinternal": ["",1,1],
    "soundcrashes": ["soundCrash",1],
    "soundlandcrashes": ["soundLandCrash",1],
    "soundwatercrashes": ["soundWaterCrash",1],
    "emptysound": ["",0,1],
    "typicalcargo": [],
    "cargoiscodriver": [0],
    "drivercompartments": "Compartment1",
    "cargocompartments": ["Compartment1"],
    "driveropticseffect": [],
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
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
    # Class: CfgVehicles|All|GunFire [Indent level: 1],
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
    # Class: CfgVehicles|All|GunClouds [Indent level: 1],
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
    # Class: CfgVehicles|All|MGunClouds [Indent level: 1],
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
    "selectiondamage": "zbytek",
    "headaimdown": 0,
    "cargocaneject": 1,
    "drivercaneject": 1,
    "fireresistance": 10,
    "aircapacity": 10,
    "damagetexdelay": 0,
    "coefinside": 2,
    "coefinsideheur": 2,
    "coefspeedinside": 2,
    "windsockexist": 0,
    "slingloadcargomemorypoints": [],
    "slingloadcargomemorypointsdir": [],
    "damagehalf": [],
    "damagefull": [],
    # Class: CfgVehicles|All|camShakeGForce [Indent level: 1],
    "camshakegforce": {
        "power": 1,
        "frequency": 20,
        "distance": 0,
        "minspeed": 1,
        "duration": 3
    },
    "mingforce": 0.2,
    "maxgforce": 2,
    "gforceshakeattenuation": 0.5,
    # Class: CfgVehicles|All|camShakeDamage [Indent level: 1],
    "camshakedamage": {
        "power": 0.5,
        "frequency": 60,
        "distance": -1,
        "minspeed": 1,
        "attenuation": 0.5,
        "duration": 3
    },
    "insidedetectcoef": 0.05,
}