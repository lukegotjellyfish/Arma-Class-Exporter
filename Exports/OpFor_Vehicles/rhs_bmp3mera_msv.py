rhs_bmp3mera_msv = {
    "editorPreview": "rhsafrf|addons|rhs_editorPreviews|data|rhs_bmp3mera_msv.paa",
    "author": "Red Hammer Studios",
    "model": "rhsafrf|addons|rhs_bmp3|bmp3m_era",
    "scope": 2,
    "displayName": "BMP-3 (Vesna-K/A)",
    # Class: CfgVehicles\rhs_bmp3mera_msv\HitPoints,
    "HitPoints": {
        # Class: CfgVehicles\rhs_bmp3mera_msv\HitPoints\Armor_Composite_50
        "Armor_Composite_50": {
            "armor": 999,
            "material": -1,
            "name": "Armor_CE_50_Hit",
            "armorComponent": "Armor_CE_50",
            "simulation": "RHS_Composite_50",
            "passThrough": 0,
            "minimalHit": 1,
            "explosionShielding": 0,
            "radius": 0.001,
            "visual": "-"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitHull,
        "HitHull": {
            "armor": 0.4,
            "material": -1,
            "name": "telo",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.44,
            "explosionShielding": 0.5,
            "radius": 0.15
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitEngine,
        "HitEngine": {
            "armor": 0.25,
            "material": -1,
            "name": "motor",
            "visual": "zbytek",
            "passThrough": 0,
            "minimalHit": 0.069,
            "explosionShielding": 0.009,
            "radius": 0.17,
            # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitEngine\DestructionEffects,
            "DestructionEffects": {
                "ammoExplosionEffect": "",
                # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke,
                "RHS_Engine_Smoke": {
                    "simulation": "particles",
                    "type": "SmallWreckSmoke",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Fire,
                "RHS_Engine_Fire": {
                    "type": "SmallFireFPlace",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sparks,
                "RHS_Engine_Sparks": {
                    "type": "RHS_FireSparks",
                    "simulation": "particles",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Sounds,
                "RHS_Engine_Sounds": {
                    "simulation": "sound",
                    "type": "Fire",
                    "position": "engine_smoke1",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small1,
                "RHS_Engine_Smoke_small1": {
                    "type": "WeaponWreckSmoke",
                    "position": "engine_smoke2",
                    "simulation": "particles",
                    "intensity": 0.5,
                    "interval": 1,
                    "lifeTime": 60
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitEngine\DestructionEffects\RHS_Engine_Smoke_small2,
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
        # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitLTrack,
        "HitLTrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_L",
            "passThrough": 0,
            "minimalHit": -0.25,
            "explosionShielding": 0.15,
            "radius": 0.3,
            "visual": "pas_L"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitRTrack,
        "HitRTrack": {
            "armor": -150,
            "material": -1,
            "name": "pas_P",
            "passThrough": 0,
            "minimalHit": -0.25,
            "explosionShielding": 0.15,
            "radius": 0.3,
            "visual": "pas_P"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\HitPoints\HitFuel,
        "HitFuel": {
            "armor": 1.2,
            "explosionShielding": 0.001,
            "material": -1,
            "passThrough": 0,
            "name": "palivo",
            "visual": "-",
            "radius": 0.05
        }
    },
    "hiddenSelections": ["camo1","camo2","camo3","camo4","camo5","n1","n2","n3","i1","f1","f2","f3","f4","f5","f6","f7","f8","f9"],
    "hiddenSelectionsTextures": ["rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_01_3mera_co.paa","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_02_3mera_co.paa","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_03_3m_co.paa","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_04_co.paa","rhsafrf|addons|rhs_bmp3|data|3m_era_co.paa"],
    # Class: CfgVehicles\rhs_bmp3mera_msv\textureSources,
    "textureSources": {
        # Class: CfgVehicles\rhs_bmp3mera_msv\textureSources\standard
        "standard": {
            "author": "Red Hammer Studios",
            "textures": ["rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_01_3mera_co.paa","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_02_3mera_co.paa","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_03_3m_co.paa","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_04_co.paa","rhsafrf|addons|rhs_bmp3|data|3m_era_co.paa"],
            "displayName": "Standard",
            "factions": []
        },
        # Class: CfgVehicles\rhs_bmp3mera_msv\textureSources\rhs_sand,
        "rhs_sand": {
            "textures": ["rhsafrf|addons|rhs_bmp3_camo|data|rhs_bmp3_01_3mera_sand_co.paa","rhsafrf|addons|rhs_bmp3_camo|data|rhs_bmp3_02_3mera_sand_co.paa","rhsafrf|addons|rhs_bmp3_camo|data|rhs_bmp3_03_3m_sand_co.paa","rhsafrf|addons|rhs_bmp3_camo|data|rhs_bmp3_04_sand_co.paa","rhsafrf|addons|rhs_bmp3_camo|data|3m_era_sand_co.paa"],
            "displayName": "Sand",
            "author": "Red Hammer Studios",
            "factions": []
        }
    },
    "unitInfoType": "RHS_RscInfoBMP3M",
    "crew": "rhs_msv_emr_crew",
    "enableGPS": 1,
    "reportOwnPosition": 1,
    "enginePower": 478,
    "peakTorque": 1650,
    "torqueCurve": [[0,0],[0.228896,0.649091],[0.4,0.892121],[0.519156,1],[0.657143,0.992727],[0.813961,0.970303],[0.942857,0.952121],[1.05,0]],
    # Class: CfgVehicles\rhs_bmp3m_msv\Wheels,
    "Wheels": {
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\L2
        "L2": {
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "boneName": "wheel_podkoloL1",
            "center": "wheel_1_2_axis",
            "boundary": "wheel_1_2_bound",
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\L3,
        "L3": {
            "boneName": "wheel_podkolol2",
            "center": "wheel_1_3_axis",
            "boundary": "wheel_1_3_bound",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\L4,
        "L4": {
            "boneName": "wheel_podkolol3",
            "center": "wheel_1_4_axis",
            "boundary": "wheel_1_4_bound",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\L5,
        "L5": {
            "boneName": "wheel_podkolol4",
            "center": "wheel_1_5_axis",
            "boundary": "wheel_1_5_bound",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\L6,
        "L6": {
            "boneName": "wheel_podkolol5",
            "center": "wheel_1_6_axis",
            "boundary": "wheel_1_6_bound",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\L7,
        "L7": {
            "boneName": "wheel_podkolol6",
            "center": "wheel_1_7_axis",
            "boundary": "wheel_1_7_bound",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\L9,
        "L9": {
            "boneName": "wheel_podkolol9",
            "center": "wheel_1_9_axis",
            "boundary": "wheel_1_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\L1,
        "L1": {
            "boneName": "",
            "center": "wheel_1_1_axis",
            "boundary": "wheel_1_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "side": "left",
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\R2,
        "R2": {
            "boneName": "wheel_podkolop1",
            "center": "wheel_2_2_axis",
            "boundary": "wheel_2_2_bound",
            "side": "right",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\R3,
        "R3": {
            "boneName": "wheel_podkolop2",
            "center": "wheel_2_3_axis",
            "boundary": "wheel_2_3_bound",
            "side": "right",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\R4,
        "R4": {
            "boneName": "wheel_podkolop3",
            "center": "wheel_2_4_axis",
            "boundary": "wheel_2_4_bound",
            "side": "right",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\R5,
        "R5": {
            "boneName": "wheel_podkolop4",
            "center": "wheel_2_5_axis",
            "boundary": "wheel_2_5_bound",
            "side": "right",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\R6,
        "R6": {
            "boneName": "wheel_podkolop5",
            "center": "wheel_2_6_axis",
            "boundary": "wheel_2_6_bound",
            "side": "right",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\R7,
        "R7": {
            "boneName": "wheel_podkolop6",
            "center": "wheel_2_7_axis",
            "boundary": "wheel_2_7_bound",
            "side": "right",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "maxDroop": 0.18,
            "maxCompression": 0.18,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\R9,
        "R9": {
            "boneName": "wheel_podkolop9",
            "center": "wheel_2_9_axis",
            "boundary": "wheel_2_9_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "side": "right",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Wheels\R1,
        "R1": {
            "boneName": "",
            "center": "wheel_2_1_axis",
            "boundary": "wheel_2_1_bound",
            "maxDroop": 0,
            "maxCompression": 0,
            "side": "right",
            "dampingRate": 1034,
            "dampingRateInAir": 1034,
            "suspTravelDirection": [-0.125,-1,0],
            "steering": 0,
            "width": 0.315,
            "mass": 120,
            "MOI": 7.5615,
            "maxBrakeTorque": 4000,
            "sprungMass": 1333.33,
            "springStrength": 127500,
            "springDamperRate": 11000,
            "dampingRateDamaged": 10,
            "dampingRateDestroyed": 10000,
            "latStiffX": 3,
            "latStiffY": 40,
            "longitudinalStiffnessPerUnitGravity": 32000,
            "frictionVsSlipGraph": [[0,0.65],[0.18,1],[0.7,0.95]]
        }
    },
    # Class: CfgVehicles\rhs_bmp3m_msv\Turrets,
    "Turrets": {
        # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret
        "MainTurret": {
            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets
            "Turrets": {
                # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics
                "CommanderOptics": {
                    "gunnerType": "rhs_msv_emr_crew_commander",
                    # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components,
                    "Components": {
                        # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft
                        "VehicleSystemsDisplayManagerComponentLeft": {
                            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\EmptyDisplay
                            "EmptyDisplay": {
                                "componentType": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\CrewDisplay,
                            "CrewDisplay": {
                                "componentType": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            },
                            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\MinimapDisplay,
                            "MinimapDisplay": {
                                "componentType": "MinimapDisplayComponent",
                                "resource": "RscCustomInfoMiniMap"
                            },
                            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentLeft\VehiclePrimaryGunnerDisplay,
                            "VehiclePrimaryGunnerDisplay": {
                                "componentType": "TransportFeedDisplayComponent",
                                "source": "PrimaryGunner"
                            }
                        },
                        # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight,
                        "VehicleSystemsDisplayManagerComponentRight": {
                            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\EmptyDisplay
                            "EmptyDisplay": {
                                "componentType": "EmptyDisplayComponent"
                            },
                            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\CrewDisplay,
                            "CrewDisplay": {
                                "componentType": "CrewDisplayComponent",
                                "resource": "RscCustomInfoCrew"
                            },
                            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\MinimapDisplay,
                            "MinimapDisplay": {
                                "componentType": "MinimapDisplayComponent",
                                "resource": "RscCustomInfoMiniMap"
                            },
                            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Turrets\CommanderOptics\Components\VehicleSystemsDisplayManagerComponentRight\VehiclePrimaryGunnerDisplay,
                            "VehiclePrimaryGunnerDisplay": {
                                "componentType": "TransportFeedDisplayComponent",
                                "source": "PrimaryGunner"
                            }
                        }
                    },
                    "gunnerDoor": "hatchC",
                    "body": "obsTurret",
                    "gun": "obsGun",
                    "commanding": 4,
                    "primaryObserver": 1,
                    "animationSourceBody": "obsTurret",
                    "animationSourceGun": "obsGun",
                    "maxHorizontalRotSpeed": 1.8,
                    "maxVerticalRotSpeed": 1.8,
                    "stabilizedInAxes": 3,
                    "minElev": -5,
                    "maxElev": 60,
                    "initElev": 0,
                    "minTurn": -360,
                    "maxTurn": 360,
                    "initTurn": 0,
                    "soundServo": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",3.16228,1,30],
                    "soundServoVertical": ["A3|Sounds_F|vehicles|armor|APC|noises|servo_APC_comm",3.16228,1,30],
                    "memoryPointGun": "usti hlavne3",
                    "gunBeg": "usti hlavne3",
                    "gunEnd": "konec hlavne3",
                    "turretInfoType": "RHS_RscWeaponTKN3_FCS",
                    "discreteDistance": [],
                    "discreteDistanceInitIndex": 0,
                    "canUseScanners": 0,
                    "allowTabLock": 0,
                    "memoryPointGunnerOutOptics": "commanderview",
                    "memoryPointGunnerOptics": "commanderview",
                    "gunnerOutOpticsModel": "",
                    "gunnerOpticsEffect": [],
                    "gunnerHasFlares": 1,
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Turrets\CommanderOptics\ViewGunner,
                    "ViewGunner": {
                        "initAngleX": 5,
                        "minAngleX": -65,
                        "maxAngleX": 85,
                        "initAngleY": 0,
                        "minAngleY": -150,
                        "maxAngleY": 150,
                        "initFov": 0.7,
                        "minFov": 0.25,
                        "maxFov": 1.1
                    },
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Turrets\CommanderOptics\ViewOptics,
                    "ViewOptics": {
                        "initAngleX": 0,
                        "minAngleX": -30,
                        "maxAngleX": 30,
                        "initAngleY": 0,
                        "minAngleY": -100,
                        "maxAngleY": 100,
                        "initFov": 0.101,
                        "minFov": 0.102,
                        "maxFov": 0.102,
                        "visionMode": ["Normal"],
                        "minMoveX": 0,
                        "maxMoveX": 0,
                        "minMoveY": 0,
                        "maxMoveY": 0,
                        "minMoveZ": 0,
                        "maxMoveZ": 0,
                        "speedZoomMaxSpeed": 1e+010,
                        "speedZoomMaxFOV": 0
                    },
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn,
                    "OpticsIn": {
                        # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Wide
                        "Wide": {
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3.p3d",
                            "initFov": 0.14,
                            "minFov": 0.14,
                            "maxFov": 0.14,
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "visionMode": ["Normal"],
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        },
                        # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\PZU,
                        "PZU": {
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_pzu3.p3d",
                            "initFov": 0.175,
                            "minFov": 0.175,
                            "maxFov": 0.175,
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "visionMode": ["Normal"],
                            "minMoveX": 0,
                            "maxMoveX": 0,
                            "minMoveY": 0,
                            "maxMoveY": 0,
                            "minMoveZ": 0,
                            "maxMoveZ": 0,
                            "speedZoomMaxSpeed": 1e+010,
                            "speedZoomMaxFOV": 0
                        },
                        # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Night,
                        "Night": {
                            "initFov": 0.166667,
                            "minFov": 0.166667,
                            "maxFov": 0.166667,
                            "visionMode": ["NVG"],
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tkn3_night.p3d",
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
                        # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Turrets\CommanderOptics\OpticsIn\Periscope,
                        "Periscope": {
                            "initAngleX": 0,
                            "minAngleX": -30,
                            "maxAngleX": 30,
                            "initAngleY": 0,
                            "minAngleY": -100,
                            "maxAngleY": 100,
                            "initFov": 0.26,
                            "minFov": 0.26,
                            "maxFov": 0.26,
                            "visionMode": ["Normal"],
                            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
                            "gunnerOpticsEffect": ["TankGunnerOptics1","OpticsBlur2","OpticsCHAbera2"],
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
                    "gunnerAction": "rhs_bmp3_commanderOut",
                    "gunnerInAction": "rhs_bmp3_commander",
                    "gunnerGetInAction": "GetInHigh",
                    "gunnerGetOutAction": "GetOutHigh",
                    "startEngine": 0,
                    "viewGunnerInExternal": 1,
                    "outGunnerMayFire": 1,
                    "inGunnerMayFire": 1,
                    "gunnerForceOptics": 0,
                    "LodOpticsIn": 0,
                    "LodOpticsOut": 0,
                    "usePiP": 2,
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints,
                    "HitPoints": {
                        # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitTurretCom
                        "HitTurretCom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "vezVelitele",
                            "visual": "vezVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.03,
                            "explosionShielding": 0.6,
                            "radius": 0.15,
                            "isTurret": 1
                        },
                        # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Turrets\CommanderOptics\HitPoints\HitGunCom,
                        "HitGunCom": {
                            "armor": 0.3,
                            "material": -1,
                            "name": "zbranVelitele",
                            "visual": "zbranVelitele",
                            "passThrough": 0,
                            "minimalHit": 0.03,
                            "explosionShielding": 0.6,
                            "radius": 0.15,
                            "isGun": 1
                        }
                    },
                    "selectionFireAnim": "",
                    "proxyType": "CPCommander",
                    "proxyIndex": 1,
                    "gunnerName": "Commander",
                    "primaryGunner": 0,
                    "animationSourceHatch": "hatchCommander",
                    "animationSourceCamElev": "camElev",
                    "gunnerOpticsModel": "A3|weapons_f|reticle|Optics_Commander_02_F",
                    "gunnerOutOpticsColor": [0,0,0,1],
                    "gunnerOutForceOptics": 0,
                    "gunnerOutOpticsShowCursor": 0,
                    "gunnerOutOpticsEffect": [],
                    "memoryPointsGetInGunner": "pos commander",
                    "memoryPointsGetInGunnerDir": "pos commander dir",
                    "weapons": [],
                    "magazines": [],
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
                    "primary": 1,
                    "hasGunner": 1,
                    "turretCanSee": 0,
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
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
                    "forceNVG": 0,
                    "isCopilot": 0,
                    "canEject": 1,
                    "gunnerLeftHandAnimName": "",
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
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurnIn,
                    "TurnIn": {
                        "turnOffset": 0
                    },
                    # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
                    "TurnOut": {
                        "turnOffset": 0
                    },
                    "showCrewAim": 0
                }
            },
            "magazines": ["rhs_mag_3UOF191_22","rhs_mag_9m117m1_8","rhs_mag_3uof8_305","rhs_mag_3ubr11_195","rhs_mag_762x54mm_2000","rhs_mag_3d17_6","rhs_laserfcsmag","rhs_laserfcsmag"],
            "turretInfoType": "RHS_RscWeaponESSA_FCS",
            "discreteDistance": [],
            "discreteDistanceInitIndex": 0,
            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\OpticsIn,
            "OpticsIn": {
                # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\OpticsIn\Wide
                "Wide": {
                    "opticsDisplayName": "DAY3",
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "initFov": 0.233333,
                    "minFov": 0.233333,
                    "maxFov": 0.233333,
                    "visionMode": ["Normal","Ti"],
                    "thermalMode": [0,1],
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\OpticsIn\Medium,
                "Medium": {
                    "opticsDisplayName": "DAY12",
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
                    "thermalMode": [0,1],
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\OpticsIn\Narrow,
                "Narrow": {
                    "opticsDisplayName": "DAY24",
                    "initFov": 0.0291667,
                    "minFov": 0.0291667,
                    "maxFov": 0.0291667,
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "visionMode": ["Normal","Ti"],
                    "thermalMode": [0,1],
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
                    "minMoveX": 0,
                    "maxMoveX": 0,
                    "minMoveY": 0,
                    "maxMoveY": 0,
                    "minMoveZ": 0,
                    "maxMoveZ": 0,
                    "speedZoomMaxSpeed": 1e+010,
                    "speedZoomMaxFOV": 0
                },
                # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\OpticsIn\Narrow2,
                "Narrow2": {
                    "opticsDisplayName": "AUTOTRACK",
                    "directionStabilized": 1,
                    "initFov": 0.0291667,
                    "minFov": 0.0291667,
                    "maxFov": 0.0291667,
                    "initAngleX": 0,
                    "minAngleX": -30,
                    "maxAngleX": 30,
                    "initAngleY": 0,
                    "minAngleY": -100,
                    "maxAngleY": 100,
                    "visionMode": ["Normal","Ti"],
                    "thermalMode": [0,1],
                    "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_thermalscreen_empty.p3d",
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
            # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Components,
            "Components": {
                # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\EmptyDisplay
                    "EmptyDisplay": {
                        "componentType": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentLeft\CrewDisplay,
                    "CrewDisplay": {
                        "componentType": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                },
                # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\EmptyDisplay
                    "EmptyDisplay": {
                        "componentType": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\MainTurret\Components\VehicleSystemsDisplayManagerComponentRight\CrewDisplay,
                    "CrewDisplay": {
                        "componentType": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                }
            },
            "gunnerDoor": "hatchG",
            "memoryPointGun": "usti hlavne2",
            "selectionFireAnim": "zasleh2",
            "gunBeg": "usti hlavne",
            "gunEnd": "konec hlavne",
            "weapons": ["rhs_weap_2a70","rhs_weap_2a72","rhs_weap_pkt_bmd_coax","rhs_weap_902a","rhs_weap_fcs"],
            "animationSourceStickX": "joystick_gunner_X",
            "animationSourceStickY": "joystick_gunner_Y",
            "gunnerLeftHandAnimName": "joystick_gunner_Y",
            "gunnerRightHandAnimName": "joystick_gunner_Y",
            "maxHorizontalRotSpeed": 0.55,
            "maxVerticalRotSpeed": 0.55,
            "minElev": -5,
            "maxElev": 60,
            "initElev": 10,
            "startEngine": 0,
            "soundServo": ["A3|Sounds_F|vehicles|armor|noises|servo_best",1,1,50],
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\TurnIn,
            "TurnIn": {
                "limitsArrayTop": [[60,-180],[60,180]],
                "limitsArrayBottom": [[-2.1,-180],[-1.9,-134.687],[-4.7683,-133.687],[-5,0],[-4.7173,133.637],[-1.9,134.687],[-2.1,180]]
            },
            "canUseScanners": 0,
            "allowTabLock": 0,
            "memoryPointGunnerOptics": "gunnerview",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsEffect": [],
            "gunnerOpticsEffect": [],
            "gunnerForceOptics": 0,
            "gunnerAction": "rhs_bmp3_gunnerOut",
            "gunnerInAction": "rhs_bmp3_gunner",
            "forceHideGunner": 0,
            "inGunnerMayFire": 1,
            "viewGunnerInExternal": 1,
            "LodOpticsIn": 0,
            "LodOpticsOut": 0,
            "usePiP": 2,
            "headAimDown": 15,
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Reflectors,
            "Reflectors": {
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Reflectors\Searchlight_FG125
                "Searchlight_FG125": {
                    "color": [1900,1300,950],
                    "ambient": [5,5,5],
                    "position": "Light_FG125",
                    "direction": "Light_FG125_end",
                    "hitpoint": "Light_FG125",
                    "selection": "Light_FG125",
                    "size": 1,
                    "innerAngle": 8,
                    "outerAngle": 15,
                    "coneFadeCoef": 1,
                    "intensity": 45,
                    "useFlare": 1,
                    "dayLight": 1,
                    "flareSize": 0.85,
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Reflectors\Searchlight_FG125\Attenuation,
                    "Attenuation": {
                        "start": 1,
                        "constant": 0,
                        "linear": 0,
                        "quadratic": 0.02,
                        "hardLimitStart": 630,
                        "hardLimitEnd": 660
                    }
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Reflectors\Searchlight_FG125_Flare,
                "Searchlight_FG125_Flare": {
                    "color": [7,6,6.5],
                    "ambient": [22,22,22],
                    "position": "Light_FG125",
                    "direction": "Light_FG125_end",
                    "hitpoint": "Light_FG125",
                    "selection": "Light_FG125",
                    "size": 1,
                    "innerAngle": 30,
                    "outerAngle": 175,
                    "coneFadeCoef": 10,
                    "intensity": 100,
                    "useFlare": 1,
                    "dayLight": 0,
                    "flareSize": 1.85,
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\Reflectors\Searchlight_FG125_Flare\Attenuation,
                    "Attenuation": {
                        "start": 0,
                        "constant": 0,
                        "linear": 0,
                        "quadratic": 10,
                        "hardLimitStart": 0,
                        "hardLimitEnd": 0.9
                    }
                }
            },
            "armorLights": 0.1,
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\ViewGunner,
            "ViewGunner": {
                "initAngleX": -15,
                "minAngleX": -65,
                "maxAngleX": 85,
                "initAngleY": -5,
                "minAngleY": -150,
                "maxAngleY": 150,
                "initFov": 0.7,
                "minFov": 0.25,
                "maxFov": 1.1
            },
            "commanding": 2,
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\HitPoints,
            "HitPoints": {
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\HitPoints\HitTurret
                "HitTurret": {
                    "armor": 0.5,
                    "material": -1,
                    "name": "vez",
                    "visual": "vez",
                    "passThrough": 0,
                    "minimalHit": 0.14,
                    "explosionShielding": 0.001,
                    "radius": 0.25,
                    "isTurret": 1
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\MainTurret\HitPoints\HitGun,
                "HitGun": {
                    "armor": 0.6,
                    "material": -1,
                    "name": "zbran",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": 0.13,
                    "explosionShielding": 0.001,
                    "radius": 0.25,
                    "isGun": 1
                }
            },
            "gunnerOpticsModel": "A3|weapons_f|reticle|optics_empty",
            "memoryPointsGetInGunner": "pos gunner",
            "memoryPointsGetInGunnerDir": "pos gunner dir",
            "gunnerGetInAction": "GetInHigh",
            "gunnerGetOutAction": "GetOutHigh",
            "primaryGunner": 1,
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
            "stabilizedInAxes": 3,
            "primary": 1,
            "hasGunner": 1,
            "turretCanSee": 0,
            # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
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
            "viewGunnerShadowDiff": 1,
            "viewGunnerShadowAmb": 1,
            "ejectDeadGunner": 0,
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "outGunnerMayFire": 0,
            "showHMD": 0,
            "lockWhenDriverOut": 0,
            "lockWhenVehicleSpeed": -1,
            "gunnerCompartments": "Compartment1",
            "LODTurnedIn": -1,
            "LODTurnedOut": -1,
            "memoryPointsGetInGunnerPrecise": "",
            "missileBeg": "spice rakety",
            "missileEnd": "konec rakety",
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
            # Class: CfgVehicles\AllVehicles\NewTurret\TurnOut,
            "TurnOut": {
                "turnOffset": 0
            },
            "showCrewAim": 0
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\GPMGTurret1,
        "GPMGTurret1": {
            "gunnerDoor": "hatchRA",
            "animationSourceHatch": "hatchR",
            "proxyIndex": 8,
            "body": "obsTurret2",
            "gun": "obsGun2",
            "animationSourceBody": "obsTurret2",
            "animationSourceGun": "obsGun2",
            "selectionFireAnim": "zasleh3",
            "gunnerName": "Right Hull Gunner",
            "hasGunner": 1,
            "gunnerType": "rhs_msv_rifleman",
            "isPersonTurret": 1,
            "showAsCargo": 1,
            "proxyType": "CPCargo",
            "personTurretAction": "vehicle_turnout_1",
            "minOutElev": -10,
            "maxOutElev": 15,
            "initOutElev": 0,
            "minOutTurn": -100,
            "maxOutTurn": 120,
            "initOutTurn": 0,
            "usePip": 1,
            "dontCreateAI": 1,
            "forceHideGunner": 0,
            "primaryObserver": 0,
            "primaryGunner": 0,
            "commanding": 0,
            "LodOpticsIn": 0,
            "LodOpticsOut": 0,
            "minElev": -24,
            "maxElev": 35,
            "minTurn": -10,
            "maxTurn": 10,
            "weapons": ["rhs_weap_pkt_bmd_bow1"],
            "magazines": ["rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250"],
            "ejectDeadGunner": 0,
            "gunBeg": "muzzle2",
            "gunEnd": "end2",
            "memoryPointGun": "memoryPointGun2",
            "memoryPointGunnerOptics": "gunnerview3",
            "memoryPointsGetInGunner": "pos cargo R",
            "memoryPointsGetInGunnerDir": "pos cargo R dir",
            "usePreciseGetInAction": 0,
            "preciseGetInOut": 0,
            "gunnerAction": "rhs_bmp3_gunner03",
            "gunnerInAction": "rhs_bmp3_gunner03",
            "gunnerGetInAction": "GetInHigh",
            "gunnerGetOutAction": "GetOutHigh",
            "viewGunnerInExternal": 1,
            "startEngine": 0,
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Turrets,
            "Turrets": {
            },
            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpp220a_right",
            "gunnerOpticsColor": [1,1,1,1],
            "gunnerForceOptics": 0,
            "gunnerOpticsEffect": ["TankGunnerOptics1","WeaponsOptics","OpticsCHAbera3"],
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\ViewOptics,
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "opticsZoomMin": 0.166666,
                "opticsZoomMax": 0.166666,
                "distanceZoomMin": 200,
                "distanceZoomMax": 2000,
                "initFov": 0.166666,
                "minFov": 0.166666,
                "maxFov": 0.166666
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\TurnIn,
            "TurnIn": {
                "limitsArrayTop": [[10,-10],[10,10]],
                "limitsArrayBottom": [[-10,-10],[-10,10]]
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\TurnOut,
            "TurnOut": {
                "limitsArrayTop": [[45,-150],[45,150]],
                "limitsArrayBottom": [[-24,-150],[-24,150]]
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components,
            "Components": {
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentLeft\EmptyDisplay
                    "EmptyDisplay": {
                        "componentType": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentLeft\CrewDisplay,
                    "CrewDisplay": {
                        "componentType": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentRight\EmptyDisplay
                    "EmptyDisplay": {
                        "componentType": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentRight\CrewDisplay,
                    "CrewDisplay": {
                        "componentType": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                }
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\HitPoints,
            "HitPoints": {
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\HitPoints\HitTurret_Bow1
                "HitTurret_Bow1": {
                    "armor": 0.5,
                    "material": -1,
                    "name": "hit_obsgun2",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": 0.14,
                    "explosionShielding": 0.001,
                    "radius": 0.25,
                    "isTurret": 1
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\HitPoints\HitGun_Bow1,
                "HitGun_Bow1": {
                    "armor": 0.6,
                    "material": -1,
                    "name": "hit_obsgun2",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": 0.13,
                    "explosionShielding": 0.001,
                    "radius": 0.25,
                    "isGun": 1
                }
            },
            "animationSourceCamElev": "camElev",
            "soundServo": ["",0.00316228,1],
            "soundElevation": ["",0.00316228,1],
            "initElev": 0,
            "initTurn": 0,
            "maxHorizontalRotSpeed": 1.2,
            "maxVerticalRotSpeed": 1.2,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "stabilizedInAxes": 3,
            "primary": 1,
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
            "gunnerOpticsShowCursor": 0,
            "turretInfoType": "",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
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
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "outGunnerMayFire": 0,
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
            "forceNVG": 0,
            "isCopilot": 0,
            "canEject": 1,
            "gunnerLeftHandAnimName": "",
            "gunnerRightHandAnimName": "",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "turretFollowFreeLook": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "disableSoundAttenuation": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            "showCrewAim": 0
        },
        # Class: CfgVehicles\rhs_bmp3m_msv\Turrets\GPMGTurret2,
        "GPMGTurret2": {
            "proxyIndex": 9,
            "gunnerDoor": "hatchLA",
            "animationSourceHatch": "hatchL",
            "weapons": ["rhs_weap_pkt_bmd_bow2"],
            "body": "LF_Seat_turret",
            "gun": "LF_Seat_gun",
            "animationSourceBody": "LF_Seat_Turret",
            "animationSourceGun": "LF_Seat_Gun",
            "gunnerName": "Left Hull Gunner",
            "memoryPointGunnerOptics": "gunnerView2",
            "commanding": 1,
            "gunnerOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tnpp220a",
            "memoryPointsGetInGunner": "pos cargo L",
            "memoryPointsGetInGunnerDir": "pos cargo L dir",
            "memoryPointGun": "memoryPointGun3",
            "gunBeg": "muzzle3",
            "gunEnd": "end3",
            "selectionFireAnim": "zasleh4",
            "gunnerAction": "rhs_bmp3_gunner02",
            "gunnerInAction": "rhs_bmp3_gunner02",
            "personTurretAction": "vehicle_turnout_2",
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret2\HitPoints,
            "HitPoints": {
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret2\HitPoints\HitTurret_Bow2
                "HitTurret_Bow2": {
                    "armor": 0.5,
                    "material": -1,
                    "name": "hit_obsgun3",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": 0.14,
                    "explosionShielding": 0.001,
                    "radius": 0.25,
                    "isTurret": 1
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret2\HitPoints\HitGun_Bow2,
                "HitGun_Bow2": {
                    "armor": 0.6,
                    "material": -1,
                    "name": "hit_obsgun3",
                    "visual": "-",
                    "passThrough": 0,
                    "minimalHit": 0.13,
                    "explosionShielding": 0.001,
                    "radius": 0.25,
                    "isGun": 1
                }
            },
            "hasGunner": 1,
            "gunnerType": "rhs_msv_rifleman",
            "isPersonTurret": 1,
            "showAsCargo": 1,
            "proxyType": "CPCargo",
            "minOutElev": -10,
            "maxOutElev": 15,
            "initOutElev": 0,
            "minOutTurn": -100,
            "maxOutTurn": 120,
            "initOutTurn": 0,
            "usePip": 1,
            "dontCreateAI": 1,
            "forceHideGunner": 0,
            "primaryObserver": 0,
            "primaryGunner": 0,
            "LodOpticsIn": 0,
            "LodOpticsOut": 0,
            "minElev": -24,
            "maxElev": 35,
            "minTurn": -10,
            "maxTurn": 10,
            "magazines": ["rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250","rhs_mag_762x54mm_250"],
            "ejectDeadGunner": 0,
            "usePreciseGetInAction": 0,
            "preciseGetInOut": 0,
            "gunnerGetInAction": "GetInHigh",
            "gunnerGetOutAction": "GetOutHigh",
            "viewGunnerInExternal": 1,
            "startEngine": 0,
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Turrets,
            "Turrets": {
            },
            "gunnerOpticsColor": [1,1,1,1],
            "gunnerForceOptics": 0,
            "gunnerOpticsEffect": ["TankGunnerOptics1","WeaponsOptics","OpticsCHAbera3"],
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\ViewOptics,
            "ViewOptics": {
                "initAngleX": 0,
                "minAngleX": -30,
                "maxAngleX": 30,
                "initAngleY": 0,
                "minAngleY": -100,
                "maxAngleY": 100,
                "opticsZoomMin": 0.166666,
                "opticsZoomMax": 0.166666,
                "distanceZoomMin": 200,
                "distanceZoomMax": 2000,
                "initFov": 0.166666,
                "minFov": 0.166666,
                "maxFov": 0.166666
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\TurnIn,
            "TurnIn": {
                "limitsArrayTop": [[10,-10],[10,10]],
                "limitsArrayBottom": [[-10,-10],[-10,10]]
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\TurnOut,
            "TurnOut": {
                "limitsArrayTop": [[45,-150],[45,150]],
                "limitsArrayBottom": [[-24,-150],[-24,150]]
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components,
            "Components": {
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentLeft
                "VehicleSystemsDisplayManagerComponentLeft": {
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentLeft\EmptyDisplay
                    "EmptyDisplay": {
                        "componentType": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentLeft\CrewDisplay,
                    "CrewDisplay": {
                        "componentType": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentRight,
                "VehicleSystemsDisplayManagerComponentRight": {
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentRight\EmptyDisplay
                    "EmptyDisplay": {
                        "componentType": "EmptyDisplayComponent"
                    },
                    # Class: CfgVehicles\rhs_bmp3tank_base\Turrets\GPMGTurret1\Components\VehicleSystemsDisplayManagerComponentRight\CrewDisplay,
                    "CrewDisplay": {
                        "componentType": "CrewDisplayComponent",
                        "resource": "RscCustomInfoCrew"
                    }
                }
            },
            "animationSourceCamElev": "camElev",
            "soundServo": ["",0.00316228,1],
            "soundElevation": ["",0.00316228,1],
            "initElev": 0,
            "initTurn": 0,
            "maxHorizontalRotSpeed": 1.2,
            "maxVerticalRotSpeed": 1.2,
            "minCamElev": -90,
            "maxCamElev": 90,
            "initCamElev": 0,
            "stabilizedInAxes": 3,
            "primary": 1,
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
            "gunnerOpticsShowCursor": 0,
            "turretInfoType": "",
            "gunnerOutOpticsModel": "",
            "gunnerOutOpticsColor": [0,0,0,1],
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
            "hideWeaponsGunner": 1,
            "canHideGunner": -1,
            "outGunnerMayFire": 0,
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
            "forceNVG": 0,
            "isCopilot": 0,
            "canEject": 1,
            "gunnerLeftHandAnimName": "",
            "gunnerRightHandAnimName": "",
            "gunnerLeftLegAnimName": "",
            "gunnerRightLegAnimName": "",
            "turretFollowFreeLook": 0,
            "allowTabLock": 1,
            "showAllTargets": 0,
            "disableSoundAttenuation": 0,
            "slingLoadOperator": 0,
            "playerPosition": 0,
            "allowLauncherIn": 0,
            "allowLauncherOut": 0,
            "showCrewAim": 0
        }
    },
    "dlc": "RHS_AFRF",
    "rhs_decalParameters": ["['Number',cRHSBMP3NumberPlaces,'DefaultRed']","['Label',cRHSBMP3PlnSymPlaces, 'Platoon',12]"],
    "category": "Armored",
    "destrType": "DestructDefault",
    "weapons": ["rhs_weap_smokegen"],
    "magazines": ["rhs_mag_smokegen"],
    "vehicleClass": "rhs_vehclass_ifv",
    "editorSubcategory": "rhs_EdSubcat_ifv",
    "faction": "rhs_faction_msv",
    "accuracy": 0.3,
    "side": 0,
    # Class: CfgVehicles\rhs_bmp3tank_base\MFD,
    "MFD": {
        # Class: CfgVehicles\rhs_bmp3tank_base\MFD\MFD_Left
        "MFD_Left": {
            "topLeft": "MFD_1_TL",
            "topRight": "MFD_1_TR",
            "bottomLeft": "MFD_1_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles\rhs_bmp3tank_base\MFD\MFD_Left\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\MFD\MFD_Left\Draw,
            "Draw": {
                "color": [0.07,0.14,0.07],
                "alpha": 0.12,
                "condition": "on",
                # Class: CfgVehicles\rhs_bmp3tank_base\MFD\MFD_Left\Draw\FuelNumber,
                "FuelNumber": {
                    "type": "text",
                    "source": "fuel",
                    "sourceScale": 677,
                    "scale": 1,
                    "align": "right",
                    "pos": [[0.655,0.205],1],
                    "right": [[0.755,0.205],1],
                    "down": [[0.655,0.515],1]
                }
            }
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\MFD\MFD_Right,
        "MFD_Right": {
            "topLeft": "MFD_2_TL",
            "topRight": "MFD_2_TR",
            "bottomLeft": "MFD_2_BL",
            "borderLeft": 0,
            "borderRight": 0,
            "borderTop": 0,
            "borderBottom": 0,
            "color": [1,1,1],
            "alpha": 0.5,
            "enableParallax": 0,
            "font": "rhs_digital_font_var",
            # Class: CfgVehicles\rhs_bmp3tank_base\MFD\MFD_Right\Bones,
            "Bones": {
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\MFD\MFD_Right\Draw,
            "Draw": {
                "color": [0.07,0.14,0.07],
                "alpha": 0.12,
                "condition": "on",
                # Class: CfgVehicles\rhs_bmp3tank_base\MFD\MFD_Right\Draw\rpmNumber,
                "rpmNumber": {
                    "type": "text",
                    "source": "rpm",
                    "sourceScale": 1,
                    "scale": 1,
                    "refreshRate": 0.05,
                    "align": "left",
                    "pos": [[0.305,0.205],1],
                    "right": [[0.405,0.205],1],
                    "down": [[0.305,0.515],1]
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\MFD\MFD_Right\Draw\SpeedNumber,
                "SpeedNumber": {
                    "type": "text",
                    "source": "speed",
                    "sourceScale": 3.6,
                    "scale": 1,
                    "refreshRate": 0.05,
                    "align": "left",
                    "pos": [[0.795,0.205],1],
                    "right": [[0.895,0.205],1],
                    "down": [[0.795,0.515],1]
                }
            }
        }
    },
    "picture": "rhsafrf|addons|rhs_bmp3|pictures|rhs_bmp3_pic_ca.paa",
    "Icon": "rhsafrf|addons|rhs_bmp3|data|bis|icon_bmp3_ca.paa",
    "mapsize": 7.1,
    "typicalCargo": ["rhs_msv_crew_commander","rhs_msv_crew","rhs_msv_crew",""],
    "getInAction": "GetInLow",
    "getOutAction": "GetOutLow",
    "cargoGetInAction": ["GetInLow"],
    "cargoGetOutAction": ["GetOutLow"],
    "transportsoldier": 7,
    "unloadInCombat": 1,
    "cargoProxyIndexes": [1,2,3,4,5,6,7],
    "getInProxyOrder": [8,9,1,2,3,4,5,6,7],
    "weaponsGroup1": "1 + 16",
    "weaponsGroup2": 128,
    "weaponsGroup3": 2,
    "weaponsGroup4": 4,
    "tf_range_api": 35000,
    "cargoAction": ["RHS_BMP3_Cargo","RHS_BMP3_Cargo","RHS_BMP3_Cargo","RHS_BMP3_Cargo","RHS_BMP3_Cargo","RHS_BMP3_Cargo","RHS_BMP3_Cargo","YouShallNotSitHere"],
    "waterPPInVehicle": 0,
    "driveOnComponent": ["Track_L","Track_R","Slide"],
    "driverOpticsModel": "rhsafrf|addons|rhs_optics|vehicles|rhs_tvn5.p3d",
    "driverDoor": "hatchD",
    "driverAction": "RHS_BMP3_driverout",
    "driverInAction": "RHS_BMP3_driver",
    "driverLeftHandAnimName": "steering",
    "driverRightHandAnimName": "steering",
    "driverForceOptics": 0,
    "viewDriverInExternal": 1,
    "LODDriverTurnedOut": 0,
    "LODDriverOpticsIn": 0,
    "LODDriverOpticsOut": 0,
    "headGforceLeaningFactor": [0.015,0.011,0.015],
    "simulation": "tankX",
    "maxSpeed": 70,
    "normalSpeedForwardCoef": 0.73,
    "slowSpeedForwardCoef": 0.35,
    "fuelCapacity": 30,
    "RHS_fuelCapacity": 672,
    "tankTurnForce": 280000,
    "tankTurnForceAngMinSpd": 0.6,
    "tankTurnForceAngSpd": 0.82,
    "accelAidForceCoef": 4,
    "accelAidForceYOffset": -4,
    "accelAidForceSpd": 2.83,
    "canFloat": 1,
    "waterLeakiness": 250,
    "maxFordingDepth": 0.05,
    "waterResistance": 1,
    "waterDamageEngine": 0.9,
    "engineShiftY": 0.7,
    "waterLinearDampingCoefY": 2,
    "waterLinearDampingCoefX": 2,
    "waterAngularDampingCoef": 1.2,
    "waterResistanceCoef": 0.15,
    "waterEffectSpeed": 5,
    "engineEffectSpeed": 5,
    "waterFastEffectSpeed": 28,
    "engineMOI": 18,
    "minOmega": 84,
    "maxOmega": 301,
    "idleRpm": 800,
    "redRpm": 2880,
    "thrustDelay": 0.6,
    "clutchStrength": 30,
    "brakeIdleSpeed": 1.78,
    "latency": 0.6,
    "antiRollbarForceCoef": 24,
    "antiRollbarForceLimit": 42,
    "antiRollbarSpeedMin": 30,
    "antiRollbarSpeedMax": 75,
    "engineLosses": 25,
    "transmissionLosses": 15,
    "changeGearType": "rpmratio",
    "changeGearOmegaRatios": [1,0.347222,0.347222,0,0.9375,0.347222,0.885417,0.659722,0.954861,0.659722,1,0.659722],
    # Class: CfgVehicles\rhs_bmp3tank_base\complexGearbox,
    "complexGearbox": {
        "GearboxRatios": ["R1",-2.51,"N",0,"D1",3.31,"D2",1.934,"D3",1.132,"D4",0.662],
        "AmphibiousRatios": ["R1",-10,"N",0,"D1",10],
        "TransmissionRatios": ["High",19],
        "gearBoxMode": "auto",
        "moveOffGear": 1,
        "driveString": "D",
        "neutralString": "N",
        "reverseString": "R",
        "transmissionDelay": 0.3
    },
    "soundGetIn": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1],
    "soundGetOut": ["A3|sounds_f|vehicles|armor|noises|get_in_out",0.562341,1,20],
    "soundDammage": ["",0.562341,1],
    "soundEngineOnInt": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_start",0.707946,1],
    "soundEngineOnExt": ["|rhsafrf|addons|rhs_bmp|sounds|utd20_start",0.630957,1,200],
    "soundEngineOffInt": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_stop",0.707946,1],
    "soundEngineOffExt": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_stop",0.630957,1,200],
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
    # Class: CfgVehicles\rhs_bmp3tank_base\Sounds,
    "Sounds": {
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Idle_ext
        "Idle_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_ext_idle",0.707946,1,200],
            "frequency": "0.95	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine,
        "Engine": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",0.794328,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine1_ext,
        "Engine1_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",0.794328,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine2_ext,
        "Engine2_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",0.891251,1,250],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine3_ext,
        "Engine3_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",1,1,300],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine4_ext,
        "Engine4_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",1.12202,1,340],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*camPos*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine5_ext,
        "Engine5_ext": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|UTD20.ogg",1.41254,1,400],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*camPos*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\IdleThrust,
        "IdleThrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_idle",0.891251,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\EngineThrust,
        "EngineThrust": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm1",1.12202,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine1_Thrust_ext,
        "Engine1_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm2",1.25893,1,200],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine2_Thrust_ext,
        "Engine2_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm3",1.41254,1,250],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine3_Thrust_ext,
        "Engine3_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm4",1.58489,1,350],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine4_Thrust_ext,
        "Engine4_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm5",1.77828,1,400],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine5_Thrust_ext,
        "Engine5_Thrust_ext": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_ext_rpm6",1.99526,1,450],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*camPos*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Idle_int,
        "Idle_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_idle",0.316228,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine_int,
        "Engine_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm1",0.354813,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine1_int,
        "Engine1_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm2",0.398107,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine2_int,
        "Engine2_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm3",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine3_int,
        "Engine3_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm4",0.501187,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine4_int,
        "Engine4_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm5",0.562341,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine5_int,
        "Engine5_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_engine_int_rpm6",0.630957,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\IdleThrust_int,
        "IdleThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_idle",0.354813,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(400/	5200),(900/	5200)])*0.15",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(100/	5200),(200/	5200)])	*	((rpm/	5200) factor[(900/	5200),(700/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\EngineThrust_int,
        "EngineThrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm1",0.398107,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(700/	5200),(1100/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(705/	5200),(850/	5200)])	*	((rpm/	5200) factor[(1100 /	5200),(950/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine1_Thrust_int,
        "Engine1_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm2",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(950/	5200),(1400/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(900/	5200),(1050/	5200)])	*	((rpm/	5200) factor[(1400/	5200),(1200/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine2_Thrust_int,
        "Engine2_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm3",0.446684,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1200/	5200),(1700/	5200)])*0.2",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1170/	5200),(1380/	5200)])	*	((rpm/	5200) factor[(1700/	5200),(1500/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine3_Thrust_int,
        "Engine3_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm4",0.501187,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1500/	5200),(2100/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1500/	5200),(1670/	5200)])	*	((rpm/	5200) factor[(2100/	5200),(1800/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine4_Thrust_int,
        "Engine4_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm5",0.562341,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(1800/	5200),(2300/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*(((rpm/	5200) factor[(1780/	5200),(2060/	5200)])	*	((rpm/	5200) factor[(2450/	5200),(2200/	5200)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\Engine5_Thrust_int,
        "Engine5_Thrust_int": {
            "sound": ["A3|Sounds_F|vehicles|armor|MBT_03|MBT_exhaust_int_rpm6",0.630957,1],
            "frequency": "0.8	+	((rpm/	5200) factor[(2100/	5200),(2640/	5200)])*0.1",
            "volume": "engineOn*(1-camPos)*(0.4+(0.6*(thrust factor[0.1,1])))*((rpm/	5200) factor[(2150/	5200),(2500/	5200)])"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\NoiseInt,
        "NoiseInt": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_int_1",0.562341,1],
            "frequency": "1",
            "volume": "(1-camPos)*(angVelocity max 0.04)*(speed factor[4, 25])"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\NoiseExt,
        "NoiseExt": {
            "sound": ["A3|sounds_f|vehicles|armor|noises|noise_tank_ext_1",0.794328,1,150],
            "frequency": "1",
            "volume": "camPos*(angVelocity max 0.04)*(speed factor[4, 25])"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsOutH0,
        "ThreadsOutH0": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.398107,1,140],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsOutH1,
        "ThreadsOutH1": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.446684,1,160],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsOutH2,
        "ThreadsOutH2": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_3.ogg",0.501187,1,180],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsOutH3,
        "ThreadsOutH3": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_4.ogg",0.562341,1,200],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsOutH4,
        "ThreadsOutH4": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_5.ogg",0.562341,1,220],
            "frequency": "1",
            "volume": "engineOn*camPos*(1-grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsOutS0,
        "ThreadsOutS0": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.316228,1,120],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsOutS1,
        "ThreadsOutS1": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_2.ogg",0.354813,1,140],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsOutS2,
        "ThreadsOutS2": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_3.ogg",0.398107,1,160],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsOutS3,
        "ThreadsOutS3": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_4.ogg",0.446684,1,180],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsOutS4,
        "ThreadsOutS4": {
            "sound": ["|rhsafrf|addons|rhs_bmp|sounds|lanc_5.ogg",0.501187,1,200],
            "frequency": "1",
            "volume": "engineOn*(camPos)*(grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsInH0,
        "ThreadsInH0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_01",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsInH1,
        "ThreadsInH1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_02",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsInH2,
        "ThreadsInH2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_03",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsInH3,
        "ThreadsInH3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_04",0.501187,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsInH4,
        "ThreadsInH4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_hard_05",0.562341,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*(1-grass)*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsInS0,
        "ThreadsInS0": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_01",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-0) max 0)/	60),(((-5) max 5)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-15) max 15)/	60),(((-10) max 10)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsInS1,
        "ThreadsInS1": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_02",0.354813,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-10) max 10)/	60),(((-15) max 15)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-30) max 30)/	60),(((-25) max 25)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsInS2,
        "ThreadsInS2": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_03",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-25) max 25)/	60),(((-30) max 30)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-45) max 45)/	60),(((-40) max 40)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsInS3,
        "ThreadsInS3": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_04",0.398107,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*(((((-speed*3.6) max speed*3.6)/	60) factor[(((-40) max 40)/	60),(((-45) max 45)/	60)])	*	((((-speed*3.6) max speed*3.6)/	60) factor[(((-55) max 55)/	60),(((-50) max 50)/	60)]))"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Sounds\ThreadsInS4,
        "ThreadsInS4": {
            "sound": ["A3|sounds_f|vehicles|armor|treads|int_treads_soft_05",0.446684,1],
            "frequency": "1",
            "volume": "engineOn*(1-camPos)*grass*((((-speed*3.6) max speed*3.6)/	60) factor[(((-49) max 49)/	60),(((-53) max 53)/	60)])"
        }
    },
    # Class: CfgVehicles\rhs_bmp3tank_base\RenderTargets,
    "RenderTargets": {
        # Class: CfgVehicles\rhs_bmp3tank_base\RenderTargets\driverView2
        "driverView2": {
            "renderTarget": "rendertarget1",
            # Class: CfgVehicles\rhs_bmp3tank_base\RenderTargets\driverView2\Camera,
            "Camera": {
                "pointPosition": "dVis2P",
                "pointDirection": "dVis2D",
                "renderVisionMode": 0,
                "renderQuality": 4,
                "fov": 0.5
            },
            "BBoxes": ["PIP_1_TL","PIP_1_TR","PIP_1_BL","PIP_1_BR"]
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\RenderTargets\driverView3,
        "driverView3": {
            "renderTarget": "rendertarget2",
            # Class: CfgVehicles\rhs_bmp3tank_base\RenderTargets\driverView3\Camera,
            "Camera": {
                "pointPosition": "dVis3P",
                "pointDirection": "dVis3D",
                "renderVisionMode": 0,
                "renderQuality": 4,
                "fov": 0.5
            },
            "BBoxes": ["PIP_2_TL","PIP_2_TR","PIP_2_BL","PIP_2_BR"]
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\RenderTargets\driverView4,
        "driverView4": {
            "renderTarget": "rendertarget3",
            # Class: CfgVehicles\rhs_bmp3tank_base\RenderTargets\driverView4\Camera,
            "Camera": {
                "pointPosition": "dVis4P",
                "pointDirection": "dVis4D",
                "renderVisionMode": 0,
                "renderQuality": 2,
                "fov": 0.5
            },
            "BBoxes": ["PIP_3_TL","PIP_3_TR","PIP_3_BL","PIP_3_BR"]
        }
    },
    "driverCanSee": "2+4+8",
    "gunnerCanSee": "2+4+8",
    "commanderCanSee": "2+4+8",
    "incomingMissileDetectionSystem": 0,
    "tracksSpeed": 1.35,
    "wheelCircumference": 1.922,
    "attenuationEffectType": "TankAttenuation",
    # Class: CfgVehicles\rhs_bmp3tank_base\SpeechVariants,
    "SpeechVariants": {
        # Class: CfgVehicles\rhs_bmp3tank_base\SpeechVariants\Default
        "Default": {
            "speechSingular": ["veh_vehicle_APC_s"],
            "speechPlural": ["veh_vehicle_APC_p"]
        }
    },
    "textSingular": "BMP",
    "textPlural": "BMPs",
    "nameSound": "veh_vehicle_APC_s",
    "extCameraPosition": [0,2,-9],
    "HeadAimDown": 0,
    "cost": 1.5e+006,
    # Class: CfgVehicles\rhs_bmp3tank_base\ViewPilot,
    "ViewPilot": {
        "initAngleX": -12,
        "minAngleY": -110,
        "maxAngleY": 110,
        "initAngleY": 0,
        "initFov": 0.75,
        "minFov": 0.25,
        "maxFov": 1.25,
        "minAngleX": -65,
        "maxAngleX": 85,
        "minMoveX": -0.075,
        "maxMoveX": 0.075,
        "minMoveY": -0.075,
        "maxMoveY": 0.075,
        "minMoveZ": -0.075,
        "maxMoveZ": 0.1,
        "speedZoomMaxSpeed": 1e+010,
        "speedZoomMaxFOV": 0
    },
    "armor": 200,
    "armorStructural": 500,
    "fuelExplosionPower": 0.5,
    "damageResistance": 0.02,
    "crewVulnerable": 0,
    # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines,
    "TransportMagazines": {
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines\_xx_rhs_30Rnd_545x39_7N10_AK
        "_xx_rhs_30Rnd_545x39_7N10_AK": {
            "magazine": "rhs_30Rnd_545x39_7N10_AK",
            "count": 30
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines\_xx_rhs_10Rnd_762x54mmR_7N1,
        "_xx_rhs_10Rnd_762x54mmR_7N1": {
            "magazine": "rhs_10Rnd_762x54mmR_7N1",
            "count": 10
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines\_xx_rhs_100Rnd_762x54mmR,
        "_xx_rhs_100Rnd_762x54mmR": {
            "magazine": "rhs_100Rnd_762x54mmR",
            "count": 3
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines\_xx_rhs_mag_rdg2_white,
        "_xx_rhs_mag_rdg2_white": {
            "magazine": "rhs_mag_rdg2_white",
            "count": 2
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines\_xx_rhs_mag_rgd5,
        "_xx_rhs_mag_rgd5": {
            "magazine": "rhs_mag_rgd5",
            "count": 9
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines\_xx_rhs_VOG25,
        "_xx_rhs_VOG25": {
            "magazine": "rhs_VOG25",
            "count": 20
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines\_xx_rhs_vg40op_white,
        "_xx_rhs_vg40op_white": {
            "magazine": "rhs_vg40op_white",
            "count": 5
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines\_xx_rhs_GRD40_white,
        "_xx_rhs_GRD40_white": {
            "magazine": "rhs_GRD40_white",
            "count": 5
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines\_xx_rhs_rpg26_mag,
        "_xx_rhs_rpg26_mag": {
            "magazine": "rhs_rpg26_mag",
            "count": 2
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportMagazines\_xx_rhs_rpg7_OG7V_mag,
        "_xx_rhs_rpg7_OG7V_mag": {
            "magazine": "rhs_rpg7_OG7V_mag",
            "count": 2
        }
    },
    # Class: CfgVehicles\rhs_bmp3tank_base\TransportWeapons,
    "TransportWeapons": {
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportWeapons\_xx_rhs_weap_ak74m
        "_xx_rhs_weap_ak74m": {
            "weapon": "rhs_weap_ak74m",
            "count": 4
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportWeapons\_xx_rhs_weap_rpg26,
        "_xx_rhs_weap_rpg26": {
            "weapon": "rhs_weap_rpg26",
            "count": 2
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportWeapons\_xx_rhs_weap_rpg7,
        "_xx_rhs_weap_rpg7": {
            "weapon": "rhs_weap_rpg7",
            "count": 1
        }
    },
    # Class: CfgVehicles\rhs_bmp3tank_base\TransportItems,
    "TransportItems": {
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportItems\_xx_FirstAidKit
        "_xx_FirstAidKit": {
            "name": "FirstAidKit",
            "count": 4
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportItems\_xx_Medikit,
        "_xx_Medikit": {
            "name": "Medikit",
            "count": 1
        }
    },
    # Class: CfgVehicles\rhs_bmp3tank_base\TransportBackpacks,
    "TransportBackpacks": {
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportBackpacks\_xx_rhs_sidor
        "_xx_rhs_sidor": {
            "backpack": "rhs_sidor",
            "count": 7
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\TransportBackpacks\_xx_rhs_rpg,
        "_xx_rhs_rpg": {
            "backpack": "rhs_rpg",
            "count": 1
        }
    },
    "textureList": [],
    # Class: CfgVehicles\rhs_bmp3tank_base\Attributes,
    "Attributes": {
        # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\ObjectTexture
        "ObjectTexture": {
            "control": "ObjectTexture",
            "data": "ObjectTexture",
            "displayName": "Skin",
            "tooltip": "Texture and material set applied on the object."
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber_type,
        "rhs_decalNumber_type": {
            "displayName": "Define font type of plate number",
            "tooltip": "Define kind of font that will be drawn on vehicle.",
            "property": "rhs_decalNumber_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];[_this,[['Number', cRHSBMP3NumberPlaces, _value]]] call rhs_fnc_decalsInit",
            "defaultValue": 0,
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber_type\values,
            "values": {
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber_type\values\DefaultRed
                "DefaultRed": {
                    "name": "Default (Red)",
                    "value": "DefaultRed"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber_type\values\Default,
                "Default": {
                    "name": "Default",
                    "value": "Default",
                    "defaultValue": "Default"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber_type\values\BoldRed,
                "BoldRed": {
                    "name": "Bold Red",
                    "value": "BoldRed"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber_type\values\CDF,
                "CDF": {
                    "name": "CDF",
                    "value": "CDF"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber_type\values\Handpaint,
                "Handpaint": {
                    "name": "Handpaint",
                    "value": "Handpaint"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber_type\values\HandpaintBlack,
                "HandpaintBlack": {
                    "name": "Handpaint Black",
                    "value": "HandpaintBlack"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber_type\values\Iraqi,
                "Iraqi": {
                    "name": "Iraqi",
                    "value": "Iraqi"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber_type\values\LicensePlate,
                "LicensePlate": {
                    "name": "License Plate",
                    "value": "LicensePlate"
                }
            }
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalNumber,
        "rhs_decalNumber": {
            "collapsed": 1,
            "displayName": "Set side number",
            "tooltip": "Set side number. 4 numbers are required. Type 0 to hide numbers complety & leave at -1 to get random number",
            "property": "rhs_decalNumber",
            "control": "Edit",
            "validate": "Number",
            "typeName": "Number",
            "defaultValue": "-1",
            "expression": "if( _value >= 0)then{if( _value == 0)then{{[_this setobjectTexture [_x,'a3|data_f|clear_empty.paa']]}foreach cRHSBMP3NumberPlaces}else{[_this, [['Number', cRHSBMP3NumberPlaces, _this getVariable ['rhs_decalNumber_type','DefaultRed'], _value] ] ] call rhs_fnc_decalsInit}};"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalPlatoon_type,
        "rhs_decalPlatoon_type": {
            "displayName": "Define platoon symbol type",
            "tooltip": "Decal type",
            "property": "rhs_decalPlatoon_type",
            "control": "Combo",
            "expression": "_this setVariable ['%s', _value];",
            "defaultValue": "0",
            "typeName": "STRING",
            # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalPlatoon_type\values,
            "values": {
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalPlatoon_type\values\Platoon
                "Platoon": {
                    "name": "Platoon",
                    "value": "Platoon"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalPlatoon_type\values\PlatoonGDR,
                "PlatoonGDR": {
                    "name": "Platoon GDR",
                    "value": "PlatoonGDR"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalPlatoon_type\values\PlatoonVDV,
                "PlatoonVDV": {
                    "name": "Platoon VDV",
                    "value": "PlatoonVDV"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalPlatoon_type\values\Army,
                "Army": {
                    "name": "Army",
                    "value": "Army",
                    "defaultValue": "Army"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalPlatoon_type\values\Honor,
                "Honor": {
                    "name": "Honor",
                    "value": "Honor"
                },
                # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalPlatoon_type\values\HonorGDR,
                "HonorGDR": {
                    "name": "Honor GDR",
                    "value": "HonorGDR"
                }
            }
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Attributes\rhs_decalPlatoon,
        "rhs_decalPlatoon": {
            "displayName": "Set platoon symbol",
            "tooltip": "Set platoon symbol located on both sides. Usually used for platoon symbols. -1 leaves current symbol & 0 clears decal.",
            "property": "rhs_decalPlatoon",
            "control": "Edit",
            "validate": "none",
            "defaultValue": "-1",
            "expression": "if(parseNumber _value >= 0)then{ [_this, [ [ 'Label', cRHSBMP3PlnSymPlaces,  _this getVariable ['rhs_decalPlatoon_type','Platoon'],call compile _value] ] ] call rhs_fnc_decalsInit};"
        }
    },
    # Class: CfgVehicles\rhs_bmp3tank_base\Damage,
    "Damage": {
        "tex": [],
        "mat": ["rhsafrf|addons|rhs_bmp3|data|3M_ERA.rvmat","rhsafrf|addons|rhs_bmp3|data|dam_3M_ERA.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_destr_bmp3.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_01.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_dam_bmp3_01.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_destr_bmp3.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_01_3M.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_dam_bmp3_01_3M.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_destr_bmp3.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_01_3MERA.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_dam_bmp3_01_3MERA.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_destr_bmp3.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_02.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_dam_bmp3_02.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_destr_bmp3.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_02_3MERA.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_dam_bmp3_02_3MERA.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_destr_bmp3.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_03.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_dam_bmp3_03.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_destr_bmp3.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_03_MOD.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_dam_bmp3_03_mod.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_destr_bmp3.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_03_3M.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_dam_bmp3_03_3M.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_destr_bmp3.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_bmp3_04.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_dam_bmp3_04.rvmat","rhsafrf|addons|rhs_bmp3|data|rhs_destr_bmp3.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4m_t.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4m_t.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4m_t.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_bmd4_03.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_dam_bmd4_03.rvmat","rhsafrf|addons|rhs_bmd_34|data|rhs_destr_bmd4_03.rvmat","a3|data_f|default.rvmat","a3|data_f|default.rvmat","a3|data_f|default_destruct.rvmat"]
    },
    # Class: CfgVehicles\rhs_bmp3tank_base\ViewOptics,
    "ViewOptics": {
        "visionMode": ["Normal","NVG"],
        "initFov": 0.7,
        "minFov": 0.7,
        "maxFov": 0.7,
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
    # Class: CfgVehicles\rhs_bmp3tank_base\Exhausts,
    "Exhausts": {
        # Class: CfgVehicles\rhs_bmp3tank_base\Exhausts\Exhaust1
        "Exhaust1": {
            "position": "exhaustl",
            "direction": "exhaustl_dir",
            "effect": "ExhaustEffectTankSide"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Exhausts\Exhaust2,
        "Exhaust2": {
            "position": "exhaustr",
            "direction": "exhaustr_dir",
            "effect": "ExhaustEffectTankSide"
        }
    },
    # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources,
    "AnimationSources": {
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\muzzle_rot_coax
        "muzzle_rot_coax": {
            "source": "ammorandom",
            "weapon": "rhs_weap_pkt_bmd_coax"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\recoil_source,
        "recoil_source": {
            "source": "reload",
            "weapon": "rhs_weap_2a70"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\muzzle_hide_cannon,
        "muzzle_hide_cannon": {
            "source": "reload",
            "weapon": "rhs_weap_2a70"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\muzzle_rot_cannon,
        "muzzle_rot_cannon": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a70"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\recoil_source2,
        "recoil_source2": {
            "source": "reload",
            "weapon": "rhs_weap_2a72"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\muzzle_hide_hmg,
        "muzzle_hide_hmg": {
            "source": "reload",
            "weapon": "rhs_weap_2a72"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\muzzle_rot_hmg,
        "muzzle_rot_hmg": {
            "source": "ammorandom",
            "weapon": "rhs_weap_2a72"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\smokecap_revolving_source,
        "smokecap_revolving_source": {
            "source": "revolving",
            "weapon": "rhs_weap_902a"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\muzzle_rot_coax2,
        "muzzle_rot_coax2": {
            "weapon": "rhs_weap_pkt_bmd_bow1",
            "source": "ammorandom"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\muzzle_rot_coax3,
        "muzzle_rot_coax3": {
            "weapon": "rhs_weap_pkt_bmd_bow2",
            "source": "ammorandom"
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\autoloader,
        "autoloader": {
            "source": "user",
            "animPeriod": 1.25,
            "initPhase": 0
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\hatchC,
        "hatchC": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\HatchG,
        "HatchG": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\HatchD,
        "HatchD": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\HatchLA,
        "HatchLA": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\HatchRA,
        "HatchRA": {
            "source": "door",
            "animPeriod": 2.1
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\elev,
        "elev": {
            "source": "user",
            "animperiod": 0.0003
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\elev_bank,
        "elev_bank": {
            "source": "user",
            "animperiod": 0.0003
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\lead,
        "lead": {
            "source": "user",
            "animperiod": 0.0016
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\AnimationSources\offset,
        "offset": {
            "source": "user",
            "animperiod": 0.0002
        }
    },
    # Class: CfgVehicles\rhs_bmp3tank_base\Reflectors,
    "Reflectors": {
        # Class: CfgVehicles\rhs_bmp3tank_base\Reflectors\Driver_FG125_Cover
        "Driver_FG125_Cover": {
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "innerAngle": 35,
            "outerAngle": 75,
            "coneFadeCoef": 5,
            "intensity": 15,
            "useFlare": 0,
            "dayLight": 1,
            "flareSize": 0.85,
            # Class: CfgVehicles\rhs_bmp3tank_base\Reflectors\Driver_FG125_Cover\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.2,
                "hardLimitStart": 130,
                "hardLimitEnd": 160
            }
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Reflectors\Driver_FG125_Cover_Flare,
        "Driver_FG125_Cover_Flare": {
            "intensity": 5,
            "innerAngle": 55,
            "outerAngle": 155,
            "flareSize": 0.3,
            "useFlare": 1,
            "color": [1900,1300,950],
            "ambient": [5,5,5],
            "position": "Light_L",
            "direction": "Light_L_end",
            "hitpoint": "Light_L",
            "selection": "Light_L",
            "size": 1,
            "coneFadeCoef": 5,
            "dayLight": 1,
            # Class: CfgVehicles\rhs_bmp3tank_base\Reflectors\Driver_FG125_Cover\Attenuation,
            "Attenuation": {
                "start": 1,
                "constant": 0,
                "linear": 0,
                "quadratic": 0.2,
                "hardLimitStart": 130,
                "hardLimitEnd": 160
            }
        }
    },
    "aggregateReflectors": [["Driver_FG125_Cover","Driver_FG125_Cover_Flare"]],
    "armorLights": 0.1,
    # Class: CfgVehicles\rhs_bmp3tank_base\EventHandlers,
    "EventHandlers": {
        # Class: CfgVehicles\rhs_bmp3tank_base\EventHandlers\RHS_EventHandlers
        "RHS_EventHandlers": {
            "init": "_this call rhs_fnc_bmp3_init;",
            "fired": "_this call RHS_fnc_bmp3_autoloader;",
            "hitpart": "_this call rhs_fnc_hitSpall",
            "engine": "[_this select 0,_this select 1,2] call rhs_fnc_engineStartupDelay",
            "getOut": "_this call rhs_fnc_hatchAbandon"
        },
        "init": "",
        "fired": "_this call (uinamespace getvariable 'BIS_fnc_effectFired');",
        "killed": "_this call (uinamespace getvariable 'BIS_fnc_effectKilled');",
        # Class: DefaultEventHandlers\RHS_DefaultEventhandlers,
        "RHS_DefaultEventhandlers": {
            "hitpart": "_this call rhs_fnc_hitPart"
        }
    },
    # Class: CfgVehicles\rhs_bmp3tank_base\Components,
    "Components": {
        # Class: CfgVehicles\rhs_bmp3tank_base\Components\VehicleSystemsDisplayManagerComponentLeft
        "VehicleSystemsDisplayManagerComponentLeft": {
            # Class: CfgVehicles\rhs_bmp3tank_base\Components\VehicleSystemsDisplayManagerComponentLeft\EmptyDisplay
            "EmptyDisplay": {
                "componentType": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\Components\VehicleSystemsDisplayManagerComponentLeft\CrewDisplay,
            "CrewDisplay": {
                "componentType": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles\rhs_bmp3tank_base\Components\VehicleSystemsDisplayManagerComponentRight,
        "VehicleSystemsDisplayManagerComponentRight": {
            # Class: CfgVehicles\rhs_bmp3tank_base\Components\VehicleSystemsDisplayManagerComponentRight\EmptyDisplay
            "EmptyDisplay": {
                "componentType": "EmptyDisplayComponent"
            },
            # Class: CfgVehicles\rhs_bmp3tank_base\Components\VehicleSystemsDisplayManagerComponentRight\CrewDisplay,
            "CrewDisplay": {
                "componentType": "CrewDisplayComponent",
                "resource": "RscCustomInfoCrew"
            }
        },
        # Class: CfgVehicles\Tank_F\Components\AITankSteeringComponent,
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
        # Class: CfgVehicles\LandVehicle\Components\TransportCountermeasuresComponent,
        "TransportCountermeasuresComponent": {
        }
    },
    "_generalMacro": "Tank_F",
    "occludeSoundsWhenIn": 0,
    "obstructSoundsWhenIn": 0,
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
    "irScanGround": 2,
    "irScanRangeMax": 0,
    "irScanRangeMin": 0,
    "irScanToEyeFactor": 1,
    "enableRadio": 1,
    "LockDetectionSystem": 0,
    "countermeasureActivationRadius": 2000,
    "soundIncommingMissile": ["|A3|Sounds_F|vehicles|air|noises|alarm_locked_by_missile_3",0.316228,1],
    "memoryPointCargoLight": "cargo light",
    "dampersBumpCoef": 4.5,
    "explosionShielding": 1,
    "minTotalDamageThreshold": 0.005,
    "crewCrashProtection": 0.25,
    "crewExplosionProtection": 0.9995,
    "secondaryExplosion": -1,
    "transportMaxWeapons": 12,
    "transportMaxMagazines": 128,
    "transportMaxBackpacks": 12,
    "maximumLoad": 3000,
    "supplyRadius": -1,
    "memoryPointSupply": "doplnovani",
    # Class: CfgVehicles\Tank_F\CamShake,
    "CamShake": {
        "power": 5,
        "frequency": 20,
        "distance": 20,
        "minSpeed": 5
    },
    "camShakeCoef": 0,
    "viewCargoShadow": 1,
    "viewCargoShadowDiff": 0.05,
    "viewCargoShadowAmb": 0.5,
    # Class: CfgVehicles\Tank_F\NVGMarkers,
    "NVGMarkers": {
        # Class: CfgVehicles\Tank_F\NVGMarkers\NVGMarker01
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
    "getInRadius": 3.5,
    "hullDamageCauseExplosion": 1,
    "selectionFireAnim": "zasleh",
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
    "type": 1,
    "threat": [0.7,1,0.3],
    "camouflage": 8,
    "driverOpticsColor": [1,1,1,1],
    # Class: CfgVehicles\Tank\CargoLight,
    "CargoLight": {
        "color": [0,0,0,0],
        "ambient": [0.6,0,0.15,1],
        "brightness": 0.007
    },
    "memoryPointTaskMarkerOffset": [0,0.3,0],
    "rightDustEffects": [["GdtKLDirt","RDustEffects"],["GdtKLGrass1","RDustEffects"],["GdtKLGrass1","RGrassEffects"],["GdtKLGrass2","RDustEffects"],["GdtKLGrass2","RGrassEffects"],["GdtKLForestCon","RDustEffects"],["GdtKLForestDec","RDustEffects"],["GdtKlMud","RDustEffects"],["GdtKlSoil","RDustEffects"],["GdtKlTarmac","RDustEffects"],["GdtKlStubble","RDustEffects"],["GdtKlStones","RStonesEffects"],["SurfRoadDirt_Enoch","RDustEffects"],["SurfTrailDirt_Enoch","RDustEffects"],["SurfRoadTarmac1_Enoch","RDustEffects"],["SurfRoadTarmac2_Enoch","RDustEffects"],["SurfRoadTarmac3_Enoch","RDustEffects"],["GdtGrassShort","RDustEffects"],["GdtGrassShort","RGrassEffectsBig"],["GdtGrassTall","RDustEffects"],["GdtGrassTall","RGrassEffectsBig"],["GdtRedDirt","RDustEffectsRed"],["GdtField","RDustEffects"],["GdtForest","RDustEffects"],["GdtVolcano","RDustEffects"],["GdtVolcano","RStonesEffectsBig"],["GdtCliff","RDustEffects"],["GdtVolcanoBeach","RDustEffects"],["SurfRoadDirt_exp","RDustEffectsRed"],["SurfRoadConcrete_exp","RDustEffects"],["SurfRoadTarmac_exp","RDustEffects"],["GdtStratisConcrete","RDustEffects"],["GdtStratisConcrete","RDirtEffectsBig"],["GdtStratisBeach","RDustEffects"],["GdtStratisBeach","RStonesEffectsBig"],["GdtStratisDirt","RDustEffects"],["GdtStratisDirt","RDirtEffectsBig"],["GdtStratisSeabedCluttered","RDustEffects"],["GdtStratisSeabed","RDustEffects"],["GdtStratisDryGrass","RDustEffects"],["GdtStratisDryGrass","RGrassEffectsDryBig"],["GdtStratisDryGrass","RDirtEffectsBig"],["GdtStratisGreenGrass","RDustEffects"],["GdtStratisGreenGrass","RGrassEffectsBig"],["GdtStratisGreenGrass","RDirtEffectsBig"],["GdtStratisRocky","RDustEffects"],["GdtStratisRocky","RGrassEffectsBig"],["GdtStratisRocky","RDirtEffectsBig"],["GdtStratisThistles","RDustEffects"],["GdtStratisThistles","RGrassEffectsBig"],["GdtStratisThistles","RDirtEffectsBig"],["GdtConcrete","RDustEffects"],["GdtConcrete","RDirtEffectsBig"],["GdtAsphalt","RDustEffects"],["GdtAsphalt","RDirtEffectsBig"],["GdtRubble","RDustEffects"],["GdtRubble","RDirtEffectsBig"],["GdtSoil","RDustEffects"],["GdtSoil","RDirtEffectsBig"],["GdtBeach","RDustEffects"],["GdtBeach","RStonesEffectsBig"],["GdtRock","RDustEffects"],["GdtRock","RDirtEffectsBig"],["GdtDead","RDustEffects"],["GdtDead","RDirtEffectsBig"],["Default","RDustEffects"],["GdtDesert","RDustEffects"],["GdtDesert","RDirtEffectsBig"],["GdtDesert","RStonesEffects"],["GdtDesert1","RDustEffects"],["GdtDesert1","RDirtEffectsBig"],["GdtDesert1","RStonesEffectsBig"],["GdtDesert2","RDustEffects"],["GdtDesert2","RGrassEffectsBig"],["GdtDesert2","RDirtEffectsBig"],["GdtDirt","RDustEffects"],["GdtDirt","RDirtEffectsBig"],["GdtGrassGreen","RDustEffects"],["GdtGrassGreen","RGrassEffectsBig"],["GdtGrassGreen","RDirtEffectsBig"],["GdtGrassDry","RDustEffects"],["GdtGrassDry","RGrassEffectsDryBig"],["GdtGrassDry","RDirtEffectsBig"],["GdtGrassWild","RDustEffects"],["GdtGrassWild","RGrassEffectsBig"],["GdtGrassWild","RDirtEffectsBig"],["GdtWildField","RDustEffects"],["GdtWildField","RGrassEffectsBig"],["GdtWildField","RDirtEffectsBig"],["GdtWeed1","RDustEffects"],["GdtWeed1","RGrassEffectsBig"],["GdtWeed1","RDirtEffectsBig"],["GdtWeed2","RDustEffects"],["GdtWeed2","RGrassEffectsBig"],["GdtWeed2","RDirtEffectsBig"],["GdtThorn","RDustEffects"],["GdtThorn","RGrassEffectsBig"],["GdtThorn","RDirtEffectsBig"],["GdtStony","RDustEffects"],["GdtStony","RGrassEffectsBig"],["GdtStony","RDirtEffectsBig"],["GdtStonyGreen","RDustEffects"],["GdtStonyGreen","RGrassEffectsBig"],["GdtStonyGreen","RDirtEffectsBig"],["GdtStonyThistle","RDustEffects"],["GdtStonyThistle","RGrassEffectsBig"],["GdtStonyThistle","RDirtEffectsBig"],["GdtSeabedDeep","RDustEffects"],["GdtSeabed","RDustEffects"],["SurfRoadDirt","RDustEffects"],["SurfRoadConcrete","RDustEffects"],["SurfRoadTarmac","RDustEffects"],["SurfWood","RDustEffects"],["SurfMetal","RDustEffects"],["SurfRoofTin","RDustEffects"],["SurfRoofTiles","RDustEffects"],["SurfIntWood","RDustEffects"],["SurfIntConcrete","RDustEffects"],["SurfIntTiles","RDustEffects"],["SurfIntMetal","RDustEffects"],["dirtrunway","RDustEffects"]],
    "leftDustEffects": [["GdtKLDirt","LDustEffects"],["GdtKLGrass1","LDustEffects"],["GdtKLGrass1","LGrassEffects"],["GdtKLGrass2","LDustEffects"],["GdtKLGrass2","LGrassEffects"],["GdtKLForestCon","LDustEffects"],["GdtKLForestDec","LDustEffects"],["GdtKlMud","LDustEffects"],["GdtKlSoil","LDustEffects"],["GdtKlTarmac","LDustEffects"],["GdtKlStubble","LDustEffects"],["GdtKlStones","LStonesEffects"],["SurfRoadDirt_Enoch","LDustEffects"],["SurfTrailDirt_Enoch","LDustEffects"],["SurfRoadTarmac1_Enoch","LDustEffects"],["SurfRoadTarmac2_Enoch","LDustEffects"],["SurfRoadTarmac3_Enoch","LDustEffects"],["GdtGrassShort","LDustEffects"],["GdtGrassShort","LGrassEffectsBig"],["GdtGrassTall","LDustEffects"],["GdtGrassTall","LGrassEffectsBig"],["GdtRedDirt","LDustEffectsRed"],["GdtField","LDustEffects"],["GdtForest","LDustEffects"],["GdtVolcano","LDustEffects"],["GdtVolcano","LStonesEffectsBig"],["GdtCliff","LDustEffects"],["GdtVolcanoBeach","LDustEffects"],["SurfRoadDirt_exp","LDustEffectsRed"],["SurfRoadConcrete_exp","LDustEffects"],["SurfRoadTarmac_exp","LDustEffects"],["GdtStratisConcrete","LDustEffects"],["GdtStratisConcrete","LDirtEffectsBig"],["GdtStratisBeach","LDustEffects"],["GdtStratisBeach","LStonesEffectsBig"],["GdtStratisDirt","LDustEffects"],["GdtStratisDirt","LDirtEffectsBig"],["GdtStratisSeabedCluttered","LDustEffects"],["GdtStratisSeabed","LDustEffects"],["GdtStratisDryGrass","LDustEffects"],["GdtStratisDryGrass","LGrassEffectsDryBig"],["GdtStratisDryGrass","LDirtEffectsBig"],["GdtStratisGreenGrass","LDustEffects"],["GdtStratisGreenGrass","LGrassEffectsBig"],["GdtStratisGreenGrass","LDirtEffectsBig"],["GdtStratisRocky","LDustEffects"],["GdtStratisRocky","LGrassEffectsBig"],["GdtStratisRocky","LDirtEffectsBig"],["GdtStratisThistles","LDustEffects"],["GdtStratisThistles","LGrassEffectsBig"],["GdtStratisThistles","LDirtEffectsBig"],["GdtConcrete","LDustEffects"],["GdtConcrete","LDirtEffectsBig"],["GdtAsphalt","LDustEffects"],["GdtAsphalt","LDirtEffectsBig"],["GdtRubble","LDustEffects"],["GdtRubble","LGrassEffectsBig"],["GdtRubble","LDirtEffectsBig"],["GdtSoil","LDustEffects"],["GdtSoil","LDirtEffectsBig"],["GdtBeach","LDustEffects"],["GdtBeach","LStonesEffectsBig"],["GdtRock","LDustEffects"],["GdtRock","LDirtEffectsBig"],["GdtDead","LDustEffects"],["GdtDead","LDirtEffectsBig"],["Default","LDustEffects"],["GdtDesert","LDustEffects"],["GdtDesert","LDirtEffectsBig"],["GdtDesert","LStonesEffects"],["GdtDesert1","LDustEffects"],["GdtDesert1","LDirtEffectsBig"],["GdtDesert1","LStonesEffectsBig"],["GdtDesert2","LDustEffects"],["GdtDesert2","LGrassEffectsBig"],["GdtDesert2","LDirtEffectsBig"],["GdtDirt","LDustEffects"],["GdtDirt","LDirtEffectsBig"],["GdtGrassGreen","LDustEffects"],["GdtGrassGreen","LGrassEffectsBig"],["GdtGrassGreen","LDirtEffectsBig"],["GdtGrassDry","LDustEffects"],["GdtGrassDry","LGrassEffectsDryBig"],["GdtGrassDry","LDirtEffectsBig"],["GdtGrassWild","LDustEffects"],["GdtGrassWild","LGrassEffectsBig"],["GdtGrassWild","LDirtEffectsBig"],["GdtWildField","LDustEffects"],["GdtWildField","LGrassEffectsBig"],["GdtWildField","LDirtEffectsBig"],["GdtWeed1","LDustEffects"],["GdtWeed1","LGrassEffectsBig"],["GdtWeed1","LDirtEffectsBig"],["GdtWeed2","LDustEffects"],["GdtWeed2","LGrassEffectsBig"],["GdtWeed2","LDirtEffectsBig"],["GdtThorn","LDustEffects"],["GdtThorn","LGrassEffectsBig"],["GdtThorn","LDirtEffectsBig"],["GdtStony","LDustEffects"],["GdtStony","LGrassEffectsBig"],["GdtStony","LDirtEffectsBig"],["GdtStonyGreen","LDustEffects"],["GdtStonyGreen","LGrassEffectsBig"],["GdtStonyGreen","LDirtEffectsBig"],["GdtStonyThistle","LDustEffects"],["GdtStonyThistle","LGrassEffectsBig"],["GdtStonyThistle","LDirtEffectsBig"],["GdtSeabedDeep","LDustEffects"],["GdtSeabed","LDustEffects"],["SurfRoadDirt","LDustEffects"],["SurfRoadConcrete","LDustEffects"],["SurfRoadTarmac","LDustEffects"],["SurfWood","LDustEffects"],["SurfMetal","LDustEffects"],["SurfRoofTin","LDustEffects"],["SurfRoofTiles","LDustEffects"],["SurfIntWood","LDustEffects"],["SurfIntConcrete","LDustEffects"],["SurfIntTiles","LDustEffects"],["SurfIntMetal","LDustEffects"],["dirtrunway","RDustEffects"]],
    # Class: CfgVehicles\Tank\DestructionEffects,
    "DestructionEffects": {
        # Class: CfgVehicles\Tank\DestructionEffects\LightBig1
        "LightBig1": {
            "simulation": "light",
            "type": "ObjectDestructionLight",
            "position": "destructionEffect1",
            "intensity": 0.001,
            "interval": 1,
            "lifeTime": 3,
            "enabled": "distToWater"
        },
        # Class: CfgVehicles\Tank\DestructionEffects\Sound,
        "Sound": {
            "simulation": "sound",
            "position": "destructionEffect1",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 1,
            "type": "Fire"
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireBig1,
        "FireBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionFire1",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\Refract1,
        "Refract1": {
            "simulation": "particles",
            "type": "ObjectDestructionRefract",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig1,
        "SmokeBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke",
            "position": "destructionEffect1",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SparksBig1,
        "SparksBig1": {
            "simulation": "particles",
            "type": "ObjectDestructionSparks",
            "position": "destructionEffect1",
            "intensity": 0,
            "interval": 1,
            "lifeTime": 0
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireSparksBig1,
        "FireSparksBig1": {
            "simulation": "particles",
            "type": "FireSparks",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 2.8
        },
        # Class: CfgVehicles\Tank\DestructionEffects\FireBig2,
        "FireBig2": {
            "simulation": "particles",
            "type": "ObjectDestructionFire2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig1_2,
        "SmokeBig1_2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke1_2",
            "position": "destructionEffect2",
            "intensity": 0.15,
            "interval": 1,
            "lifeTime": 3.5
        },
        # Class: CfgVehicles\Tank\DestructionEffects\SmokeBig2,
        "SmokeBig2": {
            "simulation": "particles",
            "type": "ObjectDestructionSmoke2",
            "position": "destructionEffect2",
            "intensity": 1,
            "interval": 1,
            "lifeTime": 3.2
        }
    },
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
    # Class: CfgVehicles\LandVehicle\CommanderOptics,
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
        # Class: CfgVehicles\LandVehicle\CommanderOptics\ViewOptics,
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
        # Class: CfgVehicles\LandVehicle\CommanderOptics\ViewGunner,
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
        # Class: CfgVehicles\AllVehicles\NewTurret\TurretSpec,
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
        "showCrewAim": 0
    },
    "wheelDamageThreshold": 0.2,
    "wheelDestroyThreshold": 0.99,
    "wheelDamageRadiusCoef": 0.9,
    "wheelDestroyRadiusCoef": 0.4,
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
    "memoryPointTaskMarker": "",
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
    "driverLeftLegAnimName": "",
    "driverRightLegAnimName": "",
    "cargoDoors": [],
    "hasTerminal": 0,
    "getInOutOnProxy": 0,
    "preciseGetInOut": 0,
    "cargoPreciseGetInOut": [0],
    "availableForSupportTypes": [],
    "impactEffectsSea": "ImpactEffectsSea",
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
    "insideSoundCoef": 0.5,
    "obstructSoundLFRatio": 0,
    "occludeSoundLFRatio": 0.25,
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
    "irTarget": 1,
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
    "radarType": 0,
    "limitedSpeedCoef": 0.22,
    "hasDriver": 1,
    "hideWeaponsDriver": 1,
    "hideWeaponsCargo": 0,
    "enableWatch": 0,
    "usePreciseGetInAction": 0,
    "allowTabLock": 1,
    "showAllTargets": 0,
    "dustFrontLeftPos": "dustFrontLeft",
    "dustFrontRightPos": "dustFrontRight",
    "dustBackLeftPos": "dustBackLeft",
    "dustBackRightPos": "dustBackRight",
    "showNVGDriver": 0,
    "showNVGCommander": 0,
    "showNVGGunner": 0,
    "showNVGCargo": [0],
    "soundAttenuationCargo": [1],
    "countsForScoreboard": 1,
    # Class: CfgVehicles\All\MarkerLights,
    "MarkerLights": {
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
    "soundCrashes": ["soundCrash",1],
    "soundLandCrashes": ["soundLandCrash",1],
    "soundWaterCrashes": ["soundWaterCrash",1],
    "emptySound": ["",0,1],
    "soundBushCrash": ["emptySound",0],
    "soundLocked": ["",1,1],
    "cargoIsCoDriver": [0],
    "driverCompartments": "Compartment1",
    "cargoCompartments": ["Compartment1"],
    "driverOpticsEffect": [],
    "forceHideDriver": 0,
    "canHideDriver": -1,
    "castDriverShadow": 0,
    "castCargoShadow": 0,
    "viewDriverShadow": 1,
    "viewDriverShadowDiff": 1,
    "viewDriverShadowAmb": 1,
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
    "cargoCanEject": 1,
    "driverCanEject": 1,
    "fireResistance": 10,
    "airCapacity": 10,
    "damageTexDelay": 0,
    "coefInside": 2,
    "coefInsideHeur": 2,
    "coefSpeedInside": 2,
    "windSockExist": 0,
    "slingLoadCargoMemoryPoints": [],
    "slingLoadCargoMemoryPointsDir": [],
    "damageHalf": [],
    "damageFull": [],
    # Class: CfgVehicles\All\camShakeGForce,
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
    # Class: CfgVehicles\All\camShakeDamage,
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
    "features": "",
    "insideDetectCoef": 0.05,
}