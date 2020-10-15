rhs_bmd4ma_vdv = {
    "editorpreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_bmd4ma_vdv.paa",
    "author": "Red Hammer Studios",
    "model": "rhsafrf|addons|rhs_bmd_34|rhs_bmd_4ma.p3d",
    "displayname": "BMD-4M (A)",
    # Class: CfgVehicles|rhs_bmd4ma_vdv|Hitpoints [Indent level: 1],
    "hitpoints": {
        # Class: CfgVehicles|rhs_bmd4ma_vdv|Hitpoints|Armor_Composite_60 [Indent level: 2]
        "armor_composite_60": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_60_Hit",
            "armorcomponent": "Armor_CE_60",
            "simulation": "RHS_Composite_60",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_bmd4ma_vdv|Hitpoints|Armor_Composite_80 [Indent level: 2],
        "armor_composite_80": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_80_Hit",
            "armorcomponent": "Armor_CE_80",
            "simulation": "RHS_Composite_80",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Hitpoints|Armor_Composite_75 [Indent level: 2],
        "armor_composite_75": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_75_Hit",
            "armorcomponent": "Armor_CE_75",
            "simulation": "RHS_Composite_75",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Hitpoints|Armor_Composite_85 [Indent level: 2],
        "armor_composite_85": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_85_Hit",
            "armorcomponent": "Armor_CE_85",
            "simulation": "RHS_Composite_85",
            "passthrough": 0,
            "minimalhit": 1,
            "explosionshielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitHull [Indent level: 2],
        "hithull": {
            "armor": 0.4,
            "material": -1,
            "name": "telo",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.54,
            "explosionshielding": 0,
            "radius": 0.15
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitEngine [Indent level: 2],
        "hitengine": {
            "armor": 0.45,
            "material": -1,
            "name": "motor",
            "visual": "zbytek",
            "passthrough": 0,
            "minimalhit": 0.139,
            "explosionshielding": 0.009,
            "radius": 0.17,
            # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitEngine|DestructionEffects [Indent level: 3],
            "destructioneffects": {
                "ammoexplosioneffect": "",
                # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke [Indent level: 4],
                "rhs_engine_smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Fire [Indent level: 4],
                "rhs_engine_fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sparks [Indent level: 4],
                "rhs_engine_sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Sounds [Indent level: 4],
                "rhs_engine_sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small1 [Indent level: 4],
                "rhs_engine_smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitEngine|DestructionEffects|RHS_Engine_Smoke_small2 [Indent level: 4],
                "rhs_engine_smoke_small2": {
                    "position": "engine_smoke3",
                    "type": "WeaponWreckSmoke",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifetime": 60
                }
            }
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitLTrack [Indent level: 2],
        "hitltrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_L",
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.15,
            "radius": 0.3,
            "visual": "pas_L"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|HitPoints|HitRTrack [Indent level: 2],
        "hitrtrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_P",
            "passthrough": 0,
            "minimalhit": -0.25,
            "explosionshielding": 0.15,
            "radius": 0.3,
            "visual": "pas_P"
        },
        # Class: CfgVehicles|Tank_F|HitPoints|HitFuel [Indent level: 2],
        "hitfuel": {
            "armor": 0.6,
            "material": -1,
            "name": "NEtelo",
            "visual": "motor",
            "passthrough": 0,
            "minimalhit": 0.1,
            "explosionshielding": 0.3
        }
    },
    "hiddenselectionstextures": ["rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_01a_co.paa","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_02a_co.paa","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4_03_co.paa","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_w_co.paa","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_a_co.paa","rhsafrf|addons|rhs_decals|Data|Labels|Misc|no_ca.paa"],
    # Class: CfgVehicles|rhs_bmd4ma_vdv|textureSources [Indent level: 1],
    "texturesources": {
        # Class: CfgVehicles|rhs_bmd4ma_vdv|textureSources|standard [Indent level: 2]
        "standard": {
            "displayname": "Standard",
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_01a_co.paa","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_02a_co.paa","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4_03_co.paa","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_w_co.paa","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_a_co.paa"],
            "factions": []
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|textureSources|r1 [Indent level: 2],
        "r1": {
            "author": "Red Hammer Studios",
            "textures": ["#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)","#(argb,8,8,3)color(0.92,0.87,0.92,1)"],
            "displayname": "#1",
            "factions": []
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|textureSources|r2 [Indent level: 2],
        "r2": {
            "author": "Red Hammer Studios",
            "textures": ["#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)","#(argb,8,8,3)color(0.07,0.98,0,1)"],
            "displayname": "#2",
            "factions": []
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|textureSources|r3 [Indent level: 2],
        "r3": {
            "author": "Red Hammer Studios",
            "textures": ["#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)","#(argb,8,8,3)color(0,0.11,0.67,1)"],
            "displayname": "#3",
            "factions": []
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|textureSources|r4 [Indent level: 2],
        "r4": {
            "author": "Red Hammer Studios",
            "textures": ["#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)","#(argb,8,8,3)color(0.99,0.27,0.25,1)"],
            "displayname": "#4",
            "factions": []
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|textureSources|r5 [Indent level: 2],
        "r5": {
            "author": "Red Hammer Studios",
            "textures": ["#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)","#(argb,8,8,3)color(00.41,0.4,0,1)"],
            "displayname": "#5",
            "factions": []
        }
    },
    "simulation": "tankX",
    "normalspeedforwardcoef": 0.85,
    "slowspeedforwardcoef": 0.5,
    "torquecurve": [[0.288462,0.45],[0.384615,0.692708],[0.461538,0.890625],[0.561538,1],[0.615385,0.942708],[0.769231,0.859375],[0.884615,0.765625],[1.11962,0]],
    "enginepower": 373,
    "peaktorque": 1920,
    "maxomega": 272.27,
    "idlerpm": 750,
    "redrpm": 2600,
    # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels [Indent level: 1],
    "wheels": {
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|L2 [Indent level: 2]
        "l2": {
            "dampingrate": 611,
            "dampingrateinair": 611,
            "susptraveldirection": [-0.125,-1,0],
            "bonename": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "side": "left",
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|L3 [Indent level: 2],
        "l3": {
            "bonename": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|L4 [Indent level: 2],
        "l4": {
            "bonename": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|L5 [Indent level: 2],
        "l5": {
            "bonename": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|L6 [Indent level: 2],
        "l6": {
            "bonename": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|L9 [Indent level: 2],
        "l9": {
            "bonename": "",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "dampingrate": 611,
            "dampingrateinair": 611,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|L1 [Indent level: 2],
        "l1": {
            "bonename": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "dampingrate": 611,
            "dampingrateinair": 611,
            "susptraveldirection": [-0.125,-1,0],
            "side": "left",
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|R2 [Indent level: 2],
        "r2": {
            "susptraveldirection": [0.125,-1,0],
            "bonename": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|R3 [Indent level: 2],
        "r3": {
            "bonename": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|R4 [Indent level: 2],
        "r4": {
            "bonename": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|R5 [Indent level: 2],
        "r5": {
            "bonename": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|R6 [Indent level: 2],
        "r6": {
            "bonename": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxdroop": 0.18,
            "maxcompression": 0.18,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|R9 [Indent level: 2],
        "r9": {
            "bonename": "",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Wheels|R1 [Indent level: 2],
        "r1": {
            "bonename": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxdroop": 0,
            "maxcompression": 0,
            "susptraveldirection": [0.125,-1,0],
            "side": "right",
            "dampingrate": 611,
            "dampingrateinair": 611,
            "width": 0.32,
            "steering": 0,
            "mass": 100,
            "moi": 5.5112,
            "maxbraketorque": 1500,
            "sprungmass": 1380,
            "springstrength": 235400,
            "springdamperrate": 8500,
            "dampingratedamaged": 10,
            "dampingratedestroyed": 10000,
            "latstiffx": 3,
            "latstiffy": 40,
            "longitudinalstiffnessperunitgravity": 42000,
            "frictionvsslipgraph": [[0,0.45],[0.18,1],[0.7,0.9]]
        }
    },
    "picture": "rhsafrf|addons|rhs_bmd_34|data|pictures|rhs_bmd4m_pic_ca.paa",
    # Class: CfgVehicles|rhs_bmd4m_vdv|Turrets [Indent level: 1],
    "turrets": {
        # Class: CfgVehicles|rhs_bmd4m_vdv|Turrets|MainTurret [Indent level: 2]
        "mainturret": {
            # Class: CfgVehicles|rhs_bmd4m_vdv|Turrets|MainTurret|Turrets [Indent level: 3]
            "turrets": {
                # Class: CfgVehicles|rhs_bmd4m_vdv|Turrets|MainTurret|Turrets|CommanderOptics [Indent level: 4]
                "commanderoptics": {
                    "body": "obsTurret",
                    "gun": "obsGun",
                    "gunnerdoor": "hatchC",
                    "animationsourcebody": "obsTurret",
                    "animationsourcegun": "obsGun",
                    "commanding": 5,
                    "primaryobserver": 0,
                    "maxhorizontalrotspeed": 1.8,
                    "maxverticalrotspeed": 1.8,
                    "stabilizedinaxes": 3,
                    "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_best",0.316228,1,50],
                    "minelev": -5,
                    "maxelev": 60,
                    "initelev": 0,
                    "minturn": -360,
                    "maxturn": 360,
                    "initturn": 0,
                    "memorypointgun": "usti hlavne3",
                    "gunbeg": "usti hlavne3",
                    "gunend": "konec hlavne3",
                    "weapons": [],
                    "magazines": [],
                    "turretinfotype": "RHS_RscWeaponESSA_commander_FCS",
                    "discretedistance": [],
                    "discretedistanceinitindex": 0,
                    "memorypointgunneroutoptics": "commanderview",
                    "memorypointgunneroptics": "commanderview",
                    "gunneropticsmodel": "A3|weapons_f|reticle|Optics_Commander_02_F",
                    "gunneroutopticsmodel": "",
                    "gunneropticseffect": [],
                    "gunnerhasflares": 1,
                    # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|ViewOptics [Indent level: 5],
                    "viewoptics": {
                        "initanglex": 0,
                        "minanglex": -30,
                        "maxanglex": 30,
                        "initangley": 0,
                        "minangley": -100,
                        "maxangley": 100,
                        "initfov": 0.155,
                        "minfov": 0.034,
                        "maxfov": 0.155,
                        "visionmode": ["Normal","TI"],
                        "thermalmode": [0,1],
                        "minmovex": 0,
                        "maxmovex": 0,
                        "minmovey": 0,
                        "maxmovey": 0,
                        "minmovez": 0,
                        "maxmovez": 0,
                        "speedzoommaxspeed": 1e+010,
                        "speedzoommaxfov": 0
                    },
                    # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn [Indent level: 5],
                    "opticsin": {
                        # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Wide [Indent level: 6]
                        "wide": {
                            "opticsdisplayname": "DAY3",
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "initfov": 0.233333,
                            "minfov": 0.233333,
                            "maxfov": 0.233333,
                            "visionmode": ["Normal","Ti"],
                            "thermalmode": [0,1],
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0,
                            "speedzoommaxspeed": 1e+010,
                            "speedzoommaxfov": 0
                        },
                        # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Medium [Indent level: 6],
                        "medium": {
                            "opticsdisplayname": "DAY12",
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
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
                            "thermalmode": [0,1],
                            "minmovex": 0,
                            "maxmovex": 0,
                            "minmovey": 0,
                            "maxmovey": 0,
                            "minmovez": 0,
                            "maxmovez": 0,
                            "speedzoommaxspeed": 1e+010,
                            "speedzoommaxfov": 0
                        },
                        # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|OpticsIn|Narrow [Indent level: 6],
                        "narrow": {
                            "opticsdisplayname": "DAY24",
                            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
                            "initfov": 0.0291667,
                            "minfov": 0.0291667,
                            "maxfov": 0.0291667,
                            "initanglex": 0,
                            "minanglex": -30,
                            "maxanglex": 30,
                            "initangley": 0,
                            "minangley": -100,
                            "maxangley": 100,
                            "visionmode": ["Normal","Ti"],
                            "thermalmode": [0,1],
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
                    "gunneraction": "mbt2_slot2b_out",
                    "gunnerinaction": "rhs_bmd4_commander_in",
                    "gunnergetinaction": "GetInHigh",
                    "gunnergetoutaction": "GetOutHigh",
                    "personturretaction": "RHS_VehicleTurnout_1",
                    "startengine": 0,
                    "viewgunnerinexternal": 1,
                    "outgunnermayfire": 1,
                    "ingunnermayfire": 1,
                    "dontcreateai": 1,
                    # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints [Indent level: 5],
                    "hitpoints": {
                        # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitTurretCom [Indent level: 6]
                        "hitturretcom": {
                            "armor": 0.7,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.13,
                            "explosionshielding": 0.001,
                            "radius": 0.12,
                            "isturret": 1
                        },
                        # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|HitPoints|HitGunCom [Indent level: 6],
                        "hitguncom": {
                            "armor": 0.7,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passthrough": 0,
                            "minimalhit": 0.13,
                            "explosionshielding": 0.001,
                            "radius": 0.12,
                            "isturret": 1
                        }
                    },
                    "selectionfireanim": "zasleh3",
                    # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components [Indent level: 5],
                    "components": {
                        # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 6]
                        "vehiclesystemsdisplaymanagercomponentleft": {
                            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            },
                            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|MinimapDisplay [Indent level: 7],
                            "minimapdisplay": {
                                "componenttype": "MinimapDisplayComponent",
                                "resource": "RscCustomInfoMiniMap"
                            },
                            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentLeft|VehiclePrimaryGunnerDisplay [Indent level: 7],
                            "vehicleprimarygunnerdisplay": {
                                "componenttype": "TransportFeedDisplayComponent",
                                "source": "PrimaryGunner"
                            }
                        },
                        # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 6],
                        "vehiclesystemsdisplaymanagercomponentright": {
                            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 7]
                            "emptydisplay": {
                                "componenttype": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 7],
                            "crewdisplay": {
                                "componenttype": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            },
                            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|MinimapDisplay [Indent level: 7],
                            "minimapdisplay": {
                                "componenttype": "MinimapDisplayComponent",
                                "resource": "RscCustomInfoMiniMap"
                            },
                            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Turrets|CommanderOptics|Components|VehicleSystemsDisplayManagerComponentRight|VehiclePrimaryGunnerDisplay [Indent level: 7],
                            "vehicleprimarygunnerdisplay": {
                                "componenttype": "TransportFeedDisplayComponent",
                                "source": "PrimaryGunner"
                            }
                        }
                    },
                    "canusescanners": 0,
                    "allowtablock": 0,
                    "ispersonturret": 1,
                    "minoutelev": -30,
                    "maxoutelev": 35,
                    "initoutelev": 0,
                    "minoutturn": -90,
                    "maxoutturn": 90,
                    "initoutturn": 0,
                    "gunnertype": "rhs_vdv_crew_commander",
                    # Class: CfgVehicles|Tank_F|Turrets|MainTurret|Turrets|CommanderOptics|ViewGunner [Indent level: 5],
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
                    "proxytype": "CPCommander",
                    "proxyindex": 1,
                    "gunnername": "Commander",
                    "primarygunner": 0,
                    "animationsourcehatch": "hatchCommander",
                    "animationsourcecamelev": "camElev",
                    "gunneroutopticscolor": [0,0,0,1],
                    "gunneroutforceoptics": 0,
                    "gunneroutopticsshowcursor": 0,
                    "gunneroutopticseffect": [],
                    "memorypointsgetingunner": "pos commander",
                    "memorypointsgetingunnerdir": "pos commander dir",
                    "soundelevation": ["",0.00316228,1],
                    "mincamelev": -90,
                    "maxcamelev": 90,
                    "initcamelev": 0,
                    "primary": 1,
                    "hasgunner": 1,
                    "turretcansee": 0,
                    # Class: CfgVehicles|AllVehicles|NewTurret|TurretSpec [Indent level: 2],
                    "turretspec": {
                        "showheadphones": 0
                    },
                    "gunneropticscolor": [0,0,0,1],
                    "gunnerforceoptics": 1,
                    "gunneropticsshowcursor": 0,
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
                    "forcenvg": 0,
                    "iscopilot": 0,
                    "caneject": 1,
                    "gunnerlefthandanimname": "",
                    "gunnerrighthandanimname": "",
                    "gunnerleftleganimname": "",
                    "gunnerrightleganimname": "",
                    "precisegetinout": 0,
                    "turretfollowfreelook": 0,
                    "showalltargets": 0,
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
                    "showcrewaim": 0
                }
            },
            "magazines": ["rhs_mag_3UOF191_22","rhs_mag_9m117m1_8","rhs_mag_3uof8_237","rhs_mag_3ubr11_227","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_3d17_6","rhs_laserfcsmag","rhs_laserfcsmag"],
            "gunnerdoor": "hatchG",
            "memorypointgun": "usti hlavne2",
            "selectionfireanim": "zasleh2",
            "gunbeg": "usti hlavne",
            "gunend": "konec hlavne",
            "weapons": ["rhs_weap_2a70","rhs_weap_2a72","rhs_weap_pkt_bmd_coax","rhs_weap_902a","rhs_weap_fcs"],
            "maxhorizontalrotspeed": 0.55,
            "maxverticalrotspeed": 0.55,
            "minelev": -5,
            "maxelev": 60,
            "initelev": 10,
            "soundservo": ["A3|Sounds_F|vehicles|armor|noises|servo_best",0.316228,1,50],
            "startengine": 0,
            "turretinfotype": "RHS_RscWeaponESSA_FCS",
            "discretedistance": [],
            "discretedistanceinitindex": 0,
            "memorypointgunneroptics": "gunnerview",
            "gunneroutopticsmodel": "",
            "gunneropticseffect": [],
            "gunneroutopticseffect": ["TankGunnerOptics1","BWTV"],
            "gunnerforceoptics": 1,
            "commanding": 3,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|OpticsIn [Indent level: 3],
            "opticsin": {
                # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|OpticsIn|Wide [Indent level: 4]
                "wide": {
                    "opticsdisplayname": "DAY3",
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "initfov": 0.233333,
                    "minfov": 0.233333,
                    "maxfov": 0.233333,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|OpticsIn|Medium [Indent level: 4],
                "medium": {
                    "opticsdisplayname": "DAY12",
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
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|OpticsIn|Narrow [Indent level: 4],
                "narrow": {
                    "opticsdisplayname": "DAY24",
                    "initfov": 0.0291667,
                    "minfov": 0.0291667,
                    "maxfov": 0.0291667,
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
                    "minmovex": 0,
                    "maxmovex": 0,
                    "minmovey": 0,
                    "maxmovey": 0,
                    "minmovez": 0,
                    "maxmovez": 0,
                    "speedzoommaxspeed": 1e+010,
                    "speedzoommaxfov": 0
                },
                # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|OpticsIn|Autotrack [Indent level: 4],
                "autotrack": {
                    "opticsdisplayname": "AUTOTRACK",
                    "directionstabilized": 1,
                    "initfov": 0.0291667,
                    "minfov": 0.0291667,
                    "maxfov": 0.0291667,
                    "initanglex": 0,
                    "minanglex": -30,
                    "maxanglex": 30,
                    "initangley": 0,
                    "minangley": -100,
                    "maxangley": 100,
                    "visionmode": ["Normal","Ti"],
                    "thermalmode": [0,1],
                    "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
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
            "gunneraction": "mbt2_slot2a_out",
            "gunnerinaction": "rhs_bmd4_gunner_in",
            "forcehidegunner": 0,
            "ingunnermayfire": 1,
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|HitPoints [Indent level: 3],
            "hitpoints": {
                # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|HitPoints|HitTurret [Indent level: 4]
                "hitturret": {
                    "armor": 0.5,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passthrough": 0,
                    "minimalhit": 0.14,
                    "explosionshielding": 0.001,
                    "radius": 0.25
                },
                # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|HitPoints|HitGun [Indent level: 4],
                "hitgun": {
                    "armor": 0.6,
                    "material": -1,
                    "name": "zbran",
                    "visual": "-",
                    "passthrough": 0,
                    "minimalhit": 0.13,
                    "explosionshielding": 0.001,
                    "radius": 0.25
                }
            },
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainTurret|Reflectors [Indent level: 3],
            "reflectors": {
            },
            "lockwhendriverout": 1,
            "ispersonturret": 1,
            "personturretaction": "RHS_VehicleTurnout_1",
            "minoutelev": -30,
            "maxoutelev": 35,
            "initoutelev": 0,
            "minoutturn": -90,
            "maxoutturn": 90,
            "initoutturn": 0,
            "canusescanners": 0,
            "allowtablock": 0,
            "armorlights": 0.1,
            # Class: CfgVehicles|rhs_a3spruttank_base|Turrets|MainTurret|Components [Indent level: 3],
            "components": {
                # Class: CfgVehicles|rhs_a3spruttank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 4]
                "vehiclesystemsdisplaymanagercomponentleft": {
                    # Class: CfgVehicles|rhs_a3spruttank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_a3spruttank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    },
                    # Class: CfgVehicles|rhs_a3spruttank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentLeft|MinimapDisplay [Indent level: 5],
                    "minimapdisplay": {
                        "componenttype": "MinimapDisplayComponent",
                        "resource": "RscCustomInfoMiniMap"
                    }
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 4],
                "vehiclesystemsdisplaymanagercomponentright": {
                    # Class: CfgVehicles|rhs_a3spruttank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 5]
                    "emptydisplay": {
                        "componenttype": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles|rhs_a3spruttank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 5],
                    "crewdisplay": {
                        "componenttype": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    },
                    # Class: CfgVehicles|rhs_a3spruttank_base|Turrets|MainTurret|Components|VehicleSystemsDisplayManagerComponentRight|MinimapDisplay [Indent level: 5],
                    "minimapdisplay": {
                        "componenttype": "MinimapDisplayComponent",
                        "resource": "RscCustomInfoMiniMap"
                    }
                }
            },
            "gunneropticsmodel": "A3|weapons_f|reticle|optics_empty",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "primarygunner": 1,
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
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
            "hasgunner": 1,
            "turretcansee": 0,
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
            "viewgunnershadowdiff": 1,
            "viewgunnershadowamb": 1,
            "ejectdeadgunner": 0,
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "outgunnermayfire": 0,
            "showhmd": 0,
            "lockwhenvehiclespeed": -1,
            "gunnercompartments": "Compartment1",
            "lodturnedin": -1,
            "lodturnedout": -1,
            "memorypointsgetingunnerprecise": "",
            "missilebeg": "spice rakety",
            "missileend": "konec rakety",
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
            "gunnerlefthandanimname": "",
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
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Turrets|GPMGTurret1 [Indent level: 2],
        "gpmgturret1": {
            "proxytype": "CPGunner",
            "proxyindex": 2,
            "body": "obsTurret2",
            "gun": "obsGun2",
            "animationsourcebody": "obsTurret2",
            "animationsourcegun": "obsGun2",
            "animationsourcehatch": "",
            "gunnerdoor": "hatchCR",
            "selectionfireanim": "zasleh3",
            "gunnername": "Right Hull Gunner",
            "hasgunner": 1,
            "dontcreateai": 1,
            "forcehidegunner": 1,
            "primaryobserver": 0,
            "primarygunner": 0,
            "commanding": 1,
            "minelev": -10,
            "maxelev": 10,
            "minturn": -10,
            "maxturn": 10,
            "weapons": ["rhs_weap_pkt_bmd_bow1"],
            "magazines": ["rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250"],
            "ejectdeadgunner": 0,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|GPMGTurret1|CargoLight [Indent level: 3],
            "cargolight": {
                "ambient": [0.6,0,0.15,1],
                "brightness": 0.007,
                "color": [0,0,0,0]
            },
            "gunbeg": "muzzle2",
            "gunend": "end2",
            "memorypointgun": "memoryPointGun2",
            "memorypointgunneroptics": "gunnerview3",
            "memorypointsgetingunner": "pos cargo R",
            "memorypointsgetingunnerdir": "pos cargo R dir",
            "gunneraction": "mbt2_slot2a_out",
            "gunnerinaction": "rhs_bmd4_cargo_in",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "viewgunnerinexternal": 1,
            "startengine": 0,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|GPMGTurret1|Turrets [Indent level: 3],
            "turrets": {
            },
            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpp220a_right",
            "gunneropticscolor": [1,1,1,1],
            "gunnerforceoptics": 1,
            "gunneropticseffect": ["TankGunnerOptics1","WeaponsOptics","OpticsCHAbera3"],
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|GPMGTurret1|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "opticszoommin": 0.166666,
                "opticszoommax": 0.166666,
                "distancezoommin": 200,
                "distancezoommax": 2000,
                "initfov": 0.166666,
                "minfov": 0.166666,
                "maxfov": 0.166666
            },
            "unloadincombat": 1,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|GPMGTurret1|HitPoints [Indent level: 3],
            "hitpoints": {
            },
            "animationsourcecamelev": "camElev",
            "gunnertype": "",
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
            "gunneropticsshowcursor": 0,
            "turretinfotype": "",
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
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
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "outgunnermayfire": 0,
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
            "forcenvg": 0,
            "iscopilot": 0,
            "caneject": 1,
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
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
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Turrets|GPMGTurret2 [Indent level: 2],
        "gpmgturret2": {
            "weapons": ["rhs_weap_pkt_bmd_bow2"],
            "body": "LF_Seat_turret",
            "gun": "LF_Seat_gun",
            "animationsourcebody": "LF_Seat_Turret",
            "animationsourcegun": "LF_Seat_Gun",
            "gunnername": "Left Hull Gunner",
            "memorypointgunneroptics": "gunnerView2",
            "commanding": 1,
            "gunnerdoor": "hatchCL",
            "memorypointsgetingunner": "pos cargo L",
            "memorypointsgetingunnerdir": "pos cargo L dir",
            "memorypointgun": "memoryPointGun3",
            "gunbeg": "muzzle3",
            "gunend": "end3",
            "selectionfireanim": "zasleh4",
            "proxyindex": 3,
            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpp220a",
            "proxytype": "CPGunner",
            "animationsourcehatch": "",
            "hasgunner": 1,
            "dontcreateai": 1,
            "forcehidegunner": 1,
            "primaryobserver": 0,
            "primarygunner": 0,
            "minelev": -10,
            "maxelev": 10,
            "minturn": -10,
            "maxturn": 10,
            "magazines": ["rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250"],
            "ejectdeadgunner": 0,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|GPMGTurret1|CargoLight [Indent level: 3],
            "cargolight": {
                "ambient": [0.6,0,0.15,1],
                "brightness": 0.007,
                "color": [0,0,0,0]
            },
            "gunneraction": "mbt2_slot2a_out",
            "gunnerinaction": "rhs_bmd4_cargo_in",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "viewgunnerinexternal": 1,
            "startengine": 0,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|GPMGTurret1|Turrets [Indent level: 3],
            "turrets": {
            },
            "gunneropticscolor": [1,1,1,1],
            "gunnerforceoptics": 1,
            "gunneropticseffect": ["TankGunnerOptics1","WeaponsOptics","OpticsCHAbera3"],
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|GPMGTurret1|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -30,
                "maxanglex": 30,
                "initangley": 0,
                "minangley": -100,
                "maxangley": 100,
                "opticszoommin": 0.166666,
                "opticszoommax": 0.166666,
                "distancezoommin": 200,
                "distancezoommax": 2000,
                "initfov": 0.166666,
                "minfov": 0.166666,
                "maxfov": 0.166666
            },
            "unloadincombat": 1,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|GPMGTurret1|HitPoints [Indent level: 3],
            "hitpoints": {
            },
            "animationsourcecamelev": "camElev",
            "gunnertype": "",
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
            "gunneropticsshowcursor": 0,
            "turretinfotype": "",
            "gunneroutopticsmodel": "",
            "gunneroutopticscolor": [0,0,0,1],
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
            "hideweaponsgunner": 1,
            "canhidegunner": -1,
            "outgunnermayfire": 0,
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
            "forcenvg": 0,
            "iscopilot": 0,
            "caneject": 1,
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
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
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Turrets|RightBack [Indent level: 2],
        "rightback": {
            "body": "RB_Seat_Turret",
            "gun": "RB_Seat_gun",
            "animationsourcebody": "RB_Seat_Turret",
            "animationsourcegun": "RB_Seat_Gun",
            "initturn": -60,
            "minturn": -60.001,
            "maxturn": -60,
            "gunnername": "Right Cargo",
            "memorypointgunneroptics": "rseat_view",
            "gunnerdoor": "hatchCR",
            "commanding": 2,
            "proxyindex": 5,
            "memorypointsgetingunner": "pos cargo R",
            "memorypointsgetingunnerdir": "pos cargo R dir",
            "proxytype": "CPGunner",
            "animationsourcehatch": "",
            "selectionfireanim": "",
            "minelev": 0,
            "maxelev": 0,
            "maxhorizontalrotspeed": 0,
            "maxverticalrotspeed": 0,
            "gunbeg": "",
            "gunend": "",
            "memorypointgun": "",
            "gunneraction": "mbt2_slot2a_out",
            "gunnerinaction": "rhs_bmd4_cargo_in",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "weapons": [],
            "magazines": [],
            "forcehidegunner": 1,
            "hasgunner": 1,
            "dontcreateai": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpo170a",
            "gunneropticscolor": [1,1,1,1],
            "gunnerforceoptics": 1,
            "startengine": 0,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|LeftBack|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -110,
                "maxanglex": 110,
                "initangley": 0,
                "minangley": -110,
                "maxangley": 110,
                "opticszoommin": 0.7,
                "opticszoommax": 0.7,
                "distancezoommin": 20,
                "distancezoommax": 2000,
                "initfov": 0.7,
                "minfov": 0.7,
                "maxfov": 0.7
            },
            "unloadincombat": 1,
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|LeftBack|HitPoints [Indent level: 3],
            "hitpoints": {
            },
            "animationsourcecamelev": "camElev",
            "gunnertype": "",
            "soundservo": ["",0.00316228,1],
            "soundelevation": ["",0.00316228,1],
            "initelev": 0,
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
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
            "outgunnermayfire": 0,
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
            "forcenvg": 0,
            "iscopilot": 0,
            "caneject": 1,
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
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
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Turrets|LeftBack [Indent level: 2],
        "leftback": {
            "gunnerdoor": "hatchCLB",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "proxytype": "CPGunner",
            "body": "LB_Seat_turret",
            "gun": "LB_Seat_Gun",
            "animationsourcebody": "LB_Seat_Turret",
            "animationsourcegun": "LB_Seat_Gun",
            "animationsourcehatch": "",
            "selectionfireanim": "",
            "minelev": 0,
            "maxelev": 0,
            "initturn": 60,
            "minturn": 60,
            "maxturn": 60.001,
            "maxhorizontalrotspeed": 0,
            "maxverticalrotspeed": 0,
            "proxyindex": 4,
            "gunnername": "Left Cargo",
            "commanding": 2,
            "gunbeg": "",
            "gunend": "",
            "memorypointgun": "",
            "memorypointgunneroptics": "lseat_view",
            "gunneraction": "mbt2_slot2a_out",
            "gunnerinaction": "rhs_bmd4_cargo_in",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "weapons": [],
            "magazines": [],
            "forcehidegunner": 1,
            "hasgunner": 1,
            "dontcreateai": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpo170a",
            "gunneropticscolor": [1,1,1,1],
            "gunnerforceoptics": 1,
            "startengine": 0,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|LeftBack|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -110,
                "maxanglex": 110,
                "initangley": 0,
                "minangley": -110,
                "maxangley": 110,
                "opticszoommin": 0.7,
                "opticszoommax": 0.7,
                "distancezoommin": 20,
                "distancezoommax": 2000,
                "initfov": 0.7,
                "minfov": 0.7,
                "maxfov": 0.7
            },
            "unloadincombat": 1,
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|LeftBack|HitPoints [Indent level: 3],
            "hitpoints": {
            },
            "animationsourcecamelev": "camElev",
            "gunnertype": "",
            "soundservo": ["",0.00316228,1],
            "soundelevation": ["",0.00316228,1],
            "initelev": 0,
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
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
            "outgunnermayfire": 0,
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
            "forcenvg": 0,
            "iscopilot": 0,
            "caneject": 1,
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
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
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Turrets|MiddleBack [Indent level: 2],
        "middleback": {
            "gunnername": "Middle Rear Cargo",
            "body": "RB_Seat_Turret",
            "gun": "RB_Seat_gun",
            "animationsourcebody": "",
            "animationsourcegun": "",
            "memorypointgunneroptics": "rseat_view",
            "proxyindex": 6,
            "gunnerdoor": "hatchCLB",
            "memorypointsgetingunner": "pos gunner",
            "memorypointsgetingunnerdir": "pos gunner dir",
            "proxytype": "CPGunner",
            "animationsourcehatch": "",
            "selectionfireanim": "",
            "minelev": 0,
            "maxelev": 0,
            "initturn": 60,
            "minturn": 60,
            "maxturn": 60.001,
            "maxhorizontalrotspeed": 0,
            "maxverticalrotspeed": 0,
            "commanding": 2,
            "gunbeg": "",
            "gunend": "",
            "memorypointgun": "",
            "gunneraction": "mbt2_slot2a_out",
            "gunnerinaction": "rhs_bmd4_cargo_in",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "weapons": [],
            "magazines": [],
            "forcehidegunner": 1,
            "hasgunner": 1,
            "dontcreateai": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpo170a",
            "gunneropticscolor": [1,1,1,1],
            "gunnerforceoptics": 1,
            "startengine": 0,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|LeftBack|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -110,
                "maxanglex": 110,
                "initangley": 0,
                "minangley": -110,
                "maxangley": 110,
                "opticszoommin": 0.7,
                "opticszoommax": 0.7,
                "distancezoommin": 20,
                "distancezoommax": 2000,
                "initfov": 0.7,
                "minfov": 0.7,
                "maxfov": 0.7
            },
            "unloadincombat": 1,
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|LeftBack|HitPoints [Indent level: 3],
            "hitpoints": {
            },
            "animationsourcecamelev": "camElev",
            "gunnertype": "",
            "soundservo": ["",0.00316228,1],
            "soundelevation": ["",0.00316228,1],
            "initelev": 0,
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
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
            "outgunnermayfire": 0,
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
            "forcenvg": 0,
            "iscopilot": 0,
            "caneject": 1,
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
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
            "showcrewaim": 0
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|MainFront [Indent level: 2],
        "mainfront": {
            "body": "LF_Seat_turret",
            "gun": "LF_Seat_gun",
            "animationsourcebody": "LF_Seat_Turret",
            "animationsourcegun": "LF_Seat_Gun",
            "initturn": 0,
            "minturn": 0,
            "maxturn": 0.001,
            "gunnername": "Front Cargo",
            "memorypointgunneroptics": "gunnerView2",
            "commanding": 1,
            "proxyindex": 3,
            "proxytype": "CPGunner",
            "animationsourcehatch": "",
            "selectionfireanim": "",
            "gunnerdoor": "hatchCL",
            "minelev": 0,
            "maxelev": 0,
            "maxhorizontalrotspeed": 0,
            "maxverticalrotspeed": 0,
            "memorypointsgetingunner": "pos cargo L",
            "memorypointsgetingunnerdir": "pos cargo L dir",
            "gunbeg": "",
            "gunend": "",
            "memorypointgun": "",
            "gunneraction": "mbt2_slot2a_out",
            "gunnerinaction": "rhs_bmd4_cargo_in",
            "gunnergetinaction": "GetInHigh",
            "gunnergetoutaction": "GetOutHigh",
            "weapons": [],
            "magazines": [],
            "forcehidegunner": 1,
            "hasgunner": 1,
            "dontcreateai": 1,
            "primarygunner": 0,
            "primaryobserver": 0,
            "gunneropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpo170a",
            "gunneropticscolor": [1,1,1,1],
            "gunnerforceoptics": 1,
            "startengine": 0,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|LeftBack|ViewOptics [Indent level: 3],
            "viewoptics": {
                "initanglex": 0,
                "minanglex": -110,
                "maxanglex": 110,
                "initangley": 0,
                "minangley": -110,
                "maxangley": 110,
                "opticszoommin": 0.7,
                "opticszoommax": 0.7,
                "distancezoommin": 20,
                "distancezoommax": 2000,
                "initfov": 0.7,
                "minfov": 0.7,
                "maxfov": 0.7
            },
            "unloadincombat": 1,
            "viewgunnerinexternal": 1,
            # Class: CfgVehicles|rhs_bmd4_vdv|Turrets|LeftBack|HitPoints [Indent level: 3],
            "hitpoints": {
            },
            "animationsourcecamelev": "camElev",
            "gunnertype": "",
            "soundservo": ["",0.00316228,1],
            "soundelevation": ["",0.00316228,1],
            "initelev": 0,
            "minoutelev": -4,
            "maxoutelev": 20,
            "initoutelev": 0,
            "minoutturn": -60,
            "maxoutturn": 60,
            "initoutturn": 0,
            "mincamelev": -90,
            "maxcamelev": 90,
            "initcamelev": 0,
            "stabilizedinaxes": 3,
            "primary": 1,
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
            "outgunnermayfire": 0,
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
            "forcenvg": 0,
            "iscopilot": 0,
            "caneject": 1,
            "gunnerlefthandanimname": "",
            "gunnerrighthandanimname": "",
            "gunnerleftleganimname": "",
            "gunnerrightleganimname": "",
            "precisegetinout": 0,
            "turretfollowfreelook": 0,
            "allowtablock": 1,
            "showalltargets": 0,
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
            "showcrewaim": 0
        }
    },
    # Class: CfgVehicles|rhs_bmd4m_vdv|Damage [Indent level: 1],
    "damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4_02.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4_02.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4_02.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4_03.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4_03.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4_03.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_01.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4m_01.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4m_01.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_01a.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4m_01a.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4m_01a.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_02a.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4m_02a.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4m_02a.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_a.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4m_a.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4m_a.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_t.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4m_t.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4m_t.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_w.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4m_w.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4m_w.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles|rhs_bmd4m_vdv|Exhausts [Indent level: 1],
    "exhausts": {
        # Class: CfgVehicles|rhs_bmd4m_vdv|Exhausts|Exhaust1 [Indent level: 2]
        "exhaust1": {
            "position": "exhaustl",
            "direction": "exhaustl_dir",
            "effect": "ExhaustEffectTankSide"
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|Exhausts|Exhaust2 [Indent level: 2],
        "exhaust2": {
            "position": "exhaustr",
            "direction": "exhaustr_dir",
            "effect": "ExhaustEffectTankSide"
        }
    },
    # Class: CfgVehicles|rhs_bmd4m_vdv|AnimationSources [Indent level: 1],
    "animationsources": {
        # Class: CfgVehicles|rhs_bmd4m_vdv|AnimationSources|muzzle_rot_mg3 [Indent level: 2]
        "muzzle_rot_mg3": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkt_bmd_bow2"
        },
        # Class: CfgVehicles|rhs_bmd4m_vdv|AnimationSources|smokecap_revolving_source [Indent level: 2],
        "smokecap_revolving_source": {
            "source": "revolving",
            "weapon": "rhs_weap_902a"
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|recoil_source [Indent level: 2],
        "recoil_source": {
            "source": "reload",
            "weapon": "rhs_weap_2a70"
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|recoil_source2 [Indent level: 2],
        "recoil_source2": {
            "source": "reload",
            "weapon": "rhs_weap_2a72"
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|muzzle_hide_cannon [Indent level: 2],
        "muzzle_hide_cannon": {
            "source": "reload",
            "weapon": "rhs_weap_2a70"
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|muzzle_rot_cannon [Indent level: 2],
        "muzzle_rot_cannon": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a70"
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|muzzle_hide_hmg [Indent level: 2],
        "muzzle_hide_hmg": {
            "source": "reload",
            "weapon": "rhs_weap_2a72"
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|muzzle_rot_hmg [Indent level: 2],
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a72"
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|muzzle_rot_mg1 [Indent level: 2],
        "muzzle_rot_mg1": {
            "weapon": "rhs_weap_pkt_bmd_coax",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|muzzle_rot_mg2 [Indent level: 2],
        "muzzle_rot_mg2": {
            "weapon": "rhs_weap_pkt_bmd_bow1",
            "source": "ammorandom"
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|autoloader [Indent level: 2],
        "autoloader": {
            "source": "user",
            "animperiod": 1.25,
            "initphase": 0
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|elev [Indent level: 2],
        "elev": {
            "source": "user",
            "animperiod": 0.0009
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|elev_bank [Indent level: 2],
        "elev_bank": {
            "source": "user",
            "animperiod": 0.0009
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|lead [Indent level: 2],
        "lead": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|offset [Indent level: 2],
        "offset": {
            "source": "user",
            "animperiod": 0.0002
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|hatchCL [Indent level: 2],
        "hatchcl": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|hatchCLB [Indent level: 2],
        "hatchclb": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|hatchCR [Indent level: 2],
        "hatchcr": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|HatchC [Indent level: 2],
        "hatchc": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|HatchG [Indent level: 2],
        "hatchg": {
            "source": "door",
            "animperiod": 2.1
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|AnimationSources|HatchD [Indent level: 2],
        "hatchd": {
            "source": "door",
            "animperiod": 2.1
        }
    },
    "rhs_decalparameters": ["['Number',cRHSBMD4NumberPlaces,'Default']","['Label',cRHSBMD4PlnSymPlaces, 'Platoon',11]"],
    "vehicleclass": "rhs_vehclass_ifv",
    "editorsubcategory": "rhs_EdSubcat_ifv",
    "scope": 2,
    "fuelcapacity": 560,
    "rhs_fuelcapacity": 560,
    "brakeidlespeed": 1,
    "tankturnforce": 350000,
    "tankturnforceangminspd": 0.7,
    "tankturnforceangspd": 0.85,
    "accelaidforcecoef": 2,
    "accelaidforceyoffset": -6,
    "accelaidforcespd": 2.23,
    "antirollbarforcecoef": 24,
    "antirollbarforcelimit": 42,
    "antirollbarspeedmin": 30,
    "antirollbarspeedmax": 75,
    "canfloat": 1,
    "waterleakiness": 250,
    "maxfordingdepth": 10.1,
    "waterresistance": 1,
    "waterdamageengine": 0.9,
    "engineshifty": 0.7,
    "waterlineardampingcoefy": 2,
    "waterlineardampingcoefx": 2,
    "waterangulardampingcoef": 1.2,
    "waterresistancecoef": 0.375,
    "watereffectspeed": 5,
    "engineeffectspeed": 5,
    "waterfasteffectspeed": 28,
    "enginemoi": 25,
    "minomega": 67.86,
    "thrustdelay": 0.25,
    "enginelosses": 32,
    "transmissionlosses": 20,
    "clutchstrength": 25,
    "switchtime": 0.1,
    "latency": 0.1,
    "changegeartype": "rpmratio",
    "changegearomegaratios": [1,0.434783,0.434783,0,0.913043,0.608696,0.956522,0.608696,0.956522,0.608696,1,0.652174],
    # Class: CfgVehicles|rhs_bmd4_vdv|complexGearbox [Indent level: 1],
    "complexgearbox": {
        "gearboxratios": ["R1",-4.31,"N",0,"D1",3.31,"D2",1.934,"D3",1.132,"D4",0.662],
        "amphibiousratios": ["R1",-9.5,"N",0,"D1",9.5],
        "transmissionratios": ["High",11.5],
        "gearboxmode": "auto",
        "moveoffgear": 1,
        "drivestring": "D",
        "neutralstring": "N",
        "reversestring": "R",
        "transmissiondelay": 0.6
    },
    "icon": "rhsafrf|addons|rhs_bmd_34|data|icons|bmd4_mapicon_ca.paa",
    "mapsize": 6.5,
    "transportsoldier": 0,
    "unloadincombat": 1,
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "weaponsgroup1": "1 + 16",
    "weaponsgroup2": 128,
    "weaponsgroup3": 2,
    "weaponsgroup4": 4,
    "cargoaction": ["YouShallNotSitHere"],
    "cargocompartments": ["Compartment3"],
    # Class: CfgVehicles|rhs_bmd4_vdv|SpeechVariants [Indent level: 1],
    "speechvariants": {
        # Class: CfgVehicles|rhs_bmd4_vdv|SpeechVariants|Default [Indent level: 2]
        "default": {
            "speechsingular": ["veh_vehicle_APC_s"],
            "speechplural": ["veh_vehicle_APC_p"]
        }
    },
    "textsingular": "BMD",
    "textplural": "BMDs",
    "namesound": "veh_vehicle_APC_s",
    "hiddenselections": ["camo1","camo2","camo3","camo4","camo5","n1","n2","n3","i1"],
    # Class: CfgVehicles|rhs_bmd4_vdv|Attributes [Indent level: 1],
    "attributes": {
        # Class: CfgVehicles|rhs_bmd4_vdv|Attributes|ObjectTexture [Indent level: 2]
        "objecttexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayname": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|Attributes|rhs_decalNumber_type [Indent level: 2],
        "rhs_decalnumber_type": {
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cRHSBMD4NumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "displayname": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalNumber_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalNumber_type|values|Default [Indent level: 4]
                "default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultvalue": "Default"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalNumber_type|values|DefaultRed [Indent level: 4],
                "defaultred": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalNumber_type|values|BoldRed [Indent level: 4],
                "boldred": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalNumber_type|values|CDF [Indent level: 4],
                "cdf": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalNumber_type|values|Handpaint [Indent level: 4],
                "handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalNumber_type|values|HandpaintBlack [Indent level: 4],
                "handpaintblack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalNumber_type|values|Iraqi [Indent level: 4],
                "iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalNumber_type|values|LicensePlate [Indent level: 4],
                "licenseplate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|Attributes|rhs_decalNumber [Indent level: 2],
        "rhs_decalnumber": {
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSBMD4NumberPlaces}else{[_this, [['Number', cRHSBMD4NumberPlaces, _this getVariable ['rhs_decalNumber_type','Default'], _value] ] ] call rhs_fnc_decalsInit}};",
            "collapsed": 1,
            "displayname": "Set side number",
            "tooltip": "Set side number. 4 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typename": "Number",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|Attributes|rhs_decalPlatoon_type [Indent level: 2],
        "rhs_decalplatoon_type": {
            "displayname": "Define platoon symbol type",
            "tooltip": "Decal type",
            "property": "rhs_decalPlatoon_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": "0",
            "typename": "STRING",
            # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalPlatoon_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalPlatoon_type|values|Platoon [Indent level: 4]
                "platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalPlatoon_type|values|PlatoonGDR [Indent level: 4],
                "platoongdr": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalPlatoon_type|values|PlatoonVDV [Indent level: 4],
                "platoonvdv": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalPlatoon_type|values|Army [Indent level: 4],
                "army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultvalue": "Army"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalPlatoon_type|values|Honor [Indent level: 4],
                "honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_decalPlatoon_type|values|HonorGDR [Indent level: 4],
                "honorgdr": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            }
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|Attributes|rhs_decalPlatoon [Indent level: 2],
        "rhs_decalplatoon": {
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHSBMD4PlnSymPlaces,  _this getVariable ['rhs_decalPlatoon_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};",
            "displayname": "Set platoon symbol",
            "tooltip": "Set platoon symbol located on both sides. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "control": "Edit",
            "validate": "none",
            "defaultvalue": "-1"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type [Indent level: 2],
        "rhs_ammoslot_1_type": {
            "displayname": "Ammo slot #1 type",
            "tooltip": "Define type of shell for #1 slot",
            "property": "rhs_ammoslot_1_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING",
            # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm46_10 [Indent level: 4]
                "rhs_mag_3bm46_10": {
                    "name": "APFSDS-T 3BM46",
                    "value": "rhs_mag_3bm46",
                    "defaultvalue": "rhs_mag_3bm46"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm9_10 [Indent level: 4],
                "rhs_mag_3bm9_10": {
                    "name": "APFSDS-T 3BM9",
                    "value": "rhs_mag_3bm9",
                    "defaultvalue": "rhs_mag_3bm9"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm12_10 [Indent level: 4],
                "rhs_mag_3bm12_10": {
                    "name": "APFSDS-T 3BM12",
                    "value": "rhs_mag_3bm12",
                    "defaultvalue": "rhs_mag_3bm12"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm15_10 [Indent level: 4],
                "rhs_mag_3bm15_10": {
                    "name": "APFSDS-T 3BM15",
                    "value": "rhs_mag_3bm15",
                    "defaultvalue": "rhs_mag_3bm15"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm17_10 [Indent level: 4],
                "rhs_mag_3bm17_10": {
                    "name": "APFSDS-T 3BM17",
                    "value": "rhs_mag_3bm17",
                    "defaultvalue": "rhs_mag_3bm17"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm22_10 [Indent level: 4],
                "rhs_mag_3bm22_10": {
                    "name": "APFSDS-T 3BM22",
                    "value": "rhs_mag_3bm22",
                    "defaultvalue": "rhs_mag_3bm22"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm29_10 [Indent level: 4],
                "rhs_mag_3bm29_10": {
                    "name": "APFSDS-T 3BM29",
                    "value": "rhs_mag_3bm29",
                    "defaultvalue": "rhs_mag_3bm29"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm26_10 [Indent level: 4],
                "rhs_mag_3bm26_10": {
                    "name": "APFSDS-T 3BM26",
                    "value": "rhs_mag_3bm26",
                    "defaultvalue": "rhs_mag_3bm26"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm32_10 [Indent level: 4],
                "rhs_mag_3bm32_10": {
                    "name": "APFSDS-T 3BM32",
                    "value": "rhs_mag_3bm32",
                    "defaultvalue": "rhs_mag_3bm32"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm42_10 [Indent level: 4],
                "rhs_mag_3bm42_10": {
                    "name": "APFSDS-T 3BM42",
                    "value": "rhs_mag_3bm42",
                    "defaultvalue": "rhs_mag_3bm42"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1_type|values|rhs_mag_3bm42m_10 [Indent level: 4],
                "rhs_mag_3bm42m_10": {
                    "name": "APFSDS-T 3BM42M",
                    "value": "rhs_mag_3bm42m",
                    "defaultvalue": "rhs_mag_3bm42m"
                }
            }
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_1 [Indent level: 2],
        "rhs_ammoslot_1": {
            "displayname": "Ammo slot #1 count",
            "tooltip": "Define number of rounds stored inside of type #1. Max 22. Leave -1 for default loadout",
            "property": "rhs_ammoslot_1",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',22] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_2_type [Indent level: 2],
        "rhs_ammoslot_2_type": {
            "displayname": "Ammo slot #2 type",
            "tooltip": "Define type of shell for #2 slot",
            "property": "rhs_ammoslot_2_type",
            # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_2_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk31_8 [Indent level: 4]
                "rhs_mag_3bk31_8": {
                    "name": "HEAT-FS 3BK31",
                    "value": "rhs_mag_3bk31",
                    "defaultvalue": "rhs_mag_3bk31"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk12_8 [Indent level: 4],
                "rhs_mag_3bk12_8": {
                    "name": "HEAT-FS 3BK12",
                    "value": "rhs_mag_3bk12",
                    "defaultvalue": "rhs_mag_3bk12"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk14_8 [Indent level: 4],
                "rhs_mag_3bk14_8": {
                    "name": "HEAT-FS 3BK14",
                    "value": "rhs_mag_3bk14",
                    "defaultvalue": "rhs_mag_3bk14"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk18_8 [Indent level: 4],
                "rhs_mag_3bk18_8": {
                    "name": "HEAT-FS 3BK18",
                    "value": "rhs_mag_3bk18",
                    "defaultvalue": "rhs_mag_3bk18"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk18m_8 [Indent level: 4],
                "rhs_mag_3bk18m_8": {
                    "name": "HEAT-FS 3BK18M",
                    "value": "rhs_mag_3bk18m",
                    "defaultvalue": "rhs_mag_3bk18m"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk21_8 [Indent level: 4],
                "rhs_mag_3bk21_8": {
                    "name": "HEAT-FS 3BK21",
                    "value": "rhs_mag_3bk21",
                    "defaultvalue": "rhs_mag_3bk21"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_2_type|values|rhs_mag_3bk29_8 [Indent level: 4],
                "rhs_mag_3bk29_8": {
                    "name": "HEAT-FS 3BK29",
                    "value": "rhs_mag_3bk29",
                    "defaultvalue": "rhs_mag_3bk29"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_2 [Indent level: 2],
        "rhs_ammoslot_2": {
            "displayname": "Ammo slot #2 count",
            "tooltip": "Define number of rounds stored inside of type #2. Max 22. Leave -1 for default loadout",
            "property": "rhs_ammoslot_2",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',22] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_3_type [Indent level: 2],
        "rhs_ammoslot_3_type": {
            "displayname": "Ammo slot #3 type",
            "tooltip": "Define type of shell for #3 slot",
            "property": "rhs_ammoslot_3_type",
            # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_3_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_3_type|values|rhs_mag_3of26_6 [Indent level: 4]
                "rhs_mag_3of26_6": {
                    "name": "HE-FRAG-FS 3OF26",
                    "value": "rhs_mag_3of26",
                    "defaultvalue": "rhs_mag_3of26"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_3_type|values|rhs_mag_3of11_6 [Indent level: 4],
                "rhs_mag_3of11_6": {
                    "name": "HE-FRAG-FS 3OF11",
                    "value": "rhs_mag_3of11",
                    "defaultvalue": "rhs_mag_3of11"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_3 [Indent level: 2],
        "rhs_ammoslot_3": {
            "displayname": "Ammo slot #3 count",
            "tooltip": "Define number of rounds stored inside of type #3. Max 22. Leave -1 for default loadout",
            "property": "rhs_ammoslot_3",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',22] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_4_type [Indent level: 2],
        "rhs_ammoslot_4_type": {
            "displayname": "Ammo slot #4 type",
            "tooltip": "Define type of shell for #4 slot",
            "property": "rhs_ammoslot4_type",
            # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_4_type|values [Indent level: 3],
            "values": {
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m119m_6 [Indent level: 4]
                "rhs_mag_9m119m_6": {
                    "name": "ATGM 9M119M",
                    "value": "rhs_mag_9m119m",
                    "defaultvalue": "rhs_mag_9m119m"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m119_6 [Indent level: 4],
                "rhs_mag_9m119_6": {
                    "name": "ATGM 9M119",
                    "value": "rhs_mag_9m119",
                    "defaultvalue": "rhs_mag_9m119"
                },
                # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_4_type|values|rhs_mag_9m119f_6 [Indent level: 4],
                "rhs_mag_9m119f_6": {
                    "name": "ATGM 9M119F",
                    "value": "rhs_mag_9m119f",
                    "defaultvalue": "rhs_mag_9m119f"
                }
            },
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultvalue": 0,
            "typename": "STRING"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Attributes|rhs_ammoslot_4 [Indent level: 2],
        "rhs_ammoslot_4": {
            "displayname": "Ammo slot #4 count",
            "tooltip": "Define number of rounds stored inside of type #4. Max 22. Leave -1 for default loadout",
            "property": "rhs_ammoslot_4",
            "control": "Edit",
            "expression": "if(_value >= 0)then{ [_this,_value,'%s',22] spawn rhs_fnc_TTanks_DefineLoadout};",
            "defaultvalue": "-1",
            "validate": "NUMBER",
            "typename": "NUMBER"
        }
    },
    # Class: CfgVehicles|rhs_bmd4_vdv|UserActions [Indent level: 1],
    "useractions": {
        # Class: CfgVehicles|rhs_bmd4_vdv|UserActions|LowerSusp [Indent level: 2]
        "lowersusp": {
            "displayname": "Lower Suspension",
            "position": "",
            "radius": 5,
            "condition": "(player == driver this) && (2 > speed this) && !(surfaceIsWater getPos this) && getmass this <15000",
            "statement": "this setmass [(getmass this)*4,7];this setVelocity [0.01,0.01,0.01]",
            "onlyforplayer": 1
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|UserActions|RaiseSusp [Indent level: 2],
        "raisesusp": {
            "displayname": "Raise Suspension",
            "condition": "(player == driver this) && (2 > speed this) && !(surfaceIsWater getPos this) && getmass this >15000",
            "statement": "this setmass [(getmass this)/4,7];this setVelocity [0.01,0.01,0.01]",
            "position": "",
            "radius": 5,
            "onlyforplayer": 1
        }
    },
    # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines [Indent level: 1],
    "transportmagazines": {
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines|_xx_rhs_30Rnd_545x39_7N10_AK [Indent level: 2]
        "_xx_rhs_30rnd_545x39_7n10_ak": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": 30
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines|_xx_rhs_10Rnd_762x54mmR_7N1 [Indent level: 2],
        "_xx_rhs_10rnd_762x54mmr_7n1": {
            "magazine": "rhs_10Rnd_762x54mmR_7N1",
            "count": 10
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines|_xx_rhs_100Rnd_762x54mmR [Indent level: 2],
        "_xx_rhs_100rnd_762x54mmr": {
            "magazine": "rhs_100Rnd_762x54mmR",
            "count": 3
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines|_xx_rhs_mag_rdg2_white [Indent level: 2],
        "_xx_rhs_mag_rdg2_white": {
            "magazine": "rhs_mag_rdg2_white",
            "count": 2
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines|_xx_rhs_mag_rgd5 [Indent level: 2],
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 9
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines|_xx_rhs_VOG25 [Indent level: 2],
        "_xx_rhs_vog25": {
            "magazine": "rhs_VOG25",
            "count": 20
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines|_xx_rhs_vg40op_white [Indent level: 2],
        "_xx_rhs_vg40op_white": {
            "magazine": "rhs_vg40op_white",
            "count": 5
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines|_xx_rhs_GRD40_white [Indent level: 2],
        "_xx_rhs_grd40_white": {
            "magazine": "rhs_GRD40_white",
            "count": 5
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines|_xx_rhs_rpg26_mag [Indent level: 2],
        "_xx_rhs_rpg26_mag": {
            "magazine": "rhs_rpg26_mag",
            "count": 2
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportMagazines|_xx_rhs_rpg7_OG7V_mag [Indent level: 2],
        "_xx_rhs_rpg7_og7v_mag": {
            "magazine": "rhs_rpg7_OG7V_mag",
            "count": 2
        }
    },
    # Class: CfgVehicles|rhs_bmd4_vdv|TransportWeapons [Indent level: 1],
    "transportweapons": {
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportWeapons|_xx_rhs_weap_ak74m [Indent level: 2]
        "_xx_rhs_weap_ak74m": {
            "weapon": "rhs_weap_ak74m",
            "count": 4
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportWeapons|_xx_rhs_weap_rpg26 [Indent level: 2],
        "_xx_rhs_weap_rpg26": {
            "weapon": "rhs_weap_rpg26",
            "count": 2
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportWeapons|_xx_rhs_weap_rpg7 [Indent level: 2],
        "_xx_rhs_weap_rpg7": {
            "weapon": "rhs_weap_rpg7",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhs_bmd4_vdv|TransportItems [Indent level: 1],
    "transportitems": {
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportItems|_xx_FirstAidKit [Indent level: 2]
        "_xx_firstaidkit": {
            "name": "FirstAidKit",
            "count": 10
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportItems|_xx_Medikit [Indent level: 2],
        "_xx_medikit": {
            "name": "Medikit",
            "count": 1
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportItems|_xx_Toolkit [Indent level: 2],
        "_xx_toolkit": {
            "name": "Toolkit",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhs_bmd4_vdv|TransportBackpacks [Indent level: 1],
    "transportbackpacks": {
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportBackpacks|_xx_rhs_sidor [Indent level: 2]
        "_xx_rhs_sidor": {
            "backpack": "rhs_sidor",
            "count": 7
        },
        # Class: CfgVehicles|rhs_bmd4_vdv|TransportBackpacks|_xx_rhs_rpg [Indent level: 2],
        "_xx_rhs_rpg": {
            "backpack": "rhs_rpg",
            "count": 1
        }
    },
    # Class: CfgVehicles|rhs_bmd4_vdv|EventHandlers [Indent level: 1],
    "eventhandlers": {
        # Class: CfgVehicles|rhs_bmd4_vdv|EventHandlers|RHS_EventHandlers [Indent level: 2]
        "rhs_eventhandlers": {
            "init": "_this call RHS_fnc_sprut_init;",
            "fired": "_this call RHS_fnc_BMD4_autoloader;",
            "hitpart": "_this call rhs_fnc_hitSpall",
            "engine": "[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay",
            "getout": "_this call rhs_fnc_hatchAbandon"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers|RHS_DefaultEventhandlers [Indent level: 0],
        "rhs_defaulteventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    "dlc": "RHS_AFRF",
    "category": "Armored",
    "slingloadcargomemorypoints": ["SlingLoadCargo1","SlingLoadCargo2","SlingLoadCargo3","SlingLoadCargo4"],
    "driveoncomponent": ["Track_L","Track_R","Slide"],
    "destrtype": "DestructDefault",
    "accuracy": 0.3,
    "crew": "rhs_vdv_combatcrew",
    "typicalcargo": [],
    "side": 0,
    "faction": "rhs_faction_vdv",
    "drivercansee": "2+4+8",
    "gunnercansee": "2+4+8",
    "commandercansee": "2+4+8",
    "unitinfotype": "RHS_RscInfoSprut",
    "tf_range_api": 35000,
    "incomingmissiledetectionsystem": 0,
    "enablegps": 1,
    "reportownposition": 1,
    "driverdoor": "hatchD",
    "driveraction": "driver_apcwheeled2_out",
    "driverinaction": "rhs_t72_driver",
    "driveropticsmodel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
    "loddriverturnedout": 0,
    "viewdriverinexternal": 1,
    "soundgetin": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1],
    "soundgetout": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1,20],
    "sounddammage": ["",0.562341,1],
    "soundengineonint": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_start",0.707946,1],
    "soundengineonext": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_start",0.630957,1,200],
    "soundengineoffint": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_stop",0.707946,1],
    "soundengineoffext": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_stop",0.630957,1,200],
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
    # Class: CfgVehicles|rhs_a3spruttank_base|Sounds [Indent level: 1],
    "sounds": {
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Idle_ext [Indent level: 2]
        "idle_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_idle",0.707946,1,200],
            "frequency": "0.95	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine [Indent level: 2],
        "engine": {
            "sound": ["|rhsafrf|addons|rhs_bmd|sounds|rhs_bmd_engine.wss",0.794328,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine1_ext [Indent level: 2],
        "engine1_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmd|sounds|rhs_bmd_engine.wss",0.794328,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine2_ext [Indent level: 2],
        "engine2_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmd|sounds|rhs_bmd_engine.wss",0.891251,1,250],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine3_ext [Indent level: 2],
        "engine3_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmd|sounds|rhs_bmd_engine.wss",1,1,300],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine4_ext [Indent level: 2],
        "engine4_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmd|sounds|rhs_bmd_engine.wss",1.12202,1,340],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine5_ext [Indent level: 2],
        "engine5_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmd|sounds|rhs_bmd_engine.wss",1.41254,1,400],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*camPos*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|IdleThrust [Indent level: 2],
        "idlethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_idle",0.891251,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|EngineThrust [Indent level: 2],
        "enginethrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm1",1.12202,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine1_Thrust_ext [Indent level: 2],
        "engine1_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm2",1.25893,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine2_Thrust_ext [Indent level: 2],
        "engine2_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm3",1.41254,1,250],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine3_Thrust_ext [Indent level: 2],
        "engine3_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm4",1.58489,1,350],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine4_Thrust_ext [Indent level: 2],
        "engine4_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm5",1.77828,1,400],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine5_Thrust_ext [Indent level: 2],
        "engine5_thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm6",1.99526,1,450],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Idle_int [Indent level: 2],
        "idle_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_idle",0.316228,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine_int [Indent level: 2],
        "engine_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm1",0.354813,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine1_int [Indent level: 2],
        "engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm2",0.398107,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine2_int [Indent level: 2],
        "engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm3",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine3_int [Indent level: 2],
        "engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm4",0.501187,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine4_int [Indent level: 2],
        "engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm5",0.562341,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine5_int [Indent level: 2],
        "engine5_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm6",0.630957,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|IdleThrust_int [Indent level: 2],
        "idlethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_idle",0.354813,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|EngineThrust_int [Indent level: 2],
        "enginethrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm1",0.398107,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine1_Thrust_int [Indent level: 2],
        "engine1_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm2",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine2_Thrust_int [Indent level: 2],
        "engine2_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm3",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine3_Thrust_int [Indent level: 2],
        "engine3_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm4",0.501187,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine4_Thrust_int [Indent level: 2],
        "engine4_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm5",0.562341,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|Engine5_Thrust_int [Indent level: 2],
        "engine5_thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm6",0.630957,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|NoiseInt [Indent level: 2],
        "noiseint": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_int_1",0.562341,1],
            "frequency": "1",
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 25])"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|NoiseExt [Indent level: 2],
        "noiseext": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_ext_1",0.794328,1,150],
            "frequency": "1",
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 25])"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsOutH0 [Indent level: 2],
        "threadsouth0": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.398107,1,140],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsOutH1 [Indent level: 2],
        "threadsouth1": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.446684,1,160],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsOutH2 [Indent level: 2],
        "threadsouth2": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_3.ogg",0.501187,1,180],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsOutH3 [Indent level: 2],
        "threadsouth3": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_4.ogg",0.562341,1,200],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsOutH4 [Indent level: 2],
        "threadsouth4": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_5.ogg",0.562341,1,220],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsOutS0 [Indent level: 2],
        "threadsouts0": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.316228,1,120],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsOutS1 [Indent level: 2],
        "threadsouts1": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.354813,1,140],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsOutS2 [Indent level: 2],
        "threadsouts2": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_3.ogg",0.398107,1,160],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsOutS3 [Indent level: 2],
        "threadsouts3": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_4.ogg",0.446684,1,180],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsOutS4 [Indent level: 2],
        "threadsouts4": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_5.ogg",0.501187,1,200],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsInH0 [Indent level: 2],
        "threadsinh0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_01",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsInH1 [Indent level: 2],
        "threadsinh1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_02",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsInH2 [Indent level: 2],
        "threadsinh2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_03",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsInH3 [Indent level: 2],
        "threadsinh3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_04",0.501187,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsInH4 [Indent level: 2],
        "threadsinh4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_05",0.562341,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsInS0 [Indent level: 2],
        "threadsins0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_01",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsInS1 [Indent level: 2],
        "threadsins1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_02",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsInS2 [Indent level: 2],
        "threadsins2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_03",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsInS3 [Indent level: 2],
        "threadsins3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_04",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Sounds|ThreadsInS4 [Indent level: 2],
        "threadsins4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_05",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        }
    },
    "tracksspeed": 1.35,
    "wheelcircumference": 2.01,
    "attenuationeffecttype": "TankAttenuation",
    "cost": 1.5e+006,
    "armor": 200,
    "armorstructural": 500,
    "damageresistance": 0.02,
    "crewvulnerable": 0,
    "texturelist": [],
    "smokelaunchergrenadecount": 3,
    "smokelaunchervelocity": 17,
    "smokelauncheronturret": 1,
    "smokelauncherangle": 60,
    # Class: CfgVehicles|rhs_a3spruttank_base|ViewOptics [Indent level: 1],
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
    # Class: CfgVehicles|rhs_a3spruttank_base|Reflectors [Indent level: 1],
    "reflectors": {
        # Class: CfgVehicles|rhs_a3spruttank_base|Reflectors|Driver_FG125_Cover [Indent level: 2]
        "driver_fg125_cover": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerangle": 35,
            "outerangle": 75,
            "conefadecoef": 5,
            "intensity": 15,
            "useflare": 0,
            "daylight": 1,
            "flaresize": 0.85,
            # Class: CfgVehicles|rhs_a3spruttank_base|Reflectors|Driver_FG125_Cover|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.2,
                "hardlimitstart": 130,
                "hardlimitend": 160
            }
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Reflectors|Driver_FG125_Cover_Flare [Indent level: 2],
        "driver_fg125_cover_flare": {
            "intensity": 5,
            "innerangle": 55,
            "outerangle": 155,
            "flaresize": 0.3,
            "useflare": 1,
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "conefadecoef": 5,
            "daylight": 1,
            # Class: CfgVehicles|rhs_a3spruttank_base|Reflectors|Driver_FG125_Cover|Attenuation [Indent level: 3],
            "attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.2,
                "hardlimitstart": 130,
                "hardlimitend": 160
            }
        }
    },
    "aggregatereflectors": [["Driver_FG125_Cover","Driver_FG125_Cover_Flare"]],
    "armorlights": 0.1,
    # Class: CfgVehicles|rhs_a3spruttank_base|Components [Indent level: 1],
    "components": {
        # Class: CfgVehicles|rhs_a3spruttank_base|Components|VehicleSystemsDisplayManagerComponentLeft [Indent level: 2]
        "vehiclesystemsdisplaymanagercomponentleft": {
            # Class: CfgVehicles|rhs_a3spruttank_base|Components|VehicleSystemsDisplayManagerComponentLeft|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_a3spruttank_base|Components|VehicleSystemsDisplayManagerComponentLeft|CrewDisplay [Indent level: 3],
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles|rhs_a3spruttank_base|Components|VehicleSystemsDisplayManagerComponentRight [Indent level: 2],
        "vehiclesystemsdisplaymanagercomponentright": {
            # Class: CfgVehicles|rhs_a3spruttank_base|Components|VehicleSystemsDisplayManagerComponentRight|EmptyDisplay [Indent level: 3]
            "emptydisplay": {
                "componenttype": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles|rhs_a3spruttank_base|Components|VehicleSystemsDisplayManagerComponentRight|CrewDisplay [Indent level: 3],
            "crewdisplay": {
                "componenttype": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
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
    "_generalmacro": "Tank_F",
    "occludesoundswhenin": 0,
    "obstructsoundswhenin": 0,
    "getinaction": "GetInMedium",
    "getoutaction": "GetOutMedium",
    "cargogetinaction": ["GetInLow"],
    "cargogetoutaction": ["GetOutLow"],
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
    "irscanground": 2,
    "irscanrangemax": 0,
    "irscanrangemin": 0,
    "irscantoeyefactor": 1,
    "enableradio": 1,
    "lockdetectionsystem": 0,
    "countermeasureactivationradius": 2000,
    "soundincommingmissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_3",0.316228,1],
    "memorypointcargolight": "cargo light",
    "dampersbumpcoef": 4.5,
    "explosionshielding": 1,
    "mintotaldamagethreshold": 0.005,
    "crewcrashprotection": 0.25,
    "crewexplosionprotection": 0.9995,
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
    "viewcargoshadow": 1,
    "viewcargoshadowdiff": 0.05,
    "viewcargoshadowamb": 0.5,
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
    "driverforceoptics": 1,
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
    "selectionfireanim": "zasleh",
    "bounding": "usti hlavne",
    "firedusteffect": "FDustEffects",
    "gearbox": [-7,0,11,8,5.7,4.2],
    "alphatracks": 0.7,
    "texturetrackwheel": 0,
    "memorypointtrack1l": "Stopa LL",
    "memorypointtrack1r": "Stopa LR",
    "memorypointtrack2l": "Stopa RL",
    "memorypointtrack2r": "Stopa RR",
    "extcameraposition": [0,1.5,-9],
    # Class: CfgVehicles|Tank|ViewPilot [Indent level: 1],
    "viewpilot": {
        "initanglex": 7,
        "initangley": 0,
        "initfov": 0.75,
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
    "predictturnsimul": 1.2,
    "predictturnplan": 1,
    "soundgear": ["",0.000316228,1],
    "outsidesoundfilter": 1,
    "nightvision": 0,
    "formationx": 20,
    "formationz": 30,
    "maxspeed": 80,
    "type": 1,
    "threat": [0.7,1,0.3],
    "camouflage": 8,
    "driveropticscolor": [1,1,1,1],
    # Class: CfgVehicles|Tank|CargoLight [Indent level: 1],
    "cargolight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
    "memorypointtaskmarkeroffset": [0,0.3,0],
    "rightdusteffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffectsBig"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffectsBig"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffectsBig"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffectsBig"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffectsBig"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffectsBig"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassEffectsDryBig"],["GdtStratisDryGrass","RDirtEffectsBig"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffectsBig"],["GdtStratisGreenGrass","RDirtEffectsBig"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffectsBig"],["GdtStratisRocky","RDirtEffectsBig"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffectsBig"],["GdtStratisThistles","RDirtEffectsBig"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffectsBig"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffectsBig"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffectsBig"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffectsBig"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffectsBig"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffectsBig"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffectsBig"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RDirtEffectsBig"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RDirtEffectsBig"],["GdtDesert1","RStonesEffectsBig"],["GdtDesert2","RDustEffects"],["GdtDesert2","RGrassEffectsBig"],["GdtDesert2","RDirtEffectsBig"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffectsBig"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffectsBig"],["GdtGrassGreen","RDirtEffectsBig"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassEffectsDryBig"],["GdtGrassDry","RDirtEffectsBig"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffectsBig"],["GdtGrassWild","RDirtEffectsBig"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffectsBig"],["GdtWildField","RDirtEffectsBig"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffectsBig"],["GdtWeed1","RDirtEffectsBig"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffectsBig"],["GdtWeed2","RDirtEffectsBig"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffectsBig"],["GdtThorn","RDirtEffectsBig"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffectsBig"],["GdtStony","RDirtEffectsBig"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffectsBig"],["GdtStonyGreen","RDirtEffectsBig"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffectsBig"],["GdtStonyThistle","RDirtEffectsBig"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftdusteffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffectsBig"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffectsBig"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffectsBig"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffectsBig"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffectsBig"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffectsBig"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassEffectsDryBig"],["GdtStratisDryGrass","LDirtEffectsBig"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffectsBig"],["GdtStratisGreenGrass","LDirtEffectsBig"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffectsBig"],["GdtStratisRocky","LDirtEffectsBig"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffectsBig"],["GdtStratisThistles","LDirtEffectsBig"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffectsBig"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffectsBig"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffectsBig"],["GdtRubble","LDirtEffectsBig"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffectsBig"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffectsBig"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffectsBig"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffectsBig"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LDirtEffectsBig"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LDirtEffectsBig"],["GdtDesert1","LStonesEffectsBig"],["GdtDesert2","LDustEffects"],["GdtDesert2","LGrassEffectsBig"],["GdtDesert2","LDirtEffectsBig"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffectsBig"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffectsBig"],["GdtGrassGreen","LDirtEffectsBig"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassEffectsDryBig"],["GdtGrassDry","LDirtEffectsBig"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffectsBig"],["GdtGrassWild","LDirtEffectsBig"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffectsBig"],["GdtWildField","LDirtEffectsBig"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffectsBig"],["GdtWeed1","LDirtEffectsBig"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffectsBig"],["GdtWeed2","LDirtEffectsBig"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffectsBig"],["GdtThorn","LDirtEffectsBig"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffectsBig"],["GdtStony","LDirtEffectsBig"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffectsBig"],["GdtStonyGreen","LDirtEffectsBig"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffectsBig"],["GdtStonyThistle","LDirtEffectsBig"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","RDustEffects"]],
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
    "headgforceleaningfactor": [0.0075,0.005,0.0075],
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
    "memorypointtaskmarker": "",
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
    # Class: CfgVehicles|AllVehicles|MFD [Indent level: 1],
    "mfd": {
    },
    # Class: CfgVehicles|AllVehicles|SoundEvents [Indent level: 1],
    "soundevents": {
    },
    # Class: CfgVehicles|AllVehicles|RenderTargets [Indent level: 1],
    "rendertargets": {
    },
    "cargoproxyindexes": [],
    "driverlefthandanimname": "",
    "driverrighthandanimname": "",
    "driverleftleganimname": "",
    "driverrightleganimname": "",
    "cargodoors": [],
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
    "insidesoundcoef": 0.5,
    "obstructsoundlfratio": 0,
    "occludesoundlfratio": 0.25,
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
    "irtarget": 1,
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
    "radartype": 0,
    "limitedspeedcoef": 0.22,
    "hasdriver": 1,
    "hideweaponsdriver": 1,
    "hideweaponscargo": 0,
    "enablewatch": 0,
    "useprecisegetinaction": 0,
    "allowtablock": 1,
    "showalltargets": 0,
    "dustfrontleftpos": "dustFrontLeft",
    "dustfrontrightpos": "dustFrontRight",
    "dustbackleftpos": "dustBackLeft",
    "dustbackrightpos": "dustBackRight",
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
    "soundbushcrash": ["emptySound",0],
    "soundlocked": ["",1,1],
    "cargoiscodriver": [0],
    "drivercompartments": "Compartment1",
    "driveropticseffect": [],
    "forcehidedriver": 0,
    "canhidedriver": -1,
    "castdrivershadow": 0,
    "castcargoshadow": 0,
    "viewdrivershadow": 1,
    "viewdrivershadowdiff": 1,
    "viewdrivershadowamb": 1,
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
    "soundturnin": ["",0.000316228,1],
    "soundturnout": ["",0.000316228,1],
    "soundturnininternal": ["",0.000316228,1],
    "soundturnoutinternal": ["",0.000316228,1],
    "features": "",
    "insidedetectcoef": 0.05,
}